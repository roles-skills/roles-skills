# Integration engineer (health interoperability)

> This is an illustrative reference profile for a generic digital health care organisation. It is not an official job description for any employer, and its job evaluation scores are not a formal evaluation.

**Family:** [Software development](../../#software-development)  
**Bands:** 5, 6, 7, 8a  
**UK GDaD PCF role:** none (this reference defines the role)  
**ESCO occupations:** [integration engineer](http://data.europa.eu/esco/occupation/07e60525-1aad-4099-aaf3-2c7014c92212) (ISCO-08 2511); [database developer](http://data.europa.eu/esco/occupation/b11e1742-5e28-4270-b081-b0193d85ee7d) (ISCO-08 2521)

## Summary

Integration engineers connect the organisation's clinical and business systems so that health and care information flows safely to where it is needed. They design, build, test, and support interfaces, APIs, and message flows using standards such as HL7 FHIR and HL7 version 2, map data and clinical codes between systems, and keep integrations running in live service.

## In a digital health care organisation

- A lost, delayed, duplicated, or wrongly matched message, such as a test result or referral, can lead directly to harm, so integration work follows the clinical risk management process.
- Integrations carry large volumes of confidential health information between organisations, so every flow needs a lawful basis, secure transport, and audit.
- Health systems use many standards and versions, from HL7 version 2 messages to HL7 FHIR APIs and IHE profiles, often with local variations.
- Clinical meaning must survive the journey, so engineers map clinical terminologies such as SNOMED CT correctly and match patients reliably.
- Many integrations support care around the clock, so they need monitoring, alerting, and clear routes for resolving failed messages.

## Role levels

| Band | Title | UK GDaD PCF level | Civil Service grades | Job evaluation points |
| --- | --- | --- | --- | --- |
| 5 | [Junior integration engineer](#band-5-junior-integration-engineer) | — | — | 335 |
| 6 | [Integration engineer](#band-6-integration-engineer) | — | — | 418 |
| 7 | [Senior integration engineer](#band-7-senior-integration-engineer) | — | — | 477 |
| 8a | [Lead integration engineer](#band-8a-lead-integration-engineer) | — | — | 551 |

## Band 5: Junior integration engineer

A junior integration engineer builds, tests, and supports integrations between health and care systems, working from specifications and with guidance from more experienced engineers.

### Responsibilities

- Build and change message mappings, transformations, and API calls from agreed specifications.
- Test integrations against specifications and sample messages, including error and edge cases.
- Monitor message flows, investigate failed or rejected messages, and resolve or escalate them.
- Handle health data securely, following information governance rules for live and test data.
- Record changes and test results so they can be used as clinical safety evidence.

### Skills

| Skill | Source | Expected level | What this level means |
| --- | --- | --- | --- |
| [Systems integration](../../skills/#systems-integration) | UK GDaD PCF | Working | You can:<br>• build and test simple interfaces between systems<br>• work on more complex integration as part of a wider team |
| [Programming and build (software engineering)](../../skills/#programming-and-build-software-engineering) | UK GDaD PCF | Working | You can:<br>• design, code, test, correct and document simple programs or scripts under the direction of others |
| [Testing](../../skills/#testing) | UK GDaD PCF | Working | You can:<br>• review requirements and specifications, and define test conditions<br>• identify issues and risks associated with work<br>• analyse and report test activities and results |
| [Service support](../../skills/#service-support) | UK GDaD PCF | Working | You can:<br>• help fix service faults following agreed procedures<br>• carry out maintenance tasks on service support infrastructure |
| [Information security](../../skills/#information-security) | UK GDaD PCF | Awareness | You can:<br>• explain information security and the security controls available to protect solutions and services |
| [Health data interoperability](../../skills/#health-data-interoperability) | This reference | Working | You can:<br>• read and use FHIR resources, profiles, and APIs<br>• build or test simple integrations under guidance<br>• check messages against a specification |
| [Clinical terminology and classification](../../skills/#clinical-terminology-and-classification) | This reference | Awareness | You can:<br>• explain the difference between a clinical terminology and a classification<br>• recognise common terminologies such as SNOMED CT and ICD |
| [Information governance and data protection](../../skills/#information-governance-and-data-protection) | This reference | Working | You can:<br>• apply data protection principles to your work<br>• contribute to data protection impact assessments<br>• handle information requests and records correctly |
| [Clinical risk management](../../skills/#clinical-risk-management) | This reference | Awareness | You can:<br>• explain how health IT systems can harm patients, for example through wrong, missing, or delayed information<br>• report a possible clinical safety issue through the right route |
| [Understanding health and care services](../../skills/#understanding-health-and-care-services) | This reference | Awareness | You can:<br>• describe the main parts of the health and care system and the services the organisation supports<br>• explain why patient safety and confidentiality matter in your work |

### Typical qualifications and experience

- A degree in computing or a related subject, a completed apprenticeship, or equivalent experience.

### Band outline

- **Knowledge:** Professional or technical knowledge, typically from a degree or equivalent experience.
- **Autonomy:** Works to broad objectives within professional standards; plans own work.
- **Scope:** Own professional work within a team or product.
- **Leadership:** May guide and check the work of support staff and apprentices.
- **Accountability:** Quality of own professional work.

### Job evaluation (illustrative)

| # | Factor | Level | Points |
| --- | --- | --- | --- |
| 1 | Communication and relationship skills | 4 | 32 |
| 2 | Knowledge, training, and experience | 5 | 120 |
| 3 | Analytical and judgemental skills | 3 | 27 |
| 4 | Planning and organisational skills | 2 | 15 |
| 5 | Physical skills | 3 | 27 |
| 6 | Responsibility for patient and client care | 1 | 4 |
| 7 | Responsibility for policy and service development | 2 | 12 |
| 8 | Responsibility for financial and physical resources | 1 | 5 |
| 9 | Responsibility for people | 1 | 5 |
| 10 | Responsibility for information resources | 4 | 24 |
| 11 | Responsibility for research and development | 2 | 12 |
| 12 | Freedom to act | 3 | 21 |
| 13 | Physical effort | 2 | 7 |
| 14 | Mental effort | 3 | 12 |
| 15 | Emotional effort | 1 | 5 |
| 16 | Working conditions | 2 | 7 |
| | **Total** | | **335** (Band 5: 326–395) |

## Band 6: Integration engineer

An integration engineer designs, builds, and supports integrations between health and care systems independently, and helps define how systems should exchange data.

### Responsibilities

- Design and build integrations, APIs, and message flows using HL7 FHIR, HL7 version 2, and messaging patterns.
- Analyse source and target systems and write interface specifications and data mappings, including clinical codes.
- Build patient matching, validation, and error handling so that information reaches the right record.
- Take part in hazard workshops and build safety controls into integrations, such as alerts for failed or delayed messages.
- Work with suppliers and partner organisations to test and go live with new connections.
- Investigate and fix problems in live integrations, and mentor junior integration engineers.

### Skills

| Skill | Source | Expected level | What this level means |
| --- | --- | --- | --- |
| [Systems integration](../../skills/#systems-integration) | UK GDaD PCF | Practitioner | You can:<br>• define the integration build<br>• co-ordinate build activities across systems<br>• understand how to undertake and support integration testing activities |
| [Programming and build (software engineering)](../../skills/#programming-and-build-software-engineering) | UK GDaD PCF | Practitioner | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../skills/#systems-design) | UK GDaD PCF | Working | You can:<br>• translate logical designs into physical designs<br>• produce detailed designs<br>• effectively document all work using required standards, methods and tools, including prototyping tools where appropriate<br>• design systems characterised by managed levels of risk, manageable business and technical complexity, and meaningful impact<br>• work with well understood technology and identify appropriate patterns |
| [Service support](../../skills/#service-support) | UK GDaD PCF | Practitioner | You can:<br>• identify, locate and fix service faults |
| [Information security](../../skills/#information-security) | UK GDaD PCF | Working | You can:<br>• use information security practices and available security controls to contribute to protecting solutions and services |
| [Health data interoperability](../../skills/#health-data-interoperability) | This reference | Practitioner | You can:<br>• design and build integrations using FHIR, HL7 version 2, and messaging patterns<br>• write and profile FHIR resources and implementation guides<br>• resolve complex mapping and data quality issues between systems |
| [Clinical terminology and classification](../../skills/#clinical-terminology-and-classification) | This reference | Working | You can:<br>• find and use the right codes for a data item or form<br>• use terminology browsers and reference sets |
| [Information governance and data protection](../../skills/#information-governance-and-data-protection) | This reference | Working | You can:<br>• apply data protection principles to your work<br>• contribute to data protection impact assessments<br>• handle information requests and records correctly |
| [Clinical risk management](../../skills/#clinical-risk-management) | This reference | Working | You can:<br>• take part in hazard workshops and contribute to a hazard log<br>• follow the clinical risk management process for your work<br>• provide evidence for a clinical safety case, such as test results |
| [Understanding health and care services](../../skills/#understanding-health-and-care-services) | This reference | Working | You can:<br>• explain the clinical and care workflows your work supports<br>• use common health care terms correctly with clinical and care colleagues<br>• recognise when a change could affect patient care and raise it |

### Typical qualifications and experience

- A degree in computing or a related subject, or equivalent experience.
- Experience of building and supporting integrations between production systems.

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
| 9 | Responsibility for people | 2 | 12 |
| 10 | Responsibility for information resources | 4 | 24 |
| 11 | Responsibility for research and development | 2 | 12 |
| 12 | Freedom to act | 4 | 32 |
| 13 | Physical effort | 1 | 3 |
| 14 | Mental effort | 4 | 18 |
| 15 | Emotional effort | 1 | 5 |
| 16 | Working conditions | 2 | 7 |
| | **Total** | | **418** (Band 6: 396–465) |

## Band 7: Senior integration engineer

A senior integration engineer leads the design and delivery of complex integrations across many systems and organisations, and sets integration standards for their area.

### Responsibilities

- Lead the technical design of complex integrations, such as shared care records, results, and referrals across organisations.
- Write and maintain FHIR profiles, implementation guides, and interface standards for the organisation.
- Design integrations to be secure, resilient, and observable, with clear routes for resolving failures.
- Work with clinical safety officers to identify integration hazards and make sure controls are designed in and tested.
- Make sure each data flow has an agreed lawful basis and data sharing arrangements, working with information governance colleagues.
- Coach and develop integration engineers in the team.

### Skills

| Skill | Source | Expected level | What this level means |
| --- | --- | --- | --- |
| [Systems integration](../../skills/#systems-integration) | UK GDaD PCF | Expert | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Programming and build (software engineering)](../../skills/#programming-and-build-software-engineering) | UK GDaD PCF | Practitioner | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../skills/#systems-design) | UK GDaD PCF | Practitioner | You can:<br>• design systems characterised by medium levels of risk, impact, and business or technical complexity<br>• select appropriate design standards, methods and tools, and ensure they are applied effectively<br>• review the systems designs of others to ensure the selection of appropriate technology, efficient use of resources and integration of multiple systems and technology |
| [Information security](../../skills/#information-security) | UK GDaD PCF | Practitioner | You can:<br>• design solutions and services with security controls included, specifically engineered to mitigate security threats |
| [Stakeholder relationship management](../../skills/#stakeholder-relationship-management) | UK GDaD PCF | Working | You can:<br>• identify important stakeholders and communicate with them clearly and regularly<br>• tailor communication to stakeholders' needs and work with them to build relationships while meeting user needs<br>• build and reach consensus with stakeholders<br>• work to improve stakeholder relationships using evidence to explain decisions |
| [Health data interoperability](../../skills/#health-data-interoperability) | This reference | Practitioner | You can:<br>• design and build integrations using FHIR, HL7 version 2, and messaging patterns<br>• write and profile FHIR resources and implementation guides<br>• resolve complex mapping and data quality issues between systems |
| [Clinical terminology and classification](../../skills/#clinical-terminology-and-classification) | This reference | Practitioner | You can:<br>• design data models and reference sets using clinical terminologies<br>• map between terminologies and classifications, and explain the limits of a mapping<br>• advise teams on terminology use in products and analytics |
| [Information governance and data protection](../../skills/#information-governance-and-data-protection) | This reference | Practitioner | You can:<br>• lead data protection impact assessments and information sharing agreements<br>• advise teams on lawful basis, consent, confidentiality, and retention<br>• investigate incidents and recommend improvements |
| [Clinical risk management](../../skills/#clinical-risk-management) | This reference | Working | You can:<br>• take part in hazard workshops and contribute to a hazard log<br>• follow the clinical risk management process for your work<br>• provide evidence for a clinical safety case, such as test results |
| [Identity and access management](../../skills/#identity-and-access-management) | This reference | Working | You can:<br>• create, change, and remove user accounts and access rights<br>• check access against role-based access rules |

### Typical qualifications and experience

- Substantial experience of designing and supporting health or other complex integrations, at a level equivalent to a master's degree.

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

## Band 8a: Lead integration engineer

A lead integration engineer leads the organisation's integration engineering, sets its technical direction and standards, and assures critical integrations across many systems.

### Responsibilities

- Lead integration engineering across the organisation, setting direction, patterns, and standards.
- Assure the design of critical integrations, such as those that carry results, medicines, or alerts.
- Shape the integration platform roadmap with architects, product managers, and suppliers.
- Represent the organisation in cross-organisation interoperability and standards work.
- Line manage or lead integration engineers and grow the integration community of practice.

### Skills

| Skill | Source | Expected level | What this level means |
| --- | --- | --- | --- |
| [Systems integration](../../skills/#systems-integration) | UK GDaD PCF | Expert | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Systems design](../../skills/#systems-design) | UK GDaD PCF | Expert | You can:<br>• design systems characterised by high levels of risk, impact, and business or technical complexity<br>• control system design practice within an enterprise or industry architecture<br>• influence industry-based models for the development of new technology applications<br>• develop effective implementation and procurement strategies, consistent with business needs<br>• ensure adherence to relevant technical strategies, policies, standards and practices |
| [Technical design throughout the life cycle](../../skills/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | Practitioner | You can:<br>• create technical designs characterised by medium risk, impact, and complexity<br>• maintain appropriate quality and architectural coherence of a technical design in response to change<br>• use feedback to optimise and refine technical designs throughout the life cycle |
| [Stakeholder relationship management](../../skills/#stakeholder-relationship-management) | UK GDaD PCF | Practitioner | You can:<br>• work with the team to develop and maintain an understanding of stakeholders<br>• work with the team to develop and implement stakeholder communications strategies<br>• identify and resolve issues, influence stakeholders and manage relationships effectively<br>• build long-term strategic relationships and communicate clearly and regularly with stakeholders |
| [Leadership and guidance](../../skills/#leadership-and-guidance) | UK GDaD PCF | Practitioner | You can:<br>• make decisions characterised by medium levels of risk and complexity and recommend decisions as risk and complexity increase<br>• build consensus between services or independent stakeholders<br>• identify problems or issues in the team dynamic and rectify them<br>• engage in varying types of feedback, choosing the right type at the appropriate time and ensuring the discussion and decision stick<br>• bring people together to form a motivated team and help create the right environment for a team to work in<br>• facilitate the best team makeup depending on the situation |
| [Health data interoperability](../../skills/#health-data-interoperability) | This reference | Expert | You can:<br>• set interoperability standards and strategy for the organisation<br>• lead national or cross-organisation standards work<br>• assure the design of critical integrations across many systems |
| [Clinical terminology and classification](../../skills/#clinical-terminology-and-classification) | This reference | Practitioner | You can:<br>• design data models and reference sets using clinical terminologies<br>• map between terminologies and classifications, and explain the limits of a mapping<br>• advise teams on terminology use in products and analytics |
| [Information governance and data protection](../../skills/#information-governance-and-data-protection) | This reference | Practitioner | You can:<br>• lead data protection impact assessments and information sharing agreements<br>• advise teams on lawful basis, consent, confidentiality, and retention<br>• investigate incidents and recommend improvements |
| [Clinical risk management](../../skills/#clinical-risk-management) | This reference | Practitioner | You can:<br>• lead hazard identification and risk assessment for a product or change<br>• write and maintain hazard logs and clinical safety case reports<br>• agree risk controls with product teams and check that they work<br>• advise teams on applying clinical risk management standards |
| [People management](../../skills/#people-management) | This reference | Practitioner | You can:<br>• line manage a team, setting objectives and running appraisals<br>• support wellbeing and manage attendance, performance, and conduct<br>• plan the team's development and succession |

### Typical qualifications and experience

- Extensive experience of leading integration engineering for complex health or care systems.

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


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
