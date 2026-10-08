# Locales

How this reference is translated, published, and served in more than one language, and which locales are done. See [`locales-by-priority.md`](locales-by-priority.md) for the order of work, and [`../locales-for-global-sharing-with-svelte/`](../locales-for-global-sharing-with-svelte/) for the general guidance this project follows.

## Status

| Locale | Name | Direction | Status | Notes |
| --- | --- | --- | --- | --- |
| en-001 | English | ltr | Done | Source language, at the unprefixed paths |
| cy-001 | Cymraeg (y byd) | ltr | Done | A copy of cy-gb, for Welsh readers anywhere; keep the two in step |
| cy-gb | Cymraeg | ltr | Done | AI-translated, not yet reviewed by a native speaker; terminology follows TermCymru |
| zh-001 | 中文 | ltr | Done | Simplified Chinese; AI-translated, not yet reviewed by a native speaker; slugs are made from the Chinese titles |
| zh-cn | 中文（中国） | ltr | Done | A copy of zh-001, for Chinese readers in China; keep the two in step |
| hi-001 | हिन्दी | ltr | Done | Hindi; AI-translated, not yet reviewed by a native speaker; slugs are made from the Devanagari titles, keeping vowel signs |
| hi-in | हिन्दी (भारत) | ltr | Done | A copy of hi-001, for Hindi readers in India; keep the two in step |
| es-001 | Español | ltr | Done | Spanish; AI-translated, not yet reviewed by a native speaker; job titles use the generic form, and "Head of" is the gender-neutral "Responsable de" |
| fr-001 | Français | ltr | Done | French; AI-translated, not yet reviewed by a native speaker; job titles use the generic form, and many "Head of" roles use the gender-neutral "Responsable de" |
| ar-001 | العربية | rtl | Done | Arabic (Modern Standard Arabic), the first right-to-left locale; AI-translated, not yet reviewed by a native speaker; job titles use the conventional masculine form, which covers everyone; slugs are made from the Arabic titles |
| bn-001 | বাংলা | ltr | Done | Bengali (standard written Bengali); AI-translated, not yet reviewed by a native speaker; Western digits; slugs are made from the Bengali titles |
| ru-001 | Русский | ltr | Next | Russian |

Every translation is AI-generated and needs a native speaker review; `tasks.md` tracks each review.

## Locale codes

A locale code is `<language>-<region>`, in lowercase: a two- or three-letter ISO 639 language code, a hyphen, then a two-letter ISO 3166 region code or the three-digit UN M49 code `001` for the world. For example `cy-gb` (Welsh in Great Britain), `cy-001` (Welsh for readers anywhere), and `zh-001`.

- Prefer the world locale, `<language>-001`. A regional locale, such as `cy-gb`, `zh-cn`, or `hi-in`, may start as a copy of its world locale, kept in step with it, so that readers in that region get a matching URL and language tag.
- Never use a bare language code, such as `en`, as a locale code, a directory name, or a URL path.
- The region code must be a real ISO 3166 code for a place where the language is spoken: India is `in` (`hi-in`), not `id` (Indonesia); Pakistan is `pk` (`ur-pk`); Great Britain is `gb` (`cy-gb`).
- The default locale is `en-001`.

A locale code is not the same as a language tag. Each locale also has a BCP 47 tag, in `LOCALE_TAGS` in `roles-skills.github.io/src/lib/locales.ts`, for `<html lang>`, `hreflang`, and screen readers: `en`, `cy`, `cy-GB`, `zh-Hans`, `zh-Hans-CN`, `hi`, `hi-IN`, `es`, `fr`, `ar`, `bn`. Use the tag, not the code, wherever a browser or search engine reads the language.

## Directory names

All locale directories use the format `<language>-<region>`. A bare language code, such as `en/`, is not allowed.

This applies to every `locales` directory:

| Directory | Holds | Written by |
| --- | --- | --- |
| `data/locales/<code>/` | The translations (source of truth) | People and translators |
| `exports/locales/<code>/` | `reference.json` and `paths.json` | `scripts/build.py` |
| `locales/<code>/` | The Markdown documents, with translated folder names | `scripts/build.py` |
| `roles-skills.github.io/content/locales/<code>/` | `ui.json` (interface strings), plus copies of the exports | People (`ui.json`) and `bin/sync` |
| `roles-skills.github.io/static/downloads/locales/<code>/` | The downloadable JSON | `bin/sync` |

The build (`scripts/locales.py`) and `bin/check` both reject any other name.

## Data

Each translation in `data/locales/<code>/` mirrors the English data and holds only translated text (see [CONTRIBUTING.md](../../CONTRIBUTING.md#translations)):

- `locale.yaml`: `code`, `name` (the endonym), `english_name`, `dir` (`ltr` or `rtl`), `complete`, `paths` (translated section names), and `strings` (document strings).
- `catalogue.yaml`: family and role titles, and optional slugs.
- `bands.yaml`, `job-evaluation.yaml`, `skills/*.yaml`.
- `roles/<role-id>.yaml`: one per role, with levels in the same order as English.

Ids stay in English. The build overlays each translation on English, uses English for anything missing, and reports the count. A locale with `complete: true` fails the build if anything is missing.

Quotations from the UK GDaD PCF and labels from ESCO stay in English in every locale, because they are quotations and ESCO is used in English only.

Translations follow the abbreviations rule in [`../abbreviations/`](../abbreviations/): on each page, write each abbreviation in full words the first time, region first, with the full words translated and the abbreviation kept as it is.

## URLs

The URL carries the locale.

- The default locale, `en-001`, is at the unprefixed paths, such as `/roles/`.
- Every other locale is under its own prefix, with its own section names and slugs, such as `/cy-gb/rolau/` and `/fr-001/rôles/gestionnaire-de-paie/`.
- Section names come from `paths:` in `locale.yaml`, published as `exports/locales/<code>/paths.json`. Slugs come from the translated titles and keep accented and non-Latin letters.
- `src/hooks.ts` maps each translated URL back to its route folder (`canonicalPath`), without changing the address bar. `localePath` and `sectionPath` build translated links.
- There is no forwarding between locale paths: `/fr-001/` is served as is, and a bare-language path such as `/fr/` or `/en/` is a 404.

### Home page redirect

On a first visit to the bare home page, `/`, the site goes to the published locale that best matches the browser's languages (`navigator.languages`):

1. The exact locale code, such as `cy_GB` or `cy-GB` to `/cy-gb/`, `zh-CN` to `/zh-cn/`, and `hi-IN` to `/hi-in/`.
2. The language's world locale, such as `cy` to `/cy-001/` and `zh-TW` to `/zh-001/`.
3. Any locale of that language.

The first language that matches wins, so a reader whose first language is English stays on `/`. The redirect runs only on the app's first load (`afterNavigate` with type `enter`), never on in-site links or deep links. Once a reader chooses a language with the picker, the choice is stored in `localStorage` under `roles-skills.locale-chosen`, and the home page stops redirecting. The matching is `browserLocale` in `src/lib/locales.ts`.

## Language picker

- The picker lists every locale in `LOCALES`, labelled with `LOCALE_LABELS`, each in its own language.
- It reflects the URL and navigates to the same page in the chosen locale, using the page's alternates; a page with no peer in that locale goes to that locale's home page.
- It gets a detached target element, so it never writes its raw code (such as `zh-001`) to `<html lang>`; the layout sets `lang` and `dir` from the BCP 47 tag instead.

## Interface strings

`roles-skills.github.io/content/locales/<code>/ui.json` holds the website's interface strings: the same keys as `en-001` (210 today), with the same `{placeholders}`. `bin/check` fails if a locale is missing a key. `banner.end` holds the closing punctuation, such as `।` for Hindi and Bengali and `。` for Chinese.

## Documents and peer ids

`scripts/build.py` writes each locale's Markdown documents to `locales/<code>/`, with translated folder names, such as `locales/cy-gb/rolau/`. Every document directory holds `index.md`, a `README.md` symlink to it, and a `.locale-peer-id` file: a 32-character lowercase hexadecimal id and a newline, identical across every locale's version of the same page, whatever its slug. `bin/check` verifies all three.

## Right-to-left locales

A locale with `dir: rtl` in `locale.yaml` and a language in `RTL` in `src/lib/locales.ts` (Arabic, Persian, Hebrew, Urdu) gets `dir="rtl"` on `<html>`. ar-001 is the first.

- The stylesheet uses logical properties, such as `padding-inline-start`, `border-inline-start`, and `text-align: start`, so the layout mirrors by itself. Never add `left` or `right` properties.
- Anything that points a direction, such as the breadcrumb chevron, needs a `[dir='rtl']` rule.
- English quotations from the UK GDaD PCF and ESCO carry `lang="en"`; in a right-to-left page, the stylesheet sets them left to right and isolates them, so their punctuation and bullets stay in place.
- Check every page layout, table, and picker in a browser, at desktop and phone widths, before publishing a right-to-left locale.

## Adding a locale

1. Translate serially, one locale at a time, without subagents.
2. Add `data/locales/<code>/`, including translated section names under `paths:` in `locale.yaml`.
3. Add `roles-skills.github.io/content/locales/<code>/ui.json`, and add the code to `LOCALES` in `roles-skills.github.io/src/lib/locale-codes.js`, its label to `LOCALE_LABELS` and tag to `LOCALE_TAGS` in `src/lib/locales.ts`, and its `ui.json` import to `src/lib/i18n.ts`.
4. Run `python3 scripts/build.py` until it reports no missing translations, then set `complete: true`.
5. Run `roles-skills.github.io/bin/sync`, `bin/check`, `python3 scripts/check_links.py`, and in `roles-skills.github.io/`, `pnpm check` and `pnpm build`.
6. Check pages in a browser: the locale's home page, search, a role level page with its self assessment, the picker, and every section.
7. Update this file's status table, `README.md`, and `tasks.md`.
8. Commit, push, publish with `make github-pages`, watch the deploy, and verify the live site.
9. Stop, and ask before starting the next locale.
