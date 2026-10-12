# 데이터 엔지니어

> 이 문서는 일반적인 디지털 헬스케어 조직을 위한 예시용 참조 프로필입니다. 특정 고용주의 공식 직무기술서가 아니며, 직무평가 점수도 공식 평가가 아닙니다.

> 이 글은 AI 어시스턴트가 영어를 한국어로 번역한 것이며, 한국어 원어민의 검토는 아직 받지 않았습니다. 영국 정부 디지털·데이터 전문직 역량 프레임워크(UK GDaD PCF)와 ESCO의 인용문은 영어 그대로 두었습니다.

**직군:** [데이터](../../#데이터)  
**밴드:** 6, 7, 8a, 8b  
**UK GDaD PCF 역할:** [Data engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/data-engineer/)  
**ESCO 직업:** [data engineer](http://data.europa.eu/esco/occupation/2079755f-d809-49e6-8037-4de6180e54c0) (ISCO-08 2511)

## 개요

데이터 엔지니어는 보건·돌봄 데이터를 임상·운영 시스템에서 분석하고 안전하게 쓸 수 있는 곳으로 옮기는 파이프라인과 플랫폼을 구축하고 운영한다. 데이터 흐름을 설계하고, 서로 다른 표준을 쓰는 소스를 통합하며, 데이터가 정확하고, 적시에 제공되고, 안전하며, 봐야 할 사람에게만 제공되도록 한다.

## 디지털 헬스케어 조직에서

- 소스 시스템에는 전자 환자 기록, 검사, 영상, 약제 시스템이 있고 HL7 버전 2, HL7 FHIR, SNOMED CT, ICD 같은 표준을 쓴다.
- 파이프라인은 식별 가능한 환자 데이터를 전달하는 경우가 많으므로, 엔지니어는 처음부터 가명처리, 접근 제어, 감사를 구축한다.
- 일부 데이터 피드는 경보나 환자 목록 등 직접 돌봄을 뒷받침하므로, 실패하거나 지연된 파이프라인은 환자에게 영향을 줄 수 있고 임상 안전 평가가 필요하다.
- 데이터는 돌봄 현장을 가로질러 연결해야 하는 경우가 많고, 이는 신뢰할 수 있는 환자 매칭과 일관된 식별자에 의존한다.

## UK GDaD PCF 역할 설명(원문은 영어)

> A data engineer develops and constructs data products and services, and integrates them into systems and business processes.

## 역할 수준

| 밴드 | 직함 | UK GDaD PCF 수준 | 영국 공무원 등급 | 직무평가 점수 |
| --- | --- | --- | --- | --- |
| 6 | [데이터 엔지니어](#밴드-6-데이터-엔지니어) | Data engineer | HEO/SEO | 421 |
| 7 | [시니어 데이터 엔지니어](#밴드-7-시니어-데이터-엔지니어) | Senior data engineer | SEO/G7 | 477 |
| 8a | [리드 데이터 엔지니어](#밴드-8a-리드-데이터-엔지니어) | Lead data engineer | G7 | 551 |
| 8b | [데이터 엔지니어링 책임자](#밴드-8b-데이터-엔지니어링-책임자) | Head of data engineering | G7/G6 | 589 |

## 밴드 6: 데이터 엔지니어

**UK GDaD PCF 수준: Data engineer**

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

### 책임

- 합의된 설계에 따라 임상·운영 시스템에서 데이터 플랫폼으로 가는 데이터 파이프라인을 구축하고 유지한다.
- 코드화된 임상 데이터를 포함하여 소스 데이터를 목표 모델에 매핑하고 그 매핑을 문서화한다.
- 가명처리, 검증, 데이터 품질 점검을 파이프라인에 내장한다.
- 직접 돌봄을 뒷받침하는 피드를 우선하여 파이프라인을 모니터링하고 장애를 수정한다.
- 정보 거버넌스 규칙을 충족하는 접근 제어와 감사 로그를 적용한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../스킬/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 인지 | You can:<br>• explain why it's important to communicate technical concepts in non-technical language<br>• explain the types of communication that can be used with internal and external stakeholders, and their impact |
| [Data analysis and synthesis](../../스킬/#data-analysis-and-synthesis) | UK GDaD PCF | 실무 | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data compliance and security](../../스킬/#data-compliance-and-security) | UK GDaD PCF | 실무 | You can:<br>• use official data classification when authoring documents<br>• apply internal procedures, policies and technologies to ensure secure data handling<br>• identify and address ethical considerations when working with data<br>• address data compliance issues using internal processes |
| [Data development process](../../스킬/#data-development-process) | UK GDaD PCF | 실무 | You can:<br>• implement simple data solutions such as data pipelines, following established approaches and standards<br>• create repeatable, reliable and reusable data solutions |
| [Data innovation](../../스킬/#data-innovation) | UK GDaD PCF | 인지 | You can:<br>• develop a basic understanding of an unfamiliar or emerging technology, or a familiar technology in a new data context, with guidance<br>• share what you learn with colleagues, including how it could help deliver more value from data |
| [Data integration design](../../스킬/#data-integration-design) | UK GDaD PCF | 실무 | You can:<br>• design simple data exchange or integration solutions using established patterns or modelling techniques<br>• include security features in your data integration designs |
| [Data modelling](../../스킬/#data-modelling) | UK GDaD PCF | 실무 | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Metadata management](../../스킬/#metadata-management) | UK GDaD PCF | 실무 | You can:<br>• use metadata repositories to complete complex tasks such as data and systems integration impact analysis<br>• maintain a metadata repository to ensure information remains accurate and up to date |
| [Problem management](../../스킬/#problem-management) | UK GDaD PCF | 인지 | You can:<br>• investigate problems in systems, processes and services, with an understanding of the level of a problem, for example, strategic, tactical or operational<br>• contribute to the implementation of remedies and preventative measures |
| [Programming and build (data and analytics engineering)](../../스킬/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | 실무 | You can:<br>• design, code, test and deploy programs or scripts following standards and good practice<br>• write readable, maintainable code<br>• use automation to improve the software development life cycle<br>• consider and adopt appropriate security measures in your solutions |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자신의 업무가 뒷받침하는 임상 및 돌봄 워크플로를 설명한다<br>• 임상 및 돌봄 동료와 일반적인 의료 용어를 올바르게 사용한다<br>• 변경이 환자 돌봄에 영향을 줄 수 있는 때를 알아보고 제기한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• FHIR 리소스, 프로파일, API를 읽고 사용한다<br>• 지도를 받아 간단한 연동을 구축하거나 테스트한다<br>• 메시지를 사양에 비추어 확인한다 |
| [임상 용어와 분류](../../스킬/#임상-용어와-분류) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 임상 용어 체계와 분류의 차이를 설명한다<br>• SNOMED CT와 ICD 같은 일반적인 용어 체계를 알아본다 |
| [가명처리와 공개 통제](../../스킬/#가명처리와-공개-통제) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 가명처리된 데이터로 작업하고, 결과물을 공개하기 전에 공개 점검을 적용한다<br>• 연결되었거나 상세한 데이터로 환자를 식별할 수 있는 경우를 알아본다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 잘못되었거나, 빠졌거나, 지연된 정보 등을 통해 보건 IT 시스템이 환자에게 어떻게 해를 끼칠 수 있는지 설명한다<br>• 임상 안전 문제 가능성을 올바른 경로로 보고한다 |

### 일반적인 자격과 경력

- 컴퓨팅 또는 관련 분야 학위, 또는 그에 준하는 경력.
- 데이터 파이프라인을 구축한 경험.

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
| 10 | 정보 자원에 대한 책임 | 5 | 34 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 4 | 32 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **421** (밴드 6: 396–465) |

## 밴드 7: 시니어 데이터 엔지니어

**UK GDaD PCF 수준: Senior data engineer**

> A senior data engineer designs and leads the implementation of data flows to connect operational systems, data for analytics and business intelligence (BI) systems.
> 
> At this role level, you will:
> - recognise opportunities to reuse existing data flows
> - lead the build of data streaming systems
> - optimise the code to ensure processes perform optimally
> - lead work on database management

### 책임

- 많은 보건·돌봄 시스템의 데이터를 집계하는 데이터 흐름과 스트리밍 서비스를 설계한다.
- 환자 매칭과 연결 프로세스를 설계하고 그것이 얼마나 잘 작동하는지 측정한다.
- 서비스가 필요할 때 데이터를 쓸 수 있도록 데이터베이스와 플랫폼의 성능 개선을 이끈다.
- 관련 전문가와 함께 데이터 흐름의 임상 안전 및 정보 거버넌스 리스크를 평가한다.
- 다른 엔지니어의 업무를 검토하고 코칭한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../스킬/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 실무 | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Data analysis and synthesis](../../스킬/#data-analysis-and-synthesis) | UK GDaD PCF | 실무 | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data compliance and security](../../스킬/#data-compliance-and-security) | UK GDaD PCF | 실천가 | You can:<br>• consistently apply data ethics, legislation, internal procedures, policies and technologies to ensure secure data handling<br>• help ensure your team remain compliant by identifying and addressing current and potential data compliance and ethical issues<br>• guide and support others in addressing data compliance issues |
| [Data development process](../../스킬/#data-development-process) | UK GDaD PCF | 실천가 | You can:<br>• lead the implementation of complex or large-scale data solutions<br>• apply appropriate technology and techniques to ensure data solutions are secure and scalable<br>• identify and implement continuous improvement to the operation and performance of data solutions |
| [Data innovation](../../스킬/#data-innovation) | UK GDaD PCF | 실무 | You can:<br>• experiment with unfamiliar and emerging technologies, or familiar technologies in new data contexts, with guidance<br>• share what you learn with the team, explaining potential benefits, risks, and practical considerations<br>• identify opportunities to apply technology to improve data processes or outcomes in an operational setting or the wider organisation |
| [Data integration design](../../스킬/#data-integration-design) | UK GDaD PCF | 실천가 | You can:<br>• select the most appropriate techniques for different integration scenarios<br>• evaluate and lead the implementation of integration using varied approaches that ensure security, efficiency and compliance |
| [Data modelling](../../스킬/#data-modelling) | UK GDaD PCF | 실천가 | You can:<br>• produce relevant data models across multiple subject areas<br>• explain which models to use for which purpose<br>• understand industry-recognised data modelling patterns and standards, and when to apply them<br>• compare and align different data models |
| [Metadata management](../../스킬/#metadata-management) | UK GDaD PCF | 실천가 | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../스킬/#problem-management) | UK GDaD PCF | 실무 | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Programming and build (data and analytics engineering)](../../스킬/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | 실천가 | You can:<br>• lead the design, code, testing and deployment of secure, resilient and maintainable solutions<br>• continuously improve the codebase and reliability of solutions<br>• create automation to improve the software development life cycle<br>• work with others to implement standards and good practice to ensure security, testability and maintainability of solutions |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자신의 업무가 뒷받침하는 임상 및 돌봄 워크플로를 설명한다<br>• 임상 및 돌봄 동료와 일반적인 의료 용어를 올바르게 사용한다<br>• 변경이 환자 돌봄에 영향을 줄 수 있는 때를 알아보고 제기한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• FHIR, HL7 버전 2, 메시징 패턴을 사용해 연동을 설계하고 구축한다<br>• FHIR 리소스와 구현 가이드를 작성하고 프로파일링한다<br>• 시스템 간의 복잡한 매핑과 데이터 품질 문제를 해결한다 |
| [임상 용어와 분류](../../스킬/#임상-용어와-분류) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 데이터 항목이나 양식에 맞는 코드를 찾아 사용한다<br>• 용어 브라우저와 참조 세트를 사용한다 |
| [가명처리와 공개 통제](../../스킬/#가명처리와-공개-통제) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 식별자를 분석 데이터와 분리해 두는 가명처리와 연결 방법을 설계한다<br>• 데이터 세트나 공표물의 재식별 위험을 평가하고 적절한 통제를 선택한다<br>• 신뢰할 수 있는 연구 환경 같은 안전한 환경에 대해 팀에 조언한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |

### 일반적인 자격과 경력

- 데이터 시스템의 설계와 구축에 관한 상당한 경력(석사에 준하는 수준).

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

## 밴드 8a: 리드 데이터 엔지니어

**UK GDaD PCF 수준: Lead data engineer**

> A lead data engineer is responsible for the design and implementation of numerous complex data flows to connect operational systems, data for analytics and business intelligence (BI) systems.
> 
> At this role level, you will:
> - recognise and share opportunities to reuse existing data flows between teams
> - be responsible for the build of data-streaming systems
> - co-ordinate teams and set best practice and standards
> - apply knowledge of systems integration to your work
> - champion data engineering across government

### 책임

- 조직의 데이터 플랫폼과 그 많은 데이터 흐름의 설계와 운영을 이끈다.
- 파이프라인, 테스트, 보안, 문서화의 엔지니어링 기준을 정한다.
- 공유 돌봄 기록과 지역 데이터 서비스를 포함하여 보건·돌봄 파트너와의 데이터 연동을 계획한다.
- 직접 돌봄을 뒷받침하는 데이터 흐름이 탄력적이고 임상 안전 케이스를 갖추도록 한다.
- 데이터 엔지니어링 팀을 조율하고 엔지니어를 직접 관리한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../스킬/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 실천가 | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Data analysis and synthesis](../../스킬/#data-analysis-and-synthesis) | UK GDaD PCF | 실천가 | You can:<br>• understand and help teams to apply a range of techniques for data profiling<br>• source system analysis from a complex single source<br>• bring multiple data sources together in a conformed model for analysis |
| [Data compliance and security](../../스킬/#data-compliance-and-security) | UK GDaD PCF | 전문가 | You can:<br>• advise senior stakeholders on data security, ethical or procedural risks<br>• improve organisational awareness of data compliance and procedures<br>• lead, guide and mentor teams in implementing secure data practices and maintaining compliance |
| [Data development process](../../스킬/#data-development-process) | UK GDaD PCF | 전문가 | You can:<br>• establish cross-organisational data solutions that include all aspects of the data development life cycle<br>• define and promote good practices for creating repeatable, reliable and reusable data solutions |
| [Data innovation](../../스킬/#data-innovation) | UK GDaD PCF | 실천가 | You can:<br>• test and evaluate the feasibility of unfamiliar and emerging technologies, or familiar technologies in new data contexts<br>• share what you learn with the organisation, explaining potential benefits, risks, and practical considerations<br>• recommend, design and implement innovative data solutions based on organisation objectives, user needs, and operational constraints |
| [Data integration design](../../스킬/#data-integration-design) | UK GDaD PCF | 전문가 | You can:<br>• establish cross-organisational data integration standards and design patterns<br>• guide teams in designing secure and interoperable systems and services |
| [Data modelling](../../스킬/#data-modelling) | UK GDaD PCF | 전문가 | You can:<br>• understand the concepts and principles of data modelling and can produce relevant data models<br>• work across government and industry, recognising opportunities for the reuse and alignment of data models in different organisations<br>• design the method to categorise data models within an organisation |
| [Metadata management](../../스킬/#metadata-management) | UK GDaD PCF | 실천가 | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../스킬/#problem-management) | UK GDaD PCF | 실천가 | You can:<br>• ensure that the right actions are taken to investigate, resolve and anticipate problems<br>• co-ordinate the team to investigate problems, implement solutions and take preventive measures |
| [Programming and build (data and analytics engineering)](../../스킬/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | 실천가 | You can:<br>• lead the design, code, testing and deployment of secure, resilient and maintainable solutions<br>• continuously improve the codebase and reliability of solutions<br>• create automation to improve the software development life cycle<br>• work with others to implement standards and good practice to ensure security, testability and maintainability of solutions |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 서비스가 조직 간 돌봄 경로에 어떻게 들어맞는지 분석한다<br>• 임상의, 돌봄 직원, 환자와 협력하여 디지털 서비스를 형성한다<br>• 디지털 결정이 돌봄, 안전, 직원 업무량에 미치는 영향을 설명한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• FHIR, HL7 버전 2, 메시징 패턴을 사용해 연동을 설계하고 구축한다<br>• FHIR 리소스와 구현 가이드를 작성하고 프로파일링한다<br>• 시스템 간의 복잡한 매핑과 데이터 품질 문제를 해결한다 |
| [임상 용어와 분류](../../스킬/#임상-용어와-분류) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 데이터 항목이나 양식에 맞는 코드를 찾아 사용한다<br>• 용어 브라우저와 참조 세트를 사용한다 |
| [가명처리와 공개 통제](../../스킬/#가명처리와-공개-통제) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 식별자를 분석 데이터와 분리해 두는 가명처리와 연결 방법을 설계한다<br>• 데이터 세트나 공표물의 재식별 위험을 평가하고 적절한 통제를 선택한다<br>• 신뢰할 수 있는 연구 환경 같은 안전한 환경에 대해 팀에 조언한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |
| [피플 매니지먼트](../../스킬/#피플-매니지먼트) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 목표를 설정하고 평가를 하며 팀을 직접 관리한다<br>• 웰빙을 지원하고 근태, 실적, 행위를 관리한다<br>• 팀의 육성과 승계를 계획한다 |

### 일반적인 자격과 경력

- 복잡한 시스템의 데이터 엔지니어링을 이끈 풍부한 경력.

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
| 8 | 재무 및 물적 자원에 대한 책임 | 2 | 12 |
| 9 | 사람에 대한 책임 | 3 | 21 |
| 10 | 정보 자원에 대한 책임 | 5 | 34 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 5 | 45 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **551** (밴드 8a: 540–584) |

## 밴드 8b: 데이터 엔지니어링 책임자

**UK GDaD PCF 수준: Head of data engineering**

> A head of data engineering leads multi-functional delivery teams to deliver robust data services for their department, other government departments and private sector partners.
> 
> At this role level, you will:
> - inspire best practice for data products and services within your teams
> - build data engineering capability by providing technical leadership and career development for the community
> - work with other senior team members to identify, plan, develop and deliver data services

### 책임

- 조직의 데이터 플랫폼과 데이터 엔지니어링 서비스의 전략을 정한다.
- 사내 팀과 보건·돌봄 파트너를 위해 데이터 서비스를 제공하는 다기능 팀을 이끈다.
- 데이터 플랫폼의 리스크, 비용, 투자에 대해 시니어 리더에게 조언한다.
- 데이터 서비스가 정보 거버넌스, 보안, 임상 안전 요구사항을 충족하도록 한다.
- 채용, 육성, 경력 경로를 통해 데이터 엔지니어링 역량을 키운다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../스킬/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 전문가 | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Data analysis and synthesis](../../스킬/#data-analysis-and-synthesis) | UK GDaD PCF | 실천가 | You can:<br>• understand and help teams to apply a range of techniques for data profiling<br>• source system analysis from a complex single source<br>• bring multiple data sources together in a conformed model for analysis |
| [Data compliance and security](../../스킬/#data-compliance-and-security) | UK GDaD PCF | 전문가 | You can:<br>• advise senior stakeholders on data security, ethical or procedural risks<br>• improve organisational awareness of data compliance and procedures<br>• lead, guide and mentor teams in implementing secure data practices and maintaining compliance |
| [Data development process](../../스킬/#data-development-process) | UK GDaD PCF | 전문가 | You can:<br>• establish cross-organisational data solutions that include all aspects of the data development life cycle<br>• define and promote good practices for creating repeatable, reliable and reusable data solutions |
| [Data innovation](../../스킬/#data-innovation) | UK GDaD PCF | 전문가 | You can:<br>• advocate for adoption of unfamiliar and emerging technologies, or familiar technologies in new data contexts, ensuring organisation objectives, user needs, and operational constraints inform decisions<br>• develop organisational capability in data innovation through leadership<br>• anticipate future technology changes and advise how to take advantage of them to realise value from data |
| [Data integration design](../../스킬/#data-integration-design) | UK GDaD PCF | 전문가 | You can:<br>• establish cross-organisational data integration standards and design patterns<br>• guide teams in designing secure and interoperable systems and services |
| [Data modelling](../../스킬/#data-modelling) | UK GDaD PCF | 실무 | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Metadata management](../../스킬/#metadata-management) | UK GDaD PCF | 전문가 | You can:<br>• identify how metadata repositories can support different areas of the organisation<br>• communicate the value of metadata repositories<br>• set up robust governance processes to keep repositories up to date |
| [Problem management](../../스킬/#problem-management) | UK GDaD PCF | 전문가 | You can:<br>• anticipate problems and defend against them at the right time<br>• understand how a problem fits into the larger picture<br>• identify and describe problems, and help others to describe them<br>• build problem-solving capabilities in others |
| [Programming and build (data and analytics engineering)](../../스킬/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | 전문가 | You can:<br>• set standards for programming tools and techniques<br>• select appropriate development methods for a problem<br>• advise on the application of standards and methods that ensure security, maintainability and compliance<br>• take technical responsibility for all stages of a software development project, providing technical advice and guidance to stakeholders |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 서비스가 조직 간 돌봄 경로에 어떻게 들어맞는지 분석한다<br>• 임상의, 돌봄 직원, 환자와 협력하여 디지털 서비스를 형성한다<br>• 디지털 결정이 돌봄, 안전, 직원 업무량에 미치는 영향을 설명한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 조직의 상호운용성 표준과 전략을 정한다<br>• 국가 또는 조직 간 표준화 작업을 이끈다<br>• 여러 시스템에 걸친 핵심 연동의 설계를 보증한다 |
| [가명처리와 공개 통제](../../스킬/#가명처리와-공개-통제) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 식별자를 분석 데이터와 분리해 두는 가명처리와 연결 방법을 설계한다<br>• 데이터 세트나 공표물의 재식별 위험을 평가하고 적절한 통제를 선택한다<br>• 신뢰할 수 있는 연구 환경 같은 안전한 환경에 대해 팀에 조언한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |
| [피플 매니지먼트](../../스킬/#피플-매니지먼트) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 목표를 설정하고 평가를 하며 팀을 직접 관리한다<br>• 웰빙을 지원하고 근태, 실적, 행위를 관리한다<br>• 팀의 육성과 승계를 계획한다 |
| [예산 관리](../../스킬/#예산-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 예산을 보유하고 관리하며, 차이를 예측하고 설명한다<br>• 비용과 편익을 보여 주는 비즈니스 케이스를 작성한다 |

### 일반적인 자격과 경력

- 여러 팀에 걸쳐 데이터 엔지니어링을 이끈 풍부한 경력.

### 밴드 개요

- **지식:** 여러 분야 또는 대규모 서비스에 걸친 전문 지식.
- **자율성:** 큰 영역의 방침과 전략을 만든다.
- **범위:** 여러 서비스와 팀, 또는 프린시펄 수준의 분야.
- **리더십:** 매니저를 관리하거나, 한 분야의 최고 전문가이다.
- **책무:** 여러 서비스, 그 직원, 그리고 예산.

### 직무평가(예시)

| # | 요소 | 수준 | 점수 |
| --- | --- | --- | --- |
| 1 | 의사소통 및 관계 형성 기술 | 5 | 45 |
| 2 | 지식, 교육, 경험 | 7 | 196 |
| 3 | 분석 및 판단 기술 | 5 | 60 |
| 4 | 계획 및 조직화 기술 | 5 | 60 |
| 5 | 신체 기술 | 2 | 15 |
| 6 | 환자·이용자 돌봄에 대한 책임 | 1 | 4 |
| 7 | 정책 및 서비스 개발에 대한 책임 | 4 | 32 |
| 8 | 재무 및 물적 자원에 대한 책임 | 3 | 21 |
| 9 | 사람에 대한 책임 | 4 | 32 |
| 10 | 정보 자원에 대한 책임 | 5 | 34 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 5 | 45 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **589** (밴드 8b: 585–629) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
