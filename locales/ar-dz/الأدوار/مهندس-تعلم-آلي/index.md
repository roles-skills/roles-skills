# مهندس تعلم آلي

> هذا ملف مرجعي توضيحي لمؤسسة رعاية صحية رقمية عامة. وهو ليس وصفًا وظيفيًا رسميًا لأي جهة عمل، ونقاط تقييم الوظائف فيه ليست تقييمًا رسميًا.

> تُرجم هذا النص من الإنجليزية بواسطة مساعد ذكاء اصطناعي، ولم يراجعه بعدُ متحدث أصلي باللغة. تبقى الاقتباسات من إطار قدرات مهنة الرقمنة والبيانات في الحكومة البريطانية (UK GDaD PCF) ومن ESCO باللغة الإنجليزية.

**العائلة:** [البيانات](../../#البيانات)  
**الفئات:** 7, 8b  
**دور UK GDaD PCF:** [Machine learning engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/machine-learning-engineer/)  
**مهن ESCO:** [artificial intelligence engineer](http://data.europa.eu/esco/occupation/35553663-deab-4d9a-bf22-15c1625d28e8) (ISCO-08 2511)

## الملخص

يأخذ مهندسو التعلم الآلي النماذج التي يبنيها علماء البيانات، أو التي تُشترى من الموردين، ويجعلونها تعمل بموثوقية في خدمات الصحة والرعاية الفعلية. وهم يبنون خطوط تدريب النماذج واختبارها ونشرها ومراقبتها، ويدمجونها مع الأنظمة السريرية والتشغيلية. ويضمنون أن تبقى النماذج آمنة ومحمية وعادلة وفعالة متى اعتمد عليها مرضى وموظفون حقيقيون.

## في مؤسسة رعاية صحية رقمية

- قد تنجرف النماذج أثناء الاستخدام الفعلي مع تغير فئات المرضى أو الممارسة السريرية أو عادات التسجيل، لذلك يُراقَب الأداء لكل فئة من المرضى ويُعاد تدريب النماذج أو تُسحب عند الحاجة.
- قد يُنظَّم نموذج يدعم التشخيص أو الفرز أو العلاج بوصفه جهازًا طبيًا، مما يفرض متطلبات رسمية لدورة حياة برمجياته وضبط التغيير والمراقبة بعد الطرح في السوق.
- تحتاج ملفات السلامة السريرية إلى أدلة على كيفية إخفاق النموذج، وكيفية عرض مخرجاته على الممارسين السريريين، وما يحدث حين يكون غير متاح.
- قد تسرّب النماذج المدرَّبة على بيانات المرضى معلومات عن أفراد، لذلك تُحمى بيانات التدريب ومخرجات النماذج والسجلات كما تُحمى البيانات نفسها.
- يجلب الذكاء الاصطناعي التوليدي والنماذج اللغوية الكبيرة مخاطر إضافية، مثل المحتوى المختلق في الملاحظات السريرية، تحتاج إلى اختبار خاص وإشراف بشري.

## وصف الدور في UK GDaD PCF (النص الإنجليزي الأصلي)

> A machine learning engineer develops, assures and maintains machine learning models so they can be used in products and services.
> 
> In this role, you will:
> - be responsible for the software development and technical infrastructure needed to design, train, deploy and scale machine learning models
> - provide and maintain effective, secure and sustainable machine learning models for use in products and services
> - support all stages of the machine learning life cycle
> - help product teams evaluate and choose appropriate machine learning solutions

## مستويات الدور

| الفئة | المسمى | مستوى UK GDaD PCF | درجات الخدمة المدنية البريطانية | نقاط تقييم الوظيفة |
| --- | --- | --- | --- | --- |
| 7 | [مهندس تعلم آلي أول](#الفئة-7-مهندس-تعلم-آلي-أول) | Senior machine learning engineer | SEO/G7/G6 | 495 |
| 8b | [مهندس تعلم آلي قائد](#الفئة-8b-مهندس-تعلم-آلي-قائد) | Lead machine learning engineer | G7/G6 | 595 |

## الفئة 7: مهندس تعلم آلي أول

**مستوى UK GDaD PCF: Senior machine learning engineer**

> A senior machine learning engineer develops machine learning models so they can be used in products and services.
> 
> At this role level, you will:
> - decide what model is most suitable for use in products and services
> - customise, optimise, re-train and maintain existing models
> - deploy models into production, testing and assuring them to ensure they meet performance requirements
> - work with others to integrate models with existing systems
> - check that models used in live products and services stay safe, secure and continue to work effectively

### المسؤوليات

- نشر النماذج في الخدمات السريرية والتشغيلية الإنتاجية، مع اختبار مؤتمت وضبط للإصدارات وإمكانية التراجع.
- بناء المراقبة لأداء النماذج وانجرافها وعدالتها بين فئات المرضى، مع تنبيهات ومسؤولين واضحين.
- دمج النماذج مع الأنظمة السريرية، باستخدام معايير مفتوحة مثل HL7 FHIR حيثما أمكن.
- إعداد أدلة الاختبار والتغيير والمراقبة اللازمة لملفات السلامة السريرية والملفات التقنية للأجهزة الطبية.
- تقييم نماذج الموردين والنماذج مفتوحة المصدر وتكييفها للاستخدام المحلي، بما فيها نماذج الذكاء الاصطناعي التوليدي.
- توجيه علماء البيانات والمهندسين في ممارسات هندسة التعلم الآلي.

### المهارات

| المهارة | المصدر | المستوى المتوقع | معنى هذا المستوى |
| --- | --- | --- | --- |
| [Applied maths, statistics and scientific practices](../../المهارات/#applied-maths-statistics-and-scientific-practices) | UK GDaD PCF | تمكّن | You can:<br>• apply designated quantitative techniques such as time series analysis, optimisation and simulation to create and embed appropriate models for analysis and prediction<br>• provide guidance on matching data sources with relevant applied mathematics and statistical techniques to meet analysis goals<br>• apply appropriate statistical techniques to available data to discover new relations and offer insight into research problems, helping to improve organisational processes and support decision making<br>• access and use the statistical tools available within the organisation |
| [Communicating between the technical and non-technical](../../المهارات/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | تمكّن | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Data ethics and privacy](../../المهارات/#data-ethics-and-privacy) | UK GDaD PCF | تمكّن | You can:<br>• work with stakeholders to identify and address ethical and privacy concerns<br>• demonstrate and communicate how data ethical issues fit into the wider organisational context<br>• research developments in data ethics and privacy to improve compliance and processes<br>• assess and constructively challenge proposed data ethics policies |
| [Data science innovation](../../المهارات/#data-science-innovation) | UK GDaD PCF | تمكّن | You can:<br>• demonstrate practical knowledge of data science tools and techniques<br>• develop data science solutions that maximise insight<br>• identify opportunities for how data science can improve data practices |
| [Programming and build (software engineering)](../../المهارات/#programming-and-build-software-engineering) | UK GDaD PCF | تمكّن | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems integration](../../المهارات/#systems-integration) | UK GDaD PCF | تمكّن | You can:<br>• define the integration build<br>• co-ordinate build activities across systems<br>• understand how to undertake and support integration testing activities |
| [فهم خدمات الصحة والرعاية](../../المهارات/#فهم-خدمات-الصحة-والرعاية) | هذا المرجع | ممارسة | يمكنك:<br>• شرح مسارات العمل السريرية ومسارات الرعاية التي يدعمها عملك<br>• استخدام المصطلحات الصحية الشائعة استخدامًا صحيحًا مع الزملاء السريريين وزملاء الرعاية<br>• إدراك متى قد يؤثر تغيير ما في رعاية المرضى والتنبيه إليه |
| [إدارة المخاطر السريرية](../../المهارات/#إدارة-المخاطر-السريرية) | هذا المرجع | ممارسة | يمكنك:<br>• المشاركة في ورش تحديد المخاطر والإسهام في سجل المخاطر<br>• اتباع عملية إدارة المخاطر السريرية في عملك<br>• تقديم أدلة لملف السلامة السريرية، مثل نتائج الاختبارات |
| [حوكمة المعلومات وحماية البيانات](../../المهارات/#حوكمة-المعلومات-وحماية-البيانات) | هذا المرجع | ممارسة | يمكنك:<br>• تطبيق مبادئ حماية البيانات في عملك<br>• الإسهام في تقييمات أثر حماية البيانات<br>• التعامل مع طلبات المعلومات والسجلات بشكل صحيح |
| [التشغيل البيني للبيانات الصحية](../../المهارات/#التشغيل-البيني-للبيانات-الصحية) | هذا المرجع | ممارسة | يمكنك:<br>• قراءة موارد FHIR وملفاتها التعريفية وواجهاتها البرمجية واستخدامها<br>• بناء عمليات تكامل بسيطة أو اختبارها بتوجيه<br>• التحقق من الرسائل مقابل مواصفة |
| [تنظيم البرمجيات بوصفها أجهزة طبية](../../المهارات/#تنظيم-البرمجيات-بوصفها-أجهزة-طبية) | هذا المرجع | ممارسة | يمكنك:<br>• اتباع عملية لدورة حياة البرمجيات تستوفي معايير الأجهزة الطبية<br>• إعداد السجلات التي تتطلبها تلك العملية |
| [الذكاء الاصطناعي الآمن والعادل في الرعاية الصحية](../../المهارات/#الذكاء-الاصطناعي-الآمن-والعادل-في-الرعاية-الصحية) | هذا المرجع | تمكّن | يمكنك:<br>• التخطيط للتحقق من صحة النموذج وتقييم تحيزه ومراقبته أثناء التشغيل مع الزملاء السريريين<br>• تقرير متى يحتاج النموذج إلى إعادة تدريب أو تقييد أو سحب<br>• تقديم المشورة للفرق بشأن متى قد يخضع النموذج للتنظيم بوصفه جهازًا طبيًا والأدلة التي يحتاجها |

### المؤهلات والخبرة المعتادة

- خبرة واسعة في بناء أنظمة التعلم الآلي وتشغيلها في بيئة الإنتاج، بمستوى يعادل درجة الماجستير.

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
| 3 | مهارات التحليل والتقدير | 5 | 60 |
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
| | **المجموع** | | **495** (الفئة 7: 466–539) |

## الفئة 8b: مهندس تعلم آلي قائد

**مستوى UK GDaD PCF: Lead machine learning engineer**

> A lead machine learning engineer leads the technical development and deployment of machine learning models.
> 
> At this role level, you will:
> - lead the most complex technical work needed to develop models for use in products and services
> - co-ordinate moving a model from the research and development stage to production
> - define ways of working across the machine learning life cycle
> - identify training needs for machine learning engineers and related roles
> - help your team work with other teams and disciplines
> - assure the effectiveness of machine learning models in use across the organisation
> - define and communicate software standards and guidelines related to ethics, risk and security

### المسؤوليات

- قيادة أكثر الأعمال تعقيدًا لنقل النماذج من البحث إلى الاستخدام الفعلي الآمن على مستوى المؤسسة.
- تحديد دورة حياة التعلم الآلي، بما في ذلك الضوابط اللازمة للنماذج الخاضعة للتنظيم والحرجة للسلامة.
- وضع معايير اختبار النماذج ومراقبتها وأمنها وأخلاقياتها، وضمان النماذج أثناء الاستخدام الفعلي.
- العمل مع مسؤولي السلامة السريرية وأخصائيي حوكمة المعلومات والشؤون التنظيمية للاتفاق على كيفية تقييم النماذج واعتمادها.
- تحديد احتياجات التدريب وتطوير مهندسي التعلم الآلي والأدوار ذات الصلة.

### المهارات

| المهارة | المصدر | المستوى المتوقع | معنى هذا المستوى |
| --- | --- | --- | --- |
| [Applied maths, statistics and scientific practices](../../المهارات/#applied-maths-statistics-and-scientific-practices) | UK GDaD PCF | تمكّن | You can:<br>• apply designated quantitative techniques such as time series analysis, optimisation and simulation to create and embed appropriate models for analysis and prediction<br>• provide guidance on matching data sources with relevant applied mathematics and statistical techniques to meet analysis goals<br>• apply appropriate statistical techniques to available data to discover new relations and offer insight into research problems, helping to improve organisational processes and support decision making<br>• access and use the statistical tools available within the organisation |
| [Communicating between the technical and non-technical](../../المهارات/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | خبرة | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Data ethics and privacy](../../المهارات/#data-ethics-and-privacy) | UK GDaD PCF | تمكّن | You can:<br>• work with stakeholders to identify and address ethical and privacy concerns<br>• demonstrate and communicate how data ethical issues fit into the wider organisational context<br>• research developments in data ethics and privacy to improve compliance and processes<br>• assess and constructively challenge proposed data ethics policies |
| [Data science innovation](../../المهارات/#data-science-innovation) | UK GDaD PCF | خبرة | You can:<br>• be a leader in the data science space<br>• demonstrate in-depth knowledge of data science tools and techniques, which you can use to solve problems creatively and to create opportunities for your team<br>• act as a coach, inspiring curiosity and creativity in others<br>• demonstrate in-depth knowledge of your chosen profession and keep up to date with changes in the industry<br>• challenge the status quo and always look for ways to improve data science |
| [Programming and build (software engineering)](../../المهارات/#programming-and-build-software-engineering) | UK GDaD PCF | خبرة | You can:<br>• advise on the right way to apply standards and methods to ensure compliance<br>• maintain technical responsibility for all the stages and iterations of a software development project<br>• provide technical advice to stakeholders and set the team-based standards for programming tools and techniques |
| [Systems integration](../../المهارات/#systems-integration) | UK GDaD PCF | خبرة | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [فهم خدمات الصحة والرعاية](../../المهارات/#فهم-خدمات-الصحة-والرعاية) | هذا المرجع | تمكّن | يمكنك:<br>• تحليل موقع خدمة ما ضمن مسارات الرعاية بين المؤسسات<br>• العمل مع الممارسين السريريين وموظفي الرعاية والمرضى لتشكيل الخدمات الرقمية<br>• شرح أثر القرارات الرقمية في الرعاية والسلامة وعبء العمل على الموظفين |
| [إدارة المخاطر السريرية](../../المهارات/#إدارة-المخاطر-السريرية) | هذا المرجع | تمكّن | يمكنك:<br>• قيادة تحديد المخاطر وتقييمها لمنتج أو تغيير<br>• كتابة سجلات المخاطر وتقارير ملفات السلامة السريرية وتحديثها<br>• الاتفاق مع فرق المنتجات على ضوابط المخاطر والتحقق من فعاليتها<br>• تقديم المشورة للفرق بشأن تطبيق معايير إدارة المخاطر السريرية |
| [حوكمة المعلومات وحماية البيانات](../../المهارات/#حوكمة-المعلومات-وحماية-البيانات) | هذا المرجع | تمكّن | يمكنك:<br>• قيادة تقييمات أثر حماية البيانات واتفاقيات تبادل المعلومات<br>• تقديم المشورة للفرق بشأن الأساس القانوني والموافقة والسرية ومدد الاحتفاظ<br>• التحقيق في الحوادث والتوصية بالتحسينات |
| [التشغيل البيني للبيانات الصحية](../../المهارات/#التشغيل-البيني-للبيانات-الصحية) | هذا المرجع | تمكّن | يمكنك:<br>• تصميم عمليات تكامل وبناؤها باستخدام FHIR وHL7 الإصدار 2 وأنماط المراسلة<br>• كتابة موارد FHIR وتعريف ملفاتها وأدلة تطبيقها<br>• حل مشكلات الربط وجودة البيانات المعقدة بين الأنظمة |
| [تنظيم البرمجيات بوصفها أجهزة طبية](../../المهارات/#تنظيم-البرمجيات-بوصفها-أجهزة-طبية) | هذا المرجع | تمكّن | يمكنك:<br>• تقييم ما إذا كان منتج ما جهازًا طبيًا، وفئته المرجّحة<br>• التخطيط للعمل التنظيمي لمنتج ما مع زملاء الجودة والزملاء السريريين |
| [الذكاء الاصطناعي الآمن والعادل في الرعاية الصحية](../../المهارات/#الذكاء-الاصطناعي-الآمن-والعادل-في-الرعاية-الصحية) | هذا المرجع | خبرة | يمكنك:<br>• وضع معايير المؤسسة لضمان الذكاء الاصطناعي في الرعاية ومراقبته<br>• قيادة ضمان النماذج عالية المخاطر قبل نشرها وبعده<br>• تمثيل المؤسسة لدى الجهات التنظيمية والشركاء في شأن الذكاء الاصطناعي الآمن والعادل |
| [إدارة الأفراد](../../المهارات/#إدارة-الأفراد) | هذا المرجع | ممارسة | يمكنك:<br>• الإشراف على العمل اليومي وتقديم الملاحظات<br>• المشاركة في التوظيف والتعريف بالعمل<br>• إجراء محادثات فردية منتظمة |

### المؤهلات والخبرة المعتادة

- خبرة واسعة في قيادة هندسة التعلم الآلي للخدمات المعقدة أو الخاضعة للتنظيم.

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
| 8 | المسؤولية عن الموارد المالية والمادية | 2 | 12 |
| 9 | المسؤولية عن الأفراد | 3 | 21 |
| 10 | المسؤولية عن موارد المعلومات | 5 | 34 |
| 11 | المسؤولية عن البحث والتطوير | 2 | 12 |
| 12 | حرية التصرف | 5 | 45 |
| 13 | الجهد البدني | 1 | 3 |
| 14 | الجهد الذهني | 4 | 18 |
| 15 | الجهد العاطفي | 1 | 5 |
| 16 | ظروف العمل | 2 | 7 |
| | **المجموع** | | **595** (الفئة 8b: 585–629) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
