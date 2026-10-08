# টেস্ট ইঞ্জিনিয়ার

> এটি একটি সাধারণ ডিজিটাল স্বাস্থ্যসেবা প্রতিষ্ঠানের জন্য একটি দৃষ্টান্তমূলক রেফারেন্স প্রোফাইল। এটি কোনো নিয়োগকর্তার আনুষ্ঠানিক পদের বিবরণ নয়, এবং এর পদ মূল্যায়নের পয়েন্ট কোনো আনুষ্ঠানিক মূল্যায়ন নয়।

> এই লেখাটি একটি কৃত্রিম বুদ্ধিমত্তা সহকারী ইংরেজি থেকে অনুবাদ করেছে, এবং কোনো মাতৃভাষী এখনও এটি পর্যালোচনা করেননি। যুক্তরাজ্য (UK) সরকারের ডিজিটাল ও ডেটা পেশা সক্ষমতা কাঠামো (UK GDaD PCF) এবং ESCO থেকে নেওয়া উদ্ধৃতিগুলো ইংরেজিতেই রাখা হয়েছে।

**পরিবার:** [মান নিশ্চিতকরণ ও টেস্টিং](../../#মান-নিশ্চিতকরণ-ও-টেস্টিং)  
**ব্যান্ড:** 4, 6, 7, 8a  
**UK GDaD PCF ভূমিকা:** [Test engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/test-engineer/)  
**ESCO পেশা:** [software tester](http://data.europa.eu/esco/occupation/106f79e4-6264-45f1-9e7a-297435cd684b) (ISCO-08 2519)

## সারসংক্ষেপ

টেস্ট ইঞ্জিনিয়াররা এমন স্বয়ংক্রিয় পরীক্ষা, টুল ও ফ্রেমওয়ার্ক তৈরি করেন যা দলগুলোকে প্রতিষ্ঠানের ডিজিটাল স্বাস্থ্যসেবা দ্রুত ও ঘন ঘন পরীক্ষা করতে দেয়। তাঁরা কার্যকারিতা, ইন্টিগ্রেশন, কর্মদক্ষতা, নিরাপত্তা ও স্থিতিস্থাপকতা পরীক্ষার কোড লেখেন, এবং ডেলিভারি পাইপলাইনে পরীক্ষা যুক্ত করেন, যাতে ক্লিনিক্যাল ও রোগীমুখী ব্যবস্থার পরিবর্তন নিরাপদে রিলিজ করা যায়।

## একটি ডিজিটাল স্বাস্থ্যসেবা প্রতিষ্ঠানে

- ক্লিনিক্যাল ব্যবস্থা নিরাপত্তা-গুরুত্বপূর্ণ, তাই স্বয়ংক্রিয় রিগ্রেশন পরীক্ষা বিপদ লগে রেকর্ডকৃত নিরাপত্তা নিয়ন্ত্রণ রক্ষা করে এবং নিরাপত্তা কেসের প্রমাণ হিসেবে রাখা হয়।
- অন্য স্বাস্থ্য ও পরিচর্যা ব্যবস্থার সাথে ইন্টিগ্রেশনের জন্য HL7 FHIR ও HL7 সংস্করণ 2-এর মতো মানদণ্ডের বিপরীতে স্বয়ংক্রিয় পরীক্ষা দরকার, প্রায়ই অনুকৃত অংশীদার ব্যবস্থা ব্যবহার করে।
- ক্লিনিক্যাল সেবা চব্বিশ ঘণ্টা চলে এবং অনুমেয় সময়ে সর্বোচ্চ চাপে পৌঁছায়, তাই কর্মদক্ষতা ও স্থিতিস্থাপকতা পরীক্ষা বাস্তব ক্লিনিক্যাল চাহিদা মডেল করে।
- পরীক্ষার পরিবেশে প্রকৃত রোগী ডেটা থাকবে না, তাই ইঞ্জিনিয়াররা বিরল ও প্রান্তিক ক্লিনিক্যাল ক্ষেত্রসহ বাস্তবসম্মত কৃত্রিম ডেটা তৈরি করেন।
- মেডিক্যাল ডিভাইস হিসেবে নিয়ন্ত্রিত সফটওয়্যারের জন্য IEC 62304-এর মতো মানদণ্ডের অধীনে এর জীবনচক্রের অংশ হিসেবে অনুসরণযোগ্য, পুনরাবৃত্তিযোগ্য পরীক্ষা দরকার।

## UK GDaD PCF-এ ভূমিকার বিবরণ (মূল ইংরেজি)

> A test engineer designs, builds, automates and executes comprehensive, robust and maintainable test suites. They apply test engineering standards, perform exploratory testing and use diverse techniques to identify risks and improve testing efficiency and quality.
> 
> In this role you will:
> - maintain automated tests in continuous integration, continuous delivery (CI/CD) pipelines
> - use, develop and standardise reusable frameworks and tools following engineering practices and standards
> - analyse and test artefacts such as products, services and business processes
> - promote quality considerations throughout the development life cycle
> - support the resolution of technical issues

## ভূমিকার স্তর

| ব্যান্ড | পদবি | UK GDaD PCF স্তর | যুক্তরাজ্যের সিভিল সার্ভিস গ্রেড | পদ মূল্যায়নের পয়েন্ট |
| --- | --- | --- | --- | --- |
| 4 | [অ্যাসোসিয়েট টেস্ট ইঞ্জিনিয়ার](#ব্যান্ড-4-অ্যাসোসিয়েট-টেস্ট-ইঞ্জিনিয়ার) | Associate test engineer | EO | 275 |
| 6 | [টেস্ট ইঞ্জিনিয়ার](#ব্যান্ড-6-টেস্ট-ইঞ্জিনিয়ার) | Test engineer | HEO/SEO | 411 |
| 7 | [সিনিয়র টেস্ট ইঞ্জিনিয়ার](#ব্যান্ড-7-সিনিয়র-টেস্ট-ইঞ্জিনিয়ার) | Senior test engineer | SEO/G7 | 477 |
| 8a | [লিড টেস্ট ইঞ্জিনিয়ার](#ব্যান্ড-8a-লিড-টেস্ট-ইঞ্জিনিয়ার) | Lead test engineer | SEO/G7/G6 | 553 |

## ব্যান্ড 4: অ্যাসোসিয়েট টেস্ট ইঞ্জিনিয়ার

**UK GDaD PCF স্তর: Associate test engineer**

> An associate test engineer works closely with other test professionals to learn test engineering activities and techniques.
> 
> At this role level, you will:
> - contribute to and maintain technical test suites under supervision
> - follow engineering practices and standards to apply test approaches, plans and strategies under supervision
> - analyse artefacts such as user stories, prototypes, processes and designs with support
> - support the development of reports, recording of outcomes and resolution of defects
> - understand the technical tooling and engineering approach to design and execute tests

### দায়িত্ব

- দলের প্রকৌশল মানদণ্ড অনুসরণ করে তত্ত্বাবধানে সরল স্বয়ংক্রিয় পরীক্ষা লেখা ও রক্ষণাবেক্ষণ করা।
- স্বয়ংক্রিয় ও হাতে করা পরীক্ষা চালানো এবং ফলাফল নির্ভুলভাবে রেকর্ড করা।
- ক্লিনিক্যাল ব্যবস্থার সাথে ইন্টিগ্রেশনসহ ত্রুটি তদন্ত ও প্রতিবেদনে সাহায্য করা।
- কৃত্রিম পরীক্ষার ডেটা ব্যবহার করা এবং পরীক্ষার পরিবেশে তথ্য সুশাসনের নিয়ম অনুসরণ করা।
- দলের পরীক্ষার টুল, কোডের চর্চা ও ক্লিনিক্যাল নিরাপত্তা প্রক্রিয়া শেখা।

### দক্ষতা

| দক্ষতা | উৎস | প্রত্যাশিত স্তর | এই স্তরের অর্থ |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../দক্ষতা/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | সচেতনতা | You can:<br>• explain why it's important to communicate technical concepts in non-technical language<br>• explain the types of communication that can be used with internal and external stakeholders, and their impact |
| [Designing and executing tests](../../দক্ষতা/#designing-and-executing-tests) | UK GDaD PCF | সচেতনতা | You can:<br>• contribute to deciding the most appropriate test types and techniques to use<br>• follow guidance to design, build and maintain simple tests that align to user needs and requirements<br>• execute simple tests with support<br>• explain the value of automation within testing |
| [Managing, reporting and resolving defects](../../দক্ষতা/#managing-reporting-and-resolving-defects) | UK GDaD PCF | সচেতনতা | You can:<br>• explain how to report and track defects<br>• follow a defect management process to report, communicate and maintain defects with appropriate information<br>• retest and escalate defects when needed |
| [Test analysis](../../দক্ষতা/#test-analysis) | UK GDaD PCF | সচেতনতা | You can:<br>• describe quality characteristics and explain why they are important<br>• analyse information, such as user stories, prototypes, processes and designs, with support<br>• explain what might be a risk in achieving quality goals |
| [Test and quality planning](../../দক্ষতা/#test-and-quality-planning) | UK GDaD PCF | সচেতনতা | You can:<br>• explain the value of quality testing approaches, plans and strategies<br>• explain how different delivery methodologies affect quality testing approaches, plans and strategies<br>• follow quality testing approaches, plans and strategies, with support<br>• explain how to measure the effectiveness of quality testing approaches, plans and strategies, and why it’s important |
| [Test engineering](../../দক্ষতা/#test-engineering) | UK GDaD PCF | সচেতনতা | You can:<br>• explain why testing processes, environments and tools are important<br>• follow test engineering practices and standards, with support<br>• support the maintenance of automated tests and tools required for testing |
| [স্বাস্থ্য ও পরিচর্যা সেবা বোঝা](../../দক্ষতা/#স্বাস্থ্য-ও-পরিচর্যা-সেবা-বোঝা) | এই রেফারেন্স | সচেতনতা | আপনি পারেন:<br>• স্বাস্থ্য ও পরিচর্যা ব্যবস্থার প্রধান অংশগুলো এবং প্রতিষ্ঠান যেসব সেবায় সহায়তা করে তা বর্ণনা করতে<br>• আপনার কাজে রোগীর নিরাপত্তা ও গোপনীয়তা কেন গুরুত্বপূর্ণ তা ব্যাখ্যা করতে |
| [ক্লিনিক্যাল ঝুঁকি ব্যবস্থাপনা](../../দক্ষতা/#ক্লিনিক্যাল-ঝুঁকি-ব্যবস্থাপনা) | এই রেফারেন্স | সচেতনতা | আপনি পারেন:<br>• স্বাস্থ্য আইটি ব্যবস্থা কীভাবে রোগীদের ক্ষতি করতে পারে তা ব্যাখ্যা করতে, যেমন ভুল, অনুপস্থিত বা বিলম্বিত তথ্যের মাধ্যমে<br>• সম্ভাব্য ক্লিনিক্যাল নিরাপত্তা সমস্যা সঠিক পথে জানাতে |
| [তথ্য সুশাসন ও ডেটা সুরক্ষা](../../দক্ষতা/#তথ্য-সুশাসন-ও-ডেটা-সুরক্ষা) | এই রেফারেন্স | সচেতনতা | আপনি পারেন:<br>• ব্যক্তিগত ও স্বাস্থ্য তথ্য সামলানোর জন্য প্রতিষ্ঠানের নিয়ম অনুসরণ করতে<br>• ডেটা লঙ্ঘন বা প্রায়-দুর্ঘটনা চিনতে ও জানাতে |

### সাধারণ যোগ্যতা ও অভিজ্ঞতা

- কোডিং বা পরীক্ষার কিছু অভিজ্ঞতা, বা প্রাসঙ্গিক শিক্ষানবিশিতে ভর্তি, বা সমমান।

### ব্যান্ডের রূপরেখা

- **জ্ঞান:** কাজের ক্ষেত্রের বিস্তারিত জ্ঞান, সাধারণত ফাউন্ডেশন ডিগ্রি, শিক্ষানবিশি বা সমমানের অভিজ্ঞতা থেকে।
- **স্বাধীনতা:** নির্দেশিকার মধ্যে কাজ করেন; বেশিরভাগ দৈনন্দিন সমস্যা সমাধান করেন; পরামর্শের জন্য ব্যবস্থাপক থাকেন।
- **পরিসর:** নিজের কাজ এবং একটি নির্দিষ্ট সেবা বা প্রক্রিয়া।
- **নেতৃত্ব:** একটি ছোট দল তত্ত্বাবধান করতে বা অন্যদের কাজ সমন্বয় করতে পারেন।
- **জবাবদিহি:** একটি নির্দিষ্ট সেবা বা প্রক্রিয়া প্রদান।

### পদ মূল্যায়ন (দৃষ্টান্তমূলক)

| # | উপাদান | স্তর | পয়েন্ট |
| --- | --- | --- | --- |
| 1 | যোগাযোগ ও সম্পর্ক স্থাপনের দক্ষতা | 3 | 21 |
| 2 | জ্ঞান, প্রশিক্ষণ ও অভিজ্ঞতা | 4 | 88 |
| 3 | বিশ্লেষণ ও বিচার-বিবেচনার দক্ষতা | 3 | 27 |
| 4 | পরিকল্পনা ও সংগঠনের দক্ষতা | 2 | 15 |
| 5 | শারীরিক দক্ষতা | 3 | 27 |
| 6 | রোগী ও সেবাগ্রহীতার পরিচর্যার দায়িত্ব | 1 | 4 |
| 7 | নীতি ও সেবা উন্নয়নের দায়িত্ব | 2 | 12 |
| 8 | আর্থিক ও ভৌত সম্পদের দায়িত্ব | 1 | 5 |
| 9 | জনবলের দায়িত্ব | 1 | 5 |
| 10 | তথ্য সম্পদের দায়িত্ব | 3 | 16 |
| 11 | গবেষণা ও উন্নয়নের দায়িত্ব | 2 | 12 |
| 12 | কাজের স্বাধীনতা | 2 | 12 |
| 13 | শারীরিক পরিশ্রম | 2 | 7 |
| 14 | মানসিক পরিশ্রম | 3 | 12 |
| 15 | মানসিক চাপ | 1 | 5 |
| 16 | কাজের পরিবেশ | 2 | 7 |
| | **মোট** | | **275** (ব্যান্ড 4: 271–325) |

## ব্যান্ড 6: টেস্ট ইঞ্জিনিয়ার

**UK GDaD PCF স্তর: Test engineer**

> A test engineer develops solutions to enable more efficient testing. They follow engineering standards to design and execute appropriate technical tests.
> 
> At this role level, you will:
> - determine test scope and estimate the effort required
> - select and use the most appropriate test approaches and techniques to mitigate risk
> - use technical tooling and engineering approaches to design and execute tests
> - develop and maintain technical test suites
> - develop reports, record outcomes and support the resolution of defects
> - contribute to and follow engineering practices and standards

### দায়িত্ব

- ক্লিনিক্যাল ও রোগীমুখী সেবার জন্য স্বয়ংক্রিয় কার্যকরী, ইন্টিগ্রেশন ও API পরীক্ষা ডিজাইন ও তৈরি করা।
- HL7 FHIR প্রোফাইল ও অন্যান্য আন্তঃকার্যক্ষমতা নির্দিষ্টকরণের বিপরীতে বার্তা যাচাই করে এমন পরীক্ষা তৈরি করা।
- বাস্তবসম্মত ও প্রান্তিক ক্লিনিক্যাল ক্ষেত্র অন্তর্ভুক্ত কৃত্রিম রোগী ডেটা তৈরি করা।
- ডেলিভারি পাইপলাইনে পরীক্ষা যোগ করা যাতে প্রতিটি পরিবর্তনে নিরাপত্তা-সংশ্লিষ্ট যাচাই চলে।
- পরীক্ষার প্রচেষ্টা অনুমান করা, ফলাফল প্রতিবেদন করা এবং ত্রুটি সমাধানে সহায়তা করা।

### দক্ষতা

| দক্ষতা | উৎস | প্রত্যাশিত স্তর | এই স্তরের অর্থ |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../দক্ষতা/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | কার্যকর | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Designing and executing tests](../../দক্ষতা/#designing-and-executing-tests) | UK GDaD PCF | কার্যকর | You can:<br>• set up suitable environments with some support<br>• select appropriate test types and techniques with some support<br>• design, build, maintain and execute tests that align to user needs and requirements<br>• conduct exploratory testing<br>• research and try new test types and techniques |
| [Managing, reporting and resolving defects](../../দক্ষতা/#managing-reporting-and-resolving-defects) | UK GDaD PCF | কার্যকর | You can:<br>• collaborate with others to create a defect management process to report, communicate and resolve defects, with support<br>• critically assess dependencies, defects and risks, with support<br>• contribute to mitigation and contingency plans<br>• clearly communicate risks and the impact of defects to stakeholders |
| [Test analysis](../../দক্ষতা/#test-analysis) | UK GDaD PCF | কার্যকর | You can:<br>• work with stakeholders to determine which functional and non-functional quality characteristics add value<br>• determine what to test following an agreed approach<br>• identify and advocate for test needs, such as data, access and environments, with support<br>• analyse information to identify risks |
| [Test and quality planning](../../দক্ষতা/#test-and-quality-planning) | UK GDaD PCF | কার্যকর | You can:<br>• create or adapt quality testing approaches based on risk, with some support<br>• follow a quality testing strategy and contribute to its development<br>• contribute to continuous improvement of quality testing approaches, plans and strategies |
| [Test engineering](../../দক্ষতা/#test-engineering) | UK GDaD PCF | কার্যকর | You can:<br>• use test engineering frameworks and tools to support testing activities<br>• follow test engineering practices and standards, such as source control and continuous integration, continuous delivery (CI/CD) pipelines<br>• integrate and execute tests to ensure early testing and continuous feedback<br>• create and maintain automated tests, with some support<br>• write and review coded solutions, with some support |
| [স্বাস্থ্য ও পরিচর্যা সেবা বোঝা](../../দক্ষতা/#স্বাস্থ্য-ও-পরিচর্যা-সেবা-বোঝা) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• আপনার কাজ যেসব ক্লিনিক্যাল ও পরিচর্যা কর্মপ্রবাহে সহায়তা করে তা ব্যাখ্যা করতে<br>• ক্লিনিক্যাল ও পরিচর্যা সহকর্মীদের সাথে প্রচলিত স্বাস্থ্যসেবা পরিভাষা সঠিকভাবে ব্যবহার করতে<br>• কোনো পরিবর্তন রোগী পরিচর্যাকে প্রভাবিত করতে পারে কি না তা চিনতে এবং তা জানাতে |
| [ক্লিনিক্যাল ঝুঁকি ব্যবস্থাপনা](../../দক্ষতা/#ক্লিনিক্যাল-ঝুঁকি-ব্যবস্থাপনা) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• বিপদ চিহ্নিতকরণ কর্মশালায় অংশ নিতে এবং বিপদ লগে অবদান রাখতে<br>• আপনার কাজের জন্য ক্লিনিক্যাল ঝুঁকি ব্যবস্থাপনা প্রক্রিয়া অনুসরণ করতে<br>• ক্লিনিক্যাল নিরাপত্তা কেসের জন্য প্রমাণ দিতে, যেমন পরীক্ষার ফলাফল |
| [তথ্য সুশাসন ও ডেটা সুরক্ষা](../../দক্ষতা/#তথ্য-সুশাসন-ও-ডেটা-সুরক্ষা) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• আপনার কাজে ডেটা সুরক্ষার নীতিগুলো প্রয়োগ করতে<br>• ডেটা সুরক্ষা প্রভাব মূল্যায়নে অবদান রাখতে<br>• তথ্যের অনুরোধ ও রেকর্ড সঠিকভাবে সামলাতে |
| [স্বাস্থ্য ডেটার আন্তঃকার্যক্ষমতা](../../দক্ষতা/#স্বাস্থ্য-ডেটার-আন্তঃকার্যক্ষমতা) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• FHIR রিসোর্স, প্রোফাইল ও API পড়তে ও ব্যবহার করতে<br>• নির্দেশনায় সরল ইন্টিগ্রেশন তৈরি বা পরীক্ষা করতে<br>• একটি নির্দিষ্টকরণের সাথে বার্তা মিলিয়ে দেখতে |

### সাধারণ যোগ্যতা ও অভিজ্ঞতা

- কম্পিউটিং বা সংশ্লিষ্ট বিষয়ে ডিগ্রি, বা সমমানের অভিজ্ঞতা।
- স্বয়ংক্রিয় পরীক্ষা তৈরির অভিজ্ঞতা।

### ব্যান্ডের রূপরেখা

- **জ্ঞান:** বিভিন্ন পদ্ধতিতে বিশেষায়িত জ্ঞান, যা অতিরিক্ত প্রশিক্ষণ বা অভিজ্ঞতার মাধ্যমে গড়ে উঠেছে।
- **স্বাধীনতা:** স্বাধীনভাবে কাজ করেন; নিজের ক্ষেত্রের জন্য নীতির ব্যাখ্যা করেন; জটিল বিষয়ে পরামর্শ নেন।
- **পরিসর:** একটি প্রোডাক্ট, সেবা বা কাজের ধারা।
- **নেতৃত্ব:** একটি ছোট দলের নেতৃত্ব দিতে বা সহকর্মীদের পরামর্শদাতা হতে পারেন।
- **জবাবদিহি:** নিজের কাজের ধারার ফলাফল এবং প্রদত্ত পরামর্শের মান।

### পদ মূল্যায়ন (দৃষ্টান্তমূলক)

| # | উপাদান | স্তর | পয়েন্ট |
| --- | --- | --- | --- |
| 1 | যোগাযোগ ও সম্পর্ক স্থাপনের দক্ষতা | 4 | 32 |
| 2 | জ্ঞান, প্রশিক্ষণ ও অভিজ্ঞতা | 6 | 156 |
| 3 | বিশ্লেষণ ও বিচার-বিবেচনার দক্ষতা | 4 | 42 |
| 4 | পরিকল্পনা ও সংগঠনের দক্ষতা | 3 | 27 |
| 5 | শারীরিক দক্ষতা | 3 | 27 |
| 6 | রোগী ও সেবাগ্রহীতার পরিচর্যার দায়িত্ব | 1 | 4 |
| 7 | নীতি ও সেবা উন্নয়নের দায়িত্ব | 2 | 12 |
| 8 | আর্থিক ও ভৌত সম্পদের দায়িত্ব | 1 | 5 |
| 9 | জনবলের দায়িত্ব | 1 | 5 |
| 10 | তথ্য সম্পদের দায়িত্ব | 4 | 24 |
| 11 | গবেষণা ও উন্নয়নের দায়িত্ব | 2 | 12 |
| 12 | কাজের স্বাধীনতা | 4 | 32 |
| 13 | শারীরিক পরিশ্রম | 1 | 3 |
| 14 | মানসিক পরিশ্রম | 4 | 18 |
| 15 | মানসিক চাপ | 1 | 5 |
| 16 | কাজের পরিবেশ | 2 | 7 |
| | **মোট** | | **411** (ব্যান্ড 6: 396–465) |

## ব্যান্ড 7: সিনিয়র টেস্ট ইঞ্জিনিয়ার

**UK GDaD PCF স্তর: Senior test engineer**

> A senior test engineer is responsible for test engineering in their area. They influence, coach and guide others in test engineering, sharing best practice and standards.
> 
> At this role level, you will:
> - select, use and guide others in using the most appropriate technical tooling, engineering approaches, test types and techniques to identify and address risks early
> - extend, standardise and build reusable frameworks and tools that support testing
> - communicate and document chosen approaches, tools, techniques and outcomes to the team and appropriate stakeholders
> - contribute to and agree engineering standards

### দায়িত্ব

- একটি ক্ষেত্রের পরীক্ষা প্রকৌশলের নেতৃত্ব দেওয়া, এর ঝুঁকি আগেভাগে মোকাবিলা করে এমন টুল, ফ্রেমওয়ার্ক ও পরীক্ষার ধরন বেছে নিয়ে।
- ক্লিনিক্যাল ব্যবস্থা ও অংশীদার ইন্টিগ্রেশনের জন্য পুনর্ব্যবহারযোগ্য পরীক্ষা ফ্রেমওয়ার্ক ও সিমুলেটর তৈরি করা।
- বাস্তব ক্লিনিক্যাল চাহিদার ভিত্তিতে কর্মদক্ষতা, লোড ও স্থিতিস্থাপকতা পরীক্ষার পরিকল্পনা ও পরিচালনা করা।
- স্বয়ংক্রিয় পরীক্ষাগুলো বিপদ ও নিরাপত্তা নিয়ন্ত্রণের সাথে যুক্ত এবং নিরাপত্তা কেসের প্রমাণ তৈরি করে তা নিশ্চিত করা।
- অন্য টেস্ট ইঞ্জিনিয়ারদের কোচিং ও দিকনির্দেশনা দেওয়া, এবং ডেভেলপারদের সাথে প্রকৌশল মানদণ্ডে একমত হওয়া।

### দক্ষতা

| দক্ষতা | উৎস | প্রত্যাশিত স্তর | এই স্তরের অর্থ |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../দক্ষতা/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Designing and executing tests](../../দক্ষতা/#designing-and-executing-tests) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• set up suitable environments<br>• influence and guide the use of appropriate test types and techniques to mitigate risk early<br>• lead others in designing, building, maintaining and executing tests that align to user needs and requirements<br>• contribute to developing and implementing standards for designing and executing tests<br>• improve test types and techniques through a structured process. |
| [Managing, reporting and resolving defects](../../দক্ষতা/#managing-reporting-and-resolving-defects) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• contribute to developing standards for defect management processes<br>• manage and escalate dependencies, defects and risks across teams<br>• contribute to mitigation and contingency plans across teams<br>• use defect patterns and trends to make recommendations on testing and quality approaches, with support<br>• manage stakeholder expectations and communications during defect resolution |
| [Test analysis](../../দক্ষতা/#test-analysis) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• lead work with stakeholders across teams to determine which functional and non-functional quality characteristics add value<br>• determine if an approach needs to change based on effort and risk<br>• ensure test needs are implemented early<br>• use multiple techniques to analyse complex information to identify risks<br>• coach others in test analysis |
| [Test and quality planning](../../দক্ষতা/#test-and-quality-planning) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• work with teams to develop and implement appropriate quality testing approaches, plans and strategies<br>• contribute to organisational quality testing strategies<br>• implement ways to capture data to drive continuous improvement of quality testing approaches, plans and strategies<br>• advocate for full team ownership of quality testing activities, encouraging early engagement |
| [Test engineering](../../দক্ষতা/#test-engineering) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• develop, standardise and extend reusable frameworks and tools to support a range of testing activities<br>• guide and coach others in creating and maintaining comprehensive and reliable tests that meet standards<br>• research and prepare for future testing needs, including tools, methodologies and techniques<br>• maintain and adapt continuous integration, continuous delivery (CI/CD) pipelines |
| [স্বাস্থ্য ও পরিচর্যা সেবা বোঝা](../../দক্ষতা/#স্বাস্থ্য-ও-পরিচর্যা-সেবা-বোঝা) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• আপনার কাজ যেসব ক্লিনিক্যাল ও পরিচর্যা কর্মপ্রবাহে সহায়তা করে তা ব্যাখ্যা করতে<br>• ক্লিনিক্যাল ও পরিচর্যা সহকর্মীদের সাথে প্রচলিত স্বাস্থ্যসেবা পরিভাষা সঠিকভাবে ব্যবহার করতে<br>• কোনো পরিবর্তন রোগী পরিচর্যাকে প্রভাবিত করতে পারে কি না তা চিনতে এবং তা জানাতে |
| [ক্লিনিক্যাল ঝুঁকি ব্যবস্থাপনা](../../দক্ষতা/#ক্লিনিক্যাল-ঝুঁকি-ব্যবস্থাপনা) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• বিপদ চিহ্নিতকরণ কর্মশালায় অংশ নিতে এবং বিপদ লগে অবদান রাখতে<br>• আপনার কাজের জন্য ক্লিনিক্যাল ঝুঁকি ব্যবস্থাপনা প্রক্রিয়া অনুসরণ করতে<br>• ক্লিনিক্যাল নিরাপত্তা কেসের জন্য প্রমাণ দিতে, যেমন পরীক্ষার ফলাফল |
| [তথ্য সুশাসন ও ডেটা সুরক্ষা](../../দক্ষতা/#তথ্য-সুশাসন-ও-ডেটা-সুরক্ষা) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• আপনার কাজে ডেটা সুরক্ষার নীতিগুলো প্রয়োগ করতে<br>• ডেটা সুরক্ষা প্রভাব মূল্যায়নে অবদান রাখতে<br>• তথ্যের অনুরোধ ও রেকর্ড সঠিকভাবে সামলাতে |
| [স্বাস্থ্য ডেটার আন্তঃকার্যক্ষমতা](../../দক্ষতা/#স্বাস্থ্য-ডেটার-আন্তঃকার্যক্ষমতা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• FHIR, HL7 সংস্করণ 2 ও বার্তা বিনিময়ের ধরন ব্যবহার করে ইন্টিগ্রেশন ডিজাইন ও তৈরি করতে<br>• FHIR রিসোর্স ও বাস্তবায়ন নির্দেশিকা লিখতে ও প্রোফাইল করতে<br>• ব্যবস্থাগুলোর মধ্যে জটিল ম্যাপিং ও ডেটার মানের সমস্যা সমাধান করতে |
| [মেডিক্যাল ডিভাইস সফটওয়্যার নিয়ন্ত্রণ](../../দক্ষতা/#মেডিক্যাল-ডিভাইস-সফটওয়্যার-নিয়ন্ত্রণ) | এই রেফারেন্স | সচেতনতা | আপনি পারেন:<br>• কিছু স্বাস্থ্য সফটওয়্যার মেডিক্যাল ডিভাইস হিসেবে নিয়ন্ত্রিত তা ব্যাখ্যা করতে<br>• কোনো প্রোডাক্ট মেডিক্যাল ডিভাইস হতে পারে মনে হলে কাকে জিজ্ঞাসা করতে হবে তা জানতে |

### সাধারণ যোগ্যতা ও অভিজ্ঞতা

- স্নাতকোত্তর ডিগ্রির সমমান স্তরে পরীক্ষা প্রকৌশলের উল্লেখযোগ্য অভিজ্ঞতা।

### ব্যান্ডের রূপরেখা

- **জ্ঞান:** অত্যন্ত উন্নত বিশেষায়িত জ্ঞান, সাধারণত স্নাতকোত্তর স্তরের বা সমমানের অভিজ্ঞতা।
- **স্বাধীনতা:** প্রতিষ্ঠানের নীতি অনুযায়ী কাজ করেন; ফলাফল কীভাবে অর্জিত হবে তা ঠিক করেন; অন্যরা যাঁর পরামর্শ নেন সেই বিশেষজ্ঞ।
- **পরিসর:** একাধিক প্রোডাক্ট বা সেবা, অথবা একটি বিশেষায়িত কার্যক্রম।
- **নেতৃত্ব:** একটি দল বা একটি পেশাগত অনুশীলন ক্ষেত্রের নেতৃত্ব দেন।
- **জবাবদিহি:** একটি সেবা বা বিশেষায়িত কার্যক্রম প্রদান, এবং বাজেট থাকলে তার দায়িত্ব।

### পদ মূল্যায়ন (দৃষ্টান্তমূলক)

| # | উপাদান | স্তর | পয়েন্ট |
| --- | --- | --- | --- |
| 1 | যোগাযোগ ও সম্পর্ক স্থাপনের দক্ষতা | 4 | 32 |
| 2 | জ্ঞান, প্রশিক্ষণ ও অভিজ্ঞতা | 7 | 196 |
| 3 | বিশ্লেষণ ও বিচার-বিবেচনার দক্ষতা | 4 | 42 |
| 4 | পরিকল্পনা ও সংগঠনের দক্ষতা | 3 | 27 |
| 5 | শারীরিক দক্ষতা | 3 | 27 |
| 6 | রোগী ও সেবাগ্রহীতার পরিচর্যার দায়িত্ব | 1 | 4 |
| 7 | নীতি ও সেবা উন্নয়নের দায়িত্ব | 3 | 21 |
| 8 | আর্থিক ও ভৌত সম্পদের দায়িত্ব | 1 | 5 |
| 9 | জনবলের দায়িত্ব | 2 | 12 |
| 10 | তথ্য সম্পদের দায়িত্ব | 5 | 34 |
| 11 | গবেষণা ও উন্নয়নের দায়িত্ব | 2 | 12 |
| 12 | কাজের স্বাধীনতা | 4 | 32 |
| 13 | শারীরিক পরিশ্রম | 1 | 3 |
| 14 | মানসিক পরিশ্রম | 4 | 18 |
| 15 | মানসিক চাপ | 1 | 5 |
| 16 | কাজের পরিবেশ | 2 | 7 |
| | **মোট** | | **477** (ব্যান্ড 7: 466–539) |

## ব্যান্ড 8a: লিড টেস্ট ইঞ্জিনিয়ার

**UK GDaD PCF স্তর: Lead test engineer**

> A lead test engineer sets the strategy for test engineering and influences test engineering practices across a broad area. They develop, monitor and evaluate quality engineering standards, and make strategic improvements to quality engineering in the organisation.
> 
> At this role level, you will:
> - lead a broad area in technical tooling, engineering approaches and test types and techniques to address risks early
> - define engineering standards, enabling others to follow them
> - lead and guide teams in quality engineering strategies and practices
> - lead and guide test engineers
> - escalate risks to senior stakeholders
> - lead and implement continuous testing, identifying opportunities to test earlier

### দায়িত্ব

- ডেলিভারি পাইপলাইনে ধারাবাহিক পরীক্ষাসহ একটি বিস্তৃত ক্ষেত্রজুড়ে পরীক্ষা প্রকৌশলের কৌশল ও মানদণ্ড নির্ধারণ করা।
- মান প্রকৌশলের চর্চায় টেস্ট ইঞ্জিনিয়ার ও দলগুলোর নেতৃত্ব ও দিকনির্দেশনা দেওয়া।
- নিয়ন্ত্রিত ও নিরাপত্তা-গুরুত্বপূর্ণ সফটওয়্যারের পরীক্ষা প্রয়োজনীয় মানদণ্ড পূরণ করে এবং অনুসরণযোগ্য তা নিশ্চিত করা।
- মান ও নিরাপত্তার ঝুঁকি জ্যেষ্ঠ প্রোডাক্ট, ক্লিনিক্যাল ও সরবরাহকারী নেতাদের কাছে পাঠানো।
- আরও আগে ও ঘন ঘন পরীক্ষার সুযোগ খোঁজা, এবং মানের ওপর এর প্রভাব পরিমাপ করা।

### দক্ষতা

| দক্ষতা | উৎস | প্রত্যাশিত স্তর | এই স্তরের অর্থ |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../দক্ষতা/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | বিশেষজ্ঞ | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Designing and executing tests](../../দক্ষতা/#designing-and-executing-tests) | UK GDaD PCF | বিশেষজ্ঞ | You can:<br>• set standards and influence organisational decisions for test types, techniques, design and execution<br>• coach others in test types, techniques, design and execution<br>• advocate for continuous improvement and refinement of test types and techniques<br>• make strategic decisions on new or improved test types and techniques used in your area |
| [Managing, reporting and resolving defects](../../দক্ষতা/#managing-reporting-and-resolving-defects) | UK GDaD PCF | বিশেষজ্ঞ | You can:<br>• lead and coach others in improving test and defect management processes<br>• support others in assessing complex and challenging defects across the organisation<br>• lead and coach others in using defect patterns and trends to make tactical and strategic recommendations<br>• influence improvements to quality processes, informed by defect patterns and trends |
| [Test analysis](../../দক্ষতা/#test-analysis) | UK GDaD PCF | বিশেষজ্ঞ | You can:<br>• lead and guide multiple teams in test analysis, ensuring it is implemented early in the life cycle<br>• advocate for risk-based analysis to drive improvements across many teams<br>• set standards and principles for test analysis across the organisation |
| [Test and quality planning](../../দক্ষতা/#test-and-quality-planning) | UK GDaD PCF | বিশেষজ্ঞ | You can:<br>• create and manage multiple quality testing plans, approaches and strategies<br>• lead and guide multiple teams in adopting quality testing strategy<br>• advocate for early quality testing involvement in organisational delivery processes<br>• guide teams across an organisation in optimising quality testing approaches, plans and strategies by using appropriate data |
| [Test engineering](../../দক্ষতা/#test-engineering) | UK GDaD PCF | বিশেষজ্ঞ | You can:<br>• establish and lead test engineering practices, standards and behaviours<br>• influence and guide test engineering technology and tool choices across the organisation<br>• advocate for the adoption and use of appropriate testing solutions, ensuring alignment with organisational goals and quality objectives |
| [স্বাস্থ্য ও পরিচর্যা সেবা বোঝা](../../দক্ষতা/#স্বাস্থ্য-ও-পরিচর্যা-সেবা-বোঝা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• বিভিন্ন প্রতিষ্ঠানজুড়ে পরিচর্যা পথে একটি সেবা কীভাবে খাপ খায় তা বিশ্লেষণ করতে<br>• ডিজিটাল সেবা গড়তে চিকিৎসক, পরিচর্যাকর্মী ও রোগীদের সাথে কাজ করতে<br>• ডিজিটাল সিদ্ধান্তের প্রভাব পরিচর্যা, নিরাপত্তা ও কর্মীদের কাজের চাপের ওপর ব্যাখ্যা করতে |
| [ক্লিনিক্যাল ঝুঁকি ব্যবস্থাপনা](../../দক্ষতা/#ক্লিনিক্যাল-ঝুঁকি-ব্যবস্থাপনা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• একটি প্রোডাক্ট বা পরিবর্তনের জন্য বিপদ চিহ্নিতকরণ ও ঝুঁকি মূল্যায়নের নেতৃত্ব দিতে<br>• বিপদ লগ ও ক্লিনিক্যাল নিরাপত্তা কেস প্রতিবেদন লিখতে ও হালনাগাদ রাখতে<br>• প্রোডাক্ট দলের সাথে ঝুঁকি নিয়ন্ত্রণে একমত হতে এবং সেগুলো কাজ করে কি না যাচাই করতে<br>• ক্লিনিক্যাল ঝুঁকি ব্যবস্থাপনার মানদণ্ড প্রয়োগে দলগুলোকে পরামর্শ দিতে |
| [তথ্য সুশাসন ও ডেটা সুরক্ষা](../../দক্ষতা/#তথ্য-সুশাসন-ও-ডেটা-সুরক্ষা) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• আপনার কাজে ডেটা সুরক্ষার নীতিগুলো প্রয়োগ করতে<br>• ডেটা সুরক্ষা প্রভাব মূল্যায়নে অবদান রাখতে<br>• তথ্যের অনুরোধ ও রেকর্ড সঠিকভাবে সামলাতে |
| [স্বাস্থ্য ডেটার আন্তঃকার্যক্ষমতা](../../দক্ষতা/#স্বাস্থ্য-ডেটার-আন্তঃকার্যক্ষমতা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• FHIR, HL7 সংস্করণ 2 ও বার্তা বিনিময়ের ধরন ব্যবহার করে ইন্টিগ্রেশন ডিজাইন ও তৈরি করতে<br>• FHIR রিসোর্স ও বাস্তবায়ন নির্দেশিকা লিখতে ও প্রোফাইল করতে<br>• ব্যবস্থাগুলোর মধ্যে জটিল ম্যাপিং ও ডেটার মানের সমস্যা সমাধান করতে |
| [মেডিক্যাল ডিভাইস সফটওয়্যার নিয়ন্ত্রণ](../../দক্ষতা/#মেডিক্যাল-ডিভাইস-সফটওয়্যার-নিয়ন্ত্রণ) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• মেডিক্যাল ডিভাইস মানদণ্ড পূরণ করে এমন একটি সফটওয়্যার জীবনচক্র প্রক্রিয়া অনুসরণ করতে<br>• সেই প্রক্রিয়ার প্রয়োজনীয় রেকর্ড তৈরি করতে |
| [জনবল ব্যবস্থাপনা](../../দক্ষতা/#জনবল-ব্যবস্থাপনা) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• দৈনন্দিন কাজ তত্ত্বাবধান করতে এবং মতামত দিতে<br>• নিয়োগ ও পরিচিতিমূলক কাজে অংশ নিতে<br>• নিয়মিত একান্ত আলোচনা করতে |

### সাধারণ যোগ্যতা ও অভিজ্ঞতা

- জটিল সেবার পরীক্ষা প্রকৌশলের নেতৃত্বে ব্যাপক অভিজ্ঞতা।

### ব্যান্ডের রূপরেখা

- **জ্ঞান:** একটি শাখা ও তার ব্যবস্থাপনায় বিশেষজ্ঞ জ্ঞান।
- **স্বাধীনতা:** একটি সেবার জন্য প্রতিষ্ঠানের নীতির ব্যাখ্যা করেন; দলের দিকনির্দেশনা ঠিক করেন।
- **পরিসর:** একটি সেবা ক্ষেত্র বা পুরো প্রতিষ্ঠানে একটি শাখা।
- **নেতৃত্ব:** একটি দল পরিচালনা করেন, অথবা সরাসরি ব্যবস্থাপনা ছাড়াই একটি শাখার নেতৃত্ব দেন।
- **জবাবদিহি:** একটি সেবা ক্ষেত্র, তার কর্মী ও বাজেট।

### পদ মূল্যায়ন (দৃষ্টান্তমূলক)

| # | উপাদান | স্তর | পয়েন্ট |
| --- | --- | --- | --- |
| 1 | যোগাযোগ ও সম্পর্ক স্থাপনের দক্ষতা | 5 | 45 |
| 2 | জ্ঞান, প্রশিক্ষণ ও অভিজ্ঞতা | 7 | 196 |
| 3 | বিশ্লেষণ ও বিচার-বিবেচনার দক্ষতা | 5 | 60 |
| 4 | পরিকল্পনা ও সংগঠনের দক্ষতা | 4 | 42 |
| 5 | শারীরিক দক্ষতা | 2 | 15 |
| 6 | রোগী ও সেবাগ্রহীতার পরিচর্যার দায়িত্ব | 1 | 4 |
| 7 | নীতি ও সেবা উন্নয়নের দায়িত্ব | 4 | 32 |
| 8 | আর্থিক ও ভৌত সম্পদের দায়িত্ব | 1 | 5 |
| 9 | জনবলের দায়িত্ব | 3 | 21 |
| 10 | তথ্য সম্পদের দায়িত্ব | 5 | 34 |
| 11 | গবেষণা ও উন্নয়নের দায়িত্ব | 3 | 21 |
| 12 | কাজের স্বাধীনতা | 5 | 45 |
| 13 | শারীরিক পরিশ্রম | 1 | 3 |
| 14 | মানসিক পরিশ্রম | 4 | 18 |
| 15 | মানসিক চাপ | 1 | 5 |
| 16 | কাজের পরিবেশ | 2 | 7 |
| | **মোট** | | **553** (ব্যান্ড 8a: 540–584) |

UK GDaD PCF এই স্তরের জন্য SEO থেকে G6 প্রস্তাব করে, যা সিনিয়র টেস্ট ইঞ্জিনিয়ারের মতো ব্যান্ড 7-এর সাথে মেলে। এই রেফারেন্স এটিকে ব্যান্ড 8a-তে রাখে, কারণ এটি একটি বিস্তৃত ক্ষেত্রজুড়ে পরীক্ষা প্রকৌশলের কৌশল ও মানদণ্ড নির্ধারণ করে।


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
