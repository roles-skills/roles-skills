# مهندس بيانات

> هذا ملف مرجعي توضيحي لمؤسسة رعاية صحية رقمية عامة. وهو ليس وصفًا وظيفيًا رسميًا لأي جهة عمل، ونقاط تقييم الوظائف فيه ليست تقييمًا رسميًا.

> تُرجم هذا النص من الإنجليزية بواسطة مساعد ذكاء اصطناعي، ولم يراجعه بعدُ متحدث أصلي باللغة. تبقى الاقتباسات من إطار قدرات مهنة الرقمنة والبيانات في الحكومة البريطانية (UK GDaD PCF) ومن ESCO باللغة الإنجليزية.

**العائلة:** [البيانات](../../#البيانات)  
**الفئات:** 6, 7, 8a, 8b  
**دور UK GDaD PCF:** [Data engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/data-engineer/)  
**مهن ESCO:** [data engineer](http://data.europa.eu/esco/occupation/2079755f-d809-49e6-8037-4de6180e54c0) (ISCO-08 2511)

## الملخص

يبني مهندسو البيانات خطوط البيانات والمنصات التي تنقل بيانات الصحة والرعاية من الأنظمة السريرية والتشغيلية إلى أماكن يمكن تحليلها واستخدامها فيها بأمان، ويشغّلونها. وهم يصممون تدفقات البيانات، ويدمجون مصادر تستخدم معايير مختلفة، ويضمنون أن تكون البيانات دقيقة وحديثة وآمنة ومتاحة فقط لمن ينبغي أن يطّلع عليها.

## في مؤسسة رعاية صحية رقمية

- تشمل الأنظمة المصدر السجلات الإلكترونية للمرضى وأنظمة المختبرات والتصوير والصيدلة، التي تستخدم معايير مثل HL7 الإصدار 2 وHL7 FHIR وSNOMED CT وICD.
- كثيرًا ما تنقل خطوط البيانات بيانات مرضى محددة للهوية، لذلك يضمّن المهندسون الترميز المستعار وضبط الوصول والتدقيق منذ البداية.
- تدعم بعض تغذيات البيانات الرعاية المباشرة، مثل التنبيهات أو قوائم المرضى، لذلك قد يؤثر خط بيانات فاشل أو متأخر في المرضى ويحتاج إلى تقييم للسلامة السريرية.
- كثيرًا ما تحتاج البيانات إلى الربط عبر بيئات الرعاية، وهو ما يعتمد على مطابقة موثوقة للمرضى ومعرّفات متسقة.

## وصف الدور في UK GDaD PCF (النص الإنجليزي الأصلي)

> A data engineer develops and constructs data products and services, and integrates them into systems and business processes.

## مستويات الدور

| الفئة | المسمى | مستوى UK GDaD PCF | درجات الخدمة المدنية البريطانية | نقاط تقييم الوظيفة |
| --- | --- | --- | --- | --- |
| 6 | [مهندس بيانات](#الفئة-6-مهندس-بيانات) | Data engineer | HEO/SEO | 421 |
| 7 | [مهندس بيانات أول](#الفئة-7-مهندس-بيانات-أول) | Senior data engineer | SEO/G7 | 477 |
| 8a | [مهندس بيانات قائد](#الفئة-8a-مهندس-بيانات-قائد) | Lead data engineer | G7 | 551 |
| 8b | [رئيس هندسة البيانات](#الفئة-8b-رئيس-هندسة-البيانات) | Head of data engineering | G7/G6 | 589 |

## الفئة 6: مهندس بيانات

**مستوى UK GDaD PCF: Data engineer**

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

### المسؤوليات

- بناء خطوط البيانات من الأنظمة السريرية والتشغيلية إلى منصة البيانات وصيانتها، وفق تصاميم متفق عليها.
- ربط بيانات المصدر، بما فيها البيانات السريرية المرمّزة، بالنماذج المستهدفة وتوثيق عمليات الربط.
- تضمين الترميز المستعار والتحقق وفحوص جودة البيانات في خطوط البيانات.
- مراقبة خطوط البيانات وإصلاح الإخفاقات، مع إعطاء الأولوية للتغذيات التي تدعم الرعاية المباشرة.
- تطبيق ضوابط الوصول وسجلات التدقيق التي تستوفي قواعد حوكمة المعلومات.

### المهارات

| المهارة | المصدر | المستوى المتوقع | معنى هذا المستوى |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../المهارات/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | إلمام | You can:<br>• explain why it's important to communicate technical concepts in non-technical language<br>• explain the types of communication that can be used with internal and external stakeholders, and their impact |
| [Data analysis and synthesis](../../المهارات/#data-analysis-and-synthesis) | UK GDaD PCF | ممارسة | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data compliance and security](../../المهارات/#data-compliance-and-security) | UK GDaD PCF | ممارسة | You can:<br>• use official data classification when authoring documents<br>• apply internal procedures, policies and technologies to ensure secure data handling<br>• identify and address ethical considerations when working with data<br>• address data compliance issues using internal processes |
| [Data development process](../../المهارات/#data-development-process) | UK GDaD PCF | ممارسة | You can:<br>• implement simple data solutions such as data pipelines, following established approaches and standards<br>• create repeatable, reliable and reusable data solutions |
| [Data innovation](../../المهارات/#data-innovation) | UK GDaD PCF | إلمام | You can:<br>• develop a basic understanding of an unfamiliar or emerging technology, or a familiar technology in a new data context, with guidance<br>• share what you learn with colleagues, including how it could help deliver more value from data |
| [Data integration design](../../المهارات/#data-integration-design) | UK GDaD PCF | ممارسة | You can:<br>• design simple data exchange or integration solutions using established patterns or modelling techniques<br>• include security features in your data integration designs |
| [Data modelling](../../المهارات/#data-modelling) | UK GDaD PCF | ممارسة | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Metadata management](../../المهارات/#metadata-management) | UK GDaD PCF | ممارسة | You can:<br>• use metadata repositories to complete complex tasks such as data and systems integration impact analysis<br>• maintain a metadata repository to ensure information remains accurate and up to date |
| [Problem management](../../المهارات/#problem-management) | UK GDaD PCF | إلمام | You can:<br>• investigate problems in systems, processes and services, with an understanding of the level of a problem, for example, strategic, tactical or operational<br>• contribute to the implementation of remedies and preventative measures |
| [Programming and build (data and analytics engineering)](../../المهارات/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | ممارسة | You can:<br>• design, code, test and deploy programs or scripts following standards and good practice<br>• write readable, maintainable code<br>• use automation to improve the software development life cycle<br>• consider and adopt appropriate security measures in your solutions |
| [فهم خدمات الصحة والرعاية](../../المهارات/#فهم-خدمات-الصحة-والرعاية) | هذا المرجع | ممارسة | يمكنك:<br>• شرح مسارات العمل السريرية ومسارات الرعاية التي يدعمها عملك<br>• استخدام المصطلحات الصحية الشائعة استخدامًا صحيحًا مع الزملاء السريريين وزملاء الرعاية<br>• إدراك متى قد يؤثر تغيير ما في رعاية المرضى والتنبيه إليه |
| [حوكمة المعلومات وحماية البيانات](../../المهارات/#حوكمة-المعلومات-وحماية-البيانات) | هذا المرجع | ممارسة | يمكنك:<br>• تطبيق مبادئ حماية البيانات في عملك<br>• الإسهام في تقييمات أثر حماية البيانات<br>• التعامل مع طلبات المعلومات والسجلات بشكل صحيح |
| [التشغيل البيني للبيانات الصحية](../../المهارات/#التشغيل-البيني-للبيانات-الصحية) | هذا المرجع | ممارسة | يمكنك:<br>• قراءة موارد FHIR وملفاتها التعريفية وواجهاتها البرمجية واستخدامها<br>• بناء عمليات تكامل بسيطة أو اختبارها بتوجيه<br>• التحقق من الرسائل مقابل مواصفة |
| [المصطلحات والتصنيفات السريرية](../../المهارات/#المصطلحات-والتصنيفات-السريرية) | هذا المرجع | إلمام | يمكنك:<br>• شرح الفرق بين المصطلحات السريرية والتصنيف<br>• التعرف على المصطلحات الشائعة مثل SNOMED CT وICD |
| [الترميز المستعار وضبط الإفصاح](../../المهارات/#الترميز-المستعار-وضبط-الإفصاح) | هذا المرجع | ممارسة | يمكنك:<br>• العمل ببيانات ذات ترميز مستعار وإجراء فحوص الإفصاح قبل إصدار المخرجات<br>• إدراك متى قد تكشف البيانات المربوطة أو التفصيلية هوية مريض |
| [إدارة المخاطر السريرية](../../المهارات/#إدارة-المخاطر-السريرية) | هذا المرجع | إلمام | يمكنك:<br>• شرح كيف قد تضر أنظمة تقنية المعلومات الصحية بالمرضى، مثلًا من خلال معلومات خاطئة أو ناقصة أو متأخرة<br>• الإبلاغ عن مشكلة محتملة في السلامة السريرية عبر القناة الصحيحة |

### المؤهلات والخبرة المعتادة

- درجة جامعية في الحوسبة أو مجال ذي صلة، أو خبرة معادلة.
- خبرة في بناء خطوط البيانات.

### وصف الفئة

- **المعرفة:** معرفة متخصصة بمجموعة من الإجراءات، اكتُسبت من تدريب إضافي أو من الخبرة.
- **الاستقلالية:** يعمل باستقلالية؛ ويفسّر السياسات في مجاله؛ ويطلب المشورة في المسائل المعقدة.
- **النطاق:** منتج أو خدمة أو مسار عمل.
- **القيادة:** قد يقود فريقًا صغيرًا أو يرشد زملاءه.
- **المساءلة:** نتائج مسار عمله وجودة المشورة التي يقدمها.

### تقييم الوظيفة (توضيحي)

| # | العامل | المستوى | النقاط |
| --- | --- | --- | --- |
| 1 | مهارات التواصل وبناء العلاقات | 4 | 32 |
| 2 | المعرفة والتدريب والخبرة | 6 | 156 |
| 3 | مهارات التحليل والتقدير | 4 | 42 |
| 4 | مهارات التخطيط والتنظيم | 3 | 27 |
| 5 | المهارات البدنية | 3 | 27 |
| 6 | المسؤولية عن رعاية المرضى والعملاء | 1 | 4 |
| 7 | المسؤولية عن تطوير السياسات والخدمات | 2 | 12 |
| 8 | المسؤولية عن الموارد المالية والمادية | 1 | 5 |
| 9 | المسؤولية عن الأفراد | 1 | 5 |
| 10 | المسؤولية عن موارد المعلومات | 5 | 34 |
| 11 | المسؤولية عن البحث والتطوير | 2 | 12 |
| 12 | حرية التصرف | 4 | 32 |
| 13 | الجهد البدني | 1 | 3 |
| 14 | الجهد الذهني | 4 | 18 |
| 15 | الجهد العاطفي | 1 | 5 |
| 16 | ظروف العمل | 2 | 7 |
| | **المجموع** | | **421** (الفئة 6: 396–465) |

## الفئة 7: مهندس بيانات أول

**مستوى UK GDaD PCF: Senior data engineer**

> A senior data engineer designs and leads the implementation of data flows to connect operational systems, data for analytics and business intelligence (BI) systems.
> 
> At this role level, you will:
> - recognise opportunities to reuse existing data flows
> - lead the build of data streaming systems
> - optimise the code to ensure processes perform optimally
> - lead work on database management

### المسؤوليات

- تصميم تدفقات البيانات وخدمات البث التي تجمع البيانات من أنظمة صحة ورعاية كثيرة.
- تصميم عمليات مطابقة المرضى وربط البيانات، وقياس مدى جودتها.
- قيادة أعمال أداء قواعد البيانات والمنصات حتى تتاح البيانات حين تحتاجها الخدمات.
- تقييم مخاطر السلامة السريرية وحوكمة المعلومات في تدفقات البيانات مع الأخصائيين المعنيين.
- مراجعة عمل المهندسين الآخرين وتوجيههم.

### المهارات

| المهارة | المصدر | المستوى المتوقع | معنى هذا المستوى |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../المهارات/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | ممارسة | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Data analysis and synthesis](../../المهارات/#data-analysis-and-synthesis) | UK GDaD PCF | ممارسة | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data compliance and security](../../المهارات/#data-compliance-and-security) | UK GDaD PCF | تمكّن | You can:<br>• consistently apply data ethics, legislation, internal procedures, policies and technologies to ensure secure data handling<br>• help ensure your team remain compliant by identifying and addressing current and potential data compliance and ethical issues<br>• guide and support others in addressing data compliance issues |
| [Data development process](../../المهارات/#data-development-process) | UK GDaD PCF | تمكّن | You can:<br>• lead the implementation of complex or large-scale data solutions<br>• apply appropriate technology and techniques to ensure data solutions are secure and scalable<br>• identify and implement continuous improvement to the operation and performance of data solutions |
| [Data innovation](../../المهارات/#data-innovation) | UK GDaD PCF | ممارسة | You can:<br>• experiment with unfamiliar and emerging technologies, or familiar technologies in new data contexts, with guidance<br>• share what you learn with the team, explaining potential benefits, risks, and practical considerations<br>• identify opportunities to apply technology to improve data processes or outcomes in an operational setting or the wider organisation |
| [Data integration design](../../المهارات/#data-integration-design) | UK GDaD PCF | تمكّن | You can:<br>• select the most appropriate techniques for different integration scenarios<br>• evaluate and lead the implementation of integration using varied approaches that ensure security, efficiency and compliance |
| [Data modelling](../../المهارات/#data-modelling) | UK GDaD PCF | تمكّن | You can:<br>• produce relevant data models across multiple subject areas<br>• explain which models to use for which purpose<br>• understand industry-recognised data modelling patterns and standards, and when to apply them<br>• compare and align different data models |
| [Metadata management](../../المهارات/#metadata-management) | UK GDaD PCF | تمكّن | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../المهارات/#problem-management) | UK GDaD PCF | ممارسة | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Programming and build (data and analytics engineering)](../../المهارات/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | تمكّن | You can:<br>• lead the design, code, testing and deployment of secure, resilient and maintainable solutions<br>• continuously improve the codebase and reliability of solutions<br>• create automation to improve the software development life cycle<br>• work with others to implement standards and good practice to ensure security, testability and maintainability of solutions |
| [فهم خدمات الصحة والرعاية](../../المهارات/#فهم-خدمات-الصحة-والرعاية) | هذا المرجع | ممارسة | يمكنك:<br>• شرح مسارات العمل السريرية ومسارات الرعاية التي يدعمها عملك<br>• استخدام المصطلحات الصحية الشائعة استخدامًا صحيحًا مع الزملاء السريريين وزملاء الرعاية<br>• إدراك متى قد يؤثر تغيير ما في رعاية المرضى والتنبيه إليه |
| [حوكمة المعلومات وحماية البيانات](../../المهارات/#حوكمة-المعلومات-وحماية-البيانات) | هذا المرجع | تمكّن | يمكنك:<br>• قيادة تقييمات أثر حماية البيانات واتفاقيات تبادل المعلومات<br>• تقديم المشورة للفرق بشأن الأساس القانوني والموافقة والسرية ومدد الاحتفاظ<br>• التحقيق في الحوادث والتوصية بالتحسينات |
| [التشغيل البيني للبيانات الصحية](../../المهارات/#التشغيل-البيني-للبيانات-الصحية) | هذا المرجع | تمكّن | يمكنك:<br>• تصميم عمليات تكامل وبناؤها باستخدام FHIR وHL7 الإصدار 2 وأنماط المراسلة<br>• كتابة موارد FHIR وتعريف ملفاتها وأدلة تطبيقها<br>• حل مشكلات الربط وجودة البيانات المعقدة بين الأنظمة |
| [المصطلحات والتصنيفات السريرية](../../المهارات/#المصطلحات-والتصنيفات-السريرية) | هذا المرجع | ممارسة | يمكنك:<br>• إيجاد الرموز الصحيحة لعنصر بيانات أو نموذج واستخدامها<br>• استخدام متصفحات المصطلحات والمجموعات المرجعية |
| [الترميز المستعار وضبط الإفصاح](../../المهارات/#الترميز-المستعار-وضبط-الإفصاح) | هذا المرجع | تمكّن | يمكنك:<br>• تصميم أساليب للترميز المستعار والربط تُبقي المعرّفات منفصلة عن بيانات التحليل<br>• تقييم خطر إعادة تحديد الهوية في مجموعة بيانات أو منشور واختيار الضوابط المناسبة<br>• تقديم المشورة للفرق بشأن البيئات الآمنة، مثل بيئات البحث الموثوقة |
| [إدارة المخاطر السريرية](../../المهارات/#إدارة-المخاطر-السريرية) | هذا المرجع | ممارسة | يمكنك:<br>• المشاركة في ورش تحديد المخاطر والإسهام في سجل المخاطر<br>• اتباع عملية إدارة المخاطر السريرية في عملك<br>• تقديم أدلة لملف السلامة السريرية، مثل نتائج الاختبارات |

### المؤهلات والخبرة المعتادة

- خبرة واسعة في تصميم أنظمة البيانات وبنائها، بمستوى يعادل درجة الماجستير.

### وصف الفئة

- **المعرفة:** معرفة متخصصة متقدمة جدًا، عادةً بمستوى الماجستير أو خبرة معادلة.
- **الاستقلالية:** يعمل وفق سياسات المؤسسة؛ ويقرر كيف تتحقق النتائج؛ وهو الخبير الذي يستشيره الآخرون.
- **النطاق:** عدة منتجات أو خدمات، أو وظيفة متخصصة.
- **القيادة:** يقود فريقًا أو مجال ممارسة مهنية.
- **المساءلة:** تقديم خدمة أو وظيفة متخصصة، وميزانيتها إن وُجدت.

### تقييم الوظيفة (توضيحي)

| # | العامل | المستوى | النقاط |
| --- | --- | --- | --- |
| 1 | مهارات التواصل وبناء العلاقات | 4 | 32 |
| 2 | المعرفة والتدريب والخبرة | 7 | 196 |
| 3 | مهارات التحليل والتقدير | 4 | 42 |
| 4 | مهارات التخطيط والتنظيم | 3 | 27 |
| 5 | المهارات البدنية | 3 | 27 |
| 6 | المسؤولية عن رعاية المرضى والعملاء | 1 | 4 |
| 7 | المسؤولية عن تطوير السياسات والخدمات | 3 | 21 |
| 8 | المسؤولية عن الموارد المالية والمادية | 1 | 5 |
| 9 | المسؤولية عن الأفراد | 2 | 12 |
| 10 | المسؤولية عن موارد المعلومات | 5 | 34 |
| 11 | المسؤولية عن البحث والتطوير | 2 | 12 |
| 12 | حرية التصرف | 4 | 32 |
| 13 | الجهد البدني | 1 | 3 |
| 14 | الجهد الذهني | 4 | 18 |
| 15 | الجهد العاطفي | 1 | 5 |
| 16 | ظروف العمل | 2 | 7 |
| | **المجموع** | | **477** (الفئة 7: 466–539) |

## الفئة 8a: مهندس بيانات قائد

**مستوى UK GDaD PCF: Lead data engineer**

> A lead data engineer is responsible for the design and implementation of numerous complex data flows to connect operational systems, data for analytics and business intelligence (BI) systems.
> 
> At this role level, you will:
> - recognise and share opportunities to reuse existing data flows between teams
> - be responsible for the build of data-streaming systems
> - co-ordinate teams and set best practice and standards
> - apply knowledge of systems integration to your work
> - champion data engineering across government

### المسؤوليات

- قيادة تصميم منصة البيانات في المؤسسة وتدفقات بياناتها الكثيرة وتشغيلها.
- وضع المعايير الهندسية لخطوط البيانات والاختبار والأمن والتوثيق.
- التخطيط لتكامل البيانات مع شركاء الصحة والرعاية، بما في ذلك سجلات الرعاية المشتركة وخدمات البيانات الإقليمية.
- ضمان أن تكون تدفقات البيانات التي تدعم الرعاية المباشرة مرنة ولها ملفات سلامة سريرية.
- تنسيق فرق هندسة البيانات والإدارة المباشرة للمهندسين.

### المهارات

| المهارة | المصدر | المستوى المتوقع | معنى هذا المستوى |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../المهارات/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | تمكّن | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Data analysis and synthesis](../../المهارات/#data-analysis-and-synthesis) | UK GDaD PCF | تمكّن | You can:<br>• understand and help teams to apply a range of techniques for data profiling<br>• source system analysis from a complex single source<br>• bring multiple data sources together in a conformed model for analysis |
| [Data compliance and security](../../المهارات/#data-compliance-and-security) | UK GDaD PCF | خبرة | You can:<br>• advise senior stakeholders on data security, ethical or procedural risks<br>• improve organisational awareness of data compliance and procedures<br>• lead, guide and mentor teams in implementing secure data practices and maintaining compliance |
| [Data development process](../../المهارات/#data-development-process) | UK GDaD PCF | خبرة | You can:<br>• establish cross-organisational data solutions that include all aspects of the data development life cycle<br>• define and promote good practices for creating repeatable, reliable and reusable data solutions |
| [Data innovation](../../المهارات/#data-innovation) | UK GDaD PCF | تمكّن | You can:<br>• test and evaluate the feasibility of unfamiliar and emerging technologies, or familiar technologies in new data contexts<br>• share what you learn with the organisation, explaining potential benefits, risks, and practical considerations<br>• recommend, design and implement innovative data solutions based on organisation objectives, user needs, and operational constraints |
| [Data integration design](../../المهارات/#data-integration-design) | UK GDaD PCF | خبرة | You can:<br>• establish cross-organisational data integration standards and design patterns<br>• guide teams in designing secure and interoperable systems and services |
| [Data modelling](../../المهارات/#data-modelling) | UK GDaD PCF | خبرة | You can:<br>• understand the concepts and principles of data modelling and can produce relevant data models<br>• work across government and industry, recognising opportunities for the reuse and alignment of data models in different organisations<br>• design the method to categorise data models within an organisation |
| [Metadata management](../../المهارات/#metadata-management) | UK GDaD PCF | تمكّن | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../المهارات/#problem-management) | UK GDaD PCF | تمكّن | You can:<br>• ensure that the right actions are taken to investigate, resolve and anticipate problems<br>• co-ordinate the team to investigate problems, implement solutions and take preventive measures |
| [Programming and build (data and analytics engineering)](../../المهارات/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | تمكّن | You can:<br>• lead the design, code, testing and deployment of secure, resilient and maintainable solutions<br>• continuously improve the codebase and reliability of solutions<br>• create automation to improve the software development life cycle<br>• work with others to implement standards and good practice to ensure security, testability and maintainability of solutions |
| [فهم خدمات الصحة والرعاية](../../المهارات/#فهم-خدمات-الصحة-والرعاية) | هذا المرجع | تمكّن | يمكنك:<br>• تحليل موقع خدمة ما ضمن مسارات الرعاية بين المؤسسات<br>• العمل مع الممارسين السريريين وموظفي الرعاية والمرضى لتشكيل الخدمات الرقمية<br>• شرح أثر القرارات الرقمية في الرعاية والسلامة وعبء العمل على الموظفين |
| [حوكمة المعلومات وحماية البيانات](../../المهارات/#حوكمة-المعلومات-وحماية-البيانات) | هذا المرجع | تمكّن | يمكنك:<br>• قيادة تقييمات أثر حماية البيانات واتفاقيات تبادل المعلومات<br>• تقديم المشورة للفرق بشأن الأساس القانوني والموافقة والسرية ومدد الاحتفاظ<br>• التحقيق في الحوادث والتوصية بالتحسينات |
| [التشغيل البيني للبيانات الصحية](../../المهارات/#التشغيل-البيني-للبيانات-الصحية) | هذا المرجع | تمكّن | يمكنك:<br>• تصميم عمليات تكامل وبناؤها باستخدام FHIR وHL7 الإصدار 2 وأنماط المراسلة<br>• كتابة موارد FHIR وتعريف ملفاتها وأدلة تطبيقها<br>• حل مشكلات الربط وجودة البيانات المعقدة بين الأنظمة |
| [المصطلحات والتصنيفات السريرية](../../المهارات/#المصطلحات-والتصنيفات-السريرية) | هذا المرجع | ممارسة | يمكنك:<br>• إيجاد الرموز الصحيحة لعنصر بيانات أو نموذج واستخدامها<br>• استخدام متصفحات المصطلحات والمجموعات المرجعية |
| [الترميز المستعار وضبط الإفصاح](../../المهارات/#الترميز-المستعار-وضبط-الإفصاح) | هذا المرجع | تمكّن | يمكنك:<br>• تصميم أساليب للترميز المستعار والربط تُبقي المعرّفات منفصلة عن بيانات التحليل<br>• تقييم خطر إعادة تحديد الهوية في مجموعة بيانات أو منشور واختيار الضوابط المناسبة<br>• تقديم المشورة للفرق بشأن البيئات الآمنة، مثل بيئات البحث الموثوقة |
| [إدارة المخاطر السريرية](../../المهارات/#إدارة-المخاطر-السريرية) | هذا المرجع | ممارسة | يمكنك:<br>• المشاركة في ورش تحديد المخاطر والإسهام في سجل المخاطر<br>• اتباع عملية إدارة المخاطر السريرية في عملك<br>• تقديم أدلة لملف السلامة السريرية، مثل نتائج الاختبارات |
| [إدارة الأفراد](../../المهارات/#إدارة-الأفراد) | هذا المرجع | تمكّن | يمكنك:<br>• الإدارة المباشرة لفريق، ووضع الأهداف وإجراء تقييمات الأداء<br>• دعم الرفاه وإدارة الحضور والأداء والسلوك<br>• التخطيط لتطوير الفريق وتعاقب أفراده |

### المؤهلات والخبرة المعتادة

- خبرة واسعة في قيادة هندسة البيانات للأنظمة المعقدة.

### وصف الفئة

- **المعرفة:** معرفة خبيرة بتخصص ما وبإدارته.
- **الاستقلالية:** يفسّر سياسات المؤسسة لخدمة ما؛ ويحدد توجه الفريق.
- **النطاق:** مجال خدمة أو تخصص على مستوى المؤسسة.
- **القيادة:** يدير فريقًا، أو يقود تخصصًا دون إدارة مباشرة للموظفين.
- **المساءلة:** مجال خدمة وموظفوه وميزانيته.

### تقييم الوظيفة (توضيحي)

| # | العامل | المستوى | النقاط |
| --- | --- | --- | --- |
| 1 | مهارات التواصل وبناء العلاقات | 5 | 45 |
| 2 | المعرفة والتدريب والخبرة | 7 | 196 |
| 3 | مهارات التحليل والتقدير | 5 | 60 |
| 4 | مهارات التخطيط والتنظيم | 4 | 42 |
| 5 | المهارات البدنية | 2 | 15 |
| 6 | المسؤولية عن رعاية المرضى والعملاء | 1 | 4 |
| 7 | المسؤولية عن تطوير السياسات والخدمات | 4 | 32 |
| 8 | المسؤولية عن الموارد المالية والمادية | 2 | 12 |
| 9 | المسؤولية عن الأفراد | 3 | 21 |
| 10 | المسؤولية عن موارد المعلومات | 5 | 34 |
| 11 | المسؤولية عن البحث والتطوير | 2 | 12 |
| 12 | حرية التصرف | 5 | 45 |
| 13 | الجهد البدني | 1 | 3 |
| 14 | الجهد الذهني | 4 | 18 |
| 15 | الجهد العاطفي | 1 | 5 |
| 16 | ظروف العمل | 2 | 7 |
| | **المجموع** | | **551** (الفئة 8a: 540–584) |

## الفئة 8b: رئيس هندسة البيانات

**مستوى UK GDaD PCF: Head of data engineering**

> A head of data engineering leads multi-functional delivery teams to deliver robust data services for their department, other government departments and private sector partners.
> 
> At this role level, you will:
> - inspire best practice for data products and services within your teams
> - build data engineering capability by providing technical leadership and career development for the community
> - work with other senior team members to identify, plan, develop and deliver data services

### المسؤوليات

- وضع استراتيجية منصات البيانات وخدمات هندسة البيانات في المؤسسة.
- قيادة فرق متعددة التخصصات تقدم خدمات البيانات للفرق الداخلية وشركاء الصحة والرعاية.
- تقديم المشورة لكبار القادة بشأن مخاطر منصات البيانات وتكاليفها والاستثمار فيها.
- ضمان استيفاء خدمات البيانات لمتطلبات حوكمة المعلومات والأمن والسلامة السريرية.
- بناء قدرات هندسة البيانات من خلال التوظيف والتطوير والمسارات المهنية.

### المهارات

| المهارة | المصدر | المستوى المتوقع | معنى هذا المستوى |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../المهارات/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | خبرة | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Data analysis and synthesis](../../المهارات/#data-analysis-and-synthesis) | UK GDaD PCF | تمكّن | You can:<br>• understand and help teams to apply a range of techniques for data profiling<br>• source system analysis from a complex single source<br>• bring multiple data sources together in a conformed model for analysis |
| [Data compliance and security](../../المهارات/#data-compliance-and-security) | UK GDaD PCF | خبرة | You can:<br>• advise senior stakeholders on data security, ethical or procedural risks<br>• improve organisational awareness of data compliance and procedures<br>• lead, guide and mentor teams in implementing secure data practices and maintaining compliance |
| [Data development process](../../المهارات/#data-development-process) | UK GDaD PCF | خبرة | You can:<br>• establish cross-organisational data solutions that include all aspects of the data development life cycle<br>• define and promote good practices for creating repeatable, reliable and reusable data solutions |
| [Data innovation](../../المهارات/#data-innovation) | UK GDaD PCF | خبرة | You can:<br>• advocate for adoption of unfamiliar and emerging technologies, or familiar technologies in new data contexts, ensuring organisation objectives, user needs, and operational constraints inform decisions<br>• develop organisational capability in data innovation through leadership<br>• anticipate future technology changes and advise how to take advantage of them to realise value from data |
| [Data integration design](../../المهارات/#data-integration-design) | UK GDaD PCF | خبرة | You can:<br>• establish cross-organisational data integration standards and design patterns<br>• guide teams in designing secure and interoperable systems and services |
| [Data modelling](../../المهارات/#data-modelling) | UK GDaD PCF | ممارسة | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Metadata management](../../المهارات/#metadata-management) | UK GDaD PCF | خبرة | You can:<br>• identify how metadata repositories can support different areas of the organisation<br>• communicate the value of metadata repositories<br>• set up robust governance processes to keep repositories up to date |
| [Problem management](../../المهارات/#problem-management) | UK GDaD PCF | خبرة | You can:<br>• anticipate problems and defend against them at the right time<br>• understand how a problem fits into the larger picture<br>• identify and describe problems, and help others to describe them<br>• build problem-solving capabilities in others |
| [Programming and build (data and analytics engineering)](../../المهارات/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | خبرة | You can:<br>• set standards for programming tools and techniques<br>• select appropriate development methods for a problem<br>• advise on the application of standards and methods that ensure security, maintainability and compliance<br>• take technical responsibility for all stages of a software development project, providing technical advice and guidance to stakeholders |
| [فهم خدمات الصحة والرعاية](../../المهارات/#فهم-خدمات-الصحة-والرعاية) | هذا المرجع | تمكّن | يمكنك:<br>• تحليل موقع خدمة ما ضمن مسارات الرعاية بين المؤسسات<br>• العمل مع الممارسين السريريين وموظفي الرعاية والمرضى لتشكيل الخدمات الرقمية<br>• شرح أثر القرارات الرقمية في الرعاية والسلامة وعبء العمل على الموظفين |
| [حوكمة المعلومات وحماية البيانات](../../المهارات/#حوكمة-المعلومات-وحماية-البيانات) | هذا المرجع | تمكّن | يمكنك:<br>• قيادة تقييمات أثر حماية البيانات واتفاقيات تبادل المعلومات<br>• تقديم المشورة للفرق بشأن الأساس القانوني والموافقة والسرية ومدد الاحتفاظ<br>• التحقيق في الحوادث والتوصية بالتحسينات |
| [التشغيل البيني للبيانات الصحية](../../المهارات/#التشغيل-البيني-للبيانات-الصحية) | هذا المرجع | خبرة | يمكنك:<br>• وضع معايير التشغيل البيني واستراتيجيته للمؤسسة<br>• قيادة أعمال المعايير على المستوى الوطني أو بين المؤسسات<br>• ضمان تصميم عمليات التكامل الحرجة عبر أنظمة كثيرة |
| [الترميز المستعار وضبط الإفصاح](../../المهارات/#الترميز-المستعار-وضبط-الإفصاح) | هذا المرجع | تمكّن | يمكنك:<br>• تصميم أساليب للترميز المستعار والربط تُبقي المعرّفات منفصلة عن بيانات التحليل<br>• تقييم خطر إعادة تحديد الهوية في مجموعة بيانات أو منشور واختيار الضوابط المناسبة<br>• تقديم المشورة للفرق بشأن البيئات الآمنة، مثل بيئات البحث الموثوقة |
| [إدارة المخاطر السريرية](../../المهارات/#إدارة-المخاطر-السريرية) | هذا المرجع | ممارسة | يمكنك:<br>• المشاركة في ورش تحديد المخاطر والإسهام في سجل المخاطر<br>• اتباع عملية إدارة المخاطر السريرية في عملك<br>• تقديم أدلة لملف السلامة السريرية، مثل نتائج الاختبارات |
| [إدارة الأفراد](../../المهارات/#إدارة-الأفراد) | هذا المرجع | تمكّن | يمكنك:<br>• الإدارة المباشرة لفريق، ووضع الأهداف وإجراء تقييمات الأداء<br>• دعم الرفاه وإدارة الحضور والأداء والسلوك<br>• التخطيط لتطوير الفريق وتعاقب أفراده |
| [إدارة الميزانية](../../المهارات/#إدارة-الميزانية) | هذا المرجع | تمكّن | يمكنك:<br>• تولّي ميزانية وإدارتها، مع التنبؤ وشرح الانحرافات<br>• إعداد دراسة جدوى تتضمن التكاليف والفوائد |

### المؤهلات والخبرة المعتادة

- خبرة واسعة في قيادة هندسة البيانات عبر فرق متعددة.

### وصف الفئة

- **المعرفة:** معرفة خبيرة بعدة تخصصات أو بخدمة كبيرة.
- **الاستقلالية:** يشكّل السياسات والاستراتيجية لمجال كبير.
- **النطاق:** عدة خدمات أو فرق، أو تخصص على المستوى الرئيسي.
- **القيادة:** يدير مديرين، أو هو المرجع الرئيسي في تخصص ما.
- **المساءلة:** عدة خدمات وموظفوها وميزانياتها.

### تقييم الوظيفة (توضيحي)

| # | العامل | المستوى | النقاط |
| --- | --- | --- | --- |
| 1 | مهارات التواصل وبناء العلاقات | 5 | 45 |
| 2 | المعرفة والتدريب والخبرة | 7 | 196 |
| 3 | مهارات التحليل والتقدير | 5 | 60 |
| 4 | مهارات التخطيط والتنظيم | 5 | 60 |
| 5 | المهارات البدنية | 2 | 15 |
| 6 | المسؤولية عن رعاية المرضى والعملاء | 1 | 4 |
| 7 | المسؤولية عن تطوير السياسات والخدمات | 4 | 32 |
| 8 | المسؤولية عن الموارد المالية والمادية | 3 | 21 |
| 9 | المسؤولية عن الأفراد | 4 | 32 |
| 10 | المسؤولية عن موارد المعلومات | 5 | 34 |
| 11 | المسؤولية عن البحث والتطوير | 2 | 12 |
| 12 | حرية التصرف | 5 | 45 |
| 13 | الجهد البدني | 1 | 3 |
| 14 | الجهد الذهني | 4 | 18 |
| 15 | الجهد العاطفي | 1 | 5 |
| 16 | ظروف العمل | 2 | 7 |
| | **المجموع** | | **589** (الفئة 8b: 585–629) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
