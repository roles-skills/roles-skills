# مهندس معماري للبيانات

> هذا ملف مرجعي توضيحي لمؤسسة رعاية صحية رقمية عامة. وهو ليس وصفًا وظيفيًا رسميًا لأي جهة عمل، ونقاط تقييم الوظائف فيه ليست تقييمًا رسميًا.

> تُرجم هذا النص من الإنجليزية بواسطة مساعد ذكاء اصطناعي، ولم يراجعه بعدُ متحدث أصلي باللغة. تبقى الاقتباسات من إطار قدرات مهنة الرقمنة والبيانات في الحكومة البريطانية (UK GDaD PCF) ومن ESCO باللغة الإنجليزية.

**العائلة:** [الهندسة المعمارية للأنظمة](../../#الهندسة-المعمارية-للأنظمة)  
**الفئات:** 8a, 8b, 8c  
**دور UK GDaD PCF:** [Data architect](https://understand-digital-data-roles-skills.service.gov.uk/role/data-architect/)  
**مهن ESCO:** [database designer](http://data.europa.eu/esco/occupation/8d9ec84d-cf2d-4179-87bc-335cda54a427) (ISCO-08 2521); [data warehouse designer](http://data.europa.eu/esco/occupation/1562c7a3-c7d9-419d-b9b6-db26610bcf84) (ISCO-08 2521)

## الملخص

يصمم المهندسون المعماريون للبيانات كيفية هيكلة المؤسسة لبيانات الصحة والرعاية وتخزينها ونقلها وحوكمتها، حتى يمكن استخدامها بأمان للرعاية المباشرة وتخطيط الخدمات والبحث. وهم يصممون نماذج البيانات ومنصاتها وتدفقاتها، ويضعون معايير البيانات، ويضمنون الحفاظ على المعنى السريري والجودة والسرية من طرف إلى طرف.

## في مؤسسة رعاية صحية رقمية

- يجب أن تحتفظ البيانات الصحية بمعناها السريري، لذلك تستخدم نماذج البيانات مصطلحات سريرية مثل SNOMED CT وتصنيفات مثل ICD.
- للبيانات المستخدمة في الرعاية المباشرة والبيانات المستخدمة في التخطيط أو البحث أسس قانونية مختلفة، لذلك يصمم المهندسون المعماريون للفصل وإزالة الهوية والوصول المضبوط.
- تأتي البيانات من أنظمة سريرية وأنظمة رعاية كثيرة متفاوتة الجودة، لذلك يصمم المهندسون المعماريون لفحوص جودة البيانات ومطابقة المرضى وتتبع مصدر البيانات.
- تعتمد سجلات الرعاية المشتركة وتبادل البيانات على نماذج مشتركة مثل موارد HL7 FHIR ومجموعات البيانات الوطنية أو الدولية المتفق عليها.
- يجب الاحتفاظ بالسجلات لفترات طويلة، لذلك يجب أن تخطط التصاميم للأرشفة والوصول إلى البيانات التاريخية.

## وصف الدور في UK GDaD PCF (النص الإنجليزي الأصلي)

> A data architect sets the vision for the organisation’s use of data, through data design, to ensure that data is managed properly and meets the organisation’s needs.

## مستويات الدور

| الفئة | المسمى | مستوى UK GDaD PCF | درجات الخدمة المدنية البريطانية | نقاط تقييم الوظيفة |
| --- | --- | --- | --- | --- |
| 8a | [مهندس معماري للبيانات](#الفئة-8a-مهندس-معماري-للبيانات) | Data architect | SEO/G7 | 560 |
| 8b | [مهندس معماري أول للبيانات](#الفئة-8b-مهندس-معماري-أول-للبيانات) | Senior data architect | G7/G6 | 613 |
| 8c | [كبير المهندسين المعماريين للبيانات](#الفئة-8c-كبير-المهندسين-المعماريين-للبيانات) | Chief data architect | G6 | 662 |

## الفئة 8a: مهندس معماري للبيانات

**مستوى UK GDaD PCF: Data architect**

> A data architect designs and builds data models to fulfil the strategic data needs of the organisation, as defined by chief data architects.
> 
> At this role level, you will:
> - design, support and provide guidance for the upgrade, management, decommission and archive of data in compliance with data policy
> - provide input into data dictionaries
> - define and maintain the data technology architecture, including metadata, integration and business intelligence or data warehouse architecture

### المسؤوليات

- تصميم نماذج البيانات المنطقية والمادية للبيانات السريرية والتشغيلية، باستخدام المصطلحات السريرية حيث يلزم.
- تصميم تدفقات البيانات ومكونات منصات البيانات، مثل طبقات المستودع وبحيرة البيانات والتكامل.
- تحديد البيانات الوصفية ومداخل قاموس البيانات وتتبع المصدر لمجموعات البيانات في مجالك.
- تصميم ضوابط إزالة الهوية والوصول حتى لا تُستخدم البيانات إلا لغرضها القانوني.
- العمل مع زملاء جودة البيانات والترميز السريري لمعالجة الأسباب البنيوية لضعف البيانات.
- توجيه مهندسي البيانات والمحللين بشأن نماذج البيانات ومعاييرها.

### المهارات

| المهارة | المصدر | المستوى المتوقع | معنى هذا المستوى |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../المهارات/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | ممارسة | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Communicating data](../../المهارات/#communicating-data) | UK GDaD PCF | إلمام | You can:<br>• show an awareness that data needs to be aligned to the needs of the end user<br>• create basic visuals and presentations |
| [Data analysis and synthesis](../../المهارات/#data-analysis-and-synthesis) | UK GDaD PCF | ممارسة | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../المهارات/#data-governance-data-architect) | UK GDaD PCF | ممارسة | You can:<br>• understand what data governance is required<br>• take responsibility for the assurance of data solutions and make recommendations to ensure compliance |
| [Data innovation](../../المهارات/#data-innovation) | UK GDaD PCF | إلمام | You can:<br>• develop a basic understanding of an unfamiliar or emerging technology, or a familiar technology in a new data context, with guidance<br>• share what you learn with colleagues, including how it could help deliver more value from data |
| [Data modelling](../../المهارات/#data-modelling) | UK GDaD PCF | ممارسة | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Data standards](../../المهارات/#data-standards) | UK GDaD PCF | ممارسة | You can:<br>• use data policies, processes and standards effectively<br>• work with subject matter experts to develop standards, policies and guidance to protect data<br>• monitor compliance with policies and standards in a team and take action if needed<br>• analyse the impact if a standard is breached |
| [Metadata management](../../المهارات/#metadata-management) | UK GDaD PCF | ممارسة | You can:<br>• use metadata repositories to complete complex tasks such as data and systems integration impact analysis<br>• maintain a metadata repository to ensure information remains accurate and up to date |
| [Problem management](../../المهارات/#problem-management) | UK GDaD PCF | ممارسة | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Strategic thinking](../../المهارات/#strategic-thinking) | UK GDaD PCF | إلمام | You can:<br>• explain the strategic context of your work and why it is important<br>• support strategic planning in an administrative capacity |
| [Turning business problems into data design](../../المهارات/#turning-business-problems-into-data-design) | UK GDaD PCF | ممارسة | You can:<br>• design data architecture by dealing with specific business problems and aligning it to enterprise-wide standards and principles<br>• work within the context of well understood architecture, and identify appropriate patterns |
| [فهم خدمات الصحة والرعاية](../../المهارات/#فهم-خدمات-الصحة-والرعاية) | هذا المرجع | ممارسة | يمكنك:<br>• شرح مسارات العمل السريرية ومسارات الرعاية التي يدعمها عملك<br>• استخدام المصطلحات الصحية الشائعة استخدامًا صحيحًا مع الزملاء السريريين وزملاء الرعاية<br>• إدراك متى قد يؤثر تغيير ما في رعاية المرضى والتنبيه إليه |
| [المصطلحات والتصنيفات السريرية](../../المهارات/#المصطلحات-والتصنيفات-السريرية) | هذا المرجع | ممارسة | يمكنك:<br>• إيجاد الرموز الصحيحة لعنصر بيانات أو نموذج واستخدامها<br>• استخدام متصفحات المصطلحات والمجموعات المرجعية |
| [التشغيل البيني للبيانات الصحية](../../المهارات/#التشغيل-البيني-للبيانات-الصحية) | هذا المرجع | تمكّن | يمكنك:<br>• تصميم عمليات تكامل وبناؤها باستخدام FHIR وHL7 الإصدار 2 وأنماط المراسلة<br>• كتابة موارد FHIR وتعريف ملفاتها وأدلة تطبيقها<br>• حل مشكلات الربط وجودة البيانات المعقدة بين الأنظمة |
| [حوكمة المعلومات وحماية البيانات](../../المهارات/#حوكمة-المعلومات-وحماية-البيانات) | هذا المرجع | تمكّن | يمكنك:<br>• قيادة تقييمات أثر حماية البيانات واتفاقيات تبادل المعلومات<br>• تقديم المشورة للفرق بشأن الأساس القانوني والموافقة والسرية ومدد الاحتفاظ<br>• التحقيق في الحوادث والتوصية بالتحسينات |
| [إدارة جودة البيانات](../../المهارات/#إدارة-جودة-البيانات) | هذا المرجع | ممارسة | يمكنك:<br>• إجراء فحوص جودة البيانات وتصحيح الأخطاء<br>• شرح تقارير جودة البيانات للزملاء |

### المؤهلات والخبرة المعتادة

- خبرة واسعة في نمذجة البيانات وتصميم منصاتها، بمستوى يعادل درجة الماجستير.

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
| 11 | المسؤولية عن البحث والتطوير | 3 | 21 |
| 12 | حرية التصرف | 5 | 45 |
| 13 | الجهد البدني | 1 | 3 |
| 14 | الجهد الذهني | 4 | 18 |
| 15 | الجهد العاطفي | 1 | 5 |
| 16 | ظروف العمل | 2 | 7 |
| | **المجموع** | | **560** (الفئة 8a: 540–584) |

مصنّف فوق الفئة المقترحة من درجة UK GDaD PCF (الفئة 7): تضع إعلانات القطاع الصحي هذا الدور في الفئة 8a. ويُقدَّر التخطيط والسياسات وحرية التصرف فوق ملف الفئة 7 لأن الوظيفة تصمم منصات بيانات وضوابط تستخدمها خدمات كثيرة.

## الفئة 8b: مهندس معماري أول للبيانات

**مستوى UK GDaD PCF: Senior data architect**

> A senior data architect delivers the vision for the organisation as set by the chief data architect.
> 
> At this role level, you will:
> - design data models and metadata systems
> - help chief data architects to interpret an organisation’s needs
> - provide oversight and advice to other data architects who are designing and producing data artefacts
> - design and support the management of data dictionaries
> - make sure that your teams are working to the standards set for the organisation by the chief data architects
> - work with technical architects to make sure that an organisation’s systems are designed in accordance with the appropriate data architecture

### المسؤوليات

- تصميم الهندسة المعمارية للبيانات لمجال رئيسي، مثل سجل الرعاية المشترك أو منصة التحليلات.
- ضمان أن تتبع تصاميم البيانات عبر الفرق معايير البيانات ونماذجها في المؤسسة.
- تصميم كيفية مشاركة البيانات مع المؤسسات الشريكة، بما في ذلك المعايير والضوابط واتفاقيات تبادل البيانات.
- تقديم المشورة لزملاء حوكمة المعلومات والسلامة السريرية بشأن مخاطر البيانات في التصاميم الجديدة.
- مراجعة عمل المهندسين المعماريين للبيانات وتوجيهه.

### المهارات

| المهارة | المصدر | المستوى المتوقع | معنى هذا المستوى |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../المهارات/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | تمكّن | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Communicating data](../../المهارات/#communicating-data) | UK GDaD PCF | ممارسة | You can:<br>• understand the appropriate media to communicate findings<br>• shape communications for the audience |
| [Data analysis and synthesis](../../المهارات/#data-analysis-and-synthesis) | UK GDaD PCF | ممارسة | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../المهارات/#data-governance-data-architect) | UK GDaD PCF | تمكّن | You can:<br>• evolve and define data governance<br>• take responsibility for supporting and collaborating around wider governance<br>• assure and integrate data services to meet the needs of multiple business services<br>• work proactively to ensure the organisation designs architecture that considers data |
| [Data innovation](../../المهارات/#data-innovation) | UK GDaD PCF | ممارسة | You can:<br>• experiment with unfamiliar and emerging technologies, or familiar technologies in new data contexts, with guidance<br>• share what you learn with the team, explaining potential benefits, risks, and practical considerations<br>• identify opportunities to apply technology to improve data processes or outcomes in an operational setting or the wider organisation |
| [Data modelling](../../المهارات/#data-modelling) | UK GDaD PCF | تمكّن | You can:<br>• produce relevant data models across multiple subject areas<br>• explain which models to use for which purpose<br>• understand industry-recognised data modelling patterns and standards, and when to apply them<br>• compare and align different data models |
| [Data standards](../../المهارات/#data-standards) | UK GDaD PCF | تمكّن | You can:<br>• create data standards for different subjects and ensure senior leaders understand them<br>• work with subject matter experts across the organisation to introduce data standards best practice<br>• monitor compliance with policies and standards in the organisation<br>• make recommendations about how the organisation should resolve breaches of standards |
| [Metadata management](../../المهارات/#metadata-management) | UK GDaD PCF | تمكّن | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../المهارات/#problem-management) | UK GDaD PCF | تمكّن | You can:<br>• ensure that the right actions are taken to investigate, resolve and anticipate problems<br>• co-ordinate the team to investigate problems, implement solutions and take preventive measures |
| [Strategic thinking](../../المهارات/#strategic-thinking) | UK GDaD PCF | ممارسة | You can:<br>• work within a strategic context and communicate how activities meet strategic goals<br>• contribute to the development of strategy and policies |
| [Turning business problems into data design](../../المهارات/#turning-business-problems-into-data-design) | UK GDaD PCF | تمكّن | You can:<br>• design data architecture that deals with problems spanning different business areas<br>• identify links between problems to devise common solutions<br>• work across multiple subject areas, or a single large or complicated subject area<br>• produce appropriate patterns |
| [فهم خدمات الصحة والرعاية](../../المهارات/#فهم-خدمات-الصحة-والرعاية) | هذا المرجع | تمكّن | يمكنك:<br>• تحليل موقع خدمة ما ضمن مسارات الرعاية بين المؤسسات<br>• العمل مع الممارسين السريريين وموظفي الرعاية والمرضى لتشكيل الخدمات الرقمية<br>• شرح أثر القرارات الرقمية في الرعاية والسلامة وعبء العمل على الموظفين |
| [المصطلحات والتصنيفات السريرية](../../المهارات/#المصطلحات-والتصنيفات-السريرية) | هذا المرجع | تمكّن | يمكنك:<br>• تصميم نماذج البيانات والمجموعات المرجعية باستخدام المصطلحات السريرية<br>• الربط بين المصطلحات والتصنيفات، وشرح حدود الربط<br>• تقديم المشورة للفرق بشأن استخدام المصطلحات في المنتجات والتحليلات |
| [التشغيل البيني للبيانات الصحية](../../المهارات/#التشغيل-البيني-للبيانات-الصحية) | هذا المرجع | تمكّن | يمكنك:<br>• تصميم عمليات تكامل وبناؤها باستخدام FHIR وHL7 الإصدار 2 وأنماط المراسلة<br>• كتابة موارد FHIR وتعريف ملفاتها وأدلة تطبيقها<br>• حل مشكلات الربط وجودة البيانات المعقدة بين الأنظمة |
| [حوكمة المعلومات وحماية البيانات](../../المهارات/#حوكمة-المعلومات-وحماية-البيانات) | هذا المرجع | تمكّن | يمكنك:<br>• قيادة تقييمات أثر حماية البيانات واتفاقيات تبادل المعلومات<br>• تقديم المشورة للفرق بشأن الأساس القانوني والموافقة والسرية ومدد الاحتفاظ<br>• التحقيق في الحوادث والتوصية بالتحسينات |
| [إدارة جودة البيانات](../../المهارات/#إدارة-جودة-البيانات) | هذا المرجع | تمكّن | يمكنك:<br>• تحديد قواعد جودة البيانات ومقاييسها<br>• العمل مع مزوّدي البيانات لمعالجة الأسباب الجذرية لضعف الجودة |
| [إدارة المخاطر السريرية](../../المهارات/#إدارة-المخاطر-السريرية) | هذا المرجع | ممارسة | يمكنك:<br>• المشاركة في ورش تحديد المخاطر والإسهام في سجل المخاطر<br>• اتباع عملية إدارة المخاطر السريرية في عملك<br>• تقديم أدلة لملف السلامة السريرية، مثل نتائج الاختبارات |
| [إدارة الأفراد](../../المهارات/#إدارة-الأفراد) | هذا المرجع | ممارسة | يمكنك:<br>• الإشراف على العمل اليومي وتقديم الملاحظات<br>• المشاركة في التوظيف والتعريف بالعمل<br>• إجراء محادثات فردية منتظمة |

### المؤهلات والخبرة المعتادة

- خبرة واسعة في الهندسة المعمارية للبيانات في المؤسسات المعقدة.

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
| 2 | المعرفة والتدريب والخبرة | 8 | 240 |
| 3 | مهارات التحليل والتقدير | 5 | 60 |
| 4 | مهارات التخطيط والتنظيم | 4 | 42 |
| 5 | المهارات البدنية | 2 | 15 |
| 6 | المسؤولية عن رعاية المرضى والعملاء | 1 | 4 |
| 7 | المسؤولية عن تطوير السياسات والخدمات | 4 | 32 |
| 8 | المسؤولية عن الموارد المالية والمادية | 3 | 21 |
| 9 | المسؤولية عن الأفراد | 3 | 21 |
| 10 | المسؤولية عن موارد المعلومات | 5 | 34 |
| 11 | المسؤولية عن البحث والتطوير | 3 | 21 |
| 12 | حرية التصرف | 5 | 45 |
| 13 | الجهد البدني | 1 | 3 |
| 14 | الجهد الذهني | 4 | 18 |
| 15 | الجهد العاطفي | 1 | 5 |
| 16 | ظروف العمل | 2 | 7 |
| | **المجموع** | | **613** (الفئة 8b: 585–629) |

## الفئة 8c: كبير المهندسين المعماريين للبيانات

**مستوى UK GDaD PCF: Chief data architect**

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

### المسؤوليات

- وضع رؤية الهندسة المعمارية للبيانات في المؤسسة وخارطة طريقها، بما يتوافق مع استراتيجية البيانات.
- تولّي نموذج البيانات المؤسسي ومعايير البيانات وقاموس البيانات في المؤسسة.
- تقديم المشورة للفريق التنفيذي وهيئات حوكمة البيانات بشأن الهندسة المعمارية للبيانات ومخاطرها والاستثمار فيها.
- تمثيل المؤسسة في أعمال معايير البيانات والتشغيل البيني المشتركة بين المؤسسات.
- قيادة ممارسة الهندسة المعمارية للبيانات وتطوير أفرادها.

### المهارات

| المهارة | المصدر | المستوى المتوقع | معنى هذا المستوى |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../المهارات/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | تمكّن | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Communicating data](../../المهارات/#communicating-data) | UK GDaD PCF | تمكّن | You can:<br>• turn complex data into clear and well understood solutions, which can be acted upon<br>• share data communication skills with the team and organisation<br>• understand and communicate different options, taking into account risks and uncertainties |
| [Data analysis and synthesis](../../المهارات/#data-analysis-and-synthesis) | UK GDaD PCF | ممارسة | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../المهارات/#data-governance-data-architect) | UK GDaD PCF | خبرة | You can:<br>• ensure data governance supports changes to the organisational strategy<br>• align data governance with wider governance (for example, budget)<br>• assure corporate services by understanding important risks and providing mitigation through assurance mechanisms |
| [Data innovation](../../المهارات/#data-innovation) | UK GDaD PCF | تمكّن | You can:<br>• test and evaluate the feasibility of unfamiliar and emerging technologies, or familiar technologies in new data contexts<br>• share what you learn with the organisation, explaining potential benefits, risks, and practical considerations<br>• recommend, design and implement innovative data solutions based on organisation objectives, user needs, and operational constraints |
| [Data modelling](../../المهارات/#data-modelling) | UK GDaD PCF | خبرة | You can:<br>• understand the concepts and principles of data modelling and can produce relevant data models<br>• work across government and industry, recognising opportunities for the reuse and alignment of data models in different organisations<br>• design the method to categorise data models within an organisation |
| [Data standards](../../المهارات/#data-standards) | UK GDaD PCF | خبرة | You can:<br>• create data standards for the organisation<br>• advocate for, and oversee compliance with, data policies and standards<br>• decide where standards need to be set across the organisation, and how to set them in the wider context of government |
| [Metadata management](../../المهارات/#metadata-management) | UK GDaD PCF | خبرة | You can:<br>• identify how metadata repositories can support different areas of the organisation<br>• communicate the value of metadata repositories<br>• set up robust governance processes to keep repositories up to date |
| [Problem management](../../المهارات/#problem-management) | UK GDaD PCF | خبرة | You can:<br>• anticipate problems and defend against them at the right time<br>• understand how a problem fits into the larger picture<br>• identify and describe problems, and help others to describe them<br>• build problem-solving capabilities in others |
| [Strategic thinking](../../المهارات/#strategic-thinking) | UK GDaD PCF | تمكّن | You can:<br>• define strategies and policies, providing guidance to others on working in the strategic context<br>• evaluate current strategies to ensure business requirements are being met and exceeded where possible |
| [Turning business problems into data design](../../المهارات/#turning-business-problems-into-data-design) | UK GDaD PCF | خبرة | You can:<br>• design data architecture that deals with problems across the enterprise<br>• work across all organisational subject areas and internal and external programmes |
| [فهم خدمات الصحة والرعاية](../../المهارات/#فهم-خدمات-الصحة-والرعاية) | هذا المرجع | خبرة | يمكنك:<br>• تشكيل استراتيجية المؤسسة بالاستناد إلى فهم عميق لمنظومة الصحة والرعاية<br>• تمثيل المؤسسة لدى شركاء الصحة والرعاية وقادتها<br>• توقّع أثر تغييرات السياسات والخدمات في الخدمات الرقمية والرعاية |
| [المصطلحات والتصنيفات السريرية](../../المهارات/#المصطلحات-والتصنيفات-السريرية) | هذا المرجع | تمكّن | يمكنك:<br>• تصميم نماذج البيانات والمجموعات المرجعية باستخدام المصطلحات السريرية<br>• الربط بين المصطلحات والتصنيفات، وشرح حدود الربط<br>• تقديم المشورة للفرق بشأن استخدام المصطلحات في المنتجات والتحليلات |
| [التشغيل البيني للبيانات الصحية](../../المهارات/#التشغيل-البيني-للبيانات-الصحية) | هذا المرجع | خبرة | يمكنك:<br>• وضع معايير التشغيل البيني واستراتيجيته للمؤسسة<br>• قيادة أعمال المعايير على المستوى الوطني أو بين المؤسسات<br>• ضمان تصميم عمليات التكامل الحرجة عبر أنظمة كثيرة |
| [حوكمة المعلومات وحماية البيانات](../../المهارات/#حوكمة-المعلومات-وحماية-البيانات) | هذا المرجع | خبرة | يمكنك:<br>• وضع سياسة حوكمة المعلومات واستراتيجيتها<br>• تقديم المشورة لمجلس الإدارة بشأن مخاطر المعلومات والامتثال<br>• تمثيل المؤسسة لدى الجهات التنظيمية والشركاء |
| [إدارة جودة البيانات](../../المهارات/#إدارة-جودة-البيانات) | هذا المرجع | تمكّن | يمكنك:<br>• تحديد قواعد جودة البيانات ومقاييسها<br>• العمل مع مزوّدي البيانات لمعالجة الأسباب الجذرية لضعف الجودة |
| [إدارة المخاطر السريرية](../../المهارات/#إدارة-المخاطر-السريرية) | هذا المرجع | تمكّن | يمكنك:<br>• قيادة تحديد المخاطر وتقييمها لمنتج أو تغيير<br>• كتابة سجلات المخاطر وتقارير ملفات السلامة السريرية وتحديثها<br>• الاتفاق مع فرق المنتجات على ضوابط المخاطر والتحقق من فعاليتها<br>• تقديم المشورة للفرق بشأن تطبيق معايير إدارة المخاطر السريرية |
| [إدارة الأفراد](../../المهارات/#إدارة-الأفراد) | هذا المرجع | تمكّن | يمكنك:<br>• الإدارة المباشرة لفريق، ووضع الأهداف وإجراء تقييمات الأداء<br>• دعم الرفاه وإدارة الحضور والأداء والسلوك<br>• التخطيط لتطوير الفريق وتعاقب أفراده |

### المؤهلات والخبرة المعتادة

- خبرة واسعة في قيادة الهندسة المعمارية للبيانات عبر المؤسسات.

### وصف الفئة

- **المعرفة:** معرفة خبيرة، وفهم واسع للمؤسسة والقطاع.
- **الاستقلالية:** يضع استراتيجية وظيفة ما؛ ويُساءَل أمام مدير.
- **النطاق:** وظيفة أو إدارة.
- **القيادة:** يقود وظيفة عبر عدة مستويات إدارية.
- **المساءلة:** أداء وظيفة ما وقوتها العاملة وميزانيتها.

### تقييم الوظيفة (توضيحي)

| # | العامل | المستوى | النقاط |
| --- | --- | --- | --- |
| 1 | مهارات التواصل وبناء العلاقات | 6 | 60 |
| 2 | المعرفة والتدريب والخبرة | 8 | 240 |
| 3 | مهارات التحليل والتقدير | 5 | 60 |
| 4 | مهارات التخطيط والتنظيم | 5 | 60 |
| 5 | المهارات البدنية | 2 | 15 |
| 6 | المسؤولية عن رعاية المرضى والعملاء | 1 | 4 |
| 7 | المسؤولية عن تطوير السياسات والخدمات | 5 | 45 |
| 8 | المسؤولية عن الموارد المالية والمادية | 3 | 21 |
| 9 | المسؤولية عن الأفراد | 3 | 21 |
| 10 | المسؤولية عن موارد المعلومات | 6 | 46 |
| 11 | المسؤولية عن البحث والتطوير | 2 | 12 |
| 12 | حرية التصرف | 5 | 45 |
| 13 | الجهد البدني | 1 | 3 |
| 14 | الجهد الذهني | 4 | 18 |
| 15 | الجهد العاطفي | 1 | 5 |
| 16 | ظروف العمل | 2 | 7 |
| | **المجموع** | | **662** (الفئة 8c: 630–674) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
