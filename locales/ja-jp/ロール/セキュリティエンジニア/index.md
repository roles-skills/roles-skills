# セキュリティエンジニア

> これは、一般的なデジタルヘルスケア組織のための例示的な参照プロファイルです。特定の雇用主の公式な職務記述書ではなく、職務評価のスコアも正式な評価ではありません。

> このテキストは英語から AI アシスタントによって翻訳されたもので、日本語を母語とする方による確認はまだ行われていません。英国政府デジタル・データ専門職能力フレームワーク(UK GDaD PCF)と ESCO からの引用は英語のままです。

**職群:** [サイバーセキュリティ](../../#サイバーセキュリティ)  
**バンド:** 6, 7, 8a  
**UK GDaD PCF のロール:** なし(このリファレンスがロールを定義しています)  
**ESCO の職業:** [ICT security administrator](http://data.europa.eu/esco/occupation/0464b062-cea6-4164-b10d-956c61956ae7) (ISCO-08 2529)

## 概要

セキュリティエンジニアは、組織のシステム、データ、利用者を守る技術的なセキュリティ管理策を設計、構築、運用する。アイデンティティとアクセス、エンドポイントとネットワークの保護、暗号化、ロギング、クラウドセキュリティに取り組み、プロダクトチームやインフラチームがセキュリティを組み込むのを支援する。医療では、ケアの現場の臨床医のアクセスを速く保ちながら、臨床システムと患者データを守る。

## デジタルヘルスケア組織において

- セキュリティ管理策は緊急のケアの妨げになってはならないため、エンジニアは、共有の臨床ワークステーションでも素早く機能する強力な認証を設計する。
- 医療機器やレガシーな臨床システムは、パッチを当てられない、またはセキュリティソフトウェアを動かせないことが多いため、エンジニアはネットワークのセグメンテーションと代替の管理策を設計する。
- ランサムウェアは医療にとって大きな脅威であるため、エンジニアはシステムを堅牢化し、バックアップを守り、攻撃が広がる範囲を限定する。
- 臨床システムは第三者が提供しサポートすることが多いため、エンジニアは供給者のセキュリティを評価し、そのリモートアクセスを管理する。
- 臨床システムのセキュリティ管理策の変更は、変更管理を通り、必要に応じて臨床安全レビューを受ける。

## ロールレベル

| バンド | 名称 | UK GDaD PCF のレベル | 英国公務員の等級 | 職務評価の点数 |
| --- | --- | --- | --- | --- |
| 6 | [セキュリティエンジニア](#バンド-6-セキュリティエンジニア) | — | — | 434 |
| 7 | [シニア セキュリティエンジニア](#バンド-7-シニア-セキュリティエンジニア) | — | — | 490 |
| 8a | [リード セキュリティエンジニア](#バンド-8a-リード-セキュリティエンジニア) | — | — | 560 |

## バンド 6: セキュリティエンジニア

セキュリティエンジニアは、セキュリティの管理策とツールを構築、設定、保守し、チームがセキュリティ上の弱点を修正するのを支援する。

### 責任

- エンドポイント保護、ファイアウォール、メールセキュリティ、セキュリティログなど、セキュリティ管理策を構築し、保守する。
- 多要素認証や特権アクセスを含め、アイデンティティとアクセスの管理策を設定する。
- インフラチームとプロダクトチームが脆弱性を修正し、合意された標準に従ってシステムを堅牢化するのを支援する。
- インフラチームと臨床工学チームと協力して、医療機器とレガシーシステムを守るためにネットワークをセグメント化する。
- 新しいシステムと供給者のリモートアクセスのセキュリティを、稼働前にレビューする。
- セキュリティインシデント対応を支えるため、待機当番に加わる。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Security technology](../../スキル/#security-technology) | UK GDaD PCF | 実務 | You can:<br>• explain the effect of vulnerabilities on current and future designs<br>• share information on a range of systems, but may specialise in one |
| [Information security](../../スキル/#information-security) | UK GDaD PCF | 実務 | You can:<br>• use information security practices and available security controls to contribute to protecting solutions and services |
| [Cyber incident management](../../スキル/#cyber-incident-management) | UK GDaD PCF | 認知 | *Senior leadership skill: the UK GDaD PCF defines it with one statement, not by level.* You can:<br>• implement cyber incident management processes that reflect the level of risk accepted by the organisation<br>• ensure the organisation is prepared for and can effectively respond to incidents<br>• determine the impact of critical incidents on the organisation’s technology<br>• lead the response to critical incidents that affect the whole organisation Examples of leadership using this skill:<br>• helping the incident management team build relationships with senior leaders<br>• leading simulation exercises with the board so they understand their role in incident response processes and the implications of potential incidents<br>• assessing what to communicate to the board, ministers or the whole organisation, and when to do it |
| [アイデンティティとアクセスの管理](../../スキル/#アイデンティティとアクセスの管理) | このリファレンス | 実務 | できること:<br>• ユーザーアカウントとアクセス権を作成、変更、削除する<br>• アクセスをロールベースのアクセス規則に照らして確認する |
| [脆弱性管理](../../スキル/#脆弱性管理) | このリファレンス | 実務 | できること:<br>• 脆弱性スキャンを実行し、結果を報告する<br>• システムのオーナーとともに修正を追跡する |
| [セキュリティ運用](../../スキル/#セキュリティ運用) | このリファレンス | 実務 | できること:<br>• アラートを監視し、ランブックを使ってトリアージする<br>• 証拠を集め、イベントをエスカレーションする<br>• 指導を受けながら、簡単な検知ルールを調整する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実務 | できること:<br>• 自分の仕事が支える臨床・ケアのワークフローを説明する<br>• 臨床・ケアの同僚と、一般的な医療用語を正しく使う<br>• 変更が患者のケアにいつ影響しうるかを見分けて伝える |

### 一般的な資格と経験

- コンピューティングまたはサイバーセキュリティの学位、関連するセキュリティ認定、または同等の経験。
- インフラまたはセキュリティツールの構築や運用の経験。

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

精神的負荷は、待機当番を含め、複雑な技術作業とインシデント支援に長時間集中することが頻繁にあることを反映している。

## バンド 7: シニア セキュリティエンジニア

シニアセキュリティエンジニアは、重要なセキュリティ管理策のデリバリーを設計して主導し、安全な設計についてチームに助言する。

### 責任

- 特権アクセス管理、セキュリティ監視、バックアップの保護など、セキュリティ管理策を設計し、デリバリーを主導する。
- 臨床向けおよび患者向けのサービスの安全な設計について、プロダクトチームとインフラチームに助言する。
- 医療機器やパッチを当てられないその他のシステムのための代替の管理策を設計する。
- クラウドサービスを含め、供給者とその製品のセキュリティを評価する。
- 技術的な専門知識と復旧計画で、重大なセキュリティインシデントへの対応を支える。
- セキュリティエンジニアをコーチし、チームを横断してグッドプラクティスを共有する。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Security technology](../../スキル/#security-technology) | UK GDaD PCF | 実践者 | This skill level is currently not defined. |
| [Information security](../../スキル/#information-security) | UK GDaD PCF | 実践者 | You can:<br>• design solutions and services with security controls included, specifically engineered to mitigate security threats |
| [Designing secure systems](../../スキル/#designing-secure-systems) | UK GDaD PCF | 実務 | You can:<br>• design and review system architectures through the application of patterns and principles |
| [Cyber risk management](../../スキル/#cyber-risk-management) | UK GDaD PCF | 実務 | *Senior leadership skill: the UK GDaD PCF defines it with one statement, not by level.* You can:<br>• maintain a clear understanding of the cyber and information security risks across the whole organisation<br>• develop and implement risk assessment processes<br>• oversee the assessment of the organisation's partners and supply chain for potential threats or vulnerabilities Examples of leadership using this skill:<br>• building a culture where teams have awareness of, and take responsibility for, risks and mitigating them<br>• advising programme owners and people running IT services about risks in a way that enables them to act on that advice<br>• communicating with senior leaders in a way that enables them to make decisions about accepting or mitigating risk |
| [アイデンティティとアクセスの管理](../../スキル/#アイデンティティとアクセスの管理) | このリファレンス | 実践者 | できること:<br>• アイデンティティとアクセスのサービスを設計し、運営する<br>• アクセスを定期的にレビューし、問題を修正する |
| [脆弱性管理](../../スキル/#脆弱性管理) | このリファレンス | 実践者 | できること:<br>• 患者サービスへのリスクを含め、リスクで脆弱性に優先順位をつける<br>• ペネトレーションテストと是正の範囲を定め、管理する |
| [セキュリティ運用](../../スキル/#セキュリティ運用) | このリファレンス | 実務 | できること:<br>• アラートを監視し、ランブックを使ってトリアージする<br>• 証拠を集め、イベントをエスカレーションする<br>• 指導を受けながら、簡単な検知ルールを調整する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実務 | できること:<br>• データ保護の原則を自分の仕事に適用する<br>• データ保護影響評価に寄与する<br>• 情報の請求と記録を正しく扱う |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実務 | できること:<br>• 自分の仕事が支える臨床・ケアのワークフローを説明する<br>• 臨床・ケアの同僚と、一般的な医療用語を正しく使う<br>• 変更が患者のケアにいつ影響しうるかを見分けて伝える |

### 一般的な資格と経験

- セキュリティエンジニアリングの相当の経験(大学院ディプロマ相当のレベル)。
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
| 15 | 感情的負荷 | 1 | 5 |
| 16 | 労働条件 | 2 | 7 |
| | **合計** | | **490** (バンド 7: 466–539) |

## バンド 8a: リード セキュリティエンジニア

リードセキュリティエンジニアは、セキュリティエンジニアリングの技術的な方向性を定め、組織全体で管理策が連携して機能するようにする。

### 責任

- 組織全体のセキュリティ管理策の技術的な方向性と標準を定める。
- クラウドホスティングへの移行や新しい電子患者記録など、主要なプログラムのセキュリティ設計を主導する。
- 管理策がランサムウェアから守り、臨床システムの迅速で安全な復旧を支えるようにする。
- アクセスと認証について臨床リードと協力し、セキュリティと臨床での使いやすさのバランスをとる。
- 技術的なリスクと投資について、サイバーセキュリティマネージャーに助言する。
- セキュリティエンジニアを率い、育成する。

### スキル

| スキル | 出典 | 期待されるレベル | このレベルの意味 |
| --- | --- | --- | --- |
| [Security technology](../../スキル/#security-technology) | UK GDaD PCF | エキスパート | You can:<br>• explain complex system architectures<br>• identify and explain how easy or difficult it will be to exploit vulnerabilities<br>• lead and influence security technology in the security industry |
| [Information security](../../スキル/#information-security) | UK GDaD PCF | 実践者 | You can:<br>• design solutions and services with security controls included, specifically engineered to mitigate security threats |
| [Designing secure systems](../../スキル/#designing-secure-systems) | UK GDaD PCF | 実践者 | You can:<br>• design and review system architectures through the development of patterns and principles |
| [Cyber risk management](../../スキル/#cyber-risk-management) | UK GDaD PCF | 実践者 | *Senior leadership skill: the UK GDaD PCF defines it with one statement, not by level.* You can:<br>• maintain a clear understanding of the cyber and information security risks across the whole organisation<br>• develop and implement risk assessment processes<br>• oversee the assessment of the organisation's partners and supply chain for potential threats or vulnerabilities Examples of leadership using this skill:<br>• building a culture where teams have awareness of, and take responsibility for, risks and mitigating them<br>• advising programme owners and people running IT services about risks in a way that enables them to act on that advice<br>• communicating with senior leaders in a way that enables them to make decisions about accepting or mitigating risk |
| [アイデンティティとアクセスの管理](../../スキル/#アイデンティティとアクセスの管理) | このリファレンス | 実践者 | できること:<br>• アイデンティティとアクセスのサービスを設計し、運営する<br>• アクセスを定期的にレビューし、問題を修正する |
| [脆弱性管理](../../スキル/#脆弱性管理) | このリファレンス | 実践者 | できること:<br>• 患者サービスへのリスクを含め、リスクで脆弱性に優先順位をつける<br>• ペネトレーションテストと是正の範囲を定め、管理する |
| [セキュリティ運用](../../スキル/#セキュリティ運用) | このリファレンス | 実践者 | できること:<br>• セキュリティインシデントを調査し、封じ込める<br>• 検知ルールを書き、脅威ハンティングを行う<br>• インシデントの後に、ランブックとツールを改善する |
| [情報ガバナンスとデータ保護](../../スキル/#情報ガバナンスとデータ保護) | このリファレンス | 実践者 | できること:<br>• データ保護影響評価と情報共有契約を主導する<br>• 適法な根拠、同意、秘密保持、保存について、チームに助言する<br>• インシデントを調査し、改善を勧告する |
| [保健・ケアサービスの理解](../../スキル/#保健ケアサービスの理解) | このリファレンス | 実務 | できること:<br>• 自分の仕事が支える臨床・ケアのワークフローを説明する<br>• 臨床・ケアの同僚と、一般的な医療用語を正しく使う<br>• 変更が患者のケアにいつ影響しうるかを見分けて伝える |
| [ピープルマネジメント](../../スキル/#ピープルマネジメント) | このリファレンス | 実務 | できること:<br>• 日々の業務を監督し、フィードバックを与える<br>• 採用と導入研修に参加する<br>• 定期的に 1 対 1 の対話を行う |

### 一般的な資格と経験

- 複雑なサービスのセキュリティエンジニアリングを率いた豊富な経験。

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


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
