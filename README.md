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
| Find a role like mine | [Role index](docs/index.md), or [roles by band](docs/bands.md) |
| Find a role by its UK GDaD PCF or ESCO name | [By UK GDaD PCF role](docs/pcf.md), or [by ESCO occupation](docs/esco.md) |
| Assess myself | [Self-assessment guide](guides/self-assessment.md), then [`exports/self-assessment/`](exports/self-assessment/) |
| Run a performance review | [Performance review guide](guides/performance-review.md) |
| Analyse a team's skills gaps | [Gap analysis guide](guides/gap-analysis.md) and [`scripts/gap_analysis.py`](scripts/gap_analysis.py) |
| Understand the frameworks | [How the frameworks fit together](guides/frameworks.md) |
| See every skill and its levels | [Skills catalogue](docs/skills.md) |

## What's included

- **15 role families**: software development, architecture, data, product and delivery, user-centred design, IT operations, cyber security, quality assurance testing, clinical informatics and clinical safety, information governance, finance, legal, human resources, procurement and commercial, and corporate services
- **73 roles** and **292 role levels**, from Band 2 to Band 9
- **253 skills**: 160 UK GDaD PCF skills used by the roles, plus 93 skills original to this reference for health care and corporate work
- a **16-factor job evaluation scheme** with band points ranges
- **ESCO links** for 92 occupations, with their essential and optional skills, and a crosswalk from all 186 UK GDaD PCF skills to ESCO skills

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
  crosswalks/pcf-esco.tsv UK GDaD PCF skills matched to ESCO skills
  sources/pcf/            UK GDaD PCF downloads
  sources/esco/           ESCO occupations and occupation skills
docs/                     generated role pages and indexes
exports/                  generated TSV files
guides/                   how-to guides
research/                 research notes on the frameworks, band mapping, and job evaluation
scripts/                  fetch, build, and analysis scripts
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

- [UK GDaD PCF](research/uk-gdad-pcf.md): structure, roles, levels, skills, grades, and licence
- [ESCO](research/esco.md): structure, version, data used, and licence
- [Framework comparison](research/framework-comparison.md): the UK GDaD PCF and ESCO compared, and the skills crosswalk
- [Band mapping](research/band-mapping.md): how bands relate to PCF levels, Civil Service grades, SFIA, and job evaluation
- [Job evaluation](research/job-evaluation.md): the 16 factors, scoring principles, and calibration
- [SFIA](research/sfia.md): levels of responsibility

## Licence and credits

Original content is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), and code under the MIT licence. See [LICENSE](LICENSE).

This reference quotes and builds on:

- the **UK Government Digital and Data Profession Capability Framework**. Contains public sector information licensed under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). © Crown copyright.
- **ESCO v1.2.1**. © European Union. Reuse is authorised under Commission Decision 2011/833/EU.

See [CREDITS.md](CREDITS.md) for full credits.
