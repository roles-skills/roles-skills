# مهندس اختبار

> هذا ملف مرجعي توضيحي لمؤسسة رعاية صحية رقمية عامة. وهو ليس وصفًا وظيفيًا رسميًا لأي جهة عمل، ونقاط تقييم الوظائف فيه ليست تقييمًا رسميًا.

> تُرجم هذا النص من الإنجليزية بواسطة مساعد ذكاء اصطناعي، ولم يراجعه بعدُ متحدث أصلي باللغة. تبقى الاقتباسات من إطار قدرات مهنة الرقمنة والبيانات في الحكومة البريطانية (UK GDaD PCF) ومن ESCO باللغة الإنجليزية.

**العائلة:** [ضمان الجودة والاختبار](../../#ضمان-الجودة-والاختبار)  
**الفئات:** 4, 6, 7, 8a  
**دور UK GDaD PCF:** [Test engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/test-engineer/)  
**مهن ESCO:** [software tester](http://data.europa.eu/esco/occupation/106f79e4-6264-45f1-9e7a-297435cd684b) (ISCO-08 2519)

## الملخص

يبني مهندسو الاختبار الاختبارات المؤتمتة والأدوات والأطر التي تمكّن الفرق من اختبار الخدمات الصحية الرقمية في المؤسسة بسرعة وتكرار. وهم يكتبون شيفرة لاختبار الوظائف وعمليات التكامل والأداء والأمن والمرونة، ويضمّنون الاختبار في خطوط التسليم، حتى يمكن إصدار التغييرات في الأنظمة السريرية والموجهة للمرضى بأمان.

## في مؤسسة رعاية صحية رقمية

- الأنظمة السريرية حرجة للسلامة، لذلك تحمي اختبارات الانحدار المؤتمتة ضوابط السلامة المسجلة في سجلات المخاطر ويُحتفظ بها أدلةً لملفات السلامة.
- تحتاج عمليات التكامل مع أنظمة الصحة والرعاية الأخرى إلى اختبارات مؤتمتة مقابل معايير مثل HL7 FHIR وHL7 الإصدار 2، وغالبًا باستخدام أنظمة شريكة محاكاة.
- تعمل الخدمات السريرية على مدار الساعة وتبلغ ذروتها في أوقات يمكن توقعها، لذلك يحاكي اختبار الأداء والمرونة الطلب السريري الحقيقي.
- يجب ألا تحتوي بيئات الاختبار على بيانات مرضى حقيقية، لذلك يولّد المهندسون بيانات اصطناعية واقعية، بما فيها الحالات السريرية النادرة والحدّية.
- تحتاج البرمجيات المنظَّمة بوصفها جهازًا طبيًا إلى اختبار قابل للتتبع والتكرار ضمن دورة حياتها وفق معايير مثل IEC 62304.

## وصف الدور في UK GDaD PCF (النص الإنجليزي الأصلي)

> A test engineer designs, builds, automates and executes comprehensive, robust and maintainable test suites. They apply test engineering standards, perform exploratory testing and use diverse techniques to identify risks and improve testing efficiency and quality.
> 
> In this role you will:
> - maintain automated tests in continuous integration, continuous delivery (CI/CD) pipelines
> - use, develop and standardise reusable frameworks and tools following engineering practices and standards
> - analyse and test artefacts such as products, services and business processes
> - promote quality considerations throughout the development life cycle
> - support the resolution of technical issues

## مستويات الدور

| الفئة | المسمى | مستوى UK GDaD PCF | درجات الخدمة المدنية البريطانية | نقاط تقييم الوظيفة |
| --- | --- | --- | --- | --- |
| 4 | [مهندس اختبار مشارك](#الفئة-4-مهندس-اختبار-مشارك) | Associate test engineer | EO | 275 |
| 6 | [مهندس اختبار](#الفئة-6-مهندس-اختبار) | Test engineer | HEO/SEO | 411 |
| 7 | [مهندس اختبار أول](#الفئة-7-مهندس-اختبار-أول) | Senior test engineer | SEO/G7 | 477 |
| 8a | [مهندس اختبار قائد](#الفئة-8a-مهندس-اختبار-قائد) | Lead test engineer | SEO/G7/G6 | 553 |

## الفئة 4: مهندس اختبار مشارك

**مستوى UK GDaD PCF: Associate test engineer**

> An associate test engineer works closely with other test professionals to learn test engineering activities and techniques.
> 
> At this role level, you will:
> - contribute to and maintain technical test suites under supervision
> - follow engineering practices and standards to apply test approaches, plans and strategies under supervision
> - analyse artefacts such as user stories, prototypes, processes and designs with support
> - support the development of reports, recording of outcomes and resolution of defects
> - understand the technical tooling and engineering approach to design and execute tests

### المسؤوليات

- كتابة اختبارات مؤتمتة بسيطة وصيانتها تحت الإشراف، وفق المعايير الهندسية للفريق.
- تشغيل الاختبارات المؤتمتة واليدوية وتسجيل النتائج بدقة.
- المساعدة في التحقيق في العيوب والإبلاغ عنها، بما في ذلك في عمليات التكامل مع الأنظمة السريرية.
- استخدام بيانات اختبار اصطناعية واتباع قواعد حوكمة المعلومات في بيئات الاختبار.
- تعلّم أدوات الاختبار لدى الفريق وممارسات الشيفرة وعملية السلامة السريرية.

### المهارات

| المهارة | المصدر | المستوى المتوقع | معنى هذا المستوى |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../المهارات/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | إلمام | You can:<br>• explain why it's important to communicate technical concepts in non-technical language<br>• explain the types of communication that can be used with internal and external stakeholders, and their impact |
| [Designing and executing tests](../../المهارات/#designing-and-executing-tests) | UK GDaD PCF | إلمام | You can:<br>• contribute to deciding the most appropriate test types and techniques to use<br>• follow guidance to design, build and maintain simple tests that align to user needs and requirements<br>• execute simple tests with support<br>• explain the value of automation within testing |
| [Managing, reporting and resolving defects](../../المهارات/#managing-reporting-and-resolving-defects) | UK GDaD PCF | إلمام | You can:<br>• explain how to report and track defects<br>• follow a defect management process to report, communicate and maintain defects with appropriate information<br>• retest and escalate defects when needed |
| [Test analysis](../../المهارات/#test-analysis) | UK GDaD PCF | إلمام | You can:<br>• describe quality characteristics and explain why they are important<br>• analyse information, such as user stories, prototypes, processes and designs, with support<br>• explain what might be a risk in achieving quality goals |
| [Test and quality planning](../../المهارات/#test-and-quality-planning) | UK GDaD PCF | إلمام | You can:<br>• explain the value of quality testing approaches, plans and strategies<br>• explain how different delivery methodologies affect quality testing approaches, plans and strategies<br>• follow quality testing approaches, plans and strategies, with support<br>• explain how to measure the effectiveness of quality testing approaches, plans and strategies, and why it’s important |
| [Test engineering](../../المهارات/#test-engineering) | UK GDaD PCF | إلمام | You can:<br>• explain why testing processes, environments and tools are important<br>• follow test engineering practices and standards, with support<br>• support the maintenance of automated tests and tools required for testing |
| [فهم خدمات الصحة والرعاية](../../المهارات/#فهم-خدمات-الصحة-والرعاية) | هذا المرجع | إلمام | يمكنك:<br>• وصف الأجزاء الرئيسية لمنظومة الصحة والرعاية والخدمات التي تدعمها المؤسسة<br>• شرح أهمية سلامة المرضى والسرية في عملك |
| [إدارة المخاطر السريرية](../../المهارات/#إدارة-المخاطر-السريرية) | هذا المرجع | إلمام | يمكنك:<br>• شرح كيف قد تضر أنظمة تقنية المعلومات الصحية بالمرضى، مثلًا من خلال معلومات خاطئة أو ناقصة أو متأخرة<br>• الإبلاغ عن مشكلة محتملة في السلامة السريرية عبر القناة الصحيحة |
| [حوكمة المعلومات وحماية البيانات](../../المهارات/#حوكمة-المعلومات-وحماية-البيانات) | هذا المرجع | إلمام | يمكنك:<br>• اتباع قواعد المؤسسة في التعامل مع المعلومات الشخصية والصحية<br>• التعرف على خرق للبيانات أو حادث كاد أن يقع والإبلاغ عنه |

### المؤهلات والخبرة المعتادة

- بعض الخبرة في البرمجة أو الاختبار، أو الالتحاق بتدريب مهني ذي صلة، أو ما يعادل ذلك.

### وصف الفئة

- **المعرفة:** معرفة تفصيلية بمجال العمل، عادةً من درجة تأسيسية أو تدريب مهني أو خبرة معادلة.
- **الاستقلالية:** يعمل ضمن إرشادات؛ ويحل معظم المشكلات اليومية؛ ويكون المدير متاحًا للمشورة.
- **النطاق:** عمله الخاص وخدمة أو عملية محددة.
- **القيادة:** قد يشرف على فريق صغير أو ينسق عمل الآخرين.
- **المساءلة:** تقديم خدمة أو عملية محددة.

### تقييم الوظيفة (توضيحي)

| # | العامل | المستوى | النقاط |
| --- | --- | --- | --- |
| 1 | مهارات التواصل وبناء العلاقات | 3 | 21 |
| 2 | المعرفة والتدريب والخبرة | 4 | 88 |
| 3 | مهارات التحليل والتقدير | 3 | 27 |
| 4 | مهارات التخطيط والتنظيم | 2 | 15 |
| 5 | المهارات البدنية | 3 | 27 |
| 6 | المسؤولية عن رعاية المرضى والعملاء | 1 | 4 |
| 7 | المسؤولية عن تطوير السياسات والخدمات | 2 | 12 |
| 8 | المسؤولية عن الموارد المالية والمادية | 1 | 5 |
| 9 | المسؤولية عن الأفراد | 1 | 5 |
| 10 | المسؤولية عن موارد المعلومات | 3 | 16 |
| 11 | المسؤولية عن البحث والتطوير | 2 | 12 |
| 12 | حرية التصرف | 2 | 12 |
| 13 | الجهد البدني | 2 | 7 |
| 14 | الجهد الذهني | 3 | 12 |
| 15 | الجهد العاطفي | 1 | 5 |
| 16 | ظروف العمل | 2 | 7 |
| | **المجموع** | | **275** (الفئة 4: 271–325) |

## الفئة 6: مهندس اختبار

**مستوى UK GDaD PCF: Test engineer**

> A test engineer develops solutions to enable more efficient testing. They follow engineering standards to design and execute appropriate technical tests.
> 
> At this role level, you will:
> - determine test scope and estimate the effort required
> - select and use the most appropriate test approaches and techniques to mitigate risk
> - use technical tooling and engineering approaches to design and execute tests
> - develop and maintain technical test suites
> - develop reports, record outcomes and support the resolution of defects
> - contribute to and follow engineering practices and standards

### المسؤوليات

- تصميم اختبارات مؤتمتة للوظائف والتكامل وواجهات البرمجة وبناؤها للخدمات السريرية والموجهة للمرضى.
- بناء اختبارات تتحقق من الرسائل مقابل ملفات HL7 FHIR التعريفية وغيرها من مواصفات التشغيل البيني.
- توليد بيانات مرضى اصطناعية تغطي الحالات السريرية الواقعية والحدّية.
- إضافة الاختبارات إلى خطوط التسليم حتى تعمل الفحوص المتعلقة بالسلامة مع كل تغيير.
- تقدير جهد الاختبار، والإبلاغ عن النتائج، ودعم حل العيوب.

### المهارات

| المهارة | المصدر | المستوى المتوقع | معنى هذا المستوى |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../المهارات/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | ممارسة | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Designing and executing tests](../../المهارات/#designing-and-executing-tests) | UK GDaD PCF | ممارسة | You can:<br>• set up suitable environments with some support<br>• select appropriate test types and techniques with some support<br>• design, build, maintain and execute tests that align to user needs and requirements<br>• conduct exploratory testing<br>• research and try new test types and techniques |
| [Managing, reporting and resolving defects](../../المهارات/#managing-reporting-and-resolving-defects) | UK GDaD PCF | ممارسة | You can:<br>• collaborate with others to create a defect management process to report, communicate and resolve defects, with support<br>• critically assess dependencies, defects and risks, with support<br>• contribute to mitigation and contingency plans<br>• clearly communicate risks and the impact of defects to stakeholders |
| [Test analysis](../../المهارات/#test-analysis) | UK GDaD PCF | ممارسة | You can:<br>• work with stakeholders to determine which functional and non-functional quality characteristics add value<br>• determine what to test following an agreed approach<br>• identify and advocate for test needs, such as data, access and environments, with support<br>• analyse information to identify risks |
| [Test and quality planning](../../المهارات/#test-and-quality-planning) | UK GDaD PCF | ممارسة | You can:<br>• create or adapt quality testing approaches based on risk, with some support<br>• follow a quality testing strategy and contribute to its development<br>• contribute to continuous improvement of quality testing approaches, plans and strategies |
| [Test engineering](../../المهارات/#test-engineering) | UK GDaD PCF | ممارسة | You can:<br>• use test engineering frameworks and tools to support testing activities<br>• follow test engineering practices and standards, such as source control and continuous integration, continuous delivery (CI/CD) pipelines<br>• integrate and execute tests to ensure early testing and continuous feedback<br>• create and maintain automated tests, with some support<br>• write and review coded solutions, with some support |
| [فهم خدمات الصحة والرعاية](../../المهارات/#فهم-خدمات-الصحة-والرعاية) | هذا المرجع | ممارسة | يمكنك:<br>• شرح مسارات العمل السريرية ومسارات الرعاية التي يدعمها عملك<br>• استخدام المصطلحات الصحية الشائعة استخدامًا صحيحًا مع الزملاء السريريين وزملاء الرعاية<br>• إدراك متى قد يؤثر تغيير ما في رعاية المرضى والتنبيه إليه |
| [إدارة المخاطر السريرية](../../المهارات/#إدارة-المخاطر-السريرية) | هذا المرجع | ممارسة | يمكنك:<br>• المشاركة في ورش تحديد المخاطر والإسهام في سجل المخاطر<br>• اتباع عملية إدارة المخاطر السريرية في عملك<br>• تقديم أدلة لملف السلامة السريرية، مثل نتائج الاختبارات |
| [حوكمة المعلومات وحماية البيانات](../../المهارات/#حوكمة-المعلومات-وحماية-البيانات) | هذا المرجع | ممارسة | يمكنك:<br>• تطبيق مبادئ حماية البيانات في عملك<br>• الإسهام في تقييمات أثر حماية البيانات<br>• التعامل مع طلبات المعلومات والسجلات بشكل صحيح |
| [التشغيل البيني للبيانات الصحية](../../المهارات/#التشغيل-البيني-للبيانات-الصحية) | هذا المرجع | ممارسة | يمكنك:<br>• قراءة موارد FHIR وملفاتها التعريفية وواجهاتها البرمجية واستخدامها<br>• بناء عمليات تكامل بسيطة أو اختبارها بتوجيه<br>• التحقق من الرسائل مقابل مواصفة |

### المؤهلات والخبرة المعتادة

- درجة جامعية في الحوسبة أو مجال ذي صلة، أو خبرة معادلة.
- خبرة في بناء الاختبارات المؤتمتة.

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
| 10 | المسؤولية عن موارد المعلومات | 4 | 24 |
| 11 | المسؤولية عن البحث والتطوير | 2 | 12 |
| 12 | حرية التصرف | 4 | 32 |
| 13 | الجهد البدني | 1 | 3 |
| 14 | الجهد الذهني | 4 | 18 |
| 15 | الجهد العاطفي | 1 | 5 |
| 16 | ظروف العمل | 2 | 7 |
| | **المجموع** | | **411** (الفئة 6: 396–465) |

## الفئة 7: مهندس اختبار أول

**مستوى UK GDaD PCF: Senior test engineer**

> A senior test engineer is responsible for test engineering in their area. They influence, coach and guide others in test engineering, sharing best practice and standards.
> 
> At this role level, you will:
> - select, use and guide others in using the most appropriate technical tooling, engineering approaches, test types and techniques to identify and address risks early
> - extend, standardise and build reusable frameworks and tools that support testing
> - communicate and document chosen approaches, tools, techniques and outcomes to the team and appropriate stakeholders
> - contribute to and agree engineering standards

### المسؤوليات

- قيادة هندسة الاختبار لمجال ما، واختيار الأدوات والأطر وأنواع الاختبار التي تعالج مخاطره مبكرًا.
- بناء أطر اختبار ومحاكيات قابلة لإعادة الاستخدام للأنظمة السريرية وعمليات التكامل مع الشركاء.
- التخطيط لاختبارات الأداء والحِمل والمرونة القائمة على الطلب السريري الحقيقي وإجراؤها.
- ضمان أن ترتبط الاختبارات المؤتمتة بالمخاطر وضوابط السلامة وأن تنتج أدلة لملفات السلامة.
- توجيه مهندسي الاختبار الآخرين وإرشادهم، والاتفاق على المعايير الهندسية مع المطورين.

### المهارات

| المهارة | المصدر | المستوى المتوقع | معنى هذا المستوى |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../المهارات/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | تمكّن | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Designing and executing tests](../../المهارات/#designing-and-executing-tests) | UK GDaD PCF | تمكّن | You can:<br>• set up suitable environments<br>• influence and guide the use of appropriate test types and techniques to mitigate risk early<br>• lead others in designing, building, maintaining and executing tests that align to user needs and requirements<br>• contribute to developing and implementing standards for designing and executing tests<br>• improve test types and techniques through a structured process. |
| [Managing, reporting and resolving defects](../../المهارات/#managing-reporting-and-resolving-defects) | UK GDaD PCF | تمكّن | You can:<br>• contribute to developing standards for defect management processes<br>• manage and escalate dependencies, defects and risks across teams<br>• contribute to mitigation and contingency plans across teams<br>• use defect patterns and trends to make recommendations on testing and quality approaches, with support<br>• manage stakeholder expectations and communications during defect resolution |
| [Test analysis](../../المهارات/#test-analysis) | UK GDaD PCF | تمكّن | You can:<br>• lead work with stakeholders across teams to determine which functional and non-functional quality characteristics add value<br>• determine if an approach needs to change based on effort and risk<br>• ensure test needs are implemented early<br>• use multiple techniques to analyse complex information to identify risks<br>• coach others in test analysis |
| [Test and quality planning](../../المهارات/#test-and-quality-planning) | UK GDaD PCF | تمكّن | You can:<br>• work with teams to develop and implement appropriate quality testing approaches, plans and strategies<br>• contribute to organisational quality testing strategies<br>• implement ways to capture data to drive continuous improvement of quality testing approaches, plans and strategies<br>• advocate for full team ownership of quality testing activities, encouraging early engagement |
| [Test engineering](../../المهارات/#test-engineering) | UK GDaD PCF | تمكّن | You can:<br>• develop, standardise and extend reusable frameworks and tools to support a range of testing activities<br>• guide and coach others in creating and maintaining comprehensive and reliable tests that meet standards<br>• research and prepare for future testing needs, including tools, methodologies and techniques<br>• maintain and adapt continuous integration, continuous delivery (CI/CD) pipelines |
| [فهم خدمات الصحة والرعاية](../../المهارات/#فهم-خدمات-الصحة-والرعاية) | هذا المرجع | ممارسة | يمكنك:<br>• شرح مسارات العمل السريرية ومسارات الرعاية التي يدعمها عملك<br>• استخدام المصطلحات الصحية الشائعة استخدامًا صحيحًا مع الزملاء السريريين وزملاء الرعاية<br>• إدراك متى قد يؤثر تغيير ما في رعاية المرضى والتنبيه إليه |
| [إدارة المخاطر السريرية](../../المهارات/#إدارة-المخاطر-السريرية) | هذا المرجع | ممارسة | يمكنك:<br>• المشاركة في ورش تحديد المخاطر والإسهام في سجل المخاطر<br>• اتباع عملية إدارة المخاطر السريرية في عملك<br>• تقديم أدلة لملف السلامة السريرية، مثل نتائج الاختبارات |
| [حوكمة المعلومات وحماية البيانات](../../المهارات/#حوكمة-المعلومات-وحماية-البيانات) | هذا المرجع | ممارسة | يمكنك:<br>• تطبيق مبادئ حماية البيانات في عملك<br>• الإسهام في تقييمات أثر حماية البيانات<br>• التعامل مع طلبات المعلومات والسجلات بشكل صحيح |
| [التشغيل البيني للبيانات الصحية](../../المهارات/#التشغيل-البيني-للبيانات-الصحية) | هذا المرجع | تمكّن | يمكنك:<br>• تصميم عمليات تكامل وبناؤها باستخدام FHIR وHL7 الإصدار 2 وأنماط المراسلة<br>• كتابة موارد FHIR وتعريف ملفاتها وأدلة تطبيقها<br>• حل مشكلات الربط وجودة البيانات المعقدة بين الأنظمة |
| [تنظيم البرمجيات بوصفها أجهزة طبية](../../المهارات/#تنظيم-البرمجيات-بوصفها-أجهزة-طبية) | هذا المرجع | إلمام | يمكنك:<br>• شرح أن بعض البرمجيات الصحية تُنظَّم بوصفها أجهزة طبية<br>• معرفة من تسأل عندما قد يكون منتج ما جهازًا طبيًا |

### المؤهلات والخبرة المعتادة

- خبرة واسعة في هندسة الاختبار، بمستوى يعادل درجة الماجستير.

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

## الفئة 8a: مهندس اختبار قائد

**مستوى UK GDaD PCF: Lead test engineer**

> A lead test engineer sets the strategy for test engineering and influences test engineering practices across a broad area. They develop, monitor and evaluate quality engineering standards, and make strategic improvements to quality engineering in the organisation.
> 
> At this role level, you will:
> - lead a broad area in technical tooling, engineering approaches and test types and techniques to address risks early
> - define engineering standards, enabling others to follow them
> - lead and guide teams in quality engineering strategies and practices
> - lead and guide test engineers
> - escalate risks to senior stakeholders
> - lead and implement continuous testing, identifying opportunities to test earlier

### المسؤوليات

- وضع استراتيجية هندسة الاختبار ومعاييرها عبر مجال واسع، بما في ذلك الاختبار المستمر في خطوط التسليم.
- قيادة مهندسي الاختبار والفرق وتوجيههم في ممارسات هندسة الجودة.
- ضمان أن يستوفي اختبار البرمجيات الخاضعة للتنظيم والحرجة للسلامة المعايير المطلوبة وأن يكون قابلًا للتتبع.
- تصعيد مخاطر الجودة والسلامة إلى كبار قادة المنتجات والقادة السريريين وقادة الموردين.
- اكتشاف فرص الاختبار في وقت أبكر وبتكرار أكبر، وقياس أثر ذلك في الجودة.

### المهارات

| المهارة | المصدر | المستوى المتوقع | معنى هذا المستوى |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../المهارات/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | خبرة | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Designing and executing tests](../../المهارات/#designing-and-executing-tests) | UK GDaD PCF | خبرة | You can:<br>• set standards and influence organisational decisions for test types, techniques, design and execution<br>• coach others in test types, techniques, design and execution<br>• advocate for continuous improvement and refinement of test types and techniques<br>• make strategic decisions on new or improved test types and techniques used in your area |
| [Managing, reporting and resolving defects](../../المهارات/#managing-reporting-and-resolving-defects) | UK GDaD PCF | خبرة | You can:<br>• lead and coach others in improving test and defect management processes<br>• support others in assessing complex and challenging defects across the organisation<br>• lead and coach others in using defect patterns and trends to make tactical and strategic recommendations<br>• influence improvements to quality processes, informed by defect patterns and trends |
| [Test analysis](../../المهارات/#test-analysis) | UK GDaD PCF | خبرة | You can:<br>• lead and guide multiple teams in test analysis, ensuring it is implemented early in the life cycle<br>• advocate for risk-based analysis to drive improvements across many teams<br>• set standards and principles for test analysis across the organisation |
| [Test and quality planning](../../المهارات/#test-and-quality-planning) | UK GDaD PCF | خبرة | You can:<br>• create and manage multiple quality testing plans, approaches and strategies<br>• lead and guide multiple teams in adopting quality testing strategy<br>• advocate for early quality testing involvement in organisational delivery processes<br>• guide teams across an organisation in optimising quality testing approaches, plans and strategies by using appropriate data |
| [Test engineering](../../المهارات/#test-engineering) | UK GDaD PCF | خبرة | You can:<br>• establish and lead test engineering practices, standards and behaviours<br>• influence and guide test engineering technology and tool choices across the organisation<br>• advocate for the adoption and use of appropriate testing solutions, ensuring alignment with organisational goals and quality objectives |
| [فهم خدمات الصحة والرعاية](../../المهارات/#فهم-خدمات-الصحة-والرعاية) | هذا المرجع | تمكّن | يمكنك:<br>• تحليل موقع خدمة ما ضمن مسارات الرعاية بين المؤسسات<br>• العمل مع الممارسين السريريين وموظفي الرعاية والمرضى لتشكيل الخدمات الرقمية<br>• شرح أثر القرارات الرقمية في الرعاية والسلامة وعبء العمل على الموظفين |
| [إدارة المخاطر السريرية](../../المهارات/#إدارة-المخاطر-السريرية) | هذا المرجع | تمكّن | يمكنك:<br>• قيادة تحديد المخاطر وتقييمها لمنتج أو تغيير<br>• كتابة سجلات المخاطر وتقارير ملفات السلامة السريرية وتحديثها<br>• الاتفاق مع فرق المنتجات على ضوابط المخاطر والتحقق من فعاليتها<br>• تقديم المشورة للفرق بشأن تطبيق معايير إدارة المخاطر السريرية |
| [حوكمة المعلومات وحماية البيانات](../../المهارات/#حوكمة-المعلومات-وحماية-البيانات) | هذا المرجع | ممارسة | يمكنك:<br>• تطبيق مبادئ حماية البيانات في عملك<br>• الإسهام في تقييمات أثر حماية البيانات<br>• التعامل مع طلبات المعلومات والسجلات بشكل صحيح |
| [التشغيل البيني للبيانات الصحية](../../المهارات/#التشغيل-البيني-للبيانات-الصحية) | هذا المرجع | تمكّن | يمكنك:<br>• تصميم عمليات تكامل وبناؤها باستخدام FHIR وHL7 الإصدار 2 وأنماط المراسلة<br>• كتابة موارد FHIR وتعريف ملفاتها وأدلة تطبيقها<br>• حل مشكلات الربط وجودة البيانات المعقدة بين الأنظمة |
| [تنظيم البرمجيات بوصفها أجهزة طبية](../../المهارات/#تنظيم-البرمجيات-بوصفها-أجهزة-طبية) | هذا المرجع | ممارسة | يمكنك:<br>• اتباع عملية لدورة حياة البرمجيات تستوفي معايير الأجهزة الطبية<br>• إعداد السجلات التي تتطلبها تلك العملية |
| [إدارة الأفراد](../../المهارات/#إدارة-الأفراد) | هذا المرجع | ممارسة | يمكنك:<br>• الإشراف على العمل اليومي وتقديم الملاحظات<br>• المشاركة في التوظيف والتعريف بالعمل<br>• إجراء محادثات فردية منتظمة |

### المؤهلات والخبرة المعتادة

- خبرة واسعة في قيادة هندسة الاختبار للخدمات المعقدة.

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
| 8 | المسؤولية عن الموارد المالية والمادية | 1 | 5 |
| 9 | المسؤولية عن الأفراد | 3 | 21 |
| 10 | المسؤولية عن موارد المعلومات | 5 | 34 |
| 11 | المسؤولية عن البحث والتطوير | 3 | 21 |
| 12 | حرية التصرف | 5 | 45 |
| 13 | الجهد البدني | 1 | 3 |
| 14 | الجهد الذهني | 4 | 18 |
| 15 | الجهد العاطفي | 1 | 5 |
| 16 | ظروف العمل | 2 | 7 |
| | **المجموع** | | **553** (الفئة 8a: 540–584) |

يقترح UK GDaD PCF الدرجات من SEO إلى G6 لهذا المستوى، وهو ما يقابل الفئة 7، فئة مهندس الاختبار الأول نفسها. ويضعه هذا المرجع في الفئة 8a، لأنه يضع استراتيجية هندسة الاختبار ومعاييرها عبر مجال واسع.


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
