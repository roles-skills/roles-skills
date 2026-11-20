# 数据架构师

> 这是一份面向通用数字医疗卫生机构的示例性参考档案。它不是任何雇主的正式职位说明，其中的岗位评估分数也不是正式评估。

> 本文由人工智能助手从英文翻译而来，尚未经过母语人士审校。引自英国政府数字与数据专业能力框架（UK GDaD PCF）和 ESCO 的内容保留英文原文。

**职族:** [架构](../../#架构)  
**职级:** 8a, 8b, 8c  
**UK GDaD PCF 角色:** [Data architect](https://understand-digital-data-roles-skills.service.gov.uk/role/data-architect/)  
**ESCO 职业:** [database designer](http://data.europa.eu/esco/occupation/8d9ec84d-cf2d-4179-87bc-335cda54a427) (ISCO-08 2521); [data warehouse designer](http://data.europa.eu/esco/occupation/1562c7a3-c7d9-419d-b9b6-db26610bcf84) (ISCO-08 2521)

## 概述

数据架构师设计组织如何构建、存储、传输和治理其医疗卫生和照护数据，使其能够安全地用于直接照护、服务规划和研究。他们设计数据模型、数据平台和数据流，制定数据标准，并确保临床含义、质量和保密性在端到端过程中得到保持。

## 在数字医疗卫生机构中

- 健康数据必须保持其临床含义，因此数据模型使用 SNOMED CT 等临床术语和 ICD 等分类。
- 用于直接照护的数据与用于规划或研究的数据具有不同的合法依据，因此架构师在设计中考虑数据分离、去标识化和受控访问。
- 数据来自许多质量不一的临床和照护系统，因此架构师在设计中考虑数据质量检查、患者匹配和数据血缘。
- 共享照护记录和数据交换依赖于 HL7 FHIR 资源等通用模型以及商定的国家或国际数据集。
- 记录必须长期保存，因此设计必须为归档和访问历史数据做好规划。

## UK GDaD PCF 角色描述（英文原文）

> A data architect sets the vision for the organisation’s use of data, through data design, to ensure that data is managed properly and meets the organisation’s needs.

## 角色级别

| 职级 | 名称 | UK GDaD PCF 级别 | 英国公务员职等 | 岗位评估分数 |
| --- | --- | --- | --- | --- |
| 8a | [数据架构师](#职级-8a-数据架构师) | Data architect | SEO/G7 | 560 |
| 8b | [高级数据架构师](#职级-8b-高级数据架构师) | Senior data architect | G7/G6 | 613 |
| 8c | [总数据架构师](#职级-8c-总数据架构师) | Chief data architect | G6 | 662 |

## 职级 8a: 数据架构师

**UK GDaD PCF 级别: Data architect**

> A data architect designs and builds data models to fulfil the strategic data needs of the organisation, as defined by chief data architects.
> 
> At this role level, you will:
> - design, support and provide guidance for the upgrade, management, decommission and archive of data in compliance with data policy
> - provide input into data dictionaries
> - define and maintain the data technology architecture, including metadata, integration and business intelligence or data warehouse architecture

### 职责

- 为临床和运营数据设计逻辑和物理数据模型，必要时使用临床术语。
- 设计数据流和数据平台组件，例如数据仓库、湖仓和集成层。
- 为您负责领域的数据集定义元数据、数据字典条目和数据血缘。
- 设计去标识化和访问控制措施，使数据只用于其合法目的。
- 与数据质量和临床编码同事合作，解决数据质量不佳的结构性原因。
- 就数据模型和标准指导数据工程师和分析师。

### 技能

| 技能 | 来源 | 期望等级 | 该等级的含义 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../技能/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 胜任 | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Communicating data](../../技能/#communicating-data) | UK GDaD PCF | 了解 | You can:<br>• show an awareness that data needs to be aligned to the needs of the end user<br>• create basic visuals and presentations |
| [Data analysis and synthesis](../../技能/#data-analysis-and-synthesis) | UK GDaD PCF | 胜任 | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../技能/#data-governance-data-architect) | UK GDaD PCF | 胜任 | You can:<br>• understand what data governance is required<br>• take responsibility for the assurance of data solutions and make recommendations to ensure compliance |
| [Data innovation](../../技能/#data-innovation) | UK GDaD PCF | 了解 | You can:<br>• develop a basic understanding of an unfamiliar or emerging technology, or a familiar technology in a new data context, with guidance<br>• share what you learn with colleagues, including how it could help deliver more value from data |
| [Data modelling](../../技能/#data-modelling) | UK GDaD PCF | 胜任 | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Data standards](../../技能/#data-standards) | UK GDaD PCF | 胜任 | You can:<br>• use data policies, processes and standards effectively<br>• work with subject matter experts to develop standards, policies and guidance to protect data<br>• monitor compliance with policies and standards in a team and take action if needed<br>• analyse the impact if a standard is breached |
| [Metadata management](../../技能/#metadata-management) | UK GDaD PCF | 胜任 | You can:<br>• use metadata repositories to complete complex tasks such as data and systems integration impact analysis<br>• maintain a metadata repository to ensure information remains accurate and up to date |
| [Problem management](../../技能/#problem-management) | UK GDaD PCF | 胜任 | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Strategic thinking](../../技能/#strategic-thinking) | UK GDaD PCF | 了解 | You can:<br>• explain the strategic context of your work and why it is important<br>• support strategic planning in an administrative capacity |
| [Turning business problems into data design](../../技能/#turning-business-problems-into-data-design) | UK GDaD PCF | 胜任 | You can:<br>• design data architecture by dealing with specific business problems and aligning it to enterprise-wide standards and principles<br>• work within the context of well understood architecture, and identify appropriate patterns |
| [了解医疗卫生和照护服务](../../技能/#了解医疗卫生和照护服务) | 本参考资料 | 胜任 | 您可以：<br>• 解释您的工作所支持的临床和照护工作流程<br>• 与临床和照护同事正确使用常见的医疗卫生术语<br>• 识别某项变更何时可能影响患者照护并提出来 |
| [临床术语与分类](../../技能/#临床术语与分类) | 本参考资料 | 胜任 | 您可以：<br>• 为数据项或表单查找并使用正确的代码<br>• 使用术语浏览器和参考集 |
| [健康数据互操作性](../../技能/#健康数据互操作性) | 本参考资料 | 熟练 | 您可以：<br>• 使用 FHIR、HL7 第 2 版和消息模式设计和构建集成<br>• 编写 FHIR 资源和实施指南并为其制定规范<br>• 解决系统之间复杂的映射和数据质量问题 |
| [信息治理与数据保护](../../技能/#信息治理与数据保护) | 本参考资料 | 熟练 | 您可以：<br>• 领导数据保护影响评估和信息共享协议<br>• 就合法依据、同意、保密和保存向团队提供建议<br>• 调查事件并提出改进建议 |
| [数据质量管理](../../技能/#数据质量管理) | 本参考资料 | 胜任 | 您可以：<br>• 运行数据质量检查并纠正错误<br>• 向同事解释数据质量报告 |

### 典型资质与经验

- 在数据建模和数据平台设计方面拥有丰富经验，相当于硕士学位水平。

### 职级概要

- **知识:** 对一门学科及其管理有专家级知识。
- **自主性:** 为一项服务解读组织政策；确定团队方向。
- **范围:** 一个服务领域，或整个组织中的一门学科。
- **领导力:** 管理一个团队，或在没有直线管理职责的情况下领导一门学科。
- **问责:** 一个服务领域及其员工和预算。

### 岗位评估（示例）

| # | 因素 | 等级 | 分数 |
| --- | --- | --- | --- |
| 1 | 沟通与人际关系技能 | 5 | 45 |
| 2 | 知识、培训和经验 | 7 | 196 |
| 3 | 分析与判断技能 | 5 | 60 |
| 4 | 规划与组织技能 | 4 | 42 |
| 5 | 身体技能 | 2 | 15 |
| 6 | 对患者和服务对象照护的责任 | 1 | 4 |
| 7 | 政策与服务发展的责任 | 4 | 32 |
| 8 | 对财务和实物资源的责任 | 2 | 12 |
| 9 | 对人员的责任 | 3 | 21 |
| 10 | 对信息资源的责任 | 5 | 34 |
| 11 | 对研究与开发的责任 | 3 | 21 |
| 12 | 行动自由度 | 5 | 45 |
| 13 | 体力消耗 | 1 | 3 |
| 14 | 脑力消耗 | 4 | 18 |
| 15 | 情绪消耗 | 1 | 5 |
| 16 | 工作条件 | 2 | 7 |
| | **总计** | | **560** (职级 8a: 540–584) |

职级高于 UK GDaD PCF 职等建议（第 7 职级）：医疗卫生行业的招聘广告将此角色定为第 8a 职级。规划、政策和行动自由度的评分高于第 7 职级概况，因为该岗位设计供许多服务使用的数据平台和控制措施。

## 职级 8b: 高级数据架构师

**UK GDaD PCF 级别: Senior data architect**

> A senior data architect delivers the vision for the organisation as set by the chief data architect.
> 
> At this role level, you will:
> - design data models and metadata systems
> - help chief data architects to interpret an organisation’s needs
> - provide oversight and advice to other data architects who are designing and producing data artefacts
> - design and support the management of data dictionaries
> - make sure that your teams are working to the standards set for the organisation by the chief data architects
> - work with technical architects to make sure that an organisation’s systems are designed in accordance with the appropriate data architecture

### 职责

- 为共享照护记录或分析平台等重要领域设计数据架构。
- 确保各团队的数据设计遵循组织的数据标准和模型。
- 设计如何与合作组织共享数据，包括标准、控制措施和数据共享协议。
- 就新设计的数据风险向信息治理和临床安全同事提供建议。
- 审查并指导数据架构师的工作。

### 技能

| 技能 | 来源 | 期望等级 | 该等级的含义 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../技能/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 熟练 | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Communicating data](../../技能/#communicating-data) | UK GDaD PCF | 胜任 | You can:<br>• understand the appropriate media to communicate findings<br>• shape communications for the audience |
| [Data analysis and synthesis](../../技能/#data-analysis-and-synthesis) | UK GDaD PCF | 胜任 | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../技能/#data-governance-data-architect) | UK GDaD PCF | 熟练 | You can:<br>• evolve and define data governance<br>• take responsibility for supporting and collaborating around wider governance<br>• assure and integrate data services to meet the needs of multiple business services<br>• work proactively to ensure the organisation designs architecture that considers data |
| [Data innovation](../../技能/#data-innovation) | UK GDaD PCF | 胜任 | You can:<br>• experiment with unfamiliar and emerging technologies, or familiar technologies in new data contexts, with guidance<br>• share what you learn with the team, explaining potential benefits, risks, and practical considerations<br>• identify opportunities to apply technology to improve data processes or outcomes in an operational setting or the wider organisation |
| [Data modelling](../../技能/#data-modelling) | UK GDaD PCF | 熟练 | You can:<br>• produce relevant data models across multiple subject areas<br>• explain which models to use for which purpose<br>• understand industry-recognised data modelling patterns and standards, and when to apply them<br>• compare and align different data models |
| [Data standards](../../技能/#data-standards) | UK GDaD PCF | 熟练 | You can:<br>• create data standards for different subjects and ensure senior leaders understand them<br>• work with subject matter experts across the organisation to introduce data standards best practice<br>• monitor compliance with policies and standards in the organisation<br>• make recommendations about how the organisation should resolve breaches of standards |
| [Metadata management](../../技能/#metadata-management) | UK GDaD PCF | 熟练 | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../技能/#problem-management) | UK GDaD PCF | 熟练 | You can:<br>• ensure that the right actions are taken to investigate, resolve and anticipate problems<br>• co-ordinate the team to investigate problems, implement solutions and take preventive measures |
| [Strategic thinking](../../技能/#strategic-thinking) | UK GDaD PCF | 胜任 | You can:<br>• work within a strategic context and communicate how activities meet strategic goals<br>• contribute to the development of strategy and policies |
| [Turning business problems into data design](../../技能/#turning-business-problems-into-data-design) | UK GDaD PCF | 熟练 | You can:<br>• design data architecture that deals with problems spanning different business areas<br>• identify links between problems to devise common solutions<br>• work across multiple subject areas, or a single large or complicated subject area<br>• produce appropriate patterns |
| [了解医疗卫生和照护服务](../../技能/#了解医疗卫生和照护服务) | 本参考资料 | 熟练 | 您可以：<br>• 分析一项服务如何融入跨组织的照护路径<br>• 与临床医生、照护人员和患者合作塑造数字服务<br>• 解释数字决策对照护、安全和员工工作量的影响 |
| [临床术语与分类](../../技能/#临床术语与分类) | 本参考资料 | 熟练 | 您可以：<br>• 使用临床术语设计数据模型和参考集<br>• 在术语和分类之间进行映射，并解释映射的局限<br>• 就产品和分析中的术语使用向团队提供建议 |
| [健康数据互操作性](../../技能/#健康数据互操作性) | 本参考资料 | 熟练 | 您可以：<br>• 使用 FHIR、HL7 第 2 版和消息模式设计和构建集成<br>• 编写 FHIR 资源和实施指南并为其制定规范<br>• 解决系统之间复杂的映射和数据质量问题 |
| [信息治理与数据保护](../../技能/#信息治理与数据保护) | 本参考资料 | 熟练 | 您可以：<br>• 领导数据保护影响评估和信息共享协议<br>• 就合法依据、同意、保密和保存向团队提供建议<br>• 调查事件并提出改进建议 |
| [数据质量管理](../../技能/#数据质量管理) | 本参考资料 | 熟练 | 您可以：<br>• 定义数据质量规则和衡量指标<br>• 与数据提供方合作，从根本上解决质量问题 |
| [临床风险管理](../../技能/#临床风险管理) | 本参考资料 | 胜任 | 您可以：<br>• 参加危害研讨会并为危害日志作出贡献<br>• 在您的工作中遵循临床风险管理流程<br>• 为临床安全案例提供证据，例如测试结果 |
| [人员管理](../../技能/#人员管理) | 本参考资料 | 胜任 | 您可以：<br>• 督导日常工作并给予反馈<br>• 参与招聘和入职引导<br>• 定期进行一对一谈话 |

### 典型资质与经验

- 在复杂组织的数据架构方面拥有广泛经验。

### 职级概要

- **知识:** 跨多个学科或一项大型服务的专家级知识。
- **自主性:** 为一个大领域制定政策和战略。
- **范围:** 多项服务或多个团队，或首席级别的一门学科。
- **领导力:** 管理经理，或是一门学科的首席权威。
- **问责:** 多项服务及其员工和预算。

### 岗位评估（示例）

| # | 因素 | 等级 | 分数 |
| --- | --- | --- | --- |
| 1 | 沟通与人际关系技能 | 5 | 45 |
| 2 | 知识、培训和经验 | 8 | 240 |
| 3 | 分析与判断技能 | 5 | 60 |
| 4 | 规划与组织技能 | 4 | 42 |
| 5 | 身体技能 | 2 | 15 |
| 6 | 对患者和服务对象照护的责任 | 1 | 4 |
| 7 | 政策与服务发展的责任 | 4 | 32 |
| 8 | 对财务和实物资源的责任 | 3 | 21 |
| 9 | 对人员的责任 | 3 | 21 |
| 10 | 对信息资源的责任 | 5 | 34 |
| 11 | 对研究与开发的责任 | 3 | 21 |
| 12 | 行动自由度 | 5 | 45 |
| 13 | 体力消耗 | 1 | 3 |
| 14 | 脑力消耗 | 4 | 18 |
| 15 | 情绪消耗 | 1 | 5 |
| 16 | 工作条件 | 2 | 7 |
| | **总计** | | **613** (职级 8b: 585–629) |

## 职级 8c: 总数据架构师

**UK GDaD PCF 级别: Chief data architect**

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

### 职责

- 按照组织的数据战略制定数据架构愿景和路线图。
- 负责组织的企业数据模型、数据标准和数据字典。
- 就数据架构、风险和投资向执行团队和数据治理机构提供建议。
- 在跨组织的数据标准和互操作性工作中代表组织。
- 领导数据架构实践并培养其人员。

### 技能

| 技能 | 来源 | 期望等级 | 该等级的含义 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../技能/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 熟练 | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Communicating data](../../技能/#communicating-data) | UK GDaD PCF | 熟练 | You can:<br>• turn complex data into clear and well understood solutions, which can be acted upon<br>• share data communication skills with the team and organisation<br>• understand and communicate different options, taking into account risks and uncertainties |
| [Data analysis and synthesis](../../技能/#data-analysis-and-synthesis) | UK GDaD PCF | 胜任 | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../技能/#data-governance-data-architect) | UK GDaD PCF | 专家 | You can:<br>• ensure data governance supports changes to the organisational strategy<br>• align data governance with wider governance (for example, budget)<br>• assure corporate services by understanding important risks and providing mitigation through assurance mechanisms |
| [Data innovation](../../技能/#data-innovation) | UK GDaD PCF | 熟练 | You can:<br>• test and evaluate the feasibility of unfamiliar and emerging technologies, or familiar technologies in new data contexts<br>• share what you learn with the organisation, explaining potential benefits, risks, and practical considerations<br>• recommend, design and implement innovative data solutions based on organisation objectives, user needs, and operational constraints |
| [Data modelling](../../技能/#data-modelling) | UK GDaD PCF | 专家 | You can:<br>• understand the concepts and principles of data modelling and can produce relevant data models<br>• work across government and industry, recognising opportunities for the reuse and alignment of data models in different organisations<br>• design the method to categorise data models within an organisation |
| [Data standards](../../技能/#data-standards) | UK GDaD PCF | 专家 | You can:<br>• create data standards for the organisation<br>• advocate for, and oversee compliance with, data policies and standards<br>• decide where standards need to be set across the organisation, and how to set them in the wider context of government |
| [Metadata management](../../技能/#metadata-management) | UK GDaD PCF | 专家 | You can:<br>• identify how metadata repositories can support different areas of the organisation<br>• communicate the value of metadata repositories<br>• set up robust governance processes to keep repositories up to date |
| [Problem management](../../技能/#problem-management) | UK GDaD PCF | 专家 | You can:<br>• anticipate problems and defend against them at the right time<br>• understand how a problem fits into the larger picture<br>• identify and describe problems, and help others to describe them<br>• build problem-solving capabilities in others |
| [Strategic thinking](../../技能/#strategic-thinking) | UK GDaD PCF | 熟练 | You can:<br>• define strategies and policies, providing guidance to others on working in the strategic context<br>• evaluate current strategies to ensure business requirements are being met and exceeded where possible |
| [Turning business problems into data design](../../技能/#turning-business-problems-into-data-design) | UK GDaD PCF | 专家 | You can:<br>• design data architecture that deals with problems across the enterprise<br>• work across all organisational subject areas and internal and external programmes |
| [了解医疗卫生和照护服务](../../技能/#了解医疗卫生和照护服务) | 本参考资料 | 专家 | 您可以：<br>• 凭借对医疗卫生和照护体系的深刻理解塑造组织战略<br>• 代表组织与医疗卫生和照护领域的合作伙伴及负责人沟通<br>• 预判政策和服务变化将如何影响数字服务和照护 |
| [临床术语与分类](../../技能/#临床术语与分类) | 本参考资料 | 熟练 | 您可以：<br>• 使用临床术语设计数据模型和参考集<br>• 在术语和分类之间进行映射，并解释映射的局限<br>• 就产品和分析中的术语使用向团队提供建议 |
| [健康数据互操作性](../../技能/#健康数据互操作性) | 本参考资料 | 专家 | 您可以：<br>• 为组织制定互操作性标准和战略<br>• 领导国家级或跨组织的标准工作<br>• 为跨多个系统的关键集成设计提供保证 |
| [信息治理与数据保护](../../技能/#信息治理与数据保护) | 本参考资料 | 专家 | 您可以：<br>• 制定信息治理政策和战略<br>• 就信息风险和合规向董事会提供建议<br>• 代表组织与监管机构和合作伙伴沟通 |
| [数据质量管理](../../技能/#数据质量管理) | 本参考资料 | 熟练 | 您可以：<br>• 定义数据质量规则和衡量指标<br>• 与数据提供方合作，从根本上解决质量问题 |
| [临床风险管理](../../技能/#临床风险管理) | 本参考资料 | 熟练 | 您可以：<br>• 领导产品或变更的危害识别和风险评估<br>• 编写和维护危害日志及临床安全案例报告<br>• 与产品团队商定风险控制措施并检查其有效性<br>• 就如何应用临床风险管理标准向团队提供建议 |
| [人员管理](../../技能/#人员管理) | 本参考资料 | 熟练 | 您可以：<br>• 直线管理一个团队，设定目标并开展考评<br>• 关注身心健康，管理出勤、绩效和行为<br>• 规划团队的发展和继任 |

### 典型资质与经验

- 在跨组织领导数据架构方面拥有广泛经验。

### 职级概要

- **知识:** 专家级知识，以及对组织和行业的广泛理解。
- **自主性:** 为一项职能制定战略；向一名总监负责。
- **范围:** 一项职能或一个部门。
- **领导力:** 通过多个管理层级领导一项职能。
- **问责:** 一项职能的绩效、人员和预算。

### 岗位评估（示例）

| # | 因素 | 等级 | 分数 |
| --- | --- | --- | --- |
| 1 | 沟通与人际关系技能 | 6 | 60 |
| 2 | 知识、培训和经验 | 8 | 240 |
| 3 | 分析与判断技能 | 5 | 60 |
| 4 | 规划与组织技能 | 5 | 60 |
| 5 | 身体技能 | 2 | 15 |
| 6 | 对患者和服务对象照护的责任 | 1 | 4 |
| 7 | 政策与服务发展的责任 | 5 | 45 |
| 8 | 对财务和实物资源的责任 | 3 | 21 |
| 9 | 对人员的责任 | 3 | 21 |
| 10 | 对信息资源的责任 | 6 | 46 |
| 11 | 对研究与开发的责任 | 2 | 12 |
| 12 | 行动自由度 | 5 | 45 |
| 13 | 体力消耗 | 1 | 3 |
| 14 | 脑力消耗 | 4 | 18 |
| 15 | 情绪消耗 | 1 | 5 |
| 16 | 工作条件 | 2 | 7 |
| | **总计** | | **662** (职级 8c: 630–674) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
