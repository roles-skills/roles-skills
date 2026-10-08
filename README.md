# Digital health care job roles reference

A public, open reference of plausible job roles for a generic digital health care organisation. For each role, at each band, it covers:

- **title and band**, from Band 2 to Band 9, with Band 8 split into 8a to 8d
- **responsibilities**
- **skills**, each with an expected proficiency level (Awareness, Working, Practitioner, or Expert)
- **job evaluation scores** across 16 factors, which show why the role sits in its band
- **links** to the UK Government Digital and Data Profession Capability Framework (UK GDaD PCF) and to ESCO, the European Skills, Competences, Qualifications and Occupations classification

It is for:

- **employees**, to find a role like their own and assess themselves against it
- **managers**, to hold clear, fair performance and development conversations
- **teams**, to run a skills gap analysis

> **Disclaimer.** These are illustrative reference profiles for a generic digital health care organisation. They are not official job descriptions for any employer, and their job evaluation scores are not a formal evaluation. Where an employee's actual job description, objectives, or evaluated job differ, those take priority.

## Start here

| I want to… | Go to |
| --- | --- |
| Find a role like mine | [Role index](docs/), or [roles by band](docs/bands/) |
| Find a role by its UK GDaD PCF or ESCO name | [By UK GDaD PCF role](docs/pcf/), or [by ESCO occupation](docs/esco/) |
| Assess myself | [Self-assessment guide](guides/self-assessment/), then [`exports/self-assessment/`](exports/self-assessment/) |
| Run a performance review | [Performance review guide](guides/performance-review/) |
| Analyse a team's skills gaps | [Gap analysis guide](guides/gap-analysis/) and [`scripts/gap_analysis.py`](scripts/gap_analysis.py) |
| Understand the frameworks | [How the frameworks fit together](guides/frameworks/) |
| See every skill and its levels | [Skills catalogue](docs/skills/) |

## What's included

- **15 role families**: software development, architecture, data, product and delivery, user-centred design, IT operations, cyber security, quality assurance testing, clinical informatics and clinical safety, information governance, finance, legal, human resources, procurement and commercial, and corporate services
- **73 roles** and **292 role levels**, from Band 2 to Band 9
- **253 skills**: 160 UK GDaD PCF skills used by the roles, plus 93 skills original to this reference for health care and corporate work
- a **16-factor job evaluation scheme** with band points ranges
- **ESCO links** for 92 occupations, with their essential and optional skills, and a crosswalk from all 186 UK GDaD PCF skills to ESCO skills

## Website

The reference is published as a static website at <https://roles-skills.github.io>, built from [`roles-skills.github.io/`](roles-skills.github.io/) with SvelteKit 3, the Lily Design System™ and its PickerBar. Each role level page has an interactive self assessment, saved in the reader's browser and exportable as TSV. The site is available in English, in Welsh (Cymraeg, at [`/cy-gb/`](https://roles-skills.github.io/cy-gb/) and, for Welsh readers anywhere, [`/cy-001/`](https://roles-skills.github.io/cy-001/)), in Simplified Chinese (中文, at [`/zh-001/`](https://roles-skills.github.io/zh-001/) and, for readers in China, [`/zh-cn/`](https://roles-skills.github.io/zh-cn/)), in Hindi (हिन्दी, at [`/hi-001/`](https://roles-skills.github.io/hi-001/) and, for readers in India, [`/hi-in/`](https://roles-skills.github.io/hi-in/)), in Spanish (Español, at [`/es-001/`](https://roles-skills.github.io/es-001/)), in French (Français, at [`/fr-001/`](https://roles-skills.github.io/fr-001/)), in Arabic (العربية, right to left, at [`/ar-001/`](https://roles-skills.github.io/ar-001/)), and in Bengali (বাংলা, at [`/bn-001/`](https://roles-skills.github.io/bn-001/)); the URL carries the locale, and the locale picker follows it. On a first visit, the bare home page, `/`, redirects to the locale that best matches the browser's languages (for example `cy_GB` to `/cy-gb/`), unless the reader has already chosen a language with the picker. Editors can change `data/` in a browser through Sveltia CMS at `/admin/`.

```sh
make build           # python3 scripts/build.py, then roles-skills.github.io/bin/sync
make check           # bin/check: data, generated files, vendored copies, links, types
make github-pages    # bin/make-github-pages: check, then git subtree push
```

See [`spec/monorepo-github-pages/`](spec/monorepo-github-pages/) and [`roles-skills.github.io/spec/`](roles-skills.github.io/spec/).

## Exports

All exports are tab-separated (TSV) files that open in any spreadsheet program.

| File | Contents |
| --- | --- |
| [`exports/self-assessment/`](exports/self-assessment/) | One file per role level. Each row is a skill with its expected level and what that level means, plus empty columns for self rating, manager rating, gap, evidence, and development action. |
| [`exports/roles.tsv`](exports/roles.tsv) | Every role level, with its family, band, PCF role and level, Civil Service grades, ESCO occupations, and job evaluation points |
| [`exports/role-skills.tsv`](exports/role-skills.tsv) | Every role level and skill, with its expected level |
| [`exports/job-evaluation.tsv`](exports/job-evaluation.tsv) | Every role level's level for each of the 16 job evaluation factors, and its total points |

## Repository layout

```text
data/
  catalogue.yaml          role families and roles, with UK GDaD PCF roles and ESCO occupations
  roles/*.yaml            one file per role: levels, responsibilities, skills, job evaluation
  skills/*.yaml           skills original to this reference, with ESCO links
  bands.yaml              bands, competency outlines, grade-to-band rule
  job-evaluation.yaml     16 factors, levels, points, band ranges
  locales/<code>/         translations of the above, such as cy-gb and cy-001 (Welsh), zh-001 and zh-cn (Chinese), hi-001 and hi-in (Hindi), es-001 (Spanish), fr-001 (French), ar-001 (Arabic), and bn-001 (Bengali)
  crosswalks/pcf-esco.tsv UK GDaD PCF skills matched to ESCO skills
  sources/pcf/            UK GDaD PCF downloads
  sources/esco/           ESCO occupations and occupation skills
docs/                     generated role pages and indexes, one <slug>/index.md each
locales/<code>/           generated pages for each translation, with translated slugs
exports/                  generated TSV files
guides/                   how-to guides
research/                 research notes on the frameworks, band mapping, and job evaluation
scripts/                  fetch, build, CMS config, link check, and analysis scripts
bin/                      check and publish scripts (see Makefile)
spec/                     specifications, such as monorepo GitHub Pages publishing
roles-skills.github.io/   the website (SvelteKit), published by git subtree
```

## Build

Requires Python 3 and PyYAML (`pip install pyyaml`).

```sh
python3 scripts/build.py --check    # validate only
python3 scripts/build.py            # validate, then regenerate docs/ and exports/
```

The build checks every role against the catalogue, the bands, the UK GDaD PCF levels and skills, the ESCO occupations, and the job evaluation scheme. Every role level's total points must fall within its band.

To refresh the source frameworks:

```sh
python3 scripts/fetch_pcf.py        # UK GDaD PCF roles, skills, change log, and grades
python3 scripts/fetch_esco.py       # ESCO v1.2.1 occupations and skills (cached)
python3 scripts/pcf_levels.py       # research/pcf-role-levels.tsv
python3 scripts/pcf_skills.py       # research/pcf-skills.tsv
```

See [CONTRIBUTING.md](CONTRIBUTING.md) to add or change roles and skills.

## Research

- [UK GDaD PCF](research/uk-gdad-pcf/): structure, roles, levels, skills, grades, and licence
- [ESCO](research/esco/): structure, version, data used, and licence
- [Framework comparison](research/framework-comparison/): the UK GDaD PCF and ESCO compared, and the skills crosswalk
- [Band mapping](research/band-mapping/): how bands relate to PCF levels, Civil Service grades, SFIA, and job evaluation
- [Job evaluation](research/job-evaluation/): the 16 factors, scoring principles, and calibration
- [SFIA](research/sfia/): levels of responsibility
- [Digital health roles](research/digital-health-roles/): 75 real job adverts compared with this reference

## Licence and credits

Original content is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), and code under the MIT licence. See [LICENSE](LICENSE).

This reference quotes and builds on:

- the **UK Government Digital and Data Profession Capability Framework**. Contains public sector information licensed under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). © Crown copyright.
- **ESCO v1.2.1**. © European Union. Reuse is authorised under Commission Decision 2011/833/EU.

See [CREDITS.md](CREDITS.md) for full credits.
