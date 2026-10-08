# টেকনিক্যাল আর্কিটেক্ট

> এটি একটি সাধারণ ডিজিটাল স্বাস্থ্যসেবা প্রতিষ্ঠানের জন্য একটি দৃষ্টান্তমূলক রেফারেন্স প্রোফাইল। এটি কোনো নিয়োগকর্তার আনুষ্ঠানিক পদের বিবরণ নয়, এবং এর পদ মূল্যায়নের পয়েন্ট কোনো আনুষ্ঠানিক মূল্যায়ন নয়।

> এই লেখাটি একটি কৃত্রিম বুদ্ধিমত্তা সহকারী ইংরেজি থেকে অনুবাদ করেছে, এবং কোনো মাতৃভাষী এখনও এটি পর্যালোচনা করেননি। যুক্তরাজ্য (UK) সরকারের ডিজিটাল ও ডেটা পেশা সক্ষমতা কাঠামো (UK GDaD PCF) এবং ESCO থেকে নেওয়া উদ্ধৃতিগুলো ইংরেজিতেই রাখা হয়েছে।

**পরিবার:** [আর্কিটেকচার](../../#আর্কিটেকচার)  
**ব্যান্ড:** 6, 7, 8a, 8b, 8c  
**UK GDaD PCF ভূমিকা:** [Technical architect](https://understand-digital-data-roles-skills.service.gov.uk/role/technical-architect/)  
**ESCO পেশা:** [software architect](http://data.europa.eu/esco/occupation/d0aa0792-4345-474b-9365-686cf4869d2e) (ISCO-08 2512); [cloud architect](http://data.europa.eu/esco/occupation/2fb96c6c-8d0b-4ef0-b1ee-3e493305e4eb) (ISCO-08 2512)

## সারসংক্ষেপ

টেকনিক্যাল আর্কিটেক্টরা প্রতিষ্ঠানের ডিজিটাল স্বাস্থ্যসেবার কারিগরি কাঠামো ডিজাইন করেন: উপাদান, প্ল্যাটফর্ম, হোস্টিং, ইন্টিগ্রেশনের ধরন, এবং নিরাপত্তা, কর্মদক্ষতা ও স্থিতিস্থাপকতার মতো অ-কার্যকরী গুণ। তাঁরা ডেভেলপার ও ডেভঅপস ইঞ্জিনিয়ারদের সাথে নিবিড়ভাবে কাজ করেন, ডেলিভারি দলকে কারিগরি নেতৃত্ব দেন, এবং সেবাগুলো টেকসই ও নিরাপদে চালানোর উপযোগী করে তৈরি হয় তা নিশ্চিত করেন।

## একটি ডিজিটাল স্বাস্থ্যসেবা প্রতিষ্ঠানে

- ক্লিনিক্যাল সেবার প্রায়ই উচ্চ প্রাপ্যতা ও দ্রুত পুনরুদ্ধার দরকার, তাই কারিগরি ডিজাইনে ব্যর্থতা ও সীমিত পরিচালনার পরিকল্পনা থাকতে হবে।
- ডিজাইনকে স্বাভাবিকভাবেই এনক্রিপশন, প্রবেশাধিকার নিয়ন্ত্রণ ও নিরীক্ষার মাধ্যমে গোপন স্বাস্থ্য তথ্য রক্ষা করতে হবে।
- সেবাগুলো প্রায়ই HL7 FHIR API ও বার্তা বিনিময়ের মাধ্যমে বহু ক্লিনিক্যাল ব্যবস্থা ও যৌথ প্ল্যাটফর্মের সাথে যুক্ত হয়, তাই ইন্টিগ্রেশনের ধরন ডিজাইনের কেন্দ্রে থাকে।
- ক্যাশিং, পুনঃচেষ্টা ও সময় সামলানোর মতো কারিগরি ডিজাইনের পছন্দ ক্লিনিক্যাল বিপদ ঘটাতে পারে, তাই আর্কিটেক্টরা নিরাপত্তা কেসে অবদান রাখেন।
- পুরোনো ক্লিনিক্যাল ব্যবস্থা ও মেডিক্যাল ডিভাইস প্রযুক্তি, নেটওয়ার্কিং ও হোস্টিংয়ের পছন্দ সীমিত করতে পারে।

## UK GDaD PCF-এ ভূমিকার বিবরণ (মূল ইংরেজি)

> A technical architect provides technical leadership and architectural design.

## ভূমিকার স্তর

| ব্যান্ড | পদবি | UK GDaD PCF স্তর | যুক্তরাজ্যের সিভিল সার্ভিস গ্রেড | পদ মূল্যায়নের পয়েন্ট |
| --- | --- | --- | --- | --- |
| 6 | [অ্যাসোসিয়েট টেকনিক্যাল আর্কিটেক্ট](#ব্যান্ড-6-অ্যাসোসিয়েট-টেকনিক্যাল-আর্কিটেক্ট) | Associate technical architect | EO/HEO | 412 |
| 7 | [টেকনিক্যাল আর্কিটেক্ট](#ব্যান্ড-7-টেকনিক্যাল-আর্কিটেক্ট) | Technical architect | SEO/G7 | 496 |
| 8a | [সিনিয়র টেকনিক্যাল আর্কিটেক্ট](#ব্যান্ড-8a-সিনিয়র-টেকনিক্যাল-আর্কিটেক্ট) | Senior technical architect | SEO/G7 | 560 |
| 8b | [লিড টেকনিক্যাল আর্কিটেক্ট](#ব্যান্ড-8b-লিড-টেকনিক্যাল-আর্কিটেক্ট) | Lead technical architect | G7/G6 | 613 |
| 8c | [প্রিন্সিপাল টেকনিক্যাল আর্কিটেক্ট](#ব্যান্ড-8c-প্রিন্সিপাল-টেকনিক্যাল-আর্কিটেক্ট) | Principal technical architect | G6 | 662 |

## ব্যান্ড 6: অ্যাসোসিয়েট টেকনিক্যাল আর্কিটেক্ট

**UK GDaD PCF স্তর: Associate technical architect**

> An associate technical architect supports technical architects in putting forward designs as solutions to technology challenges, usually under supervision.
> 
> At this role level, you will:
> - work closely with developers when designing appropriate solutions
> - have an understanding of the overall strategy and how your work supports it

### দায়িত্ব

- কারিগরি ডায়াগ্রাম আঁকা এবং বিদ্যমান সেবার উপাদান, হোস্টিং ও ইন্টিগ্রেশন নথিভুক্ত করা।
- নির্দেশনায় প্রযুক্তির বিকল্প গবেষণা করা এবং এর সুবিধা-অসুবিধা সংক্ষেপ করা।
- বিল্ডগুলো সম্মত ডিজাইন ও প্যাটার্ন অনুসরণ করে কি না যাচাই করতে ডেভেলপারদের সাথে কাজ করা।
- কারিগরি সিদ্ধান্ত রেকর্ড করা এবং ডিজাইন নথি হালনাগাদ রাখা।

### দক্ষতা

| দক্ষতা | উৎস | প্রত্যাশিত স্তর | এই স্তরের অর্থ |
| --- | --- | --- | --- |
| [Architect for the whole context](../../দক্ষতা/#architect-for-the-whole-context) | UK GDaD PCF | সচেতনতা | You can:<br>• identify relevant information that can inform your architectural work, such as strategies, roadmaps, policies and technical trends<br>• understand how your work supports the team in enabling change​ |
| [Architecture communication](../../দক্ষতা/#architecture-communication) | UK GDaD PCF | সচেতনতা | You can:<br>• show an awareness of different ways of creating architecture representations for a limited audience, including technical and non-technical stakeholders<br>• gather and explain information to be used in architecture representations |
| [Community collaboration](../../দক্ষতা/#community-collaboration) | UK GDaD PCF | সচেতনতা | You can:<br>• understand the work of others and the importance of team dynamics, collaboration and feedback |
| [Making architectural decisions](../../দক্ষতা/#making-architectural-decisions) | UK GDaD PCF | সচেতনতা | You can:<br>• describe the reasoning behind architectural design decisions<br>• gather information to inform decisions<br>• understand architectural governance and assurance relevant to your work |
| [Strategy design](../../দক্ষতা/#strategy-design) | UK GDaD PCF | সচেতনতা | You can:<br>• explain how organisational objectives link to designing strategy<br>• describe the purpose and application of strategy, standards, patterns, policies, roadmaps, vision, and mission statements |
| [Technical design throughout the life cycle](../../দক্ষতা/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | কার্যকর | You can:<br>• create technical designs characterised by managed levels of risk, impact, and complexity<br>• provide guidance and support to teams using technical designs throughout the life cycle<br>• adapt a technical design if needed during delivery<br>• work with well-understood technology and identify appropriate patterns |
| [স্বাস্থ্য ও পরিচর্যা সেবা বোঝা](../../দক্ষতা/#স্বাস্থ্য-ও-পরিচর্যা-সেবা-বোঝা) | এই রেফারেন্স | সচেতনতা | আপনি পারেন:<br>• স্বাস্থ্য ও পরিচর্যা ব্যবস্থার প্রধান অংশগুলো এবং প্রতিষ্ঠান যেসব সেবায় সহায়তা করে তা বর্ণনা করতে<br>• আপনার কাজে রোগীর নিরাপত্তা ও গোপনীয়তা কেন গুরুত্বপূর্ণ তা ব্যাখ্যা করতে |
| [স্বাস্থ্য ডেটার আন্তঃকার্যক্ষমতা](../../দক্ষতা/#স্বাস্থ্য-ডেটার-আন্তঃকার্যক্ষমতা) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• FHIR রিসোর্স, প্রোফাইল ও API পড়তে ও ব্যবহার করতে<br>• নির্দেশনায় সরল ইন্টিগ্রেশন তৈরি বা পরীক্ষা করতে<br>• একটি নির্দিষ্টকরণের সাথে বার্তা মিলিয়ে দেখতে |
| [তথ্য সুশাসন ও ডেটা সুরক্ষা](../../দক্ষতা/#তথ্য-সুশাসন-ও-ডেটা-সুরক্ষা) | এই রেফারেন্স | সচেতনতা | আপনি পারেন:<br>• ব্যক্তিগত ও স্বাস্থ্য তথ্য সামলানোর জন্য প্রতিষ্ঠানের নিয়ম অনুসরণ করতে<br>• ডেটা লঙ্ঘন বা প্রায়-দুর্ঘটনা চিনতে ও জানাতে |
| [ক্লিনিক্যাল ঝুঁকি ব্যবস্থাপনা](../../দক্ষতা/#ক্লিনিক্যাল-ঝুঁকি-ব্যবস্থাপনা) | এই রেফারেন্স | সচেতনতা | আপনি পারেন:<br>• স্বাস্থ্য আইটি ব্যবস্থা কীভাবে রোগীদের ক্ষতি করতে পারে তা ব্যাখ্যা করতে, যেমন ভুল, অনুপস্থিত বা বিলম্বিত তথ্যের মাধ্যমে<br>• সম্ভাব্য ক্লিনিক্যাল নিরাপত্তা সমস্যা সঠিক পথে জানাতে |

### সাধারণ যোগ্যতা ও অভিজ্ঞতা

- কম্পিউটিং বা সংশ্লিষ্ট বিষয়ে ডিগ্রি, বা সফটওয়্যার বা অবকাঠামো প্রকৌশলে সমমানের অভিজ্ঞতা।
- স্নাতকোত্তর ডিপ্লোমা স্তরে বা সমমানের অভিজ্ঞতায় কারিগরি ডিজাইনের বিশেষায়িত জ্ঞান।

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
| 5 | শারীরিক দক্ষতা | 2 | 15 |
| 6 | রোগী ও সেবাগ্রহীতার পরিচর্যার দায়িত্ব | 1 | 4 |
| 7 | নীতি ও সেবা উন্নয়নের দায়িত্ব | 3 | 21 |
| 8 | আর্থিক ও ভৌত সম্পদের দায়িত্ব | 1 | 5 |
| 9 | জনবলের দায়িত্ব | 1 | 5 |
| 10 | তথ্য সম্পদের দায়িত্ব | 5 | 34 |
| 11 | গবেষণা ও উন্নয়নের দায়িত্ব | 2 | 12 |
| 12 | কাজের স্বাধীনতা | 4 | 32 |
| 13 | শারীরিক পরিশ্রম | 1 | 3 |
| 14 | মানসিক পরিশ্রম | 3 | 12 |
| 15 | মানসিক চাপ | 1 | 5 |
| 16 | কাজের পরিবেশ | 2 | 7 |
| | **মোট** | | **412** (ব্যান্ড 6: 396–465) |

UK GDaD PCF গ্রেডের প্রস্তাবিত ব্যান্ডের (ব্যান্ড 5) চেয়ে উঁচুতে রাখা হয়েছে: স্বাস্থ্য খাতের বিজ্ঞাপনে এই ভূমিকা ব্যান্ড 6-এ থাকে। জ্ঞান স্নাতকোত্তর ডিপ্লোমা স্তরে স্কোর করা হয়, এবং তথ্য সম্পদ লেভেল 5-এ, কারণ পদটি প্রধান তথ্য ব্যবস্থার অংশ ডিজাইন করে।

## ব্যান্ড 7: টেকনিক্যাল আর্কিটেক্ট

**UK GDaD PCF স্তর: Technical architect**

> A technical architect is responsible for the design and build of technical architecture.
> 
> At this role level, you will:
> - undertake structured analysis of technical issues, translating this analysis into technical designs that describe a solution
> - be consulted about design and provide design patterns
> - identify deeper issues that need fixing
> - look for opportunities to collaborate and reuse components, communicating with both technical and non-technical stakeholders

### দায়িত্ব

- উপাদান, হোস্টিং, ইন্টিগ্রেশন ও নিরাপত্তাসহ একটি সেবার কারিগরি আর্কিটেকচার ডিজাইন করা।
- ডেলিভারি দলকে ডিজাইন প্যাটার্ন দেওয়া এবং তাদের কারিগরি ডিজাইন ও কোডের কাঠামো পর্যালোচনা করা।
- সেবার মালিকদের সাথে প্রাপ্যতা, কর্মদক্ষতা ও পুনরুদ্ধারের লক্ষ্যের মতো অ-কার্যকরী প্রয়োজনীয়তা সংজ্ঞায়িত করা।
- কারিগরি ঋণ ও অসমর্থিত প্রযুক্তি চিহ্নিত করা এবং তা সমাধানের পরিকল্পনা করা।
- ক্লিনিক্যাল নিরাপত্তা কেসের জন্য কারিগরি বিপদ ও নিয়ন্ত্রণ চিহ্নিত করা।

### দক্ষতা

| দক্ষতা | উৎস | প্রত্যাশিত স্তর | এই স্তরের অর্থ |
| --- | --- | --- | --- |
| [Architect for the whole context](../../দক্ষতা/#architect-for-the-whole-context) | UK GDaD PCF | কার্যকর | You can:<br>• align your work with the work being done by other architects and technical professionals<br>• track emerging issues, strategies, roadmaps, patterns and technologies over time to assess opportunities and risks to your work<br>• identify how other teams contribute to delivering outcomes through change |
| [Architecture communication](../../দক্ষতা/#architecture-communication) | UK GDaD PCF | কার্যকর | You can:<br>• listen to the needs of technical and business stakeholders<br>• create and use different architecture representations to communicate effectively, achieving agreement with technical and non-technical stakeholders<br>• provide support in discussions about architectural topics within a multidisciplinary team |
| [Community collaboration](../../দক্ষতা/#community-collaboration) | UK GDaD PCF | কার্যকর | You can:<br>• contribute to the work of others<br>• motivate and empower teams<br>• create the right environment for teams to work in, and can identify the best team makeup depending on the situation<br>• recognise and deal with issues |
| [Making architectural decisions](../../দক্ষতা/#making-architectural-decisions) | UK GDaD PCF | কার্যকর | You can:<br>• work with others to make architectural design decisions characterised by managed levels of risk and complexity<br>• identify and address architectural risks relevant to your team or domain, for example, business, data, or security<br>• engage with architectural governance and assurance to effectively manage decisions and risks, with support |
| [Strategy design](../../দক্ষতা/#strategy-design) | UK GDaD PCF | কার্যকর | You can:<br>• support the development of a strategy or vision that aligns with organisational objectives<br>• challenge requirements and assumptions, and identify opportunities to develop strategy<br>• support the implementation of a strategy or vision, for example, by using a roadmap or plan<br>• use architectural principles, patterns, and constraints when appropriate |
| [Technical design throughout the life cycle](../../দক্ষতা/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | কার্যকর | You can:<br>• create technical designs characterised by managed levels of risk, impact, and complexity<br>• provide guidance and support to teams using technical designs throughout the life cycle<br>• adapt a technical design if needed during delivery<br>• work with well-understood technology and identify appropriate patterns |
| [স্বাস্থ্য ও পরিচর্যা সেবা বোঝা](../../দক্ষতা/#স্বাস্থ্য-ও-পরিচর্যা-সেবা-বোঝা) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• আপনার কাজ যেসব ক্লিনিক্যাল ও পরিচর্যা কর্মপ্রবাহে সহায়তা করে তা ব্যাখ্যা করতে<br>• ক্লিনিক্যাল ও পরিচর্যা সহকর্মীদের সাথে প্রচলিত স্বাস্থ্যসেবা পরিভাষা সঠিকভাবে ব্যবহার করতে<br>• কোনো পরিবর্তন রোগী পরিচর্যাকে প্রভাবিত করতে পারে কি না তা চিনতে এবং তা জানাতে |
| [স্বাস্থ্য ডেটার আন্তঃকার্যক্ষমতা](../../দক্ষতা/#স্বাস্থ্য-ডেটার-আন্তঃকার্যক্ষমতা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• FHIR, HL7 সংস্করণ 2 ও বার্তা বিনিময়ের ধরন ব্যবহার করে ইন্টিগ্রেশন ডিজাইন ও তৈরি করতে<br>• FHIR রিসোর্স ও বাস্তবায়ন নির্দেশিকা লিখতে ও প্রোফাইল করতে<br>• ব্যবস্থাগুলোর মধ্যে জটিল ম্যাপিং ও ডেটার মানের সমস্যা সমাধান করতে |
| [তথ্য সুশাসন ও ডেটা সুরক্ষা](../../দক্ষতা/#তথ্য-সুশাসন-ও-ডেটা-সুরক্ষা) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• আপনার কাজে ডেটা সুরক্ষার নীতিগুলো প্রয়োগ করতে<br>• ডেটা সুরক্ষা প্রভাব মূল্যায়নে অবদান রাখতে<br>• তথ্যের অনুরোধ ও রেকর্ড সঠিকভাবে সামলাতে |
| [ক্লিনিক্যাল ঝুঁকি ব্যবস্থাপনা](../../দক্ষতা/#ক্লিনিক্যাল-ঝুঁকি-ব্যবস্থাপনা) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• বিপদ চিহ্নিতকরণ কর্মশালায় অংশ নিতে এবং বিপদ লগে অবদান রাখতে<br>• আপনার কাজের জন্য ক্লিনিক্যাল ঝুঁকি ব্যবস্থাপনা প্রক্রিয়া অনুসরণ করতে<br>• ক্লিনিক্যাল নিরাপত্তা কেসের জন্য প্রমাণ দিতে, যেমন পরীক্ষার ফলাফল |
| [পরিচয় ও প্রবেশাধিকার ব্যবস্থাপনা](../../দক্ষতা/#পরিচয়-ও-প্রবেশাধিকার-ব্যবস্থাপনা) | এই রেফারেন্স | সচেতনতা | আপনি পারেন:<br>• প্রবেশাধিকারের নিয়ম অনুসরণ করতে এবং আপনার লগইন তথ্য সুরক্ষিত রাখতে |

### সাধারণ যোগ্যতা ও অভিজ্ঞতা

- স্নাতকোত্তর স্তরে বা সমমানের অভিজ্ঞতায় কারিগরি আর্কিটেকচারের বিশেষায়িত জ্ঞান।
- প্রোডাকশন সফটওয়্যার বা অবকাঠামো ডিজাইন বা তৈরির অভিজ্ঞতা।

### ব্যান্ডের রূপরেখা

- **জ্ঞান:** অত্যন্ত উন্নত বিশেষায়িত জ্ঞান, সাধারণত স্নাতকোত্তর স্তরের বা সমমানের অভিজ্ঞতা।
- **স্বাধীনতা:** প্রতিষ্ঠানের নীতি অনুযায়ী কাজ করেন; ফলাফল কীভাবে অর্জিত হবে তা ঠিক করেন; অন্যরা যাঁর পরামর্শ নেন সেই বিশেষজ্ঞ।
- **পরিসর:** একাধিক প্রোডাক্ট বা সেবা, অথবা একটি বিশেষায়িত কার্যক্রম।
- **নেতৃত্ব:** একটি দল বা একটি পেশাগত অনুশীলন ক্ষেত্রের নেতৃত্ব দেন।
- **জবাবদিহি:** একটি সেবা বা বিশেষায়িত কার্যক্রম প্রদান, এবং বাজেট থাকলে তার দায়িত্ব।

### পদ মূল্যায়ন (দৃষ্টান্তমূলক)

| # | উপাদান | স্তর | পয়েন্ট |
| --- | --- | --- | --- |
| 1 | যোগাযোগ ও সম্পর্ক স্থাপনের দক্ষতা | 5 | 45 |
| 2 | জ্ঞান, প্রশিক্ষণ ও অভিজ্ঞতা | 7 | 196 |
| 3 | বিশ্লেষণ ও বিচার-বিবেচনার দক্ষতা | 5 | 60 |
| 4 | পরিকল্পনা ও সংগঠনের দক্ষতা | 3 | 27 |
| 5 | শারীরিক দক্ষতা | 2 | 15 |
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
| | **মোট** | | **496** (ব্যান্ড 7: 466–539) |

এই ভূমিকার জন্য স্বাস্থ্য খাতের বিজ্ঞাপনের সাথে সামঞ্জস্য রেখে UK GDaD PCF গ্রেডের প্রস্তাবিত ব্যান্ড 7-এ রাখা হয়েছে। কারিগরি আর্কিটেকচারের পুরো পরিসরজুড়ে বিশেষায়িত জ্ঞানের জন্য জ্ঞান স্নাতকোত্তর স্তরে বা সমমানে স্কোর করা হয়।

## ব্যান্ড 8a: সিনিয়র টেকনিক্যাল আর্কিটেক্ট

**UK GDaD PCF স্তর: Senior technical architect**

> A senior technical architect works on large or multiple pieces of work that are complex or risky.
> 
> At this role level, you will:
> - define strategy and be central to assuring services
> - regularly collaborate and find agreement with senior stakeholders, providing direction and challenge
> - be proactive in identifying problems and translating these into non-technical descriptions that can be widely understood
> - mentor and coach junior colleagues

### দায়িত্ব

- ক্লিনিক্যাল ব্যবস্থা ও যৌথ ইন্টিগ্রেশন প্ল্যাটফর্মের মতো বড়, জটিল বা উচ্চ ঝুঁকির সেবার কারিগরি ডিজাইনের নেতৃত্ব দেওয়া।
- এক বা একাধিক ডেলিভারি দলের কারিগরি দিকনির্দেশনা নির্ধারণ করা এবং ঝুঁকি বাড়ায় এমন ডিজাইন নিয়ে প্রশ্ন তোলা।
- স্থিতিস্থাপকতা, দুর্যোগ পুনরুদ্ধার ও নিরাপদ পরিচালনার জন্য ডিজাইন করা, এবং দলগুলো তা পরীক্ষা করে কি না যাচাই করা।
- সেবার মালিক, ক্লিনিক্যাল নেতা ও জ্যেষ্ঠ অংশীজনদের সহজ ভাষায় কারিগরি ঝুঁকি ও বিনিময় ব্যাখ্যা করা।
- টেকনিক্যাল আর্কিটেক্ট ও সিনিয়র ডেভেলপারদের পরামর্শ ও কোচিং দেওয়া।

### দক্ষতা

| দক্ষতা | উৎস | প্রত্যাশিত স্তর | এই স্তরের অর্থ |
| --- | --- | --- | --- |
| [Architect for the whole context](../../দক্ষতা/#architect-for-the-whole-context) | UK GDaD PCF | কার্যকর | You can:<br>• align your work with the work being done by other architects and technical professionals<br>• track emerging issues, strategies, roadmaps, patterns and technologies over time to assess opportunities and risks to your work<br>• identify how other teams contribute to delivering outcomes through change |
| [Architecture communication](../../দক্ষতা/#architecture-communication) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• lead the communication of complicated, complex or risky architecture topics with technical and non-technical stakeholders<br>• communicate with senior stakeholders across your organisation<br>• adapt your message and communication techniques to your audience<br>• advocate on behalf of a team to other stakeholders<br>• manage stakeholder expectations effectively |
| [Community collaboration](../../দক্ষতা/#community-collaboration) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../দক্ষতা/#making-architectural-decisions) | UK GDaD PCF | কার্যকর | You can:<br>• work with others to make architectural design decisions characterised by managed levels of risk and complexity<br>• identify and address architectural risks relevant to your team or domain, for example, business, data, or security<br>• engage with architectural governance and assurance to effectively manage decisions and risks, with support |
| [Strategy design](../../দক্ষতা/#strategy-design) | UK GDaD PCF | কার্যকর | You can:<br>• support the development of a strategy or vision that aligns with organisational objectives<br>• challenge requirements and assumptions, and identify opportunities to develop strategy<br>• support the implementation of a strategy or vision, for example, by using a roadmap or plan<br>• use architectural principles, patterns, and constraints when appropriate |
| [Technical design throughout the life cycle](../../দক্ষতা/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• create technical designs characterised by medium risk, impact, and complexity<br>• maintain appropriate quality and architectural coherence of a technical design in response to change<br>• use feedback to optimise and refine technical designs throughout the life cycle |
| [স্বাস্থ্য ও পরিচর্যা সেবা বোঝা](../../দক্ষতা/#স্বাস্থ্য-ও-পরিচর্যা-সেবা-বোঝা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• বিভিন্ন প্রতিষ্ঠানজুড়ে পরিচর্যা পথে একটি সেবা কীভাবে খাপ খায় তা বিশ্লেষণ করতে<br>• ডিজিটাল সেবা গড়তে চিকিৎসক, পরিচর্যাকর্মী ও রোগীদের সাথে কাজ করতে<br>• ডিজিটাল সিদ্ধান্তের প্রভাব পরিচর্যা, নিরাপত্তা ও কর্মীদের কাজের চাপের ওপর ব্যাখ্যা করতে |
| [স্বাস্থ্য ডেটার আন্তঃকার্যক্ষমতা](../../দক্ষতা/#স্বাস্থ্য-ডেটার-আন্তঃকার্যক্ষমতা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• FHIR, HL7 সংস্করণ 2 ও বার্তা বিনিময়ের ধরন ব্যবহার করে ইন্টিগ্রেশন ডিজাইন ও তৈরি করতে<br>• FHIR রিসোর্স ও বাস্তবায়ন নির্দেশিকা লিখতে ও প্রোফাইল করতে<br>• ব্যবস্থাগুলোর মধ্যে জটিল ম্যাপিং ও ডেটার মানের সমস্যা সমাধান করতে |
| [তথ্য সুশাসন ও ডেটা সুরক্ষা](../../দক্ষতা/#তথ্য-সুশাসন-ও-ডেটা-সুরক্ষা) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• আপনার কাজে ডেটা সুরক্ষার নীতিগুলো প্রয়োগ করতে<br>• ডেটা সুরক্ষা প্রভাব মূল্যায়নে অবদান রাখতে<br>• তথ্যের অনুরোধ ও রেকর্ড সঠিকভাবে সামলাতে |
| [ক্লিনিক্যাল ঝুঁকি ব্যবস্থাপনা](../../দক্ষতা/#ক্লিনিক্যাল-ঝুঁকি-ব্যবস্থাপনা) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• বিপদ চিহ্নিতকরণ কর্মশালায় অংশ নিতে এবং বিপদ লগে অবদান রাখতে<br>• আপনার কাজের জন্য ক্লিনিক্যাল ঝুঁকি ব্যবস্থাপনা প্রক্রিয়া অনুসরণ করতে<br>• ক্লিনিক্যাল নিরাপত্তা কেসের জন্য প্রমাণ দিতে, যেমন পরীক্ষার ফলাফল |
| [পরিচয় ও প্রবেশাধিকার ব্যবস্থাপনা](../../দক্ষতা/#পরিচয়-ও-প্রবেশাধিকার-ব্যবস্থাপনা) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• ব্যবহারকারী অ্যাকাউন্ট ও প্রবেশাধিকার তৈরি, পরিবর্তন ও অপসারণ করতে<br>• ভূমিকাভিত্তিক প্রবেশাধিকারের নিয়মের সাথে প্রবেশাধিকার মিলিয়ে দেখতে |
| [মেডিক্যাল ডিভাইস সফটওয়্যার নিয়ন্ত্রণ](../../দক্ষতা/#মেডিক্যাল-ডিভাইস-সফটওয়্যার-নিয়ন্ত্রণ) | এই রেফারেন্স | সচেতনতা | আপনি পারেন:<br>• কিছু স্বাস্থ্য সফটওয়্যার মেডিক্যাল ডিভাইস হিসেবে নিয়ন্ত্রিত তা ব্যাখ্যা করতে<br>• কোনো প্রোডাক্ট মেডিক্যাল ডিভাইস হতে পারে মনে হলে কাকে জিজ্ঞাসা করতে হবে তা জানতে |

### সাধারণ যোগ্যতা ও অভিজ্ঞতা

- স্নাতকোত্তর ডিগ্রির সমমান স্তরে জটিল সেবার কারিগরি ডিজাইনের উল্লেখযোগ্য অভিজ্ঞতা।

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

UK GDaD PCF গ্রেডের প্রস্তাবিত ব্যান্ডের (ব্যান্ড 7) চেয়ে উঁচুতে রাখা হয়েছে: স্বাস্থ্য খাতের বিজ্ঞাপনে এই ভূমিকা ব্যান্ড 8a-তে থাকে। পরিকল্পনা, নীতি ও কাজের স্বাধীনতা ব্যান্ড 7 প্রোফাইলের ওপরে স্কোর করা হয়, কারণ পদটি সামান্য তত্ত্বাবধানে একাধিক দলের কারিগরি দিকনির্দেশনা নির্ধারণ করে।

## ব্যান্ড 8b: লিড টেকনিক্যাল আর্কিটেক্ট

**UK GDaD PCF স্তর: Lead technical architect**

> A lead technical architect works with multiple projects or teams on problems that require broad architectural thinking.
> 
> At this role level, you will:
> - be responsible for leading the technical design of systems and services, justifying and communicating design decisions
> - assure other services and system quality, ensuring the technical work fits into the broader strategy for government
> - explore the benefits of cross-government alignment
> - provide mentoring within teams
> - provide leadership to other architects

### দায়িত্ব

- যৌথ প্যাটার্ন ও মানদণ্ড নির্ধারণ করে একাধিক সেবা বা দলজুড়ে কারিগরি আর্কিটেকচারের নেতৃত্ব দেওয়া।
- নিরাপত্তা, স্থিতিস্থাপকতা ও আন্তঃকার্যক্ষমতাসহ ডিজাইন কর্তৃপক্ষে ডিজাইনের কারিগরি মানের নিশ্চয়তা দেওয়া।
- এন্টারপ্রাইজ আর্কিটেক্ট ও প্রকৌশল নেতাদের সাথে প্রতিষ্ঠানের প্রযুক্তি রোডম্যাপ গড়া।
- প্রযুক্তি পছন্দ, প্ল্যাটফর্ম বিনিয়োগ ও কারিগরি ঝুঁকি নিয়ে জ্যেষ্ঠ নেতাদের পরামর্শ দেওয়া।
- টেকনিক্যাল আর্কিটেক্টদের নেতৃত্ব ও উন্নয়ন করা।

### দক্ষতা

| দক্ষতা | উৎস | প্রত্যাশিত স্তর | এই স্তরের অর্থ |
| --- | --- | --- | --- |
| [Architect for the whole context](../../দক্ষতা/#architect-for-the-whole-context) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• work to support wider organisational objectives beyond your immediate goals​<br>• track emerging internal and external issues over time that could affect the work of teams across the organisation<br>• take action to solve or mitigate problems by influencing colleagues across the organisation |
| [Architecture communication](../../দক্ষতা/#architecture-communication) | UK GDaD PCF | বিশেষজ্ঞ | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Community collaboration](../../দক্ষতা/#community-collaboration) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../দক্ষতা/#making-architectural-decisions) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• make and guide architectural design decisions characterised by medium risk and complexity<br>• identify and address architectural risks that affect multiple teams or domains<br>• use architectural governance and assurance to make design decisions and manage technical risks at the appropriate level<br>• contribute to the development of architectural governance and assurance |
| [Strategy design](../../দক্ষতা/#strategy-design) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• define strategies or visions across teams that align with organisational objectives<br>• direct the implementation of a strategy or vision, for example, by creating roadmaps or plans<br>• define architectural principles and patterns<br>• develop or maintain strategy in response to feedback and findings |
| [Technical design throughout the life cycle](../../দক্ষতা/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | বিশেষজ্ঞ | You can:<br>• create technical designs characterised by high risk, impact, and complexity<br>• lead and guide others in creating technical designs that achieve organisational objectives<br>• use feedback to optimise and refine standards for technical designs throughout the life cycle |
| [স্বাস্থ্য ও পরিচর্যা সেবা বোঝা](../../দক্ষতা/#স্বাস্থ্য-ও-পরিচর্যা-সেবা-বোঝা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• বিভিন্ন প্রতিষ্ঠানজুড়ে পরিচর্যা পথে একটি সেবা কীভাবে খাপ খায় তা বিশ্লেষণ করতে<br>• ডিজিটাল সেবা গড়তে চিকিৎসক, পরিচর্যাকর্মী ও রোগীদের সাথে কাজ করতে<br>• ডিজিটাল সিদ্ধান্তের প্রভাব পরিচর্যা, নিরাপত্তা ও কর্মীদের কাজের চাপের ওপর ব্যাখ্যা করতে |
| [স্বাস্থ্য ডেটার আন্তঃকার্যক্ষমতা](../../দক্ষতা/#স্বাস্থ্য-ডেটার-আন্তঃকার্যক্ষমতা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• FHIR, HL7 সংস্করণ 2 ও বার্তা বিনিময়ের ধরন ব্যবহার করে ইন্টিগ্রেশন ডিজাইন ও তৈরি করতে<br>• FHIR রিসোর্স ও বাস্তবায়ন নির্দেশিকা লিখতে ও প্রোফাইল করতে<br>• ব্যবস্থাগুলোর মধ্যে জটিল ম্যাপিং ও ডেটার মানের সমস্যা সমাধান করতে |
| [তথ্য সুশাসন ও ডেটা সুরক্ষা](../../দক্ষতা/#তথ্য-সুশাসন-ও-ডেটা-সুরক্ষা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• ডেটা সুরক্ষা প্রভাব মূল্যায়ন ও তথ্য বিনিময় চুক্তির নেতৃত্ব দিতে<br>• আইনি ভিত্তি, সম্মতি, গোপনীয়তা ও সংরক্ষণ নিয়ে দলগুলোকে পরামর্শ দিতে<br>• ঘটনা তদন্ত করতে এবং উন্নতির সুপারিশ করতে |
| [ক্লিনিক্যাল ঝুঁকি ব্যবস্থাপনা](../../দক্ষতা/#ক্লিনিক্যাল-ঝুঁকি-ব্যবস্থাপনা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• একটি প্রোডাক্ট বা পরিবর্তনের জন্য বিপদ চিহ্নিতকরণ ও ঝুঁকি মূল্যায়নের নেতৃত্ব দিতে<br>• বিপদ লগ ও ক্লিনিক্যাল নিরাপত্তা কেস প্রতিবেদন লিখতে ও হালনাগাদ রাখতে<br>• প্রোডাক্ট দলের সাথে ঝুঁকি নিয়ন্ত্রণে একমত হতে এবং সেগুলো কাজ করে কি না যাচাই করতে<br>• ক্লিনিক্যাল ঝুঁকি ব্যবস্থাপনার মানদণ্ড প্রয়োগে দলগুলোকে পরামর্শ দিতে |
| [পরিচয় ও প্রবেশাধিকার ব্যবস্থাপনা](../../দক্ষতা/#পরিচয়-ও-প্রবেশাধিকার-ব্যবস্থাপনা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• পরিচয় ও প্রবেশাধিকার সেবা ডিজাইন ও পরিচালনা করতে<br>• নিয়মিত প্রবেশাধিকার পর্যালোচনা করতে এবং সমস্যা সমাধান করতে |
| [মেডিক্যাল ডিভাইস সফটওয়্যার নিয়ন্ত্রণ](../../দক্ষতা/#মেডিক্যাল-ডিভাইস-সফটওয়্যার-নিয়ন্ত্রণ) | এই রেফারেন্স | কার্যকর | আপনি পারেন:<br>• মেডিক্যাল ডিভাইস মানদণ্ড পূরণ করে এমন একটি সফটওয়্যার জীবনচক্র প্রক্রিয়া অনুসরণ করতে<br>• সেই প্রক্রিয়ার প্রয়োজনীয় রেকর্ড তৈরি করতে |
| [জনবল ব্যবস্থাপনা](../../দক্ষতা/#জনবল-ব্যবস্থাপনা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• একটি দলের সরাসরি ব্যবস্থাপনা করতে, লক্ষ্য নির্ধারণ ও মূল্যায়ন পরিচালনা করতে<br>• সুস্থতায় সহায়তা করতে এবং উপস্থিতি, কর্মদক্ষতা ও আচরণ পরিচালনা করতে<br>• দলের উন্নয়ন ও উত্তরসূরি পরিকল্পনা করতে |

### সাধারণ যোগ্যতা ও অভিজ্ঞতা

- জটিল সেবার কারিগরি আর্কিটেকচারের নেতৃত্বে ব্যাপক অভিজ্ঞতা।

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

## ব্যান্ড 8c: প্রিন্সিপাল টেকনিক্যাল আর্কিটেক্ট

**UK GDaD PCF স্তর: Principal technical architect**

> A principal technical architect leads at the highest level and is responsible for making sure the strategy is agreed and followed.
> 
> At this role level, you will:
> - network and communicate with senior stakeholders across organisations
> - proactively seek opportunities for digital transformation
> - support multiple teams, finding and using best practice and emerging technologies
> - inspire other architects and help them understand how to deliver the goals of the organisation
> - be responsible for governance, solving complex and high risk issues or delivering architecture design

### দায়িত্ব

- প্রতিষ্ঠানের কারিগরি আর্কিটেকচারের কৌশল, নীতি ও মানদণ্ড নির্ধারণ করা।
- কারিগরি ডিজাইন কর্তৃপক্ষসহ প্রতিষ্ঠানজুড়ে কারিগরি ডিজাইনের সুশাসন করা।
- হোস্টিং কৌশল ও প্ল্যাটফর্ম একীভূতকরণের মতো বড় প্রযুক্তি সিদ্ধান্তে নির্বাহী দলকে পরামর্শ দেওয়া।
- আন্তঃপ্রাতিষ্ঠানিক কারিগরি ও মানদণ্ড সম্প্রদায়ে প্রতিষ্ঠানের প্রতিনিধিত্ব করা।
- প্রতিষ্ঠানজুড়ে আর্কিটেক্টদের অনুপ্রাণিত ও উন্নয়ন করা।

### দক্ষতা

| দক্ষতা | উৎস | প্রত্যাশিত স্তর | এই স্তরের অর্থ |
| --- | --- | --- | --- |
| [Architect for the whole context](../../দক্ষতা/#architect-for-the-whole-context) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• work to support wider organisational objectives beyond your immediate goals​<br>• track emerging internal and external issues over time that could affect the work of teams across the organisation<br>• take action to solve or mitigate problems by influencing colleagues across the organisation |
| [Architecture communication](../../দক্ষতা/#architecture-communication) | UK GDaD PCF | বিশেষজ্ঞ | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Community collaboration](../../দক্ষতা/#community-collaboration) | UK GDaD PCF | অনুশীলনকারী | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../দক্ষতা/#making-architectural-decisions) | UK GDaD PCF | বিশেষজ্ঞ | You can:<br>• make and guide architectural design decisions characterised by high levels of risk and complexity<br>• identify and address architectural risks across the organisation or wider government<br>• lead and evolve architectural governance and assurance<br>• represent architectural governance as part of wider governance, for example, legal or commercial |
| [Strategy design](../../দক্ষতা/#strategy-design) | UK GDaD PCF | বিশেষজ্ঞ | You can:<br>• define and connect strategies or visions across the organisation or wider government<br>• enable the implementation of strategies or visions across the organisation or wider government, for example, by advocating for resources and removing blockers |
| [Technical design throughout the life cycle](../../দক্ষতা/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | বিশেষজ্ঞ | You can:<br>• create technical designs characterised by high risk, impact, and complexity<br>• lead and guide others in creating technical designs that achieve organisational objectives<br>• use feedback to optimise and refine standards for technical designs throughout the life cycle |
| [স্বাস্থ্য ও পরিচর্যা সেবা বোঝা](../../দক্ষতা/#স্বাস্থ্য-ও-পরিচর্যা-সেবা-বোঝা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• বিভিন্ন প্রতিষ্ঠানজুড়ে পরিচর্যা পথে একটি সেবা কীভাবে খাপ খায় তা বিশ্লেষণ করতে<br>• ডিজিটাল সেবা গড়তে চিকিৎসক, পরিচর্যাকর্মী ও রোগীদের সাথে কাজ করতে<br>• ডিজিটাল সিদ্ধান্তের প্রভাব পরিচর্যা, নিরাপত্তা ও কর্মীদের কাজের চাপের ওপর ব্যাখ্যা করতে |
| [স্বাস্থ্য ডেটার আন্তঃকার্যক্ষমতা](../../দক্ষতা/#স্বাস্থ্য-ডেটার-আন্তঃকার্যক্ষমতা) | এই রেফারেন্স | বিশেষজ্ঞ | আপনি পারেন:<br>• প্রতিষ্ঠানের জন্য আন্তঃকার্যক্ষমতার মানদণ্ড ও কৌশল নির্ধারণ করতে<br>• জাতীয় বা আন্তঃপ্রাতিষ্ঠানিক মানদণ্ড কাজের নেতৃত্ব দিতে<br>• বহু ব্যবস্থাজুড়ে গুরুত্বপূর্ণ ইন্টিগ্রেশনের ডিজাইন নিশ্চিত করতে |
| [তথ্য সুশাসন ও ডেটা সুরক্ষা](../../দক্ষতা/#তথ্য-সুশাসন-ও-ডেটা-সুরক্ষা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• ডেটা সুরক্ষা প্রভাব মূল্যায়ন ও তথ্য বিনিময় চুক্তির নেতৃত্ব দিতে<br>• আইনি ভিত্তি, সম্মতি, গোপনীয়তা ও সংরক্ষণ নিয়ে দলগুলোকে পরামর্শ দিতে<br>• ঘটনা তদন্ত করতে এবং উন্নতির সুপারিশ করতে |
| [ক্লিনিক্যাল ঝুঁকি ব্যবস্থাপনা](../../দক্ষতা/#ক্লিনিক্যাল-ঝুঁকি-ব্যবস্থাপনা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• একটি প্রোডাক্ট বা পরিবর্তনের জন্য বিপদ চিহ্নিতকরণ ও ঝুঁকি মূল্যায়নের নেতৃত্ব দিতে<br>• বিপদ লগ ও ক্লিনিক্যাল নিরাপত্তা কেস প্রতিবেদন লিখতে ও হালনাগাদ রাখতে<br>• প্রোডাক্ট দলের সাথে ঝুঁকি নিয়ন্ত্রণে একমত হতে এবং সেগুলো কাজ করে কি না যাচাই করতে<br>• ক্লিনিক্যাল ঝুঁকি ব্যবস্থাপনার মানদণ্ড প্রয়োগে দলগুলোকে পরামর্শ দিতে |
| [পরিচয় ও প্রবেশাধিকার ব্যবস্থাপনা](../../দক্ষতা/#পরিচয়-ও-প্রবেশাধিকার-ব্যবস্থাপনা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• পরিচয় ও প্রবেশাধিকার সেবা ডিজাইন ও পরিচালনা করতে<br>• নিয়মিত প্রবেশাধিকার পর্যালোচনা করতে এবং সমস্যা সমাধান করতে |
| [প্রাতিষ্ঠানিক ঝুঁকি ব্যবস্থাপনা](../../দক্ষতা/#প্রাতিষ্ঠানিক-ঝুঁকি-ব্যবস্থাপনা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• একটি পরিদপ্তর বা কর্মসূচির ঝুঁকি প্রক্রিয়া পরিচালনা করতে<br>• ঝুঁকি-সহনশীলতার বিপরীতে ঝুঁকি মূল্যায়ন করতে এবং সেগুলো ঊর্ধ্বতনকে জানাতে<br>• কমিটির কাছে ঝুঁকি নিয়ে প্রতিবেদন দিতে |
| [জনবল ব্যবস্থাপনা](../../দক্ষতা/#জনবল-ব্যবস্থাপনা) | এই রেফারেন্স | অনুশীলনকারী | আপনি পারেন:<br>• একটি দলের সরাসরি ব্যবস্থাপনা করতে, লক্ষ্য নির্ধারণ ও মূল্যায়ন পরিচালনা করতে<br>• সুস্থতায় সহায়তা করতে এবং উপস্থিতি, কর্মদক্ষতা ও আচরণ পরিচালনা করতে<br>• দলের উন্নয়ন ও উত্তরসূরি পরিকল্পনা করতে |

### সাধারণ যোগ্যতা ও অভিজ্ঞতা

- একাধিক দল বা প্রতিষ্ঠানজুড়ে কারিগরি আর্কিটেকচারের নেতৃত্বে ব্যাপক অভিজ্ঞতা।

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
