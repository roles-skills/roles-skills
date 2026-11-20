# डेटा इंजीनियर

> यह एक सामान्य डिजिटल स्वास्थ्य सेवा संगठन के लिए एक उदाहरणात्मक संदर्भ प्रोफ़ाइल है। यह किसी भी नियोक्ता का आधिकारिक कार्य-विवरण नहीं है, और इसके कार्य-मूल्यांकन अंक औपचारिक मूल्यांकन नहीं हैं।

> इस पाठ का अंग्रेज़ी से अनुवाद एक कृत्रिम बुद्धिमत्ता सहायक ने किया है, और किसी मूल हिन्दी भाषी ने अभी तक इसकी समीक्षा नहीं की है। यूके सरकार के डिजिटल और डेटा पेशा क्षमता ढाँचे (UK GDaD PCF) और ESCO के उद्धरण अंग्रेज़ी में ही रखे गए हैं।

**परिवार:** [डेटा](../../#डेटा)  
**बैंड:** 6, 7, 8a, 8b  
**UK GDaD PCF भूमिका:** [Data engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/data-engineer/)  
**ESCO व्यवसाय:** [data engineer](http://data.europa.eu/esco/occupation/2079755f-d809-49e6-8037-4de6180e54c0) (ISCO-08 2511)

## सारांश

डेटा इंजीनियर वे पाइपलाइन और प्लेटफ़ॉर्म बनाते और चलाते हैं जो स्वास्थ्य और देखभाल डेटा को क्लिनिकल और परिचालन प्रणालियों से ऐसी जगहों पर ले जाते हैं जहाँ उसका विश्लेषण और सुरक्षित उपयोग हो सके। वे डेटा प्रवाह डिज़ाइन करते हैं, अलग-अलग मानकों वाले स्रोतों को एकीकृत करते हैं, और सुनिश्चित करते हैं कि डेटा सटीक, समय पर, सुरक्षित हो और केवल उन्हीं लोगों को उपलब्ध हो जिन्हें उसे देखना चाहिए।

## एक डिजिटल स्वास्थ्य सेवा संगठन में

- स्रोत प्रणालियों में इलेक्ट्रॉनिक रोगी अभिलेख, प्रयोगशाला, इमेजिंग और फ़ार्मेसी प्रणालियाँ शामिल हैं, जो HL7 संस्करण 2, HL7 FHIR, SNOMED CT और ICD जैसे मानकों का उपयोग करती हैं।
- पाइपलाइन अक्सर पहचान-योग्य रोगी डेटा ले जाती हैं, इसलिए इंजीनियर शुरू से ही छद्मनामकरण, पहुँच नियंत्रण और ऑडिट शामिल करते हैं।
- कुछ डेटा फ़ीड अलर्ट या रोगी सूचियों जैसी प्रत्यक्ष देखभाल में सहायक होती हैं, इसलिए विफल या विलंबित पाइपलाइन रोगियों को प्रभावित कर सकती है और उसका क्लिनिकल सुरक्षा आकलन चाहिए।
- डेटा को अक्सर देखभाल परिवेशों के पार जोड़ना पड़ता है, जो विश्वसनीय रोगी मिलान और एकरूप पहचानकर्ताओं पर निर्भर है।

## UK GDaD PCF भूमिका विवरण (अंग्रेज़ी मूल)

> A data engineer develops and constructs data products and services, and integrates them into systems and business processes.

## भूमिका स्तर

| बैंड | शीर्षक | UK GDaD PCF स्तर | यूके सिविल सेवा ग्रेड | कार्य-मूल्यांकन अंक |
| --- | --- | --- | --- | --- |
| 6 | [डेटा इंजीनियर](#बैंड-6-डेटा-इंजीनियर) | Data engineer | HEO/SEO | 421 |
| 7 | [वरिष्ठ डेटा इंजीनियर](#बैंड-7-वरिष्ठ-डेटा-इंजीनियर) | Senior data engineer | SEO/G7 | 477 |
| 8a | [लीड डेटा इंजीनियर](#बैंड-8a-लीड-डेटा-इंजीनियर) | Lead data engineer | G7 | 551 |
| 8b | [डेटा इंजीनियरिंग प्रमुख](#बैंड-8b-डेटा-इंजीनियरिंग-प्रमुख) | Head of data engineering | G7/G6 | 589 |

## बैंड 6: डेटा इंजीनियर

**UK GDaD PCF स्तर: Data engineer**

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

### ज़िम्मेदारियाँ

- सहमत डिज़ाइनों का पालन करते हुए क्लिनिकल और परिचालन प्रणालियों से डेटा प्लेटफ़ॉर्म तक डेटा पाइपलाइन बनाना और बनाए रखना।
- कोडित क्लिनिकल डेटा सहित स्रोत डेटा को लक्षित मॉडलों से मैप करना और मैपिंग का दस्तावेज़ीकरण करना।
- पाइपलाइन में छद्मनामकरण, सत्यापन और डेटा गुणवत्ता जाँच शामिल करना।
- पाइपलाइन की निगरानी करना और विफलताओं को ठीक करना, प्रत्यक्ष देखभाल में सहायक फ़ीड को प्राथमिकता देते हुए।
- सूचना शासन नियमों को पूरा करने वाले पहुँच नियंत्रण और ऑडिट लॉगिंग लागू करना।

### कौशल

| कौशल | स्रोत | अपेक्षित स्तर | इस स्तर का अर्थ |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../कौशल/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | जागरूकता | You can:<br>• explain why it's important to communicate technical concepts in non-technical language<br>• explain the types of communication that can be used with internal and external stakeholders, and their impact |
| [Data analysis and synthesis](../../कौशल/#data-analysis-and-synthesis) | UK GDaD PCF | कार्यरत | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data compliance and security](../../कौशल/#data-compliance-and-security) | UK GDaD PCF | कार्यरत | You can:<br>• use official data classification when authoring documents<br>• apply internal procedures, policies and technologies to ensure secure data handling<br>• identify and address ethical considerations when working with data<br>• address data compliance issues using internal processes |
| [Data development process](../../कौशल/#data-development-process) | UK GDaD PCF | कार्यरत | You can:<br>• implement simple data solutions such as data pipelines, following established approaches and standards<br>• create repeatable, reliable and reusable data solutions |
| [Data innovation](../../कौशल/#data-innovation) | UK GDaD PCF | जागरूकता | You can:<br>• develop a basic understanding of an unfamiliar or emerging technology, or a familiar technology in a new data context, with guidance<br>• share what you learn with colleagues, including how it could help deliver more value from data |
| [Data integration design](../../कौशल/#data-integration-design) | UK GDaD PCF | कार्यरत | You can:<br>• design simple data exchange or integration solutions using established patterns or modelling techniques<br>• include security features in your data integration designs |
| [Data modelling](../../कौशल/#data-modelling) | UK GDaD PCF | कार्यरत | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Metadata management](../../कौशल/#metadata-management) | UK GDaD PCF | कार्यरत | You can:<br>• use metadata repositories to complete complex tasks such as data and systems integration impact analysis<br>• maintain a metadata repository to ensure information remains accurate and up to date |
| [Problem management](../../कौशल/#problem-management) | UK GDaD PCF | जागरूकता | You can:<br>• investigate problems in systems, processes and services, with an understanding of the level of a problem, for example, strategic, tactical or operational<br>• contribute to the implementation of remedies and preventative measures |
| [Programming and build (data and analytics engineering)](../../कौशल/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | कार्यरत | You can:<br>• design, code, test and deploy programs or scripts following standards and good practice<br>• write readable, maintainable code<br>• use automation to improve the software development life cycle<br>• consider and adopt appropriate security measures in your solutions |
| [स्वास्थ्य और देखभाल सेवाओं की समझ](../../कौशल/#स्वास्थ्य-और-देखभाल-सेवाओं-की-समझ) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• उन क्लिनिकल और देखभाल कार्यप्रवाहों को समझाना जिनमें आपका काम सहायक है<br>• क्लिनिकल और देखभाल सहकर्मियों के साथ सामान्य स्वास्थ्य सेवा शब्दों का सही प्रयोग करना<br>• पहचानना कि कब कोई परिवर्तन रोगी देखभाल को प्रभावित कर सकता है, और उसे उठाना |
| [सूचना शासन और डेटा संरक्षण](../../कौशल/#सूचना-शासन-और-डेटा-संरक्षण) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• अपने काम में डेटा संरक्षण सिद्धांत लागू करना<br>• डेटा संरक्षण प्रभाव आकलनों में योगदान देना<br>• सूचना अनुरोधों और अभिलेखों को सही ढंग से संभालना |
| [स्वास्थ्य डेटा अंतर-संचालनीयता](../../कौशल/#स्वास्थ्य-डेटा-अंतर-संचालनीयता) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• FHIR संसाधन, प्रोफ़ाइल और API पढ़ना और उनका उपयोग करना<br>• मार्गदर्शन में सरल इंटीग्रेशन बनाना या उनका परीक्षण करना<br>• किसी विनिर्देश के आधार पर संदेशों की जाँच करना |
| [क्लिनिकल शब्दावली और वर्गीकरण](../../कौशल/#क्लिनिकल-शब्दावली-और-वर्गीकरण) | यह संदर्भ | जागरूकता | आप ये कर सकते हैं:<br>• क्लिनिकल शब्दावली और वर्गीकरण के बीच अंतर समझाना<br>• SNOMED CT और ICD जैसी सामान्य शब्दावलियों को पहचानना |
| [छद्मनामकरण और प्रकटीकरण नियंत्रण](../../कौशल/#छद्मनामकरण-और-प्रकटीकरण-नियंत्रण) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• छद्मनामित डेटा के साथ काम करना और आउटपुट जारी करने से पहले प्रकटीकरण जाँच करना<br>• पहचानना कि कब जुड़ा हुआ या विस्तृत डेटा किसी रोगी की पहचान उजागर कर सकता है |
| [क्लिनिकल जोखिम प्रबंधन](../../कौशल/#क्लिनिकल-जोखिम-प्रबंधन) | यह संदर्भ | जागरूकता | आप ये कर सकते हैं:<br>• समझाना कि स्वास्थ्य आईटी प्रणालियाँ रोगियों को कैसे नुकसान पहुँचा सकती हैं, उदाहरण के लिए ग़लत, गायब या विलंबित जानकारी से<br>• संभावित क्लिनिकल सुरक्षा मुद्दे की रिपोर्ट सही माध्यम से करना |

### सामान्य योग्यताएँ और अनुभव

- कंप्यूटिंग या संबंधित विषय में डिग्री, या समकक्ष अनुभव।
- डेटा पाइपलाइन बनाने का अनुभव।

### बैंड की रूपरेखा

- **ज्ञान:** अतिरिक्त प्रशिक्षण या अनुभव से विकसित, कई प्रक्रियाओं में विशेषज्ञ ज्ञान।
- **स्वायत्तता:** स्वतंत्र रूप से काम करता है; अपने क्षेत्र के लिए नीति की व्याख्या करता है; जटिल मुद्दों पर सलाह लेता है।
- **दायरा:** एक उत्पाद, सेवा या कार्यधारा।
- **नेतृत्व:** एक छोटी टीम का नेतृत्व या सहकर्मियों का मार्गदर्शन कर सकता है।
- **जवाबदेही:** अपनी कार्यधारा के परिणाम और दी गई सलाह की गुणवत्ता।

### कार्य-मूल्यांकन (उदाहरणात्मक)

| # | कारक | स्तर | अंक |
| --- | --- | --- | --- |
| 1 | संचार और संबंध कौशल | 4 | 32 |
| 2 | ज्ञान, प्रशिक्षण और अनुभव | 6 | 156 |
| 3 | विश्लेषण और निर्णय कौशल | 4 | 42 |
| 4 | योजना और संगठन कौशल | 3 | 27 |
| 5 | शारीरिक कौशल | 3 | 27 |
| 6 | रोगी और सेवार्थी देखभाल की ज़िम्मेदारी | 1 | 4 |
| 7 | नीति और सेवा विकास की ज़िम्मेदारी | 2 | 12 |
| 8 | वित्तीय और भौतिक संसाधनों की ज़िम्मेदारी | 1 | 5 |
| 9 | लोगों की ज़िम्मेदारी | 1 | 5 |
| 10 | सूचना संसाधनों की ज़िम्मेदारी | 5 | 34 |
| 11 | अनुसंधान और विकास की ज़िम्मेदारी | 2 | 12 |
| 12 | कार्य करने की स्वतंत्रता | 4 | 32 |
| 13 | शारीरिक प्रयास | 1 | 3 |
| 14 | मानसिक प्रयास | 4 | 18 |
| 15 | भावनात्मक प्रयास | 1 | 5 |
| 16 | कार्य परिस्थितियाँ | 2 | 7 |
| | **कुल** | | **421** (बैंड 6: 396–465) |

## बैंड 7: वरिष्ठ डेटा इंजीनियर

**UK GDaD PCF स्तर: Senior data engineer**

> A senior data engineer designs and leads the implementation of data flows to connect operational systems, data for analytics and business intelligence (BI) systems.
> 
> At this role level, you will:
> - recognise opportunities to reuse existing data flows
> - lead the build of data streaming systems
> - optimise the code to ensure processes perform optimally
> - lead work on database management

### ज़िम्मेदारियाँ

- कई स्वास्थ्य और देखभाल प्रणालियों के डेटा को एक साथ लाने वाले डेटा प्रवाह और स्ट्रीमिंग सेवाएँ डिज़ाइन करना।
- रोगी मिलान और लिंकेज प्रक्रियाएँ डिज़ाइन करना और मापना कि वे कितनी अच्छी तरह काम करती हैं।
- डेटाबेस और प्लेटफ़ॉर्म प्रदर्शन कार्य का नेतृत्व करना ताकि सेवाओं को आवश्यकता होने पर डेटा उपलब्ध हो।
- संबंधित विशेषज्ञों के साथ डेटा प्रवाहों के क्लिनिकल सुरक्षा और सूचना शासन जोखिमों का आकलन करना।
- अन्य इंजीनियरों के काम की समीक्षा करना और उन्हें कोचिंग देना।

### कौशल

| कौशल | स्रोत | अपेक्षित स्तर | इस स्तर का अर्थ |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../कौशल/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | कार्यरत | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Data analysis and synthesis](../../कौशल/#data-analysis-and-synthesis) | UK GDaD PCF | कार्यरत | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data compliance and security](../../कौशल/#data-compliance-and-security) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• consistently apply data ethics, legislation, internal procedures, policies and technologies to ensure secure data handling<br>• help ensure your team remain compliant by identifying and addressing current and potential data compliance and ethical issues<br>• guide and support others in addressing data compliance issues |
| [Data development process](../../कौशल/#data-development-process) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• lead the implementation of complex or large-scale data solutions<br>• apply appropriate technology and techniques to ensure data solutions are secure and scalable<br>• identify and implement continuous improvement to the operation and performance of data solutions |
| [Data innovation](../../कौशल/#data-innovation) | UK GDaD PCF | कार्यरत | You can:<br>• experiment with unfamiliar and emerging technologies, or familiar technologies in new data contexts, with guidance<br>• share what you learn with the team, explaining potential benefits, risks, and practical considerations<br>• identify opportunities to apply technology to improve data processes or outcomes in an operational setting or the wider organisation |
| [Data integration design](../../कौशल/#data-integration-design) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• select the most appropriate techniques for different integration scenarios<br>• evaluate and lead the implementation of integration using varied approaches that ensure security, efficiency and compliance |
| [Data modelling](../../कौशल/#data-modelling) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• produce relevant data models across multiple subject areas<br>• explain which models to use for which purpose<br>• understand industry-recognised data modelling patterns and standards, and when to apply them<br>• compare and align different data models |
| [Metadata management](../../कौशल/#metadata-management) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../कौशल/#problem-management) | UK GDaD PCF | कार्यरत | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Programming and build (data and analytics engineering)](../../कौशल/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• lead the design, code, testing and deployment of secure, resilient and maintainable solutions<br>• continuously improve the codebase and reliability of solutions<br>• create automation to improve the software development life cycle<br>• work with others to implement standards and good practice to ensure security, testability and maintainability of solutions |
| [स्वास्थ्य और देखभाल सेवाओं की समझ](../../कौशल/#स्वास्थ्य-और-देखभाल-सेवाओं-की-समझ) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• उन क्लिनिकल और देखभाल कार्यप्रवाहों को समझाना जिनमें आपका काम सहायक है<br>• क्लिनिकल और देखभाल सहकर्मियों के साथ सामान्य स्वास्थ्य सेवा शब्दों का सही प्रयोग करना<br>• पहचानना कि कब कोई परिवर्तन रोगी देखभाल को प्रभावित कर सकता है, और उसे उठाना |
| [सूचना शासन और डेटा संरक्षण](../../कौशल/#सूचना-शासन-और-डेटा-संरक्षण) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• डेटा संरक्षण प्रभाव आकलनों और सूचना साझाकरण समझौतों का नेतृत्व करना<br>• विधिक आधार, सहमति, गोपनीयता और प्रतिधारण पर टीमों को सलाह देना<br>• घटनाओं की जाँच करना और सुधारों की सिफ़ारिश करना |
| [स्वास्थ्य डेटा अंतर-संचालनीयता](../../कौशल/#स्वास्थ्य-डेटा-अंतर-संचालनीयता) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• FHIR, HL7 संस्करण 2 और संदेश पैटर्न का उपयोग करके इंटीग्रेशन डिज़ाइन करना और बनाना<br>• FHIR संसाधन और कार्यान्वयन गाइड लिखना और उनकी प्रोफ़ाइल बनाना<br>• प्रणालियों के बीच जटिल मैपिंग और डेटा गुणवत्ता समस्याओं को सुलझाना |
| [क्लिनिकल शब्दावली और वर्गीकरण](../../कौशल/#क्लिनिकल-शब्दावली-और-वर्गीकरण) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• किसी डेटा आइटम या फ़ॉर्म के लिए सही कोड खोजना और उपयोग करना<br>• शब्दावली ब्राउज़र और संदर्भ सेट का उपयोग करना |
| [छद्मनामकरण और प्रकटीकरण नियंत्रण](../../कौशल/#छद्मनामकरण-और-प्रकटीकरण-नियंत्रण) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• ऐसी छद्मनामकरण और लिंकेज विधियाँ डिज़ाइन करना जो पहचानकर्ताओं को विश्लेषण डेटा से अलग रखें<br>• किसी डेटासेट या प्रकाशन के पुनः-पहचान जोखिम का आकलन करना और उपयुक्त नियंत्रण चुनना<br>• विश्वसनीय अनुसंधान परिवेश जैसी सुरक्षित व्यवस्थाओं पर टीमों को सलाह देना |
| [क्लिनिकल जोखिम प्रबंधन](../../कौशल/#क्लिनिकल-जोखिम-प्रबंधन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• ख़तरा कार्यशालाओं में भाग लेना और ख़तरा लॉग में योगदान देना<br>• अपने काम के लिए क्लिनिकल जोखिम प्रबंधन प्रक्रिया का पालन करना<br>• क्लिनिकल सुरक्षा केस के लिए परीक्षण परिणाम जैसे साक्ष्य देना |

### सामान्य योग्यताएँ और अनुभव

- डेटा प्रणालियाँ डिज़ाइन करने और बनाने का पर्याप्त अनुभव, मास्टर डिग्री के समकक्ष स्तर पर।

### बैंड की रूपरेखा

- **ज्ञान:** अत्यधिक विकसित विशेषज्ञ ज्ञान, आमतौर पर स्नातकोत्तर (मास्टर) स्तर या समकक्ष अनुभव।
- **स्वायत्तता:** संगठन की नीति के अनुसार काम करता है; परिणाम कैसे प्राप्त हों, यह तय करता है; दूसरे इससे विशेषज्ञ सलाह लेते हैं।
- **दायरा:** कई उत्पाद या सेवाएँ, या एक विशेषज्ञ कार्य।
- **नेतृत्व:** एक टीम या पेशेवर अभ्यास क्षेत्र का नेतृत्व करता है।
- **जवाबदेही:** एक सेवा या विशेषज्ञ कार्य की डिलीवरी, और यदि हो तो उसका बजट।

### कार्य-मूल्यांकन (उदाहरणात्मक)

| # | कारक | स्तर | अंक |
| --- | --- | --- | --- |
| 1 | संचार और संबंध कौशल | 4 | 32 |
| 2 | ज्ञान, प्रशिक्षण और अनुभव | 7 | 196 |
| 3 | विश्लेषण और निर्णय कौशल | 4 | 42 |
| 4 | योजना और संगठन कौशल | 3 | 27 |
| 5 | शारीरिक कौशल | 3 | 27 |
| 6 | रोगी और सेवार्थी देखभाल की ज़िम्मेदारी | 1 | 4 |
| 7 | नीति और सेवा विकास की ज़िम्मेदारी | 3 | 21 |
| 8 | वित्तीय और भौतिक संसाधनों की ज़िम्मेदारी | 1 | 5 |
| 9 | लोगों की ज़िम्मेदारी | 2 | 12 |
| 10 | सूचना संसाधनों की ज़िम्मेदारी | 5 | 34 |
| 11 | अनुसंधान और विकास की ज़िम्मेदारी | 2 | 12 |
| 12 | कार्य करने की स्वतंत्रता | 4 | 32 |
| 13 | शारीरिक प्रयास | 1 | 3 |
| 14 | मानसिक प्रयास | 4 | 18 |
| 15 | भावनात्मक प्रयास | 1 | 5 |
| 16 | कार्य परिस्थितियाँ | 2 | 7 |
| | **कुल** | | **477** (बैंड 7: 466–539) |

## बैंड 8a: लीड डेटा इंजीनियर

**UK GDaD PCF स्तर: Lead data engineer**

> A lead data engineer is responsible for the design and implementation of numerous complex data flows to connect operational systems, data for analytics and business intelligence (BI) systems.
> 
> At this role level, you will:
> - recognise and share opportunities to reuse existing data flows between teams
> - be responsible for the build of data-streaming systems
> - co-ordinate teams and set best practice and standards
> - apply knowledge of systems integration to your work
> - champion data engineering across government

### ज़िम्मेदारियाँ

- संगठन के डेटा प्लेटफ़ॉर्म और उसके कई डेटा प्रवाहों के डिज़ाइन और संचालन का नेतृत्व करना।
- पाइपलाइन, परीक्षण, सुरक्षा और दस्तावेज़ीकरण के लिए इंजीनियरिंग मानक तय करना।
- साझा देखभाल अभिलेखों और क्षेत्रीय डेटा सेवाओं सहित स्वास्थ्य और देखभाल साझेदारों के साथ डेटा एकीकरण की योजना बनाना।
- सुनिश्चित करना कि प्रत्यक्ष देखभाल में सहायक डेटा प्रवाह लचीले हों और उनके क्लिनिकल सुरक्षा केस हों।
- डेटा इंजीनियरिंग टीमों का समन्वय करना और इंजीनियरों का लाइन प्रबंधन करना।

### कौशल

| कौशल | स्रोत | अपेक्षित स्तर | इस स्तर का अर्थ |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../कौशल/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Data analysis and synthesis](../../कौशल/#data-analysis-and-synthesis) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• understand and help teams to apply a range of techniques for data profiling<br>• source system analysis from a complex single source<br>• bring multiple data sources together in a conformed model for analysis |
| [Data compliance and security](../../कौशल/#data-compliance-and-security) | UK GDaD PCF | विशेषज्ञ | You can:<br>• advise senior stakeholders on data security, ethical or procedural risks<br>• improve organisational awareness of data compliance and procedures<br>• lead, guide and mentor teams in implementing secure data practices and maintaining compliance |
| [Data development process](../../कौशल/#data-development-process) | UK GDaD PCF | विशेषज्ञ | You can:<br>• establish cross-organisational data solutions that include all aspects of the data development life cycle<br>• define and promote good practices for creating repeatable, reliable and reusable data solutions |
| [Data innovation](../../कौशल/#data-innovation) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• test and evaluate the feasibility of unfamiliar and emerging technologies, or familiar technologies in new data contexts<br>• share what you learn with the organisation, explaining potential benefits, risks, and practical considerations<br>• recommend, design and implement innovative data solutions based on organisation objectives, user needs, and operational constraints |
| [Data integration design](../../कौशल/#data-integration-design) | UK GDaD PCF | विशेषज्ञ | You can:<br>• establish cross-organisational data integration standards and design patterns<br>• guide teams in designing secure and interoperable systems and services |
| [Data modelling](../../कौशल/#data-modelling) | UK GDaD PCF | विशेषज्ञ | You can:<br>• understand the concepts and principles of data modelling and can produce relevant data models<br>• work across government and industry, recognising opportunities for the reuse and alignment of data models in different organisations<br>• design the method to categorise data models within an organisation |
| [Metadata management](../../कौशल/#metadata-management) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../कौशल/#problem-management) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• ensure that the right actions are taken to investigate, resolve and anticipate problems<br>• co-ordinate the team to investigate problems, implement solutions and take preventive measures |
| [Programming and build (data and analytics engineering)](../../कौशल/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• lead the design, code, testing and deployment of secure, resilient and maintainable solutions<br>• continuously improve the codebase and reliability of solutions<br>• create automation to improve the software development life cycle<br>• work with others to implement standards and good practice to ensure security, testability and maintainability of solutions |
| [स्वास्थ्य और देखभाल सेवाओं की समझ](../../कौशल/#स्वास्थ्य-और-देखभाल-सेवाओं-की-समझ) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• विश्लेषण करना कि कोई सेवा विभिन्न संगठनों के देखभाल मार्गों में कैसे बैठती है<br>• डिजिटल सेवाओं को आकार देने के लिए चिकित्सकों, देखभाल कर्मचारियों और रोगियों के साथ काम करना<br>• देखभाल, सुरक्षा और कर्मचारियों के कार्यभार पर डिजिटल निर्णयों का प्रभाव समझाना |
| [सूचना शासन और डेटा संरक्षण](../../कौशल/#सूचना-शासन-और-डेटा-संरक्षण) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• डेटा संरक्षण प्रभाव आकलनों और सूचना साझाकरण समझौतों का नेतृत्व करना<br>• विधिक आधार, सहमति, गोपनीयता और प्रतिधारण पर टीमों को सलाह देना<br>• घटनाओं की जाँच करना और सुधारों की सिफ़ारिश करना |
| [स्वास्थ्य डेटा अंतर-संचालनीयता](../../कौशल/#स्वास्थ्य-डेटा-अंतर-संचालनीयता) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• FHIR, HL7 संस्करण 2 और संदेश पैटर्न का उपयोग करके इंटीग्रेशन डिज़ाइन करना और बनाना<br>• FHIR संसाधन और कार्यान्वयन गाइड लिखना और उनकी प्रोफ़ाइल बनाना<br>• प्रणालियों के बीच जटिल मैपिंग और डेटा गुणवत्ता समस्याओं को सुलझाना |
| [क्लिनिकल शब्दावली और वर्गीकरण](../../कौशल/#क्लिनिकल-शब्दावली-और-वर्गीकरण) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• किसी डेटा आइटम या फ़ॉर्म के लिए सही कोड खोजना और उपयोग करना<br>• शब्दावली ब्राउज़र और संदर्भ सेट का उपयोग करना |
| [छद्मनामकरण और प्रकटीकरण नियंत्रण](../../कौशल/#छद्मनामकरण-और-प्रकटीकरण-नियंत्रण) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• ऐसी छद्मनामकरण और लिंकेज विधियाँ डिज़ाइन करना जो पहचानकर्ताओं को विश्लेषण डेटा से अलग रखें<br>• किसी डेटासेट या प्रकाशन के पुनः-पहचान जोखिम का आकलन करना और उपयुक्त नियंत्रण चुनना<br>• विश्वसनीय अनुसंधान परिवेश जैसी सुरक्षित व्यवस्थाओं पर टीमों को सलाह देना |
| [क्लिनिकल जोखिम प्रबंधन](../../कौशल/#क्लिनिकल-जोखिम-प्रबंधन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• ख़तरा कार्यशालाओं में भाग लेना और ख़तरा लॉग में योगदान देना<br>• अपने काम के लिए क्लिनिकल जोखिम प्रबंधन प्रक्रिया का पालन करना<br>• क्लिनिकल सुरक्षा केस के लिए परीक्षण परिणाम जैसे साक्ष्य देना |
| [लोगों का प्रबंधन](../../कौशल/#लोगों-का-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• किसी टीम का लाइन प्रबंधन करना, उद्देश्य तय करना और मूल्यांकन करना<br>• कल्याण का समर्थन करना और उपस्थिति, प्रदर्शन तथा आचरण का प्रबंधन करना<br>• टीम के विकास और उत्तराधिकार की योजना बनाना |

### सामान्य योग्यताएँ और अनुभव

- जटिल प्रणालियों के लिए डेटा इंजीनियरिंग का नेतृत्व करने का व्यापक अनुभव।

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
| 11 | अनुसंधान और विकास की ज़िम्मेदारी | 2 | 12 |
| 12 | कार्य करने की स्वतंत्रता | 5 | 45 |
| 13 | शारीरिक प्रयास | 1 | 3 |
| 14 | मानसिक प्रयास | 4 | 18 |
| 15 | भावनात्मक प्रयास | 1 | 5 |
| 16 | कार्य परिस्थितियाँ | 2 | 7 |
| | **कुल** | | **551** (बैंड 8a: 540–584) |

## बैंड 8b: डेटा इंजीनियरिंग प्रमुख

**UK GDaD PCF स्तर: Head of data engineering**

> A head of data engineering leads multi-functional delivery teams to deliver robust data services for their department, other government departments and private sector partners.
> 
> At this role level, you will:
> - inspire best practice for data products and services within your teams
> - build data engineering capability by providing technical leadership and career development for the community
> - work with other senior team members to identify, plan, develop and deliver data services

### ज़िम्मेदारियाँ

- संगठन के डेटा प्लेटफ़ॉर्म और डेटा इंजीनियरिंग सेवाओं की रणनीति तय करना।
- आंतरिक टीमों और स्वास्थ्य तथा देखभाल साझेदारों के लिए डेटा सेवाएँ देने वाली बहु-विषयक टीमों का नेतृत्व करना।
- डेटा प्लेटफ़ॉर्म के जोखिमों, लागतों और निवेश पर वरिष्ठ प्रमुखों को सलाह देना।
- सुनिश्चित करना कि डेटा सेवाएँ सूचना शासन, सुरक्षा और क्लिनिकल सुरक्षा आवश्यकताओं को पूरा करें।
- भर्ती, विकास और करियर मार्गों के माध्यम से डेटा इंजीनियरिंग क्षमता बनाना।

### कौशल

| कौशल | स्रोत | अपेक्षित स्तर | इस स्तर का अर्थ |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../कौशल/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | विशेषज्ञ | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Data analysis and synthesis](../../कौशल/#data-analysis-and-synthesis) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• understand and help teams to apply a range of techniques for data profiling<br>• source system analysis from a complex single source<br>• bring multiple data sources together in a conformed model for analysis |
| [Data compliance and security](../../कौशल/#data-compliance-and-security) | UK GDaD PCF | विशेषज्ञ | You can:<br>• advise senior stakeholders on data security, ethical or procedural risks<br>• improve organisational awareness of data compliance and procedures<br>• lead, guide and mentor teams in implementing secure data practices and maintaining compliance |
| [Data development process](../../कौशल/#data-development-process) | UK GDaD PCF | विशेषज्ञ | You can:<br>• establish cross-organisational data solutions that include all aspects of the data development life cycle<br>• define and promote good practices for creating repeatable, reliable and reusable data solutions |
| [Data innovation](../../कौशल/#data-innovation) | UK GDaD PCF | विशेषज्ञ | You can:<br>• advocate for adoption of unfamiliar and emerging technologies, or familiar technologies in new data contexts, ensuring organisation objectives, user needs, and operational constraints inform decisions<br>• develop organisational capability in data innovation through leadership<br>• anticipate future technology changes and advise how to take advantage of them to realise value from data |
| [Data integration design](../../कौशल/#data-integration-design) | UK GDaD PCF | विशेषज्ञ | You can:<br>• establish cross-organisational data integration standards and design patterns<br>• guide teams in designing secure and interoperable systems and services |
| [Data modelling](../../कौशल/#data-modelling) | UK GDaD PCF | कार्यरत | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Metadata management](../../कौशल/#metadata-management) | UK GDaD PCF | विशेषज्ञ | You can:<br>• identify how metadata repositories can support different areas of the organisation<br>• communicate the value of metadata repositories<br>• set up robust governance processes to keep repositories up to date |
| [Problem management](../../कौशल/#problem-management) | UK GDaD PCF | विशेषज्ञ | You can:<br>• anticipate problems and defend against them at the right time<br>• understand how a problem fits into the larger picture<br>• identify and describe problems, and help others to describe them<br>• build problem-solving capabilities in others |
| [Programming and build (data and analytics engineering)](../../कौशल/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | विशेषज्ञ | You can:<br>• set standards for programming tools and techniques<br>• select appropriate development methods for a problem<br>• advise on the application of standards and methods that ensure security, maintainability and compliance<br>• take technical responsibility for all stages of a software development project, providing technical advice and guidance to stakeholders |
| [स्वास्थ्य और देखभाल सेवाओं की समझ](../../कौशल/#स्वास्थ्य-और-देखभाल-सेवाओं-की-समझ) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• विश्लेषण करना कि कोई सेवा विभिन्न संगठनों के देखभाल मार्गों में कैसे बैठती है<br>• डिजिटल सेवाओं को आकार देने के लिए चिकित्सकों, देखभाल कर्मचारियों और रोगियों के साथ काम करना<br>• देखभाल, सुरक्षा और कर्मचारियों के कार्यभार पर डिजिटल निर्णयों का प्रभाव समझाना |
| [सूचना शासन और डेटा संरक्षण](../../कौशल/#सूचना-शासन-और-डेटा-संरक्षण) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• डेटा संरक्षण प्रभाव आकलनों और सूचना साझाकरण समझौतों का नेतृत्व करना<br>• विधिक आधार, सहमति, गोपनीयता और प्रतिधारण पर टीमों को सलाह देना<br>• घटनाओं की जाँच करना और सुधारों की सिफ़ारिश करना |
| [स्वास्थ्य डेटा अंतर-संचालनीयता](../../कौशल/#स्वास्थ्य-डेटा-अंतर-संचालनीयता) | यह संदर्भ | विशेषज्ञ | आप ये कर सकते हैं:<br>• संगठन के लिए अंतर-संचालनीयता मानक और रणनीति तय करना<br>• राष्ट्रीय या अंतर-संगठनात्मक मानक कार्य का नेतृत्व करना<br>• कई प्रणालियों में महत्वपूर्ण इंटीग्रेशन के डिज़ाइन का आश्वासन देना |
| [छद्मनामकरण और प्रकटीकरण नियंत्रण](../../कौशल/#छद्मनामकरण-और-प्रकटीकरण-नियंत्रण) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• ऐसी छद्मनामकरण और लिंकेज विधियाँ डिज़ाइन करना जो पहचानकर्ताओं को विश्लेषण डेटा से अलग रखें<br>• किसी डेटासेट या प्रकाशन के पुनः-पहचान जोखिम का आकलन करना और उपयुक्त नियंत्रण चुनना<br>• विश्वसनीय अनुसंधान परिवेश जैसी सुरक्षित व्यवस्थाओं पर टीमों को सलाह देना |
| [क्लिनिकल जोखिम प्रबंधन](../../कौशल/#क्लिनिकल-जोखिम-प्रबंधन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• ख़तरा कार्यशालाओं में भाग लेना और ख़तरा लॉग में योगदान देना<br>• अपने काम के लिए क्लिनिकल जोखिम प्रबंधन प्रक्रिया का पालन करना<br>• क्लिनिकल सुरक्षा केस के लिए परीक्षण परिणाम जैसे साक्ष्य देना |
| [लोगों का प्रबंधन](../../कौशल/#लोगों-का-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• किसी टीम का लाइन प्रबंधन करना, उद्देश्य तय करना और मूल्यांकन करना<br>• कल्याण का समर्थन करना और उपस्थिति, प्रदर्शन तथा आचरण का प्रबंधन करना<br>• टीम के विकास और उत्तराधिकार की योजना बनाना |
| [बजट प्रबंधन](../../कौशल/#बजट-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• बजट रखना और उसका प्रबंधन करना, पूर्वानुमान लगाना और अंतरों की व्याख्या करना<br>• लागत और लाभ सहित बिज़नेस केस तैयार करना |

### सामान्य योग्यताएँ और अनुभव

- कई टीमों में डेटा इंजीनियरिंग का नेतृत्व करने का व्यापक अनुभव।

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
| 2 | ज्ञान, प्रशिक्षण और अनुभव | 7 | 196 |
| 3 | विश्लेषण और निर्णय कौशल | 5 | 60 |
| 4 | योजना और संगठन कौशल | 5 | 60 |
| 5 | शारीरिक कौशल | 2 | 15 |
| 6 | रोगी और सेवार्थी देखभाल की ज़िम्मेदारी | 1 | 4 |
| 7 | नीति और सेवा विकास की ज़िम्मेदारी | 4 | 32 |
| 8 | वित्तीय और भौतिक संसाधनों की ज़िम्मेदारी | 3 | 21 |
| 9 | लोगों की ज़िम्मेदारी | 4 | 32 |
| 10 | सूचना संसाधनों की ज़िम्मेदारी | 5 | 34 |
| 11 | अनुसंधान और विकास की ज़िम्मेदारी | 2 | 12 |
| 12 | कार्य करने की स्वतंत्रता | 5 | 45 |
| 13 | शारीरिक प्रयास | 1 | 3 |
| 14 | मानसिक प्रयास | 4 | 18 |
| 15 | भावनात्मक प्रयास | 1 | 5 |
| 16 | कार्य परिस्थितियाँ | 2 | 7 |
| | **कुल** | | **589** (बैंड 8b: 585–629) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
