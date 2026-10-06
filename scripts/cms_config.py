#!/usr/bin/env python3
"""Generate the Sveltia CMS configuration for the website's /admin/ page.

Usage:
    python3 scripts/cms_config.py [OUTPUT]   # default: roles-skills.github.io/static/admin/config.yml

Sveltia CMS edits the source of truth: the YAML files under data/ in this
monorepo, through the GitHub backend. It never edits the website's vendored
copy (roles-skills.github.io/content/), which bin/sync regenerates.

The select lists (bands, skills, skill levels, and job evaluation factor
levels) come from the data itself, so re-run this after adding a skill, a
band, or a factor level. roles-skills.github.io/bin/sync runs it.
"""
import csv
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
SITE = "roles-skills.github.io"

# The GitHub repository that holds this monorepo, as owner/name.
REPOSITORY = os.environ.get("ROLES_SKILLS_REPOSITORY", "roles-skills/roles-skills")

LEVELS = ["awareness", "working", "practitioner", "expert"]
MATCHES = ["exact", "close", "broad", "narrow"]


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def load(*parts):
    with open(os.path.join(DATA, *parts), encoding="utf-8") as f:
        return yaml.safe_load(f)


def string(name, label, required=True, hint=None):
    field = {"name": name, "label": label, "widget": "string"}
    if not required:
        field["required"] = False
    if hint:
        field["hint"] = hint
    return field


def text(name, label, required=True, hint=None):
    field = string(name, label, required, hint)
    field["widget"] = "text"
    return field


def strings(name, label, required=True, hint=None):
    field = {"name": name, "label": label, "widget": "list", "field": {"name": "item", "label": "Item", "widget": "text"}}
    if not required:
        field["required"] = False
    if hint:
        field["hint"] = hint
    return field


def select(name, label, options, required=True, hint=None):
    field = {"name": name, "label": label, "widget": "select", "options": options}
    if not required:
        field["required"] = False
    if hint:
        field["hint"] = hint
    return field


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, SITE, "static", "admin", "config.yml")

    bands = [b["id"] for b in load("bands.yaml")["bands"]]
    factors = load("job-evaluation.yaml")["factors"]

    skill_options = []
    with open(os.path.join(DATA, "sources", "pcf", "skills.csv"), encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            skill_options.append({"label": f"{row['Skill Name']} (UK GDaD PCF)", "value": "pcf:" + slug(row["Skill Name"])})
    skill_files = sorted(n for n in os.listdir(os.path.join(DATA, "skills")) if n.endswith(".yaml"))
    for name in skill_files:
        for s in load("skills", name)["skills"]:
            skill_options.append({"label": s["name"], "value": s["id"]})
    skill_options.sort(key=lambda o: o["label"].lower())

    pcf_levels = set()
    with open(os.path.join(DATA, "sources", "pcf", "roles.csv"), encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            if row["Role Level"] != "NOT IN USE":
                pcf_levels.add(row["Role Level"])

    level_fields = [
        string("title", "Title"),
        select("band", "Band", bands),
        select("pcf_level", "UK GDaD PCF level", sorted(pcf_levels), required=False,
               hint="Only for roles that have a UK GDaD PCF role. Its description and skills are added automatically."),
        text("summary", "Summary", required=False, hint="Required when there is no UK GDaD PCF level."),
        strings("responsibilities", "Responsibilities", hint="4 to 7 bullets, each starting with a verb."),
        {"name": "skills", "label": "Skills", "widget": "list", "required": False,
         "hint": "For roles with a UK GDaD PCF level, list only the extra skills.",
         "summary": "{{fields.skill}}: {{fields.level}}",
         "fields": [select("skill", "Skill", skill_options), select("level", "Expected level", LEVELS)]},
        strings("qualifications", "Typical qualifications and experience", required=False),
        {"name": "job_evaluation", "label": "Job evaluation", "widget": "object",
         "hint": "Score every factor. The total must fall within the band's points range.",
         "fields": [select(f["id"], f["name"], [{"label": f"{lv}: {f['levels'][lv]}", "value": int(lv)} for lv in f["levels"]])
                    for f in factors]},
        text("job_evaluation_notes", "Job evaluation notes", required=False),
    ]

    config = {
        "backend": {"name": "github", "repo": REPOSITORY, "branch": "main"},
        # Sveltia CMS needs a media folder, even though this site has no media.
        "media_folder": f"{SITE}/static/assets",
        "public_folder": "/assets",
        "collections": [
            {
                "name": "roles",
                "label": "Roles",
                "label_singular": "Role",
                "description": "One file per role in data/roles/. Add a new role to the catalogue too.",
                "folder": "data/roles",
                "extension": "yaml",
                "format": "yaml",
                "create": True,
                "identifier_field": "id",
                "slug": "{{id}}",
                "summary": "{{id}}",
                "sortable_fields": ["id"],
                "fields": [
                    string("id", "Id", hint="Must match the file name and data/catalogue.yaml."),
                    text("summary", "Summary"),
                    strings("health_context", "In a digital health care organisation", required=False),
                    {"name": "levels", "label": "Levels", "label_singular": "Level", "widget": "list",
                     "summary": "Band {{fields.band}}: {{fields.title}}", "fields": level_fields},
                    strings("sources", "Sources", required=False),
                ],
            },
            {
                "name": "skills",
                "label": "Skills",
                "description": "Skills original to this reference, one file per domain in data/skills/.",
                "files": [
                    {
                        "name": slug(name[:-5]),
                        "label": name[:-5].replace("-", " ").capitalize(),
                        "file": f"data/skills/{name}",
                        "format": "yaml",
                        "fields": [{
                            "name": "skills", "label": "Skills", "label_singular": "Skill", "widget": "list",
                            "summary": "{{fields.name}}",
                            "fields": [
                                string("id", "Id", hint="Unique across all skill files."),
                                string("name", "Name"),
                                text("description", "Description"),
                                {"name": "esco", "label": "Closest ESCO skills", "widget": "list", "required": False,
                                 "summary": "{{fields.label}} ({{fields.match}})",
                                 "fields": [string("uri", "ESCO skill URI"), string("label", "ESCO skill label"),
                                            select("match", "Match", MATCHES)]},
                                {"name": "levels", "label": "Levels", "widget": "object",
                                 "fields": [text(lv, lv.capitalize()) for lv in LEVELS]},
                            ],
                        }],
                    }
                    for name in skill_files
                ],
            },
            {
                "name": "settings",
                "label": "Catalogue and bands",
                "files": [
                    {
                        "name": "catalogue", "label": "Role catalogue", "file": "data/catalogue.yaml", "format": "yaml",
                        "fields": [{
                            "name": "families", "label": "Families", "label_singular": "Family", "widget": "list",
                            "summary": "{{fields.title}}",
                            "fields": [
                                string("id", "Id"), string("title", "Title"),
                                string("pcf_family", "UK GDaD PCF family", required=False),
                                {"name": "roles", "label": "Roles", "label_singular": "Role", "widget": "list",
                                 "summary": "{{fields.title}}",
                                 "fields": [string("id", "Id"), string("title", "Title"),
                                            string("pcf_role", "UK GDaD PCF role", required=False),
                                            {"name": "esco", "label": "ESCO occupation ids", "widget": "list",
                                             "hint": "The last part of each ESCO occupation URI. Run scripts/fetch_esco.py after changing these."}]},
                            ],
                        }],
                    },
                    {
                        "name": "bands", "label": "Bands", "file": "data/bands.yaml", "format": "yaml",
                        "fields": [
                            {"name": "bands", "label": "Bands", "label_singular": "Band", "widget": "list",
                             "summary": "{{fields.title}}",
                             "fields": [string("id", "Id"), string("title", "Title"), string("stage", "Stage"),
                                        string("sfia_level", "SFIA level"),
                                        {"name": "civil_service_grades", "label": "Civil Service grades", "widget": "list"},
                                        text("knowledge", "Knowledge"), text("autonomy", "Autonomy"), text("scope", "Scope"),
                                        text("leadership", "Leadership"), text("accountability", "Accountability")]},
                            {"name": "grade_to_band", "label": "Civil Service grade to band", "widget": "keyvalue",
                             "key_label": "Grades", "value_label": "Band"},
                        ],
                    },
                ],
            },
        ],
    }

    header = (
        "# GENERATED by scripts/cms_config.py from data/ in the monorepo; do not edit.\n"
        "# Sveltia CMS at /admin/ edits data/ in the monorepo through the GitHub backend.\n"
        "# After an edit, run python3 scripts/build.py, then roles-skills.github.io/bin/sync.\n"
    )
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(header)
        yaml.safe_dump(config, f, sort_keys=False, allow_unicode=True, width=1000)


if __name__ == "__main__":
    main()
