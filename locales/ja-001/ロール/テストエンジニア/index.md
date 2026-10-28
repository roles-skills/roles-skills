# テストエンジニア

> これは、一般的なデジタルヘルスケア組織のための例示的な参照プロファイルです。特定の雇用主の公式な職務記述書ではなく、職務評価のスコアも正式な評価ではありません。

> このテキストは英語から AI アシスタントによって翻訳されたもので、日本語を母語とする方による確認はまだ行われていません。英国政府デジタル・データ専門職能力フレームワーク(UK GDaD PCF)と ESCO からの引用は英語のままです。

**職群:** [品質保証とテスト](../../#品質保証とテスト)  
**バンド:** 4, 6, 7, 8a  
**UK GDaD PCF のロール:** [Test engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/test-engineer/)  
**ESCO の職業:** [software tester](http://data.europa.eu/esco/occupation/106f79e4-6264-45f1-9e7a-297435cd684b) (ISCO-08 2519)

## 概要

テストエンジニアは、チームが組織のデジタルヘルスサービスを素早く頻繁にテストできるようにする、自動テスト、ツール、フレームワークを構築する。機能、連携、性能、セキュリティ、レジリエンスをテストするコードを書き、デリバリーのパイプラインにテストを組み込んで、臨床システムや患者向けシステムへの変更を安全にリリースできるようにする。

## デジタルヘルスケア組織において

- 臨床システムは安全上重要であるため、自動回帰テストはハザードログに記録された安全の管理策を守り、安全ケースの根拠として保管される。
- 他の保健・ケアのシステムとの連携には、HL7 FHIR や HL7 バージョン 2 などの標準に照らした自動テストが必要で、パートナーシステムを模擬して行うことが多い。
- 臨床サービスは終日稼働し、予測できる時間帯にピークを迎えるため、性能とレジリエンスのテストは実際の臨床の需要をモデル化する。
- テスト環境には実際の患者データを置いてはならないため、エンジニアは、まれなケースやエッジケースを含む、現実的な合成データを生成する。
- 医療機器として規制されるソフトウェアには、IEC 62304 などの標準にもとづく、ライフサイクルの一部としてのトレーサブルで再現可能なテストが必要である。

## UK GDaD PCF のロール説明(原文は英語)

> A test engineer designs, builds, automates and executes comprehensive, robust and maintainable test suites. They apply test engineering standards, perform exploratory testing and use diverse techniques to identify risks and improve testing efficiency and quality.
> 
> In this role you will:
> - maintain automated tests in continuous integration, continuous delivery (CI/CD) pipelines
> - use, develop and standardise reusable frameworks and tools following engineering practices and standards
> - analyse and test artefacts such as products, services and business processes
> - promote quality considerations throughout the development life cycle
> - support the resolution of technical issues

## ロールレベル

| バンド | 名称 | UK GDaD PCF のレベル | 英国公務員の等級 | 職務評価の点数 |
| --- | --- | --- | --- | --- |
| 4 | [アソシエイト テストエンジニア](#バンド-4-アソシエイト-テストエンジニア) | Associate test engineer | EO | 275 |
| 6 | [テストエンジニア](#バンド-6-テストエンジニア) | Test engineer | HEO/SEO | 411 |
| 7 | [シニア テストエンジニア](#バンド-7-シニア-テストエンジニア) | Senior test engineer | SEO/G7 | 477 |
| 8a | [リード テストエンジニア](#バンド-8a-リード-テストエンジニア) | Lead test engineer | SEO/G7/G6 | 553 |

## バンド 4: アソシエイト テストエンジニア

**UK GDaD PCF のレベル: Associate test engineer**

> An associate test engineer works closely with other test professionals to learn test engineering activities and techniques.
> 
> At this role level, you will:
> - contribute to and maintain technical test suites under supervision
> - follow engineering practices and standards to apply test approaches, plans and strategies under supervision
> - analyse artefacts such as user stories, prototypes, processes and designs with support
> - support the development of reports, recording of outcomes and resolution of defects
> - understand the technical tooling and engineering approach to design and execute tests

### 責任

- 監督のもとで、チームのエンジニアリング標準に従い、簡単な自動テストを書いて保守する。
- 自動テストと手動テストを実行し、結果を正確に記録する。
- 臨床システムとの連携を含め、不具合の調査と報告を手伝う。
- 合成テストデータを使い、テスト環境で情報ガバナンスの規則に従う。
- チームのテストツール、コーディングの実践、臨床安全のプロセスを学ぶ。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../スキル/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 認知 | You can:<br>• explain why it's important to communicate technical concepts in non-technical language<br>• explain the types of communication that can be used with internal and external stakeholders, and their impact |
| [Designing and executing tests](../../スキル/#designing-and-executing-tests) | UK GDaD PCF | 認知 | You can:<br>• contribute to deciding the most appropriate test types and techniques to use<br>• follow guidance to design, build and maintain simple tests that align to user needs and requirements<br>• execute simple tests with support<br>• explain the value of automation within testing |
| [Managing, reporting and resolving defects](../../スキル/#managing-reporting-and-resolving-defects) | UK GDaD PCF | 認知 | You can:<br>• explain how to report and track defects<br>• follow a defect management process to report, communicate and maintain defects with appropriate information<br>• retest and escalate defects when needed |
| [Test analysis](../../スキル/#test-analysis) | UK GDaD PCF | 認知 | You can:<br>• describe quality characteristics and explain why they are important<br>• analyse information, such as user stories, prototypes, processes and designs, with support<br>• explain what might be a risk in achieving quality goals |
| [Test and quality planning](../../スキル/#test-and-quality-planning) | UK GDaD PCF | 認知 | You can:<br>• explain the value of quality testing approaches, plans and strategies<br>• explain how different delivery methodologies affect quality testing approaches, plans and strategies<br>• follow quality testing approaches, plans and strategies, with support<br>• explain how to measure the effectiveness of quality testing approaches, plans and strategies, and why it’s important |
| [Test engineering](../../スキル/#test-engineering) | UK GDaD PCF | 認知 | You can:<br>• explain why testing processes, environments and tools are important<br>• follow test engineering practices and standards, with support<br>• support the maintenance of automated tests and tools required for testing |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 認知 | できること:<br>• 保健・ケアのシステムの主な部分と、組織が支えるサービスを説明する<br>• 自分の仕事で、患者の安全と秘密保持が重要な理由を説明する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 認知 | できること:<br>• 誤った、欠けた、または遅れた情報などを通じて、医療 IT システムがどう患者に害を及ぼしうるかを説明する<br>• 臨床安全上の問題の可能性を、適切な経路で報告する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 認知 | できること:<br>• 個人情報と健康情報の取り扱いに関する組織の規則に従う<br>• データ侵害やヒヤリハットを見分けて報告する |

### 一般的な資格と経験

- コーディングまたはテストの一定の経験、または関連するアプレンティスシップへの在籍、または同等のもの。

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
| 7 | 方針とサービス開発に対する責任 | 2 | 12 |
| 8 | 財務・物的資源に対する責任 | 1 | 5 |
| 9 | 人に対する責任 | 1 | 5 |
| 10 | 情報資源に対する責任 | 3 | 16 |
| 11 | 研究開発に対する責任 | 2 | 12 |
| 12 | 行動の自由度 | 2 | 12 |
| 13 | 身体的負荷 | 2 | 7 |
| 14 | 精神的負荷 | 3 | 12 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **275** (バンド 4: 271–325) |

## バンド 6: テストエンジニア

**UK GDaD PCF のレベル: Test engineer**

> A test engineer develops solutions to enable more efficient testing. They follow engineering standards to design and execute appropriate technical tests.
> 
> At this role level, you will:
> - determine test scope and estimate the effort required
> - select and use the most appropriate test approaches and techniques to mitigate risk
> - use technical tooling and engineering approaches to design and execute tests
> - develop and maintain technical test suites
> - develop reports, record outcomes and support the resolution of defects
> - contribute to and follow engineering practices and standards

### 責任

- 臨床向けおよび患者向けのサービスの、自動化された機能、連携、API のテストを設計し、構築する。
- HL7 FHIR プロファイルやその他の相互運用性の仕様に照らして、メッセージを確認するテストを構築する。
- 現実的なケースとエッジケースの臨床ケースを網羅する、合成の患者データを生成する。
- 安全に関するチェックがすべての変更で実行されるよう、デリバリーパイプラインにテストを追加する。
- テストの工数を見積もり、結果を報告し、不具合の解決を支援する。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../スキル/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 実務 | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Designing and executing tests](../../スキル/#designing-and-executing-tests) | UK GDaD PCF | 実務 | You can:<br>• set up suitable environments with some support<br>• select appropriate test types and techniques with some support<br>• design, build, maintain and execute tests that align to user needs and requirements<br>• conduct exploratory testing<br>• research and try new test types and techniques |
| [Managing, reporting and resolving defects](../../スキル/#managing-reporting-and-resolving-defects) | UK GDaD PCF | 実務 | You can:<br>• collaborate with others to create a defect management process to report, communicate and resolve defects, with support<br>• critically assess dependencies, defects and risks, with support<br>• contribute to mitigation and contingency plans<br>• clearly communicate risks and the impact of defects to stakeholders |
| [Test analysis](../../スキル/#test-analysis) | UK GDaD PCF | 実務 | You can:<br>• work with stakeholders to determine which functional and non-functional quality characteristics add value<br>• determine what to test following an agreed approach<br>• identify and advocate for test needs, such as data, access and environments, with support<br>• analyse information to identify risks |
| [Test and quality planning](../../スキル/#test-and-quality-planning) | UK GDaD PCF | 実務 | You can:<br>• create or adapt quality testing approaches based on risk, with some support<br>• follow a quality testing strategy and contribute to its development<br>• contribute to continuous improvement of quality testing approaches, plans and strategies |
| [Test engineering](../../スキル/#test-engineering) | UK GDaD PCF | 実務 | You can:<br>• use test engineering frameworks and tools to support testing activities<br>• follow test engineering practices and standards, such as source control and continuous integration, continuous delivery (CI/CD) pipelines<br>• integrate and execute tests to ensure early testing and continuous feedback<br>• create and maintain automated tests, with some support<br>• write and review coded solutions, with some support |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実務 | できること:<br>• 自分の仕事が支える臨床・ケアのワークフローを説明する<br>• 臨床・ケアの同僚と、一般的な医療用語を正しく使う<br>• 変更が患者のケアにいつ影響しうるかを見分けて伝える |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実務 | できること:<br>• ハザードのワークショップに参加し、ハザードログに寄与する<br>• 自分の仕事のために、臨床リスク管理プロセスに従う<br>• テスト結果など、臨床安全ケースのための根拠を提供する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | 実務 | できること:<br>• FHIR のリソース、プロファイル、API を読み、使う<br>• 指導を受けながら、簡単な連携を構築またはテストする<br>• メッセージを仕様に照らして確認する |

### 一般的な資格と経験

- コンピューティングまたは関連する科目の学位、または同等の経験。
- 自動テストを構築した経験。

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
| 9 | 人に対する責任 | 1 | 5 |
| 10 | 情報資源に対する責任 | 4 | 24 |
| 11 | 研究開発に対する責任 | 2 | 12 |
| 12 | 行動の自由度 | 4 | 32 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 4 | 18 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **411** (バンド 6: 396–465) |

## バンド 7: シニア テストエンジニア

**UK GDaD PCF のレベル: Senior test engineer**

> A senior test engineer is responsible for test engineering in their area. They influence, coach and guide others in test engineering, sharing best practice and standards.
> 
> At this role level, you will:
> - select, use and guide others in using the most appropriate technical tooling, engineering approaches, test types and techniques to identify and address risks early
> - extend, standardise and build reusable frameworks and tools that support testing
> - communicate and document chosen approaches, tools, techniques and outcomes to the team and appropriate stakeholders
> - contribute to and agree engineering standards

### 責任

- 領域のテストエンジニアリングを主導し、そのリスクに早期に対処するツール、フレームワーク、テストの種類を選ぶ。
- 臨床システムとパートナー連携のために、再利用可能なテストフレームワークとシミュレーターを構築する。
- 実際の臨床の需要にもとづいて、性能、負荷、レジリエンスのテストを計画し、実行する。
- 自動テストがハザードと安全の管理策にたどれるようにし、安全ケースのための根拠を生むようにする。
- 他のテストエンジニアをコーチして導き、開発者とエンジニアリング標準に合意する。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../スキル/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 実践者 | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Designing and executing tests](../../スキル/#designing-and-executing-tests) | UK GDaD PCF | 実践者 | You can:<br>• set up suitable environments<br>• influence and guide the use of appropriate test types and techniques to mitigate risk early<br>• lead others in designing, building, maintaining and executing tests that align to user needs and requirements<br>• contribute to developing and implementing standards for designing and executing tests<br>• improve test types and techniques through a structured process. |
| [Managing, reporting and resolving defects](../../スキル/#managing-reporting-and-resolving-defects) | UK GDaD PCF | 実践者 | You can:<br>• contribute to developing standards for defect management processes<br>• manage and escalate dependencies, defects and risks across teams<br>• contribute to mitigation and contingency plans across teams<br>• use defect patterns and trends to make recommendations on testing and quality approaches, with support<br>• manage stakeholder expectations and communications during defect resolution |
| [Test analysis](../../スキル/#test-analysis) | UK GDaD PCF | 実践者 | You can:<br>• lead work with stakeholders across teams to determine which functional and non-functional quality characteristics add value<br>• determine if an approach needs to change based on effort and risk<br>• ensure test needs are implemented early<br>• use multiple techniques to analyse complex information to identify risks<br>• coach others in test analysis |
| [Test and quality planning](../../スキル/#test-and-quality-planning) | UK GDaD PCF | 実践者 | You can:<br>• work with teams to develop and implement appropriate quality testing approaches, plans and strategies<br>• contribute to organisational quality testing strategies<br>• implement ways to capture data to drive continuous improvement of quality testing approaches, plans and strategies<br>• advocate for full team ownership of quality testing activities, encouraging early engagement |
| [Test engineering](../../スキル/#test-engineering) | UK GDaD PCF | 実践者 | You can:<br>• develop, standardise and extend reusable frameworks and tools to support a range of testing activities<br>• guide and coach others in creating and maintaining comprehensive and reliable tests that meet standards<br>• research and prepare for future testing needs, including tools, methodologies and techniques<br>• maintain and adapt continuous integration, continuous delivery (CI/CD) pipelines |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実務 | できること:<br>• 自分の仕事が支える臨床・ケアのワークフローを説明する<br>• 臨床・ケアの同僚と、一般的な医療用語を正しく使う<br>• 変更が患者のケアにいつ影響しうるかを見分けて伝える |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実務 | できること:<br>• ハザードのワークショップに参加し、ハザードログに寄与する<br>• 自分の仕事のために、臨床リスク管理プロセスに従う<br>• テスト結果など、臨床安全ケースのための根拠を提供する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | 実践者 | できること:<br>• FHIR、HL7 バージョン 2、メッセージングパターンを使って連携を設計し、構築する<br>• FHIR リソースと実装ガイドを書き、プロファイル化する<br>• システム間の複雑なマッピングやデータ品質の問題を解決する |
| [医療機器ソフトウェアの規制](../../スキル/#医療機器ソフトウェアの規制) | このリファレンス | 認知 | できること:<br>• 一部の医療ソフトウェアが医療機器として規制されることを説明する<br>• 製品が医療機器にあたるかもしれないとき、誰に尋ねればよいかを知っている |

### 一般的な資格と経験

- テストエンジニアリングの相当の経験(修士相当のレベル)。

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

## バンド 8a: リード テストエンジニア

**UK GDaD PCF のレベル: Lead test engineer**

> A lead test engineer sets the strategy for test engineering and influences test engineering practices across a broad area. They develop, monitor and evaluate quality engineering standards, and make strategic improvements to quality engineering in the organisation.
> 
> At this role level, you will:
> - lead a broad area in technical tooling, engineering approaches and test types and techniques to address risks early
> - define engineering standards, enabling others to follow them
> - lead and guide teams in quality engineering strategies and practices
> - lead and guide test engineers
> - escalate risks to senior stakeholders
> - lead and implement continuous testing, identifying opportunities to test earlier

### 責任

- デリバリーパイプラインでの継続的テストを含め、幅広い領域のテストエンジニアリングの戦略と標準を定める。
- テストエンジニアとチームを率い、品質エンジニアリングの実践を導く。
- 規制対象や安全上重要なソフトウェアのテストが、必要な標準を満たし、トレーサブルであるようにする。
- 品質と安全のリスクを、プロダクト、臨床、供給者のシニアリードにエスカレーションする。
- より早く、より頻繁にテストする機会を見つけ、それが品質に与える影響を測定する。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../スキル/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | エキスパート | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Designing and executing tests](../../スキル/#designing-and-executing-tests) | UK GDaD PCF | エキスパート | You can:<br>• set standards and influence organisational decisions for test types, techniques, design and execution<br>• coach others in test types, techniques, design and execution<br>• advocate for continuous improvement and refinement of test types and techniques<br>• make strategic decisions on new or improved test types and techniques used in your area |
| [Managing, reporting and resolving defects](../../スキル/#managing-reporting-and-resolving-defects) | UK GDaD PCF | エキスパート | You can:<br>• lead and coach others in improving test and defect management processes<br>• support others in assessing complex and challenging defects across the organisation<br>• lead and coach others in using defect patterns and trends to make tactical and strategic recommendations<br>• influence improvements to quality processes, informed by defect patterns and trends |
| [Test analysis](../../スキル/#test-analysis) | UK GDaD PCF | エキスパート | You can:<br>• lead and guide multiple teams in test analysis, ensuring it is implemented early in the life cycle<br>• advocate for risk-based analysis to drive improvements across many teams<br>• set standards and principles for test analysis across the organisation |
| [Test and quality planning](../../スキル/#test-and-quality-planning) | UK GDaD PCF | エキスパート | You can:<br>• create and manage multiple quality testing plans, approaches and strategies<br>• lead and guide multiple teams in adopting quality testing strategy<br>• advocate for early quality testing involvement in organisational delivery processes<br>• guide teams across an organisation in optimising quality testing approaches, plans and strategies by using appropriate data |
| [Test engineering](../../スキル/#test-engineering) | UK GDaD PCF | エキスパート | You can:<br>• establish and lead test engineering practices, standards and behaviours<br>• influence and guide test engineering technology and tool choices across the organisation<br>• advocate for the adoption and use of appropriate testing solutions, ensuring alignment with organisational goals and quality objectives |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実践者 | できること:<br>• サービスが組織間のケアパスにどう収まるかを分析する<br>• 臨床医、ケア職員、患者と協力して、デジタルサービスを形づくる<br>• デジタルに関する決定が、ケア、安全、職員の業務量に与える影響を説明する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実践者 | できること:<br>• プロダクトや変更のハザード特定とリスク評価を主導する<br>• ハザードログと臨床安全ケース報告書を書き、維持する<br>• プロダクトチームとリスクの管理策に合意し、それが機能しているかを確認する<br>• 臨床リスク管理の基準の適用について、チームに助言する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | 実践者 | できること:<br>• FHIR、HL7 バージョン 2、メッセージングパターンを使って連携を設計し、構築する<br>• FHIR リソースと実装ガイドを書き、プロファイル化する<br>• システム間の複雑なマッピングやデータ品質の問題を解決する |
| [医療機器ソフトウェアの規制](../../スキル/#医療機器ソフトウェアの規制) | このリファレンス | 実務 | できること:<br>• 医療機器の標準を満たすソフトウェアライフサイクルのプロセスに従う<br>• そのプロセスが必要とする記録を作成する |
| [ピープルマネジメント](../../スキル/#ピープルマネジメント) | このリファレンス | 実務 | できること:<br>• 日々の業務を監督し、フィードバックを与える<br>• 採用と導入研修に参加する<br>• 定期的に 1 対 1 の対話を行う |

### 一般的な資格と経験

- 複雑なサービスのテストエンジニアリングを率いた豊富な経験。

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
| 8 | 財務・物的資源に対する責任 | 1 | 5 |
| 9 | 人に対する責任 | 3 | 21 |
| 10 | 情報資源に対する責任 | 5 | 34 |
| 11 | 研究開発に対する責任 | 3 | 21 |
| 12 | 行動の自由度 | 5 | 45 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 4 | 18 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **553** (バンド 8a: 540–584) |

UK GDaD PCF はこのレベルに、シニアテストエンジニアと同じバンド 7 に対応する SEO から G6 を示唆している。このリファレンスは、幅広い領域のテストエンジニアリングの戦略と標準を定めるため、バンド 8a に置いている。


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
