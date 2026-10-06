#!/usr/bin/env python3
"""Check that every relative link in the repository's Markdown files resolves.

Checks the file or directory a link points to (a document directory
holds index.md, which GitHub shows through its README.md symlink), and for links into generated docs (docs/ and locales/) with a
#fragment, that the fragment exists as a heading or an <a id> anchor.
Skips URLs, site-absolute paths, the website's node_modules, and data/sources/.

Usage: python3 scripts/check_links.py
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r"\]\(([^)\s]+)\)")


def anchors(path, cache={}):
    if path not in cache:
        text = open(path, encoding="utf-8").read()
        found = set(re.findall(r'<a id="([^"]+)"', text))
        for heading in re.findall(r"^#+\s+(.*)$", text, re.M):
            # GitHub keeps Unicode letters, such as Welsh accented vowels, in heading anchors.
            found.add(re.sub(r"[^\w\- ]", "", heading.lower()).strip().replace(" ", "-"))
        cache[path] = found
    return cache[path]


def main():
    os.chdir(ROOT)
    # -z: NUL-separated and unquoted, so paths with non-ASCII slugs (Welsh, Chinese) are kept.
    files = subprocess.check_output(["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard", "*.md"], text=True).split("\0")
    files = [f for f in files if os.path.isfile(f) and not os.path.islink(f) and not f.startswith("data/sources/") and "node_modules" not in f]
    broken = 0
    for f in files:
        text = open(f, encoding="utf-8").read()
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        for target in LINK.findall(text):
            if re.match(r"^[a-z]+:", target) or target.startswith(("/", "#", "<")):
                continue
            path, _, frag = target.partition("#")
            resolved = os.path.normpath(os.path.join(os.path.dirname(f), path or "."))
            if os.path.isdir(resolved):
                # A document directory: GitHub shows its README.md, a symlink to index.md.
                # A data directory (no index.md) is fine as a plain folder link.
                if os.path.isfile(os.path.join(resolved, "index.md")):
                    resolved = os.path.join(resolved, "index.md")
                elif frag:
                    print(f"{f}: anchor into a directory with no index.md: {target}")
                    broken += 1
                    continue
            if not os.path.exists(resolved):
                print(f"{f}: missing {target}")
                broken += 1
            elif frag and resolved.endswith(".md") and resolved.startswith(("docs/", "locales/")) and frag not in anchors(resolved):
                print(f"{f}: missing anchor {target}")
                broken += 1
    print(f"{len(files)} files checked, {broken} broken links")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
