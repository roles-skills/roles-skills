# 보안 엔지니어

> 이 문서는 일반적인 디지털 헬스케어 조직을 위한 예시용 참조 프로필입니다. 특정 고용주의 공식 직무기술서가 아니며, 직무평가 점수도 공식 평가가 아닙니다.

> 이 글은 AI 어시스턴트가 영어를 한국어로 번역한 것이며, 한국어 원어민의 검토는 아직 받지 않았습니다. 영국 정부 디지털·데이터 전문직 역량 프레임워크(UK GDaD PCF)와 ESCO의 인용문은 영어 그대로 두었습니다.

**직군:** [사이버 보안](../../#사이버-보안)  
**밴드:** 6, 7, 8a  
**UK GDaD PCF 역할:** 없음(이 레퍼런스가 역할을 정의합니다)  
**ESCO 직업:** [ICT security administrator](http://data.europa.eu/esco/occupation/0464b062-cea6-4164-b10d-956c61956ae7) (ISCO-08 2529)

## 개요

보안 엔지니어는 조직의 시스템, 데이터, 이용자를 보호하는 기술적 보안 통제를 설계, 구축, 운영한다. 아이덴티티와 접근, 엔드포인트와 네트워크 보호, 암호화, 로깅, 클라우드 보안을 다루며, 프로덕트 팀과 인프라 팀이 보안을 내재화하도록 돕는다. 의료에서는 현장의 임상의 접근을 빠르게 유지하면서 임상 시스템과 환자 데이터를 보호한다.

## 디지털 헬스케어 조직에서

- 보안 통제는 긴급한 돌봄을 방해해서는 안 되므로, 엔지니어는 공용 임상 워크스테이션에서도 빠르게 작동하는 강력한 인증을 설계한다.
- 의료기기와 레거시 임상 시스템은 패치를 적용하지 못하거나 보안 소프트웨어를 실행하지 못하는 경우가 많으므로, 엔지니어는 네트워크 세그먼테이션과 보완 통제를 설계한다.
- 랜섬웨어는 의료에 큰 위협이므로, 엔지니어는 시스템을 견고하게 만들고, 백업을 보호하며, 공격이 번지는 범위를 제한한다.
- 임상 시스템은 제3자가 제공하고 지원하는 경우가 많으므로, 엔지니어는 공급자의 보안을 평가하고 그 원격 접근을 통제한다.
- 임상 시스템의 보안 통제 변경은 변경 관리를 거치고, 필요하면 임상 안전 검토를 받는다.

## 역할 수준

| 밴드 | 직함 | UK GDaD PCF 수준 | 영국 공무원 등급 | 직무평가 점수 |
| --- | --- | --- | --- | --- |
| 6 | [보안 엔지니어](#밴드-6-보안-엔지니어) | — | — | 434 |
| 7 | [시니어 보안 엔지니어](#밴드-7-시니어-보안-엔지니어) | — | — | 490 |
| 8a | [리드 보안 엔지니어](#밴드-8a-리드-보안-엔지니어) | — | — | 560 |

## 밴드 6: 보안 엔지니어

보안 엔지니어는 보안 통제와 도구를 구축, 설정, 유지하고 팀이 보안상의 약점을 수정하도록 돕는다.

### 책임

- 엔드포인트 보호, 방화벽, 이메일 보안, 보안 로그 등 보안 통제를 구축하고 유지한다.
- 다중 인증과 특권 접근을 포함하여 아이덴티티 및 접근 통제를 설정한다.
- 인프라 팀과 프로덕트 팀이 취약점을 수정하고 합의된 기준에 따라 시스템을 견고하게 만들도록 돕는다.
- 인프라 팀 및 임상 공학 팀과 협력하여 의료기기와 레거시 시스템을 보호하도록 네트워크를 세그먼트화한다.
- 새 시스템과 공급자의 원격 접근의 보안을 가동 전에 검토한다.
- 보안 인시던트 대응을 지원하기 위해 대기 당번에 참여한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Security technology](../../스킬/#security-technology) | UK GDaD PCF | 실무 | You can:<br>• explain the effect of vulnerabilities on current and future designs<br>• share information on a range of systems, but may specialise in one |
| [Information security](../../스킬/#information-security) | UK GDaD PCF | 실무 | You can:<br>• use information security practices and available security controls to contribute to protecting solutions and services |
| [Cyber incident management](../../스킬/#cyber-incident-management) | UK GDaD PCF | 인지 | *Senior leadership skill: the UK GDaD PCF defines it with one statement, not by level.* You can:<br>• implement cyber incident management processes that reflect the level of risk accepted by the organisation<br>• ensure the organisation is prepared for and can effectively respond to incidents<br>• determine the impact of critical incidents on the organisation’s technology<br>• lead the response to critical incidents that affect the whole organisation Examples of leadership using this skill:<br>• helping the incident management team build relationships with senior leaders<br>• leading simulation exercises with the board so they understand their role in incident response processes and the implications of potential incidents<br>• assessing what to communicate to the board, ministers or the whole organisation, and when to do it |
| [아이덴티티 및 접근 관리](../../스킬/#아이덴티티-및-접근-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 사용자 계정과 접근 권한을 생성, 변경, 삭제한다<br>• 접근 권한을 역할 기반 접근 규칙에 비추어 확인한다 |
| [취약점 관리](../../스킬/#취약점-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 취약점 스캔을 실행하고 결과를 보고한다<br>• 시스템 담당자와 함께 수정 사항을 추적한다 |
| [보안 운영](../../스킬/#보안-운영) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 알림을 모니터링하고 런북을 사용해 분류한다<br>• 증거를 수집하고 이벤트를 상위에 보고한다<br>• 지도를 받아 간단한 탐지 규칙을 조정한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자신의 업무가 뒷받침하는 임상 및 돌봄 워크플로를 설명한다<br>• 임상 및 돌봄 동료와 일반적인 의료 용어를 올바르게 사용한다<br>• 변경이 환자 돌봄에 영향을 줄 수 있는 때를 알아보고 제기한다 |

### 일반적인 자격과 경력

- 컴퓨팅 또는 사이버 보안 학위, 관련 보안 인증, 또는 그에 준하는 경력.
- 인프라 또는 보안 도구를 구축하거나 운영한 경험.

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

정신적 부담은 대기 당번을 포함해 복잡한 기술 업무와 인시던트 지원에 장시간 집중하는 경우가 잦음을 반영한다.

## 밴드 7: 시니어 보안 엔지니어

시니어 보안 엔지니어는 중요한 보안 통제의 제공을 설계하고 이끌며, 안전한 설계에 대해 팀에 조언한다.

### 책임

- 특권 접근 관리, 보안 모니터링, 백업 보호 등 보안 통제를 설계하고 제공을 이끈다.
- 임상용 및 환자용 서비스의 안전한 설계에 대해 프로덕트 팀과 인프라 팀에 조언한다.
- 의료기기와 패치할 수 없는 그 밖의 시스템을 위한 보완 통제를 설계한다.
- 클라우드 서비스를 포함하여 공급자와 그 제품의 보안을 평가한다.
- 기술적 전문성과 복구 계획으로 중대한 보안 인시던트에 대한 대응을 지원한다.
- 보안 엔지니어를 코칭하고 팀 전반에 우수 사례를 공유한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Security technology](../../스킬/#security-technology) | UK GDaD PCF | 실천가 | This skill level is currently not defined. |
| [Information security](../../스킬/#information-security) | UK GDaD PCF | 실천가 | You can:<br>• design solutions and services with security controls included, specifically engineered to mitigate security threats |
| [Designing secure systems](../../스킬/#designing-secure-systems) | UK GDaD PCF | 실무 | You can:<br>• design and review system architectures through the application of patterns and principles |
| [Cyber risk management](../../스킬/#cyber-risk-management) | UK GDaD PCF | 실무 | *Senior leadership skill: the UK GDaD PCF defines it with one statement, not by level.* You can:<br>• maintain a clear understanding of the cyber and information security risks across the whole organisation<br>• develop and implement risk assessment processes<br>• oversee the assessment of the organisation's partners and supply chain for potential threats or vulnerabilities Examples of leadership using this skill:<br>• building a culture where teams have awareness of, and take responsibility for, risks and mitigating them<br>• advising programme owners and people running IT services about risks in a way that enables them to act on that advice<br>• communicating with senior leaders in a way that enables them to make decisions about accepting or mitigating risk |
| [아이덴티티 및 접근 관리](../../스킬/#아이덴티티-및-접근-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 아이덴티티 및 접근 서비스를 설계하고 운영한다<br>• 접근 권한을 정기적으로 검토하고 문제를 수정한다 |
| [취약점 관리](../../스킬/#취약점-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 환자 서비스에 대한 위험을 포함하여 리스크에 따라 취약점의 우선순위를 정한다<br>• 침투 테스트와 시정 조치의 범위를 정하고 관리한다 |
| [보안 운영](../../스킬/#보안-운영) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 알림을 모니터링하고 런북을 사용해 분류한다<br>• 증거를 수집하고 이벤트를 상위에 보고한다<br>• 지도를 받아 간단한 탐지 규칙을 조정한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자신의 업무가 뒷받침하는 임상 및 돌봄 워크플로를 설명한다<br>• 임상 및 돌봄 동료와 일반적인 의료 용어를 올바르게 사용한다<br>• 변경이 환자 돌봄에 영향을 줄 수 있는 때를 알아보고 제기한다 |

### 일반적인 자격과 경력

- 보안 엔지니어링에 관한 상당한 경력(대학원 디플로마에 준하는 수준).
- 관련 고급 보안 인증, 또는 그에 준하는 경력.

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

## 밴드 8a: 리드 보안 엔지니어

리드 보안 엔지니어는 보안 엔지니어링의 기술적 방향을 정하고 조직 전반에서 통제가 함께 작동하도록 한다.

### 책임

- 조직 전반의 보안 통제에 대한 기술적 방향과 기준을 정한다.
- 클라우드 호스팅으로의 이전이나 새 전자 환자 기록 등 주요 프로그램의 보안 설계를 이끈다.
- 통제가 랜섬웨어를 막고 임상 시스템의 빠르고 안전한 복구를 뒷받침하도록 한다.
- 접근과 인증에 대해 임상 리드와 협력하여 보안과 임상에서의 사용 편의의 균형을 맞춘다.
- 기술적 리스크와 투자에 대해 사이버 보안 매니저에게 조언한다.
- 보안 엔지니어를 이끌고 육성한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Security technology](../../스킬/#security-technology) | UK GDaD PCF | 전문가 | You can:<br>• explain complex system architectures<br>• identify and explain how easy or difficult it will be to exploit vulnerabilities<br>• lead and influence security technology in the security industry |
| [Information security](../../스킬/#information-security) | UK GDaD PCF | 실천가 | You can:<br>• design solutions and services with security controls included, specifically engineered to mitigate security threats |
| [Designing secure systems](../../스킬/#designing-secure-systems) | UK GDaD PCF | 실천가 | You can:<br>• design and review system architectures through the development of patterns and principles |
| [Cyber risk management](../../스킬/#cyber-risk-management) | UK GDaD PCF | 실천가 | *Senior leadership skill: the UK GDaD PCF defines it with one statement, not by level.* You can:<br>• maintain a clear understanding of the cyber and information security risks across the whole organisation<br>• develop and implement risk assessment processes<br>• oversee the assessment of the organisation's partners and supply chain for potential threats or vulnerabilities Examples of leadership using this skill:<br>• building a culture where teams have awareness of, and take responsibility for, risks and mitigating them<br>• advising programme owners and people running IT services about risks in a way that enables them to act on that advice<br>• communicating with senior leaders in a way that enables them to make decisions about accepting or mitigating risk |
| [아이덴티티 및 접근 관리](../../스킬/#아이덴티티-및-접근-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 아이덴티티 및 접근 서비스를 설계하고 운영한다<br>• 접근 권한을 정기적으로 검토하고 문제를 수정한다 |
| [취약점 관리](../../스킬/#취약점-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 환자 서비스에 대한 위험을 포함하여 리스크에 따라 취약점의 우선순위를 정한다<br>• 침투 테스트와 시정 조치의 범위를 정하고 관리한다 |
| [보안 운영](../../스킬/#보안-운영) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 보안 인시던트를 조사하고 봉쇄한다<br>• 탐지 규칙을 작성하고 위협 헌팅을 수행한다<br>• 인시던트 이후 런북과 도구를 개선한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자신의 업무가 뒷받침하는 임상 및 돌봄 워크플로를 설명한다<br>• 임상 및 돌봄 동료와 일반적인 의료 용어를 올바르게 사용한다<br>• 변경이 환자 돌봄에 영향을 줄 수 있는 때를 알아보고 제기한다 |
| [피플 매니지먼트](../../스킬/#피플-매니지먼트) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 일상 업무를 감독하고 피드백을 준다<br>• 채용과 입사 교육에 참여한다<br>• 정기적으로 1대1 면담을 한다 |

### 일반적인 자격과 경력

- 복잡한 서비스의 보안 엔지니어링을 이끈 풍부한 경력.

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


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
