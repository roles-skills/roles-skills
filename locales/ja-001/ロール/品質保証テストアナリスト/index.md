# 品質保証テストアナリスト

> これは、一般的なデジタルヘルスケア組織のための例示的な参照プロファイルです。特定の雇用主の公式な職務記述書ではなく、職務評価のスコアも正式な評価ではありません。

> このテキストは英語から AI アシスタントによって翻訳されたもので、日本語を母語とする方による確認はまだ行われていません。英国政府デジタル・データ専門職能力フレームワーク(UK GDaD PCF)と ESCO からの引用は英語のままです。

**職群:** [品質保証とテスト](../../#品質保証とテスト)  
**バンド:** 4, 5, 6, 8a  
**UK GDaD PCF のロール:** [Quality assurance test analyst](https://understand-digital-data-roles-skills.service.gov.uk/role/quality-assurance-test-analyst/)  
**ESCO の職業:** [ICT test analyst](http://data.europa.eu/esco/occupation/0ab5c12c-c1c1-4772-8345-aa287d0e391d) (ISCO-08 2519)

## 概要

品質保証テストアナリストは、組織のデジタルヘルスサービスが、患者、臨床医、ケア職員が必要とすることを、安全かつ確実に果たしているかを確認する。要件や設計を分析してリスクを早期に見つけ、機能テストと非機能テストを設計して実行し、不具合を明確に報告する。医療では、臨床ワークフロー、データの正確さ、患者を害から守る管理策のテストも含まれる。

## デジタルヘルスケア組織において

- 臨床システムの不具合は、誤った投薬量、見落とされた結果、他の患者の記録の表示などを通じて、患者に害を及ぼしうるため、テストは臨床リスクで優先順位がつけられる。
- テストは臨床安全ケースとハザードログのための根拠を提供するため、テスト計画は特定されたハザードとその管理策にたどれるようになっている。
- テストデータが実際の患者を明らかにしてはならないため、アナリストは合成データ、または適切に匿名化されたテストデータを使う。
- 多くのサービスは他の保健・ケアのシステムとデータを交換するため、テストでは、HL7 FHIR などの標準に照らしてメッセージを確認し、臨床コードの意味を確認する。
- 利用者には、時間的プレッシャーのもとにいる臨床医、幅広いニーズを持つ患者、支援技術の利用者が含まれるため、ユーザビリティとアクセシビリティのテストが重要である。

## UK GDaD PCF のロール説明(原文は英語)

> A quality assurance test analyst interprets testing needs, creating and executing appropriate tests to ensure quality and alignment with requirements.
> 
> In this role, you will:
> - plan, design and execute tests
> - apply testing techniques and standards to learn about systems and mitigate risk
> - analyse artefacts and prototypes
> - test outcomes and record defects
> - seek to improve testing practices to enhance quality and reliability
> - recommend testing approaches

## ロールレベル

| バンド | 名称 | UK GDaD PCF のレベル | 英国公務員の等級 | 職務評価の点数 |
| --- | --- | --- | --- | --- |
| 4 | [アソシエイト 品質保証テストアナリスト](#バンド-4-アソシエイト-品質保証テストアナリスト) | Associate quality assurance test analyst | EO | 275 |
| 5 | [品質保証テストアナリスト](#バンド-5-品質保証テストアナリスト) | Quality assurance test analyst | HEO/SEO | 327 |
| 6 | [シニア 品質保証テストアナリスト](#バンド-6-シニア-品質保証テストアナリスト) | Senior quality assurance test analyst | HEO/SEO | 404 |
| 8a | [リード 品質保証テストアナリスト](#バンド-8a-リード-品質保証テストアナリスト) | Lead quality assurance test analyst | G7/G6 | 543 |

## バンド 4: アソシエイト 品質保証テストアナリスト

**UK GDaD PCF のレベル: Associate quality assurance test analyst**

> An associate quality assurance test analyst works with other test professionals to learn quality assurance testing and analysis techniques.
> 
> At this role level, you will:
> - follow and apply test approaches, plans and strategies, under supervision
> - analyse artefacts, such as user stories, prototypes, processes and designs, with support
> - use basic functional and non-functional testing techniques
> - increase your understanding of how to design and execute basic tests, develop reports, record outcomes and support the resolution of defects

### 責任

- 監督のもとで、臨床および事務のワークフローのテストスクリプトを実行し、結果を正確に記録する。
- 手順、データ、関係する画面を含め、明確な不具合報告を起票する。
- 合成テストデータを使い、テスト環境で実際の患者データを決して使わない。
- チームのテストの進め方、ツール、臨床安全のプロセスを学ぶ。
- スタンドアップ、計画、振り返りなど、チームの儀式に参加する。

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

- 優れた分析力と文章力、およびテストやデジタルシステムを扱った一定の経験、または同等のもの。

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

## バンド 5: 品質保証テストアナリスト

**UK GDaD PCF のレベル: Quality assurance test analyst**

> A quality assurance test analyst designs and executes appropriate functional and non-functional tests. They apply multiple testing techniques to inform the approach to mitigate risk.
> 
> At this role level, you will:
> - apply the most appropriate test approaches and plans based on risk
> - analyse artefacts, such as user stories, prototypes, processes and designs
> - determine what to test following an agreed approach
> - ensure test coverage aligns with business risk
> - follow appropriate standards to mitigate risk early
> - execute tests, develop reports, record outcomes and support the resolution of defects

### 責任

- ユーザーストーリー、設計、臨床ワークフローを分析し、患者とサービスへのリスクにもとづいて、何をテストするかを決める。
- エンドツーエンドの臨床シナリオを含め、機能、アクセシビリティ、ユーザビリティのテストを設計して実行する。
- テストをハザードと安全の管理策にたどれるようにし、臨床安全ケースのためのテストの根拠を提供する。
- 利用者に表示されるデータを、元のシステムと合意された臨床コードに照らして確認する。
- 現実的な合成テストデータを作成し、維持する。
- 不具合を解決まで追跡し、修正を再テストする。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../スキル/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 実務 | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Designing and executing tests](../../スキル/#designing-and-executing-tests) | UK GDaD PCF | 実務 | You can:<br>• set up suitable environments with some support<br>• select appropriate test types and techniques with some support<br>• design, build, maintain and execute tests that align to user needs and requirements<br>• conduct exploratory testing<br>• research and try new test types and techniques |
| [Managing, reporting and resolving defects](../../スキル/#managing-reporting-and-resolving-defects) | UK GDaD PCF | 実務 | You can:<br>• collaborate with others to create a defect management process to report, communicate and resolve defects, with support<br>• critically assess dependencies, defects and risks, with support<br>• contribute to mitigation and contingency plans<br>• clearly communicate risks and the impact of defects to stakeholders |
| [Test analysis](../../スキル/#test-analysis) | UK GDaD PCF | 実務 | You can:<br>• work with stakeholders to determine which functional and non-functional quality characteristics add value<br>• determine what to test following an agreed approach<br>• identify and advocate for test needs, such as data, access and environments, with support<br>• analyse information to identify risks |
| [Test and quality planning](../../スキル/#test-and-quality-planning) | UK GDaD PCF | 実務 | You can:<br>• create or adapt quality testing approaches based on risk, with some support<br>• follow a quality testing strategy and contribute to its development<br>• contribute to continuous improvement of quality testing approaches, plans and strategies |
| [Test engineering](../../スキル/#test-engineering) | UK GDaD PCF | 認知 | You can:<br>• explain why testing processes, environments and tools are important<br>• follow test engineering practices and standards, with support<br>• support the maintenance of automated tests and tools required for testing |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実務 | できること:<br>• 自分の仕事が支える臨床・ケアのワークフローを説明する<br>• 臨床・ケアの同僚と、一般的な医療用語を正しく使う<br>• 変更が患者のケアにいつ影響しうるかを見分けて伝える |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実務 | できること:<br>• ハザードのワークショップに参加し、ハザードログに寄与する<br>• 自分の仕事のために、臨床リスク管理プロセスに従う<br>• テスト結果など、臨床安全ケースのための根拠を提供する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | 認知 | できること:<br>• 相互運用性が連携したケアにとって重要な理由を説明する<br>• HL7 FHIR など、主な医療データ交換標準の名前を挙げる |

### 一般的な資格と経験

- デジタルサービスのテストを設計して実行した経験、または同等のもの。

### バンドの概要

- **知識:** 専門的または技術的な知識。通常は学位または同等の経験による。
- **自律性:** 専門職の基準の範囲で幅広い目標に向けて働き、自分の仕事を計画する。
- **範囲:** チームまたはプロダクト内の自分の専門的な業務。
- **リーダーシップ:** サポート職員やアプレンティスを指導し、その仕事を確認することがある。
- **説明責任:** 自分の専門的な仕事の品質。

### 職務評価(例示)

| # | 要素 | レベル | 点数 |
| --- | --- | --- | --- |
| 1 | コミュニケーションと関係構築のスキル | 4 | 32 |
| 2 | 知識、研修、経験 | 5 | 120 |
| 3 | 分析と判断のスキル | 3 | 27 |
| 4 | 計画と組織化のスキル | 2 | 15 |
| 5 | 身体的スキル | 3 | 27 |
| 6 | 患者・利用者のケアに対する責任 | 1 | 4 |
| 7 | 方針とサービス開発に対する責任 | 2 | 12 |
| 8 | 財務・物的資源に対する責任 | 1 | 5 |
| 9 | 人に対する責任 | 1 | 5 |
| 10 | 情報資源に対する責任 | 3 | 16 |
| 11 | 研究開発に対する責任 | 2 | 12 |
| 12 | 行動の自由度 | 3 | 21 |
| 13 | 身体的負荷 | 2 | 7 |
| 14 | 精神的負荷 | 3 | 12 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **327** (バンド 5: 326–395) |

UK GDaD PCF は、このレベルとシニアレベルの両方に HEO または SEO を示唆しており、どちらもバンド 6 に対応する。このリファレンスは、2 つのレベルが別のバンドになるよう、このレベルをバンド 5、シニアレベルをバンド 6 に置いている。

## バンド 6: シニア 品質保証テストアナリスト

**UK GDaD PCF のレベル: Senior quality assurance test analyst**

> A senior quality assurance test analyst influences and guides others in test analysis, coordinating quality assurance activities in a defined area. They assess the business impact of testing outcomes and use insights to improve quality assurance processes.
> 
> At this role level, you will:
> - use the most appropriate tools and techniques to analyse artefacts such as products, services, processes and change, to identify risks early
> - work with others to support teams in developing approaches, plans and strategy, considering environments, data, tools and resources
> - communicate chosen approaches, tools, techniques and outcomes to stakeholders
> - guide others in quality assurance tools and techniques
> - contribute to, and enable others to follow, quality assurance and testing standards

### 責任

- テストの進め方、環境、データ、ツールに合意しながら、プロダクトまたは領域の品質保証を調整する。
- 臨床医やプロダクトチームとともに要件、設計、変更をレビューして、臨床上および運用上のリスクを早期に特定する。
- 臨床医とケア職員とのユーザー受け入れテストを計画し、主導する。
- プロダクトオーナーと臨床安全責任者がリリースの判断を下せるよう、テストの結果と残存リスクを報告する。
- 他のテストアナリストを導き、テストと臨床安全の標準に従うのを手助けする。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../スキル/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 実践者 | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Designing and executing tests](../../スキル/#designing-and-executing-tests) | UK GDaD PCF | 実践者 | You can:<br>• set up suitable environments<br>• influence and guide the use of appropriate test types and techniques to mitigate risk early<br>• lead others in designing, building, maintaining and executing tests that align to user needs and requirements<br>• contribute to developing and implementing standards for designing and executing tests<br>• improve test types and techniques through a structured process. |
| [Managing, reporting and resolving defects](../../スキル/#managing-reporting-and-resolving-defects) | UK GDaD PCF | 実践者 | You can:<br>• contribute to developing standards for defect management processes<br>• manage and escalate dependencies, defects and risks across teams<br>• contribute to mitigation and contingency plans across teams<br>• use defect patterns and trends to make recommendations on testing and quality approaches, with support<br>• manage stakeholder expectations and communications during defect resolution |
| [Test analysis](../../スキル/#test-analysis) | UK GDaD PCF | 実践者 | You can:<br>• lead work with stakeholders across teams to determine which functional and non-functional quality characteristics add value<br>• determine if an approach needs to change based on effort and risk<br>• ensure test needs are implemented early<br>• use multiple techniques to analyse complex information to identify risks<br>• coach others in test analysis |
| [Test and quality planning](../../スキル/#test-and-quality-planning) | UK GDaD PCF | 実践者 | You can:<br>• work with teams to develop and implement appropriate quality testing approaches, plans and strategies<br>• contribute to organisational quality testing strategies<br>• implement ways to capture data to drive continuous improvement of quality testing approaches, plans and strategies<br>• advocate for full team ownership of quality testing activities, encouraging early engagement |
| [Test engineering](../../スキル/#test-engineering) | UK GDaD PCF | 認知 | You can:<br>• explain why testing processes, environments and tools are important<br>• follow test engineering practices and standards, with support<br>• support the maintenance of automated tests and tools required for testing |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実務 | できること:<br>• 自分の仕事が支える臨床・ケアのワークフローを説明する<br>• 臨床・ケアの同僚と、一般的な医療用語を正しく使う<br>• 変更が患者のケアにいつ影響しうるかを見分けて伝える |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実務 | できること:<br>• ハザードのワークショップに参加し、ハザードログに寄与する<br>• 自分の仕事のために、臨床リスク管理プロセスに従う<br>• テスト結果など、臨床安全ケースのための根拠を提供する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | 実務 | できること:<br>• FHIR のリソース、プロファイル、API を読み、使う<br>• 指導を受けながら、簡単な連携を構築またはテストする<br>• メッセージを仕様に照らして確認する |
| [Business and user acceptance testing](../../スキル/#business-and-user-acceptance-testing) | UK GDaD PCF | 実践者 | You can:<br>• advise others how to ensure appropriate test coverage, data and scenarios, in line with acceptance criteria<br>• analyse business risk and impacts of defects so that appropriate action can be taken to enable business acceptance<br>• provide assurance on the suitability, business readiness and viability of delivered solutions |

### 一般的な資格と経験

- 複雑な、または規制対象の環境を含む、テスト分析の相当の経験、または同等のもの。

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
| 10 | 情報資源に対する責任 | 3 | 16 |
| 11 | 研究開発に対する責任 | 2 | 12 |
| 12 | 行動の自由度 | 4 | 32 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 3 | 12 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **404** (バンド 6: 396–465) |

## バンド 8a: リード 品質保証テストアナリスト

**UK GDaD PCF のレベル: Lead quality assurance test analyst**

> A lead quality assurance test analyst sets the strategy for test analysis and influences test analysis practices across a broad area. They develop, monitor and evaluate test analysis standards and methods, and make strategic decisions that improve test analysis in the organisation.
> 
> At this role level, you will:
> - lead on setting standards and good practices across the test analysis community
> - lead and guide teams across the organisation in test analysis
> - define and implement test strategies
> - mentor and coach other quality assurance test analysts
> - negotiate and escalate major risks, issues and defects

### 責任

- 臨床システムのリスクベースのテストを含め、組織全体のテスト分析の基準とグッドプラクティスを定める。
- 電子患者記録の変更や新しい患者向けサービスなど、主要なプログラムのテスト戦略を定義する。
- テストが、臨床安全ケースと、該当する場合は医療機器の技術文書に必要な根拠を生むようにする。
- プロダクト、臨床、供給者のシニアリードと、重大なリスク、課題、不具合を交渉し、エスカレーションする。
- テストアナリストをメンターしてコーチし、テスト分析のコミュニティを率いる。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../スキル/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | エキスパート | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Designing and executing tests](../../スキル/#designing-and-executing-tests) | UK GDaD PCF | エキスパート | You can:<br>• set standards and influence organisational decisions for test types, techniques, design and execution<br>• coach others in test types, techniques, design and execution<br>• advocate for continuous improvement and refinement of test types and techniques<br>• make strategic decisions on new or improved test types and techniques used in your area |
| [Managing, reporting and resolving defects](../../スキル/#managing-reporting-and-resolving-defects) | UK GDaD PCF | エキスパート | You can:<br>• lead and coach others in improving test and defect management processes<br>• support others in assessing complex and challenging defects across the organisation<br>• lead and coach others in using defect patterns and trends to make tactical and strategic recommendations<br>• influence improvements to quality processes, informed by defect patterns and trends |
| [Test analysis](../../スキル/#test-analysis) | UK GDaD PCF | エキスパート | You can:<br>• lead and guide multiple teams in test analysis, ensuring it is implemented early in the life cycle<br>• advocate for risk-based analysis to drive improvements across many teams<br>• set standards and principles for test analysis across the organisation |
| [Test and quality planning](../../スキル/#test-and-quality-planning) | UK GDaD PCF | エキスパート | You can:<br>• create and manage multiple quality testing plans, approaches and strategies<br>• lead and guide multiple teams in adopting quality testing strategy<br>• advocate for early quality testing involvement in organisational delivery processes<br>• guide teams across an organisation in optimising quality testing approaches, plans and strategies by using appropriate data |
| [Test engineering](../../スキル/#test-engineering) | UK GDaD PCF | 認知 | You can:<br>• explain why testing processes, environments and tools are important<br>• follow test engineering practices and standards, with support<br>• support the maintenance of automated tests and tools required for testing |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実践者 | できること:<br>• サービスが組織間のケアパスにどう収まるかを分析する<br>• 臨床医、ケア職員、患者と協力して、デジタルサービスを形づくる<br>• デジタルに関する決定が、ケア、安全、職員の業務量に与える影響を説明する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実践者 | できること:<br>• プロダクトや変更のハザード特定とリスク評価を主導する<br>• ハザードログと臨床安全ケース報告書を書き、維持する<br>• プロダクトチームとリスクの管理策に合意し、それが機能しているかを確認する<br>• 臨床リスク管理の基準の適用について、チームに助言する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | 実務 | できること:<br>• FHIR のリソース、プロファイル、API を読み、使う<br>• 指導を受けながら、簡単な連携を構築またはテストする<br>• メッセージを仕様に照らして確認する |
| [医療機器ソフトウェアの規制](../../スキル/#医療機器ソフトウェアの規制) | このリファレンス | 実務 | できること:<br>• 医療機器の標準を満たすソフトウェアライフサイクルのプロセスに従う<br>• そのプロセスが必要とする記録を作成する |
| [ピープルマネジメント](../../スキル/#ピープルマネジメント) | このリファレンス | 実務 | できること:<br>• 日々の業務を監督し、フィードバックを与える<br>• 採用と導入研修に参加する<br>• 定期的に 1 対 1 の対話を行う |

### 一般的な資格と経験

- 複雑なサービスのテスト分析を率いた豊富な経験。

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
| 10 | 情報資源に対する責任 | 4 | 24 |
| 11 | 研究開発に対する責任 | 3 | 21 |
| 12 | 行動の自由度 | 5 | 45 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 4 | 18 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **543** (バンド 8a: 540–584) |

UK GDaD PCF はこのレベルに、バンド 8b に対応する G7 または G6 を示唆している。このリファレンスは、すべてのテストではなく 1 つのテスト分野を率いるため、リードテストエンジニアと同じバンド 8a に置いている。テスト責任者はバンド 8c である。


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
