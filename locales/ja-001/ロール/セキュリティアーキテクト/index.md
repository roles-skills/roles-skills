# セキュリティアーキテクト

> これは、一般的なデジタルヘルスケア組織のための例示的な参照プロファイルです。特定の雇用主の公式な職務記述書ではなく、職務評価のスコアも正式な評価ではありません。

> このテキストは英語から AI アシスタントによって翻訳されたもので、日本語を母語とする方による確認はまだ行われていません。英国政府デジタル・データ専門職能力フレームワーク(UK GDaD PCF)と ESCO からの引用は英語のままです。

**職群:** [アーキテクチャ](../../#アーキテクチャ)  
**バンド:** 8a, 8b, 8c  
**UK GDaD PCF のロール:** [Security architect](https://understand-digital-data-roles-skills.service.gov.uk/role/security-architect/)  
**ESCO の職業:** [ICT system architect](http://data.europa.eu/esco/occupation/e1c72b5f-4c5c-487c-a6df-e84b64a51dae) (ISCO-08 2511); [cybersecurity risk manager](http://data.europa.eu/esco/occupation/7754d570-9519-48c2-b1c9-8e165f8bca0f) (ISCO-08 2529)

## 概要

セキュリティアーキテクトは、患者情報が機密に保たれ、正確で、ケアが必要とするときに利用できるよう、組織のデジタルヘルスサービスのセキュリティを設計する。セキュリティのパターンと管理策を定め、新しい設計や供給者のセキュリティリスクを評価し、サービスを臨床医と患者にとって安全で使いやすいものに保つ、リスクに基づく判断をチームが行うのを手助けする。

## デジタルヘルスケア組織において

- 医療機関はランサムウェアやデータ窃取の標的になりやすく、攻撃は臨床サービスを止めうるため、可用性は機密性と同じくらい重要である。
- セキュリティの管理策は緊急のケアの妨げになってはならないため、設計は強力な認証と、臨床現場での迅速なアクセスのバランスをとる。
- 接続された医療機器やレガシーな臨床システムは、すぐにはパッチを当てられないことが多いため、アーキテクトはセグメンテーションなどの代替管理策を設計する。
- 多くの職員、パートナー組織、供給者が患者記録へのアクセスを必要とするため、アイデンティティ、ロールベースのアクセス、監査が中心になる。
- セキュリティの設計は、情報ガバナンスの義務や、ISO/IEC 27001 などの公表されたセキュリティ標準を支えなければならない。

## UK GDaD PCF のロール説明(原文は英語)

> A security architect designs and builds secure solutions.

## ロールレベル

| バンド | 名称 | UK GDaD PCF のレベル | 英国公務員の等級 | 職務評価の点数 |
| --- | --- | --- | --- | --- |
| 8a | [セキュリティアーキテクト](#バンド-8a-セキュリティアーキテクト) | Security architect | HEO/SEO/G7 | 560 |
| 8b | [リード セキュリティアーキテクト](#バンド-8b-リード-セキュリティアーキテクト) | Lead security architect | G7/G6 | 613 |
| 8c | [プリンシパル セキュリティアーキテクト](#バンド-8c-プリンシパル-セキュリティアーキテクト) | Principal security architect | G6 | 662 |

## バンド 8a: セキュリティアーキテクト

**UK GDaD PCF のレベル: Security architect**

> A security architect creates and designs security for a system or service, maintains security documentation and develops architecture patterns and security approaches to new technologies.
> 
> At this role level, you will:
> - recommend security controls and identify solutions that support a business objective
> - provide specialist advice and recommend approaches across teams and various stakeholders
> - communicate widely with other stakeholders
> - advise on important security-related technologies and assess the risk associated with proposed changes
> - inspire and influence others to execute security principles
> - help review other people’s work

### 責任

- アイデンティティ、暗号化、ロギング、ネットワーク保護を含め、サービスとシステムのセキュリティ管理策を設計する。
- 新しい設計と供給者の製品のセキュリティを評価し、リスクと推奨される管理策を記録する。
- 患者のログインや職員のシングルサインオンなど、デリバリーチームが再利用できるセキュリティパターンを開発する。
- 簡単に更新できない医療機器やレガシーな臨床システムのための代替管理策について助言する。
- 情報ガバナンスと臨床安全の同僚と協力して、セキュリティ、プライバシー、安全のリスクを合わせて評価する。
- セキュリティエンジニアや他のアーキテクトを、安全な設計についてコーチする。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Analysis](../../スキル/#analysis) | UK GDaD PCF | 実務 | You can:<br>• apply the approach to real problems and consider all relevant information<br>• apply appropriate rigour to ensure a full solution is designed and achieves the business outcome |
| [Communication (security architect)](../../スキル/#communication-security-architect) | UK GDaD PCF | 実践者 | You can:<br>• demonstrate a deep understanding of security concepts and can apply them to a technical level<br>• effectively translate and accurately communicate security and risk implications to technical and non-technical stakeholders<br>• successfully respond to challenges<br>• manage stakeholder expectations and be flexible, adapting to stakeholder reactions to reach consensus |
| [Designing secure systems](../../スキル/#designing-secure-systems) | UK GDaD PCF | 実務 | You can:<br>• design and review system architectures through the application of patterns and principles |
| [Enabling and informing risk-based decisions](../../スキル/#enabling-and-informing-risk-based-decisions) | UK GDaD PCF | 実務 | You can:<br>• work with risk owners to advise and give feedback<br>• advise on risk impact and whether it's within risk tolerance<br>• describe different risk methodologies and how these are applied, as well as the proportionality of risk |
| [Research and innovation](../../スキル/#research-and-innovation) | UK GDaD PCF | 実務 | You can:<br>• advise on developments to security properties in technology<br>• identify new technologies and design their use in a business context |
| [Security technology](../../スキル/#security-technology) | UK GDaD PCF | 実務 | You can:<br>• explain the effect of vulnerabilities on current and future designs<br>• share information on a range of systems, but may specialise in one |
| [Understanding security implications of transformation](../../スキル/#understanding-security-implications-of-transformation) | UK GDaD PCF | 実務 | You can:<br>• interpret and apply an understanding of policy and process, business architecture, and legal and political implications to assist the development of technical solutions or controls |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実務 | できること:<br>• 自分の仕事が支える臨床・ケアのワークフローを説明する<br>• 臨床・ケアの同僚と、一般的な医療用語を正しく使う<br>• 変更が患者のケアにいつ影響しうるかを見分けて伝える |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実践者 | できること:<br>• データ保護影響評価と情報共有契約を主導する<br>• 適法な根拠、同意、秘密保持、保存について、チームに助言する<br>• インシデントを調査し、改善を勧告する |
| [アイデンティティとアクセスの管理](../../スキル/#アイデンティティとアクセスの管理) | このリファレンス | 実践者 | できること:<br>• アイデンティティとアクセスのサービスを設計し、運営する<br>• アクセスを定期的にレビューし、問題を修正する |
| [脆弱性管理](../../スキル/#脆弱性管理) | このリファレンス | 実践者 | できること:<br>• 患者サービスへのリスクを含め、リスクで脆弱性に優先順位をつける<br>• ペネトレーションテストと是正の範囲を定め、管理する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実務 | できること:<br>• ハザードのワークショップに参加し、ハザードログに寄与する<br>• 自分の仕事のために、臨床リスク管理プロセスに従う<br>• テスト結果など、臨床安全ケースのための根拠を提供する |
| [医療機器ソフトウェアの規制](../../スキル/#医療機器ソフトウェアの規制) | このリファレンス | 認知 | できること:<br>• 一部の医療ソフトウェアが医療機器として規制されることを説明する<br>• 製品が医療機器にあたるかもしれないとき、誰に尋ねればよいかを知っている |

### 一般的な資格と経験

- セキュリティアーキテクチャまたはセキュリティエンジニアリングの相当の経験(修士相当のレベル)。
- 認められたセキュリティ資格、または同等の経験。

### バンドの概要

- **知識:** ある分野とそのマネジメントに関する専門的な知識。
- **自律性:** サービスのために組織の方針を解釈し、チームの方向性を定める。
- **範囲:** サービス領域、または組織全体にわたる分野。
- **リーダーシップ:** チームを管理する、またはライン管理なしで分野を率いる。
- **説明責任:** サービス領域、その職員、その予算。

### 職務評価(例示)

| # | 要素 | レベル | 点数 |
| --- | --- | --- | --- |
| 1 | コミュニケーションと関係構築のスキル | 5 | 45 |
| 2 | 知識、研修、経験 | 7 | 196 |
| 3 | 分析と判断のスキル | 5 | 60 |
| 4 | 計画と組織化のスキル | 4 | 42 |
| 5 | 身体的スキル | 2 | 15 |
| 6 | 患者・利用者のケアに対する責任 | 1 | 4 |
| 7 | 方針とサービス開発に対する責任 | 4 | 32 |
| 8 | 財務・物的資源に対する責任 | 2 | 12 |
| 9 | 人に対する責任 | 3 | 21 |
| 10 | 情報資源に対する責任 | 5 | 34 |
| 11 | 研究開発に対する責任 | 3 | 21 |
| 12 | 行動の自由度 | 5 | 45 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 4 | 18 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **560** (バンド 8a: 540–584) |

UK GDaD PCF の等級の示唆(バンド 6)より高いバンドに置いている。保健分野の求人はこのロールをバンド 8a に置いている。この職務は少ない監督で重要な臨床システムのセキュリティを設計するため、分析と行動の自由度はバンド 7 の水準を上回って評価している。

## バンド 8b: リード セキュリティアーキテクト

**UK GDaD PCF のレベル: Lead security architect**

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

### 責任

- 臨床システムやクラウドホスティングなど、複数のリスクの高いプロジェクトまたは主要領域のセキュリティアーキテクチャを主導する。
- 担当領域の設計のセキュリティ原則と基準を定め、設計機関で保証する。
- セキュリティリスクとその管理の選択肢について、シニアなリスクオーナーに助言する。
- パートナー組織や供給者と共有するデータのセキュリティを設計する。
- セキュリティアーキテクトを率い、育成する。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Analysis](../../スキル/#analysis) | UK GDaD PCF | 実践者 | You can:<br>• monitor the analysis of a technical solution and ensure analysis is reused for similar problem sets<br>• review solutions and identify areas for change<br>• drive the collection of information that is used and analysed<br>• feed back on policy and requirements |
| [Communication (security architect)](../../スキル/#communication-security-architect) | UK GDaD PCF | 実践者 | You can:<br>• demonstrate a deep understanding of security concepts and can apply them to a technical level<br>• effectively translate and accurately communicate security and risk implications to technical and non-technical stakeholders<br>• successfully respond to challenges<br>• manage stakeholder expectations and be flexible, adapting to stakeholder reactions to reach consensus |
| [Designing secure systems](../../スキル/#designing-secure-systems) | UK GDaD PCF | 実践者 | You can:<br>• design and review system architectures through the development of patterns and principles |
| [Enabling and informing risk-based decisions](../../スキル/#enabling-and-informing-risk-based-decisions) | UK GDaD PCF | 実践者 | You can:<br>• work with higher impact or more complex risks, advising on the impact and whether it's within risk tolerance<br>• apply different risk methodologies in proportion to the risk |
| [Research and innovation](../../スキル/#research-and-innovation) | UK GDaD PCF | 実践者 | You can:<br>• contribute to and inform developments on security properties in technology<br>• identify new technologies and design the use of these in the business context across the organisation<br>• engage with the broader security community |
| [Security technology](../../スキル/#security-technology) | UK GDaD PCF | エキスパート | You can:<br>• explain complex system architectures<br>• identify and explain how easy or difficult it will be to exploit vulnerabilities<br>• lead and influence security technology in the security industry |
| [Understanding security implications of transformation](../../スキル/#understanding-security-implications-of-transformation) | UK GDaD PCF | 実践者 | You can:<br>• interpret and apply understanding across a complex area<br>• start influencing policy and process, business architecture, and legal and political implications |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実践者 | できること:<br>• サービスが組織間のケアパスにどう収まるかを分析する<br>• 臨床医、ケア職員、患者と協力して、デジタルサービスを形づくる<br>• デジタルに関する決定が、ケア、安全、職員の業務量に与える影響を説明する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実践者 | できること:<br>• データ保護影響評価と情報共有契約を主導する<br>• 適法な根拠、同意、秘密保持、保存について、チームに助言する<br>• インシデントを調査し、改善を勧告する |
| [アイデンティティとアクセスの管理](../../スキル/#アイデンティティとアクセスの管理) | このリファレンス | エキスパート | できること:<br>• 職員、患者、システムのアイデンティティとアクセスの戦略を定める<br>• 新しいアイデンティティ標準の導入を主導する |
| [脆弱性管理](../../スキル/#脆弱性管理) | このリファレンス | 実践者 | できること:<br>• 患者サービスへのリスクを含め、リスクで脆弱性に優先順位をつける<br>• ペネトレーションテストと是正の範囲を定め、管理する |
| [セキュリティ運用](../../スキル/#セキュリティ運用) | このリファレンス | 実務 | できること:<br>• アラートを監視し、ランブックを使ってトリアージする<br>• 証拠を集め、イベントをエスカレーションする<br>• 指導を受けながら、簡単な検知ルールを調整する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実務 | できること:<br>• ハザードのワークショップに参加し、ハザードログに寄与する<br>• 自分の仕事のために、臨床リスク管理プロセスに従う<br>• テスト結果など、臨床安全ケースのための根拠を提供する |
| [組織のリスクマネジメント](../../スキル/#組織のリスクマネジメント) | このリファレンス | 実践者 | できること:<br>• ディレクトレートまたはプログラムのリスクプロセスを運営する<br>• リスクをリスク選好に照らして評価し、エスカレーションする<br>• リスクを委員会に報告する |
| [ピープルマネジメント](../../スキル/#ピープルマネジメント) | このリファレンス | 実践者 | できること:<br>• 目標を設定し、評価を行いながら、チームをライン管理する<br>• 心身の健康を支え、勤怠、実績、行為を管理する<br>• チームの育成と後継者計画を立てる |

### 一般的な資格と経験

- 複雑なサービスのセキュリティアーキテクチャの豊富な経験。

### バンドの概要

- **知識:** 複数の分野または大規模なサービスにわたる専門的な知識。
- **自律性:** 大きな領域の方針と戦略を形づくる。
- **範囲:** 複数のサービスやチーム、またはプリンシパルレベルの分野。
- **リーダーシップ:** マネージャーを管理する、またはある分野の第一人者である。
- **説明責任:** 複数のサービス、その職員、その予算。

### 職務評価(例示)

| # | 要素 | レベル | 点数 |
| --- | --- | --- | --- |
| 1 | コミュニケーションと関係構築のスキル | 5 | 45 |
| 2 | 知識、研修、経験 | 8 | 240 |
| 3 | 分析と判断のスキル | 5 | 60 |
| 4 | 計画と組織化のスキル | 4 | 42 |
| 5 | 身体的スキル | 2 | 15 |
| 6 | 患者・利用者のケアに対する責任 | 1 | 4 |
| 7 | 方針とサービス開発に対する責任 | 4 | 32 |
| 8 | 財務・物的資源に対する責任 | 3 | 21 |
| 9 | 人に対する責任 | 3 | 21 |
| 10 | 情報資源に対する責任 | 5 | 34 |
| 11 | 研究開発に対する責任 | 3 | 21 |
| 12 | 行動の自由度 | 5 | 45 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 4 | 18 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **613** (バンド 8b: 585–629) |

## バンド 8c: プリンシパル セキュリティアーキテクト

**UK GDaD PCF のレベル: Principal security architect**

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

### 責任

- 組織のセキュリティアーキテクチャのビジョン、原則、戦略を定める。
- 患者のケアとサービスに対するサイバーセキュリティリスクについて、経営陣と取締役会に助言する。
- 大規模攻撃からの復旧を含むサイバーレジリエンスが、重要な臨床サービスに設計として組み込まれるようにする。
- 組織を横断するサイバーセキュリティと標準のコミュニティで、組織を代表する。
- セキュリティアーキテクチャの実践を率い、その人材を育てる。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Analysis](../../スキル/#analysis) | UK GDaD PCF | エキスパート | You can:<br>• provide direction and lead on change regarding factors that feed into analysis<br>• monitor changes in the technical environment and assess whether risks are still at acceptable levels or whether previous decisions need to be revisited<br>• direct and influence others on best practice and policy |
| [Communication (security architect)](../../スキル/#communication-security-architect) | UK GDaD PCF | エキスパート | You can:<br>• demonstrate expert understanding of security concepts and can apply them to a technical level, at the highest levels of risk complexity<br>• effectively translate and accurately communicate security and risk implications at the most senior levels across technical and non-technical stakeholders<br>• successfully respond to challenges<br>• manage stakeholder expectations across high risk and complexity or under constrained timescales |
| [Designing secure systems](../../スキル/#designing-secure-systems) | UK GDaD PCF | エキスパート | You can:<br>• lead design and review solutions to complex problems with system architectures by defining and challenging patterns and principles<br>• create precedents and set direction |
| [Enabling and informing risk-based decisions](../../スキル/#enabling-and-informing-risk-based-decisions) | UK GDaD PCF | エキスパート | You can:<br>• act as a point of escalation<br>• be trusted by senior risk owners as an expert in security<br>• apply risk methodologies at the most complex levels of risk |
| [Research and innovation](../../スキル/#research-and-innovation) | UK GDaD PCF | 実践者 | You can:<br>• contribute to and inform developments on security properties in technology<br>• identify new technologies and design the use of these in the business context across the organisation<br>• engage with the broader security community |
| [Security technology](../../スキル/#security-technology) | UK GDaD PCF | エキスパート | You can:<br>• explain complex system architectures<br>• identify and explain how easy or difficult it will be to exploit vulnerabilities<br>• lead and influence security technology in the security industry |
| [Understanding security implications of transformation](../../スキル/#understanding-security-implications-of-transformation) | UK GDaD PCF | エキスパート | You can:<br>• challenge and lead changes to policy and processes to support business outcomes, business architecture, and legal and political implications |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実践者 | できること:<br>• サービスが組織間のケアパスにどう収まるかを分析する<br>• 臨床医、ケア職員、患者と協力して、デジタルサービスを形づくる<br>• デジタルに関する決定が、ケア、安全、職員の業務量に与える影響を説明する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | エキスパート | できること:<br>• 情報ガバナンスの方針と戦略を定める<br>• 情報リスクとコンプライアンスについて、取締役会に助言する<br>• 規制当局やパートナーに対して組織を代表する |
| [アイデンティティとアクセスの管理](../../スキル/#アイデンティティとアクセスの管理) | このリファレンス | エキスパート | できること:<br>• 職員、患者、システムのアイデンティティとアクセスの戦略を定める<br>• 新しいアイデンティティ標準の導入を主導する |
| [脆弱性管理](../../スキル/#脆弱性管理) | このリファレンス | 実践者 | できること:<br>• 患者サービスへのリスクを含め、リスクで脆弱性に優先順位をつける<br>• ペネトレーションテストと是正の範囲を定め、管理する |
| [セキュリティ運用](../../スキル/#セキュリティ運用) | このリファレンス | 実践者 | できること:<br>• セキュリティインシデントを調査し、封じ込める<br>• 検知ルールを書き、脅威ハンティングを行う<br>• インシデントの後に、ランブックとツールを改善する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実践者 | できること:<br>• プロダクトや変更のハザード特定とリスク評価を主導する<br>• ハザードログと臨床安全ケース報告書を書き、維持する<br>• プロダクトチームとリスクの管理策に合意し、それが機能しているかを確認する<br>• 臨床リスク管理の基準の適用について、チームに助言する |
| [医療機器ソフトウェアの規制](../../スキル/#医療機器ソフトウェアの規制) | このリファレンス | 実務 | できること:<br>• 医療機器の標準を満たすソフトウェアライフサイクルのプロセスに従う<br>• そのプロセスが必要とする記録を作成する |
| [組織のリスクマネジメント](../../スキル/#組織のリスクマネジメント) | このリファレンス | エキスパート | できること:<br>• 組織のリスクマネジメントの枠組みとリスク選好を設計する<br>• 戦略的リスクについて、取締役会に助言する |
| [ピープルマネジメント](../../スキル/#ピープルマネジメント) | このリファレンス | 実践者 | できること:<br>• 目標を設定し、評価を行いながら、チームをライン管理する<br>• 心身の健康を支え、勤怠、実績、行為を管理する<br>• チームの育成と後継者計画を立てる |

### 一般的な資格と経験

- 複数の組織にわたってセキュリティアーキテクチャを率いた豊富な経験。

### バンドの概要

- **知識:** 専門的な知識に加え、広い組織・セクターへの理解。
- **自律性:** 機能の戦略を定め、ディレクターに対して責任を負う。
- **範囲:** 機能または部門。
- **リーダーシップ:** 複数の管理階層を通じて機能を率いる。
- **説明責任:** 機能の成果、人員、予算。

### 職務評価(例示)

| # | 要素 | レベル | 点数 |
| --- | --- | --- | --- |
| 1 | コミュニケーションと関係構築のスキル | 6 | 60 |
| 2 | 知識、研修、経験 | 8 | 240 |
| 3 | 分析と判断のスキル | 5 | 60 |
| 4 | 計画と組織化のスキル | 5 | 60 |
| 5 | 身体的スキル | 2 | 15 |
| 6 | 患者・利用者のケアに対する責任 | 1 | 4 |
| 7 | 方針とサービス開発に対する責任 | 5 | 45 |
| 8 | 財務・物的資源に対する責任 | 3 | 21 |
| 9 | 人に対する責任 | 3 | 21 |
| 10 | 情報資源に対する責任 | 6 | 46 |
| 11 | 研究開発に対する責任 | 2 | 12 |
| 12 | 行動の自由度 | 5 | 45 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 4 | 18 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **662** (バンド 8c: 630–674) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
