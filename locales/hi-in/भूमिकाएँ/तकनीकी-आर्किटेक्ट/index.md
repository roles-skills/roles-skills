# तकनीकी आर्किटेक्ट

> यह एक सामान्य डिजिटल स्वास्थ्य सेवा संगठन के लिए एक उदाहरणात्मक संदर्भ प्रोफ़ाइल है। यह किसी भी नियोक्ता का आधिकारिक कार्य-विवरण नहीं है, और इसके कार्य-मूल्यांकन अंक औपचारिक मूल्यांकन नहीं हैं।

> इस पाठ का अंग्रेज़ी से अनुवाद एक कृत्रिम बुद्धिमत्ता सहायक ने किया है, और किसी मूल हिन्दी भाषी ने अभी तक इसकी समीक्षा नहीं की है। यूके सरकार के डिजिटल और डेटा पेशा क्षमता ढाँचे (UK GDaD PCF) और ESCO के उद्धरण अंग्रेज़ी में ही रखे गए हैं।

**परिवार:** [आर्किटेक्चर](../../#आर्किटेक्चर)  
**बैंड:** 6, 7, 8a, 8b, 8c  
**UK GDaD PCF भूमिका:** [Technical architect](https://understand-digital-data-roles-skills.service.gov.uk/role/technical-architect/)  
**ESCO व्यवसाय:** [software architect](http://data.europa.eu/esco/occupation/d0aa0792-4345-474b-9365-686cf4869d2e) (ISCO-08 2512); [cloud architect](http://data.europa.eu/esco/occupation/2fb96c6c-8d0b-4ef0-b1ee-3e493305e4eb) (ISCO-08 2512)

## सारांश

तकनीकी आर्किटेक्ट संगठन की डिजिटल स्वास्थ्य सेवाओं की तकनीकी संरचना डिज़ाइन करते हैं: घटक, प्लेटफ़ॉर्म, होस्टिंग, इंटीग्रेशन पैटर्न, और सुरक्षा, प्रदर्शन तथा लचीलेपन जैसी ग़ैर-कार्यात्मक विशेषताएँ। वे डेवलपरों और DevOps इंजीनियरों के साथ निकटता से काम करते हैं, डिलीवरी टीमों को तकनीकी नेतृत्व देते हैं, और सुनिश्चित करते हैं कि सेवाएँ टिकाऊ बनें और चलाने में सुरक्षित हों।

## एक डिजिटल स्वास्थ्य सेवा संगठन में

- क्लिनिकल सेवाओं को अक्सर उच्च उपलब्धता और तेज़ पुनर्प्राप्ति चाहिए, इसलिए तकनीकी डिज़ाइनों में विफलता और आंशिक संचालन की योजना होनी चाहिए।
- डिज़ाइनों को डिफ़ॉल्ट रूप से एन्क्रिप्शन, पहुँच नियंत्रण और ऑडिट के माध्यम से गोपनीय स्वास्थ्य जानकारी की रक्षा करनी चाहिए।
- सेवाएँ कई क्लिनिकल प्रणालियों और साझा प्लेटफ़ॉर्म से जुड़ती हैं, अक्सर HL7 FHIR API और संदेशों के माध्यम से, इसलिए इंटीग्रेशन पैटर्न डिज़ाइन के केंद्र में हैं।
- कैशिंग, पुनःप्रयास और समय प्रबंधन जैसे तकनीकी डिज़ाइन विकल्प क्लिनिकल ख़तरे पैदा कर सकते हैं, इसलिए आर्किटेक्ट सुरक्षा केस में योगदान देते हैं।
- पुरानी क्लिनिकल प्रणालियाँ और चिकित्सा उपकरण तकनीक, नेटवर्किंग और होस्टिंग के विकल्पों को सीमित कर सकते हैं।

## UK GDaD PCF भूमिका विवरण (अंग्रेज़ी मूल)

> A technical architect provides technical leadership and architectural design.

## भूमिका स्तर

| बैंड | शीर्षक | UK GDaD PCF स्तर | यूके सिविल सेवा ग्रेड | कार्य-मूल्यांकन अंक |
| --- | --- | --- | --- | --- |
| 6 | [एसोसिएट तकनीकी आर्किटेक्ट](#बैंड-6-एसोसिएट-तकनीकी-आर्किटेक्ट) | Associate technical architect | EO/HEO | 412 |
| 7 | [तकनीकी आर्किटेक्ट](#बैंड-7-तकनीकी-आर्किटेक्ट) | Technical architect | SEO/G7 | 496 |
| 8a | [वरिष्ठ तकनीकी आर्किटेक्ट](#बैंड-8a-वरिष्ठ-तकनीकी-आर्किटेक्ट) | Senior technical architect | SEO/G7 | 560 |
| 8b | [लीड तकनीकी आर्किटेक्ट](#बैंड-8b-लीड-तकनीकी-आर्किटेक्ट) | Lead technical architect | G7/G6 | 613 |
| 8c | [प्रधान तकनीकी आर्किटेक्ट](#बैंड-8c-प्रधान-तकनीकी-आर्किटेक्ट) | Principal technical architect | G6 | 662 |

## बैंड 6: एसोसिएट तकनीकी आर्किटेक्ट

**UK GDaD PCF स्तर: Associate technical architect**

> An associate technical architect supports technical architects in putting forward designs as solutions to technology challenges, usually under supervision.
> 
> At this role level, you will:
> - work closely with developers when designing appropriate solutions
> - have an understanding of the overall strategy and how your work supports it

### ज़िम्मेदारियाँ

- तकनीकी आरेख बनाना और मौजूदा सेवाओं के घटकों, होस्टिंग और इंटीग्रेशन का दस्तावेज़ीकरण करना।
- मार्गदर्शन के साथ तकनीकी विकल्पों पर शोध करना और उनके फ़ायदे-नुक़सान का सारांश बनाना।
- डेवलपरों के साथ काम करके जाँचना कि निर्माण सहमत डिज़ाइनों और पैटर्न का पालन करते हैं।
- तकनीकी निर्णय दर्ज करना और डिज़ाइन दस्तावेज़ अद्यतन रखना।

### कौशल

| कौशल | स्रोत | अपेक्षित स्तर | इस स्तर का अर्थ |
| --- | --- | --- | --- |
| [Architect for the whole context](../../कौशल/#architect-for-the-whole-context) | UK GDaD PCF | जागरूकता | You can:<br>• identify relevant information that can inform your architectural work, such as strategies, roadmaps, policies and technical trends<br>• understand how your work supports the team in enabling change​ |
| [Architecture communication](../../कौशल/#architecture-communication) | UK GDaD PCF | जागरूकता | You can:<br>• show an awareness of different ways of creating architecture representations for a limited audience, including technical and non-technical stakeholders<br>• gather and explain information to be used in architecture representations |
| [Community collaboration](../../कौशल/#community-collaboration) | UK GDaD PCF | जागरूकता | You can:<br>• understand the work of others and the importance of team dynamics, collaboration and feedback |
| [Making architectural decisions](../../कौशल/#making-architectural-decisions) | UK GDaD PCF | जागरूकता | You can:<br>• describe the reasoning behind architectural design decisions<br>• gather information to inform decisions<br>• understand architectural governance and assurance relevant to your work |
| [Strategy design](../../कौशल/#strategy-design) | UK GDaD PCF | जागरूकता | You can:<br>• explain how organisational objectives link to designing strategy<br>• describe the purpose and application of strategy, standards, patterns, policies, roadmaps, vision, and mission statements |
| [Technical design throughout the life cycle](../../कौशल/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | कार्यरत | You can:<br>• create technical designs characterised by managed levels of risk, impact, and complexity<br>• provide guidance and support to teams using technical designs throughout the life cycle<br>• adapt a technical design if needed during delivery<br>• work with well-understood technology and identify appropriate patterns |
| [स्वास्थ्य और देखभाल सेवाओं की समझ](../../कौशल/#स्वास्थ्य-और-देखभाल-सेवाओं-की-समझ) | यह संदर्भ | जागरूकता | आप ये कर सकते हैं:<br>• स्वास्थ्य और देखभाल प्रणाली के मुख्य भागों और संगठन द्वारा समर्थित सेवाओं का वर्णन करना<br>• समझाना कि आपके काम में रोगी सुरक्षा और गोपनीयता क्यों महत्वपूर्ण हैं |
| [स्वास्थ्य डेटा अंतर-संचालनीयता](../../कौशल/#स्वास्थ्य-डेटा-अंतर-संचालनीयता) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• FHIR संसाधन, प्रोफ़ाइल और API पढ़ना और उनका उपयोग करना<br>• मार्गदर्शन में सरल इंटीग्रेशन बनाना या उनका परीक्षण करना<br>• किसी विनिर्देश के आधार पर संदेशों की जाँच करना |
| [सूचना शासन और डेटा संरक्षण](../../कौशल/#सूचना-शासन-और-डेटा-संरक्षण) | यह संदर्भ | जागरूकता | आप ये कर सकते हैं:<br>• व्यक्तिगत और स्वास्थ्य जानकारी संभालने के संगठन के नियमों का पालन करना<br>• डेटा उल्लंघन या बाल-बाल बची घटना को पहचानना और रिपोर्ट करना |
| [क्लिनिकल जोखिम प्रबंधन](../../कौशल/#क्लिनिकल-जोखिम-प्रबंधन) | यह संदर्भ | जागरूकता | आप ये कर सकते हैं:<br>• समझाना कि स्वास्थ्य आईटी प्रणालियाँ रोगियों को कैसे नुकसान पहुँचा सकती हैं, उदाहरण के लिए ग़लत, गायब या विलंबित जानकारी से<br>• संभावित क्लिनिकल सुरक्षा मुद्दे की रिपोर्ट सही माध्यम से करना |

### सामान्य योग्यताएँ और अनुभव

- कंप्यूटिंग या संबंधित विषय में डिग्री, या सॉफ़्टवेयर या इन्फ़्रास्ट्रक्चर इंजीनियरिंग में समकक्ष अनुभव।
- तकनीकी डिज़ाइन का विशेषज्ञ ज्ञान, स्नातकोत्तर डिप्लोमा स्तर या समकक्ष अनुभव।

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
| 5 | शारीरिक कौशल | 2 | 15 |
| 6 | रोगी और सेवार्थी देखभाल की ज़िम्मेदारी | 1 | 4 |
| 7 | नीति और सेवा विकास की ज़िम्मेदारी | 3 | 21 |
| 8 | वित्तीय और भौतिक संसाधनों की ज़िम्मेदारी | 1 | 5 |
| 9 | लोगों की ज़िम्मेदारी | 1 | 5 |
| 10 | सूचना संसाधनों की ज़िम्मेदारी | 5 | 34 |
| 11 | अनुसंधान और विकास की ज़िम्मेदारी | 2 | 12 |
| 12 | कार्य करने की स्वतंत्रता | 4 | 32 |
| 13 | शारीरिक प्रयास | 1 | 3 |
| 14 | मानसिक प्रयास | 3 | 12 |
| 15 | भावनात्मक प्रयास | 1 | 5 |
| 16 | कार्य परिस्थितियाँ | 2 | 7 |
| | **कुल** | | **412** (बैंड 6: 396–465) |

UK GDaD PCF ग्रेड सुझाव (बैंड 5) से ऊँचे बैंड पर: स्वास्थ्य क्षेत्र के विज्ञापन इस भूमिका को बैंड 6 पर रखते हैं। ज्ञान का अंक स्नातकोत्तर डिप्लोमा स्तर पर है, और सूचना संसाधन स्तर 5 पर है क्योंकि यह पद प्रमुख सूचना प्रणालियों के हिस्से डिज़ाइन करता है।

## बैंड 7: तकनीकी आर्किटेक्ट

**UK GDaD PCF स्तर: Technical architect**

> A technical architect is responsible for the design and build of technical architecture.
> 
> At this role level, you will:
> - undertake structured analysis of technical issues, translating this analysis into technical designs that describe a solution
> - be consulted about design and provide design patterns
> - identify deeper issues that need fixing
> - look for opportunities to collaborate and reuse components, communicating with both technical and non-technical stakeholders

### ज़िम्मेदारियाँ

- किसी सेवा का तकनीकी आर्किटेक्चर डिज़ाइन करना, जिसमें घटक, होस्टिंग, इंटीग्रेशन और सुरक्षा शामिल हैं।
- डिलीवरी टीमों को डिज़ाइन पैटर्न देना और उनके तकनीकी डिज़ाइनों तथा कोड संरचना की समीक्षा करना।
- सेवा स्वामियों के साथ उपलब्धता, प्रदर्शन और पुनर्प्राप्ति लक्ष्यों जैसी ग़ैर-कार्यात्मक आवश्यकताएँ परिभाषित करना।
- तकनीकी ऋण और असमर्थित तकनीक पहचानना, और उसे ठीक करने की योजना बनाना।
- क्लिनिकल सुरक्षा केस के लिए तकनीकी ख़तरे और नियंत्रण पहचानना।

### कौशल

| कौशल | स्रोत | अपेक्षित स्तर | इस स्तर का अर्थ |
| --- | --- | --- | --- |
| [Architect for the whole context](../../कौशल/#architect-for-the-whole-context) | UK GDaD PCF | कार्यरत | You can:<br>• align your work with the work being done by other architects and technical professionals<br>• track emerging issues, strategies, roadmaps, patterns and technologies over time to assess opportunities and risks to your work<br>• identify how other teams contribute to delivering outcomes through change |
| [Architecture communication](../../कौशल/#architecture-communication) | UK GDaD PCF | कार्यरत | You can:<br>• listen to the needs of technical and business stakeholders<br>• create and use different architecture representations to communicate effectively, achieving agreement with technical and non-technical stakeholders<br>• provide support in discussions about architectural topics within a multidisciplinary team |
| [Community collaboration](../../कौशल/#community-collaboration) | UK GDaD PCF | कार्यरत | You can:<br>• contribute to the work of others<br>• motivate and empower teams<br>• create the right environment for teams to work in, and can identify the best team makeup depending on the situation<br>• recognise and deal with issues |
| [Making architectural decisions](../../कौशल/#making-architectural-decisions) | UK GDaD PCF | कार्यरत | You can:<br>• work with others to make architectural design decisions characterised by managed levels of risk and complexity<br>• identify and address architectural risks relevant to your team or domain, for example, business, data, or security<br>• engage with architectural governance and assurance to effectively manage decisions and risks, with support |
| [Strategy design](../../कौशल/#strategy-design) | UK GDaD PCF | कार्यरत | You can:<br>• support the development of a strategy or vision that aligns with organisational objectives<br>• challenge requirements and assumptions, and identify opportunities to develop strategy<br>• support the implementation of a strategy or vision, for example, by using a roadmap or plan<br>• use architectural principles, patterns, and constraints when appropriate |
| [Technical design throughout the life cycle](../../कौशल/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | कार्यरत | You can:<br>• create technical designs characterised by managed levels of risk, impact, and complexity<br>• provide guidance and support to teams using technical designs throughout the life cycle<br>• adapt a technical design if needed during delivery<br>• work with well-understood technology and identify appropriate patterns |
| [स्वास्थ्य और देखभाल सेवाओं की समझ](../../कौशल/#स्वास्थ्य-और-देखभाल-सेवाओं-की-समझ) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• उन क्लिनिकल और देखभाल कार्यप्रवाहों को समझाना जिनमें आपका काम सहायक है<br>• क्लिनिकल और देखभाल सहकर्मियों के साथ सामान्य स्वास्थ्य सेवा शब्दों का सही प्रयोग करना<br>• पहचानना कि कब कोई परिवर्तन रोगी देखभाल को प्रभावित कर सकता है, और उसे उठाना |
| [स्वास्थ्य डेटा अंतर-संचालनीयता](../../कौशल/#स्वास्थ्य-डेटा-अंतर-संचालनीयता) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• FHIR, HL7 संस्करण 2 और संदेश पैटर्न का उपयोग करके इंटीग्रेशन डिज़ाइन करना और बनाना<br>• FHIR संसाधन और कार्यान्वयन गाइड लिखना और उनकी प्रोफ़ाइल बनाना<br>• प्रणालियों के बीच जटिल मैपिंग और डेटा गुणवत्ता समस्याओं को सुलझाना |
| [सूचना शासन और डेटा संरक्षण](../../कौशल/#सूचना-शासन-और-डेटा-संरक्षण) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• अपने काम में डेटा संरक्षण सिद्धांत लागू करना<br>• डेटा संरक्षण प्रभाव आकलनों में योगदान देना<br>• सूचना अनुरोधों और अभिलेखों को सही ढंग से संभालना |
| [क्लिनिकल जोखिम प्रबंधन](../../कौशल/#क्लिनिकल-जोखिम-प्रबंधन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• ख़तरा कार्यशालाओं में भाग लेना और ख़तरा लॉग में योगदान देना<br>• अपने काम के लिए क्लिनिकल जोखिम प्रबंधन प्रक्रिया का पालन करना<br>• क्लिनिकल सुरक्षा केस के लिए परीक्षण परिणाम जैसे साक्ष्य देना |
| [पहचान और पहुँच प्रबंधन](../../कौशल/#पहचान-और-पहुँच-प्रबंधन) | यह संदर्भ | जागरूकता | आप ये कर सकते हैं:<br>• पहुँच नियमों का पालन करना और अपने क्रेडेंशियल सुरक्षित रखना |

### सामान्य योग्यताएँ और अनुभव

- तकनीकी आर्किटेक्चर का विशेषज्ञ ज्ञान, मास्टर स्तर या समकक्ष अनुभव।
- उत्पादन सॉफ़्टवेयर या इन्फ़्रास्ट्रक्चर डिज़ाइन करने या बनाने का अनुभव।

### बैंड की रूपरेखा

- **ज्ञान:** अत्यधिक विकसित विशेषज्ञ ज्ञान, आमतौर पर स्नातकोत्तर (मास्टर) स्तर या समकक्ष अनुभव।
- **स्वायत्तता:** संगठन की नीति के अनुसार काम करता है; परिणाम कैसे प्राप्त हों, यह तय करता है; दूसरे इससे विशेषज्ञ सलाह लेते हैं।
- **दायरा:** कई उत्पाद या सेवाएँ, या एक विशेषज्ञ कार्य।
- **नेतृत्व:** एक टीम या पेशेवर अभ्यास क्षेत्र का नेतृत्व करता है।
- **जवाबदेही:** एक सेवा या विशेषज्ञ कार्य की डिलीवरी, और यदि हो तो उसका बजट।

### कार्य-मूल्यांकन (उदाहरणात्मक)

| # | कारक | स्तर | अंक |
| --- | --- | --- | --- |
| 1 | संचार और संबंध कौशल | 5 | 45 |
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
| | **कुल** | | **496** (बैंड 7: 466–539) |

UK GDaD PCF के बैंड 7 के ग्रेड सुझाव पर, इस भूमिका के लिए स्वास्थ्य क्षेत्र के विज्ञापनों के अनुरूप। ज्ञान का अंक मास्टर स्तर या समकक्ष पर है, तकनीकी आर्किटेक्चर की पूरी श्रृंखला के विशेषज्ञ ज्ञान के लिए।

## बैंड 8a: वरिष्ठ तकनीकी आर्किटेक्ट

**UK GDaD PCF स्तर: Senior technical architect**

> A senior technical architect works on large or multiple pieces of work that are complex or risky.
> 
> At this role level, you will:
> - define strategy and be central to assuring services
> - regularly collaborate and find agreement with senior stakeholders, providing direction and challenge
> - be proactive in identifying problems and translating these into non-technical descriptions that can be widely understood
> - mentor and coach junior colleagues

### ज़िम्मेदारियाँ

- क्लिनिकल प्रणालियों और साझा इंटीग्रेशन प्लेटफ़ॉर्म जैसी बड़ी, जटिल या उच्च-जोखिम सेवाओं के तकनीकी डिज़ाइन का नेतृत्व करना।
- एक या अधिक डिलीवरी टीमों के लिए तकनीकी दिशा तय करना और जोखिम बढ़ाने वाले डिज़ाइनों को चुनौती देना।
- लचीलेपन, आपदा पुनर्प्राप्ति और सुरक्षित संचालन के लिए डिज़ाइन करना, और जाँचना कि टीमें उसका परीक्षण करें।
- सेवा स्वामियों, क्लिनिकल प्रमुखों और वरिष्ठ हितधारकों को तकनीकी जोखिम और समझौते सरल भाषा में समझाना।
- तकनीकी आर्किटेक्टों और वरिष्ठ डेवलपरों का मार्गदर्शन और कोचिंग करना।

### कौशल

| कौशल | स्रोत | अपेक्षित स्तर | इस स्तर का अर्थ |
| --- | --- | --- | --- |
| [Architect for the whole context](../../कौशल/#architect-for-the-whole-context) | UK GDaD PCF | कार्यरत | You can:<br>• align your work with the work being done by other architects and technical professionals<br>• track emerging issues, strategies, roadmaps, patterns and technologies over time to assess opportunities and risks to your work<br>• identify how other teams contribute to delivering outcomes through change |
| [Architecture communication](../../कौशल/#architecture-communication) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• lead the communication of complicated, complex or risky architecture topics with technical and non-technical stakeholders<br>• communicate with senior stakeholders across your organisation<br>• adapt your message and communication techniques to your audience<br>• advocate on behalf of a team to other stakeholders<br>• manage stakeholder expectations effectively |
| [Community collaboration](../../कौशल/#community-collaboration) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../कौशल/#making-architectural-decisions) | UK GDaD PCF | कार्यरत | You can:<br>• work with others to make architectural design decisions characterised by managed levels of risk and complexity<br>• identify and address architectural risks relevant to your team or domain, for example, business, data, or security<br>• engage with architectural governance and assurance to effectively manage decisions and risks, with support |
| [Strategy design](../../कौशल/#strategy-design) | UK GDaD PCF | कार्यरत | You can:<br>• support the development of a strategy or vision that aligns with organisational objectives<br>• challenge requirements and assumptions, and identify opportunities to develop strategy<br>• support the implementation of a strategy or vision, for example, by using a roadmap or plan<br>• use architectural principles, patterns, and constraints when appropriate |
| [Technical design throughout the life cycle](../../कौशल/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• create technical designs characterised by medium risk, impact, and complexity<br>• maintain appropriate quality and architectural coherence of a technical design in response to change<br>• use feedback to optimise and refine technical designs throughout the life cycle |
| [स्वास्थ्य और देखभाल सेवाओं की समझ](../../कौशल/#स्वास्थ्य-और-देखभाल-सेवाओं-की-समझ) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• विश्लेषण करना कि कोई सेवा विभिन्न संगठनों के देखभाल मार्गों में कैसे बैठती है<br>• डिजिटल सेवाओं को आकार देने के लिए चिकित्सकों, देखभाल कर्मचारियों और रोगियों के साथ काम करना<br>• देखभाल, सुरक्षा और कर्मचारियों के कार्यभार पर डिजिटल निर्णयों का प्रभाव समझाना |
| [स्वास्थ्य डेटा अंतर-संचालनीयता](../../कौशल/#स्वास्थ्य-डेटा-अंतर-संचालनीयता) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• FHIR, HL7 संस्करण 2 और संदेश पैटर्न का उपयोग करके इंटीग्रेशन डिज़ाइन करना और बनाना<br>• FHIR संसाधन और कार्यान्वयन गाइड लिखना और उनकी प्रोफ़ाइल बनाना<br>• प्रणालियों के बीच जटिल मैपिंग और डेटा गुणवत्ता समस्याओं को सुलझाना |
| [सूचना शासन और डेटा संरक्षण](../../कौशल/#सूचना-शासन-और-डेटा-संरक्षण) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• अपने काम में डेटा संरक्षण सिद्धांत लागू करना<br>• डेटा संरक्षण प्रभाव आकलनों में योगदान देना<br>• सूचना अनुरोधों और अभिलेखों को सही ढंग से संभालना |
| [क्लिनिकल जोखिम प्रबंधन](../../कौशल/#क्लिनिकल-जोखिम-प्रबंधन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• ख़तरा कार्यशालाओं में भाग लेना और ख़तरा लॉग में योगदान देना<br>• अपने काम के लिए क्लिनिकल जोखिम प्रबंधन प्रक्रिया का पालन करना<br>• क्लिनिकल सुरक्षा केस के लिए परीक्षण परिणाम जैसे साक्ष्य देना |
| [पहचान और पहुँच प्रबंधन](../../कौशल/#पहचान-और-पहुँच-प्रबंधन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• उपयोगकर्ता खाते और पहुँच अधिकार बनाना, बदलना और हटाना<br>• भूमिका-आधारित पहुँच नियमों के आधार पर पहुँच की जाँच करना |
| [चिकित्सा उपकरण सॉफ़्टवेयर विनियमन](../../कौशल/#चिकित्सा-उपकरण-सॉफ़्टवेयर-विनियमन) | यह संदर्भ | जागरूकता | आप ये कर सकते हैं:<br>• समझाना कि कुछ स्वास्थ्य सॉफ़्टवेयर चिकित्सा उपकरण के रूप में विनियमित होते हैं<br>• जानना कि जब कोई उत्पाद चिकित्सा उपकरण हो सकता है तो किससे पूछना है |

### सामान्य योग्यताएँ और अनुभव

- जटिल सेवाओं के तकनीकी डिज़ाइन का पर्याप्त अनुभव, मास्टर डिग्री के समकक्ष स्तर पर।

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

UK GDaD PCF ग्रेड सुझाव (बैंड 7) से ऊँचे बैंड पर: स्वास्थ्य क्षेत्र के विज्ञापन इस भूमिका को बैंड 8a पर रखते हैं। योजना, नीति और कार्य करने की स्वतंत्रता का अंक बैंड 7 प्रोफ़ाइल से ऊपर है क्योंकि यह पद कम पर्यवेक्षण में कई टीमों के लिए तकनीकी दिशा तय करता है।

## बैंड 8b: लीड तकनीकी आर्किटेक्ट

**UK GDaD PCF स्तर: Lead technical architect**

> A lead technical architect works with multiple projects or teams on problems that require broad architectural thinking.
> 
> At this role level, you will:
> - be responsible for leading the technical design of systems and services, justifying and communicating design decisions
> - assure other services and system quality, ensuring the technical work fits into the broader strategy for government
> - explore the benefits of cross-government alignment
> - provide mentoring within teams
> - provide leadership to other architects

### ज़िम्मेदारियाँ

- कई सेवाओं या टीमों में तकनीकी आर्किटेक्चर का नेतृत्व करना, साझा पैटर्न और मानक तय करते हुए।
- सुरक्षा, लचीलेपन और अंतर-संचालनीयता सहित डिज़ाइन प्राधिकरणों में डिज़ाइनों की तकनीकी गुणवत्ता का आश्वासन देना।
- एंटरप्राइज़ आर्किटेक्टों और इंजीनियरिंग प्रमुखों के साथ संगठन के तकनीकी रोडमैप को आकार देना।
- तकनीकी विकल्पों, प्लेटफ़ॉर्म निवेश और तकनीकी जोखिम पर वरिष्ठ प्रमुखों को सलाह देना।
- तकनीकी आर्किटेक्टों का नेतृत्व और विकास करना।

### कौशल

| कौशल | स्रोत | अपेक्षित स्तर | इस स्तर का अर्थ |
| --- | --- | --- | --- |
| [Architect for the whole context](../../कौशल/#architect-for-the-whole-context) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• work to support wider organisational objectives beyond your immediate goals​<br>• track emerging internal and external issues over time that could affect the work of teams across the organisation<br>• take action to solve or mitigate problems by influencing colleagues across the organisation |
| [Architecture communication](../../कौशल/#architecture-communication) | UK GDaD PCF | विशेषज्ञ | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Community collaboration](../../कौशल/#community-collaboration) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../कौशल/#making-architectural-decisions) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• make and guide architectural design decisions characterised by medium risk and complexity<br>• identify and address architectural risks that affect multiple teams or domains<br>• use architectural governance and assurance to make design decisions and manage technical risks at the appropriate level<br>• contribute to the development of architectural governance and assurance |
| [Strategy design](../../कौशल/#strategy-design) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• define strategies or visions across teams that align with organisational objectives<br>• direct the implementation of a strategy or vision, for example, by creating roadmaps or plans<br>• define architectural principles and patterns<br>• develop or maintain strategy in response to feedback and findings |
| [Technical design throughout the life cycle](../../कौशल/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | विशेषज्ञ | You can:<br>• create technical designs characterised by high risk, impact, and complexity<br>• lead and guide others in creating technical designs that achieve organisational objectives<br>• use feedback to optimise and refine standards for technical designs throughout the life cycle |
| [स्वास्थ्य और देखभाल सेवाओं की समझ](../../कौशल/#स्वास्थ्य-और-देखभाल-सेवाओं-की-समझ) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• विश्लेषण करना कि कोई सेवा विभिन्न संगठनों के देखभाल मार्गों में कैसे बैठती है<br>• डिजिटल सेवाओं को आकार देने के लिए चिकित्सकों, देखभाल कर्मचारियों और रोगियों के साथ काम करना<br>• देखभाल, सुरक्षा और कर्मचारियों के कार्यभार पर डिजिटल निर्णयों का प्रभाव समझाना |
| [स्वास्थ्य डेटा अंतर-संचालनीयता](../../कौशल/#स्वास्थ्य-डेटा-अंतर-संचालनीयता) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• FHIR, HL7 संस्करण 2 और संदेश पैटर्न का उपयोग करके इंटीग्रेशन डिज़ाइन करना और बनाना<br>• FHIR संसाधन और कार्यान्वयन गाइड लिखना और उनकी प्रोफ़ाइल बनाना<br>• प्रणालियों के बीच जटिल मैपिंग और डेटा गुणवत्ता समस्याओं को सुलझाना |
| [सूचना शासन और डेटा संरक्षण](../../कौशल/#सूचना-शासन-और-डेटा-संरक्षण) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• डेटा संरक्षण प्रभाव आकलनों और सूचना साझाकरण समझौतों का नेतृत्व करना<br>• विधिक आधार, सहमति, गोपनीयता और प्रतिधारण पर टीमों को सलाह देना<br>• घटनाओं की जाँच करना और सुधारों की सिफ़ारिश करना |
| [क्लिनिकल जोखिम प्रबंधन](../../कौशल/#क्लिनिकल-जोखिम-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• किसी उत्पाद या परिवर्तन के लिए ख़तरा पहचान और जोखिम आकलन का नेतृत्व करना<br>• ख़तरा लॉग और क्लिनिकल सुरक्षा केस रिपोर्ट लिखना और बनाए रखना<br>• उत्पाद टीमों के साथ जोखिम नियंत्रणों पर सहमति बनाना और जाँचना कि वे काम करते हैं<br>• क्लिनिकल जोखिम प्रबंधन मानकों को लागू करने पर टीमों को सलाह देना |
| [पहचान और पहुँच प्रबंधन](../../कौशल/#पहचान-और-पहुँच-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• पहचान और पहुँच सेवाएँ डिज़ाइन करना और चलाना<br>• नियमित रूप से पहुँच की समीक्षा करना और समस्याएँ ठीक करना |
| [चिकित्सा उपकरण सॉफ़्टवेयर विनियमन](../../कौशल/#चिकित्सा-उपकरण-सॉफ़्टवेयर-विनियमन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• चिकित्सा उपकरण मानकों को पूरा करने वाली सॉफ़्टवेयर जीवनचक्र प्रक्रिया का पालन करना<br>• ऐसी प्रक्रिया के लिए आवश्यक अभिलेख तैयार करना |
| [लोगों का प्रबंधन](../../कौशल/#लोगों-का-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• किसी टीम का लाइन प्रबंधन करना, उद्देश्य तय करना और मूल्यांकन करना<br>• कल्याण का समर्थन करना और उपस्थिति, प्रदर्शन तथा आचरण का प्रबंधन करना<br>• टीम के विकास और उत्तराधिकार की योजना बनाना |

### सामान्य योग्यताएँ और अनुभव

- जटिल सेवाओं के तकनीकी आर्किटेक्चर का नेतृत्व करने का व्यापक अनुभव।

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

## बैंड 8c: प्रधान तकनीकी आर्किटेक्ट

**UK GDaD PCF स्तर: Principal technical architect**

> A principal technical architect leads at the highest level and is responsible for making sure the strategy is agreed and followed.
> 
> At this role level, you will:
> - network and communicate with senior stakeholders across organisations
> - proactively seek opportunities for digital transformation
> - support multiple teams, finding and using best practice and emerging technologies
> - inspire other architects and help them understand how to deliver the goals of the organisation
> - be responsible for governance, solving complex and high risk issues or delivering architecture design

### ज़िम्मेदारियाँ

- संगठन की तकनीकी आर्किटेक्चर रणनीति, सिद्धांत और मानक तय करना।
- तकनीकी डिज़ाइन प्राधिकरण सहित पूरे संगठन में तकनीकी डिज़ाइन का शासन करना।
- होस्टिंग रणनीति और प्लेटफ़ॉर्म समेकन जैसे प्रमुख तकनीकी निर्णयों पर कार्यकारी टीम को सलाह देना।
- अंतर-संगठनात्मक तकनीकी और मानक समुदायों में संगठन का प्रतिनिधित्व करना।
- पूरे संगठन के आर्किटेक्टों को प्रेरित करना और उनका विकास करना।

### कौशल

| कौशल | स्रोत | अपेक्षित स्तर | इस स्तर का अर्थ |
| --- | --- | --- | --- |
| [Architect for the whole context](../../कौशल/#architect-for-the-whole-context) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• work to support wider organisational objectives beyond your immediate goals​<br>• track emerging internal and external issues over time that could affect the work of teams across the organisation<br>• take action to solve or mitigate problems by influencing colleagues across the organisation |
| [Architecture communication](../../कौशल/#architecture-communication) | UK GDaD PCF | विशेषज्ञ | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Community collaboration](../../कौशल/#community-collaboration) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../कौशल/#making-architectural-decisions) | UK GDaD PCF | विशेषज्ञ | You can:<br>• make and guide architectural design decisions characterised by high levels of risk and complexity<br>• identify and address architectural risks across the organisation or wider government<br>• lead and evolve architectural governance and assurance<br>• represent architectural governance as part of wider governance, for example, legal or commercial |
| [Strategy design](../../कौशल/#strategy-design) | UK GDaD PCF | विशेषज्ञ | You can:<br>• define and connect strategies or visions across the organisation or wider government<br>• enable the implementation of strategies or visions across the organisation or wider government, for example, by advocating for resources and removing blockers |
| [Technical design throughout the life cycle](../../कौशल/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | विशेषज्ञ | You can:<br>• create technical designs characterised by high risk, impact, and complexity<br>• lead and guide others in creating technical designs that achieve organisational objectives<br>• use feedback to optimise and refine standards for technical designs throughout the life cycle |
| [स्वास्थ्य और देखभाल सेवाओं की समझ](../../कौशल/#स्वास्थ्य-और-देखभाल-सेवाओं-की-समझ) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• विश्लेषण करना कि कोई सेवा विभिन्न संगठनों के देखभाल मार्गों में कैसे बैठती है<br>• डिजिटल सेवाओं को आकार देने के लिए चिकित्सकों, देखभाल कर्मचारियों और रोगियों के साथ काम करना<br>• देखभाल, सुरक्षा और कर्मचारियों के कार्यभार पर डिजिटल निर्णयों का प्रभाव समझाना |
| [स्वास्थ्य डेटा अंतर-संचालनीयता](../../कौशल/#स्वास्थ्य-डेटा-अंतर-संचालनीयता) | यह संदर्भ | विशेषज्ञ | आप ये कर सकते हैं:<br>• संगठन के लिए अंतर-संचालनीयता मानक और रणनीति तय करना<br>• राष्ट्रीय या अंतर-संगठनात्मक मानक कार्य का नेतृत्व करना<br>• कई प्रणालियों में महत्वपूर्ण इंटीग्रेशन के डिज़ाइन का आश्वासन देना |
| [सूचना शासन और डेटा संरक्षण](../../कौशल/#सूचना-शासन-और-डेटा-संरक्षण) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• डेटा संरक्षण प्रभाव आकलनों और सूचना साझाकरण समझौतों का नेतृत्व करना<br>• विधिक आधार, सहमति, गोपनीयता और प्रतिधारण पर टीमों को सलाह देना<br>• घटनाओं की जाँच करना और सुधारों की सिफ़ारिश करना |
| [क्लिनिकल जोखिम प्रबंधन](../../कौशल/#क्लिनिकल-जोखिम-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• किसी उत्पाद या परिवर्तन के लिए ख़तरा पहचान और जोखिम आकलन का नेतृत्व करना<br>• ख़तरा लॉग और क्लिनिकल सुरक्षा केस रिपोर्ट लिखना और बनाए रखना<br>• उत्पाद टीमों के साथ जोखिम नियंत्रणों पर सहमति बनाना और जाँचना कि वे काम करते हैं<br>• क्लिनिकल जोखिम प्रबंधन मानकों को लागू करने पर टीमों को सलाह देना |
| [पहचान और पहुँच प्रबंधन](../../कौशल/#पहचान-और-पहुँच-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• पहचान और पहुँच सेवाएँ डिज़ाइन करना और चलाना<br>• नियमित रूप से पहुँच की समीक्षा करना और समस्याएँ ठीक करना |
| [संगठनात्मक जोखिम प्रबंधन](../../कौशल/#संगठनात्मक-जोखिम-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• किसी निदेशालय या कार्यक्रम के लिए जोखिम प्रक्रिया चलाना<br>• जोखिम सहनशीलता के आधार पर जोखिमों का आकलन करना और उन्हें आगे बढ़ाना<br>• समितियों को जोखिमों की रिपोर्ट देना |
| [लोगों का प्रबंधन](../../कौशल/#लोगों-का-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• किसी टीम का लाइन प्रबंधन करना, उद्देश्य तय करना और मूल्यांकन करना<br>• कल्याण का समर्थन करना और उपस्थिति, प्रदर्शन तथा आचरण का प्रबंधन करना<br>• टीम के विकास और उत्तराधिकार की योजना बनाना |

### सामान्य योग्यताएँ और अनुभव

- कई टीमों या संगठनों में तकनीकी आर्किटेक्चर का नेतृत्व करने का व्यापक अनुभव।

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
