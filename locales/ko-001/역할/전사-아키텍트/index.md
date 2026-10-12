# 전사 아키텍트

> 이 문서는 일반적인 디지털 헬스케어 조직을 위한 예시용 참조 프로필입니다. 특정 고용주의 공식 직무기술서가 아니며, 직무평가 점수도 공식 평가가 아닙니다.

> 이 글은 AI 어시스턴트가 영어를 한국어로 번역한 것이며, 한국어 원어민의 검토는 아직 받지 않았습니다. 영국 정부 디지털·데이터 전문직 역량 프레임워크(UK GDaD PCF)와 ESCO의 인용문은 영어 그대로 두었습니다.

**직군:** [아키텍처](../../#아키텍처)  
**밴드:** 8a, 8b, 8c, 8d  
**UK GDaD PCF 역할:** [Enterprise architect](https://understand-digital-data-roles-skills.service.gov.uk/role/enterprise-architect/)  
**ESCO 직업:** [enterprise architect](http://data.europa.eu/esco/occupation/2bef94db-0088-4507-982a-2ca717529adb) (ISCO-08 2511)

## 개요

전사 아키텍트는 조직의 서비스, 정보, 애플리케이션, 기술을 조망하고, 이를 활용해 보건·돌봄 전략을 일관된 변화 계획으로 바꾼다. 아키텍처 원칙, 기준, 로드맵을 정하고 투자 결정을 이끌며, 디지털 변화가 조직 전반에서 환자 안전과 연계된 돌봄을 뒷받침하도록 한다.

## 디지털 헬스케어 조직에서

- 돌봄 경로는 여러 조직과 시스템에 걸쳐 있으므로, 아키텍처는 경계를 넘나드는 기록, 결과, 의뢰서의 공유를 뒷받침해야 한다.
- 기존 자산에는 변경하기 어려운 오래된 임상 시스템, 의료기기, 공급자 계약이 포함되는 경우가 많아, 로드맵은 이행을 신중하게 계획해야 한다.
- 아키텍처 결정은 환자 안전, 프라이버시, 밤낮없이 운영되는 서비스의 복원력에 영향을 준다.
- HL7 FHIR, SNOMED CT, IHE 프로파일 같은 개방형 표준은 종속을 피하고 상호운용성을 실현하는 데 핵심이다.
- 자금은 한정되어 있고 엄격히 심사되므로, 아키텍트는 비용 효율과 기존 공용 플랫폼의 재사용을 보여 주어야 한다.

## UK GDaD PCF 역할 설명(원문은 영어)

> Enterprise architects are leaders working across different levels within an organisation to translate the business strategy into business change and technical delivery.
> 
> In this role, you will:
> - identify priorities for change to enable delivery at pace
> - lead and influence the delivery of cross-cutting capabilities that enable change
> - own the enterprise architecture vision, strategy and roadmaps from a business, technology and data perspective, including ‘as is’, ‘to be’ and transitional states
> - consult and support collaboration across the business
> - understand the organisation’s ecosystem and its interdependencies, including reference architectures
> - take a strategic view across all architectural domains, portfolios and programmes
> - guide the organisation to make appropriate business, technology and data decisions by recommending reuse, sustainability and scalability, to achieve value for money and reduce risk
> - establish architectural principles, policies and standards
> - collaborate and consult with stakeholders to assure business, technology and data decisions are aligned with enterprise architecture strategy
> - develop the architecture community
> - carry out horizon scanning across industry, identifying emerging trends and their potential impact and opportunity for the organisation

## 역할 수준

| 밴드 | 직함 | UK GDaD PCF 수준 | 영국 공무원 등급 | 직무평가 점수 |
| --- | --- | --- | --- | --- |
| 8a | [전사 아키텍트](#밴드-8a-전사-아키텍트) | Enterprise architect | HEO/SEO | 560 |
| 8b | [시니어 전사 아키텍트](#밴드-8b-시니어-전사-아키텍트) | Senior enterprise architect | SEO/G7 | 622 |
| 8c | [리드 전사 아키텍트](#밴드-8c-리드-전사-아키텍트) | Lead enterprise architect | G7/G6 | 658 |
| 8d | [프린시펄 전사 아키텍트](#밴드-8d-프린시펄-전사-아키텍트) | Principal enterprise architect | G6 | 703 |

## 밴드 8a: 전사 아키텍트

**UK GDaD PCF 수준: Enterprise architect**

> An enterprise architect supports other architects in developing the strategy.
> 
> At this role level, you will:
> - network and communicate with stakeholders across domains or enterprises, and identify opportunities for improvement
> - use best practice
> - use emerging technologies and approaches
> - learn to identify influences or risks
> - play a part in successful delivery of the team’s objectives

### 책임

- 진단이나 지역사회 돌봄 등 한 영역에 대해 조직의 현재와 목표 서비스, 정보, 애플리케이션, 기술을 모델링한다.
- 애플리케이션과 데이터 흐름 카탈로그를 포함하여 아키텍처 저장소를 최신으로 유지한다.
- 제안을 아키텍처 원칙과 기준에 비추어 검토하고 설계 기구에 권고한다.
- 시스템이 기능을 중복하는 곳이나 지원되지 않는 기술에 의존하는 곳을 찾아 리스크를 제기한다.
- 솔루션 아키텍트, 임상 리드와 협력하여 돌봄 경로가 시스템을 어떻게 쓰는지 이해한다.
- 설계가 영역의 아키텍처에 어떻게 맞는지에 대해 솔루션 아키텍트를 이끈다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../스킬/#architect-for-the-whole-context) | UK GDaD PCF | 실천가 | You can:<br>• work to support wider organisational objectives beyond your immediate goals​<br>• track emerging internal and external issues over time that could affect the work of teams across the organisation<br>• take action to solve or mitigate problems by influencing colleagues across the organisation |
| [Architecture communication](../../스킬/#architecture-communication) | UK GDaD PCF | 실천가 | You can:<br>• lead the communication of complicated, complex or risky architecture topics with technical and non-technical stakeholders<br>• communicate with senior stakeholders across your organisation<br>• adapt your message and communication techniques to your audience<br>• advocate on behalf of a team to other stakeholders<br>• manage stakeholder expectations effectively |
| [Commercial perspective](../../스킬/#commercial-perspective) | UK GDaD PCF | 실무 | You can:<br>• understand commercial processes and the appropriate internal contacts within a government department<br>• understand different sourcing strategies and when to apply them |
| [Community collaboration](../../스킬/#community-collaboration) | UK GDaD PCF | 실무 | You can:<br>• contribute to the work of others<br>• motivate and empower teams<br>• create the right environment for teams to work in, and can identify the best team makeup depending on the situation<br>• recognise and deal with issues |
| [Enterprise architecture](../../스킬/#enterprise-architecture) | UK GDaD PCF | 실무 | You can:<br>• turn an organisation's goals into clear objectives, with limited direction<br>• design an architecture that defines the technology, people, process and other elements needed to achieve organisation objectives, with support |
| [Making architectural decisions](../../스킬/#making-architectural-decisions) | UK GDaD PCF | 실무 | You can:<br>• work with others to make architectural design decisions characterised by managed levels of risk and complexity<br>• identify and address architectural risks relevant to your team or domain, for example, business, data, or security<br>• engage with architectural governance and assurance to effectively manage decisions and risks, with support |
| [Problem definition and shaping](../../스킬/#problem-definition-and-shaping) | UK GDaD PCF | 실무 | You can:<br>• help to frame a problem characterised by managed levels of complexity, complication, or risk so that a solution can be created<br>• help to create options for solving problems at an appropriate level of detail |
| [Strategy design](../../스킬/#strategy-design) | UK GDaD PCF | 실무 | You can:<br>• support the development of a strategy or vision that aligns with organisational objectives<br>• challenge requirements and assumptions, and identify opportunities to develop strategy<br>• support the implementation of a strategy or vision, for example, by using a roadmap or plan<br>• use architectural principles, patterns, and constraints when appropriate |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 서비스가 조직 간 돌봄 경로에 어떻게 들어맞는지 분석한다<br>• 임상의, 돌봄 직원, 환자와 협력하여 디지털 서비스를 형성한다<br>• 디지털 결정이 돌봄, 안전, 직원 업무량에 미치는 영향을 설명한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• FHIR, HL7 버전 2, 메시징 패턴을 사용해 연동을 설계하고 구축한다<br>• FHIR 리소스와 구현 가이드를 작성하고 프로파일링한다<br>• 시스템 간의 복잡한 매핑과 데이터 품질 문제를 해결한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |
| [조직 리스크 관리](../../스킬/#조직-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자기 영역의 리스크를 기록하고 갱신한다<br>• 통제 방안을 제안하고 대응을 추적한다 |

### 일반적인 자격과 경력

- 복잡한 조직에서의 아키텍처, 분석, 또는 기술 설계에 관한 상당한 경력(석사에 준하는 수준).
- TOGAF 같은 전사 아키텍처 프레임워크에 대한 지식, 또는 그에 준하는 경력.

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

UK GDaD PCF의 등급 제안(밴드 6)보다 높은 밴드에 둔다. 보건 분야 채용 공고는 이 역할을 밴드 8a에 둔다. 이 직무는 영역 전체의 목표 아키텍처를 형성하고 설계 기구에 조언하므로, 지식, 분석, 계획, 정책, 행동의 자유는 밴드 8a 수준으로 평가했다.

## 밴드 8b: 시니어 전사 아키텍트

**UK GDaD PCF 수준: Senior enterprise architect**

> A senior enterprise architect supports lead architects in ensuring the strategy is developed, agreed and followed.
> 
> At this role level, you will:
> - network and communicate with stakeholders across domains or enterprises
> - identify opportunities for improvement
> - support a community or team
> - use best practice
> - use emerging technologies and approaches
> - play an active part in the team and understand how to deliver the team’s objectives to meet organisational goals
> - identify influences or risks
> - play a part in successful delivery of the long-term strategy

### 책임

- 조직의 하나 이상의 영역에 대한 목표 아키텍처와 이행 로드맵을 수립한다.
- 투자가 목표 아키텍처에 맞고 공용 플랫폼을 재사용하도록 비즈니스 케이스를 형성한다.
- 설계 기구에서 아키텍처 리뷰를 이끌고 핵심 제안에 대해 권고한다.
- 데이터 이전과 안전 리스크를 포함하여 오래된 임상·업무 시스템의 교체나 폐기를 계획한다.
- 상호운용성, 보안, 정보 거버넌스 요구가 로드맵에 반영되도록 한다.
- 전사 아키텍트와 솔루션 아키텍트를 코칭하고 이끈다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../스킬/#architect-for-the-whole-context) | UK GDaD PCF | 실천가 | You can:<br>• work to support wider organisational objectives beyond your immediate goals​<br>• track emerging internal and external issues over time that could affect the work of teams across the organisation<br>• take action to solve or mitigate problems by influencing colleagues across the organisation |
| [Architecture communication](../../스킬/#architecture-communication) | UK GDaD PCF | 실천가 | You can:<br>• lead the communication of complicated, complex or risky architecture topics with technical and non-technical stakeholders<br>• communicate with senior stakeholders across your organisation<br>• adapt your message and communication techniques to your audience<br>• advocate on behalf of a team to other stakeholders<br>• manage stakeholder expectations effectively |
| [Commercial perspective](../../스킬/#commercial-perspective) | UK GDaD PCF | 실무 | You can:<br>• understand commercial processes and the appropriate internal contacts within a government department<br>• understand different sourcing strategies and when to apply them |
| [Community collaboration](../../스킬/#community-collaboration) | UK GDaD PCF | 실천가 | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Enterprise architecture](../../스킬/#enterprise-architecture) | UK GDaD PCF | 실천가 | You can:<br>• design an architecture that defines the technology, people, process and other elements needed to achieve organisation objectives<br>• work with others across the organisation to ensure your design is used to achieve the organisation’s objectives |
| [Making architectural decisions](../../스킬/#making-architectural-decisions) | UK GDaD PCF | 실천가 | You can:<br>• make and guide architectural design decisions characterised by medium risk and complexity<br>• identify and address architectural risks that affect multiple teams or domains<br>• use architectural governance and assurance to make design decisions and manage technical risks at the appropriate level<br>• contribute to the development of architectural governance and assurance |
| [Problem definition and shaping](../../스킬/#problem-definition-and-shaping) | UK GDaD PCF | 실천가 | You can:<br>• frame a problem characterised by medium complexity, complication, or risk so that a solution can be created<br>• produce architectural representations that enable different teams to have a shared understanding of problems throughout the life cycle<br>• describe options for solving problems so that appropriate delivery methods can be decided |
| [Strategy design](../../스킬/#strategy-design) | UK GDaD PCF | 실천가 | You can:<br>• define strategies or visions across teams that align with organisational objectives<br>• direct the implementation of a strategy or vision, for example, by creating roadmaps or plans<br>• define architectural principles and patterns<br>• develop or maintain strategy in response to feedback and findings |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 서비스가 조직 간 돌봄 경로에 어떻게 들어맞는지 분석한다<br>• 임상의, 돌봄 직원, 환자와 협력하여 디지털 서비스를 형성한다<br>• 디지털 결정이 돌봄, 안전, 직원 업무량에 미치는 영향을 설명한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• FHIR, HL7 버전 2, 메시징 패턴을 사용해 연동을 설계하고 구축한다<br>• FHIR 리소스와 구현 가이드를 작성하고 프로파일링한다<br>• 시스템 간의 복잡한 매핑과 데이터 품질 문제를 해결한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |
| [조직 리스크 관리](../../스킬/#조직-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자기 영역의 리스크를 기록하고 갱신한다<br>• 통제 방안을 제안하고 대응을 추적한다 |

### 일반적인 자격과 경력

- 여러 영역에 걸친 전사 또는 솔루션 아키텍처의 풍부한 경력.
- TOGAF 같은 전사 아키텍처 프레임워크에 대한 지식, 또는 그에 준하는 경력.

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
| 4 | 계획 및 조직화 기술 | 5 | 60 |
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
| | **합계** | | **622** (밴드 8b: 585–629) |

UK GDaD PCF의 등급 제안(밴드 7)보다 높은 밴드에 둔다. 보건 분야 채용 공고는 이 역할을 밴드 8b에 둔다. 계획은 조직 전체에 영향을 주는 장기 로드맵이므로 레벨 5, 지식은 비즈니스, 정보, 애플리케이션, 기술 아키텍처에 걸친 지식이므로 레벨 8로 한다.

## 밴드 8c: 리드 전사 아키텍트

**UK GDaD PCF 수준: Lead enterprise architect**

> A lead enterprise architect plays a high level role in ensuring the strategy is developed, agreed and followed.
> 
> At this role level, you will:
> - network and communicate with senior stakeholders across enterprises, and seek opportunities for improvement
> - support at least one community or team, or a combination of both
> - find and use best practice and emerging technologies and approaches
> - lead teams including enterprise architects and help them understand how to deliver the team’s objectives to meet organisational goals
> - horizon scan for influences or risks
> - support successful delivery of the long-term strategy
> - take a leading role in the overall direction of business and digital capabilities

### 책임

- 임상 시스템과 공용 인프라 등 조직의 주요 부분의 전사 아키텍처를 맡는다.
- 아키텍처 설계 기구를 주재하거나 이끌고 프로젝트가 충족해야 할 기준을 정한다.
- 투자 우선순위, 공급자 전략, 기술 리스크에 대해 디렉터에게 조언한다.
- 파트너 조직과 협력하여 돌봄 경로와 공유 기록에 걸친 아키텍처를 일치시킨다.
- 전사 아키텍트를 이끌고 육성하며 아키텍처 실천 공동체를 키운다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../스킬/#architect-for-the-whole-context) | UK GDaD PCF | 전문가 | You can:<br>• assess how trends in society and industry practices might impact the organisation<br>• work with people outside of your organisation to inform policies, strategies and standards<br>• anticipate changes to policy and build resilience through your architectural work<br>• coach others in identifying important trends |
| [Architecture communication](../../스킬/#architecture-communication) | UK GDaD PCF | 전문가 | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Commercial perspective](../../스킬/#commercial-perspective) | UK GDaD PCF | 실천가 | You can:<br>• identify appropriate contractual frameworks and approaches<br>• identify, evaluate and select appropriate suppliers |
| [Community collaboration](../../스킬/#community-collaboration) | UK GDaD PCF | 실천가 | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Enterprise architecture](../../스킬/#enterprise-architecture) | UK GDaD PCF | 실천가 | You can:<br>• design an architecture that defines the technology, people, process and other elements needed to achieve organisation objectives<br>• work with others across the organisation to ensure your design is used to achieve the organisation’s objectives |
| [Making architectural decisions](../../스킬/#making-architectural-decisions) | UK GDaD PCF | 실천가 | You can:<br>• make and guide architectural design decisions characterised by medium risk and complexity<br>• identify and address architectural risks that affect multiple teams or domains<br>• use architectural governance and assurance to make design decisions and manage technical risks at the appropriate level<br>• contribute to the development of architectural governance and assurance |
| [Problem definition and shaping](../../스킬/#problem-definition-and-shaping) | UK GDaD PCF | 전문가 | You can:<br>• lead the framing of a problem characterised by high complexity, complication, or risk so that a solution can be created<br>• coach others in defining problems and describing appropriate options for solutions<br>• help others challenge requirements and assumptions, and identify opportunities when defining problems and solution options |
| [Strategy design](../../스킬/#strategy-design) | UK GDaD PCF | 전문가 | You can:<br>• define and connect strategies or visions across the organisation or wider government<br>• enable the implementation of strategies or visions across the organisation or wider government, for example, by advocating for resources and removing blockers |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 서비스가 조직 간 돌봄 경로에 어떻게 들어맞는지 분석한다<br>• 임상의, 돌봄 직원, 환자와 협력하여 디지털 서비스를 형성한다<br>• 디지털 결정이 돌봄, 안전, 직원 업무량에 미치는 영향을 설명한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• FHIR, HL7 버전 2, 메시징 패턴을 사용해 연동을 설계하고 구축한다<br>• FHIR 리소스와 구현 가이드를 작성하고 프로파일링한다<br>• 시스템 간의 복잡한 매핑과 데이터 품질 문제를 해결한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 프로덕트나 변경의 위험 요소 식별과 리스크 평가를 이끈다<br>• 위험 요소 로그와 임상 안전 케이스 보고서를 작성하고 유지한다<br>• 프로덕트 팀과 리스크 통제에 합의하고 그것이 작동하는지 확인한다<br>• 임상 리스크 관리 기준의 적용에 대해 팀에 조언한다 |
| [조직 리스크 관리](../../스킬/#조직-리스크-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 디렉터레이트나 프로그램의 리스크 프로세스를 운영한다<br>• 리스크를 리스크 선호도에 비추어 평가하고 상위에 보고한다<br>• 리스크를 위원회에 보고한다 |
| [피플 매니지먼트](../../스킬/#피플-매니지먼트) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 목표를 설정하고 평가를 하며 팀을 직접 관리한다<br>• 웰빙을 지원하고 근태, 실적, 행위를 관리한다<br>• 팀의 육성과 승계를 계획한다 |
| [예산 관리](../../스킬/#예산-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 작은 예산에 대한 지출을 추적하고 차이를 알린다<br>• 자신의 한도 안에서 지출을 승인한다 |

### 일반적인 자격과 경력

- 복잡한 조직에서의 전사 아키텍처에 관한 풍부한 경력.

### 밴드 개요

- **지식:** 전문 지식에 더해 더 넓은 조직과 분야에 대한 이해.
- **자율성:** 기능의 전략을 정하고 디렉터에게 책임을 진다.
- **범위:** 기능 또는 부문.
- **리더십:** 여러 관리 계층을 통해 기능을 이끈다.
- **책무:** 기능의 성과, 인력, 예산.

### 직무평가(예시)

| # | 요소 | 수준 | 점수 |
| --- | --- | --- | --- |
| 1 | 의사소통 및 관계 형성 기술 | 5 | 45 |
| 2 | 지식, 교육, 경험 | 8 | 240 |
| 3 | 분석 및 판단 기술 | 5 | 60 |
| 4 | 계획 및 조직화 기술 | 5 | 60 |
| 5 | 신체 기술 | 2 | 15 |
| 6 | 환자·이용자 돌봄에 대한 책임 | 1 | 4 |
| 7 | 정책 및 서비스 개발에 대한 책임 | 5 | 45 |
| 8 | 재무 및 물적 자원에 대한 책임 | 3 | 21 |
| 9 | 사람에 대한 책임 | 4 | 32 |
| 10 | 정보 자원에 대한 책임 | 6 | 46 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 5 | 45 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **658** (밴드 8c: 630–674) |

UK GDaD PCF의 등급 제안(밴드 8b)보다 높은 밴드에 둔다. 보건 분야 채용 공고는 이 역할을 밴드 8c에 둔다. 정보 자원은 조직의 주요 부분의 정보 시스템 아키텍처를 관리하므로 레벨 6으로 한다. 모든 프로젝트의 기준을 정하고 전사 아키텍트를 이끌므로, 정책과 사람은 밴드 8b 수준을 웃돈다.

## 밴드 8d: 프린시펄 전사 아키텍트

**UK GDaD PCF 수준: Principal enterprise architect**

> A principal enterprise architect leads at the highest level and is responsible for ensuring the strategy is developed, agreed and followed.
> 
> At this role level, you will:
> - network and communicate with senior stakeholders across enterprises, and actively seek opportunities for improvement
> - support multiple communities and teams
> - find and use best practice
> - find and use emerging technologies and approaches
> - inspire other enterprise architects and help them understand how to meet organisational goals
> - horizon scan for external influences or risks
> - support successful delivery of the long-term strategy
> - be responsible for the overall direction of business and digital capabilities
> - be responsible for the creation, maintenance and consumption of a Digital Twin

### 책임

- 보건·돌봄 전략에 맞춰 조직의 전사 아키텍처 비전, 원칙, 전략을 정한다.
- 주요 디지털 투자의 아키텍처, 리스크, 가치에 대해 경영진과 이사회에 조언한다.
- 조직의 아키텍처 실천, 거버넌스, 기준을 이끈다.
- 조직 간 아키텍처 및 상호운용성 포럼에서 조직을 대표한다.
- 채용과 경력 경로를 포함하여 조직 전체의 아키텍처 역량을 키운다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../스킬/#architect-for-the-whole-context) | UK GDaD PCF | 전문가 | You can:<br>• assess how trends in society and industry practices might impact the organisation<br>• work with people outside of your organisation to inform policies, strategies and standards<br>• anticipate changes to policy and build resilience through your architectural work<br>• coach others in identifying important trends |
| [Architecture communication](../../스킬/#architecture-communication) | UK GDaD PCF | 전문가 | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Commercial perspective](../../스킬/#commercial-perspective) | UK GDaD PCF | 실천가 | You can:<br>• identify appropriate contractual frameworks and approaches<br>• identify, evaluate and select appropriate suppliers |
| [Community collaboration](../../스킬/#community-collaboration) | UK GDaD PCF | 전문가 | You can:<br>• solve and unblock issues between teams or departments at the highest level<br>• coach the organisation on team dynamics and conflict resolution, while also building and growing the community |
| [Enterprise architecture](../../스킬/#enterprise-architecture) | UK GDaD PCF | 전문가 | You can:<br>• lead others designing architectures defining the technology, people, process and other elements needed to achieve organisation objectives<br>• work with others beyond the organisation to influence organisational structures, technology, people and processes to achieve objectives<br>• ensure organisation-wide changes align with the architectural strategy |
| [Making architectural decisions](../../스킬/#making-architectural-decisions) | UK GDaD PCF | 전문가 | You can:<br>• make and guide architectural design decisions characterised by high levels of risk and complexity<br>• identify and address architectural risks across the organisation or wider government<br>• lead and evolve architectural governance and assurance<br>• represent architectural governance as part of wider governance, for example, legal or commercial |
| [Problem definition and shaping](../../스킬/#problem-definition-and-shaping) | UK GDaD PCF | 전문가 | You can:<br>• lead the framing of a problem characterised by high complexity, complication, or risk so that a solution can be created<br>• coach others in defining problems and describing appropriate options for solutions<br>• help others challenge requirements and assumptions, and identify opportunities when defining problems and solution options |
| [Strategy design](../../스킬/#strategy-design) | UK GDaD PCF | 전문가 | You can:<br>• define and connect strategies or visions across the organisation or wider government<br>• enable the implementation of strategies or visions across the organisation or wider government, for example, by advocating for resources and removing blockers |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 보건·돌봄 시스템에 대한 깊은 이해를 바탕으로 조직 전략을 형성한다<br>• 보건·돌봄 파트너와 리더에게 조직을 대표한다<br>• 정책과 서비스 변화가 디지털 서비스와 돌봄에 어떤 영향을 줄지 예측한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 조직의 상호운용성 표준과 전략을 정한다<br>• 국가 또는 조직 간 표준화 작업을 이끈다<br>• 여러 시스템에 걸친 핵심 연동의 설계를 보증한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 정보 거버넌스 정책과 전략을 정한다<br>• 정보 리스크와 준수에 대해 이사회에 조언한다<br>• 규제 기관과 파트너에게 조직을 대표한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 프로덕트나 변경의 위험 요소 식별과 리스크 평가를 이끈다<br>• 위험 요소 로그와 임상 안전 케이스 보고서를 작성하고 유지한다<br>• 프로덕트 팀과 리스크 통제에 합의하고 그것이 작동하는지 확인한다<br>• 임상 리스크 관리 기준의 적용에 대해 팀에 조언한다 |
| [조직 리스크 관리](../../스킬/#조직-리스크-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 디렉터레이트나 프로그램의 리스크 프로세스를 운영한다<br>• 리스크를 리스크 선호도에 비추어 평가하고 상위에 보고한다<br>• 리스크를 위원회에 보고한다 |
| [피플 매니지먼트](../../스킬/#피플-매니지먼트) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 매니저를 이끌고 큰 영역의 문화를 형성한다<br>• 인력 계획과 조직 변경을 설계한다<br>• 리더를 코칭하고 복잡한 사람 문제를 해결한다 |
| [예산 관리](../../스킬/#예산-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 예산을 보유하고 관리하며, 차이를 예측하고 설명한다<br>• 비용과 편익을 보여 주는 비즈니스 케이스를 작성한다 |

### 일반적인 자격과 경력

- 여러 조직에 걸쳐 전사 아키텍처를 이끈 풍부한 경력.

### 밴드 개요

- **지식:** 여러 기능과 더 넓은 보건·돌봄 시스템에 걸친 전략적 지식.
- **자율성:** 조직 전체의 전략을 만들고 디렉터를 대리한다.
- **범위:** 주요 기능 또는 여러 기능.
- **리더십:** 여러 기능 또는 큰 부문을 이끈다.
- **책무:** 주요 기능, 큰 예산, 조직 전체의 리스크.

### 직무평가(예시)

| # | 요소 | 수준 | 점수 |
| --- | --- | --- | --- |
| 1 | 의사소통 및 관계 형성 기술 | 6 | 60 |
| 2 | 지식, 교육, 경험 | 8 | 240 |
| 3 | 분석 및 판단 기술 | 5 | 60 |
| 4 | 계획 및 조직화 기술 | 5 | 60 |
| 5 | 신체 기술 | 2 | 15 |
| 6 | 환자·이용자 돌봄에 대한 책임 | 1 | 4 |
| 7 | 정책 및 서비스 개발에 대한 책임 | 6 | 60 |
| 8 | 재무 및 물적 자원에 대한 책임 | 3 | 21 |
| 9 | 사람에 대한 책임 | 4 | 32 |
| 10 | 정보 자원에 대한 책임 | 6 | 46 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 6 | 60 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **703** (밴드 8d: 675–720) |

UK GDaD PCF의 등급 제안(밴드 8c)보다 높은 밴드에 둔다. 보건 분야 채용 공고는 이 역할을 밴드 8d에 둔다. 이 직무는 조직의 아키텍처 비전, 원칙, 전략에 대한 조직 전체의 책임을 지므로, 정책과 행동의 자유는 레벨 6으로 한다.


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
