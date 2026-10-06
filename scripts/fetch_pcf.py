#!/usr/bin/env python3
"""Download UK GDaD PCF content into data/sources/pcf/.

Fetches the official role, skill, and change-note CSV downloads, and the
most common Civil Service job grades for each role level (scraped from the
role pages, because the CSV downloads do not include grades).

Source: Government Digital and Data Profession Capability Framework,
https://understand-digital-data-roles-skills.service.gov.uk/
Licence: Open Government Licence v3.0, (c) Crown copyright.
"""
import csv
import datetime
import html
import os
import re
import sys
import time
import urllib.request

BASE = "https://understand-digital-data-roles-skills.service.gov.uk"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "sources", "pcf")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "role-reference-fetcher"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def text(fragment):
    return html.unescape(re.sub(r"<[^>]+>", " ", fragment)).strip()


def fetch_csvs():
    for name in ("roles", "skills", "changelog"):
        data = get(f"{BASE}/download/{name}.csv").decode("utf-8-sig")
        with open(os.path.join(OUT, f"{name}.csv"), "w", encoding="utf-8", newline="") as f:
            f.write(data)


def fetch_grades():
    home = get(BASE + "/").decode("utf-8")
    slugs = sorted(set(re.findall(r'href="/role/([a-z0-9-]+)/?"', home)))
    rows, seen = [], set()
    for slug in slugs:
        page = get(f"{BASE}/role/{slug}/").decode("utf-8")
        role = text(re.search(r"<title>(.*?) - ", page).group(1))
        if role in seen:  # some slugs redirect to the same role
            continue
        seen.add(role)
        for part in re.split(r'<h3 class="govuk-heading-m role-level-header"[^>]*>', page)[1:]:
            head = text(part.split("</h3>")[0])
            m = re.match(r"(\d+)\.\s*(.*)", head)
            number, level = (m.group(1), m.group(2)) if m else ("", head)
            intro = text(part.split("<table")[0])
            grades = re.findall(r"\b(AA|AO|EO|HEO|SEO|G7|G6|SCS\w*)\s*\(", intro)
            rows.append([role, slug, number, level, "/".join(grades)])
        time.sleep(0.2)
    with open(os.path.join(OUT, "grades.tsv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["role", "slug", "level_number", "role_level", "civil_service_grades"])
        w.writerows(rows)


def main():
    os.makedirs(OUT, exist_ok=True)
    fetch_csvs()
    fetch_grades()
    with open(os.path.join(OUT, "ACCESSED.txt"), "w") as f:
        f.write(f"{BASE}\naccessed {datetime.date.today().isoformat()}\n")
    print("PCF content saved to", OUT)


if __name__ == "__main__":
    sys.exit(main())
