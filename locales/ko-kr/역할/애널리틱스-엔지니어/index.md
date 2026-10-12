# 애널리틱스 엔지니어

> 이 문서는 일반적인 디지털 헬스케어 조직을 위한 예시용 참조 프로필입니다. 특정 고용주의 공식 직무기술서가 아니며, 직무평가 점수도 공식 평가가 아닙니다.

> 이 글은 AI 어시스턴트가 영어를 한국어로 번역한 것이며, 한국어 원어민의 검토는 아직 받지 않았습니다. 영국 정부 디지털·데이터 전문직 역량 프레임워크(UK GDaD PCF)와 ESCO의 인용문은 영어 그대로 두었습니다.

**직군:** [데이터](../../#데이터)  
**밴드:** 4, 6, 7, 8a, 8c  
**UK GDaD PCF 역할:** [Analytics engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/analytics-engineer/)  
**ESCO 직업:** [data engineer](http://data.europa.eu/esco/occupation/2079755f-d809-49e6-8037-4de6180e54c0) (ISCO-08 2511); [business intelligence manager](http://data.europa.eu/esco/occupation/207d7b18-6540-432e-8aa6-785ed434572f) (ISCO-08 2421)

## 개요

애널리틱스 엔지니어는 날것의 보건·돌봄 데이터를 분석가, 데이터 사이언티스트, 보고 도구가 믿고 쓸 수 있는 깨끗하고, 테스트되고, 문서화된 데이터 모델로 바꾼다. 데이터 엔지니어링과 분석 사이에 위치하며, 버전 관리, 테스트, 코드 리뷰 같은 소프트웨어 엔지니어링 관행을 조직의 보고서와 대시보드 이면의 변환 작업에 적용한다.

## 디지털 헬스케어 조직에서

- 데이터 모델은 무엇을 입원, 재입원, 대기 시간 기준 위반으로 셀지 등 임상과 운영의 정의를 담으므로, 정의는 임상·운영 리드와 합의된다.
- SNOMED CT와 ICD 같은 용어 체계·분류의 임상 코드는 분석을 위해 참조 세트로 묶이며 신중한 버전 관리가 필요하다.
- 성과나 자금 보고에 쓰이는 모델은 오류가 서비스 관련 결정에 영향을 줄 수 있으므로 일관되고 감사 가능해야 한다.
- 모델은 가명처리된 환자 수준 데이터를 보유하는 경우가 많으므로, 접근, 문서화, 데이터 최소화가 내장된다.

## UK GDaD PCF 역할 설명(원문은 영어)

> An analytics engineer transforms data relevant to the organisation into structures that enable analysis and decision-making.
> 
> In this role, you will:
> - work with subject matter experts to understand organisational processes and translate these into data structures optimised for analysis
> - work with data users to design and build data models they can use for effective analysis and decision-making, using modelling techniques such as Kimball or Inmon
> - support data quality improvement
> - develop standards for data transformation
> - create and maintain data documentation
> - refine requirements in response to feedback from users and changes in the organisation
> - provide ongoing support to users

## 역할 수준

| 밴드 | 직함 | UK GDaD PCF 수준 | 영국 공무원 등급 | 직무평가 점수 |
| --- | --- | --- | --- | --- |
| 4 | [트레이니 애널리틱스 엔지니어](#밴드-4-트레이니-애널리틱스-엔지니어) | Trainee analytics engineer | AO/EO | 276 |
| 6 | [애널리틱스 엔지니어](#밴드-6-애널리틱스-엔지니어) | Analytics engineer | HEO/SEO | 418 |
| 7 | [시니어 애널리틱스 엔지니어](#밴드-7-시니어-애널리틱스-엔지니어) | Senior analytics engineer | SEO/G7 | 477 |
| 8a | [리드 애널리틱스 엔지니어](#밴드-8a-리드-애널리틱스-엔지니어) | Lead analytics engineer | G7 | 551 |
| 8c | [애널리틱스 엔지니어링 책임자](#밴드-8c-애널리틱스-엔지니어링-책임자) | Head of analytics engineering | G6 | 634 |

## 밴드 4: 트레이니 애널리틱스 엔지니어

**UK GDaD PCF 수준: Trainee analytics engineer**

> A trainee analytics engineer attends training and develops skills on the job.
> 
> At this role level, you will:
> - spend time shadowing other analytics engineers
> - build your knowledge of the organisation
> - learn skills for managing data
> - learn to use different applications, tools, templates and best practices
> - handle simple queries from users and document their data requirements
> - contribute to data documentation and user training

### 책임

- 교육과 페어 작업을 통해 팀의 데이터 모델링 도구와 관행을 배운다.
- 감독을 받으며 데이터 모델에 작고 명확하게 정의된 변경을 가한다.
- 데이터 항목과 그 정의를 데이터 카탈로그에 문서화한다.
- 데이터 이용자의 단순한 질문에 답하고 요구사항을 기록한다.
- 환자 데이터를 다룰 때 정보 거버넌스 규칙을 따른다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../스킬/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 인지 | You can:<br>• explain why it's important to communicate technical concepts in non-technical language<br>• explain the types of communication that can be used with internal and external stakeholders, and their impact |
| [Data analysis and synthesis](../../스킬/#data-analysis-and-synthesis) | UK GDaD PCF | 인지 | You can:<br>• interpret data to find key insights |
| [Data innovation](../../스킬/#data-innovation) | UK GDaD PCF | 인지 | You can:<br>• develop a basic understanding of an unfamiliar or emerging technology, or a familiar technology in a new data context, with guidance<br>• share what you learn with colleagues, including how it could help deliver more value from data |
| [Data modelling, cleansing and enrichment](../../스킬/#data-modelling-cleansing-and-enrichment) | UK GDaD PCF | 인지 | You can:<br>• show an awareness of different data models and tools, and understand when they could be used<br>• show an awareness of industry-recognised data modelling patterns and standards |
| [Metadata management](../../스킬/#metadata-management) | UK GDaD PCF | 인지 | You can:<br>• explain what metadata is<br>• maintain the information stored in metadata repositories under the direction of others |
| [Problem management](../../스킬/#problem-management) | UK GDaD PCF | 인지 | You can:<br>• investigate problems in systems, processes and services, with an understanding of the level of a problem, for example, strategic, tactical or operational<br>• contribute to the implementation of remedies and preventative measures |
| [Testing](../../스킬/#testing) | UK GDaD PCF | 인지 | You can:<br>• correctly execute test scripts under supervision<br>• understand the role of testing and how it works |
| [Turning business problems into data design](../../스킬/#turning-business-problems-into-data-design) | UK GDaD PCF | 인지 | You can:<br>• contribute to the design of data architecture under the direction of others |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 보건·돌봄 시스템의 주요 부분과 조직이 지원하는 서비스를 설명한다<br>• 자신의 업무에서 환자 안전과 비밀 유지가 중요한 이유를 설명한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 개인 정보와 건강 정보를 다루는 조직의 규칙을 따른다<br>• 데이터 침해나 아차 사고를 알아보고 보고한다 |
| [데이터 품질 관리](../../스킬/#데이터-품질-관리) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 정확한 보건 데이터가 돌봄과 계획에 중요한 이유를 설명한다<br>• 데이터를 정확하게 기록하고 오류를 보고한다 |
| [임상 용어와 분류](../../스킬/#임상-용어와-분류) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 임상 용어 체계와 분류의 차이를 설명한다<br>• SNOMED CT와 ICD 같은 일반적인 용어 체계를 알아본다 |

### 일반적인 자격과 경력

- 데이터 어프렌티스십 또는 그에 준하는 과정에 등록했거나 취득을 목표로 하고 있다.

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
| 7 | 정책 및 서비스 개발에 대한 책임 | 1 | 5 |
| 8 | 재무 및 물적 자원에 대한 책임 | 1 | 5 |
| 9 | 사람에 대한 책임 | 1 | 5 |
| 10 | 정보 자원에 대한 책임 | 4 | 24 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 2 | 12 |
| 13 | 신체적 부담 | 2 | 7 |
| 14 | 정신적 부담 | 3 | 12 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **276** (밴드 4: 271–325) |

지식은 업무를 수행할 수 있을 만큼 교육이 끝난 시점에 직무가 요구하는 수준으로 평가했다.

## 밴드 6: 애널리틱스 엔지니어

**UK GDaD PCF 수준: Analytics engineer**

> An analytics engineer develops and tests data models assigned by more senior analytics engineers to help people in a defined area access and use data.
> 
> At this role level, you will:
> - draft documentation of data that meets standards
> - work with other analytics engineers to resolve issues and risks
> - support trainee analytics engineers
> - provide training and support for users of data sets
> - work with more experienced analytics engineers to develop your skills

### 책임

- 합의된 설계에서 입원 환자 활동이나 지역사회 돌봄 등 서비스 영역의 데이터 모델을 구축하고 테스트한다.
- 데이터 모델을 합의된 임상·운영 정의에 비추어 확인하는 자동화 테스트를 작성한다.
- 분석에 쓰는 임상 코드 참조 세트를 명확한 버전과 함께 유지한다.
- 분석가가 모델의 의미, 소스, 한계를 이해할 수 있도록 모델을 문서화한다.
- 팀의 데이터셋 이용자를 교육하고 지원한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../스킬/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 실무 | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Data analysis and synthesis](../../스킬/#data-analysis-and-synthesis) | UK GDaD PCF | 실무 | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data innovation](../../스킬/#data-innovation) | UK GDaD PCF | 인지 | You can:<br>• develop a basic understanding of an unfamiliar or emerging technology, or a familiar technology in a new data context, with guidance<br>• share what you learn with colleagues, including how it could help deliver more value from data |
| [Data modelling, cleansing and enrichment](../../스킬/#data-modelling-cleansing-and-enrichment) | UK GDaD PCF | 실무 | You can:<br>• produce data models and understand where to use different types of data models<br>• understand different tools and can compare different data models<br>• reverse-engineer a data model from a live system<br>• understand industry-recognised data modelling patterns and standards |
| [Metadata management](../../스킬/#metadata-management) | UK GDaD PCF | 실무 | You can:<br>• use metadata repositories to complete complex tasks such as data and systems integration impact analysis<br>• maintain a metadata repository to ensure information remains accurate and up to date |
| [Problem management](../../스킬/#problem-management) | UK GDaD PCF | 인지 | You can:<br>• investigate problems in systems, processes and services, with an understanding of the level of a problem, for example, strategic, tactical or operational<br>• contribute to the implementation of remedies and preventative measures |
| [Programming and build (data and analytics engineering)](../../스킬/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | 실무 | You can:<br>• design, code, test and deploy programs or scripts following standards and good practice<br>• write readable, maintainable code<br>• use automation to improve the software development life cycle<br>• consider and adopt appropriate security measures in your solutions |
| [Testing](../../스킬/#testing) | UK GDaD PCF | 인지 | You can:<br>• correctly execute test scripts under supervision<br>• understand the role of testing and how it works |
| [Turning business problems into data design](../../스킬/#turning-business-problems-into-data-design) | UK GDaD PCF | 실무 | You can:<br>• design data architecture by dealing with specific business problems and aligning it to enterprise-wide standards and principles<br>• work within the context of well understood architecture, and identify appropriate patterns |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자신의 업무가 뒷받침하는 임상 및 돌봄 워크플로를 설명한다<br>• 임상 및 돌봄 동료와 일반적인 의료 용어를 올바르게 사용한다<br>• 변경이 환자 돌봄에 영향을 줄 수 있는 때를 알아보고 제기한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [데이터 품질 관리](../../스킬/#데이터-품질-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 데이터 품질 점검을 실행하고 오류를 바로잡는다<br>• 데이터 품질 보고서를 동료에게 설명한다 |
| [임상 용어와 분류](../../스킬/#임상-용어와-분류) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 데이터 항목이나 양식에 맞는 코드를 찾아 사용한다<br>• 용어 브라우저와 참조 세트를 사용한다 |
| [가명처리와 공개 통제](../../스킬/#가명처리와-공개-통제) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 식별 가능한 데이터, 가명처리된 데이터, 익명처리된 데이터의 차이를 설명한다<br>• 결과물에서 소수 값을 가리는 조직의 규칙을 따른다 |

### 일반적인 자격과 경력

- 정량적 또는 컴퓨팅 분야 학위, 또는 그에 준하는 경력.
- 데이터 모델 또는 분석 코드를 구축한 경험.

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
| 10 | 정보 자원에 대한 책임 | 4 | 24 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 4 | 32 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **418** (밴드 6: 396–465) |

## 밴드 7: 시니어 애널리틱스 엔지니어

**UK GDaD PCF 수준: Senior analytics engineer**

> A senior analytics engineer oversees the development and testing of data models, including directing the work of other analytics engineers.
> 
> At this role level, you will:
> - oversee tasks and support less senior analytics engineers
> - build relationships with stakeholders within a defined area
> - coach and mentor less senior analytics engineers
> - ensure documentation of data meets standards
> - ensure issues and risks are resolved
> - oversee training and support for users of data sets
> - explore and develop new ways of working with data

### 책임

- 여러 서비스 영역에 걸친 데이터 모델의 설계와 테스트를 감독한다.
- 임상, 운영, 재무 리드와 핵심 지표의 정의에 합의하고 모델이 이를 일관되게 적용하도록 한다.
- 성과나 자금 보고에 쓰이는 모델이 감사 가능하고 충분히 테스트되도록 한다.
- 데이터 엔지니어, 데이터 오너와 함께 데이터 과제와 리스크를 해결한다.
- 다른 애널리틱스 엔지니어의 업무를 코칭하고 방향을 제시한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../스킬/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 실무 | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Data analysis and synthesis](../../스킬/#data-analysis-and-synthesis) | UK GDaD PCF | 실무 | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data innovation](../../스킬/#data-innovation) | UK GDaD PCF | 실무 | You can:<br>• experiment with unfamiliar and emerging technologies, or familiar technologies in new data contexts, with guidance<br>• share what you learn with the team, explaining potential benefits, risks, and practical considerations<br>• identify opportunities to apply technology to improve data processes or outcomes in an operational setting or the wider organisation |
| [Data modelling, cleansing and enrichment](../../스킬/#data-modelling-cleansing-and-enrichment) | UK GDaD PCF | 실천가 | You can:<br>• build and review complex data models, ensuring adherence to standards<br>• use data integration tools and languages to integrate and store data, and advise teams on best practice<br>• ensure data for analysis meets data quality standards and is interoperable with other data sets, enabling reuse<br>• work with other data professionals to improve modelling and integration patterns and standards |
| [Metadata management](../../스킬/#metadata-management) | UK GDaD PCF | 실천가 | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../스킬/#problem-management) | UK GDaD PCF | 실무 | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Programming and build (data and analytics engineering)](../../스킬/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | 실천가 | You can:<br>• lead the design, code, testing and deployment of secure, resilient and maintainable solutions<br>• continuously improve the codebase and reliability of solutions<br>• create automation to improve the software development life cycle<br>• work with others to implement standards and good practice to ensure security, testability and maintainability of solutions |
| [Testing](../../스킬/#testing) | UK GDaD PCF | 실무 | You can:<br>• review requirements and specifications, and define test conditions<br>• identify issues and risks associated with work<br>• analyse and report test activities and results |
| [Turning business problems into data design](../../스킬/#turning-business-problems-into-data-design) | UK GDaD PCF | 실천가 | You can:<br>• design data architecture that deals with problems spanning different business areas<br>• identify links between problems to devise common solutions<br>• work across multiple subject areas, or a single large or complicated subject area<br>• produce appropriate patterns |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 서비스가 조직 간 돌봄 경로에 어떻게 들어맞는지 분석한다<br>• 임상의, 돌봄 직원, 환자와 협력하여 디지털 서비스를 형성한다<br>• 디지털 결정이 돌봄, 안전, 직원 업무량에 미치는 영향을 설명한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [데이터 품질 관리](../../스킬/#데이터-품질-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 데이터 품질 규칙과 지표를 정의한다<br>• 데이터 제공처와 협력해 품질 저하의 근본 원인을 수정한다 |
| [임상 용어와 분류](../../스킬/#임상-용어와-분류) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 임상 용어 체계를 사용하여 데이터 모델과 참조 세트를 설계한다<br>• 용어 체계와 분류 사이를 매핑하고 매핑의 한계를 설명한다<br>• 프로덕트와 분석에서의 용어 사용에 대해 팀에 조언한다 |
| [가명처리와 공개 통제](../../스킬/#가명처리와-공개-통제) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 가명처리된 데이터로 작업하고, 결과물을 공개하기 전에 공개 점검을 적용한다<br>• 연결되었거나 상세한 데이터로 환자를 식별할 수 있는 경우를 알아본다 |

### 일반적인 자격과 경력

- 데이터 모델링과 애널리틱스 엔지니어링에 관한 상당한 경력(석사에 준하는 수준).

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

## 밴드 8a: 리드 애널리틱스 엔지니어

**UK GDaD PCF 수준: Lead analytics engineer**

> A lead analytics engineer leads the design and deployment of data models for analysis.
> 
> At this role level, you will:
> - lead and support a team of analytics engineers to design, build and maintain data models
> - work with stakeholders and teams across the organisation to understand relationships between data and organisational processes, and use this to define data requirements
> - promote, build awareness and support understanding of analytics engineering
> - review the work of other analytics engineers
> - create standards for communication, data models and documentation
> - define and improve ways of working in the team

### 책임

- 조직의 분석용 데이터 모델을 설계, 구축, 유지하는 팀을 이끈다.
- 데이터 모델, 테스트, 문서화, 지표 정의의 기준을 정한다.
- 조직 전체의 팀과 협력하여 임상·운영 프로세스가 데이터를 어떻게 만들어 내는지 이해한다.
- 다른 애널리틱스 엔지니어의 업무를 검토하고 팀의 업무 방식을 개선한다.
- 애널리틱스 엔지니어를 직접 관리한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../스킬/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 실천가 | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Data analysis and synthesis](../../스킬/#data-analysis-and-synthesis) | UK GDaD PCF | 실천가 | You can:<br>• understand and help teams to apply a range of techniques for data profiling<br>• source system analysis from a complex single source<br>• bring multiple data sources together in a conformed model for analysis |
| [Data innovation](../../스킬/#data-innovation) | UK GDaD PCF | 실천가 | You can:<br>• test and evaluate the feasibility of unfamiliar and emerging technologies, or familiar technologies in new data contexts<br>• share what you learn with the organisation, explaining potential benefits, risks, and practical considerations<br>• recommend, design and implement innovative data solutions based on organisation objectives, user needs, and operational constraints |
| [Data modelling, cleansing and enrichment](../../스킬/#data-modelling-cleansing-and-enrichment) | UK GDaD PCF | 실천가 | You can:<br>• build and review complex data models, ensuring adherence to standards<br>• use data integration tools and languages to integrate and store data, and advise teams on best practice<br>• ensure data for analysis meets data quality standards and is interoperable with other data sets, enabling reuse<br>• work with other data professionals to improve modelling and integration patterns and standards |
| [Metadata management](../../스킬/#metadata-management) | UK GDaD PCF | 실천가 | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../스킬/#problem-management) | UK GDaD PCF | 실천가 | You can:<br>• ensure that the right actions are taken to investigate, resolve and anticipate problems<br>• co-ordinate the team to investigate problems, implement solutions and take preventive measures |
| [Programming and build (data and analytics engineering)](../../스킬/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | 실천가 | You can:<br>• lead the design, code, testing and deployment of secure, resilient and maintainable solutions<br>• continuously improve the codebase and reliability of solutions<br>• create automation to improve the software development life cycle<br>• work with others to implement standards and good practice to ensure security, testability and maintainability of solutions |
| [Testing](../../스킬/#testing) | UK GDaD PCF | 실무 | You can:<br>• review requirements and specifications, and define test conditions<br>• identify issues and risks associated with work<br>• analyse and report test activities and results |
| [Turning business problems into data design](../../스킬/#turning-business-problems-into-data-design) | UK GDaD PCF | 실천가 | You can:<br>• design data architecture that deals with problems spanning different business areas<br>• identify links between problems to devise common solutions<br>• work across multiple subject areas, or a single large or complicated subject area<br>• produce appropriate patterns |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 서비스가 조직 간 돌봄 경로에 어떻게 들어맞는지 분석한다<br>• 임상의, 돌봄 직원, 환자와 협력하여 디지털 서비스를 형성한다<br>• 디지털 결정이 돌봄, 안전, 직원 업무량에 미치는 영향을 설명한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [데이터 품질 관리](../../스킬/#데이터-품질-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 데이터 품질 규칙과 지표를 정의한다<br>• 데이터 제공처와 협력해 품질 저하의 근본 원인을 수정한다 |
| [임상 용어와 분류](../../스킬/#임상-용어와-분류) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 임상 용어 체계를 사용하여 데이터 모델과 참조 세트를 설계한다<br>• 용어 체계와 분류 사이를 매핑하고 매핑의 한계를 설명한다<br>• 프로덕트와 분석에서의 용어 사용에 대해 팀에 조언한다 |
| [가명처리와 공개 통제](../../스킬/#가명처리와-공개-통제) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 가명처리된 데이터로 작업하고, 결과물을 공개하기 전에 공개 점검을 적용한다<br>• 연결되었거나 상세한 데이터로 환자를 식별할 수 있는 경우를 알아본다 |
| [피플 매니지먼트](../../스킬/#피플-매니지먼트) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 목표를 설정하고 평가를 하며 팀을 직접 관리한다<br>• 웰빙을 지원하고 근태, 실적, 행위를 관리한다<br>• 팀의 육성과 승계를 계획한다 |

### 일반적인 자격과 경력

- 애널리틱스 엔지니어링 또는 데이터 모델링을 이끈 풍부한 경력.

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

## 밴드 8c: 애널리틱스 엔지니어링 책임자

**UK GDaD PCF 수준: Head of analytics engineering**

> A head of analytics engineering oversees the development of a range of data models that meet analysis needs across the organisation.
> 
> At this role level, you will:
> - build relationships with senior stakeholders across the organisation to determine what the organisation needs
> - ensure the activities of the analytics engineering team align with strategic priorities
> - ensure the team works to standards for communication, data models and documentation
> - advocate for the analytics engineering role to senior leadership and other organisations
> - build analytics engineering capability by providing technical leadership and career development for the community
> - ensure appropriate technology is available for the community

### 책임

- 조직 전체의 분석이 하나의 신뢰할 수 있는 정의 집합을 쓸 수 있도록 조직의 분석용 데이터 모델의 방향을 정한다.
- 애널리틱스 엔지니어링의 우선순위가 조직의 전략과 보고 의무를 뒷받침하도록 한다.
- 주요 보고서와 의사결정 이면의 데이터 신뢰성에 대해 시니어 리더에게 조언한다.
- 커뮤니티가 필요한 도구와 플랫폼을 갖추도록 하고 관련 예산을 관리한다.
- 기술적 리더십과 경력 개발을 통해 애널리틱스 엔지니어링 역량을 키운다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../스킬/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 전문가 | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Data analysis and synthesis](../../스킬/#data-analysis-and-synthesis) | UK GDaD PCF | 실천가 | You can:<br>• understand and help teams to apply a range of techniques for data profiling<br>• source system analysis from a complex single source<br>• bring multiple data sources together in a conformed model for analysis |
| [Data innovation](../../스킬/#data-innovation) | UK GDaD PCF | 전문가 | You can:<br>• advocate for adoption of unfamiliar and emerging technologies, or familiar technologies in new data contexts, ensuring organisation objectives, user needs, and operational constraints inform decisions<br>• develop organisational capability in data innovation through leadership<br>• anticipate future technology changes and advise how to take advantage of them to realise value from data |
| [Data modelling, cleansing and enrichment](../../스킬/#data-modelling-cleansing-and-enrichment) | UK GDaD PCF | 전문가 | You can:<br>• understand different ways to model data to maximise its use and value<br>• ensure data is modelled appropriately, and modelling standards exist and are complied with<br>• understand a number of data integration tools and patterns, and ensure your teams have the support and training needed to use the most appropriate methods<br>• build relationships with other senior data professionals (in fields such as data architecture, data engineering and data science) to share best practice and continually improve data modelling and integration processes and standards |
| [Metadata management](../../스킬/#metadata-management) | UK GDaD PCF | 전문가 | You can:<br>• identify how metadata repositories can support different areas of the organisation<br>• communicate the value of metadata repositories<br>• set up robust governance processes to keep repositories up to date |
| [Problem management](../../스킬/#problem-management) | UK GDaD PCF | 전문가 | You can:<br>• anticipate problems and defend against them at the right time<br>• understand how a problem fits into the larger picture<br>• identify and describe problems, and help others to describe them<br>• build problem-solving capabilities in others |
| [Programming and build (data and analytics engineering)](../../스킬/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | 전문가 | You can:<br>• set standards for programming tools and techniques<br>• select appropriate development methods for a problem<br>• advise on the application of standards and methods that ensure security, maintainability and compliance<br>• take technical responsibility for all stages of a software development project, providing technical advice and guidance to stakeholders |
| [Testing](../../스킬/#testing) | UK GDaD PCF | 실무 | You can:<br>• review requirements and specifications, and define test conditions<br>• identify issues and risks associated with work<br>• analyse and report test activities and results |
| [Turning business problems into data design](../../스킬/#turning-business-problems-into-data-design) | UK GDaD PCF | 전문가 | You can:<br>• design data architecture that deals with problems across the enterprise<br>• work across all organisational subject areas and internal and external programmes |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 보건·돌봄 시스템에 대한 깊은 이해를 바탕으로 조직 전략을 형성한다<br>• 보건·돌봄 파트너와 리더에게 조직을 대표한다<br>• 정책과 서비스 변화가 디지털 서비스와 돌봄에 어떤 영향을 줄지 예측한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [데이터 품질 관리](../../스킬/#데이터-품질-관리) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 조직과 그 파트너의 데이터 품질 기준을 정한다<br>• 데이터 품질 개선 프로그램을 이끈다 |
| [임상 용어와 분류](../../스킬/#임상-용어와-분류) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 임상 용어 체계를 사용하여 데이터 모델과 참조 세트를 설계한다<br>• 용어 체계와 분류 사이를 매핑하고 매핑의 한계를 설명한다<br>• 프로덕트와 분석에서의 용어 사용에 대해 팀에 조언한다 |
| [피플 매니지먼트](../../스킬/#피플-매니지먼트) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 매니저를 이끌고 큰 영역의 문화를 형성한다<br>• 인력 계획과 조직 변경을 설계한다<br>• 리더를 코칭하고 복잡한 사람 문제를 해결한다 |
| [예산 관리](../../스킬/#예산-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 예산을 보유하고 관리하며, 차이를 예측하고 설명한다<br>• 비용과 편익을 보여 주는 비즈니스 케이스를 작성한다 |

### 일반적인 자격과 경력

- 조직 전체에서 애널리틱스 엔지니어링을 이끈 풍부한 경력.

### 밴드 개요

- **지식:** 전문 지식에 더해 더 넓은 조직과 분야에 대한 이해.
- **자율성:** 기능의 전략을 정하고 디렉터에게 책임을 진다.
- **범위:** 기능 또는 부문.
- **리더십:** 여러 관리 계층을 통해 기능을 이끈다.
- **책무:** 기능의 성과, 인력, 예산.

### 직무평가(예시)

| # | 요소 | 수준 | 점수 |
| --- | --- | --- | --- |
| 1 | 의사소통 및 관계 형성 기술 | 6 | 60 |
| 2 | 지식, 교육, 경험 | 7 | 196 |
| 3 | 분석 및 판단 기술 | 5 | 60 |
| 4 | 계획 및 조직화 기술 | 5 | 60 |
| 5 | 신체 기술 | 2 | 15 |
| 6 | 환자·이용자 돌봄에 대한 책임 | 1 | 4 |
| 7 | 정책 및 서비스 개발에 대한 책임 | 5 | 45 |
| 8 | 재무 및 물적 자원에 대한 책임 | 4 | 32 |
| 9 | 사람에 대한 책임 | 4 | 32 |
| 10 | 정보 자원에 대한 책임 | 6 | 46 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 5 | 45 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 3 | 12 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **634** (밴드 8c: 630–674) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
