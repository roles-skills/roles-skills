# ソリューションアーキテクト

> これは、一般的なデジタルヘルスケア組織のための例示的な参照プロファイルです。特定の雇用主の公式な職務記述書ではなく、職務評価のスコアも正式な評価ではありません。

> このテキストは英語から AI アシスタントによって翻訳されたもので、日本語を母語とする方による確認はまだ行われていません。英国政府デジタル・データ専門職能力フレームワーク(UK GDaD PCF)と ESCO からの引用は英語のままです。

**職群:** [アーキテクチャ](../../#アーキテクチャ)  
**バンド:** 7, 8a, 8b, 8c, 8d  
**UK GDaD PCF のロール:** [Solution architect](https://understand-digital-data-roles-skills.service.gov.uk/role/solution-architect/)  
**ESCO の職業:** [ICT system architect](http://data.europa.eu/esco/occupation/e1c72b5f-4c5c-487c-a6df-e84b64a51dae) (ISCO-08 2511)

## 概要

ソリューションアーキテクトは、新規または変更されるサービスが、利用者のニーズや臨床ワークフローから、アプリケーション、データ、連携、ホスティング、セキュリティまで、エンドツーエンドでどう機能するかを設計する。各ソリューションが組織のアーキテクチャに適合し、安全性、プライバシー、相互運用性のニーズを満たし、無理のないコストで構築、運用、サポートできるようにする。

## デジタルヘルスケア組織において

- ソリューションは、購入した臨床システム、自社開発のサービス、共有プラットフォームを組み合わせることが多いため、アーキテクトは供給者の境界を越えて設計しなければならない。
- 設計上の選択は、結果の紛失や患者の誤った突合などの臨床ハザードを生じうるため、ソリューション設計は臨床安全ケースに反映される。
- 患者情報の新しいデータフローには、適法な根拠とデータ保護影響評価が必要なため、アーキテクトは情報ガバナンスと密に協力する。
- HL7 FHIR などの標準を使った、他の保健・ケア組織との相互運用性は、通常、中核的な要件である。
- 一部のソリューションには医療機器にあたるソフトウェアが含まれ、設計、保証、供給者への要件が変わる。

## UK GDaD PCF のロール説明(原文は英語)

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

## ロールレベル

| バンド | 名称 | UK GDaD PCF のレベル | 英国公務員の等級 | 職務評価の点数 |
| --- | --- | --- | --- | --- |
| 7 | [アソシエイト ソリューションアーキテクト](#バンド-7-アソシエイト-ソリューションアーキテクト) | Associate solution architect | HEO/SEO | 483 |
| 8a | [ソリューションアーキテクト](#バンド-8a-ソリューションアーキテクト) | Solution architect | SEO/G7 | 560 |
| 8b | [シニア ソリューションアーキテクト](#バンド-8b-シニア-ソリューションアーキテクト) | Senior solution architect | G7 | 604 |
| 8c | [リード ソリューションアーキテクト](#バンド-8c-リード-ソリューションアーキテクト) | Lead solution architect | G7/G6 | 655 |
| 8d | [プリンシパル ソリューションアーキテクト](#バンド-8d-プリンシパル-ソリューションアーキテクト) | Principal solution architect | G6 | 699 |

## バンド 7: アソシエイト ソリューションアーキテクト

**UK GDaD PCF のレベル: Associate solution architect**

> An associate solution architect supports other solution architects to design solutions. You will usually work under supervision.
> 
> At this role level, you will:
> - support the design of solutions by working with stakeholders
> - help your team achieve its objectives

### 責任

- プロダクトチーム、臨床医、供給者から要件を集めて、ソリューション設計の材料にする。
- コンテキスト、データフロー、連携の図など、現在と目標の状態の図を描く。
- 監督のもとで、ソリューション設計書と決定記録の一部を起草する。
- 設計をアーキテクチャ基準とセキュリティ・情報ガバナンスの要件に照らして確認する。
- 設計が設計機関のレビューを受ける準備を手伝う。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../スキル/#architect-for-the-whole-context) | UK GDaD PCF | 認知 | You can:<br>• identify relevant information that can inform your architectural work, such as strategies, roadmaps, policies and technical trends<br>• understand how your work supports the team in enabling change​ |
| [Architecture communication](../../スキル/#architecture-communication) | UK GDaD PCF | 実務 | You can:<br>• listen to the needs of technical and business stakeholders<br>• create and use different architecture representations to communicate effectively, achieving agreement with technical and non-technical stakeholders<br>• provide support in discussions about architectural topics within a multidisciplinary team |
| [Commercial perspective](../../スキル/#commercial-perspective) | UK GDaD PCF | 認知 | You can:<br>• show an awareness of government commercial processes<br>• show an awareness of legal and compliance rules |
| [Community collaboration](../../スキル/#community-collaboration) | UK GDaD PCF | 認知 | You can:<br>• understand the work of others and the importance of team dynamics, collaboration and feedback |
| [Making architectural decisions](../../スキル/#making-architectural-decisions) | UK GDaD PCF | 認知 | You can:<br>• describe the reasoning behind architectural design decisions<br>• gather information to inform decisions<br>• understand architectural governance and assurance relevant to your work |
| [Problem definition and shaping](../../スキル/#problem-definition-and-shaping) | UK GDaD PCF | 実務 | You can:<br>• help to frame a problem characterised by managed levels of complexity, complication, or risk so that a solution can be created<br>• help to create options for solving problems at an appropriate level of detail |
| [Strategy design](../../スキル/#strategy-design) | UK GDaD PCF | 認知 | You can:<br>• explain how organisational objectives link to designing strategy<br>• describe the purpose and application of strategy, standards, patterns, policies, roadmaps, vision, and mission statements |
| [Technical design throughout the life cycle](../../スキル/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | 実務 | You can:<br>• create technical designs characterised by managed levels of risk, impact, and complexity<br>• provide guidance and support to teams using technical designs throughout the life cycle<br>• adapt a technical design if needed during delivery<br>• work with well-understood technology and identify appropriate patterns |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実務 | できること:<br>• 自分の仕事が支える臨床・ケアのワークフローを説明する<br>• 臨床・ケアの同僚と、一般的な医療用語を正しく使う<br>• 変更が患者のケアにいつ影響しうるかを見分けて伝える |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | 実務 | できること:<br>• FHIR のリソース、プロファイル、API を読み、使う<br>• 指導を受けながら、簡単な連携を構築またはテストする<br>• メッセージを仕様に照らして確認する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実務 | できること:<br>• ハザードのワークショップに参加し、ハザードログに寄与する<br>• 自分の仕事のために、臨床リスク管理プロセスに従う<br>• テスト結果など、臨床安全ケースのための根拠を提供する |

### 一般的な資格と経験

- ソリューション設計の専門知識(修士レベルまたは同等の経験)。
- 分析、開発、または技術設計の経験。

### バンドの概要

- **知識:** 高度に発達した専門知識。通常は修士相当または同等の経験による。
- **自律性:** 組織の方針に沿って働き、成果の出し方を決め、他の人が相談する専門家である。
- **範囲:** 複数のプロダクトやサービス、または専門機能。
- **リーダーシップ:** チームまたは専門実務の領域を率いる。
- **説明責任:** サービスまたは専門機能の提供と、予算を持つ場合はその予算。

### 職務評価(例示)

| # | 要素 | レベル | 点数 |
| --- | --- | --- | --- |
| 1 | コミュニケーションと関係構築のスキル | 4 | 32 |
| 2 | 知識、研修、経験 | 7 | 196 |
| 3 | 分析と判断のスキル | 5 | 60 |
| 4 | 計画と組織化のスキル | 3 | 27 |
| 5 | 身体的スキル | 2 | 15 |
| 6 | 患者・利用者のケアに対する責任 | 1 | 4 |
| 7 | 方針とサービス開発に対する責任 | 3 | 21 |
| 8 | 財務・物的資源に対する責任 | 1 | 5 |
| 9 | 人に対する責任 | 2 | 12 |
| 10 | 情報資源に対する責任 | 5 | 34 |
| 11 | 研究開発に対する責任 | 2 | 12 |
| 12 | 行動の自由度 | 4 | 32 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 4 | 18 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **483** (バンド 7: 466–539) |

UK GDaD PCF の等級の示唆(バンド 6)より高いバンドに置いている。保健分野の求人はこのロールをバンド 7 に置いている。この職務はアプリケーション、データ、連携、セキュリティにまたがって設計するため、知識は修士レベルまたは同等で評価している。

## バンド 8a: ソリューションアーキテクト

**UK GDaD PCF のレベル: Solution architect**

> A solution architect is responsible for a single solution. They usually work independently on solutions where risk is low. They also often support or contribute to work led by more senior solution architects.
> 
> At this role level, you will:
> - build relationships with stakeholders across different business or technical areas in the organisation
> - be proactive in identifying opportunities to improve the organisation
> - follow best practice for solution design
> - use emerging technologies and approaches
> - help your team achieve its objective

### 責任

- 職員向けツールや単純な患者向けサービスなど、リスクの低いサービスのエンドツーエンドのソリューションを設計する。
- 購入、構築、共有プラットフォームの再利用を含む選択肢を比較し、明確な理由とともに 1 つを勧告する。
- 標準がある場合はオープンな標準を使って、ソリューションの連携、データフロー、アイデンティティとアクセスを設計する。
- ソリューションのハザード特定とデータ保護影響評価に寄与する。
- 設計を設計機関に発表し、構築と稼働の間、デリバリーチームを支援する。
- アソシエイト ソリューションアーキテクトをコーチし、その仕事をレビューする。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../スキル/#architect-for-the-whole-context) | UK GDaD PCF | 実務 | You can:<br>• align your work with the work being done by other architects and technical professionals<br>• track emerging issues, strategies, roadmaps, patterns and technologies over time to assess opportunities and risks to your work<br>• identify how other teams contribute to delivering outcomes through change |
| [Architecture communication](../../スキル/#architecture-communication) | UK GDaD PCF | 実践者 | You can:<br>• lead the communication of complicated, complex or risky architecture topics with technical and non-technical stakeholders<br>• communicate with senior stakeholders across your organisation<br>• adapt your message and communication techniques to your audience<br>• advocate on behalf of a team to other stakeholders<br>• manage stakeholder expectations effectively |
| [Commercial perspective](../../スキル/#commercial-perspective) | UK GDaD PCF | 実務 | You can:<br>• understand commercial processes and the appropriate internal contacts within a government department<br>• understand different sourcing strategies and when to apply them |
| [Community collaboration](../../スキル/#community-collaboration) | UK GDaD PCF | 実務 | You can:<br>• contribute to the work of others<br>• motivate and empower teams<br>• create the right environment for teams to work in, and can identify the best team makeup depending on the situation<br>• recognise and deal with issues |
| [Making architectural decisions](../../スキル/#making-architectural-decisions) | UK GDaD PCF | 実務 | You can:<br>• work with others to make architectural design decisions characterised by managed levels of risk and complexity<br>• identify and address architectural risks relevant to your team or domain, for example, business, data, or security<br>• engage with architectural governance and assurance to effectively manage decisions and risks, with support |
| [Problem definition and shaping](../../スキル/#problem-definition-and-shaping) | UK GDaD PCF | 実践者 | You can:<br>• frame a problem characterised by medium complexity, complication, or risk so that a solution can be created<br>• produce architectural representations that enable different teams to have a shared understanding of problems throughout the life cycle<br>• describe options for solving problems so that appropriate delivery methods can be decided |
| [Strategy design](../../スキル/#strategy-design) | UK GDaD PCF | 実務 | You can:<br>• support the development of a strategy or vision that aligns with organisational objectives<br>• challenge requirements and assumptions, and identify opportunities to develop strategy<br>• support the implementation of a strategy or vision, for example, by using a roadmap or plan<br>• use architectural principles, patterns, and constraints when appropriate |
| [Technical design throughout the life cycle](../../スキル/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | 実務 | You can:<br>• create technical designs characterised by managed levels of risk, impact, and complexity<br>• provide guidance and support to teams using technical designs throughout the life cycle<br>• adapt a technical design if needed during delivery<br>• work with well-understood technology and identify appropriate patterns |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実務 | できること:<br>• 自分の仕事が支える臨床・ケアのワークフローを説明する<br>• 臨床・ケアの同僚と、一般的な医療用語を正しく使う<br>• 変更が患者のケアにいつ影響しうるかを見分けて伝える |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | 実践者 | できること:<br>• FHIR、HL7 バージョン 2、メッセージングパターンを使って連携を設計し、構築する<br>• FHIR リソースと実装ガイドを書き、プロファイル化する<br>• システム間の複雑なマッピングやデータ品質の問題を解決する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実践者 | できること:<br>• データ保護影響評価と情報共有契約を主導する<br>• 適法な根拠、同意、秘密保持、保存について、チームに助言する<br>• インシデントを調査し、改善を勧告する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実務 | できること:<br>• ハザードのワークショップに参加し、ハザードログに寄与する<br>• 自分の仕事のために、臨床リスク管理プロセスに従う<br>• テスト結果など、臨床安全ケースのための根拠を提供する |
| [アイデンティティとアクセスの管理](../../スキル/#アイデンティティとアクセスの管理) | このリファレンス | 実務 | できること:<br>• ユーザーアカウントとアクセス権を作成、変更、削除する<br>• アクセスをロールベースのアクセス規則に照らして確認する |

### 一般的な資格と経験

- ソリューション設計またはソフトウェアエンジニアリングの相当の経験(修士相当のレベル)。

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

UK GDaD PCF の等級の示唆(バンド 7)より高いバンドに置いている。保健分野の求人はこのロールをバンド 8a に置いている。この職務はエンドツーエンドの設計を担い、設計機関に選択肢を勧告するため、計画、方針、行動の自由度はバンド 7 の水準を上回って評価している。

## バンド 8b: シニア ソリューションアーキテクト

**UK GDaD PCF のレベル: Senior solution architect**

> A senior solution architect is responsible for a single, more complex, solution. They usually work on solutions where the risk is moderate. They may lead and coach other solution architects.
> 
> At this role level, you will:
> - build relationships with senior stakeholders across different business or technical areas in the organisation
> - be proactive in identifying opportunities to improve the organisation
> - support multiple architecture projects
> - find and use emerging technologies and approaches
> - support others to follow best practice for solution architecture

### 責任

- 臨床システムや複数の組織で使われるサービスなど、中程度のリスクの複雑なソリューションを設計する。
- 相互運用性、セキュリティ、安全性を含め、調達における供給者製品の技術評価を主導する。
- ソリューションが昼夜を問わずケアを支える場合は、レジリエンスと事業継続を考慮して設計する。
- 臨床安全責任者と協力して、設計上の決定とリスクの管理策が安全ケースに記録されるようにする。
- 他のソリューションアーキテクトをコーチし、その仕事をレビューする。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../スキル/#architect-for-the-whole-context) | UK GDaD PCF | 実務 | You can:<br>• align your work with the work being done by other architects and technical professionals<br>• track emerging issues, strategies, roadmaps, patterns and technologies over time to assess opportunities and risks to your work<br>• identify how other teams contribute to delivering outcomes through change |
| [Architecture communication](../../スキル/#architecture-communication) | UK GDaD PCF | 実践者 | You can:<br>• lead the communication of complicated, complex or risky architecture topics with technical and non-technical stakeholders<br>• communicate with senior stakeholders across your organisation<br>• adapt your message and communication techniques to your audience<br>• advocate on behalf of a team to other stakeholders<br>• manage stakeholder expectations effectively |
| [Commercial perspective](../../スキル/#commercial-perspective) | UK GDaD PCF | 実務 | You can:<br>• understand commercial processes and the appropriate internal contacts within a government department<br>• understand different sourcing strategies and when to apply them |
| [Community collaboration](../../スキル/#community-collaboration) | UK GDaD PCF | 実践者 | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../スキル/#making-architectural-decisions) | UK GDaD PCF | 実践者 | You can:<br>• make and guide architectural design decisions characterised by medium risk and complexity<br>• identify and address architectural risks that affect multiple teams or domains<br>• use architectural governance and assurance to make design decisions and manage technical risks at the appropriate level<br>• contribute to the development of architectural governance and assurance |
| [Problem definition and shaping](../../スキル/#problem-definition-and-shaping) | UK GDaD PCF | 実践者 | You can:<br>• frame a problem characterised by medium complexity, complication, or risk so that a solution can be created<br>• produce architectural representations that enable different teams to have a shared understanding of problems throughout the life cycle<br>• describe options for solving problems so that appropriate delivery methods can be decided |
| [Strategy design](../../スキル/#strategy-design) | UK GDaD PCF | 実務 | You can:<br>• support the development of a strategy or vision that aligns with organisational objectives<br>• challenge requirements and assumptions, and identify opportunities to develop strategy<br>• support the implementation of a strategy or vision, for example, by using a roadmap or plan<br>• use architectural principles, patterns, and constraints when appropriate |
| [Technical design throughout the life cycle](../../スキル/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | 実践者 | You can:<br>• create technical designs characterised by medium risk, impact, and complexity<br>• maintain appropriate quality and architectural coherence of a technical design in response to change<br>• use feedback to optimise and refine technical designs throughout the life cycle |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実践者 | できること:<br>• サービスが組織間のケアパスにどう収まるかを分析する<br>• 臨床医、ケア職員、患者と協力して、デジタルサービスを形づくる<br>• デジタルに関する決定が、ケア、安全、職員の業務量に与える影響を説明する |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | 実践者 | できること:<br>• FHIR、HL7 バージョン 2、メッセージングパターンを使って連携を設計し、構築する<br>• FHIR リソースと実装ガイドを書き、プロファイル化する<br>• システム間の複雑なマッピングやデータ品質の問題を解決する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実践者 | できること:<br>• データ保護影響評価と情報共有契約を主導する<br>• 適法な根拠、同意、秘密保持、保存について、チームに助言する<br>• インシデントを調査し、改善を勧告する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実践者 | できること:<br>• プロダクトや変更のハザード特定とリスク評価を主導する<br>• ハザードログと臨床安全ケース報告書を書き、維持する<br>• プロダクトチームとリスクの管理策に合意し、それが機能しているかを確認する<br>• 臨床リスク管理の基準の適用について、チームに助言する |
| [アイデンティティとアクセスの管理](../../スキル/#アイデンティティとアクセスの管理) | このリファレンス | 実務 | できること:<br>• ユーザーアカウントとアクセス権を作成、変更、削除する<br>• アクセスをロールベースのアクセス規則に照らして確認する |
| [医療機器ソフトウェアの規制](../../スキル/#医療機器ソフトウェアの規制) | このリファレンス | 認知 | できること:<br>• 一部の医療ソフトウェアが医療機器として規制されることを説明する<br>• 製品が医療機器にあたるかもしれないとき、誰に尋ねればよいかを知っている |
| [組織のリスクマネジメント](../../スキル/#組織のリスクマネジメント) | このリファレンス | 実務 | できること:<br>• 自分の領域のリスクを記録し、更新する<br>• 管理策を提案し、対応を追跡する |

### 一般的な資格と経験

- 複数の分野にわたる複雑なソリューション設計の豊富な経験(修士を超えるレベル)。

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
| 8 | 財務・物的資源に対する責任 | 2 | 12 |
| 9 | 人に対する責任 | 3 | 21 |
| 10 | 情報資源に対する責任 | 5 | 34 |
| 11 | 研究開発に対する責任 | 3 | 21 |
| 12 | 行動の自由度 | 5 | 45 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 4 | 18 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **604** (バンド 8b: 585–629) |

UK GDaD PCF の等級の示唆(バンド 8a)より高いバンドに置いている。保健分野の求人はこのロールをバンド 8b に置いている。知識は、アプリケーション、データ、連携、セキュリティ、臨床安全など、複数の分野にわたる専門知識のためレベル 8 とする。

## バンド 8c: リード ソリューションアーキテクト

**UK GDaD PCF のレベル: Lead solution architect**

> A lead solution architect is responsible for a group of solution architecture projects, or a single more complex area. They may lead teams of more junior solution architects.
> 
> At this role level, you will:
> - build relationships with senior stakeholders across multiple business or technical areas in the organisation
> - be proactive in identifying opportunities to improve the organisation
> - support multiple architecture projects or programmes
> - find and use emerging technologies and approaches
> - develop best practice for solution architecture

### 責任

- 電子患者記録の置き換えなど、プログラムまたは複雑な領域のソリューションアーキテクチャを主導する。
- プログラム全体のソリューションが一貫し、相互運用可能で、目標アーキテクチャと整合するようにする。
- 設計リスク、依存関係、供給者の選択、コストについて、プログラム委員会に助言する。
- 設計機関で、他のソリューションアーキテクトの設計を保証する。
- ソリューションアーキテクトのチームを率い、育成する。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../スキル/#architect-for-the-whole-context) | UK GDaD PCF | 実践者 | You can:<br>• work to support wider organisational objectives beyond your immediate goals​<br>• track emerging internal and external issues over time that could affect the work of teams across the organisation<br>• take action to solve or mitigate problems by influencing colleagues across the organisation |
| [Architecture communication](../../スキル/#architecture-communication) | UK GDaD PCF | エキスパート | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Commercial perspective](../../スキル/#commercial-perspective) | UK GDaD PCF | 実践者 | You can:<br>• identify appropriate contractual frameworks and approaches<br>• identify, evaluate and select appropriate suppliers |
| [Community collaboration](../../スキル/#community-collaboration) | UK GDaD PCF | 実践者 | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../スキル/#making-architectural-decisions) | UK GDaD PCF | 実践者 | You can:<br>• make and guide architectural design decisions characterised by medium risk and complexity<br>• identify and address architectural risks that affect multiple teams or domains<br>• use architectural governance and assurance to make design decisions and manage technical risks at the appropriate level<br>• contribute to the development of architectural governance and assurance |
| [Problem definition and shaping](../../スキル/#problem-definition-and-shaping) | UK GDaD PCF | エキスパート | You can:<br>• lead the framing of a problem characterised by high complexity, complication, or risk so that a solution can be created<br>• coach others in defining problems and describing appropriate options for solutions<br>• help others challenge requirements and assumptions, and identify opportunities when defining problems and solution options |
| [Strategy design](../../スキル/#strategy-design) | UK GDaD PCF | 実践者 | You can:<br>• define strategies or visions across teams that align with organisational objectives<br>• direct the implementation of a strategy or vision, for example, by creating roadmaps or plans<br>• define architectural principles and patterns<br>• develop or maintain strategy in response to feedback and findings |
| [Technical design throughout the life cycle](../../スキル/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | エキスパート | You can:<br>• create technical designs characterised by high risk, impact, and complexity<br>• lead and guide others in creating technical designs that achieve organisational objectives<br>• use feedback to optimise and refine standards for technical designs throughout the life cycle |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実践者 | できること:<br>• サービスが組織間のケアパスにどう収まるかを分析する<br>• 臨床医、ケア職員、患者と協力して、デジタルサービスを形づくる<br>• デジタルに関する決定が、ケア、安全、職員の業務量に与える影響を説明する |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | エキスパート | できること:<br>• 組織の相互運用性の標準と戦略を定める<br>• 国や組織を横断する標準化の取り組みを主導する<br>• 多数のシステムにまたがる重要な連携の設計を保証する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実践者 | できること:<br>• データ保護影響評価と情報共有契約を主導する<br>• 適法な根拠、同意、秘密保持、保存について、チームに助言する<br>• インシデントを調査し、改善を勧告する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実践者 | できること:<br>• プロダクトや変更のハザード特定とリスク評価を主導する<br>• ハザードログと臨床安全ケース報告書を書き、維持する<br>• プロダクトチームとリスクの管理策に合意し、それが機能しているかを確認する<br>• 臨床リスク管理の基準の適用について、チームに助言する |
| [医療機器ソフトウェアの規制](../../スキル/#医療機器ソフトウェアの規制) | このリファレンス | 実務 | できること:<br>• 医療機器の標準を満たすソフトウェアライフサイクルのプロセスに従う<br>• そのプロセスが必要とする記録を作成する |
| [組織のリスクマネジメント](../../スキル/#組織のリスクマネジメント) | このリファレンス | 実践者 | できること:<br>• ディレクトレートまたはプログラムのリスクプロセスを運営する<br>• リスクをリスク選好に照らして評価し、エスカレーションする<br>• リスクを委員会に報告する |
| [ピープルマネジメント](../../スキル/#ピープルマネジメント) | このリファレンス | 実践者 | できること:<br>• 目標を設定し、評価を行いながら、チームをライン管理する<br>• 心身の健康を支え、勤怠、実績、行為を管理する<br>• チームの育成と後継者計画を立てる |

### 一般的な資格と経験

- 複雑なプログラムのソリューションアーキテクチャを率いた豊富な経験。

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
| 10 | 情報資源に対する責任 | 5 | 34 |
| 11 | 研究開発に対する責任 | 3 | 21 |
| 12 | 行動の自由度 | 5 | 45 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 4 | 18 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **655** (バンド 8c: 630–674) |

UK GDaD PCF の等級の示唆(バンド 8b)より高いバンドに置いている。保健分野の求人はこのロールをバンド 8c に置いている。この職務はプログラム全体のアーキテクチャを計画し、ソリューションアーキテクトのチームを率いるため、計画、方針、人はバンド 8b の水準を上回って評価している。

## バンド 8d: プリンシパル ソリューションアーキテクト

**UK GDaD PCF のレベル: Principal solution architect**

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

### 責任

- 組織の最大または最重要のプログラムのソリューションアーキテクチャを主導する。
- 組織のソリューションアーキテクチャの基準、パターン、手法を定める。
- 重要で共有される保健・ケアのサービスの設計について、ディレクターとパートナー組織に助言する。
- プログラム、供給者、パートナー組織の間の最も難しい設計上の対立を解決する。
- ソリューションアーキテクチャの実践を率い、その人材を育てる。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Architect for the whole context](../../スキル/#architect-for-the-whole-context) | UK GDaD PCF | エキスパート | You can:<br>• assess how trends in society and industry practices might impact the organisation<br>• work with people outside of your organisation to inform policies, strategies and standards<br>• anticipate changes to policy and build resilience through your architectural work<br>• coach others in identifying important trends |
| [Architecture communication](../../スキル/#architecture-communication) | UK GDaD PCF | エキスパート | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Commercial perspective](../../スキル/#commercial-perspective) | UK GDaD PCF | 実践者 | You can:<br>• identify appropriate contractual frameworks and approaches<br>• identify, evaluate and select appropriate suppliers |
| [Community collaboration](../../スキル/#community-collaboration) | UK GDaD PCF | エキスパート | You can:<br>• solve and unblock issues between teams or departments at the highest level<br>• coach the organisation on team dynamics and conflict resolution, while also building and growing the community |
| [Making architectural decisions](../../スキル/#making-architectural-decisions) | UK GDaD PCF | エキスパート | You can:<br>• make and guide architectural design decisions characterised by high levels of risk and complexity<br>• identify and address architectural risks across the organisation or wider government<br>• lead and evolve architectural governance and assurance<br>• represent architectural governance as part of wider governance, for example, legal or commercial |
| [Problem definition and shaping](../../スキル/#problem-definition-and-shaping) | UK GDaD PCF | エキスパート | You can:<br>• lead the framing of a problem characterised by high complexity, complication, or risk so that a solution can be created<br>• coach others in defining problems and describing appropriate options for solutions<br>• help others challenge requirements and assumptions, and identify opportunities when defining problems and solution options |
| [Strategy design](../../スキル/#strategy-design) | UK GDaD PCF | エキスパート | You can:<br>• define and connect strategies or visions across the organisation or wider government<br>• enable the implementation of strategies or visions across the organisation or wider government, for example, by advocating for resources and removing blockers |
| [Technical design throughout the life cycle](../../スキル/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | エキスパート | You can:<br>• create technical designs characterised by high risk, impact, and complexity<br>• lead and guide others in creating technical designs that achieve organisational objectives<br>• use feedback to optimise and refine standards for technical designs throughout the life cycle |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | エキスパート | できること:<br>• 保健・ケアのシステムへの深い理解にもとづいて、組織の戦略を形づくる<br>• 保健・ケアのパートナーやリーダーに対して組織を代表する<br>• 政策やサービスの変更が、デジタルサービスとケアにどう影響するかを予測する |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | エキスパート | できること:<br>• 組織の相互運用性の標準と戦略を定める<br>• 国や組織を横断する標準化の取り組みを主導する<br>• 多数のシステムにまたがる重要な連携の設計を保証する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | エキスパート | できること:<br>• 情報ガバナンスの方針と戦略を定める<br>• 情報リスクとコンプライアンスについて、取締役会に助言する<br>• 規制当局やパートナーに対して組織を代表する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実践者 | できること:<br>• プロダクトや変更のハザード特定とリスク評価を主導する<br>• ハザードログと臨床安全ケース報告書を書き、維持する<br>• プロダクトチームとリスクの管理策に合意し、それが機能しているかを確認する<br>• 臨床リスク管理の基準の適用について、チームに助言する |
| [医療機器ソフトウェアの規制](../../スキル/#医療機器ソフトウェアの規制) | このリファレンス | 実務 | できること:<br>• 医療機器の標準を満たすソフトウェアライフサイクルのプロセスに従う<br>• そのプロセスが必要とする記録を作成する |
| [組織のリスクマネジメント](../../スキル/#組織のリスクマネジメント) | このリファレンス | 実践者 | できること:<br>• ディレクトレートまたはプログラムのリスクプロセスを運営する<br>• リスクをリスク選好に照らして評価し、エスカレーションする<br>• リスクを委員会に報告する |
| [ピープルマネジメント](../../スキル/#ピープルマネジメント) | このリファレンス | 実践者 | できること:<br>• 目標を設定し、評価を行いながら、チームをライン管理する<br>• 心身の健康を支え、勤怠、実績、行為を管理する<br>• チームの育成と後継者計画を立てる |
| [予算管理](../../スキル/#予算管理) | このリファレンス | 実務 | できること:<br>• 小さな予算に対する支出を追跡し、差異を伝える<br>• 自分の限度内で支出を承認する |

### 一般的な資格と経験

- 複数のプログラムや組織にわたってソリューションアーキテクチャを率いた豊富な経験。

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
| 7 | 方針とサービス開発に対する責任 | 5 | 45 |
| 8 | 財務・物的資源に対する責任 | 4 | 32 |
| 9 | 人に対する責任 | 4 | 32 |
| 10 | 情報資源に対する責任 | 6 | 46 |
| 11 | 研究開発に対する責任 | 2 | 12 |
| 12 | 行動の自由度 | 6 | 60 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 4 | 18 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **699** (バンド 8d: 675–720) |

UK GDaD PCF の等級の示唆(バンド 8c)より高いバンドに置いている。保健分野の求人はこのロールをバンド 8d に置いている。この職務は組織のソリューションアーキテクチャの基準を定めるため、行動の自由度はレベル 6、実践とその予算を率いるため、財務資源と人はレベル 4 とする。


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
