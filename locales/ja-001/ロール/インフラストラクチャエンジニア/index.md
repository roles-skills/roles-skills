# インフラストラクチャエンジニア

> これは、一般的なデジタルヘルスケア組織のための例示的な参照プロファイルです。特定の雇用主の公式な職務記述書ではなく、職務評価のスコアも正式な評価ではありません。

> このテキストは英語から AI アシスタントによって翻訳されたもので、日本語を母語とする方による確認はまだ行われていません。英国政府デジタル・データ専門職能力フレームワーク(UK GDaD PCF)と ESCO からの引用は英語のままです。

**職群:** [IT 運用](../../#it-運用)  
**バンド:** 4, 6, 7, 8a, 8b  
**UK GDaD PCF のロール:** [Infrastructure engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/infrastructure-engineer/)  
**ESCO の職業:** [ICT system administrator](http://data.europa.eu/esco/occupation/9e2e6e1e-363b-4e1b-a673-7bc0f7343300) (ISCO-08 2522); [ICT network engineer](http://data.europa.eu/esco/occupation/cf2b03cd-feb7-4f47-90f6-ff1ed6016d3d) (ISCO-08 2523); [cloud engineer](http://data.europa.eu/esco/occupation/349ee6f6-c295-4c38-9b98-48765b55280e) (ISCO-08 2512)

## 概要

インフラストラクチャエンジニアは、組織のデジタルサービスが依存するネットワーク、サーバー、ストレージ、クラウドプラットフォーム、ホスティングを設計、構築、運用、サポートする。このインフラを利用可能、安全、復旧可能に保ち、供給者やアーキテクトと協力して安全に変更する。医療では、インフラの障害が 1 つでも、病院や地域サービスの臨床システムを一度に止めうる。

## デジタルヘルスケア組織において

- 臨床システムには非常に高い可用性が必要なため、インフラはレジリエンスを考慮して設計され、変更は臨床活動に合わせて計画される。
- 夜間や週末のインフラの障害は患者のケアを止めうるため、エンジニアは待機当番に加わる。
- ネットワークには、輸液ポンプ、患者モニター、画像機器などの医療機器が接続されており、IEC 80001-1 に従ったネットワークのセグメンテーションと慎重な変更が必要である。
- 医療はランサムウェアの標的になりやすいため、バックアップは保護され、テストされ、合意された復旧時間内に復元できなければならない。
- インフラには古い技術と新しい技術が混在することが多く、簡単にパッチを当てられないレガシーな臨床システムも含まれるため、エンジニアは代替の管理策を整える。

## UK GDaD PCF のロール説明(原文は英語)

> An infrastructure engineer designs, builds, manages and supports the infrastructure services that underpin all internal user services and services to the public.

## ロールレベル

| バンド | 名称 | UK GDaD PCF のレベル | 英国公務員の等級 | 職務評価の点数 |
| --- | --- | --- | --- | --- |
| 4 | [アソシエイト インフラストラクチャエンジニア](#バンド-4-アソシエイト-インフラストラクチャエンジニア) | Associate infrastructure engineer | EO | 275 |
| 6 | [インフラストラクチャエンジニア](#バンド-6-インフラストラクチャエンジニア) | Infrastructure engineer | HEO/SEO | 434 |
| 7 | [シニア インフラストラクチャエンジニア](#バンド-7-シニア-インフラストラクチャエンジニア) | Senior infrastructure engineer | SEO/G7 | 490 |
| 8a | [リード インフラストラクチャエンジニア](#バンド-8a-リード-インフラストラクチャエンジニア) | Lead infrastructure engineer | G7/G6 | 560 |
| 8b | [プリンシパル インフラストラクチャエンジニア](#バンド-8b-プリンシパル-インフラストラクチャエンジニア) | Principal infrastructure engineer | G7/G6 | 600 |

## バンド 4: アソシエイト インフラストラクチャエンジニア

**UK GDaD PCF のレベル: Associate infrastructure engineer**

> As a trainee, you will work in an established team and support infrastructure engineers in their daily work, under their direction.

### 責任

- サーバーの構築、バックアップの確認、ネットワークの変更などの定型作業で、インフラストラクチャエンジニアを支える。
- インフラを監視し、アラートと不具合を適切なチームに報告する。
- すべての作業で、変更、セキュリティ、情報ガバナンスの手順に従う。
- 構成と資産の詳細を正確に記録する。
- インフラのアプレンティスシップまたは同等の資格の取得に向けて取り組む。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Information security](../../スキル/#information-security) | UK GDaD PCF | 認知 | You can:<br>• explain information security and the security controls available to protect solutions and services |
| [IT infrastructure](../../スキル/#it-infrastructure) | UK GDaD PCF | 認知 | You can:<br>• support infrastructure solutions and services, and other computer, storage, networking, physical infrastructure, software, commercial-off-the-shelf (COTS) software and open source packages and solutions<br>• support virtual and cloud computing, including Infrastructure as a Service (IaaS), Platform as a Service (PaaS) and Software as a Service (SaaS) |
| [Modern development standards](../../スキル/#modern-development-standards) | UK GDaD PCF | 認知 | You can:<br>• explain the importance of using modern development standards |
| [Ownership and initiative](../../スキル/#ownership-and-initiative) | UK GDaD PCF | 認知 | You can:<br>• show an awareness of problem resolution processes<br>• pass problems on to your team |
| [Problem management](../../スキル/#problem-management) | UK GDaD PCF | 認知 | You can:<br>• investigate problems in systems, processes and services, with an understanding of the level of a problem, for example, strategic, tactical or operational<br>• contribute to the implementation of remedies and preventative measures |
| [Systems design](../../スキル/#systems-design) | UK GDaD PCF | 認知 | You can:<br>• assist as part of a team in the design of components of larger systems |
| [Systems integration](../../スキル/#systems-integration) | UK GDaD PCF | 認知 | You can:<br>• explain the process and principles of integrating systems.<br>• describe challenges of designing, building and testing interfaces between systems |
| [Technical understanding](../../スキル/#technical-understanding) | UK GDaD PCF | 認知 | You can:<br>• show an awareness of the relevant subject matter and a high level understanding of what it involves |
| [Troubleshooting and problem resolution](../../スキル/#troubleshooting-and-problem-resolution) | UK GDaD PCF | 認知 | You can:<br>• show an awareness of different technology capabilities<br>• demonstrate basic troubleshooting capability |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 認知 | できること:<br>• 保健・ケアのシステムの主な部分と、組織が支えるサービスを説明する<br>• 自分の仕事で、患者の安全と秘密保持が重要な理由を説明する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 認知 | できること:<br>• 個人情報と健康情報の取り扱いに関する組織の規則に従う<br>• データ侵害やヒヤリハットを見分けて報告する |
| [セキュリティ運用](../../スキル/#セキュリティ運用) | このリファレンス | 認知 | できること:<br>• フィッシングやランサムウェアなど、一般的なサイバー脅威を説明する<br>• セキュリティイベントの疑いを報告する |
| [脆弱性管理](../../スキル/#脆弱性管理) | このリファレンス | 認知 | できること:<br>• 迅速なパッチ適用と安全な設定が重要な理由を説明する |

### 一般的な資格と経験

- インフラまたはネットワークのアプレンティスシップまたは同等のものに在籍している、または取得を目指している。

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
| 8 | 財務・物的資源に対する責任 | 2 | 12 |
| 9 | 人に対する責任 | 1 | 5 |
| 10 | 情報資源に対する責任 | 3 | 16 |
| 11 | 研究開発に対する責任 | 1 | 5 |
| 12 | 行動の自由度 | 2 | 12 |
| 13 | 身体的負荷 | 2 | 7 |
| 14 | 精神的負荷 | 3 | 12 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **275** (バンド 4: 271–325) |

知識は、仕事ができるだけの研修が終わった時点で職務が必要とするレベルで評価している。

## バンド 6: インフラストラクチャエンジニア

**UK GDaD PCF のレベル: Infrastructure engineer**

> Working in a team of infrastructure specialists and engineers, an infrastructure engineer supports and maintains infrastructure solutions and services as directed and according to departmental policy.
> 
> At this role level, you will:
> - ensure services are delivered and used as required
> - work with and support third parties to provide infrastructure services

### 責任

- 臨床および共通部門のシステムをホスティングする、サーバー、ストレージ、ネットワーク、クラウドサービスを構築、設定、保守する。
- セキュリティリスクと臨床システムを利用可能に保つ必要性のバランスをとりながら、インフラに速やかにパッチを適用する。
- 重要な臨床システムを含め、バックアップとリストアを実行し、テストする。
- 臨床工学チームと協力して、医療機器やその他の臨床機器のためのセグメント化されたネットワークを支える。
- 待機当番の一環としてを含め、インフラの不具合を調査して直す。
- スクリプトと Infrastructure as Code を使って、定型作業を自動化する。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Coding and scripting](../../スキル/#coding-and-scripting) | UK GDaD PCF | 認知 | You can:<br>• describe different scripting tools and software that are available and currently in use |
| [Information security](../../スキル/#information-security) | UK GDaD PCF | 認知 | You can:<br>• explain information security and the security controls available to protect solutions and services |
| [IT infrastructure](../../スキル/#it-infrastructure) | UK GDaD PCF | 実務 | You can:<br>• build, configure, administer and support infrastructure solutions and services, for example, networking and physical infrastructure, commercial-off-the-shelf (COTS) software, open source packages and solutions, or virtual and cloud computing |
| [Modern development standards](../../スキル/#modern-development-standards) | UK GDaD PCF | 実務 | You can:<br>• explain the most important principles of modern development standards and how they apply to your work<br>• apply modern development standards principles under guidance |
| [Ownership and initiative](../../スキル/#ownership-and-initiative) | UK GDaD PCF | 実務 | You can:<br>• own an issue until a new owner has been found or the problem has been mitigated or resolved |
| [Problem management](../../スキル/#problem-management) | UK GDaD PCF | 認知 | You can:<br>• investigate problems in systems, processes and services, with an understanding of the level of a problem, for example, strategic, tactical or operational<br>• contribute to the implementation of remedies and preventative measures |
| [Service focus](../../スキル/#service-focus) | UK GDaD PCF | 実務 | You can:<br>• take inputs and establish coherent frameworks that work |
| [Systems design](../../スキル/#systems-design) | UK GDaD PCF | 実務 | You can:<br>• translate logical designs into physical designs<br>• produce detailed designs<br>• effectively document all work using required standards, methods and tools, including prototyping tools where appropriate<br>• design systems characterised by managed levels of risk, manageable business and technical complexity, and meaningful impact<br>• work with well understood technology and identify appropriate patterns |
| [Systems integration](../../スキル/#systems-integration) | UK GDaD PCF | 実務 | You can:<br>• build and test simple interfaces between systems<br>• work on more complex integration as part of a wider team |
| [Technical understanding](../../スキル/#technical-understanding) | UK GDaD PCF | 実務 | You can:<br>• understand the core technical concepts related to the role, and apply them with guidance |
| [Testing](../../スキル/#testing) | UK GDaD PCF | 認知 | You can:<br>• correctly execute test scripts under supervision<br>• understand the role of testing and how it works |
| [Troubleshooting and problem resolution](../../スキル/#troubleshooting-and-problem-resolution) | UK GDaD PCF | 実務 | You can:<br>• troubleshoot and identify problems across different technology capabilities |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実務 | できること:<br>• 自分の仕事が支える臨床・ケアのワークフローを説明する<br>• 臨床・ケアの同僚と、一般的な医療用語を正しく使う<br>• 変更が患者のケアにいつ影響しうるかを見分けて伝える |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [セキュリティ運用](../../スキル/#セキュリティ運用) | このリファレンス | 認知 | できること:<br>• フィッシングやランサムウェアなど、一般的なサイバー脅威を説明する<br>• セキュリティイベントの疑いを報告する |
| [脆弱性管理](../../スキル/#脆弱性管理) | このリファレンス | 実務 | できること:<br>• 脆弱性スキャンを実行し、結果を報告する<br>• システムのオーナーとともに修正を追跡する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 認知 | できること:<br>• 誤った、欠けた、または遅れた情報などを通じて、医療 IT システムがどう患者に害を及ぼしうるかを説明する<br>• 臨床安全上の問題の可能性を、適切な経路で報告する |

### 一般的な資格と経験

- コンピューティングまたは関連する科目の学位、関連する技術認定、または同等の経験。
- 本番インフラのサポートの経験。

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
| 7 | 方針とサービス開発に対する責任 | 3 | 21 |
| 8 | 財務・物的資源に対する責任 | 2 | 12 |
| 9 | 人に対する責任 | 2 | 12 |
| 10 | 情報資源に対する責任 | 4 | 24 |
| 11 | 研究開発に対する責任 | 2 | 12 |
| 12 | 行動の自由度 | 4 | 32 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 4 | 18 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **434** (バンド 6: 396–465) |

精神的負荷は、時間外の待機当番を含め、予測できない不具合に長時間集中することが頻繁にあることを反映している。

## バンド 7: シニア インフラストラクチャエンジニア

**UK GDaD PCF のレベル: Senior infrastructure engineer**

> Working in a team of infrastructure specialists and engineers, a senior infrastructure engineer builds, administers, supports and maintains solutions as directed and according to departmental policy.
> 
> At this role level, you will:
> - ensure services are integrated, delivered and operated as required
> - work with and support third parties in providing infrastructure services
> - work with technical architects to translate architectural designs into operations
> - provide input into overall management - workforce, budget, technology roadmaps, projects and tasks
> - lead and direct infrastructure specialist teams in building, managing, supporting and maintaining solutions according to departmental policy (if taking a managerial path)

### 責任

- アーキテクトの設計から、臨床サービスが必要とするレジリエンスを備えたインフラソリューションを設計し、構築する。
- データセンターの移転、ネットワークの更新、クラウド移行などの大規模なインフラの変更を、臨床活動に合わせて計画し、主導する。
- 重要な臨床システムの災害復旧とランサムウェアからの復旧を設計し、テストする。
- インフラのインシデントへの技術的な対応を主導し、その原因の修正を推進する。
- パッチを当てられないレガシーシステムや医療機器のための代替の管理策を管理する。
- インフラストラクチャエンジニアを率い、コーチする。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Coding and scripting](../../スキル/#coding-and-scripting) | UK GDaD PCF | 認知 | You can:<br>• describe different scripting tools and software that are available and currently in use |
| [Information security](../../スキル/#information-security) | UK GDaD PCF | 実務 | You can:<br>• use information security practices and available security controls to contribute to protecting solutions and services |
| [IT infrastructure](../../スキル/#it-infrastructure) | UK GDaD PCF | 実践者 | You can:<br>• design and implement infrastructure solutions and services, for example, networking and physical infrastructure, commercial-off-the-shelf (COTS) software, open source packages and solutions, or virtual and cloud computing |
| [Modern development standards](../../スキル/#modern-development-standards) | UK GDaD PCF | 実践者 | You can:<br>• apply modern development standards and support others in applying them |
| [Ownership and initiative](../../スキル/#ownership-and-initiative) | UK GDaD PCF | 実務 | You can:<br>• own an issue until a new owner has been found or the problem has been mitigated or resolved |
| [Problem management](../../スキル/#problem-management) | UK GDaD PCF | 実務 | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Service focus](../../スキル/#service-focus) | UK GDaD PCF | 実務 | You can:<br>• take inputs and establish coherent frameworks that work |
| [Systems design](../../スキル/#systems-design) | UK GDaD PCF | 実践者 | You can:<br>• design systems characterised by medium levels of risk, impact, and business or technical complexity<br>• select appropriate design standards, methods and tools, and ensure they are applied effectively<br>• review the systems designs of others to ensure the selection of appropriate technology, efficient use of resources and integration of multiple systems and technology |
| [Systems integration](../../スキル/#systems-integration) | UK GDaD PCF | 実践者 | You can:<br>• define the integration build<br>• co-ordinate build activities across systems<br>• understand how to undertake and support integration testing activities |
| [Technical understanding](../../スキル/#technical-understanding) | UK GDaD PCF | 実践者 | You can:<br>• show a thorough understanding of the technical concepts required for the role, and can explain how these fit into the wider technical landscape |
| [Testing](../../スキル/#testing) | UK GDaD PCF | 実務 | You can:<br>• review requirements and specifications, and define test conditions<br>• identify issues and risks associated with work<br>• analyse and report test activities and results |
| [Troubleshooting and problem resolution](../../スキル/#troubleshooting-and-problem-resolution) | UK GDaD PCF | 実践者 | You can:<br>• break a problem down into its component parts to identify and diagnose root causes<br>• troubleshoot and identify problems across different technology capabilities |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実務 | できること:<br>• 自分の仕事が支える臨床・ケアのワークフローを説明する<br>• 臨床・ケアの同僚と、一般的な医療用語を正しく使う<br>• 変更が患者のケアにいつ影響しうるかを見分けて伝える |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [セキュリティ運用](../../スキル/#セキュリティ運用) | このリファレンス | 実務 | できること:<br>• アラートを監視し、ランブックを使ってトリアージする<br>• 証拠を集め、イベントをエスカレーションする<br>• 指導を受けながら、簡単な検知ルールを調整する |
| [脆弱性管理](../../スキル/#脆弱性管理) | このリファレンス | 実践者 | できること:<br>• 患者サービスへのリスクを含め、リスクで脆弱性に優先順位をつける<br>• ペネトレーションテストと是正の範囲を定め、管理する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実務 | できること:<br>• ハザードのワークショップに参加し、ハザードログに寄与する<br>• 自分の仕事のために、臨床リスク管理プロセスに従う<br>• テスト結果など、臨床安全ケースのための根拠を提供する |
| [組織のリスクマネジメント](../../スキル/#組織のリスクマネジメント) | このリファレンス | 実務 | できること:<br>• 自分の領域のリスクを記録し、更新する<br>• 管理策を提案し、対応を追跡する |

### 一般的な資格と経験

- 本番インフラの設計と運用の相当の経験(大学院ディプロマ相当のレベル)。

### バンドの概要

- **知識:** 高度に発達した専門知識。通常は修士相当または同等の経験による。
- **自律性:** 組織の方針に沿って働き、成果の出し方を決め、他の人が相談する専門家である。
- **範囲:** 複数のプロダクトやサービス、または専門機能。
- **リーダーシップ:** チームまたは専門実務の領域を率いる。
- **説明責任:** サービスまたは専門機能の提供と、予算を持つ場合はその予算。

### 職務評価(例示)

| # | 要素 | レベル | 点数 |
| --- | --- | --- | --- |
| 1 | コミュニケーションと関係構築のスキル | 5 | 45 |
| 2 | 知識、研修、経験 | 6 | 156 |
| 3 | 分析と判断のスキル | 4 | 42 |
| 4 | 計画と組織化のスキル | 4 | 42 |
| 5 | 身体的スキル | 3 | 27 |
| 6 | 患者・利用者のケアに対する責任 | 1 | 4 |
| 7 | 方針とサービス開発に対する責任 | 3 | 21 |
| 8 | 財務・物的資源に対する責任 | 3 | 21 |
| 9 | 人に対する責任 | 3 | 21 |
| 10 | 情報資源に対する責任 | 5 | 34 |
| 11 | 研究開発に対する責任 | 2 | 12 |
| 12 | 行動の自由度 | 4 | 32 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 4 | 18 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **490** (バンド 7: 466–539) |

精神的負荷は、時間外を含め、インシデントや複雑な変更の間に長時間集中することが頻繁にあることを反映している。

## バンド 8a: リード インフラストラクチャエンジニア

**UK GDaD PCF のレベル: Lead infrastructure engineer**

> A lead infrastructure engineer manages third party provision of infrastructure services and the provision of expertise to develop architectural solutions for infrastructure services, throughout the service product life cycle.
> 
> At this role level, you will:
> - oversee programmes and projects
> - work with technical architects to translate the architectural designs into operations and support technical architects in operationalising the designs
> - lead and direct infrastructure specialist teams in building, managing, supporting and maintaining solutions according to departmental policy (if taking a managerial path)

### 責任

- 主要なプラットフォームまたはサービス群のインフラを主導し、その技術的な方向性を定める。
- サードパーティのインフラ供給者を管理し、可用性と復旧に関するサービスレベルを守らせる。
- ネットワークの更新やクラウドホスティングへの移行など、インフラのプログラムを監督する。
- インフラがセキュリティ、情報ガバナンス、医療機器ネットワークの標準を満たすようにする。
- インフラのチームを率い、そのスキルを育成する。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Coding and scripting](../../スキル/#coding-and-scripting) | UK GDaD PCF | 実務 | You can:<br>• interact with, read and write code<br>• carry out baseline repair activities |
| [Information security](../../スキル/#information-security) | UK GDaD PCF | 実践者 | You can:<br>• design solutions and services with security controls included, specifically engineered to mitigate security threats |
| [IT infrastructure](../../スキル/#it-infrastructure) | UK GDaD PCF | エキスパート | You can:<br>• lead teams and departments in the design, implementation, administration and support of infrastructure solutions and services |
| [Modern development standards](../../スキル/#modern-development-standards) | UK GDaD PCF | エキスパート | You can:<br>• identify and apply modern development standards to support complex projects and programmes<br>• lead others in applying modern development standards |
| [Ownership and initiative](../../スキル/#ownership-and-initiative) | UK GDaD PCF | 実践者 | You can:<br>• take accountability for issues that occur and be proactive in searching for potential problems<br>• achieve excellent user outcomes |
| [Problem management](../../スキル/#problem-management) | UK GDaD PCF | 実務 | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Service focus](../../スキル/#service-focus) | UK GDaD PCF | 実務 | You can:<br>• take inputs and establish coherent frameworks that work |
| [Systems design](../../スキル/#systems-design) | UK GDaD PCF | 実践者 | You can:<br>• design systems characterised by medium levels of risk, impact, and business or technical complexity<br>• select appropriate design standards, methods and tools, and ensure they are applied effectively<br>• review the systems designs of others to ensure the selection of appropriate technology, efficient use of resources and integration of multiple systems and technology |
| [Systems integration](../../スキル/#systems-integration) | UK GDaD PCF | エキスパート | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Technical understanding](../../スキル/#technical-understanding) | UK GDaD PCF | エキスパート | You can:<br>• anticipate and advise on future technology changes that present opportunities for the product or programme |
| [Testing](../../スキル/#testing) | UK GDaD PCF | 実践者 | You can:<br>• manage the planning of system and acceptance tests, co-ordinating both functional and non-functional specifications<br>• provide authoritative advice and guidance on test planning<br>• identify process improvements and contribute to the definition of best practice |
| [Troubleshooting and problem resolution](../../スキル/#troubleshooting-and-problem-resolution) | UK GDaD PCF | エキスパート | You can:<br>• use lateral thinking to break a problem down into its component parts to identify and diagnose root causes<br>• troubleshoot and identify problems across different technology capabilities including computing, storage, networking, physical infrastructure, software, commercial-off-the-shelf software (COTS) and open source software |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実践者 | できること:<br>• サービスが組織間のケアパスにどう収まるかを分析する<br>• 臨床医、ケア職員、患者と協力して、デジタルサービスを形づくる<br>• デジタルに関する決定が、ケア、安全、職員の業務量に与える影響を説明する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実践者 | できること:<br>• データ保護影響評価と情報共有契約を主導する<br>• 適法な根拠、同意、秘密保持、保存について、チームに助言する<br>• インシデントを調査し、改善を勧告する |
| [セキュリティ運用](../../スキル/#セキュリティ運用) | このリファレンス | 実務 | できること:<br>• アラートを監視し、ランブックを使ってトリアージする<br>• 証拠を集め、イベントをエスカレーションする<br>• 指導を受けながら、簡単な検知ルールを調整する |
| [脆弱性管理](../../スキル/#脆弱性管理) | このリファレンス | 実践者 | できること:<br>• 患者サービスへのリスクを含め、リスクで脆弱性に優先順位をつける<br>• ペネトレーションテストと是正の範囲を定め、管理する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実務 | できること:<br>• ハザードのワークショップに参加し、ハザードログに寄与する<br>• 自分の仕事のために、臨床リスク管理プロセスに従う<br>• テスト結果など、臨床安全ケースのための根拠を提供する |
| [組織のリスクマネジメント](../../スキル/#組織のリスクマネジメント) | このリファレンス | 実践者 | できること:<br>• ディレクトレートまたはプログラムのリスクプロセスを運営する<br>• リスクをリスク選好に照らして評価し、エスカレーションする<br>• リスクを委員会に報告する |
| [ピープルマネジメント](../../スキル/#ピープルマネジメント) | このリファレンス | 実践者 | できること:<br>• 目標を設定し、評価を行いながら、チームをライン管理する<br>• 心身の健康を支え、勤怠、実績、行為を管理する<br>• チームの育成と後継者計画を立てる |

### 一般的な資格と経験

- 複雑で高可用性のサービスのインフラエンジニアリングを率いた豊富な経験。

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
| 8 | 財務・物的資源に対する責任 | 3 | 21 |
| 9 | 人に対する責任 | 3 | 21 |
| 10 | 情報資源に対する責任 | 5 | 34 |
| 11 | 研究開発に対する責任 | 2 | 12 |
| 12 | 行動の自由度 | 5 | 45 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 4 | 18 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **560** (バンド 8a: 540–584) |

UK GDaD PCF は、リードとプリンシパルのインフラストラクチャエンジニアの両方にバンド 8b を示唆している。このリファレンスは、他の技術職群のリードとプリンシパルのロールに合わせて、2 つのレベルが別のバンドになるよう、リードをバンド 8a に置いている。

## バンド 8b: プリンシパル インフラストラクチャエンジニア

**UK GDaD PCF のレベル: Principal infrastructure engineer**

> A principal infrastructure engineer is an accomplished technical leader.
> 
> At this role level, you will:
> - develop strategic and tactical engineering roadmaps for technologies and services in your area of responsibility, ensuring they're future-proofed and that the organisation derives maximum value from investment in technologies
> - potentially own the operational relationships with suppliers, ensuring services and products are delivered and aligned to industry best practice and regulatory and contractual requirements
> - work with technical architects to translate the architectural designs into operations and support technical architects in operationalising the designs
> - lead and direct infrastructure specialist teams in building, managing, supporting and maintaining solutions according to departmental policy (if taking a managerial path)

### 責任

- 投資が臨床サービスのためにレジリエントで、安全で、持続可能なホスティングをもたらすよう、インフラの戦略とロードマップを策定する。
- 戦略的なインフラおよびネットワークの供給者との運用上の関係を担う。
- 寿命を迎えた技術、単一障害点、サイバーレジリエンスを含め、インフラのリスクについて、シニアリーダーに助言する。
- サービスオーナーとともに臨床システムの目標復旧時間と目標復旧時点を定め、インフラがそれを満たせるようにする。
- 組織全体でインフラエンジニアリング専門職を率い、その能力を育てる。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Coding and scripting](../../スキル/#coding-and-scripting) | UK GDaD PCF | 実務 | You can:<br>• interact with, read and write code<br>• carry out baseline repair activities |
| [Information security](../../スキル/#information-security) | UK GDaD PCF | 実践者 | You can:<br>• design solutions and services with security controls included, specifically engineered to mitigate security threats |
| [IT infrastructure](../../スキル/#it-infrastructure) | UK GDaD PCF | 実践者 | You can:<br>• design and implement infrastructure solutions and services, for example, networking and physical infrastructure, commercial-off-the-shelf (COTS) software, open source packages and solutions, or virtual and cloud computing |
| [Modern development standards](../../スキル/#modern-development-standards) | UK GDaD PCF | エキスパート | You can:<br>• identify and apply modern development standards to support complex projects and programmes<br>• lead others in applying modern development standards |
| [Ownership and initiative](../../スキル/#ownership-and-initiative) | UK GDaD PCF | 実践者 | You can:<br>• take accountability for issues that occur and be proactive in searching for potential problems<br>• achieve excellent user outcomes |
| [Problem management](../../スキル/#problem-management) | UK GDaD PCF | 実践者 | You can:<br>• ensure that the right actions are taken to investigate, resolve and anticipate problems<br>• co-ordinate the team to investigate problems, implement solutions and take preventive measures |
| [Service focus](../../スキル/#service-focus) | UK GDaD PCF | 実践者 | You can:<br>• see the bigger picture by taking groups of services and investigating how to get the best of underlying services |
| [Systems design](../../スキル/#systems-design) | UK GDaD PCF | エキスパート | You can:<br>• design systems characterised by high levels of risk, impact, and business or technical complexity<br>• control system design practice within an enterprise or industry architecture<br>• influence industry-based models for the development of new technology applications<br>• develop effective implementation and procurement strategies, consistent with business needs<br>• ensure adherence to relevant technical strategies, policies, standards and practices |
| [Systems integration](../../スキル/#systems-integration) | UK GDaD PCF | エキスパート | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Technical understanding](../../スキル/#technical-understanding) | UK GDaD PCF | 実践者 | You can:<br>• show a thorough understanding of the technical concepts required for the role, and can explain how these fit into the wider technical landscape |
| [Testing](../../スキル/#testing) | UK GDaD PCF | エキスパート | You can:<br>• manage testing activities within development or integration activities<br>• manage risks and take preventative action when risks become unacceptable<br>• manage customer relations |
| [Troubleshooting and problem resolution](../../スキル/#troubleshooting-and-problem-resolution) | UK GDaD PCF | エキスパート | You can:<br>• use lateral thinking to break a problem down into its component parts to identify and diagnose root causes<br>• troubleshoot and identify problems across different technology capabilities including computing, storage, networking, physical infrastructure, software, commercial-off-the-shelf software (COTS) and open source software |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実践者 | できること:<br>• サービスが組織間のケアパスにどう収まるかを分析する<br>• 臨床医、ケア職員、患者と協力して、デジタルサービスを形づくる<br>• デジタルに関する決定が、ケア、安全、職員の業務量に与える影響を説明する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実践者 | できること:<br>• データ保護影響評価と情報共有契約を主導する<br>• 適法な根拠、同意、秘密保持、保存について、チームに助言する<br>• インシデントを調査し、改善を勧告する |
| [セキュリティ運用](../../スキル/#セキュリティ運用) | このリファレンス | 実務 | できること:<br>• アラートを監視し、ランブックを使ってトリアージする<br>• 証拠を集め、イベントをエスカレーションする<br>• 指導を受けながら、簡単な検知ルールを調整する |
| [脆弱性管理](../../スキル/#脆弱性管理) | このリファレンス | エキスパート | できること:<br>• 脆弱性管理の方針とその目標を定める<br>• 技術的なセキュリティリスクを、シニアリーダーに報告する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実務 | できること:<br>• ハザードのワークショップに参加し、ハザードログに寄与する<br>• 自分の仕事のために、臨床リスク管理プロセスに従う<br>• テスト結果など、臨床安全ケースのための根拠を提供する |
| [組織のリスクマネジメント](../../スキル/#組織のリスクマネジメント) | このリファレンス | 実践者 | できること:<br>• ディレクトレートまたはプログラムのリスクプロセスを運営する<br>• リスクをリスク選好に照らして評価し、エスカレーションする<br>• リスクを委員会に報告する |
| [ピープルマネジメント](../../スキル/#ピープルマネジメント) | このリファレンス | 実践者 | できること:<br>• 目標を設定し、評価を行いながら、チームをライン管理する<br>• 心身の健康を支え、勤怠、実績、行為を管理する<br>• チームの育成と後継者計画を立てる |
| [予算管理](../../スキル/#予算管理) | このリファレンス | 実践者 | できること:<br>• 予算を保有して管理し、差異を予測して説明する<br>• コストと便益を示したビジネスケースを作成する |

### 一般的な資格と経験

- 複数のチームや組織にわたってインフラエンジニアリングを率いた豊富な経験。

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
| 2 | 知識、研修、経験 | 7 | 196 |
| 3 | 分析と判断のスキル | 5 | 60 |
| 4 | 計画と組織化のスキル | 5 | 60 |
| 5 | 身体的スキル | 2 | 15 |
| 6 | 患者・利用者のケアに対する責任 | 1 | 4 |
| 7 | 方針とサービス開発に対する責任 | 4 | 32 |
| 8 | 財務・物的資源に対する責任 | 4 | 32 |
| 9 | 人に対する責任 | 4 | 32 |
| 10 | 情報資源に対する責任 | 5 | 34 |
| 11 | 研究開発に対する責任 | 2 | 12 |
| 12 | 行動の自由度 | 5 | 45 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 4 | 18 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **600** (バンド 8b: 585–629) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
