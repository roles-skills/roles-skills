#!/usr/bin/env python3
"""Search ESCO for candidate matches to each UK GDaD PCF skill.

Writes research/pcf-esco-candidates.tsv with the top ESCO skills returned by
the ESCO search API for each PCF skill name. A person then judges each
candidate and records the agreed matches in data/crosswalks/pcf-esco.tsv.
"""
import csv
import json
import os
import re
import ssl
import time
import urllib.parse
import urllib.request

VERSION = "v1.2.1"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "data", "sources", "esco", "cache", "search")


def context():
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def search(text):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, slug(text) + ".json")
    if os.path.exists(path):
        return json.load(open(path, encoding="utf-8"))
    url = "https://ec.europa.eu/esco/api/search?" + urllib.parse.urlencode(
        {"text": text, "type": "skill", "language": "en", "limit": 6, "selectedVersion": VERSION})
    with urllib.request.urlopen(url, context=context(), timeout=60) as r:
        data = json.load(r)
    json.dump(data, open(path, "w", encoding="utf-8"))
    time.sleep(0.3)
    return data


def main():
    with open(os.path.join(ROOT, "data", "sources", "pcf", "skills.csv"), encoding="utf-8-sig") as f:
        skills = list(csv.DictReader(f))
    with open(os.path.join(ROOT, "research", "pcf-esco-candidates.tsv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["pcf_skill_id", "pcf_skill", "rank", "esco_skill_uri", "esco_skill_label"])
        for s in skills:
            # Search on the name without any "(role)" qualifier.
            name = re.sub(r"\s*\(.*?\)", "", s["Skill Name"]).strip()
            results = search(name).get("_embedded", {}).get("results", [])
            for i, r in enumerate(results, 1):
                w.writerow(["pcf:" + slug(s["Skill Name"]), s["Skill Name"], i, r["uri"], r["title"]])
    print("wrote research/pcf-esco-candidates.tsv")


if __name__ == "__main__":
    main()
