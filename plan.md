# Plan: Digital health care job roles reference

## Goal

Create a public reference of plausible job roles for a generic digital health care organisation. Each role covers its title, pay band, responsibilities, and skills. Align the roles with two public frameworks, quoting, crediting, comparing, and referencing both:

- the **UK Government Digital and Data Profession Capability Framework (GDaD PCF)**
- **ESCO** (European Skills, Competences, Qualifications and Occupations)

Every employee should be able to find a role that plausibly matches their own job, then use it for:

1. **Skills gap analysis**: compare the skills and levels the role expects with the skills and levels the employee has now.
2. **Performance review**: give the manager and the employee a shared, written statement of what the role expects at each band.
3. **Self assessment**: let the employee rate themselves against each skill, using a defined scale.

## Context

- **The organisation** is a generic digital health care body. It builds and runs digital services, data platforms, and infrastructure for clinicians, care providers, and patients. It is not modelled on any real organisation.
- **Pay bands** follow a generic structure of Bands 1 to 9. Bands 2 to 4 are support and entry roles, 5 to 6 are practitioner roles, 7 is senior or specialist roles, 8 is lead and management roles, and 9 is head-of and director-level roles. Band 8 splits into sub-bands 8a, 8b, 8c, and 8d to separate levels of lead and management responsibility. A short competency outline describes each band: knowledge, autonomy, scope of impact, leadership, and accountability.
- **Job evaluation** uses a generic 16-factor points scheme. Each role level gets a level and points for every factor, and the total points place it in a band. The factors cover communication and relationship skills; knowledge, training and experience; analytical and judgemental skills; planning and organisational skills; physical skills; responsibility for patient and client care, for policy and service development, for financial and physical resources, for people, for information resources, and for research and development; freedom to act; physical effort; mental effort; emotional effort; and working conditions. The scores are illustrative, to show why a role sits in its band. They are not a formal evaluation.
- **UK GDaD PCF** is the UK Government's public framework for digital, data, and technology jobs. It defines role families, roles, role levels, and skills. Each skill has a proficiency level (Awareness, Working, Practitioner, Expert). It is published openly, so we can quote, credit, compare, and reference it. It is the primary source for role structure, role levels, and skill proficiency.
- **ESCO** is the European Commission's multilingual classification of occupations, skills and competences, and qualifications. Each occupation has a description, alternative labels, and essential and optional skills, and links to the International Standard Classification of Occupations (ISCO-08). Every concept has a stable URI. ESCO is available through a public API and as downloadable data, in many languages. It is the primary source for occupation codes, skill vocabulary, and translations. ESCO does not define proficiency levels, so the PCF scale supplies those.
- **Related frameworks to consider**: SFIA 9 (Skills Framework for the Information Age), health informatics professional registration frameworks, and international health IT standards: HL7 FHIR, SNOMED CT, ISO 14971, IEC 62304, IEC 80001, and ISO 27001.

## How the two frameworks fit together

| Concern              | UK GDaD PCF                              | ESCO                                                          | Our reference                                                                                      |
| -------------------- | ---------------------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Role or occupation   | Role families and roles                  | Occupations, linked to ISCO-08                                | Each role links to a PCF role and one or more ESCO occupations                                     |
| Seniority            | Role levels (e.g. junior to head of), with most common Civil Service grades | None (occupations have no levels) | Bands 1 to 9, mapped to PCF role levels, Civil Service grades, and SFIA levels, and justified by 16-factor job evaluation scores |
| Skills               | Skills per role, curated and fairly few  | Large skill vocabulary, essential and optional per occupation | Skills catalogue: PCF skills, each cross-referenced to ESCO skill URIs, plus health care additions |
| Proficiency          | Awareness, Working, Practitioner, Expert | None                                                          | PCF scale used throughout                                                                          |
| Languages            | English                                  | Many languages                                                | ESCO labels make translation easier                                                                |
| Health care coverage | Little                                   | Some health and health IT occupations and skills              | Health care additions fill the gaps in both                                                        |

## Principles

- **Public sources only.** Use UK GDaD PCF, ESCO, other published frameworks and standards, and publicly advertised digital health job descriptions. Do not use internal or confidential documents.
- **Generic and illustrative.** Clearly label every role as an illustrative reference profile for a generic organisation, not the job description of any real employer. The authoritative documents remain the employee's actual job description and their organisation's grading.
- **Quote, credit, compare, reference.** Quote PCF and ESCO text where it is useful, and credit every quotation with its source, version, URL, and licence. Use the stable URI for every ESCO concept. Write a comparison of the two frameworks and show where they agree and where they differ.
- **Reuse, don't reinvent.** Use PCF skill names and level definitions, and ESCO occupation and skill labels. Only add skills of our own where both frameworks have a gap, for example clinical safety, information governance, health data standards, and working in clinical settings.
- **Machine-readable as well as human-readable.** The same data should drive both web pages and spreadsheets for gap analysis.
- **Translation-ready.** Structure the content so translations can be added later, starting from ESCO's multilingual labels. Do not translate in the first phase.

## Scope

### In scope

- The role families a digital health care organisation typically employs:
  - Software development and engineering
  - Architecture (enterprise, solution, technical, data, integration)
  - Data (data engineering, data science, analysis, information management, performance analysis)
  - Product and delivery (product manager, delivery manager, business analyst, programme and project management)
  - User-centred design (user research, service design, interaction and content design, accessibility)
  - IT operations, infrastructure, and cloud (service desk, networks, hosting, DevOps / SRE)
  - Cyber security (security operations, security architecture, assurance)
  - Quality assurance and testing
  - Clinical informatics and clinical safety (clinical safety officer, clinical informaticians)
  - Information governance and records
  - Corporate and business functions, covered as deeply as the digital families: finance, legal, human resources, procurement and commercial, PMO, communications, governance, and administration.
- Bands 2 to 9, mapped to UK GDaD PCF role levels and SFIA levels.
- For each role at each band: a summary, responsibilities, skills with an expected level for each, links to the PCF role and the ESCO occupations (with both their essential and optional skills), the band competency outline, scores against the 16 job evaluation factors, and typical qualifications and experience.
- Research summaries of UK GDaD PCF and ESCO, and a comparison of the two.
- A crosswalk from PCF skills to ESCO skills.
- Templates for self assessment and gap analysis.

### Out of scope (for now)

- Medical, nursing, and other frontline clinical roles, apart from clinical informatics roles. Executive roles.
- Formal job evaluation or band determination.
- Pay figures.
- Any HR system integration.
- Translation, beyond storing ESCO's multilingual labels.

## Approach

### Phase 1: Research

1. **UK GDaD PCF**: record its official name, current version, URL, structure, all role families and roles, role levels, skill list with proficiency definitions, licence and attribution wording, and any published SFIA mapping.
2. **ESCO**: record the current version, the data model (occupations, skills and competences, skill types, essential and optional relations, ISCO-08 links), the API and downloads, the licence and attribution wording, and the occupations and skills that relate to digital, data, and health IT.
3. **Framework comparison**: compare PCF roles with ESCO occupations, and PCF skills with ESCO skills. Record where they match, where they partly match, and where one has a gap.
4. **SFIA**: record its levels of responsibility (1 to 7) and the generic attributes of each level. These anchor the band competency outlines.
5. **Digital health roles**: gather a sample of 40 to 80 publicly advertised digital health job descriptions across families and seniority. Record each one's title, seniority, and key duties, then generalise them. Do not record employer names in the published content.
6. **Job evaluation scheme**: define the 16 factors, the levels within each factor, the points for each level, and the points range for each band.
7. **Band-to-level mapping**: draft a generic mapping from Bands 2 to 9 to PCF role levels, the Civil Service grades the PCF publishes for each role level, and SFIA levels, and write down the reasoning.

### Phase 2: Data model

Use one YAML file per role as the source of truth, listed in `data/catalogue.yaml` with its PCF role and ESCO occupations. A build script (`scripts/build.py`) validates the data and generates Markdown pages and TSV files from it.

```yaml
id: software-developer
summary: ...
health_context: [...]
levels:                          # PCF role and ESCO occupations are in data/catalogue.yaml
  - band: "5"
    pcf_level: Junior developer      # PCF level description and skills are quoted automatically
    title: Junior software developer
    responsibilities: [...]
    skills:
      - skill: clinical-safety # extra skill; PCF skills are added automatically
        level: working # awareness | working | practitioner | expert
    qualifications: [...]
    job_evaluation:                   # factor id: level; points come from data/job-evaluation.yaml
      communication: 4
      knowledge: 6
      analytical: 4
      # ... all 16 factors
sources: [...]
```

UK GDaD PCF skills are read directly from the PCF download and referred to as `pcf:<slug>`. The build includes the PCF skills for each PCF role level automatically. Skills original to this reference live in `data/skills/*.yaml`, one file per domain: shared health care skills, finance, legal, human resources, and so on. Each skill has an id, name, description, the definition of each proficiency level, and a list of matching ESCO skill URIs, each with the strength of the match (exact, close, broad, or narrow). Roles refer to skills by id, so every role uses the same skill wording. PCF skills are linked to ESCO skills through `data/crosswalks/pcf-esco.tsv`.

### Phase 3: Content

1. Write the skills catalogue: the UK GDaD PCF skills, cross-referenced to ESCO, plus the health care additions.
2. Write role profiles one family at a time, starting with the largest families in a typical digital health organisation. Expected order: software development, IT operations, data, then product and delivery.
3. For each role, check the ESCO occupation's essential skills against the role's skills, and record any essential skill that we left out and why.
4. Have a second reviewer check each family against the sample job descriptions, to confirm the titles and bands look plausible.

### Phase 4: Outputs

- `README.md`: purpose, disclaimer, how to use the reference, licences, credits, and sources.
- `research/`: notes on UK GDaD PCF, ESCO, the framework comparison, SFIA, digital health roles, and the band mapping.
- `data/`: `catalogue.yaml` (families and roles), `roles/*.yaml`, `skills/*.yaml`, `bands.yaml`, `job-evaluation.yaml`, `crosswalks/pcf-esco.tsv`, and `sources/` (downloaded PCF and ESCO data).
- `docs/`: a generated Markdown page per role, plus index pages by family, by band, by PCF role, and by ESCO occupation.
- `exports/`: a TSV self-assessment file for each role level, with columns for skill, PCF reference, ESCO reference, expected level, self rating, manager rating, gap, evidence, and development action. Also a TSV of job evaluation scores for every role level.
- `guides/`: short how-to guides for employees (self assessment), managers (performance review), and teams (gap analysis).

### Phase 5: Validation and publication

- Check that every role validates against the schema, every skill reference resolves, every ESCO URI resolves, every band and level is valid, and every role level's job evaluation total falls within its band's points range.
- Check every source link.
- Ask a few people working in digital health to try it: can they find a role that fits their job in under five minutes?
- Publish it as a public repository. Licence our original content under CC BY 4.0, and credit the UK GDaD PCF and ESCO content as their licences require.

## Self assessment and gap analysis method

- **Scale**: use the four UK GDaD PCF proficiency levels (Awareness, Working, Practitioner, Expert), shown as numbers 1 to 4, with 0 for "not yet".
- **Gap**: expected level minus assessed level. A positive gap marks a development need.
- **Evidence**: each rating should include a short example of the employee's work.
- **Roll-up**: team gap analysis adds up individual gaps per skill, giving a heatmap of skill against team.
- **Interoperability**: because each skill carries ESCO URIs, the results can be compared with training catalogues, job adverts, and other tools that use ESCO.
- **Review cycle**: fits a generic annual appraisal with a mid-year check-in. Output fields should be general enough to copy into most appraisal systems.

## Risks and mitigations

| Risk                                                  | Mitigation                                                                                                                      |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Profiles are mistaken for official job descriptions   | Put a clear disclaimer on every page and in every export; label them "reference profile"                                        |
| Band-to-PCF mapping is disputed                       | Publish the reasoning; present it as indicative; allow a range (e.g. Band 6 to 7)                                               |
| Job evaluation scores are mistaken for a formal evaluation | Label them illustrative; explain that a real evaluation scores the actual job, by a trained panel |
| PCF or ESCO content changes between versions          | Record the version and date accessed for each; pin ESCO to one version; re-check when a new version comes out                   |
| Attribution is missed or wrong                        | Put the exact credit wording for each framework in the README, on every page that quotes it, and in every export                |
| PCF and ESCO skills don't match one to one            | Record the strength of each match (exact, close, broad, narrow) rather than forcing a match                                     |
| ESCO skill lists are too long for a usable assessment | Use PCF skills as the assessment items; use ESCO for references and vocabulary, not as the checklist                            |
| Generic profiles too vague to be useful               | Ground each role in real advertised duties, then generalise them; include concrete health care examples                         |
| Too many roles to maintain                            | Begin with the core families; one data model; generated outputs                                                                 |
| Using a role for performance review feels punitive    | The guides frame it as development-first and say it is not a substitute for the employee's actual job description or objectives |

## Decisions

- The output is a repository only, with no static site.
- Keep the Band 8 sub-bands (8a to 8d).
- Exports are TSV files, not XLSX or CSV.
- Corporate roles are covered as deeply as the digital roles, for example finance, legal, human resources, and procurement.
- Each role page shows both ESCO's essential skills and its optional skills.
- Each role level carries illustrative scores against the 16 job evaluation factors.

## Definition of done (first release)

- The UK GDaD PCF and ESCO research notes are complete and cited, along with the framework comparison.
- A band to PCF/SFIA level mapping is published, with its reasoning.
- The 16-factor job evaluation scheme is defined, with levels, points, and band ranges.
- The skills catalogue is complete, with a PCF-to-ESCO crosswalk.
- At least 25 role profiles across at least 8 families, covering Bands 3 to 9, each linked to an ESCO occupation and to a PCF role where one exists, with job evaluation scores that fall within each band.
- Corporate roles (finance, legal, human resources, procurement) covered as deeply as the digital roles.
- Generated docs and self-assessment exports exist for every role.
- The README, disclaimer, licences, credits, and three how-to guides are written.
