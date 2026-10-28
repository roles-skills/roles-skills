# セキュリティオペレーションアナリスト

> これは、一般的なデジタルヘルスケア組織のための例示的な参照プロファイルです。特定の雇用主の公式な職務記述書ではなく、職務評価のスコアも正式な評価ではありません。

> このテキストは英語から AI アシスタントによって翻訳されたもので、日本語を母語とする方による確認はまだ行われていません。英国政府デジタル・データ専門職能力フレームワーク(UK GDaD PCF)と ESCO からの引用は英語のままです。

**職群:** [サイバーセキュリティ](../../#サイバーセキュリティ)  
**バンド:** 5, 6, 7  
**UK GDaD PCF のロール:** なし(このリファレンスがロールを定義しています)  
**ESCO の職業:** [cyber incident responder](http://data.europa.eu/esco/occupation/0ce5a9f4-e00a-4bbe-b255-3c63407167a4) (ISCO-08 2529); [ICT security technician](http://data.europa.eu/esco/occupation/a44a1dc5-be08-4840-8bd5-770c4ac1ca6d) (ISCO-08 3512)

## 概要

セキュリティ運用アナリストは、組織のシステムとデータに対するサイバーセキュリティの脅威を監視し、調査し、対応する。セキュリティ監視ツールからのアラートをトリアージし、不審な活動を調査し、インシデントを封じ込め、弱点の修正を支援する。医療では、迅速な検知と対応が、ランサムウェアなどの攻撃から、臨床サービスと機密性の高い患者情報を守る。

## デジタルヘルスケア組織において

- 医療はランサムウェアやデータ窃取の標的になりやすく、1 回の攻撃が組織全体の臨床システムを止めうる。
- サーバーやネットワークの一部を隔離するといった封じ込めの判断は、セキュリティリスクと患者のケアへの影響を比較衡量しなければならないため、アナリストは臨床・運用のリードと協力する。
- ネットワークには、セキュリティエージェントを動かせない、またはすぐにパッチを当てられない医療機器やレガシーシステムが含まれるため、アナリストはネットワーク監視と代替の管理策に頼る。
- 監視は患者記録へのアクセスも対象とするため、アナリストは情報ガバナンスと協力して、外部からの攻撃だけでなく、内部者による不適切なアクセスの検知を手助けする。
- セキュリティ監視は終日行われるため、アナリストはシフトや待機当番で働くことがある。

## ロールレベル

| バンド | 名称 | UK GDaD PCF のレベル | 英国公務員の等級 | 職務評価の点数 |
| --- | --- | --- | --- | --- |
| 5 | [ジュニア セキュリティ運用アナリスト](#バンド-5-ジュニア-セキュリティ運用アナリスト) | — | — | 348 |
| 6 | [セキュリティ運用アナリスト](#バンド-6-セキュリティ運用アナリスト) | — | — | 440 |
| 7 | [シニア セキュリティ運用アナリスト](#バンド-7-シニア-セキュリティ運用アナリスト) | — | — | 496 |

## バンド 5: ジュニア セキュリティ運用アナリスト

ジュニアセキュリティ運用アナリストは、経験のあるアナリストの指導を受けながら、セキュリティアラートを監視し、ランブックを使ってトリアージし、イベントをエスカレーションする。

### 責任

- セキュリティ監視ツールとエンドポイントツールからのアラートを監視し、ランブックを使ってトリアージする。
- フィッシングメールや異常なログインなど、不審な活動の証拠を集めてエスカレーションする。
- 職員から報告されたフィッシングメールを確認し、悪意のあるメールをメールボックスから削除するのを手伝う。
- イベントとアクションを、ケース管理ツールに正確に記録する。
- 脆弱性スキャンを実行し、期限の来た修正についてシステムオーナーに注意を促す。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [セキュリティ運用](../../スキル/#セキュリティ運用) | このリファレンス | 実務 | できること:<br>• アラートを監視し、ランブックを使ってトリアージする<br>• 証拠を集め、イベントをエスカレーションする<br>• 指導を受けながら、簡単な検知ルールを調整する |
| [脆弱性管理](../../スキル/#脆弱性管理) | このリファレンス | 実務 | できること:<br>• 脆弱性スキャンを実行し、結果を報告する<br>• システムのオーナーとともに修正を追跡する |
| [アイデンティティとアクセスの管理](../../スキル/#アイデンティティとアクセスの管理) | このリファレンス | 認知 | できること:<br>• アクセスの規則に従い、自分の認証情報を守る |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 認知 | できること:<br>• 保健・ケアのシステムの主な部分と、組織が支えるサービスを説明する<br>• 自分の仕事で、患者の安全と秘密保持が重要な理由を説明する |
| [Cyber incident management](../../スキル/#cyber-incident-management) | UK GDaD PCF | 認知 | *Senior leadership skill: the UK GDaD PCF defines it with one statement, not by level.* You can:<br>• implement cyber incident management processes that reflect the level of risk accepted by the organisation<br>• ensure the organisation is prepared for and can effectively respond to incidents<br>• determine the impact of critical incidents on the organisation’s technology<br>• lead the response to critical incidents that affect the whole organisation Examples of leadership using this skill:<br>• helping the incident management team build relationships with senior leaders<br>• leading simulation exercises with the board so they understand their role in incident response processes and the implications of potential incidents<br>• assessing what to communicate to the board, ministers or the whole organisation, and when to do it |
| [Information security](../../スキル/#information-security) | UK GDaD PCF | 認知 | You can:<br>• explain information security and the security controls available to protect solutions and services |
| [Security technology](../../スキル/#security-technology) | UK GDaD PCF | 認知 | You can:<br>• describe some security architectures<br>• explain why security technology is important |

### 一般的な資格と経験

- コンピューティングまたはサイバーセキュリティの資格、サイバーセキュリティのアプレンティスシップ、または同等の経験。

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
| 8 | 財務・物的資源に対する責任 | 2 | 12 |
| 9 | 人に対する責任 | 1 | 5 |
| 10 | 情報資源に対する責任 | 4 | 24 |
| 11 | 研究開発に対する責任 | 2 | 12 |
| 12 | 行動の自由度 | 3 | 21 |
| 13 | 身体的負荷 | 2 | 7 |
| 14 | 精神的負荷 | 4 | 18 |
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **348** (バンド 5: 326–395) |

精神的負荷は、予測できないアラートの監視とトリアージに長時間集中することが頻繁にあることを反映している。

## バンド 6: セキュリティ運用アナリスト

セキュリティ運用アナリストは、セキュリティインシデントを調査して封じ込め、検知ルールを書き、組織のセキュリティ監視を改善する。

### 責任

- システムオーナーや臨床サービスと協力して、セキュリティインシデントを調査し、その範囲を割り出し、封じ込める。
- 検知ルールを書いて調整し、医療に対する現在の脅威にもとづいて脅威ハンティングを行う。
- 患者記録への不適切なアクセスを監視し、ケースを情報ガバナンスに引き継ぐ。
- 臨床サービスや医療機器への影響を含め、脆弱性をリスクで評価する。
- インシデントの後に、ランブックとツールを改善する。
- 時間外のセキュリティインシデントに備えて、待機当番に加わる。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [セキュリティ運用](../../スキル/#セキュリティ運用) | このリファレンス | 実践者 | できること:<br>• セキュリティインシデントを調査し、封じ込める<br>• 検知ルールを書き、脅威ハンティングを行う<br>• インシデントの後に、ランブックとツールを改善する |
| [脆弱性管理](../../スキル/#脆弱性管理) | このリファレンス | 実務 | できること:<br>• 脆弱性スキャンを実行し、結果を報告する<br>• システムのオーナーとともに修正を追跡する |
| [アイデンティティとアクセスの管理](../../スキル/#アイデンティティとアクセスの管理) | このリファレンス | 実務 | できること:<br>• ユーザーアカウントとアクセス権を作成、変更、削除する<br>• アクセスをロールベースのアクセス規則に照らして確認する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実務 | できること:<br>• 自分の仕事が支える臨床・ケアのワークフローを説明する<br>• 臨床・ケアの同僚と、一般的な医療用語を正しく使う<br>• 変更が患者のケアにいつ影響しうるかを見分けて伝える |
| [組織のリスクマネジメント](../../スキル/#組織のリスクマネジメント) | このリファレンス | 認知 | できること:<br>• リスクとは何か、どう提起するかを説明する |
| [Cyber incident management](../../スキル/#cyber-incident-management) | UK GDaD PCF | 実務 | *Senior leadership skill: the UK GDaD PCF defines it with one statement, not by level.* You can:<br>• implement cyber incident management processes that reflect the level of risk accepted by the organisation<br>• ensure the organisation is prepared for and can effectively respond to incidents<br>• determine the impact of critical incidents on the organisation’s technology<br>• lead the response to critical incidents that affect the whole organisation Examples of leadership using this skill:<br>• helping the incident management team build relationships with senior leaders<br>• leading simulation exercises with the board so they understand their role in incident response processes and the implications of potential incidents<br>• assessing what to communicate to the board, ministers or the whole organisation, and when to do it |
| [Information security](../../スキル/#information-security) | UK GDaD PCF | 実務 | You can:<br>• use information security practices and available security controls to contribute to protecting solutions and services |
| [Security technology](../../スキル/#security-technology) | UK GDaD PCF | 実務 | You can:<br>• explain the effect of vulnerabilities on current and future designs<br>• share information on a range of systems, but may specialise in one |

### 一般的な資格と経験

- コンピューティングまたはサイバーセキュリティの学位、関連するセキュリティ認定、または同等の経験。
- セキュリティ監視またはインシデント対応の経験。

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
| 15 | 感情的負荷 | 2 | 11 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **440** (バンド 6: 396–465) |

精神的負荷は、待機当番を含め、調査の間に長時間集中することが頻繁にあることを反映している。感情的負荷は、患者記録のつらい内容や、稼働中のインシデントのプレッシャーに間接的に触れることが頻繁にあることを反映している。

## バンド 7: シニア セキュリティ運用アナリスト

シニアセキュリティ運用アナリストは、重大なセキュリティインシデントへの対応を主導し、脅威ハンティングを主導し、セキュリティ運用チームの仕事を導く。

### 責任

- ランサムウェアやデータ窃取を含む重大なセキュリティインシデントへの技術的な対応を主導し、インシデント管理と調整する。
- 患者のケアに影響する封じ込めの判断について、臨床・運用のリーダーに助言する。
- 脅威ハンティングと脅威インテリジェンスの作業を主導し、医療のセキュリティパートナーと情報を共有する。
- 医療機器のネットワークを含め、検知エンジニアリングと監視範囲の優先順位を定める。
- 技術チームと臨床チームでインシデント対応をテストする演習を主導する。
- セキュリティ運用アナリストをコーチし、導く。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [セキュリティ運用](../../スキル/#セキュリティ運用) | このリファレンス | 実践者 | できること:<br>• セキュリティインシデントを調査し、封じ込める<br>• 検知ルールを書き、脅威ハンティングを行う<br>• インシデントの後に、ランブックとツールを改善する |
| [脆弱性管理](../../スキル/#脆弱性管理) | このリファレンス | 実践者 | できること:<br>• 患者サービスへのリスクを含め、リスクで脆弱性に優先順位をつける<br>• ペネトレーションテストと是正の範囲を定め、管理する |
| [アイデンティティとアクセスの管理](../../スキル/#アイデンティティとアクセスの管理) | このリファレンス | 実務 | できること:<br>• ユーザーアカウントとアクセス権を作成、変更、削除する<br>• アクセスをロールベースのアクセス規則に照らして確認する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実務 | できること:<br>• 自分の仕事が支える臨床・ケアのワークフローを説明する<br>• 臨床・ケアの同僚と、一般的な医療用語を正しく使う<br>• 変更が患者のケアにいつ影響しうるかを見分けて伝える |
| [組織のリスクマネジメント](../../スキル/#組織のリスクマネジメント) | このリファレンス | 実務 | できること:<br>• 自分の領域のリスクを記録し、更新する<br>• 管理策を提案し、対応を追跡する |
| [Cyber incident management](../../スキル/#cyber-incident-management) | UK GDaD PCF | 実践者 | *Senior leadership skill: the UK GDaD PCF defines it with one statement, not by level.* You can:<br>• implement cyber incident management processes that reflect the level of risk accepted by the organisation<br>• ensure the organisation is prepared for and can effectively respond to incidents<br>• determine the impact of critical incidents on the organisation’s technology<br>• lead the response to critical incidents that affect the whole organisation Examples of leadership using this skill:<br>• helping the incident management team build relationships with senior leaders<br>• leading simulation exercises with the board so they understand their role in incident response processes and the implications of potential incidents<br>• assessing what to communicate to the board, ministers or the whole organisation, and when to do it |
| [Cyber risk management](../../スキル/#cyber-risk-management) | UK GDaD PCF | 実務 | *Senior leadership skill: the UK GDaD PCF defines it with one statement, not by level.* You can:<br>• maintain a clear understanding of the cyber and information security risks across the whole organisation<br>• develop and implement risk assessment processes<br>• oversee the assessment of the organisation's partners and supply chain for potential threats or vulnerabilities Examples of leadership using this skill:<br>• building a culture where teams have awareness of, and take responsibility for, risks and mitigating them<br>• advising programme owners and people running IT services about risks in a way that enables them to act on that advice<br>• communicating with senior leaders in a way that enables them to make decisions about accepting or mitigating risk |
| [Information security](../../スキル/#information-security) | UK GDaD PCF | 実践者 | You can:<br>• design solutions and services with security controls included, specifically engineered to mitigate security threats |
| [Security technology](../../スキル/#security-technology) | UK GDaD PCF | 実践者 | This skill level is currently not defined. |

### 一般的な資格と経験

- セキュリティ運用とインシデント対応の相当の経験(大学院ディプロマ相当のレベル)。
- 関連する上級のセキュリティ認定、または同等の経験。

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
| 15 | 感情的負荷 | 2 | 11 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **496** (バンド 7: 466–539) |

精神的負荷と感情的負荷は、多くは時間外に、臨床サービスが危険にさらされているときに、プレッシャーの下で重大なインシデントへの対応を主導することを反映している。


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
