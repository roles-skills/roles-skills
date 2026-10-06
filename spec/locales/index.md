# Locales

How this reference is translated, and which locales are done. See [`locales-by-priority.md`](locales-by-priority.md) for the order, and [`../locales-for-global-sharing-with-svelte/`](../locales-for-global-sharing-with-svelte/) for how the website handles locales.

## Status

| Locale | Name | Status | Notes |
| --- | --- | --- | --- |
| en-001 | English | Done | Source language, at the unprefixed paths |
| cy-001 | Cymraeg (y byd) | Done | A copy of cy-gb, for Welsh readers anywhere; keep the two in step |
| cy-gb | Cymraeg | Done | AI-translated, not yet reviewed by a native speaker; terminology follows TermCymru |
| zh-001 | 中文 | Done | Simplified Chinese; AI-translated, not yet reviewed by a native speaker; slugs are made from the Chinese titles |

## Process

1. Translate serially, one locale at a time, without subagents.
2. Add `data/locales/<code>/`, including translated section names under `paths:` in `locale.yaml`, (see [CONTRIBUTING.md](../../CONTRIBUTING.md#translations)) and `roles-skills.github.io/content/locales/<code>/ui.json`, and add the code to `roles-skills.github.io/src/lib/locale-codes.js` and its label to `src/lib/locales.ts`.
3. Run `make build` until the build reports no missing translations, then set `complete: true`.
4. Run `make check`, build the website, and check pages in a browser.
5. Commit, push, publish with `make github-pages`, and verify the live site.
6. Stop, and ask before starting the next locale.
