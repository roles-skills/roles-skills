# 技术架构师

> 这是一份面向通用数字医疗卫生机构的示例性参考档案。它不是任何雇主的正式职位说明，其中的岗位评估分数也不是正式评估。

> 本文由人工智能助手从英文翻译而来，尚未经过母语人士审校。引自英国政府数字与数据专业能力框架（UK GDaD PCF）和 ESCO 的内容保留英文原文。

**职族:** [架构](../../#架构)  
**职级:** 6, 7, 8a, 8b, 8c  
**UK GDaD PCF 角色:** [Technical architect](https://understand-digital-data-roles-skills.service.gov.uk/role/technical-architect/)  
**ESCO 职业:** [software architect](http://data.europa.eu/esco/occupation/d0aa0792-4345-474b-9365-686cf4869d2e) (ISCO-08 2512); [cloud architect](http://data.europa.eu/esco/occupation/2fb96c6c-8d0b-4ef0-b1ee-3e493305e4eb) (ISCO-08 2512)

## 概述

技术架构师设计组织数字健康服务的技术结构：组件、平台、托管、集成模式，以及安全、性能和韧性等非功能特性。他们与开发人员和 DevOps 工程师密切合作，为交付团队提供技术领导，并确保服务经久耐用、运行安全。

## 在数字医疗卫生机构中

- 临床服务通常需要高可用性和快速恢复，因此技术设计必须为故障和降级运行做好规划。
- 设计必须默认通过加密、访问控制和审计来保护保密的健康信息。
- 服务通常通过 HL7 FHIR API 和消息与许多临床系统和共享平台相连，因此集成模式是设计的核心。
- 缓存、重试和时间处理等技术设计选择可能造成临床危害，因此架构师为安全案例作出贡献。
- 遗留临床系统和医疗器械可能限制技术、网络和托管方面的选择。

## UK GDaD PCF 角色描述（英文原文）

> A technical architect provides technical leadership and architectural design.

## 角色级别

| 职级 | 名称 | UK GDaD PCF 级别 | 英国公务员职等 | 岗位评估分数 |
| --- | --- | --- | --- | --- |
| 6 | [助理技术架构师](#职级-6-助理技术架构师) | Associate technical architect | EO/HEO | 412 |
| 7 | [技术架构师](#职级-7-技术架构师) | Technical architect | SEO/G7 | 496 |
| 8a | [高级技术架构师](#职级-8a-高级技术架构师) | Senior technical architect | SEO/G7 | 560 |
| 8b | [首席技术架构师](#职级-8b-首席技术架构师) | Lead technical architect | G7/G6 | 613 |
| 8c | [主任技术架构师](#职级-8c-主任技术架构师) | Principal technical architect | G6 | 662 |

## 职级 6: 助理技术架构师

**UK GDaD PCF 级别: Associate technical architect**

> An associate technical architect supports technical architects in putting forward designs as solutions to technology challenges, usually under supervision.
> 
> At this role level, you will:
> - work closely with developers when designing appropriate solutions
> - have an understanding of the overall strategy and how your work supports it

### 职责

- 绘制技术图表，记录现有服务的组件、托管和集成。
- 在指导下研究技术方案并总结其利弊。
- 与开发人员合作，检查构建是否遵循商定的设计和模式。
- 记录技术决策，保持设计文档为最新。

### 技能

| 技能 | 来源 | 期望等级 | 该等级的含义 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../skills/#architect-for-the-whole-context) | UK GDaD PCF | 了解 | You can:<br>• identify relevant information that can inform your architectural work, such as strategies, roadmaps, policies and technical trends<br>• understand how your work supports the team in enabling change​ |
| [Architecture communication](../../skills/#architecture-communication) | UK GDaD PCF | 了解 | You can:<br>• show an awareness of different ways of creating architecture representations for a limited audience, including technical and non-technical stakeholders<br>• gather and explain information to be used in architecture representations |
| [Community collaboration](../../skills/#community-collaboration) | UK GDaD PCF | 了解 | You can:<br>• understand the work of others and the importance of team dynamics, collaboration and feedback |
| [Making architectural decisions](../../skills/#making-architectural-decisions) | UK GDaD PCF | 了解 | You can:<br>• describe the reasoning behind architectural design decisions<br>• gather information to inform decisions<br>• understand architectural governance and assurance relevant to your work |
| [Strategy design](../../skills/#strategy-design) | UK GDaD PCF | 了解 | You can:<br>• explain how organisational objectives link to designing strategy<br>• describe the purpose and application of strategy, standards, patterns, policies, roadmaps, vision, and mission statements |
| [Technical design throughout the life cycle](../../skills/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | 胜任 | You can:<br>• create technical designs characterised by managed levels of risk, impact, and complexity<br>• provide guidance and support to teams using technical designs throughout the life cycle<br>• adapt a technical design if needed during delivery<br>• work with well-understood technology and identify appropriate patterns |
| [了解医疗卫生和照护服务](../../skills/#了解医疗卫生和照护服务) | 本参考资料 | 了解 | 您可以：<br>• 描述医疗卫生和照护体系的主要组成部分以及组织所支持的服务<br>• 解释为什么患者安全和保密在您的工作中很重要 |
| [健康数据互操作性](../../skills/#健康数据互操作性) | 本参考资料 | 胜任 | 您可以：<br>• 阅读和使用 FHIR 资源、规范和 API<br>• 在指导下构建或测试简单的集成<br>• 依据规范检查消息 |
| [信息治理与数据保护](../../skills/#信息治理与数据保护) | 本参考资料 | 了解 | 您可以：<br>• 遵循组织处理个人信息和健康信息的规则<br>• 识别并报告数据泄露或未遂事件 |
| [临床风险管理](../../skills/#临床风险管理) | 本参考资料 | 了解 | 您可以：<br>• 解释医疗信息系统可能如何伤害患者，例如通过错误、缺失或延迟的信息<br>• 通过正确途径报告可能的临床安全问题 |

### 典型资质与经验

- 计算机或相关学科的学位，或软件或基础设施工程方面的同等经验。
- 具备技术设计方面的专门知识，达到研究生文凭水平或同等经验。

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
| 5 | 身体技能 | 2 | 15 |
| 6 | 对患者和服务对象照护的责任 | 1 | 4 |
| 7 | 政策与服务发展的责任 | 3 | 21 |
| 8 | 对财务和实物资源的责任 | 1 | 5 |
| 9 | 对人员的责任 | 1 | 5 |
| 10 | 对信息资源的责任 | 5 | 34 |
| 11 | 对研究与开发的责任 | 2 | 12 |
| 12 | 行动自由度 | 4 | 32 |
| 13 | 体力消耗 | 1 | 3 |
| 14 | 脑力消耗 | 3 | 12 |
| 15 | 情绪消耗 | 1 | 5 |
| 16 | 工作条件 | 2 | 7 |
| | **总计** | | **412** (职级 6: 396–465) |

职级高于 UK GDaD PCF 职等建议（第 5 职级）：医疗卫生行业的招聘广告将此角色定为第 6 职级。知识按研究生文凭水平评分，信息资源为第 5 级，因为该岗位设计主要信息系统的部分内容。

## 职级 7: 技术架构师

**UK GDaD PCF 级别: Technical architect**

> A technical architect is responsible for the design and build of technical architecture.
> 
> At this role level, you will:
> - undertake structured analysis of technical issues, translating this analysis into technical designs that describe a solution
> - be consulted about design and provide design patterns
> - identify deeper issues that need fixing
> - look for opportunities to collaborate and reuse components, communicating with both technical and non-technical stakeholders

### 职责

- 为一项服务设计技术架构，包括组件、托管、集成和安全。
- 为交付团队提供设计模式，并审查其技术设计和代码结构。
- 与服务负责人一起定义可用性、性能和恢复目标等非功能需求。
- 识别技术债务和不受支持的技术，并规划如何解决。
- 为临床安全案例识别技术危害和控制措施。

### 技能

| 技能 | 来源 | 期望等级 | 该等级的含义 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../skills/#architect-for-the-whole-context) | UK GDaD PCF | 胜任 | You can:<br>• align your work with the work being done by other architects and technical professionals<br>• track emerging issues, strategies, roadmaps, patterns and technologies over time to assess opportunities and risks to your work<br>• identify how other teams contribute to delivering outcomes through change |
| [Architecture communication](../../skills/#architecture-communication) | UK GDaD PCF | 胜任 | You can:<br>• listen to the needs of technical and business stakeholders<br>• create and use different architecture representations to communicate effectively, achieving agreement with technical and non-technical stakeholders<br>• provide support in discussions about architectural topics within a multidisciplinary team |
| [Community collaboration](../../skills/#community-collaboration) | UK GDaD PCF | 胜任 | You can:<br>• contribute to the work of others<br>• motivate and empower teams<br>• create the right environment for teams to work in, and can identify the best team makeup depending on the situation<br>• recognise and deal with issues |
| [Making architectural decisions](../../skills/#making-architectural-decisions) | UK GDaD PCF | 胜任 | You can:<br>• work with others to make architectural design decisions characterised by managed levels of risk and complexity<br>• identify and address architectural risks relevant to your team or domain, for example, business, data, or security<br>• engage with architectural governance and assurance to effectively manage decisions and risks, with support |
| [Strategy design](../../skills/#strategy-design) | UK GDaD PCF | 胜任 | You can:<br>• support the development of a strategy or vision that aligns with organisational objectives<br>• challenge requirements and assumptions, and identify opportunities to develop strategy<br>• support the implementation of a strategy or vision, for example, by using a roadmap or plan<br>• use architectural principles, patterns, and constraints when appropriate |
| [Technical design throughout the life cycle](../../skills/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | 胜任 | You can:<br>• create technical designs characterised by managed levels of risk, impact, and complexity<br>• provide guidance and support to teams using technical designs throughout the life cycle<br>• adapt a technical design if needed during delivery<br>• work with well-understood technology and identify appropriate patterns |
| [了解医疗卫生和照护服务](../../skills/#了解医疗卫生和照护服务) | 本参考资料 | 胜任 | 您可以：<br>• 解释您的工作所支持的临床和照护工作流程<br>• 与临床和照护同事正确使用常见的医疗卫生术语<br>• 识别某项变更何时可能影响患者照护并提出来 |
| [健康数据互操作性](../../skills/#健康数据互操作性) | 本参考资料 | 熟练 | 您可以：<br>• 使用 FHIR、HL7 第 2 版和消息模式设计和构建集成<br>• 编写 FHIR 资源和实施指南并为其制定规范<br>• 解决系统之间复杂的映射和数据质量问题 |
| [信息治理与数据保护](../../skills/#信息治理与数据保护) | 本参考资料 | 胜任 | 您可以：<br>• 在工作中应用数据保护原则<br>• 为数据保护影响评估作出贡献<br>• 正确处理信息请求和记录 |
| [临床风险管理](../../skills/#临床风险管理) | 本参考资料 | 胜任 | 您可以：<br>• 参加危害研讨会并为危害日志作出贡献<br>• 在您的工作中遵循临床风险管理流程<br>• 为临床安全案例提供证据，例如测试结果 |
| [身份与访问管理](../../skills/#身份与访问管理) | 本参考资料 | 了解 | 您可以：<br>• 遵守访问规则并保护您的凭据 |

### 典型资质与经验

- 具备技术架构方面的专门知识，达到硕士水平或同等经验。
- 具有设计或构建生产环境软件或基础设施的经验。

### 职级概要

- **知识:** 高度发达的专门知识，通常达到硕士水平或同等经验。
- **自主性:** 按组织政策工作；决定如何取得成果；是他人咨询的专家。
- **范围:** 多个产品或服务，或一项专门职能。
- **领导力:** 领导一个团队或一个专业实践领域。
- **问责:** 交付一项服务或专门职能，以及其预算（如有）。

### 岗位评估（示例）

| # | 因素 | 等级 | 分数 |
| --- | --- | --- | --- |
| 1 | 沟通与人际关系技能 | 5 | 45 |
| 2 | 知识、培训和经验 | 7 | 196 |
| 3 | 分析与判断技能 | 5 | 60 |
| 4 | 规划与组织技能 | 3 | 27 |
| 5 | 身体技能 | 2 | 15 |
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
| | **总计** | | **496** (职级 7: 466–539) |

职级与 UK GDaD PCF 建议的第 7 职级一致，也与医疗卫生行业该角色的招聘广告一致。知识按硕士水平或同等评分，因为需要涵盖技术架构各方面的专门知识。

## 职级 8a: 高级技术架构师

**UK GDaD PCF 级别: Senior technical architect**

> A senior technical architect works on large or multiple pieces of work that are complex or risky.
> 
> At this role level, you will:
> - define strategy and be central to assuring services
> - regularly collaborate and find agreement with senior stakeholders, providing direction and challenge
> - be proactive in identifying problems and translating these into non-technical descriptions that can be widely understood
> - mentor and coach junior colleagues

### 职责

- 领导大型、复杂或高风险服务（例如临床系统和共享集成平台）的技术设计。
- 为一个或多个交付团队确定技术方向，并质疑增加风险的设计。
- 针对韧性、灾难恢复和安全运行进行设计，并检查团队是否对其进行测试。
- 用通俗易懂的语言向服务负责人、临床负责人和高级利益相关方解释技术风险和取舍。
- 指导和辅导技术架构师及高级开发人员。

### 技能

| 技能 | 来源 | 期望等级 | 该等级的含义 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../skills/#architect-for-the-whole-context) | UK GDaD PCF | 胜任 | You can:<br>• align your work with the work being done by other architects and technical professionals<br>• track emerging issues, strategies, roadmaps, patterns and technologies over time to assess opportunities and risks to your work<br>• identify how other teams contribute to delivering outcomes through change |
| [Architecture communication](../../skills/#architecture-communication) | UK GDaD PCF | 熟练 | You can:<br>• lead the communication of complicated, complex or risky architecture topics with technical and non-technical stakeholders<br>• communicate with senior stakeholders across your organisation<br>• adapt your message and communication techniques to your audience<br>• advocate on behalf of a team to other stakeholders<br>• manage stakeholder expectations effectively |
| [Community collaboration](../../skills/#community-collaboration) | UK GDaD PCF | 熟练 | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../skills/#making-architectural-decisions) | UK GDaD PCF | 胜任 | You can:<br>• work with others to make architectural design decisions characterised by managed levels of risk and complexity<br>• identify and address architectural risks relevant to your team or domain, for example, business, data, or security<br>• engage with architectural governance and assurance to effectively manage decisions and risks, with support |
| [Strategy design](../../skills/#strategy-design) | UK GDaD PCF | 胜任 | You can:<br>• support the development of a strategy or vision that aligns with organisational objectives<br>• challenge requirements and assumptions, and identify opportunities to develop strategy<br>• support the implementation of a strategy or vision, for example, by using a roadmap or plan<br>• use architectural principles, patterns, and constraints when appropriate |
| [Technical design throughout the life cycle](../../skills/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | 熟练 | You can:<br>• create technical designs characterised by medium risk, impact, and complexity<br>• maintain appropriate quality and architectural coherence of a technical design in response to change<br>• use feedback to optimise and refine technical designs throughout the life cycle |
| [了解医疗卫生和照护服务](../../skills/#了解医疗卫生和照护服务) | 本参考资料 | 熟练 | 您可以：<br>• 分析一项服务如何融入跨组织的照护路径<br>• 与临床医生、照护人员和患者合作塑造数字服务<br>• 解释数字决策对照护、安全和员工工作量的影响 |
| [健康数据互操作性](../../skills/#健康数据互操作性) | 本参考资料 | 熟练 | 您可以：<br>• 使用 FHIR、HL7 第 2 版和消息模式设计和构建集成<br>• 编写 FHIR 资源和实施指南并为其制定规范<br>• 解决系统之间复杂的映射和数据质量问题 |
| [信息治理与数据保护](../../skills/#信息治理与数据保护) | 本参考资料 | 胜任 | 您可以：<br>• 在工作中应用数据保护原则<br>• 为数据保护影响评估作出贡献<br>• 正确处理信息请求和记录 |
| [临床风险管理](../../skills/#临床风险管理) | 本参考资料 | 胜任 | 您可以：<br>• 参加危害研讨会并为危害日志作出贡献<br>• 在您的工作中遵循临床风险管理流程<br>• 为临床安全案例提供证据，例如测试结果 |
| [身份与访问管理](../../skills/#身份与访问管理) | 本参考资料 | 胜任 | 您可以：<br>• 创建、更改和删除用户账户及访问权限<br>• 依据基于角色的访问规则检查访问权限 |
| [医疗器械软件监管](../../skills/#医疗器械软件监管) | 本参考资料 | 了解 | 您可以：<br>• 解释一些健康软件作为医疗器械受到监管<br>• 知道当某个产品可能属于医疗器械时应向谁咨询 |

### 典型资质与经验

- 在复杂服务的技术设计方面拥有丰富经验，相当于硕士学位水平。

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

职级高于 UK GDaD PCF 职等建议（第 7 职级）：医疗卫生行业的招聘广告将此角色定为第 8a 职级。规划、政策和行动自由度的评分高于第 7 职级概况，因为该岗位在很少督导下为多个团队确定技术方向。

## 职级 8b: 首席技术架构师

**UK GDaD PCF 级别: Lead technical architect**

> A lead technical architect works with multiple projects or teams on problems that require broad architectural thinking.
> 
> At this role level, you will:
> - be responsible for leading the technical design of systems and services, justifying and communicating design decisions
> - assure other services and system quality, ensuring the technical work fits into the broader strategy for government
> - explore the benefits of cross-government alignment
> - provide mentoring within teams
> - provide leadership to other architects

### 职责

- 领导多项服务或多个团队的技术架构，制定共享的模式和标准。
- 在设计委员会中为设计的技术质量提供保证，包括安全、韧性和互操作性。
- 与企业架构师和工程负责人一起制定组织的技术路线图。
- 就技术选择、平台投资和技术风险向高级负责人提供建议。
- 领导和培养技术架构师。

### 技能

| 技能 | 来源 | 期望等级 | 该等级的含义 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../skills/#architect-for-the-whole-context) | UK GDaD PCF | 熟练 | You can:<br>• work to support wider organisational objectives beyond your immediate goals​<br>• track emerging internal and external issues over time that could affect the work of teams across the organisation<br>• take action to solve or mitigate problems by influencing colleagues across the organisation |
| [Architecture communication](../../skills/#architecture-communication) | UK GDaD PCF | 专家 | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Community collaboration](../../skills/#community-collaboration) | UK GDaD PCF | 熟练 | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../skills/#making-architectural-decisions) | UK GDaD PCF | 熟练 | You can:<br>• make and guide architectural design decisions characterised by medium risk and complexity<br>• identify and address architectural risks that affect multiple teams or domains<br>• use architectural governance and assurance to make design decisions and manage technical risks at the appropriate level<br>• contribute to the development of architectural governance and assurance |
| [Strategy design](../../skills/#strategy-design) | UK GDaD PCF | 熟练 | You can:<br>• define strategies or visions across teams that align with organisational objectives<br>• direct the implementation of a strategy or vision, for example, by creating roadmaps or plans<br>• define architectural principles and patterns<br>• develop or maintain strategy in response to feedback and findings |
| [Technical design throughout the life cycle](../../skills/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | 专家 | You can:<br>• create technical designs characterised by high risk, impact, and complexity<br>• lead and guide others in creating technical designs that achieve organisational objectives<br>• use feedback to optimise and refine standards for technical designs throughout the life cycle |
| [了解医疗卫生和照护服务](../../skills/#了解医疗卫生和照护服务) | 本参考资料 | 熟练 | 您可以：<br>• 分析一项服务如何融入跨组织的照护路径<br>• 与临床医生、照护人员和患者合作塑造数字服务<br>• 解释数字决策对照护、安全和员工工作量的影响 |
| [健康数据互操作性](../../skills/#健康数据互操作性) | 本参考资料 | 熟练 | 您可以：<br>• 使用 FHIR、HL7 第 2 版和消息模式设计和构建集成<br>• 编写 FHIR 资源和实施指南并为其制定规范<br>• 解决系统之间复杂的映射和数据质量问题 |
| [信息治理与数据保护](../../skills/#信息治理与数据保护) | 本参考资料 | 熟练 | 您可以：<br>• 领导数据保护影响评估和信息共享协议<br>• 就合法依据、同意、保密和保存向团队提供建议<br>• 调查事件并提出改进建议 |
| [临床风险管理](../../skills/#临床风险管理) | 本参考资料 | 熟练 | 您可以：<br>• 领导产品或变更的危害识别和风险评估<br>• 编写和维护危害日志及临床安全案例报告<br>• 与产品团队商定风险控制措施并检查其有效性<br>• 就如何应用临床风险管理标准向团队提供建议 |
| [身份与访问管理](../../skills/#身份与访问管理) | 本参考资料 | 熟练 | 您可以：<br>• 设计并运行身份与访问服务<br>• 定期审查访问权限并解决问题 |
| [医疗器械软件监管](../../skills/#医疗器械软件监管) | 本参考资料 | 胜任 | 您可以：<br>• 遵循符合医疗器械标准的软件生命周期流程<br>• 编制此类流程所要求的记录 |
| [人员管理](../../skills/#人员管理) | 本参考资料 | 熟练 | 您可以：<br>• 直线管理一个团队，设定目标并开展考评<br>• 关注身心健康，管理出勤、绩效和行为<br>• 规划团队的发展和继任 |

### 典型资质与经验

- 在领导复杂服务的技术架构方面拥有广泛经验。

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

## 职级 8c: 主任技术架构师

**UK GDaD PCF 级别: Principal technical architect**

> A principal technical architect leads at the highest level and is responsible for making sure the strategy is agreed and followed.
> 
> At this role level, you will:
> - network and communicate with senior stakeholders across organisations
> - proactively seek opportunities for digital transformation
> - support multiple teams, finding and using best practice and emerging technologies
> - inspire other architects and help them understand how to deliver the goals of the organisation
> - be responsible for governance, solving complex and high risk issues or delivering architecture design

### 职责

- 制定组织的技术架构战略、原则和标准。
- 治理全组织的技术设计，包括技术设计委员会。
- 就托管战略和平台整合等重大技术决策向执行团队提供建议。
- 在跨组织的技术和标准社群中代表组织。
- 激励和培养全组织的架构师。

### 技能

| 技能 | 来源 | 期望等级 | 该等级的含义 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../skills/#architect-for-the-whole-context) | UK GDaD PCF | 熟练 | You can:<br>• work to support wider organisational objectives beyond your immediate goals​<br>• track emerging internal and external issues over time that could affect the work of teams across the organisation<br>• take action to solve or mitigate problems by influencing colleagues across the organisation |
| [Architecture communication](../../skills/#architecture-communication) | UK GDaD PCF | 专家 | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Community collaboration](../../skills/#community-collaboration) | UK GDaD PCF | 熟练 | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../skills/#making-architectural-decisions) | UK GDaD PCF | 专家 | You can:<br>• make and guide architectural design decisions characterised by high levels of risk and complexity<br>• identify and address architectural risks across the organisation or wider government<br>• lead and evolve architectural governance and assurance<br>• represent architectural governance as part of wider governance, for example, legal or commercial |
| [Strategy design](../../skills/#strategy-design) | UK GDaD PCF | 专家 | You can:<br>• define and connect strategies or visions across the organisation or wider government<br>• enable the implementation of strategies or visions across the organisation or wider government, for example, by advocating for resources and removing blockers |
| [Technical design throughout the life cycle](../../skills/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | 专家 | You can:<br>• create technical designs characterised by high risk, impact, and complexity<br>• lead and guide others in creating technical designs that achieve organisational objectives<br>• use feedback to optimise and refine standards for technical designs throughout the life cycle |
| [了解医疗卫生和照护服务](../../skills/#了解医疗卫生和照护服务) | 本参考资料 | 熟练 | 您可以：<br>• 分析一项服务如何融入跨组织的照护路径<br>• 与临床医生、照护人员和患者合作塑造数字服务<br>• 解释数字决策对照护、安全和员工工作量的影响 |
| [健康数据互操作性](../../skills/#健康数据互操作性) | 本参考资料 | 专家 | 您可以：<br>• 为组织制定互操作性标准和战略<br>• 领导国家级或跨组织的标准工作<br>• 为跨多个系统的关键集成设计提供保证 |
| [信息治理与数据保护](../../skills/#信息治理与数据保护) | 本参考资料 | 熟练 | 您可以：<br>• 领导数据保护影响评估和信息共享协议<br>• 就合法依据、同意、保密和保存向团队提供建议<br>• 调查事件并提出改进建议 |
| [临床风险管理](../../skills/#临床风险管理) | 本参考资料 | 熟练 | 您可以：<br>• 领导产品或变更的危害识别和风险评估<br>• 编写和维护危害日志及临床安全案例报告<br>• 与产品团队商定风险控制措施并检查其有效性<br>• 就如何应用临床风险管理标准向团队提供建议 |
| [身份与访问管理](../../skills/#身份与访问管理) | 本参考资料 | 熟练 | 您可以：<br>• 设计并运行身份与访问服务<br>• 定期审查访问权限并解决问题 |
| [组织风险管理](../../skills/#组织风险管理) | 本参考资料 | 熟练 | 您可以：<br>• 为一个总监部或项目群运行风险流程<br>• 依据风险偏好评估风险并逐级上报<br>• 向委员会报告风险 |
| [人员管理](../../skills/#人员管理) | 本参考资料 | 熟练 | 您可以：<br>• 直线管理一个团队，设定目标并开展考评<br>• 关注身心健康，管理出勤、绩效和行为<br>• 规划团队的发展和继任 |

### 典型资质与经验

- 在领导多个团队或组织的技术架构方面拥有广泛经验。

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
