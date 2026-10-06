"""Locales: translations of this reference's original content.

English (en-001) is the source. Each other locale lives in data/locales/<code>/:

    locale.yaml          code, name, English name, direction, complete flag, document strings
    catalogue.yaml       families and roles: {id: {title, slug}}
    roles/<role-id>.yaml summary, health_context, and levels in English order:
                         [{title, slug, summary, responsibilities, qualifications, job_evaluation_notes}]
    skills/*.yaml        skills original to this reference, one file per domain as in data/skills/:
                         {id: {name, slug, description, levels}}
    bands.yaml           {band-id: {title, stage, knowledge, autonomy, scope, leadership, accountability}}
    job-evaluation.yaml  {factor-id: {name, description, levels: {level: text}}}

Quotations from the UK GDaD PCF and ESCO stay in their source language: they
are quotations, and ESCO has no translation for every locale.

Every role, level, skill, and family keeps its English id, which is stable
across locales, and has a per-locale slug: slugs are not shared between
locales. A missing translation falls back to English and is counted; a
locale marked `complete: true` must have none.

build.py calls localize() to write exports/locales/<code>/reference.json for
the website, and write_docs() to write the locale's documents to
locales/<code>/, each with the same .locale-peer-id as its English peer in docs/.
"""
import copy
import json
import os
import re
import shutil

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_LOCALES = os.path.join(ROOT, "data", "locales")
DOC_LOCALES = os.path.join(ROOT, "locales")
EXPORT_LOCALES = os.path.join(ROOT, "exports", "locales")

LEVELS = ["awareness", "working", "practitioner", "expert"]

# Strings used in generated documents. A locale's locale.yaml `strings`
# overrides any of these.
STRINGS = {
    "disclaimer": "This is an illustrative reference profile for a generic digital health care organisation. "
                  "It is not an official job description for any employer, and its job evaluation scores are not a formal evaluation.",
    "translation_note": "",
    "home_title": "Role index",
    "home_lede": "Find the family closest to your work, then the role, then the band.",
    "roles_title": "Roles A to Z",
    "bands_title": "Roles by band",
    "skills_title": "Skills",
    "skills_lede": "Each skill has four proficiency levels: Awareness (1), Working (2), Practitioner (3), and Expert (4). "
                   "Skills from the UK GDaD PCF are quoted from it in English. Other skills are original to this reference.",
    "pcf_title": "Roles by UK GDaD PCF role",
    "esco_title": "Roles by ESCO occupation",
    "role": "Role", "roles": "Roles", "family": "Family", "band": "Band", "bands": "Bands", "title": "Title",
    "role_level": "Role level", "skill": "Skill", "source": "Source", "expected_level": "Expected level",
    "level_meaning": "What this level means", "factor": "Factor", "level": "Level", "points": "Points", "total": "Total",
    "summary": "Summary", "health_context": "In a digital health care organisation",
    "pcf_role": "UK GDaD PCF role", "pcf_role_none": "none (this reference defines the role)",
    "pcf_role_description": "UK GDaD PCF role description (English original)",
    "pcf_level": "UK GDaD PCF level", "civil_service_grades": "Civil Service grades",
    "esco_occupations": "ESCO occupations", "role_levels": "Role levels", "job_evaluation_points": "Job evaluation points",
    "responsibilities": "Responsibilities", "skills": "Skills", "qualifications": "Typical qualifications and experience",
    "band_outline": "Band outline", "knowledge": "Knowledge", "autonomy": "Autonomy", "scope": "Scope",
    "leadership": "Leadership", "accountability": "Accountability", "job_evaluation": "Job evaluation (illustrative)",
    "source_pcf": "UK GDaD PCF", "source_reference": "This reference", "used_in": "Used in {n} role levels.",
    "awareness": "Awareness", "working": "Working", "practitioner": "Practitioner", "expert": "Expert",
    "sfia_level": "SFIA level", "esco_occupation": "ESCO occupation", "pcf_family": "PCF family",
    "roles_in_reference": "Roles in this reference",
}


def slugify(text):
    """A URL slug that keeps accented and non-Latin letters, for per-locale slugs."""
    return re.sub(r"[^\w]+", "-", text.lower(), flags=re.UNICODE).strip("-_")


def anchor(text):
    """The anchor GitHub gives a Markdown heading: lowercase, punctuation removed, spaces to hyphens."""
    text = re.sub(r"[^\w\- ]", "", text.lower(), flags=re.UNICODE)
    return text.replace(" ", "-")


def codes():
    if not os.path.isdir(DATA_LOCALES):
        return []
    return sorted(c for c in os.listdir(DATA_LOCALES) if os.path.isfile(os.path.join(DATA_LOCALES, c, "locale.yaml")))


def _load(code, *parts, default=None):
    path = os.path.join(DATA_LOCALES, code, *parts)
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or default


class Locale:
    def __init__(self, code):
        self.code = code
        meta = _load(code, "locale.yaml", default={})
        self.name = meta.get("name", code)
        self.english_name = meta.get("english_name", code)
        self.dir = meta.get("dir", "ltr")
        self.complete = bool(meta.get("complete", False))
        self.strings = dict(STRINGS, **(meta.get("strings") or {}))
        self.catalogue = _load(code, "catalogue.yaml", default={}) or {}
        # Skills may be one skills.yaml or, mirroring data/skills/, one file per domain in skills/.
        self.skills = dict(_load(code, "skills.yaml", default={}) or {})
        skills_dir = os.path.join(DATA_LOCALES, code, "skills")
        if os.path.isdir(skills_dir):
            for name in sorted(os.listdir(skills_dir)):
                if name.endswith(".yaml"):
                    self.skills.update(_load(code, "skills", name, default={}) or {})
        self.bands = _load(code, "bands.yaml", default={}) or {}
        self.factors = _load(code, "job-evaluation.yaml", default={}) or {}
        self.roles = {}
        roles_dir = os.path.join(DATA_LOCALES, code, "roles")
        if os.path.isdir(roles_dir):
            for name in sorted(os.listdir(roles_dir)):
                if name.endswith(".yaml"):
                    self.roles[name[:-5]] = _load(code, "roles", name, default={}) or {}
        self.missing = []

    def s(self, key, **kw):
        return self.strings[key].format(**kw) if kw else self.strings[key]


def localize(reference, loc):
    """Overlay a locale's translations on the English reference. Returns (localized, errors)."""
    ref = copy.deepcopy(reference)
    errors = []
    loc.missing = []

    def pick(table, key, field, english, where):
        value = (table.get(key) or {}).get(field) if isinstance(table.get(key), dict) else None
        if value in (None, "", []):
            loc.missing.append(f"{where}: {field}")
            return english
        return value

    ref["meta"]["locale"] = loc.code
    ref["meta"]["localeName"] = loc.name
    ref["meta"]["disclaimer"] = loc.s("disclaimer")
    ref["meta"]["translationNote"] = loc.s("translation_note")
    for lv in ref["meta"]["levels"]:
        lv["name"] = loc.s(lv["id"])

    families = loc.catalogue.get("families") or {}
    for f in ref["families"]:
        f["title"] = pick(families, f["id"], "title", f["title"], f"catalogue family {f['id']}")
        f["slug"] = (families.get(f["id"]) or {}).get("slug") or slugify(f["title"])

    for b in ref["bands"]:
        for field in ("title", "stage", "knowledge", "autonomy", "scope", "leadership", "accountability"):
            b[field] = pick(loc.bands, b["id"], field, b[field], f"band {b['id']}")

    for f in ref["factors"]:
        f["name"] = pick(loc.factors, f["id"], "name", f["name"], f"factor {f['id']}")
        f["description"] = pick(loc.factors, f["id"], "description", f["description"], f"factor {f['id']}")
        levels = (loc.factors.get(f["id"]) or {}).get("levels") or {}
        for lv in f["levels"]:
            # YAML may read an unquoted level key such as 1 as a number.
            text = levels.get(lv) or (levels.get(int(lv)) if str(lv).isdigit() else None)
            if text:
                f["levels"][lv] = text
            else:
                loc.missing.append(f"factor {f['id']}: level {lv}")

    for s in ref["skills"]:
        if s["source"] == "pcf":
            continue  # quoted from the UK GDaD PCF, in English
        t = loc.skills.get(s["id"]) or {}
        s["name"] = pick(loc.skills, s["id"], "name", s["name"], f"skill {s['id']}")
        s["description"] = pick(loc.skills, s["id"], "description", s["description"], f"skill {s['id']}")
        for lv in LEVELS:
            text = (t.get("levels") or {}).get(lv)
            if text:
                s["levels"][lv] = text.strip()
            else:
                loc.missing.append(f"skill {s['id']}: level {lv}")
        s["slug"] = t.get("slug") or slugify(s["name"])

    role_titles = loc.catalogue.get("roles") or {}
    for r in ref["roles"]:
        r["title"] = pick(role_titles, r["id"], "title", r["title"], f"catalogue role {r['id']}")
        r["slug"] = (role_titles.get(r["id"]) or {}).get("slug") or slugify(r["title"])
        t = loc.roles.get(r["id"]) or {}
        where = f"roles/{r['id']}.yaml"
        if not t:
            loc.missing.append(f"{where}: whole file")
        r["summary"] = (t.get("summary") or "").strip() or r["summary"]
        if not t.get("summary"):
            loc.missing.append(f"{where}: summary")
        if r["healthContext"]:
            if t.get("health_context"):
                r["healthContext"] = t["health_context"]
            else:
                loc.missing.append(f"{where}: health_context")
        tl = t.get("levels") or []
        if tl and len(tl) != len(r["levels"]):
            errors.append(f"{loc.code}: {where}: has {len(tl)} levels, English has {len(r['levels'])}")
            tl = []
        for i, level in enumerate(r["levels"]):
            lt = tl[i] if i < len(tl) else {}
            lw = f"{where}: level {i + 1}"
            for field, key in (("title", "title"), ("summary", "summary"), ("responsibilities", "responsibilities"),
                               ("qualifications", "qualifications"), ("job_evaluation_notes", "jobEvaluationNotes")):
                english = level[key]
                if not english:
                    continue
                if lt.get(field):
                    level[key] = lt[field].strip() if isinstance(lt[field], str) else lt[field]
                else:
                    loc.missing.append(f"{lw}: {field}")
            level["slug"] = lt.get("slug") or slugify(level["title"])

    # Slugs must be unique and URL-safe within each kind.
    def check(kind, items):
        seen = {}
        for item in items:
            sl = item["slug"]
            if not sl or "/" in sl or sl != sl.strip("-") or any(c.isspace() for c in sl) or sl != sl.lower():
                errors.append(f"{loc.code}: {kind} '{item['id']}' has an invalid slug '{sl}'")
            if sl in seen:
                errors.append(f"{loc.code}: {kind} slug '{sl}' is used by both '{seen[sl]}' and '{item['id']}'")
            seen[sl] = item["id"]
    check("family", ref["families"])
    check("role", ref["roles"])
    check("skill", ref["skills"])
    for r in ref["roles"]:
        check(f"level of {r['id']}", r["levels"])

    if loc.complete and loc.missing:
        errors.append(f"{loc.code}: marked complete, but {len(loc.missing)} translations are missing, "
                      f"for example {loc.missing[0]}")
    return ref, errors


def write_reference(ref, loc):
    out = os.path.join(EXPORT_LOCALES, loc.code)
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "reference.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(ref, f, ensure_ascii=False, indent=1)
        f.write("\n")


# ---------------------------------------------------------------- documents

def _cell(text):
    text = text.strip().replace("|", "\\|")
    return re.sub(r"\n-\s*", "<br>• ", text).replace("\n", " ")


def _quote(text):
    return "> " + "\n".join(line.rstrip() for line in text.strip().splitlines()).replace("\n", "\n> ")


def write_docs(ref, loc, write_doc):
    """Write the locale's documents to locales/<code>/, mirroring docs/."""
    root = os.path.join(DOC_LOCALES, loc.code)
    shutil.rmtree(root, ignore_errors=True)
    S = loc.s
    skills = {s["id"]: s for s in ref["skills"]}
    bands = {b["id"]: b for b in ref["bands"]}
    families = {f["id"]: f for f in ref["families"]}
    occupations = {o["id"]: o for o in ref["occupations"]}
    meta = ref["meta"]
    head = [f"> {S('disclaimer')}", ""] + ([f"> {S('translation_note')}", ""] if S("translation_note") else [])
    footer = ["", "---", "", f"*{meta['pcf']['credit']}*  ", f"*{meta['esco']['credit']}*"]

    def level_heading(level):
        return f"{S('band')} {level['band']}: {level['title']}"

    for r in ref["roles"]:
        fam = families[r["family"]]
        out = [f"# {r['title']}", ""] + head
        out += [f"**{S('family')}:** [{fam['title']}](../../#{anchor(fam['title'])})  ",
                f"**{S('bands')}:** {', '.join(l['band'] for l in r['levels'])}  "]
        if r["pcfRole"]:
            out.append(f"**{S('pcf_role')}:** [{r['pcfRole']['name']}]({r['pcfRole']['url']})  ")
        else:
            out.append(f"**{S('pcf_role')}:** {S('pcf_role_none')}  ")
        occs = [occupations[u] for u in r["esco"] if u in occupations]
        out.append(f"**{S('esco_occupations')}:** " + "; ".join(f"[{o['label']}]({o['uri']}) (ISCO-08 {o['isco08']})" for o in occs))
        out += ["", f"## {S('summary')}", "", r["summary"], ""]
        if r["healthContext"]:
            out += [f"## {S('health_context')}", ""] + [f"- {x}" for x in r["healthContext"]] + [""]
        if r["pcfRole"]:
            out += [f"## {S('pcf_role_description')}", "", _quote(r["pcfRole"]["description"]), ""]
        out += [f"## {S('role_levels')}", "",
                f"| {S('band')} | {S('title')} | {S('pcf_level')} | {S('civil_service_grades')} | {S('job_evaluation_points')} |",
                "| --- | --- | --- | --- | --- |"]
        for l in r["levels"]:
            out.append(f"| {l['band']} | [{l['title']}](#{anchor(level_heading(l))}) | {l['pcfLevel'] or '—'} | "
                       f"{l['civilServiceGrades'] or '—'} | {l['jobEvaluationPoints']} |")
        out.append("")
        for l in r["levels"]:
            b = bands[l["band"]]
            out += [f"## {level_heading(l)}", ""]
            if l["summary"]:
                out += [l["summary"], ""]
            if l["pcfLevelDescription"]:
                out += [f"**{S('pcf_level')}: {l['pcfLevel']}**", "", _quote(l["pcfLevelDescription"]), ""]
            out += [f"### {S('responsibilities')}", ""] + [f"- {x}" for x in l["responsibilities"]] + [""]
            out += [f"### {S('skills')}", "",
                    f"| {S('skill')} | {S('source')} | {S('expected_level')} | {S('level_meaning')} |", "| --- | --- | --- | --- |"]
            for use in l["skills"]:
                sk = skills[use["id"]]
                src = S("source_pcf") if sk["source"] == "pcf" else S("source_reference")
                out.append(f"| [{sk['name']}](../../skills/#{anchor(sk['name'])}) | {src} | {S(use['level'])} | {_cell(sk['levels'][use['level']])} |")
            out.append("")
            if l["qualifications"]:
                out += [f"### {S('qualifications')}", ""] + [f"- {x}" for x in l["qualifications"]] + [""]
            out += [f"### {S('band_outline')}", ""] + [f"- **{S(k)}:** {b[k]}" for k in ("knowledge", "autonomy", "scope", "leadership", "accountability")] + [""]
            out += [f"### {S('job_evaluation')}", "", f"| # | {S('factor')} | {S('level')} | {S('points')} |", "| --- | --- | --- | --- |"]
            for i, f in enumerate(ref["factors"], 1):
                lv = l["jobEvaluation"][f["id"]]
                out.append(f"| {i} | {f['name']} | {lv} | {f['points'][lv]} |")
            out += [f"| | **{S('total')}** | | **{l['jobEvaluationPoints']}** ({S('band')} {l['band']}: {b['points']['min']}–{b['points']['max']}) |", ""]
            if l["jobEvaluationNotes"]:
                out += [l["jobEvaluationNotes"], ""]
        write_doc(os.path.join(root, "roles", r["slug"]), "\n".join(out + footer), peer=f"role:{r['id']}")

    roles_by_family = {}
    for r in ref["roles"]:
        roles_by_family.setdefault(r["family"], []).append(r)

    out = [f"# {S('home_title')}", ""] + head + [S("home_lede"), ""]
    for f in ref["families"]:
        out += [f"## {f['title']}", "", f"| {S('role')} | {S('bands')} | {S('pcf_role')} |", "| --- | --- | --- |"]
        for r in roles_by_family.get(f["id"], []):
            out.append(f"| [{r['title']}](roles/{r['slug']}/) | {', '.join(l['band'] for l in r['levels'])} | "
                       f"{r['pcfRole']['name'] if r['pcfRole'] else '—'} |")
        out.append("")
    write_doc(root, "\n".join(out + footer), peer="home")

    out = [f"# {S('roles_title')}", ""] + head + [f"| {S('role')} | {S('family')} | {S('bands')} |", "| --- | --- | --- |"]
    for r in sorted(ref["roles"], key=lambda r: r["title"].lower()):
        fam = families[r["family"]]
        out.append(f"| [{r['title']}]({r['slug']}/) | [{fam['title']}](../#{anchor(fam['title'])}) | {', '.join(l['band'] for l in r['levels'])} |")
    write_doc(os.path.join(root, "roles"), "\n".join(out + footer), peer="roles")

    out = [f"# {S('bands_title')}", ""] + head
    for b in ref["bands"]:
        out += [f"## {S('band')} {b['id']}", "", f"*{b['stage']}. {S('sfia_level')} {b['sfia_level']}. "
                f"{S('job_evaluation_points')} {b['points']['min']}–{b['points']['max']}.*", ""]
        out += [f"- **{S(k)}:** {b[k]}" for k in ("knowledge", "autonomy", "scope", "leadership", "accountability")] + [""]
        rows = [(r, l) for r in ref["roles"] for l in r["levels"] if l["band"] == b["id"]]
        if rows:
            out += [f"| {S('role_level')} | {S('family')} |", "| --- | --- |"]
            for r, l in sorted(rows, key=lambda x: (families[x[0]["family"]]["title"], x[1]["title"])):
                out.append(f"| [{l['title']}](../roles/{r['slug']}/#{anchor(level_heading(l))}) | {families[r['family']]['title']} |")
            out.append("")
    write_doc(os.path.join(root, "bands"), "\n".join(out + footer), peer="bands")

    used = {}
    for r in ref["roles"]:
        for l in r["levels"]:
            for use in l["skills"]:
                used[use["id"]] = used.get(use["id"], 0) + 1
    out = [f"# {S('skills_title')}", ""] + head + [S("skills_lede"), ""]
    for sk in sorted(ref["skills"], key=lambda s: s["name"].lower()):
        src = S("source_pcf") if sk["source"] == "pcf" else S("source_reference")
        out += [f"## {sk['name']}", "", f"*{src}. {S('used_in', n=used.get(sk['id'], 0))}*", "", sk["description"], ""]
        for lv in LEVELS:
            out += [f"**{S(lv)}:**", "", sk["levels"][lv], ""]
    write_doc(os.path.join(root, "skills"), "\n".join(out + footer), peer="skills")

    out = [f"# {S('pcf_title')}", ""] + head + [
        f"| {S('pcf_family')} | {S('pcf_role')} | {S('pcf_level')} | {S('civil_service_grades')} | {S('role_level')} | {S('band')} |",
        "| --- | --- | --- | --- | --- | --- |"]
    for r in sorted((r for r in ref["roles"] if r["pcfRole"]), key=lambda r: (r["pcfRole"]["family"], r["pcfRole"]["name"])):
        for l in r["levels"]:
            if l["pcfLevel"]:
                out.append(f"| {r['pcfRole']['family']} | {r['pcfRole']['name']} | {l['pcfLevel']} | {l['civilServiceGrades'] or '—'} | "
                           f"[{l['title']}](../roles/{r['slug']}/#{anchor(level_heading(l))}) | {l['band']} |")
    write_doc(os.path.join(root, "pcf"), "\n".join(out + footer), peer="pcf")

    out = [f"# {S('esco_title')}", ""] + head + [f"| {S('esco_occupation')} | ISCO-08 | {S('roles_in_reference')} |", "| --- | --- | --- |"]
    for o in sorted(ref["occupations"], key=lambda o: o["label"]):
        rs = [r for r in ref["roles"] if o["id"] in r["esco"]]
        out.append(f"| [{o['label']}]({o['uri']}) | {o['isco08']} | " + ", ".join(f"[{r['title']}](../roles/{r['slug']}/)" for r in rs) + " |")
    write_doc(os.path.join(root, "esco"), "\n".join(out + footer), peer="esco")
