# Contributing

This guide explains how to add or change roles and skills. All content lives in `data/`. The pages in `docs/` and the files in `exports/` are generated, so never edit them by hand.

## Workflow

1. Edit or add files in `data/roles/` or `data/skills/`.
2. Run `python3 scripts/build.py --check` and fix every error.
3. Run `python3 scripts/build.py` to regenerate `docs/` and `exports/`.

To refresh the source frameworks, run `python3 scripts/fetch_pcf.py` and `python3 scripts/fetch_esco.py`. Then run `python3 scripts/pcf_levels.py` and `python3 scripts/pcf_skills.py` to refresh the research tables.

## Documents: the directory is the slug

Every Markdown document lives in a directory named for its slug, as `<slug>/index.md`, with `README.md` beside it as a symlink to `index.md`. GitHub shows the `README.md` when you open the directory. For example, the product manager role is `docs/roles/product-manager/index.md`, and GitHub shows it at `docs/roles/product-manager/`.

- **Link to the directory, not the file**: `[Product manager](docs/roles/product-manager/)`, and `[Band 7](docs/bands/#band-7)` for a heading.
- **To add a document**, create `<slug>/index.md`, then `ln -s index.md <slug>/README.md`.
- **Generated documents** in `docs/` follow the same layout. `scripts/build.py` writes the symlinks.
- **Exceptions**: the repository's own top-level files (`README.md`, `CONTRIBUTING.md`, `CREDITS.md`, `plan.md`, `tasks.md`) stay at the root, as GitHub expects.

Run `python3 scripts/check_links.py` to check that every relative link resolves.

## Where things are

| File | What it holds |
| --- | --- |
| `data/catalogue.yaml` | Every family and role, with its UK GDaD PCF role and ESCO occupations |
| `data/roles/<role-id>.yaml` | One role: summary, health context, and its levels |
| `data/skills/*.yaml` | Skills original to this reference, with four level definitions and links to ESCO skills |
| `data/bands.yaml` | Bands, their competency outlines, and the Civil Service grade to band rule |
| `data/job-evaluation.yaml` | The 16 job evaluation factors, their levels and points, and band points ranges |
| `research/pcf-role-levels.tsv` | Every UK GDaD PCF role level with its Civil Service grades and suggested band |
| `research/pcf-skills.tsv` | Every UK GDaD PCF skill with the id to use in role files (`pcf:<slug>`) |
| `research/job-evaluation/` | Scoring principles and a typical factor profile for each band |
| `data/sources/esco/occupation-skills.tsv` | Essential and optional ESCO skills for every occupation in the catalogue, with URIs |

## Role file format

```yaml
id: software-developer            # must match the file name and catalogue.yaml
summary: >                        # 2-4 sentences, in this organisation's context
  ...
health_context:                   # 3-5 bullets: what is different about this role in digital health care
  - ...
levels:                           # lowest band first
  - pcf_level: Junior developer   # only for roles with a pcf_role; exact PCF level name
    title: Junior software developer
    band: "5"                     # "2" to "9", or 8a, 8b, 8c, 8d
    summary: ...                  # required when there is no pcf_level; optional otherwise
    responsibilities:             # 4-7 bullets, each starting with a verb
      - ...
    skills:                       # extra skills, added to the PCF skills for the pcf_level
      - {skill: clinical-safety, level: awareness}
    qualifications:               # 1-3 bullets; always allow "or equivalent experience"
      - ...
    job_evaluation: {communication: 4, knowledge: 5, analytical: 3, planning: 2, physical-skills: 3, patient-care: 1, policy: 2, financial-resources: 1, people: 1, information-resources: 4, research: 2, freedom-to-act: 3, physical-effort: 2, mental-effort: 3, emotional-effort: 1, working-conditions: 2}
    job_evaluation_notes: ...     # optional; explain any unusual factor score or band choice
sources: []                       # optional; public URLs used
```

### Skills

- **Roles with a PCF role:** the build adds the PCF skills and levels for each `pcf_level` automatically. List only the extra skills, usually the health care skills from `data/skills/shared.yaml`.
- **Roles without a PCF role:** list every skill, normally 6 to 10 per level. Reuse PCF skills where they fit (for example `pcf:stakeholder-relationship-management`, `pcf:financial-management`, `pcf:commercial-management`, `pcf:communicating-information`, `pcf:leadership-and-guidance`, `pcf:planning`). Reuse shared skills (such as `people-management`, `budget-management`, `risk-management`, and `information-governance`), and add skills of your own only where nothing fits.
- **Levels:** `awareness`, `working`, `practitioner`, or `expert`. Expected levels should generally rise with the band.

### Bands

- For PCF roles, start from `suggested_band` in `research/pcf-role-levels.tsv`. Change it only for a good reason, and explain the change in `job_evaluation_notes`.
- You may leave out PCF levels that don't fit a digital health care organisation, or the PCF's "- management" variants. You may also put two PCF levels in neighbouring bands to avoid a gap.

### Job evaluation

- Score all 16 factors for every level. Start from the typical profile for the band in `research/job-evaluation/`, then adjust factors to fit the role.
- The total must fall within the band's points range. The build fails if it doesn't.
- Score the job, not a person. Most office and digital roles score level 2 for working conditions (near-continuous screen use) and level 1 or 2 for physical effort.

## Skill file format

```yaml
skills:
  - id: finance-financial-reporting   # unique across all skill files; prefix with your domain
    name: Financial reporting
    description: One sentence on what the skill involves.
    esco:                             # closest ESCO skills, from data/sources/esco/occupation-skills.tsv
      - {uri: http://data.europa.eu/esco/skill/..., label: ..., match: close}   # exact | close | broad | narrow
    levels:
      awareness: |
        You can:
        - ...
      working: |
        You can:
        - ...
      practitioner: |
        You can:
        - ...
      expert: |
        You can:
        - ...
```

Each level has 1 to 4 bullets, each starting with a verb, and each level builds on the one below.

## Style

- Write in plain English: short sentences, active voice, and sentence case for titles.
- Keep everything generic. Do not name any real employer, health service, country, or region. The only frameworks named are the UK GDaD PCF, ESCO, SFIA, and international standards such as HL7 FHIR, SNOMED CT, ICD, ISO, and IEC.
- Use "patients", "service users", "clinicians", and "care staff", and keep the health and care context concrete.
- When you quote UK GDaD PCF or ESCO text, keep it word for word. The build credits it automatically.
