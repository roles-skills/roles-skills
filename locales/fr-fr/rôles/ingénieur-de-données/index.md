# Ingénieur de données

> Ceci est un profil de référence illustratif pour une organisation générique de santé numérique. Ce n'est la fiche de poste officielle d'aucun employeur, et ses points d'évaluation des emplois ne constituent pas une évaluation formelle.

> Ce texte a été traduit de l'anglais par un assistant d'intelligence artificielle et n'a pas encore été relu par un locuteur natif. Les citations du référentiel des compétences de la profession numérique et données du gouvernement britannique (UK GDaD PCF) et d'ESCO restent en anglais.

**Famille:** [Données](../../#données)  
**Bandes:** 6, 7, 8a, 8b  
**Rôle du UK GDaD PCF:** [Data engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/data-engineer/)  
**Professions ESCO:** [data engineer](http://data.europa.eu/esco/occupation/2079755f-d809-49e6-8037-4de6180e54c0) (ISCO-08 2511)

## Résumé

Les ingénieurs de données conçoivent et exploitent les flux et les plateformes qui acheminent les données de santé et de soins des systèmes cliniques et opérationnels vers des lieux où elles peuvent être analysées et utilisées en sécurité. Ils conçoivent les flux de données, intègrent des sources qui utilisent des normes différentes et veillent à ce que les données soient exactes, à jour, sécurisées et accessibles seulement aux personnes autorisées.

## Dans une organisation de santé numérique

- Les systèmes source comprennent les dossiers patients informatisés et les systèmes de laboratoire, d'imagerie et de pharmacie, qui utilisent des normes comme HL7 version 2, HL7 FHIR, SNOMED CT et la CIM.
- Les flux transportent souvent des données identifiantes de patients, c'est pourquoi les ingénieurs intègrent dès le départ la pseudonymisation, le contrôle d'accès et la traçabilité.
- Certains flux de données soutiennent les soins directs, comme les alertes ou les listes de patients, c'est pourquoi un flux en échec ou en retard peut toucher les patients et doit faire l'objet d'une évaluation de sécurité clinique.
- Les données doivent souvent être reliées entre structures de soins, ce qui repose sur un rapprochement fiable des patients et des identifiants cohérents.

## Description du rôle dans le UK GDaD PCF (original anglais)

> A data engineer develops and constructs data products and services, and integrates them into systems and business processes.

## Niveaux de rôle

| Bande | Intitulé | Niveau du UK GDaD PCF | Grades de la fonction publique britannique | Points d'évaluation de l'emploi |
| --- | --- | --- | --- | --- |
| 6 | [Ingénieur de données](#bande-6-ingénieur-de-données) | Data engineer | HEO/SEO | 421 |
| 7 | [Ingénieur de données senior](#bande-7-ingénieur-de-données-senior) | Senior data engineer | SEO/G7 | 477 |
| 8a | [Ingénieur de données référent](#bande-8a-ingénieur-de-données-référent) | Lead data engineer | G7 | 551 |
| 8b | [Responsable de l'ingénierie des données](#bande-8b-responsable-de-lingénierie-des-données) | Head of data engineering | G7/G6 | 589 |

## Bande 6: Ingénieur de données

**Niveau du UK GDaD PCF: Data engineer**

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

### Responsabilités

- Développer et maintenir les flux de données des systèmes cliniques et opérationnels vers la plateforme de données, selon des conceptions convenues.
- Établir la correspondance des données source, y compris les données cliniques codées, avec les modèles cibles et documenter les correspondances.
- Intégrer aux flux la pseudonymisation, la validation et les contrôles de qualité des données.
- Superviser les flux et corriger les défaillances, en donnant la priorité à ceux qui soutiennent les soins directs.
- Appliquer des contrôles d'accès et une journalisation d'audit conformes aux règles de gouvernance de l'information.

### Compétences

| Compétence | Source | Niveau attendu | Ce que signifie ce niveau |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../compétences/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Sensibilisation | You can:<br>• explain why it's important to communicate technical concepts in non-technical language<br>• explain the types of communication that can be used with internal and external stakeholders, and their impact |
| [Data analysis and synthesis](../../compétences/#data-analysis-and-synthesis) | UK GDaD PCF | Pratique | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data compliance and security](../../compétences/#data-compliance-and-security) | UK GDaD PCF | Pratique | You can:<br>• use official data classification when authoring documents<br>• apply internal procedures, policies and technologies to ensure secure data handling<br>• identify and address ethical considerations when working with data<br>• address data compliance issues using internal processes |
| [Data development process](../../compétences/#data-development-process) | UK GDaD PCF | Pratique | You can:<br>• implement simple data solutions such as data pipelines, following established approaches and standards<br>• create repeatable, reliable and reusable data solutions |
| [Data innovation](../../compétences/#data-innovation) | UK GDaD PCF | Sensibilisation | You can:<br>• develop a basic understanding of an unfamiliar or emerging technology, or a familiar technology in a new data context, with guidance<br>• share what you learn with colleagues, including how it could help deliver more value from data |
| [Data integration design](../../compétences/#data-integration-design) | UK GDaD PCF | Pratique | You can:<br>• design simple data exchange or integration solutions using established patterns or modelling techniques<br>• include security features in your data integration designs |
| [Data modelling](../../compétences/#data-modelling) | UK GDaD PCF | Pratique | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Metadata management](../../compétences/#metadata-management) | UK GDaD PCF | Pratique | You can:<br>• use metadata repositories to complete complex tasks such as data and systems integration impact analysis<br>• maintain a metadata repository to ensure information remains accurate and up to date |
| [Problem management](../../compétences/#problem-management) | UK GDaD PCF | Sensibilisation | You can:<br>• investigate problems in systems, processes and services, with an understanding of the level of a problem, for example, strategic, tactical or operational<br>• contribute to the implementation of remedies and preventative measures |
| [Programming and build (data and analytics engineering)](../../compétences/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | Pratique | You can:<br>• design, code, test and deploy programs or scripts following standards and good practice<br>• write readable, maintainable code<br>• use automation to improve the software development life cycle<br>• consider and adopt appropriate security measures in your solutions |
| [Compréhension des services de santé et de soins](../../compétences/#compréhension-des-services-de-santé-et-de-soins) | Cette référence | Pratique | Vous pouvez :<br>• expliquer les parcours de travail cliniques et de soins que soutient votre travail<br>• employer correctement les termes de santé courants avec les collègues cliniques et soignants<br>• reconnaître quand un changement pourrait toucher la prise en charge des patients et le signaler |
| [Gouvernance de l'information et protection des données](../../compétences/#gouvernance-de-linformation-et-protection-des-données) | Cette référence | Pratique | Vous pouvez :<br>• appliquer les principes de protection des données à votre travail<br>• contribuer aux analyses d'impact relatives à la protection des données<br>• traiter correctement les demandes d'information et les dossiers |
| [Interopérabilité des données de santé](../../compétences/#interopérabilité-des-données-de-santé) | Cette référence | Pratique | Vous pouvez :<br>• lire et utiliser des ressources, des profils et des API FHIR<br>• développer ou tester des intégrations simples avec un accompagnement<br>• vérifier des messages par rapport à une spécification |
| [Terminologie et classification cliniques](../../compétences/#terminologie-et-classification-cliniques) | Cette référence | Sensibilisation | Vous pouvez :<br>• expliquer la différence entre une terminologie clinique et une classification<br>• reconnaître des terminologies courantes comme SNOMED CT et la CIM |
| [Pseudonymisation et contrôle de la divulgation](../../compétences/#pseudonymisation-et-contrôle-de-la-divulgation) | Cette référence | Pratique | Vous pouvez :<br>• travailler avec des données pseudonymisées et appliquer des contrôles de divulgation avant de publier des résultats<br>• reconnaître quand des données reliées ou détaillées pourraient identifier un patient |
| [Gestion des risques cliniques](../../compétences/#gestion-des-risques-cliniques) | Cette référence | Sensibilisation | Vous pouvez :<br>• expliquer comment les systèmes informatiques de santé peuvent nuire aux patients, par exemple par des informations erronées, manquantes ou tardives<br>• signaler un éventuel problème de sécurité clinique par le bon canal |

### Qualifications et expérience habituelles

- Une licence en informatique ou dans une discipline voisine, ou une expérience équivalente.
- Une expérience du développement de flux de données.

### Description de la bande

- **Connaissances:** Connaissances spécialisées sur diverses procédures, acquises par une formation complémentaire ou l'expérience.
- **Autonomie:** Travaille en autonomie ; interprète la politique pour son domaine ; demande conseil sur les questions complexes.
- **Périmètre:** Un produit, un service ou un chantier.
- **Leadership:** Peut diriger une petite équipe ou accompagner ses collègues.
- **Responsabilité:** Les résultats de son chantier et la qualité des conseils donnés.

### Évaluation de l'emploi (illustrative)

| # | Facteur | Niveau | Points |
| --- | --- | --- | --- |
| 1 | Compétences de communication et relationnelles | 4 | 32 |
| 2 | Connaissances, formation et expérience | 6 | 156 |
| 3 | Compétences d'analyse et de jugement | 4 | 42 |
| 4 | Compétences de planification et d'organisation | 3 | 27 |
| 5 | Compétences physiques | 3 | 27 |
| 6 | Responsabilité de la prise en charge des patients et des usagers | 1 | 4 |
| 7 | Responsabilité de l'élaboration des politiques et des services | 2 | 12 |
| 8 | Responsabilité des ressources financières et matérielles | 1 | 5 |
| 9 | Responsabilité des personnes | 1 | 5 |
| 10 | Responsabilité des ressources d'information | 5 | 34 |
| 11 | Responsabilité de la recherche et du développement | 2 | 12 |
| 12 | Liberté d'action | 4 | 32 |
| 13 | Effort physique | 1 | 3 |
| 14 | Effort mental | 4 | 18 |
| 15 | Effort émotionnel | 1 | 5 |
| 16 | Conditions de travail | 2 | 7 |
| | **Total** | | **421** (Bande 6: 396–465) |

## Bande 7: Ingénieur de données senior

**Niveau du UK GDaD PCF: Senior data engineer**

> A senior data engineer designs and leads the implementation of data flows to connect operational systems, data for analytics and business intelligence (BI) systems.
> 
> At this role level, you will:
> - recognise opportunities to reuse existing data flows
> - lead the build of data streaming systems
> - optimise the code to ensure processes perform optimally
> - lead work on database management

### Responsabilités

- Concevoir des flux de données et des services de diffusion en continu qui rassemblent les données de nombreux systèmes de santé et de soins.
- Concevoir les processus de rapprochement et de chaînage des patients, et mesurer leur efficacité.
- Diriger le travail de performance des bases de données et de la plateforme pour que les données soient disponibles quand les services en ont besoin.
- Évaluer avec les spécialistes concernés les risques de sécurité clinique et de gouvernance de l'information des flux de données.
- Relire le travail des autres ingénieurs et les accompagner.

### Compétences

| Compétence | Source | Niveau attendu | Ce que signifie ce niveau |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../compétences/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Pratique | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Data analysis and synthesis](../../compétences/#data-analysis-and-synthesis) | UK GDaD PCF | Pratique | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data compliance and security](../../compétences/#data-compliance-and-security) | UK GDaD PCF | Confirmé | You can:<br>• consistently apply data ethics, legislation, internal procedures, policies and technologies to ensure secure data handling<br>• help ensure your team remain compliant by identifying and addressing current and potential data compliance and ethical issues<br>• guide and support others in addressing data compliance issues |
| [Data development process](../../compétences/#data-development-process) | UK GDaD PCF | Confirmé | You can:<br>• lead the implementation of complex or large-scale data solutions<br>• apply appropriate technology and techniques to ensure data solutions are secure and scalable<br>• identify and implement continuous improvement to the operation and performance of data solutions |
| [Data innovation](../../compétences/#data-innovation) | UK GDaD PCF | Pratique | You can:<br>• experiment with unfamiliar and emerging technologies, or familiar technologies in new data contexts, with guidance<br>• share what you learn with the team, explaining potential benefits, risks, and practical considerations<br>• identify opportunities to apply technology to improve data processes or outcomes in an operational setting or the wider organisation |
| [Data integration design](../../compétences/#data-integration-design) | UK GDaD PCF | Confirmé | You can:<br>• select the most appropriate techniques for different integration scenarios<br>• evaluate and lead the implementation of integration using varied approaches that ensure security, efficiency and compliance |
| [Data modelling](../../compétences/#data-modelling) | UK GDaD PCF | Confirmé | You can:<br>• produce relevant data models across multiple subject areas<br>• explain which models to use for which purpose<br>• understand industry-recognised data modelling patterns and standards, and when to apply them<br>• compare and align different data models |
| [Metadata management](../../compétences/#metadata-management) | UK GDaD PCF | Confirmé | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../compétences/#problem-management) | UK GDaD PCF | Pratique | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Programming and build (data and analytics engineering)](../../compétences/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | Confirmé | You can:<br>• lead the design, code, testing and deployment of secure, resilient and maintainable solutions<br>• continuously improve the codebase and reliability of solutions<br>• create automation to improve the software development life cycle<br>• work with others to implement standards and good practice to ensure security, testability and maintainability of solutions |
| [Compréhension des services de santé et de soins](../../compétences/#compréhension-des-services-de-santé-et-de-soins) | Cette référence | Pratique | Vous pouvez :<br>• expliquer les parcours de travail cliniques et de soins que soutient votre travail<br>• employer correctement les termes de santé courants avec les collègues cliniques et soignants<br>• reconnaître quand un changement pourrait toucher la prise en charge des patients et le signaler |
| [Gouvernance de l'information et protection des données](../../compétences/#gouvernance-de-linformation-et-protection-des-données) | Cette référence | Confirmé | Vous pouvez :<br>• diriger des analyses d'impact relatives à la protection des données et des accords de partage d'informations<br>• conseiller les équipes sur la base légale, le consentement, la confidentialité et la conservation<br>• enquêter sur les incidents et recommander des améliorations |
| [Interopérabilité des données de santé](../../compétences/#interopérabilité-des-données-de-santé) | Cette référence | Confirmé | Vous pouvez :<br>• concevoir et développer des intégrations avec FHIR, HL7 version 2 et des modèles de messagerie<br>• rédiger et profiler des ressources FHIR et des guides d'implémentation<br>• résoudre des problèmes complexes de correspondance et de qualité des données entre systèmes |
| [Terminologie et classification cliniques](../../compétences/#terminologie-et-classification-cliniques) | Cette référence | Pratique | Vous pouvez :<br>• trouver et utiliser les bons codes pour une donnée ou un formulaire<br>• utiliser des navigateurs de terminologie et des ensembles de référence |
| [Pseudonymisation et contrôle de la divulgation](../../compétences/#pseudonymisation-et-contrôle-de-la-divulgation) | Cette référence | Confirmé | Vous pouvez :<br>• concevoir des méthodes de pseudonymisation et de chaînage qui séparent les identifiants des données d'analyse<br>• évaluer le risque de réidentification d'un jeu de données ou d'une publication et choisir des mesures adaptées<br>• conseiller les équipes sur les environnements sécurisés, comme les environnements de recherche de confiance |
| [Gestion des risques cliniques](../../compétences/#gestion-des-risques-cliniques) | Cette référence | Pratique | Vous pouvez :<br>• participer à des ateliers d'identification des dangers et contribuer à un registre des dangers<br>• suivre le processus de gestion des risques cliniques dans votre travail<br>• fournir des preuves pour un dossier de sécurité clinique, comme des résultats de tests |

### Qualifications et expérience habituelles

- Une expérience significative de la conception et du développement de systèmes de données, d'un niveau équivalent à un master.

### Description de la bande

- **Connaissances:** Connaissances spécialisées très développées, généralement de niveau master ou une expérience équivalente.
- **Autonomie:** Travaille selon la politique de l'organisation ; décide de la manière d'atteindre les résultats ; est l'expert que les autres consultent.
- **Périmètre:** Plusieurs produits ou services, ou une fonction spécialisée.
- **Leadership:** Dirige une équipe ou un domaine de pratique professionnelle.
- **Responsabilité:** La prestation d'un service ou d'une fonction spécialisée, et son budget le cas échéant.

### Évaluation de l'emploi (illustrative)

| # | Facteur | Niveau | Points |
| --- | --- | --- | --- |
| 1 | Compétences de communication et relationnelles | 4 | 32 |
| 2 | Connaissances, formation et expérience | 7 | 196 |
| 3 | Compétences d'analyse et de jugement | 4 | 42 |
| 4 | Compétences de planification et d'organisation | 3 | 27 |
| 5 | Compétences physiques | 3 | 27 |
| 6 | Responsabilité de la prise en charge des patients et des usagers | 1 | 4 |
| 7 | Responsabilité de l'élaboration des politiques et des services | 3 | 21 |
| 8 | Responsabilité des ressources financières et matérielles | 1 | 5 |
| 9 | Responsabilité des personnes | 2 | 12 |
| 10 | Responsabilité des ressources d'information | 5 | 34 |
| 11 | Responsabilité de la recherche et du développement | 2 | 12 |
| 12 | Liberté d'action | 4 | 32 |
| 13 | Effort physique | 1 | 3 |
| 14 | Effort mental | 4 | 18 |
| 15 | Effort émotionnel | 1 | 5 |
| 16 | Conditions de travail | 2 | 7 |
| | **Total** | | **477** (Bande 7: 466–539) |

## Bande 8a: Ingénieur de données référent

**Niveau du UK GDaD PCF: Lead data engineer**

> A lead data engineer is responsible for the design and implementation of numerous complex data flows to connect operational systems, data for analytics and business intelligence (BI) systems.
> 
> At this role level, you will:
> - recognise and share opportunities to reuse existing data flows between teams
> - be responsible for the build of data-streaming systems
> - co-ordinate teams and set best practice and standards
> - apply knowledge of systems integration to your work
> - champion data engineering across government

### Responsabilités

- Diriger la conception et l'exploitation de la plateforme de données de l'organisation et de ses nombreux flux.
- Fixer des normes d'ingénierie pour les flux, les tests, la sécurité et la documentation.
- Planifier l'intégration des données avec les partenaires de santé et de soins, y compris les dossiers de soins partagés et les services régionaux de données.
- Veiller à ce que les flux de données qui soutiennent les soins directs soient résilients et disposent de dossiers de sécurité clinique.
- Coordonner les équipes d'ingénierie des données et encadrer les ingénieurs.

### Compétences

| Compétence | Source | Niveau attendu | Ce que signifie ce niveau |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../compétences/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Confirmé | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Data analysis and synthesis](../../compétences/#data-analysis-and-synthesis) | UK GDaD PCF | Confirmé | You can:<br>• understand and help teams to apply a range of techniques for data profiling<br>• source system analysis from a complex single source<br>• bring multiple data sources together in a conformed model for analysis |
| [Data compliance and security](../../compétences/#data-compliance-and-security) | UK GDaD PCF | Expert | You can:<br>• advise senior stakeholders on data security, ethical or procedural risks<br>• improve organisational awareness of data compliance and procedures<br>• lead, guide and mentor teams in implementing secure data practices and maintaining compliance |
| [Data development process](../../compétences/#data-development-process) | UK GDaD PCF | Expert | You can:<br>• establish cross-organisational data solutions that include all aspects of the data development life cycle<br>• define and promote good practices for creating repeatable, reliable and reusable data solutions |
| [Data innovation](../../compétences/#data-innovation) | UK GDaD PCF | Confirmé | You can:<br>• test and evaluate the feasibility of unfamiliar and emerging technologies, or familiar technologies in new data contexts<br>• share what you learn with the organisation, explaining potential benefits, risks, and practical considerations<br>• recommend, design and implement innovative data solutions based on organisation objectives, user needs, and operational constraints |
| [Data integration design](../../compétences/#data-integration-design) | UK GDaD PCF | Expert | You can:<br>• establish cross-organisational data integration standards and design patterns<br>• guide teams in designing secure and interoperable systems and services |
| [Data modelling](../../compétences/#data-modelling) | UK GDaD PCF | Expert | You can:<br>• understand the concepts and principles of data modelling and can produce relevant data models<br>• work across government and industry, recognising opportunities for the reuse and alignment of data models in different organisations<br>• design the method to categorise data models within an organisation |
| [Metadata management](../../compétences/#metadata-management) | UK GDaD PCF | Confirmé | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../compétences/#problem-management) | UK GDaD PCF | Confirmé | You can:<br>• ensure that the right actions are taken to investigate, resolve and anticipate problems<br>• co-ordinate the team to investigate problems, implement solutions and take preventive measures |
| [Programming and build (data and analytics engineering)](../../compétences/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | Confirmé | You can:<br>• lead the design, code, testing and deployment of secure, resilient and maintainable solutions<br>• continuously improve the codebase and reliability of solutions<br>• create automation to improve the software development life cycle<br>• work with others to implement standards and good practice to ensure security, testability and maintainability of solutions |
| [Compréhension des services de santé et de soins](../../compétences/#compréhension-des-services-de-santé-et-de-soins) | Cette référence | Confirmé | Vous pouvez :<br>• analyser la place d'un service dans les parcours de soins entre organisations<br>• travailler avec les cliniciens, le personnel soignant et les patients pour façonner les services numériques<br>• expliquer l'effet des décisions numériques sur les soins, la sécurité et la charge de travail du personnel |
| [Gouvernance de l'information et protection des données](../../compétences/#gouvernance-de-linformation-et-protection-des-données) | Cette référence | Confirmé | Vous pouvez :<br>• diriger des analyses d'impact relatives à la protection des données et des accords de partage d'informations<br>• conseiller les équipes sur la base légale, le consentement, la confidentialité et la conservation<br>• enquêter sur les incidents et recommander des améliorations |
| [Interopérabilité des données de santé](../../compétences/#interopérabilité-des-données-de-santé) | Cette référence | Confirmé | Vous pouvez :<br>• concevoir et développer des intégrations avec FHIR, HL7 version 2 et des modèles de messagerie<br>• rédiger et profiler des ressources FHIR et des guides d'implémentation<br>• résoudre des problèmes complexes de correspondance et de qualité des données entre systèmes |
| [Terminologie et classification cliniques](../../compétences/#terminologie-et-classification-cliniques) | Cette référence | Pratique | Vous pouvez :<br>• trouver et utiliser les bons codes pour une donnée ou un formulaire<br>• utiliser des navigateurs de terminologie et des ensembles de référence |
| [Pseudonymisation et contrôle de la divulgation](../../compétences/#pseudonymisation-et-contrôle-de-la-divulgation) | Cette référence | Confirmé | Vous pouvez :<br>• concevoir des méthodes de pseudonymisation et de chaînage qui séparent les identifiants des données d'analyse<br>• évaluer le risque de réidentification d'un jeu de données ou d'une publication et choisir des mesures adaptées<br>• conseiller les équipes sur les environnements sécurisés, comme les environnements de recherche de confiance |
| [Gestion des risques cliniques](../../compétences/#gestion-des-risques-cliniques) | Cette référence | Pratique | Vous pouvez :<br>• participer à des ateliers d'identification des dangers et contribuer à un registre des dangers<br>• suivre le processus de gestion des risques cliniques dans votre travail<br>• fournir des preuves pour un dossier de sécurité clinique, comme des résultats de tests |
| [Management des personnes](../../compétences/#management-des-personnes) | Cette référence | Confirmé | Vous pouvez :<br>• encadrer hiérarchiquement une équipe, en fixant des objectifs et en menant les entretiens annuels<br>• soutenir le bien-être et gérer l'assiduité, la performance et la conduite<br>• planifier le développement et la relève de l'équipe |

### Qualifications et expérience habituelles

- Une solide expérience de la direction de l'ingénierie des données de systèmes complexes.

### Description de la bande

- **Connaissances:** Connaissance experte d'une discipline et de sa gestion.
- **Autonomie:** Interprète la politique de l'organisation pour un service ; fixe l'orientation de l'équipe.
- **Périmètre:** Un domaine de service ou une discipline dans toute l'organisation.
- **Leadership:** Gère une équipe, ou dirige une discipline sans encadrement hiérarchique.
- **Responsabilité:** Un domaine de service, son personnel et son budget.

### Évaluation de l'emploi (illustrative)

| # | Facteur | Niveau | Points |
| --- | --- | --- | --- |
| 1 | Compétences de communication et relationnelles | 5 | 45 |
| 2 | Connaissances, formation et expérience | 7 | 196 |
| 3 | Compétences d'analyse et de jugement | 5 | 60 |
| 4 | Compétences de planification et d'organisation | 4 | 42 |
| 5 | Compétences physiques | 2 | 15 |
| 6 | Responsabilité de la prise en charge des patients et des usagers | 1 | 4 |
| 7 | Responsabilité de l'élaboration des politiques et des services | 4 | 32 |
| 8 | Responsabilité des ressources financières et matérielles | 2 | 12 |
| 9 | Responsabilité des personnes | 3 | 21 |
| 10 | Responsabilité des ressources d'information | 5 | 34 |
| 11 | Responsabilité de la recherche et du développement | 2 | 12 |
| 12 | Liberté d'action | 5 | 45 |
| 13 | Effort physique | 1 | 3 |
| 14 | Effort mental | 4 | 18 |
| 15 | Effort émotionnel | 1 | 5 |
| 16 | Conditions de travail | 2 | 7 |
| | **Total** | | **551** (Bande 8a: 540–584) |

## Bande 8b: Responsable de l'ingénierie des données

**Niveau du UK GDaD PCF: Head of data engineering**

> A head of data engineering leads multi-functional delivery teams to deliver robust data services for their department, other government departments and private sector partners.
> 
> At this role level, you will:
> - inspire best practice for data products and services within your teams
> - build data engineering capability by providing technical leadership and career development for the community
> - work with other senior team members to identify, plan, develop and deliver data services

### Responsabilités

- Fixer la stratégie des plateformes de données et des services d'ingénierie des données de l'organisation.
- Diriger des équipes pluridisciplinaires qui fournissent des services de données aux équipes internes et aux partenaires de santé et de soins.
- Conseiller la direction sur les risques, les coûts et les investissements de la plateforme de données.
- Veiller à ce que les services de données respectent les exigences de gouvernance de l'information, de sécurité et de sécurité clinique.
- Développer la capacité d'ingénierie des données par le recrutement, le développement et les parcours de carrière.

### Compétences

| Compétence | Source | Niveau attendu | Ce que signifie ce niveau |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../compétences/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Expert | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Data analysis and synthesis](../../compétences/#data-analysis-and-synthesis) | UK GDaD PCF | Confirmé | You can:<br>• understand and help teams to apply a range of techniques for data profiling<br>• source system analysis from a complex single source<br>• bring multiple data sources together in a conformed model for analysis |
| [Data compliance and security](../../compétences/#data-compliance-and-security) | UK GDaD PCF | Expert | You can:<br>• advise senior stakeholders on data security, ethical or procedural risks<br>• improve organisational awareness of data compliance and procedures<br>• lead, guide and mentor teams in implementing secure data practices and maintaining compliance |
| [Data development process](../../compétences/#data-development-process) | UK GDaD PCF | Expert | You can:<br>• establish cross-organisational data solutions that include all aspects of the data development life cycle<br>• define and promote good practices for creating repeatable, reliable and reusable data solutions |
| [Data innovation](../../compétences/#data-innovation) | UK GDaD PCF | Expert | You can:<br>• advocate for adoption of unfamiliar and emerging technologies, or familiar technologies in new data contexts, ensuring organisation objectives, user needs, and operational constraints inform decisions<br>• develop organisational capability in data innovation through leadership<br>• anticipate future technology changes and advise how to take advantage of them to realise value from data |
| [Data integration design](../../compétences/#data-integration-design) | UK GDaD PCF | Expert | You can:<br>• establish cross-organisational data integration standards and design patterns<br>• guide teams in designing secure and interoperable systems and services |
| [Data modelling](../../compétences/#data-modelling) | UK GDaD PCF | Pratique | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Metadata management](../../compétences/#metadata-management) | UK GDaD PCF | Expert | You can:<br>• identify how metadata repositories can support different areas of the organisation<br>• communicate the value of metadata repositories<br>• set up robust governance processes to keep repositories up to date |
| [Problem management](../../compétences/#problem-management) | UK GDaD PCF | Expert | You can:<br>• anticipate problems and defend against them at the right time<br>• understand how a problem fits into the larger picture<br>• identify and describe problems, and help others to describe them<br>• build problem-solving capabilities in others |
| [Programming and build (data and analytics engineering)](../../compétences/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | Expert | You can:<br>• set standards for programming tools and techniques<br>• select appropriate development methods for a problem<br>• advise on the application of standards and methods that ensure security, maintainability and compliance<br>• take technical responsibility for all stages of a software development project, providing technical advice and guidance to stakeholders |
| [Compréhension des services de santé et de soins](../../compétences/#compréhension-des-services-de-santé-et-de-soins) | Cette référence | Confirmé | Vous pouvez :<br>• analyser la place d'un service dans les parcours de soins entre organisations<br>• travailler avec les cliniciens, le personnel soignant et les patients pour façonner les services numériques<br>• expliquer l'effet des décisions numériques sur les soins, la sécurité et la charge de travail du personnel |
| [Gouvernance de l'information et protection des données](../../compétences/#gouvernance-de-linformation-et-protection-des-données) | Cette référence | Confirmé | Vous pouvez :<br>• diriger des analyses d'impact relatives à la protection des données et des accords de partage d'informations<br>• conseiller les équipes sur la base légale, le consentement, la confidentialité et la conservation<br>• enquêter sur les incidents et recommander des améliorations |
| [Interopérabilité des données de santé](../../compétences/#interopérabilité-des-données-de-santé) | Cette référence | Expert | Vous pouvez :<br>• fixer les normes et la stratégie d'interopérabilité de l'organisation<br>• diriger des travaux de normalisation nationaux ou interorganisations<br>• garantir la conception d'intégrations critiques entre de nombreux systèmes |
| [Pseudonymisation et contrôle de la divulgation](../../compétences/#pseudonymisation-et-contrôle-de-la-divulgation) | Cette référence | Confirmé | Vous pouvez :<br>• concevoir des méthodes de pseudonymisation et de chaînage qui séparent les identifiants des données d'analyse<br>• évaluer le risque de réidentification d'un jeu de données ou d'une publication et choisir des mesures adaptées<br>• conseiller les équipes sur les environnements sécurisés, comme les environnements de recherche de confiance |
| [Gestion des risques cliniques](../../compétences/#gestion-des-risques-cliniques) | Cette référence | Pratique | Vous pouvez :<br>• participer à des ateliers d'identification des dangers et contribuer à un registre des dangers<br>• suivre le processus de gestion des risques cliniques dans votre travail<br>• fournir des preuves pour un dossier de sécurité clinique, comme des résultats de tests |
| [Management des personnes](../../compétences/#management-des-personnes) | Cette référence | Confirmé | Vous pouvez :<br>• encadrer hiérarchiquement une équipe, en fixant des objectifs et en menant les entretiens annuels<br>• soutenir le bien-être et gérer l'assiduité, la performance et la conduite<br>• planifier le développement et la relève de l'équipe |
| [Gestion budgétaire](../../compétences/#gestion-budgétaire) | Cette référence | Confirmé | Vous pouvez :<br>• détenir et gérer un budget, en établissant des prévisions et en expliquant les écarts<br>• élaborer une étude d'opportunité avec ses coûts et ses bénéfices |

### Qualifications et expérience habituelles

- Une solide expérience de la direction de l'ingénierie des données dans plusieurs équipes.

### Description de la bande

- **Connaissances:** Connaissance experte de plusieurs disciplines ou d'un service de grande taille.
- **Autonomie:** Façonne la politique et la stratégie d'un domaine étendu.
- **Périmètre:** Plusieurs services ou équipes, ou une discipline de niveau principal.
- **Leadership:** Gère des responsables, ou est l'autorité de référence d'une discipline.
- **Responsabilité:** Plusieurs services, leur personnel et leurs budgets.

### Évaluation de l'emploi (illustrative)

| # | Facteur | Niveau | Points |
| --- | --- | --- | --- |
| 1 | Compétences de communication et relationnelles | 5 | 45 |
| 2 | Connaissances, formation et expérience | 7 | 196 |
| 3 | Compétences d'analyse et de jugement | 5 | 60 |
| 4 | Compétences de planification et d'organisation | 5 | 60 |
| 5 | Compétences physiques | 2 | 15 |
| 6 | Responsabilité de la prise en charge des patients et des usagers | 1 | 4 |
| 7 | Responsabilité de l'élaboration des politiques et des services | 4 | 32 |
| 8 | Responsabilité des ressources financières et matérielles | 3 | 21 |
| 9 | Responsabilité des personnes | 4 | 32 |
| 10 | Responsabilité des ressources d'information | 5 | 34 |
| 11 | Responsabilité de la recherche et du développement | 2 | 12 |
| 12 | Liberté d'action | 5 | 45 |
| 13 | Effort physique | 1 | 3 |
| 14 | Effort mental | 4 | 18 |
| 15 | Effort émotionnel | 1 | 5 |
| 16 | Conditions de travail | 2 | 7 |
| | **Total** | | **589** (Bande 8b: 585–629) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
