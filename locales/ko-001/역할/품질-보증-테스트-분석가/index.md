# 품질 보증 테스트 분석가

> 이 문서는 일반적인 디지털 헬스케어 조직을 위한 예시용 참조 프로필입니다. 특정 고용주의 공식 직무기술서가 아니며, 직무평가 점수도 공식 평가가 아닙니다.

> 이 글은 AI 어시스턴트가 영어를 한국어로 번역한 것이며, 한국어 원어민의 검토는 아직 받지 않았습니다. 영국 정부 디지털·데이터 전문직 역량 프레임워크(UK GDaD PCF)와 ESCO의 인용문은 영어 그대로 두었습니다.

**직군:** [품질 보증과 테스트](../../#품질-보증과-테스트)  
**밴드:** 4, 5, 6, 8a  
**UK GDaD PCF 역할:** [Quality assurance test analyst](https://understand-digital-data-roles-skills.service.gov.uk/role/quality-assurance-test-analyst/)  
**ESCO 직업:** [ICT test analyst](http://data.europa.eu/esco/occupation/0ab5c12c-c1c1-4772-8345-aa287d0e391d) (ISCO-08 2519)

## 개요

품질 보증 테스트 분석가는 조직의 디지털 헬스 서비스가 환자, 임상의, 돌봄 직원에게 필요한 일을 안전하고 확실하게 하는지 확인한다. 요구사항과 설계를 분석해 리스크를 일찍 찾아내고, 기능 및 비기능 테스트를 설계하여 실행하며, 결함을 명확하게 보고한다. 의료에서는 임상 워크플로, 데이터 정확성, 환자를 해로부터 보호하는 통제에 대한 테스트도 포함된다.

## 디지털 헬스케어 조직에서

- 임상 시스템의 결함은 잘못된 투약량, 놓친 결과, 다른 환자의 기록 표시 등을 통해 환자에게 해를 끼칠 수 있으므로, 테스트는 임상 리스크로 우선순위가 정해진다.
- 테스트는 임상 안전 케이스와 위험 요소 로그의 근거를 제공하므로, 테스트 계획은 식별된 위험 요소와 그 통제에 추적 가능하다.
- 테스트 데이터가 실제 환자를 드러내서는 안 되므로, 분석가는 합성 데이터 또는 적절히 비식별화된 테스트 데이터를 사용한다.
- 많은 서비스가 다른 보건·돌봄 시스템과 데이터를 교환하므로, 테스트에서는 HL7 FHIR 같은 표준에 비추어 메시지를 점검하고 임상 코드의 의미를 확인한다.
- 이용자에는 시간 압박 속의 임상의, 폭넓은 요구를 가진 환자, 보조 기술 이용자가 포함되므로, 사용성 및 접근성 테스트가 중요하다.

## UK GDaD PCF 역할 설명(원문은 영어)

> A quality assurance test analyst interprets testing needs, creating and executing appropriate tests to ensure quality and alignment with requirements.
> 
> In this role, you will:
> - plan, design and execute tests
> - apply testing techniques and standards to learn about systems and mitigate risk
> - analyse artefacts and prototypes
> - test outcomes and record defects
> - seek to improve testing practices to enhance quality and reliability
> - recommend testing approaches

## 역할 수준

| 밴드 | 직함 | UK GDaD PCF 수준 | 영국 공무원 등급 | 직무평가 점수 |
| --- | --- | --- | --- | --- |
| 4 | [어소시에이트 품질 보증 테스트 분석가](#밴드-4-어소시에이트-품질-보증-테스트-분석가) | Associate quality assurance test analyst | EO | 275 |
| 5 | [품질 보증 테스트 분석가](#밴드-5-품질-보증-테스트-분석가) | Quality assurance test analyst | HEO/SEO | 327 |
| 6 | [시니어 품질 보증 테스트 분석가](#밴드-6-시니어-품질-보증-테스트-분석가) | Senior quality assurance test analyst | HEO/SEO | 404 |
| 8a | [리드 품질 보증 테스트 분석가](#밴드-8a-리드-품질-보증-테스트-분석가) | Lead quality assurance test analyst | G7/G6 | 543 |

## 밴드 4: 어소시에이트 품질 보증 테스트 분석가

**UK GDaD PCF 수준: Associate quality assurance test analyst**

> An associate quality assurance test analyst works with other test professionals to learn quality assurance testing and analysis techniques.
> 
> At this role level, you will:
> - follow and apply test approaches, plans and strategies, under supervision
> - analyse artefacts, such as user stories, prototypes, processes and designs, with support
> - use basic functional and non-functional testing techniques
> - increase your understanding of how to design and execute basic tests, develop reports, record outcomes and support the resolution of defects

### 책임

- 감독을 받으며 임상 및 사무 워크플로의 테스트 스크립트를 실행하고 결과를 정확하게 기록한다.
- 절차, 데이터, 관련 화면을 포함하여 명확한 결함 보고서를 올린다.
- 합성 테스트 데이터를 사용하고 테스트 환경에서 실제 환자 데이터를 절대 쓰지 않는다.
- 팀의 테스트 접근법, 도구, 임상 안전 프로세스를 배운다.
- 스탠드업, 계획, 회고 같은 팀 행사에 참여한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../스킬/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 인지 | You can:<br>• explain why it's important to communicate technical concepts in non-technical language<br>• explain the types of communication that can be used with internal and external stakeholders, and their impact |
| [Designing and executing tests](../../스킬/#designing-and-executing-tests) | UK GDaD PCF | 인지 | You can:<br>• contribute to deciding the most appropriate test types and techniques to use<br>• follow guidance to design, build and maintain simple tests that align to user needs and requirements<br>• execute simple tests with support<br>• explain the value of automation within testing |
| [Managing, reporting and resolving defects](../../스킬/#managing-reporting-and-resolving-defects) | UK GDaD PCF | 인지 | You can:<br>• explain how to report and track defects<br>• follow a defect management process to report, communicate and maintain defects with appropriate information<br>• retest and escalate defects when needed |
| [Test analysis](../../스킬/#test-analysis) | UK GDaD PCF | 인지 | You can:<br>• describe quality characteristics and explain why they are important<br>• analyse information, such as user stories, prototypes, processes and designs, with support<br>• explain what might be a risk in achieving quality goals |
| [Test and quality planning](../../스킬/#test-and-quality-planning) | UK GDaD PCF | 인지 | You can:<br>• explain the value of quality testing approaches, plans and strategies<br>• explain how different delivery methodologies affect quality testing approaches, plans and strategies<br>• follow quality testing approaches, plans and strategies, with support<br>• explain how to measure the effectiveness of quality testing approaches, plans and strategies, and why it’s important |
| [Test engineering](../../스킬/#test-engineering) | UK GDaD PCF | 인지 | You can:<br>• explain why testing processes, environments and tools are important<br>• follow test engineering practices and standards, with support<br>• support the maintenance of automated tests and tools required for testing |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 보건·돌봄 시스템의 주요 부분과 조직이 지원하는 서비스를 설명한다<br>• 자신의 업무에서 환자 안전과 비밀 유지가 중요한 이유를 설명한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 잘못되었거나, 빠졌거나, 지연된 정보 등을 통해 보건 IT 시스템이 환자에게 어떻게 해를 끼칠 수 있는지 설명한다<br>• 임상 안전 문제 가능성을 올바른 경로로 보고한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 개인 정보와 건강 정보를 다루는 조직의 규칙을 따른다<br>• 데이터 침해나 아차 사고를 알아보고 보고한다 |

### 일반적인 자격과 경력

- 우수한 분석력과 글쓰기 능력, 그리고 테스트나 디지털 시스템을 다룬 일정한 경력, 또는 그에 준하는 것.

### 밴드 개요

- **지식:** 담당 분야에 대한 상세한 지식. 보통 전문대학 학위, 도제 과정, 또는 그에 준하는 경력으로 얻는다.
- **자율성:** 가이드라인 안에서 일하고, 일상적인 문제 대부분을 해결하며, 조언을 구할 상급자가 있다.
- **범위:** 자신의 업무와 정해진 서비스 또는 프로세스.
- **리더십:** 작은 팀을 감독하거나 다른 사람의 업무를 조정할 수 있다.
- **책무:** 정해진 서비스 또는 프로세스의 제공.

### 직무평가(예시)

| # | 요소 | 수준 | 점수 |
| --- | --- | --- | --- |
| 1 | 의사소통 및 관계 형성 기술 | 3 | 21 |
| 2 | 지식, 교육, 경험 | 4 | 88 |
| 3 | 분석 및 판단 기술 | 3 | 27 |
| 4 | 계획 및 조직화 기술 | 2 | 15 |
| 5 | 신체 기술 | 3 | 27 |
| 6 | 환자·이용자 돌봄에 대한 책임 | 1 | 4 |
| 7 | 정책 및 서비스 개발에 대한 책임 | 2 | 12 |
| 8 | 재무 및 물적 자원에 대한 책임 | 1 | 5 |
| 9 | 사람에 대한 책임 | 1 | 5 |
| 10 | 정보 자원에 대한 책임 | 3 | 16 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 2 | 12 |
| 13 | 신체적 부담 | 2 | 7 |
| 14 | 정신적 부담 | 3 | 12 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **275** (밴드 4: 271–325) |

## 밴드 5: 품질 보증 테스트 분석가

**UK GDaD PCF 수준: Quality assurance test analyst**

> A quality assurance test analyst designs and executes appropriate functional and non-functional tests. They apply multiple testing techniques to inform the approach to mitigate risk.
> 
> At this role level, you will:
> - apply the most appropriate test approaches and plans based on risk
> - analyse artefacts, such as user stories, prototypes, processes and designs
> - determine what to test following an agreed approach
> - ensure test coverage aligns with business risk
> - follow appropriate standards to mitigate risk early
> - execute tests, develop reports, record outcomes and support the resolution of defects

### 책임

- 사용자 스토리, 설계, 임상 워크플로를 분석하여 환자와 서비스에 대한 리스크를 바탕으로 무엇을 테스트할지 결정한다.
- 엔드투엔드 임상 시나리오를 포함하여 기능, 접근성, 사용성 테스트를 설계하고 실행한다.
- 테스트를 위험 요소와 안전 통제에 추적 가능하게 하고 임상 안전 케이스를 위한 테스트 근거를 제공한다.
- 이용자에게 표시되는 데이터를 원본 시스템과 합의된 임상 코드에 비추어 확인한다.
- 현실적인 합성 테스트 데이터를 만들고 유지한다.
- 결함을 해결될 때까지 추적하고 수정 사항을 재테스트한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../스킬/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 실무 | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Designing and executing tests](../../스킬/#designing-and-executing-tests) | UK GDaD PCF | 실무 | You can:<br>• set up suitable environments with some support<br>• select appropriate test types and techniques with some support<br>• design, build, maintain and execute tests that align to user needs and requirements<br>• conduct exploratory testing<br>• research and try new test types and techniques |
| [Managing, reporting and resolving defects](../../스킬/#managing-reporting-and-resolving-defects) | UK GDaD PCF | 실무 | You can:<br>• collaborate with others to create a defect management process to report, communicate and resolve defects, with support<br>• critically assess dependencies, defects and risks, with support<br>• contribute to mitigation and contingency plans<br>• clearly communicate risks and the impact of defects to stakeholders |
| [Test analysis](../../스킬/#test-analysis) | UK GDaD PCF | 실무 | You can:<br>• work with stakeholders to determine which functional and non-functional quality characteristics add value<br>• determine what to test following an agreed approach<br>• identify and advocate for test needs, such as data, access and environments, with support<br>• analyse information to identify risks |
| [Test and quality planning](../../스킬/#test-and-quality-planning) | UK GDaD PCF | 실무 | You can:<br>• create or adapt quality testing approaches based on risk, with some support<br>• follow a quality testing strategy and contribute to its development<br>• contribute to continuous improvement of quality testing approaches, plans and strategies |
| [Test engineering](../../스킬/#test-engineering) | UK GDaD PCF | 인지 | You can:<br>• explain why testing processes, environments and tools are important<br>• follow test engineering practices and standards, with support<br>• support the maintenance of automated tests and tools required for testing |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자신의 업무가 뒷받침하는 임상 및 돌봄 워크플로를 설명한다<br>• 임상 및 돌봄 동료와 일반적인 의료 용어를 올바르게 사용한다<br>• 변경이 환자 돌봄에 영향을 줄 수 있는 때를 알아보고 제기한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 연계된 돌봄에 상호운용성이 중요한 이유를 설명한다<br>• HL7 FHIR 등 주요 보건 데이터 교환 표준의 이름을 말한다 |

### 일반적인 자격과 경력

- 디지털 서비스의 테스트를 설계하고 실행한 경험, 또는 그에 준하는 것.

### 밴드 개요

- **지식:** 전문적이거나 기술적인 지식. 보통 학위 또는 그에 준하는 경력으로 얻는다.
- **자율성:** 전문직 기준 안에서 폭넓은 목표를 향해 일하며, 자신의 업무를 계획한다.
- **범위:** 팀 또는 프로덕트 안의 자신의 전문 업무.
- **리더십:** 지원 직원이나 어프렌티스를 지도하고 그 업무를 점검할 수 있다.
- **책무:** 자신의 전문 업무의 품질.

### 직무평가(예시)

| # | 요소 | 수준 | 점수 |
| --- | --- | --- | --- |
| 1 | 의사소통 및 관계 형성 기술 | 4 | 32 |
| 2 | 지식, 교육, 경험 | 5 | 120 |
| 3 | 분석 및 판단 기술 | 3 | 27 |
| 4 | 계획 및 조직화 기술 | 2 | 15 |
| 5 | 신체 기술 | 3 | 27 |
| 6 | 환자·이용자 돌봄에 대한 책임 | 1 | 4 |
| 7 | 정책 및 서비스 개발에 대한 책임 | 2 | 12 |
| 8 | 재무 및 물적 자원에 대한 책임 | 1 | 5 |
| 9 | 사람에 대한 책임 | 1 | 5 |
| 10 | 정보 자원에 대한 책임 | 3 | 16 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 3 | 21 |
| 13 | 신체적 부담 | 2 | 7 |
| 14 | 정신적 부담 | 3 | 12 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **327** (밴드 5: 326–395) |

UK GDaD PCF는 이 수준과 시니어 수준 모두에 HEO 또는 SEO를 제안하며 이는 둘 다 밴드 6에 해당한다. 이 레퍼런스는 두 수준이 다른 밴드가 되도록 이 수준을 밴드 5, 시니어 수준을 밴드 6에 둔다.

## 밴드 6: 시니어 품질 보증 테스트 분석가

**UK GDaD PCF 수준: Senior quality assurance test analyst**

> A senior quality assurance test analyst influences and guides others in test analysis, coordinating quality assurance activities in a defined area. They assess the business impact of testing outcomes and use insights to improve quality assurance processes.
> 
> At this role level, you will:
> - use the most appropriate tools and techniques to analyse artefacts such as products, services, processes and change, to identify risks early
> - work with others to support teams in developing approaches, plans and strategy, considering environments, data, tools and resources
> - communicate chosen approaches, tools, techniques and outcomes to stakeholders
> - guide others in quality assurance tools and techniques
> - contribute to, and enable others to follow, quality assurance and testing standards

### 책임

- 테스트 접근법, 환경, 데이터, 도구에 합의하며 프로덕트 또는 영역의 품질 보증을 조율한다.
- 임상의 및 프로덕트 팀과 요구사항, 설계, 변경을 검토하여 임상적, 운영적 리스크를 일찍 식별한다.
- 임상의 및 돌봄 직원과의 사용자 인수 테스트를 계획하고 이끈다.
- 프로덕트 오너와 임상 안전 책임자가 릴리스 결정을 내릴 수 있도록 테스트 결과와 잔여 리스크를 보고한다.
- 다른 테스트 분석가를 이끌고 테스트 및 임상 안전 표준을 따르도록 돕는다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../스킬/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 실천가 | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Designing and executing tests](../../스킬/#designing-and-executing-tests) | UK GDaD PCF | 실천가 | You can:<br>• set up suitable environments<br>• influence and guide the use of appropriate test types and techniques to mitigate risk early<br>• lead others in designing, building, maintaining and executing tests that align to user needs and requirements<br>• contribute to developing and implementing standards for designing and executing tests<br>• improve test types and techniques through a structured process. |
| [Managing, reporting and resolving defects](../../스킬/#managing-reporting-and-resolving-defects) | UK GDaD PCF | 실천가 | You can:<br>• contribute to developing standards for defect management processes<br>• manage and escalate dependencies, defects and risks across teams<br>• contribute to mitigation and contingency plans across teams<br>• use defect patterns and trends to make recommendations on testing and quality approaches, with support<br>• manage stakeholder expectations and communications during defect resolution |
| [Test analysis](../../스킬/#test-analysis) | UK GDaD PCF | 실천가 | You can:<br>• lead work with stakeholders across teams to determine which functional and non-functional quality characteristics add value<br>• determine if an approach needs to change based on effort and risk<br>• ensure test needs are implemented early<br>• use multiple techniques to analyse complex information to identify risks<br>• coach others in test analysis |
| [Test and quality planning](../../스킬/#test-and-quality-planning) | UK GDaD PCF | 실천가 | You can:<br>• work with teams to develop and implement appropriate quality testing approaches, plans and strategies<br>• contribute to organisational quality testing strategies<br>• implement ways to capture data to drive continuous improvement of quality testing approaches, plans and strategies<br>• advocate for full team ownership of quality testing activities, encouraging early engagement |
| [Test engineering](../../스킬/#test-engineering) | UK GDaD PCF | 인지 | You can:<br>• explain why testing processes, environments and tools are important<br>• follow test engineering practices and standards, with support<br>• support the maintenance of automated tests and tools required for testing |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자신의 업무가 뒷받침하는 임상 및 돌봄 워크플로를 설명한다<br>• 임상 및 돌봄 동료와 일반적인 의료 용어를 올바르게 사용한다<br>• 변경이 환자 돌봄에 영향을 줄 수 있는 때를 알아보고 제기한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• FHIR 리소스, 프로파일, API를 읽고 사용한다<br>• 지도를 받아 간단한 연동을 구축하거나 테스트한다<br>• 메시지를 사양에 비추어 확인한다 |
| [Business and user acceptance testing](../../스킬/#business-and-user-acceptance-testing) | UK GDaD PCF | 실천가 | You can:<br>• advise others how to ensure appropriate test coverage, data and scenarios, in line with acceptance criteria<br>• analyse business risk and impacts of defects so that appropriate action can be taken to enable business acceptance<br>• provide assurance on the suitability, business readiness and viability of delivered solutions |

### 일반적인 자격과 경력

- 복잡하거나 규제 대상인 환경을 포함한 테스트 분석에 관한 상당한 경력, 또는 그에 준하는 것.

### 밴드 개요

- **지식:** 여러 절차에 걸친 전문 지식. 추가 교육과 경험으로 쌓는다.
- **자율성:** 자율적으로 일하고, 자기 분야의 방침을 해석하며, 복잡한 문제에서는 조언을 구한다.
- **범위:** 프로덕트, 서비스, 또는 워크스트림.
- **리더십:** 작은 팀을 이끌거나 동료를 멘토링할 수 있다.
- **책무:** 자신의 워크스트림의 성과와 제공한 조언의 질.

### 직무평가(예시)

| # | 요소 | 수준 | 점수 |
| --- | --- | --- | --- |
| 1 | 의사소통 및 관계 형성 기술 | 4 | 32 |
| 2 | 지식, 교육, 경험 | 6 | 156 |
| 3 | 분석 및 판단 기술 | 4 | 42 |
| 4 | 계획 및 조직화 기술 | 3 | 27 |
| 5 | 신체 기술 | 3 | 27 |
| 6 | 환자·이용자 돌봄에 대한 책임 | 1 | 4 |
| 7 | 정책 및 서비스 개발에 대한 책임 | 2 | 12 |
| 8 | 재무 및 물적 자원에 대한 책임 | 1 | 5 |
| 9 | 사람에 대한 책임 | 2 | 12 |
| 10 | 정보 자원에 대한 책임 | 3 | 16 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 4 | 32 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 3 | 12 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **404** (밴드 6: 396–465) |

## 밴드 8a: 리드 품질 보증 테스트 분석가

**UK GDaD PCF 수준: Lead quality assurance test analyst**

> A lead quality assurance test analyst sets the strategy for test analysis and influences test analysis practices across a broad area. They develop, monitor and evaluate test analysis standards and methods, and make strategic decisions that improve test analysis in the organisation.
> 
> At this role level, you will:
> - lead on setting standards and good practices across the test analysis community
> - lead and guide teams across the organisation in test analysis
> - define and implement test strategies
> - mentor and coach other quality assurance test analysts
> - negotiate and escalate major risks, issues and defects

### 책임

- 임상 시스템의 리스크 기반 테스트를 포함하여 조직 전체의 테스트 분석 기준과 우수 사례를 정한다.
- 전자 환자 기록 변경이나 새로운 환자용 서비스 등 주요 프로그램의 테스트 전략을 정의한다.
- 테스트가 임상 안전 케이스와 해당하는 경우 의료기기 기술 문서에 필요한 근거를 만들도록 한다.
- 프로덕트, 임상, 공급자의 시니어 리드와 중대한 리스크, 이슈, 결함을 협상하고 상위 보고한다.
- 테스트 분석가를 멘토링하고 코칭하며 테스트 분석 커뮤니티를 이끈다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../스킬/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 전문가 | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Designing and executing tests](../../스킬/#designing-and-executing-tests) | UK GDaD PCF | 전문가 | You can:<br>• set standards and influence organisational decisions for test types, techniques, design and execution<br>• coach others in test types, techniques, design and execution<br>• advocate for continuous improvement and refinement of test types and techniques<br>• make strategic decisions on new or improved test types and techniques used in your area |
| [Managing, reporting and resolving defects](../../스킬/#managing-reporting-and-resolving-defects) | UK GDaD PCF | 전문가 | You can:<br>• lead and coach others in improving test and defect management processes<br>• support others in assessing complex and challenging defects across the organisation<br>• lead and coach others in using defect patterns and trends to make tactical and strategic recommendations<br>• influence improvements to quality processes, informed by defect patterns and trends |
| [Test analysis](../../스킬/#test-analysis) | UK GDaD PCF | 전문가 | You can:<br>• lead and guide multiple teams in test analysis, ensuring it is implemented early in the life cycle<br>• advocate for risk-based analysis to drive improvements across many teams<br>• set standards and principles for test analysis across the organisation |
| [Test and quality planning](../../스킬/#test-and-quality-planning) | UK GDaD PCF | 전문가 | You can:<br>• create and manage multiple quality testing plans, approaches and strategies<br>• lead and guide multiple teams in adopting quality testing strategy<br>• advocate for early quality testing involvement in organisational delivery processes<br>• guide teams across an organisation in optimising quality testing approaches, plans and strategies by using appropriate data |
| [Test engineering](../../스킬/#test-engineering) | UK GDaD PCF | 인지 | You can:<br>• explain why testing processes, environments and tools are important<br>• follow test engineering practices and standards, with support<br>• support the maintenance of automated tests and tools required for testing |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 서비스가 조직 간 돌봄 경로에 어떻게 들어맞는지 분석한다<br>• 임상의, 돌봄 직원, 환자와 협력하여 디지털 서비스를 형성한다<br>• 디지털 결정이 돌봄, 안전, 직원 업무량에 미치는 영향을 설명한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 프로덕트나 변경의 위험 요소 식별과 리스크 평가를 이끈다<br>• 위험 요소 로그와 임상 안전 케이스 보고서를 작성하고 유지한다<br>• 프로덕트 팀과 리스크 통제에 합의하고 그것이 작동하는지 확인한다<br>• 임상 리스크 관리 기준의 적용에 대해 팀에 조언한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• FHIR 리소스, 프로파일, API를 읽고 사용한다<br>• 지도를 받아 간단한 연동을 구축하거나 테스트한다<br>• 메시지를 사양에 비추어 확인한다 |
| [의료기기 소프트웨어 규제](../../스킬/#의료기기-소프트웨어-규제) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 의료기기 표준을 충족하는 소프트웨어 생애 주기 프로세스를 따른다<br>• 그 프로세스가 요구하는 기록을 작성한다 |
| [피플 매니지먼트](../../스킬/#피플-매니지먼트) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 일상 업무를 감독하고 피드백을 준다<br>• 채용과 입사 교육에 참여한다<br>• 정기적으로 1대1 면담을 한다 |

### 일반적인 자격과 경력

- 복잡한 서비스의 테스트 분석을 이끈 풍부한 경력.

### 밴드 개요

- **지식:** 한 분야와 그 관리에 대한 전문 지식.
- **자율성:** 서비스를 위해 조직의 방침을 해석하고 팀의 방향을 정한다.
- **범위:** 서비스 영역, 또는 조직 전체에 걸친 분야.
- **리더십:** 팀을 관리하거나, 직접 보고 관계 없이 한 분야를 이끈다.
- **책무:** 서비스 영역, 그 직원, 그리고 예산.

### 직무평가(예시)

| # | 요소 | 수준 | 점수 |
| --- | --- | --- | --- |
| 1 | 의사소통 및 관계 형성 기술 | 5 | 45 |
| 2 | 지식, 교육, 경험 | 7 | 196 |
| 3 | 분석 및 판단 기술 | 5 | 60 |
| 4 | 계획 및 조직화 기술 | 4 | 42 |
| 5 | 신체 기술 | 2 | 15 |
| 6 | 환자·이용자 돌봄에 대한 책임 | 1 | 4 |
| 7 | 정책 및 서비스 개발에 대한 책임 | 4 | 32 |
| 8 | 재무 및 물적 자원에 대한 책임 | 1 | 5 |
| 9 | 사람에 대한 책임 | 3 | 21 |
| 10 | 정보 자원에 대한 책임 | 4 | 24 |
| 11 | 연구 및 개발에 대한 책임 | 3 | 21 |
| 12 | 행동의 자유 | 5 | 45 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **543** (밴드 8a: 540–584) |

UK GDaD PCF는 이 수준에 밴드 8b에 해당하는 G7 또는 G6을 제안한다. 이 레퍼런스는 모든 테스트가 아니라 하나의 테스트 분야를 이끌므로, 리드 테스트 엔지니어와 같은 밴드 8a에 둔다. 테스트 책임자는 밴드 8c이다.


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
