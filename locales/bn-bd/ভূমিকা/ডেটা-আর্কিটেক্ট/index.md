# ডেটা আর্কিটেক্ট

> এটি একটি সাধারণ ডিজিটাল স্বাস্থ্যসেবা প্রতিষ্ঠানের জন্য একটি দৃষ্টান্তমূলক রেফারেন্স প্রোফাইল। এটি কোনো নিয়োগকর্তার আনুষ্ঠানিক পদের বিবরণ নয়, এবং এর পদ মূল্যায়নের পয়েন্ট কোনো আনুষ্ঠানিক মূল্যায়ন নয়।

> এই লেখাটি একটি কৃত্রিম বুদ্ধিমত্তা সহকারী ইংরেজি থেকে অনুবাদ করেছে, এবং কোনো মাতৃভাষী এখনও এটি পর্যালোচনা করেননি। যুক্তরাজ্য (UK) সরকারের ডিজিটাল ও ডেটা পেশা সক্ষমতা কাঠামো (UK GDaD PCF) এবং ESCO থেকে নেওয়া উদ্ধৃতিগুলো ইংরেজিতেই রাখা হয়েছে।

**পরিবার:** [আর্কিটেকচার](../../#আর্কিটেকচার)  
**ব্যান্ড:** 8a, 8b, 8c  
**UK GDaD PCF ভূমিকা:** [Data architect](https://understand-digital-data-roles-skills.service.gov.uk/role/data-architect/)  
**ESCO পেশা:** [database designer](http://data.europa.eu/esco/occupation/8d9ec84d-cf2d-4179-87bc-335cda54a427) (ISCO-08 2521); [data warehouse designer](http://data.europa.eu/esco/occupation/1562c7a3-c7d9-419d-b9b6-db26610bcf84) (ISCO-08 2521)

## সারসংক্ষেপ

ডেটা আর্কিটেক্টরা ডিজাইন করেন প্রতিষ্ঠান কীভাবে তার স্বাস্থ্য ও পরিচর্যা ডেটা গঠন, সংরক্ষণ, স্থানান্তর ও সুশাসন করবে, যাতে সরাসরি পরিচর্যা, সেবা পরিকল্পনা ও গবেষণায় তা নিরাপদে ব্যবহার করা যায়। তাঁরা ডেটা মডেল, ডেটা প্ল্যাটফর্ম ও ডেটা প্রবাহ ডিজাইন করেন, ডেটার মানদণ্ড নির্ধারণ করেন, এবং শুরু থেকে শেষ পর্যন্ত ক্লিনিক্যাল অর্থ, মান ও গোপনীয়তা বজায় থাকে তা নিশ্চিত করেন।

## একটি ডিজিটাল স্বাস্থ্যসেবা প্রতিষ্ঠানে

- স্বাস্থ্য ডেটাকে তার ক্লিনিক্যাল অর্থ ধরে রাখতে হয়, তাই ডেটা মডেলে SNOMED CT-এর মতো ক্লিনিক্যাল পরিভাষা ও ICD-এর মতো শ্রেণিবিন্যাস ব্যবহার করা হয়।
- সরাসরি পরিচর্যায় ব্যবহৃত ডেটা এবং পরিকল্পনা বা গবেষণায় ব্যবহৃত ডেটার আইনি ভিত্তি ভিন্ন, তাই আর্কিটেক্টরা পৃথকীকরণ, পরিচয় অপসারণ ও নিয়ন্ত্রিত প্রবেশাধিকারের জন্য ডিজাইন করেন।
- ডেটা আসে বিভিন্ন মানের বহু ক্লিনিক্যাল ও পরিচর্যা ব্যবস্থা থেকে, তাই আর্কিটেক্টরা ডেটার মান যাচাই, রোগী মেলানো ও উৎস অনুসরণের জন্য ডিজাইন করেন।
- যৌথ পরিচর্যা রেকর্ড ও ডেটা বিনিময় HL7 FHIR রিসোর্সের মতো সাধারণ মডেল এবং সম্মত জাতীয় বা আন্তর্জাতিক ডেটাসেটের ওপর নির্ভর করে।
- রেকর্ড দীর্ঘ সময় সংরক্ষণ করতে হয়, তাই ডিজাইনে আর্কাইভ ও ঐতিহাসিক ডেটায় প্রবেশের পরিকল্পনা থাকতে হয়।

## UK GDaD PCF-এ ভূমিকার বিবরণ (মূল ইংরেজি)

> A data architect sets the vision for the organisation’s use of data, through data design, to ensure that data is managed properly and meets the organisation’s needs.

## ভূমিকার স্তর

| ব্যান্ড | পদবি | UK GDaD PCF স্তর | যুক্তরাজ্যের সিভিল সার্ভিস গ্রেড | পদ মূল্যায়নের পয়েন্ট |
| --- | --- | --- | --- | --- |
| 8a | [ডেটা আর্কিটেক্ট](#ব্যান্ড-8a-ডেটা-আর্কিটেক্ট) | Data architect | SEO/G7 | 560 |
| 8b | [সিনিয়র ডেটা আর্কিটেক্ট](#ব্যান্ড-8b-সিনিয়র-ডেটা-আর্কিটেক্ট) | Senior data architect | G7/G6 | 613 |
| 8c | [চিফ ডেটা আর্কিটেক্ট](#ব্যান্ড-8c-চিফ-ডেটা-আর্কিটেক্ট) | Chief data architect | G6 | 662 |

## ব্যান্ড 8a: ডেটা আর্কিটেক্ট

**UK GDaD PCF স্তর: Data architect**

> A data architect designs and builds data models to fulfil the strategic data needs of the organisation, as defined by chief data architects.
> 
> At this role level, you will:
> - design, support and provide guidance for the upgrade, management, decommission and archive of data in compliance with data policy
> - provide input into data dictionaries
> - define and maintain the data technology architecture, including metadata, integration and business intelligence or data warehouse architecture

### দায়িত্ব

- প্রয়োজনে ক্লিনিক্যাল পরিভাষা ব্যবহার করে ক্লিনিক্যাল ও পরিচালন ডেটার যৌক্তিক ও ভৌত ডেটা মডেল ডিজাইন করা।
- ওয়্যারহাউস, লেকহাউস ও ইন্টিগ্রেশন স্তরের মতো ডেটা প্রবাহ ও ডেটা প্ল্যাটফর্মের উপাদান ডিজাইন করা।
- আপনার ক্ষেত্রের ডেটাসেটের মেটাডেটা, ডেটা অভিধানের ভুক্তি ও উৎস সংজ্ঞায়িত করা।
- পরিচয় অপসারণ ও প্রবেশাধিকার নিয়ন্ত্রণ ডিজাইন করা যাতে ডেটা কেবল তার আইনসম্মত উদ্দেশ্যে ব্যবহৃত হয়।
- দুর্বল ডেটার কাঠামোগত কারণ সমাধানে ডেটার মান ও ক্লিনিক্যাল কোডিং সহকর্মীদের সাথে কাজ করা।
- ডেটা মডেল ও মানদণ্ড নিয়ে ডেটা ইঞ্জিনিয়ার ও অ্যানালিস্টদের দিকনির্দেশনা দেওয়া।

### দক্ষতা

| দক্ষতা | উৎস | প্রত্যাশিত স্তর | এই স্তরের অর্থ |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../দক্ষতা/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | কার্যকর | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Communicating data](../../দক্ষতা/#communicating-data) | UK GDaD PCF | সচেতনতা | You can:<br>• show an awareness that data needs to be aligned to the needs of the end user<br>• create basic visuals and presentations |
| [Data analysis and synthesis](../../দক্ষতা/#data-analysis-and-synthesis) | UK GDaD PCF | কার্যকর | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../দক্ষতা/#data-governance-data-architect) | UK GDaD PCF | কার্যকর | You can:<br>• understand what data governance is required<br>• take responsibility for the assurance of data solutions and make recommendations to ensure compliance |
| [Data innovation](../../দক্ষতা/#data-innovation) | UK GDaD PCF | সচেতনতা | You can:<br>• develop a basic understanding of an unfamiliar or emerging technology, or a familiar technology in a new data context, with guidance<br>• share what you learn with colleagues, including how it could help deliver more value from data |
| [Data modelling](../../দক্ষতা/#data-modelling) | UK GDaD PCF | কার্যকর | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Data standards](../../দক্ষতা/#data-standards) | UK GDaD PCF | কার্যকর | You can:<br>• use data policies, processes and standards effectively<br>• work with subject matter experts to develop standards, policies and guidance to protect data<br>• monitor compliance with policies and standards in a team and take action if needed<br>• analyse the impact if a standard is breached |
| [Metadata management](../../দক্ষতা/#metadata-management) | UK GDaD PCF | কার্যকর | You can:<br>• use metadata repositories to complete complex tasks such as data and systems integration impact analysis<br>• maintain a metadata repository to ensure information remains accurate and up to date |
| [Problem management](../../দক্ষতা/#problem-management) | UK GDaD PCF | কার্যকর | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Strategic thinking](../../দক্ষতা/#strategic-thinking) | UK GDaD PCF | সচেতনতা | You can:<br>• explain the strategic context of your work and why it is important<br>• support strategic planning in an administrative capacity |
| [Turning business problems into data design](../../দক্ষতা/#turning-business-problems-into-data-design) | UK GDaD PCF | কার্যকর | You can:<br>• design data architecture by dealing with specific business problems and aligning it to enterprise-wide standards and principles<br>• work within the context of well understood architecture, and identify appropriate patterns |
| [স্বাস্থ্য ও পরিচর্যা সেবা বোঝা](../../দক্ষতা/#স্বাস্থ্য-ও-পরিচর্যা-সেবা-বোঝা) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• আপনার কাজ যেসব ক্লিনিক্যাল ও পরিচর্যা কর্মপ্রবাহে সহায়তা করে তা ব্যাখ্যা করতে<br>• ক্লিনিক্যাল ও পরিচর্যা সহকর্মীদের সাথে প্রচলিত স্বাস্থ্যসেবা পরিভাষা সঠিকভাবে ব্যবহার করতে<br>• কোনো পরিবর্তন রোগী পরিচর্যাকে প্রভাবিত করতে পারে কি না তা চিনতে এবং তা জানাতে |
| [ক্লিনিক্যাল পরিভাষা ও শ্রেণিবিন্যাস](../../দক্ষতা/#ক্লিনিক্যাল-পরিভাষা-ও-শ্রেণিবিন্যাস) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• একটি ডেটা আইটেম বা ফর্মের জন্য সঠিক কোড খুঁজে ব্যবহার করতে<br>• পরিভাষা ব্রাউজার ও রেফারেন্স সেট ব্যবহার করতে |
| [স্বাস্থ্য ডেটার আন্তঃকার্যক্ষমতা](../../দক্ষতা/#স্বাস্থ্য-ডেটার-আন্তঃকার্যক্ষমতা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• FHIR, HL7 সংস্করণ 2 ও বার্তা বিনিময়ের ধরন ব্যবহার করে ইন্টিগ্রেশন ডিজাইন ও তৈরি করতে<br>• FHIR রিসোর্স ও বাস্তবায়ন নির্দেশিকা লিখতে ও প্রোফাইল করতে<br>• ব্যবস্থাগুলোর মধ্যে জটিল ম্যাপিং ও ডেটার মানের সমস্যা সমাধান করতে |
| [তথ্য সুশাসন ও ডেটা সুরক্ষা](../../দক্ষতা/#তথ্য-সুশাসন-ও-ডেটা-সুরক্ষা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• ডেটা সুরক্ষা প্রভাব মূল্যায়ন ও তথ্য বিনিময় চুক্তির নেতৃত্ব দিতে<br>• আইনি ভিত্তি, সম্মতি, গোপনীয়তা ও সংরক্ষণ নিয়ে দলগুলোকে পরামর্শ দিতে<br>• ঘটনা তদন্ত করতে এবং উন্নতির সুপারিশ করতে |
| [ডেটার মান ব্যবস্থাপনা](../../দক্ষতা/#ডেটার-মান-ব্যবস্থাপনা) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• ডেটার মান যাচাই চালাতে এবং ভুল সংশোধন করতে<br>• সহকর্মীদের কাছে ডেটার মানের প্রতিবেদন ব্যাখ্যা করতে |

### সাধারণ যোগ্যতা ও অভিজ্ঞতা

- স্নাতকোত্তর ডিগ্রির সমমান স্তরে ডেটা মডেলিং ও ডেটা প্ল্যাটফর্ম ডিজাইনের উল্লেখযোগ্য অভিজ্ঞতা।

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
| 8 | আর্থিক ও ভৌত সম্পদের দায়িত্ব | 2 | 12 |
| 9 | জনবলের দায়িত্ব | 3 | 21 |
| 10 | তথ্য সম্পদের দায়িত্ব | 5 | 34 |
| 11 | গবেষণা ও উন্নয়নের দায়িত্ব | 3 | 21 |
| 12 | কাজের স্বাধীনতা | 5 | 45 |
| 13 | শারীরিক পরিশ্রম | 1 | 3 |
| 14 | মানসিক পরিশ্রম | 4 | 18 |
| 15 | মানসিক চাপ | 1 | 5 |
| 16 | কাজের পরিবেশ | 2 | 7 |
| | **মোট** | | **560** (ব্যান্ড 8a: 540–584) |

UK GDaD PCF গ্রেডের প্রস্তাবিত ব্যান্ডের (ব্যান্ড 7) চেয়ে উঁচুতে রাখা হয়েছে: স্বাস্থ্য খাতের বিজ্ঞাপনে এই ভূমিকা ব্যান্ড 8a-তে থাকে। পরিকল্পনা, নীতি ও কাজের স্বাধীনতা ব্যান্ড 7 প্রোফাইলের ওপরে স্কোর করা হয়, কারণ পদটি বহু সেবায় ব্যবহৃত ডেটা প্ল্যাটফর্ম ও নিয়ন্ত্রণ ডিজাইন করে।

## ব্যান্ড 8b: সিনিয়র ডেটা আর্কিটেক্ট

**UK GDaD PCF স্তর: Senior data architect**

> A senior data architect delivers the vision for the organisation as set by the chief data architect.
> 
> At this role level, you will:
> - design data models and metadata systems
> - help chief data architects to interpret an organisation’s needs
> - provide oversight and advice to other data architects who are designing and producing data artefacts
> - design and support the management of data dictionaries
> - make sure that your teams are working to the standards set for the organisation by the chief data architects
> - work with technical architects to make sure that an organisation’s systems are designed in accordance with the appropriate data architecture

### দায়িত্ব

- যৌথ পরিচর্যা রেকর্ড বা বিশ্লেষণ প্ল্যাটফর্মের মতো একটি প্রধান ক্ষেত্রের ডেটা আর্কিটেকচার ডিজাইন করা।
- দলগুলোর ডেটা ডিজাইন প্রতিষ্ঠানের ডেটা মানদণ্ড ও মডেল অনুসরণ করে তা নিশ্চিত করা।
- মানদণ্ড, নিয়ন্ত্রণ ও ডেটা বিনিময় চুক্তিসহ অংশীদার প্রতিষ্ঠানের সাথে ডেটা কীভাবে বিনিময় হবে তা ডিজাইন করা।
- নতুন ডিজাইনের ডেটা ঝুঁকি নিয়ে তথ্য সুশাসন ও ক্লিনিক্যাল নিরাপত্তা সহকর্মীদের পরামর্শ দেওয়া।
- ডেটা আর্কিটেক্টদের কাজ পর্যালোচনা ও দিকনির্দেশনা দেওয়া।

### দক্ষতা

| দক্ষতা | উৎস | প্রত্যাশিত স্তর | এই স্তরের অর্থ |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../দক্ষতা/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Communicating data](../../দক্ষতা/#communicating-data) | UK GDaD PCF | কার্যকর | You can:<br>• understand the appropriate media to communicate findings<br>• shape communications for the audience |
| [Data analysis and synthesis](../../দক্ষতা/#data-analysis-and-synthesis) | UK GDaD PCF | কার্যকর | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../দক্ষতা/#data-governance-data-architect) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• evolve and define data governance<br>• take responsibility for supporting and collaborating around wider governance<br>• assure and integrate data services to meet the needs of multiple business services<br>• work proactively to ensure the organisation designs architecture that considers data |
| [Data innovation](../../দক্ষতা/#data-innovation) | UK GDaD PCF | কার্যকর | You can:<br>• experiment with unfamiliar and emerging technologies, or familiar technologies in new data contexts, with guidance<br>• share what you learn with the team, explaining potential benefits, risks, and practical considerations<br>• identify opportunities to apply technology to improve data processes or outcomes in an operational setting or the wider organisation |
| [Data modelling](../../দক্ষতা/#data-modelling) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• produce relevant data models across multiple subject areas<br>• explain which models to use for which purpose<br>• understand industry-recognised data modelling patterns and standards, and when to apply them<br>• compare and align different data models |
| [Data standards](../../দক্ষতা/#data-standards) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• create data standards for different subjects and ensure senior leaders understand them<br>• work with subject matter experts across the organisation to introduce data standards best practice<br>• monitor compliance with policies and standards in the organisation<br>• make recommendations about how the organisation should resolve breaches of standards |
| [Metadata management](../../দক্ষতা/#metadata-management) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../দক্ষতা/#problem-management) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• ensure that the right actions are taken to investigate, resolve and anticipate problems<br>• co-ordinate the team to investigate problems, implement solutions and take preventive measures |
| [Strategic thinking](../../দক্ষতা/#strategic-thinking) | UK GDaD PCF | কার্যকর | You can:<br>• work within a strategic context and communicate how activities meet strategic goals<br>• contribute to the development of strategy and policies |
| [Turning business problems into data design](../../দক্ষতা/#turning-business-problems-into-data-design) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• design data architecture that deals with problems spanning different business areas<br>• identify links between problems to devise common solutions<br>• work across multiple subject areas, or a single large or complicated subject area<br>• produce appropriate patterns |
| [স্বাস্থ্য ও পরিচর্যা সেবা বোঝা](../../দক্ষতা/#স্বাস্থ্য-ও-পরিচর্যা-সেবা-বোঝা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• বিভিন্ন প্রতিষ্ঠানজুড়ে পরিচর্যা পথে একটি সেবা কীভাবে খাপ খায় তা বিশ্লেষণ করতে<br>• ডিজিটাল সেবা গড়তে চিকিৎসক, পরিচর্যাকর্মী ও রোগীদের সাথে কাজ করতে<br>• ডিজিটাল সিদ্ধান্তের প্রভাব পরিচর্যা, নিরাপত্তা ও কর্মীদের কাজের চাপের ওপর ব্যাখ্যা করতে |
| [ক্লিনিক্যাল পরিভাষা ও শ্রেণিবিন্যাস](../../দক্ষতা/#ক্লিনিক্যাল-পরিভাষা-ও-শ্রেণিবিন্যাস) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• ক্লিনিক্যাল পরিভাষা ব্যবহার করে ডেটা মডেল ও রেফারেন্স সেট ডিজাইন করতে<br>• পরিভাষা ও শ্রেণিবিন্যাসের মধ্যে ম্যাপিং করতে এবং ম্যাপিংয়ের সীমাবদ্ধতা ব্যাখ্যা করতে<br>• প্রোডাক্ট ও বিশ্লেষণে পরিভাষার ব্যবহার নিয়ে দলগুলোকে পরামর্শ দিতে |
| [স্বাস্থ্য ডেটার আন্তঃকার্যক্ষমতা](../../দক্ষতা/#স্বাস্থ্য-ডেটার-আন্তঃকার্যক্ষমতা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• FHIR, HL7 সংস্করণ 2 ও বার্তা বিনিময়ের ধরন ব্যবহার করে ইন্টিগ্রেশন ডিজাইন ও তৈরি করতে<br>• FHIR রিসোর্স ও বাস্তবায়ন নির্দেশিকা লিখতে ও প্রোফাইল করতে<br>• ব্যবস্থাগুলোর মধ্যে জটিল ম্যাপিং ও ডেটার মানের সমস্যা সমাধান করতে |
| [তথ্য সুশাসন ও ডেটা সুরক্ষা](../../দক্ষতা/#তথ্য-সুশাসন-ও-ডেটা-সুরক্ষা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• ডেটা সুরক্ষা প্রভাব মূল্যায়ন ও তথ্য বিনিময় চুক্তির নেতৃত্ব দিতে<br>• আইনি ভিত্তি, সম্মতি, গোপনীয়তা ও সংরক্ষণ নিয়ে দলগুলোকে পরামর্শ দিতে<br>• ঘটনা তদন্ত করতে এবং উন্নতির সুপারিশ করতে |
| [ডেটার মান ব্যবস্থাপনা](../../দক্ষতা/#ডেটার-মান-ব্যবস্থাপনা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• ডেটার মানের নিয়ম ও পরিমাপ সংজ্ঞায়িত করতে<br>• দুর্বল মানের মূল কারণ সমাধানে ডেটা সরবরাহকারীদের সাথে কাজ করতে |
| [ক্লিনিক্যাল ঝুঁকি ব্যবস্থাপনা](../../দক্ষতা/#ক্লিনিক্যাল-ঝুঁকি-ব্যবস্থাপনা) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• বিপদ চিহ্নিতকরণ কর্মশালায় অংশ নিতে এবং বিপদ লগে অবদান রাখতে<br>• আপনার কাজের জন্য ক্লিনিক্যাল ঝুঁকি ব্যবস্থাপনা প্রক্রিয়া অনুসরণ করতে<br>• ক্লিনিক্যাল নিরাপত্তা কেসের জন্য প্রমাণ দিতে, যেমন পরীক্ষার ফলাফল |
| [জনবল ব্যবস্থাপনা](../../দক্ষতা/#জনবল-ব্যবস্থাপনা) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• দৈনন্দিন কাজ তত্ত্বাবধান করতে এবং মতামত দিতে<br>• নিয়োগ ও পরিচিতিমূলক কাজে অংশ নিতে<br>• নিয়মিত একান্ত আলোচনা করতে |

### সাধারণ যোগ্যতা ও অভিজ্ঞতা

- জটিল প্রতিষ্ঠানের ডেটা আর্কিটেকচারে ব্যাপক অভিজ্ঞতা।

### ব্যান্ডের রূপরেখা

- **জ্ঞান:** একাধিক শাখা বা একটি বড় সেবায় বিশেষজ্ঞ জ্ঞান।
- **স্বাধীনতা:** একটি বড় ক্ষেত্রের নীতি ও কৌশল গঠন করেন।
- **পরিসর:** একাধিক সেবা বা দল, অথবা প্রিন্সিপাল স্তরের একটি শাখা।
- **নেতৃত্ব:** ব্যবস্থাপকদের পরিচালনা করেন, অথবা একটি শাখার প্রধান কর্তৃপক্ষ।
- **জবাবদিহি:** একাধিক সেবা, তাদের কর্মী ও বাজেট।

### পদ মূল্যায়ন (দৃষ্টান্তমূলক)

| # | উপাদান | স্তর | পয়েন্ট |
| --- | --- | --- | --- |
| 1 | যোগাযোগ ও সম্পর্ক স্থাপনের দক্ষতা | 5 | 45 |
| 2 | জ্ঞান, প্রশিক্ষণ ও অভিজ্ঞতা | 8 | 240 |
| 3 | বিশ্লেষণ ও বিচার-বিবেচনার দক্ষতা | 5 | 60 |
| 4 | পরিকল্পনা ও সংগঠনের দক্ষতা | 4 | 42 |
| 5 | শারীরিক দক্ষতা | 2 | 15 |
| 6 | রোগী ও সেবাগ্রহীতার পরিচর্যার দায়িত্ব | 1 | 4 |
| 7 | নীতি ও সেবা উন্নয়নের দায়িত্ব | 4 | 32 |
| 8 | আর্থিক ও ভৌত সম্পদের দায়িত্ব | 3 | 21 |
| 9 | জনবলের দায়িত্ব | 3 | 21 |
| 10 | তথ্য সম্পদের দায়িত্ব | 5 | 34 |
| 11 | গবেষণা ও উন্নয়নের দায়িত্ব | 3 | 21 |
| 12 | কাজের স্বাধীনতা | 5 | 45 |
| 13 | শারীরিক পরিশ্রম | 1 | 3 |
| 14 | মানসিক পরিশ্রম | 4 | 18 |
| 15 | মানসিক চাপ | 1 | 5 |
| 16 | কাজের পরিবেশ | 2 | 7 |
| | **মোট** | | **613** (ব্যান্ড 8b: 585–629) |

## ব্যান্ড 8c: চিফ ডেটা আর্কিটেক্ট

**UK GDaD PCF স্তর: Chief data architect**

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

### দায়িত্ব

- প্রতিষ্ঠানের ডেটা কৌশলের সাথে সামঞ্জস্য রেখে এর ডেটা আর্কিটেকচারের দৃষ্টিভঙ্গি ও রোডম্যাপ নির্ধারণ করা।
- প্রতিষ্ঠানের এন্টারপ্রাইজ ডেটা মডেল, ডেটা মানদণ্ড ও ডেটা অভিধানের দায়িত্ব নেওয়া।
- ডেটা আর্কিটেকচার, ঝুঁকি ও বিনিয়োগ নিয়ে নির্বাহী দল ও ডেটা সুশাসন সংস্থাকে পরামর্শ দেওয়া।
- আন্তঃপ্রাতিষ্ঠানিক ডেটা মানদণ্ড ও আন্তঃকার্যক্ষমতার কাজে প্রতিষ্ঠানের প্রতিনিধিত্ব করা।
- ডেটা আর্কিটেকচার চর্চার নেতৃত্ব দেওয়া এবং এর মানুষদের উন্নয়ন করা।

### দক্ষতা

| দক্ষতা | উৎস | প্রত্যাশিত স্তর | এই স্তরের অর্থ |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../দক্ষতা/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Communicating data](../../দক্ষতা/#communicating-data) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• turn complex data into clear and well understood solutions, which can be acted upon<br>• share data communication skills with the team and organisation<br>• understand and communicate different options, taking into account risks and uncertainties |
| [Data analysis and synthesis](../../দক্ষতা/#data-analysis-and-synthesis) | UK GDaD PCF | কার্যকর | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../দক্ষতা/#data-governance-data-architect) | UK GDaD PCF | বিশেষজ্ঞ | You can:<br>• ensure data governance supports changes to the organisational strategy<br>• align data governance with wider governance (for example, budget)<br>• assure corporate services by understanding important risks and providing mitigation through assurance mechanisms |
| [Data innovation](../../দক্ষতা/#data-innovation) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• test and evaluate the feasibility of unfamiliar and emerging technologies, or familiar technologies in new data contexts<br>• share what you learn with the organisation, explaining potential benefits, risks, and practical considerations<br>• recommend, design and implement innovative data solutions based on organisation objectives, user needs, and operational constraints |
| [Data modelling](../../দক্ষতা/#data-modelling) | UK GDaD PCF | বিশেষজ্ঞ | You can:<br>• understand the concepts and principles of data modelling and can produce relevant data models<br>• work across government and industry, recognising opportunities for the reuse and alignment of data models in different organisations<br>• design the method to categorise data models within an organisation |
| [Data standards](../../দক্ষতা/#data-standards) | UK GDaD PCF | বিশেষজ্ঞ | You can:<br>• create data standards for the organisation<br>• advocate for, and oversee compliance with, data policies and standards<br>• decide where standards need to be set across the organisation, and how to set them in the wider context of government |
| [Metadata management](../../দক্ষতা/#metadata-management) | UK GDaD PCF | বিশেষজ্ঞ | You can:<br>• identify how metadata repositories can support different areas of the organisation<br>• communicate the value of metadata repositories<br>• set up robust governance processes to keep repositories up to date |
| [Problem management](../../দক্ষতা/#problem-management) | UK GDaD PCF | বিশেষজ্ঞ | You can:<br>• anticipate problems and defend against them at the right time<br>• understand how a problem fits into the larger picture<br>• identify and describe problems, and help others to describe them<br>• build problem-solving capabilities in others |
| [Strategic thinking](../../দক্ষতা/#strategic-thinking) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• define strategies and policies, providing guidance to others on working in the strategic context<br>• evaluate current strategies to ensure business requirements are being met and exceeded where possible |
| [Turning business problems into data design](../../দক্ষতা/#turning-business-problems-into-data-design) | UK GDaD PCF | বিশেষজ্ঞ | You can:<br>• design data architecture that deals with problems across the enterprise<br>• work across all organisational subject areas and internal and external programmes |
| [স্বাস্থ্য ও পরিচর্যা সেবা বোঝা](../../দক্ষতা/#স্বাস্থ্য-ও-পরিচর্যা-সেবা-বোঝা) | এই রেফারেন্স | বিশেষজ্ঞ | আপনি পারেন:<br>• স্বাস্থ্য ও পরিচর্যা ব্যবস্থার গভীর জ্ঞান ব্যবহার করে প্রতিষ্ঠানের কৌশল গড়তে<br>• স্বাস্থ্য ও পরিচর্যা অংশীদার ও নেতাদের কাছে প্রতিষ্ঠানের প্রতিনিধিত্ব করতে<br>• নীতি ও সেবার পরিবর্তন ডিজিটাল সেবা ও পরিচর্যাকে কীভাবে প্রভাবিত করবে তা আগে থেকে অনুমান করতে |
| [ক্লিনিক্যাল পরিভাষা ও শ্রেণিবিন্যাস](../../দক্ষতা/#ক্লিনিক্যাল-পরিভাষা-ও-শ্রেণিবিন্যাস) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• ক্লিনিক্যাল পরিভাষা ব্যবহার করে ডেটা মডেল ও রেফারেন্স সেট ডিজাইন করতে<br>• পরিভাষা ও শ্রেণিবিন্যাসের মধ্যে ম্যাপিং করতে এবং ম্যাপিংয়ের সীমাবদ্ধতা ব্যাখ্যা করতে<br>• প্রোডাক্ট ও বিশ্লেষণে পরিভাষার ব্যবহার নিয়ে দলগুলোকে পরামর্শ দিতে |
| [স্বাস্থ্য ডেটার আন্তঃকার্যক্ষমতা](../../দক্ষতা/#স্বাস্থ্য-ডেটার-আন্তঃকার্যক্ষমতা) | এই রেফারেন্স | বিশেষজ্ঞ | আপনি পারেন:<br>• প্রতিষ্ঠানের জন্য আন্তঃকার্যক্ষমতার মানদণ্ড ও কৌশল নির্ধারণ করতে<br>• জাতীয় বা আন্তঃপ্রাতিষ্ঠানিক মানদণ্ড কাজের নেতৃত্ব দিতে<br>• বহু ব্যবস্থাজুড়ে গুরুত্বপূর্ণ ইন্টিগ্রেশনের ডিজাইন নিশ্চিত করতে |
| [তথ্য সুশাসন ও ডেটা সুরক্ষা](../../দক্ষতা/#তথ্য-সুশাসন-ও-ডেটা-সুরক্ষা) | এই রেফারেন্স | বিশেষজ্ঞ | আপনি পারেন:<br>• তথ্য সুশাসনের নীতি ও কৌশল নির্ধারণ করতে<br>• তথ্য ঝুঁকি ও সম্মতি নিয়ে পরিচালনা পর্ষদকে পরামর্শ দিতে<br>• নিয়ন্ত্রক ও অংশীদারদের কাছে প্রতিষ্ঠানের প্রতিনিধিত্ব করতে |
| [ডেটার মান ব্যবস্থাপনা](../../দক্ষতা/#ডেটার-মান-ব্যবস্থাপনা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• ডেটার মানের নিয়ম ও পরিমাপ সংজ্ঞায়িত করতে<br>• দুর্বল মানের মূল কারণ সমাধানে ডেটা সরবরাহকারীদের সাথে কাজ করতে |
| [ক্লিনিক্যাল ঝুঁকি ব্যবস্থাপনা](../../দক্ষতা/#ক্লিনিক্যাল-ঝুঁকি-ব্যবস্থাপনা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• একটি প্রোডাক্ট বা পরিবর্তনের জন্য বিপদ চিহ্নিতকরণ ও ঝুঁকি মূল্যায়নের নেতৃত্ব দিতে<br>• বিপদ লগ ও ক্লিনিক্যাল নিরাপত্তা কেস প্রতিবেদন লিখতে ও হালনাগাদ রাখতে<br>• প্রোডাক্ট দলের সাথে ঝুঁকি নিয়ন্ত্রণে একমত হতে এবং সেগুলো কাজ করে কি না যাচাই করতে<br>• ক্লিনিক্যাল ঝুঁকি ব্যবস্থাপনার মানদণ্ড প্রয়োগে দলগুলোকে পরামর্শ দিতে |
| [জনবল ব্যবস্থাপনা](../../দক্ষতা/#জনবল-ব্যবস্থাপনা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• একটি দলের সরাসরি ব্যবস্থাপনা করতে, লক্ষ্য নির্ধারণ ও মূল্যায়ন পরিচালনা করতে<br>• সুস্থতায় সহায়তা করতে এবং উপস্থিতি, কর্মদক্ষতা ও আচরণ পরিচালনা করতে<br>• দলের উন্নয়ন ও উত্তরসূরি পরিকল্পনা করতে |

### সাধারণ যোগ্যতা ও অভিজ্ঞতা

- বিভিন্ন প্রতিষ্ঠানজুড়ে ডেটা আর্কিটেকচারের নেতৃত্বে ব্যাপক অভিজ্ঞতা।

### ব্যান্ডের রূপরেখা

- **জ্ঞান:** বিশেষজ্ঞ জ্ঞান, এবং প্রতিষ্ঠান ও খাত সম্পর্কে বিস্তৃত ধারণা।
- **স্বাধীনতা:** একটি কার্যক্রমের কৌশল ঠিক করেন; একজন পরিচালকের কাছে জবাবদিহি করেন।
- **পরিসর:** একটি কার্যক্রম বা বিভাগ।
- **নেতৃত্ব:** একাধিক ব্যবস্থাপনা স্তরের মাধ্যমে একটি কার্যক্রমের নেতৃত্ব দেন।
- **জবাবদিহি:** একটি কার্যক্রমের কর্মদক্ষতা, জনবল ও বাজেট।

### পদ মূল্যায়ন (দৃষ্টান্তমূলক)

| # | উপাদান | স্তর | পয়েন্ট |
| --- | --- | --- | --- |
| 1 | যোগাযোগ ও সম্পর্ক স্থাপনের দক্ষতা | 6 | 60 |
| 2 | জ্ঞান, প্রশিক্ষণ ও অভিজ্ঞতা | 8 | 240 |
| 3 | বিশ্লেষণ ও বিচার-বিবেচনার দক্ষতা | 5 | 60 |
| 4 | পরিকল্পনা ও সংগঠনের দক্ষতা | 5 | 60 |
| 5 | শারীরিক দক্ষতা | 2 | 15 |
| 6 | রোগী ও সেবাগ্রহীতার পরিচর্যার দায়িত্ব | 1 | 4 |
| 7 | নীতি ও সেবা উন্নয়নের দায়িত্ব | 5 | 45 |
| 8 | আর্থিক ও ভৌত সম্পদের দায়িত্ব | 3 | 21 |
| 9 | জনবলের দায়িত্ব | 3 | 21 |
| 10 | তথ্য সম্পদের দায়িত্ব | 6 | 46 |
| 11 | গবেষণা ও উন্নয়নের দায়িত্ব | 2 | 12 |
| 12 | কাজের স্বাধীনতা | 5 | 45 |
| 13 | শারীরিক পরিশ্রম | 1 | 3 |
| 14 | মানসিক পরিশ্রম | 4 | 18 |
| 15 | মানসিক চাপ | 1 | 5 |
| 16 | কাজের পরিবেশ | 2 | 7 |
| | **মোট** | | **662** (ব্যান্ড 8c: 630–674) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
