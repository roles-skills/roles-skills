# 测试工程师

> 这是一份面向通用数字医疗卫生机构的示例性参考档案。它不是任何雇主的正式职位说明，其中的岗位评估分数也不是正式评估。

> 本文由人工智能助手从英文翻译而来，尚未经过母语人士审校。引自英国政府数字与数据专业能力框架（UK GDaD PCF）和 ESCO 的内容保留英文原文。

**职族:** [质量保证测试](../../#质量保证测试)  
**职级:** 4, 6, 7, 8a  
**UK GDaD PCF 角色:** [Test engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/test-engineer/)  
**ESCO 职业:** [software tester](http://data.europa.eu/esco/occupation/106f79e4-6264-45f1-9e7a-297435cd684b) (ISCO-08 2519)

## 概述

测试工程师构建自动化测试、工具和框架，使团队能够快速、频繁地测试组织的数字健康服务。他们编写代码来测试功能、集成、性能、安全和韧性，并将测试内置于交付流水线中，使对临床系统和面向患者系统的变更能够安全发布。

## 在数字医疗卫生机构中

- 临床系统是安全关键系统，因此自动化回归测试保护危害日志中记录的安全控制措施，并作为安全案例的证据保存。
- 与其他医疗卫生和照护系统的集成需要依据 HL7 FHIR 和 HL7 第 2 版等标准进行自动化测试，通常使用模拟的合作方系统。
- 临床服务全天候运行，并在可预测的时间达到高峰，因此性能和韧性测试模拟真实的临床需求。
- 测试环境不得存有真实患者数据，因此工程师生成逼真的合成数据，包括罕见和边界临床病例。
- 作为医疗器械受到监管的软件，需要在其生命周期中按照 IEC 62304 等标准进行可追溯、可重复的测试。

## UK GDaD PCF 角色描述（英文原文）

> A test engineer designs, builds, automates and executes comprehensive, robust and maintainable test suites. They apply test engineering standards, perform exploratory testing and use diverse techniques to identify risks and improve testing efficiency and quality.
> 
> In this role you will:
> - maintain automated tests in continuous integration, continuous delivery (CI/CD) pipelines
> - use, develop and standardise reusable frameworks and tools following engineering practices and standards
> - analyse and test artefacts such as products, services and business processes
> - promote quality considerations throughout the development life cycle
> - support the resolution of technical issues

## 角色级别

| 职级 | 名称 | UK GDaD PCF 级别 | 英国公务员职等 | 岗位评估分数 |
| --- | --- | --- | --- | --- |
| 4 | [助理测试工程师](#职级-4-助理测试工程师) | Associate test engineer | EO | 275 |
| 6 | [测试工程师](#职级-6-测试工程师) | Test engineer | HEO/SEO | 411 |
| 7 | [高级测试工程师](#职级-7-高级测试工程师) | Senior test engineer | SEO/G7 | 477 |
| 8a | [首席测试工程师](#职级-8a-首席测试工程师) | Lead test engineer | SEO/G7/G6 | 553 |

## 职级 4: 助理测试工程师

**UK GDaD PCF 级别: Associate test engineer**

> An associate test engineer works closely with other test professionals to learn test engineering activities and techniques.
> 
> At this role level, you will:
> - contribute to and maintain technical test suites under supervision
> - follow engineering practices and standards to apply test approaches, plans and strategies under supervision
> - analyse artefacts such as user stories, prototypes, processes and designs with support
> - support the development of reports, recording of outcomes and resolution of defects
> - understand the technical tooling and engineering approach to design and execute tests

### 职责

- 在督导下按照团队的工程标准编写和维护简单的自动化测试。
- 执行自动化和手动测试，并准确记录结果。
- 协助调查和报告缺陷，包括与临床系统集成中的缺陷。
- 在测试环境中使用合成测试数据，并遵守信息治理规则。
- 学习团队的测试工具、编码实践和临床安全流程。

### 技能

| 技能 | 来源 | 期望等级 | 该等级的含义 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../skills/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 了解 | You can:<br>• explain why it's important to communicate technical concepts in non-technical language<br>• explain the types of communication that can be used with internal and external stakeholders, and their impact |
| [Designing and executing tests](../../skills/#designing-and-executing-tests) | UK GDaD PCF | 了解 | You can:<br>• contribute to deciding the most appropriate test types and techniques to use<br>• follow guidance to design, build and maintain simple tests that align to user needs and requirements<br>• execute simple tests with support<br>• explain the value of automation within testing |
| [Managing, reporting and resolving defects](../../skills/#managing-reporting-and-resolving-defects) | UK GDaD PCF | 了解 | You can:<br>• explain how to report and track defects<br>• follow a defect management process to report, communicate and maintain defects with appropriate information<br>• retest and escalate defects when needed |
| [Test analysis](../../skills/#test-analysis) | UK GDaD PCF | 了解 | You can:<br>• describe quality characteristics and explain why they are important<br>• analyse information, such as user stories, prototypes, processes and designs, with support<br>• explain what might be a risk in achieving quality goals |
| [Test and quality planning](../../skills/#test-and-quality-planning) | UK GDaD PCF | 了解 | You can:<br>• explain the value of quality testing approaches, plans and strategies<br>• explain how different delivery methodologies affect quality testing approaches, plans and strategies<br>• follow quality testing approaches, plans and strategies, with support<br>• explain how to measure the effectiveness of quality testing approaches, plans and strategies, and why it’s important |
| [Test engineering](../../skills/#test-engineering) | UK GDaD PCF | 了解 | You can:<br>• explain why testing processes, environments and tools are important<br>• follow test engineering practices and standards, with support<br>• support the maintenance of automated tests and tools required for testing |
| [了解医疗卫生和照护服务](../../skills/#了解医疗卫生和照护服务) | 本参考资料 | 了解 | 您可以：<br>• 描述医疗卫生和照护体系的主要组成部分以及组织所支持的服务<br>• 解释为什么患者安全和保密在您的工作中很重要 |
| [临床风险管理](../../skills/#临床风险管理) | 本参考资料 | 了解 | 您可以：<br>• 解释医疗信息系统可能如何伤害患者，例如通过错误、缺失或延迟的信息<br>• 通过正确途径报告可能的临床安全问题 |
| [信息治理与数据保护](../../skills/#信息治理与数据保护) | 本参考资料 | 了解 | 您可以：<br>• 遵循组织处理个人信息和健康信息的规则<br>• 识别并报告数据泄露或未遂事件 |

### 典型资质与经验

- 具有一定的编程或测试经验，或已注册相关学徒项目，或同等条件。

### 职级概要

- **知识:** 对工作领域有详细了解，通常来自基础学位、学徒制或同等经验。
- **自主性:** 在指导原则范围内工作；解决大多数日常问题；可向经理寻求建议。
- **范围:** 自己的工作以及一项明确的服务或流程。
- **领导力:** 可能督导一个小团队或协调他人的工作。
- **问责:** 交付一项明确的服务或流程。

### 岗位评估（示例）

| # | 因素 | 等级 | 分数 |
| --- | --- | --- | --- |
| 1 | 沟通与人际关系技能 | 3 | 21 |
| 2 | 知识、培训和经验 | 4 | 88 |
| 3 | 分析与判断技能 | 3 | 27 |
| 4 | 规划与组织技能 | 2 | 15 |
| 5 | 身体技能 | 3 | 27 |
| 6 | 对患者和服务对象照护的责任 | 1 | 4 |
| 7 | 政策与服务发展的责任 | 2 | 12 |
| 8 | 对财务和实物资源的责任 | 1 | 5 |
| 9 | 对人员的责任 | 1 | 5 |
| 10 | 对信息资源的责任 | 3 | 16 |
| 11 | 对研究与开发的责任 | 2 | 12 |
| 12 | 行动自由度 | 2 | 12 |
| 13 | 体力消耗 | 2 | 7 |
| 14 | 脑力消耗 | 3 | 12 |
| 15 | 情绪消耗 | 1 | 5 |
| 16 | 工作条件 | 2 | 7 |
| | **总计** | | **275** (职级 4: 271–325) |

## 职级 6: 测试工程师

**UK GDaD PCF 级别: Test engineer**

> A test engineer develops solutions to enable more efficient testing. They follow engineering standards to design and execute appropriate technical tests.
> 
> At this role level, you will:
> - determine test scope and estimate the effort required
> - select and use the most appropriate test approaches and techniques to mitigate risk
> - use technical tooling and engineering approaches to design and execute tests
> - develop and maintain technical test suites
> - develop reports, record outcomes and support the resolution of defects
> - contribute to and follow engineering practices and standards

### 职责

- 为临床服务和面向患者的服务设计和构建自动化的功能、集成和 API 测试。
- 构建依据 HL7 FHIR 规范和其他互操作性规范检查消息的测试。
- 生成涵盖真实和边界临床病例的合成患者数据。
- 将测试加入交付流水线，使与安全相关的检查在每次变更时运行。
- 估算测试工作量，报告结果，并支持缺陷的解决。

### 技能

| 技能 | 来源 | 期望等级 | 该等级的含义 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../skills/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 胜任 | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Designing and executing tests](../../skills/#designing-and-executing-tests) | UK GDaD PCF | 胜任 | You can:<br>• set up suitable environments with some support<br>• select appropriate test types and techniques with some support<br>• design, build, maintain and execute tests that align to user needs and requirements<br>• conduct exploratory testing<br>• research and try new test types and techniques |
| [Managing, reporting and resolving defects](../../skills/#managing-reporting-and-resolving-defects) | UK GDaD PCF | 胜任 | You can:<br>• collaborate with others to create a defect management process to report, communicate and resolve defects, with support<br>• critically assess dependencies, defects and risks, with support<br>• contribute to mitigation and contingency plans<br>• clearly communicate risks and the impact of defects to stakeholders |
| [Test analysis](../../skills/#test-analysis) | UK GDaD PCF | 胜任 | You can:<br>• work with stakeholders to determine which functional and non-functional quality characteristics add value<br>• determine what to test following an agreed approach<br>• identify and advocate for test needs, such as data, access and environments, with support<br>• analyse information to identify risks |
| [Test and quality planning](../../skills/#test-and-quality-planning) | UK GDaD PCF | 胜任 | You can:<br>• create or adapt quality testing approaches based on risk, with some support<br>• follow a quality testing strategy and contribute to its development<br>• contribute to continuous improvement of quality testing approaches, plans and strategies |
| [Test engineering](../../skills/#test-engineering) | UK GDaD PCF | 胜任 | You can:<br>• use test engineering frameworks and tools to support testing activities<br>• follow test engineering practices and standards, such as source control and continuous integration, continuous delivery (CI/CD) pipelines<br>• integrate and execute tests to ensure early testing and continuous feedback<br>• create and maintain automated tests, with some support<br>• write and review coded solutions, with some support |
| [了解医疗卫生和照护服务](../../skills/#了解医疗卫生和照护服务) | 本参考资料 | 胜任 | 您可以：<br>• 解释您的工作所支持的临床和照护工作流程<br>• 与临床和照护同事正确使用常见的医疗卫生术语<br>• 识别某项变更何时可能影响患者照护并提出来 |
| [临床风险管理](../../skills/#临床风险管理) | 本参考资料 | 胜任 | 您可以：<br>• 参加危害研讨会并为危害日志作出贡献<br>• 在您的工作中遵循临床风险管理流程<br>• 为临床安全案例提供证据，例如测试结果 |
| [信息治理与数据保护](../../skills/#信息治理与数据保护) | 本参考资料 | 胜任 | 您可以：<br>• 在工作中应用数据保护原则<br>• 为数据保护影响评估作出贡献<br>• 正确处理信息请求和记录 |
| [健康数据互操作性](../../skills/#健康数据互操作性) | 本参考资料 | 胜任 | 您可以：<br>• 阅读和使用 FHIR 资源、规范和 API<br>• 在指导下构建或测试简单的集成<br>• 依据规范检查消息 |

### 典型资质与经验

- 计算机或相关学科的学位，或同等经验。
- 具有构建自动化测试的经验。

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
| 10 | 对信息资源的责任 | 4 | 24 |
| 11 | 对研究与开发的责任 | 2 | 12 |
| 12 | 行动自由度 | 4 | 32 |
| 13 | 体力消耗 | 1 | 3 |
| 14 | 脑力消耗 | 4 | 18 |
| 15 | 情绪消耗 | 1 | 5 |
| 16 | 工作条件 | 2 | 7 |
| | **总计** | | **411** (职级 6: 396–465) |

## 职级 7: 高级测试工程师

**UK GDaD PCF 级别: Senior test engineer**

> A senior test engineer is responsible for test engineering in their area. They influence, coach and guide others in test engineering, sharing best practice and standards.
> 
> At this role level, you will:
> - select, use and guide others in using the most appropriate technical tooling, engineering approaches, test types and techniques to identify and address risks early
> - extend, standardise and build reusable frameworks and tools that support testing
> - communicate and document chosen approaches, tools, techniques and outcomes to the team and appropriate stakeholders
> - contribute to and agree engineering standards

### 职责

- 领导某一领域的测试工程，选择能及早应对其风险的工具、框架和测试类型。
- 为临床系统和合作方集成构建可复用的测试框架和模拟器。
- 根据真实临床需求规划并执行性能、负载和韧性测试。
- 确保自动化测试可追溯到危害和安全控制措施，并为安全案例产生证据。
- 辅导和指导其他测试工程师，并与开发人员商定工程标准。

### 技能

| 技能 | 来源 | 期望等级 | 该等级的含义 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../skills/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 熟练 | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Designing and executing tests](../../skills/#designing-and-executing-tests) | UK GDaD PCF | 熟练 | You can:<br>• set up suitable environments<br>• influence and guide the use of appropriate test types and techniques to mitigate risk early<br>• lead others in designing, building, maintaining and executing tests that align to user needs and requirements<br>• contribute to developing and implementing standards for designing and executing tests<br>• improve test types and techniques through a structured process. |
| [Managing, reporting and resolving defects](../../skills/#managing-reporting-and-resolving-defects) | UK GDaD PCF | 熟练 | You can:<br>• contribute to developing standards for defect management processes<br>• manage and escalate dependencies, defects and risks across teams<br>• contribute to mitigation and contingency plans across teams<br>• use defect patterns and trends to make recommendations on testing and quality approaches, with support<br>• manage stakeholder expectations and communications during defect resolution |
| [Test analysis](../../skills/#test-analysis) | UK GDaD PCF | 熟练 | You can:<br>• lead work with stakeholders across teams to determine which functional and non-functional quality characteristics add value<br>• determine if an approach needs to change based on effort and risk<br>• ensure test needs are implemented early<br>• use multiple techniques to analyse complex information to identify risks<br>• coach others in test analysis |
| [Test and quality planning](../../skills/#test-and-quality-planning) | UK GDaD PCF | 熟练 | You can:<br>• work with teams to develop and implement appropriate quality testing approaches, plans and strategies<br>• contribute to organisational quality testing strategies<br>• implement ways to capture data to drive continuous improvement of quality testing approaches, plans and strategies<br>• advocate for full team ownership of quality testing activities, encouraging early engagement |
| [Test engineering](../../skills/#test-engineering) | UK GDaD PCF | 熟练 | You can:<br>• develop, standardise and extend reusable frameworks and tools to support a range of testing activities<br>• guide and coach others in creating and maintaining comprehensive and reliable tests that meet standards<br>• research and prepare for future testing needs, including tools, methodologies and techniques<br>• maintain and adapt continuous integration, continuous delivery (CI/CD) pipelines |
| [了解医疗卫生和照护服务](../../skills/#了解医疗卫生和照护服务) | 本参考资料 | 胜任 | 您可以：<br>• 解释您的工作所支持的临床和照护工作流程<br>• 与临床和照护同事正确使用常见的医疗卫生术语<br>• 识别某项变更何时可能影响患者照护并提出来 |
| [临床风险管理](../../skills/#临床风险管理) | 本参考资料 | 胜任 | 您可以：<br>• 参加危害研讨会并为危害日志作出贡献<br>• 在您的工作中遵循临床风险管理流程<br>• 为临床安全案例提供证据，例如测试结果 |
| [信息治理与数据保护](../../skills/#信息治理与数据保护) | 本参考资料 | 胜任 | 您可以：<br>• 在工作中应用数据保护原则<br>• 为数据保护影响评估作出贡献<br>• 正确处理信息请求和记录 |
| [健康数据互操作性](../../skills/#健康数据互操作性) | 本参考资料 | 熟练 | 您可以：<br>• 使用 FHIR、HL7 第 2 版和消息模式设计和构建集成<br>• 编写 FHIR 资源和实施指南并为其制定规范<br>• 解决系统之间复杂的映射和数据质量问题 |
| [医疗器械软件监管](../../skills/#医疗器械软件监管) | 本参考资料 | 了解 | 您可以：<br>• 解释一些健康软件作为医疗器械受到监管<br>• 知道当某个产品可能属于医疗器械时应向谁咨询 |

### 典型资质与经验

- 在测试工程方面拥有丰富经验，相当于硕士学位水平。

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

## 职级 8a: 首席测试工程师

**UK GDaD PCF 级别: Lead test engineer**

> A lead test engineer sets the strategy for test engineering and influences test engineering practices across a broad area. They develop, monitor and evaluate quality engineering standards, and make strategic improvements to quality engineering in the organisation.
> 
> At this role level, you will:
> - lead a broad area in technical tooling, engineering approaches and test types and techniques to address risks early
> - define engineering standards, enabling others to follow them
> - lead and guide teams in quality engineering strategies and practices
> - lead and guide test engineers
> - escalate risks to senior stakeholders
> - lead and implement continuous testing, identifying opportunities to test earlier

### 职责

- 为广泛领域制定测试工程策略和标准，包括交付流水线中的持续测试。
- 领导和指导测试工程师及团队开展质量工程实践。
- 确保对受监管和安全关键软件的测试达到要求的标准并可追溯。
- 向高级产品、临床和供应商负责人上报质量和安全风险。
- 寻找更早、更频繁测试的机会，并衡量其对质量的影响。

### 技能

| 技能 | 来源 | 期望等级 | 该等级的含义 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../skills/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 专家 | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Designing and executing tests](../../skills/#designing-and-executing-tests) | UK GDaD PCF | 专家 | You can:<br>• set standards and influence organisational decisions for test types, techniques, design and execution<br>• coach others in test types, techniques, design and execution<br>• advocate for continuous improvement and refinement of test types and techniques<br>• make strategic decisions on new or improved test types and techniques used in your area |
| [Managing, reporting and resolving defects](../../skills/#managing-reporting-and-resolving-defects) | UK GDaD PCF | 专家 | You can:<br>• lead and coach others in improving test and defect management processes<br>• support others in assessing complex and challenging defects across the organisation<br>• lead and coach others in using defect patterns and trends to make tactical and strategic recommendations<br>• influence improvements to quality processes, informed by defect patterns and trends |
| [Test analysis](../../skills/#test-analysis) | UK GDaD PCF | 专家 | You can:<br>• lead and guide multiple teams in test analysis, ensuring it is implemented early in the life cycle<br>• advocate for risk-based analysis to drive improvements across many teams<br>• set standards and principles for test analysis across the organisation |
| [Test and quality planning](../../skills/#test-and-quality-planning) | UK GDaD PCF | 专家 | You can:<br>• create and manage multiple quality testing plans, approaches and strategies<br>• lead and guide multiple teams in adopting quality testing strategy<br>• advocate for early quality testing involvement in organisational delivery processes<br>• guide teams across an organisation in optimising quality testing approaches, plans and strategies by using appropriate data |
| [Test engineering](../../skills/#test-engineering) | UK GDaD PCF | 专家 | You can:<br>• establish and lead test engineering practices, standards and behaviours<br>• influence and guide test engineering technology and tool choices across the organisation<br>• advocate for the adoption and use of appropriate testing solutions, ensuring alignment with organisational goals and quality objectives |
| [了解医疗卫生和照护服务](../../skills/#了解医疗卫生和照护服务) | 本参考资料 | 熟练 | 您可以：<br>• 分析一项服务如何融入跨组织的照护路径<br>• 与临床医生、照护人员和患者合作塑造数字服务<br>• 解释数字决策对照护、安全和员工工作量的影响 |
| [临床风险管理](../../skills/#临床风险管理) | 本参考资料 | 熟练 | 您可以：<br>• 领导产品或变更的危害识别和风险评估<br>• 编写和维护危害日志及临床安全案例报告<br>• 与产品团队商定风险控制措施并检查其有效性<br>• 就如何应用临床风险管理标准向团队提供建议 |
| [信息治理与数据保护](../../skills/#信息治理与数据保护) | 本参考资料 | 胜任 | 您可以：<br>• 在工作中应用数据保护原则<br>• 为数据保护影响评估作出贡献<br>• 正确处理信息请求和记录 |
| [健康数据互操作性](../../skills/#健康数据互操作性) | 本参考资料 | 熟练 | 您可以：<br>• 使用 FHIR、HL7 第 2 版和消息模式设计和构建集成<br>• 编写 FHIR 资源和实施指南并为其制定规范<br>• 解决系统之间复杂的映射和数据质量问题 |
| [医疗器械软件监管](../../skills/#医疗器械软件监管) | 本参考资料 | 胜任 | 您可以：<br>• 遵循符合医疗器械标准的软件生命周期流程<br>• 编制此类流程所要求的记录 |
| [人员管理](../../skills/#人员管理) | 本参考资料 | 胜任 | 您可以：<br>• 督导日常工作并给予反馈<br>• 参与招聘和入职引导<br>• 定期进行一对一谈话 |

### 典型资质与经验

- 在领导复杂服务的测试工程方面拥有广泛经验。

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
| 8 | 对财务和实物资源的责任 | 1 | 5 |
| 9 | 对人员的责任 | 3 | 21 |
| 10 | 对信息资源的责任 | 5 | 34 |
| 11 | 对研究与开发的责任 | 3 | 21 |
| 12 | 行动自由度 | 5 | 45 |
| 13 | 体力消耗 | 1 | 3 |
| 14 | 脑力消耗 | 4 | 18 |
| 15 | 情绪消耗 | 1 | 5 |
| 16 | 工作条件 | 2 | 7 |
| | **总计** | | **553** (职级 8a: 540–584) |

UK GDaD PCF 建议此级别为 SEO 至 G6，对应第 7 职级，与高级测试工程师相同。本参考资料将其定为第 8a 职级，因为它为广泛领域制定测试工程策略和标准。


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
