# 머신러닝 엔지니어

> 이 문서는 일반적인 디지털 헬스케어 조직을 위한 예시용 참조 프로필입니다. 특정 고용주의 공식 직무기술서가 아니며, 직무평가 점수도 공식 평가가 아닙니다.

> 이 글은 AI 어시스턴트가 영어를 한국어로 번역한 것이며, 한국어 원어민의 검토는 아직 받지 않았습니다. 영국 정부 디지털·데이터 전문직 역량 프레임워크(UK GDaD PCF)와 ESCO의 인용문은 영어 그대로 두었습니다.

**직군:** [데이터](../../#데이터)  
**밴드:** 7, 8b  
**UK GDaD PCF 역할:** [Machine learning engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/machine-learning-engineer/)  
**ESCO 직업:** [artificial intelligence engineer](http://data.europa.eu/esco/occupation/35553663-deab-4d9a-bf22-15c1625d28e8) (ISCO-08 2511)

## 개요

머신러닝 엔지니어는 데이터 사이언티스트가 만들었거나 공급자로부터 구매한 모델이 운영 중인 보건·돌봄 서비스에서 확실히 작동하도록 한다. 모델을 학습, 테스트, 배포, 모니터링하는 파이프라인을 구축하고 임상·운영 시스템과 통합한다. 실제 환자와 직원이 의존하게 된 뒤에도 모델이 안전하고, 견고하고, 공정하며, 유효하게 유지되도록 한다.

## 디지털 헬스케어 조직에서

- 가동 중인 모델은 환자 집단, 임상 실무, 기록 습관이 변함에 따라 드리프트할 수 있으므로, 성능은 환자 집단별로 모니터링되고 필요하면 모델을 재학습하거나 철회한다.
- 진단, 트리아지, 치료에 정보를 제공하는 모델은 의료기기로 규제될 수 있으므로, 그 소프트웨어 생애 주기, 변경 관리, 시판 후 감시에 공식 요건이 생긴다.
- 임상 안전 케이스에는 모델이 어떻게 실패하는지, 출력이 임상의에게 어떻게 표시되는지, 모델을 쓸 수 없을 때 어떻게 되는지에 대한 근거가 필요하다.
- 환자 데이터로 학습한 모델은 개인에 관한 정보를 누설할 수 있으므로, 학습 데이터, 모델 결과물, 로그는 데이터 자체와 같이 보호된다.
- 생성형 AI와 대규모 언어 모델에는 임상 기록에 지어낸 내용이 섞여 들어가는 등 추가적인 리스크가 있어 고유한 테스트와 사람의 감독이 필요하다.

## UK GDaD PCF 역할 설명(원문은 영어)

> A machine learning engineer develops, assures and maintains machine learning models so they can be used in products and services.
> 
> In this role, you will:
> - be responsible for the software development and technical infrastructure needed to design, train, deploy and scale machine learning models
> - provide and maintain effective, secure and sustainable machine learning models for use in products and services
> - support all stages of the machine learning life cycle
> - help product teams evaluate and choose appropriate machine learning solutions

## 역할 수준

| 밴드 | 직함 | UK GDaD PCF 수준 | 영국 공무원 등급 | 직무평가 점수 |
| --- | --- | --- | --- | --- |
| 7 | [시니어 머신러닝 엔지니어](#밴드-7-시니어-머신러닝-엔지니어) | Senior machine learning engineer | SEO/G7/G6 | 495 |
| 8b | [리드 머신러닝 엔지니어](#밴드-8b-리드-머신러닝-엔지니어) | Lead machine learning engineer | G7/G6 | 595 |

## 밴드 7: 시니어 머신러닝 엔지니어

**UK GDaD PCF 수준: Senior machine learning engineer**

> A senior machine learning engineer develops machine learning models so they can be used in products and services.
> 
> At this role level, you will:
> - decide what model is most suitable for use in products and services
> - customise, optimise, re-train and maintain existing models
> - deploy models into production, testing and assuring them to ensure they meet performance requirements
> - work with others to integrate models with existing systems
> - check that models used in live products and services stay safe, secure and continue to work effectively

### 책임

- 자동화 테스트, 버전 관리, 롤백을 갖추어 운영 임상·업무 서비스에 모델을 배포한다.
- 모델 성능, 드리프트, 환자 집단 간 공정성을 모니터링하는 체계를 경보와 명확한 오너와 함께 구축한다.
- 가능한 한 HL7 FHIR 같은 개방형 표준을 사용하여 모델을 임상 시스템과 통합한다.
- 임상 안전 케이스와 의료기기 기술 문서에 필요한 테스트, 변경, 모니터링 근거를 만든다.
- 생성형 AI 모델을 포함해 공급자와 오픈소스 모델을 지역에서의 사용을 위해 평가하고 조정한다.
- 머신러닝 엔지니어링 관행에 대해 데이터 사이언티스트와 엔지니어를 코칭한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Applied maths, statistics and scientific practices](../../스킬/#applied-maths-statistics-and-scientific-practices) | UK GDaD PCF | 실천가 | You can:<br>• apply designated quantitative techniques such as time series analysis, optimisation and simulation to create and embed appropriate models for analysis and prediction<br>• provide guidance on matching data sources with relevant applied mathematics and statistical techniques to meet analysis goals<br>• apply appropriate statistical techniques to available data to discover new relations and offer insight into research problems, helping to improve organisational processes and support decision making<br>• access and use the statistical tools available within the organisation |
| [Communicating between the technical and non-technical](../../스킬/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 실천가 | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Data ethics and privacy](../../스킬/#data-ethics-and-privacy) | UK GDaD PCF | 실천가 | You can:<br>• work with stakeholders to identify and address ethical and privacy concerns<br>• demonstrate and communicate how data ethical issues fit into the wider organisational context<br>• research developments in data ethics and privacy to improve compliance and processes<br>• assess and constructively challenge proposed data ethics policies |
| [Data science innovation](../../스킬/#data-science-innovation) | UK GDaD PCF | 실천가 | You can:<br>• demonstrate practical knowledge of data science tools and techniques<br>• develop data science solutions that maximise insight<br>• identify opportunities for how data science can improve data practices |
| [Programming and build (software engineering)](../../스킬/#programming-and-build-software-engineering) | UK GDaD PCF | 실천가 | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems integration](../../스킬/#systems-integration) | UK GDaD PCF | 실천가 | You can:<br>• define the integration build<br>• co-ordinate build activities across systems<br>• understand how to undertake and support integration testing activities |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 자신의 업무가 뒷받침하는 임상 및 돌봄 워크플로를 설명한다<br>• 임상 및 돌봄 동료와 일반적인 의료 용어를 올바르게 사용한다<br>• 변경이 환자 돌봄에 영향을 줄 수 있는 때를 알아보고 제기한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 위험 요소 워크숍에 참여하고 위험 요소 로그에 기여한다<br>• 자신의 업무에 대해 임상 리스크 관리 프로세스를 따른다<br>• 테스트 결과 같은 임상 안전 케이스의 근거를 제공한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 개인정보 보호 원칙을 자신의 업무에 적용한다<br>• 개인정보 영향평가에 기여한다<br>• 정보 요청과 기록을 올바르게 처리한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• FHIR 리소스, 프로파일, API를 읽고 사용한다<br>• 지도를 받아 간단한 연동을 구축하거나 테스트한다<br>• 메시지를 사양에 비추어 확인한다 |
| [의료기기 소프트웨어 규제](../../스킬/#의료기기-소프트웨어-규제) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 의료기기 표준을 충족하는 소프트웨어 생애 주기 프로세스를 따른다<br>• 그 프로세스가 요구하는 기록을 작성한다 |
| [보건·돌봄 분야의 안전하고 공정한 AI](../../스킬/#보건돌봄-분야의-안전하고-공정한-ai) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 임상 동료와 함께 모델의 검증, 편향 평가, 실제 운영 중 모니터링을 계획한다<br>• 모델을 재학습하거나, 제한하거나, 철회해야 하는 시점을 판단한다<br>• 모델이 의료기기로 규제될 수 있는 시점과 필요한 근거에 대해 팀에 조언한다 |

### 일반적인 자격과 경력

- 운영 환경의 머신러닝 시스템을 구축하고 운영한 상당한 경력(석사에 준하는 수준).

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
| | **합계** | | **495** (밴드 7: 466–539) |

## 밴드 8b: 리드 머신러닝 엔지니어

**UK GDaD PCF 수준: Lead machine learning engineer**

> A lead machine learning engineer leads the technical development and deployment of machine learning models.
> 
> At this role level, you will:
> - lead the most complex technical work needed to develop models for use in products and services
> - co-ordinate moving a model from the research and development stage to production
> - define ways of working across the machine learning life cycle
> - identify training needs for machine learning engineers and related roles
> - help your team work with other teams and disciplines
> - assure the effectiveness of machine learning models in use across the organisation
> - define and communicate software standards and guidelines related to ethics, risk and security

### 책임

- 연구에서 조직 전체의 안전한 실제 운영으로 모델을 옮기는 가장 복잡한 작업을 이끈다.
- 규제 대상이거나 안전이 중요한 모델에 필요한 통제를 포함하여 머신러닝 생애 주기를 정의한다.
- 모델 테스트, 모니터링, 보안, 윤리의 기준을 정하고 가동 중인 모델을 보증한다.
- 임상 안전 책임자, 정보 거버넌스, 규제 전문가와 협력하여 모델을 어떻게 평가하고 승인할지 합의한다.
- 교육 필요를 파악하고 머신러닝 엔지니어와 관련 역할을 육성한다.

### 스킬

| 스킬 | 출처 | 기대 수준 | 이 수준의 의미 |
| --- | --- | --- | --- |
| [Applied maths, statistics and scientific practices](../../스킬/#applied-maths-statistics-and-scientific-practices) | UK GDaD PCF | 실천가 | You can:<br>• apply designated quantitative techniques such as time series analysis, optimisation and simulation to create and embed appropriate models for analysis and prediction<br>• provide guidance on matching data sources with relevant applied mathematics and statistical techniques to meet analysis goals<br>• apply appropriate statistical techniques to available data to discover new relations and offer insight into research problems, helping to improve organisational processes and support decision making<br>• access and use the statistical tools available within the organisation |
| [Communicating between the technical and non-technical](../../스킬/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 전문가 | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Data ethics and privacy](../../스킬/#data-ethics-and-privacy) | UK GDaD PCF | 실천가 | You can:<br>• work with stakeholders to identify and address ethical and privacy concerns<br>• demonstrate and communicate how data ethical issues fit into the wider organisational context<br>• research developments in data ethics and privacy to improve compliance and processes<br>• assess and constructively challenge proposed data ethics policies |
| [Data science innovation](../../스킬/#data-science-innovation) | UK GDaD PCF | 전문가 | You can:<br>• be a leader in the data science space<br>• demonstrate in-depth knowledge of data science tools and techniques, which you can use to solve problems creatively and to create opportunities for your team<br>• act as a coach, inspiring curiosity and creativity in others<br>• demonstrate in-depth knowledge of your chosen profession and keep up to date with changes in the industry<br>• challenge the status quo and always look for ways to improve data science |
| [Programming and build (software engineering)](../../스킬/#programming-and-build-software-engineering) | UK GDaD PCF | 전문가 | You can:<br>• advise on the right way to apply standards and methods to ensure compliance<br>• maintain technical responsibility for all the stages and iterations of a software development project<br>• provide technical advice to stakeholders and set the team-based standards for programming tools and techniques |
| [Systems integration](../../스킬/#systems-integration) | UK GDaD PCF | 전문가 | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [보건·돌봄 서비스 이해](../../스킬/#보건돌봄-서비스-이해) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 서비스가 조직 간 돌봄 경로에 어떻게 들어맞는지 분석한다<br>• 임상의, 돌봄 직원, 환자와 협력하여 디지털 서비스를 형성한다<br>• 디지털 결정이 돌봄, 안전, 직원 업무량에 미치는 영향을 설명한다 |
| [임상 리스크 관리](../../스킬/#임상-리스크-관리) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 프로덕트나 변경의 위험 요소 식별과 리스크 평가를 이끈다<br>• 위험 요소 로그와 임상 안전 케이스 보고서를 작성하고 유지한다<br>• 프로덕트 팀과 리스크 통제에 합의하고 그것이 작동하는지 확인한다<br>• 임상 리스크 관리 기준의 적용에 대해 팀에 조언한다 |
| [정보 거버넌스와 개인정보 보호](../../스킬/#정보-거버넌스와-개인정보-보호) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 개인정보 영향평가와 정보 공유 협약을 이끈다<br>• 적법한 근거, 동의, 비밀 유지, 보존에 대해 팀에 조언한다<br>• 인시던트를 조사하고 개선을 권고한다 |
| [보건 데이터 상호운용성](../../스킬/#보건-데이터-상호운용성) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• FHIR, HL7 버전 2, 메시징 패턴을 사용해 연동을 설계하고 구축한다<br>• FHIR 리소스와 구현 가이드를 작성하고 프로파일링한다<br>• 시스템 간의 복잡한 매핑과 데이터 품질 문제를 해결한다 |
| [의료기기 소프트웨어 규제](../../스킬/#의료기기-소프트웨어-규제) | 이 레퍼런스 | 실천가 | 할 수 있는 일:<br>• 제품이 의료기기인지와 그 가능성이 높은 등급을 평가한다<br>• 품질 및 임상 동료와 함께 제품의 규제 대응 작업을 계획한다 |
| [보건·돌봄 분야의 안전하고 공정한 AI](../../스킬/#보건돌봄-분야의-안전하고-공정한-ai) | 이 레퍼런스 | 전문가 | 할 수 있는 일:<br>• 돌봄 분야 AI의 보증과 모니터링에 관한 조직의 기준을 정한다<br>• 고위험 모델의 배포 전후 보증을 이끈다<br>• 안전하고 공정한 AI에 관해 규제 기관과 파트너에게 조직을 대표한다 |
| [피플 매니지먼트](../../스킬/#피플-매니지먼트) | 이 레퍼런스 | 실무 | 할 수 있는 일:<br>• 일상 업무를 감독하고 피드백을 준다<br>• 채용과 입사 교육에 참여한다<br>• 정기적으로 1대1 면담을 한다 |

### 일반적인 자격과 경력

- 복잡하거나 규제 대상인 서비스의 머신러닝 엔지니어링을 이끈 풍부한 경력.

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
| 11 | 연구 및 개발에 대한 책임 | 2 | 12 |
| 12 | 행동의 자유 | 5 | 45 |
| 13 | 신체적 부담 | 1 | 3 |
| 14 | 정신적 부담 | 4 | 18 |
| 15 | 감정적 부담 | 1 | 5 |
| 16 | 근무 환경 | 2 | 7 |
| | **합계** | | **595** (밴드 8b: 585–629) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
