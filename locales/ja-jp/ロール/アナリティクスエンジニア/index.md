# アナリティクスエンジニア

> これは、一般的なデジタルヘルスケア組織のための例示的な参照プロファイルです。特定の雇用主の公式な職務記述書ではなく、職務評価のスコアも正式な評価ではありません。

> このテキストは英語から AI アシスタントによって翻訳されたもので、日本語を母語とする方による確認はまだ行われていません。英国政府デジタル・データ専門職能力フレームワーク(UK GDaD PCF)と ESCO からの引用は英語のままです。

**職群:** [データ](../../#データ)  
**バンド:** 4, 6, 7, 8a, 8c  
**UK GDaD PCF のロール:** [Analytics engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/analytics-engineer/)  
**ESCO の職業:** [data engineer](http://data.europa.eu/esco/occupation/2079755f-d809-49e6-8037-4de6180e54c0) (ISCO-08 2511); [business intelligence manager](http://data.europa.eu/esco/occupation/207d7b18-6540-432e-8aa6-785ed434572f) (ISCO-08 2421)

## 概要

アナリティクスエンジニアは、生の保健・ケアのデータを、アナリスト、データサイエンティスト、レポートツールが頼れる、クリーンで、テストされ、文書化されたデータモデルに変える。データエンジニアリングと分析の間に位置し、バージョン管理、テスト、コードレビューといったソフトウェアエンジニアリングの実践を、組織の報告書やダッシュボードの裏にある変換処理に適用する。

## デジタルヘルスケア組織において

- データモデルは、何を入院、再入院、待ち時間基準の違反と数えるかなど、臨床と運用の定義を取り込むため、定義は臨床・運用のリードと合意される。
- SNOMED CT や ICD などの用語集・分類の臨床コードは、分析のためにリファレンスセットにまとめられ、慎重なバージョン管理が必要である。
- パフォーマンスや資金の報告に使うモデルは、誤りがサービスに関する決定に影響しうるため、一貫していて監査可能でなければならない。
- モデルは仮名化された患者レベルのデータを保持することが多いため、アクセス、文書化、データ最小化が組み込まれる。

## UK GDaD PCF のロール説明(原文は英語)

> An analytics engineer transforms data relevant to the organisation into structures that enable analysis and decision-making.
> 
> In this role, you will:
> - work with subject matter experts to understand organisational processes and translate these into data structures optimised for analysis
> - work with data users to design and build data models they can use for effective analysis and decision-making, using modelling techniques such as Kimball or Inmon
> - support data quality improvement
> - develop standards for data transformation
> - create and maintain data documentation
> - refine requirements in response to feedback from users and changes in the organisation
> - provide ongoing support to users

## ロールレベル

| バンド | 名称 | UK GDaD PCF のレベル | 英国公務員の等級 | 職務評価の点数 |
| --- | --- | --- | --- | --- |
| 4 | [トレーニー アナリティクスエンジニア](#バンド-4-トレーニー-アナリティクスエンジニア) | Trainee analytics engineer | AO/EO | 276 |
| 6 | [アナリティクスエンジニア](#バンド-6-アナリティクスエンジニア) | Analytics engineer | HEO/SEO | 418 |
| 7 | [シニア アナリティクスエンジニア](#バンド-7-シニア-アナリティクスエンジニア) | Senior analytics engineer | SEO/G7 | 477 |
| 8a | [リード アナリティクスエンジニア](#バンド-8a-リード-アナリティクスエンジニア) | Lead analytics engineer | G7 | 551 |
| 8c | [アナリティクスエンジニアリング責任者](#バンド-8c-アナリティクスエンジニアリング責任者) | Head of analytics engineering | G6 | 634 |

## バンド 4: トレーニー アナリティクスエンジニア

**UK GDaD PCF のレベル: Trainee analytics engineer**

> A trainee analytics engineer attends training and develops skills on the job.
> 
> At this role level, you will:
> - spend time shadowing other analytics engineers
> - build your knowledge of the organisation
> - learn skills for managing data
> - learn to use different applications, tools, templates and best practices
> - handle simple queries from users and document their data requirements
> - contribute to data documentation and user training

### 責任

- 研修とペアワークを通じて、チームのデータモデリングのツールと実践を学ぶ。
- 監督のもとで、データモデルに小さく明確に定義された変更を加える。
- データ項目とその定義をデータカタログに文書化する。
- データ利用者からの単純な質問に答え、その要件を記録する。
- 患者データを扱う際に、情報ガバナンスの規則に従う。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../スキル/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 認知 | You can:<br>• explain why it's important to communicate technical concepts in non-technical language<br>• explain the types of communication that can be used with internal and external stakeholders, and their impact |
| [Data analysis and synthesis](../../スキル/#data-analysis-and-synthesis) | UK GDaD PCF | 認知 | You can:<br>• interpret data to find key insights |
| [Data innovation](../../スキル/#data-innovation) | UK GDaD PCF | 認知 | You can:<br>• develop a basic understanding of an unfamiliar or emerging technology, or a familiar technology in a new data context, with guidance<br>• share what you learn with colleagues, including how it could help deliver more value from data |
| [Data modelling, cleansing and enrichment](../../スキル/#data-modelling-cleansing-and-enrichment) | UK GDaD PCF | 認知 | You can:<br>• show an awareness of different data models and tools, and understand when they could be used<br>• show an awareness of industry-recognised data modelling patterns and standards |
| [Metadata management](../../スキル/#metadata-management) | UK GDaD PCF | 認知 | You can:<br>• explain what metadata is<br>• maintain the information stored in metadata repositories under the direction of others |
| [Problem management](../../スキル/#problem-management) | UK GDaD PCF | 認知 | You can:<br>• investigate problems in systems, processes and services, with an understanding of the level of a problem, for example, strategic, tactical or operational<br>• contribute to the implementation of remedies and preventative measures |
| [Testing](../../スキル/#testing) | UK GDaD PCF | 認知 | You can:<br>• correctly execute test scripts under supervision<br>• understand the role of testing and how it works |
| [Turning business problems into data design](../../スキル/#turning-business-problems-into-data-design) | UK GDaD PCF | 認知 | You can:<br>• contribute to the design of data architecture under the direction of others |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 認知 | できること:<br>• 保健・ケアのシステムの主な部分と、組織が支えるサービスを説明する<br>• 自分の仕事で、患者の安全と秘密保持が重要な理由を説明する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 認知 | できること:<br>• 個人情報と健康情報の取り扱いに関する組織の規則に従う<br>• データ侵害やヒヤリハットを見分けて報告する |
| [データ品質管理](../../スキル/#データ品質管理) | このリファレンス | 認知 | できること:<br>• 正確な医療データが、ケアと計画にとって重要な理由を説明する<br>• データを正確に記録し、誤りを報告する |
| [臨床用語と分類](../../スキル/#臨床用語と分類) | このリファレンス | 認知 | できること:<br>• 臨床用語集と分類の違いを説明する<br>• SNOMED CT や ICD など、一般的な用語集を見分ける |

### 一般的な資格と経験

- データのアプレンティスシップまたは同等のものに在籍している、または取得を目指している。

### バンドの概要

- **知識:** 担当領域の詳細な知識。通常は短期大学相当の学位、アプレンティスシップ、または同等の経験による。
- **自律性:** ガイドラインの範囲で働き、日々の問題の大半を解決し、助言を求められる上司がいる。
- **範囲:** 自分の業務と、定められたサービスまたはプロセス。
- **リーダーシップ:** 小さなチームを監督したり、他の人の仕事を調整したりすることがある。
- **説明責任:** 定められたサービスまたはプロセスの提供。

### 職務評価(例示)

| # | 要素 | レベル | 点数 |
| --- | --- | --- | --- |
| 1 | コミュニケーションと関係構築のスキル | 3 | 21 |
| 2 | 知識、研修、経験 | 4 | 88 |
| 3 | 分析と判断のスキル | 3 | 27 |
| 4 | 計画と組織化のスキル | 2 | 15 |
| 5 | 身体的スキル | 3 | 27 |
| 6 | 患者・利用者のケアに対する責任 | 1 | 4 |
| 7 | 方針とサービス開発に対する責任 | 1 | 5 |
| 8 | 財務・物的資源に対する責任 | 1 | 5 |
| 9 | 人に対する責任 | 1 | 5 |
| 10 | 情報資源に対する責任 | 4 | 24 |
| 11 | 研究開発に対する責任 | 2 | 12 |
| 12 | 行動の自由度 | 2 | 12 |
| 13 | 身体的負荷 | 2 | 7 |
| 14 | 精神的負荷 | 3 | 12 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **276** (バンド 4: 271–325) |

知識は、仕事ができるだけの研修が終わった時点で職務が必要とするレベルで評価している。

## バンド 6: アナリティクスエンジニア

**UK GDaD PCF のレベル: Analytics engineer**

> An analytics engineer develops and tests data models assigned by more senior analytics engineers to help people in a defined area access and use data.
> 
> At this role level, you will:
> - draft documentation of data that meets standards
> - work with other analytics engineers to resolve issues and risks
> - support trainee analytics engineers
> - provide training and support for users of data sets
> - work with more experienced analytics engineers to develop your skills

### 責任

- 合意された設計から、入院患者の活動やコミュニティケアなど、サービス領域のデータモデルを構築しテストする。
- データモデルを、合意された臨床・運用の定義に照らして確認する自動テストを書く。
- 分析で使う臨床コードのリファレンスセットを、明確なバージョンとともに維持する。
- アナリストがモデルの意味、ソース、限界を理解できるよう、モデルを文書化する。
- チームのデータセットの利用者を研修し、支援する。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../スキル/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 実務 | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Data analysis and synthesis](../../スキル/#data-analysis-and-synthesis) | UK GDaD PCF | 実務 | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data innovation](../../スキル/#data-innovation) | UK GDaD PCF | 認知 | You can:<br>• develop a basic understanding of an unfamiliar or emerging technology, or a familiar technology in a new data context, with guidance<br>• share what you learn with colleagues, including how it could help deliver more value from data |
| [Data modelling, cleansing and enrichment](../../スキル/#data-modelling-cleansing-and-enrichment) | UK GDaD PCF | 実務 | You can:<br>• produce data models and understand where to use different types of data models<br>• understand different tools and can compare different data models<br>• reverse-engineer a data model from a live system<br>• understand industry-recognised data modelling patterns and standards |
| [Metadata management](../../スキル/#metadata-management) | UK GDaD PCF | 実務 | You can:<br>• use metadata repositories to complete complex tasks such as data and systems integration impact analysis<br>• maintain a metadata repository to ensure information remains accurate and up to date |
| [Problem management](../../スキル/#problem-management) | UK GDaD PCF | 認知 | You can:<br>• investigate problems in systems, processes and services, with an understanding of the level of a problem, for example, strategic, tactical or operational<br>• contribute to the implementation of remedies and preventative measures |
| [Programming and build (data and analytics engineering)](../../スキル/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | 実務 | You can:<br>• design, code, test and deploy programs or scripts following standards and good practice<br>• write readable, maintainable code<br>• use automation to improve the software development life cycle<br>• consider and adopt appropriate security measures in your solutions |
| [Testing](../../スキル/#testing) | UK GDaD PCF | 認知 | You can:<br>• correctly execute test scripts under supervision<br>• understand the role of testing and how it works |
| [Turning business problems into data design](../../スキル/#turning-business-problems-into-data-design) | UK GDaD PCF | 実務 | You can:<br>• design data architecture by dealing with specific business problems and aligning it to enterprise-wide standards and principles<br>• work within the context of well understood architecture, and identify appropriate patterns |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実務 | できること:<br>• 自分の仕事が支える臨床・ケアのワークフローを説明する<br>• 臨床・ケアの同僚と、一般的な医療用語を正しく使う<br>• 変更が患者のケアにいつ影響しうるかを見分けて伝える |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [データ品質管理](../../スキル/#データ品質管理) | このリファレンス | 実務 | できること:<br>• データ品質のチェックを実行し、誤りを訂正する<br>• データ品質の報告を同僚に説明する |
| [臨床用語と分類](../../スキル/#臨床用語と分類) | このリファレンス | 実務 | できること:<br>• データ項目やフォームに適切なコードを見つけて使う<br>• 用語ブラウザとリファレンスセットを使う |
| [仮名化と開示管理](../../スキル/#仮名化と開示管理) | このリファレンス | 認知 | できること:<br>• 識別可能なデータ、仮名化されたデータ、匿名化されたデータの違いを説明する<br>• 成果物で少数値を秘匿するための組織の規則に従う |

### 一般的な資格と経験

- 数量的またはコンピューティングの分野の学位、または同等の経験。
- データモデルまたは分析コードの構築経験。

### バンドの概要

- **知識:** さまざまな手順にわたる専門知識。追加の研修や経験によって培われる。
- **自律性:** 自立して働き、自分の領域の方針を解釈し、複雑な問題では助言を求める。
- **範囲:** プロダクト、サービス、またはワークストリーム。
- **リーダーシップ:** 小さなチームを率いたり、同僚をメンターしたりすることがある。
- **説明責任:** 自分のワークストリームの成果と、提供した助言の質。

### 職務評価(例示)

| # | 要素 | レベル | 点数 |
| --- | --- | --- | --- |
| 1 | コミュニケーションと関係構築のスキル | 4 | 32 |
| 2 | 知識、研修、経験 | 6 | 156 |
| 3 | 分析と判断のスキル | 4 | 42 |
| 4 | 計画と組織化のスキル | 3 | 27 |
| 5 | 身体的スキル | 3 | 27 |
| 6 | 患者・利用者のケアに対する責任 | 1 | 4 |
| 7 | 方針とサービス開発に対する責任 | 2 | 12 |
| 8 | 財務・物的資源に対する責任 | 1 | 5 |
| 9 | 人に対する責任 | 2 | 12 |
| 10 | 情報資源に対する責任 | 4 | 24 |
| 11 | 研究開発に対する責任 | 2 | 12 |
| 12 | 行動の自由度 | 4 | 32 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 4 | 18 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **418** (バンド 6: 396–465) |

## バンド 7: シニア アナリティクスエンジニア

**UK GDaD PCF のレベル: Senior analytics engineer**

> A senior analytics engineer oversees the development and testing of data models, including directing the work of other analytics engineers.
> 
> At this role level, you will:
> - oversee tasks and support less senior analytics engineers
> - build relationships with stakeholders within a defined area
> - coach and mentor less senior analytics engineers
> - ensure documentation of data meets standards
> - ensure issues and risks are resolved
> - oversee training and support for users of data sets
> - explore and develop new ways of working with data

### 責任

- 複数のサービス領域にわたるデータモデルの設計とテストを監督する。
- 臨床、運用、財務のリードと主要な指標の定義に合意し、モデルがそれを一貫して適用するようにする。
- パフォーマンスや資金の報告に使うモデルが、監査可能で、十分にテストされているようにする。
- データエンジニアやデータオーナーとともに、データの課題とリスクを解決する。
- 他のアナリティクスエンジニアの仕事をコーチし、方向づける。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../スキル/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 実務 | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Data analysis and synthesis](../../スキル/#data-analysis-and-synthesis) | UK GDaD PCF | 実務 | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data innovation](../../スキル/#data-innovation) | UK GDaD PCF | 実務 | You can:<br>• experiment with unfamiliar and emerging technologies, or familiar technologies in new data contexts, with guidance<br>• share what you learn with the team, explaining potential benefits, risks, and practical considerations<br>• identify opportunities to apply technology to improve data processes or outcomes in an operational setting or the wider organisation |
| [Data modelling, cleansing and enrichment](../../スキル/#data-modelling-cleansing-and-enrichment) | UK GDaD PCF | 実践者 | You can:<br>• build and review complex data models, ensuring adherence to standards<br>• use data integration tools and languages to integrate and store data, and advise teams on best practice<br>• ensure data for analysis meets data quality standards and is interoperable with other data sets, enabling reuse<br>• work with other data professionals to improve modelling and integration patterns and standards |
| [Metadata management](../../スキル/#metadata-management) | UK GDaD PCF | 実践者 | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../スキル/#problem-management) | UK GDaD PCF | 実務 | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Programming and build (data and analytics engineering)](../../スキル/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | 実践者 | You can:<br>• lead the design, code, testing and deployment of secure, resilient and maintainable solutions<br>• continuously improve the codebase and reliability of solutions<br>• create automation to improve the software development life cycle<br>• work with others to implement standards and good practice to ensure security, testability and maintainability of solutions |
| [Testing](../../スキル/#testing) | UK GDaD PCF | 実務 | You can:<br>• review requirements and specifications, and define test conditions<br>• identify issues and risks associated with work<br>• analyse and report test activities and results |
| [Turning business problems into data design](../../スキル/#turning-business-problems-into-data-design) | UK GDaD PCF | 実践者 | You can:<br>• design data architecture that deals with problems spanning different business areas<br>• identify links between problems to devise common solutions<br>• work across multiple subject areas, or a single large or complicated subject area<br>• produce appropriate patterns |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実践者 | できること:<br>• サービスが組織間のケアパスにどう収まるかを分析する<br>• 臨床医、ケア職員、患者と協力して、デジタルサービスを形づくる<br>• デジタルに関する決定が、ケア、安全、職員の業務量に与える影響を説明する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [データ品質管理](../../スキル/#データ品質管理) | このリファレンス | 実践者 | できること:<br>• データ品質の規則と指標を定義する<br>• データ提供元と協力して、品質低下の根本原因を修正する |
| [臨床用語と分類](../../スキル/#臨床用語と分類) | このリファレンス | 実践者 | できること:<br>• 臨床用語集を使って、データモデルとリファレンスセットを設計する<br>• 用語集や分類の間をマッピングし、マッピングの限界を説明する<br>• プロダクトや分析での用語集の使い方について、チームに助言する |
| [仮名化と開示管理](../../スキル/#仮名化と開示管理) | このリファレンス | 実務 | できること:<br>• 仮名化されたデータを扱い、成果物を公開する前に開示確認を行う<br>• 連結された、または詳細なデータが、いつ患者を特定しうるかを見分ける |

### 一般的な資格と経験

- データモデリングとアナリティクスエンジニアリングの相当の経験(修士相当のレベル)。

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
| 3 | 分析と判断のスキル | 4 | 42 |
| 4 | 計画と組織化のスキル | 3 | 27 |
| 5 | 身体的スキル | 3 | 27 |
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
| | **合計** | | **477** (バンド 7: 466–539) |

## バンド 8a: リード アナリティクスエンジニア

**UK GDaD PCF のレベル: Lead analytics engineer**

> A lead analytics engineer leads the design and deployment of data models for analysis.
> 
> At this role level, you will:
> - lead and support a team of analytics engineers to design, build and maintain data models
> - work with stakeholders and teams across the organisation to understand relationships between data and organisational processes, and use this to define data requirements
> - promote, build awareness and support understanding of analytics engineering
> - review the work of other analytics engineers
> - create standards for communication, data models and documentation
> - define and improve ways of working in the team

### 責任

- 組織の分析用データモデルを設計、構築、維持するチームを率いる。
- データモデル、テスト、文書化、指標の定義の基準を定める。
- 組織全体のチームと協力して、臨床・運用のプロセスがどのようにデータを生み出すかを理解する。
- 他のアナリティクスエンジニアの仕事をレビューし、チームの仕事の進め方を改善する。
- アナリティクスエンジニアをライン管理する。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../スキル/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 実践者 | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Data analysis and synthesis](../../スキル/#data-analysis-and-synthesis) | UK GDaD PCF | 実践者 | You can:<br>• understand and help teams to apply a range of techniques for data profiling<br>• source system analysis from a complex single source<br>• bring multiple data sources together in a conformed model for analysis |
| [Data innovation](../../スキル/#data-innovation) | UK GDaD PCF | 実践者 | You can:<br>• test and evaluate the feasibility of unfamiliar and emerging technologies, or familiar technologies in new data contexts<br>• share what you learn with the organisation, explaining potential benefits, risks, and practical considerations<br>• recommend, design and implement innovative data solutions based on organisation objectives, user needs, and operational constraints |
| [Data modelling, cleansing and enrichment](../../スキル/#data-modelling-cleansing-and-enrichment) | UK GDaD PCF | 実践者 | You can:<br>• build and review complex data models, ensuring adherence to standards<br>• use data integration tools and languages to integrate and store data, and advise teams on best practice<br>• ensure data for analysis meets data quality standards and is interoperable with other data sets, enabling reuse<br>• work with other data professionals to improve modelling and integration patterns and standards |
| [Metadata management](../../スキル/#metadata-management) | UK GDaD PCF | 実践者 | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../スキル/#problem-management) | UK GDaD PCF | 実践者 | You can:<br>• ensure that the right actions are taken to investigate, resolve and anticipate problems<br>• co-ordinate the team to investigate problems, implement solutions and take preventive measures |
| [Programming and build (data and analytics engineering)](../../スキル/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | 実践者 | You can:<br>• lead the design, code, testing and deployment of secure, resilient and maintainable solutions<br>• continuously improve the codebase and reliability of solutions<br>• create automation to improve the software development life cycle<br>• work with others to implement standards and good practice to ensure security, testability and maintainability of solutions |
| [Testing](../../スキル/#testing) | UK GDaD PCF | 実務 | You can:<br>• review requirements and specifications, and define test conditions<br>• identify issues and risks associated with work<br>• analyse and report test activities and results |
| [Turning business problems into data design](../../スキル/#turning-business-problems-into-data-design) | UK GDaD PCF | 実践者 | You can:<br>• design data architecture that deals with problems spanning different business areas<br>• identify links between problems to devise common solutions<br>• work across multiple subject areas, or a single large or complicated subject area<br>• produce appropriate patterns |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実践者 | できること:<br>• サービスが組織間のケアパスにどう収まるかを分析する<br>• 臨床医、ケア職員、患者と協力して、デジタルサービスを形づくる<br>• デジタルに関する決定が、ケア、安全、職員の業務量に与える影響を説明する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実践者 | できること:<br>• データ保護影響評価と情報共有契約を主導する<br>• 適法な根拠、同意、秘密保持、保存について、チームに助言する<br>• インシデントを調査し、改善を勧告する |
| [データ品質管理](../../スキル/#データ品質管理) | このリファレンス | 実践者 | できること:<br>• データ品質の規則と指標を定義する<br>• データ提供元と協力して、品質低下の根本原因を修正する |
| [臨床用語と分類](../../スキル/#臨床用語と分類) | このリファレンス | 実践者 | できること:<br>• 臨床用語集を使って、データモデルとリファレンスセットを設計する<br>• 用語集や分類の間をマッピングし、マッピングの限界を説明する<br>• プロダクトや分析での用語集の使い方について、チームに助言する |
| [仮名化と開示管理](../../スキル/#仮名化と開示管理) | このリファレンス | 実務 | できること:<br>• 仮名化されたデータを扱い、成果物を公開する前に開示確認を行う<br>• 連結された、または詳細なデータが、いつ患者を特定しうるかを見分ける |
| [ピープルマネジメント](../../スキル/#ピープルマネジメント) | このリファレンス | 実践者 | できること:<br>• 目標を設定し、評価を行いながら、チームをライン管理する<br>• 心身の健康を支え、勤怠、実績、行為を管理する<br>• チームの育成と後継者計画を立てる |

### 一般的な資格と経験

- アナリティクスエンジニアリングまたはデータモデリングを率いた豊富な経験。

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
| 11 | 研究開発に対する責任 | 2 | 12 |
| 12 | 行動の自由度 | 5 | 45 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 4 | 18 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **551** (バンド 8a: 540–584) |

## バンド 8c: アナリティクスエンジニアリング責任者

**UK GDaD PCF のレベル: Head of analytics engineering**

> A head of analytics engineering oversees the development of a range of data models that meet analysis needs across the organisation.
> 
> At this role level, you will:
> - build relationships with senior stakeholders across the organisation to determine what the organisation needs
> - ensure the activities of the analytics engineering team align with strategic priorities
> - ensure the team works to standards for communication, data models and documentation
> - advocate for the analytics engineering role to senior leadership and other organisations
> - build analytics engineering capability by providing technical leadership and career development for the community
> - ensure appropriate technology is available for the community

### 責任

- 組織全体の分析が 1 つの信頼できる定義の集合を使えるよう、組織の分析用データモデルの方向性を定める。
- アナリティクスエンジニアリングの優先事項が、組織の戦略と報告義務を支えるようにする。
- 主要な報告書や意思決定の裏にあるデータの信頼性について、シニアリーダーに助言する。
- コミュニティが必要なツールとプラットフォームを持てるようにし、関連する予算を管理する。
- 技術的なリーダーシップとキャリア開発を通じて、アナリティクスエンジニアリングの能力を築く。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../スキル/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | エキスパート | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Data analysis and synthesis](../../スキル/#data-analysis-and-synthesis) | UK GDaD PCF | 実践者 | You can:<br>• understand and help teams to apply a range of techniques for data profiling<br>• source system analysis from a complex single source<br>• bring multiple data sources together in a conformed model for analysis |
| [Data innovation](../../スキル/#data-innovation) | UK GDaD PCF | エキスパート | You can:<br>• advocate for adoption of unfamiliar and emerging technologies, or familiar technologies in new data contexts, ensuring organisation objectives, user needs, and operational constraints inform decisions<br>• develop organisational capability in data innovation through leadership<br>• anticipate future technology changes and advise how to take advantage of them to realise value from data |
| [Data modelling, cleansing and enrichment](../../スキル/#data-modelling-cleansing-and-enrichment) | UK GDaD PCF | エキスパート | You can:<br>• understand different ways to model data to maximise its use and value<br>• ensure data is modelled appropriately, and modelling standards exist and are complied with<br>• understand a number of data integration tools and patterns, and ensure your teams have the support and training needed to use the most appropriate methods<br>• build relationships with other senior data professionals (in fields such as data architecture, data engineering and data science) to share best practice and continually improve data modelling and integration processes and standards |
| [Metadata management](../../スキル/#metadata-management) | UK GDaD PCF | エキスパート | You can:<br>• identify how metadata repositories can support different areas of the organisation<br>• communicate the value of metadata repositories<br>• set up robust governance processes to keep repositories up to date |
| [Problem management](../../スキル/#problem-management) | UK GDaD PCF | エキスパート | You can:<br>• anticipate problems and defend against them at the right time<br>• understand how a problem fits into the larger picture<br>• identify and describe problems, and help others to describe them<br>• build problem-solving capabilities in others |
| [Programming and build (data and analytics engineering)](../../スキル/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | エキスパート | You can:<br>• set standards for programming tools and techniques<br>• select appropriate development methods for a problem<br>• advise on the application of standards and methods that ensure security, maintainability and compliance<br>• take technical responsibility for all stages of a software development project, providing technical advice and guidance to stakeholders |
| [Testing](../../スキル/#testing) | UK GDaD PCF | 実務 | You can:<br>• review requirements and specifications, and define test conditions<br>• identify issues and risks associated with work<br>• analyse and report test activities and results |
| [Turning business problems into data design](../../スキル/#turning-business-problems-into-data-design) | UK GDaD PCF | エキスパート | You can:<br>• design data architecture that deals with problems across the enterprise<br>• work across all organisational subject areas and internal and external programmes |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | エキスパート | できること:<br>• 保健・ケアのシステムへの深い理解にもとづいて、組織の戦略を形づくる<br>• 保健・ケアのパートナーやリーダーに対して組織を代表する<br>• 政策やサービスの変更が、デジタルサービスとケアにどう影響するかを予測する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実践者 | できること:<br>• データ保護影響評価と情報共有契約を主導する<br>• 適法な根拠、同意、秘密保持、保存について、チームに助言する<br>• インシデントを調査し、改善を勧告する |
| [データ品質管理](../../スキル/#データ品質管理) | このリファレンス | エキスパート | できること:<br>• 組織とそのパートナーのデータ品質の基準を定める<br>• データ品質の改善プログラムを主導する |
| [臨床用語と分類](../../スキル/#臨床用語と分類) | このリファレンス | 実践者 | できること:<br>• 臨床用語集を使って、データモデルとリファレンスセットを設計する<br>• 用語集や分類の間をマッピングし、マッピングの限界を説明する<br>• プロダクトや分析での用語集の使い方について、チームに助言する |
| [ピープルマネジメント](../../スキル/#ピープルマネジメント) | このリファレンス | エキスパート | できること:<br>• マネージャーを率い、大きな領域の文化を形づくる<br>• 人員計画と組織変更を設計する<br>• リーダーをコーチし、複雑な人の問題を解決する |
| [予算管理](../../スキル/#予算管理) | このリファレンス | 実践者 | できること:<br>• 予算を保有して管理し、差異を予測して説明する<br>• コストと便益を示したビジネスケースを作成する |

### 一般的な資格と経験

- 組織全体でアナリティクスエンジニアリングを率いた豊富な経験。

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
| 2 | 知識、研修、経験 | 7 | 196 |
| 3 | 分析と判断のスキル | 5 | 60 |
| 4 | 計画と組織化のスキル | 5 | 60 |
| 5 | 身体的スキル | 2 | 15 |
| 6 | 患者・利用者のケアに対する責任 | 1 | 4 |
| 7 | 方針とサービス開発に対する責任 | 5 | 45 |
| 8 | 財務・物的資源に対する責任 | 4 | 32 |
| 9 | 人に対する責任 | 4 | 32 |
| 10 | 情報資源に対する責任 | 6 | 46 |
| 11 | 研究開発に対する責任 | 2 | 12 |
| 12 | 行動の自由度 | 5 | 45 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 3 | 12 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **634** (バンド 8c: 630–674) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
