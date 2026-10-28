# 인프라 엔지니어

> 이 문서는 일반적인 디지털 헬스케어 조직을 위한 예시용 참조 프로필입니다. 특정 고용주의 공식 직무기술서가 아니며, 직무평가 점수도 공식 평가가 아닙니다.

> 이 글은 AI 어시스턴트가 영어를 한국어로 번역한 것이며, 한국어 원어민의 검토는 아직 받지 않았습니다. 영국 정부 디지털·데이터 전문직 역량 프레임워크(UK GDaD PCF)와 ESCO의 인용문은 영어 그대로 두었습니다.

**직군:** [IT 운영](../../#it-운영)  
**밴드:** 4, 6, 7, 8a, 8b  
**UK GDaD PCF 역할:** [Infrastructure engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/infrastructure-engineer/)  
**ESCO 직업:** [ICT system administrator](http://data.europa.eu/esco/occupation/9e2e6e1e-363b-4e1b-a673-7bc0f7343300) (ISCO-08 2522); [ICT network engineer](http://data.europa.eu/esco/occupation/cf2b03cd-feb7-4f47-90f6-ff1ed6016d3d) (ISCO-08 2523); [cloud engineer](http://data.europa.eu/esco/occupation/349ee6f6-c295-4c38-9b98-48765b55280e) (ISCO-08 2512)

## 개요

인프라 엔지니어는 조직의 디지털 서비스가 의존하는 네트워크, 서버, 스토리지, 클라우드 플랫폼, 호스팅을 설계, 구축, 운영, 지원한다. 이 인프라를 가용하고, 안전하며, 복구 가능하게 유지하고 공급자 및 아키텍트와 협력해 안전하게 변경한다. 의료에서는 인프라 장애 하나가 병원과 지역사회 서비스의 임상 시스템을 한꺼번에 멈출 수 있다.

## 디지털 헬스케어 조직에서

- 임상 시스템에는 매우 높은 가용성이 필요하므로, 인프라는 복원력을 고려해 설계되고 변경은 임상 활동에 맞춰 계획된다.
- 밤이나 주말의 인프라 장애는 환자 돌봄을 멈출 수 있으므로, 엔지니어는 대기 당번에 참여한다.
- 네트워크에는 수액 펌프, 환자 모니터, 영상 장비 등 의료기기가 연결되어 있어 IEC 80001-1에 따른 네트워크 세그먼테이션과 신중한 변경이 필요하다.
- 의료는 랜섬웨어의 잦은 표적이므로, 백업은 보호되고, 테스트되며, 합의된 복구 시간 안에 복원할 수 있어야 한다.
- 인프라에는 오래된 기술과 새로운 기술이 섞여 있고 쉽게 패치할 수 없는 레거시 임상 시스템도 포함되므로, 엔지니어는 보완 통제를 마련한다.

## UK GDaD PCF 역할 설명(원문은 영어)

> An infrastructure engineer designs, builds, manages and supports the infrastructure services that underpin all internal user services and services to the public.

## 역할 수준

| 밴드 | 직함 | UK GDaD PCF 수준 | 영국 공무원 등급 | 직무평가 점수 |
| --- | --- | --- | --- | --- |
| 4 | [어소시에이트 인프라 엔지니어](#밴드-4-어소시에이트-인프라-엔지니어) | Associate infrastructure engineer | EO | 275 |
| 6 | [인프라 엔지니어](#밴드-6-인프라-엔지니어) | Infrastructure engineer | HEO/SEO | 434 |
| 7 | [시니어 인프라 엔지니어](#밴드-7-시니어-인프라-엔지니어) | Senior infrastructure engineer | SEO/G7 | 490 |
| 8a | [리드 인프라 엔지니어](#밴드-8a-리드-인프라-엔지니어) | Lead infrastructure engineer | G7/G6 | 560 |
| 8b | [프린시펄 인프라 엔지니어](#밴드-8b-프린시펄-인프라-엔지니어) | Principal infrastructure engineer | G7/G6 | 600 |

## 밴드 4: 어소시에이트 인프라 엔지니어

**UK GDaD PCF 수준: Associate infrastructure engineer**

> As a trainee, you will work in an established team and support infrastructure engineers in their daily work, under their direction.

### 책임

- 서버 구축, 백업 점검, 네트워크 변경 같은 정형 작업에서 인프라 엔지니어를 지원한다.
- 인프라를 모니터링하고 경보와 결함을 적절한 팀에 보고한다.
- 모든 작업에서 변경, 보안, 정보 거버넌스 절차를 따른다.
- 구성과 자산 세부 정보를 정확하게 기록한다.
- 인프라 어프렌티스십 또는 그에 준하는 자격 취득을 위해 노력한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Information security](../../스킬/#information-security) | UK GDaD PCF | 인지 | You can:<br>• explain information security and the security controls available to protect solutions and services |
| [IT infrastructure](../../스킬/#it-infrastructure) | UK GDaD PCF | 인지 | You can:<br>• support infrastructure solutions and services, and other computer, storage, networking, physical infrastructure, software, commercial-off-the-shelf (COTS) software and open source packages and solutions<br>• support virtual and cloud computing, including Infrastructure as a Service (IaaS), Platform as a Service (PaaS) and Software as a Service (SaaS) |
| [Modern development standards](../../스킬/#modern-development-standards) | UK GDaD PCF | 인지 | You can:<br>• explain the importance of using modern development standards |
| [Ownership and initiative](../../스킬/#ownership-and-initiative) | UK GDaD PCF | 인지 | You can:<br>• show an awareness of problem resolution processes<br>• pass problems on to your team |
| [Problem management](../../스킬/#problem-management) | UK GDaD PCF | 인지 | You can:<br>• investigate problems in systems, processes and services, with an understanding of the level of a problem, for example, strategic, tactical or operational<br>• contribute to the implementation of remedies and preventative measures |
| [Systems design](../../스킬/#systems-design) | UK GDaD PCF | 인지 | You can:<br>• assist as part of a team in the design of components of larger systems |
| [Systems integration](../../스킬/#systems-integration) | UK GDaD PCF | 인지 | You can:<br>• explain the process and principles of integrating systems.<br>• describe challenges of designing, building and testing interfaces between systems |
| [Technical understanding](../../스킬/#technical-understanding) | UK GDaD PCF | 인지 | You can:<br>• show an awareness of the relevant subject matter and a high level understanding of what it involves |
| [Troubleshooting and problem resolution](../../스킬/#troubleshooting-and-problem-resolution) | UK GDaD PCF | 인지 | You can:<br>• show an awareness of different technology capabilities<br>• demonstrate basic troubleshooting capability |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 보건·돌봄 시스템의 주요 부분과 조직이 지원하는 서비스를 설명한다<br>• 자신의 업무에서 환자 안전과 비밀 유지가 중요한 이유를 설명한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 개인 정보와 건강 정보를 다루는 조직의 규칙을 따른다<br>• 데이터 침해나 아차 사고를 알아보고 보고한다 |
| [보안 운영](../../스킬/#보안-운영) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 피싱과 랜섬웨어 같은 일반적인 사이버 위협을 설명한다<br>• 의심스러운 보안 이벤트를 보고한다 |
| [취약점 관리](../../스킬/#취약점-관리) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 신속한 패치 적용과 안전한 구성이 중요한 이유를 설명한다 |

### 일반적인 자격과 경력

- 인프라 또는 네트워크 어프렌티스십 또는 그에 준하는 과정에 등록했거나 취득을 목표로 하고 있다.

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
| 8 | 재무 및 물적 자원에 대한 책임 | 2 | 12 |
| 9 | 사람에 대한 책임 | 1 | 5 |
| 10 | 정보 자원에 대한 책임 | 3 | 16 |
| 11 | 연구 및 개발에 대한 책임 | 1 | 5 |
| 12 | 행동의 자유 | 2 | 12 |
| 13 | 신체적 부담 | 2 | 7 |
| 14 | 정신적 부담 | 3 | 12 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **275** (밴드 4: 271–325) |

지식은 업무를 수행할 수 있을 만큼 교육이 끝난 시점에 직무가 요구하는 수준으로 평가했다.

## 밴드 6: 인프라 엔지니어

**UK GDaD PCF 수준: Infrastructure engineer**

> Working in a team of infrastructure specialists and engineers, an infrastructure engineer supports and maintains infrastructure solutions and services as directed and according to departmental policy.
> 
> At this role level, you will:
> - ensure services are delivered and used as required
> - work with and support third parties to provide infrastructure services

### 책임

- 임상 및 공통 부문 시스템을 호스팅하는 서버, 스토리지, 네트워크, 클라우드 서비스를 구축, 설정, 유지한다.
- 보안 리스크와 임상 시스템을 계속 사용할 수 있게 해야 할 필요 사이의 균형을 맞추며 인프라에 신속히 패치를 적용한다.
- 핵심 임상 시스템을 포함하여 백업과 복원을 실행하고 테스트한다.
- 임상 공학 팀과 협력하여 의료기기와 그 밖의 임상 장비를 위한 세그먼트된 네트워크를 지원한다.
- 대기 당번의 일환으로를 포함하여 인프라 결함을 조사하고 고친다.
- 스크립트와 코드로서의 인프라로 정형 업무를 자동화한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Coding and scripting](../../스킬/#coding-and-scripting) | UK GDaD PCF | 인지 | You can:<br>• describe different scripting tools and software that are available and currently in use |
| [Information security](../../스킬/#information-security) | UK GDaD PCF | 인지 | You can:<br>• explain information security and the security controls available to protect solutions and services |
| [IT infrastructure](../../스킬/#it-infrastructure) | UK GDaD PCF | 실무 | You can:<br>• build, configure, administer and support infrastructure solutions and services, for example, networking and physical infrastructure, commercial-off-the-shelf (COTS) software, open source packages and solutions, or virtual and cloud computing |
| [Modern development standards](../../스킬/#modern-development-standards) | UK GDaD PCF | 실무 | You can:<br>• explain the most important principles of modern development standards and how they apply to your work<br>• apply modern development standards principles under guidance |
| [Ownership and initiative](../../스킬/#ownership-and-initiative) | UK GDaD PCF | 실무 | You can:<br>• own an issue until a new owner has been found or the problem has been mitigated or resolved |
| [Problem management](../../스킬/#problem-management) | UK GDaD PCF | 인지 | You can:<br>• investigate problems in systems, processes and services, with an understanding of the level of a problem, for example, strategic, tactical or operational<br>• contribute to the implementation of remedies and preventative measures |
| [Service focus](../../스킬/#service-focus) | UK GDaD PCF | 실무 | You can:<br>• take inputs and establish coherent frameworks that work |
| [Systems design](../../스킬/#systems-design) | UK GDaD PCF | 실무 | You can:<br>• translate logical designs into physical designs<br>• produce detailed designs<br>• effectively document all work using required standards, methods and tools, including prototyping tools where appropriate<br>• design systems characterised by managed levels of risk, manageable business and technical complexity, and meaningful impact<br>• work with well understood technology and identify appropriate patterns |
| [Systems integration](../../스킬/#systems-integration) | UK GDaD PCF | 실무 | You can:<br>• build and test simple interfaces between systems<br>• work on more complex integration as part of a wider team |
| [Technical understanding](../../스킬/#technical-understanding) | UK GDaD PCF | 실무 | You can:<br>• understand the core technical concepts related to the role, and apply them with guidance |
| [Testing](../../스킬/#testing) | UK GDaD PCF | 인지 | You can:<br>• correctly execute test scripts under supervision<br>• understand the role of testing and how it works |
| [Troubleshooting and problem resolution](../../스킬/#troubleshooting-and-problem-resolution) | UK GDaD PCF | 실무 | You can:<br>• troubleshoot and identify problems across different technology capabilities |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자신의 업무가 뒷받침하는 임상 및 돌봄 워크플로를 설명한다<br>• 임상 및 돌봄 동료와 일반적인 의료 용어를 올바르게 사용한다<br>• 변경이 환자 돌봄에 영향을 줄 수 있는 때를 알아보고 제기한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [보안 운영](../../스킬/#보안-운영) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 피싱과 랜섬웨어 같은 일반적인 사이버 위협을 설명한다<br>• 의심스러운 보안 이벤트를 보고한다 |
| [취약점 관리](../../스킬/#취약점-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 취약점 스캔을 실행하고 결과를 보고한다<br>• 시스템 담당자와 함께 수정 사항을 추적한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 잘못되었거나, 빠졌거나, 지연된 정보 등을 통해 보건 IT 시스템이 환자에게 어떻게 해를 끼칠 수 있는지 설명한다<br>• 임상 안전 문제 가능성을 올바른 경로로 보고한다 |

### 일반적인 자격과 경력

- 컴퓨팅 또는 관련 분야 학위, 관련 기술 인증, 또는 그에 준하는 경력.
- 운영 인프라를 지원한 경험.

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
| 7 | 정책 및 서비스 개발에 대한 책임 | 3 | 21 |
| 8 | 재무 및 물적 자원에 대한 책임 | 2 | 12 |
| 9 | 사람에 대한 책임 | 2 | 12 |
| 10 | 정보 자원에 대한 책임 | 4 | 24 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 4 | 32 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **434** (밴드 6: 396–465) |

정신적 부담은 시간 외 대기 당번을 포함하여 예측하기 어려운 결함에 장시간 집중하는 경우가 잦음을 반영한다.

## 밴드 7: 시니어 인프라 엔지니어

**UK GDaD PCF 수준: Senior infrastructure engineer**

> Working in a team of infrastructure specialists and engineers, a senior infrastructure engineer builds, administers, supports and maintains solutions as directed and according to departmental policy.
> 
> At this role level, you will:
> - ensure services are integrated, delivered and operated as required
> - work with and support third parties in providing infrastructure services
> - work with technical architects to translate architectural designs into operations
> - provide input into overall management - workforce, budget, technology roadmaps, projects and tasks
> - lead and direct infrastructure specialist teams in building, managing, supporting and maintaining solutions according to departmental policy (if taking a managerial path)

### 책임

- 아키텍트의 설계에서 임상 서비스가 필요로 하는 복원력을 갖춘 인프라 솔루션을 설계하고 구축한다.
- 데이터 센터 이전, 네트워크 교체, 클라우드 이전 등 대규모 인프라 변경을 임상 활동에 맞춰 계획하고 이끈다.
- 핵심 임상 시스템의 재해 복구와 랜섬웨어 복구를 설계하고 테스트한다.
- 인프라 인시던트에 대한 기술적 대응을 이끌고 그 원인의 수정을 추진한다.
- 패치할 수 없는 레거시 시스템과 의료기기를 위한 보완 통제를 관리한다.
- 인프라 엔지니어를 이끌고 코칭한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Coding and scripting](../../스킬/#coding-and-scripting) | UK GDaD PCF | 인지 | You can:<br>• describe different scripting tools and software that are available and currently in use |
| [Information security](../../스킬/#information-security) | UK GDaD PCF | 실무 | You can:<br>• use information security practices and available security controls to contribute to protecting solutions and services |
| [IT infrastructure](../../스킬/#it-infrastructure) | UK GDaD PCF | 실천가 | You can:<br>• design and implement infrastructure solutions and services, for example, networking and physical infrastructure, commercial-off-the-shelf (COTS) software, open source packages and solutions, or virtual and cloud computing |
| [Modern development standards](../../스킬/#modern-development-standards) | UK GDaD PCF | 실천가 | You can:<br>• apply modern development standards and support others in applying them |
| [Ownership and initiative](../../스킬/#ownership-and-initiative) | UK GDaD PCF | 실무 | You can:<br>• own an issue until a new owner has been found or the problem has been mitigated or resolved |
| [Problem management](../../스킬/#problem-management) | UK GDaD PCF | 실무 | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Service focus](../../스킬/#service-focus) | UK GDaD PCF | 실무 | You can:<br>• take inputs and establish coherent frameworks that work |
| [Systems design](../../스킬/#systems-design) | UK GDaD PCF | 실천가 | You can:<br>• design systems characterised by medium levels of risk, impact, and business or technical complexity<br>• select appropriate design standards, methods and tools, and ensure they are applied effectively<br>• review the systems designs of others to ensure the selection of appropriate technology, efficient use of resources and integration of multiple systems and technology |
| [Systems integration](../../스킬/#systems-integration) | UK GDaD PCF | 실천가 | You can:<br>• define the integration build<br>• co-ordinate build activities across systems<br>• understand how to undertake and support integration testing activities |
| [Technical understanding](../../스킬/#technical-understanding) | UK GDaD PCF | 실천가 | You can:<br>• show a thorough understanding of the technical concepts required for the role, and can explain how these fit into the wider technical landscape |
| [Testing](../../스킬/#testing) | UK GDaD PCF | 실무 | You can:<br>• review requirements and specifications, and define test conditions<br>• identify issues and risks associated with work<br>• analyse and report test activities and results |
| [Troubleshooting and problem resolution](../../스킬/#troubleshooting-and-problem-resolution) | UK GDaD PCF | 실천가 | You can:<br>• break a problem down into its component parts to identify and diagnose root causes<br>• troubleshoot and identify problems across different technology capabilities |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자신의 업무가 뒷받침하는 임상 및 돌봄 워크플로를 설명한다<br>• 임상 및 돌봄 동료와 일반적인 의료 용어를 올바르게 사용한다<br>• 변경이 환자 돌봄에 영향을 줄 수 있는 때를 알아보고 제기한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [보안 운영](../../스킬/#보안-운영) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 알림을 모니터링하고 런북을 사용해 분류한다<br>• 증거를 수집하고 이벤트를 상위에 보고한다<br>• 지도를 받아 간단한 탐지 규칙을 조정한다 |
| [취약점 관리](../../스킬/#취약점-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 환자 서비스에 대한 위험을 포함하여 리스크에 따라 취약점의 우선순위를 정한다<br>• 침투 테스트와 시정 조치의 범위를 정하고 관리한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |
| [조직 리스크 관리](../../스킬/#조직-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자기 영역의 리스크를 기록하고 갱신한다<br>• 통제 방안을 제안하고 대응을 추적한다 |

### 일반적인 자격과 경력

- 운영 인프라의 설계와 운영에 관한 상당한 경력(대학원 디플로마에 준하는 수준).

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
| 2 | 지식, 교육, 경험 | 6 | 156 |
| 3 | 분석 및 판단 기술 | 4 | 42 |
| 4 | 계획 및 조직화 기술 | 4 | 42 |
| 5 | 신체 기술 | 3 | 27 |
| 6 | 환자·이용자 돌봄에 대한 책임 | 1 | 4 |
| 7 | 정책 및 서비스 개발에 대한 책임 | 3 | 21 |
| 8 | 재무 및 물적 자원에 대한 책임 | 3 | 21 |
| 9 | 사람에 대한 책임 | 3 | 21 |
| 10 | 정보 자원에 대한 책임 | 5 | 34 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 4 | 32 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **490** (밴드 7: 466–539) |

정신적 부담은 시간 외를 포함해 인시던트와 복잡한 변경 중에 장시간 집중하는 경우가 잦음을 반영한다.

## 밴드 8a: 리드 인프라 엔지니어

**UK GDaD PCF 수준: Lead infrastructure engineer**

> A lead infrastructure engineer manages third party provision of infrastructure services and the provision of expertise to develop architectural solutions for infrastructure services, throughout the service product life cycle.
> 
> At this role level, you will:
> - oversee programmes and projects
> - work with technical architects to translate the architectural designs into operations and support technical architects in operationalising the designs
> - lead and direct infrastructure specialist teams in building, managing, supporting and maintaining solutions according to departmental policy (if taking a managerial path)

### 책임

- 주요 플랫폼 또는 서비스군의 인프라를 이끌고 그 기술적 방향을 정한다.
- 서드파티 인프라 공급자를 관리하고 가용성과 복구에 관한 서비스 수준을 지키게 한다.
- 네트워크 갱신이나 클라우드 호스팅으로의 이전 같은 인프라 프로그램을 감독한다.
- 인프라가 보안, 정보 거버넌스, 의료기기 네트워크 기준을 충족하도록 한다.
- 인프라 팀을 이끌고 그 기술을 육성한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Coding and scripting](../../스킬/#coding-and-scripting) | UK GDaD PCF | 실무 | You can:<br>• interact with, read and write code<br>• carry out baseline repair activities |
| [Information security](../../스킬/#information-security) | UK GDaD PCF | 실천가 | You can:<br>• design solutions and services with security controls included, specifically engineered to mitigate security threats |
| [IT infrastructure](../../스킬/#it-infrastructure) | UK GDaD PCF | 전문가 | You can:<br>• lead teams and departments in the design, implementation, administration and support of infrastructure solutions and services |
| [Modern development standards](../../스킬/#modern-development-standards) | UK GDaD PCF | 전문가 | You can:<br>• identify and apply modern development standards to support complex projects and programmes<br>• lead others in applying modern development standards |
| [Ownership and initiative](../../스킬/#ownership-and-initiative) | UK GDaD PCF | 실천가 | You can:<br>• take accountability for issues that occur and be proactive in searching for potential problems<br>• achieve excellent user outcomes |
| [Problem management](../../스킬/#problem-management) | UK GDaD PCF | 실무 | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Service focus](../../스킬/#service-focus) | UK GDaD PCF | 실무 | You can:<br>• take inputs and establish coherent frameworks that work |
| [Systems design](../../스킬/#systems-design) | UK GDaD PCF | 실천가 | You can:<br>• design systems characterised by medium levels of risk, impact, and business or technical complexity<br>• select appropriate design standards, methods and tools, and ensure they are applied effectively<br>• review the systems designs of others to ensure the selection of appropriate technology, efficient use of resources and integration of multiple systems and technology |
| [Systems integration](../../스킬/#systems-integration) | UK GDaD PCF | 전문가 | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Technical understanding](../../스킬/#technical-understanding) | UK GDaD PCF | 전문가 | You can:<br>• anticipate and advise on future technology changes that present opportunities for the product or programme |
| [Testing](../../스킬/#testing) | UK GDaD PCF | 실천가 | You can:<br>• manage the planning of system and acceptance tests, co-ordinating both functional and non-functional specifications<br>• provide authoritative advice and guidance on test planning<br>• identify process improvements and contribute to the definition of best practice |
| [Troubleshooting and problem resolution](../../스킬/#troubleshooting-and-problem-resolution) | UK GDaD PCF | 전문가 | You can:<br>• use lateral thinking to break a problem down into its component parts to identify and diagnose root causes<br>• troubleshoot and identify problems across different technology capabilities including computing, storage, networking, physical infrastructure, software, commercial-off-the-shelf software (COTS) and open source software |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 서비스가 조직 간 돌봄 경로에 어떻게 들어맞는지 분석한다<br>• 임상의, 돌봄 직원, 환자와 협력하여 디지털 서비스를 형성한다<br>• 디지털 결정이 돌봄, 안전, 직원 업무량에 미치는 영향을 설명한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [보안 운영](../../스킬/#보안-운영) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 알림을 모니터링하고 런북을 사용해 분류한다<br>• 증거를 수집하고 이벤트를 상위에 보고한다<br>• 지도를 받아 간단한 탐지 규칙을 조정한다 |
| [취약점 관리](../../스킬/#취약점-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 환자 서비스에 대한 위험을 포함하여 리스크에 따라 취약점의 우선순위를 정한다<br>• 침투 테스트와 시정 조치의 범위를 정하고 관리한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |
| [조직 리스크 관리](../../스킬/#조직-리스크-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 디렉터레이트나 프로그램의 리스크 프로세스를 운영한다<br>• 리스크를 리스크 선호도에 비추어 평가하고 상위에 보고한다<br>• 리스크를 위원회에 보고한다 |
| [피플 매니지먼트](../../스킬/#피플-매니지먼트) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 목표를 설정하고 평가를 하며 팀을 직접 관리한다<br>• 웰빙을 지원하고 근태, 실적, 행위를 관리한다<br>• 팀의 육성과 승계를 계획한다 |

### 일반적인 자격과 경력

- 복잡하고 고가용성인 서비스의 인프라 엔지니어링을 이끈 풍부한 경력.

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
| 8 | 재무 및 물적 자원에 대한 책임 | 3 | 21 |
| 9 | 사람에 대한 책임 | 3 | 21 |
| 10 | 정보 자원에 대한 책임 | 5 | 34 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 5 | 45 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **560** (밴드 8a: 540–584) |

UK GDaD PCF는 리드와 프린시펄 인프라 엔지니어 모두에 밴드 8b를 제안한다. 이 레퍼런스는 다른 기술 직군의 리드와 프린시펄 역할에 맞춰 두 수준이 다른 밴드에 놓이도록 리드를 밴드 8a에 둔다.

## 밴드 8b: 프린시펄 인프라 엔지니어

**UK GDaD PCF 수준: Principal infrastructure engineer**

> A principal infrastructure engineer is an accomplished technical leader.
> 
> At this role level, you will:
> - develop strategic and tactical engineering roadmaps for technologies and services in your area of responsibility, ensuring they're future-proofed and that the organisation derives maximum value from investment in technologies
> - potentially own the operational relationships with suppliers, ensuring services and products are delivered and aligned to industry best practice and regulatory and contractual requirements
> - work with technical architects to translate the architectural designs into operations and support technical architects in operationalising the designs
> - lead and direct infrastructure specialist teams in building, managing, supporting and maintaining solutions according to departmental policy (if taking a managerial path)

### 책임

- 투자가 임상 서비스를 위해 탄력적이고, 안전하며, 지속 가능한 호스팅을 제공하도록 인프라 전략과 로드맵을 수립한다.
- 전략적 인프라 및 네트워크 공급자와의 운영상의 관계를 맡는다.
- 수명이 다한 기술, 단일 장애 지점, 사이버 복원력을 포함하여 인프라 리스크에 대해 시니어 리더에게 조언한다.
- 서비스 오너와 함께 임상 시스템의 목표 복구 시간과 목표 복구 시점을 정하고 인프라가 이를 충족하도록 한다.
- 조직 전체의 인프라 엔지니어링 직군을 이끌고 그 역량을 키운다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Coding and scripting](../../스킬/#coding-and-scripting) | UK GDaD PCF | 실무 | You can:<br>• interact with, read and write code<br>• carry out baseline repair activities |
| [Information security](../../스킬/#information-security) | UK GDaD PCF | 실천가 | You can:<br>• design solutions and services with security controls included, specifically engineered to mitigate security threats |
| [IT infrastructure](../../스킬/#it-infrastructure) | UK GDaD PCF | 실천가 | You can:<br>• design and implement infrastructure solutions and services, for example, networking and physical infrastructure, commercial-off-the-shelf (COTS) software, open source packages and solutions, or virtual and cloud computing |
| [Modern development standards](../../스킬/#modern-development-standards) | UK GDaD PCF | 전문가 | You can:<br>• identify and apply modern development standards to support complex projects and programmes<br>• lead others in applying modern development standards |
| [Ownership and initiative](../../스킬/#ownership-and-initiative) | UK GDaD PCF | 실천가 | You can:<br>• take accountability for issues that occur and be proactive in searching for potential problems<br>• achieve excellent user outcomes |
| [Problem management](../../스킬/#problem-management) | UK GDaD PCF | 실천가 | You can:<br>• ensure that the right actions are taken to investigate, resolve and anticipate problems<br>• co-ordinate the team to investigate problems, implement solutions and take preventive measures |
| [Service focus](../../스킬/#service-focus) | UK GDaD PCF | 실천가 | You can:<br>• see the bigger picture by taking groups of services and investigating how to get the best of underlying services |
| [Systems design](../../스킬/#systems-design) | UK GDaD PCF | 전문가 | You can:<br>• design systems characterised by high levels of risk, impact, and business or technical complexity<br>• control system design practice within an enterprise or industry architecture<br>• influence industry-based models for the development of new technology applications<br>• develop effective implementation and procurement strategies, consistent with business needs<br>• ensure adherence to relevant technical strategies, policies, standards and practices |
| [Systems integration](../../스킬/#systems-integration) | UK GDaD PCF | 전문가 | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Technical understanding](../../스킬/#technical-understanding) | UK GDaD PCF | 실천가 | You can:<br>• show a thorough understanding of the technical concepts required for the role, and can explain how these fit into the wider technical landscape |
| [Testing](../../스킬/#testing) | UK GDaD PCF | 전문가 | You can:<br>• manage testing activities within development or integration activities<br>• manage risks and take preventative action when risks become unacceptable<br>• manage customer relations |
| [Troubleshooting and problem resolution](../../스킬/#troubleshooting-and-problem-resolution) | UK GDaD PCF | 전문가 | You can:<br>• use lateral thinking to break a problem down into its component parts to identify and diagnose root causes<br>• troubleshoot and identify problems across different technology capabilities including computing, storage, networking, physical infrastructure, software, commercial-off-the-shelf software (COTS) and open source software |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 서비스가 조직 간 돌봄 경로에 어떻게 들어맞는지 분석한다<br>• 임상의, 돌봄 직원, 환자와 협력하여 디지털 서비스를 형성한다<br>• 디지털 결정이 돌봄, 안전, 직원 업무량에 미치는 영향을 설명한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [보안 운영](../../스킬/#보안-운영) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 알림을 모니터링하고 런북을 사용해 분류한다<br>• 증거를 수집하고 이벤트를 상위에 보고한다<br>• 지도를 받아 간단한 탐지 규칙을 조정한다 |
| [취약점 관리](../../스킬/#취약점-관리) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 취약점 관리 정책과 그 목표를 정한다<br>• 기술적 보안 리스크를 시니어 리더에게 보고한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |
| [조직 리스크 관리](../../스킬/#조직-리스크-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 디렉터레이트나 프로그램의 리스크 프로세스를 운영한다<br>• 리스크를 리스크 선호도에 비추어 평가하고 상위에 보고한다<br>• 리스크를 위원회에 보고한다 |
| [피플 매니지먼트](../../스킬/#피플-매니지먼트) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 목표를 설정하고 평가를 하며 팀을 직접 관리한다<br>• 웰빙을 지원하고 근태, 실적, 행위를 관리한다<br>• 팀의 육성과 승계를 계획한다 |
| [예산 관리](../../스킬/#예산-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 예산을 보유하고 관리하며, 차이를 예측하고 설명한다<br>• 비용과 편익을 보여 주는 비즈니스 케이스를 작성한다 |

### 일반적인 자격과 경력

- 여러 팀이나 조직에 걸쳐 인프라 엔지니어링을 이끈 풍부한 경력.

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
| 8 | 재무 및 물적 자원에 대한 책임 | 4 | 32 |
| 9 | 사람에 대한 책임 | 4 | 32 |
| 10 | 정보 자원에 대한 책임 | 5 | 34 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 5 | 45 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **600** (밴드 8b: 585–629) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
