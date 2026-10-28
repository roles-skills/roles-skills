# Data architect

> This is an illustrative reference profile for a generic digital health care organization. It is not an official job description for any employer, and its job evaluation scores are not a formal evaluation.

**Family:** [Architecture](../../#architecture)  
**Bands:** 8a, 8b, 8c  
**UK GDaD PCF role:** [Data architect](https://understand-digital-data-roles-skills.service.gov.uk/role/data-architect/)  
**ESCO occupations:** [database designer](http://data.europa.eu/esco/occupation/8d9ec84d-cf2d-4179-87bc-335cda54a427) (ISCO-08 2521); [data warehouse designer](http://data.europa.eu/esco/occupation/1562c7a3-c7d9-419d-b9b6-db26610bcf84) (ISCO-08 2521)

## Summary

Data architects design how the organization structures, stores, moves, and governs its health and care data, so that it can be used safely for direct care, service planning, and research. They design data models, data platforms, and data flows, set data standards, and make sure clinical meaning, quality, and confidentiality are kept from end to end.

## In a digital health care organization

- Health data must keep its clinical meaning, so data models use clinical terminologies such as SNOMED CT and classifications such as ICD.
- Data used for direct care and data used for planning or research have different legal bases, so architects design for separation, de-identification, and controlled access.
- Data comes from many clinical and care systems of varying quality, so architects design for data quality checks, patient matching, and lineage.
- Shared care records and data exchange depend on common models such as HL7 FHIR resources and agreed national or international datasets.
- Records must be kept for long retention periods, so designs must plan for archiving and access to historical data.

## UK GDaD PCF role description (English original)

> A data architect sets the vision for the organisation’s use of data, through data design, to ensure that data is managed properly and meets the organisation’s needs.

## Role levels

| Band | Title | UK GDaD PCF level | Civil Service grades | Job evaluation points |
| --- | --- | --- | --- | --- |
| 8a | [Data architect](#band-8a-data-architect) | Data architect | SEO/G7 | 560 |
| 8b | [Senior data architect](#band-8b-senior-data-architect) | Senior data architect | G7/G6 | 613 |
| 8c | [Chief data architect](#band-8c-chief-data-architect) | Chief data architect | G6 | 662 |

## Band 8a: Data architect

**UK GDaD PCF level: Data architect**

> A data architect designs and builds data models to fulfil the strategic data needs of the organisation, as defined by chief data architects.
> 
> At this role level, you will:
> - design, support and provide guidance for the upgrade, management, decommission and archive of data in compliance with data policy
> - provide input into data dictionaries
> - define and maintain the data technology architecture, including metadata, integration and business intelligence or data warehouse architecture

### Responsibilities

- Design logical and physical data models for clinical and operational data, using clinical terminologies where needed.
- Design data flows and data platform components, such as warehouse, lakehouse, and integration layers.
- Define metadata, data dictionary entries, and lineage for the datasets in your area.
- Design de-identification and access controls so that data is used only for its lawful purpose.
- Work with data quality and clinical coding colleagues to fix structural causes of poor data.
- Guide data engineers and analysts on data models and standards.

### Skills

| Skill | Source | Expected level | What this level means |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../skills/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Working | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Communicating data](../../skills/#communicating-data) | UK GDaD PCF | Awareness | You can:<br>• show an awareness that data needs to be aligned to the needs of the end user<br>• create basic visuals and presentations |
| [Data analysis and synthesis](../../skills/#data-analysis-and-synthesis) | UK GDaD PCF | Working | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../skills/#data-governance-data-architect) | UK GDaD PCF | Working | You can:<br>• understand what data governance is required<br>• take responsibility for the assurance of data solutions and make recommendations to ensure compliance |
| [Data innovation](../../skills/#data-innovation) | UK GDaD PCF | Awareness | You can:<br>• develop a basic understanding of an unfamiliar or emerging technology, or a familiar technology in a new data context, with guidance<br>• share what you learn with colleagues, including how it could help deliver more value from data |
| [Data modelling](../../skills/#data-modelling) | UK GDaD PCF | Working | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Data standards](../../skills/#data-standards) | UK GDaD PCF | Working | You can:<br>• use data policies, processes and standards effectively<br>• work with subject matter experts to develop standards, policies and guidance to protect data<br>• monitor compliance with policies and standards in a team and take action if needed<br>• analyse the impact if a standard is breached |
| [Metadata management](../../skills/#metadata-management) | UK GDaD PCF | Working | You can:<br>• use metadata repositories to complete complex tasks such as data and systems integration impact analysis<br>• maintain a metadata repository to ensure information remains accurate and up to date |
| [Problem management](../../skills/#problem-management) | UK GDaD PCF | Working | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Strategic thinking](../../skills/#strategic-thinking) | UK GDaD PCF | Awareness | You can:<br>• explain the strategic context of your work and why it is important<br>• support strategic planning in an administrative capacity |
| [Turning business problems into data design](../../skills/#turning-business-problems-into-data-design) | UK GDaD PCF | Working | You can:<br>• design data architecture by dealing with specific business problems and aligning it to enterprise-wide standards and principles<br>• work within the context of well understood architecture, and identify appropriate patterns |
| [Understanding health and care services](../../skills/#understanding-health-and-care-services) | This reference | Working | You can:<br>• explain the clinical and care workflows your work supports<br>• use common health care terms correctly with clinical and care colleagues<br>• recognize when a change could affect patient care and raise it |
| [Clinical terminology and classification](../../skills/#clinical-terminology-and-classification) | This reference | Working | You can:<br>• find and use the right codes for a data item or form<br>• use terminology browsers and reference sets |
| [Health data interoperability](../../skills/#health-data-interoperability) | This reference | Practitioner | You can:<br>• design and build integrations using FHIR, HL7 version 2, and messaging patterns<br>• write and profile FHIR resources and implementation guides<br>• resolve complex mapping and data quality issues between systems |
| [Information governance and data protection](../../skills/#information-governance-and-data-protection) | This reference | Practitioner | You can:<br>• lead data protection impact assessments and information sharing agreements<br>• advise teams on lawful basis, consent, confidentiality, and retention<br>• investigate incidents and recommend improvements |
| [Data quality management](../../skills/#data-quality-management) | This reference | Working | You can:<br>• run data quality checks and correct errors<br>• explain data quality reports to colleagues |

### Typical qualifications and experience

- Substantial experience of data modeling and data platform design, at a level equivalent to a master's degree.

### Band outline

- **Knowledge:** Expert knowledge of a discipline and its management.
- **Autonomy:** Interprets organizational policy for a service; sets the team's direction.
- **Scope:** A service area or a discipline across the organization.
- **Leadership:** Manages a team, or leads a discipline without line management.
- **Accountability:** A service area, its staff, and its budget.

### Job evaluation (illustrative)

| # | Factor | Level | Points |
| --- | --- | --- | --- |
| 1 | Communication and relationship skills | 5 | 45 |
| 2 | Knowledge, training, and experience | 7 | 196 |
| 3 | Analytical and judgmental skills | 5 | 60 |
| 4 | Planning and organizational skills | 4 | 42 |
| 5 | Physical skills | 2 | 15 |
| 6 | Responsibility for patient and client care | 1 | 4 |
| 7 | Responsibility for policy and service development | 4 | 32 |
| 8 | Responsibility for financial and physical resources | 2 | 12 |
| 9 | Responsibility for people | 3 | 21 |
| 10 | Responsibility for information resources | 5 | 34 |
| 11 | Responsibility for research and development | 3 | 21 |
| 12 | Freedom to act | 5 | 45 |
| 13 | Physical effort | 1 | 3 |
| 14 | Mental effort | 4 | 18 |
| 15 | Emotional effort | 1 | 5 |
| 16 | Working conditions | 2 | 7 |
| | **Total** | | **560** (Band 8a: 540–584) |

Banded above the UK GDaD PCF grade suggestion (Band 7): health-sector adverts place this role at Band 8a. Planning, policy, and freedom to act are scored above the Band 7 profile because the job designs data platforms and controls used across many services.

## Band 8b: Senior data architect

**UK GDaD PCF level: Senior data architect**

> A senior data architect delivers the vision for the organisation as set by the chief data architect.
> 
> At this role level, you will:
> - design data models and metadata systems
> - help chief data architects to interpret an organisation’s needs
> - provide oversight and advice to other data architects who are designing and producing data artefacts
> - design and support the management of data dictionaries
> - make sure that your teams are working to the standards set for the organisation by the chief data architects
> - work with technical architects to make sure that an organisation’s systems are designed in accordance with the appropriate data architecture

### Responsibilities

- Design the data architecture for a major domain, such as the shared care record or the analytics platform.
- Make sure data designs across teams follow the organization's data standards and models.
- Design how data is shared with partner organizations, including standards, controls, and data sharing agreements.
- Advise information governance and clinical safety colleagues on the data risks of new designs.
- Review and guide the work of data architects.

### Skills

| Skill | Source | Expected level | What this level means |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../skills/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Practitioner | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Communicating data](../../skills/#communicating-data) | UK GDaD PCF | Working | You can:<br>• understand the appropriate media to communicate findings<br>• shape communications for the audience |
| [Data analysis and synthesis](../../skills/#data-analysis-and-synthesis) | UK GDaD PCF | Working | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../skills/#data-governance-data-architect) | UK GDaD PCF | Practitioner | You can:<br>• evolve and define data governance<br>• take responsibility for supporting and collaborating around wider governance<br>• assure and integrate data services to meet the needs of multiple business services<br>• work proactively to ensure the organisation designs architecture that considers data |
| [Data innovation](../../skills/#data-innovation) | UK GDaD PCF | Working | You can:<br>• experiment with unfamiliar and emerging technologies, or familiar technologies in new data contexts, with guidance<br>• share what you learn with the team, explaining potential benefits, risks, and practical considerations<br>• identify opportunities to apply technology to improve data processes or outcomes in an operational setting or the wider organisation |
| [Data modelling](../../skills/#data-modelling) | UK GDaD PCF | Practitioner | You can:<br>• produce relevant data models across multiple subject areas<br>• explain which models to use for which purpose<br>• understand industry-recognised data modelling patterns and standards, and when to apply them<br>• compare and align different data models |
| [Data standards](../../skills/#data-standards) | UK GDaD PCF | Practitioner | You can:<br>• create data standards for different subjects and ensure senior leaders understand them<br>• work with subject matter experts across the organisation to introduce data standards best practice<br>• monitor compliance with policies and standards in the organisation<br>• make recommendations about how the organisation should resolve breaches of standards |
| [Metadata management](../../skills/#metadata-management) | UK GDaD PCF | Practitioner | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../skills/#problem-management) | UK GDaD PCF | Practitioner | You can:<br>• ensure that the right actions are taken to investigate, resolve and anticipate problems<br>• co-ordinate the team to investigate problems, implement solutions and take preventive measures |
| [Strategic thinking](../../skills/#strategic-thinking) | UK GDaD PCF | Working | You can:<br>• work within a strategic context and communicate how activities meet strategic goals<br>• contribute to the development of strategy and policies |
| [Turning business problems into data design](../../skills/#turning-business-problems-into-data-design) | UK GDaD PCF | Practitioner | You can:<br>• design data architecture that deals with problems spanning different business areas<br>• identify links between problems to devise common solutions<br>• work across multiple subject areas, or a single large or complicated subject area<br>• produce appropriate patterns |
| [Understanding health and care services](../../skills/#understanding-health-and-care-services) | This reference | Practitioner | You can:<br>• analyze how a service fits into care pathways across organizations<br>• work with clinicians, care staff, and patients to shape digital services<br>• explain the effect of digital decisions on care, safety, and staff workload |
| [Clinical terminology and classification](../../skills/#clinical-terminology-and-classification) | This reference | Practitioner | You can:<br>• design data models and reference sets using clinical terminologies<br>• map between terminologies and classifications, and explain the limits of a mapping<br>• advise teams on terminology use in products and analytics |
| [Health data interoperability](../../skills/#health-data-interoperability) | This reference | Practitioner | You can:<br>• design and build integrations using FHIR, HL7 version 2, and messaging patterns<br>• write and profile FHIR resources and implementation guides<br>• resolve complex mapping and data quality issues between systems |
| [Information governance and data protection](../../skills/#information-governance-and-data-protection) | This reference | Practitioner | You can:<br>• lead data protection impact assessments and information sharing agreements<br>• advise teams on lawful basis, consent, confidentiality, and retention<br>• investigate incidents and recommend improvements |
| [Data quality management](../../skills/#data-quality-management) | This reference | Practitioner | You can:<br>• define data quality rules and measures<br>• work with data providers to fix the root causes of poor quality |
| [Clinical risk management](../../skills/#clinical-risk-management) | This reference | Working | You can:<br>• take part in hazard workshops and contribute to a hazard log<br>• follow the clinical risk management process for your work<br>• provide evidence for a clinical safety case, such as test results |
| [People management](../../skills/#people-management) | This reference | Working | You can:<br>• supervise day-to-day work and give feedback<br>• take part in recruitment and induction<br>• hold regular one-to-one conversations |

### Typical qualifications and experience

- Extensive experience of data architecture for complex organizations.

### Band outline

- **Knowledge:** Expert knowledge across several disciplines or a large service.
- **Autonomy:** Shapes policy and strategy for a large area.
- **Scope:** Several services or teams, or a principal-level discipline.
- **Leadership:** Manages managers, or is the principal authority in a discipline.
- **Accountability:** Several services, their staff, and their budgets.

### Job evaluation (illustrative)

| # | Factor | Level | Points |
| --- | --- | --- | --- |
| 1 | Communication and relationship skills | 5 | 45 |
| 2 | Knowledge, training, and experience | 8 | 240 |
| 3 | Analytical and judgmental skills | 5 | 60 |
| 4 | Planning and organizational skills | 4 | 42 |
| 5 | Physical skills | 2 | 15 |
| 6 | Responsibility for patient and client care | 1 | 4 |
| 7 | Responsibility for policy and service development | 4 | 32 |
| 8 | Responsibility for financial and physical resources | 3 | 21 |
| 9 | Responsibility for people | 3 | 21 |
| 10 | Responsibility for information resources | 5 | 34 |
| 11 | Responsibility for research and development | 3 | 21 |
| 12 | Freedom to act | 5 | 45 |
| 13 | Physical effort | 1 | 3 |
| 14 | Mental effort | 4 | 18 |
| 15 | Emotional effort | 1 | 5 |
| 16 | Working conditions | 2 | 7 |
| | **Total** | | **613** (Band 8b: 585–629) |

## Band 8c: Chief data architect

**UK GDaD PCF level: Chief data architect**

> A chief data architect sets the vision for the organisation’s use of data as directed by the appropriate governance body.
> 
> At this role level, you will:
> - oversee the design of multiple data models and have a broad understanding of how each model fulfils the needs of the organisation
> - be accountable for supporting and aligning to the organisation’s data strategy
> - champion data architecture both internally and through collaborating and communicating at the most senior levels across government
> - set the standards and ways of working for the data architecture community
> - be accountable for assuring data models at the level of a project or enterprise
> - provide advice to project teams and oversee the management of the full data product life cycle
> - be responsible for ensuring that the organisation’s systems are designed in accordance with the enterprise data architecture

### Responsibilities

- Set the organization's data architecture vision and roadmap, in line with its data strategy.
- Own the organization's enterprise data model, data standards, and data dictionary.
- Advise the executive team and data governance bodies on data architecture, risks, and investment.
- Represent the organization in cross-organization data standards and interoperability work.
- Lead the data architecture practice and develop its people.

### Skills

| Skill | Source | Expected level | What this level means |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../skills/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Practitioner | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Communicating data](../../skills/#communicating-data) | UK GDaD PCF | Practitioner | You can:<br>• turn complex data into clear and well understood solutions, which can be acted upon<br>• share data communication skills with the team and organisation<br>• understand and communicate different options, taking into account risks and uncertainties |
| [Data analysis and synthesis](../../skills/#data-analysis-and-synthesis) | UK GDaD PCF | Working | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../skills/#data-governance-data-architect) | UK GDaD PCF | Expert | You can:<br>• ensure data governance supports changes to the organisational strategy<br>• align data governance with wider governance (for example, budget)<br>• assure corporate services by understanding important risks and providing mitigation through assurance mechanisms |
| [Data innovation](../../skills/#data-innovation) | UK GDaD PCF | Practitioner | You can:<br>• test and evaluate the feasibility of unfamiliar and emerging technologies, or familiar technologies in new data contexts<br>• share what you learn with the organisation, explaining potential benefits, risks, and practical considerations<br>• recommend, design and implement innovative data solutions based on organisation objectives, user needs, and operational constraints |
| [Data modelling](../../skills/#data-modelling) | UK GDaD PCF | Expert | You can:<br>• understand the concepts and principles of data modelling and can produce relevant data models<br>• work across government and industry, recognising opportunities for the reuse and alignment of data models in different organisations<br>• design the method to categorise data models within an organisation |
| [Data standards](../../skills/#data-standards) | UK GDaD PCF | Expert | You can:<br>• create data standards for the organisation<br>• advocate for, and oversee compliance with, data policies and standards<br>• decide where standards need to be set across the organisation, and how to set them in the wider context of government |
| [Metadata management](../../skills/#metadata-management) | UK GDaD PCF | Expert | You can:<br>• identify how metadata repositories can support different areas of the organisation<br>• communicate the value of metadata repositories<br>• set up robust governance processes to keep repositories up to date |
| [Problem management](../../skills/#problem-management) | UK GDaD PCF | Expert | You can:<br>• anticipate problems and defend against them at the right time<br>• understand how a problem fits into the larger picture<br>• identify and describe problems, and help others to describe them<br>• build problem-solving capabilities in others |
| [Strategic thinking](../../skills/#strategic-thinking) | UK GDaD PCF | Practitioner | You can:<br>• define strategies and policies, providing guidance to others on working in the strategic context<br>• evaluate current strategies to ensure business requirements are being met and exceeded where possible |
| [Turning business problems into data design](../../skills/#turning-business-problems-into-data-design) | UK GDaD PCF | Expert | You can:<br>• design data architecture that deals with problems across the enterprise<br>• work across all organisational subject areas and internal and external programmes |
| [Understanding health and care services](../../skills/#understanding-health-and-care-services) | This reference | Expert | You can:<br>• shape organizational strategy using a deep understanding of the health and care system<br>• represent the organization with health and care partners and leaders<br>• anticipate how policy and service changes will affect digital services and care |
| [Clinical terminology and classification](../../skills/#clinical-terminology-and-classification) | This reference | Practitioner | You can:<br>• design data models and reference sets using clinical terminologies<br>• map between terminologies and classifications, and explain the limits of a mapping<br>• advise teams on terminology use in products and analytics |
| [Health data interoperability](../../skills/#health-data-interoperability) | This reference | Expert | You can:<br>• set interoperability standards and strategy for the organization<br>• lead national or cross-organization standards work<br>• assure the design of critical integrations across many systems |
| [Information governance and data protection](../../skills/#information-governance-and-data-protection) | This reference | Expert | You can:<br>• set information governance policy and strategy<br>• advise the board on information risk and compliance<br>• represent the organization with regulators and partners |
| [Data quality management](../../skills/#data-quality-management) | This reference | Practitioner | You can:<br>• define data quality rules and measures<br>• work with data providers to fix the root causes of poor quality |
| [Clinical risk management](../../skills/#clinical-risk-management) | This reference | Practitioner | You can:<br>• lead hazard identification and risk assessment for a product or change<br>• write and maintain hazard logs and clinical safety case reports<br>• agree risk controls with product teams and check that they work<br>• advise teams on applying clinical risk management standards |
| [People management](../../skills/#people-management) | This reference | Practitioner | You can:<br>• line manage a team, setting objectives and running appraisals<br>• support wellbeing and manage attendance, performance, and conduct<br>• plan the team's development and succession |

### Typical qualifications and experience

- Extensive experience of leading data architecture across organizations.

### Band outline

- **Knowledge:** Expert knowledge, and wide organizational and sector understanding.
- **Autonomy:** Sets strategy for a function; accountable to a director.
- **Scope:** A function or department.
- **Leadership:** Leads a function through several management layers.
- **Accountability:** A function's performance, workforce, and budget.

### Job evaluation (illustrative)

| # | Factor | Level | Points |
| --- | --- | --- | --- |
| 1 | Communication and relationship skills | 6 | 60 |
| 2 | Knowledge, training, and experience | 8 | 240 |
| 3 | Analytical and judgmental skills | 5 | 60 |
| 4 | Planning and organizational skills | 5 | 60 |
| 5 | Physical skills | 2 | 15 |
| 6 | Responsibility for patient and client care | 1 | 4 |
| 7 | Responsibility for policy and service development | 5 | 45 |
| 8 | Responsibility for financial and physical resources | 3 | 21 |
| 9 | Responsibility for people | 3 | 21 |
| 10 | Responsibility for information resources | 6 | 46 |
| 11 | Responsibility for research and development | 2 | 12 |
| 12 | Freedom to act | 5 | 45 |
| 13 | Physical effort | 1 | 3 |
| 14 | Mental effort | 4 | 18 |
| 15 | Emotional effort | 1 | 5 |
| 16 | Working conditions | 2 | 7 |
| | **Total** | | **662** (Band 8c: 630–674) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
