# Tasks

See [plan.md](plan.md) for the context and reasoning.

## 0. Setup

- [x] Get answers from the owner to the open questions in plan.md (see Decisions)
- [x] Initialise the git repository and create the folder layout
- [x] Choose the licences (CC BY 4.0 for content, MIT for code) and add a `LICENSE` file
- [x] Add a `CREDITS.md` with the exact attribution wording for UK GDaD PCF and ESCO
- [x] Draft the disclaimer text (in README, on every page, and in the build)

## 1. Research: UK GDaD PCF

- [x] Confirm the framework's official current name, URL, version, and date accessed
- [x] Record changes from earlier versions of the framework
- [x] List all role families and the roles in each
- [x] List the role levels for each role, with their Civil Service grades (`research/pcf-role-levels.tsv`)
- [x] List all skills, with descriptions and level definitions (`data/sources/pcf/skills.csv`, `research/pcf-skills.tsv`)
- [x] Confirm the licence (OGL v3.0) and the attribution wording
- [x] Record any published SFIA mapping (none published)
- [x] Write `research/uk-gdad-pcf.md`, with quotations and citations

## 2. Research: ESCO

- [x] Confirm the current ESCO version (v1.2.1), URL, and date accessed, and pin the version
- [x] Summarise the data model
- [x] Document the API and the bulk downloads, and choose one (API, cached)
- [x] Confirm the licence (Commission Decision 2011/833/EU) and the attribution wording
- [x] Extract the relevant ESCO occupations, with URIs and ISCO-08 codes (92 occupations)
- [x] Extract the essential and optional skills for each of those occupations (5,378 links)
- [x] Write `research/esco.md`
- [x] Write `scripts/fetch_esco.py`

## 3. Research: framework comparison

- [x] Map each PCF role used here to one or more ESCO occupations (`data/catalogue.yaml`)
- [x] Map each PCF skill to ESCO skills, with match strength (`data/crosswalks/pcf-esco.tsv`, 470 rows, all 186 skills)
- [x] Note where each framework has a gap
- [x] Write `research/framework-comparison.md`
- [ ] Peer review the weakest crosswalk matches (listed in the comparison note)

## 4. Research: SFIA and band structure

- [x] Summarise the SFIA levels of responsibility (names only; SFIA text is licensed separately)
- [x] Define the generic Bands 1 to 9, with Band 8 sub-bands 8a to 8d
- [x] Write a competency outline for each band
- [x] Write `research/sfia.md` and `data/bands.yaml`

## 5. Research: digital health roles

- [ ] Gather 40 to 80 publicly advertised digital health job descriptions, recording title, seniority, family, key duties, and URL
- [ ] Tabulate the findings in `research/role-samples.tsv` (internal working data; no employer names in published content)
- [ ] Write `research/digital-health-roles.md`
- [ ] Review role titles, bands, and duties against the sample, and adjust

## 6. Research: job evaluation scheme

- [x] Define the 16 factors, with a one-line definition of each
- [x] Define the levels within each factor and the points for each level
- [x] Define the points range for each band
- [x] Write scoring guidance
- [x] Write `research/job-evaluation.md` (with a calibration profile for each band) and `data/job-evaluation.yaml`

## 6b. Research: band-to-level mapping

- [x] Draft a mapping from Civil Service grades (as published by the PCF) to bands, and bands to SFIA levels
- [x] Write down the reasoning in `research/band-mapping.md`
- [x] Add the mapping to `data/bands.yaml`

## 7. Data model and tooling

- [x] Define the data formats (`CONTRIBUTING.md`)
- [x] Write a validator: references, bands, PCF levels, ESCO occupations, skill levels, 16 factors, and band points ranges (`scripts/build.py --check`)
- [x] Write a generator: a page per role, plus indexes by family, band, PCF role, and ESCO occupation, and a skills catalogue
- [x] Export a TSV self-assessment file per role level (292 files)
- [x] Export TSVs of roles, role skills, and job evaluation scores
- [x] Write a team gap analysis script (`scripts/gap_analysis.py`)
- [ ] Add a link checker for cited sources

## 8. Content: skills catalogue

- [x] Use the UK GDaD PCF skills directly, with credit (160 used)
- [x] Link PCF skills to ESCO skills through the crosswalk
- [x] Add skills original to this reference, each linked to ESCO (93 skills in `data/skills/`)
- [ ] Peer review the catalogue

## 9. Content: role profiles

- [x] Software development (4 roles)
- [x] Architecture (7 roles)
- [x] Data (8 roles)
- [x] Product and delivery (7 roles)
- [x] User-centred design (5 roles)
- [x] IT operations (8 roles)
- [x] Cyber security (3 roles)
- [x] Quality assurance testing (3 roles)
- [x] Clinical informatics and clinical safety (3 roles)
- [x] Information governance (3 roles)
- [x] Finance (5 roles)
- [x] Legal (3 roles)
- [x] Human resources (5 roles)
- [x] Procurement and commercial (4 roles)
- [x] Corporate services (5 roles)
- [ ] Peer review each family by a person working in that field

## 10. Guides and README

- [x] `README.md`
- [x] `guides/self-assessment.md`
- [x] `guides/performance-review.md`
- [x] `guides/gap-analysis.md`
- [x] `guides/frameworks.md`

## 11. Validation and release

- [x] Run the validator, and fix any failures
- [x] Check that generated pages and exports carry the PCF and ESCO credits
- [ ] Usability check: can test users find a fitting role in under five minutes?
- [ ] Check the definition of done in plan.md
- [ ] Commit, publish the repository, and tag v1.0
