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

| Band | Title | UK GDaD PCF level | Civil Service grades (PCF) | Job evaluation points |
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
| [Systems integration](../../skills/#pcf-systems-integration) | UK GDaD PCF | Working | You can:<br>• build and test simple interfaces between systems<br>• work on more complex integration as part of a wider team |
| [Programming and build (software engineering)](../../skills/#pcf-programming-and-build-software-engineering) | UK GDaD PCF | Working | You can:<br>• design, code, test, correct and document simple programs or scripts under the direction of others |
| [Testing](../../skills/#pcf-testing) | UK GDaD PCF | Working | You can:<br>• review requirements and specifications, and define test conditions<br>• identify issues and risks associated with work<br>• analyse and report test activities and results |
| [Service support](../../skills/#pcf-service-support) | UK GDaD PCF | Working | You can:<br>• help fix service faults following agreed procedures<br>• carry out maintenance tasks on service support infrastructure |
| [Information security](../../skills/#pcf-information-security) | UK GDaD PCF | Awareness | You can:<br>• explain information security and the security controls available to protect solutions and services |
| [Health data interoperability](../../skills/#health-data-interoperability) | This reference | Working | You can:<br>• read and use FHIR resources, profiles, and APIs<br>• build or test simple integrations under guidance<br>• check messages against a specification |
| [Clinical terminology and classification](../../skills/#clinical-terminology) | This reference | Awareness | You can:<br>• explain the difference between a clinical terminology and a classification<br>• recognise common terminologies such as SNOMED CT and ICD |
| [Information governance and data protection](../../skills/#information-governance) | This reference | Working | You can:<br>• apply data protection principles to your work<br>• contribute to data protection impact assessments<br>• handle information requests and records correctly |
| [Clinical risk management](../../skills/#clinical-safety) | This reference | Awareness | You can:<br>• explain how health IT systems can harm patients, for example through wrong, missing, or delayed information<br>• report a possible clinical safety issue through the right route |
| [Understanding health and care services](../../skills/#health-care-context) | This reference | Awareness | You can:<br>• describe the main parts of the health and care system and the services the organisation supports<br>• explain why patient safety and confidentiality matter in your work |

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
| [Systems integration](../../skills/#pcf-systems-integration) | UK GDaD PCF | Practitioner | You can:<br>• define the integration build<br>• co-ordinate build activities across systems<br>• understand how to undertake and support integration testing activities |
| [Programming and build (software engineering)](../../skills/#pcf-programming-and-build-software-engineering) | UK GDaD PCF | Practitioner | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../skills/#pcf-systems-design) | UK GDaD PCF | Working | You can:<br>• translate logical designs into physical designs<br>• produce detailed designs<br>• effectively document all work using required standards, methods and tools, including prototyping tools where appropriate<br>• design systems characterised by managed levels of risk, manageable business and technical complexity, and meaningful impact<br>• work with well understood technology and identify appropriate patterns |
| [Service support](../../skills/#pcf-service-support) | UK GDaD PCF | Practitioner | You can:<br>• identify, locate and fix service faults |
| [Information security](../../skills/#pcf-information-security) | UK GDaD PCF | Working | You can:<br>• use information security practices and available security controls to contribute to protecting solutions and services |
| [Health data interoperability](../../skills/#health-data-interoperability) | This reference | Practitioner | You can:<br>• design and build integrations using FHIR, HL7 version 2, and messaging patterns<br>• write and profile FHIR resources and implementation guides<br>• resolve complex mapping and data quality issues between systems |
| [Clinical terminology and classification](../../skills/#clinical-terminology) | This reference | Working | You can:<br>• find and use the right codes for a data item or form<br>• use terminology browsers and reference sets |
| [Information governance and data protection](../../skills/#information-governance) | This reference | Working | You can:<br>• apply data protection principles to your work<br>• contribute to data protection impact assessments<br>• handle information requests and records correctly |
| [Clinical risk management](../../skills/#clinical-safety) | This reference | Working | You can:<br>• take part in hazard workshops and contribute to a hazard log<br>• follow the clinical risk management process for your work<br>• provide evidence for a clinical safety case, such as test results |
| [Understanding health and care services](../../skills/#health-care-context) | This reference | Working | You can:<br>• explain the clinical and care workflows your work supports<br>• use common health care terms correctly with clinical and care colleagues<br>• recognise when a change could affect patient care and raise it |

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
| [Systems integration](../../skills/#pcf-systems-integration) | UK GDaD PCF | Expert | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Programming and build (software engineering)](../../skills/#pcf-programming-and-build-software-engineering) | UK GDaD PCF | Practitioner | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../skills/#pcf-systems-design) | UK GDaD PCF | Practitioner | You can:<br>• design systems characterised by medium levels of risk, impact, and business or technical complexity<br>• select appropriate design standards, methods and tools, and ensure they are applied effectively<br>• review the systems designs of others to ensure the selection of appropriate technology, efficient use of resources and integration of multiple systems and technology |
| [Information security](../../skills/#pcf-information-security) | UK GDaD PCF | Practitioner | You can:<br>• design solutions and services with security controls included, specifically engineered to mitigate security threats |
| [Stakeholder relationship management](../../skills/#pcf-stakeholder-relationship-management) | UK GDaD PCF | Working | You can:<br>• identify important stakeholders and communicate with them clearly and regularly<br>• tailor communication to stakeholders' needs and work with them to build relationships while meeting user needs<br>• build and reach consensus with stakeholders<br>• work to improve stakeholder relationships using evidence to explain decisions |
| [Health data interoperability](../../skills/#health-data-interoperability) | This reference | Practitioner | You can:<br>• design and build integrations using FHIR, HL7 version 2, and messaging patterns<br>• write and profile FHIR resources and implementation guides<br>• resolve complex mapping and data quality issues between systems |
| [Clinical terminology and classification](../../skills/#clinical-terminology) | This reference | Practitioner | You can:<br>• design data models and reference sets using clinical terminologies<br>• map between terminologies and classifications, and explain the limits of a mapping<br>• advise teams on terminology use in products and analytics |
| [Information governance and data protection](../../skills/#information-governance) | This reference | Practitioner | You can:<br>• lead data protection impact assessments and information sharing agreements<br>• advise teams on lawful basis, consent, confidentiality, and retention<br>• investigate incidents and recommend improvements |
| [Clinical risk management](../../skills/#clinical-safety) | This reference | Working | You can:<br>• take part in hazard workshops and contribute to a hazard log<br>• follow the clinical risk management process for your work<br>• provide evidence for a clinical safety case, such as test results |
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
| [Systems integration](../../skills/#pcf-systems-integration) | UK GDaD PCF | Expert | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Systems design](../../skills/#pcf-systems-design) | UK GDaD PCF | Expert | You can:<br>• design systems characterised by high levels of risk, impact, and business or technical complexity<br>• control system design practice within an enterprise or industry architecture<br>• influence industry-based models for the development of new technology applications<br>• develop effective implementation and procurement strategies, consistent with business needs<br>• ensure adherence to relevant technical strategies, policies, standards and practices |
| [Technical design throughout the life cycle](../../skills/#pcf-technical-design-throughout-the-life-cycle) | UK GDaD PCF | Practitioner | You can:<br>• create technical designs characterised by medium risk, impact, and complexity<br>• maintain appropriate quality and architectural coherence of a technical design in response to change<br>• use feedback to optimise and refine technical designs throughout the life cycle |
| [Stakeholder relationship management](../../skills/#pcf-stakeholder-relationship-management) | UK GDaD PCF | Practitioner | You can:<br>• work with the team to develop and maintain an understanding of stakeholders<br>• work with the team to develop and implement stakeholder communications strategies<br>• identify and resolve issues, influence stakeholders and manage relationships effectively<br>• build long-term strategic relationships and communicate clearly and regularly with stakeholders |
| [Leadership and guidance](../../skills/#pcf-leadership-and-guidance) | UK GDaD PCF | Practitioner | You can:<br>• make decisions characterised by medium levels of risk and complexity and recommend decisions as risk and complexity increase<br>• build consensus between services or independent stakeholders<br>• identify problems or issues in the team dynamic and rectify them<br>• engage in varying types of feedback, choosing the right type at the appropriate time and ensuring the discussion and decision stick<br>• bring people together to form a motivated team and help create the right environment for a team to work in<br>• facilitate the best team makeup depending on the situation |
| [Health data interoperability](../../skills/#health-data-interoperability) | This reference | Expert | You can:<br>• set interoperability standards and strategy for the organisation<br>• lead national or cross-organisation standards work<br>• assure the design of critical integrations across many systems |
| [Clinical terminology and classification](../../skills/#clinical-terminology) | This reference | Practitioner | You can:<br>• design data models and reference sets using clinical terminologies<br>• map between terminologies and classifications, and explain the limits of a mapping<br>• advise teams on terminology use in products and analytics |
| [Information governance and data protection](../../skills/#information-governance) | This reference | Practitioner | You can:<br>• lead data protection impact assessments and information sharing agreements<br>• advise teams on lawful basis, consent, confidentiality, and retention<br>• investigate incidents and recommend improvements |
| [Clinical risk management](../../skills/#clinical-safety) | This reference | Practitioner | You can:<br>• lead hazard identification and risk assessment for a product or change<br>• write and maintain hazard logs and clinical safety case reports<br>• agree risk controls with product teams and check that they work<br>• advise teams on applying clinical risk management standards |
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

## ESCO occupations and skills

### integration engineer

- **URI:** <http://data.europa.eu/esco/occupation/07e60525-1aad-4099-aaf3-2c7014c92212>
- **ESCO code:** 2511.17  ·  **ISCO-08:** 2511 Systems analysts
- **Alternative labels:** software integration engineer; ICT integration engineers; IT integration engineer; system integration engineer

> Integration engineers develop and implement solutions which coordinate applications across the enterprise or its units and departments. They evaluate existing components or systems to determine integration requirements and ensure that the final solutions meet organisational needs. They reuse components when possible and assist management in taking decisions. They perform ICT system integration troubleshooting.

<details><summary>Essential skills and knowledge (16)</summary>

**Skills and competences:** [analyse network bandwidth requirements](http://data.europa.eu/esco/skill/da042121-959d-451b-b4d0-3bbf07c1bc67), [apply ICT system usage policies](http://data.europa.eu/esco/skill/9707091a-323b-4240-877a-5999a19286f0), [apply company policies](http://data.europa.eu/esco/skill/0a43729f-2a79-4dae-9faa-95520daae79f), [define integration strategy](http://data.europa.eu/esco/skill/a4a882a1-0263-4dd2-b29a-f0028cac2393), [define technology strategy](http://data.europa.eu/esco/skill/248894d1-42dc-474f-af6e-2da52ac0c679), [deploy ICT systems](http://data.europa.eu/esco/skill/71c2f41e-14de-4b23-82ad-5dbcd54ba5b0), [design component interfaces](http://data.europa.eu/esco/skill/f6868852-9bf6-4899-a5d6-5f9532fb877d), [integrate system components](http://data.europa.eu/esco/skill/ed8de897-adbe-4f0e-b4d2-534953e64c72), [use scripting programming](http://data.europa.eu/esco/skill/5ef0c719-5bcb-49f8-b8eb-824388225333)

**Knowledge:** [ICT communications protocols](http://data.europa.eu/esco/skill/6e4f75b4-c60f-4623-a9ba-760c8245753b), [ICT project management methodologies](http://data.europa.eu/esco/skill/bec4359e-cb92-468f-a997-8fb28e32fba9), [ICT system user requirements](http://data.europa.eu/esco/skill/ca73ac82-867a-4afa-9732-834aebe896ff), [hardware components suppliers](http://data.europa.eu/esco/skill/ed1fbdc3-1071-423c-9bb4-e3288ca6d1fe), [inter-organisational middleware system](http://data.europa.eu/esco/skill/46e93774-7c6a-4dc5-bae9-be97cc461093), [procurement of ICT network equipment](http://data.europa.eu/esco/skill/32428b21-514b-42c2-81b5-244a7804ea74), [software components suppliers](http://data.europa.eu/esco/skill/e6b8f934-7f35-4dc6-9a64-f6c43acdc00b)

</details>

<details><summary>Optional skills and knowledge (71)</summary>

**Skills and competences:** [adapt to changing situations](http://data.europa.eu/esco/skill/5592ab32-4e7a-4cda-8e64-ca36d5de8a10), [communicate with customers](http://data.europa.eu/esco/skill/0da516ee-e70e-4384-be13-f5ff80be8127), [design computer network](http://data.europa.eu/esco/skill/2164e860-7f20-48bc-b98c-5d9f8a561550), [implement a firewall](http://data.europa.eu/esco/skill/e5b5053e-0ef6-4c4e-a3f2-42f955f4322c), [implement anti-virus software](http://data.europa.eu/esco/skill/bb2b4485-2bad-402f-8517-44bf7d9afff4), [perform project management](http://data.europa.eu/esco/skill/cd5efa8c-e44d-4cbc-91c6-796018dbed68), [use an application-specific interface](http://data.europa.eu/esco/skill/04fe962b-4017-4eb7-9139-7d69b6922bc9), [use back-up and recovery tools](http://data.europa.eu/esco/skill/82de2df7-0d6c-42b1-94ac-b3e9a029e917), [utilise computer-aided software engineering tools](http://data.europa.eu/esco/skill/172020d1-e151-445b-8173-e2a5fb16fe51)

**Knowledge:** [ABAP](http://data.europa.eu/esco/skill/eb0e5615-1575-4a86-a1a2-7d39595033c5), [AJAX](http://data.europa.eu/esco/skill/b4dc6e4f-dc7d-445f-8ce2-d7b9d225e282), [APL](http://data.europa.eu/esco/skill/58d7a289-dafd-4363-833f-d1dc4140885e), [ASP.NET](http://data.europa.eu/esco/skill/56a7f561-1d55-43c9-9cd7-36a0a9bc6c50), [Agile project management](http://data.europa.eu/esco/skill/0a9acb6b-1139-4be9-b431-3a80a959f2f4), [Ansible](http://data.europa.eu/esco/skill/6f8a40d6-f9ce-43ec-a72f-d4213a53f3ed), [Apache Maven](http://data.europa.eu/esco/skill/0d168770-4d9c-4096-b048-a6577818d306), [Assembly (computer programming)](http://data.europa.eu/esco/skill/47b9bbcf-356c-4782-83a4-7f5a1b2b51a3), [C#](http://data.europa.eu/esco/skill/4c016b68-4116-468c-9dc6-42710c239e4a), [C++](http://data.europa.eu/esco/skill/b633eb55-8f1f-4ae6-ab4c-2022ffe2cb7f), [COBOL](http://data.europa.eu/esco/skill/def007fa-5fed-4a5f-91a2-b0d7e3db1be1), [Cisco](http://data.europa.eu/esco/skill/709ef32a-7435-48e2-8fa2-16e389ecab8a), [Common Lisp](http://data.europa.eu/esco/skill/0cd6dcf1-5778-42a5-b685-4d01ae4a4871), [Groovy](http://data.europa.eu/esco/skill/52cf3037-ab53-4806-85ed-7fd21ea7f6a1), [Haskell](http://data.europa.eu/esco/skill/000f1d3d-220f-4789-9c0a-cc742521fb02), [ICT debugging tools](http://data.europa.eu/esco/skill/6014921e-1d25-4039-adc2-04852d61880e), [ICT infrastructure](http://data.europa.eu/esco/skill/d0c6d77e-cb25-4770-bf77-2073fc5f7523), [ICT network routing](http://data.europa.eu/esco/skill/0da6cab1-0ee9-4391-a299-f71fbf21db56), [ICT recovery techniques](http://data.europa.eu/esco/skill/c9e96450-421d-48af-9ee6-d9c50e29afc2), [ICT system integration](http://data.europa.eu/esco/skill/6fa1c2c0-a012-4ca0-9642-e01569ba322c), [ICT system programming](http://data.europa.eu/esco/skill/b105ec9b-0857-41d6-8d07-a83e58b73d90), [Java (computer programming)](http://data.europa.eu/esco/skill/19a8293b-8e95-4de3-983f-77484079c389), [JavaScript](http://data.europa.eu/esco/skill/3cd569a2-4f88-4c1e-9995-8dce8c5e51a7), [Jenkins (tools for software configuration management)](http://data.europa.eu/esco/skill/f47a1998-0beb-43be-9f46-380aa4d183da), [Lisp](http://data.europa.eu/esco/skill/0de61385-de6d-4146-ba32-1cc1bc102220), [MATLAB](http://data.europa.eu/esco/skill/c3a03c5a-c260-4c26-9b9a-873abb396f4d), [ML (computer programming)](http://data.europa.eu/esco/skill/a4d336a6-9ffd-402a-91cc-f359716ba4e0), [Microsoft Visual C++](http://data.europa.eu/esco/skill/8369ede5-4200-4a44-be2e-bc60ef959259), [Objective-C](http://data.europa.eu/esco/skill/9973a5a2-7822-4161-99e9-95c781eb63f8), [OpenEdge Advanced Business Language](http://data.europa.eu/esco/skill/300d432b-f457-4cd3-9cb1-1858c7d14954), [PHP](http://data.europa.eu/esco/skill/4350c38d-0fe9-4ca7-bab9-40ed7f72b04f), [Pascal (computer programming)](http://data.europa.eu/esco/skill/e8b89eb6-51e8-4c3a-babb-88b2e110376b), [Perl](http://data.europa.eu/esco/skill/401eb8d8-6daa-4f8b-90ad-60afc71eb4f8), [Process-based management](http://data.europa.eu/esco/skill/d5a59ca8-2e91-472e-8571-d12ce4478679), [Prolog (computer programming)](http://data.europa.eu/esco/skill/2bde42ae-e776-41c1-9ded-b07b30bfe985), [Puppet (tools for software configuration management)](http://data.europa.eu/esco/skill/6417a4cc-6f61-4459-a114-761a7fa0279d), [Python (computer programming)](http://data.europa.eu/esco/skill/ccd0a1d9-afda-43d9-b901-96344886e14d), [R](http://data.europa.eu/esco/skill/51586df8-1c46-4b47-8583-773cb63bf00b), [Ruby (computer programming)](http://data.europa.eu/esco/skill/0ccdfe98-f845-4598-84a1-3dca66e9d9a3), [SAP R3](http://data.europa.eu/esco/skill/bb99af26-71ff-4dca-bde7-1eb1f6194426), [SAS language](http://data.europa.eu/esco/skill/04f1b938-d4d4-4cb1-a863-982af76b9d93), [STAF](http://data.europa.eu/esco/skill/69f0167e-75d9-46cf-847f-72a592880ebb), [Salt (tools for software configuration management)](http://data.europa.eu/esco/skill/c7451027-8249-405a-bb1b-342ff0f3fb3b), [Scala](http://data.europa.eu/esco/skill/ffddfc7c-a9dd-449f-9e96-882dc447c8b6), [Scratch (computer programming)](http://data.europa.eu/esco/skill/d56fc2b5-4b0a-4e7e-9bde-a33736f6ff18), [Swift (computer programming)](http://data.europa.eu/esco/skill/be80acfc-b6f2-4411-9b8d-b19d9cd2556a), [Vagrant](http://data.europa.eu/esco/skill/6b3afb82-c4ea-4f14-be54-a757fb762663), [Visual Basic](http://data.europa.eu/esco/skill/13bdd41a-2a18-441f-96db-41252c519413), [computer programming](http://data.europa.eu/esco/skill/21d2f96d-35f7-4e3f-9745-c533d2dd6e97), [embedded systems](http://data.europa.eu/esco/skill/2180bd8c-86de-4889-8165-adac902eee9d), [engineering processes](http://data.europa.eu/esco/skill/72a74f69-5cf1-43c5-99b9-62a444578919), [hardware components](http://data.europa.eu/esco/skill/4b51e76e-9e8a-455f-a289-5b48246345c4), [information architecture](http://data.europa.eu/esco/skill/1bba98a7-92b9-450b-9235-e0c905f8f3c4), [information security strategy](http://data.europa.eu/esco/skill/11eebd42-44ab-401d-8a2c-bdb9fc9beb50), [interfacing techniques](http://data.europa.eu/esco/skill/23b45aa6-a479-486d-9e6f-062cbab7c68a), [lean project management](http://data.europa.eu/esco/skill/da6393d5-a53c-4863-abc7-51f36281d74e), [model based system engineering](http://data.europa.eu/esco/skill/25df422a-bf0a-4f76-8631-d0be91cb8751), [software components libraries](http://data.europa.eu/esco/skill/484df271-bb52-49f1-8f50-f19624bf4df2), [solution deployment](http://data.europa.eu/esco/skill/1d86f05e-e9cc-40ce-99d8-2b21cc71b16b), [systems development life-cycle](http://data.europa.eu/esco/skill/09f2f811-a3fb-4de3-a70f-6420a6935575), [tools for ICT test automation](http://data.europa.eu/esco/skill/7557f0f4-b8bc-4ac0-b91e-222ab1ba744f), [tools for software configuration management](http://data.europa.eu/esco/skill/9d2e926f-53d9-41f5-98f3-19dfaa687f3f)

</details>

### database developer

- **URI:** <http://data.europa.eu/esco/occupation/b11e1742-5e28-4270-b081-b0193d85ee7d>
- **ESCO code:** 2521.3  ·  **ISCO-08:** 2521 Database designers and administrators
- **Alternative labels:** database developers; data base developer; data base developers; database development engineer; database coder; database design specialist; database programmer

> Database developers program, implement and coordinate changes to computer databases based on their expertise of database management systems.

<details><summary>Essential skills and knowledge (20)</summary>

**Skills and competences:** [apply information security policies](http://data.europa.eu/esco/skill/86d2e2ea-1ba2-4aa6-b465-8a1f9abc81b8), [balance database resources](http://data.europa.eu/esco/skill/9ba8fd27-275d-4bad-8c48-f668aa99a578), [collect customer feedback on applications](http://data.europa.eu/esco/skill/71746a0b-e58d-4dc4-ad03-bd84082eae21), [create data models](http://data.europa.eu/esco/skill/fbafa41f-cd05-4109-a649-8b44d306d779), [estimate duration of work](http://data.europa.eu/esco/skill/e207163b-7963-4c3e-9494-7a4bb000211b), [identify customer requirements](http://data.europa.eu/esco/skill/0e0c9c11-b39e-43cf-ba95-2fe646f5de64), [interpret technical texts](http://data.europa.eu/esco/skill/85c11255-469f-41bd-a6d1-382bc4a87783), [perform backups](http://data.europa.eu/esco/skill/cf3e976d-2c3e-495c-a874-f9e8a66d3b48), [report analysis results](http://data.europa.eu/esco/skill/c544a9f3-5945-4b54-afed-de0697852817), [test ICT queries](http://data.europa.eu/esco/skill/e2fb1ee4-fbf9-4690-b677-3e6ff7cfdc48), [use an application-specific interface](http://data.europa.eu/esco/skill/04fe962b-4017-4eb7-9139-7d69b6922bc9), [use databases](http://data.europa.eu/esco/skill/4463a721-69f3-413d-8321-43e3af13a4f1), [write database documentation](http://data.europa.eu/esco/skill/64db87c7-2360-4e20-88d3-d222402e477c)

**Knowledge:** [data extraction, transformation and loading tools](http://data.europa.eu/esco/skill/9d0d89be-bffa-4393-b6f6-8d05bea49051), [data quality assessment](http://data.europa.eu/esco/skill/cc7370dd-69fa-4c67-a96f-d4d135d38700), [data storage](http://data.europa.eu/esco/skill/a7f0fbe0-c546-4f30-8e41-34a58c64567e), [database development tools](http://data.europa.eu/esco/skill/9ef0f3a0-9ce2-4ef1-a987-0366b5cb2dbe), [database management systems](http://data.europa.eu/esco/skill/ab1e97ed-2319-4293-a8b7-072d2648822f), [query languages](http://data.europa.eu/esco/skill/9cf681c7-89ec-470c-b651-7fe03786f586), [resource description framework query language](http://data.europa.eu/esco/skill/99207709-d076-4cce-ba38-e90d3bb28806)

</details>

<details><summary>Optional skills and knowledge (96)</summary>

**Skills and competences:** [address problems critically](http://data.europa.eu/esco/skill/b9f16465-56a9-426b-a047-0f9f1f95ec92), [create solutions to problems](http://data.europa.eu/esco/skill/03b9b491-fc9b-4868-914a-bf7cd47b5041), [execute ICT audits](http://data.europa.eu/esco/skill/7e1f9657-ab4e-407c-842f-b846197060e3), [execute analytical mathematical calculations](http://data.europa.eu/esco/skill/31c69100-b612-4a61-8db5-fd314318854c), [execute integration testing](http://data.europa.eu/esco/skill/ea412de3-9d7a-4943-8d8c-c6d3c7495d0e), [execute software tests](http://data.europa.eu/esco/skill/913e7e83-b8f8-4574-b1ca-1b38f3fd974a), [identify ICT security risks](http://data.europa.eu/esco/skill/fe1c2b32-7fe9-4668-affa-07ff658a68cf), [integrate system components](http://data.europa.eu/esco/skill/ed8de897-adbe-4f0e-b4d2-534953e64c72), [manage business knowledge](http://data.europa.eu/esco/skill/41bf7ede-fc84-4a57-8c89-b548d11b0ba1), [manage cloud data and storage](http://data.europa.eu/esco/skill/d3286405-49f8-4e8a-8046-a4376b4e7963), [manage digital documents](http://data.europa.eu/esco/skill/b769f524-0f25-44d7-8538-5c46710a040e), [perform data mining](http://data.europa.eu/esco/skill/4216e465-7baa-4884-a241-54b197bb9278), [store digital data and systems](http://data.europa.eu/esco/skill/611ed16b-99bf-4840-9cab-f55d1d286e0a), [use back-up and recovery tools](http://data.europa.eu/esco/skill/82de2df7-0d6c-42b1-94ac-b3e9a029e917), [use personal organization software](http://data.europa.eu/esco/skill/fdf15b35-9028-4acb-bfd2-43f00a015cd9), [use query languages](http://data.europa.eu/esco/skill/75f839c2-fd9a-4ad3-8921-6e734608568d), [use software design patterns](http://data.europa.eu/esco/skill/2b7a79e5-84d8-4880-be66-3d9bb05bea17), [use spreadsheets software](http://data.europa.eu/esco/skill/1973c966-f236-40c9-b2d4-5d71a89019be), [verify formal ICT specifications](http://data.europa.eu/esco/skill/ee3b1553-2dc5-434b-8dcf-4ae3a40b3a48)

**Knowledge:** [ABAP](http://data.europa.eu/esco/skill/eb0e5615-1575-4a86-a1a2-7d39595033c5), [AJAX](http://data.europa.eu/esco/skill/b4dc6e4f-dc7d-445f-8ce2-d7b9d225e282), [APL](http://data.europa.eu/esco/skill/58d7a289-dafd-4363-833f-d1dc4140885e), [ASP.NET](http://data.europa.eu/esco/skill/56a7f561-1d55-43c9-9cd7-36a0a9bc6c50), [Ajax Framework](http://data.europa.eu/esco/skill/8c88d336-c249-4537-b26e-d679a85c4b9b), [Assembly (computer programming)](http://data.europa.eu/esco/skill/47b9bbcf-356c-4782-83a4-7f5a1b2b51a3), [C#](http://data.europa.eu/esco/skill/4c016b68-4116-468c-9dc6-42710c239e4a), [C++](http://data.europa.eu/esco/skill/b633eb55-8f1f-4ae6-ab4c-2022ffe2cb7f), [CA Datacom/DB](http://data.europa.eu/esco/skill/c5ed451b-ef39-47a3-aee7-8f5be0aa8431), [COBOL](http://data.europa.eu/esco/skill/def007fa-5fed-4a5f-91a2-b0d7e3db1be1), [CoffeeScript](http://data.europa.eu/esco/skill/993b1e23-f2de-4bd8-b33f-f86dde1c8e9d), [Common Lisp](http://data.europa.eu/esco/skill/0cd6dcf1-5778-42a5-b685-4d01ae4a4871), [DB2](http://data.europa.eu/esco/skill/3cee858e-79e8-4a4b-b99f-93c7f735d58b), [Erlang](http://data.europa.eu/esco/skill/034c29fa-c3ba-45ea-b8f3-bf8e3705e386), [Filemaker (database management systems)](http://data.europa.eu/esco/skill/b8eb2517-37d8-43e6-9856-9c29d5c51fde), [Groovy](http://data.europa.eu/esco/skill/52cf3037-ab53-4806-85ed-7fd21ea7f6a1), [Haskell](http://data.europa.eu/esco/skill/000f1d3d-220f-4789-9c0a-cc742521fb02), [IBM InfoSphere DataStage](http://data.europa.eu/esco/skill/14fdac88-6d4a-4e47-9df5-02c6d1e86fdd), [IBM InfoSphere Information Server](http://data.europa.eu/esco/skill/81b082fb-9a00-4660-976a-10c985979100), [IBM Informix](http://data.europa.eu/esco/skill/84251cb1-babf-4d17-a3cd-baa642c24c8d), [ICT infrastructure](http://data.europa.eu/esco/skill/d0c6d77e-cb25-4770-bf77-2073fc5f7523), [ICT power consumption](http://data.europa.eu/esco/skill/f88002a8-6355-4d33-9496-285c166ff375), [Informatica PowerCenter](http://data.europa.eu/esco/skill/0f00f63f-3ab4-4057-b92f-500584b51757), [Java (computer programming)](http://data.europa.eu/esco/skill/19a8293b-8e95-4de3-983f-77484079c389), [JavaScript](http://data.europa.eu/esco/skill/3cd569a2-4f88-4c1e-9995-8dce8c5e51a7), [JavaScript Framework](http://data.europa.eu/esco/skill/9b9de2a4-d8af-4a7b-933a-a8334ae60067), [LDAP](http://data.europa.eu/esco/skill/a57a54b6-2f2e-43e4-9621-b52f4a63cb08), [LINQ](http://data.europa.eu/esco/skill/c7d24594-0c11-4b27-9039-fe0bb903da8e), [Lisp](http://data.europa.eu/esco/skill/0de61385-de6d-4146-ba32-1cc1bc102220), [MATLAB](http://data.europa.eu/esco/skill/c3a03c5a-c260-4c26-9b9a-873abb396f4d), [MDX](http://data.europa.eu/esco/skill/1b7c716e-af95-4cda-a42f-6479c8b139f5), [ML (computer programming)](http://data.europa.eu/esco/skill/a4d336a6-9ffd-402a-91cc-f359716ba4e0), [MarkLogic](http://data.europa.eu/esco/skill/e819cc1e-09d9-47f2-b418-93972852daef), [Microsoft Access](http://data.europa.eu/esco/skill/3d03c40c-1b83-4793-8902-2523f40af59e), [Microsoft Visual C++](http://data.europa.eu/esco/skill/8369ede5-4200-4a44-be2e-bc60ef959259), [MySQL](http://data.europa.eu/esco/skill/4da171e5-779c-4983-a76f-91c16751e99f), [N1QL](http://data.europa.eu/esco/skill/f597f772-24d3-4cec-813c-cf5a7027c794), [ObjectStore](http://data.europa.eu/esco/skill/4959697d-3a24-4f46-af0c-b752318e6c54), [Objective-C](http://data.europa.eu/esco/skill/9973a5a2-7822-4161-99e9-95c781eb63f8), [OpenEdge Advanced Business Language](http://data.europa.eu/esco/skill/300d432b-f457-4cd3-9cb1-1858c7d14954), [OpenEdge Database](http://data.europa.eu/esco/skill/43ec6db6-33f7-449b-a566-5779a7e8997a), [Oracle Application Development Framework](http://data.europa.eu/esco/skill/8764d4b1-e069-44f2-8baa-fb1eee1850ec), [Oracle Data Integrator](http://data.europa.eu/esco/skill/3af687cb-8c7a-46ea-a730-32dbaed040c6), [Oracle Relational Database](http://data.europa.eu/esco/skill/de9f85ba-e77f-48fd-8c66-f5ebaf32d655), [Oracle Warehouse Builder](http://data.europa.eu/esco/skill/23900e3d-06fa-424c-a5dc-c0ea42edde1e), [PHP](http://data.europa.eu/esco/skill/4350c38d-0fe9-4ca7-bab9-40ed7f72b04f), [Pascal (computer programming)](http://data.europa.eu/esco/skill/e8b89eb6-51e8-4c3a-babb-88b2e110376b), [Pentaho Data Integration](http://data.europa.eu/esco/skill/42c3287f-5e50-4559-a2d1-2000c70e0aab), [Perl](http://data.europa.eu/esco/skill/401eb8d8-6daa-4f8b-90ad-60afc71eb4f8), [PostgreSQL](http://data.europa.eu/esco/skill/a8d07b5a-c1a1-42c6-9d53-db9c7a2ca996), [Prolog (computer programming)](http://data.europa.eu/esco/skill/2bde42ae-e776-41c1-9ded-b07b30bfe985), [Python (computer programming)](http://data.europa.eu/esco/skill/ccd0a1d9-afda-43d9-b901-96344886e14d), [QlikView Expressor](http://data.europa.eu/esco/skill/97bdd757-29d4-4126-92a6-07608825aa3b), [R](http://data.europa.eu/esco/skill/51586df8-1c46-4b47-8583-773cb63bf00b), [Ruby (computer programming)](http://data.europa.eu/esco/skill/0ccdfe98-f845-4598-84a1-3dca66e9d9a3), [SAP Data Services](http://data.europa.eu/esco/skill/f8e3425c-fe44-4ffb-bafe-0e20d91dadf4), [SAP R3](http://data.europa.eu/esco/skill/bb99af26-71ff-4dca-bde7-1eb1f6194426), [SAS Data Management](http://data.europa.eu/esco/skill/e5a6e1e0-1b07-4432-83ba-77d593b2cb47), [SAS language](http://data.europa.eu/esco/skill/04f1b938-d4d4-4cb1-a863-982af76b9d93), [SPARQL](http://data.europa.eu/esco/skill/5da8018b-ae85-4cde-ad93-0394369018f3), [SQL](http://data.europa.eu/esco/skill/598de5b0-5b58-4ea7-8058-a4bc4d18c742), [SQL Server](http://data.europa.eu/esco/skill/c062bab3-3ea0-4291-9220-a2d8fef4bead), [SQL Server Integration Services](http://data.europa.eu/esco/skill/6f7512ab-d46d-402a-8c30-a8878d7c1f88), [Scala](http://data.europa.eu/esco/skill/ffddfc7c-a9dd-449f-9e96-882dc447c8b6), [Scratch (computer programming)](http://data.europa.eu/esco/skill/d56fc2b5-4b0a-4e7e-9bde-a33736f6ff18), [Smalltalk (computer programming)](http://data.europa.eu/esco/skill/42ed3bfb-1a01-4c8b-9758-fc6438865734), [Swift (computer programming)](http://data.europa.eu/esco/skill/be80acfc-b6f2-4411-9b8d-b19d9cd2556a), [Teradata Database](http://data.europa.eu/esco/skill/d9eaf831-9348-4330-a83e-b7c099cdc8f6), [TripleStore](http://data.europa.eu/esco/skill/4e6d2538-a48e-48a7-8dad-14b067cfcb8b), [TypeScript](http://data.europa.eu/esco/skill/867137fb-ff1b-4ca3-99f3-cb6969aa2c68), [VBScript](http://data.europa.eu/esco/skill/dcdd5ddf-82a6-4ac3-8edc-d4b23cae9a88), [Visual Basic](http://data.europa.eu/esco/skill/13bdd41a-2a18-441f-96db-41252c519413), [WordPress](http://data.europa.eu/esco/skill/6d289e8b-2cc1-4eda-ab1f-ad1090ef98f0), [XQuery](http://data.europa.eu/esco/skill/3f4dab51-572b-4e2c-85ef-3b4c3f7094e1), [computer programming](http://data.europa.eu/esco/skill/21d2f96d-35f7-4e3f-9745-c533d2dd6e97), [data engineering](http://data.europa.eu/esco/skill/48db96bf-3314-45c6-bad8-fdb6e20e5639), [hardware architectures](http://data.europa.eu/esco/skill/e043aeeb-78f5-4049-afbf-12bba52225bc)

</details>

---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
