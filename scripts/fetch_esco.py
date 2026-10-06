#!/usr/bin/env python3
"""Download the ESCO occupations used by data/catalogue.yaml into data/sources/esco/.

For each occupation, saves its label, description, alternative labels, ISCO-08
group, and its essential and optional skills (with skill type).

Source: ESCO (European Skills, Competences, Qualifications and Occupations),
European Commission, https://esco.ec.europa.eu/ — API https://ec.europa.eu/esco/api
Reuse is authorised, provided the source is acknowledged
(Commission Decision 2011/833/EU).
"""
import csv
import datetime
import json
import os
import ssl
import sys
import time
import urllib.parse
import urllib.request

import yaml

VERSION = "v1.2.1"
API = "https://ec.europa.eu/esco/api/resource/occupation"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "sources", "esco")
CACHE = os.path.join(OUT, "cache")


def context():
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


def fetch(uuid):
    path = os.path.join(CACHE, uuid + ".json")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    uri = "http://data.europa.eu/esco/occupation/" + uuid
    url = API + "?" + urllib.parse.urlencode({"uri": uri, "language": "en", "selectedVersion": VERSION})
    with urllib.request.urlopen(url, context=context(), timeout=60) as r:
        data = json.load(r)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    time.sleep(0.3)
    return data


def isco_label(code):
    path = os.path.join(CACHE, f"isco-{code}.json")
    if not os.path.exists(path):
        url = "https://ec.europa.eu/esco/api/resource/concept?" + urllib.parse.urlencode(
            {"uri": f"http://data.europa.eu/esco/isco/C{code}", "language": "en", "selectedVersion": VERSION})
        with urllib.request.urlopen(url, context=context(), timeout=60) as r:
            data = json.load(r)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
    with open(path, encoding="utf-8") as f:
        return json.load(f).get("title", "")


def main():
    os.makedirs(CACHE, exist_ok=True)
    with open(os.path.join(ROOT, "data", "catalogue.yaml"), encoding="utf-8") as f:
        catalogue = yaml.safe_load(f)
    uuids = []
    for family in catalogue["families"]:
        for role in family["roles"]:
            for u in role["esco"]:
                if u not in uuids:
                    uuids.append(u)

    occupations, skills = [], []
    for u in uuids:
        d = fetch(u)
        links = d.get("_links", {})
        isco = (links.get("broaderIscoGroup") or [{}])[0]
        if not isco.get("code"):
            # Some occupations sit under another occupation, not directly under an
            # ISCO-08 group; their ISCO-08 group is the first four digits of the code.
            code = d.get("code", "")[:4]
            isco = {"code": code, "title": isco_label(code)}
        occupations.append({
            "id": u,
            "uri": d["uri"],
            "label": d.get("title", ""),
            "code": d.get("code", ""),
            "isco_08": isco.get("code", ""),
            "isco_08_label": isco.get("title", ""),
            "description": (d.get("description", {}).get("en", {}) or {}).get("literal", "").strip(),
            "alternative_labels": "; ".join(d.get("alternativeLabel", {}).get("en", [])),
        })
        for relation, key in (("essential", "hasEssentialSkill"), ("optional", "hasOptionalSkill")):
            for s in links.get(key, []):
                skills.append({
                    "occupation_id": u,
                    "occupation_label": d.get("title", ""),
                    "relation": relation,
                    "skill_uri": s["uri"],
                    "skill_label": s.get("title", ""),
                    "skill_type": s.get("skillType", "").rsplit("/", 1)[-1],
                })

    def write(name, rows):
        with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter="\t", lineterminator="\n")
            w.writeheader()
            for r in rows:
                w.writerow({k: str(v).replace("\t", " ").replace("\n", " ") for k, v in r.items()})

    write("occupations.tsv", occupations)
    write("occupation-skills.tsv", skills)
    with open(os.path.join(OUT, "ACCESSED.txt"), "w") as f:
        f.write(f"ESCO {VERSION} via {API}\naccessed {datetime.date.today().isoformat()}\n")
    print(f"{len(occupations)} occupations, {len(skills)} occupation-skill relations saved to {OUT}")


if __name__ == "__main__":
    sys.exit(main())
