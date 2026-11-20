# सॉल्यूशन आर्किटेक्ट

> यह एक सामान्य डिजिटल स्वास्थ्य सेवा संगठन के लिए एक उदाहरणात्मक संदर्भ प्रोफ़ाइल है। यह किसी भी नियोक्ता का आधिकारिक कार्य-विवरण नहीं है, और इसके कार्य-मूल्यांकन अंक औपचारिक मूल्यांकन नहीं हैं।

> इस पाठ का अंग्रेज़ी से अनुवाद एक कृत्रिम बुद्धिमत्ता सहायक ने किया है, और किसी मूल हिन्दी भाषी ने अभी तक इसकी समीक्षा नहीं की है। यूके सरकार के डिजिटल और डेटा पेशा क्षमता ढाँचे (UK GDaD PCF) और ESCO के उद्धरण अंग्रेज़ी में ही रखे गए हैं।

**परिवार:** [आर्किटेक्चर](../../#आर्किटेक्चर)  
**बैंड:** 7, 8a, 8b, 8c, 8d  
**UK GDaD PCF भूमिका:** [Solution architect](https://understand-digital-data-roles-skills.service.gov.uk/role/solution-architect/)  
**ESCO व्यवसाय:** [ICT system architect](http://data.europa.eu/esco/occupation/e1c72b5f-4c5c-487c-a6df-e84b64a51dae) (ISCO-08 2511)

## सारांश

सॉल्यूशन आर्किटेक्ट डिज़ाइन करते हैं कि कोई नई या बदली हुई सेवा शुरू से अंत तक कैसे काम करेगी, उपयोगकर्ता आवश्यकताओं और क्लिनिकल कार्यप्रवाहों से लेकर एप्लिकेशन, डेटा, इंटीग्रेशन, होस्टिंग और सुरक्षा तक। वे सुनिश्चित करते हैं कि हर समाधान संगठन के आर्किटेक्चर में बैठे, उसकी सुरक्षा, निजता और अंतर-संचालनीयता आवश्यकताओं को पूरा करे, और वहनीय रूप से बनाया, चलाया और समर्थित किया जा सके।

## एक डिजिटल स्वास्थ्य सेवा संगठन में

- समाधानों में अक्सर ख़रीदी गई क्लिनिकल प्रणालियाँ, आंतरिक सेवाएँ और साझा प्लेटफ़ॉर्म मिले होते हैं, इसलिए आर्किटेक्टों को आपूर्तिकर्ता सीमाओं के पार डिज़ाइन करना होता है।
- डिज़ाइन विकल्प खोए हुए परिणाम या ग़लत रोगी मिलान जैसे क्लिनिकल ख़तरे पैदा कर सकते हैं, इसलिए समाधान डिज़ाइन क्लिनिकल सुरक्षा केस में शामिल होते हैं।
- रोगी जानकारी के हर नए डेटा प्रवाह के लिए विधिक आधार और डेटा संरक्षण प्रभाव आकलन चाहिए, इसलिए आर्किटेक्ट सूचना शासन के साथ निकटता से काम करते हैं।
- HL7 FHIR जैसे मानकों का उपयोग करके अन्य स्वास्थ्य और देखभाल संगठनों के साथ अंतर-संचालनीयता आमतौर पर एक मूल आवश्यकता होती है।
- कुछ समाधानों में ऐसा सॉफ़्टवेयर होता है जो चिकित्सा उपकरण है, जिससे डिज़ाइन, आश्वासन और आपूर्तिकर्ता आवश्यकताएँ बदल जाती हैं।

## UK GDaD PCF भूमिका विवरण (अंग्रेज़ी मूल)

> A solution architect designs solutions for problems that affect the organisation.
> 
> In this role, you will:
> - ensure a problem and the desired outcomes are properly defined
> - ensure the scope of a solution meets the organisation's requirements
> - stay up to date on technology trends and approaches
> - understand organisational objectives and external drivers, for example, legislation or financial constraints
> - work with others to develop business and technical strategies
> - work within business and technical constraints
> - design and document solutions so they can be implemented by the organisation
> - comply with standards and governance
> - communicate and work effectively with stakeholders
> - manage risks and decisions in a transparent way

## भूमिका स्तर

| बैंड | शीर्षक | UK GDaD PCF स्तर | यूके सिविल सेवा ग्रेड | कार्य-मूल्यांकन अंक |
| --- | --- | --- | --- | --- |
| 7 | [एसोसिएट सॉल्यूशन आर्किटेक्ट](#बैंड-7-एसोसिएट-सॉल्यूशन-आर्किटेक्ट) | Associate solution architect | HEO/SEO | 483 |
| 8a | [सॉल्यूशन आर्किटेक्ट](#बैंड-8a-सॉल्यूशन-आर्किटेक्ट) | Solution architect | SEO/G7 | 560 |
| 8b | [वरिष्ठ सॉल्यूशन आर्किटेक्ट](#बैंड-8b-वरिष्ठ-सॉल्यूशन-आर्किटेक्ट) | Senior solution architect | G7 | 604 |
| 8c | [लीड सॉल्यूशन आर्किटेक्ट](#बैंड-8c-लीड-सॉल्यूशन-आर्किटेक्ट) | Lead solution architect | G7/G6 | 655 |
| 8d | [प्रधान सॉल्यूशन आर्किटेक्ट](#बैंड-8d-प्रधान-सॉल्यूशन-आर्किटेक्ट) | Principal solution architect | G6 | 699 |

## बैंड 7: एसोसिएट सॉल्यूशन आर्किटेक्ट

**UK GDaD PCF स्तर: Associate solution architect**

> An associate solution architect supports other solution architects to design solutions. You will usually work under supervision.
> 
> At this role level, you will:
> - support the design of solutions by working with stakeholders
> - help your team achieve its objectives

### ज़िम्मेदारियाँ

- समाधान डिज़ाइनों के लिए उत्पाद टीमों, चिकित्सकों और आपूर्तिकर्ताओं से आवश्यकताएँ एकत्र करना।
- संदर्भ, डेटा प्रवाह और इंटीग्रेशन दृश्यों जैसे वर्तमान और लक्षित स्थिति के आरेख बनाना।
- पर्यवेक्षण में समाधान डिज़ाइनों और निर्णय अभिलेखों के अनुभागों का मसौदा बनाना।
- आर्किटेक्चर मानकों, सुरक्षा और सूचना शासन आवश्यकताओं के आधार पर डिज़ाइनों की जाँच करना।
- डिज़ाइन प्राधिकरणों में समीक्षा के लिए डिज़ाइन तैयार करने में मदद करना।

### कौशल

| कौशल | स्रोत | अपेक्षित स्तर | इस स्तर का अर्थ |
| --- | --- | --- | --- |
| [Architect for the whole context](../../कौशल/#architect-for-the-whole-context) | UK GDaD PCF | जागरूकता | You can:<br>• identify relevant information that can inform your architectural work, such as strategies, roadmaps, policies and technical trends<br>• understand how your work supports the team in enabling change​ |
| [Architecture communication](../../कौशल/#architecture-communication) | UK GDaD PCF | कार्यरत | You can:<br>• listen to the needs of technical and business stakeholders<br>• create and use different architecture representations to communicate effectively, achieving agreement with technical and non-technical stakeholders<br>• provide support in discussions about architectural topics within a multidisciplinary team |
| [Commercial perspective](../../कौशल/#commercial-perspective) | UK GDaD PCF | जागरूकता | You can:<br>• show an awareness of government commercial processes<br>• show an awareness of legal and compliance rules |
| [Community collaboration](../../कौशल/#community-collaboration) | UK GDaD PCF | जागरूकता | You can:<br>• understand the work of others and the importance of team dynamics, collaboration and feedback |
| [Making architectural decisions](../../कौशल/#making-architectural-decisions) | UK GDaD PCF | जागरूकता | You can:<br>• describe the reasoning behind architectural design decisions<br>• gather information to inform decisions<br>• understand architectural governance and assurance relevant to your work |
| [Problem definition and shaping](../../कौशल/#problem-definition-and-shaping) | UK GDaD PCF | कार्यरत | You can:<br>• help to frame a problem characterised by managed levels of complexity, complication, or risk so that a solution can be created<br>• help to create options for solving problems at an appropriate level of detail |
| [Strategy design](../../कौशल/#strategy-design) | UK GDaD PCF | जागरूकता | You can:<br>• explain how organisational objectives link to designing strategy<br>• describe the purpose and application of strategy, standards, patterns, policies, roadmaps, vision, and mission statements |
| [Technical design throughout the life cycle](../../कौशल/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | कार्यरत | You can:<br>• create technical designs characterised by managed levels of risk, impact, and complexity<br>• provide guidance and support to teams using technical designs throughout the life cycle<br>• adapt a technical design if needed during delivery<br>• work with well-understood technology and identify appropriate patterns |
| [स्वास्थ्य और देखभाल सेवाओं की समझ](../../कौशल/#स्वास्थ्य-और-देखभाल-सेवाओं-की-समझ) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• उन क्लिनिकल और देखभाल कार्यप्रवाहों को समझाना जिनमें आपका काम सहायक है<br>• क्लिनिकल और देखभाल सहकर्मियों के साथ सामान्य स्वास्थ्य सेवा शब्दों का सही प्रयोग करना<br>• पहचानना कि कब कोई परिवर्तन रोगी देखभाल को प्रभावित कर सकता है, और उसे उठाना |
| [स्वास्थ्य डेटा अंतर-संचालनीयता](../../कौशल/#स्वास्थ्य-डेटा-अंतर-संचालनीयता) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• FHIR संसाधन, प्रोफ़ाइल और API पढ़ना और उनका उपयोग करना<br>• मार्गदर्शन में सरल इंटीग्रेशन बनाना या उनका परीक्षण करना<br>• किसी विनिर्देश के आधार पर संदेशों की जाँच करना |
| [सूचना शासन और डेटा संरक्षण](../../कौशल/#सूचना-शासन-और-डेटा-संरक्षण) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• अपने काम में डेटा संरक्षण सिद्धांत लागू करना<br>• डेटा संरक्षण प्रभाव आकलनों में योगदान देना<br>• सूचना अनुरोधों और अभिलेखों को सही ढंग से संभालना |
| [क्लिनिकल जोखिम प्रबंधन](../../कौशल/#क्लिनिकल-जोखिम-प्रबंधन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• ख़तरा कार्यशालाओं में भाग लेना और ख़तरा लॉग में योगदान देना<br>• अपने काम के लिए क्लिनिकल जोखिम प्रबंधन प्रक्रिया का पालन करना<br>• क्लिनिकल सुरक्षा केस के लिए परीक्षण परिणाम जैसे साक्ष्य देना |

### सामान्य योग्यताएँ और अनुभव

- समाधान डिज़ाइन का विशेषज्ञ ज्ञान, मास्टर स्तर या समकक्ष अनुभव।
- विश्लेषण, विकास या तकनीकी डिज़ाइन का अनुभव।

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
| 3 | विश्लेषण और निर्णय कौशल | 5 | 60 |
| 4 | योजना और संगठन कौशल | 3 | 27 |
| 5 | शारीरिक कौशल | 2 | 15 |
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
| | **कुल** | | **483** (बैंड 7: 466–539) |

UK GDaD PCF ग्रेड सुझाव (बैंड 6) से ऊँचे बैंड पर: स्वास्थ्य क्षेत्र के विज्ञापन इस भूमिका को बैंड 7 पर रखते हैं। ज्ञान का अंक मास्टर स्तर या समकक्ष पर है, क्योंकि यह पद एप्लिकेशन, डेटा, इंटीग्रेशन और सुरक्षा के पार डिज़ाइन करता है।

## बैंड 8a: सॉल्यूशन आर्किटेक्ट

**UK GDaD PCF स्तर: Solution architect**

> A solution architect is responsible for a single solution. They usually work independently on solutions where risk is low. They also often support or contribute to work led by more senior solution architects.
> 
> At this role level, you will:
> - build relationships with stakeholders across different business or technical areas in the organisation
> - be proactive in identifying opportunities to improve the organisation
> - follow best practice for solution design
> - use emerging technologies and approaches
> - help your team achieve its objective

### ज़िम्मेदारियाँ

- कर्मचारी उपकरणों या सरल रोगी-उन्मुख सेवाओं जैसी कम-जोखिम सेवाओं के लिए शुरू से अंत तक समाधान डिज़ाइन करना।
- ख़रीदने, बनाने और साझा प्लेटफ़ॉर्म के पुनः उपयोग सहित विकल्पों की तुलना करना और स्पष्ट कारणों के साथ एक की सिफ़ारिश करना।
- जहाँ उपलब्ध हों वहाँ खुले मानकों का उपयोग करते हुए समाधान के लिए इंटीग्रेशन, डेटा प्रवाह और पहचान तथा पहुँच डिज़ाइन करना।
- समाधान के ख़तरा पहचान और डेटा संरक्षण प्रभाव आकलनों में योगदान देना।
- डिज़ाइन प्राधिकरणों के सामने डिज़ाइन प्रस्तुत करना और निर्माण तथा लाइव होने में डिलीवरी टीमों की सहायता करना।
- एसोसिएट सॉल्यूशन आर्किटेक्टों को कोचिंग देना और उनके काम की समीक्षा करना।

### कौशल

| कौशल | स्रोत | अपेक्षित स्तर | इस स्तर का अर्थ |
| --- | --- | --- | --- |
| [Architect for the whole context](../../कौशल/#architect-for-the-whole-context) | UK GDaD PCF | कार्यरत | You can:<br>• align your work with the work being done by other architects and technical professionals<br>• track emerging issues, strategies, roadmaps, patterns and technologies over time to assess opportunities and risks to your work<br>• identify how other teams contribute to delivering outcomes through change |
| [Architecture communication](../../कौशल/#architecture-communication) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• lead the communication of complicated, complex or risky architecture topics with technical and non-technical stakeholders<br>• communicate with senior stakeholders across your organisation<br>• adapt your message and communication techniques to your audience<br>• advocate on behalf of a team to other stakeholders<br>• manage stakeholder expectations effectively |
| [Commercial perspective](../../कौशल/#commercial-perspective) | UK GDaD PCF | कार्यरत | You can:<br>• understand commercial processes and the appropriate internal contacts within a government department<br>• understand different sourcing strategies and when to apply them |
| [Community collaboration](../../कौशल/#community-collaboration) | UK GDaD PCF | कार्यरत | You can:<br>• contribute to the work of others<br>• motivate and empower teams<br>• create the right environment for teams to work in, and can identify the best team makeup depending on the situation<br>• recognise and deal with issues |
| [Making architectural decisions](../../कौशल/#making-architectural-decisions) | UK GDaD PCF | कार्यरत | You can:<br>• work with others to make architectural design decisions characterised by managed levels of risk and complexity<br>• identify and address architectural risks relevant to your team or domain, for example, business, data, or security<br>• engage with architectural governance and assurance to effectively manage decisions and risks, with support |
| [Problem definition and shaping](../../कौशल/#problem-definition-and-shaping) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• frame a problem characterised by medium complexity, complication, or risk so that a solution can be created<br>• produce architectural representations that enable different teams to have a shared understanding of problems throughout the life cycle<br>• describe options for solving problems so that appropriate delivery methods can be decided |
| [Strategy design](../../कौशल/#strategy-design) | UK GDaD PCF | कार्यरत | You can:<br>• support the development of a strategy or vision that aligns with organisational objectives<br>• challenge requirements and assumptions, and identify opportunities to develop strategy<br>• support the implementation of a strategy or vision, for example, by using a roadmap or plan<br>• use architectural principles, patterns, and constraints when appropriate |
| [Technical design throughout the life cycle](../../कौशल/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | कार्यरत | You can:<br>• create technical designs characterised by managed levels of risk, impact, and complexity<br>• provide guidance and support to teams using technical designs throughout the life cycle<br>• adapt a technical design if needed during delivery<br>• work with well-understood technology and identify appropriate patterns |
| [स्वास्थ्य और देखभाल सेवाओं की समझ](../../कौशल/#स्वास्थ्य-और-देखभाल-सेवाओं-की-समझ) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• उन क्लिनिकल और देखभाल कार्यप्रवाहों को समझाना जिनमें आपका काम सहायक है<br>• क्लिनिकल और देखभाल सहकर्मियों के साथ सामान्य स्वास्थ्य सेवा शब्दों का सही प्रयोग करना<br>• पहचानना कि कब कोई परिवर्तन रोगी देखभाल को प्रभावित कर सकता है, और उसे उठाना |
| [स्वास्थ्य डेटा अंतर-संचालनीयता](../../कौशल/#स्वास्थ्य-डेटा-अंतर-संचालनीयता) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• FHIR, HL7 संस्करण 2 और संदेश पैटर्न का उपयोग करके इंटीग्रेशन डिज़ाइन करना और बनाना<br>• FHIR संसाधन और कार्यान्वयन गाइड लिखना और उनकी प्रोफ़ाइल बनाना<br>• प्रणालियों के बीच जटिल मैपिंग और डेटा गुणवत्ता समस्याओं को सुलझाना |
| [सूचना शासन और डेटा संरक्षण](../../कौशल/#सूचना-शासन-और-डेटा-संरक्षण) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• डेटा संरक्षण प्रभाव आकलनों और सूचना साझाकरण समझौतों का नेतृत्व करना<br>• विधिक आधार, सहमति, गोपनीयता और प्रतिधारण पर टीमों को सलाह देना<br>• घटनाओं की जाँच करना और सुधारों की सिफ़ारिश करना |
| [क्लिनिकल जोखिम प्रबंधन](../../कौशल/#क्लिनिकल-जोखिम-प्रबंधन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• ख़तरा कार्यशालाओं में भाग लेना और ख़तरा लॉग में योगदान देना<br>• अपने काम के लिए क्लिनिकल जोखिम प्रबंधन प्रक्रिया का पालन करना<br>• क्लिनिकल सुरक्षा केस के लिए परीक्षण परिणाम जैसे साक्ष्य देना |
| [पहचान और पहुँच प्रबंधन](../../कौशल/#पहचान-और-पहुँच-प्रबंधन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• उपयोगकर्ता खाते और पहुँच अधिकार बनाना, बदलना और हटाना<br>• भूमिका-आधारित पहुँच नियमों के आधार पर पहुँच की जाँच करना |

### सामान्य योग्यताएँ और अनुभव

- समाधान डिज़ाइन या सॉफ़्टवेयर इंजीनियरिंग का पर्याप्त अनुभव, मास्टर डिग्री के समकक्ष स्तर पर।

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

UK GDaD PCF ग्रेड सुझाव (बैंड 7) से ऊँचे बैंड पर: स्वास्थ्य क्षेत्र के विज्ञापन इस भूमिका को बैंड 8a पर रखते हैं। योजना, नीति और कार्य करने की स्वतंत्रता का अंक बैंड 7 प्रोफ़ाइल से ऊपर है क्योंकि यह पद शुरू से अंत तक के डिज़ाइनों का स्वामित्व रखता है और डिज़ाइन प्राधिकरणों को विकल्प सुझाता है।

## बैंड 8b: वरिष्ठ सॉल्यूशन आर्किटेक्ट

**UK GDaD PCF स्तर: Senior solution architect**

> A senior solution architect is responsible for a single, more complex, solution. They usually work on solutions where the risk is moderate. They may lead and coach other solution architects.
> 
> At this role level, you will:
> - build relationships with senior stakeholders across different business or technical areas in the organisation
> - be proactive in identifying opportunities to improve the organisation
> - support multiple architecture projects
> - find and use emerging technologies and approaches
> - support others to follow best practice for solution architecture

### ज़िम्मेदारियाँ

- क्लिनिकल प्रणालियों या कई संगठनों में उपयोग होने वाली सेवाओं जैसे मध्यम जोखिम वाले जटिल समाधान डिज़ाइन करना।
- ख़रीद में आपूर्तिकर्ता उत्पादों के तकनीकी मूल्यांकन का नेतृत्व करना, जिसमें अंतर-संचालनीयता, सुरक्षा और क्लिनिकल सुरक्षा शामिल हैं।
- जहाँ समाधान चौबीसों घंटे देखभाल में सहायक हो, वहाँ लचीलेपन और व्यावसायिक निरंतरता के लिए डिज़ाइन करना।
- क्लिनिकल सुरक्षा अधिकारियों के साथ काम करना ताकि डिज़ाइन निर्णय और जोखिम नियंत्रण सुरक्षा केस में दर्ज हों।
- अन्य सॉल्यूशन आर्किटेक्टों को कोचिंग देना और उनके काम की समीक्षा करना।

### कौशल

| कौशल | स्रोत | अपेक्षित स्तर | इस स्तर का अर्थ |
| --- | --- | --- | --- |
| [Architect for the whole context](../../कौशल/#architect-for-the-whole-context) | UK GDaD PCF | कार्यरत | You can:<br>• align your work with the work being done by other architects and technical professionals<br>• track emerging issues, strategies, roadmaps, patterns and technologies over time to assess opportunities and risks to your work<br>• identify how other teams contribute to delivering outcomes through change |
| [Architecture communication](../../कौशल/#architecture-communication) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• lead the communication of complicated, complex or risky architecture topics with technical and non-technical stakeholders<br>• communicate with senior stakeholders across your organisation<br>• adapt your message and communication techniques to your audience<br>• advocate on behalf of a team to other stakeholders<br>• manage stakeholder expectations effectively |
| [Commercial perspective](../../कौशल/#commercial-perspective) | UK GDaD PCF | कार्यरत | You can:<br>• understand commercial processes and the appropriate internal contacts within a government department<br>• understand different sourcing strategies and when to apply them |
| [Community collaboration](../../कौशल/#community-collaboration) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../कौशल/#making-architectural-decisions) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• make and guide architectural design decisions characterised by medium risk and complexity<br>• identify and address architectural risks that affect multiple teams or domains<br>• use architectural governance and assurance to make design decisions and manage technical risks at the appropriate level<br>• contribute to the development of architectural governance and assurance |
| [Problem definition and shaping](../../कौशल/#problem-definition-and-shaping) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• frame a problem characterised by medium complexity, complication, or risk so that a solution can be created<br>• produce architectural representations that enable different teams to have a shared understanding of problems throughout the life cycle<br>• describe options for solving problems so that appropriate delivery methods can be decided |
| [Strategy design](../../कौशल/#strategy-design) | UK GDaD PCF | कार्यरत | You can:<br>• support the development of a strategy or vision that aligns with organisational objectives<br>• challenge requirements and assumptions, and identify opportunities to develop strategy<br>• support the implementation of a strategy or vision, for example, by using a roadmap or plan<br>• use architectural principles, patterns, and constraints when appropriate |
| [Technical design throughout the life cycle](../../कौशल/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• create technical designs characterised by medium risk, impact, and complexity<br>• maintain appropriate quality and architectural coherence of a technical design in response to change<br>• use feedback to optimise and refine technical designs throughout the life cycle |
| [स्वास्थ्य और देखभाल सेवाओं की समझ](../../कौशल/#स्वास्थ्य-और-देखभाल-सेवाओं-की-समझ) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• विश्लेषण करना कि कोई सेवा विभिन्न संगठनों के देखभाल मार्गों में कैसे बैठती है<br>• डिजिटल सेवाओं को आकार देने के लिए चिकित्सकों, देखभाल कर्मचारियों और रोगियों के साथ काम करना<br>• देखभाल, सुरक्षा और कर्मचारियों के कार्यभार पर डिजिटल निर्णयों का प्रभाव समझाना |
| [स्वास्थ्य डेटा अंतर-संचालनीयता](../../कौशल/#स्वास्थ्य-डेटा-अंतर-संचालनीयता) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• FHIR, HL7 संस्करण 2 और संदेश पैटर्न का उपयोग करके इंटीग्रेशन डिज़ाइन करना और बनाना<br>• FHIR संसाधन और कार्यान्वयन गाइड लिखना और उनकी प्रोफ़ाइल बनाना<br>• प्रणालियों के बीच जटिल मैपिंग और डेटा गुणवत्ता समस्याओं को सुलझाना |
| [सूचना शासन और डेटा संरक्षण](../../कौशल/#सूचना-शासन-और-डेटा-संरक्षण) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• डेटा संरक्षण प्रभाव आकलनों और सूचना साझाकरण समझौतों का नेतृत्व करना<br>• विधिक आधार, सहमति, गोपनीयता और प्रतिधारण पर टीमों को सलाह देना<br>• घटनाओं की जाँच करना और सुधारों की सिफ़ारिश करना |
| [क्लिनिकल जोखिम प्रबंधन](../../कौशल/#क्लिनिकल-जोखिम-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• किसी उत्पाद या परिवर्तन के लिए ख़तरा पहचान और जोखिम आकलन का नेतृत्व करना<br>• ख़तरा लॉग और क्लिनिकल सुरक्षा केस रिपोर्ट लिखना और बनाए रखना<br>• उत्पाद टीमों के साथ जोखिम नियंत्रणों पर सहमति बनाना और जाँचना कि वे काम करते हैं<br>• क्लिनिकल जोखिम प्रबंधन मानकों को लागू करने पर टीमों को सलाह देना |
| [पहचान और पहुँच प्रबंधन](../../कौशल/#पहचान-और-पहुँच-प्रबंधन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• उपयोगकर्ता खाते और पहुँच अधिकार बनाना, बदलना और हटाना<br>• भूमिका-आधारित पहुँच नियमों के आधार पर पहुँच की जाँच करना |
| [चिकित्सा उपकरण सॉफ़्टवेयर विनियमन](../../कौशल/#चिकित्सा-उपकरण-सॉफ़्टवेयर-विनियमन) | यह संदर्भ | जागरूकता | आप ये कर सकते हैं:<br>• समझाना कि कुछ स्वास्थ्य सॉफ़्टवेयर चिकित्सा उपकरण के रूप में विनियमित होते हैं<br>• जानना कि जब कोई उत्पाद चिकित्सा उपकरण हो सकता है तो किससे पूछना है |
| [संगठनात्मक जोखिम प्रबंधन](../../कौशल/#संगठनात्मक-जोखिम-प्रबंधन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• अपने क्षेत्र के जोखिम दर्ज करना और अद्यतन करना<br>• नियंत्रण सुझाना और कार्रवाइयों को ट्रैक करना |

### सामान्य योग्यताएँ और अनुभव

- कई विधाओं में जटिल समाधान डिज़ाइन करने का व्यापक अनुभव, मास्टर डिग्री से आगे के स्तर पर।

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
| 8 | वित्तीय और भौतिक संसाधनों की ज़िम्मेदारी | 2 | 12 |
| 9 | लोगों की ज़िम्मेदारी | 3 | 21 |
| 10 | सूचना संसाधनों की ज़िम्मेदारी | 5 | 34 |
| 11 | अनुसंधान और विकास की ज़िम्मेदारी | 3 | 21 |
| 12 | कार्य करने की स्वतंत्रता | 5 | 45 |
| 13 | शारीरिक प्रयास | 1 | 3 |
| 14 | मानसिक प्रयास | 4 | 18 |
| 15 | भावनात्मक प्रयास | 1 | 5 |
| 16 | कार्य परिस्थितियाँ | 2 | 7 |
| | **कुल** | | **604** (बैंड 8b: 585–629) |

UK GDaD PCF ग्रेड सुझाव (बैंड 8a) से ऊँचे बैंड पर: स्वास्थ्य क्षेत्र के विज्ञापन इस भूमिका को बैंड 8b पर रखते हैं। ज्ञान का अंक स्तर 8 पर है, एप्लिकेशन, डेटा, इंटीग्रेशन, सुरक्षा और क्लिनिकल सुरक्षा जैसी कई विधाओं के विशेषज्ञ ज्ञान के लिए।

## बैंड 8c: लीड सॉल्यूशन आर्किटेक्ट

**UK GDaD PCF स्तर: Lead solution architect**

> A lead solution architect is responsible for a group of solution architecture projects, or a single more complex area. They may lead teams of more junior solution architects.
> 
> At this role level, you will:
> - build relationships with senior stakeholders across multiple business or technical areas in the organisation
> - be proactive in identifying opportunities to improve the organisation
> - support multiple architecture projects or programmes
> - find and use emerging technologies and approaches
> - develop best practice for solution architecture

### ज़िम्मेदारियाँ

- किसी कार्यक्रम या जटिल क्षेत्र, जैसे इलेक्ट्रॉनिक रोगी अभिलेख के प्रतिस्थापन, के सॉल्यूशन आर्किटेक्चर का नेतृत्व करना।
- सुनिश्चित करना कि पूरे कार्यक्रम के समाधान एकरूप, अंतर-संचालनीय और लक्षित आर्किटेक्चर के अनुरूप हों।
- डिज़ाइन जोखिमों, निर्भरताओं, आपूर्तिकर्ता विकल्पों और लागतों पर कार्यक्रम बोर्डों को सलाह देना।
- डिज़ाइन प्राधिकरणों में अन्य सॉल्यूशन आर्किटेक्टों के डिज़ाइनों का आश्वासन देना।
- सॉल्यूशन आर्किटेक्टों की एक टीम का नेतृत्व और विकास करना।

### कौशल

| कौशल | स्रोत | अपेक्षित स्तर | इस स्तर का अर्थ |
| --- | --- | --- | --- |
| [Architect for the whole context](../../कौशल/#architect-for-the-whole-context) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• work to support wider organisational objectives beyond your immediate goals​<br>• track emerging internal and external issues over time that could affect the work of teams across the organisation<br>• take action to solve or mitigate problems by influencing colleagues across the organisation |
| [Architecture communication](../../कौशल/#architecture-communication) | UK GDaD PCF | विशेषज्ञ | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Commercial perspective](../../कौशल/#commercial-perspective) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• identify appropriate contractual frameworks and approaches<br>• identify, evaluate and select appropriate suppliers |
| [Community collaboration](../../कौशल/#community-collaboration) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../कौशल/#making-architectural-decisions) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• make and guide architectural design decisions characterised by medium risk and complexity<br>• identify and address architectural risks that affect multiple teams or domains<br>• use architectural governance and assurance to make design decisions and manage technical risks at the appropriate level<br>• contribute to the development of architectural governance and assurance |
| [Problem definition and shaping](../../कौशल/#problem-definition-and-shaping) | UK GDaD PCF | विशेषज्ञ | You can:<br>• lead the framing of a problem characterised by high complexity, complication, or risk so that a solution can be created<br>• coach others in defining problems and describing appropriate options for solutions<br>• help others challenge requirements and assumptions, and identify opportunities when defining problems and solution options |
| [Strategy design](../../कौशल/#strategy-design) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• define strategies or visions across teams that align with organisational objectives<br>• direct the implementation of a strategy or vision, for example, by creating roadmaps or plans<br>• define architectural principles and patterns<br>• develop or maintain strategy in response to feedback and findings |
| [Technical design throughout the life cycle](../../कौशल/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | विशेषज्ञ | You can:<br>• create technical designs characterised by high risk, impact, and complexity<br>• lead and guide others in creating technical designs that achieve organisational objectives<br>• use feedback to optimise and refine standards for technical designs throughout the life cycle |
| [स्वास्थ्य और देखभाल सेवाओं की समझ](../../कौशल/#स्वास्थ्य-और-देखभाल-सेवाओं-की-समझ) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• विश्लेषण करना कि कोई सेवा विभिन्न संगठनों के देखभाल मार्गों में कैसे बैठती है<br>• डिजिटल सेवाओं को आकार देने के लिए चिकित्सकों, देखभाल कर्मचारियों और रोगियों के साथ काम करना<br>• देखभाल, सुरक्षा और कर्मचारियों के कार्यभार पर डिजिटल निर्णयों का प्रभाव समझाना |
| [स्वास्थ्य डेटा अंतर-संचालनीयता](../../कौशल/#स्वास्थ्य-डेटा-अंतर-संचालनीयता) | यह संदर्भ | विशेषज्ञ | आप ये कर सकते हैं:<br>• संगठन के लिए अंतर-संचालनीयता मानक और रणनीति तय करना<br>• राष्ट्रीय या अंतर-संगठनात्मक मानक कार्य का नेतृत्व करना<br>• कई प्रणालियों में महत्वपूर्ण इंटीग्रेशन के डिज़ाइन का आश्वासन देना |
| [सूचना शासन और डेटा संरक्षण](../../कौशल/#सूचना-शासन-और-डेटा-संरक्षण) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• डेटा संरक्षण प्रभाव आकलनों और सूचना साझाकरण समझौतों का नेतृत्व करना<br>• विधिक आधार, सहमति, गोपनीयता और प्रतिधारण पर टीमों को सलाह देना<br>• घटनाओं की जाँच करना और सुधारों की सिफ़ारिश करना |
| [क्लिनिकल जोखिम प्रबंधन](../../कौशल/#क्लिनिकल-जोखिम-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• किसी उत्पाद या परिवर्तन के लिए ख़तरा पहचान और जोखिम आकलन का नेतृत्व करना<br>• ख़तरा लॉग और क्लिनिकल सुरक्षा केस रिपोर्ट लिखना और बनाए रखना<br>• उत्पाद टीमों के साथ जोखिम नियंत्रणों पर सहमति बनाना और जाँचना कि वे काम करते हैं<br>• क्लिनिकल जोखिम प्रबंधन मानकों को लागू करने पर टीमों को सलाह देना |
| [चिकित्सा उपकरण सॉफ़्टवेयर विनियमन](../../कौशल/#चिकित्सा-उपकरण-सॉफ़्टवेयर-विनियमन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• चिकित्सा उपकरण मानकों को पूरा करने वाली सॉफ़्टवेयर जीवनचक्र प्रक्रिया का पालन करना<br>• ऐसी प्रक्रिया के लिए आवश्यक अभिलेख तैयार करना |
| [संगठनात्मक जोखिम प्रबंधन](../../कौशल/#संगठनात्मक-जोखिम-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• किसी निदेशालय या कार्यक्रम के लिए जोखिम प्रक्रिया चलाना<br>• जोखिम सहनशीलता के आधार पर जोखिमों का आकलन करना और उन्हें आगे बढ़ाना<br>• समितियों को जोखिमों की रिपोर्ट देना |
| [लोगों का प्रबंधन](../../कौशल/#लोगों-का-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• किसी टीम का लाइन प्रबंधन करना, उद्देश्य तय करना और मूल्यांकन करना<br>• कल्याण का समर्थन करना और उपस्थिति, प्रदर्शन तथा आचरण का प्रबंधन करना<br>• टीम के विकास और उत्तराधिकार की योजना बनाना |

### सामान्य योग्यताएँ और अनुभव

- जटिल कार्यक्रमों के सॉल्यूशन आर्किटेक्चर का नेतृत्व करने का व्यापक अनुभव।

### बैंड की रूपरेखा

- **ज्ञान:** विशेषज्ञ ज्ञान, और संगठन तथा क्षेत्र की व्यापक समझ।
- **स्वायत्तता:** किसी कार्य के लिए रणनीति तय करता है; किसी निदेशक के प्रति जवाबदेह होता है।
- **दायरा:** एक कार्य या विभाग।
- **नेतृत्व:** कई प्रबंधन स्तरों के माध्यम से किसी कार्य का नेतृत्व करता है।
- **जवाबदेही:** किसी कार्य का प्रदर्शन, कार्यबल और बजट।

### कार्य-मूल्यांकन (उदाहरणात्मक)

| # | कारक | स्तर | अंक |
| --- | --- | --- | --- |
| 1 | संचार और संबंध कौशल | 5 | 45 |
| 2 | ज्ञान, प्रशिक्षण और अनुभव | 8 | 240 |
| 3 | विश्लेषण और निर्णय कौशल | 5 | 60 |
| 4 | योजना और संगठन कौशल | 5 | 60 |
| 5 | शारीरिक कौशल | 2 | 15 |
| 6 | रोगी और सेवार्थी देखभाल की ज़िम्मेदारी | 1 | 4 |
| 7 | नीति और सेवा विकास की ज़िम्मेदारी | 5 | 45 |
| 8 | वित्तीय और भौतिक संसाधनों की ज़िम्मेदारी | 3 | 21 |
| 9 | लोगों की ज़िम्मेदारी | 4 | 32 |
| 10 | सूचना संसाधनों की ज़िम्मेदारी | 5 | 34 |
| 11 | अनुसंधान और विकास की ज़िम्मेदारी | 3 | 21 |
| 12 | कार्य करने की स्वतंत्रता | 5 | 45 |
| 13 | शारीरिक प्रयास | 1 | 3 |
| 14 | मानसिक प्रयास | 4 | 18 |
| 15 | भावनात्मक प्रयास | 1 | 5 |
| 16 | कार्य परिस्थितियाँ | 2 | 7 |
| | **कुल** | | **655** (बैंड 8c: 630–674) |

UK GDaD PCF ग्रेड सुझाव (बैंड 8b) से ऊँचे बैंड पर: स्वास्थ्य क्षेत्र के विज्ञापन इस भूमिका को बैंड 8c पर रखते हैं। योजना, नीति और लोगों का अंक बैंड 8b प्रोफ़ाइल से ऊपर है क्योंकि यह पद पूरे कार्यक्रम के आर्किटेक्चर की योजना बनाता है और सॉल्यूशन आर्किटेक्टों की एक टीम का नेतृत्व करता है।

## बैंड 8d: प्रधान सॉल्यूशन आर्किटेक्ट

**UK GDaD PCF स्तर: Principal solution architect**

> A principal solution architect can be responsible for a large programme or group of solution architecture projects, or a single, very complex or critical business area.
> 
> At this role level, you will:
> - lead teams of more junior solution architects
> - lead multiple architecture projects or programmes
> - build relationships with senior stakeholders across multiple business or technical areas in the organisation and its partners
> - be proactive in identifying opportunities to improve the organisation and its partners
> - work with technology partners to inform their roadmaps
> - take a leading role in the overall direction of business and digital capabilities
> - inspire other architects and help them understand how to meet organisational goals

### ज़िम्मेदारियाँ

- संगठन के सबसे बड़े या सबसे महत्वपूर्ण कार्यक्रमों के सॉल्यूशन आर्किटेक्चर का नेतृत्व करना।
- संगठन के लिए सॉल्यूशन आर्किटेक्चर मानक, पैटर्न और विधियाँ तय करना।
- महत्वपूर्ण, साझा स्वास्थ्य और देखभाल सेवाओं के डिज़ाइन पर निदेशकों और साझेदार संगठनों को सलाह देना।
- कार्यक्रमों, आपूर्तिकर्ताओं और साझेदार संगठनों के बीच सबसे कठिन डिज़ाइन टकराव सुलझाना।
- सॉल्यूशन आर्किटेक्चर अभ्यास का नेतृत्व करना और उसके लोगों का विकास करना।

### कौशल

| कौशल | स्रोत | अपेक्षित स्तर | इस स्तर का अर्थ |
| --- | --- | --- | --- |
| [Architect for the whole context](../../कौशल/#architect-for-the-whole-context) | UK GDaD PCF | विशेषज्ञ | You can:<br>• assess how trends in society and industry practices might impact the organisation<br>• work with people outside of your organisation to inform policies, strategies and standards<br>• anticipate changes to policy and build resilience through your architectural work<br>• coach others in identifying important trends |
| [Architecture communication](../../कौशल/#architecture-communication) | UK GDaD PCF | विशेषज्ञ | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Commercial perspective](../../कौशल/#commercial-perspective) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• identify appropriate contractual frameworks and approaches<br>• identify, evaluate and select appropriate suppliers |
| [Community collaboration](../../कौशल/#community-collaboration) | UK GDaD PCF | विशेषज्ञ | You can:<br>• solve and unblock issues between teams or departments at the highest level<br>• coach the organisation on team dynamics and conflict resolution, while also building and growing the community |
| [Making architectural decisions](../../कौशल/#making-architectural-decisions) | UK GDaD PCF | विशेषज्ञ | You can:<br>• make and guide architectural design decisions characterised by high levels of risk and complexity<br>• identify and address architectural risks across the organisation or wider government<br>• lead and evolve architectural governance and assurance<br>• represent architectural governance as part of wider governance, for example, legal or commercial |
| [Problem definition and shaping](../../कौशल/#problem-definition-and-shaping) | UK GDaD PCF | विशेषज्ञ | You can:<br>• lead the framing of a problem characterised by high complexity, complication, or risk so that a solution can be created<br>• coach others in defining problems and describing appropriate options for solutions<br>• help others challenge requirements and assumptions, and identify opportunities when defining problems and solution options |
| [Strategy design](../../कौशल/#strategy-design) | UK GDaD PCF | विशेषज्ञ | You can:<br>• define and connect strategies or visions across the organisation or wider government<br>• enable the implementation of strategies or visions across the organisation or wider government, for example, by advocating for resources and removing blockers |
| [Technical design throughout the life cycle](../../कौशल/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | विशेषज्ञ | You can:<br>• create technical designs characterised by high risk, impact, and complexity<br>• lead and guide others in creating technical designs that achieve organisational objectives<br>• use feedback to optimise and refine standards for technical designs throughout the life cycle |
| [स्वास्थ्य और देखभाल सेवाओं की समझ](../../कौशल/#स्वास्थ्य-और-देखभाल-सेवाओं-की-समझ) | यह संदर्भ | विशेषज्ञ | आप ये कर सकते हैं:<br>• स्वास्थ्य और देखभाल प्रणाली की गहरी समझ के आधार पर संगठन की रणनीति को आकार देना<br>• स्वास्थ्य और देखभाल साझेदारों और प्रमुखों के समक्ष संगठन का प्रतिनिधित्व करना<br>• अनुमान लगाना कि नीति और सेवा में परिवर्तन डिजिटल सेवाओं और देखभाल को कैसे प्रभावित करेंगे |
| [स्वास्थ्य डेटा अंतर-संचालनीयता](../../कौशल/#स्वास्थ्य-डेटा-अंतर-संचालनीयता) | यह संदर्भ | विशेषज्ञ | आप ये कर सकते हैं:<br>• संगठन के लिए अंतर-संचालनीयता मानक और रणनीति तय करना<br>• राष्ट्रीय या अंतर-संगठनात्मक मानक कार्य का नेतृत्व करना<br>• कई प्रणालियों में महत्वपूर्ण इंटीग्रेशन के डिज़ाइन का आश्वासन देना |
| [सूचना शासन और डेटा संरक्षण](../../कौशल/#सूचना-शासन-और-डेटा-संरक्षण) | यह संदर्भ | विशेषज्ञ | आप ये कर सकते हैं:<br>• सूचना शासन नीति और रणनीति तय करना<br>• सूचना जोखिम और अनुपालन पर बोर्ड को सलाह देना<br>• नियामकों और साझेदारों के समक्ष संगठन का प्रतिनिधित्व करना |
| [क्लिनिकल जोखिम प्रबंधन](../../कौशल/#क्लिनिकल-जोखिम-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• किसी उत्पाद या परिवर्तन के लिए ख़तरा पहचान और जोखिम आकलन का नेतृत्व करना<br>• ख़तरा लॉग और क्लिनिकल सुरक्षा केस रिपोर्ट लिखना और बनाए रखना<br>• उत्पाद टीमों के साथ जोखिम नियंत्रणों पर सहमति बनाना और जाँचना कि वे काम करते हैं<br>• क्लिनिकल जोखिम प्रबंधन मानकों को लागू करने पर टीमों को सलाह देना |
| [चिकित्सा उपकरण सॉफ़्टवेयर विनियमन](../../कौशल/#चिकित्सा-उपकरण-सॉफ़्टवेयर-विनियमन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• चिकित्सा उपकरण मानकों को पूरा करने वाली सॉफ़्टवेयर जीवनचक्र प्रक्रिया का पालन करना<br>• ऐसी प्रक्रिया के लिए आवश्यक अभिलेख तैयार करना |
| [संगठनात्मक जोखिम प्रबंधन](../../कौशल/#संगठनात्मक-जोखिम-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• किसी निदेशालय या कार्यक्रम के लिए जोखिम प्रक्रिया चलाना<br>• जोखिम सहनशीलता के आधार पर जोखिमों का आकलन करना और उन्हें आगे बढ़ाना<br>• समितियों को जोखिमों की रिपोर्ट देना |
| [लोगों का प्रबंधन](../../कौशल/#लोगों-का-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• किसी टीम का लाइन प्रबंधन करना, उद्देश्य तय करना और मूल्यांकन करना<br>• कल्याण का समर्थन करना और उपस्थिति, प्रदर्शन तथा आचरण का प्रबंधन करना<br>• टीम के विकास और उत्तराधिकार की योजना बनाना |
| [बजट प्रबंधन](../../कौशल/#बजट-प्रबंधन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• किसी छोटे बजट के मुक़ाबले ख़र्च को ट्रैक करना और अंतर बताना<br>• अपनी सीमा के भीतर ख़र्च स्वीकृत करना |

### सामान्य योग्यताएँ और अनुभव

- कई कार्यक्रमों या संगठनों में सॉल्यूशन आर्किटेक्चर का नेतृत्व करने का व्यापक अनुभव।

### बैंड की रूपरेखा

- **ज्ञान:** विभिन्न कार्यों और व्यापक स्वास्थ्य एवं देखभाल प्रणाली का रणनीतिक ज्ञान।
- **स्वायत्तता:** पूरे संगठन की रणनीति को आकार देता है; किसी निदेशक का प्रतिनिधित्व करता है।
- **दायरा:** एक प्रमुख कार्य या कई कार्य।
- **नेतृत्व:** कई कार्यों या एक बड़े विभाग का नेतृत्व करता है।
- **जवाबदेही:** प्रमुख कार्य, बड़े बजट और पूरे संगठन के जोखिम।

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
| 8 | वित्तीय और भौतिक संसाधनों की ज़िम्मेदारी | 4 | 32 |
| 9 | लोगों की ज़िम्मेदारी | 4 | 32 |
| 10 | सूचना संसाधनों की ज़िम्मेदारी | 6 | 46 |
| 11 | अनुसंधान और विकास की ज़िम्मेदारी | 2 | 12 |
| 12 | कार्य करने की स्वतंत्रता | 6 | 60 |
| 13 | शारीरिक प्रयास | 1 | 3 |
| 14 | मानसिक प्रयास | 4 | 18 |
| 15 | भावनात्मक प्रयास | 1 | 5 |
| 16 | कार्य परिस्थितियाँ | 2 | 7 |
| | **कुल** | | **699** (बैंड 8d: 675–720) |

UK GDaD PCF ग्रेड सुझाव (बैंड 8c) से ऊँचे बैंड पर: स्वास्थ्य क्षेत्र के विज्ञापन इस भूमिका को बैंड 8d पर रखते हैं। कार्य करने की स्वतंत्रता स्तर 6 पर है क्योंकि यह पद संगठन के सॉल्यूशन आर्किटेक्चर मानक तय करता है; वित्तीय संसाधन और लोग स्तर 4 पर हैं क्योंकि यह अभ्यास और उसके बजट का नेतृत्व करता है।


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
