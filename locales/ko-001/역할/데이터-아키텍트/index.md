# 데이터 아키텍트

> 이 문서는 일반적인 디지털 헬스케어 조직을 위한 예시용 참조 프로필입니다. 특정 고용주의 공식 직무기술서가 아니며, 직무평가 점수도 공식 평가가 아닙니다.

> 이 글은 AI 어시스턴트가 영어를 한국어로 번역한 것이며, 한국어 원어민의 검토는 아직 받지 않았습니다. 영국 정부 디지털·데이터 전문직 역량 프레임워크(UK GDaD PCF)와 ESCO의 인용문은 영어 그대로 두었습니다.

**직군:** [아키텍처](../../#아키텍처)  
**밴드:** 8a, 8b, 8c  
**UK GDaD PCF 역할:** [Data architect](https://understand-digital-data-roles-skills.service.gov.uk/role/data-architect/)  
**ESCO 직업:** [database designer](http://data.europa.eu/esco/occupation/8d9ec84d-cf2d-4179-87bc-335cda54a427) (ISCO-08 2521); [data warehouse designer](http://data.europa.eu/esco/occupation/1562c7a3-c7d9-419d-b9b6-db26610bcf84) (ISCO-08 2521)

## 개요

데이터 아키텍트는 조직이 보건·돌봄 데이터를 어떻게 구조화하고, 저장하고, 이동하고, 통제할지를 설계하여, 직접 돌봄, 서비스 계획, 연구에 안전하게 쓸 수 있도록 한다. 데이터 모델, 데이터 플랫폼, 데이터 흐름을 설계하고 데이터 표준을 정하며, 임상적 의미, 품질, 비밀이 처음부터 끝까지 유지되도록 한다.

## 디지털 헬스케어 조직에서

- 건강 데이터는 임상적 의미를 유지해야 하므로, 데이터 모델은 SNOMED CT 같은 임상 용어 체계와 ICD 같은 분류를 사용한다.
- 직접 돌봄에 쓰는 데이터와 계획이나 연구에 쓰는 데이터는 법적 근거가 다르므로, 아키텍트는 분리, 비식별화, 관리된 접근을 설계한다.
- 데이터는 품질이 다양한 여러 임상·돌봄 시스템에서 오므로, 아키텍트는 데이터 품질 점검, 환자 매칭, 데이터 계보를 설계한다.
- 공유 돌봄 기록과 데이터 교환은 HL7 FHIR 리소스 같은 공통 모델과 합의된 국내외 데이터셋에 의존한다.
- 기록은 긴 보존 기간 동안 보관해야 하므로, 설계는 과거 데이터의 보관과 접근을 계획해야 한다.

## UK GDaD PCF 역할 설명(원문은 영어)

> A data architect sets the vision for the organisation’s use of data, through data design, to ensure that data is managed properly and meets the organisation’s needs.

## 역할 수준

| 밴드 | 직함 | UK GDaD PCF 수준 | 영국 공무원 등급 | 직무평가 점수 |
| --- | --- | --- | --- | --- |
| 8a | [데이터 아키텍트](#밴드-8a-데이터-아키텍트) | Data architect | SEO/G7 | 560 |
| 8b | [시니어 데이터 아키텍트](#밴드-8b-시니어-데이터-아키텍트) | Senior data architect | G7/G6 | 613 |
| 8c | [최고 데이터 아키텍트](#밴드-8c-최고-데이터-아키텍트) | Chief data architect | G6 | 662 |

## 밴드 8a: 데이터 아키텍트

**UK GDaD PCF 수준: Data architect**

> A data architect designs and builds data models to fulfil the strategic data needs of the organisation, as defined by chief data architects.
> 
> At this role level, you will:
> - design, support and provide guidance for the upgrade, management, decommission and archive of data in compliance with data policy
> - provide input into data dictionaries
> - define and maintain the data technology architecture, including metadata, integration and business intelligence or data warehouse architecture

### 책임

- 필요에 따라 임상 용어 체계를 사용해 임상 및 운영 데이터의 논리·물리 데이터 모델을 설계한다.
- 데이터 웨어하우스, 레이크하우스, 연동 계층 등 데이터 흐름과 데이터 플랫폼 컴포넌트를 설계한다.
- 담당 영역의 데이터셋에 대해 메타데이터, 데이터 사전 항목, 데이터 계보를 정의한다.
- 데이터가 적법한 목적에만 쓰이도록 비식별화와 접근 제어를 설계한다.
- 데이터 품질 및 임상 코딩 동료와 협력하여 데이터 품질 저하의 구조적 원인을 수정한다.
- 데이터 모델과 표준에 대해 데이터 엔지니어와 분석가를 이끈다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../스킬/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 실무 | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Communicating data](../../스킬/#communicating-data) | UK GDaD PCF | 인지 | You can:<br>• show an awareness that data needs to be aligned to the needs of the end user<br>• create basic visuals and presentations |
| [Data analysis and synthesis](../../스킬/#data-analysis-and-synthesis) | UK GDaD PCF | 실무 | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../스킬/#data-governance-data-architect) | UK GDaD PCF | 실무 | You can:<br>• understand what data governance is required<br>• take responsibility for the assurance of data solutions and make recommendations to ensure compliance |
| [Data innovation](../../스킬/#data-innovation) | UK GDaD PCF | 인지 | You can:<br>• develop a basic understanding of an unfamiliar or emerging technology, or a familiar technology in a new data context, with guidance<br>• share what you learn with colleagues, including how it could help deliver more value from data |
| [Data modelling](../../스킬/#data-modelling) | UK GDaD PCF | 실무 | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Data standards](../../스킬/#data-standards) | UK GDaD PCF | 실무 | You can:<br>• use data policies, processes and standards effectively<br>• work with subject matter experts to develop standards, policies and guidance to protect data<br>• monitor compliance with policies and standards in a team and take action if needed<br>• analyse the impact if a standard is breached |
| [Metadata management](../../스킬/#metadata-management) | UK GDaD PCF | 실무 | You can:<br>• use metadata repositories to complete complex tasks such as data and systems integration impact analysis<br>• maintain a metadata repository to ensure information remains accurate and up to date |
| [Problem management](../../스킬/#problem-management) | UK GDaD PCF | 실무 | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Strategic thinking](../../스킬/#strategic-thinking) | UK GDaD PCF | 인지 | You can:<br>• explain the strategic context of your work and why it is important<br>• support strategic planning in an administrative capacity |
| [Turning business problems into data design](../../스킬/#turning-business-problems-into-data-design) | UK GDaD PCF | 실무 | You can:<br>• design data architecture by dealing with specific business problems and aligning it to enterprise-wide standards and principles<br>• work within the context of well understood architecture, and identify appropriate patterns |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자신의 업무가 뒷받침하는 임상 및 돌봄 워크플로를 설명한다<br>• 임상 및 돌봄 동료와 일반적인 의료 용어를 올바르게 사용한다<br>• 변경이 환자 돌봄에 영향을 줄 수 있는 때를 알아보고 제기한다 |
| [임상 용어와 분류](../../스킬/#임상-용어와-분류) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 데이터 항목이나 양식에 맞는 코드를 찾아 사용한다<br>• 용어 브라우저와 참조 세트를 사용한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• FHIR, HL7 버전 2, 메시징 패턴을 사용해 연동을 설계하고 구축한다<br>• FHIR 리소스와 구현 가이드를 작성하고 프로파일링한다<br>• 시스템 간의 복잡한 매핑과 데이터 품질 문제를 해결한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [데이터 품질 관리](../../스킬/#데이터-품질-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 데이터 품질 점검을 실행하고 오류를 바로잡는다<br>• 데이터 품질 보고서를 동료에게 설명한다 |

### 일반적인 자격과 경력

- 데이터 모델링과 데이터 플랫폼 설계에 관한 상당한 경력(석사에 준하는 수준).

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
| 11 | 연구 및 개발에 대한 책임 | 3 | 21 |
| 12 | 행동의 자유 | 5 | 45 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **560** (밴드 8a: 540–584) |

UK GDaD PCF의 등급 제안(밴드 7)보다 높은 밴드에 둔다. 보건 분야 채용 공고는 이 역할을 밴드 8a에 둔다. 이 직무는 많은 서비스가 쓰는 데이터 플랫폼과 통제를 설계하므로, 계획, 정책, 행동의 자유는 밴드 7 수준을 웃돌게 평가했다.

## 밴드 8b: 시니어 데이터 아키텍트

**UK GDaD PCF 수준: Senior data architect**

> A senior data architect delivers the vision for the organisation as set by the chief data architect.
> 
> At this role level, you will:
> - design data models and metadata systems
> - help chief data architects to interpret an organisation’s needs
> - provide oversight and advice to other data architects who are designing and producing data artefacts
> - design and support the management of data dictionaries
> - make sure that your teams are working to the standards set for the organisation by the chief data architects
> - work with technical architects to make sure that an organisation’s systems are designed in accordance with the appropriate data architecture

### 책임

- 공유 돌봄 기록이나 분석 플랫폼 등 주요 영역의 데이터 아키텍처를 설계한다.
- 팀 간 데이터 설계가 조직의 데이터 표준과 모델을 따르도록 한다.
- 표준, 통제, 데이터 공유 계약을 포함하여 파트너 조직과의 데이터 공유 방식을 설계한다.
- 새 설계의 데이터 리스크에 대해 정보 거버넌스 및 임상 안전 동료에게 조언한다.
- 데이터 아키텍트의 업무를 검토하고 이끈다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../스킬/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 실천가 | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Communicating data](../../스킬/#communicating-data) | UK GDaD PCF | 실무 | You can:<br>• understand the appropriate media to communicate findings<br>• shape communications for the audience |
| [Data analysis and synthesis](../../스킬/#data-analysis-and-synthesis) | UK GDaD PCF | 실무 | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../스킬/#data-governance-data-architect) | UK GDaD PCF | 실천가 | You can:<br>• evolve and define data governance<br>• take responsibility for supporting and collaborating around wider governance<br>• assure and integrate data services to meet the needs of multiple business services<br>• work proactively to ensure the organisation designs architecture that considers data |
| [Data innovation](../../스킬/#data-innovation) | UK GDaD PCF | 실무 | You can:<br>• experiment with unfamiliar and emerging technologies, or familiar technologies in new data contexts, with guidance<br>• share what you learn with the team, explaining potential benefits, risks, and practical considerations<br>• identify opportunities to apply technology to improve data processes or outcomes in an operational setting or the wider organisation |
| [Data modelling](../../스킬/#data-modelling) | UK GDaD PCF | 실천가 | You can:<br>• produce relevant data models across multiple subject areas<br>• explain which models to use for which purpose<br>• understand industry-recognised data modelling patterns and standards, and when to apply them<br>• compare and align different data models |
| [Data standards](../../스킬/#data-standards) | UK GDaD PCF | 실천가 | You can:<br>• create data standards for different subjects and ensure senior leaders understand them<br>• work with subject matter experts across the organisation to introduce data standards best practice<br>• monitor compliance with policies and standards in the organisation<br>• make recommendations about how the organisation should resolve breaches of standards |
| [Metadata management](../../스킬/#metadata-management) | UK GDaD PCF | 실천가 | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../스킬/#problem-management) | UK GDaD PCF | 실천가 | You can:<br>• ensure that the right actions are taken to investigate, resolve and anticipate problems<br>• co-ordinate the team to investigate problems, implement solutions and take preventive measures |
| [Strategic thinking](../../스킬/#strategic-thinking) | UK GDaD PCF | 실무 | You can:<br>• work within a strategic context and communicate how activities meet strategic goals<br>• contribute to the development of strategy and policies |
| [Turning business problems into data design](../../스킬/#turning-business-problems-into-data-design) | UK GDaD PCF | 실천가 | You can:<br>• design data architecture that deals with problems spanning different business areas<br>• identify links between problems to devise common solutions<br>• work across multiple subject areas, or a single large or complicated subject area<br>• produce appropriate patterns |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 서비스가 조직 간 돌봄 경로에 어떻게 들어맞는지 분석한다<br>• 임상의, 돌봄 직원, 환자와 협력하여 디지털 서비스를 형성한다<br>• 디지털 결정이 돌봄, 안전, 직원 업무량에 미치는 영향을 설명한다 |
| [임상 용어와 분류](../../스킬/#임상-용어와-분류) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 임상 용어 체계를 사용하여 데이터 모델과 참조 세트를 설계한다<br>• 용어 체계와 분류 사이를 매핑하고 매핑의 한계를 설명한다<br>• 프로덕트와 분석에서의 용어 사용에 대해 팀에 조언한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• FHIR, HL7 버전 2, 메시징 패턴을 사용해 연동을 설계하고 구축한다<br>• FHIR 리소스와 구현 가이드를 작성하고 프로파일링한다<br>• 시스템 간의 복잡한 매핑과 데이터 품질 문제를 해결한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [데이터 품질 관리](../../스킬/#데이터-품질-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 데이터 품질 규칙과 지표를 정의한다<br>• 데이터 제공처와 협력해 품질 저하의 근본 원인을 수정한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |
| [피플 매니지먼트](../../스킬/#피플-매니지먼트) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 일상 업무를 감독하고 피드백을 준다<br>• 채용과 입사 교육에 참여한다<br>• 정기적으로 1대1 면담을 한다 |

### 일반적인 자격과 경력

- 복잡한 조직의 데이터 아키텍처에 관한 풍부한 경력.

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
| 2 | 지식, 교육, 경험 | 8 | 240 |
| 3 | 분석 및 판단 기술 | 5 | 60 |
| 4 | 계획 및 조직화 기술 | 4 | 42 |
| 5 | 신체 기술 | 2 | 15 |
| 6 | 환자·이용자 돌봄에 대한 책임 | 1 | 4 |
| 7 | 정책 및 서비스 개발에 대한 책임 | 4 | 32 |
| 8 | 재무 및 물적 자원에 대한 책임 | 3 | 21 |
| 9 | 사람에 대한 책임 | 3 | 21 |
| 10 | 정보 자원에 대한 책임 | 5 | 34 |
| 11 | 연구 및 개발에 대한 책임 | 3 | 21 |
| 12 | 행동의 자유 | 5 | 45 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **613** (밴드 8b: 585–629) |

## 밴드 8c: 최고 데이터 아키텍트

**UK GDaD PCF 수준: Chief data architect**

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

### 책임

- 데이터 전략에 맞춰 조직의 데이터 아키텍처 비전과 로드맵을 정한다.
- 조직의 전사 데이터 모델, 데이터 표준, 데이터 사전을 맡는다.
- 데이터 아키텍처, 리스크, 투자에 대해 경영진과 데이터 거버넌스 기구에 조언한다.
- 조직 간 데이터 표준 및 상호운용성 활동에서 조직을 대표한다.
- 데이터 아키텍처 실천을 이끌고 그 인력을 키운다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../스킬/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 실천가 | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Communicating data](../../스킬/#communicating-data) | UK GDaD PCF | 실천가 | You can:<br>• turn complex data into clear and well understood solutions, which can be acted upon<br>• share data communication skills with the team and organisation<br>• understand and communicate different options, taking into account risks and uncertainties |
| [Data analysis and synthesis](../../스킬/#data-analysis-and-synthesis) | UK GDaD PCF | 실무 | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../스킬/#data-governance-data-architect) | UK GDaD PCF | 전문가 | You can:<br>• ensure data governance supports changes to the organisational strategy<br>• align data governance with wider governance (for example, budget)<br>• assure corporate services by understanding important risks and providing mitigation through assurance mechanisms |
| [Data innovation](../../스킬/#data-innovation) | UK GDaD PCF | 실천가 | You can:<br>• test and evaluate the feasibility of unfamiliar and emerging technologies, or familiar technologies in new data contexts<br>• share what you learn with the organisation, explaining potential benefits, risks, and practical considerations<br>• recommend, design and implement innovative data solutions based on organisation objectives, user needs, and operational constraints |
| [Data modelling](../../스킬/#data-modelling) | UK GDaD PCF | 전문가 | You can:<br>• understand the concepts and principles of data modelling and can produce relevant data models<br>• work across government and industry, recognising opportunities for the reuse and alignment of data models in different organisations<br>• design the method to categorise data models within an organisation |
| [Data standards](../../스킬/#data-standards) | UK GDaD PCF | 전문가 | You can:<br>• create data standards for the organisation<br>• advocate for, and oversee compliance with, data policies and standards<br>• decide where standards need to be set across the organisation, and how to set them in the wider context of government |
| [Metadata management](../../스킬/#metadata-management) | UK GDaD PCF | 전문가 | You can:<br>• identify how metadata repositories can support different areas of the organisation<br>• communicate the value of metadata repositories<br>• set up robust governance processes to keep repositories up to date |
| [Problem management](../../스킬/#problem-management) | UK GDaD PCF | 전문가 | You can:<br>• anticipate problems and defend against them at the right time<br>• understand how a problem fits into the larger picture<br>• identify and describe problems, and help others to describe them<br>• build problem-solving capabilities in others |
| [Strategic thinking](../../스킬/#strategic-thinking) | UK GDaD PCF | 실천가 | You can:<br>• define strategies and policies, providing guidance to others on working in the strategic context<br>• evaluate current strategies to ensure business requirements are being met and exceeded where possible |
| [Turning business problems into data design](../../스킬/#turning-business-problems-into-data-design) | UK GDaD PCF | 전문가 | You can:<br>• design data architecture that deals with problems across the enterprise<br>• work across all organisational subject areas and internal and external programmes |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 보건·돌봄 시스템에 대한 깊은 이해를 바탕으로 조직 전략을 형성한다<br>• 보건·돌봄 파트너와 리더에게 조직을 대표한다<br>• 정책과 서비스 변화가 디지털 서비스와 돌봄에 어떤 영향을 줄지 예측한다 |
| [임상 용어와 분류](../../스킬/#임상-용어와-분류) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 임상 용어 체계를 사용하여 데이터 모델과 참조 세트를 설계한다<br>• 용어 체계와 분류 사이를 매핑하고 매핑의 한계를 설명한다<br>• 프로덕트와 분석에서의 용어 사용에 대해 팀에 조언한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 조직의 상호운용성 표준과 전략을 정한다<br>• 국가 또는 조직 간 표준화 작업을 이끈다<br>• 여러 시스템에 걸친 핵심 연동의 설계를 보증한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 정보 거버넌스 정책과 전략을 정한다<br>• 정보 리스크와 준수에 대해 이사회에 조언한다<br>• 규제 기관과 파트너에게 조직을 대표한다 |
| [데이터 품질 관리](../../스킬/#데이터-품질-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 데이터 품질 규칙과 지표를 정의한다<br>• 데이터 제공처와 협력해 품질 저하의 근본 원인을 수정한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 프로덕트나 변경의 위험 요소 식별과 리스크 평가를 이끈다<br>• 위험 요소 로그와 임상 안전 케이스 보고서를 작성하고 유지한다<br>• 프로덕트 팀과 리스크 통제에 합의하고 그것이 작동하는지 확인한다<br>• 임상 리스크 관리 기준의 적용에 대해 팀에 조언한다 |
| [피플 매니지먼트](../../스킬/#피플-매니지먼트) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 목표를 설정하고 평가를 하며 팀을 직접 관리한다<br>• 웰빙을 지원하고 근태, 실적, 행위를 관리한다<br>• 팀의 육성과 승계를 계획한다 |

### 일반적인 자격과 경력

- 여러 조직에 걸쳐 데이터 아키텍처를 이끈 풍부한 경력.

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
| 2 | 지식, 교육, 경험 | 8 | 240 |
| 3 | 분석 및 판단 기술 | 5 | 60 |
| 4 | 계획 및 조직화 기술 | 5 | 60 |
| 5 | 신체 기술 | 2 | 15 |
| 6 | 환자·이용자 돌봄에 대한 책임 | 1 | 4 |
| 7 | 정책 및 서비스 개발에 대한 책임 | 5 | 45 |
| 8 | 재무 및 물적 자원에 대한 책임 | 3 | 21 |
| 9 | 사람에 대한 책임 | 3 | 21 |
| 10 | 정보 자원에 대한 책임 | 6 | 46 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 5 | 45 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **662** (밴드 8c: 630–674) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
