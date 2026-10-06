#!/usr/bin/env python3
"""Validate the role data and generate docs/ and exports/.

Usage:
    python3 scripts/build.py            # validate, then generate
    python3 scripts/build.py --check    # validate only

Inputs (all under data/):
    catalogue.yaml          role families and roles, with PCF and ESCO links
    bands.yaml              bands, competency outlines, grade-to-band rule
    job-evaluation.yaml     16 factors, levels, points, band points ranges
    skills/*.yaml           skills original to this reference
    roles/*.yaml            one file per role
    sources/pcf/            UK GDaD PCF downloads (see scripts/fetch_pcf.py)
    sources/esco/           ESCO downloads (see scripts/fetch_esco.py)
    crosswalks/pcf-esco.tsv UK GDaD PCF skills matched to ESCO skills
"""
import collections
import csv
import datetime
import json
import os
import re
import shutil
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
DOCS = os.path.join(ROOT, "docs")
EXPORTS = os.path.join(ROOT, "exports")

LEVELS = ["awareness", "working", "practitioner", "expert"]
LEVEL_NUMBER = {name: i + 1 for i, name in enumerate(LEVELS)}

PCF_URL = "https://understand-digital-data-roles-skills.service.gov.uk/"
ESCO_URL = "https://esco.ec.europa.eu/"
DISCLAIMER = (
    "This is an illustrative reference profile for a generic digital health care "
    "organisation. It is not an official job description for any employer, and its "
    "job evaluation scores are not a formal evaluation."
)
PCF_CREDIT = (
    "Contains public sector information from the UK Government Digital and Data "
    f"Profession Capability Framework ({PCF_URL}), licensed under the Open Government "
    "Licence v3.0. © Crown copyright."
)
ESCO_CREDIT = (
    f"Contains ESCO v1.2.1 data ({ESCO_URL}). © European Union. Reuse authorised "
    "under Commission Decision 2011/833/EU."
)


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def load_yaml(*parts):
    with open(os.path.join(DATA, *parts), encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_tsv(*parts):
    with open(os.path.join(DATA, *parts), encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def load_csv(*parts):
    with open(os.path.join(DATA, *parts), encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


# ---------------------------------------------------------------- loading

class Data:
    def __init__(self):
        self.catalogue = load_yaml("catalogue.yaml")
        self.bands = load_yaml("bands.yaml")
        self.jes = load_yaml("job-evaluation.yaml")
        self.own_skills = {}
        self.skill_files = {}
        for name in sorted(os.listdir(os.path.join(DATA, "skills"))):
            if name.endswith(".yaml"):
                for s in load_yaml("skills", name)["skills"]:
                    if s["id"] in self.own_skills:
                        raise SystemExit(f"error: skill '{s['id']}' is defined in both {self.skill_files[s['id']]} and {name}")
                    s.setdefault("source", "reference")
                    self.own_skills[s["id"]] = s
                    self.skill_files[s["id"]] = name

        self.band_ids = [b["id"] for b in self.bands["bands"]]
        self.band_by_id = {b["id"]: b for b in self.bands["bands"]}
        self.band_points = {b["band"]: (b["min"], b["max"]) for b in self.jes["bands"]}
        self.factors = self.jes["factors"]
        self.factor_by_id = {f["id"]: f for f in self.factors}

        # UK GDaD PCF
        self.pcf_skills = {}
        for row in load_csv("sources", "pcf", "skills.csv"):
            sid = "pcf:" + slug(row["Skill Name"])
            levels = {lv: row[lv.capitalize()] for lv in LEVELS}
            description = row["Skill Description"]
            if not any(v.strip() for v in levels.values()):
                # Senior leadership skills are defined by one statement, not by level.
                statement = "*Senior leadership skill: the UK GDaD PCF defines it with one statement, not by level.*\n" + description
                levels = {lv: statement for lv in LEVELS}
                description = "A senior leadership skill. " + description
            self.pcf_skills[sid] = {
                "id": sid,
                "name": row["Skill Name"],
                "description": description,
                "source": "pcf",
                "levels": levels,
            }
        self.pcf_levels = collections.OrderedDict()  # (role, level) -> info
        self.pcf_roles = {}
        for row in load_csv("sources", "pcf", "roles.csv"):
            self.pcf_roles.setdefault(row["Role"], {"family": row["Role Family"], "description": row["Role Description"]})
            key = (row["Role"], row["Role Level"])
            info = self.pcf_levels.setdefault(key, {"description": row["Role Level Description"], "skills": []})
            if row["Skill Name"]:
                info["skills"].append(("pcf:" + slug(row["Skill Name"]), row["Skill Level"].lower()))
        self.pcf_grades = {}
        for row in load_tsv("sources", "pcf", "grades.tsv"):
            self.pcf_grades[(row["role"], row["role_level"])] = row["civil_service_grades"]
            self.pcf_roles.get(row["role"], {}).setdefault("slug", row["slug"])

        # ESCO
        self.esco = {r["id"]: r for r in load_tsv("sources", "esco", "occupations.tsv")}
        self.esco_skills = collections.defaultdict(list)
        for r in load_tsv("sources", "esco", "occupation-skills.tsv"):
            self.esco_skills[r["occupation_id"]].append(r)

        # UK GDaD PCF to ESCO crosswalk, if present
        crosswalk = os.path.join(DATA, "crosswalks", "pcf-esco.tsv")
        if os.path.exists(crosswalk):
            for r in load_tsv("crosswalks", "pcf-esco.tsv"):
                s = self.pcf_skills.get(r["pcf_skill_id"])
                if s is not None and r.get("esco_skill_uri"):
                    s.setdefault("esco", []).append({"uri": r["esco_skill_uri"], "label": r["esco_skill_label"], "match": r["match"]})

        self.skills = dict(self.pcf_skills)
        self.skills.update(self.own_skills)

        # Roles
        self.roles = {}
        self.role_meta = {}
        for family in self.catalogue["families"]:
            for role in family["roles"]:
                self.role_meta[role["id"]] = dict(role, family=family["id"], family_title=family["title"])
        roles_dir = os.path.join(DATA, "roles")
        for name in sorted(os.listdir(roles_dir)):
            if name.endswith(".yaml"):
                role = load_yaml("roles", name)
                role["_file"] = name
                self.roles[role["id"]] = role

    def level_skills(self, role, level):
        """All skills for a role level: PCF skills for its PCF level, then extra skills."""
        out = collections.OrderedDict()
        meta = self.role_meta[role["id"]]
        if meta.get("pcf_role") and level.get("pcf_level"):
            for sid, lv in self.pcf_levels.get((meta["pcf_role"], level["pcf_level"]), {}).get("skills", []):
                out[sid] = {"skill": sid, "level": lv, "source": "pcf"}
        for s in level.get("skills", []) or []:
            out[s["skill"]] = {"skill": s["skill"], "level": s["level"], "source": self.skills.get(s["skill"], {}).get("source", "")}
        return list(out.values())

    def jes_total(self, level):
        total = 0
        for f in self.factors:
            lv = str(level.get("job_evaluation", {}).get(f["id"], ""))
            total += self.factor_by_id[f["id"]]["points"].get(lv, 0) if lv else 0
        return total

    def band_for_points(self, points):
        for band, (lo, hi) in self.band_points.items():
            if lo <= points <= hi:
                return band
        return None


# ---------------------------------------------------------------- validation

def validate(d):
    errors, warnings = [], []
    for sid, s in d.own_skills.items():
        for lv in LEVELS:
            if not s.get("levels", {}).get(lv):
                errors.append(f"skills/{d.skill_files[sid]}: {sid} has no '{lv}' level definition")
        if sid.startswith("pcf:"):
            errors.append(f"skills/{d.skill_files[sid]}: {sid} must not use the 'pcf:' prefix")

    for rid in d.role_meta:
        if rid not in d.roles:
            warnings.append(f"catalogue role '{rid}' has no file data/roles/{rid}.yaml")

    for f in d.factors:
        for lv, pts in f["points"].items():
            if not isinstance(pts, int):
                errors.append(f"job-evaluation.yaml: factor {f['id']} level {lv} points must be an integer")

    for rid, role in d.roles.items():
        where = f"roles/{role['_file']}"
        if role["_file"] != f"{rid}.yaml":
            errors.append(f"{where}: id '{rid}' does not match file name")
        meta = d.role_meta.get(rid)
        if not meta:
            errors.append(f"{where}: role '{rid}' is not in catalogue.yaml")
            continue
        for u in meta["esco"]:
            if u not in d.esco:
                errors.append(f"{where}: ESCO occupation {u} is not in data/sources/esco (run scripts/fetch_esco.py)")
        if meta.get("pcf_role") and meta["pcf_role"] not in d.pcf_roles:
            errors.append(f"catalogue.yaml: {rid}: PCF role '{meta['pcf_role']}' not found")
        for key in ("summary", "levels"):
            if not role.get(key):
                errors.append(f"{where}: missing '{key}'")
        previous = -1
        for level in role.get("levels", []):
            lw = f"{where}: level '{level.get('title')}'"
            band = str(level.get("band"))
            if band not in d.band_ids:
                errors.append(f"{lw}: unknown band '{band}'")
                continue
            if d.band_ids.index(band) < previous:
                warnings.append(f"{lw}: bands are not in ascending order")
            previous = d.band_ids.index(band)
            if level.get("pcf_level"):
                if not meta.get("pcf_role"):
                    errors.append(f"{lw}: has pcf_level but the role has no pcf_role")
                elif (meta["pcf_role"], level["pcf_level"]) not in d.pcf_levels:
                    errors.append(f"{lw}: PCF level '{level['pcf_level']}' not found for '{meta['pcf_role']}'")
            if not level.get("responsibilities"):
                errors.append(f"{lw}: no responsibilities")
            if not level.get("pcf_level") and not level.get("summary"):
                errors.append(f"{lw}: no summary (required when there is no pcf_level)")
            skills = d.level_skills(role, level)
            if not skills:
                errors.append(f"{lw}: no skills")
            for s in skills:
                if s["skill"] not in d.skills:
                    errors.append(f"{lw}: unknown skill '{s['skill']}'")
                if s["level"] not in LEVELS:
                    errors.append(f"{lw}: skill '{s['skill']}' has invalid level '{s['level']}'")
            jes = level.get("job_evaluation") or {}
            for f in d.factors:
                lv = str(jes.get(f["id"], ""))
                if not lv:
                    errors.append(f"{lw}: job_evaluation is missing factor '{f['id']}'")
                elif lv not in f["points"]:
                    errors.append(f"{lw}: job_evaluation factor '{f['id']}' has invalid level '{lv}'")
            for k in jes:
                if k not in d.factor_by_id:
                    errors.append(f"{lw}: job_evaluation has unknown factor '{k}'")
            if len(jes) == len(d.factors):
                total = d.jes_total(level)
                lo, hi = d.band_points[band]
                if not lo <= total <= hi:
                    errors.append(f"{lw}: job evaluation total {total} is outside Band {band} ({lo}-{hi}); it falls in Band {d.band_for_points(total)}")
    return errors, warnings


# ---------------------------------------------------------------- generation

def md_escape(text):
    """Fit multi-line text into a Markdown table cell."""
    text = text.strip().replace("|", "\\|")
    return re.sub(r"\n-\s*", "<br>• ", text).replace("\n", " ")


def bullets(text):
    """Turn PCF text with '- ' lines into Markdown, keeping its paragraphs."""
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


def level_anchor(level):
    return slug(f"band-{level['band']}-{level['title']}")


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text.rstrip() + "\n")


def write_doc(directory, text):
    """Write a Markdown document as <directory>/index.md, with README.md as a symlink to it."""
    write(os.path.join(directory, "index.md"), text)
    readme = os.path.join(directory, "README.md")
    if os.path.islink(readme) or os.path.exists(readme):
        os.remove(readme)
    os.symlink("index.md", readme)


def write_tsv(path, header, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
        w.writerow(header)
        for r in rows:
            w.writerow([str(v).replace("\t", " ").replace("\r", "").replace("\n", " ") for v in r])


def esco_link(occ):
    return f"[{occ['label']}]({occ['uri']})"


def role_page(d, role):
    meta = d.role_meta[role["id"]]
    pcf = meta.get("pcf_role")
    out = [f"# {meta['title']}", "", f"> {DISCLAIMER}", ""]
    out += [f"**Family:** [{meta['family_title']}](../../#{meta['family']})  ",
            f"**Bands:** {', '.join(str(l['band']) for l in role['levels'])}  "]
    if pcf:
        pslug = d.pcf_roles[pcf].get("slug", slug(pcf))
        out.append(f"**UK GDaD PCF role:** [{pcf}]({PCF_URL}role/{pslug}/)  ")
    else:
        out.append("**UK GDaD PCF role:** none (this reference defines the role)  ")
    occs = [d.esco[u] for u in meta["esco"] if u in d.esco]
    out.append("**ESCO occupations:** " + "; ".join(f"{esco_link(o)} (ISCO-08 {o['isco_08']})" for o in occs))
    out += ["", "## Summary", "", role["summary"].strip(), ""]
    if role.get("health_context"):
        out += ["## In a digital health care organisation", ""]
        out += [f"- {x}" for x in role["health_context"]] + [""]
    if pcf:
        out += ["## UK GDaD PCF role description", "", "> " + bullets(d.pcf_roles[pcf]["description"]).replace("\n", "\n> "), "",
                f"*Quoted from the UK GDaD PCF. {PCF_CREDIT}*", ""]

    out += ["## Role levels", "", "| Band | Title | UK GDaD PCF level | Civil Service grades (PCF) | Job evaluation points |", "| --- | --- | --- | --- | --- |"]
    for level in role["levels"]:
        grades = d.pcf_grades.get((pcf, level.get("pcf_level")), "") if pcf else ""
        out.append(f"| {level['band']} | [{level['title']}](#{level_anchor(level)}) | {level.get('pcf_level') or '—'} | {grades or '—'} | {d.jes_total(level)} |")
    out.append("")

    for level in role["levels"]:
        out += [f"## Band {level['band']}: {level['title']}", ""]
        band = d.band_by_id[str(level["band"])]
        if level.get("summary"):
            out += [level["summary"].strip(), ""]
        if level.get("pcf_level"):
            desc = d.pcf_levels[(pcf, level["pcf_level"])]["description"]
            out += [f"**UK GDaD PCF level: {level['pcf_level']}**", "", "> " + bullets(desc).replace("\n", "\n> "), ""]
        out += ["### Responsibilities", ""] + [f"- {r}" for r in level["responsibilities"]] + [""]
        out += ["### Skills", "", "| Skill | Source | Expected level | What this level means |", "| --- | --- | --- | --- |"]
        for s in d.level_skills(role, level):
            sk = d.skills[s["skill"]]
            src = "UK GDaD PCF" if sk["source"] == "pcf" else "This reference"
            meaning = md_escape(sk["levels"][s["level"]])
            out.append(f"| [{sk['name']}](../../skills/#{slug(sk['id'])}) | {src} | {s['level'].capitalize()} | {meaning} |")
        out.append("")
        if level.get("qualifications"):
            out += ["### Typical qualifications and experience", ""] + [f"- {q}" for q in level["qualifications"]] + [""]
        out += ["### Band outline", "",
                f"- **Knowledge:** {band['knowledge']}", f"- **Autonomy:** {band['autonomy']}",
                f"- **Scope:** {band['scope']}", f"- **Leadership:** {band['leadership']}",
                f"- **Accountability:** {band['accountability']}", ""]
        out += ["### Job evaluation (illustrative)", "", "| # | Factor | Level | Points |", "| --- | --- | --- | --- |"]
        for i, f in enumerate(d.factors, 1):
            lv = str(level["job_evaluation"].get(f["id"], ""))
            out.append(f"| {i} | {f['name']} | {lv} | {f['points'].get(lv, '')} |")
        lo, hi = d.band_points[str(level["band"])]
        out += [f"| | **Total** | | **{d.jes_total(level)}** (Band {level['band']}: {lo}–{hi}) |", ""]
        if level.get("job_evaluation_notes"):
            out += [level["job_evaluation_notes"].strip(), ""]

    out += ["## ESCO occupations and skills", ""]
    for o in occs:
        out += [f"### {o['label']}", "", f"- **URI:** <{o['uri']}>", f"- **ESCO code:** {o['code']}  ·  **ISCO-08:** {o['isco_08']} {o['isco_08_label']}"]
        if o["alternative_labels"]:
            out.append(f"- **Alternative labels:** {o['alternative_labels']}")
        out += ["", f"> {o['description']}", ""]
        for relation in ("essential", "optional"):
            rows = [r for r in d.esco_skills[o["id"]] if r["relation"] == relation]
            if not rows:
                continue
            out += [f"<details><summary>{relation.capitalize()} skills and knowledge ({len(rows)})</summary>", ""]
            for kind, label in (("skill", "Skills and competences"), ("knowledge", "Knowledge")):
                sub = sorted((r for r in rows if r["skill_type"] == kind), key=lambda r: r["skill_label"])
                if sub:
                    out += [f"**{label}:** " + ", ".join(f"[{r['skill_label']}]({r['skill_uri']})" for r in sub), ""]
            other = [r for r in rows if r["skill_type"] not in ("skill", "knowledge")]
            if other:
                out += ["**Other:** " + ", ".join(f"[{r['skill_label']}]({r['skill_uri']})" for r in other), ""]
            out += ["</details>", ""]
    if role.get("sources"):
        out += ["## Sources", ""] + [f"- {s}" for s in role["sources"]] + [""]
    out += ["---", "", f"*{PCF_CREDIT}*  ", f"*{ESCO_CREDIT}*"]
    return "\n".join(out)


def generate(d):
    for path in [os.path.join(EXPORTS, "self-assessment")] + [os.path.join(DOCS, name) for name in ("roles", "bands", "pcf", "esco", "skills")]:
        shutil.rmtree(path, ignore_errors=True)

    footer = ["", "---", "", f"*{DISCLAIMER}*  ", f"*{PCF_CREDIT}*  ", f"*{ESCO_CREDIT}*"]
    all_levels = []  # (role, meta, level)
    for rid, role in d.roles.items():
        write_doc(os.path.join(DOCS, "roles", rid), role_page(d, role))
        for level in role["levels"]:
            all_levels.append((role, d.role_meta[rid], level))

    # Index by family
    out = ["# Role index", "", f"> {DISCLAIMER}", "", "Find the family closest to your work, then the role, then the band.", ""]
    for family in d.catalogue["families"]:
        out += [f"## {family['title']}", f'<a id="{family["id"]}"></a>', "", "| Role | Bands | UK GDaD PCF role | ESCO occupation |", "| --- | --- | --- | --- |"]
        for r in family["roles"]:
            role = d.roles.get(r["id"])
            bands = ", ".join(str(l["band"]) for l in role["levels"]) if role else "(not written yet)"
            name = f"[{r['title']}](roles/{r['id']}/)" if role else r["title"]
            occ = d.esco.get(r["esco"][0])
            out.append(f"| {name} | {bands} | {r.get('pcf_role') or '—'} | {esco_link(occ) if occ else '—'} |")
        out.append("")
    write_doc(DOCS, "\n".join(out + footer))

    # Roles A to Z
    out = ["# Roles A to Z", "", f"> {DISCLAIMER}", "", "| Role | Family | Bands |", "| --- | --- | --- |"]
    for rid, role in sorted(d.roles.items(), key=lambda x: d.role_meta[x[0]]["title"].lower()):
        m = d.role_meta[rid]
        out.append(f"| [{m['title']}]({rid}/) | [{m['family_title']}](../#{m['family']}) | {', '.join(str(l['band']) for l in role['levels'])} |")
    write_doc(os.path.join(DOCS, "roles"), "\n".join(out + footer))

    # Index by band
    out = ["# Roles by band", "", f"> {DISCLAIMER}", ""]
    for b in d.bands["bands"]:
        rows = [(m, l) for r, m, l in all_levels if str(l["band"]) == b["id"]]
        lo, hi = d.band_points.get(b["id"], ("", ""))
        out += [f"## Band {b['id']}", "", f"*{b['stage']}. SFIA level {b['sfia_level']}. Job evaluation points {lo}–{hi}.*", "",
                f"- **Knowledge:** {b['knowledge']}", f"- **Autonomy:** {b['autonomy']}", f"- **Scope:** {b['scope']}",
                f"- **Leadership:** {b['leadership']}", f"- **Accountability:** {b['accountability']}", ""]
        if rows:
            out += ["| Role level | Family |", "| --- | --- |"]
            for m, l in sorted(rows, key=lambda x: (x[0]["family_title"], x[1]["title"])):
                out.append(f"| [{l['title']}](../roles/{m['id']}/#{level_anchor(l)}) | {m['family_title']} |")
            out.append("")
    write_doc(os.path.join(DOCS, "bands"), "\n".join(out + footer))

    # Index by PCF role
    out = ["# Roles by UK GDaD PCF role", "", f"> {DISCLAIMER}", "",
           "| PCF family | PCF role | PCF level | Civil Service grades | Role level in this reference | Band |", "| --- | --- | --- | --- | --- | --- |"]
    for r, m, l in sorted(all_levels, key=lambda x: (d.pcf_roles.get(x[1].get("pcf_role") or "", {}).get("family", "~"), x[1].get("pcf_role") or "~", d.band_ids.index(str(x[2]["band"])))):
        if m.get("pcf_role") and l.get("pcf_level"):
            out.append(f"| {d.pcf_roles[m['pcf_role']]['family']} | {m['pcf_role']} | {l['pcf_level']} | {d.pcf_grades.get((m['pcf_role'], l['pcf_level']), '') or '—'} | [{l['title']}](../roles/{m['id']}/#{level_anchor(l)}) | {l['band']} |")
    unused = sorted(set(d.pcf_roles) - {m.get("pcf_role") for m in d.role_meta.values()})
    out += ["", "PCF roles not used in this reference: " + (", ".join(unused) if unused else "none") + "."]
    write_doc(os.path.join(DOCS, "pcf"), "\n".join(out + footer))

    # Index by ESCO occupation
    out = ["# Roles by ESCO occupation", "", f"> {DISCLAIMER}", "",
           "| ESCO occupation | ISCO-08 | Roles in this reference |", "| --- | --- | --- |"]
    by_occ = collections.defaultdict(list)
    for rid, m in d.role_meta.items():
        for u in m["esco"]:
            by_occ[u].append(m)
    for u, ms in sorted(by_occ.items(), key=lambda x: d.esco.get(x[0], {}).get("label", "")):
        o = d.esco.get(u)
        if o:
            out.append(f"| {esco_link(o)} | {o['isco_08']} | " + ", ".join(f"[{m['title']}](../roles/{m['id']}/)" if m["id"] in d.roles else m["title"] for m in ms) + " |")
    write_doc(os.path.join(DOCS, "esco"), "\n".join(out + footer))

    # Skills catalogue
    used = collections.Counter()
    for r, m, l in all_levels:
        for s in d.level_skills(r, l):
            used[s["skill"]] += 1
    out = ["# Skills", "", f"> {DISCLAIMER}", "",
           "Each skill has four proficiency levels: Awareness (1), Working (2), Practitioner (3), and Expert (4). "
           "Skills marked *UK GDaD PCF* are quoted from that framework. Other skills are original to this reference, "
           "and list the closest ESCO skills where they exist.", ""]
    for sid, s in sorted(d.skills.items(), key=lambda x: x[1]["name"].lower()):
        if not used[sid] and s["source"] == "pcf":
            continue
        src = "UK GDaD PCF" if s["source"] == "pcf" else "This reference"
        out += [f'<a id="{slug(sid)}"></a>', "", f"## {s['name']}", "", f"*{src}. Used in {used[sid]} role levels.*", "", s["description"].strip(), ""]
        for lv in LEVELS:
            out += [f"**{lv.capitalize()}:**", "", bullets(s["levels"][lv]), ""]
        if s.get("esco"):
            out += ["**Closest ESCO skills:** " + ", ".join(f"[{e['label']}]({e['uri']}) ({e['match']})" for e in s["esco"]), ""]
    write_doc(os.path.join(DOCS, "skills"), "\n".join(out + footer))

    # Exports
    sa_header = ["role", "role_level", "band", "skill", "skill_source", "pcf_reference", "esco_reference",
                 "expected_level", "expected_level_number", "expected_level_description",
                 "self_rating", "manager_rating", "gap", "evidence", "development_action"]
    roles_rows, jes_rows, skill_rows = [], [], []
    for r, m, l in all_levels:
        rows = []
        for s in d.level_skills(r, l):
            sk = d.skills[s["skill"]]
            pcf_ref = f"{PCF_URL}skills/" if sk["source"] == "pcf" else ""
            esco_ref = "; ".join(e["uri"] for e in sk.get("esco", []))
            rows.append([m["title"], l["title"], l["band"], sk["name"], "UK GDaD PCF" if sk["source"] == "pcf" else "this reference",
                         pcf_ref, esco_ref, s["level"], LEVEL_NUMBER[s["level"]], sk["levels"][s["level"]], "", "", "", "", ""])
            skill_rows.append([m["id"], m["title"], l["title"], l["band"], sk["id"], sk["name"], s["level"], LEVEL_NUMBER[s["level"]]])
        name = f"{m['id']}--band-{l['band']}--{slug(l['title'])}.tsv"
        write_tsv(os.path.join(EXPORTS, "self-assessment", name), sa_header, rows)
        roles_rows.append([m["family_title"], m["id"], m["title"], l["title"], l["band"], m.get("pcf_role") or "", l.get("pcf_level") or "",
                           d.pcf_grades.get((m.get("pcf_role"), l.get("pcf_level")), ""), "; ".join(d.esco[u]["label"] for u in m["esco"] if u in d.esco),
                           "; ".join(d.esco[u]["uri"] for u in m["esco"] if u in d.esco), d.jes_total(l), f"docs/roles/{m['id']}/"])
        jes_rows.append([m["id"], l["title"], l["band"]] + [l["job_evaluation"].get(f["id"], "") for f in d.factors] + [d.jes_total(l)])
    write_tsv(os.path.join(EXPORTS, "roles.tsv"),
              ["family", "role_id", "role", "role_level", "band", "pcf_role", "pcf_level", "civil_service_grades", "esco_occupations", "esco_uris", "job_evaluation_points", "page"], roles_rows)
    write_tsv(os.path.join(EXPORTS, "job-evaluation.tsv"), ["role_id", "role_level", "band"] + [f["id"] for f in d.factors] + ["total_points"], jes_rows)
    write_tsv(os.path.join(EXPORTS, "role-skills.tsv"), ["role_id", "role", "role_level", "band", "skill_id", "skill", "expected_level", "expected_level_number"], skill_rows)
    write_reference_json(d, used)
    return len(d.roles), len(all_levels)


def write_reference_json(d, used):
    """Write exports/reference.json: the whole reference, fully resolved, for the website."""
    def read_accessed(name):
        path = os.path.join(DATA, "sources", name, "ACCESSED.txt")
        return open(path, encoding="utf-8").read().strip().splitlines()[-1].replace("accessed ", "") if os.path.exists(path) else ""

    skills = []
    for sid, s in sorted(d.skills.items(), key=lambda x: x[1]["name"].lower()):
        if not used[sid] and s["source"] == "pcf":
            continue
        skills.append({"id": sid, "slug": slug(sid), "name": s["name"], "description": s["description"].strip(),
                       "source": s["source"], "file": d.skill_files.get(sid, ""),
                       "levels": {lv: s["levels"][lv].strip() for lv in LEVELS}, "esco": s.get("esco", [])})

    occupation_ids = sorted({u for m in d.role_meta.values() for u in m["esco"] if u in d.esco})
    occupations = []
    for u in occupation_ids:
        o = d.esco[u]
        rel = {"essential": [], "optional": []}
        for r in sorted(d.esco_skills[u], key=lambda r: r["skill_label"]):
            rel[r["relation"]].append({"uri": r["skill_uri"], "label": r["skill_label"], "type": r["skill_type"]})
        occupations.append({"id": u, "uri": o["uri"], "label": o["label"], "code": o["code"], "isco08": o["isco_08"],
                            "isco08Label": o["isco_08_label"], "description": o["description"],
                            "alternativeLabels": [x for x in o["alternative_labels"].split("; ") if x], **rel})

    roles = []
    for family in d.catalogue["families"]:
        for r in family["roles"]:
            role = d.roles.get(r["id"])
            if not role:
                continue
            meta = d.role_meta[r["id"]]
            pcf = meta.get("pcf_role")
            levels = []
            for level in role["levels"]:
                pcf_level = level.get("pcf_level")
                levels.append({
                    "slug": slug(level["title"]),
                    "title": level["title"],
                    "band": str(level["band"]),
                    "summary": (level.get("summary") or "").strip(),
                    "pcfLevel": pcf_level,
                    "pcfLevelDescription": d.pcf_levels[(pcf, pcf_level)]["description"].strip() if pcf and pcf_level else None,
                    "civilServiceGrades": d.pcf_grades.get((pcf, pcf_level), "") if pcf else "",
                    "responsibilities": level["responsibilities"],
                    "qualifications": level.get("qualifications", []),
                    "skills": [{"id": s["skill"], "slug": slug(s["skill"]), "level": s["level"], "levelNumber": LEVEL_NUMBER[s["level"]]}
                               for s in d.level_skills(role, level)],
                    "jobEvaluation": {f["id"]: str(level["job_evaluation"][f["id"]]) for f in d.factors},
                    "jobEvaluationPoints": d.jes_total(level),
                    "jobEvaluationNotes": (level.get("job_evaluation_notes") or "").strip(),
                    "selfAssessmentFile": f"{meta['id']}--band-{level['band']}--{slug(level['title'])}.tsv",
                })
            roles.append({
                "id": meta["id"], "slug": meta["id"], "title": meta["title"], "family": family["id"],
                "summary": role["summary"].strip(), "healthContext": role.get("health_context", []),
                "pcfRole": {"name": pcf, "url": f"{PCF_URL}role/{d.pcf_roles[pcf].get('slug', slug(pcf))}/",
                            "description": d.pcf_roles[pcf]["description"].strip(), "family": d.pcf_roles[pcf]["family"]} if pcf else None,
                "esco": [u for u in meta["esco"] if u in d.esco],
                "levels": levels,
                "sources": role.get("sources", []),
            })

    bands = []
    for b in d.bands["bands"]:
        lo, hi = d.band_points[b["id"]]
        bands.append({**b, "civil_service_grades": b.get("civil_service_grades", []), "points": {"min": lo, "max": hi}})

    reference = {
        "meta": {
            "title": "Digital health care job roles reference",
            "disclaimer": DISCLAIMER,
            "pcf": {"name": "UK Government Digital and Data Profession Capability Framework", "url": PCF_URL,
                    "accessed": read_accessed("pcf"), "credit": PCF_CREDIT},
            "esco": {"name": "ESCO", "version": "v1.2.1", "url": ESCO_URL, "accessed": read_accessed("esco"), "credit": ESCO_CREDIT},
            "levels": [{"id": lv, "number": LEVEL_NUMBER[lv], "name": lv.capitalize()} for lv in LEVELS],
        },
        "families": [{"id": f["id"], "title": f["title"], "pcfFamily": f.get("pcf_family"),
                      "roles": [r["id"] for r in f["roles"] if r["id"] in d.roles]} for f in d.catalogue["families"]],
        "bands": bands,
        "factors": [{"id": f["id"], "name": f["name"], "description": f["description"], "levels": f["levels"], "points": f["points"]} for f in d.factors],
        "skills": skills,
        "occupations": occupations,
        "roles": roles,
    }
    with open(os.path.join(EXPORTS, "reference.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(reference, f, ensure_ascii=False, indent=1)
        f.write("\n")


def main():
    d = Data()
    errors, warnings = validate(d)
    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("error:", e)
    if errors:
        print(f"{len(errors)} errors")
        return 1
    if "--check" in sys.argv:
        print("ok")
        return 0
    roles, levels = generate(d)
    print(f"ok: {roles} roles, {levels} role levels generated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
