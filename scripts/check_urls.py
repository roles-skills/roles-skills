#!/usr/bin/env python3
"""Check the external links cited in this repository.

Collects every http(s) URL from the hand-written Markdown, the data YAML and
TSV files, and the website source. Then:

- ESCO concept URIs (http://data.europa.eu/esco/...) are checked against the
  ESCO data downloaded by scripts/fetch_esco.py and the curated crosswalk,
  without a request per URI. With --esco-online, any not found locally are
  looked up in the ESCO API.
- Every other URL is requested (HEAD, then GET if HEAD is refused), a few at
  a time, and reported if it does not answer with a 2xx or 3xx status.

Generated docs/ and exports/ are not scanned: they only repeat URLs from data/.
Nor is research/pcf-esco-candidates.tsv, which holds raw ESCO search results.

Usage:
    python3 scripts/check_urls.py [--esco-online]
"""
import concurrent.futures
import csv
import json
import os
import re
import ssl
import subprocess
import sys
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = re.compile(r"https?://[^\s)\]>\"'`|,]+")
SKIP_PREFIXES = (
    "https://roles-skills.github.io",          # the website itself, checked by its own build
    "http://localhost",
    "https://ec.europa.eu/esco/api",           # API base addresses in the fetch scripts
)
# Hosts that refuse automated requests, or that only accept a URL with
# placeholders or parameters filled in.
SKIP_HOSTS = {"www.linkedin.com", "www.reddit.com", "bsky.app", "mastodonshare.com", "unpkg.com"}


def context():
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


def collect():
    os.chdir(ROOT)
    files = subprocess.check_output(["git", "ls-files"], text=True).split()
    wanted = [f for f in files
              if not f.startswith(("docs/", "exports/", "data/sources/", "roles-skills.github.io/content/",
                                   "roles-skills.github.io/static/downloads/", "roles-skills.github.io/static/assets/themes/",
                                   # raw ESCO search results, before curation
                                   "research/pcf-esco-candidates.tsv"))
              and f.endswith((".md", ".yaml", ".yml", ".tsv", ".py", ".ts", ".svelte", ".html", ".txt"))
              and os.path.isfile(f) and not os.path.islink(f)]
    found = {}
    for f in wanted:
        for url in URL.findall(open(f, encoding="utf-8", errors="replace").read()):
            url = url.rstrip(".;:")
            if "{" in url or "$" in url or "<" in url or re.fullmatch(r"http://data\.europa\.eu/esco/[a-z]+/", url):
                continue  # templates and base addresses, not links
            found.setdefault(url, f)
    return found


def esco_known():
    known = set()
    with open(os.path.join(ROOT, "data", "sources", "esco", "occupations.tsv"), encoding="utf-8") as f:
        known.update(r["uri"] for r in csv.DictReader(f, delimiter="\t"))
    with open(os.path.join(ROOT, "data", "sources", "esco", "occupation-skills.tsv"), encoding="utf-8") as f:
        known.update(r["skill_uri"] for r in csv.DictReader(f, delimiter="\t"))
    with open(os.path.join(ROOT, "data", "crosswalks", "pcf-esco.tsv"), encoding="utf-8") as f:
        known.update(r["esco_skill_uri"] for r in csv.DictReader(f, delimiter="\t") if r["esco_skill_uri"])
    return known


def esco_online(uri):
    kind = uri.split("/esco/")[1].split("/")[0]
    api = f"https://ec.europa.eu/esco/api/resource/{kind}?" + urllib.parse.urlencode(
        {"uri": uri, "language": "en", "selectedVersion": "v1.2.1"})
    try:
        with urllib.request.urlopen(api, context=context(), timeout=30) as r:
            return json.load(r).get("uri") == uri
    except Exception:
        return False


def fetch(url):
    headers = {"User-Agent": "Mozilla/5.0 (link check; roles-skills)"}
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers=headers)
            with urllib.request.urlopen(req, context=context(), timeout=30) as r:
                return r.status
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 405, 400, 404, 501):
                continue
            return e.code
        except Exception as e:
            if method == "HEAD":
                continue
            return type(e).__name__
    return "error"


def main():
    online = "--esco-online" in sys.argv
    urls = collect()
    known = esco_known()
    esco = sorted(u for u in urls if u.startswith("http://data.europa.eu/esco/"))
    other = sorted(u for u in urls if u not in esco and not u.startswith(SKIP_PREFIXES)
                   and urllib.parse.urlparse(u).hostname not in SKIP_HOSTS)
    problems = []

    for u in esco:
        if u not in known and not (online and esco_online(u)):
            problems.append((u, "not in the local ESCO data" + ("" if online else " (try --esco-online)")))

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        for u, status in zip(other, pool.map(fetch, other)):
            if not (isinstance(status, int) and 200 <= status < 400):
                problems.append((u, status))

    for u, why in problems:
        print(f"{why}\t{u}\t(first seen in {urls[u]})")
    print(f"{len(esco)} ESCO URIs and {len(other)} other URLs checked; {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
