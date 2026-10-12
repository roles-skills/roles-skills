# 기술 아키텍트

> 이 문서는 일반적인 디지털 헬스케어 조직을 위한 예시용 참조 프로필입니다. 특정 고용주의 공식 직무기술서가 아니며, 직무평가 점수도 공식 평가가 아닙니다.

> 이 글은 AI 어시스턴트가 영어를 한국어로 번역한 것이며, 한국어 원어민의 검토는 아직 받지 않았습니다. 영국 정부 디지털·데이터 전문직 역량 프레임워크(UK GDaD PCF)와 ESCO의 인용문은 영어 그대로 두었습니다.

**직군:** [아키텍처](../../#아키텍처)  
**밴드:** 6, 7, 8a, 8b, 8c  
**UK GDaD PCF 역할:** [Technical architect](https://understand-digital-data-roles-skills.service.gov.uk/role/technical-architect/)  
**ESCO 직업:** [software architect](http://data.europa.eu/esco/occupation/d0aa0792-4345-474b-9365-686cf4869d2e) (ISCO-08 2512); [cloud architect](http://data.europa.eu/esco/occupation/2fb96c6c-8d0b-4ef0-b1ee-3e493305e4eb) (ISCO-08 2512)

## 개요

기술 아키텍트는 조직의 디지털 헬스 서비스의 기술 구조를 설계한다. 컴포넌트, 플랫폼, 호스팅, 연동 패턴, 그리고 보안, 성능, 복원력 같은 비기능적 품질이다. 개발자와 DevOps 엔지니어와 긴밀히 협력하고 전달 팀에 기술적 리더십을 발휘하여, 서비스가 오래 가고 안전하게 운영할 수 있게 구축되도록 한다.

## 디지털 헬스케어 조직에서

- 임상 서비스는 높은 가용성과 빠른 복구를 요구하는 경우가 많으므로, 기술 설계는 장애와 축소 운영을 상정해야 한다.
- 설계는 암호화, 접근 제어, 감사를 기본으로 하여 민감한 건강 정보를 보호해야 한다.
- 서비스는 흔히 HL7 FHIR API나 메시징으로 많은 임상 시스템과 공용 플랫폼에 연결되므로, 연동 패턴이 설계의 중심이 된다.
- 캐시, 재시도, 시간 처리 같은 기술 설계의 선택은 임상 위험 요소를 만들 수 있으므로, 아키텍트는 안전 케이스에 기여한다.
- 오래된 임상 시스템과 의료기기는 기술, 네트워크, 호스팅 선택을 제약할 수 있다.

## UK GDaD PCF 역할 설명(원문은 영어)

> A technical architect provides technical leadership and architectural design.

## 역할 수준

| 밴드 | 직함 | UK GDaD PCF 수준 | 영국 공무원 등급 | 직무평가 점수 |
| --- | --- | --- | --- | --- |
| 6 | [어소시에이트 기술 아키텍트](#밴드-6-어소시에이트-기술-아키텍트) | Associate technical architect | EO/HEO | 412 |
| 7 | [기술 아키텍트](#밴드-7-기술-아키텍트) | Technical architect | SEO/G7 | 496 |
| 8a | [시니어 기술 아키텍트](#밴드-8a-시니어-기술-아키텍트) | Senior technical architect | SEO/G7 | 560 |
| 8b | [리드 기술 아키텍트](#밴드-8b-리드-기술-아키텍트) | Lead technical architect | G7/G6 | 613 |
| 8c | [프린시펄 기술 아키텍트](#밴드-8c-프린시펄-기술-아키텍트) | Principal technical architect | G6 | 662 |

## 밴드 6: 어소시에이트 기술 아키텍트

**UK GDaD PCF 수준: Associate technical architect**

> An associate technical architect supports technical architects in putting forward designs as solutions to technology challenges, usually under supervision.
> 
> At this role level, you will:
> - work closely with developers when designing appropriate solutions
> - have an understanding of the overall strategy and how your work supports it

### 책임

- 기술 도해를 그리고 기존 서비스의 컴포넌트, 호스팅, 연동을 문서화한다.
- 지도를 받으며 기술적 선택지를 조사하고 장단점을 요약한다.
- 개발자와 협력하여 구축이 합의된 설계와 패턴을 따르는지 확인한다.
- 기술적 결정을 기록하고 설계 문서를 최신으로 유지한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../스킬/#architect-for-the-whole-context) | UK GDaD PCF | 인지 | You can:<br>• identify relevant information that can inform your architectural work, such as strategies, roadmaps, policies and technical trends<br>• understand how your work supports the team in enabling change​ |
| [Architecture communication](../../스킬/#architecture-communication) | UK GDaD PCF | 인지 | You can:<br>• show an awareness of different ways of creating architecture representations for a limited audience, including technical and non-technical stakeholders<br>• gather and explain information to be used in architecture representations |
| [Community collaboration](../../스킬/#community-collaboration) | UK GDaD PCF | 인지 | You can:<br>• understand the work of others and the importance of team dynamics, collaboration and feedback |
| [Making architectural decisions](../../스킬/#making-architectural-decisions) | UK GDaD PCF | 인지 | You can:<br>• describe the reasoning behind architectural design decisions<br>• gather information to inform decisions<br>• understand architectural governance and assurance relevant to your work |
| [Strategy design](../../스킬/#strategy-design) | UK GDaD PCF | 인지 | You can:<br>• explain how organisational objectives link to designing strategy<br>• describe the purpose and application of strategy, standards, patterns, policies, roadmaps, vision, and mission statements |
| [Technical design throughout the life cycle](../../스킬/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | 실무 | You can:<br>• create technical designs characterised by managed levels of risk, impact, and complexity<br>• provide guidance and support to teams using technical designs throughout the life cycle<br>• adapt a technical design if needed during delivery<br>• work with well-understood technology and identify appropriate patterns |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 보건·돌봄 시스템의 주요 부분과 조직이 지원하는 서비스를 설명한다<br>• 자신의 업무에서 환자 안전과 비밀 유지가 중요한 이유를 설명한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• FHIR 리소스, 프로파일, API를 읽고 사용한다<br>• 지도를 받아 간단한 연동을 구축하거나 테스트한다<br>• 메시지를 사양에 비추어 확인한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 개인 정보와 건강 정보를 다루는 조직의 규칙을 따른다<br>• 데이터 침해나 아차 사고를 알아보고 보고한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 잘못되었거나, 빠졌거나, 지연된 정보 등을 통해 보건 IT 시스템이 환자에게 어떻게 해를 끼칠 수 있는지 설명한다<br>• 임상 안전 문제 가능성을 올바른 경로로 보고한다 |

### 일반적인 자격과 경력

- 컴퓨팅 또는 관련 분야 학위, 또는 소프트웨어나 인프라 엔지니어링에서의 그에 준하는 경력.
- 기술 설계 전문 지식(대학원 디플로마 수준 또는 그에 준하는 경력).

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
| 5 | 신체 기술 | 2 | 15 |
| 6 | 환자·이용자 돌봄에 대한 책임 | 1 | 4 |
| 7 | 정책 및 서비스 개발에 대한 책임 | 3 | 21 |
| 8 | 재무 및 물적 자원에 대한 책임 | 1 | 5 |
| 9 | 사람에 대한 책임 | 1 | 5 |
| 10 | 정보 자원에 대한 책임 | 5 | 34 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 4 | 32 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 3 | 12 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **412** (밴드 6: 396–465) |

UK GDaD PCF의 등급 제안(밴드 5)보다 높은 밴드에 둔다. 보건 분야 채용 공고는 이 역할을 밴드 6에 둔다. 이 직무는 대규모 정보 시스템의 일부를 설계하므로, 지식은 대학원 디플로마 수준, 정보 자원은 레벨 5로 평가했다.

## 밴드 7: 기술 아키텍트

**UK GDaD PCF 수준: Technical architect**

> A technical architect is responsible for the design and build of technical architecture.
> 
> At this role level, you will:
> - undertake structured analysis of technical issues, translating this analysis into technical designs that describe a solution
> - be consulted about design and provide design patterns
> - identify deeper issues that need fixing
> - look for opportunities to collaborate and reuse components, communicating with both technical and non-technical stakeholders

### 책임

- 컴포넌트, 호스팅, 연동, 보안을 포함하여 서비스의 기술 아키텍처를 설계한다.
- 전달 팀에 설계 패턴을 제공하고 기술 설계와 코드 구조를 검토한다.
- 서비스 오너와 함께 가용성, 성능, 복구 목표 같은 비기능 요구사항을 정의한다.
- 기술 부채와 지원되지 않는 기술을 식별하고 이를 해소하는 방법을 계획한다.
- 임상 안전 케이스를 위해 기술적 위험 요소와 통제를 식별한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../스킬/#architect-for-the-whole-context) | UK GDaD PCF | 실무 | You can:<br>• align your work with the work being done by other architects and technical professionals<br>• track emerging issues, strategies, roadmaps, patterns and technologies over time to assess opportunities and risks to your work<br>• identify how other teams contribute to delivering outcomes through change |
| [Architecture communication](../../스킬/#architecture-communication) | UK GDaD PCF | 실무 | You can:<br>• listen to the needs of technical and business stakeholders<br>• create and use different architecture representations to communicate effectively, achieving agreement with technical and non-technical stakeholders<br>• provide support in discussions about architectural topics within a multidisciplinary team |
| [Community collaboration](../../스킬/#community-collaboration) | UK GDaD PCF | 실무 | You can:<br>• contribute to the work of others<br>• motivate and empower teams<br>• create the right environment for teams to work in, and can identify the best team makeup depending on the situation<br>• recognise and deal with issues |
| [Making architectural decisions](../../스킬/#making-architectural-decisions) | UK GDaD PCF | 실무 | You can:<br>• work with others to make architectural design decisions characterised by managed levels of risk and complexity<br>• identify and address architectural risks relevant to your team or domain, for example, business, data, or security<br>• engage with architectural governance and assurance to effectively manage decisions and risks, with support |
| [Strategy design](../../스킬/#strategy-design) | UK GDaD PCF | 실무 | You can:<br>• support the development of a strategy or vision that aligns with organisational objectives<br>• challenge requirements and assumptions, and identify opportunities to develop strategy<br>• support the implementation of a strategy or vision, for example, by using a roadmap or plan<br>• use architectural principles, patterns, and constraints when appropriate |
| [Technical design throughout the life cycle](../../스킬/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | 실무 | You can:<br>• create technical designs characterised by managed levels of risk, impact, and complexity<br>• provide guidance and support to teams using technical designs throughout the life cycle<br>• adapt a technical design if needed during delivery<br>• work with well-understood technology and identify appropriate patterns |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자신의 업무가 뒷받침하는 임상 및 돌봄 워크플로를 설명한다<br>• 임상 및 돌봄 동료와 일반적인 의료 용어를 올바르게 사용한다<br>• 변경이 환자 돌봄에 영향을 줄 수 있는 때를 알아보고 제기한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• FHIR, HL7 버전 2, 메시징 패턴을 사용해 연동을 설계하고 구축한다<br>• FHIR 리소스와 구현 가이드를 작성하고 프로파일링한다<br>• 시스템 간의 복잡한 매핑과 데이터 품질 문제를 해결한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |
| [아이덴티티 및 접근 관리](../../스킬/#아이덴티티-및-접근-관리) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 접근 규칙을 따르고 자신의 인증 정보를 보호한다 |

### 일반적인 자격과 경력

- 기술 아키텍처 전문 지식(석사 수준 또는 그에 준하는 경력).
- 운영 소프트웨어나 인프라를 설계하거나 구축한 경험.

### 밴드 개요

- **지식:** 고도로 발달한 전문 지식. 보통 석사에 준하거나 그에 준하는 경력으로 얻는다.
- **자율성:** 조직의 방침에 맞춰 일하고, 성과를 내는 방법을 정하며, 다른 사람이 상담하는 전문가이다.
- **범위:** 여러 프로덕트나 서비스, 또는 전문 기능.
- **리더십:** 팀 또는 전문 실무 영역을 이끈다.
- **책무:** 서비스 또는 전문 기능의 제공, 그리고 예산이 있다면 그 예산.

### 직무평가(예시)

| # | 요소 | 수준 | 점수 |
| --- | --- | --- | --- |
| 1 | 의사소통 및 관계 형성 기술 | 5 | 45 |
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
| | **합계** | | **496** (밴드 7: 466–539) |

이 역할에 관한 보건 분야 채용 공고에 맞춰, UK GDaD PCF의 등급 제안인 밴드 7에 둔다. 지식은 기술 아키텍처 전 범위에 걸친 전문 지식이므로 석사 수준 또는 그에 준하는 수준으로 평가했다.

## 밴드 8a: 시니어 기술 아키텍트

**UK GDaD PCF 수준: Senior technical architect**

> A senior technical architect works on large or multiple pieces of work that are complex or risky.
> 
> At this role level, you will:
> - define strategy and be central to assuring services
> - regularly collaborate and find agreement with senior stakeholders, providing direction and challenge
> - be proactive in identifying problems and translating these into non-technical descriptions that can be widely understood
> - mentor and coach junior colleagues

### 책임

- 임상 시스템이나 공용 연동 플랫폼 등 대규모이거나 복잡하거나 위험이 높은 서비스의 기술 설계를 이끈다.
- 하나 이상의 전달 팀의 기술적 방향을 정하고 리스크를 높이는 설계에 이의를 제기한다.
- 복원력, 재해 복구, 안전한 운영을 고려해 설계하고 팀이 이를 테스트하는지 확인한다.
- 기술적 리스크와 득실을 서비스 오너, 임상 리드, 시니어 이해관계자에게 쉬운 말로 설명한다.
- 기술 아키텍트와 시니어 개발자를 멘토링하고 코칭한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../스킬/#architect-for-the-whole-context) | UK GDaD PCF | 실무 | You can:<br>• align your work with the work being done by other architects and technical professionals<br>• track emerging issues, strategies, roadmaps, patterns and technologies over time to assess opportunities and risks to your work<br>• identify how other teams contribute to delivering outcomes through change |
| [Architecture communication](../../스킬/#architecture-communication) | UK GDaD PCF | 실천가 | You can:<br>• lead the communication of complicated, complex or risky architecture topics with technical and non-technical stakeholders<br>• communicate with senior stakeholders across your organisation<br>• adapt your message and communication techniques to your audience<br>• advocate on behalf of a team to other stakeholders<br>• manage stakeholder expectations effectively |
| [Community collaboration](../../스킬/#community-collaboration) | UK GDaD PCF | 실천가 | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../스킬/#making-architectural-decisions) | UK GDaD PCF | 실무 | You can:<br>• work with others to make architectural design decisions characterised by managed levels of risk and complexity<br>• identify and address architectural risks relevant to your team or domain, for example, business, data, or security<br>• engage with architectural governance and assurance to effectively manage decisions and risks, with support |
| [Strategy design](../../스킬/#strategy-design) | UK GDaD PCF | 실무 | You can:<br>• support the development of a strategy or vision that aligns with organisational objectives<br>• challenge requirements and assumptions, and identify opportunities to develop strategy<br>• support the implementation of a strategy or vision, for example, by using a roadmap or plan<br>• use architectural principles, patterns, and constraints when appropriate |
| [Technical design throughout the life cycle](../../스킬/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | 실천가 | You can:<br>• create technical designs characterised by medium risk, impact, and complexity<br>• maintain appropriate quality and architectural coherence of a technical design in response to change<br>• use feedback to optimise and refine technical designs throughout the life cycle |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 서비스가 조직 간 돌봄 경로에 어떻게 들어맞는지 분석한다<br>• 임상의, 돌봄 직원, 환자와 협력하여 디지털 서비스를 형성한다<br>• 디지털 결정이 돌봄, 안전, 직원 업무량에 미치는 영향을 설명한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• FHIR, HL7 버전 2, 메시징 패턴을 사용해 연동을 설계하고 구축한다<br>• FHIR 리소스와 구현 가이드를 작성하고 프로파일링한다<br>• 시스템 간의 복잡한 매핑과 데이터 품질 문제를 해결한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |
| [아이덴티티 및 접근 관리](../../스킬/#아이덴티티-및-접근-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 사용자 계정과 접근 권한을 생성, 변경, 삭제한다<br>• 접근 권한을 역할 기반 접근 규칙에 비추어 확인한다 |
| [의료기기 소프트웨어 규제](../../스킬/#의료기기-소프트웨어-규제) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 일부 보건 소프트웨어는 의료기기로 규제됨을 설명한다<br>• 제품이 의료기기일 수 있을 때 누구에게 물어야 하는지 안다 |

### 일반적인 자격과 경력

- 복잡한 서비스의 기술 설계에 관한 상당한 경력(석사에 준하는 수준).

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

UK GDaD PCF의 등급 제안(밴드 7)보다 높은 밴드에 둔다. 보건 분야 채용 공고는 이 역할을 밴드 8a에 둔다. 이 직무는 적은 감독으로 여러 팀의 기술적 방향을 정하므로, 계획, 정책, 행동의 자유는 밴드 7 수준을 웃돌게 평가했다.

## 밴드 8b: 리드 기술 아키텍트

**UK GDaD PCF 수준: Lead technical architect**

> A lead technical architect works with multiple projects or teams on problems that require broad architectural thinking.
> 
> At this role level, you will:
> - be responsible for leading the technical design of systems and services, justifying and communicating design decisions
> - assure other services and system quality, ensuring the technical work fits into the broader strategy for government
> - explore the benefits of cross-government alignment
> - provide mentoring within teams
> - provide leadership to other architects

### 책임

- 여러 서비스와 팀에 걸친 기술 아키텍처를 이끌고 공용 패턴과 기준을 정한다.
- 보안, 복원력, 상호운용성을 포함하여 설계 기구에서 설계의 기술적 품질을 보증한다.
- 전사 아키텍트, 엔지니어링 리드와 함께 조직의 기술 로드맵을 형성한다.
- 기술 선택, 플랫폼 투자, 기술 리스크에 대해 시니어 리더에게 조언한다.
- 기술 아키텍트를 이끌고 육성한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../스킬/#architect-for-the-whole-context) | UK GDaD PCF | 실천가 | You can:<br>• work to support wider organisational objectives beyond your immediate goals​<br>• track emerging internal and external issues over time that could affect the work of teams across the organisation<br>• take action to solve or mitigate problems by influencing colleagues across the organisation |
| [Architecture communication](../../스킬/#architecture-communication) | UK GDaD PCF | 전문가 | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Community collaboration](../../스킬/#community-collaboration) | UK GDaD PCF | 실천가 | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../스킬/#making-architectural-decisions) | UK GDaD PCF | 실천가 | You can:<br>• make and guide architectural design decisions characterised by medium risk and complexity<br>• identify and address architectural risks that affect multiple teams or domains<br>• use architectural governance and assurance to make design decisions and manage technical risks at the appropriate level<br>• contribute to the development of architectural governance and assurance |
| [Strategy design](../../스킬/#strategy-design) | UK GDaD PCF | 실천가 | You can:<br>• define strategies or visions across teams that align with organisational objectives<br>• direct the implementation of a strategy or vision, for example, by creating roadmaps or plans<br>• define architectural principles and patterns<br>• develop or maintain strategy in response to feedback and findings |
| [Technical design throughout the life cycle](../../스킬/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | 전문가 | You can:<br>• create technical designs characterised by high risk, impact, and complexity<br>• lead and guide others in creating technical designs that achieve organisational objectives<br>• use feedback to optimise and refine standards for technical designs throughout the life cycle |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 서비스가 조직 간 돌봄 경로에 어떻게 들어맞는지 분석한다<br>• 임상의, 돌봄 직원, 환자와 협력하여 디지털 서비스를 형성한다<br>• 디지털 결정이 돌봄, 안전, 직원 업무량에 미치는 영향을 설명한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• FHIR, HL7 버전 2, 메시징 패턴을 사용해 연동을 설계하고 구축한다<br>• FHIR 리소스와 구현 가이드를 작성하고 프로파일링한다<br>• 시스템 간의 복잡한 매핑과 데이터 품질 문제를 해결한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 프로덕트나 변경의 위험 요소 식별과 리스크 평가를 이끈다<br>• 위험 요소 로그와 임상 안전 케이스 보고서를 작성하고 유지한다<br>• 프로덕트 팀과 리스크 통제에 합의하고 그것이 작동하는지 확인한다<br>• 임상 리스크 관리 기준의 적용에 대해 팀에 조언한다 |
| [아이덴티티 및 접근 관리](../../스킬/#아이덴티티-및-접근-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 아이덴티티 및 접근 서비스를 설계하고 운영한다<br>• 접근 권한을 정기적으로 검토하고 문제를 수정한다 |
| [의료기기 소프트웨어 규제](../../스킬/#의료기기-소프트웨어-규제) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 의료기기 표준을 충족하는 소프트웨어 생애 주기 프로세스를 따른다<br>• 그 프로세스가 요구하는 기록을 작성한다 |
| [피플 매니지먼트](../../스킬/#피플-매니지먼트) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 목표를 설정하고 평가를 하며 팀을 직접 관리한다<br>• 웰빙을 지원하고 근태, 실적, 행위를 관리한다<br>• 팀의 육성과 승계를 계획한다 |

### 일반적인 자격과 경력

- 복잡한 서비스의 기술 아키텍처를 이끈 풍부한 경력.

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

## 밴드 8c: 프린시펄 기술 아키텍트

**UK GDaD PCF 수준: Principal technical architect**

> A principal technical architect leads at the highest level and is responsible for making sure the strategy is agreed and followed.
> 
> At this role level, you will:
> - network and communicate with senior stakeholders across organisations
> - proactively seek opportunities for digital transformation
> - support multiple teams, finding and using best practice and emerging technologies
> - inspire other architects and help them understand how to deliver the goals of the organisation
> - be responsible for governance, solving complex and high risk issues or delivering architecture design

### 책임

- 조직의 기술 아키텍처 전략, 원칙, 기준을 정한다.
- 기술 설계 기구를 포함하여 조직 전체의 기술 설계를 통제한다.
- 호스팅 전략이나 플랫폼 통합 같은 주요 기술 결정에 대해 경영진에게 조언한다.
- 조직 간 기술 및 표준 커뮤니티에서 조직을 대표한다.
- 조직 전체의 아키텍트에게 영감을 주고 육성한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../스킬/#architect-for-the-whole-context) | UK GDaD PCF | 실천가 | You can:<br>• work to support wider organisational objectives beyond your immediate goals​<br>• track emerging internal and external issues over time that could affect the work of teams across the organisation<br>• take action to solve or mitigate problems by influencing colleagues across the organisation |
| [Architecture communication](../../스킬/#architecture-communication) | UK GDaD PCF | 전문가 | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Community collaboration](../../스킬/#community-collaboration) | UK GDaD PCF | 실천가 | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../스킬/#making-architectural-decisions) | UK GDaD PCF | 전문가 | You can:<br>• make and guide architectural design decisions characterised by high levels of risk and complexity<br>• identify and address architectural risks across the organisation or wider government<br>• lead and evolve architectural governance and assurance<br>• represent architectural governance as part of wider governance, for example, legal or commercial |
| [Strategy design](../../스킬/#strategy-design) | UK GDaD PCF | 전문가 | You can:<br>• define and connect strategies or visions across the organisation or wider government<br>• enable the implementation of strategies or visions across the organisation or wider government, for example, by advocating for resources and removing blockers |
| [Technical design throughout the life cycle](../../스킬/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | 전문가 | You can:<br>• create technical designs characterised by high risk, impact, and complexity<br>• lead and guide others in creating technical designs that achieve organisational objectives<br>• use feedback to optimise and refine standards for technical designs throughout the life cycle |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 서비스가 조직 간 돌봄 경로에 어떻게 들어맞는지 분석한다<br>• 임상의, 돌봄 직원, 환자와 협력하여 디지털 서비스를 형성한다<br>• 디지털 결정이 돌봄, 안전, 직원 업무량에 미치는 영향을 설명한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 조직의 상호운용성 표준과 전략을 정한다<br>• 국가 또는 조직 간 표준화 작업을 이끈다<br>• 여러 시스템에 걸친 핵심 연동의 설계를 보증한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 프로덕트나 변경의 위험 요소 식별과 리스크 평가를 이끈다<br>• 위험 요소 로그와 임상 안전 케이스 보고서를 작성하고 유지한다<br>• 프로덕트 팀과 리스크 통제에 합의하고 그것이 작동하는지 확인한다<br>• 임상 리스크 관리 기준의 적용에 대해 팀에 조언한다 |
| [아이덴티티 및 접근 관리](../../스킬/#아이덴티티-및-접근-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 아이덴티티 및 접근 서비스를 설계하고 운영한다<br>• 접근 권한을 정기적으로 검토하고 문제를 수정한다 |
| [조직 리스크 관리](../../스킬/#조직-리스크-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 디렉터레이트나 프로그램의 리스크 프로세스를 운영한다<br>• 리스크를 리스크 선호도에 비추어 평가하고 상위에 보고한다<br>• 리스크를 위원회에 보고한다 |
| [피플 매니지먼트](../../스킬/#피플-매니지먼트) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 목표를 설정하고 평가를 하며 팀을 직접 관리한다<br>• 웰빙을 지원하고 근태, 실적, 행위를 관리한다<br>• 팀의 육성과 승계를 계획한다 |

### 일반적인 자격과 경력

- 여러 팀과 조직에 걸쳐 기술 아키텍처를 이끈 풍부한 경력.

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
