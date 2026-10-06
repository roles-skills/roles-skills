# Band mapping

This note explains how each role level in this reference is placed in a band, and how the bands line up with UK GDaD PCF role levels, Civil Service grades, SFIA levels, and job evaluation points.

Bands are indicative. A real organisation sets a job's band through its own job evaluation of the actual job.

## Three sources of evidence

Each role level's band is supported by three kinds of evidence:

1. **UK GDaD PCF Civil Service grades.** For each PCF role level, the framework publishes the one or two Civil Service grades it is most often performed at. This is real workforce data about seniority.
2. **Job evaluation points.** Each role level is scored on the 16 factors in [`data/job-evaluation.yaml`](../../data/job-evaluation.yaml), and its total must fall within the band's points range. This checks the band against what the job actually involves.
3. **SFIA level of responsibility.** Each band has a typical SFIA level (see [`sfia.md`](../sfia/)), which lets you cross-check against other frameworks.

## From Civil Service grades to bands

Civil Service grades and the bands in this reference are different scales, so there is no exact conversion. This reference uses the following rule. Where a PCF role level shows two or three grades, the rule takes the middle of the range. It then places the role level in the band that best matches the responsibility at that point.

| PCF Civil Service grades | Suggested band | Reasoning |
| --- | --- | --- |
| AA | 2 | Routine support work |
| AO | 3 | Experienced support work, following procedures |
| AO/EO | 4 | Entry and trainee levels, such as apprentices and trainees |
| EO | 4 | Entry practitioner, or experienced support |
| EO/HEO | 5 | Junior or associate practitioner |
| HEO | 5 | Practitioner working to broad objectives |
| HEO/SEO, SEO, HEO/SEO/G7 | 6 | Experienced, independent practitioner |
| SEO/G7, SEO/G7/G6 | 7 | Senior practitioner or specialist |
| G7 | 8a | Lead for a team or discipline |
| G7/G6 | 8b | Lead or principal across several teams |
| G6 | 8c | Head of a discipline or function |
| SCS1 | 8d | Deputy director level |

The rule is stored in `grade_to_band` in [`data/bands.yaml`](../../data/bands.yaml). The suggested band for every PCF role level is in [`pcf-role-levels.tsv`](../pcf-role-levels.tsv).

Role files can change a suggested band. They do so mainly when two PCF levels would otherwise fall in the same band. For example, the PCF shows G7/G6 for both lead developer and principal developer, so this reference puts lead developer at Band 8a and principal developer at Band 8b. Every change is explained in the role level's `job_evaluation_notes`.

## Roles without a PCF role

Corporate, clinical informatics, information governance, and cyber security operations roles have no PCF role, so they have no Civil Service grade evidence. Their bands rest on:

- **job evaluation scores**, starting from the typical factor profile for each band in [`job-evaluation.md`](../job-evaluation/)
- **the band competency outlines** in [`data/bands.yaml`](../../data/bands.yaml)
- **comparison with similar PCF role levels**, for example comparing a category manager with a digital portfolio manager

## Summary by band

| Band | Stage | Typical PCF role levels | Civil Service grades | SFIA level | Points |
| --- | --- | --- | --- | --- | --- |
| 2 | Support | — | AA, AO | 1 | 161–215 |
| 3 | Support | Service desk analyst | AO | 2 | 216–270 |
| 4 | Support and entry practitioner | Apprentice, trainee, associate | AO, EO | 2–3 | 271–325 |
| 5 | Practitioner | Junior, associate | EO, HEO | 3 | 326–395 |
| 6 | Experienced practitioner | Practitioner level (e.g. "developer") | HEO, SEO | 4 | 396–465 |
| 7 | Senior or specialist | Senior | SEO, G7 | 5 | 466–539 |
| 8a | Lead | Lead | G7 | 5–6 | 540–584 |
| 8b | Lead | Lead, principal | G7, G6 | 6 | 585–629 |
| 8c | Senior lead | Principal, head of | G6 | 6 | 630–674 |
| 8d | Senior lead | Head of, deputy director | G6, SCS1 | 6–7 | 675–720 |
| 9 | Head of profession or director | Chief roles, director | SCS1 | 7 | 721–765 |
