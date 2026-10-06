#!/usr/bin/env python3
"""Write research/pcf-role-levels.tsv: every UK GDaD PCF role level, with its
most common Civil Service grades and the band suggested by bands.yaml."""
import csv
import os

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rule = yaml.safe_load(open(os.path.join(ROOT, "data", "bands.yaml")))["grade_to_band"]
family = {}
with open(os.path.join(ROOT, "data", "sources", "pcf", "roles.csv"), encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        family[row["Role"]] = row["Role Family"]
with open(os.path.join(ROOT, "data", "sources", "pcf", "grades.tsv"), encoding="utf-8") as f:
    grades = list(csv.DictReader(f, delimiter="\t"))
with open(os.path.join(ROOT, "research", "pcf-role-levels.tsv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["pcf_family", "pcf_role", "level_number", "pcf_level", "civil_service_grades", "suggested_band"])
    for g in grades:
        w.writerow([family.get(g["role"], ""), g["role"], g["level_number"], g["role_level"], g["civil_service_grades"], rule.get(g["civil_service_grades"], "")])
print("wrote research/pcf-role-levels.tsv")
