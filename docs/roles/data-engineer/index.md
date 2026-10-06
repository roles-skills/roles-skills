# Data engineer

> This is an illustrative reference profile for a generic digital health care organisation. It is not an official job description for any employer, and its job evaluation scores are not a formal evaluation.

**Family:** [Data](../../#data)  
**Bands:** 6, 7, 8a, 8b  
**UK GDaD PCF role:** [Data engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/data-engineer/)  
**ESCO occupations:** [data engineer](http://data.europa.eu/esco/occupation/2079755f-d809-49e6-8037-4de6180e54c0) (ISCO-08 2511)

## Summary

Data engineers build and run the pipelines and platforms that move health and care data from clinical and operational systems into places where it can be analysed and used safely. They design data flows, integrate sources that use different standards, and make sure data is accurate, timely, secure, and only available to the people who should see it.

## In a digital health care organisation

- Source systems include electronic patient records, laboratory, imaging, and pharmacy systems, which use standards such as HL7 version 2, HL7 FHIR, SNOMED CT, and ICD.
- Pipelines often carry identifiable patient data, so engineers build in pseudonymisation, access control, and audit from the start.
- Some data feeds support direct care, such as alerts or patient lists, so a failed or late pipeline can affect patients and needs clinical safety assessment.
- Data often needs linking across care settings, which depends on reliable patient matching and consistent identifiers.

## UK GDaD PCF role description

> A data engineer develops and constructs data products and services, and integrates them into systems and business processes.

*Quoted from the UK GDaD PCF. Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*

## Role levels

| Band | Title | UK GDaD PCF level | Civil Service grades (PCF) | Job evaluation points |
| --- | --- | --- | --- | --- |
| 6 | [Data engineer](#band-6-data-engineer) | Data engineer | HEO/SEO | 421 |
| 7 | [Senior data engineer](#band-7-senior-data-engineer) | Senior data engineer | SEO/G7 | 477 |
| 8a | [Lead data engineer](#band-8a-lead-data-engineer) | Lead data engineer | G7 | 551 |
| 8b | [Head of data engineering](#band-8b-head-of-data-engineering) | Head of data engineering | G7/G6 | 589 |

## Band 6: Data engineer

**UK GDaD PCF level: Data engineer**

> A data engineer delivers the designs set by more senior members of the data engineering community.
> 
> At this role level, you will:
> - implement data flows to connect operational systems, data for analytics and business intelligence (BI) systems
> - document source-to-target mappings
> - re-engineer manual data flows to enable scaling and repeatable use
> - support the build of data streaming systems
> - write ETL (extract, transform, load) scripts and code to ensure the ETL process performs optimally
> - develop business intelligence reports that can be reused
> - build accessible data for analysis

### Responsibilities

- Build and maintain data pipelines from clinical and operational systems to the data platform, following agreed designs.
- Map source data, including coded clinical data, to target models and document the mappings.
- Build pseudonymisation, validation, and data quality checks into pipelines.
- Monitor pipelines and fix failures, prioritising feeds that support direct care.
- Apply access controls and audit logging that meet information governance rules.

### Skills

| Skill | Source | Expected level | What this level means |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../skills/#pcf-communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Awareness | You can:<br>• explain why it's important to communicate technical concepts in non-technical language<br>• explain the types of communication that can be used with internal and external stakeholders, and their impact |
| [Data analysis and synthesis](../../skills/#pcf-data-analysis-and-synthesis) | UK GDaD PCF | Working | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data compliance and security](../../skills/#pcf-data-compliance-and-security) | UK GDaD PCF | Working | You can:<br>• use official data classification when authoring documents<br>• apply internal procedures, policies and technologies to ensure secure data handling<br>• identify and address ethical considerations when working with data<br>• address data compliance issues using internal processes |
| [Data development process](../../skills/#pcf-data-development-process) | UK GDaD PCF | Working | You can:<br>• implement simple data solutions such as data pipelines, following established approaches and standards<br>• create repeatable, reliable and reusable data solutions |
| [Data innovation](../../skills/#pcf-data-innovation) | UK GDaD PCF | Awareness | You can:<br>• develop a basic understanding of an unfamiliar or emerging technology, or a familiar technology in a new data context, with guidance<br>• share what you learn with colleagues, including how it could help deliver more value from data |
| [Data integration design](../../skills/#pcf-data-integration-design) | UK GDaD PCF | Working | You can:<br>• design simple data exchange or integration solutions using established patterns or modelling techniques<br>• include security features in your data integration designs |
| [Data modelling](../../skills/#pcf-data-modelling) | UK GDaD PCF | Working | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Metadata management](../../skills/#pcf-metadata-management) | UK GDaD PCF | Working | You can:<br>• use metadata repositories to complete complex tasks such as data and systems integration impact analysis<br>• maintain a metadata repository to ensure information remains accurate and up to date |
| [Problem management](../../skills/#pcf-problem-management) | UK GDaD PCF | Awareness | You can:<br>• investigate problems in systems, processes and services, with an understanding of the level of a problem, for example, strategic, tactical or operational<br>• contribute to the implementation of remedies and preventative measures |
| [Programming and build (data and analytics engineering)](../../skills/#pcf-programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | Working | You can:<br>• design, code, test and deploy programs or scripts following standards and good practice<br>• write readable, maintainable code<br>• use automation to improve the software development life cycle<br>• consider and adopt appropriate security measures in your solutions |
| [Understanding health and care services](../../skills/#health-care-context) | This reference | Working | You can:<br>• explain the clinical and care workflows your work supports<br>• use common health care terms correctly with clinical and care colleagues<br>• recognise when a change could affect patient care and raise it |
| [Information governance and data protection](../../skills/#information-governance) | This reference | Working | You can:<br>• apply data protection principles to your work<br>• contribute to data protection impact assessments<br>• handle information requests and records correctly |
| [Health data interoperability](../../skills/#health-data-interoperability) | This reference | Working | You can:<br>• read and use FHIR resources, profiles, and APIs<br>• build or test simple integrations under guidance<br>• check messages against a specification |
| [Clinical terminology and classification](../../skills/#clinical-terminology) | This reference | Awareness | You can:<br>• explain the difference between a clinical terminology and a classification<br>• recognise common terminologies such as SNOMED CT and ICD |
| [Pseudonymisation and disclosure control](../../skills/#data-deidentification) | This reference | Working | You can:<br>• work with pseudonymised data and apply disclosure checks before releasing outputs<br>• recognise when linked or detailed data could identify a patient |
| [Clinical risk management](../../skills/#clinical-safety) | This reference | Awareness | You can:<br>• explain how health IT systems can harm patients, for example through wrong, missing, or delayed information<br>• report a possible clinical safety issue through the right route |

### Typical qualifications and experience

- A degree in computing or a related subject, or equivalent experience.
- Experience of building data pipelines.

### Band outline

- **Knowledge:** Specialist knowledge across a range of procedures, built through further training or experience.
- **Autonomy:** Works independently; interprets policy for own area; seeks advice on complex issues.
- **Scope:** A product, service, or workstream.
- **Leadership:** May lead a small team or mentor colleagues.
- **Accountability:** Outcomes of own workstream and quality of advice given.

### Job evaluation (illustrative)

| # | Factor | Level | Points |
| --- | --- | --- | --- |
| 1 | Communication and relationship skills | 4 | 32 |
| 2 | Knowledge, training, and experience | 6 | 156 |
| 3 | Analytical and judgemental skills | 4 | 42 |
| 4 | Planning and organisational skills | 3 | 27 |
| 5 | Physical skills | 3 | 27 |
| 6 | Responsibility for patient and client care | 1 | 4 |
| 7 | Responsibility for policy and service development | 2 | 12 |
| 8 | Responsibility for financial and physical resources | 1 | 5 |
| 9 | Responsibility for people | 1 | 5 |
| 10 | Responsibility for information resources | 5 | 34 |
| 11 | Responsibility for research and development | 2 | 12 |
| 12 | Freedom to act | 4 | 32 |
| 13 | Physical effort | 1 | 3 |
| 14 | Mental effort | 4 | 18 |
| 15 | Emotional effort | 1 | 5 |
| 16 | Working conditions | 2 | 7 |
| | **Total** | | **421** (Band 6: 396–465) |

## Band 7: Senior data engineer

**UK GDaD PCF level: Senior data engineer**

> A senior data engineer designs and leads the implementation of data flows to connect operational systems, data for analytics and business intelligence (BI) systems.
> 
> At this role level, you will:
> - recognise opportunities to reuse existing data flows
> - lead the build of data streaming systems
> - optimise the code to ensure processes perform optimally
> - lead work on database management

### Responsibilities

- Design data flows and streaming services that bring together data from many health and care systems.
- Design patient matching and linkage processes, and measure how well they work.
- Lead database and platform performance work so data is available when services need it.
- Assess the clinical safety and information governance risks of data flows with the relevant specialists.
- Review the work of other engineers and coach them.

### Skills

| Skill | Source | Expected level | What this level means |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../skills/#pcf-communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Working | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Data analysis and synthesis](../../skills/#pcf-data-analysis-and-synthesis) | UK GDaD PCF | Working | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data compliance and security](../../skills/#pcf-data-compliance-and-security) | UK GDaD PCF | Practitioner | You can:<br>• consistently apply data ethics, legislation, internal procedures, policies and technologies to ensure secure data handling<br>• help ensure your team remain compliant by identifying and addressing current and potential data compliance and ethical issues<br>• guide and support others in addressing data compliance issues |
| [Data development process](../../skills/#pcf-data-development-process) | UK GDaD PCF | Practitioner | You can:<br>• lead the implementation of complex or large-scale data solutions<br>• apply appropriate technology and techniques to ensure data solutions are secure and scalable<br>• identify and implement continuous improvement to the operation and performance of data solutions |
| [Data innovation](../../skills/#pcf-data-innovation) | UK GDaD PCF | Working | You can:<br>• experiment with unfamiliar and emerging technologies, or familiar technologies in new data contexts, with guidance<br>• share what you learn with the team, explaining potential benefits, risks, and practical considerations<br>• identify opportunities to apply technology to improve data processes or outcomes in an operational setting or the wider organisation |
| [Data integration design](../../skills/#pcf-data-integration-design) | UK GDaD PCF | Practitioner | You can:<br>• select the most appropriate techniques for different integration scenarios<br>• evaluate and lead the implementation of integration using varied approaches that ensure security, efficiency and compliance |
| [Data modelling](../../skills/#pcf-data-modelling) | UK GDaD PCF | Practitioner | You can:<br>• produce relevant data models across multiple subject areas<br>• explain which models to use for which purpose<br>• understand industry-recognised data modelling patterns and standards, and when to apply them<br>• compare and align different data models |
| [Metadata management](../../skills/#pcf-metadata-management) | UK GDaD PCF | Practitioner | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../skills/#pcf-problem-management) | UK GDaD PCF | Working | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Programming and build (data and analytics engineering)](../../skills/#pcf-programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | Practitioner | You can:<br>• lead the design, code, testing and deployment of secure, resilient and maintainable solutions<br>• continuously improve the codebase and reliability of solutions<br>• create automation to improve the software development life cycle<br>• work with others to implement standards and good practice to ensure security, testability and maintainability of solutions |
| [Understanding health and care services](../../skills/#health-care-context) | This reference | Working | You can:<br>• explain the clinical and care workflows your work supports<br>• use common health care terms correctly with clinical and care colleagues<br>• recognise when a change could affect patient care and raise it |
| [Information governance and data protection](../../skills/#information-governance) | This reference | Practitioner | You can:<br>• lead data protection impact assessments and information sharing agreements<br>• advise teams on lawful basis, consent, confidentiality, and retention<br>• investigate incidents and recommend improvements |
| [Health data interoperability](../../skills/#health-data-interoperability) | This reference | Practitioner | You can:<br>• design and build integrations using FHIR, HL7 version 2, and messaging patterns<br>• write and profile FHIR resources and implementation guides<br>• resolve complex mapping and data quality issues between systems |
| [Clinical terminology and classification](../../skills/#clinical-terminology) | This reference | Working | You can:<br>• find and use the right codes for a data item or form<br>• use terminology browsers and reference sets |
| [Pseudonymisation and disclosure control](../../skills/#data-deidentification) | This reference | Practitioner | You can:<br>• design pseudonymisation and linkage methods that keep identifiers separate from analysis data<br>• assess the re-identification risk of a data set or publication and choose suitable controls<br>• advise teams on safe settings, such as trusted research environments |
| [Clinical risk management](../../skills/#clinical-safety) | This reference | Working | You can:<br>• take part in hazard workshops and contribute to a hazard log<br>• follow the clinical risk management process for your work<br>• provide evidence for a clinical safety case, such as test results |

### Typical qualifications and experience

- Substantial experience of designing and building data systems, at a level equivalent to a master's degree.

### Band outline

- **Knowledge:** Highly developed specialist knowledge, typically to master's level or equivalent experience.
- **Autonomy:** Works to organisational policy; decides how results are achieved; is the expert others consult.
- **Scope:** Several products or services, or a specialist function.
- **Leadership:** Leads a team or a professional practice area.
- **Accountability:** Delivery of a service or specialist function, and its budget if held.

### Job evaluation (illustrative)

| # | Factor | Level | Points |
| --- | --- | --- | --- |
| 1 | Communication and relationship skills | 4 | 32 |
| 2 | Knowledge, training, and experience | 7 | 196 |
| 3 | Analytical and judgemental skills | 4 | 42 |
| 4 | Planning and organisational skills | 3 | 27 |
| 5 | Physical skills | 3 | 27 |
| 6 | Responsibility for patient and client care | 1 | 4 |
| 7 | Responsibility for policy and service development | 3 | 21 |
| 8 | Responsibility for financial and physical resources | 1 | 5 |
| 9 | Responsibility for people | 2 | 12 |
| 10 | Responsibility for information resources | 5 | 34 |
| 11 | Responsibility for research and development | 2 | 12 |
| 12 | Freedom to act | 4 | 32 |
| 13 | Physical effort | 1 | 3 |
| 14 | Mental effort | 4 | 18 |
| 15 | Emotional effort | 1 | 5 |
| 16 | Working conditions | 2 | 7 |
| | **Total** | | **477** (Band 7: 466–539) |

## Band 8a: Lead data engineer

**UK GDaD PCF level: Lead data engineer**

> A lead data engineer is responsible for the design and implementation of numerous complex data flows to connect operational systems, data for analytics and business intelligence (BI) systems.
> 
> At this role level, you will:
> - recognise and share opportunities to reuse existing data flows between teams
> - be responsible for the build of data-streaming systems
> - co-ordinate teams and set best practice and standards
> - apply knowledge of systems integration to your work
> - champion data engineering across government

### Responsibilities

- Lead the design and running of the organisation's data platform and its many data flows.
- Set engineering standards for pipelines, testing, security, and documentation.
- Plan data integration with health and care partners, including shared care records and regional data services.
- Make sure data flows that support direct care are resilient and have clinical safety cases.
- Coordinate data engineering teams and line manage engineers.

### Skills

| Skill | Source | Expected level | What this level means |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../skills/#pcf-communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Practitioner | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Data analysis and synthesis](../../skills/#pcf-data-analysis-and-synthesis) | UK GDaD PCF | Practitioner | You can:<br>• understand and help teams to apply a range of techniques for data profiling<br>• source system analysis from a complex single source<br>• bring multiple data sources together in a conformed model for analysis |
| [Data compliance and security](../../skills/#pcf-data-compliance-and-security) | UK GDaD PCF | Expert | You can:<br>• advise senior stakeholders on data security, ethical or procedural risks<br>• improve organisational awareness of data compliance and procedures<br>• lead, guide and mentor teams in implementing secure data practices and maintaining compliance |
| [Data development process](../../skills/#pcf-data-development-process) | UK GDaD PCF | Expert | You can:<br>• establish cross-organisational data solutions that include all aspects of the data development life cycle<br>• define and promote good practices for creating repeatable, reliable and reusable data solutions |
| [Data innovation](../../skills/#pcf-data-innovation) | UK GDaD PCF | Practitioner | You can:<br>• test and evaluate the feasibility of unfamiliar and emerging technologies, or familiar technologies in new data contexts<br>• share what you learn with the organisation, explaining potential benefits, risks, and practical considerations<br>• recommend, design and implement innovative data solutions based on organisation objectives, user needs, and operational constraints |
| [Data integration design](../../skills/#pcf-data-integration-design) | UK GDaD PCF | Expert | You can:<br>• establish cross-organisational data integration standards and design patterns<br>• guide teams in designing secure and interoperable systems and services |
| [Data modelling](../../skills/#pcf-data-modelling) | UK GDaD PCF | Expert | You can:<br>• understand the concepts and principles of data modelling and can produce relevant data models<br>• work across government and industry, recognising opportunities for the reuse and alignment of data models in different organisations<br>• design the method to categorise data models within an organisation |
| [Metadata management](../../skills/#pcf-metadata-management) | UK GDaD PCF | Practitioner | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../skills/#pcf-problem-management) | UK GDaD PCF | Practitioner | You can:<br>• ensure that the right actions are taken to investigate, resolve and anticipate problems<br>• co-ordinate the team to investigate problems, implement solutions and take preventive measures |
| [Programming and build (data and analytics engineering)](../../skills/#pcf-programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | Practitioner | You can:<br>• lead the design, code, testing and deployment of secure, resilient and maintainable solutions<br>• continuously improve the codebase and reliability of solutions<br>• create automation to improve the software development life cycle<br>• work with others to implement standards and good practice to ensure security, testability and maintainability of solutions |
| [Understanding health and care services](../../skills/#health-care-context) | This reference | Practitioner | You can:<br>• analyse how a service fits into care pathways across organisations<br>• work with clinicians, care staff, and patients to shape digital services<br>• explain the effect of digital decisions on care, safety, and staff workload |
| [Information governance and data protection](../../skills/#information-governance) | This reference | Practitioner | You can:<br>• lead data protection impact assessments and information sharing agreements<br>• advise teams on lawful basis, consent, confidentiality, and retention<br>• investigate incidents and recommend improvements |
| [Health data interoperability](../../skills/#health-data-interoperability) | This reference | Practitioner | You can:<br>• design and build integrations using FHIR, HL7 version 2, and messaging patterns<br>• write and profile FHIR resources and implementation guides<br>• resolve complex mapping and data quality issues between systems |
| [Clinical terminology and classification](../../skills/#clinical-terminology) | This reference | Working | You can:<br>• find and use the right codes for a data item or form<br>• use terminology browsers and reference sets |
| [Pseudonymisation and disclosure control](../../skills/#data-deidentification) | This reference | Practitioner | You can:<br>• design pseudonymisation and linkage methods that keep identifiers separate from analysis data<br>• assess the re-identification risk of a data set or publication and choose suitable controls<br>• advise teams on safe settings, such as trusted research environments |
| [Clinical risk management](../../skills/#clinical-safety) | This reference | Working | You can:<br>• take part in hazard workshops and contribute to a hazard log<br>• follow the clinical risk management process for your work<br>• provide evidence for a clinical safety case, such as test results |
| [People management](../../skills/#people-management) | This reference | Practitioner | You can:<br>• line manage a team, setting objectives and running appraisals<br>• support wellbeing and manage attendance, performance, and conduct<br>• plan the team's development and succession |

### Typical qualifications and experience

- Extensive experience of leading data engineering for complex systems.

### Band outline

- **Knowledge:** Expert knowledge of a discipline and its management.
- **Autonomy:** Interprets organisational policy for a service; sets the team's direction.
- **Scope:** A service area or a discipline across the organisation.
- **Leadership:** Manages a team, or leads a discipline without line management.
- **Accountability:** A service area, its staff, and its budget.

### Job evaluation (illustrative)

| # | Factor | Level | Points |
| --- | --- | --- | --- |
| 1 | Communication and relationship skills | 5 | 45 |
| 2 | Knowledge, training, and experience | 7 | 196 |
| 3 | Analytical and judgemental skills | 5 | 60 |
| 4 | Planning and organisational skills | 4 | 42 |
| 5 | Physical skills | 2 | 15 |
| 6 | Responsibility for patient and client care | 1 | 4 |
| 7 | Responsibility for policy and service development | 4 | 32 |
| 8 | Responsibility for financial and physical resources | 2 | 12 |
| 9 | Responsibility for people | 3 | 21 |
| 10 | Responsibility for information resources | 5 | 34 |
| 11 | Responsibility for research and development | 2 | 12 |
| 12 | Freedom to act | 5 | 45 |
| 13 | Physical effort | 1 | 3 |
| 14 | Mental effort | 4 | 18 |
| 15 | Emotional effort | 1 | 5 |
| 16 | Working conditions | 2 | 7 |
| | **Total** | | **551** (Band 8a: 540–584) |

## Band 8b: Head of data engineering

**UK GDaD PCF level: Head of data engineering**

> A head of data engineering leads multi-functional delivery teams to deliver robust data services for their department, other government departments and private sector partners.
> 
> At this role level, you will:
> - inspire best practice for data products and services within your teams
> - build data engineering capability by providing technical leadership and career development for the community
> - work with other senior team members to identify, plan, develop and deliver data services

### Responsibilities

- Set the strategy for the organisation's data platforms and data engineering services.
- Lead multidisciplinary teams that deliver data services for internal teams and health and care partners.
- Advise senior leaders on data platform risks, costs, and investment.
- Make sure data services meet information governance, security, and clinical safety requirements.
- Build data engineering capability through recruitment, development, and career paths.

### Skills

| Skill | Source | Expected level | What this level means |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../skills/#pcf-communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Expert | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Data analysis and synthesis](../../skills/#pcf-data-analysis-and-synthesis) | UK GDaD PCF | Practitioner | You can:<br>• understand and help teams to apply a range of techniques for data profiling<br>• source system analysis from a complex single source<br>• bring multiple data sources together in a conformed model for analysis |
| [Data compliance and security](../../skills/#pcf-data-compliance-and-security) | UK GDaD PCF | Expert | You can:<br>• advise senior stakeholders on data security, ethical or procedural risks<br>• improve organisational awareness of data compliance and procedures<br>• lead, guide and mentor teams in implementing secure data practices and maintaining compliance |
| [Data development process](../../skills/#pcf-data-development-process) | UK GDaD PCF | Expert | You can:<br>• establish cross-organisational data solutions that include all aspects of the data development life cycle<br>• define and promote good practices for creating repeatable, reliable and reusable data solutions |
| [Data innovation](../../skills/#pcf-data-innovation) | UK GDaD PCF | Expert | You can:<br>• advocate for adoption of unfamiliar and emerging technologies, or familiar technologies in new data contexts, ensuring organisation objectives, user needs, and operational constraints inform decisions<br>• develop organisational capability in data innovation through leadership<br>• anticipate future technology changes and advise how to take advantage of them to realise value from data |
| [Data integration design](../../skills/#pcf-data-integration-design) | UK GDaD PCF | Expert | You can:<br>• establish cross-organisational data integration standards and design patterns<br>• guide teams in designing secure and interoperable systems and services |
| [Data modelling](../../skills/#pcf-data-modelling) | UK GDaD PCF | Working | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Metadata management](../../skills/#pcf-metadata-management) | UK GDaD PCF | Expert | You can:<br>• identify how metadata repositories can support different areas of the organisation<br>• communicate the value of metadata repositories<br>• set up robust governance processes to keep repositories up to date |
| [Problem management](../../skills/#pcf-problem-management) | UK GDaD PCF | Expert | You can:<br>• anticipate problems and defend against them at the right time<br>• understand how a problem fits into the larger picture<br>• identify and describe problems, and help others to describe them<br>• build problem-solving capabilities in others |
| [Programming and build (data and analytics engineering)](../../skills/#pcf-programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | Expert | You can:<br>• set standards for programming tools and techniques<br>• select appropriate development methods for a problem<br>• advise on the application of standards and methods that ensure security, maintainability and compliance<br>• take technical responsibility for all stages of a software development project, providing technical advice and guidance to stakeholders |
| [Understanding health and care services](../../skills/#health-care-context) | This reference | Practitioner | You can:<br>• analyse how a service fits into care pathways across organisations<br>• work with clinicians, care staff, and patients to shape digital services<br>• explain the effect of digital decisions on care, safety, and staff workload |
| [Information governance and data protection](../../skills/#information-governance) | This reference | Practitioner | You can:<br>• lead data protection impact assessments and information sharing agreements<br>• advise teams on lawful basis, consent, confidentiality, and retention<br>• investigate incidents and recommend improvements |
| [Health data interoperability](../../skills/#health-data-interoperability) | This reference | Expert | You can:<br>• set interoperability standards and strategy for the organisation<br>• lead national or cross-organisation standards work<br>• assure the design of critical integrations across many systems |
| [Pseudonymisation and disclosure control](../../skills/#data-deidentification) | This reference | Practitioner | You can:<br>• design pseudonymisation and linkage methods that keep identifiers separate from analysis data<br>• assess the re-identification risk of a data set or publication and choose suitable controls<br>• advise teams on safe settings, such as trusted research environments |
| [Clinical risk management](../../skills/#clinical-safety) | This reference | Working | You can:<br>• take part in hazard workshops and contribute to a hazard log<br>• follow the clinical risk management process for your work<br>• provide evidence for a clinical safety case, such as test results |
| [People management](../../skills/#people-management) | This reference | Practitioner | You can:<br>• line manage a team, setting objectives and running appraisals<br>• support wellbeing and manage attendance, performance, and conduct<br>• plan the team's development and succession |
| [Budget management](../../skills/#budget-management) | This reference | Practitioner | You can:<br>• hold and manage a budget, forecasting and explaining variances<br>• build a business case with costs and benefits |

### Typical qualifications and experience

- Extensive experience of leading data engineering across multiple teams.

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
| 2 | Knowledge, training, and experience | 7 | 196 |
| 3 | Analytical and judgemental skills | 5 | 60 |
| 4 | Planning and organisational skills | 5 | 60 |
| 5 | Physical skills | 2 | 15 |
| 6 | Responsibility for patient and client care | 1 | 4 |
| 7 | Responsibility for policy and service development | 4 | 32 |
| 8 | Responsibility for financial and physical resources | 3 | 21 |
| 9 | Responsibility for people | 4 | 32 |
| 10 | Responsibility for information resources | 5 | 34 |
| 11 | Responsibility for research and development | 2 | 12 |
| 12 | Freedom to act | 5 | 45 |
| 13 | Physical effort | 1 | 3 |
| 14 | Mental effort | 4 | 18 |
| 15 | Emotional effort | 1 | 5 |
| 16 | Working conditions | 2 | 7 |
| | **Total** | | **589** (Band 8b: 585–629) |

## ESCO occupations and skills

### data engineer

- **URI:** <http://data.europa.eu/esco/occupation/2079755f-d809-49e6-8037-4de6180e54c0>
- **ESCO code:** 2511.20  ·  **ISCO-08:** 2511 Systems analysts
- **Alternative labels:** research data engineer; data engineer expert

> Data engineers develop the architecture needed to process, manage, and store large amounts of data which will be used by data scientists for analysis. They design the infrastructure and maintain data pipelines and warehouses to leverage data for strategic advantage.

<details><summary>Essential skills and knowledge (23)</summary>

**Skills and competences:** [create data sets](http://data.europa.eu/esco/skill/906323f4-00c4-4c3b-ab5a-8af77be3456e), [design database in the cloud](http://data.europa.eu/esco/skill/7e796b51-49d7-4e73-95af-2e7323763f15), [develop data processing applications](http://data.europa.eu/esco/skill/f9670490-8aa4-4540-b121-d440a8294aab), [establish data processes](http://data.europa.eu/esco/skill/2daec0e6-f0c1-43e8-8178-aedba99130ec), [implement data warehousing techniques](http://data.europa.eu/esco/skill/fd6d2981-3d4a-4ce2-9741-cfc98c5b74bd), [manage ICT data architecture](http://data.europa.eu/esco/skill/4d85b881-e490-4b4c-897a-2faa4ef53956), [manage data](http://data.europa.eu/esco/skill/9ff9db9d-d14b-426e-83f3-e7449af6c79f), [manage quantitative data](http://data.europa.eu/esco/skill/57231a22-4da7-49c8-97b8-75672feadf1e), [manage research data](http://data.europa.eu/esco/skill/08b04e53-ed25-41a2-9f90-0b9cd939ba3d), [perform dimensionality reduction](http://data.europa.eu/esco/skill/3e2ab38a-4519-4bef-b762-a8bf4836a775), [process data](http://data.europa.eu/esco/skill/f2d57f41-43b4-4f5b-8100-3df5c21eda50), [store digital data and systems](http://data.europa.eu/esco/skill/611ed16b-99bf-4840-9cab-f55d1d286e0a), [use data processing techniques](http://data.europa.eu/esco/skill/1b70a55d-b8a4-49fc-96c6-15ab4cff2522), [use databases](http://data.europa.eu/esco/skill/4463a721-69f3-413d-8321-43e3af13a4f1)

**Knowledge:** [cloud technologies](http://data.europa.eu/esco/skill/bd14968e-e409-45af-b362-3495ed7b10e0), [computer science](http://data.europa.eu/esco/skill/7b5cce4d-c7fe-4119-b48f-70aa05391787), [data analytics](http://data.europa.eu/esco/skill/97bd1c21-66b2-4b7e-ad0f-e3cda590e378), [data models](http://data.europa.eu/esco/skill/fecf8a0d-62c4-4e71-9b03-0f4fc2ad7bf5), [data storage](http://data.europa.eu/esco/skill/a7f0fbe0-c546-4f30-8e41-34a58c64567e), [data warehouse](http://data.europa.eu/esco/skill/3ec2e4d6-7000-4905-bf1a-c5b1679416de), [database management systems](http://data.europa.eu/esco/skill/ab1e97ed-2319-4293-a8b7-072d2648822f), [unstructured data](http://data.europa.eu/esco/skill/c5e8abde-d2ba-4e8e-a65e-720b71180666)

**Other:** [digital data processing](http://data.europa.eu/esco/skill/629685b8-5f9e-4522-8cff-b3e2c4ec625a)

</details>

<details><summary>Optional skills and knowledge (5)</summary>

**Skills and competences:** [analyse pipeline database information](http://data.europa.eu/esco/skill/484d048c-a5d1-46a5-b57f-45b69c0ac552), [create data models](http://data.europa.eu/esco/skill/fbafa41f-cd05-4109-a649-8b44d306d779)

**Knowledge:** [SAS Data Management](http://data.europa.eu/esco/skill/e5a6e1e0-1b07-4432-83ba-77d593b2cb47), [Teradata Database](http://data.europa.eu/esco/skill/d9eaf831-9348-4330-a83e-b7c099cdc8f6), [statistics](http://data.europa.eu/esco/skill/7ee4c2ea-b349-4bd2-81a3-ec31475d4833)

</details>

---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
