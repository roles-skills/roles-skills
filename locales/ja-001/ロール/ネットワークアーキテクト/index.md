# ネットワークアーキテクト

> これは、一般的なデジタルヘルスケア組織のための例示的な参照プロファイルです。特定の雇用主の公式な職務記述書ではなく、職務評価のスコアも正式な評価ではありません。

> このテキストは英語から AI アシスタントによって翻訳されたもので、日本語を母語とする方による確認はまだ行われていません。英国政府デジタル・データ専門職能力フレームワーク(UK GDaD PCF)と ESCO からの引用は英語のままです。

**職群:** [アーキテクチャ](../../#アーキテクチャ)  
**バンド:** 6, 7, 8a  
**UK GDaD PCF のロール:** [Network architect](https://understand-digital-data-roles-skills.service.gov.uk/role/network-architect/)  
**ESCO の職業:** [ICT network architect](http://data.europa.eu/esco/occupation/e0b544dd-b621-4126-a55e-054af25c6ea0) (ISCO-08 2523)

## 概要

ネットワークアーキテクトは、組織の拠点、職員、臨床システム、医療機器をつなぐ、ローカル、広域、無線、クラウドのネットワークを設計する。ネットワークがケアを止めないだけの速度、レジリエンス、安全性を備えるようにし、サービスがクラウドに移行してパートナー組織と接続するのに合わせて、ネットワークがどう変わるかを計画する。

## デジタルヘルスケア組織において

- 臨床システム、電話、医療機器はネットワークに依存しているため、障害はケアを止めうる。設計にはレジリエンスとテスト済みのフェイルオーバーが必要である。
- ネットワークには、パッチを当てにくい接続された医療機器が載ることが多いため、アーキテクトはそれらを守るセグメンテーションと監視を設計する。
- 職員は病院、クリニック、地域、患者の自宅で働くため、設計は安全なモバイルおよびリモートアクセスを支えなければならない。
- ネットワークは、独自の接続・セキュリティ要件を持つ共有の保健・ケアネットワークやパートナー組織に接続される。
- 臨床エリアの変更には、混雑する時間帯を避けて作業を予定するなど、患者のケアを踏まえた慎重な計画が必要である。

## UK GDaD PCF のロール説明(原文は英語)

> A network architect is responsible for network designs and specifications, including cloud networks.

## ロールレベル

| バンド | 名称 | UK GDaD PCF のレベル | 英国公務員の等級 | 職務評価の点数 |
| --- | --- | --- | --- | --- |
| 6 | [アソシエイト ネットワークアーキテクト](#バンド-6-アソシエイト-ネットワークアーキテクト) | Associate network architect | EO/HEO | 412 |
| 7 | [ネットワークアーキテクト](#バンド-7-ネットワークアーキテクト) | Network architect | HEO/SEO | 496 |
| 8a | [リード ネットワークアーキテクト](#バンド-8a-リード-ネットワークアーキテクト) | Lead network architect | SEO/G7 | 572 |

## バンド 6: アソシエイト ネットワークアーキテクト

**UK GDaD PCF のレベル: Associate network architect**

> An associate network architect works with network architects on designs and specifications, with guidance.
> 
> At this role level, you will:
> - be aware and knowledgeable of new technology solutions and produce network design policy
> - draft recommendations for network support, creating and maintaining network plans and planning infrastructure runs
> - ensure designs meet SLAs (service level agreements) and develop an understanding of common tools
> - have an understanding of one or two of the following network technologies: LAN (local area network), WAN (wide area network), wifi, data centre LAN, SD (software-defined) networks, telephony, mobile solutions infrastructure, unified comms, network management solutions, network specific security and remote access technologies and approaches
> - collaborate with engineers to ensure systems are practically designed

### 責任

- ネットワークアーキテクトの指導のもとで、ネットワーク設計、図、仕様の案を作成する。
- 拠点を調査し、無線のカバレッジや機器の接続を含め、臨床エリアの要件を集める。
- ネットワークトポロジー、アドレス割り当て、接続機器の記録を最新に保つ。
- レビューの前に、設計がサービスレベルとセキュリティ基準を満たしているかを確認する。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Governance and assurance](../../スキル/#governance-and-assurance) | UK GDaD PCF | 認知 | You can:<br>• explain why governance and assurance is important<br>• follow governance and assurance processes, under supervision |
| [IT infrastructure](../../スキル/#it-infrastructure) | UK GDaD PCF | 実務 | You can:<br>• build, configure, administer and support infrastructure solutions and services, for example, networking and physical infrastructure, commercial-off-the-shelf (COTS) software, open source packages and solutions, or virtual and cloud computing |
| [Systems design](../../スキル/#systems-design) | UK GDaD PCF | 実務 | You can:<br>• translate logical designs into physical designs<br>• produce detailed designs<br>• effectively document all work using required standards, methods and tools, including prototyping tools where appropriate<br>• design systems characterised by managed levels of risk, manageable business and technical complexity, and meaningful impact<br>• work with well understood technology and identify appropriate patterns |
| [Systems integration](../../スキル/#systems-integration) | UK GDaD PCF | 認知 | You can:<br>• explain the process and principles of integrating systems.<br>• describe challenges of designing, building and testing interfaces between systems |
| [Technical understanding](../../スキル/#technical-understanding) | UK GDaD PCF | 認知 | You can:<br>• show an awareness of the relevant subject matter and a high level understanding of what it involves |
| [Troubleshooting and problem resolution](../../スキル/#troubleshooting-and-problem-resolution) | UK GDaD PCF | 実務 | You can:<br>• troubleshoot and identify problems across different technology capabilities |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実務 | できること:<br>• 自分の仕事が支える臨床・ケアのワークフローを説明する<br>• 臨床・ケアの同僚と、一般的な医療用語を正しく使う<br>• 変更が患者のケアにいつ影響しうるかを見分けて伝える |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 認知 | できること:<br>• 個人情報と健康情報の取り扱いに関する組織の規則に従う<br>• データ侵害やヒヤリハットを見分けて報告する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 認知 | できること:<br>• 誤った、欠けた、または遅れた情報などを通じて、医療 IT システムがどう患者に害を及ぼしうるかを説明する<br>• 臨床安全上の問題の可能性を、適切な経路で報告する |

### 一般的な資格と経験

- コンピューティングまたはネットワークの学位、認められたネットワーク資格、または同等の経験。
- ネットワーク設計の専門知識(大学院ディプロマレベルまたは同等の経験)。

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
| 5 | 身体的スキル | 2 | 15 |
| 6 | 患者・利用者のケアに対する責任 | 1 | 4 |
| 7 | 方針とサービス開発に対する責任 | 3 | 21 |
| 8 | 財務・物的資源に対する責任 | 1 | 5 |
| 9 | 人に対する責任 | 1 | 5 |
| 10 | 情報資源に対する責任 | 5 | 34 |
| 11 | 研究開発に対する責任 | 2 | 12 |
| 12 | 行動の自由度 | 4 | 32 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 3 | 12 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **412** (バンド 6: 396–465) |

UK GDaD PCF の等級の示唆(バンド 5)より高いバンドに置いている。保健分野の求人はこのロールをバンド 6 に置いている。この職務は主要な情報システムが依存するネットワークの一部を設計するため、知識は大学院ディプロマレベル、情報資源はレベル 5 で評価している。

## バンド 7: ネットワークアーキテクト

**UK GDaD PCF のレベル: Network architect**

> A network architect has responsibility for network designs and specifications to support business strategies using common tools.
> 
> At this role level, you will:
> - research new technologies and solutions, and ensure appropriate levels of assurance
> - plan, direct and co-ordinate activities, engaging with other stakeholders to manage and implement a programme
> - agree SLAs (service level agreements) and engage with third party vendors
> - have an understanding of most of the following network technologies: LAN (local area network), WAN (wide area network), wifi, data-centre LAN, SD (software-defined) networks, telephony, mobile solutions infrastructure, unified comms, network management solutions, network-specific security and remote access technologies and approaches
> - coach and mentor associate network architects where appropriate
> - collaborate with engineers to ensure systems are practically designed

### 責任

- 拠点とサービスのために、ローカル、広域、無線、クラウドのネットワークソリューションを設計する。
- 医療機器、臨床システム、ゲストアクセスのためのネットワークセグメンテーションを設計する。
- ケアが妨げられないよう、サービスリードとともに、臨床エリアでのネットワーク変更を計画する。
- 供給者とサービスレベルを、パートナーのネットワークと接続要件を合意する。
- 新しいネットワーク技術と、組織のセキュリティ基準への適合を評価する。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Governance and assurance](../../スキル/#governance-and-assurance) | UK GDaD PCF | 実践者 | You can:<br>• develop appropriate governance and assurance processes<br>• identify and recommend improvements to governance and assurance processes<br>• support others in following or applying governance and assurance processes |
| [IT infrastructure](../../スキル/#it-infrastructure) | UK GDaD PCF | 実践者 | You can:<br>• design and implement infrastructure solutions and services, for example, networking and physical infrastructure, commercial-off-the-shelf (COTS) software, open source packages and solutions, or virtual and cloud computing |
| [Systems design](../../スキル/#systems-design) | UK GDaD PCF | 実践者 | You can:<br>• design systems characterised by medium levels of risk, impact, and business or technical complexity<br>• select appropriate design standards, methods and tools, and ensure they are applied effectively<br>• review the systems designs of others to ensure the selection of appropriate technology, efficient use of resources and integration of multiple systems and technology |
| [Systems integration](../../スキル/#systems-integration) | UK GDaD PCF | 実践者 | You can:<br>• define the integration build<br>• co-ordinate build activities across systems<br>• understand how to undertake and support integration testing activities |
| [Technical understanding](../../スキル/#technical-understanding) | UK GDaD PCF | 実践者 | You can:<br>• show a thorough understanding of the technical concepts required for the role, and can explain how these fit into the wider technical landscape |
| [Troubleshooting and problem resolution](../../スキル/#troubleshooting-and-problem-resolution) | UK GDaD PCF | 実践者 | You can:<br>• break a problem down into its component parts to identify and diagnose root causes<br>• troubleshoot and identify problems across different technology capabilities |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実務 | できること:<br>• 自分の仕事が支える臨床・ケアのワークフローを説明する<br>• 臨床・ケアの同僚と、一般的な医療用語を正しく使う<br>• 変更が患者のケアにいつ影響しうるかを見分けて伝える |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実務 | できること:<br>• ハザードのワークショップに参加し、ハザードログに寄与する<br>• 自分の仕事のために、臨床リスク管理プロセスに従う<br>• テスト結果など、臨床安全ケースのための根拠を提供する |
| [アイデンティティとアクセスの管理](../../スキル/#アイデンティティとアクセスの管理) | このリファレンス | 実務 | できること:<br>• ユーザーアカウントとアクセス権を作成、変更、削除する<br>• アクセスをロールベースのアクセス規則に照らして確認する |
| [脆弱性管理](../../スキル/#脆弱性管理) | このリファレンス | 実務 | できること:<br>• 脆弱性スキャンを実行し、結果を報告する<br>• システムのオーナーとともに修正を追跡する |

### 一般的な資格と経験

- ネットワークアーキテクチャの専門知識(修士レベルまたは同等の経験)。
- 企業ネットワークの設計と支援の経験。

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
| | **合計** | | **496** (バンド 7: 466–539) |

UK GDaD PCF の等級の示唆(バンド 6)より高いバンドに置いている。保健分野の求人はこのロールをバンド 7 に置いている。この職務はローカル、広域、無線、クラウドのネットワークにわたる専門知識を要するため、知識は修士レベルまたは同等で評価している。

## バンド 8a: リード ネットワークアーキテクト

**UK GDaD PCF のレベル: Lead network architect**

> A lead network architect is accountable for designs and networks representing their business area.
> 
> At this role level, you will:
> - be a point of escalation
> - actively input into governance forums that determine IT strategy
> - cascade messages, standards and best practice from other architecture teams and design authorities to the network architecture team
> - act as a subject matter expert for network architects
> - represent network architects internally and externally
> - have an understanding of all network technology including LAN (local area network), WAN (wide area network), wifi, data centre LAN, SD (software-defined) networks, telephony, mobile solutions infrastructure, unified comms, network management solutions, and network specific security and remote access technologies and approaches
> - champion new technologies and solutions
> - coach and mentor network architects and associate network architects
> - be a strategic thinker who can communicate network concepts to technical and non-technical stakeholders

### 責任

- 拠点、データセンター、クラウド接続を含め、組織のネットワークアーキテクチャを担う。
- ネットワーク設計の基準を定め、設計機関で設計を保証する。
- 重要な臨床サービスのネットワークのレジリエンスと復旧を設計し、それがテストされているようにする。
- ネットワーク投資、供給者契約、新しいサービスのネットワークリスクについて助言する。
- 専門家としてのエスカレーション先となり、他のネットワークアーキテクトやエンジニアを導く。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Governance and assurance](../../スキル/#governance-and-assurance) | UK GDaD PCF | エキスパート | You can:<br>• ensure appropriate and proportionate governance and assurance is in place and is continuously improved, aligned to organisational and government needs<br>• guide teams through governance and assurance processes, such as service assessments, to ensure standards are met<br>• share the team's governance and assurance processes so stakeholders trust them to deliver value in a sustainable way |
| [IT infrastructure](../../スキル/#it-infrastructure) | UK GDaD PCF | エキスパート | You can:<br>• lead teams and departments in the design, implementation, administration and support of infrastructure solutions and services |
| [Systems design](../../スキル/#systems-design) | UK GDaD PCF | エキスパート | You can:<br>• design systems characterised by high levels of risk, impact, and business or technical complexity<br>• control system design practice within an enterprise or industry architecture<br>• influence industry-based models for the development of new technology applications<br>• develop effective implementation and procurement strategies, consistent with business needs<br>• ensure adherence to relevant technical strategies, policies, standards and practices |
| [Systems integration](../../スキル/#systems-integration) | UK GDaD PCF | 実践者 | You can:<br>• define the integration build<br>• co-ordinate build activities across systems<br>• understand how to undertake and support integration testing activities |
| [Technical understanding](../../スキル/#technical-understanding) | UK GDaD PCF | エキスパート | You can:<br>• anticipate and advise on future technology changes that present opportunities for the product or programme |
| [Troubleshooting and problem resolution](../../スキル/#troubleshooting-and-problem-resolution) | UK GDaD PCF | 実践者 | You can:<br>• break a problem down into its component parts to identify and diagnose root causes<br>• troubleshoot and identify problems across different technology capabilities |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実践者 | できること:<br>• サービスが組織間のケアパスにどう収まるかを分析する<br>• 臨床医、ケア職員、患者と協力して、デジタルサービスを形づくる<br>• デジタルに関する決定が、ケア、安全、職員の業務量に与える影響を説明する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実務 | できること:<br>• ハザードのワークショップに参加し、ハザードログに寄与する<br>• 自分の仕事のために、臨床リスク管理プロセスに従う<br>• テスト結果など、臨床安全ケースのための根拠を提供する |
| [アイデンティティとアクセスの管理](../../スキル/#アイデンティティとアクセスの管理) | このリファレンス | 実務 | できること:<br>• ユーザーアカウントとアクセス権を作成、変更、削除する<br>• アクセスをロールベースのアクセス規則に照らして確認する |
| [脆弱性管理](../../スキル/#脆弱性管理) | このリファレンス | 実践者 | できること:<br>• 患者サービスへのリスクを含め、リスクで脆弱性に優先順位をつける<br>• ペネトレーションテストと是正の範囲を定め、管理する |
| [医療機器ソフトウェアの規制](../../スキル/#医療機器ソフトウェアの規制) | このリファレンス | 認知 | できること:<br>• 一部の医療ソフトウェアが医療機器として規制されることを説明する<br>• 製品が医療機器にあたるかもしれないとき、誰に尋ねればよいかを知っている |
| [組織のリスクマネジメント](../../スキル/#組織のリスクマネジメント) | このリファレンス | 実務 | できること:<br>• 自分の領域のリスクを記録し、更新する<br>• 管理策を提案し、対応を追跡する |

### 一般的な資格と経験

- 複雑な組織のネットワークアーキテクチャの相当の経験(修士相当のレベル)。

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
| 10 | 情報資源に対する責任 | 6 | 46 |
| 11 | 研究開発に対する責任 | 3 | 21 |
| 12 | 行動の自由度 | 5 | 45 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 4 | 18 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **572** (バンド 8a: 540–584) |

UK GDaD PCF の等級の示唆(バンド 7)より高いバンドに置いている。保健分野の求人はこのロールをバンド 8a に置いている。この職務は組織のすべての情報システムが依存するネットワークアーキテクチャを担うため、情報資源はレベル 6 とする。


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
