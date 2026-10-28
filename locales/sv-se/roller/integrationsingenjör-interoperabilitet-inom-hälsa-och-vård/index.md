# Integrationsingenjör (interoperabilitet inom hälsa och vård)

> Detta är en illustrativ referensprofil för en generisk organisation inom digital hälsa och vård. Det är inte en officiell befattningsbeskrivning för någon arbetsgivare, och poängen i arbetsvärderingen är inte en formell värdering.

> Den här texten har översatts från engelska av en AI-assistent och har ännu inte granskats av en modersmålstalare. Citat från ramverket för digitala och datarelaterade yrkesroller i Storbritanniens regering (UK GDaD PCF) och från ESCO står kvar på engelska.

**Familj:** [Programvaruutveckling](../../#programvaruutveckling)  
**Band:** 5, 6, 7, 8a  
**Roll i UK GDaD PCF:** ingen (den här referensen definierar rollen)  
**Yrken i ESCO:** [integration engineer](http://data.europa.eu/esco/occupation/07e60525-1aad-4099-aaf3-2c7014c92212) (ISCO-08 2511); [database developer](http://data.europa.eu/esco/occupation/b11e1742-5e28-4270-b081-b0193d85ee7d) (ISCO-08 2521)

## Sammanfattning

Integrationsingenjörer kopplar samman organisationens kliniska system och verksamhetssystem så att hälso- och vårdinformation flödar tryggt dit den behövs. De utformar, bygger, testar och stöder gränssnitt, API:er och meddelandeflöden med standarder såsom HL7 FHIR och HL7 version 2, mappar data och kliniska koder mellan system och håller integrationer igång i drift.

## I en organisation inom digital hälsa och vård

- Ett förlorat, försenat, duplicerat eller felmatchat meddelande, såsom ett provsvar eller en remiss, kan direkt leda till skada, så integrationsarbete följer processen för klinisk riskhantering.
- Integrationer bär stora mängder konfidentiell hälsoinformation mellan organisationer, så varje flöde behöver en rättslig grund, säker transport och granskningsspår.
- Hälso- och sjukvårdssystem använder många standarder och versioner, från HL7 version 2-meddelanden till HL7 FHIR-API:er och IHE-profiler, ofta med lokala variationer.
- Klinisk betydelse måste överleva resan, så ingenjörer mappar kliniska terminologier såsom SNOMED CT korrekt och matchar patienter pålitligt.
- Många integrationer stöder vården dygnet runt, så de behöver övervakning, larm och tydliga vägar för att lösa misslyckade meddelanden.

## Rollnivåer

| Band | Titel | Nivå i UK GDaD PCF | Tjänstegrader i Storbritanniens statliga förvaltning | Poäng i arbetsvärderingen |
| --- | --- | --- | --- | --- |
| 5 | [Junior integrationsingenjör](#band-5-junior-integrationsingenjör) | — | — | 335 |
| 6 | [Integrationsingenjör](#band-6-integrationsingenjör) | — | — | 418 |
| 7 | [Senior integrationsingenjör](#band-7-senior-integrationsingenjör) | — | — | 477 |
| 8a | [Ledande integrationsingenjör](#band-8a-ledande-integrationsingenjör) | — | — | 551 |

## Band 5: Junior integrationsingenjör

En junior integrationsingenjör bygger, testar och stöder integrationer mellan hälso- och vårdsystem utifrån specifikationer och med vägledning från mer erfarna ingenjörer.

### Ansvarsområden

- Bygga och ändra meddelandemappningar, transformationer och API-anrop utifrån överenskomna specifikationer.
- Testa integrationer mot specifikationer och exempelmeddelanden, inklusive fel- och gränsfall.
- Övervaka meddelandeflöden, utreda misslyckade eller avvisade meddelanden och lösa eller eskalera dem.
- Hantera hälsodata säkert enligt reglerna för informationsstyrning för livedata och testdata.
- Registrera ändringar och testresultat så att de kan användas som evidens för klinisk säkerhet.

### Färdigheter

| Färdighet | Källa | Förväntad nivå | Vad nivån innebär |
| --- | --- | --- | --- |
| [Systems integration](../../färdigheter/#systems-integration) | UK GDaD PCF | Tillämpande | You can:<br>• build and test simple interfaces between systems<br>• work on more complex integration as part of a wider team |
| [Programming and build (software engineering)](../../färdigheter/#programming-and-build-software-engineering) | UK GDaD PCF | Tillämpande | You can:<br>• design, code, test, correct and document simple programs or scripts under the direction of others |
| [Testing](../../färdigheter/#testing) | UK GDaD PCF | Tillämpande | You can:<br>• review requirements and specifications, and define test conditions<br>• identify issues and risks associated with work<br>• analyse and report test activities and results |
| [Service support](../../färdigheter/#service-support) | UK GDaD PCF | Tillämpande | You can:<br>• help fix service faults following agreed procedures<br>• carry out maintenance tasks on service support infrastructure |
| [Information security](../../färdigheter/#information-security) | UK GDaD PCF | Medvetenhet | You can:<br>• explain information security and the security controls available to protect solutions and services |
| [Interoperabilitet för hälsodata](../../färdigheter/#interoperabilitet-för-hälsodata) | Den här referensen | Tillämpande | Du kan:<br>• läsa och använda FHIR-resurser, profiler och API:er<br>• bygga eller testa enkla integrationer under handledning<br>• kontrollera meddelanden mot en specifikation |
| [Klinisk terminologi och klassifikation](../../färdigheter/#klinisk-terminologi-och-klassifikation) | Den här referensen | Medvetenhet | Du kan:<br>• förklara skillnaden mellan en klinisk terminologi och en klassifikation<br>• känna igen vanliga terminologier såsom SNOMED CT och ICD |
| [Informationsstyrning och dataskydd](../../färdigheter/#informationsstyrning-och-dataskydd) | Den här referensen | Tillämpande | Du kan:<br>• tillämpa dataskyddsprinciperna i ditt arbete<br>• bidra till konsekvensbedömningar avseende dataskydd<br>• hantera informationsbegäranden och journaler korrekt |
| [Klinisk riskhantering](../../färdigheter/#klinisk-riskhantering) | Den här referensen | Medvetenhet | Du kan:<br>• förklara hur IT-system inom hälso- och sjukvården kan skada patienter, till exempel genom felaktig, saknad eller försenad information<br>• rapportera ett möjligt kliniskt säkerhetsproblem genom rätt kanal |
| [Förståelse för hälso- och sjukvårdstjänster](../../färdigheter/#förståelse-för-hälso--och-sjukvårdstjänster) | Den här referensen | Medvetenhet | Du kan:<br>• beskriva hälso- och sjukvårdssystemets huvuddelar och de tjänster organisationen stöder<br>• förklara varför patientsäkerhet och sekretess är viktiga i ditt arbete |

### Typiska kvalifikationer och erfarenhet

- En examen i datavetenskap eller ett närliggande ämne, en genomförd lärlingsutbildning eller motsvarande erfarenhet.

### Översikt av bandet

- **Kunskap:** Professionell eller teknisk kunskap, vanligen genom en examen eller motsvarande erfarenhet.
- **Självständighet:** Arbetar mot breda mål inom professionella standarder; planerar sitt eget arbete.
- **Omfattning:** Eget professionellt arbete inom ett team eller en produkt.
- **Ledarskap:** Kan vägleda och granska arbetet hos stödpersonal och lärlingar.
- **Ansvarsskyldighet:** Kvaliteten på det egna professionella arbetet.

### Arbetsvärdering (illustrativ)

| # | Faktor | Nivå | Poäng |
| --- | --- | --- | --- |
| 1 | Kommunikations- och relationsfärdigheter | 4 | 32 |
| 2 | Kunskap, utbildning och erfarenhet | 5 | 120 |
| 3 | Analytiska färdigheter och omdöme | 3 | 27 |
| 4 | Planerings- och organisationsförmåga | 2 | 15 |
| 5 | Fysiska färdigheter | 3 | 27 |
| 6 | Ansvar för patient- och klientvård | 1 | 4 |
| 7 | Ansvar för policy- och tjänsteutveckling | 2 | 12 |
| 8 | Ansvar för ekonomiska och fysiska resurser | 1 | 5 |
| 9 | Ansvar för människor | 1 | 5 |
| 10 | Ansvar för informationsresurser | 4 | 24 |
| 11 | Ansvar för forskning och utveckling | 2 | 12 |
| 12 | Handlingsfrihet | 3 | 21 |
| 13 | Fysisk ansträngning | 2 | 7 |
| 14 | Mental ansträngning | 3 | 12 |
| 15 | Känslomässig ansträngning | 1 | 5 |
| 16 | Arbetsförhållanden | 2 | 7 |
| | **Summa** | | **335** (Band 5: 326–395) |

## Band 6: Integrationsingenjör

En integrationsingenjör utformar, bygger och stöder självständigt integrationer mellan hälso- och vårdsystem och hjälper till att definiera hur system ska utbyta data.

### Ansvarsområden

- Utforma och bygga integrationer, API:er och meddelandeflöden med HL7 FHIR, HL7 version 2 och meddelandemönster.
- Analysera käll- och målsystem och skriva gränssnittsspecifikationer och datamappningar, inklusive kliniska koder.
- Bygga patientmatchning, validering och felhantering så att information når rätt journal.
- Delta i riskworkshoppar och bygga in säkerhetskontroller i integrationer, såsom larm för misslyckade eller försenade meddelanden.
- Arbeta med leverantörer och partnerorganisationer för att testa och driftsätta nya kopplingar.
- Utreda och åtgärda problem i integrationer i drift och handleda juniora integrationsingenjörer.

### Färdigheter

| Färdighet | Källa | Förväntad nivå | Vad nivån innebär |
| --- | --- | --- | --- |
| [Systems integration](../../färdigheter/#systems-integration) | UK GDaD PCF | Erfaren | You can:<br>• define the integration build<br>• co-ordinate build activities across systems<br>• understand how to undertake and support integration testing activities |
| [Programming and build (software engineering)](../../färdigheter/#programming-and-build-software-engineering) | UK GDaD PCF | Erfaren | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../färdigheter/#systems-design) | UK GDaD PCF | Tillämpande | You can:<br>• translate logical designs into physical designs<br>• produce detailed designs<br>• effectively document all work using required standards, methods and tools, including prototyping tools where appropriate<br>• design systems characterised by managed levels of risk, manageable business and technical complexity, and meaningful impact<br>• work with well understood technology and identify appropriate patterns |
| [Service support](../../färdigheter/#service-support) | UK GDaD PCF | Erfaren | You can:<br>• identify, locate and fix service faults |
| [Information security](../../färdigheter/#information-security) | UK GDaD PCF | Tillämpande | You can:<br>• use information security practices and available security controls to contribute to protecting solutions and services |
| [Interoperabilitet för hälsodata](../../färdigheter/#interoperabilitet-för-hälsodata) | Den här referensen | Erfaren | Du kan:<br>• utforma och bygga integrationer med FHIR, HL7 version 2 och meddelandemönster<br>• skriva och profilera FHIR-resurser och implementeringsguider<br>• lösa komplexa mappnings- och datakvalitetsproblem mellan system |
| [Klinisk terminologi och klassifikation](../../färdigheter/#klinisk-terminologi-och-klassifikation) | Den här referensen | Tillämpande | Du kan:<br>• hitta och använda rätt koder för ett dataelement eller ett formulär<br>• använda terminologiwebbläsare och referensmängder |
| [Informationsstyrning och dataskydd](../../färdigheter/#informationsstyrning-och-dataskydd) | Den här referensen | Tillämpande | Du kan:<br>• tillämpa dataskyddsprinciperna i ditt arbete<br>• bidra till konsekvensbedömningar avseende dataskydd<br>• hantera informationsbegäranden och journaler korrekt |
| [Klinisk riskhantering](../../färdigheter/#klinisk-riskhantering) | Den här referensen | Tillämpande | Du kan:<br>• delta i riskworkshoppar och bidra till ett faroregister<br>• följa processen för klinisk riskhantering i ditt arbete<br>• ta fram underlag till ett kliniskt säkerhetsunderlag, till exempel testresultat |
| [Förståelse för hälso- och sjukvårdstjänster](../../färdigheter/#förståelse-för-hälso--och-sjukvårdstjänster) | Den här referensen | Tillämpande | Du kan:<br>• förklara de kliniska arbetsflöden och vårdarbetsflöden som ditt arbete stöder<br>• använda vanliga hälso- och sjukvårdstermer korrekt med kliniska kollegor och kollegor inom vården<br>• känna igen när en förändring kan påverka patientvården och lyfta det |

### Typiska kvalifikationer och erfarenhet

- En examen i datavetenskap eller ett närliggande ämne, eller motsvarande erfarenhet.
- Erfarenhet av att bygga och stödja integrationer mellan produktionssystem.

### Översikt av bandet

- **Kunskap:** Specialistkunskap över en rad förfaranden, uppbyggd genom vidareutbildning eller erfarenhet.
- **Självständighet:** Arbetar självständigt; tolkar policy för det egna området; söker råd i komplexa frågor.
- **Omfattning:** En produkt, en tjänst eller ett arbetsflöde.
- **Ledarskap:** Kan leda ett litet team eller handleda kollegor.
- **Ansvarsskyldighet:** Resultaten av det egna arbetsflödet och kvaliteten på de råd som ges.

### Arbetsvärdering (illustrativ)

| # | Faktor | Nivå | Poäng |
| --- | --- | --- | --- |
| 1 | Kommunikations- och relationsfärdigheter | 4 | 32 |
| 2 | Kunskap, utbildning och erfarenhet | 6 | 156 |
| 3 | Analytiska färdigheter och omdöme | 4 | 42 |
| 4 | Planerings- och organisationsförmåga | 3 | 27 |
| 5 | Fysiska färdigheter | 3 | 27 |
| 6 | Ansvar för patient- och klientvård | 1 | 4 |
| 7 | Ansvar för policy- och tjänsteutveckling | 2 | 12 |
| 8 | Ansvar för ekonomiska och fysiska resurser | 1 | 5 |
| 9 | Ansvar för människor | 2 | 12 |
| 10 | Ansvar för informationsresurser | 4 | 24 |
| 11 | Ansvar för forskning och utveckling | 2 | 12 |
| 12 | Handlingsfrihet | 4 | 32 |
| 13 | Fysisk ansträngning | 1 | 3 |
| 14 | Mental ansträngning | 4 | 18 |
| 15 | Känslomässig ansträngning | 1 | 5 |
| 16 | Arbetsförhållanden | 2 | 7 |
| | **Summa** | | **418** (Band 6: 396–465) |

## Band 7: Senior integrationsingenjör

En senior integrationsingenjör leder utformningen och leveransen av komplexa integrationer över många system och organisationer och fastställer integrationsstandarder för sitt område.

### Ansvarsområden

- Leda den tekniska utformningen av komplexa integrationer, såsom delade vårdjournaler, resultat och remisser över organisationer.
- Skriva och underhålla FHIR-profiler, implementeringsguider och gränssnittsstandarder för organisationen.
- Utforma integrationer så att de är säkra, motståndskraftiga och observerbara, med tydliga vägar för att lösa fel.
- Arbeta med kliniska säkerhetsansvariga för att identifiera integrationsfaror och säkerställa att kontroller utformas in och testas.
- Se till att varje dataflöde har en överenskommen rättslig grund och arrangemang för datadelning, tillsammans med kollegor inom informationsstyrning.
- Coacha och utveckla integrationsingenjörer i teamet.

### Färdigheter

| Färdighet | Källa | Förväntad nivå | Vad nivån innebär |
| --- | --- | --- | --- |
| [Systems integration](../../färdigheter/#systems-integration) | UK GDaD PCF | Expert | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Programming and build (software engineering)](../../färdigheter/#programming-and-build-software-engineering) | UK GDaD PCF | Erfaren | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../färdigheter/#systems-design) | UK GDaD PCF | Erfaren | You can:<br>• design systems characterised by medium levels of risk, impact, and business or technical complexity<br>• select appropriate design standards, methods and tools, and ensure they are applied effectively<br>• review the systems designs of others to ensure the selection of appropriate technology, efficient use of resources and integration of multiple systems and technology |
| [Information security](../../färdigheter/#information-security) | UK GDaD PCF | Erfaren | You can:<br>• design solutions and services with security controls included, specifically engineered to mitigate security threats |
| [Stakeholder relationship management](../../färdigheter/#stakeholder-relationship-management) | UK GDaD PCF | Tillämpande | You can:<br>• identify important stakeholders and communicate with them clearly and regularly<br>• tailor communication to stakeholders' needs and work with them to build relationships while meeting user needs<br>• build and reach consensus with stakeholders<br>• work to improve stakeholder relationships using evidence to explain decisions |
| [Interoperabilitet för hälsodata](../../färdigheter/#interoperabilitet-för-hälsodata) | Den här referensen | Erfaren | Du kan:<br>• utforma och bygga integrationer med FHIR, HL7 version 2 och meddelandemönster<br>• skriva och profilera FHIR-resurser och implementeringsguider<br>• lösa komplexa mappnings- och datakvalitetsproblem mellan system |
| [Klinisk terminologi och klassifikation](../../färdigheter/#klinisk-terminologi-och-klassifikation) | Den här referensen | Erfaren | Du kan:<br>• utforma datamodeller och referensmängder med kliniska terminologier<br>• mappa mellan terminologier och klassifikationer, och förklara en mappnings begränsningar<br>• ge team råd om användning av terminologi i produkter och analys |
| [Informationsstyrning och dataskydd](../../färdigheter/#informationsstyrning-och-dataskydd) | Den här referensen | Erfaren | Du kan:<br>• leda konsekvensbedömningar avseende dataskydd och avtal om informationsdelning<br>• ge team råd om rättslig grund, samtycke, sekretess och gallring<br>• utreda incidenter och rekommendera förbättringar |
| [Klinisk riskhantering](../../färdigheter/#klinisk-riskhantering) | Den här referensen | Tillämpande | Du kan:<br>• delta i riskworkshoppar och bidra till ett faroregister<br>• följa processen för klinisk riskhantering i ditt arbete<br>• ta fram underlag till ett kliniskt säkerhetsunderlag, till exempel testresultat |
| [Identitets- och åtkomsthantering](../../färdigheter/#identitets--och-åtkomsthantering) | Den här referensen | Tillämpande | Du kan:<br>• skapa, ändra och ta bort användarkonton och behörigheter<br>• kontrollera åtkomst mot regler för rollbaserad åtkomst |

### Typiska kvalifikationer och erfarenhet

- Betydande erfarenhet av att utforma och stödja integrationer inom hälso- och sjukvården eller andra komplexa integrationer, på en nivå motsvarande en masterexamen.

### Översikt av bandet

- **Kunskap:** Högt utvecklad specialistkunskap, vanligen på masternivå eller motsvarande erfarenhet.
- **Självständighet:** Arbetar enligt organisationens policy; avgör hur resultat uppnås; är den expert andra rådfrågar.
- **Omfattning:** Flera produkter eller tjänster, eller en specialistfunktion.
- **Ledarskap:** Leder ett team eller ett professionellt praxisområde.
- **Ansvarsskyldighet:** Leverans av en tjänst eller specialistfunktion, och dess budget om en sådan finns.

### Arbetsvärdering (illustrativ)

| # | Faktor | Nivå | Poäng |
| --- | --- | --- | --- |
| 1 | Kommunikations- och relationsfärdigheter | 4 | 32 |
| 2 | Kunskap, utbildning och erfarenhet | 7 | 196 |
| 3 | Analytiska färdigheter och omdöme | 4 | 42 |
| 4 | Planerings- och organisationsförmåga | 3 | 27 |
| 5 | Fysiska färdigheter | 3 | 27 |
| 6 | Ansvar för patient- och klientvård | 1 | 4 |
| 7 | Ansvar för policy- och tjänsteutveckling | 3 | 21 |
| 8 | Ansvar för ekonomiska och fysiska resurser | 1 | 5 |
| 9 | Ansvar för människor | 2 | 12 |
| 10 | Ansvar för informationsresurser | 5 | 34 |
| 11 | Ansvar för forskning och utveckling | 2 | 12 |
| 12 | Handlingsfrihet | 4 | 32 |
| 13 | Fysisk ansträngning | 1 | 3 |
| 14 | Mental ansträngning | 4 | 18 |
| 15 | Känslomässig ansträngning | 1 | 5 |
| 16 | Arbetsförhållanden | 2 | 7 |
| | **Summa** | | **477** (Band 7: 466–539) |

## Band 8a: Ledande integrationsingenjör

En ledande integrationsingenjör leder organisationens integrationsutveckling, fastställer dess tekniska riktning och standarder och kvalitetssäkrar kritiska integrationer över många system.

### Ansvarsområden

- Leda integrationsutvecklingen i hela organisationen och sätta riktning, mönster och standarder.
- Kvalitetssäkra utformningen av kritiska integrationer, såsom sådana som bär resultat, läkemedel eller larm.
- Forma färdplanen för integrationsplattformen tillsammans med arkitekter, produktchefer och leverantörer.
- Företräda organisationen i arbete med interoperabilitet och standarder över organisationer.
- Ha linjeansvar för eller leda integrationsingenjörer och bygga praktikgemenskapen för integration.

### Färdigheter

| Färdighet | Källa | Förväntad nivå | Vad nivån innebär |
| --- | --- | --- | --- |
| [Systems integration](../../färdigheter/#systems-integration) | UK GDaD PCF | Expert | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Systems design](../../färdigheter/#systems-design) | UK GDaD PCF | Expert | You can:<br>• design systems characterised by high levels of risk, impact, and business or technical complexity<br>• control system design practice within an enterprise or industry architecture<br>• influence industry-based models for the development of new technology applications<br>• develop effective implementation and procurement strategies, consistent with business needs<br>• ensure adherence to relevant technical strategies, policies, standards and practices |
| [Technical design throughout the life cycle](../../färdigheter/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | Erfaren | You can:<br>• create technical designs characterised by medium risk, impact, and complexity<br>• maintain appropriate quality and architectural coherence of a technical design in response to change<br>• use feedback to optimise and refine technical designs throughout the life cycle |
| [Stakeholder relationship management](../../färdigheter/#stakeholder-relationship-management) | UK GDaD PCF | Erfaren | You can:<br>• work with the team to develop and maintain an understanding of stakeholders<br>• work with the team to develop and implement stakeholder communications strategies<br>• identify and resolve issues, influence stakeholders and manage relationships effectively<br>• build long-term strategic relationships and communicate clearly and regularly with stakeholders |
| [Leadership and guidance](../../färdigheter/#leadership-and-guidance) | UK GDaD PCF | Erfaren | You can:<br>• make decisions characterised by medium levels of risk and complexity and recommend decisions as risk and complexity increase<br>• build consensus between services or independent stakeholders<br>• identify problems or issues in the team dynamic and rectify them<br>• engage in varying types of feedback, choosing the right type at the appropriate time and ensuring the discussion and decision stick<br>• bring people together to form a motivated team and help create the right environment for a team to work in<br>• facilitate the best team makeup depending on the situation |
| [Interoperabilitet för hälsodata](../../färdigheter/#interoperabilitet-för-hälsodata) | Den här referensen | Expert | Du kan:<br>• fastställa standarder och strategi för interoperabilitet i organisationen<br>• leda nationellt arbete med standarder eller arbete över organisationsgränser<br>• kvalitetssäkra utformningen av kritiska integrationer över många system |
| [Klinisk terminologi och klassifikation](../../färdigheter/#klinisk-terminologi-och-klassifikation) | Den här referensen | Erfaren | Du kan:<br>• utforma datamodeller och referensmängder med kliniska terminologier<br>• mappa mellan terminologier och klassifikationer, och förklara en mappnings begränsningar<br>• ge team råd om användning av terminologi i produkter och analys |
| [Informationsstyrning och dataskydd](../../färdigheter/#informationsstyrning-och-dataskydd) | Den här referensen | Erfaren | Du kan:<br>• leda konsekvensbedömningar avseende dataskydd och avtal om informationsdelning<br>• ge team råd om rättslig grund, samtycke, sekretess och gallring<br>• utreda incidenter och rekommendera förbättringar |
| [Klinisk riskhantering](../../färdigheter/#klinisk-riskhantering) | Den här referensen | Erfaren | Du kan:<br>• leda identifiering av faror och riskbedömning för en produkt eller en förändring<br>• skriva och underhålla faroregister och rapporter om kliniska säkerhetsunderlag<br>• komma överens med produktteam om riskkontroller och kontrollera att de fungerar<br>• ge team råd om att tillämpa standarder för klinisk riskhantering |
| [Personalledning](../../färdigheter/#personalledning) | Den här referensen | Erfaren | Du kan:<br>• ha linjeansvar för ett team, sätta mål och hålla medarbetarsamtal<br>• stödja välbefinnande och hantera närvaro, prestation och uppförande<br>• planera teamets utveckling och successioner |

### Typiska kvalifikationer och erfarenhet

- Omfattande erfarenhet av att leda integrationsutveckling för komplexa hälso- och vårdsystem.

### Översikt av bandet

- **Kunskap:** Expertkunskap om en disciplin och dess ledning.
- **Självständighet:** Tolkar organisationens policy för en tjänst; anger teamets riktning.
- **Omfattning:** Ett tjänsteområde eller en disciplin i hela organisationen.
- **Ledarskap:** Leder ett team, eller leder en disciplin utan linjeansvar.
- **Ansvarsskyldighet:** Ett tjänsteområde, dess personal och dess budget.

### Arbetsvärdering (illustrativ)

| # | Faktor | Nivå | Poäng |
| --- | --- | --- | --- |
| 1 | Kommunikations- och relationsfärdigheter | 5 | 45 |
| 2 | Kunskap, utbildning och erfarenhet | 7 | 196 |
| 3 | Analytiska färdigheter och omdöme | 5 | 60 |
| 4 | Planerings- och organisationsförmåga | 4 | 42 |
| 5 | Fysiska färdigheter | 2 | 15 |
| 6 | Ansvar för patient- och klientvård | 1 | 4 |
| 7 | Ansvar för policy- och tjänsteutveckling | 4 | 32 |
| 8 | Ansvar för ekonomiska och fysiska resurser | 2 | 12 |
| 9 | Ansvar för människor | 3 | 21 |
| 10 | Ansvar för informationsresurser | 5 | 34 |
| 11 | Ansvar för forskning och utveckling | 2 | 12 |
| 12 | Handlingsfrihet | 5 | 45 |
| 13 | Fysisk ansträngning | 1 | 3 |
| 14 | Mental ansträngning | 4 | 18 |
| 15 | Känslomässig ansträngning | 1 | 5 |
| 16 | Arbetsförhållanden | 2 | 7 |
| | **Summa** | | **551** (Band 8a: 540–584) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
