# UK Government Digital and Data Profession Capability Framework (UK GDaD PCF)

## At a glance

| Item | Detail |
| --- | --- |
| Official name | Government Digital and Data Profession Capability Framework |
| Publisher | Government Digital Service (GDS), Department for Science, Innovation and Technology, UK Government |
| Website | <https://understand-digital-data-roles-skills.service.gov.uk/> |
| Former names and addresses | Digital, Data and Technology (DDaT) Capability Framework, at `ddat-capability-framework.service.gov.uk` (which now redirects) |
| Version used here | The website content as downloaded on 6 October 2026. The framework has no version numbers; it changes continuously and keeps a change log. |
| Licence | Open Government Licence v3.0, except where otherwise stated. © Crown copyright. |
| Downloads | `roles.csv` (every role, role level, and skill with its level), `skills.csv` (every skill with all four level definitions), `changelog.csv` (every change since 2017) |
| Local copy | [`data/sources/pcf/`](../data/sources/pcf/), refreshed by [`scripts/fetch_pcf.py`](../scripts/fetch_pcf.py) |

## History

- **March 2017**: first published as a national framework of digital, data, and technology job roles for government ([blog post](https://digitalpeople.blog.gov.uk/2017/03/30/building-the-first-national-framework-of-digital-data-and-technology-job-roles/)).
- **October 2019**: made easier to use ([blog post](https://digitalpeople.blog.gov.uk/2019/10/24/making-the-digital-data-and-technology-capability-framework-more-user-friendly/)).
- **September 2023**: redesigned ([blog post](https://digitalpeople.blog.gov.uk/2023/09/18/redesigning-the-ddat-capability-framework/)).
- **November 2023**: the "Government Digital and Data" brand launched for digital and technology specialists in government ([news story](https://www.gov.uk/government/news/digital-skills-rebrand-to-attract-top-tech-talent-to-civil-service)).
- **November 2024**: Senior Civil Service roles (the chief digital and data family) added ([blog post](https://cddo.blog.gov.uk/2024/11/07/making-leadership-more-visible-senior-civil-service-roles-are-now-on-the-digital-and-data-capability-framework/)).
- **August 2026**: the most common Civil Service grades for each role level were last reviewed. The agile coach role was published.
- **30 September 2026**: the website moved from `ddat-capability-framework.service.gov.uk` to `understand-digital-data-roles-skills.service.gov.uk`.

The change log has 288 entries, from 23 March 2017 to 30 September 2026.

## Structure

The framework has four layers:

1. **Role families**: 8 groups of related roles.
2. **Roles**: 53 roles, each with a description and typical responsibilities.
3. **Role levels**: 206 published levels across those roles. The 4 chief digital and data roles have no published levels. Examples include "junior developer" and "lead developer". Each has a description that starts "At this role level, you will:".
4. **Skills**: 186 skills. Each role level lists the skills it needs, and the proficiency level needed for each.

### Role families and roles

| Role family | Roles | Roles in the family |
| --- | --- | --- |
| Architecture | 7 | Business architect, Data architect, Enterprise architect, Network architect, Security architect, Solution architect, Technical architect |
| Chief digital and data | 4 | Chief data officer, Chief digital and information officer, Chief information security officer, Chief technology officer |
| Data | 9 | Analytics engineer, Data analyst, Data and artificial intelligence (AI) ethicist, Data engineer, Data governance manager, Data scientist, Digital evaluator, Machine learning engineer, Performance analyst |
| IT operations | 12 | Application operations engineer, Business relationship manager, Change and release manager, Command and control centre manager, End user computing engineer, IT service manager, Incident manager, Infrastructure engineer, Infrastructure operations engineer, Problem manager, Service desk manager, Service transition manager |
| Product and delivery | 7 | Agile coach, Business analyst, Delivery manager, Digital portfolio manager, Product manager, Programme delivery manager, Service owner |
| Quality assurance testing (QAT) | 3 | Quality assurance test analyst, Test engineer, Test manager |
| Software development | 3 | Development operations (DevOps) engineer, Frontend developer, Software developer |
| User-centred design | 8 | Accessibility specialist, Content designer, Content strategist, Graphic designer, Interaction designer, Service designer, Technical writer, User researcher |

The full list of role levels, with grades and the band this reference suggests for each, is in [`pcf-role-levels.tsv`](pcf-role-levels.tsv).

### Role levels

Level names vary by role, but they follow a common ladder: apprentice or trainee, associate or junior, the practitioner level (for example "developer"), senior, lead, principal, and head of. Some roles also have a "management" variant of the senior, lead, and principal levels, for people who line manage as well as practise.

### Skill proficiency levels

Every skill has four ascending levels, each defined as "You can: …":

| Level | Meaning in general |
| --- | --- |
| Awareness | Knows about the skill and can explain it; works under direction |
| Working | Applies the skill with some supervision |
| Practitioner | Applies the skill independently, and guides others |
| Expert | Leads, sets standards, and is recognised as an authority |

For example, the skill **Communicating information** is described as: *"Communication involves conveying information using the most effective medium and language for the audience."* At **Awareness** level: *"You can: listen to the needs of design and business stakeholders and interpret information; take part in discussions within a multidisciplinary team."* At **Expert** level: *"You can: mediate between people and mend relationships, communicating with stakeholders at all levels; …"*

Some skills have role-specific variants, such as "Programming and build (software engineering)" and "Programming and build (data science)". This reference treats each variant as a separate skill.

### Civil Service grades

Most role levels show the one or two Civil Service grades that the level is most often performed at. They are based on government workforce data. In the framework's words, *"The grades are not mandatory for a role level … Each organisation will decide which specific grade an individual job is performed at."* One grade means over 85% of mapped jobs use that grade. Two grades means each is used by at least 15% of jobs, and together they cover more than 85%.

The grades, from lowest to highest, are AA, AO, EO, HEO, SEO, G7, G6, and Senior Civil Service (SCS). This reference uses them to suggest a band for each PCF role level. See [`band-mapping.md`](band-mapping.md).

The download files do not include grades, so [`scripts/fetch_pcf.py`](../scripts/fetch_pcf.py) reads them from each role page. A few levels have no grade published: agile coach, the first two data and AI ethicist levels, lead digital evaluator, and the "management" variants.

### SFIA

The current framework does not publish a mapping to SFIA. This reference maps bands to SFIA levels of responsibility separately (see [`sfia.md`](sfia.md)).

## How this reference uses the UK GDaD PCF

- **Roles and levels**: where a PCF role fits, this reference uses it as the base for the role, and quotes its role and level descriptions word for word.
- **Skills**: the PCF skills and levels for each role level are included automatically, so assessments use the PCF wording. This reference adds health care skills, and defines its own skills for families the PCF does not cover: cyber security operations, clinical informatics, information governance, finance, legal, human resources, procurement, and corporate services.
- **Proficiency scale**: the four PCF levels are the scale for every skill in this reference, including skills original to it.
- **Seniority**: PCF Civil Service grades are used to suggest bands.

## What the UK GDaD PCF does not cover

- **Health and care**: there are no health-specific skills, such as clinical safety, health data interoperability, or clinical terminology.
- **Corporate functions**: finance, legal, HR, and procurement have their own government professions and frameworks, so they are outside the PCF.
- **Cyber security operations**: security analysts and engineers belong to a separate government security profession. Only security architect and chief information security officer are in the PCF.
- **Project management**: this is covered by a separate government project delivery profession, so only programme delivery manager is in the PCF.
- **Job evaluation**: the PCF does not evaluate or grade jobs. Its grades are descriptive.

---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (<https://understand-digital-data-roles-skills.service.gov.uk/>), licensed under the Open Government Licence v3.0. © Crown copyright.*
