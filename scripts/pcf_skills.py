#!/usr/bin/env python3
"""Write research/pcf-skills.tsv: every UK GDaD PCF skill with the id that
role files use to refer to it (pcf:<slug>), and the PCF roles that use it."""
import csv
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


with open(os.path.join(ROOT, "data", "sources", "pcf", "skills.csv"), encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
with open(os.path.join(ROOT, "research", "pcf-skills.tsv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["skill_id", "skill_name", "description", "roles_that_require_skill"])
    for r in rows:
        w.writerow(["pcf:" + slug(r["Skill Name"]), r["Skill Name"], r["Skill Description"].replace("\n", " "), r["Roles that require Skill"].replace("\n", " ")])
print(f"wrote research/pcf-skills.tsv ({len(rows)} skills)")
