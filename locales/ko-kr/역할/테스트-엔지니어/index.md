# 테스트 엔지니어

> 이 문서는 일반적인 디지털 헬스케어 조직을 위한 예시용 참조 프로필입니다. 특정 고용주의 공식 직무기술서가 아니며, 직무평가 점수도 공식 평가가 아닙니다.

> 이 글은 AI 어시스턴트가 영어를 한국어로 번역한 것이며, 한국어 원어민의 검토는 아직 받지 않았습니다. 영국 정부 디지털·데이터 전문직 역량 프레임워크(UK GDaD PCF)와 ESCO의 인용문은 영어 그대로 두었습니다.

**직군:** [품질 보증과 테스트](../../#품질-보증과-테스트)  
**밴드:** 4, 6, 7, 8a  
**UK GDaD PCF 역할:** [Test engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/test-engineer/)  
**ESCO 직업:** [software tester](http://data.europa.eu/esco/occupation/106f79e4-6264-45f1-9e7a-297435cd684b) (ISCO-08 2519)

## 개요

테스트 엔지니어는 팀이 조직의 디지털 헬스 서비스를 빠르고 자주 테스트할 수 있게 하는 자동화 테스트, 도구, 프레임워크를 구축한다. 기능, 연동, 성능, 보안, 복원력을 테스트하는 코드를 작성하고 전달 파이프라인에 테스트를 내장하여, 임상 시스템과 환자용 시스템의 변경을 안전하게 릴리스할 수 있도록 한다.

## 디지털 헬스케어 조직에서

- 임상 시스템은 안전이 중요하므로, 자동화 회귀 테스트는 위험 요소 로그에 기록된 안전 통제를 지키며 안전 케이스의 근거로 보관된다.
- 다른 보건·돌봄 시스템과의 연동에는 HL7 FHIR와 HL7 버전 2 같은 표준에 비추어 하는 자동화 테스트가 필요하며, 파트너 시스템을 모사해서 하는 경우가 많다.
- 임상 서비스는 종일 운영되고 예측 가능한 시간대에 피크를 맞이하므로, 성능 및 복원력 테스트는 실제 임상 수요를 모델링한다.
- 테스트 환경에는 실제 환자 데이터를 두어서는 안 되므로, 엔지니어는 드문 사례와 예외 상황의 임상 사례를 포함한 현실적인 합성 데이터를 생성한다.
- 의료기기로 규제되는 소프트웨어에는 IEC 62304 같은 표준에 따른, 생애 주기의 일부로서 추적 가능하고 재현 가능한 테스트가 필요하다.

## UK GDaD PCF 역할 설명(원문은 영어)

> A test engineer designs, builds, automates and executes comprehensive, robust and maintainable test suites. They apply test engineering standards, perform exploratory testing and use diverse techniques to identify risks and improve testing efficiency and quality.
> 
> In this role you will:
> - maintain automated tests in continuous integration, continuous delivery (CI/CD) pipelines
> - use, develop and standardise reusable frameworks and tools following engineering practices and standards
> - analyse and test artefacts such as products, services and business processes
> - promote quality considerations throughout the development life cycle
> - support the resolution of technical issues

## 역할 수준

| 밴드 | 직함 | UK GDaD PCF 수준 | 영국 공무원 등급 | 직무평가 점수 |
| --- | --- | --- | --- | --- |
| 4 | [어소시에이트 테스트 엔지니어](#밴드-4-어소시에이트-테스트-엔지니어) | Associate test engineer | EO | 275 |
| 6 | [테스트 엔지니어](#밴드-6-테스트-엔지니어) | Test engineer | HEO/SEO | 411 |
| 7 | [시니어 테스트 엔지니어](#밴드-7-시니어-테스트-엔지니어) | Senior test engineer | SEO/G7 | 477 |
| 8a | [리드 테스트 엔지니어](#밴드-8a-리드-테스트-엔지니어) | Lead test engineer | SEO/G7/G6 | 553 |

## 밴드 4: 어소시에이트 테스트 엔지니어

**UK GDaD PCF 수준: Associate test engineer**

> An associate test engineer works closely with other test professionals to learn test engineering activities and techniques.
> 
> At this role level, you will:
> - contribute to and maintain technical test suites under supervision
> - follow engineering practices and standards to apply test approaches, plans and strategies under supervision
> - analyse artefacts such as user stories, prototypes, processes and designs with support
> - support the development of reports, recording of outcomes and resolution of defects
> - understand the technical tooling and engineering approach to design and execute tests

### 책임

- 감독을 받으며 팀의 엔지니어링 기준에 따라 간단한 자동화 테스트를 작성하고 유지한다.
- 자동화 및 수동 테스트를 실행하고 결과를 정확하게 기록한다.
- 임상 시스템과의 연동을 포함하여 결함의 조사와 보고를 돕는다.
- 합성 테스트 데이터를 사용하고 테스트 환경에서 정보 거버넌스 규칙을 따른다.
- 팀의 테스트 도구, 코딩 관행, 임상 안전 프로세스를 배운다.

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

- 코딩이나 테스트의 일정한 경력, 또는 관련 어프렌티스십에 등록, 또는 그에 준하는 것.

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

## 밴드 6: 테스트 엔지니어

**UK GDaD PCF 수준: Test engineer**

> A test engineer develops solutions to enable more efficient testing. They follow engineering standards to design and execute appropriate technical tests.
> 
> At this role level, you will:
> - determine test scope and estimate the effort required
> - select and use the most appropriate test approaches and techniques to mitigate risk
> - use technical tooling and engineering approaches to design and execute tests
> - develop and maintain technical test suites
> - develop reports, record outcomes and support the resolution of defects
> - contribute to and follow engineering practices and standards

### 책임

- 임상용 및 환자용 서비스의 자동화된 기능, 연동, API 테스트를 설계하고 구축한다.
- HL7 FHIR 프로파일과 그 밖의 상호운용성 사양에 비추어 메시지를 점검하는 테스트를 구축한다.
- 현실적인 사례와 예외 상황의 임상 사례를 아우르는 합성 환자 데이터를 생성한다.
- 안전 관련 점검이 모든 변경에서 실행되도록 전달 파이프라인에 테스트를 추가한다.
- 테스트 공수를 추정하고 결과를 보고하며 결함 해결을 지원한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../스킬/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 실무 | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Designing and executing tests](../../스킬/#designing-and-executing-tests) | UK GDaD PCF | 실무 | You can:<br>• set up suitable environments with some support<br>• select appropriate test types and techniques with some support<br>• design, build, maintain and execute tests that align to user needs and requirements<br>• conduct exploratory testing<br>• research and try new test types and techniques |
| [Managing, reporting and resolving defects](../../스킬/#managing-reporting-and-resolving-defects) | UK GDaD PCF | 실무 | You can:<br>• collaborate with others to create a defect management process to report, communicate and resolve defects, with support<br>• critically assess dependencies, defects and risks, with support<br>• contribute to mitigation and contingency plans<br>• clearly communicate risks and the impact of defects to stakeholders |
| [Test analysis](../../스킬/#test-analysis) | UK GDaD PCF | 실무 | You can:<br>• work with stakeholders to determine which functional and non-functional quality characteristics add value<br>• determine what to test following an agreed approach<br>• identify and advocate for test needs, such as data, access and environments, with support<br>• analyse information to identify risks |
| [Test and quality planning](../../스킬/#test-and-quality-planning) | UK GDaD PCF | 실무 | You can:<br>• create or adapt quality testing approaches based on risk, with some support<br>• follow a quality testing strategy and contribute to its development<br>• contribute to continuous improvement of quality testing approaches, plans and strategies |
| [Test engineering](../../스킬/#test-engineering) | UK GDaD PCF | 실무 | You can:<br>• use test engineering frameworks and tools to support testing activities<br>• follow test engineering practices and standards, such as source control and continuous integration, continuous delivery (CI/CD) pipelines<br>• integrate and execute tests to ensure early testing and continuous feedback<br>• create and maintain automated tests, with some support<br>• write and review coded solutions, with some support |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자신의 업무가 뒷받침하는 임상 및 돌봄 워크플로를 설명한다<br>• 임상 및 돌봄 동료와 일반적인 의료 용어를 올바르게 사용한다<br>• 변경이 환자 돌봄에 영향을 줄 수 있는 때를 알아보고 제기한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• FHIR 리소스, 프로파일, API를 읽고 사용한다<br>• 지도를 받아 간단한 연동을 구축하거나 테스트한다<br>• 메시지를 사양에 비추어 확인한다 |

### 일반적인 자격과 경력

- 컴퓨팅 또는 관련 분야 학위, 또는 그에 준하는 경력.
- 자동화 테스트를 구축한 경험.

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
| 9 | 사람에 대한 책임 | 1 | 5 |
| 10 | 정보 자원에 대한 책임 | 4 | 24 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 4 | 32 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **411** (밴드 6: 396–465) |

## 밴드 7: 시니어 테스트 엔지니어

**UK GDaD PCF 수준: Senior test engineer**

> A senior test engineer is responsible for test engineering in their area. They influence, coach and guide others in test engineering, sharing best practice and standards.
> 
> At this role level, you will:
> - select, use and guide others in using the most appropriate technical tooling, engineering approaches, test types and techniques to identify and address risks early
> - extend, standardise and build reusable frameworks and tools that support testing
> - communicate and document chosen approaches, tools, techniques and outcomes to the team and appropriate stakeholders
> - contribute to and agree engineering standards

### 책임

- 영역의 테스트 엔지니어링을 이끌며 그 리스크를 일찍 다루는 도구, 프레임워크, 테스트 유형을 고른다.
- 임상 시스템과 파트너 연동을 위한 재사용 가능한 테스트 프레임워크와 시뮬레이터를 구축한다.
- 실제 임상 수요를 바탕으로 성능, 부하, 복원력 테스트를 계획하고 실행한다.
- 자동화 테스트가 위험 요소와 안전 통제에 추적 가능하게 하고 안전 케이스의 근거를 만들도록 한다.
- 다른 테스트 엔지니어를 코칭하고 이끌며 개발자와 엔지니어링 기준에 합의한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../스킬/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 실천가 | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Designing and executing tests](../../스킬/#designing-and-executing-tests) | UK GDaD PCF | 실천가 | You can:<br>• set up suitable environments<br>• influence and guide the use of appropriate test types and techniques to mitigate risk early<br>• lead others in designing, building, maintaining and executing tests that align to user needs and requirements<br>• contribute to developing and implementing standards for designing and executing tests<br>• improve test types and techniques through a structured process. |
| [Managing, reporting and resolving defects](../../스킬/#managing-reporting-and-resolving-defects) | UK GDaD PCF | 실천가 | You can:<br>• contribute to developing standards for defect management processes<br>• manage and escalate dependencies, defects and risks across teams<br>• contribute to mitigation and contingency plans across teams<br>• use defect patterns and trends to make recommendations on testing and quality approaches, with support<br>• manage stakeholder expectations and communications during defect resolution |
| [Test analysis](../../스킬/#test-analysis) | UK GDaD PCF | 실천가 | You can:<br>• lead work with stakeholders across teams to determine which functional and non-functional quality characteristics add value<br>• determine if an approach needs to change based on effort and risk<br>• ensure test needs are implemented early<br>• use multiple techniques to analyse complex information to identify risks<br>• coach others in test analysis |
| [Test and quality planning](../../스킬/#test-and-quality-planning) | UK GDaD PCF | 실천가 | You can:<br>• work with teams to develop and implement appropriate quality testing approaches, plans and strategies<br>• contribute to organisational quality testing strategies<br>• implement ways to capture data to drive continuous improvement of quality testing approaches, plans and strategies<br>• advocate for full team ownership of quality testing activities, encouraging early engagement |
| [Test engineering](../../스킬/#test-engineering) | UK GDaD PCF | 실천가 | You can:<br>• develop, standardise and extend reusable frameworks and tools to support a range of testing activities<br>• guide and coach others in creating and maintaining comprehensive and reliable tests that meet standards<br>• research and prepare for future testing needs, including tools, methodologies and techniques<br>• maintain and adapt continuous integration, continuous delivery (CI/CD) pipelines |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자신의 업무가 뒷받침하는 임상 및 돌봄 워크플로를 설명한다<br>• 임상 및 돌봄 동료와 일반적인 의료 용어를 올바르게 사용한다<br>• 변경이 환자 돌봄에 영향을 줄 수 있는 때를 알아보고 제기한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• FHIR, HL7 버전 2, 메시징 패턴을 사용해 연동을 설계하고 구축한다<br>• FHIR 리소스와 구현 가이드를 작성하고 프로파일링한다<br>• 시스템 간의 복잡한 매핑과 데이터 품질 문제를 해결한다 |
| [의료기기 소프트웨어 규제](../../스킬/#의료기기-소프트웨어-규제) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 일부 보건 소프트웨어는 의료기기로 규제됨을 설명한다<br>• 제품이 의료기기일 수 있을 때 누구에게 물어야 하는지 안다 |

### 일반적인 자격과 경력

- 테스트 엔지니어링에 관한 상당한 경력(석사에 준하는 수준).

### 밴드 개요

- **지식:** 고도로 발달한 전문 지식. 보통 석사에 준하거나 그에 준하는 경력으로 얻는다.
- **자율성:** 조직의 방침에 맞춰 일하고, 성과를 내는 방법을 정하며, 다른 사람이 상담하는 전문가이다.
- **범위:** 여러 프로덕트나 서비스, 또는 전문 기능.
- **리더십:** 팀 또는 전문 실무 영역을 이끈다.
- **책무:** 서비스 또는 전문 기능의 제공, 그리고 예산이 있다면 그 예산.

### 직무평가(예시)

| # | 요소 | 수준 | 점수 |
| --- | --- | --- | --- |
| 1 | 의사소통 및 관계 형성 기술 | 4 | 32 |
| 2 | 지식, 교육, 경험 | 7 | 196 |
| 3 | 분석 및 판단 기술 | 4 | 42 |
| 4 | 계획 및 조직화 기술 | 3 | 27 |
| 5 | 신체 기술 | 3 | 27 |
| 6 | 환자·이용자 돌봄에 대한 책임 | 1 | 4 |
| 7 | 정책 및 서비스 개발에 대한 책임 | 3 | 21 |
| 8 | 재무 및 물적 자원에 대한 책임 | 1 | 5 |
| 9 | 사람에 대한 책임 | 2 | 12 |
| 10 | 정보 자원에 대한 책임 | 5 | 34 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 4 | 32 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **477** (밴드 7: 466–539) |

## 밴드 8a: 리드 테스트 엔지니어

**UK GDaD PCF 수준: Lead test engineer**

> A lead test engineer sets the strategy for test engineering and influences test engineering practices across a broad area. They develop, monitor and evaluate quality engineering standards, and make strategic improvements to quality engineering in the organisation.
> 
> At this role level, you will:
> - lead a broad area in technical tooling, engineering approaches and test types and techniques to address risks early
> - define engineering standards, enabling others to follow them
> - lead and guide teams in quality engineering strategies and practices
> - lead and guide test engineers
> - escalate risks to senior stakeholders
> - lead and implement continuous testing, identifying opportunities to test earlier

### 책임

- 전달 파이프라인의 지속적 테스트를 포함하여 폭넓은 영역의 테스트 엔지니어링 전략과 기준을 정한다.
- 테스트 엔지니어와 팀을 이끌고 품질 엔지니어링 실천을 이끈다.
- 규제 대상이거나 안전이 중요한 소프트웨어의 테스트가 요구되는 표준을 충족하고 추적 가능하도록 한다.
- 품질과 안전 리스크를 프로덕트, 임상, 공급자의 시니어 리드에게 상위 보고한다.
- 더 일찍, 더 자주 테스트할 기회를 찾고 그것이 품질에 미치는 영향을 측정한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../스킬/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 전문가 | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Designing and executing tests](../../스킬/#designing-and-executing-tests) | UK GDaD PCF | 전문가 | You can:<br>• set standards and influence organisational decisions for test types, techniques, design and execution<br>• coach others in test types, techniques, design and execution<br>• advocate for continuous improvement and refinement of test types and techniques<br>• make strategic decisions on new or improved test types and techniques used in your area |
| [Managing, reporting and resolving defects](../../스킬/#managing-reporting-and-resolving-defects) | UK GDaD PCF | 전문가 | You can:<br>• lead and coach others in improving test and defect management processes<br>• support others in assessing complex and challenging defects across the organisation<br>• lead and coach others in using defect patterns and trends to make tactical and strategic recommendations<br>• influence improvements to quality processes, informed by defect patterns and trends |
| [Test analysis](../../스킬/#test-analysis) | UK GDaD PCF | 전문가 | You can:<br>• lead and guide multiple teams in test analysis, ensuring it is implemented early in the life cycle<br>• advocate for risk-based analysis to drive improvements across many teams<br>• set standards and principles for test analysis across the organisation |
| [Test and quality planning](../../스킬/#test-and-quality-planning) | UK GDaD PCF | 전문가 | You can:<br>• create and manage multiple quality testing plans, approaches and strategies<br>• lead and guide multiple teams in adopting quality testing strategy<br>• advocate for early quality testing involvement in organisational delivery processes<br>• guide teams across an organisation in optimising quality testing approaches, plans and strategies by using appropriate data |
| [Test engineering](../../스킬/#test-engineering) | UK GDaD PCF | 전문가 | You can:<br>• establish and lead test engineering practices, standards and behaviours<br>• influence and guide test engineering technology and tool choices across the organisation<br>• advocate for the adoption and use of appropriate testing solutions, ensuring alignment with organisational goals and quality objectives |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 서비스가 조직 간 돌봄 경로에 어떻게 들어맞는지 분석한다<br>• 임상의, 돌봄 직원, 환자와 협력하여 디지털 서비스를 형성한다<br>• 디지털 결정이 돌봄, 안전, 직원 업무량에 미치는 영향을 설명한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 프로덕트나 변경의 위험 요소 식별과 리스크 평가를 이끈다<br>• 위험 요소 로그와 임상 안전 케이스 보고서를 작성하고 유지한다<br>• 프로덕트 팀과 리스크 통제에 합의하고 그것이 작동하는지 확인한다<br>• 임상 리스크 관리 기준의 적용에 대해 팀에 조언한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• FHIR, HL7 버전 2, 메시징 패턴을 사용해 연동을 설계하고 구축한다<br>• FHIR 리소스와 구현 가이드를 작성하고 프로파일링한다<br>• 시스템 간의 복잡한 매핑과 데이터 품질 문제를 해결한다 |
| [의료기기 소프트웨어 규제](../../스킬/#의료기기-소프트웨어-규제) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 의료기기 표준을 충족하는 소프트웨어 생애 주기 프로세스를 따른다<br>• 그 프로세스가 요구하는 기록을 작성한다 |
| [피플 매니지먼트](../../스킬/#피플-매니지먼트) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 일상 업무를 감독하고 피드백을 준다<br>• 채용과 입사 교육에 참여한다<br>• 정기적으로 1대1 면담을 한다 |

### 일반적인 자격과 경력

- 복잡한 서비스의 테스트 엔지니어링을 이끈 풍부한 경력.

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
| 10 | 정보 자원에 대한 책임 | 5 | 34 |
| 11 | 연구 및 개발에 대한 책임 | 3 | 21 |
| 12 | 행동의 자유 | 5 | 45 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **553** (밴드 8a: 540–584) |

UK GDaD PCF는 이 수준에 시니어 테스트 엔지니어와 같은 밴드 7에 해당하는 SEO에서 G6을 제안한다. 이 레퍼런스는 폭넓은 영역의 테스트 엔지니어링 전략과 기준을 정하므로 밴드 8a에 둔다.


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
