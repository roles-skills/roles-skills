# エンタープライズアーキテクト

> これは、一般的なデジタルヘルスケア組織のための例示的な参照プロファイルです。特定の雇用主の公式な職務記述書ではなく、職務評価のスコアも正式な評価ではありません。

> このテキストは英語から AI アシスタントによって翻訳されたもので、日本語を母語とする方による確認はまだ行われていません。英国政府デジタル・データ専門職能力フレームワーク(UK GDaD PCF)と ESCO からの引用は英語のままです。

**職群:** [アーキテクチャ](../../#アーキテクチャ)  
**バンド:** 8a, 8b, 8c, 8d  
**UK GDaD PCF のロール:** [Enterprise architect](https://understand-digital-data-roles-skills.service.gov.uk/role/enterprise-architect/)  
**ESCO の職業:** [enterprise architect](http://data.europa.eu/esco/occupation/2bef94db-0088-4507-982a-2ca717529adb) (ISCO-08 2511)

## 概要

エンタープライズアーキテクトは、組織のサービス、情報、アプリケーション、技術を俯瞰的に捉え、それを使って保健・ケアの戦略を一貫した変革計画に変える。アーキテクチャの原則、基準、ロードマップを定め、投資判断を導き、デジタルの変化が組織を横断した患者の安全で連携したケアを支えるようにする。

## デジタルヘルスケア組織において

- ケアパスは多くの組織とシステムにまたがるため、アーキテクチャは境界を越えた記録、結果、紹介状の共有を支えなければならない。
- 保有資産には、変更が難しい長寿命の臨床システム、医療機器、供給者契約が含まれることが多いため、ロードマップは移行を慎重に計画しなければならない。
- アーキテクチャの決定は、患者の安全、プライバシー、昼夜を問わず稼働するサービスのレジリエンスに影響する。
- HL7 FHIR、SNOMED CT、IHE プロファイルなどのオープンな標準は、ロックインを避け、相互運用性を実現するうえで鍵になる。
- 資金は限られ、厳しく精査されるため、アーキテクトは費用対効果と、既存の共有プラットフォームの再利用を示さなければならない。

## UK GDaD PCF のロール説明(原文は英語)

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

## ロールレベル

| バンド | 名称 | UK GDaD PCF のレベル | 英国公務員の等級 | 職務評価の点数 |
| --- | --- | --- | --- | --- |
| 8a | [エンタープライズアーキテクト](#バンド-8a-エンタープライズアーキテクト) | Enterprise architect | HEO/SEO | 560 |
| 8b | [シニア エンタープライズアーキテクト](#バンド-8b-シニア-エンタープライズアーキテクト) | Senior enterprise architect | SEO/G7 | 622 |
| 8c | [リード エンタープライズアーキテクト](#バンド-8c-リード-エンタープライズアーキテクト) | Lead enterprise architect | G7/G6 | 658 |
| 8d | [プリンシパル エンタープライズアーキテクト](#バンド-8d-プリンシパル-エンタープライズアーキテクト) | Principal enterprise architect | G6 | 703 |

## バンド 8a: エンタープライズアーキテクト

**UK GDaD PCF のレベル: Enterprise architect**

> An enterprise architect supports other architects in developing the strategy.
> 
> At this role level, you will:
> - network and communicate with stakeholders across domains or enterprises, and identify opportunities for improvement
> - use best practice
> - use emerging technologies and approaches
> - learn to identify influences or risks
> - play a part in successful delivery of the team’s objectives

### 責任

- 診断やコミュニティケアなど、ある領域について、組織の現在と目標のサービス、情報、アプリケーション、技術をモデル化する。
- アプリケーションとデータフローのカタログを含め、アーキテクチャのリポジトリを最新に保つ。
- 提案をアーキテクチャの原則と基準に照らしてレビューし、設計機関に勧告する。
- システムが機能を重複させている箇所や、サポートされていない技術に依存している箇所を特定し、リスクを提起する。
- ソリューションアーキテクトや臨床リードと協力して、ケアパスがシステムをどう使っているかを理解する。
- 設計が領域のアーキテクチャにどう適合するかについて、ソリューションアーキテクトを導く。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../スキル/#architect-for-the-whole-context) | UK GDaD PCF | 実践者 | You can:<br>• work to support wider organisational objectives beyond your immediate goals​<br>• track emerging internal and external issues over time that could affect the work of teams across the organisation<br>• take action to solve or mitigate problems by influencing colleagues across the organisation |
| [Architecture communication](../../スキル/#architecture-communication) | UK GDaD PCF | 実践者 | You can:<br>• lead the communication of complicated, complex or risky architecture topics with technical and non-technical stakeholders<br>• communicate with senior stakeholders across your organisation<br>• adapt your message and communication techniques to your audience<br>• advocate on behalf of a team to other stakeholders<br>• manage stakeholder expectations effectively |
| [Commercial perspective](../../スキル/#commercial-perspective) | UK GDaD PCF | 実務 | You can:<br>• understand commercial processes and the appropriate internal contacts within a government department<br>• understand different sourcing strategies and when to apply them |
| [Community collaboration](../../スキル/#community-collaboration) | UK GDaD PCF | 実務 | You can:<br>• contribute to the work of others<br>• motivate and empower teams<br>• create the right environment for teams to work in, and can identify the best team makeup depending on the situation<br>• recognise and deal with issues |
| [Enterprise architecture](../../スキル/#enterprise-architecture) | UK GDaD PCF | 実務 | You can:<br>• turn an organisation's goals into clear objectives, with limited direction<br>• design an architecture that defines the technology, people, process and other elements needed to achieve organisation objectives, with support |
| [Making architectural decisions](../../スキル/#making-architectural-decisions) | UK GDaD PCF | 実務 | You can:<br>• work with others to make architectural design decisions characterised by managed levels of risk and complexity<br>• identify and address architectural risks relevant to your team or domain, for example, business, data, or security<br>• engage with architectural governance and assurance to effectively manage decisions and risks, with support |
| [Problem definition and shaping](../../スキル/#problem-definition-and-shaping) | UK GDaD PCF | 実務 | You can:<br>• help to frame a problem characterised by managed levels of complexity, complication, or risk so that a solution can be created<br>• help to create options for solving problems at an appropriate level of detail |
| [Strategy design](../../スキル/#strategy-design) | UK GDaD PCF | 実務 | You can:<br>• support the development of a strategy or vision that aligns with organisational objectives<br>• challenge requirements and assumptions, and identify opportunities to develop strategy<br>• support the implementation of a strategy or vision, for example, by using a roadmap or plan<br>• use architectural principles, patterns, and constraints when appropriate |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実践者 | できること:<br>• サービスが組織間のケアパスにどう収まるかを分析する<br>• 臨床医、ケア職員、患者と協力して、デジタルサービスを形づくる<br>• デジタルに関する決定が、ケア、安全、職員の業務量に与える影響を説明する |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | 実践者 | できること:<br>• FHIR、HL7 バージョン 2、メッセージングパターンを使って連携を設計し、構築する<br>• FHIR リソースと実装ガイドを書き、プロファイル化する<br>• システム間の複雑なマッピングやデータ品質の問題を解決する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実務 | できること:<br>• ハザードのワークショップに参加し、ハザードログに寄与する<br>• 自分の仕事のために、臨床リスク管理プロセスに従う<br>• テスト結果など、臨床安全ケースのための根拠を提供する |
| [組織のリスクマネジメント](../../スキル/#組織のリスクマネジメント) | このリファレンス | 実務 | できること:<br>• 自分の領域のリスクを記録し、更新する<br>• 管理策を提案し、対応を追跡する |

### 一般的な資格と経験

- 複雑な組織におけるアーキテクチャ、分析、または技術設計の相当の経験(修士相当のレベル)。
- TOGAF などのエンタープライズアーキテクチャのフレームワークの知識、または同等の経験。

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

UK GDaD PCF の等級の示唆(バンド 6)より高いバンドに置いている。保健分野の求人はこのロールをバンド 8a に置いている。この職務は領域全体の目標アーキテクチャを形づくり、設計機関に助言するため、知識、分析、計画、方針、行動の自由度はバンド 8a の水準で評価している。

## バンド 8b: シニア エンタープライズアーキテクト

**UK GDaD PCF のレベル: Senior enterprise architect**

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

### 責任

- 組織の 1 つ以上の領域について、目標アーキテクチャと移行ロードマップを策定する。
- 投資が目標アーキテクチャに適合し、共有プラットフォームを再利用するよう、ビジネスケースを形づくる。
- 設計機関でのアーキテクチャレビューを主導し、重要な提案に勧告する。
- データ移行と安全面のリスクを含め、レガシーな臨床・業務システムの置き換えや廃止を計画する。
- 相互運用性、セキュリティ、情報ガバナンスのニーズがロードマップに組み込まれるようにする。
- エンタープライズアーキテクトとソリューションアーキテクトをコーチし、導く。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../スキル/#architect-for-the-whole-context) | UK GDaD PCF | 実践者 | You can:<br>• work to support wider organisational objectives beyond your immediate goals​<br>• track emerging internal and external issues over time that could affect the work of teams across the organisation<br>• take action to solve or mitigate problems by influencing colleagues across the organisation |
| [Architecture communication](../../スキル/#architecture-communication) | UK GDaD PCF | 実践者 | You can:<br>• lead the communication of complicated, complex or risky architecture topics with technical and non-technical stakeholders<br>• communicate with senior stakeholders across your organisation<br>• adapt your message and communication techniques to your audience<br>• advocate on behalf of a team to other stakeholders<br>• manage stakeholder expectations effectively |
| [Commercial perspective](../../スキル/#commercial-perspective) | UK GDaD PCF | 実務 | You can:<br>• understand commercial processes and the appropriate internal contacts within a government department<br>• understand different sourcing strategies and when to apply them |
| [Community collaboration](../../スキル/#community-collaboration) | UK GDaD PCF | 実践者 | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Enterprise architecture](../../スキル/#enterprise-architecture) | UK GDaD PCF | 実践者 | You can:<br>• design an architecture that defines the technology, people, process and other elements needed to achieve organisation objectives<br>• work with others across the organisation to ensure your design is used to achieve the organisation’s objectives |
| [Making architectural decisions](../../スキル/#making-architectural-decisions) | UK GDaD PCF | 実践者 | You can:<br>• make and guide architectural design decisions characterised by medium risk and complexity<br>• identify and address architectural risks that affect multiple teams or domains<br>• use architectural governance and assurance to make design decisions and manage technical risks at the appropriate level<br>• contribute to the development of architectural governance and assurance |
| [Problem definition and shaping](../../スキル/#problem-definition-and-shaping) | UK GDaD PCF | 実践者 | You can:<br>• frame a problem characterised by medium complexity, complication, or risk so that a solution can be created<br>• produce architectural representations that enable different teams to have a shared understanding of problems throughout the life cycle<br>• describe options for solving problems so that appropriate delivery methods can be decided |
| [Strategy design](../../スキル/#strategy-design) | UK GDaD PCF | 実践者 | You can:<br>• define strategies or visions across teams that align with organisational objectives<br>• direct the implementation of a strategy or vision, for example, by creating roadmaps or plans<br>• define architectural principles and patterns<br>• develop or maintain strategy in response to feedback and findings |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実践者 | できること:<br>• サービスが組織間のケアパスにどう収まるかを分析する<br>• 臨床医、ケア職員、患者と協力して、デジタルサービスを形づくる<br>• デジタルに関する決定が、ケア、安全、職員の業務量に与える影響を説明する |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | 実践者 | できること:<br>• FHIR、HL7 バージョン 2、メッセージングパターンを使って連携を設計し、構築する<br>• FHIR リソースと実装ガイドを書き、プロファイル化する<br>• システム間の複雑なマッピングやデータ品質の問題を解決する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実践者 | できること:<br>• データ保護影響評価と情報共有契約を主導する<br>• 適法な根拠、同意、秘密保持、保存について、チームに助言する<br>• インシデントを調査し、改善を勧告する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実務 | できること:<br>• ハザードのワークショップに参加し、ハザードログに寄与する<br>• 自分の仕事のために、臨床リスク管理プロセスに従う<br>• テスト結果など、臨床安全ケースのための根拠を提供する |
| [組織のリスクマネジメント](../../スキル/#組織のリスクマネジメント) | このリファレンス | 実務 | できること:<br>• 自分の領域のリスクを記録し、更新する<br>• 管理策を提案し、対応を追跡する |

### 一般的な資格と経験

- 複数の領域にわたるエンタープライズまたはソリューションアーキテクチャの豊富な経験。
- TOGAF などのエンタープライズアーキテクチャのフレームワークの知識、または同等の経験。

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
| 4 | 計画と組織化のスキル | 5 | 60 |
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
| | **合計** | | **622** (バンド 8b: 585–629) |

UK GDaD PCF の等級の示唆(バンド 7)より高いバンドに置いている。保健分野の求人はこのロールをバンド 8b に置いている。計画は、組織全体に影響する長期ロードマップのためレベル 5、知識は、ビジネス、情報、アプリケーション、技術のアーキテクチャにわたる知識のためレベル 8 とする。

## バンド 8c: リード エンタープライズアーキテクト

**UK GDaD PCF のレベル: Lead enterprise architect**

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

### 責任

- 臨床システムや共有インフラなど、組織の主要部分のエンタープライズアーキテクチャを担う。
- アーキテクチャ設計機関を主宰または率い、プロジェクトが満たすべき基準を定める。
- 投資の優先順位、供給者の戦略、技術リスクについて、ディレクターに助言する。
- パートナー組織と協力して、ケアパスと共有記録にわたるアーキテクチャを整合させる。
- エンタープライズアーキテクトを率い、育成し、アーキテクチャのコミュニティ・オブ・プラクティスを育てる。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../スキル/#architect-for-the-whole-context) | UK GDaD PCF | エキスパート | You can:<br>• assess how trends in society and industry practices might impact the organisation<br>• work with people outside of your organisation to inform policies, strategies and standards<br>• anticipate changes to policy and build resilience through your architectural work<br>• coach others in identifying important trends |
| [Architecture communication](../../スキル/#architecture-communication) | UK GDaD PCF | エキスパート | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Commercial perspective](../../スキル/#commercial-perspective) | UK GDaD PCF | 実践者 | You can:<br>• identify appropriate contractual frameworks and approaches<br>• identify, evaluate and select appropriate suppliers |
| [Community collaboration](../../スキル/#community-collaboration) | UK GDaD PCF | 実践者 | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Enterprise architecture](../../スキル/#enterprise-architecture) | UK GDaD PCF | 実践者 | You can:<br>• design an architecture that defines the technology, people, process and other elements needed to achieve organisation objectives<br>• work with others across the organisation to ensure your design is used to achieve the organisation’s objectives |
| [Making architectural decisions](../../スキル/#making-architectural-decisions) | UK GDaD PCF | 実践者 | You can:<br>• make and guide architectural design decisions characterised by medium risk and complexity<br>• identify and address architectural risks that affect multiple teams or domains<br>• use architectural governance and assurance to make design decisions and manage technical risks at the appropriate level<br>• contribute to the development of architectural governance and assurance |
| [Problem definition and shaping](../../スキル/#problem-definition-and-shaping) | UK GDaD PCF | エキスパート | You can:<br>• lead the framing of a problem characterised by high complexity, complication, or risk so that a solution can be created<br>• coach others in defining problems and describing appropriate options for solutions<br>• help others challenge requirements and assumptions, and identify opportunities when defining problems and solution options |
| [Strategy design](../../スキル/#strategy-design) | UK GDaD PCF | エキスパート | You can:<br>• define and connect strategies or visions across the organisation or wider government<br>• enable the implementation of strategies or visions across the organisation or wider government, for example, by advocating for resources and removing blockers |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実践者 | できること:<br>• サービスが組織間のケアパスにどう収まるかを分析する<br>• 臨床医、ケア職員、患者と協力して、デジタルサービスを形づくる<br>• デジタルに関する決定が、ケア、安全、職員の業務量に与える影響を説明する |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | 実践者 | できること:<br>• FHIR、HL7 バージョン 2、メッセージングパターンを使って連携を設計し、構築する<br>• FHIR リソースと実装ガイドを書き、プロファイル化する<br>• システム間の複雑なマッピングやデータ品質の問題を解決する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実践者 | できること:<br>• データ保護影響評価と情報共有契約を主導する<br>• 適法な根拠、同意、秘密保持、保存について、チームに助言する<br>• インシデントを調査し、改善を勧告する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実践者 | できること:<br>• プロダクトや変更のハザード特定とリスク評価を主導する<br>• ハザードログと臨床安全ケース報告書を書き、維持する<br>• プロダクトチームとリスクの管理策に合意し、それが機能しているかを確認する<br>• 臨床リスク管理の基準の適用について、チームに助言する |
| [組織のリスクマネジメント](../../スキル/#組織のリスクマネジメント) | このリファレンス | 実践者 | できること:<br>• ディレクトレートまたはプログラムのリスクプロセスを運営する<br>• リスクをリスク選好に照らして評価し、エスカレーションする<br>• リスクを委員会に報告する |
| [ピープルマネジメント](../../スキル/#ピープルマネジメント) | このリファレンス | 実践者 | できること:<br>• 目標を設定し、評価を行いながら、チームをライン管理する<br>• 心身の健康を支え、勤怠、実績、行為を管理する<br>• チームの育成と後継者計画を立てる |
| [予算管理](../../スキル/#予算管理) | このリファレンス | 実務 | できること:<br>• 小さな予算に対する支出を追跡し、差異を伝える<br>• 自分の限度内で支出を承認する |

### 一般的な資格と経験

- 複雑な組織でのエンタープライズアーキテクチャの豊富な経験。

### バンドの概要

- **知識:** 専門的な知識に加え、広い組織・セクターへの理解。
- **自律性:** 機能の戦略を定め、ディレクターに対して責任を負う。
- **範囲:** 機能または部門。
- **リーダーシップ:** 複数の管理階層を通じて機能を率いる。
- **説明責任:** 機能の成果、人員、予算。

### 職務評価(例示)

| # | 要素 | レベル | 点数 |
| --- | --- | --- | --- |
| 1 | コミュニケーションと関係構築のスキル | 5 | 45 |
| 2 | 知識、研修、経験 | 8 | 240 |
| 3 | 分析と判断のスキル | 5 | 60 |
| 4 | 計画と組織化のスキル | 5 | 60 |
| 5 | 身体的スキル | 2 | 15 |
| 6 | 患者・利用者のケアに対する責任 | 1 | 4 |
| 7 | 方針とサービス開発に対する責任 | 5 | 45 |
| 8 | 財務・物的資源に対する責任 | 3 | 21 |
| 9 | 人に対する責任 | 4 | 32 |
| 10 | 情報資源に対する責任 | 6 | 46 |
| 11 | 研究開発に対する責任 | 2 | 12 |
| 12 | 行動の自由度 | 5 | 45 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 4 | 18 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **658** (バンド 8c: 630–674) |

UK GDaD PCF の等級の示唆(バンド 8b)より高いバンドに置いている。保健分野の求人はこのロールをバンド 8c に置いている。情報資源は、組織の主要部分の情報システムのアーキテクチャを管理するためレベル 6 とする。すべてのプロジェクトの基準を定め、エンタープライズアーキテクトを率いるため、方針と人はバンド 8b の水準を上回る。

## バンド 8d: プリンシパル エンタープライズアーキテクト

**UK GDaD PCF のレベル: Principal enterprise architect**

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

### 責任

- 保健・ケアの戦略に沿って、組織のエンタープライズアーキテクチャのビジョン、原則、戦略を定める。
- 主要なデジタル投資のアーキテクチャ、リスク、価値について、経営陣と取締役会に助言する。
- 組織のアーキテクチャの実践、ガバナンス、基準を率いる。
- 組織を横断するアーキテクチャと相互運用性のフォーラムで、組織を代表する。
- 採用やキャリアパスを含め、組織全体のアーキテクチャ能力を築く。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../スキル/#architect-for-the-whole-context) | UK GDaD PCF | エキスパート | You can:<br>• assess how trends in society and industry practices might impact the organisation<br>• work with people outside of your organisation to inform policies, strategies and standards<br>• anticipate changes to policy and build resilience through your architectural work<br>• coach others in identifying important trends |
| [Architecture communication](../../スキル/#architecture-communication) | UK GDaD PCF | エキスパート | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Commercial perspective](../../スキル/#commercial-perspective) | UK GDaD PCF | 実践者 | You can:<br>• identify appropriate contractual frameworks and approaches<br>• identify, evaluate and select appropriate suppliers |
| [Community collaboration](../../スキル/#community-collaboration) | UK GDaD PCF | エキスパート | You can:<br>• solve and unblock issues between teams or departments at the highest level<br>• coach the organisation on team dynamics and conflict resolution, while also building and growing the community |
| [Enterprise architecture](../../スキル/#enterprise-architecture) | UK GDaD PCF | エキスパート | You can:<br>• lead others designing architectures defining the technology, people, process and other elements needed to achieve organisation objectives<br>• work with others beyond the organisation to influence organisational structures, technology, people and processes to achieve objectives<br>• ensure organisation-wide changes align with the architectural strategy |
| [Making architectural decisions](../../スキル/#making-architectural-decisions) | UK GDaD PCF | エキスパート | You can:<br>• make and guide architectural design decisions characterised by high levels of risk and complexity<br>• identify and address architectural risks across the organisation or wider government<br>• lead and evolve architectural governance and assurance<br>• represent architectural governance as part of wider governance, for example, legal or commercial |
| [Problem definition and shaping](../../スキル/#problem-definition-and-shaping) | UK GDaD PCF | エキスパート | You can:<br>• lead the framing of a problem characterised by high complexity, complication, or risk so that a solution can be created<br>• coach others in defining problems and describing appropriate options for solutions<br>• help others challenge requirements and assumptions, and identify opportunities when defining problems and solution options |
| [Strategy design](../../スキル/#strategy-design) | UK GDaD PCF | エキスパート | You can:<br>• define and connect strategies or visions across the organisation or wider government<br>• enable the implementation of strategies or visions across the organisation or wider government, for example, by advocating for resources and removing blockers |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | エキスパート | できること:<br>• 保健・ケアのシステムへの深い理解にもとづいて、組織の戦略を形づくる<br>• 保健・ケアのパートナーやリーダーに対して組織を代表する<br>• 政策やサービスの変更が、デジタルサービスとケアにどう影響するかを予測する |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | エキスパート | できること:<br>• 組織の相互運用性の標準と戦略を定める<br>• 国や組織を横断する標準化の取り組みを主導する<br>• 多数のシステムにまたがる重要な連携の設計を保証する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | エキスパート | できること:<br>• 情報ガバナンスの方針と戦略を定める<br>• 情報リスクとコンプライアンスについて、取締役会に助言する<br>• 規制当局やパートナーに対して組織を代表する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実践者 | できること:<br>• プロダクトや変更のハザード特定とリスク評価を主導する<br>• ハザードログと臨床安全ケース報告書を書き、維持する<br>• プロダクトチームとリスクの管理策に合意し、それが機能しているかを確認する<br>• 臨床リスク管理の基準の適用について、チームに助言する |
| [組織のリスクマネジメント](../../スキル/#組織のリスクマネジメント) | このリファレンス | 実践者 | できること:<br>• ディレクトレートまたはプログラムのリスクプロセスを運営する<br>• リスクをリスク選好に照らして評価し、エスカレーションする<br>• リスクを委員会に報告する |
| [ピープルマネジメント](../../スキル/#ピープルマネジメント) | このリファレンス | エキスパート | できること:<br>• マネージャーを率い、大きな領域の文化を形づくる<br>• 人員計画と組織変更を設計する<br>• リーダーをコーチし、複雑な人の問題を解決する |
| [予算管理](../../スキル/#予算管理) | このリファレンス | 実践者 | できること:<br>• 予算を保有して管理し、差異を予測して説明する<br>• コストと便益を示したビジネスケースを作成する |

### 一般的な資格と経験

- 複数の組織にわたってエンタープライズアーキテクチャを率いた豊富な経験。

### バンドの概要

- **知識:** 複数の機能と、より広い保健・ケアのシステムにわたる戦略的な知識。
- **自律性:** 組織全体の戦略を形づくり、ディレクターの代理を務める。
- **範囲:** 主要な機能または複数の機能。
- **リーダーシップ:** 複数の機能または大きな部門を率いる。
- **説明責任:** 主要な機能、大きな予算、組織全体のリスク。

### 職務評価(例示)

| # | 要素 | レベル | 点数 |
| --- | --- | --- | --- |
| 1 | コミュニケーションと関係構築のスキル | 6 | 60 |
| 2 | 知識、研修、経験 | 8 | 240 |
| 3 | 分析と判断のスキル | 5 | 60 |
| 4 | 計画と組織化のスキル | 5 | 60 |
| 5 | 身体的スキル | 2 | 15 |
| 6 | 患者・利用者のケアに対する責任 | 1 | 4 |
| 7 | 方針とサービス開発に対する責任 | 6 | 60 |
| 8 | 財務・物的資源に対する責任 | 3 | 21 |
| 9 | 人に対する責任 | 4 | 32 |
| 10 | 情報資源に対する責任 | 6 | 46 |
| 11 | 研究開発に対する責任 | 2 | 12 |
| 12 | 行動の自由度 | 6 | 60 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 4 | 18 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **703** (バンド 8d: 675–720) |

UK GDaD PCF の等級の示唆(バンド 8c)より高いバンドに置いている。保健分野の求人はこのロールをバンド 8d に置いている。この職務は組織のアーキテクチャのビジョン、原則、戦略に対して組織全体の責任を負うため、方針と行動の自由度はレベル 6 とする。


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
