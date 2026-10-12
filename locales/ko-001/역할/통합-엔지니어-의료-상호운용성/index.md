# 통합 엔지니어(의료 상호운용성)

> 이 문서는 일반적인 디지털 헬스케어 조직을 위한 예시용 참조 프로필입니다. 특정 고용주의 공식 직무기술서가 아니며, 직무평가 점수도 공식 평가가 아닙니다.

> 이 글은 AI 어시스턴트가 영어를 한국어로 번역한 것이며, 한국어 원어민의 검토는 아직 받지 않았습니다. 영국 정부 디지털·데이터 전문직 역량 프레임워크(UK GDaD PCF)와 ESCO의 인용문은 영어 그대로 두었습니다.

**직군:** [소프트웨어 개발](../../#소프트웨어-개발)  
**밴드:** 5, 6, 7, 8a  
**UK GDaD PCF 역할:** 없음(이 레퍼런스가 역할을 정의합니다)  
**ESCO 직업:** [integration engineer](http://data.europa.eu/esco/occupation/07e60525-1aad-4099-aaf3-2c7014c92212) (ISCO-08 2511); [database developer](http://data.europa.eu/esco/occupation/b11e1742-5e28-4270-b081-b0193d85ee7d) (ISCO-08 2521)

## 개요

통합 엔지니어는 보건·돌봄 정보가 필요한 곳으로 안전하게 흐르도록 조직의 임상 시스템과 업무 시스템을 연결한다. HL7 FHIR와 HL7 버전 2 같은 표준을 사용하여 인터페이스, API, 메시지 흐름을 설계, 구축, 테스트, 지원하고, 시스템 간에 데이터와 임상 코드를 매핑하며, 운영 중인 연동이 계속 작동하도록 한다.

## 디지털 헬스케어 조직에서

- 검사 결과나 의뢰서 같은 메시지가 유실되거나, 지연되거나, 중복되거나, 잘못 매칭되면 직접적인 해로 이어질 수 있으므로, 연동 작업은 임상 리스크 관리 프로세스를 따른다.
- 연동은 대량의 민감한 건강 정보를 조직 간에 전달하므로, 모든 흐름에는 적법한 근거, 안전한 전송, 감사가 필요하다.
- 보건 시스템은 HL7 버전 2 메시지부터 HL7 FHIR API, IHE 프로파일까지 여러 표준과 버전을 쓰며, 지역별 차이가 있는 경우가 많다.
- 임상적 의미가 교환 과정에서 사라져서는 안 되므로, 엔지니어는 SNOMED CT 같은 임상 용어 체계를 올바르게 매핑하고 환자를 확실하게 매칭한다.
- 많은 연동이 밤낮없이 돌봄을 뒷받침하므로, 모니터링, 경보, 실패한 메시지를 해결하는 명확한 경로가 필요하다.

## 역할 수준

| 밴드 | 직함 | UK GDaD PCF 수준 | 영국 공무원 등급 | 직무평가 점수 |
| --- | --- | --- | --- | --- |
| 5 | [주니어 통합 엔지니어](#밴드-5-주니어-통합-엔지니어) | — | — | 335 |
| 6 | [통합 엔지니어](#밴드-6-통합-엔지니어) | — | — | 418 |
| 7 | [시니어 통합 엔지니어](#밴드-7-시니어-통합-엔지니어) | — | — | 477 |
| 8a | [리드 통합 엔지니어](#밴드-8a-리드-통합-엔지니어) | — | — | 551 |

## 밴드 5: 주니어 통합 엔지니어

주니어 통합 엔지니어는 사양에 따라, 경험 있는 엔지니어의 지도를 받으며 보건·돌봄 시스템 간의 연동을 구축, 테스트, 지원한다.

### 책임

- 합의된 사양에서 메시지 매핑, 변환, API 호출을 구축하고 변경한다.
- 오류와 예외 상황을 포함하여 사양과 샘플 메시지에 비추어 연동을 테스트한다.
- 메시지 흐름을 모니터링하고 실패하거나 거부된 메시지를 조사하여 해결하거나 상위에 보고한다.
- 운영 데이터와 테스트 데이터의 정보 거버넌스 규칙에 따라 건강 데이터를 안전하게 다룬다.
- 임상 안전의 근거로 쓸 수 있도록 변경과 테스트 결과를 기록한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Systems integration](../../스킬/#systems-integration) | UK GDaD PCF | 실무 | You can:<br>• build and test simple interfaces between systems<br>• work on more complex integration as part of a wider team |
| [Programming and build (software engineering)](../../스킬/#programming-and-build-software-engineering) | UK GDaD PCF | 실무 | You can:<br>• design, code, test, correct and document simple programs or scripts under the direction of others |
| [Testing](../../스킬/#testing) | UK GDaD PCF | 실무 | You can:<br>• review requirements and specifications, and define test conditions<br>• identify issues and risks associated with work<br>• analyse and report test activities and results |
| [Service support](../../스킬/#service-support) | UK GDaD PCF | 실무 | You can:<br>• help fix service faults following agreed procedures<br>• carry out maintenance tasks on service support infrastructure |
| [Information security](../../스킬/#information-security) | UK GDaD PCF | 인지 | You can:<br>• explain information security and the security controls available to protect solutions and services |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• FHIR 리소스, 프로파일, API를 읽고 사용한다<br>• 지도를 받아 간단한 연동을 구축하거나 테스트한다<br>• 메시지를 사양에 비추어 확인한다 |
| [임상 용어와 분류](../../스킬/#임상-용어와-분류) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 임상 용어 체계와 분류의 차이를 설명한다<br>• SNOMED CT와 ICD 같은 일반적인 용어 체계를 알아본다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 잘못되었거나, 빠졌거나, 지연된 정보 등을 통해 보건 IT 시스템이 환자에게 어떻게 해를 끼칠 수 있는지 설명한다<br>• 임상 안전 문제 가능성을 올바른 경로로 보고한다 |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 인지 | 할 수 있는 일:<br>• 보건·돌봄 시스템의 주요 부분과 조직이 지원하는 서비스를 설명한다<br>• 자신의 업무에서 환자 안전과 비밀 유지가 중요한 이유를 설명한다 |

### 일반적인 자격과 경력

- 컴퓨팅 또는 관련 분야 학위, 수료한 어프렌티스십, 또는 그에 준하는 경력.

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
| 8 | 재무 및 물적 자원에 대한 책임 | 1 | 5 |
| 9 | 사람에 대한 책임 | 1 | 5 |
| 10 | 정보 자원에 대한 책임 | 4 | 24 |
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 3 | 21 |
| 13 | 신체적 부담 | 2 | 7 |
| 14 | 정신적 부담 | 3 | 12 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **335** (밴드 5: 326–395) |

## 밴드 6: 통합 엔지니어

통합 엔지니어는 보건·돌봄 시스템 간의 연동을 자율적으로 설계, 구축, 지원하며 시스템이 데이터를 어떻게 교환해야 하는지 정의하는 일을 돕는다.

### 책임

- HL7 FHIR, HL7 버전 2, 메시징 패턴을 사용해 연동, API, 메시지 흐름을 설계하고 구축한다.
- 연동 대상 시스템을 분석하고 임상 코드를 포함한 인터페이스 사양과 데이터 매핑을 작성한다.
- 정보가 올바른 기록에 도달하도록 환자 매칭, 검증, 오류 처리를 구축한다.
- 위험 요소 워크숍에 참여하고 실패하거나 지연된 메시지의 경보 같은 안전 통제를 연동에 반영한다.
- 공급자 및 파트너 조직과 협력하여 새로운 연결을 테스트하고 가동한다.
- 운영 중인 연동의 문제를 조사하여 수정하고 주니어 통합 엔지니어를 멘토링한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Systems integration](../../스킬/#systems-integration) | UK GDaD PCF | 실천가 | You can:<br>• define the integration build<br>• co-ordinate build activities across systems<br>• understand how to undertake and support integration testing activities |
| [Programming and build (software engineering)](../../스킬/#programming-and-build-software-engineering) | UK GDaD PCF | 실천가 | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../스킬/#systems-design) | UK GDaD PCF | 실무 | You can:<br>• translate logical designs into physical designs<br>• produce detailed designs<br>• effectively document all work using required standards, methods and tools, including prototyping tools where appropriate<br>• design systems characterised by managed levels of risk, manageable business and technical complexity, and meaningful impact<br>• work with well understood technology and identify appropriate patterns |
| [Service support](../../스킬/#service-support) | UK GDaD PCF | 실천가 | You can:<br>• identify, locate and fix service faults |
| [Information security](../../스킬/#information-security) | UK GDaD PCF | 실무 | You can:<br>• use information security practices and available security controls to contribute to protecting solutions and services |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• FHIR, HL7 버전 2, 메시징 패턴을 사용해 연동을 설계하고 구축한다<br>• FHIR 리소스와 구현 가이드를 작성하고 프로파일링한다<br>• 시스템 간의 복잡한 매핑과 데이터 품질 문제를 해결한다 |
| [임상 용어와 분류](../../스킬/#임상-용어와-분류) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 데이터 항목이나 양식에 맞는 코드를 찾아 사용한다<br>• 용어 브라우저와 참조 세트를 사용한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자신의 업무가 뒷받침하는 임상 및 돌봄 워크플로를 설명한다<br>• 임상 및 돌봄 동료와 일반적인 의료 용어를 올바르게 사용한다<br>• 변경이 환자 돌봄에 영향을 줄 수 있는 때를 알아보고 제기한다 |

### 일반적인 자격과 경력

- 컴퓨팅 또는 관련 분야 학위, 또는 그에 준하는 경력.
- 운영 시스템 간 연동을 구축하고 지원한 경험.

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

## 밴드 7: 시니어 통합 엔지니어

시니어 통합 엔지니어는 여러 시스템과 조직에 걸친 복잡한 연동의 설계와 제공을 이끌고 담당 영역의 연동 기준을 정한다.

### 책임

- 조직 간 공유 돌봄 기록, 검사 결과, 의뢰서 등 복잡한 연동의 기술 설계를 이끈다.
- 조직을 위해 FHIR 프로파일, 구현 가이드, 인터페이스 표준을 작성하고 유지한다.
- 연동이 안전하고, 탄력적이며, 관측 가능하도록 설계하고 장애 해결 경로를 명확히 한다.
- 임상 안전 책임자와 협력하여 연동의 위험 요소를 식별하고 통제가 설계에 반영되어 테스트되도록 한다.
- 정보 거버넌스 동료와 협력하여 각 데이터 흐름에 합의된 적법한 근거와 데이터 공유 약정이 있도록 한다.
- 팀의 통합 엔지니어를 코칭하고 육성한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Systems integration](../../스킬/#systems-integration) | UK GDaD PCF | 전문가 | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Programming and build (software engineering)](../../스킬/#programming-and-build-software-engineering) | UK GDaD PCF | 실천가 | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../스킬/#systems-design) | UK GDaD PCF | 실천가 | You can:<br>• design systems characterised by medium levels of risk, impact, and business or technical complexity<br>• select appropriate design standards, methods and tools, and ensure they are applied effectively<br>• review the systems designs of others to ensure the selection of appropriate technology, efficient use of resources and integration of multiple systems and technology |
| [Information security](../../스킬/#information-security) | UK GDaD PCF | 실천가 | You can:<br>• design solutions and services with security controls included, specifically engineered to mitigate security threats |
| [Stakeholder relationship management](../../스킬/#stakeholder-relationship-management) | UK GDaD PCF | 실무 | You can:<br>• identify important stakeholders and communicate with them clearly and regularly<br>• tailor communication to stakeholders' needs and work with them to build relationships while meeting user needs<br>• build and reach consensus with stakeholders<br>• work to improve stakeholder relationships using evidence to explain decisions |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• FHIR, HL7 버전 2, 메시징 패턴을 사용해 연동을 설계하고 구축한다<br>• FHIR 리소스와 구현 가이드를 작성하고 프로파일링한다<br>• 시스템 간의 복잡한 매핑과 데이터 품질 문제를 해결한다 |
| [임상 용어와 분류](../../스킬/#임상-용어와-분류) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 임상 용어 체계를 사용하여 데이터 모델과 참조 세트를 설계한다<br>• 용어 체계와 분류 사이를 매핑하고 매핑의 한계를 설명한다<br>• 프로덕트와 분석에서의 용어 사용에 대해 팀에 조언한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |
| [아이덴티티 및 접근 관리](../../스킬/#아이덴티티-및-접근-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 사용자 계정과 접근 권한을 생성, 변경, 삭제한다<br>• 접근 권한을 역할 기반 접근 규칙에 비추어 확인한다 |

### 일반적인 자격과 경력

- 보건 분야 또는 그 밖의 복잡한 연동의 설계와 지원에 관한 상당한 경력(석사에 준하는 수준).

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

## 밴드 8a: 리드 통합 엔지니어

리드 통합 엔지니어는 조직의 통합 엔지니어링을 이끌고, 기술적 방향과 기준을 정하며, 여러 시스템에 걸친 핵심 연동을 보증한다.

### 책임

- 조직 전체의 통합 엔지니어링을 이끌고 방향, 패턴, 기준을 정한다.
- 검사 결과, 약물, 경보를 전달하는 것 등 핵심 연동의 설계를 보증한다.
- 아키텍트, 프로덕트 매니저, 공급자와 함께 연동 플랫폼 로드맵을 형성한다.
- 조직 간 상호운용성 및 표준화 활동에서 조직을 대표한다.
- 통합 엔지니어를 직접 관리하거나 이끌고 연동 실천 공동체를 키운다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Systems integration](../../스킬/#systems-integration) | UK GDaD PCF | 전문가 | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Systems design](../../스킬/#systems-design) | UK GDaD PCF | 전문가 | You can:<br>• design systems characterised by high levels of risk, impact, and business or technical complexity<br>• control system design practice within an enterprise or industry architecture<br>• influence industry-based models for the development of new technology applications<br>• develop effective implementation and procurement strategies, consistent with business needs<br>• ensure adherence to relevant technical strategies, policies, standards and practices |
| [Technical design throughout the life cycle](../../스킬/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | 실천가 | You can:<br>• create technical designs characterised by medium risk, impact, and complexity<br>• maintain appropriate quality and architectural coherence of a technical design in response to change<br>• use feedback to optimise and refine technical designs throughout the life cycle |
| [Stakeholder relationship management](../../스킬/#stakeholder-relationship-management) | UK GDaD PCF | 실천가 | You can:<br>• work with the team to develop and maintain an understanding of stakeholders<br>• work with the team to develop and implement stakeholder communications strategies<br>• identify and resolve issues, influence stakeholders and manage relationships effectively<br>• build long-term strategic relationships and communicate clearly and regularly with stakeholders |
| [Leadership and guidance](../../스킬/#leadership-and-guidance) | UK GDaD PCF | 실천가 | You can:<br>• make decisions characterised by medium levels of risk and complexity and recommend decisions as risk and complexity increase<br>• build consensus between services or independent stakeholders<br>• identify problems or issues in the team dynamic and rectify them<br>• engage in varying types of feedback, choosing the right type at the appropriate time and ensuring the discussion and decision stick<br>• bring people together to form a motivated team and help create the right environment for a team to work in<br>• facilitate the best team makeup depending on the situation |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 조직의 상호운용성 표준과 전략을 정한다<br>• 국가 또는 조직 간 표준화 작업을 이끈다<br>• 여러 시스템에 걸친 핵심 연동의 설계를 보증한다 |
| [임상 용어와 분류](../../스킬/#임상-용어와-분류) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 임상 용어 체계를 사용하여 데이터 모델과 참조 세트를 설계한다<br>• 용어 체계와 분류 사이를 매핑하고 매핑의 한계를 설명한다<br>• 프로덕트와 분석에서의 용어 사용에 대해 팀에 조언한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 프로덕트나 변경의 위험 요소 식별과 리스크 평가를 이끈다<br>• 위험 요소 로그와 임상 안전 케이스 보고서를 작성하고 유지한다<br>• 프로덕트 팀과 리스크 통제에 합의하고 그것이 작동하는지 확인한다<br>• 임상 리스크 관리 기준의 적용에 대해 팀에 조언한다 |
| [피플 매니지먼트](../../스킬/#피플-매니지먼트) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 목표를 설정하고 평가를 하며 팀을 직접 관리한다<br>• 웰빙을 지원하고 근태, 실적, 행위를 관리한다<br>• 팀의 육성과 승계를 계획한다 |

### 일반적인 자격과 경력

- 복잡한 보건 또는 돌봄 시스템의 연동 엔지니어링을 이끈 풍부한 경력.

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


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
