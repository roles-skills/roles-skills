# データアーキテクト

> これは、一般的なデジタルヘルスケア組織のための例示的な参照プロファイルです。特定の雇用主の公式な職務記述書ではなく、職務評価のスコアも正式な評価ではありません。

> このテキストは英語から AI アシスタントによって翻訳されたもので、日本語を母語とする方による確認はまだ行われていません。英国政府デジタル・データ専門職能力フレームワーク(UK GDaD PCF)と ESCO からの引用は英語のままです。

**職群:** [アーキテクチャ](../../#アーキテクチャ)  
**バンド:** 8a, 8b, 8c  
**UK GDaD PCF のロール:** [Data architect](https://understand-digital-data-roles-skills.service.gov.uk/role/data-architect/)  
**ESCO の職業:** [database designer](http://data.europa.eu/esco/occupation/8d9ec84d-cf2d-4179-87bc-335cda54a427) (ISCO-08 2521); [data warehouse designer](http://data.europa.eu/esco/occupation/1562c7a3-c7d9-419d-b9b6-db26610bcf84) (ISCO-08 2521)

## 概要

データアーキテクトは、組織が保健・ケアのデータをどう構造化し、保管し、移動し、統制するかを設計し、直接のケア、サービス計画、研究のために安全に使えるようにする。データモデル、データプラットフォーム、データフローを設計し、データ標準を定め、臨床上の意味、品質、秘密が端から端まで保たれるようにする。

## デジタルヘルスケア組織において

- 健康データは臨床上の意味を保たなければならないため、データモデルは SNOMED CT などの臨床用語集や ICD などの分類を使う。
- 直接のケアに使うデータと、計画や研究に使うデータは法的根拠が異なるため、アーキテクトは分離、非識別化、管理されたアクセスを設計する。
- データは品質がさまざまな多くの臨床・ケアのシステムから来るため、アーキテクトはデータ品質チェック、患者の突合、データの系統を設計する。
- 共有ケア記録とデータ交換は、HL7 FHIR リソースのような共通モデルと、合意された国内外のデータセットに依存する。
- 記録は長い保存期間にわたって保管しなければならないため、設計は過去のデータのアーカイブとアクセスを計画しなければならない。

## UK GDaD PCF のロール説明(原文は英語)

> A data architect sets the vision for the organisation’s use of data, through data design, to ensure that data is managed properly and meets the organisation’s needs.

## ロールレベル

| バンド | 名称 | UK GDaD PCF のレベル | 英国公務員の等級 | 職務評価の点数 |
| --- | --- | --- | --- | --- |
| 8a | [データアーキテクト](#バンド-8a-データアーキテクト) | Data architect | SEO/G7 | 560 |
| 8b | [シニア データアーキテクト](#バンド-8b-シニア-データアーキテクト) | Senior data architect | G7/G6 | 613 |
| 8c | [チーフ データアーキテクト](#バンド-8c-チーフ-データアーキテクト) | Chief data architect | G6 | 662 |

## バンド 8a: データアーキテクト

**UK GDaD PCF のレベル: Data architect**

> A data architect designs and builds data models to fulfil the strategic data needs of the organisation, as defined by chief data architects.
> 
> At this role level, you will:
> - design, support and provide guidance for the upgrade, management, decommission and archive of data in compliance with data policy
> - provide input into data dictionaries
> - define and maintain the data technology architecture, including metadata, integration and business intelligence or data warehouse architecture

### 責任

- 必要に応じて臨床用語集を使い、臨床データと運用データの論理・物理データモデルを設計する。
- データウェアハウス、レイクハウス、連携層など、データフローとデータプラットフォームのコンポーネントを設計する。
- 担当領域のデータセットについて、メタデータ、データ辞書の項目、データの系統を定義する。
- データが適法な目的にのみ使われるよう、非識別化とアクセス制御を設計する。
- データ品質や臨床コーディングの同僚と協力して、データ品質低下の構造的な原因を修正する。
- データモデルと標準について、データエンジニアとアナリストを導く。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../スキル/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 実務 | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Communicating data](../../スキル/#communicating-data) | UK GDaD PCF | 認知 | You can:<br>• show an awareness that data needs to be aligned to the needs of the end user<br>• create basic visuals and presentations |
| [Data analysis and synthesis](../../スキル/#data-analysis-and-synthesis) | UK GDaD PCF | 実務 | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../スキル/#data-governance-data-architect) | UK GDaD PCF | 実務 | You can:<br>• understand what data governance is required<br>• take responsibility for the assurance of data solutions and make recommendations to ensure compliance |
| [Data innovation](../../スキル/#data-innovation) | UK GDaD PCF | 認知 | You can:<br>• develop a basic understanding of an unfamiliar or emerging technology, or a familiar technology in a new data context, with guidance<br>• share what you learn with colleagues, including how it could help deliver more value from data |
| [Data modelling](../../スキル/#data-modelling) | UK GDaD PCF | 実務 | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Data standards](../../スキル/#data-standards) | UK GDaD PCF | 実務 | You can:<br>• use data policies, processes and standards effectively<br>• work with subject matter experts to develop standards, policies and guidance to protect data<br>• monitor compliance with policies and standards in a team and take action if needed<br>• analyse the impact if a standard is breached |
| [Metadata management](../../スキル/#metadata-management) | UK GDaD PCF | 実務 | You can:<br>• use metadata repositories to complete complex tasks such as data and systems integration impact analysis<br>• maintain a metadata repository to ensure information remains accurate and up to date |
| [Problem management](../../スキル/#problem-management) | UK GDaD PCF | 実務 | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Strategic thinking](../../スキル/#strategic-thinking) | UK GDaD PCF | 認知 | You can:<br>• explain the strategic context of your work and why it is important<br>• support strategic planning in an administrative capacity |
| [Turning business problems into data design](../../スキル/#turning-business-problems-into-data-design) | UK GDaD PCF | 実務 | You can:<br>• design data architecture by dealing with specific business problems and aligning it to enterprise-wide standards and principles<br>• work within the context of well understood architecture, and identify appropriate patterns |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実務 | できること:<br>• 自分の仕事が支える臨床・ケアのワークフローを説明する<br>• 臨床・ケアの同僚と、一般的な医療用語を正しく使う<br>• 変更が患者のケアにいつ影響しうるかを見分けて伝える |
| [臨床用語と分類](../../スキル/#臨床用語と分類) | このリファレンス | 実務 | できること:<br>• データ項目やフォームに適切なコードを見つけて使う<br>• 用語ブラウザとリファレンスセットを使う |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | 実践者 | できること:<br>• FHIR、HL7 バージョン 2、メッセージングパターンを使って連携を設計し、構築する<br>• FHIR リソースと実装ガイドを書き、プロファイル化する<br>• システム間の複雑なマッピングやデータ品質の問題を解決する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実践者 | できること:<br>• データ保護影響評価と情報共有契約を主導する<br>• 適法な根拠、同意、秘密保持、保存について、チームに助言する<br>• インシデントを調査し、改善を勧告する |
| [データ品質管理](../../スキル/#データ品質管理) | このリファレンス | 実務 | できること:<br>• データ品質のチェックを実行し、誤りを訂正する<br>• データ品質の報告を同僚に説明する |

### 一般的な資格と経験

- データモデリングとデータプラットフォーム設計の相当の経験(修士相当のレベル)。

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

UK GDaD PCF の等級の示唆(バンド 7)より高いバンドに置いている。保健分野の求人はこのロールをバンド 8a に置いている。この職務は多くのサービスで使われるデータプラットフォームと管理策を設計するため、計画、方針、行動の自由度はバンド 7 の水準を上回って評価している。

## バンド 8b: シニア データアーキテクト

**UK GDaD PCF のレベル: Senior data architect**

> A senior data architect delivers the vision for the organisation as set by the chief data architect.
> 
> At this role level, you will:
> - design data models and metadata systems
> - help chief data architects to interpret an organisation’s needs
> - provide oversight and advice to other data architects who are designing and producing data artefacts
> - design and support the management of data dictionaries
> - make sure that your teams are working to the standards set for the organisation by the chief data architects
> - work with technical architects to make sure that an organisation’s systems are designed in accordance with the appropriate data architecture

### 責任

- 共有ケア記録や分析プラットフォームなど、主要な領域のデータアーキテクチャを設計する。
- チームを横断するデータ設計が、組織のデータ標準とモデルに従うようにする。
- 標準、管理策、データ共有契約を含め、パートナー組織とのデータ共有の方法を設計する。
- 新しい設計のデータリスクについて、情報ガバナンスと臨床安全の同僚に助言する。
- データアーキテクトの仕事をレビューし、導く。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../スキル/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 実践者 | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Communicating data](../../スキル/#communicating-data) | UK GDaD PCF | 実務 | You can:<br>• understand the appropriate media to communicate findings<br>• shape communications for the audience |
| [Data analysis and synthesis](../../スキル/#data-analysis-and-synthesis) | UK GDaD PCF | 実務 | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../スキル/#data-governance-data-architect) | UK GDaD PCF | 実践者 | You can:<br>• evolve and define data governance<br>• take responsibility for supporting and collaborating around wider governance<br>• assure and integrate data services to meet the needs of multiple business services<br>• work proactively to ensure the organisation designs architecture that considers data |
| [Data innovation](../../スキル/#data-innovation) | UK GDaD PCF | 実務 | You can:<br>• experiment with unfamiliar and emerging technologies, or familiar technologies in new data contexts, with guidance<br>• share what you learn with the team, explaining potential benefits, risks, and practical considerations<br>• identify opportunities to apply technology to improve data processes or outcomes in an operational setting or the wider organisation |
| [Data modelling](../../スキル/#data-modelling) | UK GDaD PCF | 実践者 | You can:<br>• produce relevant data models across multiple subject areas<br>• explain which models to use for which purpose<br>• understand industry-recognised data modelling patterns and standards, and when to apply them<br>• compare and align different data models |
| [Data standards](../../スキル/#data-standards) | UK GDaD PCF | 実践者 | You can:<br>• create data standards for different subjects and ensure senior leaders understand them<br>• work with subject matter experts across the organisation to introduce data standards best practice<br>• monitor compliance with policies and standards in the organisation<br>• make recommendations about how the organisation should resolve breaches of standards |
| [Metadata management](../../スキル/#metadata-management) | UK GDaD PCF | 実践者 | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../スキル/#problem-management) | UK GDaD PCF | 実践者 | You can:<br>• ensure that the right actions are taken to investigate, resolve and anticipate problems<br>• co-ordinate the team to investigate problems, implement solutions and take preventive measures |
| [Strategic thinking](../../スキル/#strategic-thinking) | UK GDaD PCF | 実務 | You can:<br>• work within a strategic context and communicate how activities meet strategic goals<br>• contribute to the development of strategy and policies |
| [Turning business problems into data design](../../スキル/#turning-business-problems-into-data-design) | UK GDaD PCF | 実践者 | You can:<br>• design data architecture that deals with problems spanning different business areas<br>• identify links between problems to devise common solutions<br>• work across multiple subject areas, or a single large or complicated subject area<br>• produce appropriate patterns |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実践者 | できること:<br>• サービスが組織間のケアパスにどう収まるかを分析する<br>• 臨床医、ケア職員、患者と協力して、デジタルサービスを形づくる<br>• デジタルに関する決定が、ケア、安全、職員の業務量に与える影響を説明する |
| [臨床用語と分類](../../スキル/#臨床用語と分類) | このリファレンス | 実践者 | できること:<br>• 臨床用語集を使って、データモデルとリファレンスセットを設計する<br>• 用語集や分類の間をマッピングし、マッピングの限界を説明する<br>• プロダクトや分析での用語集の使い方について、チームに助言する |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | 実践者 | できること:<br>• FHIR、HL7 バージョン 2、メッセージングパターンを使って連携を設計し、構築する<br>• FHIR リソースと実装ガイドを書き、プロファイル化する<br>• システム間の複雑なマッピングやデータ品質の問題を解決する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実践者 | できること:<br>• データ保護影響評価と情報共有契約を主導する<br>• 適法な根拠、同意、秘密保持、保存について、チームに助言する<br>• インシデントを調査し、改善を勧告する |
| [データ品質管理](../../スキル/#データ品質管理) | このリファレンス | 実践者 | できること:<br>• データ品質の規則と指標を定義する<br>• データ提供元と協力して、品質低下の根本原因を修正する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実務 | できること:<br>• ハザードのワークショップに参加し、ハザードログに寄与する<br>• 自分の仕事のために、臨床リスク管理プロセスに従う<br>• テスト結果など、臨床安全ケースのための根拠を提供する |
| [ピープルマネジメント](../../スキル/#ピープルマネジメント) | このリファレンス | 実務 | できること:<br>• 日々の業務を監督し、フィードバックを与える<br>• 採用と導入研修に参加する<br>• 定期的に 1 対 1 の対話を行う |

### 一般的な資格と経験

- 複雑な組織のデータアーキテクチャの豊富な経験。

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

## バンド 8c: チーフ データアーキテクト

**UK GDaD PCF のレベル: Chief data architect**

> A chief data architect sets the vision for the organisation’s use of data as directed by the appropriate governance body.
> 
> At this role level, you will:
> - oversee the design of multiple data models and have a broad understanding of how each model fulfils the needs of the organisation
> - be accountable for supporting and aligning to the organisation’s data strategy
> - champion data architecture both internally and through collaborating and communicating at the most senior levels across government
> - set the standards and ways of working for the data architecture community
> - be accountable for assuring data models at the level of a project or enterprise
> - provide advice to project teams and oversee the management of the full data product life cycle
> - be responsible for ensuring that the organisation’s systems are designed in accordance with the enterprise data architecture

### 責任

- データ戦略に沿って、組織のデータアーキテクチャのビジョンとロードマップを定める。
- 組織のエンタープライズデータモデル、データ標準、データ辞書を担う。
- データアーキテクチャ、リスク、投資について、経営陣とデータガバナンスの機関に助言する。
- 組織を横断するデータ標準と相互運用性の取り組みで、組織を代表する。
- データアーキテクチャの実践を率い、その人材を育てる。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../スキル/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 実践者 | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Communicating data](../../スキル/#communicating-data) | UK GDaD PCF | 実践者 | You can:<br>• turn complex data into clear and well understood solutions, which can be acted upon<br>• share data communication skills with the team and organisation<br>• understand and communicate different options, taking into account risks and uncertainties |
| [Data analysis and synthesis](../../スキル/#data-analysis-and-synthesis) | UK GDaD PCF | 実務 | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../スキル/#data-governance-data-architect) | UK GDaD PCF | エキスパート | You can:<br>• ensure data governance supports changes to the organisational strategy<br>• align data governance with wider governance (for example, budget)<br>• assure corporate services by understanding important risks and providing mitigation through assurance mechanisms |
| [Data innovation](../../スキル/#data-innovation) | UK GDaD PCF | 実践者 | You can:<br>• test and evaluate the feasibility of unfamiliar and emerging technologies, or familiar technologies in new data contexts<br>• share what you learn with the organisation, explaining potential benefits, risks, and practical considerations<br>• recommend, design and implement innovative data solutions based on organisation objectives, user needs, and operational constraints |
| [Data modelling](../../スキル/#data-modelling) | UK GDaD PCF | エキスパート | You can:<br>• understand the concepts and principles of data modelling and can produce relevant data models<br>• work across government and industry, recognising opportunities for the reuse and alignment of data models in different organisations<br>• design the method to categorise data models within an organisation |
| [Data standards](../../スキル/#data-standards) | UK GDaD PCF | エキスパート | You can:<br>• create data standards for the organisation<br>• advocate for, and oversee compliance with, data policies and standards<br>• decide where standards need to be set across the organisation, and how to set them in the wider context of government |
| [Metadata management](../../スキル/#metadata-management) | UK GDaD PCF | エキスパート | You can:<br>• identify how metadata repositories can support different areas of the organisation<br>• communicate the value of metadata repositories<br>• set up robust governance processes to keep repositories up to date |
| [Problem management](../../スキル/#problem-management) | UK GDaD PCF | エキスパート | You can:<br>• anticipate problems and defend against them at the right time<br>• understand how a problem fits into the larger picture<br>• identify and describe problems, and help others to describe them<br>• build problem-solving capabilities in others |
| [Strategic thinking](../../スキル/#strategic-thinking) | UK GDaD PCF | 実践者 | You can:<br>• define strategies and policies, providing guidance to others on working in the strategic context<br>• evaluate current strategies to ensure business requirements are being met and exceeded where possible |
| [Turning business problems into data design](../../スキル/#turning-business-problems-into-data-design) | UK GDaD PCF | エキスパート | You can:<br>• design data architecture that deals with problems across the enterprise<br>• work across all organisational subject areas and internal and external programmes |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | エキスパート | できること:<br>• 保健・ケアのシステムへの深い理解にもとづいて、組織の戦略を形づくる<br>• 保健・ケアのパートナーやリーダーに対して組織を代表する<br>• 政策やサービスの変更が、デジタルサービスとケアにどう影響するかを予測する |
| [臨床用語と分類](../../スキル/#臨床用語と分類) | このリファレンス | 実践者 | できること:<br>• 臨床用語集を使って、データモデルとリファレンスセットを設計する<br>• 用語集や分類の間をマッピングし、マッピングの限界を説明する<br>• プロダクトや分析での用語集の使い方について、チームに助言する |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | エキスパート | できること:<br>• 組織の相互運用性の標準と戦略を定める<br>• 国や組織を横断する標準化の取り組みを主導する<br>• 多数のシステムにまたがる重要な連携の設計を保証する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | エキスパート | できること:<br>• 情報ガバナンスの方針と戦略を定める<br>• 情報リスクとコンプライアンスについて、取締役会に助言する<br>• 規制当局やパートナーに対して組織を代表する |
| [データ品質管理](../../スキル/#データ品質管理) | このリファレンス | 実践者 | できること:<br>• データ品質の規則と指標を定義する<br>• データ提供元と協力して、品質低下の根本原因を修正する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実践者 | できること:<br>• プロダクトや変更のハザード特定とリスク評価を主導する<br>• ハザードログと臨床安全ケース報告書を書き、維持する<br>• プロダクトチームとリスクの管理策に合意し、それが機能しているかを確認する<br>• 臨床リスク管理の基準の適用について、チームに助言する |
| [ピープルマネジメント](../../スキル/#ピープルマネジメント) | このリファレンス | 実践者 | できること:<br>• 目標を設定し、評価を行いながら、チームをライン管理する<br>• 心身の健康を支え、勤怠、実績、行為を管理する<br>• チームの育成と後継者計画を立てる |

### 一般的な資格と経験

- 複数の組織にわたってデータアーキテクチャを率いた豊富な経験。

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
