# Ingénieur d'intégration (interopérabilité en santé)

> Ceci est un profil de référence illustratif pour une organisation générique de santé numérique. Ce n'est la fiche de poste officielle d'aucun employeur, et ses points d'évaluation des emplois ne constituent pas une évaluation formelle.

> Ce texte a été traduit de l'anglais par un assistant d'intelligence artificielle et n'a pas encore été relu par un locuteur natif. Les citations du référentiel des compétences de la profession numérique et données du gouvernement britannique (UK GDaD PCF) et d'ESCO restent en anglais.

**Famille:** [Développement logiciel](../../#développement-logiciel)  
**Bandes:** 5, 6, 7, 8a  
**Rôle du UK GDaD PCF:** Aucun (ce rôle est défini par cette référence)  
**Professions ESCO:** [integration engineer](http://data.europa.eu/esco/occupation/07e60525-1aad-4099-aaf3-2c7014c92212) (ISCO-08 2511); [database developer](http://data.europa.eu/esco/occupation/b11e1742-5e28-4270-b081-b0193d85ee7d) (ISCO-08 2521)

## Résumé

Les ingénieurs d'intégration relient les systèmes cliniques et de gestion de l'organisation pour que les informations de santé et de soins circulent en toute sécurité là où elles sont nécessaires. Ils conçoivent, développent, testent et maintiennent des interfaces, des API et des flux de messages avec des normes comme HL7 FHIR et HL7 version 2, établissent les correspondances de données et de codes cliniques entre systèmes, et maintiennent les intégrations en fonctionnement en production.

## Dans une organisation de santé numérique

- Un message perdu, retardé, dupliqué ou rattaché au mauvais patient, comme un résultat d'examen ou une demande d'avis, peut directement causer un préjudice, c'est pourquoi le travail d'intégration suit le processus de gestion des risques cliniques.
- Les intégrations transportent de grands volumes d'informations de santé confidentielles entre organisations, c'est pourquoi chaque flux a besoin d'une base légale, d'un transport sécurisé et d'une traçabilité.
- Les systèmes de santé utilisent de nombreuses normes et versions, des messages HL7 version 2 aux API HL7 FHIR et aux profils IHE, souvent avec des variantes locales.
- Le sens clinique doit être préservé de bout en bout, c'est pourquoi les ingénieurs établissent correctement les correspondances des terminologies cliniques comme SNOMED CT et rapprochent les patients de façon fiable.
- De nombreuses intégrations soutiennent les soins jour et nuit, c'est pourquoi elles ont besoin de supervision, d'alertes et de circuits clairs pour traiter les messages en échec.

## Niveaux de rôle

| Bande | Intitulé | Niveau du UK GDaD PCF | Grades de la fonction publique britannique | Points d'évaluation de l'emploi |
| --- | --- | --- | --- | --- |
| 5 | [Ingénieur d'intégration junior](#bande-5-ingénieur-dintégration-junior) | — | — | 335 |
| 6 | [Ingénieur d'intégration](#bande-6-ingénieur-dintégration) | — | — | 418 |
| 7 | [Ingénieur d'intégration senior](#bande-7-ingénieur-dintégration-senior) | — | — | 477 |
| 8a | [Ingénieur d'intégration référent](#bande-8a-ingénieur-dintégration-référent) | — | — | 551 |

## Bande 5: Ingénieur d'intégration junior

L'ingénieur d'intégration junior développe, teste et maintient des intégrations entre systèmes de santé et de soins, à partir de spécifications et avec l'accompagnement d'ingénieurs plus expérimentés.

### Responsabilités

- Développer et modifier des correspondances de messages, des transformations et des appels d'API à partir de spécifications convenues.
- Tester les intégrations au regard des spécifications et de messages exemples, y compris les cas d'erreur et les cas limites.
- Superviser les flux de messages, analyser les messages en échec ou rejetés, et les résoudre ou les faire remonter.
- Traiter les données de santé de façon sûre, selon les règles de gouvernance de l'information pour les données réelles et de test.
- Consigner les changements et les résultats de tests pour qu'ils servent de preuves de sécurité clinique.

### Compétences

| Compétence | Source | Niveau attendu | Ce que signifie ce niveau |
| --- | --- | --- | --- |
| [Systems integration](../../compétences/#systems-integration) | UK GDaD PCF | Pratique | You can:<br>• build and test simple interfaces between systems<br>• work on more complex integration as part of a wider team |
| [Programming and build (software engineering)](../../compétences/#programming-and-build-software-engineering) | UK GDaD PCF | Pratique | You can:<br>• design, code, test, correct and document simple programs or scripts under the direction of others |
| [Testing](../../compétences/#testing) | UK GDaD PCF | Pratique | You can:<br>• review requirements and specifications, and define test conditions<br>• identify issues and risks associated with work<br>• analyse and report test activities and results |
| [Service support](../../compétences/#service-support) | UK GDaD PCF | Pratique | You can:<br>• help fix service faults following agreed procedures<br>• carry out maintenance tasks on service support infrastructure |
| [Information security](../../compétences/#information-security) | UK GDaD PCF | Sensibilisation | You can:<br>• explain information security and the security controls available to protect solutions and services |
| [Interopérabilité des données de santé](../../compétences/#interopérabilité-des-données-de-santé) | Cette référence | Pratique | Vous pouvez :<br>• lire et utiliser des ressources, des profils et des API FHIR<br>• développer ou tester des intégrations simples avec un accompagnement<br>• vérifier des messages par rapport à une spécification |
| [Terminologie et classification cliniques](../../compétences/#terminologie-et-classification-cliniques) | Cette référence | Sensibilisation | Vous pouvez :<br>• expliquer la différence entre une terminologie clinique et une classification<br>• reconnaître des terminologies courantes comme SNOMED CT et la CIM |
| [Gouvernance de l'information et protection des données](../../compétences/#gouvernance-de-linformation-et-protection-des-données) | Cette référence | Pratique | Vous pouvez :<br>• appliquer les principes de protection des données à votre travail<br>• contribuer aux analyses d'impact relatives à la protection des données<br>• traiter correctement les demandes d'information et les dossiers |
| [Gestion des risques cliniques](../../compétences/#gestion-des-risques-cliniques) | Cette référence | Sensibilisation | Vous pouvez :<br>• expliquer comment les systèmes informatiques de santé peuvent nuire aux patients, par exemple par des informations erronées, manquantes ou tardives<br>• signaler un éventuel problème de sécurité clinique par le bon canal |
| [Compréhension des services de santé et de soins](../../compétences/#compréhension-des-services-de-santé-et-de-soins) | Cette référence | Sensibilisation | Vous pouvez :<br>• décrire les principales composantes du système de santé et de soins et les services que soutient l'organisation<br>• expliquer pourquoi la sécurité des patients et la confidentialité comptent dans votre travail |

### Qualifications et expérience habituelles

- Une licence en informatique ou dans une discipline voisine, un apprentissage achevé ou une expérience équivalente.

### Description de la bande

- **Connaissances:** Connaissances professionnelles ou techniques, généralement acquises par une licence ou une expérience équivalente.
- **Autonomie:** Travaille vers des objectifs généraux dans le respect des normes professionnelles ; planifie son propre travail.
- **Périmètre:** Son propre travail professionnel au sein d'une équipe ou d'un produit.
- **Leadership:** Peut orienter et vérifier le travail du personnel de soutien et des apprentis.
- **Responsabilité:** La qualité de son propre travail professionnel.

### Évaluation de l'emploi (illustrative)

| # | Facteur | Niveau | Points |
| --- | --- | --- | --- |
| 1 | Compétences de communication et relationnelles | 4 | 32 |
| 2 | Connaissances, formation et expérience | 5 | 120 |
| 3 | Compétences d'analyse et de jugement | 3 | 27 |
| 4 | Compétences de planification et d'organisation | 2 | 15 |
| 5 | Compétences physiques | 3 | 27 |
| 6 | Responsabilité de la prise en charge des patients et des usagers | 1 | 4 |
| 7 | Responsabilité de l'élaboration des politiques et des services | 2 | 12 |
| 8 | Responsabilité des ressources financières et matérielles | 1 | 5 |
| 9 | Responsabilité des personnes | 1 | 5 |
| 10 | Responsabilité des ressources d'information | 4 | 24 |
| 11 | Responsabilité de la recherche et du développement | 2 | 12 |
| 12 | Liberté d'action | 3 | 21 |
| 13 | Effort physique | 2 | 7 |
| 14 | Effort mental | 3 | 12 |
| 15 | Effort émotionnel | 1 | 5 |
| 16 | Conditions de travail | 2 | 7 |
| | **Total** | | **335** (Bande 5: 326–395) |

## Bande 6: Ingénieur d'intégration

L'ingénieur d'intégration conçoit, développe et maintient en autonomie des intégrations entre systèmes de santé et de soins, et aide à définir comment les systèmes doivent échanger des données.

### Responsabilités

- Concevoir et développer des intégrations, des API et des flux de messages avec HL7 FHIR, HL7 version 2 et des modèles de messagerie.
- Analyser les systèmes source et cible et rédiger des spécifications d'interface et des correspondances de données, y compris les codes cliniques.
- Mettre en place le rapprochement des patients, la validation et la gestion des erreurs pour que les informations parviennent au bon dossier.
- Participer aux ateliers d'identification des dangers et intégrer des mesures de sécurité aux intégrations, comme des alertes sur les messages en échec ou retardés.
- Travailler avec les fournisseurs et les organisations partenaires pour tester et mettre en service de nouvelles connexions.
- Analyser et corriger les problèmes des intégrations en production, et accompagner les ingénieurs d'intégration juniors.

### Compétences

| Compétence | Source | Niveau attendu | Ce que signifie ce niveau |
| --- | --- | --- | --- |
| [Systems integration](../../compétences/#systems-integration) | UK GDaD PCF | Confirmé | You can:<br>• define the integration build<br>• co-ordinate build activities across systems<br>• understand how to undertake and support integration testing activities |
| [Programming and build (software engineering)](../../compétences/#programming-and-build-software-engineering) | UK GDaD PCF | Confirmé | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../compétences/#systems-design) | UK GDaD PCF | Pratique | You can:<br>• translate logical designs into physical designs<br>• produce detailed designs<br>• effectively document all work using required standards, methods and tools, including prototyping tools where appropriate<br>• design systems characterised by managed levels of risk, manageable business and technical complexity, and meaningful impact<br>• work with well understood technology and identify appropriate patterns |
| [Service support](../../compétences/#service-support) | UK GDaD PCF | Confirmé | You can:<br>• identify, locate and fix service faults |
| [Information security](../../compétences/#information-security) | UK GDaD PCF | Pratique | You can:<br>• use information security practices and available security controls to contribute to protecting solutions and services |
| [Interopérabilité des données de santé](../../compétences/#interopérabilité-des-données-de-santé) | Cette référence | Confirmé | Vous pouvez :<br>• concevoir et développer des intégrations avec FHIR, HL7 version 2 et des modèles de messagerie<br>• rédiger et profiler des ressources FHIR et des guides d'implémentation<br>• résoudre des problèmes complexes de correspondance et de qualité des données entre systèmes |
| [Terminologie et classification cliniques](../../compétences/#terminologie-et-classification-cliniques) | Cette référence | Pratique | Vous pouvez :<br>• trouver et utiliser les bons codes pour une donnée ou un formulaire<br>• utiliser des navigateurs de terminologie et des ensembles de référence |
| [Gouvernance de l'information et protection des données](../../compétences/#gouvernance-de-linformation-et-protection-des-données) | Cette référence | Pratique | Vous pouvez :<br>• appliquer les principes de protection des données à votre travail<br>• contribuer aux analyses d'impact relatives à la protection des données<br>• traiter correctement les demandes d'information et les dossiers |
| [Gestion des risques cliniques](../../compétences/#gestion-des-risques-cliniques) | Cette référence | Pratique | Vous pouvez :<br>• participer à des ateliers d'identification des dangers et contribuer à un registre des dangers<br>• suivre le processus de gestion des risques cliniques dans votre travail<br>• fournir des preuves pour un dossier de sécurité clinique, comme des résultats de tests |
| [Compréhension des services de santé et de soins](../../compétences/#compréhension-des-services-de-santé-et-de-soins) | Cette référence | Pratique | Vous pouvez :<br>• expliquer les parcours de travail cliniques et de soins que soutient votre travail<br>• employer correctement les termes de santé courants avec les collègues cliniques et soignants<br>• reconnaître quand un changement pourrait toucher la prise en charge des patients et le signaler |

### Qualifications et expérience habituelles

- Une licence en informatique ou dans une discipline voisine, ou une expérience équivalente.
- Une expérience du développement et du support d'intégrations entre systèmes en production.

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
| 9 | Responsabilité des personnes | 2 | 12 |
| 10 | Responsabilité des ressources d'information | 4 | 24 |
| 11 | Responsabilité de la recherche et du développement | 2 | 12 |
| 12 | Liberté d'action | 4 | 32 |
| 13 | Effort physique | 1 | 3 |
| 14 | Effort mental | 4 | 18 |
| 15 | Effort émotionnel | 1 | 5 |
| 16 | Conditions de travail | 2 | 7 |
| | **Total** | | **418** (Bande 6: 396–465) |

## Bande 7: Ingénieur d'intégration senior

L'ingénieur d'intégration senior dirige la conception et la livraison d'intégrations complexes entre de nombreux systèmes et organisations, et fixe les normes d'intégration de son domaine.

### Responsabilités

- Diriger la conception technique d'intégrations complexes, comme les dossiers de soins partagés, les résultats et les demandes d'avis entre organisations.
- Rédiger et tenir à jour des profils FHIR, des guides d'implémentation et des normes d'interface pour l'organisation.
- Concevoir des intégrations sécurisées, résilientes et observables, avec des circuits clairs pour traiter les défaillances.
- Travailler avec les responsables de la sécurité clinique pour identifier les dangers liés à l'intégration et veiller à ce que les mesures soient conçues dès le départ et testées.
- Veiller à ce que chaque flux de données repose sur une base légale et des accords de partage convenus, avec les collègues de la gouvernance de l'information.
- Accompagner et faire progresser les ingénieurs d'intégration de l'équipe.

### Compétences

| Compétence | Source | Niveau attendu | Ce que signifie ce niveau |
| --- | --- | --- | --- |
| [Systems integration](../../compétences/#systems-integration) | UK GDaD PCF | Expert | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Programming and build (software engineering)](../../compétences/#programming-and-build-software-engineering) | UK GDaD PCF | Confirmé | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../compétences/#systems-design) | UK GDaD PCF | Confirmé | You can:<br>• design systems characterised by medium levels of risk, impact, and business or technical complexity<br>• select appropriate design standards, methods and tools, and ensure they are applied effectively<br>• review the systems designs of others to ensure the selection of appropriate technology, efficient use of resources and integration of multiple systems and technology |
| [Information security](../../compétences/#information-security) | UK GDaD PCF | Confirmé | You can:<br>• design solutions and services with security controls included, specifically engineered to mitigate security threats |
| [Stakeholder relationship management](../../compétences/#stakeholder-relationship-management) | UK GDaD PCF | Pratique | You can:<br>• identify important stakeholders and communicate with them clearly and regularly<br>• tailor communication to stakeholders' needs and work with them to build relationships while meeting user needs<br>• build and reach consensus with stakeholders<br>• work to improve stakeholder relationships using evidence to explain decisions |
| [Interopérabilité des données de santé](../../compétences/#interopérabilité-des-données-de-santé) | Cette référence | Confirmé | Vous pouvez :<br>• concevoir et développer des intégrations avec FHIR, HL7 version 2 et des modèles de messagerie<br>• rédiger et profiler des ressources FHIR et des guides d'implémentation<br>• résoudre des problèmes complexes de correspondance et de qualité des données entre systèmes |
| [Terminologie et classification cliniques](../../compétences/#terminologie-et-classification-cliniques) | Cette référence | Confirmé | Vous pouvez :<br>• concevoir des modèles de données et des ensembles de référence à l'aide de terminologies cliniques<br>• établir des correspondances entre terminologies et classifications, et expliquer les limites d'une correspondance<br>• conseiller les équipes sur l'usage des terminologies dans les produits et l'analyse |
| [Gouvernance de l'information et protection des données](../../compétences/#gouvernance-de-linformation-et-protection-des-données) | Cette référence | Confirmé | Vous pouvez :<br>• diriger des analyses d'impact relatives à la protection des données et des accords de partage d'informations<br>• conseiller les équipes sur la base légale, le consentement, la confidentialité et la conservation<br>• enquêter sur les incidents et recommander des améliorations |
| [Gestion des risques cliniques](../../compétences/#gestion-des-risques-cliniques) | Cette référence | Pratique | Vous pouvez :<br>• participer à des ateliers d'identification des dangers et contribuer à un registre des dangers<br>• suivre le processus de gestion des risques cliniques dans votre travail<br>• fournir des preuves pour un dossier de sécurité clinique, comme des résultats de tests |
| [Gestion des identités et des accès](../../compétences/#gestion-des-identités-et-des-accès) | Cette référence | Pratique | Vous pouvez :<br>• créer, modifier et supprimer des comptes utilisateurs et des droits d'accès<br>• vérifier les accès par rapport aux règles d'accès fondées sur les rôles |

### Qualifications et expérience habituelles

- Une expérience significative de la conception et du support d'intégrations en santé ou d'autres intégrations complexes, d'un niveau équivalent à un master.

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

## Bande 8a: Ingénieur d'intégration référent

L'ingénieur d'intégration référent dirige l'ingénierie d'intégration de l'organisation, fixe son orientation technique et ses normes, et garantit les intégrations critiques entre de nombreux systèmes.

### Responsabilités

- Diriger l'ingénierie d'intégration dans toute l'organisation, en fixant l'orientation, les modèles et les normes.
- Garantir la conception des intégrations critiques, comme celles qui transportent des résultats, des médicaments ou des alertes.
- Façonner la feuille de route de la plateforme d'intégration avec les architectes, les chefs de produit et les fournisseurs.
- Représenter l'organisation dans les travaux interorganisations d'interopérabilité et de normalisation.
- Encadrer ou diriger les ingénieurs d'intégration et faire grandir la communauté de pratique de l'intégration.

### Compétences

| Compétence | Source | Niveau attendu | Ce que signifie ce niveau |
| --- | --- | --- | --- |
| [Systems integration](../../compétences/#systems-integration) | UK GDaD PCF | Expert | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Systems design](../../compétences/#systems-design) | UK GDaD PCF | Expert | You can:<br>• design systems characterised by high levels of risk, impact, and business or technical complexity<br>• control system design practice within an enterprise or industry architecture<br>• influence industry-based models for the development of new technology applications<br>• develop effective implementation and procurement strategies, consistent with business needs<br>• ensure adherence to relevant technical strategies, policies, standards and practices |
| [Technical design throughout the life cycle](../../compétences/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | Confirmé | You can:<br>• create technical designs characterised by medium risk, impact, and complexity<br>• maintain appropriate quality and architectural coherence of a technical design in response to change<br>• use feedback to optimise and refine technical designs throughout the life cycle |
| [Stakeholder relationship management](../../compétences/#stakeholder-relationship-management) | UK GDaD PCF | Confirmé | You can:<br>• work with the team to develop and maintain an understanding of stakeholders<br>• work with the team to develop and implement stakeholder communications strategies<br>• identify and resolve issues, influence stakeholders and manage relationships effectively<br>• build long-term strategic relationships and communicate clearly and regularly with stakeholders |
| [Leadership and guidance](../../compétences/#leadership-and-guidance) | UK GDaD PCF | Confirmé | You can:<br>• make decisions characterised by medium levels of risk and complexity and recommend decisions as risk and complexity increase<br>• build consensus between services or independent stakeholders<br>• identify problems or issues in the team dynamic and rectify them<br>• engage in varying types of feedback, choosing the right type at the appropriate time and ensuring the discussion and decision stick<br>• bring people together to form a motivated team and help create the right environment for a team to work in<br>• facilitate the best team makeup depending on the situation |
| [Interopérabilité des données de santé](../../compétences/#interopérabilité-des-données-de-santé) | Cette référence | Expert | Vous pouvez :<br>• fixer les normes et la stratégie d'interopérabilité de l'organisation<br>• diriger des travaux de normalisation nationaux ou interorganisations<br>• garantir la conception d'intégrations critiques entre de nombreux systèmes |
| [Terminologie et classification cliniques](../../compétences/#terminologie-et-classification-cliniques) | Cette référence | Confirmé | Vous pouvez :<br>• concevoir des modèles de données et des ensembles de référence à l'aide de terminologies cliniques<br>• établir des correspondances entre terminologies et classifications, et expliquer les limites d'une correspondance<br>• conseiller les équipes sur l'usage des terminologies dans les produits et l'analyse |
| [Gouvernance de l'information et protection des données](../../compétences/#gouvernance-de-linformation-et-protection-des-données) | Cette référence | Confirmé | Vous pouvez :<br>• diriger des analyses d'impact relatives à la protection des données et des accords de partage d'informations<br>• conseiller les équipes sur la base légale, le consentement, la confidentialité et la conservation<br>• enquêter sur les incidents et recommander des améliorations |
| [Gestion des risques cliniques](../../compétences/#gestion-des-risques-cliniques) | Cette référence | Confirmé | Vous pouvez :<br>• diriger l'identification des dangers et l'évaluation des risques d'un produit ou d'un changement<br>• rédiger et tenir à jour des registres des dangers et des rapports de dossier de sécurité clinique<br>• convenir de mesures de maîtrise des risques avec les équipes produit et vérifier qu'elles fonctionnent<br>• conseiller les équipes sur l'application des normes de gestion des risques cliniques |
| [Management des personnes](../../compétences/#management-des-personnes) | Cette référence | Confirmé | Vous pouvez :<br>• encadrer hiérarchiquement une équipe, en fixant des objectifs et en menant les entretiens annuels<br>• soutenir le bien-être et gérer l'assiduité, la performance et la conduite<br>• planifier le développement et la relève de l'équipe |

### Qualifications et expérience habituelles

- Une solide expérience de la direction de l'ingénierie d'intégration de systèmes de santé ou de soins complexes.

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


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
