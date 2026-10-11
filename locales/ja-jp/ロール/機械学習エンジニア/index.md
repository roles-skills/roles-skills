# 機械学習エンジニア

> これは、一般的なデジタルヘルスケア組織のための例示的な参照プロファイルです。特定の雇用主の公式な職務記述書ではなく、職務評価のスコアも正式な評価ではありません。

> このテキストは英語から AI アシスタントによって翻訳されたもので、日本語を母語とする方による確認はまだ行われていません。英国政府デジタル・データ専門職能力フレームワーク(UK GDaD PCF)と ESCO からの引用は英語のままです。

**職群:** [データ](../../#データ)  
**バンド:** 7, 8b  
**UK GDaD PCF のロール:** [Machine learning engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/machine-learning-engineer/)  
**ESCO の職業:** [artificial intelligence engineer](http://data.europa.eu/esco/occupation/35553663-deab-4d9a-bf22-15c1625d28e8) (ISCO-08 2511)

## 概要

機械学習エンジニアは、データサイエンティストが構築した、または供給者から購入したモデルを、本番稼働中の保健・ケアのサービスで確実に機能させる。モデルを学習、テスト、デプロイ、監視するパイプラインを構築し、臨床・運用システムと統合する。実際の患者と職員が頼るようになった後も、モデルが安全で、堅牢で、公正で、有効であり続けるようにする。

## デジタルヘルスケア組織において

- 稼働中のモデルは、患者集団、臨床実践、記録の習慣が変わるにつれてドリフトしうるため、性能は患者集団ごとに監視され、必要に応じてモデルが再学習または撤回される。
- 診断、トリアージ、治療に情報を提供するモデルは医療機器として規制されうるため、そのソフトウェアライフサイクル、変更管理、市販後調査に正式な要件が生じる。
- 臨床安全ケースには、モデルがどのように失敗するか、出力が臨床医にどう表示されるか、モデルが利用できないときに何が起こるかについての根拠が必要である。
- 患者データで学習したモデルは個人に関する情報を漏らしうるため、学習データ、モデルの成果物、ログは、データそのものと同様に保護される。
- 生成 AI と大規模言語モデルには、臨床記録に作り話が入り込むなど、さらなるリスクがあり、特有のテストと人による監督が必要である。

## UK GDaD PCF のロール説明(原文は英語)

> A machine learning engineer develops, assures and maintains machine learning models so they can be used in products and services.
> 
> In this role, you will:
> - be responsible for the software development and technical infrastructure needed to design, train, deploy and scale machine learning models
> - provide and maintain effective, secure and sustainable machine learning models for use in products and services
> - support all stages of the machine learning life cycle
> - help product teams evaluate and choose appropriate machine learning solutions

## ロールレベル

| バンド | 名称 | UK GDaD PCF のレベル | 英国公務員の等級 | 職務評価の点数 |
| --- | --- | --- | --- | --- |
| 7 | [シニア 機械学習エンジニア](#バンド-7-シニア-機械学習エンジニア) | Senior machine learning engineer | SEO/G7/G6 | 495 |
| 8b | [リード 機械学習エンジニア](#バンド-8b-リード-機械学習エンジニア) | Lead machine learning engineer | G7/G6 | 595 |

## バンド 7: シニア 機械学習エンジニア

**UK GDaD PCF のレベル: Senior machine learning engineer**

> A senior machine learning engineer develops machine learning models so they can be used in products and services.
> 
> At this role level, you will:
> - decide what model is most suitable for use in products and services
> - customise, optimise, re-train and maintain existing models
> - deploy models into production, testing and assuring them to ensure they meet performance requirements
> - work with others to integrate models with existing systems
> - check that models used in live products and services stay safe, secure and continue to work effectively

### 責任

- 自動テスト、バージョン管理、ロールバックを備えて、本番の臨床・運用サービスにモデルをデプロイする。
- モデルの性能、ドリフト、患者集団間の公平性を監視する仕組みを、アラートと明確なオーナーとともに構築する。
- 可能な限り HL7 FHIR などのオープンな標準を使って、モデルを臨床システムと統合する。
- 臨床安全ケースと医療機器の技術文書に必要な、テスト、変更、監視の根拠を作成する。
- 生成 AI モデルを含め、供給者やオープンソースのモデルを、地域での使用に向けて評価し、調整する。
- 機械学習エンジニアリングの実践について、データサイエンティストやエンジニアをコーチする。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Applied maths, statistics and scientific practices](../../スキル/#applied-maths-statistics-and-scientific-practices) | UK GDaD PCF | 実践者 | You can:<br>• apply designated quantitative techniques such as time series analysis, optimisation and simulation to create and embed appropriate models for analysis and prediction<br>• provide guidance on matching data sources with relevant applied mathematics and statistical techniques to meet analysis goals<br>• apply appropriate statistical techniques to available data to discover new relations and offer insight into research problems, helping to improve organisational processes and support decision making<br>• access and use the statistical tools available within the organisation |
| [Communicating between the technical and non-technical](../../スキル/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | 実践者 | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Data ethics and privacy](../../スキル/#data-ethics-and-privacy) | UK GDaD PCF | 実践者 | You can:<br>• work with stakeholders to identify and address ethical and privacy concerns<br>• demonstrate and communicate how data ethical issues fit into the wider organisational context<br>• research developments in data ethics and privacy to improve compliance and processes<br>• assess and constructively challenge proposed data ethics policies |
| [Data science innovation](../../スキル/#data-science-innovation) | UK GDaD PCF | 実践者 | You can:<br>• demonstrate practical knowledge of data science tools and techniques<br>• develop data science solutions that maximise insight<br>• identify opportunities for how data science can improve data practices |
| [Programming and build (software engineering)](../../スキル/#programming-and-build-software-engineering) | UK GDaD PCF | 実践者 | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems integration](../../スキル/#systems-integration) | UK GDaD PCF | 実践者 | You can:<br>• define the integration build<br>• co-ordinate build activities across systems<br>• understand how to undertake and support integration testing activities |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実務 | できること:<br>• 自分の仕事が支える臨床・ケアのワークフローを説明する<br>• 臨床・ケアの同僚と、一般的な医療用語を正しく使う<br>• 変更が患者のケアにいつ影響しうるかを見分けて伝える |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実務 | できること:<br>• ハザードのワークショップに参加し、ハザードログに寄与する<br>• 自分の仕事のために、臨床リスク管理プロセスに従う<br>• テスト結果など、臨床安全ケースのための根拠を提供する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | 実務 | できること:<br>• FHIR のリソース、プロファイル、API を読み、使う<br>• 指導を受けながら、簡単な連携を構築またはテストする<br>• メッセージを仕様に照らして確認する |
| [医療機器ソフトウェアの規制](../../スキル/#医療機器ソフトウェアの規制) | このリファレンス | 実務 | できること:<br>• 医療機器の標準を満たすソフトウェアライフサイクルのプロセスに従う<br>• そのプロセスが必要とする記録を作成する |
| [医療における安全で公正な AI](../../スキル/#医療における安全で公正な-ai) | このリファレンス | 実践者 | できること:<br>• 臨床の同僚とともに、モデルの検証、バイアス評価、本番での監視を計画する<br>• モデルをいつ再学習、制限、撤回する必要があるかを判断する<br>• モデルがいつ医療機器として規制されうるか、どのような根拠が必要かをチームに助言する |

### 一般的な資格と経験

- 本番での機械学習システムの構築と運用の相当の経験(修士相当のレベル)。

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
| | **合計** | | **495** (バンド 7: 466–539) |

## バンド 8b: リード 機械学習エンジニア

**UK GDaD PCF のレベル: Lead machine learning engineer**

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

### 責任

- 研究から組織全体での安全な稼働利用へとモデルを移す、最も複雑な作業を主導する。
- 規制対象や安全上重要なモデルに必要な管理策を含め、機械学習のライフサイクルを定義する。
- モデルのテスト、監視、セキュリティ、倫理の基準を定め、稼働中のモデルを保証する。
- 臨床安全責任者、情報ガバナンス、規制の専門家と協力して、モデルをどう評価し承認するかに合意する。
- 研修ニーズを特定し、機械学習エンジニアと関連するロールを育成する。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Applied maths, statistics and scientific practices](../../スキル/#applied-maths-statistics-and-scientific-practices) | UK GDaD PCF | 実践者 | You can:<br>• apply designated quantitative techniques such as time series analysis, optimisation and simulation to create and embed appropriate models for analysis and prediction<br>• provide guidance on matching data sources with relevant applied mathematics and statistical techniques to meet analysis goals<br>• apply appropriate statistical techniques to available data to discover new relations and offer insight into research problems, helping to improve organisational processes and support decision making<br>• access and use the statistical tools available within the organisation |
| [Communicating between the technical and non-technical](../../スキル/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | エキスパート | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Data ethics and privacy](../../スキル/#data-ethics-and-privacy) | UK GDaD PCF | 実践者 | You can:<br>• work with stakeholders to identify and address ethical and privacy concerns<br>• demonstrate and communicate how data ethical issues fit into the wider organisational context<br>• research developments in data ethics and privacy to improve compliance and processes<br>• assess and constructively challenge proposed data ethics policies |
| [Data science innovation](../../スキル/#data-science-innovation) | UK GDaD PCF | エキスパート | You can:<br>• be a leader in the data science space<br>• demonstrate in-depth knowledge of data science tools and techniques, which you can use to solve problems creatively and to create opportunities for your team<br>• act as a coach, inspiring curiosity and creativity in others<br>• demonstrate in-depth knowledge of your chosen profession and keep up to date with changes in the industry<br>• challenge the status quo and always look for ways to improve data science |
| [Programming and build (software engineering)](../../スキル/#programming-and-build-software-engineering) | UK GDaD PCF | エキスパート | You can:<br>• advise on the right way to apply standards and methods to ensure compliance<br>• maintain technical responsibility for all the stages and iterations of a software development project<br>• provide technical advice to stakeholders and set the team-based standards for programming tools and techniques |
| [Systems integration](../../スキル/#systems-integration) | UK GDaD PCF | エキスパート | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実践者 | できること:<br>• サービスが組織間のケアパスにどう収まるかを分析する<br>• 臨床医、ケア職員、患者と協力して、デジタルサービスを形づくる<br>• デジタルに関する決定が、ケア、安全、職員の業務量に与える影響を説明する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実践者 | できること:<br>• プロダクトや変更のハザード特定とリスク評価を主導する<br>• ハザードログと臨床安全ケース報告書を書き、維持する<br>• プロダクトチームとリスクの管理策に合意し、それが機能しているかを確認する<br>• 臨床リスク管理の基準の適用について、チームに助言する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実践者 | できること:<br>• データ保護影響評価と情報共有契約を主導する<br>• 適法な根拠、同意、秘密保持、保存について、チームに助言する<br>• インシデントを調査し、改善を勧告する |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | 実践者 | できること:<br>• FHIR、HL7 バージョン 2、メッセージングパターンを使って連携を設計し、構築する<br>• FHIR リソースと実装ガイドを書き、プロファイル化する<br>• システム間の複雑なマッピングやデータ品質の問題を解決する |
| [医療機器ソフトウェアの規制](../../スキル/#医療機器ソフトウェアの規制) | このリファレンス | 実践者 | できること:<br>• 製品が医療機器かどうか、またその可能性の高いクラスを評価する<br>• 品質および臨床の同僚とともに、製品の規制対応の作業を計画する |
| [医療における安全で公正な AI](../../スキル/#医療における安全で公正な-ai) | このリファレンス | エキスパート | できること:<br>• ケアにおける AI を保証し、監視するための組織の基準を定める<br>• 導入の前後に、高リスクのモデルの保証を主導する<br>• 安全で公正な AI について、規制当局やパートナーに対して組織を代表する |
| [ピープルマネジメント](../../スキル/#ピープルマネジメント) | このリファレンス | 実務 | できること:<br>• 日々の業務を監督し、フィードバックを与える<br>• 採用と導入研修に参加する<br>• 定期的に 1 対 1 の対話を行う |

### 一般的な資格と経験

- 複雑または規制対象のサービスの機械学習エンジニアリングを率いた豊富な経験。

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
| 11 | 研究開発に対する責任 | 2 | 12 |
| 12 | 行動の自由度 | 5 | 45 |
| 13 | 身体的負荷 | 1 | 3 |
| 14 | 精神的負荷 | 4 | 18 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **595** (バンド 8b: 585–629) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
