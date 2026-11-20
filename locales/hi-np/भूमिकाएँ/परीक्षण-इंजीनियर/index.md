# परीक्षण इंजीनियर

> यह एक सामान्य डिजिटल स्वास्थ्य सेवा संगठन के लिए एक उदाहरणात्मक संदर्भ प्रोफ़ाइल है। यह किसी भी नियोक्ता का आधिकारिक कार्य-विवरण नहीं है, और इसके कार्य-मूल्यांकन अंक औपचारिक मूल्यांकन नहीं हैं।

> इस पाठ का अंग्रेज़ी से अनुवाद एक कृत्रिम बुद्धिमत्ता सहायक ने किया है, और किसी मूल हिन्दी भाषी ने अभी तक इसकी समीक्षा नहीं की है। यूके सरकार के डिजिटल और डेटा पेशा क्षमता ढाँचे (UK GDaD PCF) और ESCO के उद्धरण अंग्रेज़ी में ही रखे गए हैं।

**परिवार:** [गुणवत्ता आश्वासन परीक्षण](../../#गुणवत्ता-आश्वासन-परीक्षण)  
**बैंड:** 4, 6, 7, 8a  
**UK GDaD PCF भूमिका:** [Test engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/test-engineer/)  
**ESCO व्यवसाय:** [software tester](http://data.europa.eu/esco/occupation/106f79e4-6264-45f1-9e7a-297435cd684b) (ISCO-08 2519)

## सारांश

परीक्षण इंजीनियर वे स्वचालित परीक्षण, उपकरण और ढाँचे बनाते हैं जिनसे टीमें संगठन की डिजिटल स्वास्थ्य सेवाओं का जल्दी और बार-बार परीक्षण कर सकें। वे कार्यों, इंटीग्रेशन, प्रदर्शन, सुरक्षा और लचीलेपन के परीक्षण के लिए कोड लिखते हैं, और परीक्षण को डिलीवरी पाइपलाइन में शामिल करते हैं, ताकि क्लिनिकल और रोगी-उन्मुख प्रणालियों में परिवर्तन सुरक्षित रूप से रिलीज़ हो सकें।

## एक डिजिटल स्वास्थ्य सेवा संगठन में

- क्लिनिकल प्रणालियाँ सुरक्षा-महत्वपूर्ण हैं, इसलिए स्वचालित रिग्रेशन परीक्षण ख़तरा लॉग में दर्ज सुरक्षा नियंत्रणों की रक्षा करते हैं और सुरक्षा केस के साक्ष्य के रूप में रखे जाते हैं।
- अन्य स्वास्थ्य और देखभाल प्रणालियों के साथ इंटीग्रेशन को HL7 FHIR और HL7 संस्करण 2 जैसे मानकों के आधार पर स्वचालित परीक्षण चाहिए, अक्सर सिम्युलेटेड साझेदार प्रणालियों का उपयोग करके।
- क्लिनिकल सेवाएँ चौबीसों घंटे चलती हैं और पूर्वानुमेय समय पर चरम पर होती हैं, इसलिए प्रदर्शन और लचीलापन परीक्षण वास्तविक क्लिनिकल माँग का मॉडल बनाता है।
- परीक्षण परिवेशों में वास्तविक रोगी डेटा नहीं होना चाहिए, इसलिए इंजीनियर दुर्लभ और सीमांत क्लिनिकल मामलों सहित यथार्थवादी सिंथेटिक डेटा बनाते हैं।
- चिकित्सा उपकरण के रूप में विनियमित सॉफ़्टवेयर को IEC 62304 जैसे मानकों के तहत अपने जीवनचक्र के हिस्से के रूप में अनुरेखणीय, दोहराने योग्य परीक्षण चाहिए।

## UK GDaD PCF भूमिका विवरण (अंग्रेज़ी मूल)

> A test engineer designs, builds, automates and executes comprehensive, robust and maintainable test suites. They apply test engineering standards, perform exploratory testing and use diverse techniques to identify risks and improve testing efficiency and quality.
> 
> In this role you will:
> - maintain automated tests in continuous integration, continuous delivery (CI/CD) pipelines
> - use, develop and standardise reusable frameworks and tools following engineering practices and standards
> - analyse and test artefacts such as products, services and business processes
> - promote quality considerations throughout the development life cycle
> - support the resolution of technical issues

## भूमिका स्तर

| बैंड | शीर्षक | UK GDaD PCF स्तर | यूके सिविल सेवा ग्रेड | कार्य-मूल्यांकन अंक |
| --- | --- | --- | --- | --- |
| 4 | [एसोसिएट परीक्षण इंजीनियर](#बैंड-4-एसोसिएट-परीक्षण-इंजीनियर) | Associate test engineer | EO | 275 |
| 6 | [परीक्षण इंजीनियर](#बैंड-6-परीक्षण-इंजीनियर) | Test engineer | HEO/SEO | 411 |
| 7 | [वरिष्ठ परीक्षण इंजीनियर](#बैंड-7-वरिष्ठ-परीक्षण-इंजीनियर) | Senior test engineer | SEO/G7 | 477 |
| 8a | [लीड परीक्षण इंजीनियर](#बैंड-8a-लीड-परीक्षण-इंजीनियर) | Lead test engineer | SEO/G7/G6 | 553 |

## बैंड 4: एसोसिएट परीक्षण इंजीनियर

**UK GDaD PCF स्तर: Associate test engineer**

> An associate test engineer works closely with other test professionals to learn test engineering activities and techniques.
> 
> At this role level, you will:
> - contribute to and maintain technical test suites under supervision
> - follow engineering practices and standards to apply test approaches, plans and strategies under supervision
> - analyse artefacts such as user stories, prototypes, processes and designs with support
> - support the development of reports, recording of outcomes and resolution of defects
> - understand the technical tooling and engineering approach to design and execute tests

### ज़िम्मेदारियाँ

- टीम के इंजीनियरिंग मानकों का पालन करते हुए पर्यवेक्षण में सरल स्वचालित परीक्षण लिखना और बनाए रखना।
- स्वचालित और मैन्युअल परीक्षण चलाना और परिणाम सटीकता से दर्ज करना।
- क्लिनिकल प्रणालियों के साथ इंटीग्रेशन सहित दोषों की जाँच और रिपोर्ट में मदद करना।
- सिंथेटिक परीक्षण डेटा का उपयोग करना और परीक्षण परिवेशों में सूचना शासन नियमों का पालन करना।
- टीम के परीक्षण उपकरण, कोड पद्धतियाँ और क्लिनिकल सुरक्षा प्रक्रिया सीखना।

### कौशल

| कौशल | स्रोत | अपेक्षित स्तर | इस स्तर का अर्थ |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../कौशल/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | जागरूकता | You can:<br>• explain why it's important to communicate technical concepts in non-technical language<br>• explain the types of communication that can be used with internal and external stakeholders, and their impact |
| [Designing and executing tests](../../कौशल/#designing-and-executing-tests) | UK GDaD PCF | जागरूकता | You can:<br>• contribute to deciding the most appropriate test types and techniques to use<br>• follow guidance to design, build and maintain simple tests that align to user needs and requirements<br>• execute simple tests with support<br>• explain the value of automation within testing |
| [Managing, reporting and resolving defects](../../कौशल/#managing-reporting-and-resolving-defects) | UK GDaD PCF | जागरूकता | You can:<br>• explain how to report and track defects<br>• follow a defect management process to report, communicate and maintain defects with appropriate information<br>• retest and escalate defects when needed |
| [Test analysis](../../कौशल/#test-analysis) | UK GDaD PCF | जागरूकता | You can:<br>• describe quality characteristics and explain why they are important<br>• analyse information, such as user stories, prototypes, processes and designs, with support<br>• explain what might be a risk in achieving quality goals |
| [Test and quality planning](../../कौशल/#test-and-quality-planning) | UK GDaD PCF | जागरूकता | You can:<br>• explain the value of quality testing approaches, plans and strategies<br>• explain how different delivery methodologies affect quality testing approaches, plans and strategies<br>• follow quality testing approaches, plans and strategies, with support<br>• explain how to measure the effectiveness of quality testing approaches, plans and strategies, and why it’s important |
| [Test engineering](../../कौशल/#test-engineering) | UK GDaD PCF | जागरूकता | You can:<br>• explain why testing processes, environments and tools are important<br>• follow test engineering practices and standards, with support<br>• support the maintenance of automated tests and tools required for testing |
| [स्वास्थ्य और देखभाल सेवाओं की समझ](../../कौशल/#स्वास्थ्य-और-देखभाल-सेवाओं-की-समझ) | यह संदर्भ | जागरूकता | आप ये कर सकते हैं:<br>• स्वास्थ्य और देखभाल प्रणाली के मुख्य भागों और संगठन द्वारा समर्थित सेवाओं का वर्णन करना<br>• समझाना कि आपके काम में रोगी सुरक्षा और गोपनीयता क्यों महत्वपूर्ण हैं |
| [क्लिनिकल जोखिम प्रबंधन](../../कौशल/#क्लिनिकल-जोखिम-प्रबंधन) | यह संदर्भ | जागरूकता | आप ये कर सकते हैं:<br>• समझाना कि स्वास्थ्य आईटी प्रणालियाँ रोगियों को कैसे नुकसान पहुँचा सकती हैं, उदाहरण के लिए ग़लत, गायब या विलंबित जानकारी से<br>• संभावित क्लिनिकल सुरक्षा मुद्दे की रिपोर्ट सही माध्यम से करना |
| [सूचना शासन और डेटा संरक्षण](../../कौशल/#सूचना-शासन-और-डेटा-संरक्षण) | यह संदर्भ | जागरूकता | आप ये कर सकते हैं:<br>• व्यक्तिगत और स्वास्थ्य जानकारी संभालने के संगठन के नियमों का पालन करना<br>• डेटा उल्लंघन या बाल-बाल बची घटना को पहचानना और रिपोर्ट करना |

### सामान्य योग्यताएँ और अनुभव

- कोडिंग या परीक्षण का कुछ अनुभव, या किसी संबंधित अप्रेंटिसशिप में नामांकन, या समकक्ष।

### बैंड की रूपरेखा

- **ज्ञान:** कार्य क्षेत्र का विस्तृत ज्ञान, आमतौर पर फ़ाउंडेशन डिग्री, अप्रेंटिसशिप या समकक्ष अनुभव से।
- **स्वायत्तता:** दिशानिर्देशों के भीतर काम करता है; अधिकांश दैनिक समस्याएँ सुलझाता है; सलाह के लिए प्रबंधक उपलब्ध रहता है।
- **दायरा:** अपना काम और एक परिभाषित सेवा या प्रक्रिया।
- **नेतृत्व:** एक छोटी टीम का पर्यवेक्षण या दूसरों के काम का समन्वय कर सकता है।
- **जवाबदेही:** एक परिभाषित सेवा या प्रक्रिया की डिलीवरी।

### कार्य-मूल्यांकन (उदाहरणात्मक)

| # | कारक | स्तर | अंक |
| --- | --- | --- | --- |
| 1 | संचार और संबंध कौशल | 3 | 21 |
| 2 | ज्ञान, प्रशिक्षण और अनुभव | 4 | 88 |
| 3 | विश्लेषण और निर्णय कौशल | 3 | 27 |
| 4 | योजना और संगठन कौशल | 2 | 15 |
| 5 | शारीरिक कौशल | 3 | 27 |
| 6 | रोगी और सेवार्थी देखभाल की ज़िम्मेदारी | 1 | 4 |
| 7 | नीति और सेवा विकास की ज़िम्मेदारी | 2 | 12 |
| 8 | वित्तीय और भौतिक संसाधनों की ज़िम्मेदारी | 1 | 5 |
| 9 | लोगों की ज़िम्मेदारी | 1 | 5 |
| 10 | सूचना संसाधनों की ज़िम्मेदारी | 3 | 16 |
| 11 | अनुसंधान और विकास की ज़िम्मेदारी | 2 | 12 |
| 12 | कार्य करने की स्वतंत्रता | 2 | 12 |
| 13 | शारीरिक प्रयास | 2 | 7 |
| 14 | मानसिक प्रयास | 3 | 12 |
| 15 | भावनात्मक प्रयास | 1 | 5 |
| 16 | कार्य परिस्थितियाँ | 2 | 7 |
| | **कुल** | | **275** (बैंड 4: 271–325) |

## बैंड 6: परीक्षण इंजीनियर

**UK GDaD PCF स्तर: Test engineer**

> A test engineer develops solutions to enable more efficient testing. They follow engineering standards to design and execute appropriate technical tests.
> 
> At this role level, you will:
> - determine test scope and estimate the effort required
> - select and use the most appropriate test approaches and techniques to mitigate risk
> - use technical tooling and engineering approaches to design and execute tests
> - develop and maintain technical test suites
> - develop reports, record outcomes and support the resolution of defects
> - contribute to and follow engineering practices and standards

### ज़िम्मेदारियाँ

- क्लिनिकल और रोगी-उन्मुख सेवाओं के लिए स्वचालित कार्यात्मक, इंटीग्रेशन और API परीक्षण डिज़ाइन करना और बनाना।
- HL7 FHIR प्रोफ़ाइल और अन्य अंतर-संचालनीयता विनिर्देशों के आधार पर संदेशों की जाँच करने वाले परीक्षण बनाना।
- यथार्थवादी और सीमांत क्लिनिकल मामलों को कवर करने वाला सिंथेटिक रोगी डेटा बनाना।
- डिलीवरी पाइपलाइन में परीक्षण जोड़ना ताकि सुरक्षा-संबंधी जाँचें हर परिवर्तन पर चलें।
- परीक्षण प्रयास का अनुमान लगाना, परिणामों की रिपोर्ट देना, और दोषों के समाधान में सहायता करना।

### कौशल

| कौशल | स्रोत | अपेक्षित स्तर | इस स्तर का अर्थ |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../कौशल/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | कार्यरत | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Designing and executing tests](../../कौशल/#designing-and-executing-tests) | UK GDaD PCF | कार्यरत | You can:<br>• set up suitable environments with some support<br>• select appropriate test types and techniques with some support<br>• design, build, maintain and execute tests that align to user needs and requirements<br>• conduct exploratory testing<br>• research and try new test types and techniques |
| [Managing, reporting and resolving defects](../../कौशल/#managing-reporting-and-resolving-defects) | UK GDaD PCF | कार्यरत | You can:<br>• collaborate with others to create a defect management process to report, communicate and resolve defects, with support<br>• critically assess dependencies, defects and risks, with support<br>• contribute to mitigation and contingency plans<br>• clearly communicate risks and the impact of defects to stakeholders |
| [Test analysis](../../कौशल/#test-analysis) | UK GDaD PCF | कार्यरत | You can:<br>• work with stakeholders to determine which functional and non-functional quality characteristics add value<br>• determine what to test following an agreed approach<br>• identify and advocate for test needs, such as data, access and environments, with support<br>• analyse information to identify risks |
| [Test and quality planning](../../कौशल/#test-and-quality-planning) | UK GDaD PCF | कार्यरत | You can:<br>• create or adapt quality testing approaches based on risk, with some support<br>• follow a quality testing strategy and contribute to its development<br>• contribute to continuous improvement of quality testing approaches, plans and strategies |
| [Test engineering](../../कौशल/#test-engineering) | UK GDaD PCF | कार्यरत | You can:<br>• use test engineering frameworks and tools to support testing activities<br>• follow test engineering practices and standards, such as source control and continuous integration, continuous delivery (CI/CD) pipelines<br>• integrate and execute tests to ensure early testing and continuous feedback<br>• create and maintain automated tests, with some support<br>• write and review coded solutions, with some support |
| [स्वास्थ्य और देखभाल सेवाओं की समझ](../../कौशल/#स्वास्थ्य-और-देखभाल-सेवाओं-की-समझ) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• उन क्लिनिकल और देखभाल कार्यप्रवाहों को समझाना जिनमें आपका काम सहायक है<br>• क्लिनिकल और देखभाल सहकर्मियों के साथ सामान्य स्वास्थ्य सेवा शब्दों का सही प्रयोग करना<br>• पहचानना कि कब कोई परिवर्तन रोगी देखभाल को प्रभावित कर सकता है, और उसे उठाना |
| [क्लिनिकल जोखिम प्रबंधन](../../कौशल/#क्लिनिकल-जोखिम-प्रबंधन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• ख़तरा कार्यशालाओं में भाग लेना और ख़तरा लॉग में योगदान देना<br>• अपने काम के लिए क्लिनिकल जोखिम प्रबंधन प्रक्रिया का पालन करना<br>• क्लिनिकल सुरक्षा केस के लिए परीक्षण परिणाम जैसे साक्ष्य देना |
| [सूचना शासन और डेटा संरक्षण](../../कौशल/#सूचना-शासन-और-डेटा-संरक्षण) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• अपने काम में डेटा संरक्षण सिद्धांत लागू करना<br>• डेटा संरक्षण प्रभाव आकलनों में योगदान देना<br>• सूचना अनुरोधों और अभिलेखों को सही ढंग से संभालना |
| [स्वास्थ्य डेटा अंतर-संचालनीयता](../../कौशल/#स्वास्थ्य-डेटा-अंतर-संचालनीयता) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• FHIR संसाधन, प्रोफ़ाइल और API पढ़ना और उनका उपयोग करना<br>• मार्गदर्शन में सरल इंटीग्रेशन बनाना या उनका परीक्षण करना<br>• किसी विनिर्देश के आधार पर संदेशों की जाँच करना |

### सामान्य योग्यताएँ और अनुभव

- कंप्यूटिंग या संबंधित विषय में डिग्री, या समकक्ष अनुभव।
- स्वचालित परीक्षण बनाने का अनुभव।

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
| 10 | सूचना संसाधनों की ज़िम्मेदारी | 4 | 24 |
| 11 | अनुसंधान और विकास की ज़िम्मेदारी | 2 | 12 |
| 12 | कार्य करने की स्वतंत्रता | 4 | 32 |
| 13 | शारीरिक प्रयास | 1 | 3 |
| 14 | मानसिक प्रयास | 4 | 18 |
| 15 | भावनात्मक प्रयास | 1 | 5 |
| 16 | कार्य परिस्थितियाँ | 2 | 7 |
| | **कुल** | | **411** (बैंड 6: 396–465) |

## बैंड 7: वरिष्ठ परीक्षण इंजीनियर

**UK GDaD PCF स्तर: Senior test engineer**

> A senior test engineer is responsible for test engineering in their area. They influence, coach and guide others in test engineering, sharing best practice and standards.
> 
> At this role level, you will:
> - select, use and guide others in using the most appropriate technical tooling, engineering approaches, test types and techniques to identify and address risks early
> - extend, standardise and build reusable frameworks and tools that support testing
> - communicate and document chosen approaches, tools, techniques and outcomes to the team and appropriate stakeholders
> - contribute to and agree engineering standards

### ज़िम्मेदारियाँ

- किसी क्षेत्र की परीक्षण इंजीनियरिंग का नेतृत्व करना, ऐसे उपकरण, ढाँचे और परीक्षण प्रकार चुनते हुए जो उसके जोखिमों को जल्दी संबोधित करें।
- क्लिनिकल प्रणालियों और साझेदार इंटीग्रेशन के लिए पुनः उपयोग-योग्य परीक्षण ढाँचे और सिम्युलेटर बनाना।
- वास्तविक क्लिनिकल माँग के आधार पर प्रदर्शन, लोड और लचीलापन परीक्षणों की योजना बनाना और उन्हें चलाना।
- सुनिश्चित करना कि स्वचालित परीक्षण ख़तरों और सुरक्षा नियंत्रणों तक अनुरेखित हों और सुरक्षा केस के लिए साक्ष्य दें।
- अन्य परीक्षण इंजीनियरों को कोचिंग और मार्गदर्शन देना, और डेवलपरों के साथ इंजीनियरिंग मानकों पर सहमति बनाना।

### कौशल

| कौशल | स्रोत | अपेक्षित स्तर | इस स्तर का अर्थ |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../कौशल/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Designing and executing tests](../../कौशल/#designing-and-executing-tests) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• set up suitable environments<br>• influence and guide the use of appropriate test types and techniques to mitigate risk early<br>• lead others in designing, building, maintaining and executing tests that align to user needs and requirements<br>• contribute to developing and implementing standards for designing and executing tests<br>• improve test types and techniques through a structured process. |
| [Managing, reporting and resolving defects](../../कौशल/#managing-reporting-and-resolving-defects) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• contribute to developing standards for defect management processes<br>• manage and escalate dependencies, defects and risks across teams<br>• contribute to mitigation and contingency plans across teams<br>• use defect patterns and trends to make recommendations on testing and quality approaches, with support<br>• manage stakeholder expectations and communications during defect resolution |
| [Test analysis](../../कौशल/#test-analysis) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• lead work with stakeholders across teams to determine which functional and non-functional quality characteristics add value<br>• determine if an approach needs to change based on effort and risk<br>• ensure test needs are implemented early<br>• use multiple techniques to analyse complex information to identify risks<br>• coach others in test analysis |
| [Test and quality planning](../../कौशल/#test-and-quality-planning) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• work with teams to develop and implement appropriate quality testing approaches, plans and strategies<br>• contribute to organisational quality testing strategies<br>• implement ways to capture data to drive continuous improvement of quality testing approaches, plans and strategies<br>• advocate for full team ownership of quality testing activities, encouraging early engagement |
| [Test engineering](../../कौशल/#test-engineering) | UK GDaD PCF | अभ्यासकर्ता | You can:<br>• develop, standardise and extend reusable frameworks and tools to support a range of testing activities<br>• guide and coach others in creating and maintaining comprehensive and reliable tests that meet standards<br>• research and prepare for future testing needs, including tools, methodologies and techniques<br>• maintain and adapt continuous integration, continuous delivery (CI/CD) pipelines |
| [स्वास्थ्य और देखभाल सेवाओं की समझ](../../कौशल/#स्वास्थ्य-और-देखभाल-सेवाओं-की-समझ) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• उन क्लिनिकल और देखभाल कार्यप्रवाहों को समझाना जिनमें आपका काम सहायक है<br>• क्लिनिकल और देखभाल सहकर्मियों के साथ सामान्य स्वास्थ्य सेवा शब्दों का सही प्रयोग करना<br>• पहचानना कि कब कोई परिवर्तन रोगी देखभाल को प्रभावित कर सकता है, और उसे उठाना |
| [क्लिनिकल जोखिम प्रबंधन](../../कौशल/#क्लिनिकल-जोखिम-प्रबंधन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• ख़तरा कार्यशालाओं में भाग लेना और ख़तरा लॉग में योगदान देना<br>• अपने काम के लिए क्लिनिकल जोखिम प्रबंधन प्रक्रिया का पालन करना<br>• क्लिनिकल सुरक्षा केस के लिए परीक्षण परिणाम जैसे साक्ष्य देना |
| [सूचना शासन और डेटा संरक्षण](../../कौशल/#सूचना-शासन-और-डेटा-संरक्षण) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• अपने काम में डेटा संरक्षण सिद्धांत लागू करना<br>• डेटा संरक्षण प्रभाव आकलनों में योगदान देना<br>• सूचना अनुरोधों और अभिलेखों को सही ढंग से संभालना |
| [स्वास्थ्य डेटा अंतर-संचालनीयता](../../कौशल/#स्वास्थ्य-डेटा-अंतर-संचालनीयता) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• FHIR, HL7 संस्करण 2 और संदेश पैटर्न का उपयोग करके इंटीग्रेशन डिज़ाइन करना और बनाना<br>• FHIR संसाधन और कार्यान्वयन गाइड लिखना और उनकी प्रोफ़ाइल बनाना<br>• प्रणालियों के बीच जटिल मैपिंग और डेटा गुणवत्ता समस्याओं को सुलझाना |
| [चिकित्सा उपकरण सॉफ़्टवेयर विनियमन](../../कौशल/#चिकित्सा-उपकरण-सॉफ़्टवेयर-विनियमन) | यह संदर्भ | जागरूकता | आप ये कर सकते हैं:<br>• समझाना कि कुछ स्वास्थ्य सॉफ़्टवेयर चिकित्सा उपकरण के रूप में विनियमित होते हैं<br>• जानना कि जब कोई उत्पाद चिकित्सा उपकरण हो सकता है तो किससे पूछना है |

### सामान्य योग्यताएँ और अनुभव

- परीक्षण इंजीनियरिंग का पर्याप्त अनुभव, मास्टर डिग्री के समकक्ष स्तर पर।

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

## बैंड 8a: लीड परीक्षण इंजीनियर

**UK GDaD PCF स्तर: Lead test engineer**

> A lead test engineer sets the strategy for test engineering and influences test engineering practices across a broad area. They develop, monitor and evaluate quality engineering standards, and make strategic improvements to quality engineering in the organisation.
> 
> At this role level, you will:
> - lead a broad area in technical tooling, engineering approaches and test types and techniques to address risks early
> - define engineering standards, enabling others to follow them
> - lead and guide teams in quality engineering strategies and practices
> - lead and guide test engineers
> - escalate risks to senior stakeholders
> - lead and implement continuous testing, identifying opportunities to test earlier

### ज़िम्मेदारियाँ

- डिलीवरी पाइपलाइन में निरंतर परीक्षण सहित किसी व्यापक क्षेत्र में परीक्षण इंजीनियरिंग रणनीति और मानक तय करना।
- गुणवत्ता इंजीनियरिंग अभ्यास में परीक्षण इंजीनियरों और टीमों का नेतृत्व और मार्गदर्शन करना।
- सुनिश्चित करना कि विनियमित और सुरक्षा-महत्वपूर्ण सॉफ़्टवेयर का परीक्षण आवश्यक मानकों को पूरा करे और अनुरेखणीय हो।
- वरिष्ठ उत्पाद, क्लिनिकल और आपूर्तिकर्ता प्रमुखों तक गुणवत्ता और सुरक्षा जोखिम आगे बढ़ाना।
- पहले और अधिक बार परीक्षण के अवसर खोजना, और गुणवत्ता पर प्रभाव मापना।

### कौशल

| कौशल | स्रोत | अपेक्षित स्तर | इस स्तर का अर्थ |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../कौशल/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | विशेषज्ञ | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Designing and executing tests](../../कौशल/#designing-and-executing-tests) | UK GDaD PCF | विशेषज्ञ | You can:<br>• set standards and influence organisational decisions for test types, techniques, design and execution<br>• coach others in test types, techniques, design and execution<br>• advocate for continuous improvement and refinement of test types and techniques<br>• make strategic decisions on new or improved test types and techniques used in your area |
| [Managing, reporting and resolving defects](../../कौशल/#managing-reporting-and-resolving-defects) | UK GDaD PCF | विशेषज्ञ | You can:<br>• lead and coach others in improving test and defect management processes<br>• support others in assessing complex and challenging defects across the organisation<br>• lead and coach others in using defect patterns and trends to make tactical and strategic recommendations<br>• influence improvements to quality processes, informed by defect patterns and trends |
| [Test analysis](../../कौशल/#test-analysis) | UK GDaD PCF | विशेषज्ञ | You can:<br>• lead and guide multiple teams in test analysis, ensuring it is implemented early in the life cycle<br>• advocate for risk-based analysis to drive improvements across many teams<br>• set standards and principles for test analysis across the organisation |
| [Test and quality planning](../../कौशल/#test-and-quality-planning) | UK GDaD PCF | विशेषज्ञ | You can:<br>• create and manage multiple quality testing plans, approaches and strategies<br>• lead and guide multiple teams in adopting quality testing strategy<br>• advocate for early quality testing involvement in organisational delivery processes<br>• guide teams across an organisation in optimising quality testing approaches, plans and strategies by using appropriate data |
| [Test engineering](../../कौशल/#test-engineering) | UK GDaD PCF | विशेषज्ञ | You can:<br>• establish and lead test engineering practices, standards and behaviours<br>• influence and guide test engineering technology and tool choices across the organisation<br>• advocate for the adoption and use of appropriate testing solutions, ensuring alignment with organisational goals and quality objectives |
| [स्वास्थ्य और देखभाल सेवाओं की समझ](../../कौशल/#स्वास्थ्य-और-देखभाल-सेवाओं-की-समझ) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• विश्लेषण करना कि कोई सेवा विभिन्न संगठनों के देखभाल मार्गों में कैसे बैठती है<br>• डिजिटल सेवाओं को आकार देने के लिए चिकित्सकों, देखभाल कर्मचारियों और रोगियों के साथ काम करना<br>• देखभाल, सुरक्षा और कर्मचारियों के कार्यभार पर डिजिटल निर्णयों का प्रभाव समझाना |
| [क्लिनिकल जोखिम प्रबंधन](../../कौशल/#क्लिनिकल-जोखिम-प्रबंधन) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• किसी उत्पाद या परिवर्तन के लिए ख़तरा पहचान और जोखिम आकलन का नेतृत्व करना<br>• ख़तरा लॉग और क्लिनिकल सुरक्षा केस रिपोर्ट लिखना और बनाए रखना<br>• उत्पाद टीमों के साथ जोखिम नियंत्रणों पर सहमति बनाना और जाँचना कि वे काम करते हैं<br>• क्लिनिकल जोखिम प्रबंधन मानकों को लागू करने पर टीमों को सलाह देना |
| [सूचना शासन और डेटा संरक्षण](../../कौशल/#सूचना-शासन-और-डेटा-संरक्षण) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• अपने काम में डेटा संरक्षण सिद्धांत लागू करना<br>• डेटा संरक्षण प्रभाव आकलनों में योगदान देना<br>• सूचना अनुरोधों और अभिलेखों को सही ढंग से संभालना |
| [स्वास्थ्य डेटा अंतर-संचालनीयता](../../कौशल/#स्वास्थ्य-डेटा-अंतर-संचालनीयता) | यह संदर्भ | अभ्यासकर्ता | आप ये कर सकते हैं:<br>• FHIR, HL7 संस्करण 2 और संदेश पैटर्न का उपयोग करके इंटीग्रेशन डिज़ाइन करना और बनाना<br>• FHIR संसाधन और कार्यान्वयन गाइड लिखना और उनकी प्रोफ़ाइल बनाना<br>• प्रणालियों के बीच जटिल मैपिंग और डेटा गुणवत्ता समस्याओं को सुलझाना |
| [चिकित्सा उपकरण सॉफ़्टवेयर विनियमन](../../कौशल/#चिकित्सा-उपकरण-सॉफ़्टवेयर-विनियमन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• चिकित्सा उपकरण मानकों को पूरा करने वाली सॉफ़्टवेयर जीवनचक्र प्रक्रिया का पालन करना<br>• ऐसी प्रक्रिया के लिए आवश्यक अभिलेख तैयार करना |
| [लोगों का प्रबंधन](../../कौशल/#लोगों-का-प्रबंधन) | यह संदर्भ | कार्यरत | आप ये कर सकते हैं:<br>• दैनिक काम का पर्यवेक्षण करना और प्रतिक्रिया देना<br>• भर्ती और प्रारंभिक प्रशिक्षण में भाग लेना<br>• नियमित रूप से आमने-सामने बातचीत करना |

### सामान्य योग्यताएँ और अनुभव

- जटिल सेवाओं के लिए परीक्षण इंजीनियरिंग का नेतृत्व करने का व्यापक अनुभव।

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
| 8 | वित्तीय और भौतिक संसाधनों की ज़िम्मेदारी | 1 | 5 |
| 9 | लोगों की ज़िम्मेदारी | 3 | 21 |
| 10 | सूचना संसाधनों की ज़िम्मेदारी | 5 | 34 |
| 11 | अनुसंधान और विकास की ज़िम्मेदारी | 3 | 21 |
| 12 | कार्य करने की स्वतंत्रता | 5 | 45 |
| 13 | शारीरिक प्रयास | 1 | 3 |
| 14 | मानसिक प्रयास | 4 | 18 |
| 15 | भावनात्मक प्रयास | 1 | 5 |
| 16 | कार्य परिस्थितियाँ | 2 | 7 |
| | **कुल** | | **553** (बैंड 8a: 540–584) |

UK GDaD PCF इस स्तर के लिए SEO से G6 सुझाता है, जो बैंड 7 से जुड़ता है, वरिष्ठ परीक्षण इंजीनियर के बराबर। यह संदर्भ इसे बैंड 8a पर रखता है, क्योंकि यह किसी व्यापक क्षेत्र में परीक्षण इंजीनियरिंग रणनीति और मानक तय करता है।


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
