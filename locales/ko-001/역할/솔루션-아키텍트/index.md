# 솔루션 아키텍트

> 이 문서는 일반적인 디지털 헬스케어 조직을 위한 예시용 참조 프로필입니다. 특정 고용주의 공식 직무기술서가 아니며, 직무평가 점수도 공식 평가가 아닙니다.

> 이 글은 AI 어시스턴트가 영어를 한국어로 번역한 것이며, 한국어 원어민의 검토는 아직 받지 않았습니다. 영국 정부 디지털·데이터 전문직 역량 프레임워크(UK GDaD PCF)와 ESCO의 인용문은 영어 그대로 두었습니다.

**직군:** [아키텍처](../../#아키텍처)  
**밴드:** 7, 8a, 8b, 8c, 8d  
**UK GDaD PCF 역할:** [Solution architect](https://understand-digital-data-roles-skills.service.gov.uk/role/solution-architect/)  
**ESCO 직업:** [ICT system architect](http://data.europa.eu/esco/occupation/e1c72b5f-4c5c-487c-a6df-e84b64a51dae) (ISCO-08 2511)

## 개요

솔루션 아키텍트는 새로 만들거나 바뀌는 서비스가 이용자의 요구와 임상 워크플로에서부터 애플리케이션, 데이터, 연동, 호스팅, 보안까지 처음부터 끝까지 어떻게 작동하는지 설계한다. 각 솔루션이 조직의 아키텍처에 맞고, 안전성, 프라이버시, 상호운용성 요구를 충족하며, 합리적인 비용으로 구축, 운영, 지원할 수 있도록 한다.

## 디지털 헬스케어 조직에서

- 솔루션은 구매한 임상 시스템, 자체 개발한 서비스, 공용 플랫폼을 조합하는 경우가 많으므로, 아키텍트는 공급자 경계를 넘어 설계해야 한다.
- 설계상의 선택은 결과 누락이나 환자 오매칭 같은 임상 위험 요소를 만들 수 있으므로, 솔루션 설계는 임상 안전 케이스에 반영된다.
- 환자 정보의 새로운 데이터 흐름에는 적법한 근거와 개인정보 영향평가가 필요하므로, 아키텍트는 정보 거버넌스와 긴밀히 협력한다.
- HL7 FHIR 같은 표준을 활용한 다른 보건·돌봄 조직과의 상호운용성은 대개 핵심 요구사항이다.
- 일부 솔루션에는 의료기기에 해당하는 소프트웨어가 포함되며, 이는 설계, 보증, 공급자에 대한 요구사항을 바꾼다.

## UK GDaD PCF 역할 설명(원문은 영어)

> A solution architect designs solutions for problems that affect the organisation.
> 
> In this role, you will:
> - ensure a problem and the desired outcomes are properly defined
> - ensure the scope of a solution meets the organisation's requirements
> - stay up to date on technology trends and approaches
> - understand organisational objectives and external drivers, for example, legislation or financial constraints
> - work with others to develop business and technical strategies
> - work within business and technical constraints
> - design and document solutions so they can be implemented by the organisation
> - comply with standards and governance
> - communicate and work effectively with stakeholders
> - manage risks and decisions in a transparent way

## 역할 수준

| 밴드 | 직함 | UK GDaD PCF 수준 | 영국 공무원 등급 | 직무평가 점수 |
| --- | --- | --- | --- | --- |
| 7 | [어소시에이트 솔루션 아키텍트](#밴드-7-어소시에이트-솔루션-아키텍트) | Associate solution architect | HEO/SEO | 483 |
| 8a | [솔루션 아키텍트](#밴드-8a-솔루션-아키텍트) | Solution architect | SEO/G7 | 560 |
| 8b | [시니어 솔루션 아키텍트](#밴드-8b-시니어-솔루션-아키텍트) | Senior solution architect | G7 | 604 |
| 8c | [리드 솔루션 아키텍트](#밴드-8c-리드-솔루션-아키텍트) | Lead solution architect | G7/G6 | 655 |
| 8d | [프린시펄 솔루션 아키텍트](#밴드-8d-프린시펄-솔루션-아키텍트) | Principal solution architect | G6 | 699 |

## 밴드 7: 어소시에이트 솔루션 아키텍트

**UK GDaD PCF 수준: Associate solution architect**

> An associate solution architect supports other solution architects to design solutions. You will usually work under supervision.
> 
> At this role level, you will:
> - support the design of solutions by working with stakeholders
> - help your team achieve its objectives

### 책임

- 프로덕트 팀, 임상의, 공급자로부터 요구사항을 모아 솔루션 설계의 재료로 삼는다.
- 컨텍스트, 데이터 흐름, 연동 다이어그램 등 현재와 목표 상태의 도해를 그린다.
- 감독을 받으며 솔루션 설계 문서와 결정 기록의 일부를 작성한다.
- 설계를 아키텍처 기준과 보안·정보 거버넌스 요구사항에 비추어 점검한다.
- 설계가 설계 기구의 검토를 받을 준비를 돕는다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../스킬/#architect-for-the-whole-context) | UK GDaD PCF | 인지 | You can:<br>• identify relevant information that can inform your architectural work, such as strategies, roadmaps, policies and technical trends<br>• understand how your work supports the team in enabling change​ |
| [Architecture communication](../../스킬/#architecture-communication) | UK GDaD PCF | 실무 | You can:<br>• listen to the needs of technical and business stakeholders<br>• create and use different architecture representations to communicate effectively, achieving agreement with technical and non-technical stakeholders<br>• provide support in discussions about architectural topics within a multidisciplinary team |
| [Commercial perspective](../../스킬/#commercial-perspective) | UK GDaD PCF | 인지 | You can:<br>• show an awareness of government commercial processes<br>• show an awareness of legal and compliance rules |
| [Community collaboration](../../스킬/#community-collaboration) | UK GDaD PCF | 인지 | You can:<br>• understand the work of others and the importance of team dynamics, collaboration and feedback |
| [Making architectural decisions](../../스킬/#making-architectural-decisions) | UK GDaD PCF | 인지 | You can:<br>• describe the reasoning behind architectural design decisions<br>• gather information to inform decisions<br>• understand architectural governance and assurance relevant to your work |
| [Problem definition and shaping](../../스킬/#problem-definition-and-shaping) | UK GDaD PCF | 실무 | You can:<br>• help to frame a problem characterised by managed levels of complexity, complication, or risk so that a solution can be created<br>• help to create options for solving problems at an appropriate level of detail |
| [Strategy design](../../스킬/#strategy-design) | UK GDaD PCF | 인지 | You can:<br>• explain how organisational objectives link to designing strategy<br>• describe the purpose and application of strategy, standards, patterns, policies, roadmaps, vision, and mission statements |
| [Technical design throughout the life cycle](../../스킬/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | 실무 | You can:<br>• create technical designs characterised by managed levels of risk, impact, and complexity<br>• provide guidance and support to teams using technical designs throughout the life cycle<br>• adapt a technical design if needed during delivery<br>• work with well-understood technology and identify appropriate patterns |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자신의 업무가 뒷받침하는 임상 및 돌봄 워크플로를 설명한다<br>• 임상 및 돌봄 동료와 일반적인 의료 용어를 올바르게 사용한다<br>• 변경이 환자 돌봄에 영향을 줄 수 있는 때를 알아보고 제기한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• FHIR 리소스, 프로파일, API를 읽고 사용한다<br>• 지도를 받아 간단한 연동을 구축하거나 테스트한다<br>• 메시지를 사양에 비추어 확인한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |

### 일반적인 자격과 경력

- 솔루션 설계 전문 지식(석사 수준 또는 그에 준하는 경력).
- 분석, 개발, 또는 기술 설계 경력.

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
| 3 | 분석 및 판단 기술 | 5 | 60 |
| 4 | 계획 및 조직화 기술 | 3 | 27 |
| 5 | 신체 기술 | 2 | 15 |
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
| | **합계** | | **483** (밴드 7: 466–539) |

UK GDaD PCF의 등급 제안(밴드 6)보다 높은 밴드에 둔다. 보건 분야 채용 공고는 이 역할을 밴드 7에 둔다. 이 직무는 애플리케이션, 데이터, 연동, 보안에 걸쳐 설계하므로, 지식은 석사 수준 또는 그에 준하는 수준으로 평가했다.

## 밴드 8a: 솔루션 아키텍트

**UK GDaD PCF 수준: Solution architect**

> A solution architect is responsible for a single solution. They usually work independently on solutions where risk is low. They also often support or contribute to work led by more senior solution architects.
> 
> At this role level, you will:
> - build relationships with stakeholders across different business or technical areas in the organisation
> - be proactive in identifying opportunities to improve the organisation
> - follow best practice for solution design
> - use emerging technologies and approaches
> - help your team achieve its objective

### 책임

- 직원용 도구나 단순한 환자용 서비스 등 위험이 낮은 서비스의 엔드투엔드 솔루션을 설계한다.
- 구매, 구축, 공용 플랫폼 재사용을 포함한 선택지를 비교하고 명확한 이유와 함께 하나를 권고한다.
- 표준이 있는 경우 개방형 표준으로 솔루션의 연동, 데이터 흐름, 아이덴티티와 접근을 설계한다.
- 솔루션의 위험 요소 식별과 개인정보 영향평가에 기여한다.
- 설계를 설계 기구에 발표하고 구축과 가동 동안 전달 팀을 지원한다.
- 어소시에이트 솔루션 아키텍트를 코칭하고 그 업무를 검토한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../스킬/#architect-for-the-whole-context) | UK GDaD PCF | 실무 | You can:<br>• align your work with the work being done by other architects and technical professionals<br>• track emerging issues, strategies, roadmaps, patterns and technologies over time to assess opportunities and risks to your work<br>• identify how other teams contribute to delivering outcomes through change |
| [Architecture communication](../../스킬/#architecture-communication) | UK GDaD PCF | 실천가 | You can:<br>• lead the communication of complicated, complex or risky architecture topics with technical and non-technical stakeholders<br>• communicate with senior stakeholders across your organisation<br>• adapt your message and communication techniques to your audience<br>• advocate on behalf of a team to other stakeholders<br>• manage stakeholder expectations effectively |
| [Commercial perspective](../../스킬/#commercial-perspective) | UK GDaD PCF | 실무 | You can:<br>• understand commercial processes and the appropriate internal contacts within a government department<br>• understand different sourcing strategies and when to apply them |
| [Community collaboration](../../스킬/#community-collaboration) | UK GDaD PCF | 실무 | You can:<br>• contribute to the work of others<br>• motivate and empower teams<br>• create the right environment for teams to work in, and can identify the best team makeup depending on the situation<br>• recognise and deal with issues |
| [Making architectural decisions](../../스킬/#making-architectural-decisions) | UK GDaD PCF | 실무 | You can:<br>• work with others to make architectural design decisions characterised by managed levels of risk and complexity<br>• identify and address architectural risks relevant to your team or domain, for example, business, data, or security<br>• engage with architectural governance and assurance to effectively manage decisions and risks, with support |
| [Problem definition and shaping](../../스킬/#problem-definition-and-shaping) | UK GDaD PCF | 실천가 | You can:<br>• frame a problem characterised by medium complexity, complication, or risk so that a solution can be created<br>• produce architectural representations that enable different teams to have a shared understanding of problems throughout the life cycle<br>• describe options for solving problems so that appropriate delivery methods can be decided |
| [Strategy design](../../스킬/#strategy-design) | UK GDaD PCF | 실무 | You can:<br>• support the development of a strategy or vision that aligns with organisational objectives<br>• challenge requirements and assumptions, and identify opportunities to develop strategy<br>• support the implementation of a strategy or vision, for example, by using a roadmap or plan<br>• use architectural principles, patterns, and constraints when appropriate |
| [Technical design throughout the life cycle](../../스킬/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | 실무 | You can:<br>• create technical designs characterised by managed levels of risk, impact, and complexity<br>• provide guidance and support to teams using technical designs throughout the life cycle<br>• adapt a technical design if needed during delivery<br>• work with well-understood technology and identify appropriate patterns |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자신의 업무가 뒷받침하는 임상 및 돌봄 워크플로를 설명한다<br>• 임상 및 돌봄 동료와 일반적인 의료 용어를 올바르게 사용한다<br>• 변경이 환자 돌봄에 영향을 줄 수 있는 때를 알아보고 제기한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• FHIR, HL7 버전 2, 메시징 패턴을 사용해 연동을 설계하고 구축한다<br>• FHIR 리소스와 구현 가이드를 작성하고 프로파일링한다<br>• 시스템 간의 복잡한 매핑과 데이터 품질 문제를 해결한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |
| [아이덴티티 및 접근 관리](../../스킬/#아이덴티티-및-접근-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 사용자 계정과 접근 권한을 생성, 변경, 삭제한다<br>• 접근 권한을 역할 기반 접근 규칙에 비추어 확인한다 |

### 일반적인 자격과 경력

- 솔루션 설계 또는 소프트웨어 엔지니어링에 관한 상당한 경력(석사에 준하는 수준).

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

UK GDaD PCF의 등급 제안(밴드 7)보다 높은 밴드에 둔다. 보건 분야 채용 공고는 이 역할을 밴드 8a에 둔다. 이 직무는 엔드투엔드 설계를 맡고 설계 기구에 선택지를 권고하므로, 계획, 정책, 행동의 자유는 밴드 7 수준을 웃돌게 평가했다.

## 밴드 8b: 시니어 솔루션 아키텍트

**UK GDaD PCF 수준: Senior solution architect**

> A senior solution architect is responsible for a single, more complex, solution. They usually work on solutions where the risk is moderate. They may lead and coach other solution architects.
> 
> At this role level, you will:
> - build relationships with senior stakeholders across different business or technical areas in the organisation
> - be proactive in identifying opportunities to improve the organisation
> - support multiple architecture projects
> - find and use emerging technologies and approaches
> - support others to follow best practice for solution architecture

### 책임

- 임상 시스템이나 여러 조직이 쓰는 서비스 등 위험이 중간 정도인 복잡한 솔루션을 설계한다.
- 상호운용성, 보안, 안전을 포함하여 조달에서 공급자 제품의 기술 평가를 이끈다.
- 솔루션이 밤낮없이 돌봄을 뒷받침하는 경우 복원력과 업무 연속성을 고려해 설계한다.
- 임상 안전 책임자와 협력하여 설계 결정과 리스크 통제가 안전 케이스에 기록되도록 한다.
- 다른 솔루션 아키텍트를 코칭하고 업무를 검토한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../스킬/#architect-for-the-whole-context) | UK GDaD PCF | 실무 | You can:<br>• align your work with the work being done by other architects and technical professionals<br>• track emerging issues, strategies, roadmaps, patterns and technologies over time to assess opportunities and risks to your work<br>• identify how other teams contribute to delivering outcomes through change |
| [Architecture communication](../../스킬/#architecture-communication) | UK GDaD PCF | 실천가 | You can:<br>• lead the communication of complicated, complex or risky architecture topics with technical and non-technical stakeholders<br>• communicate with senior stakeholders across your organisation<br>• adapt your message and communication techniques to your audience<br>• advocate on behalf of a team to other stakeholders<br>• manage stakeholder expectations effectively |
| [Commercial perspective](../../스킬/#commercial-perspective) | UK GDaD PCF | 실무 | You can:<br>• understand commercial processes and the appropriate internal contacts within a government department<br>• understand different sourcing strategies and when to apply them |
| [Community collaboration](../../스킬/#community-collaboration) | UK GDaD PCF | 실천가 | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../스킬/#making-architectural-decisions) | UK GDaD PCF | 실천가 | You can:<br>• make and guide architectural design decisions characterised by medium risk and complexity<br>• identify and address architectural risks that affect multiple teams or domains<br>• use architectural governance and assurance to make design decisions and manage technical risks at the appropriate level<br>• contribute to the development of architectural governance and assurance |
| [Problem definition and shaping](../../스킬/#problem-definition-and-shaping) | UK GDaD PCF | 실천가 | You can:<br>• frame a problem characterised by medium complexity, complication, or risk so that a solution can be created<br>• produce architectural representations that enable different teams to have a shared understanding of problems throughout the life cycle<br>• describe options for solving problems so that appropriate delivery methods can be decided |
| [Strategy design](../../스킬/#strategy-design) | UK GDaD PCF | 실무 | You can:<br>• support the development of a strategy or vision that aligns with organisational objectives<br>• challenge requirements and assumptions, and identify opportunities to develop strategy<br>• support the implementation of a strategy or vision, for example, by using a roadmap or plan<br>• use architectural principles, patterns, and constraints when appropriate |
| [Technical design throughout the life cycle](../../스킬/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | 실천가 | You can:<br>• create technical designs characterised by medium risk, impact, and complexity<br>• maintain appropriate quality and architectural coherence of a technical design in response to change<br>• use feedback to optimise and refine technical designs throughout the life cycle |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 서비스가 조직 간 돌봄 경로에 어떻게 들어맞는지 분석한다<br>• 임상의, 돌봄 직원, 환자와 협력하여 디지털 서비스를 형성한다<br>• 디지털 결정이 돌봄, 안전, 직원 업무량에 미치는 영향을 설명한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• FHIR, HL7 버전 2, 메시징 패턴을 사용해 연동을 설계하고 구축한다<br>• FHIR 리소스와 구현 가이드를 작성하고 프로파일링한다<br>• 시스템 간의 복잡한 매핑과 데이터 품질 문제를 해결한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 프로덕트나 변경의 위험 요소 식별과 리스크 평가를 이끈다<br>• 위험 요소 로그와 임상 안전 케이스 보고서를 작성하고 유지한다<br>• 프로덕트 팀과 리스크 통제에 합의하고 그것이 작동하는지 확인한다<br>• 임상 리스크 관리 기준의 적용에 대해 팀에 조언한다 |
| [아이덴티티 및 접근 관리](../../스킬/#아이덴티티-및-접근-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 사용자 계정과 접근 권한을 생성, 변경, 삭제한다<br>• 접근 권한을 역할 기반 접근 규칙에 비추어 확인한다 |
| [의료기기 소프트웨어 규제](../../스킬/#의료기기-소프트웨어-규제) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 일부 보건 소프트웨어는 의료기기로 규제됨을 설명한다<br>• 제품이 의료기기일 수 있을 때 누구에게 물어야 하는지 안다 |
| [조직 리스크 관리](../../스킬/#조직-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자기 영역의 리스크를 기록하고 갱신한다<br>• 통제 방안을 제안하고 대응을 추적한다 |

### 일반적인 자격과 경력

- 여러 분야에 걸친 복잡한 솔루션 설계의 풍부한 경력(석사를 넘는 수준).

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
| 8 | 재무 및 물적 자원에 대한 책임 | 2 | 12 |
| 9 | 사람에 대한 책임 | 3 | 21 |
| 10 | 정보 자원에 대한 책임 | 5 | 34 |
| 11 | 연구 및 개발에 대한 책임 | 3 | 21 |
| 12 | 행동의 자유 | 5 | 45 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **604** (밴드 8b: 585–629) |

UK GDaD PCF의 등급 제안(밴드 8a)보다 높은 밴드에 둔다. 보건 분야 채용 공고는 이 역할을 밴드 8b에 둔다. 지식은 애플리케이션, 데이터, 연동, 보안, 임상 안전 등 여러 분야에 걸친 전문 지식이므로 레벨 8로 한다.

## 밴드 8c: 리드 솔루션 아키텍트

**UK GDaD PCF 수준: Lead solution architect**

> A lead solution architect is responsible for a group of solution architecture projects, or a single more complex area. They may lead teams of more junior solution architects.
> 
> At this role level, you will:
> - build relationships with senior stakeholders across multiple business or technical areas in the organisation
> - be proactive in identifying opportunities to improve the organisation
> - support multiple architecture projects or programmes
> - find and use emerging technologies and approaches
> - develop best practice for solution architecture

### 책임

- 전자 환자 기록 교체 같은 프로그램 또는 복잡한 영역의 솔루션 아키텍처를 이끈다.
- 프로그램 전체의 솔루션이 일관되고, 상호운용 가능하며, 목표 아키텍처와 일치하도록 한다.
- 설계 리스크, 의존성, 공급자 선택, 비용에 대해 프로그램 위원회에 조언한다.
- 설계 기구에서 다른 솔루션 아키텍트의 설계를 보증한다.
- 솔루션 아키텍트 팀을 이끌고 육성한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../스킬/#architect-for-the-whole-context) | UK GDaD PCF | 실천가 | You can:<br>• work to support wider organisational objectives beyond your immediate goals​<br>• track emerging internal and external issues over time that could affect the work of teams across the organisation<br>• take action to solve or mitigate problems by influencing colleagues across the organisation |
| [Architecture communication](../../스킬/#architecture-communication) | UK GDaD PCF | 전문가 | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Commercial perspective](../../스킬/#commercial-perspective) | UK GDaD PCF | 실천가 | You can:<br>• identify appropriate contractual frameworks and approaches<br>• identify, evaluate and select appropriate suppliers |
| [Community collaboration](../../스킬/#community-collaboration) | UK GDaD PCF | 실천가 | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../스킬/#making-architectural-decisions) | UK GDaD PCF | 실천가 | You can:<br>• make and guide architectural design decisions characterised by medium risk and complexity<br>• identify and address architectural risks that affect multiple teams or domains<br>• use architectural governance and assurance to make design decisions and manage technical risks at the appropriate level<br>• contribute to the development of architectural governance and assurance |
| [Problem definition and shaping](../../스킬/#problem-definition-and-shaping) | UK GDaD PCF | 전문가 | You can:<br>• lead the framing of a problem characterised by high complexity, complication, or risk so that a solution can be created<br>• coach others in defining problems and describing appropriate options for solutions<br>• help others challenge requirements and assumptions, and identify opportunities when defining problems and solution options |
| [Strategy design](../../스킬/#strategy-design) | UK GDaD PCF | 실천가 | You can:<br>• define strategies or visions across teams that align with organisational objectives<br>• direct the implementation of a strategy or vision, for example, by creating roadmaps or plans<br>• define architectural principles and patterns<br>• develop or maintain strategy in response to feedback and findings |
| [Technical design throughout the life cycle](../../스킬/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | 전문가 | You can:<br>• create technical designs characterised by high risk, impact, and complexity<br>• lead and guide others in creating technical designs that achieve organisational objectives<br>• use feedback to optimise and refine standards for technical designs throughout the life cycle |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 서비스가 조직 간 돌봄 경로에 어떻게 들어맞는지 분석한다<br>• 임상의, 돌봄 직원, 환자와 협력하여 디지털 서비스를 형성한다<br>• 디지털 결정이 돌봄, 안전, 직원 업무량에 미치는 영향을 설명한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 조직의 상호운용성 표준과 전략을 정한다<br>• 국가 또는 조직 간 표준화 작업을 이끈다<br>• 여러 시스템에 걸친 핵심 연동의 설계를 보증한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 프로덕트나 변경의 위험 요소 식별과 리스크 평가를 이끈다<br>• 위험 요소 로그와 임상 안전 케이스 보고서를 작성하고 유지한다<br>• 프로덕트 팀과 리스크 통제에 합의하고 그것이 작동하는지 확인한다<br>• 임상 리스크 관리 기준의 적용에 대해 팀에 조언한다 |
| [의료기기 소프트웨어 규제](../../스킬/#의료기기-소프트웨어-규제) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 의료기기 표준을 충족하는 소프트웨어 생애 주기 프로세스를 따른다<br>• 그 프로세스가 요구하는 기록을 작성한다 |
| [조직 리스크 관리](../../스킬/#조직-리스크-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 디렉터레이트나 프로그램의 리스크 프로세스를 운영한다<br>• 리스크를 리스크 선호도에 비추어 평가하고 상위에 보고한다<br>• 리스크를 위원회에 보고한다 |
| [피플 매니지먼트](../../스킬/#피플-매니지먼트) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 목표를 설정하고 평가를 하며 팀을 직접 관리한다<br>• 웰빙을 지원하고 근태, 실적, 행위를 관리한다<br>• 팀의 육성과 승계를 계획한다 |

### 일반적인 자격과 경력

- 복잡한 프로그램의 솔루션 아키텍처를 이끈 풍부한 경력.

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
| 10 | 정보 자원에 대한 책임 | 5 | 34 |
| 11 | 연구 및 개발에 대한 책임 | 3 | 21 |
| 12 | 행동의 자유 | 5 | 45 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **655** (밴드 8c: 630–674) |

UK GDaD PCF의 등급 제안(밴드 8b)보다 높은 밴드에 둔다. 보건 분야 채용 공고는 이 역할을 밴드 8c에 둔다. 이 직무는 프로그램 전체의 아키텍처를 계획하고 솔루션 아키텍트 팀을 이끌므로, 계획, 정책, 사람은 밴드 8b 수준을 웃돌게 평가했다.

## 밴드 8d: 프린시펄 솔루션 아키텍트

**UK GDaD PCF 수준: Principal solution architect**

> A principal solution architect can be responsible for a large programme or group of solution architecture projects, or a single, very complex or critical business area.
> 
> At this role level, you will:
> - lead teams of more junior solution architects
> - lead multiple architecture projects or programmes
> - build relationships with senior stakeholders across multiple business or technical areas in the organisation and its partners
> - be proactive in identifying opportunities to improve the organisation and its partners
> - work with technology partners to inform their roadmaps
> - take a leading role in the overall direction of business and digital capabilities
> - inspire other architects and help them understand how to meet organisational goals

### 책임

- 조직에서 가장 크거나 가장 중요한 프로그램의 솔루션 아키텍처를 이끈다.
- 조직의 솔루션 아키텍처 기준, 패턴, 방법을 정한다.
- 핵심적이고 공유되는 보건·돌봄 서비스의 설계에 대해 디렉터와 파트너 조직에 조언한다.
- 프로그램, 공급자, 파트너 조직 간의 가장 어려운 설계 충돌을 해결한다.
- 솔루션 아키텍처 실천을 이끌고 그 인력을 키운다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../스킬/#architect-for-the-whole-context) | UK GDaD PCF | 전문가 | You can:<br>• assess how trends in society and industry practices might impact the organisation<br>• work with people outside of your organisation to inform policies, strategies and standards<br>• anticipate changes to policy and build resilience through your architectural work<br>• coach others in identifying important trends |
| [Architecture communication](../../스킬/#architecture-communication) | UK GDaD PCF | 전문가 | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Commercial perspective](../../스킬/#commercial-perspective) | UK GDaD PCF | 실천가 | You can:<br>• identify appropriate contractual frameworks and approaches<br>• identify, evaluate and select appropriate suppliers |
| [Community collaboration](../../스킬/#community-collaboration) | UK GDaD PCF | 전문가 | You can:<br>• solve and unblock issues between teams or departments at the highest level<br>• coach the organisation on team dynamics and conflict resolution, while also building and growing the community |
| [Making architectural decisions](../../스킬/#making-architectural-decisions) | UK GDaD PCF | 전문가 | You can:<br>• make and guide architectural design decisions characterised by high levels of risk and complexity<br>• identify and address architectural risks across the organisation or wider government<br>• lead and evolve architectural governance and assurance<br>• represent architectural governance as part of wider governance, for example, legal or commercial |
| [Problem definition and shaping](../../스킬/#problem-definition-and-shaping) | UK GDaD PCF | 전문가 | You can:<br>• lead the framing of a problem characterised by high complexity, complication, or risk so that a solution can be created<br>• coach others in defining problems and describing appropriate options for solutions<br>• help others challenge requirements and assumptions, and identify opportunities when defining problems and solution options |
| [Strategy design](../../스킬/#strategy-design) | UK GDaD PCF | 전문가 | You can:<br>• define and connect strategies or visions across the organisation or wider government<br>• enable the implementation of strategies or visions across the organisation or wider government, for example, by advocating for resources and removing blockers |
| [Technical design throughout the life cycle](../../스킬/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | 전문가 | You can:<br>• create technical designs characterised by high risk, impact, and complexity<br>• lead and guide others in creating technical designs that achieve organisational objectives<br>• use feedback to optimise and refine standards for technical designs throughout the life cycle |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 보건·돌봄 시스템에 대한 깊은 이해를 바탕으로 조직 전략을 형성한다<br>• 보건·돌봄 파트너와 리더에게 조직을 대표한다<br>• 정책과 서비스 변화가 디지털 서비스와 돌봄에 어떤 영향을 줄지 예측한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 조직의 상호운용성 표준과 전략을 정한다<br>• 국가 또는 조직 간 표준화 작업을 이끈다<br>• 여러 시스템에 걸친 핵심 연동의 설계를 보증한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 정보 거버넌스 정책과 전략을 정한다<br>• 정보 리스크와 준수에 대해 이사회에 조언한다<br>• 규제 기관과 파트너에게 조직을 대표한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 프로덕트나 변경의 위험 요소 식별과 리스크 평가를 이끈다<br>• 위험 요소 로그와 임상 안전 케이스 보고서를 작성하고 유지한다<br>• 프로덕트 팀과 리스크 통제에 합의하고 그것이 작동하는지 확인한다<br>• 임상 리스크 관리 기준의 적용에 대해 팀에 조언한다 |
| [의료기기 소프트웨어 규제](../../스킬/#의료기기-소프트웨어-규제) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 의료기기 표준을 충족하는 소프트웨어 생애 주기 프로세스를 따른다<br>• 그 프로세스가 요구하는 기록을 작성한다 |
| [조직 리스크 관리](../../스킬/#조직-리스크-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 디렉터레이트나 프로그램의 리스크 프로세스를 운영한다<br>• 리스크를 리스크 선호도에 비추어 평가하고 상위에 보고한다<br>• 리스크를 위원회에 보고한다 |
| [피플 매니지먼트](../../스킬/#피플-매니지먼트) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 목표를 설정하고 평가를 하며 팀을 직접 관리한다<br>• 웰빙을 지원하고 근태, 실적, 행위를 관리한다<br>• 팀의 육성과 승계를 계획한다 |
| [예산 관리](../../스킬/#예산-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 작은 예산에 대한 지출을 추적하고 차이를 알린다<br>• 자신의 한도 안에서 지출을 승인한다 |

### 일반적인 자격과 경력

- 여러 프로그램과 조직에 걸쳐 솔루션 아키텍처를 이끈 풍부한 경력.

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
| 7 | 정책 및 서비스 개발에 대한 책임 | 5 | 45 |
| 8 | 재무 및 물적 자원에 대한 책임 | 4 | 32 |
| 9 | 사람에 대한 책임 | 4 | 32 |
| 10 | 정보 자원에 대한 책임 | 6 | 46 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 6 | 60 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **699** (밴드 8d: 675–720) |

UK GDaD PCF의 등급 제안(밴드 8c)보다 높은 밴드에 둔다. 보건 분야 채용 공고는 이 역할을 밴드 8d에 둔다. 이 직무는 조직의 솔루션 아키텍처 기준을 정하므로 행동의 자유는 레벨 6, 실천 공동체와 그 예산을 이끌므로 재무 자원과 사람은 레벨 4로 한다.


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
