# 보안 운영 분석가

> 이 문서는 일반적인 디지털 헬스케어 조직을 위한 예시용 참조 프로필입니다. 특정 고용주의 공식 직무기술서가 아니며, 직무평가 점수도 공식 평가가 아닙니다.

> 이 글은 AI 어시스턴트가 영어를 한국어로 번역한 것이며, 한국어 원어민의 검토는 아직 받지 않았습니다. 영국 정부 디지털·데이터 전문직 역량 프레임워크(UK GDaD PCF)와 ESCO의 인용문은 영어 그대로 두었습니다.

**직군:** [사이버 보안](../../#사이버-보안)  
**밴드:** 5, 6, 7  
**UK GDaD PCF 역할:** 없음(이 레퍼런스가 역할을 정의합니다)  
**ESCO 직업:** [cyber incident responder](http://data.europa.eu/esco/occupation/0ce5a9f4-e00a-4bbe-b255-3c63407167a4) (ISCO-08 2529); [ICT security technician](http://data.europa.eu/esco/occupation/a44a1dc5-be08-4840-8bd5-770c4ac1ca6d) (ISCO-08 3512)

## 개요

보안 운영 분석가는 조직의 시스템과 데이터에 대한 사이버 보안 위협을 감시하고, 조사하고, 대응한다. 보안 모니터링 도구의 경보를 분류하고, 의심스러운 활동을 조사하며, 인시던트를 봉쇄하고, 취약점 수정을 돕는다. 의료에서는 신속한 탐지와 대응이 랜섬웨어 같은 공격으로부터 임상 서비스와 기밀 환자 정보를 보호한다.

## 디지털 헬스케어 조직에서

- 의료는 랜섬웨어와 데이터 탈취의 잦은 표적이며, 한 번의 공격이 조직 전체의 임상 시스템을 멈출 수 있다.
- 서버나 네트워크 일부를 격리하는 등의 봉쇄 결정은 보안 리스크와 환자 돌봄에 대한 영향을 저울질해야 하므로, 분석가는 임상·운영 리드와 협력한다.
- 네트워크에는 보안 에이전트를 실행하지 못하거나 빠르게 패치할 수 없는 의료기기와 레거시 시스템이 포함되므로, 분석가는 네트워크 모니터링과 보완 통제에 의존한다.
- 모니터링은 환자 기록에 대한 접근도 대상으로 하므로, 분석가는 정보 거버넌스와 협력하여 외부 공격뿐 아니라 내부자의 부적절한 접근을 탐지하는 일을 돕는다.
- 보안 모니터링은 종일 운영되므로, 분석가는 교대나 대기 당번으로 일할 수 있다.

## 역할 수준

| 밴드 | 직함 | UK GDaD PCF 수준 | 영국 공무원 등급 | 직무평가 점수 |
| --- | --- | --- | --- | --- |
| 5 | [주니어 보안 운영 분석가](#밴드-5-주니어-보안-운영-분석가) | — | — | 348 |
| 6 | [보안 운영 분석가](#밴드-6-보안-운영-분석가) | — | — | 440 |
| 7 | [시니어 보안 운영 분석가](#밴드-7-시니어-보안-운영-분석가) | — | — | 496 |

## 밴드 5: 주니어 보안 운영 분석가

주니어 보안 운영 분석가는 경험 있는 분석가의 지도를 받으며 보안 경보를 모니터링하고, 런북으로 분류하며, 이벤트를 상위에 보고한다.

### 책임

- 보안 모니터링 및 엔드포인트 도구의 경보를 모니터링하고 런북을 사용해 분류한다.
- 피싱 이메일이나 비정상적인 로그인 등 의심스러운 활동의 증거를 모아 상위에 보고한다.
- 직원이 신고한 피싱 이메일을 확인하고 악성 이메일을 사서함에서 삭제하는 것을 돕는다.
- 이벤트와 조치를 사례 관리 도구에 정확하게 기록한다.
- 취약점 스캔을 실행하고 기한이 된 수정에 대해 시스템 오너에게 상기시킨다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [보안 운영](../../스킬/#보안-운영) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 알림을 모니터링하고 런북을 사용해 분류한다<br>• 증거를 수집하고 이벤트를 상위에 보고한다<br>• 지도를 받아 간단한 탐지 규칙을 조정한다 |
| [취약점 관리](../../스킬/#취약점-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 취약점 스캔을 실행하고 결과를 보고한다<br>• 시스템 담당자와 함께 수정 사항을 추적한다 |
| [아이덴티티 및 접근 관리](../../스킬/#아이덴티티-및-접근-관리) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 접근 규칙을 따르고 자신의 인증 정보를 보호한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 보건·돌봄 시스템의 주요 부분과 조직이 지원하는 서비스를 설명한다<br>• 자신의 업무에서 환자 안전과 비밀 유지가 중요한 이유를 설명한다 |
| [Cyber incident management](../../스킬/#cyber-incident-management) | UK GDaD PCF | 인지 | *Senior leadership skill: the UK GDaD PCF defines it with one statement, not by level.* You can:<br>• implement cyber incident management processes that reflect the level of risk accepted by the organisation<br>• ensure the organisation is prepared for and can effectively respond to incidents<br>• determine the impact of critical incidents on the organisation’s technology<br>• lead the response to critical incidents that affect the whole organisation Examples of leadership using this skill:<br>• helping the incident management team build relationships with senior leaders<br>• leading simulation exercises with the board so they understand their role in incident response processes and the implications of potential incidents<br>• assessing what to communicate to the board, ministers or the whole organisation, and when to do it |
| [Information security](../../스킬/#information-security) | UK GDaD PCF | 인지 | You can:<br>• explain information security and the security controls available to protect solutions and services |
| [Security technology](../../스킬/#security-technology) | UK GDaD PCF | 인지 | You can:<br>• describe some security architectures<br>• explain why security technology is important |

### 일반적인 자격과 경력

- 컴퓨팅 또는 사이버 보안 자격, 사이버 보안 어프렌티스십, 또는 그에 준하는 경력.

### 밴드 개요

- **지식:** 전문적이거나 기술적인 지식. 보통 학위 또는 그에 준하는 경력으로 얻는다.
- **자율성:** 전문직 기준 안에서 폭넓은 목표를 향해 일하며, 자신의 업무를 계획한다.
- **범위:** 팀 또는 프로덕트 안의 자신의 전문 업무.
- **리더십:** 지원 직원이나 어프렌티스를 지도하고 그 업무를 점검할 수 있다.
- **책무:** 자신의 전문 업무의 품질.

### 직무평가(예시)

| # | 요소 | 수준 | 점수 |
| --- | --- | --- | --- |
| 1 | 의사소통 및 관계 형성 기술 | 4 | 32 |
| 2 | 지식, 교육, 경험 | 5 | 120 |
| 3 | 분석 및 판단 기술 | 3 | 27 |
| 4 | 계획 및 조직화 기술 | 2 | 15 |
| 5 | 신체 기술 | 3 | 27 |
| 6 | 환자·이용자 돌봄에 대한 책임 | 1 | 4 |
| 7 | 정책 및 서비스 개발에 대한 책임 | 2 | 12 |
| 8 | 재무 및 물적 자원에 대한 책임 | 2 | 12 |
| 9 | 사람에 대한 책임 | 1 | 5 |
| 10 | 정보 자원에 대한 책임 | 4 | 24 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 3 | 21 |
| 13 | 신체적 부담 | 2 | 7 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **348** (밴드 5: 326–395) |

정신적 부담은 예측하기 어려운 경보의 모니터링과 분류에 장시간 집중하는 경우가 잦음을 반영한다.

## 밴드 6: 보안 운영 분석가

보안 운영 분석가는 보안 인시던트를 조사하고 봉쇄하며, 탐지 규칙을 작성하고, 조직의 보안 모니터링을 개선한다.

### 책임

- 시스템 오너 및 임상 서비스와 협력하여 보안 인시던트를 조사하고, 범위를 파악하고, 봉쇄한다.
- 탐지 규칙을 작성하고 조정하며 의료에 대한 현재의 위협을 바탕으로 위협 헌팅을 수행한다.
- 환자 기록에 대한 부적절한 접근을 모니터링하고 사안을 정보 거버넌스로 넘긴다.
- 임상 서비스와 의료기기에 대한 영향을 포함하여 취약점을 리스크로 평가한다.
- 인시던트 이후 런북과 도구를 개선한다.
- 시간 외 보안 인시던트에 대비해 대기 당번에 참여한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [보안 운영](../../스킬/#보안-운영) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 보안 인시던트를 조사하고 봉쇄한다<br>• 탐지 규칙을 작성하고 위협 헌팅을 수행한다<br>• 인시던트 이후 런북과 도구를 개선한다 |
| [취약점 관리](../../스킬/#취약점-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 취약점 스캔을 실행하고 결과를 보고한다<br>• 시스템 담당자와 함께 수정 사항을 추적한다 |
| [아이덴티티 및 접근 관리](../../스킬/#아이덴티티-및-접근-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 사용자 계정과 접근 권한을 생성, 변경, 삭제한다<br>• 접근 권한을 역할 기반 접근 규칙에 비추어 확인한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자신의 업무가 뒷받침하는 임상 및 돌봄 워크플로를 설명한다<br>• 임상 및 돌봄 동료와 일반적인 의료 용어를 올바르게 사용한다<br>• 변경이 환자 돌봄에 영향을 줄 수 있는 때를 알아보고 제기한다 |
| [조직 리스크 관리](../../스킬/#조직-리스크-관리) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 리스크가 무엇이고 어떻게 제기하는지 설명한다 |
| [Cyber incident management](../../스킬/#cyber-incident-management) | UK GDaD PCF | 실무 | *Senior leadership skill: the UK GDaD PCF defines it with one statement, not by level.* You can:<br>• implement cyber incident management processes that reflect the level of risk accepted by the organisation<br>• ensure the organisation is prepared for and can effectively respond to incidents<br>• determine the impact of critical incidents on the organisation’s technology<br>• lead the response to critical incidents that affect the whole organisation Examples of leadership using this skill:<br>• helping the incident management team build relationships with senior leaders<br>• leading simulation exercises with the board so they understand their role in incident response processes and the implications of potential incidents<br>• assessing what to communicate to the board, ministers or the whole organisation, and when to do it |
| [Information security](../../스킬/#information-security) | UK GDaD PCF | 실무 | You can:<br>• use information security practices and available security controls to contribute to protecting solutions and services |
| [Security technology](../../스킬/#security-technology) | UK GDaD PCF | 실무 | You can:<br>• explain the effect of vulnerabilities on current and future designs<br>• share information on a range of systems, but may specialise in one |

### 일반적인 자격과 경력

- 컴퓨팅 또는 사이버 보안 학위, 관련 보안 인증, 또는 그에 준하는 경력.
- 보안 모니터링 또는 인시던트 대응 경력.

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
| 15 | 감정적 부담 | 2 | 11 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **440** (밴드 6: 396–465) |

정신적 부담은 대기 당번을 포함해 조사 중에 장시간 집중하는 경우가 잦음을 반영한다. 감정적 부담은 환자 기록의 힘든 내용과 진행 중인 인시던트의 압박을 간접적으로 접하는 경우가 잦음을 반영한다.

## 밴드 7: 시니어 보안 운영 분석가

시니어 보안 운영 분석가는 중대한 보안 인시던트에 대한 대응을 이끌고, 위협 헌팅을 이끌며, 보안 운영 팀의 업무를 지도한다.

### 책임

- 랜섬웨어와 데이터 탈취를 포함한 중대한 보안 인시던트에 대한 기술적 대응을 이끌고 인시던트 관리와 조율한다.
- 환자 돌봄에 영향을 주는 봉쇄 결정에 대해 임상·운영 리더에게 조언한다.
- 위협 헌팅과 위협 인텔리전스 업무를 이끌고 의료 보안 파트너와 정보를 공유한다.
- 의료기기 네트워크를 포함하여 탐지 엔지니어링과 모니터링 범위의 우선순위를 정한다.
- 기술 팀과 임상 팀으로 인시던트 대응을 테스트하는 훈련을 이끈다.
- 보안 운영 분석가를 코칭하고 이끈다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [보안 운영](../../스킬/#보안-운영) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 보안 인시던트를 조사하고 봉쇄한다<br>• 탐지 규칙을 작성하고 위협 헌팅을 수행한다<br>• 인시던트 이후 런북과 도구를 개선한다 |
| [취약점 관리](../../스킬/#취약점-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 환자 서비스에 대한 위험을 포함하여 리스크에 따라 취약점의 우선순위를 정한다<br>• 침투 테스트와 시정 조치의 범위를 정하고 관리한다 |
| [아이덴티티 및 접근 관리](../../스킬/#아이덴티티-및-접근-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 사용자 계정과 접근 권한을 생성, 변경, 삭제한다<br>• 접근 권한을 역할 기반 접근 규칙에 비추어 확인한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자신의 업무가 뒷받침하는 임상 및 돌봄 워크플로를 설명한다<br>• 임상 및 돌봄 동료와 일반적인 의료 용어를 올바르게 사용한다<br>• 변경이 환자 돌봄에 영향을 줄 수 있는 때를 알아보고 제기한다 |
| [조직 리스크 관리](../../스킬/#조직-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자기 영역의 리스크를 기록하고 갱신한다<br>• 통제 방안을 제안하고 대응을 추적한다 |
| [Cyber incident management](../../스킬/#cyber-incident-management) | UK GDaD PCF | 실천가 | *Senior leadership skill: the UK GDaD PCF defines it with one statement, not by level.* You can:<br>• implement cyber incident management processes that reflect the level of risk accepted by the organisation<br>• ensure the organisation is prepared for and can effectively respond to incidents<br>• determine the impact of critical incidents on the organisation’s technology<br>• lead the response to critical incidents that affect the whole organisation Examples of leadership using this skill:<br>• helping the incident management team build relationships with senior leaders<br>• leading simulation exercises with the board so they understand their role in incident response processes and the implications of potential incidents<br>• assessing what to communicate to the board, ministers or the whole organisation, and when to do it |
| [Cyber risk management](../../스킬/#cyber-risk-management) | UK GDaD PCF | 실무 | *Senior leadership skill: the UK GDaD PCF defines it with one statement, not by level.* You can:<br>• maintain a clear understanding of the cyber and information security risks across the whole organisation<br>• develop and implement risk assessment processes<br>• oversee the assessment of the organisation's partners and supply chain for potential threats or vulnerabilities Examples of leadership using this skill:<br>• building a culture where teams have awareness of, and take responsibility for, risks and mitigating them<br>• advising programme owners and people running IT services about risks in a way that enables them to act on that advice<br>• communicating with senior leaders in a way that enables them to make decisions about accepting or mitigating risk |
| [Information security](../../스킬/#information-security) | UK GDaD PCF | 실천가 | You can:<br>• design solutions and services with security controls included, specifically engineered to mitigate security threats |
| [Security technology](../../스킬/#security-technology) | UK GDaD PCF | 실천가 | This skill level is currently not defined. |

### 일반적인 자격과 경력

- 보안 운영과 인시던트 대응에 관한 상당한 경력(대학원 디플로마에 준하는 수준).
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
| 15 | 감정적 부담 | 2 | 11 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **496** (밴드 7: 466–539) |

정신적 부담과 감정적 부담은 흔히 시간 외에, 임상 서비스가 위험에 처한 상황에서 압박 속에 중대한 인시던트에 대한 대응을 이끄는 것을 반영한다.


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
