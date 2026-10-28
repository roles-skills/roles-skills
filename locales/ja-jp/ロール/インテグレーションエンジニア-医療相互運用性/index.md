# インテグレーションエンジニア(医療相互運用性)

> これは、一般的なデジタルヘルスケア組織のための例示的な参照プロファイルです。特定の雇用主の公式な職務記述書ではなく、職務評価のスコアも正式な評価ではありません。

> このテキストは英語から AI アシスタントによって翻訳されたもので、日本語を母語とする方による確認はまだ行われていません。英国政府デジタル・データ専門職能力フレームワーク(UK GDaD PCF)と ESCO からの引用は英語のままです。

**職群:** [ソフトウェア開発](../../#ソフトウェア開発)  
**バンド:** 5, 6, 7, 8a  
**UK GDaD PCF のロール:** なし(このリファレンスがロールを定義しています)  
**ESCO の職業:** [integration engineer](http://data.europa.eu/esco/occupation/07e60525-1aad-4099-aaf3-2c7014c92212) (ISCO-08 2511); [database developer](http://data.europa.eu/esco/occupation/b11e1742-5e28-4270-b081-b0193d85ee7d) (ISCO-08 2521)

## 概要

インテグレーションエンジニアは、保健・ケアの情報が必要な場所へ安全に流れるよう、組織の臨床システムと業務システムをつなぐ。HL7 FHIR や HL7 バージョン 2 などの標準を使って、インターフェース、API、メッセージフローを設計、構築、テスト、サポートし、システム間でデータと臨床コードをマッピングし、本番稼働中の連携を動かし続ける。

## デジタルヘルスケア組織において

- 検査結果や紹介状などのメッセージが、失われる、遅れる、重複する、または誤って突合されることは、直接害につながりうるため、連携の作業は臨床リスク管理プロセスに従う。
- 連携は大量の機密性の高い健康情報を組織間で運ぶため、あらゆるフローには適法な根拠、安全な伝送、監査が必要である。
- 保健システムは、HL7 バージョン 2 のメッセージから HL7 FHIR の API、IHE プロファイルまで、多くの標準とバージョンを使い、しばしばローカルな差異がある。
- 臨床上の意味はやりとりの途中で失われてはならないため、エンジニアは SNOMED CT などの臨床用語集を正しくマッピングし、患者を確実に突合する。
- 多くの連携は昼夜を問わずケアを支えるため、監視、アラート、失敗したメッセージを解決する明確な経路が必要である。

## ロールレベル

| バンド | 名称 | UK GDaD PCF のレベル | 英国公務員の等級 | 職務評価の点数 |
| --- | --- | --- | --- | --- |
| 5 | [ジュニア インテグレーションエンジニア](#バンド-5-ジュニア-インテグレーションエンジニア) | — | — | 335 |
| 6 | [インテグレーションエンジニア](#バンド-6-インテグレーションエンジニア) | — | — | 418 |
| 7 | [シニア インテグレーションエンジニア](#バンド-7-シニア-インテグレーションエンジニア) | — | — | 477 |
| 8a | [リード インテグレーションエンジニア](#バンド-8a-リード-インテグレーションエンジニア) | — | — | 551 |

## バンド 5: ジュニア インテグレーションエンジニア

ジュニア インテグレーションエンジニアは、仕様に沿って、経験のあるエンジニアの指導のもと、保健・ケアのシステム間の連携を構築、テスト、サポートする。

### 責任

- 合意された仕様から、メッセージのマッピング、変換、API 呼び出しを構築し、変更する。
- エラーやエッジケースを含め、仕様とサンプルメッセージに照らして連携をテストする。
- メッセージフローを監視し、失敗または拒否されたメッセージを調査して、解決またはエスカレーションする。
- 本番データとテストデータの情報ガバナンスの規則に従って、健康データを安全に扱う。
- 臨床安全の根拠として使えるよう、変更とテスト結果を記録する。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Systems integration](../../スキル/#systems-integration) | UK GDaD PCF | 実務 | You can:<br>• build and test simple interfaces between systems<br>• work on more complex integration as part of a wider team |
| [Programming and build (software engineering)](../../スキル/#programming-and-build-software-engineering) | UK GDaD PCF | 実務 | You can:<br>• design, code, test, correct and document simple programs or scripts under the direction of others |
| [Testing](../../スキル/#testing) | UK GDaD PCF | 実務 | You can:<br>• review requirements and specifications, and define test conditions<br>• identify issues and risks associated with work<br>• analyse and report test activities and results |
| [Service support](../../スキル/#service-support) | UK GDaD PCF | 実務 | You can:<br>• help fix service faults following agreed procedures<br>• carry out maintenance tasks on service support infrastructure |
| [Information security](../../スキル/#information-security) | UK GDaD PCF | 認知 | You can:<br>• explain information security and the security controls available to protect solutions and services |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | 実務 | できること:<br>• FHIR のリソース、プロファイル、API を読み、使う<br>• 指導を受けながら、簡単な連携を構築またはテストする<br>• メッセージを仕様に照らして確認する |
| [臨床用語と分類](../../スキル/#臨床用語と分類) | このリファレンス | 認知 | できること:<br>• 臨床用語集と分類の違いを説明する<br>• SNOMED CT や ICD など、一般的な用語集を見分ける |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 認知 | できること:<br>• 誤った、欠けた、または遅れた情報などを通じて、医療 IT システムがどう患者に害を及ぼしうるかを説明する<br>• 臨床安全上の問題の可能性を、適切な経路で報告する |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 認知 | できること:<br>• 保健・ケアのシステムの主な部分と、組織が支えるサービスを説明する<br>• 自分の仕事で、患者の安全と秘密保持が重要な理由を説明する |

### 一般的な資格と経験

- コンピューティングまたは関連分野の学位、修了したアプレンティスシップ、または同等の経験。

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
| 10 | 情報資源に対する責任 | 4 | 24 |
| 11 | 研究開発に対する責任 | 2 | 12 |
| 12 | 行動の自由度 | 3 | 21 |
| 13 | 身体的負荷 | 2 | 7 |
| 14 | 精神的負荷 | 3 | 12 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **335** (バンド 5: 326–395) |

## バンド 6: インテグレーションエンジニア

インテグレーションエンジニアは、保健・ケアのシステム間の連携を自立して設計、構築、サポートし、システムがどのようにデータを交換すべきかの定義を手助けする。

### 責任

- HL7 FHIR、HL7 バージョン 2、メッセージングパターンを使って、連携、API、メッセージフローを設計し、構築する。
- 連携元と連携先のシステムを分析し、臨床コードを含むインターフェース仕様とデータマッピングを書く。
- 情報が正しい記録に届くよう、患者の突合、検証、エラー処理を構築する。
- ハザードのワークショップに参加し、失敗または遅れたメッセージのアラートなど、安全の管理策を連携に組み込む。
- 供給者やパートナー組織と協力して、新しい接続をテストし、稼働させる。
- 本番稼働中の連携の問題を調査して修正し、ジュニアのインテグレーションエンジニアをメンターする。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Systems integration](../../スキル/#systems-integration) | UK GDaD PCF | 実践者 | You can:<br>• define the integration build<br>• co-ordinate build activities across systems<br>• understand how to undertake and support integration testing activities |
| [Programming and build (software engineering)](../../スキル/#programming-and-build-software-engineering) | UK GDaD PCF | 実践者 | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../スキル/#systems-design) | UK GDaD PCF | 実務 | You can:<br>• translate logical designs into physical designs<br>• produce detailed designs<br>• effectively document all work using required standards, methods and tools, including prototyping tools where appropriate<br>• design systems characterised by managed levels of risk, manageable business and technical complexity, and meaningful impact<br>• work with well understood technology and identify appropriate patterns |
| [Service support](../../スキル/#service-support) | UK GDaD PCF | 実践者 | You can:<br>• identify, locate and fix service faults |
| [Information security](../../スキル/#information-security) | UK GDaD PCF | 実務 | You can:<br>• use information security practices and available security controls to contribute to protecting solutions and services |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | 実践者 | できること:<br>• FHIR、HL7 バージョン 2、メッセージングパターンを使って連携を設計し、構築する<br>• FHIR リソースと実装ガイドを書き、プロファイル化する<br>• システム間の複雑なマッピングやデータ品質の問題を解決する |
| [臨床用語と分類](../../スキル/#臨床用語と分類) | このリファレンス | 実務 | できること:<br>• データ項目やフォームに適切なコードを見つけて使う<br>• 用語ブラウザとリファレンスセットを使う |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実務 | できること:<br>• ハザードのワークショップに参加し、ハザードログに寄与する<br>• 自分の仕事のために、臨床リスク管理プロセスに従う<br>• テスト結果など、臨床安全ケースのための根拠を提供する |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実務 | できること:<br>• 自分の仕事が支える臨床・ケアのワークフローを説明する<br>• 臨床・ケアの同僚と、一般的な医療用語を正しく使う<br>• 変更が患者のケアにいつ影響しうるかを見分けて伝える |

### 一般的な資格と経験

- コンピューティングまたは関連分野の学位、または同等の経験。
- 本番システム間の連携の構築と支援の経験。

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

## バンド 7: シニア インテグレーションエンジニア

シニア インテグレーションエンジニアは、多数のシステムと組織にまたがる複雑な連携の設計と提供を主導し、担当領域の連携の基準を定める。

### 責任

- 組織間の共有ケア記録、検査結果、紹介状など、複雑な連携の技術設計を主導する。
- 組織のために、FHIR プロファイル、実装ガイド、インターフェース標準を書き、維持する。
- 連携が安全で、レジリエントで、観測可能になるよう設計し、障害の解決経路を明確にする。
- 臨床安全責任者と協力して、連携のハザードを特定し、管理策が設計に組み込まれてテストされるようにする。
- 情報ガバナンスの同僚と協力して、各データフローに合意された適法な根拠とデータ共有の取り決めがあるようにする。
- チームのインテグレーションエンジニアをコーチし、育成する。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Systems integration](../../スキル/#systems-integration) | UK GDaD PCF | エキスパート | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Programming and build (software engineering)](../../スキル/#programming-and-build-software-engineering) | UK GDaD PCF | 実践者 | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../スキル/#systems-design) | UK GDaD PCF | 実践者 | You can:<br>• design systems characterised by medium levels of risk, impact, and business or technical complexity<br>• select appropriate design standards, methods and tools, and ensure they are applied effectively<br>• review the systems designs of others to ensure the selection of appropriate technology, efficient use of resources and integration of multiple systems and technology |
| [Information security](../../スキル/#information-security) | UK GDaD PCF | 実践者 | You can:<br>• design solutions and services with security controls included, specifically engineered to mitigate security threats |
| [Stakeholder relationship management](../../スキル/#stakeholder-relationship-management) | UK GDaD PCF | 実務 | You can:<br>• identify important stakeholders and communicate with them clearly and regularly<br>• tailor communication to stakeholders' needs and work with them to build relationships while meeting user needs<br>• build and reach consensus with stakeholders<br>• work to improve stakeholder relationships using evidence to explain decisions |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | 実践者 | できること:<br>• FHIR、HL7 バージョン 2、メッセージングパターンを使って連携を設計し、構築する<br>• FHIR リソースと実装ガイドを書き、プロファイル化する<br>• システム間の複雑なマッピングやデータ品質の問題を解決する |
| [臨床用語と分類](../../スキル/#臨床用語と分類) | このリファレンス | 実践者 | できること:<br>• 臨床用語集を使って、データモデルとリファレンスセットを設計する<br>• 用語集や分類の間をマッピングし、マッピングの限界を説明する<br>• プロダクトや分析での用語集の使い方について、チームに助言する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実践者 | できること:<br>• データ保護影響評価と情報共有契約を主導する<br>• 適法な根拠、同意、秘密保持、保存について、チームに助言する<br>• インシデントを調査し、改善を勧告する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実務 | できること:<br>• ハザードのワークショップに参加し、ハザードログに寄与する<br>• 自分の仕事のために、臨床リスク管理プロセスに従う<br>• テスト結果など、臨床安全ケースのための根拠を提供する |
| [アイデンティティとアクセスの管理](../../スキル/#アイデンティティとアクセスの管理) | このリファレンス | 実務 | できること:<br>• ユーザーアカウントとアクセス権を作成、変更、削除する<br>• アクセスをロールベースのアクセス規則に照らして確認する |

### 一般的な資格と経験

- 保健分野またはその他の複雑な連携の設計と支援における相当の経験(修士相当のレベル)。

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

## バンド 8a: リード インテグレーションエンジニア

リード インテグレーションエンジニアは、組織のインテグレーションエンジニアリングを率い、技術的な方向性と基準を定め、多数のシステムにまたがる重要な連携を保証する。

### 責任

- 組織全体のインテグレーションエンジニアリングを率い、方向性、パターン、基準を定める。
- 検査結果、薬、アラートを運ぶものなど、重要な連携の設計を保証する。
- アーキテクト、プロダクトマネージャー、供給者とともに、連携プラットフォームのロードマップを形づくる。
- 組織を横断する相互運用性と標準化の取り組みで、組織を代表する。
- インテグレーションエンジニアをライン管理または率い、連携のコミュニティ・オブ・プラクティスを育てる。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Systems integration](../../スキル/#systems-integration) | UK GDaD PCF | エキスパート | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Systems design](../../スキル/#systems-design) | UK GDaD PCF | エキスパート | You can:<br>• design systems characterised by high levels of risk, impact, and business or technical complexity<br>• control system design practice within an enterprise or industry architecture<br>• influence industry-based models for the development of new technology applications<br>• develop effective implementation and procurement strategies, consistent with business needs<br>• ensure adherence to relevant technical strategies, policies, standards and practices |
| [Technical design throughout the life cycle](../../スキル/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | 実践者 | You can:<br>• create technical designs characterised by medium risk, impact, and complexity<br>• maintain appropriate quality and architectural coherence of a technical design in response to change<br>• use feedback to optimise and refine technical designs throughout the life cycle |
| [Stakeholder relationship management](../../スキル/#stakeholder-relationship-management) | UK GDaD PCF | 実践者 | You can:<br>• work with the team to develop and maintain an understanding of stakeholders<br>• work with the team to develop and implement stakeholder communications strategies<br>• identify and resolve issues, influence stakeholders and manage relationships effectively<br>• build long-term strategic relationships and communicate clearly and regularly with stakeholders |
| [Leadership and guidance](../../スキル/#leadership-and-guidance) | UK GDaD PCF | 実践者 | You can:<br>• make decisions characterised by medium levels of risk and complexity and recommend decisions as risk and complexity increase<br>• build consensus between services or independent stakeholders<br>• identify problems or issues in the team dynamic and rectify them<br>• engage in varying types of feedback, choosing the right type at the appropriate time and ensuring the discussion and decision stick<br>• bring people together to form a motivated team and help create the right environment for a team to work in<br>• facilitate the best team makeup depending on the situation |
| [医療データの相互運用性](../../スキル/#医療データの相互運用性) | このリファレンス | エキスパート | できること:<br>• 組織の相互運用性の標準と戦略を定める<br>• 国や組織を横断する標準化の取り組みを主導する<br>• 多数のシステムにまたがる重要な連携の設計を保証する |
| [臨床用語と分類](../../スキル/#臨床用語と分類) | このリファレンス | 実践者 | できること:<br>• 臨床用語集を使って、データモデルとリファレンスセットを設計する<br>• 用語集や分類の間をマッピングし、マッピングの限界を説明する<br>• プロダクトや分析での用語集の使い方について、チームに助言する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実践者 | できること:<br>• データ保護影響評価と情報共有契約を主導する<br>• 適法な根拠、同意、秘密保持、保存について、チームに助言する<br>• インシデントを調査し、改善を勧告する |
| [臨床リスク管理](../../スキル/#臨床リスク管理) | このリファレンス | 実践者 | できること:<br>• プロダクトや変更のハザード特定とリスク評価を主導する<br>• ハザードログと臨床安全ケース報告書を書き、維持する<br>• プロダクトチームとリスクの管理策に合意し、それが機能しているかを確認する<br>• 臨床リスク管理の基準の適用について、チームに助言する |
| [ピープルマネジメント](../../スキル/#ピープルマネジメント) | このリファレンス | 実践者 | できること:<br>• 目標を設定し、評価を行いながら、チームをライン管理する<br>• 心身の健康を支え、勤怠、実績、行為を管理する<br>• チームの育成と後継者計画を立てる |

### 一般的な資格と経験

- 複雑な保健またはケアのシステムの連携エンジニアリングを率いた豊富な経験。

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


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
