# 보안 아키텍트

> 이 문서는 일반적인 디지털 헬스케어 조직을 위한 예시용 참조 프로필입니다. 특정 고용주의 공식 직무기술서가 아니며, 직무평가 점수도 공식 평가가 아닙니다.

> 이 글은 AI 어시스턴트가 영어를 한국어로 번역한 것이며, 한국어 원어민의 검토는 아직 받지 않았습니다. 영국 정부 디지털·데이터 전문직 역량 프레임워크(UK GDaD PCF)와 ESCO의 인용문은 영어 그대로 두었습니다.

**직군:** [아키텍처](../../#아키텍처)  
**밴드:** 8a, 8b, 8c  
**UK GDaD PCF 역할:** [Security architect](https://understand-digital-data-roles-skills.service.gov.uk/role/security-architect/)  
**ESCO 직업:** [ICT system architect](http://data.europa.eu/esco/occupation/e1c72b5f-4c5c-487c-a6df-e84b64a51dae) (ISCO-08 2511); [cybersecurity risk manager](http://data.europa.eu/esco/occupation/7754d570-9519-48c2-b1c9-8e165f8bca0f) (ISCO-08 2529)

## 개요

보안 아키텍트는 환자 정보가 기밀로 유지되고, 정확하며, 돌봄에 필요할 때 쓸 수 있도록 조직의 디지털 헬스 서비스의 보안을 설계한다. 보안 패턴과 통제를 정하고, 새로운 설계와 공급자의 보안 리스크를 평가하며, 서비스를 임상의와 환자가 안전하고 쓰기 쉽게 유지하는 리스크 기반 판단을 팀이 내리도록 돕는다.

## 디지털 헬스케어 조직에서

- 의료 기관은 랜섬웨어와 데이터 탈취의 표적이 되기 쉽고 공격은 임상 서비스를 멈출 수 있으므로, 가용성은 기밀성만큼 중요하다.
- 보안 통제가 긴급한 돌봄을 방해해서는 안 되므로, 설계는 강력한 인증과 임상 현장에서의 빠른 접근 사이의 균형을 맞춘다.
- 연결된 의료기기와 오래된 임상 시스템은 곧바로 패치를 적용하지 못하는 경우가 많으므로, 아키텍트는 세그먼테이션 같은 보완 통제를 설계한다.
- 많은 직원, 파트너 조직, 공급자가 환자 기록에 접근해야 하므로, 아이덴티티, 역할 기반 접근, 감사가 중심이 된다.
- 보안 설계는 정보 거버넌스 의무와 ISO/IEC 27001 같은 공표된 보안 표준을 뒷받침해야 한다.

## UK GDaD PCF 역할 설명(원문은 영어)

> A security architect designs and builds secure solutions.

## 역할 수준

| 밴드 | 직함 | UK GDaD PCF 수준 | 영국 공무원 등급 | 직무평가 점수 |
| --- | --- | --- | --- | --- |
| 8a | [보안 아키텍트](#밴드-8a-보안-아키텍트) | Security architect | HEO/SEO/G7 | 560 |
| 8b | [리드 보안 아키텍트](#밴드-8b-리드-보안-아키텍트) | Lead security architect | G7/G6 | 613 |
| 8c | [프린시펄 보안 아키텍트](#밴드-8c-프린시펄-보안-아키텍트) | Principal security architect | G6 | 662 |

## 밴드 8a: 보안 아키텍트

**UK GDaD PCF 수준: Security architect**

> A security architect creates and designs security for a system or service, maintains security documentation and develops architecture patterns and security approaches to new technologies.
> 
> At this role level, you will:
> - recommend security controls and identify solutions that support a business objective
> - provide specialist advice and recommend approaches across teams and various stakeholders
> - communicate widely with other stakeholders
> - advise on important security-related technologies and assess the risk associated with proposed changes
> - inspire and influence others to execute security principles
> - help review other people’s work

### 책임

- 아이덴티티, 암호화, 로깅, 네트워크 보호를 포함하여 서비스와 시스템의 보안 통제를 설계한다.
- 새로운 설계와 공급자 제품의 보안을 평가하고 리스크와 권장 통제를 기록한다.
- 환자 로그인이나 직원 싱글 사인온 등 전달 팀이 재사용할 수 있는 보안 패턴을 개발한다.
- 쉽게 업데이트할 수 없는 의료기기와 오래된 임상 시스템을 위한 보완 통제에 대해 조언한다.
- 정보 거버넌스 및 임상 안전 동료와 협력하여 보안, 프라이버시, 안전 리스크를 함께 평가한다.
- 보안 엔지니어와 다른 아키텍트를 안전한 설계에 대해 코칭한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Analysis](../../스킬/#analysis) | UK GDaD PCF | 실무 | You can:<br>• apply the approach to real problems and consider all relevant information<br>• apply appropriate rigour to ensure a full solution is designed and achieves the business outcome |
| [Communication (security architect)](../../스킬/#communication-security-architect) | UK GDaD PCF | 실천가 | You can:<br>• demonstrate a deep understanding of security concepts and can apply them to a technical level<br>• effectively translate and accurately communicate security and risk implications to technical and non-technical stakeholders<br>• successfully respond to challenges<br>• manage stakeholder expectations and be flexible, adapting to stakeholder reactions to reach consensus |
| [Designing secure systems](../../스킬/#designing-secure-systems) | UK GDaD PCF | 실무 | You can:<br>• design and review system architectures through the application of patterns and principles |
| [Enabling and informing risk-based decisions](../../스킬/#enabling-and-informing-risk-based-decisions) | UK GDaD PCF | 실무 | You can:<br>• work with risk owners to advise and give feedback<br>• advise on risk impact and whether it's within risk tolerance<br>• describe different risk methodologies and how these are applied, as well as the proportionality of risk |
| [Research and innovation](../../스킬/#research-and-innovation) | UK GDaD PCF | 실무 | You can:<br>• advise on developments to security properties in technology<br>• identify new technologies and design their use in a business context |
| [Security technology](../../스킬/#security-technology) | UK GDaD PCF | 실무 | You can:<br>• explain the effect of vulnerabilities on current and future designs<br>• share information on a range of systems, but may specialise in one |
| [Understanding security implications of transformation](../../스킬/#understanding-security-implications-of-transformation) | UK GDaD PCF | 실무 | You can:<br>• interpret and apply an understanding of policy and process, business architecture, and legal and political implications to assist the development of technical solutions or controls |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자신의 업무가 뒷받침하는 임상 및 돌봄 워크플로를 설명한다<br>• 임상 및 돌봄 동료와 일반적인 의료 용어를 올바르게 사용한다<br>• 변경이 환자 돌봄에 영향을 줄 수 있는 때를 알아보고 제기한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [아이덴티티 및 접근 관리](../../스킬/#아이덴티티-및-접근-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 아이덴티티 및 접근 서비스를 설계하고 운영한다<br>• 접근 권한을 정기적으로 검토하고 문제를 수정한다 |
| [취약점 관리](../../스킬/#취약점-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 환자 서비스에 대한 위험을 포함하여 리스크에 따라 취약점의 우선순위를 정한다<br>• 침투 테스트와 시정 조치의 범위를 정하고 관리한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |
| [의료기기 소프트웨어 규제](../../스킬/#의료기기-소프트웨어-규제) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 일부 보건 소프트웨어는 의료기기로 규제됨을 설명한다<br>• 제품이 의료기기일 수 있을 때 누구에게 물어야 하는지 안다 |

### 일반적인 자격과 경력

- 보안 아키텍처 또는 보안 엔지니어링에 관한 상당한 경력(석사에 준하는 수준).
- 공인된 보안 자격, 또는 그에 준하는 경력.

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

UK GDaD PCF의 등급 제안(밴드 6)보다 높은 밴드에 둔다. 보건 분야 채용 공고는 이 역할을 밴드 8a에 둔다. 이 직무는 적은 감독으로 핵심 임상 시스템의 보안을 설계하므로, 분석과 행동의 자유는 밴드 7 수준을 웃돌게 평가했다.

## 밴드 8b: 리드 보안 아키텍트

**UK GDaD PCF 수준: Lead security architect**

> A lead security architect undertakes complex work of a high risk level, often working on several projects.
> 
> At this role level, you will:
> - interact with senior stakeholders across departments
> - reach and influence a wide range of people across larger teams and communities
> - research and apply innovative security architecture solutions to new or existing problems and be able to justify and communicate design decisions
> - develop vision, principles and strategy for security architects for one project or technology
> - work out subtle security needs
> - understand the impact of decisions, balancing requirements and deciding between approaches
> - produce particular patterns and support quality assurance
> - be the point of escalation for architects in lower grade roles
> - lead the technical design of systems and services

### 책임

- 임상 시스템이나 클라우드 호스팅 등 여러 고위험 프로젝트 또는 주요 영역의 보안 아키텍처를 이끈다.
- 담당 영역 설계의 보안 원칙과 기준을 정하고 설계 기구에서 보증한다.
- 보안 리스크와 그 관리 선택지에 대해 시니어 리스크 오너에게 조언한다.
- 파트너 조직 및 공급자와 공유하는 데이터의 보안을 설계한다.
- 보안 아키텍트를 이끌고 육성한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Analysis](../../스킬/#analysis) | UK GDaD PCF | 실천가 | You can:<br>• monitor the analysis of a technical solution and ensure analysis is reused for similar problem sets<br>• review solutions and identify areas for change<br>• drive the collection of information that is used and analysed<br>• feed back on policy and requirements |
| [Communication (security architect)](../../스킬/#communication-security-architect) | UK GDaD PCF | 실천가 | You can:<br>• demonstrate a deep understanding of security concepts and can apply them to a technical level<br>• effectively translate and accurately communicate security and risk implications to technical and non-technical stakeholders<br>• successfully respond to challenges<br>• manage stakeholder expectations and be flexible, adapting to stakeholder reactions to reach consensus |
| [Designing secure systems](../../스킬/#designing-secure-systems) | UK GDaD PCF | 실천가 | You can:<br>• design and review system architectures through the development of patterns and principles |
| [Enabling and informing risk-based decisions](../../스킬/#enabling-and-informing-risk-based-decisions) | UK GDaD PCF | 실천가 | You can:<br>• work with higher impact or more complex risks, advising on the impact and whether it's within risk tolerance<br>• apply different risk methodologies in proportion to the risk |
| [Research and innovation](../../스킬/#research-and-innovation) | UK GDaD PCF | 실천가 | You can:<br>• contribute to and inform developments on security properties in technology<br>• identify new technologies and design the use of these in the business context across the organisation<br>• engage with the broader security community |
| [Security technology](../../스킬/#security-technology) | UK GDaD PCF | 전문가 | You can:<br>• explain complex system architectures<br>• identify and explain how easy or difficult it will be to exploit vulnerabilities<br>• lead and influence security technology in the security industry |
| [Understanding security implications of transformation](../../스킬/#understanding-security-implications-of-transformation) | UK GDaD PCF | 실천가 | You can:<br>• interpret and apply understanding across a complex area<br>• start influencing policy and process, business architecture, and legal and political implications |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 서비스가 조직 간 돌봄 경로에 어떻게 들어맞는지 분석한다<br>• 임상의, 돌봄 직원, 환자와 협력하여 디지털 서비스를 형성한다<br>• 디지털 결정이 돌봄, 안전, 직원 업무량에 미치는 영향을 설명한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [아이덴티티 및 접근 관리](../../스킬/#아이덴티티-및-접근-관리) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 직원, 환자, 시스템의 아이덴티티 및 접근 전략을 정한다<br>• 새로운 아이덴티티 표준의 도입을 이끈다 |
| [취약점 관리](../../스킬/#취약점-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 환자 서비스에 대한 위험을 포함하여 리스크에 따라 취약점의 우선순위를 정한다<br>• 침투 테스트와 시정 조치의 범위를 정하고 관리한다 |
| [보안 운영](../../스킬/#보안-운영) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 알림을 모니터링하고 런북을 사용해 분류한다<br>• 증거를 수집하고 이벤트를 상위에 보고한다<br>• 지도를 받아 간단한 탐지 규칙을 조정한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |
| [조직 리스크 관리](../../스킬/#조직-리스크-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 디렉터레이트나 프로그램의 리스크 프로세스를 운영한다<br>• 리스크를 리스크 선호도에 비추어 평가하고 상위에 보고한다<br>• 리스크를 위원회에 보고한다 |
| [피플 매니지먼트](../../스킬/#피플-매니지먼트) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 목표를 설정하고 평가를 하며 팀을 직접 관리한다<br>• 웰빙을 지원하고 근태, 실적, 행위를 관리한다<br>• 팀의 육성과 승계를 계획한다 |

### 일반적인 자격과 경력

- 복잡한 서비스의 보안 아키텍처에 관한 풍부한 경력.

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

## 밴드 8c: 프린시펄 보안 아키텍트

**UK GDaD PCF 수준: Principal security architect**

> A principal security architect works on services of high complexity and risk, making decisions to enable the business to achieve its needs.
> 
> At this role level, you will:
> - work on projects with high strategic impact, setting a strategy that can be used in the long term and across the breadth of the organisation
> - communicate with a broad range of senior stakeholders and be responsible for defining the vision, principles and strategy for security architects
> - recommend security design across several projects or technologies, up to an organisational or inter-organisational level
> - have a deep and evolving level of technical expertise, so you can act as an exemplar
> - make and influence important business and architectural decisions
> - research, identify, validate and adopt new technologies and methodologies
> - be a recognised expert and demonstrate this expertise by solving unprecedented issues and problems
> - further the profession, demonstrating and sharing best practice within and outside the organisation

### 책임

- 조직의 보안 아키텍처 비전, 원칙, 전략을 정한다.
- 환자 돌봄과 서비스에 대한 사이버 보안 리스크에 대해 경영진과 이사회에 조언한다.
- 대규모 공격으로부터의 복구를 포함한 사이버 복원력이 핵심 임상 서비스에 설계로 반영되도록 한다.
- 조직 간 사이버 보안 및 표준 커뮤니티에서 조직을 대표한다.
- 보안 아키텍처 실천을 이끌고 그 인력을 키운다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Analysis](../../스킬/#analysis) | UK GDaD PCF | 전문가 | You can:<br>• provide direction and lead on change regarding factors that feed into analysis<br>• monitor changes in the technical environment and assess whether risks are still at acceptable levels or whether previous decisions need to be revisited<br>• direct and influence others on best practice and policy |
| [Communication (security architect)](../../스킬/#communication-security-architect) | UK GDaD PCF | 전문가 | You can:<br>• demonstrate expert understanding of security concepts and can apply them to a technical level, at the highest levels of risk complexity<br>• effectively translate and accurately communicate security and risk implications at the most senior levels across technical and non-technical stakeholders<br>• successfully respond to challenges<br>• manage stakeholder expectations across high risk and complexity or under constrained timescales |
| [Designing secure systems](../../스킬/#designing-secure-systems) | UK GDaD PCF | 전문가 | You can:<br>• lead design and review solutions to complex problems with system architectures by defining and challenging patterns and principles<br>• create precedents and set direction |
| [Enabling and informing risk-based decisions](../../스킬/#enabling-and-informing-risk-based-decisions) | UK GDaD PCF | 전문가 | You can:<br>• act as a point of escalation<br>• be trusted by senior risk owners as an expert in security<br>• apply risk methodologies at the most complex levels of risk |
| [Research and innovation](../../스킬/#research-and-innovation) | UK GDaD PCF | 실천가 | You can:<br>• contribute to and inform developments on security properties in technology<br>• identify new technologies and design the use of these in the business context across the organisation<br>• engage with the broader security community |
| [Security technology](../../스킬/#security-technology) | UK GDaD PCF | 전문가 | You can:<br>• explain complex system architectures<br>• identify and explain how easy or difficult it will be to exploit vulnerabilities<br>• lead and influence security technology in the security industry |
| [Understanding security implications of transformation](../../스킬/#understanding-security-implications-of-transformation) | UK GDaD PCF | 전문가 | You can:<br>• challenge and lead changes to policy and processes to support business outcomes, business architecture, and legal and political implications |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 서비스가 조직 간 돌봄 경로에 어떻게 들어맞는지 분석한다<br>• 임상의, 돌봄 직원, 환자와 협력하여 디지털 서비스를 형성한다<br>• 디지털 결정이 돌봄, 안전, 직원 업무량에 미치는 영향을 설명한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 정보 거버넌스 정책과 전략을 정한다<br>• 정보 리스크와 준수에 대해 이사회에 조언한다<br>• 규제 기관과 파트너에게 조직을 대표한다 |
| [아이덴티티 및 접근 관리](../../스킬/#아이덴티티-및-접근-관리) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 직원, 환자, 시스템의 아이덴티티 및 접근 전략을 정한다<br>• 새로운 아이덴티티 표준의 도입을 이끈다 |
| [취약점 관리](../../스킬/#취약점-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 환자 서비스에 대한 위험을 포함하여 리스크에 따라 취약점의 우선순위를 정한다<br>• 침투 테스트와 시정 조치의 범위를 정하고 관리한다 |
| [보안 운영](../../스킬/#보안-운영) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 보안 인시던트를 조사하고 봉쇄한다<br>• 탐지 규칙을 작성하고 위협 헌팅을 수행한다<br>• 인시던트 이후 런북과 도구를 개선한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 프로덕트나 변경의 위험 요소 식별과 리스크 평가를 이끈다<br>• 위험 요소 로그와 임상 안전 케이스 보고서를 작성하고 유지한다<br>• 프로덕트 팀과 리스크 통제에 합의하고 그것이 작동하는지 확인한다<br>• 임상 리스크 관리 기준의 적용에 대해 팀에 조언한다 |
| [의료기기 소프트웨어 규제](../../스킬/#의료기기-소프트웨어-규제) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 의료기기 표준을 충족하는 소프트웨어 생애 주기 프로세스를 따른다<br>• 그 프로세스가 요구하는 기록을 작성한다 |
| [조직 리스크 관리](../../스킬/#조직-리스크-관리) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 조직의 리스크 관리 체계와 리스크 선호도를 설계한다<br>• 전략적 리스크에 대해 이사회에 조언한다 |
| [피플 매니지먼트](../../스킬/#피플-매니지먼트) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 목표를 설정하고 평가를 하며 팀을 직접 관리한다<br>• 웰빙을 지원하고 근태, 실적, 행위를 관리한다<br>• 팀의 육성과 승계를 계획한다 |

### 일반적인 자격과 경력

- 여러 조직에 걸쳐 보안 아키텍처를 이끈 풍부한 경력.

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
