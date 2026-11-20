# डेटा आर्किटेक्ट

> यह एक सामान्य डिजिटल स्वास्थ्य सेवा संगठन के लिए एक उदाहरणात्मक संदर्भ प्रोफ़ाइल है। यह किसी भी नियोक्ता का आधिकारिक कार्य-विवरण नहीं है, और इसके कार्य-मूल्यांकन अंक औपचारिक मूल्यांकन नहीं हैं।

> इस पाठ का अंग्रेज़ी से अनुवाद एक कृत्रिम बुद्धिमत्ता सहायक ने किया है, और किसी मूल हिन्दी भाषी ने अभी तक इसकी समीक्षा नहीं की है। यूके सरकार के डिजिटल और डेटा पेशा क्षमता ढाँचे (UK GDaD PCF) और ESCO के उद्धरण अंग्रेज़ी में ही रखे गए हैं।

**परिवार:** [आर्किटेक्चर](../../#आर्किटेक्चर)  
**बैंड:** 8a, 8b, 8c  
**UK GDaD PCF भूमिका:** [Data architect](https://understand-digital-data-roles-skills.service.gov.uk/role/data-architect/)  
**ESCO व्यवसाय:** [database designer](http://data.europa.eu/esco/occupation/8d9ec84d-cf2d-4179-87bc-335cda54a427) (ISCO-08 2521); [data warehouse designer](http://data.europa.eu/esco/occupation/1562c7a3-c7d9-419d-b9b6-db26610bcf84) (ISCO-08 2521)

## सारांश

डेटा आर्किटेक्ट डिज़ाइन करते हैं कि संगठन अपने स्वास्थ्य और देखभाल डेटा को कैसे संरचित, संग्रहीत, स्थानांतरित और शासित करता है, ताकि उसका प्रत्यक्ष देखभाल, सेवा योजना और अनुसंधान के लिए सुरक्षित उपयोग हो सके। वे डेटा मॉडल, डेटा प्लेटफ़ॉर्म और डेटा प्रवाह डिज़ाइन करते हैं, डेटा मानक तय करते हैं, और सुनिश्चित करते हैं कि क्लिनिकल अर्थ, गुणवत्ता और गोपनीयता शुरू से अंत तक बनी रहे।

## एक डिजिटल स्वास्थ्य सेवा संगठन में

- स्वास्थ्य डेटा को अपना क्लिनिकल अर्थ बनाए रखना चाहिए, इसलिए डेटा मॉडल SNOMED CT जैसी क्लिनिकल शब्दावलियों और ICD जैसे वर्गीकरणों का उपयोग करते हैं।
- प्रत्यक्ष देखभाल के लिए उपयोग होने वाले डेटा और योजना या अनुसंधान के लिए उपयोग होने वाले डेटा के विधिक आधार अलग होते हैं, इसलिए आर्किटेक्ट पृथक्करण, डी-आइडेंटिफ़िकेशन और नियंत्रित पहुँच के लिए डिज़ाइन करते हैं।
- डेटा कई क्लिनिकल और देखभाल प्रणालियों से अलग-अलग गुणवत्ता के साथ आता है, इसलिए आर्किटेक्ट डेटा गुणवत्ता जाँच, रोगी मिलान और डेटा वंशावली के लिए डिज़ाइन करते हैं।
- साझा देखभाल अभिलेख और डेटा विनिमय HL7 FHIR संसाधनों और सहमत राष्ट्रीय या अंतरराष्ट्रीय डेटासेट जैसे साझा मॉडलों पर निर्भर करते हैं।
- अभिलेखों को लंबी अवधि तक रखना होता है, इसलिए डिज़ाइनों में संग्रहण और ऐतिहासिक डेटा तक पहुँच की योजना होनी चाहिए।

## UK GDaD PCF भूमिका विवरण (अंग्रेज़ी मूल)

> A data architect sets the vision for the organisation’s use of data, through data design, to ensure that data is managed properly and meets the organisation’s needs.

## भूमिका स्तर

| बैंड | शीर्षक | UK GDaD PCF स्तर | यूके सिविल सेवा ग्रेड | कार्य-मूल्यांकन अंक |
| --- | --- | --- | --- | --- |
| 8a | [डेटा आर्किटेक्ट](#बैंड-8a-डेटा-आर्किटेक्ट) | Data architect | SEO/G7 | 560 |
| 8b | [वरिष्ठ डेटा आर्किटेक्ट](#बैंड-8b-वरिष्ठ-डेटा-आर्किटेक्ट) | Senior data architect | G7/G6 | 613 |
| 8c | [मुख्य डेटा आर्किटेक्ट](#बैंड-8c-मुख्य-डेटा-आर्किटेक्ट) | Chief data architect | G6 | 662 |

## बैंड 8a: डेटा आर्किटेक्ट

**UK GDaD PCF स्तर: Data architect**

> A data architect designs and builds data models to fulfil the strategic data needs of the organisation, as defined by chief data architects.
> 
> At this role level, you will:
> - design, support and provide guidance for the upgrade, management, decommission and archive of data in compliance with data policy
> - provide input into data dictionaries
> - define and maintain the data technology architecture, including metadata, integration and business intelligence or data warehouse architecture

### ज़िम्मेदारियाँ

- आवश्यकता होने पर क्लिनिकल शब्दावलियों का उपयोग करते हुए क्लिनिकल और परिचालन डेटा के लिए तार्किक और भौतिक डेटा मॉडल डिज़ाइन करना।
- डेटा वेयरहाउस, लेकहाउस और इंटीग्रेशन परतों जैसे डेटा प्रवाह और डेटा प्लेटफ़ॉर्म घटक डिज़ाइन करना।
- अपने क्षेत्र के डेटासेट के लिए मेटाडेटा, डेटा शब्दकोश प्रविष्टियाँ और वंशावली परिभाषित करना।
- डी-आइडेंटिफ़िकेशन और पहुँच नियंत्रण डिज़ाइन करना ताकि डेटा का उपयोग केवल उसके विधिसम्मत उद्देश्य के लिए हो।
- ख़राब डेटा के संरचनात्मक कारणों को ठीक करने के लिए डेटा गुणवत्ता और क्लिनिकल कोडिंग सहकर्मियों के साथ काम करना।
- डेटा मॉडल और मानकों पर डेटा इंजीनियरों और विश्लेषकों का मार्गदर्शन करना।

### कौशल

| कौशल | स्रोत | अपेक्षित स्तर | इस स्तर का अर्थ |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../कौशल/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | कार्यरत | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Communicating data](../../कौशल/#communicating-data) | UK GDaD PCF | जागरूकता | You can:<br>• show an awareness that data needs to be aligned to the needs of the end user<br>• create basic visuals and presentations |
| [Data analysis and synthesis](../../कौशल/#data-analysis-and-synthesis) | UK GDaD PCF | कार्यरत | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../कौशल/#data-governance-data-architect) | UK GDaD PCF | कार्यरत | You can:<br>• understand what data governance is required<br>• take responsibility for the assurance of data solutions and make recommendations to ensure compliance |
| [Data innovation](../../कौशल/#data-innovation) | UK GDaD PCF | जागरूकता | You can:<br>• develop a basic understanding of an unfamiliar or emerging technology, or a familiar technology in a new data context, with guidance<br>• share what you learn with colleagues, including how it could help deliver more value from data |
| [Data modelling](../../कौशल/#data-modelling) | UK GDaD PCF | कार्यरत | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Data standards](../../कौशल/#data-standards) | UK GDaD PCF | कार्यरत | You can:<br>• use data policies, processes and standards effectively<br>• work with subject matter experts to develop standards, policies and guidance to protect data<br>• monitor compliance with policies and standards in a team and take action if needed<br>• analyse the impact if a standard is breached |
| [Metadata management](../../कौशल/#metadata-management) | UK GDaD PCF | कार्यरत | You can:<br>• use metadata repositories to complete complex tasks such as data and systems integration impact analysis<br>• maintain a metadata repository to ensure information remains accurate and up to date |
| [Problem management](../../कौशल/#problem-management) | UK GDaD PCF | कार्यरत | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Strategic thinking](../../कौशल/#strategic-thinking) | UK GDaD PCF | जागरूकता | You can:<br>• explain the strategic context of your work and why it is important<br>• support strategic planning in an administrative capacity |
| [Turning business problems into data design](../../कौशल/#turning-business-problems-into-data-design) | UK GDaD PCF | कार्यरत | You can:<br>• design data architecture by dealing with specific business problems and aligning it to enterprise-wide standards and principles<br>• work within the context of well understood architecture, and identify appropriate patterns |
| [स्वास्थ्य और देखभाल सेवाओं की समझ](../../कौशल/#स्वास्थ्य-और-देखभाल-सेवाओं-की-समझ) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• उन क्लिनिकल और देखभाल कार्यप्रवाहों को समझाना जिनमें आपका काम सहायक है<br>• क्लिनिकल और देखभाल सहकर्मियों के साथ सामान्य स्वास्थ्य सेवा शब्दों का सही प्रयोग करना<br>• पहचानना कि कब कोई परिवर्तन रोगी देखभाल को प्रभावित कर सकता है, और उसे उठाना |
| [क्लिनिकल शब्दावली और वर्गीकरण](../../कौशल/#क्लिनिकल-शब्दावली-और-वर्गीकरण) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• किसी डेटा आइटम या फ़ॉर्म के लिए सही कोड खोजना और उपयोग करना<br>• शब्दावली ब्राउज़र और संदर्भ सेट का उपयोग करना |
| [स्वास्थ्य डेटा अंतर-संचालनीयता](../../कौशल/#स्वास्थ्य-डेटा-अंतर-संचालनीयता) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• FHIR, HL7 संस्करण 2 और संदेश पैटर्न का उपयोग करके इंटीग्रेशन डिज़ाइन करना और बनाना<br>• FHIR संसाधन और कार्यान्वयन गाइड लिखना और उनकी प्रोफ़ाइल बनाना<br>• प्रणालियों के बीच जटिल मैपिंग और डेटा गुणवत्ता समस्याओं को सुलझाना |
| [सूचना शासन और डेटा संरक्षण](../../कौशल/#सूचना-शासन-और-डेटा-संरक्षण) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• डेटा संरक्षण प्रभाव आकलनों और सूचना साझाकरण समझौतों का नेतृत्व करना<br>• विधिक आधार, सहमति, गोपनीयता और प्रतिधारण पर टीमों को सलाह देना<br>• घटनाओं की जाँच करना और सुधारों की सिफ़ारिश करना |
| [डेटा गुणवत्ता प्रबंधन](../../कौशल/#डेटा-गुणवत्ता-प्रबंधन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• डेटा गुणवत्ता जाँच चलाना और त्रुटियाँ सुधारना<br>• सहकर्मियों को डेटा गुणवत्ता रिपोर्ट समझाना |

### सामान्य योग्यताएँ और अनुभव

- डेटा मॉडलिंग और डेटा प्लेटफ़ॉर्म डिज़ाइन का पर्याप्त अनुभव, मास्टर डिग्री के समकक्ष स्तर पर।

### बैंड की रूपरेखा

- **ज्ञान:** किसी विधा और उसके प्रबंधन का विशेषज्ञ ज्ञान।
- **स्वायत्तता:** किसी सेवा के लिए संगठन की नीति की व्याख्या करता है; टीम की दिशा तय करता है।
- **दायरा:** एक सेवा क्षेत्र, या पूरे संगठन में एक विधा।
- **नेतृत्व:** एक टीम का प्रबंधन करता है, या लाइन प्रबंधन के बिना किसी विधा का नेतृत्व करता है।
- **जवाबदेही:** एक सेवा क्षेत्र, उसके कर्मचारी और उसका बजट।

### कार्य-मूल्यांकन (उदाहरणात्मक)

| # | कारक | स्तर | अंक |
| --- | --- | --- | --- |
| 1 | संचार और संबंध कौशल | 5 | 45 |
| 2 | ज्ञान, प्रशिक्षण और अनुभव | 7 | 196 |
| 3 | विश्लेषण और निर्णय कौशल | 5 | 60 |
| 4 | योजना और संगठन कौशल | 4 | 42 |
| 5 | शारीरिक कौशल | 2 | 15 |
| 6 | रोगी और सेवार्थी देखभाल की ज़िम्मेदारी | 1 | 4 |
| 7 | नीति और सेवा विकास की ज़िम्मेदारी | 4 | 32 |
| 8 | वित्तीय और भौतिक संसाधनों की ज़िम्मेदारी | 2 | 12 |
| 9 | लोगों की ज़िम्मेदारी | 3 | 21 |
| 10 | सूचना संसाधनों की ज़िम्मेदारी | 5 | 34 |
| 11 | अनुसंधान और विकास की ज़िम्मेदारी | 3 | 21 |
| 12 | कार्य करने की स्वतंत्रता | 5 | 45 |
| 13 | शारीरिक प्रयास | 1 | 3 |
| 14 | मानसिक प्रयास | 4 | 18 |
| 15 | भावनात्मक प्रयास | 1 | 5 |
| 16 | कार्य परिस्थितियाँ | 2 | 7 |
| | **कुल** | | **560** (बैंड 8a: 540–584) |

UK GDaD PCF ग्रेड सुझाव (बैंड 7) से ऊँचे बैंड पर: स्वास्थ्य क्षेत्र के विज्ञापन इस भूमिका को बैंड 8a पर रखते हैं। योजना, नीति और कार्य करने की स्वतंत्रता का अंक बैंड 7 प्रोफ़ाइल से ऊपर है क्योंकि यह पद कई सेवाओं द्वारा उपयोग किए जाने वाले डेटा प्लेटफ़ॉर्म और नियंत्रण डिज़ाइन करता है।

## बैंड 8b: वरिष्ठ डेटा आर्किटेक्ट

**UK GDaD PCF स्तर: Senior data architect**

> A senior data architect delivers the vision for the organisation as set by the chief data architect.
> 
> At this role level, you will:
> - design data models and metadata systems
> - help chief data architects to interpret an organisation’s needs
> - provide oversight and advice to other data architects who are designing and producing data artefacts
> - design and support the management of data dictionaries
> - make sure that your teams are working to the standards set for the organisation by the chief data architects
> - work with technical architects to make sure that an organisation’s systems are designed in accordance with the appropriate data architecture

### ज़िम्मेदारियाँ

- साझा देखभाल अभिलेख या एनालिटिक्स प्लेटफ़ॉर्म जैसे किसी प्रमुख क्षेत्र का डेटा आर्किटेक्चर डिज़ाइन करना।
- सुनिश्चित करना कि सभी टीमों के डेटा डिज़ाइन संगठन के डेटा मानकों और मॉडलों का पालन करें।
- मानकों, नियंत्रणों और डेटा साझाकरण समझौतों सहित साझेदार संगठनों के साथ डेटा साझा करने का तरीक़ा डिज़ाइन करना।
- नए डिज़ाइनों के डेटा जोखिमों पर सूचना शासन और क्लिनिकल सुरक्षा सहकर्मियों को सलाह देना।
- डेटा आर्किटेक्टों के काम की समीक्षा और मार्गदर्शन करना।

### कौशल

| कौशल | स्रोत | अपेक्षित स्तर | इस स्तर का अर्थ |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../कौशल/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Communicating data](../../कौशल/#communicating-data) | UK GDaD PCF | कार्यरत | You can:<br>• understand the appropriate media to communicate findings<br>• shape communications for the audience |
| [Data analysis and synthesis](../../कौशल/#data-analysis-and-synthesis) | UK GDaD PCF | कार्यरत | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../कौशल/#data-governance-data-architect) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• evolve and define data governance<br>• take responsibility for supporting and collaborating around wider governance<br>• assure and integrate data services to meet the needs of multiple business services<br>• work proactively to ensure the organisation designs architecture that considers data |
| [Data innovation](../../कौशल/#data-innovation) | UK GDaD PCF | कार्यरत | You can:<br>• experiment with unfamiliar and emerging technologies, or familiar technologies in new data contexts, with guidance<br>• share what you learn with the team, explaining potential benefits, risks, and practical considerations<br>• identify opportunities to apply technology to improve data processes or outcomes in an operational setting or the wider organisation |
| [Data modelling](../../कौशल/#data-modelling) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• produce relevant data models across multiple subject areas<br>• explain which models to use for which purpose<br>• understand industry-recognised data modelling patterns and standards, and when to apply them<br>• compare and align different data models |
| [Data standards](../../कौशल/#data-standards) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• create data standards for different subjects and ensure senior leaders understand them<br>• work with subject matter experts across the organisation to introduce data standards best practice<br>• monitor compliance with policies and standards in the organisation<br>• make recommendations about how the organisation should resolve breaches of standards |
| [Metadata management](../../कौशल/#metadata-management) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../कौशल/#problem-management) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• ensure that the right actions are taken to investigate, resolve and anticipate problems<br>• co-ordinate the team to investigate problems, implement solutions and take preventive measures |
| [Strategic thinking](../../कौशल/#strategic-thinking) | UK GDaD PCF | कार्यरत | You can:<br>• work within a strategic context and communicate how activities meet strategic goals<br>• contribute to the development of strategy and policies |
| [Turning business problems into data design](../../कौशल/#turning-business-problems-into-data-design) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• design data architecture that deals with problems spanning different business areas<br>• identify links between problems to devise common solutions<br>• work across multiple subject areas, or a single large or complicated subject area<br>• produce appropriate patterns |
| [स्वास्थ्य और देखभाल सेवाओं की समझ](../../कौशल/#स्वास्थ्य-और-देखभाल-सेवाओं-की-समझ) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• विश्लेषण करना कि कोई सेवा विभिन्न संगठनों के देखभाल मार्गों में कैसे बैठती है<br>• डिजिटल सेवाओं को आकार देने के लिए चिकित्सकों, देखभाल कर्मचारियों और रोगियों के साथ काम करना<br>• देखभाल, सुरक्षा और कर्मचारियों के कार्यभार पर डिजिटल निर्णयों का प्रभाव समझाना |
| [क्लिनिकल शब्दावली और वर्गीकरण](../../कौशल/#क्लिनिकल-शब्दावली-और-वर्गीकरण) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• क्लिनिकल शब्दावलियों का उपयोग करके डेटा मॉडल और संदर्भ सेट डिज़ाइन करना<br>• शब्दावलियों और वर्गीकरणों के बीच मैपिंग करना, और मैपिंग की सीमाएँ समझाना<br>• उत्पादों और एनालिटिक्स में शब्दावली के उपयोग पर टीमों को सलाह देना |
| [स्वास्थ्य डेटा अंतर-संचालनीयता](../../कौशल/#स्वास्थ्य-डेटा-अंतर-संचालनीयता) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• FHIR, HL7 संस्करण 2 और संदेश पैटर्न का उपयोग करके इंटीग्रेशन डिज़ाइन करना और बनाना<br>• FHIR संसाधन और कार्यान्वयन गाइड लिखना और उनकी प्रोफ़ाइल बनाना<br>• प्रणालियों के बीच जटिल मैपिंग और डेटा गुणवत्ता समस्याओं को सुलझाना |
| [सूचना शासन और डेटा संरक्षण](../../कौशल/#सूचना-शासन-और-डेटा-संरक्षण) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• डेटा संरक्षण प्रभाव आकलनों और सूचना साझाकरण समझौतों का नेतृत्व करना<br>• विधिक आधार, सहमति, गोपनीयता और प्रतिधारण पर टीमों को सलाह देना<br>• घटनाओं की जाँच करना और सुधारों की सिफ़ारिश करना |
| [डेटा गुणवत्ता प्रबंधन](../../कौशल/#डेटा-गुणवत्ता-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• डेटा गुणवत्ता नियम और माप परिभाषित करना<br>• ख़राब गुणवत्ता के मूल कारणों को ठीक करने के लिए डेटा प्रदाताओं के साथ काम करना |
| [क्लिनिकल जोखिम प्रबंधन](../../कौशल/#क्लिनिकल-जोखिम-प्रबंधन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• ख़तरा कार्यशालाओं में भाग लेना और ख़तरा लॉग में योगदान देना<br>• अपने काम के लिए क्लिनिकल जोखिम प्रबंधन प्रक्रिया का पालन करना<br>• क्लिनिकल सुरक्षा केस के लिए परीक्षण परिणाम जैसे साक्ष्य देना |
| [लोगों का प्रबंधन](../../कौशल/#लोगों-का-प्रबंधन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• दैनिक काम का पर्यवेक्षण करना और प्रतिक्रिया देना<br>• भर्ती और प्रारंभिक प्रशिक्षण में भाग लेना<br>• नियमित रूप से आमने-सामने बातचीत करना |

### सामान्य योग्यताएँ और अनुभव

- जटिल संगठनों के लिए डेटा आर्किटेक्चर का व्यापक अनुभव।

### बैंड की रूपरेखा

- **ज्ञान:** कई विधाओं या एक बड़ी सेवा का विशेषज्ञ ज्ञान।
- **स्वायत्तता:** एक बड़े क्षेत्र के लिए नीति और रणनीति को आकार देता है।
- **दायरा:** कई सेवाएँ या टीमें, या प्रधान स्तर की एक विधा।
- **नेतृत्व:** प्रबंधकों का प्रबंधन करता है, या किसी विधा में प्रधान प्राधिकारी होता है।
- **जवाबदेही:** कई सेवाएँ, उनके कर्मचारी और उनके बजट।

### कार्य-मूल्यांकन (उदाहरणात्मक)

| # | कारक | स्तर | अंक |
| --- | --- | --- | --- |
| 1 | संचार और संबंध कौशल | 5 | 45 |
| 2 | ज्ञान, प्रशिक्षण और अनुभव | 8 | 240 |
| 3 | विश्लेषण और निर्णय कौशल | 5 | 60 |
| 4 | योजना और संगठन कौशल | 4 | 42 |
| 5 | शारीरिक कौशल | 2 | 15 |
| 6 | रोगी और सेवार्थी देखभाल की ज़िम्मेदारी | 1 | 4 |
| 7 | नीति और सेवा विकास की ज़िम्मेदारी | 4 | 32 |
| 8 | वित्तीय और भौतिक संसाधनों की ज़िम्मेदारी | 3 | 21 |
| 9 | लोगों की ज़िम्मेदारी | 3 | 21 |
| 10 | सूचना संसाधनों की ज़िम्मेदारी | 5 | 34 |
| 11 | अनुसंधान और विकास की ज़िम्मेदारी | 3 | 21 |
| 12 | कार्य करने की स्वतंत्रता | 5 | 45 |
| 13 | शारीरिक प्रयास | 1 | 3 |
| 14 | मानसिक प्रयास | 4 | 18 |
| 15 | भावनात्मक प्रयास | 1 | 5 |
| 16 | कार्य परिस्थितियाँ | 2 | 7 |
| | **कुल** | | **613** (बैंड 8b: 585–629) |

## बैंड 8c: मुख्य डेटा आर्किटेक्ट

**UK GDaD PCF स्तर: Chief data architect**

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

### ज़िम्मेदारियाँ

- संगठन की डेटा रणनीति के अनुरूप उसका डेटा आर्किटेक्चर दृष्टिकोण और रोडमैप तय करना।
- संगठन के एंटरप्राइज़ डेटा मॉडल, डेटा मानकों और डेटा शब्दकोश का स्वामित्व रखना।
- डेटा आर्किटेक्चर, जोखिमों और निवेश पर कार्यकारी टीम और डेटा शासन निकायों को सलाह देना।
- अंतर-संगठनात्मक डेटा मानक और अंतर-संचालनीयता कार्य में संगठन का प्रतिनिधित्व करना।
- डेटा आर्किटेक्चर अभ्यास का नेतृत्व करना और उसके लोगों का विकास करना।

### कौशल

| कौशल | स्रोत | अपेक्षित स्तर | इस स्तर का अर्थ |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../कौशल/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Communicating data](../../कौशल/#communicating-data) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• turn complex data into clear and well understood solutions, which can be acted upon<br>• share data communication skills with the team and organisation<br>• understand and communicate different options, taking into account risks and uncertainties |
| [Data analysis and synthesis](../../कौशल/#data-analysis-and-synthesis) | UK GDaD PCF | कार्यरत | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../कौशल/#data-governance-data-architect) | UK GDaD PCF | विशेषज्ञ | You can:<br>• ensure data governance supports changes to the organisational strategy<br>• align data governance with wider governance (for example, budget)<br>• assure corporate services by understanding important risks and providing mitigation through assurance mechanisms |
| [Data innovation](../../कौशल/#data-innovation) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• test and evaluate the feasibility of unfamiliar and emerging technologies, or familiar technologies in new data contexts<br>• share what you learn with the organisation, explaining potential benefits, risks, and practical considerations<br>• recommend, design and implement innovative data solutions based on organisation objectives, user needs, and operational constraints |
| [Data modelling](../../कौशल/#data-modelling) | UK GDaD PCF | विशेषज्ञ | You can:<br>• understand the concepts and principles of data modelling and can produce relevant data models<br>• work across government and industry, recognising opportunities for the reuse and alignment of data models in different organisations<br>• design the method to categorise data models within an organisation |
| [Data standards](../../कौशल/#data-standards) | UK GDaD PCF | विशेषज्ञ | You can:<br>• create data standards for the organisation<br>• advocate for, and oversee compliance with, data policies and standards<br>• decide where standards need to be set across the organisation, and how to set them in the wider context of government |
| [Metadata management](../../कौशल/#metadata-management) | UK GDaD PCF | विशेषज्ञ | You can:<br>• identify how metadata repositories can support different areas of the organisation<br>• communicate the value of metadata repositories<br>• set up robust governance processes to keep repositories up to date |
| [Problem management](../../कौशल/#problem-management) | UK GDaD PCF | विशेषज्ञ | You can:<br>• anticipate problems and defend against them at the right time<br>• understand how a problem fits into the larger picture<br>• identify and describe problems, and help others to describe them<br>• build problem-solving capabilities in others |
| [Strategic thinking](../../कौशल/#strategic-thinking) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• define strategies and policies, providing guidance to others on working in the strategic context<br>• evaluate current strategies to ensure business requirements are being met and exceeded where possible |
| [Turning business problems into data design](../../कौशल/#turning-business-problems-into-data-design) | UK GDaD PCF | विशेषज्ञ | You can:<br>• design data architecture that deals with problems across the enterprise<br>• work across all organisational subject areas and internal and external programmes |
| [स्वास्थ्य और देखभाल सेवाओं की समझ](../../कौशल/#स्वास्थ्य-और-देखभाल-सेवाओं-की-समझ) | यह संदर्भ | विशेषज्ञ | आप ये कर सकते हैं:<br>• स्वास्थ्य और देखभाल प्रणाली की गहरी समझ के आधार पर संगठन की रणनीति को आकार देना<br>• स्वास्थ्य और देखभाल साझेदारों और प्रमुखों के समक्ष संगठन का प्रतिनिधित्व करना<br>• अनुमान लगाना कि नीति और सेवा में परिवर्तन डिजिटल सेवाओं और देखभाल को कैसे प्रभावित करेंगे |
| [क्लिनिकल शब्दावली और वर्गीकरण](../../कौशल/#क्लिनिकल-शब्दावली-और-वर्गीकरण) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• क्लिनिकल शब्दावलियों का उपयोग करके डेटा मॉडल और संदर्भ सेट डिज़ाइन करना<br>• शब्दावलियों और वर्गीकरणों के बीच मैपिंग करना, और मैपिंग की सीमाएँ समझाना<br>• उत्पादों और एनालिटिक्स में शब्दावली के उपयोग पर टीमों को सलाह देना |
| [स्वास्थ्य डेटा अंतर-संचालनीयता](../../कौशल/#स्वास्थ्य-डेटा-अंतर-संचालनीयता) | यह संदर्भ | विशेषज्ञ | आप ये कर सकते हैं:<br>• संगठन के लिए अंतर-संचालनीयता मानक और रणनीति तय करना<br>• राष्ट्रीय या अंतर-संगठनात्मक मानक कार्य का नेतृत्व करना<br>• कई प्रणालियों में महत्वपूर्ण इंटीग्रेशन के डिज़ाइन का आश्वासन देना |
| [सूचना शासन और डेटा संरक्षण](../../कौशल/#सूचना-शासन-और-डेटा-संरक्षण) | यह संदर्भ | विशेषज्ञ | आप ये कर सकते हैं:<br>• सूचना शासन नीति और रणनीति तय करना<br>• सूचना जोखिम और अनुपालन पर बोर्ड को सलाह देना<br>• नियामकों और साझेदारों के समक्ष संगठन का प्रतिनिधित्व करना |
| [डेटा गुणवत्ता प्रबंधन](../../कौशल/#डेटा-गुणवत्ता-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• डेटा गुणवत्ता नियम और माप परिभाषित करना<br>• ख़राब गुणवत्ता के मूल कारणों को ठीक करने के लिए डेटा प्रदाताओं के साथ काम करना |
| [क्लिनिकल जोखिम प्रबंधन](../../कौशल/#क्लिनिकल-जोखिम-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• किसी उत्पाद या परिवर्तन के लिए ख़तरा पहचान और जोखिम आकलन का नेतृत्व करना<br>• ख़तरा लॉग और क्लिनिकल सुरक्षा केस रिपोर्ट लिखना और बनाए रखना<br>• उत्पाद टीमों के साथ जोखिम नियंत्रणों पर सहमति बनाना और जाँचना कि वे काम करते हैं<br>• क्लिनिकल जोखिम प्रबंधन मानकों को लागू करने पर टीमों को सलाह देना |
| [लोगों का प्रबंधन](../../कौशल/#लोगों-का-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• किसी टीम का लाइन प्रबंधन करना, उद्देश्य तय करना और मूल्यांकन करना<br>• कल्याण का समर्थन करना और उपस्थिति, प्रदर्शन तथा आचरण का प्रबंधन करना<br>• टीम के विकास और उत्तराधिकार की योजना बनाना |

### सामान्य योग्यताएँ और अनुभव

- विभिन्न संगठनों में डेटा आर्किटेक्चर का नेतृत्व करने का व्यापक अनुभव।

### बैंड की रूपरेखा

- **ज्ञान:** विशेषज्ञ ज्ञान, और संगठन तथा क्षेत्र की व्यापक समझ।
- **स्वायत्तता:** किसी कार्य के लिए रणनीति तय करता है; किसी निदेशक के प्रति जवाबदेह होता है।
- **दायरा:** एक कार्य या विभाग।
- **नेतृत्व:** कई प्रबंधन स्तरों के माध्यम से किसी कार्य का नेतृत्व करता है।
- **जवाबदेही:** किसी कार्य का प्रदर्शन, कार्यबल और बजट।

### कार्य-मूल्यांकन (उदाहरणात्मक)

| # | कारक | स्तर | अंक |
| --- | --- | --- | --- |
| 1 | संचार और संबंध कौशल | 6 | 60 |
| 2 | ज्ञान, प्रशिक्षण और अनुभव | 8 | 240 |
| 3 | विश्लेषण और निर्णय कौशल | 5 | 60 |
| 4 | योजना और संगठन कौशल | 5 | 60 |
| 5 | शारीरिक कौशल | 2 | 15 |
| 6 | रोगी और सेवार्थी देखभाल की ज़िम्मेदारी | 1 | 4 |
| 7 | नीति और सेवा विकास की ज़िम्मेदारी | 5 | 45 |
| 8 | वित्तीय और भौतिक संसाधनों की ज़िम्मेदारी | 3 | 21 |
| 9 | लोगों की ज़िम्मेदारी | 3 | 21 |
| 10 | सूचना संसाधनों की ज़िम्मेदारी | 6 | 46 |
| 11 | अनुसंधान और विकास की ज़िम्मेदारी | 2 | 12 |
| 12 | कार्य करने की स्वतंत्रता | 5 | 45 |
| 13 | शारीरिक प्रयास | 1 | 3 |
| 14 | मानसिक प्रयास | 4 | 18 |
| 15 | भावनात्मक प्रयास | 1 | 5 |
| 16 | कार्य परिस्थितियाँ | 2 | 7 |
| | **कुल** | | **662** (बैंड 8c: 630–674) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
