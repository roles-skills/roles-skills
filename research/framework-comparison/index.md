# Framework comparison: PCF and ESCO

This note compares the UK Government Digital and Data Profession Capability Framework (PCF) with ESCO v1.2.1 (European Skills, Competences, Qualifications and Occupations), and explains how this reference uses each one. The skill-level crosswalk between them is in [`data/crosswalks/pcf-esco.tsv`](../../data/crosswalks/pcf-esco.tsv).

## Structure

### PCF

- **Role families** group related roles, such as user-centred design, data, or IT operations. The framework has 8 families: 7 practitioner families, and the chief digital and data family of Senior Civil Service roles.
- **Roles** sit in a family, such as business analyst or security architect. The framework has 53 roles. The 4 chief digital and data roles have no published role levels.
- **Role levels** describe a career path within a role, such as junior, mid, senior, lead, and head. The framework has 206 published role levels.
- **Civil Service grades** are given for each role level, such as EO/HEO or G7/G6, which gives a pay and seniority anchor.
- **Skills** are listed for each role level. The extract has 186 distinct skills, each with a short description.
- **Proficiency levels** apply to every skill at every role level, on a 4-point scale: awareness, working, practitioner, and expert.

The PCF is written for assessing people and designing jobs. It tells you what a role level needs and how well.

### ESCO

- **Occupations** form a hierarchy under ISCO-08 (International Standard Classification of Occupations) unit groups. ESCO v1.2.1 has 3,039 occupations.
- **Skills and knowledge** form a separate vocabulary of 13,939 concepts in ESCO v1.2.1. Each concept is typed as a skill/competence or as knowledge.
- **Occupation–skill relations** link each occupation to skills marked as **essential** or **optional**.
- **Multilingual labels** give a preferred label, alternative labels, and a description in each of the ESCO languages (all official EU languages and several others).
- **Stable URIs** identify every concept, such as `http://data.europa.eu/esco/skill/...`, published as linked open data and through a public API.
- **No proficiency levels.** ESCO says that an occupation needs a skill, but not how well, and it has no seniority levels within an occupation.

ESCO is written for matching and interoperability, such as job vacancies, CVs, labour market statistics, and education. It tells you what an occupation involves, in many languages.

## How this reference uses each

| Purpose | Source |
| --- | --- |
| Role families, roles, and role levels | PCF |
| Assessed skills for each role level | PCF |
| Proficiency scale (awareness, working, practitioner, expert) | PCF |
| Civil Service grade anchors for each level | PCF |
| Occupation codes and ISCO-08 groups | ESCO |
| Skill vocabulary with stable identifiers | ESCO |
| Translations of occupation and skill labels | ESCO |
| Interoperability with job boards, CV tools, and labour market data | ESCO |

The crosswalk joins the two: a PCF skill keeps its PCF description and proficiency scale, and gains one to three ESCO skill URIs that other systems can understand.

## The crosswalk

Each PCF skill maps to one to three ESCO skills, best match first. Each mapping has a match strength:

- **exact**: the same concept.
- **close**: largely the same concept.
- **broad**: the ESCO skill is wider than the PCF skill.
- **narrow**: the ESCO skill is narrower than the PCF skill, or is one part of it.

Mappings were judged from the PCF skill description, not only its name. Where a PCF skill had no description, the judgement used its name and the roles that need it.

### Summary statistics

| Measure | Count |
| --- | --- |
| PCF skills | 186 |
| Crosswalk rows | 470 |
| Distinct ESCO skills used | 301 |
| ESCO skills used that also appear on the occupations in this reference | 257 |
| PCF skills with no reasonable ESCO match | 0 |

Rows by match strength:

| Match | Rows | PCF skills whose best match has this strength |
| --- | --- | --- |
| exact | 17 | 17 |
| close | 193 | 134 |
| broad | 33 | 13 |
| narrow | 227 | 22 |
| **Total** | **470** | **186** |

So 151 of 186 PCF skills (81%) have at least one exact or close ESCO match. The other 35 only have broad or narrow matches. Most narrow rows are there because a PCF skill bundles several activities and ESCO splits them into smaller skills, such as data preparation and linkage, which maps to data processing, data cleansing, and data integration.

The ESCO skills used most often are *Agile project management*, *identify ICT user needs*, *plan product management*, *strategic planning*, and *track key performance indicators*, each by 5 PCF skills.

### Illustrative mappings

| PCF skill | ESCO skill | Match |
| --- | --- | --- |
| Stakeholder relationship management | manage relationships with stakeholders | exact |
| Strategic thinking | apply strategic thinking | exact |
| Troubleshooting and problem resolution | perform ICT troubleshooting | exact |
| User research methods | execute ICT user research activities | exact |
| Communicating between the technical and non-technical | apply technical communication skills | exact |
| Programming and build (software engineering) | computer programming | close |
| Product and service monitoring | reconstruct program theory | close |
| Service management framework knowledge | apply operations for an ITIL-based environment | close |
| Incident management | manage major incidents | narrow |
| Data maturity | ICT process quality models | narrow |

## Gaps in each framework

### Gaps in the PCF

- **Little outside digital, data, and technology.** The PCF has almost nothing for health care practice, finance, legal, human resources, procurement, estates, or administration. ESCO covers all of these, so the reference needs ESCO (or another source) for those role families.
- **Commercial and financial skills are thin.** Skills such as commercial management and financial management exist only at a high level, with no detail on contracts, procurement law, or accounting.
- **Duplicated skills.** Several PCF skills share the same description but appear under different names for different roles, such as the three agile skills, the three strategy skills, and the role-specific variants of leadership, user focus, and communication. This is why some ESCO skills appear many times in the crosswalk.
- **Missing descriptions.** 31 of the 186 PCF skills in the extract have no description, which makes precise mapping harder.
- **Named for one government.** The PCF uses Civil Service grades and government-specific phases (discovery, alpha, beta, live), which need translation for other employers.

### Gaps in ESCO

- **No proficiency or seniority levels.** ESCO cannot say whether a role needs awareness or expert proficiency, nor tell a junior role from a head of profession. The reference uses the PCF scale for this.
- **Large optional skill lists.** Many occupations have long optional lists that mix related and loosely related skills. In this reference the occupations have 2,237 essential and 3,141 optional relations; some occupations have more than 80 optional skills.
- **Missing modern ICT practice.** ESCO has no clear skill for IT service incident management in the ITIL sense (its *handle incidents* is about accidents and theft), service design, content design, data governance as a practice, data maturity, web performance optimisation, or agile coaching. The crosswalk uses narrow or broad matches for these.
- **Missing occupations.** ESCO has no distinct occupation for service designer, user researcher, content designer, delivery manager, agile coach, product owner, service owner, or performance analyst. DevOps does exist, but only as *cloud DevOps engineer*. Data architects are covered by *database designer*, *data warehouse designer*, or *ICT system architect*.
- **Cross-domain noise.** Searches for ICT terms often return skills from unrelated industries, such as transport, mining, or the arts, so mappings need human review.

## Method

1. Candidate ESCO skills came from three places: the essential and optional skills of the ESCO occupations used in this reference, a keyword search of the ESCO API for each PCF skill name, and extra targeted searches for gaps.
2. Each PCF skill was mapped by hand, from its description, to the one to three best ESCO skills, with a match strength and an optional note.
3. Every ESCO URI in the crosswalk was checked against the ESCO v1.2.1 API, and its label was confirmed.

The crosswalk is a curated starting point, not an official mapping by either framework owner.

## Credits

Contains public sector information from the UK Government Digital and Data Profession Capability Framework, licensed under the Open Government Licence v3.0. © Crown copyright.

Contains ESCO v1.2.1 data. © European Union. Reuse authorised under Commission Decision 2011/833/EU.
