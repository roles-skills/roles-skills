#!/usr/bin/env python3
"""Summarise completed self-assessment TSV files into a team gap analysis.

Usage:
    python3 scripts/gap_analysis.py OUTPUT_DIR FILE.tsv [FILE.tsv ...]

Each input is a copy of a file from exports/self-assessment/, filled in by one
person. Name each copy after the person, for example "alex.tsv". Ratings may
be numbers (0-4) or level names (not yet, awareness, working, practitioner,
expert). The manager rating is used where present, otherwise the self rating.

Writes to OUTPUT_DIR:
    gap-by-person.tsv   one row per person and skill, with expected, assessed, and gap
    gap-by-skill.tsv    one row per skill: people assessed, people below expected, average gap
    gap-matrix.tsv      skills down the side, people across the top, gap in each cell
"""
import collections
import csv
import os
import sys

LEVELS = {"not yet": 0, "none": 0, "awareness": 1, "working": 2, "practitioner": 3, "expert": 4}


def rating(value):
    value = (value or "").strip().lower()
    if not value:
        return None
    if value in LEVELS:
        return LEVELS[value]
    try:
        n = int(float(value))
    except ValueError:
        raise SystemExit(f"error: cannot read rating '{value}'")
    if not 0 <= n <= 4:
        raise SystemExit(f"error: rating {n} is outside 0-4")
    return n


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    out_dir, files = argv[1], argv[2:]
    os.makedirs(out_dir, exist_ok=True)
    rows, people, skills = [], [], []
    for path in files:
        person = os.path.splitext(os.path.basename(path))[0]
        people.append(person)
        with open(path, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                expected = int(r["expected_level_number"])
                assessed = rating(r.get("manager_rating")) if rating(r.get("manager_rating")) is not None else rating(r.get("self_rating"))
                gap = "" if assessed is None else max(expected - assessed, 0)
                rows.append({"person": person, "role_level": r["role_level"], "band": r["band"], "skill": r["skill"],
                             "expected": expected, "assessed": "" if assessed is None else assessed, "gap": gap,
                             "development_action": r.get("development_action", "")})
                if r["skill"] not in skills:
                    skills.append(r["skill"])

    def write(name, header, data):
        with open(os.path.join(out_dir, name), "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter="\t", lineterminator="\n")
            w.writerow(header)
            w.writerows(data)

    write("gap-by-person.tsv", ["person", "role_level", "band", "skill", "expected", "assessed", "gap", "development_action"],
          [[r[k] for k in ("person", "role_level", "band", "skill", "expected", "assessed", "gap", "development_action")] for r in rows])

    by_skill = collections.defaultdict(list)
    for r in rows:
        if r["gap"] != "":
            by_skill[r["skill"]].append(r["gap"])
    summary = []
    for s in skills:
        gaps = by_skill.get(s, [])
        below = sum(1 for g in gaps if g > 0)
        avg = round(sum(gaps) / len(gaps), 2) if gaps else ""
        summary.append([s, len(gaps), below, avg])
    summary.sort(key=lambda x: (-(x[2] or 0), -(x[3] or 0) if x[3] != "" else 0))
    write("gap-by-skill.tsv", ["skill", "people_assessed", "people_below_expected", "average_gap"], summary)

    cell = {(r["skill"], r["person"]): r["gap"] for r in rows}
    write("gap-matrix.tsv", ["skill"] + people, [[s] + [cell.get((s, p), "") for p in people] for s in skills])
    print(f"{len(people)} people, {len(skills)} skills; wrote {out_dir}/gap-by-person.tsv, gap-by-skill.tsv, gap-matrix.tsv")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
