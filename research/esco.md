# ESCO (European Skills, Competences, Qualifications and Occupations)

## At a glance

| Item | Detail |
| --- | --- |
| Name | ESCO: European Skills, Competences, Qualifications and Occupations |
| Publisher | European Commission |
| Website | <https://esco.ec.europa.eu/> |
| API | <https://ec.europa.eu/esco/api> (for example `/resource/occupation?uri=…&language=en&selectedVersion=v1.2.1`) |
| Version used here | **v1.2.1** (the latest dataset listed on the ESCO download page on 6 October 2026), pinned with `selectedVersion=v1.2.1` |
| Size | 3,039 occupations and 13,939 skills and knowledge concepts in v1.2.1 |
| Languages | 28 language labels for each concept: the EU languages, plus Arabic, Icelandic, Norwegian, and Ukrainian |
| Licence | Free to download, use, reproduce, and reuse for any purpose, provided the source is acknowledged, under the Commission's reuse policy (Commission Decision 2011/833/EU) |
| Local copy | [`data/sources/esco/`](../data/sources/esco/), refreshed by [`scripts/fetch_esco.py`](../scripts/fetch_esco.py) |

## Structure

ESCO has three pillars. This reference uses the first two.

1. **Occupations.** Each occupation has a preferred label, alternative labels, a description, a scope note, and a code that places it under a group in the International Standard Classification of Occupations (ISCO-08). For example, *software developer* has ESCO code 2512.4, under ISCO-08 group 2512, "Software developers".
2. **Skills and competences, and knowledge.** Each concept has a type: *skill/competence* (what someone can do, such as "debug software") or *knowledge* (what someone knows, such as "computer programming"). There are also transversal skills that apply across occupations.
3. **Qualifications.** Qualifications from national databases. This pillar is not used here.

Every concept has a stable URI, for example `http://data.europa.eu/esco/occupation/f2b15a0e-e65a-438a-affb-29b9d50b77d1`.

### Essential and optional skills

Each occupation links to skills and knowledge as either:

- **Essential**: usually needed for the occupation, whatever the employer or country.
- **Optional**: may be needed, depending on the employer, the specialism, or the country.

ESCO does **not** define proficiency levels, and it does not separate seniority. A junior and a principal software developer are both "software developer" in ESCO.

## The ESCO data used in this reference

[`data/catalogue.yaml`](../data/catalogue.yaml) links each role to one or more ESCO occupations, with the closest first. [`scripts/fetch_esco.py`](../scripts/fetch_esco.py) downloads those occupations and writes:

- [`occupations.tsv`](../data/sources/esco/occupations.tsv): 92 occupations, each with URI, label, ESCO code, ISCO-08 group, description, and alternative labels.
- [`occupation-skills.tsv`](../data/sources/esco/occupation-skills.tsv): 5,378 occupation–skill links.

| Relation | Skill/competence | Knowledge | Other | Total |
| --- | --- | --- | --- | --- |
| Essential | 1,491 | 733 | 13 | 2,237 |
| Optional | 1,265 | 1,875 | 1 | 3,141 |

These links cover 1,532 distinct ESCO skills and knowledge concepts. Each role page lists both the essential and the optional skills for each of its ESCO occupations.

## How ESCO occupations were chosen

For each role, the ESCO search API was queried with the role title and its common synonyms, and the closest occupations were chosen by comparing ESCO descriptions with the role. Where ESCO has no close occupation, the nearest wider one is used, and a second occupation is added for coverage. For example:

- **DevOps engineer** uses *cloud DevOps engineer* and *cloud engineer*.
- **Service designer** uses *user experience analyst* and *user interface designer*, because ESCO has no separate service designer occupation.
- **Clinical safety officer** uses *clinical informatics manager* and *regulatory affairs manager*.
- **Delivery manager** uses *ICT project manager*.

## How this reference uses ESCO

- **Occupation codes**: each role is linked to ESCO occupations and ISCO-08 groups, so the roles can be compared with labour market data, job adverts, and other ESCO-based tools.
- **Skill vocabulary**: skills original to this reference list their closest ESCO skills, with the strength of the match (exact, close, broad, or narrow). UK GDaD PCF skills are linked to ESCO skills in [`data/crosswalks/pcf-esco.tsv`](../data/crosswalks/pcf-esco.tsv).
- **Role pages**: each role page lists the essential and optional skills and knowledge of its ESCO occupations, as a checklist for development conversations.
- **Translation**: because each ESCO concept has labels in 28 languages, the reference can later be translated starting from ESCO's own labels.

## What ESCO does not cover

- **Proficiency levels and seniority**: these come from the UK GDaD PCF and the bands in this reference.
- **Some modern digital roles**: for example service designer, delivery manager, and site reliability engineer have no separate ESCO occupation.
- **Health care digital specialisms**: for example clinical safety officer and FHIR integration engineer have no ESCO occupation, though ESCO has related skills such as "medical informatics", "clinical coding", and "health records management".

---

*Contains ESCO v1.2.1 data (<https://esco.ec.europa.eu/>). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
