# 数据工程师

> 这是一份面向通用数字医疗卫生机构的示例性参考档案。它不是任何雇主的正式职位说明，其中的岗位评估分数也不是正式评估。

> 本文由人工智能助手从英文翻译而来，尚未经过母语人士审校。引自英国政府数字与数据专业能力框架（UK GDaD PCF）和 ESCO 的内容保留英文原文。

**职族:** [数据](../../#数据)  
**职级:** 6, 7, 8a, 8b  
**UK GDaD PCF 角色:** [Data engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/data-engineer/)  
**ESCO 职业:** [data engineer](http://data.europa.eu/esco/occupation/2079755f-d809-49e6-8037-4de6180e54c0) (ISCO-08 2511)

## 概述

数据工程师构建并运行将医疗卫生和照护数据从临床和运营系统传输到可安全分析和使用之处的流水线和平台。他们设计数据流，集成使用不同标准的数据源，并确保数据准确、及时、安全，且只对应当看到它的人可用。

## 在数字医疗卫生机构中

- 源系统包括电子病历、实验室、影像和药房系统，这些系统使用 HL7 第 2 版、HL7 FHIR、SNOMED CT 和 ICD 等标准。
- 流水线经常传输可识别的患者数据，因此工程师从一开始就内置假名化、访问控制和审计。
- 一些数据源支持直接照护，例如警报或患者名单，因此流水线失败或延迟可能影响患者，需要进行临床安全评估。
- 数据经常需要跨照护场所关联，这依赖于可靠的患者匹配和一致的标识符。

## UK GDaD PCF 角色描述（英文原文）

> A data engineer develops and constructs data products and services, and integrates them into systems and business processes.

## 角色级别

| 职级 | 名称 | UK GDaD PCF 级别 | 英国公务员职等 | 岗位评估分数 |
| --- | --- | --- | --- | --- |
| 6 | [数据工程师](#职级-6-数据工程师) | Data engineer | HEO/SEO | 421 |
| 7 | [高级数据工程师](#职级-7-高级数据工程师) | Senior data engineer | SEO/G7 | 477 |
| 8a | [首席数据工程师](#职级-8a-首席数据工程师) | Lead data engineer | G7 | 551 |
| 8b | [数据工程主管](#职级-8b-数据工程主管) | Head of data engineering | G7/G6 | 589 |

## 职级 6: 数据工程师

**UK GDaD PCF 级别: Data engineer**

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

### 职责

- 按照商定的设计，构建和维护从临床和运营系统到数据平台的数据流水线。
- 将源数据（包括编码的临床数据）映射到目标模型，并记录映射关系。
- 在流水线中内置假名化、校验和数据质量检查。
- 监控流水线并修复故障，优先处理支持直接照护的数据源。
- 实施符合信息治理规则的访问控制和审计日志。

### 技能

| 技能 | 来源 | 期望等级 | 该等级的含义 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../skills/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 了解 | You can:<br>• explain why it's important to communicate technical concepts in non-technical language<br>• explain the types of communication that can be used with internal and external stakeholders, and their impact |
| [Data analysis and synthesis](../../skills/#data-analysis-and-synthesis) | UK GDaD PCF | 胜任 | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data compliance and security](../../skills/#data-compliance-and-security) | UK GDaD PCF | 胜任 | You can:<br>• use official data classification when authoring documents<br>• apply internal procedures, policies and technologies to ensure secure data handling<br>• identify and address ethical considerations when working with data<br>• address data compliance issues using internal processes |
| [Data development process](../../skills/#data-development-process) | UK GDaD PCF | 胜任 | You can:<br>• implement simple data solutions such as data pipelines, following established approaches and standards<br>• create repeatable, reliable and reusable data solutions |
| [Data innovation](../../skills/#data-innovation) | UK GDaD PCF | 了解 | You can:<br>• develop a basic understanding of an unfamiliar or emerging technology, or a familiar technology in a new data context, with guidance<br>• share what you learn with colleagues, including how it could help deliver more value from data |
| [Data integration design](../../skills/#data-integration-design) | UK GDaD PCF | 胜任 | You can:<br>• design simple data exchange or integration solutions using established patterns or modelling techniques<br>• include security features in your data integration designs |
| [Data modelling](../../skills/#data-modelling) | UK GDaD PCF | 胜任 | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Metadata management](../../skills/#metadata-management) | UK GDaD PCF | 胜任 | You can:<br>• use metadata repositories to complete complex tasks such as data and systems integration impact analysis<br>• maintain a metadata repository to ensure information remains accurate and up to date |
| [Problem management](../../skills/#problem-management) | UK GDaD PCF | 了解 | You can:<br>• investigate problems in systems, processes and services, with an understanding of the level of a problem, for example, strategic, tactical or operational<br>• contribute to the implementation of remedies and preventative measures |
| [Programming and build (data and analytics engineering)](../../skills/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | 胜任 | You can:<br>• design, code, test and deploy programs or scripts following standards and good practice<br>• write readable, maintainable code<br>• use automation to improve the software development life cycle<br>• consider and adopt appropriate security measures in your solutions |
| [了解医疗卫生和照护服务](../../skills/#了解医疗卫生和照护服务) | 本参考资料 | 胜任 | 您可以：<br>• 解释您的工作所支持的临床和照护工作流程<br>• 与临床和照护同事正确使用常见的医疗卫生术语<br>• 识别某项变更何时可能影响患者照护并提出来 |
| [信息治理与数据保护](../../skills/#信息治理与数据保护) | 本参考资料 | 胜任 | 您可以：<br>• 在工作中应用数据保护原则<br>• 为数据保护影响评估作出贡献<br>• 正确处理信息请求和记录 |
| [健康数据互操作性](../../skills/#健康数据互操作性) | 本参考资料 | 胜任 | 您可以：<br>• 阅读和使用 FHIR 资源、规范和 API<br>• 在指导下构建或测试简单的集成<br>• 依据规范检查消息 |
| [临床术语与分类](../../skills/#临床术语与分类) | 本参考资料 | 了解 | 您可以：<br>• 解释临床术语与分类之间的区别<br>• 识别 SNOMED CT 和 ICD 等常见术语 |
| [假名化与披露控制](../../skills/#假名化与披露控制) | 本参考资料 | 胜任 | 您可以：<br>• 使用假名化数据，并在发布输出前进行披露检查<br>• 识别关联数据或详细数据何时可能识别出某位患者 |
| [临床风险管理](../../skills/#临床风险管理) | 本参考资料 | 了解 | 您可以：<br>• 解释医疗信息系统可能如何伤害患者，例如通过错误、缺失或延迟的信息<br>• 通过正确途径报告可能的临床安全问题 |

### 典型资质与经验

- 计算机或相关学科的学位，或同等经验。
- 具有构建数据流水线的经验。

### 职级概要

- **知识:** 通过进一步培训或经验积累，具备覆盖一系列流程的专门知识。
- **自主性:** 独立工作；为本领域解读政策；在复杂问题上寻求建议。
- **范围:** 一个产品、服务或工作流。
- **领导力:** 可能领导一个小团队或指导同事。
- **问责:** 自己工作流的成果以及所提供建议的质量。

### 岗位评估（示例）

| # | 因素 | 等级 | 分数 |
| --- | --- | --- | --- |
| 1 | 沟通与人际关系技能 | 4 | 32 |
| 2 | 知识、培训和经验 | 6 | 156 |
| 3 | 分析与判断技能 | 4 | 42 |
| 4 | 规划与组织技能 | 3 | 27 |
| 5 | 身体技能 | 3 | 27 |
| 6 | 对患者和服务对象照护的责任 | 1 | 4 |
| 7 | 政策与服务发展的责任 | 2 | 12 |
| 8 | 对财务和实物资源的责任 | 1 | 5 |
| 9 | 对人员的责任 | 1 | 5 |
| 10 | 对信息资源的责任 | 5 | 34 |
| 11 | 对研究与开发的责任 | 2 | 12 |
| 12 | 行动自由度 | 4 | 32 |
| 13 | 体力消耗 | 1 | 3 |
| 14 | 脑力消耗 | 4 | 18 |
| 15 | 情绪消耗 | 1 | 5 |
| 16 | 工作条件 | 2 | 7 |
| | **总计** | | **421** (职级 6: 396–465) |

## 职级 7: 高级数据工程师

**UK GDaD PCF 级别: Senior data engineer**

> A senior data engineer designs and leads the implementation of data flows to connect operational systems, data for analytics and business intelligence (BI) systems.
> 
> At this role level, you will:
> - recognise opportunities to reuse existing data flows
> - lead the build of data streaming systems
> - optimise the code to ensure processes perform optimally
> - lead work on database management

### 职责

- 设计汇集来自众多医疗卫生和照护系统数据的数据流和流式服务。
- 设计患者匹配和关联流程，并衡量其效果。
- 领导数据库和平台性能工作，使数据在服务需要时可用。
- 与相关专家一起评估数据流的临床安全和信息治理风险。
- 审查其他工程师的工作并对其进行辅导。

### 技能

| 技能 | 来源 | 期望等级 | 该等级的含义 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../skills/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 胜任 | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Data analysis and synthesis](../../skills/#data-analysis-and-synthesis) | UK GDaD PCF | 胜任 | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data compliance and security](../../skills/#data-compliance-and-security) | UK GDaD PCF | 熟练 | You can:<br>• consistently apply data ethics, legislation, internal procedures, policies and technologies to ensure secure data handling<br>• help ensure your team remain compliant by identifying and addressing current and potential data compliance and ethical issues<br>• guide and support others in addressing data compliance issues |
| [Data development process](../../skills/#data-development-process) | UK GDaD PCF | 熟练 | You can:<br>• lead the implementation of complex or large-scale data solutions<br>• apply appropriate technology and techniques to ensure data solutions are secure and scalable<br>• identify and implement continuous improvement to the operation and performance of data solutions |
| [Data innovation](../../skills/#data-innovation) | UK GDaD PCF | 胜任 | You can:<br>• experiment with unfamiliar and emerging technologies, or familiar technologies in new data contexts, with guidance<br>• share what you learn with the team, explaining potential benefits, risks, and practical considerations<br>• identify opportunities to apply technology to improve data processes or outcomes in an operational setting or the wider organisation |
| [Data integration design](../../skills/#data-integration-design) | UK GDaD PCF | 熟练 | You can:<br>• select the most appropriate techniques for different integration scenarios<br>• evaluate and lead the implementation of integration using varied approaches that ensure security, efficiency and compliance |
| [Data modelling](../../skills/#data-modelling) | UK GDaD PCF | 熟练 | You can:<br>• produce relevant data models across multiple subject areas<br>• explain which models to use for which purpose<br>• understand industry-recognised data modelling patterns and standards, and when to apply them<br>• compare and align different data models |
| [Metadata management](../../skills/#metadata-management) | UK GDaD PCF | 熟练 | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../skills/#problem-management) | UK GDaD PCF | 胜任 | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Programming and build (data and analytics engineering)](../../skills/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | 熟练 | You can:<br>• lead the design, code, testing and deployment of secure, resilient and maintainable solutions<br>• continuously improve the codebase and reliability of solutions<br>• create automation to improve the software development life cycle<br>• work with others to implement standards and good practice to ensure security, testability and maintainability of solutions |
| [了解医疗卫生和照护服务](../../skills/#了解医疗卫生和照护服务) | 本参考资料 | 胜任 | 您可以：<br>• 解释您的工作所支持的临床和照护工作流程<br>• 与临床和照护同事正确使用常见的医疗卫生术语<br>• 识别某项变更何时可能影响患者照护并提出来 |
| [信息治理与数据保护](../../skills/#信息治理与数据保护) | 本参考资料 | 熟练 | 您可以：<br>• 领导数据保护影响评估和信息共享协议<br>• 就合法依据、同意、保密和保存向团队提供建议<br>• 调查事件并提出改进建议 |
| [健康数据互操作性](../../skills/#健康数据互操作性) | 本参考资料 | 熟练 | 您可以：<br>• 使用 FHIR、HL7 第 2 版和消息模式设计和构建集成<br>• 编写 FHIR 资源和实施指南并为其制定规范<br>• 解决系统之间复杂的映射和数据质量问题 |
| [临床术语与分类](../../skills/#临床术语与分类) | 本参考资料 | 胜任 | 您可以：<br>• 为数据项或表单查找并使用正确的代码<br>• 使用术语浏览器和参考集 |
| [假名化与披露控制](../../skills/#假名化与披露控制) | 本参考资料 | 熟练 | 您可以：<br>• 设计将标识符与分析数据分开保存的假名化和关联方法<br>• 评估数据集或出版物的再识别风险，并选择合适的控制措施<br>• 就可信研究环境等安全环境向团队提供建议 |
| [临床风险管理](../../skills/#临床风险管理) | 本参考资料 | 胜任 | 您可以：<br>• 参加危害研讨会并为危害日志作出贡献<br>• 在您的工作中遵循临床风险管理流程<br>• 为临床安全案例提供证据，例如测试结果 |

### 典型资质与经验

- 在设计和构建数据系统方面拥有丰富经验，相当于硕士学位水平。

### 职级概要

- **知识:** 高度发达的专门知识，通常达到硕士水平或同等经验。
- **自主性:** 按组织政策工作；决定如何取得成果；是他人咨询的专家。
- **范围:** 多个产品或服务，或一项专门职能。
- **领导力:** 领导一个团队或一个专业实践领域。
- **问责:** 交付一项服务或专门职能，以及其预算（如有）。

### 岗位评估（示例）

| # | 因素 | 等级 | 分数 |
| --- | --- | --- | --- |
| 1 | 沟通与人际关系技能 | 4 | 32 |
| 2 | 知识、培训和经验 | 7 | 196 |
| 3 | 分析与判断技能 | 4 | 42 |
| 4 | 规划与组织技能 | 3 | 27 |
| 5 | 身体技能 | 3 | 27 |
| 6 | 对患者和服务对象照护的责任 | 1 | 4 |
| 7 | 政策与服务发展的责任 | 3 | 21 |
| 8 | 对财务和实物资源的责任 | 1 | 5 |
| 9 | 对人员的责任 | 2 | 12 |
| 10 | 对信息资源的责任 | 5 | 34 |
| 11 | 对研究与开发的责任 | 2 | 12 |
| 12 | 行动自由度 | 4 | 32 |
| 13 | 体力消耗 | 1 | 3 |
| 14 | 脑力消耗 | 4 | 18 |
| 15 | 情绪消耗 | 1 | 5 |
| 16 | 工作条件 | 2 | 7 |
| | **总计** | | **477** (职级 7: 466–539) |

## 职级 8a: 首席数据工程师

**UK GDaD PCF 级别: Lead data engineer**

> A lead data engineer is responsible for the design and implementation of numerous complex data flows to connect operational systems, data for analytics and business intelligence (BI) systems.
> 
> At this role level, you will:
> - recognise and share opportunities to reuse existing data flows between teams
> - be responsible for the build of data-streaming systems
> - co-ordinate teams and set best practice and standards
> - apply knowledge of systems integration to your work
> - champion data engineering across government

### 职责

- 领导组织数据平台及其众多数据流的设计和运行。
- 为流水线、测试、安全和文档制定工程标准。
- 规划与医疗卫生和照护合作伙伴的数据集成，包括共享照护记录和区域数据服务。
- 确保支持直接照护的数据流具有韧性并有临床安全案例。
- 协调数据工程团队，直线管理工程师。

### 技能

| 技能 | 来源 | 期望等级 | 该等级的含义 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../skills/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 熟练 | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Data analysis and synthesis](../../skills/#data-analysis-and-synthesis) | UK GDaD PCF | 熟练 | You can:<br>• understand and help teams to apply a range of techniques for data profiling<br>• source system analysis from a complex single source<br>• bring multiple data sources together in a conformed model for analysis |
| [Data compliance and security](../../skills/#data-compliance-and-security) | UK GDaD PCF | 专家 | You can:<br>• advise senior stakeholders on data security, ethical or procedural risks<br>• improve organisational awareness of data compliance and procedures<br>• lead, guide and mentor teams in implementing secure data practices and maintaining compliance |
| [Data development process](../../skills/#data-development-process) | UK GDaD PCF | 专家 | You can:<br>• establish cross-organisational data solutions that include all aspects of the data development life cycle<br>• define and promote good practices for creating repeatable, reliable and reusable data solutions |
| [Data innovation](../../skills/#data-innovation) | UK GDaD PCF | 熟练 | You can:<br>• test and evaluate the feasibility of unfamiliar and emerging technologies, or familiar technologies in new data contexts<br>• share what you learn with the organisation, explaining potential benefits, risks, and practical considerations<br>• recommend, design and implement innovative data solutions based on organisation objectives, user needs, and operational constraints |
| [Data integration design](../../skills/#data-integration-design) | UK GDaD PCF | 专家 | You can:<br>• establish cross-organisational data integration standards and design patterns<br>• guide teams in designing secure and interoperable systems and services |
| [Data modelling](../../skills/#data-modelling) | UK GDaD PCF | 专家 | You can:<br>• understand the concepts and principles of data modelling and can produce relevant data models<br>• work across government and industry, recognising opportunities for the reuse and alignment of data models in different organisations<br>• design the method to categorise data models within an organisation |
| [Metadata management](../../skills/#metadata-management) | UK GDaD PCF | 熟练 | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../skills/#problem-management) | UK GDaD PCF | 熟练 | You can:<br>• ensure that the right actions are taken to investigate, resolve and anticipate problems<br>• co-ordinate the team to investigate problems, implement solutions and take preventive measures |
| [Programming and build (data and analytics engineering)](../../skills/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | 熟练 | You can:<br>• lead the design, code, testing and deployment of secure, resilient and maintainable solutions<br>• continuously improve the codebase and reliability of solutions<br>• create automation to improve the software development life cycle<br>• work with others to implement standards and good practice to ensure security, testability and maintainability of solutions |
| [了解医疗卫生和照护服务](../../skills/#了解医疗卫生和照护服务) | 本参考资料 | 熟练 | 您可以：<br>• 分析一项服务如何融入跨组织的照护路径<br>• 与临床医生、照护人员和患者合作塑造数字服务<br>• 解释数字决策对照护、安全和员工工作量的影响 |
| [信息治理与数据保护](../../skills/#信息治理与数据保护) | 本参考资料 | 熟练 | 您可以：<br>• 领导数据保护影响评估和信息共享协议<br>• 就合法依据、同意、保密和保存向团队提供建议<br>• 调查事件并提出改进建议 |
| [健康数据互操作性](../../skills/#健康数据互操作性) | 本参考资料 | 熟练 | 您可以：<br>• 使用 FHIR、HL7 第 2 版和消息模式设计和构建集成<br>• 编写 FHIR 资源和实施指南并为其制定规范<br>• 解决系统之间复杂的映射和数据质量问题 |
| [临床术语与分类](../../skills/#临床术语与分类) | 本参考资料 | 胜任 | 您可以：<br>• 为数据项或表单查找并使用正确的代码<br>• 使用术语浏览器和参考集 |
| [假名化与披露控制](../../skills/#假名化与披露控制) | 本参考资料 | 熟练 | 您可以：<br>• 设计将标识符与分析数据分开保存的假名化和关联方法<br>• 评估数据集或出版物的再识别风险，并选择合适的控制措施<br>• 就可信研究环境等安全环境向团队提供建议 |
| [临床风险管理](../../skills/#临床风险管理) | 本参考资料 | 胜任 | 您可以：<br>• 参加危害研讨会并为危害日志作出贡献<br>• 在您的工作中遵循临床风险管理流程<br>• 为临床安全案例提供证据，例如测试结果 |
| [人员管理](../../skills/#人员管理) | 本参考资料 | 熟练 | 您可以：<br>• 直线管理一个团队，设定目标并开展考评<br>• 关注身心健康，管理出勤、绩效和行为<br>• 规划团队的发展和继任 |

### 典型资质与经验

- 在领导复杂系统的数据工程方面拥有广泛经验。

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
| 11 | 对研究与开发的责任 | 2 | 12 |
| 12 | 行动自由度 | 5 | 45 |
| 13 | 体力消耗 | 1 | 3 |
| 14 | 脑力消耗 | 4 | 18 |
| 15 | 情绪消耗 | 1 | 5 |
| 16 | 工作条件 | 2 | 7 |
| | **总计** | | **551** (职级 8a: 540–584) |

## 职级 8b: 数据工程主管

**UK GDaD PCF 级别: Head of data engineering**

> A head of data engineering leads multi-functional delivery teams to deliver robust data services for their department, other government departments and private sector partners.
> 
> At this role level, you will:
> - inspire best practice for data products and services within your teams
> - build data engineering capability by providing technical leadership and career development for the community
> - work with other senior team members to identify, plan, develop and deliver data services

### 职责

- 为组织的数据平台和数据工程服务制定战略。
- 领导为内部团队以及医疗卫生和照护合作伙伴提供数据服务的多学科团队。
- 就数据平台的风险、成本和投资向高级负责人提供建议。
- 确保数据服务符合信息治理、安全和临床安全要求。
- 通过招聘、培养和职业路径建设数据工程能力。

### 技能

| 技能 | 来源 | 期望等级 | 该等级的含义 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../skills/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 专家 | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Data analysis and synthesis](../../skills/#data-analysis-and-synthesis) | UK GDaD PCF | 熟练 | You can:<br>• understand and help teams to apply a range of techniques for data profiling<br>• source system analysis from a complex single source<br>• bring multiple data sources together in a conformed model for analysis |
| [Data compliance and security](../../skills/#data-compliance-and-security) | UK GDaD PCF | 专家 | You can:<br>• advise senior stakeholders on data security, ethical or procedural risks<br>• improve organisational awareness of data compliance and procedures<br>• lead, guide and mentor teams in implementing secure data practices and maintaining compliance |
| [Data development process](../../skills/#data-development-process) | UK GDaD PCF | 专家 | You can:<br>• establish cross-organisational data solutions that include all aspects of the data development life cycle<br>• define and promote good practices for creating repeatable, reliable and reusable data solutions |
| [Data innovation](../../skills/#data-innovation) | UK GDaD PCF | 专家 | You can:<br>• advocate for adoption of unfamiliar and emerging technologies, or familiar technologies in new data contexts, ensuring organisation objectives, user needs, and operational constraints inform decisions<br>• develop organisational capability in data innovation through leadership<br>• anticipate future technology changes and advise how to take advantage of them to realise value from data |
| [Data integration design](../../skills/#data-integration-design) | UK GDaD PCF | 专家 | You can:<br>• establish cross-organisational data integration standards and design patterns<br>• guide teams in designing secure and interoperable systems and services |
| [Data modelling](../../skills/#data-modelling) | UK GDaD PCF | 胜任 | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Metadata management](../../skills/#metadata-management) | UK GDaD PCF | 专家 | You can:<br>• identify how metadata repositories can support different areas of the organisation<br>• communicate the value of metadata repositories<br>• set up robust governance processes to keep repositories up to date |
| [Problem management](../../skills/#problem-management) | UK GDaD PCF | 专家 | You can:<br>• anticipate problems and defend against them at the right time<br>• understand how a problem fits into the larger picture<br>• identify and describe problems, and help others to describe them<br>• build problem-solving capabilities in others |
| [Programming and build (data and analytics engineering)](../../skills/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | 专家 | You can:<br>• set standards for programming tools and techniques<br>• select appropriate development methods for a problem<br>• advise on the application of standards and methods that ensure security, maintainability and compliance<br>• take technical responsibility for all stages of a software development project, providing technical advice and guidance to stakeholders |
| [了解医疗卫生和照护服务](../../skills/#了解医疗卫生和照护服务) | 本参考资料 | 熟练 | 您可以：<br>• 分析一项服务如何融入跨组织的照护路径<br>• 与临床医生、照护人员和患者合作塑造数字服务<br>• 解释数字决策对照护、安全和员工工作量的影响 |
| [信息治理与数据保护](../../skills/#信息治理与数据保护) | 本参考资料 | 熟练 | 您可以：<br>• 领导数据保护影响评估和信息共享协议<br>• 就合法依据、同意、保密和保存向团队提供建议<br>• 调查事件并提出改进建议 |
| [健康数据互操作性](../../skills/#健康数据互操作性) | 本参考资料 | 专家 | 您可以：<br>• 为组织制定互操作性标准和战略<br>• 领导国家级或跨组织的标准工作<br>• 为跨多个系统的关键集成设计提供保证 |
| [假名化与披露控制](../../skills/#假名化与披露控制) | 本参考资料 | 熟练 | 您可以：<br>• 设计将标识符与分析数据分开保存的假名化和关联方法<br>• 评估数据集或出版物的再识别风险，并选择合适的控制措施<br>• 就可信研究环境等安全环境向团队提供建议 |
| [临床风险管理](../../skills/#临床风险管理) | 本参考资料 | 胜任 | 您可以：<br>• 参加危害研讨会并为危害日志作出贡献<br>• 在您的工作中遵循临床风险管理流程<br>• 为临床安全案例提供证据，例如测试结果 |
| [人员管理](../../skills/#人员管理) | 本参考资料 | 熟练 | 您可以：<br>• 直线管理一个团队，设定目标并开展考评<br>• 关注身心健康，管理出勤、绩效和行为<br>• 规划团队的发展和继任 |
| [预算管理](../../skills/#预算管理) | 本参考资料 | 熟练 | 您可以：<br>• 持有并管理预算，进行预测并解释差异<br>• 编制包含成本和效益的商业论证 |

### 典型资质与经验

- 在领导多个团队的数据工程方面拥有广泛经验。

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
| 2 | 知识、培训和经验 | 7 | 196 |
| 3 | 分析与判断技能 | 5 | 60 |
| 4 | 规划与组织技能 | 5 | 60 |
| 5 | 身体技能 | 2 | 15 |
| 6 | 对患者和服务对象照护的责任 | 1 | 4 |
| 7 | 政策与服务发展的责任 | 4 | 32 |
| 8 | 对财务和实物资源的责任 | 3 | 21 |
| 9 | 对人员的责任 | 4 | 32 |
| 10 | 对信息资源的责任 | 5 | 34 |
| 11 | 对研究与开发的责任 | 2 | 12 |
| 12 | 行动自由度 | 5 | 45 |
| 13 | 体力消耗 | 1 | 3 |
| 14 | 脑力消耗 | 4 | 18 |
| 15 | 情绪消耗 | 1 | 5 |
| 16 | 工作条件 | 2 | 7 |
| | **总计** | | **589** (职级 8b: 585–629) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
