# 集成工程师（医疗互操作性）

> 这是一份面向通用数字医疗卫生机构的示例性参考档案。它不是任何雇主的正式职位说明，其中的岗位评估分数也不是正式评估。

> 本文由人工智能助手从英文翻译而来，尚未经过母语人士审校。引自英国政府数字与数据专业能力框架（UK GDaD PCF）和 ESCO 的内容保留英文原文。

**职族:** [软件开发](../../#软件开发)  
**职级:** 5, 6, 7, 8a  
**UK GDaD PCF 角色:** 无（本参考资料定义该角色）  
**ESCO 职业:** [integration engineer](http://data.europa.eu/esco/occupation/07e60525-1aad-4099-aaf3-2c7014c92212) (ISCO-08 2511); [database developer](http://data.europa.eu/esco/occupation/b11e1742-5e28-4270-b081-b0193d85ee7d) (ISCO-08 2521)

## 概述

集成工程师连接组织的临床和业务系统，使医疗卫生和照护信息安全地流向需要它的地方。他们使用 HL7 FHIR 和 HL7 第 2 版等标准设计、构建、测试和支持接口、API 和消息流，在系统之间映射数据和临床代码，并保持集成在上线服务中正常运行。

## 在数字医疗卫生机构中

- 消息（例如检查结果或转诊）丢失、延迟、重复或匹配错误可能直接导致伤害，因此集成工作遵循临床风险管理流程。
- 集成在组织之间传输大量保密的健康信息，因此每个数据流都需要合法依据、安全传输和审计。
- 医疗系统使用许多标准和版本，从 HL7 第 2 版消息到 HL7 FHIR API 和 IHE 规范，往往还带有本地变体。
- 临床含义必须在传输过程中保持不变，因此工程师要正确映射 SNOMED CT 等临床术语，并可靠地匹配患者。
- 许多集成全天候支持照护，因此需要监控、警报以及处理失败消息的清晰途径。

## 角色级别

| 职级 | 名称 | UK GDaD PCF 级别 | 英国公务员职等 | 岗位评估分数 |
| --- | --- | --- | --- | --- |
| 5 | [初级集成工程师](#职级-5-初级集成工程师) | — | — | 335 |
| 6 | [集成工程师](#职级-6-集成工程师) | — | — | 418 |
| 7 | [高级集成工程师](#职级-7-高级集成工程师) | — | — | 477 |
| 8a | [首席集成工程师](#职级-8a-首席集成工程师) | — | — | 551 |

## 职级 5: 初级集成工程师

初级集成工程师根据规范并在更有经验的工程师指导下，构建、测试和支持医疗卫生和照护系统之间的集成。

### 职责

- 根据商定的规范构建和修改消息映射、转换和 API 调用。
- 依据规范和示例消息测试集成，包括错误和边界情况。
- 监控消息流，调查失败或被拒绝的消息，并予以解决或上报。
- 遵循上线数据和测试数据的信息治理规则，安全地处理健康数据。
- 记录变更和测试结果，以便用作临床安全证据。

### 技能

| 技能 | 来源 | 期望等级 | 该等级的含义 |
| --- | --- | --- | --- |
| [Systems integration](../../skills/#systems-integration) | UK GDaD PCF | 胜任 | You can:<br>• build and test simple interfaces between systems<br>• work on more complex integration as part of a wider team |
| [Programming and build (software engineering)](../../skills/#programming-and-build-software-engineering) | UK GDaD PCF | 胜任 | You can:<br>• design, code, test, correct and document simple programs or scripts under the direction of others |
| [Testing](../../skills/#testing) | UK GDaD PCF | 胜任 | You can:<br>• review requirements and specifications, and define test conditions<br>• identify issues and risks associated with work<br>• analyse and report test activities and results |
| [Service support](../../skills/#service-support) | UK GDaD PCF | 胜任 | You can:<br>• help fix service faults following agreed procedures<br>• carry out maintenance tasks on service support infrastructure |
| [Information security](../../skills/#information-security) | UK GDaD PCF | 了解 | You can:<br>• explain information security and the security controls available to protect solutions and services |
| [健康数据互操作性](../../skills/#健康数据互操作性) | 本参考资料 | 胜任 | 您可以：<br>• 阅读和使用 FHIR 资源、规范和 API<br>• 在指导下构建或测试简单的集成<br>• 依据规范检查消息 |
| [临床术语与分类](../../skills/#临床术语与分类) | 本参考资料 | 了解 | 您可以：<br>• 解释临床术语与分类之间的区别<br>• 识别 SNOMED CT 和 ICD 等常见术语 |
| [信息治理与数据保护](../../skills/#信息治理与数据保护) | 本参考资料 | 胜任 | 您可以：<br>• 在工作中应用数据保护原则<br>• 为数据保护影响评估作出贡献<br>• 正确处理信息请求和记录 |
| [临床风险管理](../../skills/#临床风险管理) | 本参考资料 | 了解 | 您可以：<br>• 解释医疗信息系统可能如何伤害患者，例如通过错误、缺失或延迟的信息<br>• 通过正确途径报告可能的临床安全问题 |
| [了解医疗卫生和照护服务](../../skills/#了解医疗卫生和照护服务) | 本参考资料 | 了解 | 您可以：<br>• 描述医疗卫生和照护体系的主要组成部分以及组织所支持的服务<br>• 解释为什么患者安全和保密在您的工作中很重要 |

### 典型资质与经验

- 计算机或相关学科的学位、已完成的学徒培训，或同等经验。

### 职级概要

- **知识:** 具备专业或技术知识，通常来自学位或同等经验。
- **自主性:** 在专业标准范围内按总体目标工作；自行规划工作。
- **范围:** 团队或产品内自己的专业工作。
- **领导力:** 可能指导并检查支持人员和学徒的工作。
- **问责:** 自己专业工作的质量。

### 岗位评估（示例）

| # | 因素 | 等级 | 分数 |
| --- | --- | --- | --- |
| 1 | 沟通与人际关系技能 | 4 | 32 |
| 2 | 知识、培训和经验 | 5 | 120 |
| 3 | 分析与判断技能 | 3 | 27 |
| 4 | 规划与组织技能 | 2 | 15 |
| 5 | 身体技能 | 3 | 27 |
| 6 | 对患者和服务对象照护的责任 | 1 | 4 |
| 7 | 政策与服务发展的责任 | 2 | 12 |
| 8 | 对财务和实物资源的责任 | 1 | 5 |
| 9 | 对人员的责任 | 1 | 5 |
| 10 | 对信息资源的责任 | 4 | 24 |
| 11 | 对研究与开发的责任 | 2 | 12 |
| 12 | 行动自由度 | 3 | 21 |
| 13 | 体力消耗 | 2 | 7 |
| 14 | 脑力消耗 | 3 | 12 |
| 15 | 情绪消耗 | 1 | 5 |
| 16 | 工作条件 | 2 | 7 |
| | **总计** | | **335** (职级 5: 326–395) |

## 职级 6: 集成工程师

集成工程师独立设计、构建和支持医疗卫生和照护系统之间的集成，并帮助确定系统应如何交换数据。

### 职责

- 使用 HL7 FHIR、HL7 第 2 版和消息模式设计和构建集成、API 和消息流。
- 分析源系统和目标系统，编写接口规范和数据映射，包括临床代码。
- 构建患者匹配、校验和错误处理，使信息进入正确的记录。
- 参加危害研讨会，将失败或延迟消息警报等安全控制措施构建到集成中。
- 与供应商和合作组织一起测试新的连接并使其上线。
- 调查并修复上线集成中的问题，并指导初级集成工程师。

### 技能

| 技能 | 来源 | 期望等级 | 该等级的含义 |
| --- | --- | --- | --- |
| [Systems integration](../../skills/#systems-integration) | UK GDaD PCF | 熟练 | You can:<br>• define the integration build<br>• co-ordinate build activities across systems<br>• understand how to undertake and support integration testing activities |
| [Programming and build (software engineering)](../../skills/#programming-and-build-software-engineering) | UK GDaD PCF | 熟练 | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../skills/#systems-design) | UK GDaD PCF | 胜任 | You can:<br>• translate logical designs into physical designs<br>• produce detailed designs<br>• effectively document all work using required standards, methods and tools, including prototyping tools where appropriate<br>• design systems characterised by managed levels of risk, manageable business and technical complexity, and meaningful impact<br>• work with well understood technology and identify appropriate patterns |
| [Service support](../../skills/#service-support) | UK GDaD PCF | 熟练 | You can:<br>• identify, locate and fix service faults |
| [Information security](../../skills/#information-security) | UK GDaD PCF | 胜任 | You can:<br>• use information security practices and available security controls to contribute to protecting solutions and services |
| [健康数据互操作性](../../skills/#健康数据互操作性) | 本参考资料 | 熟练 | 您可以：<br>• 使用 FHIR、HL7 第 2 版和消息模式设计和构建集成<br>• 编写 FHIR 资源和实施指南并为其制定规范<br>• 解决系统之间复杂的映射和数据质量问题 |
| [临床术语与分类](../../skills/#临床术语与分类) | 本参考资料 | 胜任 | 您可以：<br>• 为数据项或表单查找并使用正确的代码<br>• 使用术语浏览器和参考集 |
| [信息治理与数据保护](../../skills/#信息治理与数据保护) | 本参考资料 | 胜任 | 您可以：<br>• 在工作中应用数据保护原则<br>• 为数据保护影响评估作出贡献<br>• 正确处理信息请求和记录 |
| [临床风险管理](../../skills/#临床风险管理) | 本参考资料 | 胜任 | 您可以：<br>• 参加危害研讨会并为危害日志作出贡献<br>• 在您的工作中遵循临床风险管理流程<br>• 为临床安全案例提供证据，例如测试结果 |
| [了解医疗卫生和照护服务](../../skills/#了解医疗卫生和照护服务) | 本参考资料 | 胜任 | 您可以：<br>• 解释您的工作所支持的临床和照护工作流程<br>• 与临床和照护同事正确使用常见的医疗卫生术语<br>• 识别某项变更何时可能影响患者照护并提出来 |

### 典型资质与经验

- 计算机或相关学科的学位，或同等经验。
- 构建和支持生产系统之间集成的经验。

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
| 9 | 对人员的责任 | 2 | 12 |
| 10 | 对信息资源的责任 | 4 | 24 |
| 11 | 对研究与开发的责任 | 2 | 12 |
| 12 | 行动自由度 | 4 | 32 |
| 13 | 体力消耗 | 1 | 3 |
| 14 | 脑力消耗 | 4 | 18 |
| 15 | 情绪消耗 | 1 | 5 |
| 16 | 工作条件 | 2 | 7 |
| | **总计** | | **418** (职级 6: 396–465) |

## 职级 7: 高级集成工程师

高级集成工程师领导跨多个系统和组织的复杂集成的设计和交付，并为其负责领域制定集成标准。

### 职责

- 领导复杂集成的技术设计，例如跨组织的共享照护记录、检查结果和转诊。
- 为组织编写和维护 FHIR 规范、实施指南和接口标准。
- 将集成设计为安全、有韧性且可观测，并具备处理故障的清晰途径。
- 与临床安全官合作识别集成危害，确保控制措施在设计中落实并经过测试。
- 与信息治理同事合作，确保每个数据流都有商定的合法依据和数据共享安排。
- 辅导和培养团队中的集成工程师。

### 技能

| 技能 | 来源 | 期望等级 | 该等级的含义 |
| --- | --- | --- | --- |
| [Systems integration](../../skills/#systems-integration) | UK GDaD PCF | 专家 | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Programming and build (software engineering)](../../skills/#programming-and-build-software-engineering) | UK GDaD PCF | 熟练 | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../skills/#systems-design) | UK GDaD PCF | 熟练 | You can:<br>• design systems characterised by medium levels of risk, impact, and business or technical complexity<br>• select appropriate design standards, methods and tools, and ensure they are applied effectively<br>• review the systems designs of others to ensure the selection of appropriate technology, efficient use of resources and integration of multiple systems and technology |
| [Information security](../../skills/#information-security) | UK GDaD PCF | 熟练 | You can:<br>• design solutions and services with security controls included, specifically engineered to mitigate security threats |
| [Stakeholder relationship management](../../skills/#stakeholder-relationship-management) | UK GDaD PCF | 胜任 | You can:<br>• identify important stakeholders and communicate with them clearly and regularly<br>• tailor communication to stakeholders' needs and work with them to build relationships while meeting user needs<br>• build and reach consensus with stakeholders<br>• work to improve stakeholder relationships using evidence to explain decisions |
| [健康数据互操作性](../../skills/#健康数据互操作性) | 本参考资料 | 熟练 | 您可以：<br>• 使用 FHIR、HL7 第 2 版和消息模式设计和构建集成<br>• 编写 FHIR 资源和实施指南并为其制定规范<br>• 解决系统之间复杂的映射和数据质量问题 |
| [临床术语与分类](../../skills/#临床术语与分类) | 本参考资料 | 熟练 | 您可以：<br>• 使用临床术语设计数据模型和参考集<br>• 在术语和分类之间进行映射，并解释映射的局限<br>• 就产品和分析中的术语使用向团队提供建议 |
| [信息治理与数据保护](../../skills/#信息治理与数据保护) | 本参考资料 | 熟练 | 您可以：<br>• 领导数据保护影响评估和信息共享协议<br>• 就合法依据、同意、保密和保存向团队提供建议<br>• 调查事件并提出改进建议 |
| [临床风险管理](../../skills/#临床风险管理) | 本参考资料 | 胜任 | 您可以：<br>• 参加危害研讨会并为危害日志作出贡献<br>• 在您的工作中遵循临床风险管理流程<br>• 为临床安全案例提供证据，例如测试结果 |
| [身份与访问管理](../../skills/#身份与访问管理) | 本参考资料 | 胜任 | 您可以：<br>• 创建、更改和删除用户账户及访问权限<br>• 依据基于角色的访问规则检查访问权限 |

### 典型资质与经验

- 在设计和支持健康领域或其他复杂集成方面拥有丰富经验，相当于硕士学位水平。

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

## 职级 8a: 首席集成工程师

首席集成工程师领导组织的集成工程，确定其技术方向和标准，并为跨多个系统的关键集成提供保证。

### 职责

- 领导全组织的集成工程，确定方向、模式和标准。
- 为承载检查结果、药物或警报的关键集成的设计提供保证。
- 与架构师、产品经理和供应商一起制定集成平台路线图。
- 在跨组织的互操作性和标准工作中代表组织。
- 直线管理或领导集成工程师，发展集成实践社群。

### 技能

| 技能 | 来源 | 期望等级 | 该等级的含义 |
| --- | --- | --- | --- |
| [Systems integration](../../skills/#systems-integration) | UK GDaD PCF | 专家 | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Systems design](../../skills/#systems-design) | UK GDaD PCF | 专家 | You can:<br>• design systems characterised by high levels of risk, impact, and business or technical complexity<br>• control system design practice within an enterprise or industry architecture<br>• influence industry-based models for the development of new technology applications<br>• develop effective implementation and procurement strategies, consistent with business needs<br>• ensure adherence to relevant technical strategies, policies, standards and practices |
| [Technical design throughout the life cycle](../../skills/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | 熟练 | You can:<br>• create technical designs characterised by medium risk, impact, and complexity<br>• maintain appropriate quality and architectural coherence of a technical design in response to change<br>• use feedback to optimise and refine technical designs throughout the life cycle |
| [Stakeholder relationship management](../../skills/#stakeholder-relationship-management) | UK GDaD PCF | 熟练 | You can:<br>• work with the team to develop and maintain an understanding of stakeholders<br>• work with the team to develop and implement stakeholder communications strategies<br>• identify and resolve issues, influence stakeholders and manage relationships effectively<br>• build long-term strategic relationships and communicate clearly and regularly with stakeholders |
| [Leadership and guidance](../../skills/#leadership-and-guidance) | UK GDaD PCF | 熟练 | You can:<br>• make decisions characterised by medium levels of risk and complexity and recommend decisions as risk and complexity increase<br>• build consensus between services or independent stakeholders<br>• identify problems or issues in the team dynamic and rectify them<br>• engage in varying types of feedback, choosing the right type at the appropriate time and ensuring the discussion and decision stick<br>• bring people together to form a motivated team and help create the right environment for a team to work in<br>• facilitate the best team makeup depending on the situation |
| [健康数据互操作性](../../skills/#健康数据互操作性) | 本参考资料 | 专家 | 您可以：<br>• 为组织制定互操作性标准和战略<br>• 领导国家级或跨组织的标准工作<br>• 为跨多个系统的关键集成设计提供保证 |
| [临床术语与分类](../../skills/#临床术语与分类) | 本参考资料 | 熟练 | 您可以：<br>• 使用临床术语设计数据模型和参考集<br>• 在术语和分类之间进行映射，并解释映射的局限<br>• 就产品和分析中的术语使用向团队提供建议 |
| [信息治理与数据保护](../../skills/#信息治理与数据保护) | 本参考资料 | 熟练 | 您可以：<br>• 领导数据保护影响评估和信息共享协议<br>• 就合法依据、同意、保密和保存向团队提供建议<br>• 调查事件并提出改进建议 |
| [临床风险管理](../../skills/#临床风险管理) | 本参考资料 | 熟练 | 您可以：<br>• 领导产品或变更的危害识别和风险评估<br>• 编写和维护危害日志及临床安全案例报告<br>• 与产品团队商定风险控制措施并检查其有效性<br>• 就如何应用临床风险管理标准向团队提供建议 |
| [人员管理](../../skills/#人员管理) | 本参考资料 | 熟练 | 您可以：<br>• 直线管理一个团队，设定目标并开展考评<br>• 关注身心健康，管理出勤、绩效和行为<br>• 规划团队的发展和继任 |

### 典型资质与经验

- 在领导复杂医疗卫生或照护系统的集成工程方面拥有广泛经验。

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


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
