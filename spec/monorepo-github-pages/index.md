# Monorepo GitHub pages

Goal: publish the website by using git subtree to export it from this monorepo to a sibling read-only repository.

This project is a monorepo: `roles-skills/roles-skills` on GitHub.

It contains a GitHub Pages subproject: `roles-skills.github.io/`.

The GitHub Pages subproject uses:

- [GitHub Pages](https://pages.github.com/)
- [SvelteKit](https://svelte.dev/docs/kit/)
- [Lily Design System](https://github.com/LilyDesignSystem/lily-design-system), including its PickerBar
- [Sveltia CMS](https://github.com/sveltia/sveltia-cms)

## Locales

The website serves every published locale from the same build: English at the unprefixed paths, and each other locale under `/<language>-<region>/`, such as `/cy-gb/`. See [`../locales/index.md`](../locales/index.md).

## Publish

To publish the GitHub Pages subproject, use git subtree to derive a sibling read-only export repository: `roles-skills/roles-skills.github.io` on GitHub, served at <https://roles-skills.github.io>.

## Makefile

File `Makefile` provides task `make github-pages`, which delegates to the POSIX shell script `bin/make-github-pages`. The script runs the subtree push:

```sh
git subtree push --prefix=roles-skills.github.io github-pages main
```

The remote is always named `github-pages`, the same as the task and the script. One name means nothing is left to guess. The script, not the Makefile, carries the safety checks, so they live in one place and the Makefile task stays a one-line delegation:

- an uncommitted-changes guard
- a validation pass: `bin/check`

```make
.PHONY: github-pages
github-pages:
	bin/make-github-pages
```

To add the remote once:

```sh
git remote add github-pages git@github.com:roles-skills/roles-skills.github.io.git
```

## Maintenance

Always maintain the GitHub Pages subproject here: `roles-skills.github.io/`.

To maintain the sibling read-only export repository, always use git subtree. Never work directly in `roles-skills/roles-skills.github.io`. A commit made there directly has no common ancestor with the next subtree split, so the next publish is rejected.

## Content editing

Sveltia CMS at `/admin/` on the website edits this monorepo's `data/` through the GitHub backend (`roles-skills/roles-skills`, branch `main`). It never edits the export repository. After an edit, regenerate and publish:

```sh
git pull
python3 scripts/build.py
roles-skills.github.io/bin/sync
git commit -am "Regenerate after content edits"
make github-pages
```
