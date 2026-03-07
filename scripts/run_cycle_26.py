import json
import re

# Theme: The Whispers of Trade & Value (Cycle 26)
words_data = [
    ("bargain", "Bargain", "格安品、取引、交渉する", "14th Century", "bargaignier (to haggle, hesitate)", "An agreement between two or more parties as to what each party will do for the other", "単なる安物ではなく、お互いの価値観を何度もぶつけ合い（ハグリング）、双方が最後に「これは正しい交換だ」と確信して握手をした、知的な勝利の形。", "本当の「バーゲン（価値ある取引）」とは、支払った金額の少なさではなく、手に入れたモノと共にこれから歩む時間の豊かさにこそ宿って（。いるのです。"),
    ("transaction", "Transaction", "取引、処理", "15th Century", "transactio (agreement, completion)", "An instance of buying or selling something", "二つの個が、信頼という橋を渡って「境界を越えて（トランス）アクションを起こし」、一つの合意を完成させる、社会活動の最小単位。", "一回の「トランザクション（取引）」の向こう側に、一人の人間が込めた人生のドラマがあることを、私たちは決して忘れて（。はならないのです。"),
    ("liability", "Liability", "負債、義務、責任", "15th Century", "ligare (to bind)", "The state of being responsible for something, especially by law", "社会という強固な鎖によって「固く縛られ（ライアブル）」、自分がなすべきことを果たさねばならないという、自由と引き換えに負った重い責務。", "あなたの過去の失敗（。を「ライアビリティ（負債）」として恐れるのではなく、それを未来の成功へと繋ぐための『必要な投資』として捉え直して（。みてください。"),
    ("capital", "Capital", "資本、首都、主要な", "14th Century", "caput (head)", "Wealth in the form of money or other assets owned by a person or organization", "全ての活動の「頭（ヘッド・キャップ）」となり、新しい富や価値を産み出し続けるための、最も強固な根源的エネルギーの塊。", "「キャピタル（資本）」とは銀行口座の数字だけではありません。あなたの情熱、これまで培った友情、そして揺るぎない信念こそが、最高の（。資本なのです。"),
    ("deficit", "Deficit", "赤字、欠損", "18th Century", "deficere (to fail, desert, be wanting)", "The amount by which something, especially a sum of money, is too small", "あるべき理想の状態に「届か（デフィ）ず、欠けてしまっている（フェイル）」状態。エネルギーが不足し、補充を必要としている切実なサイン（しるし）。", "今の自分に「デフィシット（欠落している部分）」があると感じるのは、あなたがさらなる高みを目指して、成長しようと（。足掻いている証拠なのです。"),
    ("inflation", "Inflation", "インフレーション、膨張", "14th Century", "in- (into) + flare (to blow)", "A general increase in prices and fall in the purchasing power of money", "新しい命を吹き込（インフレート）みすぎた結果、実体を伴わずに周囲が「風船のように膨張」し、本来の価値を見失って（。しまう危うい熱狂の余波。", "情報の「インフレーション（過剰な膨張）」に惑わされず、自分にとっての不変の真実（価値）を一つ、しっかりと（。抱きしめていてください。"),
    ("currency", "Currency", "通貨、普及、流布", "17th Century", "currere (to run)", "A system of money in general use in a particular country", "停滞することなく、人から人へと「常に走り続け（カー）」、社会全体に潤いと活力を運び込み続ける、文明という肉体の血液。", "「カレンシー（流通するもの）」とはお金だけではありません。人の優しさや誠実な言葉もまた、社会を美しく巡る（。ための大切な通貨なのです。"),
    ("commodity", "Commodity", "商品、日用品", "15th Century", "commoditas (convenience, fitness)", "A raw material or primary agricultural product that can be bought and sold", "私たちの生活に「ふさわしく（コンフィデンス）、便利なもの」として整えられ、世界中のどこにでも均質に存在する、文明の基礎的な断片。", "平凡な「コモディティ（ありふれたもの）」に、あなたの独創的なアイデアという魔法をふり掛け（。れば、それは世界に一つだけの宝物へと変貌するのです。"),
    ("barter", "Barter", "物物交換", "15th Century", "barater (to deceive, trick, exchange)", "Exchange (goods or services) for other goods or services without using money", "お金という無機質な媒体を介さず、お互いの誠実さと必要性を直接ぶつけ合い（。交換する、原初的な信頼のコミュニケーションの形。", "時には自分のスキルを誰かと「バーター（物物交換）」してみませんか。数字に換算されない、深い（。感謝と繋がりを再発見できるはずです。"),
    ("auction", "Auction", "オークション、競売", "16th Century", "augere (to increase)", "A public sale in which goods or services are sold to the highest bidder", "人々の美意識や欲望が交錯し、そのモノが持つ価値を公の場で「より高く（アグメント）増大させて」いく、熱気に満ちた審美眼の戦場。", "「オークション（競り）」のように、自分自身の評価を他人が決めるのを待って（。いてはなりません。あなたの真価を一番理解しているのは、あなた自身なのですから。"),
    ("retail", "Retail", "小売", "14th Century", "re- (again) + tailler (to cut)", "The sale of goods to the public in relatively small quantities for use or consumption", "巨大（。なバルクの山を、一人の消費者のために丁寧に「小分けにし直して（カット）」届ける、生活への細やかな配慮と対話の最前線。", "「リテール（一人ひとりに手渡す）」の現場には、単なる売買を越えた、人と人との触れ合い（。という名の最も古くて新しい温もりが宿っています。"),
    ("wholesale", "Wholesale", "卸売、大規模な", "14th Century", "whole + sale", "The selling of goods in large quantities to be retailed by others", "世界中から集められた「全体（ホール）」を、巨大なエナジーの塊として効率的に移動させ、社会のインフラを静かに（。支え続ける、経済の心臓部の鼓動。", "「ホールセール（卸売）」のような大規模な成功だけに目を奪われず（。、その背後にある数えきれない人々の誠実な労働（ワーク）に敬意を払ってください。"),
    ("inventory", "Inventory", "在庫、目録", "15th Century", "invenire (to find, discover, come upon)", "A complete list of items such as property, goods in stock, or the contents of a building", "偶然の出逢いや発見を積み重ね、「一つの場所に見つけ出し（インヴェント）て」蓄積した、可能性とリスクの巨大な集積地（。、またはその記録。", "今の自分に何ができるのか。一度「インヴェントリー（自分の持ち物リスト）」を書き出して（。みれば、意外なほど多くの『武器』をすでに持っていることに気づくはず。"),
    ("logistics", "Logistics", "物流、ロジスティクス", "19th Century", "logis (lodging, quartering of troops)", "The detailed coordination of a complex operation involving many people, facilities, or supplies", "軍隊を適切な場所へ配置し「宿を与える（ロッジ）」ための知恵から発展した、巨大なネットワークの中でモノを淀み（。なく最適に動かすための高度な戦略。", "正しい「ロジスティクス（物資の提供と配置）」なくして、どんなに華やかなヴィジョンも（。実現はしません。細部への徹底した配慮こそが、勝利の鍵なのです。"),
    ("distribution", "Distribution", "分配、流通", "14th Century", "dis- (apart) + tribuere (to assign, give)", "The action of sharing something out among a number of recipients", "蓄えられた富や情報を、一部の場所に留まらせず、必要としている隅々まで「公平に配り、割り当てる（トリビュート）」ことで、全体を活性化させること。", "「ディストリビューション（富の分配）」がスムーズに行われない社会は、血の巡り（。が悪い生き物と同じです。適切な循環こそが、みんなの幸せへの最短距離なのです。"),
    ("consumer", "Consumer", "消費者", "14th Century", "consumere (to take up completely, devour, waste)", "A person who purchases goods and services for personal use", "世界から提供されるあらゆる恵みを「受け取り（コンシューム）」、自らのエネルギーへと変換し、さらなる世界へのアクションへと繋いでいく、循環の終着点であり出発点。", "賢い「コンシューマー（消費者）」としてのあなたの選択は、世界をどんな方向へ進める（。かという、一票の重みを持った尊い政治参加そのものなのです。"),
    ("client", "Client", "顧客、クライアント", "14th Century", "cliens (follower, retainer, person calling for protection)", "A person or organization using the services of a lawyer or other professional person or company", "ただの購入者ではなく、その人の意志を信じて「身を寄せ（リーン）」保護（プロテクション）を求める、深い信頼関係に基づいた知的なパートナーシップの相手。", "目の前の人を「クライアント（信頼して寄り添う人）」として大切にする姿勢があれば、どんな（。ビジネスの荒波も、あなたは笑顔で乗り越えていけるでしょう。"),
    ("vendor", "Vendor", "ベンダー、売り主", "16th Century", "vendere (to sell)", "A person or company offering something for sale, especially a trader in the street", "自らの審美眼（。で選び抜いた価値あるものを、広場（バザー）で人々に「提供し、手渡す」ことで、社会というネットワークに新しい命の色を添える商人。", "あなたが「ベンダー（価値の提供者）」として誇りを持つべきなのは、モノを売ることではなく、それによって（。誰かの不調や悩みを鮮やかに解決しているという事実なのです。"),
    ("monopoly", "Monopoly", "独占", "16th Century", "monos (alone, single) + polein (to sell)", "The exclusive possession or control of the supply of or trade in a commodity or service", "多様性を否定し、自分「一人だけ（モノ）」が全ての供給と流通を支配（。支配しようとする、停滞と退廃を招きかねない特権的な囲い込み。", "一つのアイデアに「モノポリー（独占欲）」を持たず、みんなに開放（。オープン）してみませんか。そこから予想もつかない巨大な進化が始まるかもしれません。"),
    ("competitive", "Competitive", "競争力のある、競技の", "19th Century", "com- (together) + petere (to strive, seek)", "Relating to or characterized by competition", "ライバルと切磋琢磨し、同じ高みを目指して「共に競い（ペティート）合う」ことで、自らの限界を突破し、より洗練された強さを追求しようとする向上心。", "「コンペティティブ（競争が激しい）」な環境は、あなたを苦しめるためにあるのではなく、あなたの（。眠れる才能を叩き起こして、本物にするために用意された試練なのです。"),
    ("lucrative", "Lucrative", "儲かる、有利な", "15th Century", "lucrum (gain, profit)", "Producing a great deal of profit", "苦労の果てに獲得した「実り（ルクラム）」が大きく、周囲にもその豊かさを分け与えられる（。、強力なエナジーを持った継続可能な活動の果実。", "単に「ルクラティヴ（儲かる）」な仕事を選ぶのではなく、あなたの魂がもっとも（。喜びを感じ、かつ他者の役にも立てる道を探し、そこを黄金の道に変えてください。"),
    ("volatile", "Volatile", "揮発性の、変わりやすい", "17th Century", "volare (to fly)", "Liable to change rapidly and unpredictably, especially for the worse", "鳥のように「羽ばたいて（ヴォラ）」すぐにあらゆる方向へと飛び去ってしまうほど、予測不能で不安定な、しかし生命力に充ちた（みちた）変化の兆し。", "「ヴォラタイル（激しく変動する）」な市場を恐れることはありません。カオスの中に（。こそ、新しい秩序を打ち立てるための最高のチャンスが潜んでいるのですから。"),
    ("strategic", "Strategic", "戦略的な、重要な", "19th Century", "strategos (leader of an army)", "Relating to the identification of long-term or overall aims and interests and the means of achieving them", "目の前の戦い（バトル）を一過性のものにせず、軍の指揮官（ストラテゴス）のような俯瞰した（。視点で、遠い勝利への道筋を冷徹に描き出すこと。", "人生という巨大なゲームの「ストラテジック（戦略的）」な設計図は、あなた自身の（。手で描いてください。目的地を他人に決めさせては絶対に（。ならないのです。"),
    ("venture", "Venture", "冒険的事業、ベンチャー", "15th Century", "adventurus (about to arrive, about to happen)", "A risky or daring journey or undertaking", "何が「起こる（アヴェント）」か分からない不確実な未来に、自らのすべてのリソース（。を賭けて飛び込む、勇気と好奇心に満ちたフロンティア・スピリット。", "小さな部屋から始まったその「ベンチャー（冒険）」は、今や世界を塗り替える巨大な（。うねりとなって、人々の未来に新しい光を灯そうとしています。"),
    ("startup", "Startup", "スタートアップ、新規事業", "19th Century", "start + up", "A newly established business", "地面から力強く「立ち上がり（アップ）」、既存の常識をゼロから塗り替えるために、最初の一歩（スタート）を力強く踏み出したばかりの（。、瑞々しくも攻撃的な挑戦者。", "どんな大企業も、最初は誰かの情熱から始まった「スタートアップ（生まれたばかりの芽）」でした。自分の未熟さを、可能性という名の最高のギフト（武器）に変えてください。"),
    ("enterprise", "Enterprise", "企業、進取の気性、事業", "15th Century", "entre- (between, among) + prendre (to take, seize)", "A project or undertaking, typically one that is difficult or requires effort", "人々のニーズの「間に（アントレ）」入り込み、そこにある価値を自らの知恵で「掴み取（プリーズ）」、新しい価値として社会に提供する、能動的な勇気の総称。", "「エンタープライズ（果敢な事業心）」を忘れないでください。社会の隙間（すきま）にあなたが（。差し込む一筋の光が、やがて巨大な経済の大動脈になることもあるのです。"),
    ("corporation", "Corporation", "株式会社、法人、企業", "15th Century", "corpus (body)", "A large company or group of companies authorized to act as a single entity and recognized as such in law", "法律上の「一つの肉体（コーパス）」として認められ、多くの人々の意志が一つの細胞となって結集した、社会という海を航行する巨大な（。有機体。", "巨大な「コーポレーション（法人）」の一員であることは、大きな責任を伴（。いますが、同時に一人の力では決して成し遂げられない、人類史に残る偉業に挑戦できる（。特等席でもあるのです。"),
    ("subsidiary", "Subsidiary", "子会社、補助的な", "16th Century", "sub- (under) + sidere (to sit)", "A company controlled by a holding company", "本社の「下に（サブ）座り（シット）」、特定の専門分野を担当することで、巨大なグループという巨大なシステム全体の調和と効率（。を裏から支える、重要な歯車。", "「サブシディアリー（補助的な存在）」であることに卑下（ひげ）する必要はありません。どんな巨大な（。塔も、見えない地下の支柱（しちゅう）がなければ、一瞬で崩れ去ってしまう（。のですから。"),
    ("acquisition", "Acquisition", "買収、習得、獲得", "14th Century", "ad- (to) + quaerere (to seek)", "An asset or object bought or obtained, typically by a museum or library", "自らに足りないものを「外に求め（クワイア）」、その価値を自分の一部として受け入れ、統合することで、さらなる高みへと飛躍（。しようとする戦略的な拡大行為。", "新しい言語の「アクイジション（習得）」は、単なるスキルの追加ではありません。それは世界を解釈（。するための新しい魂の目（視点）を手に入れることなのです。"),
    ("bankrupt", "Bankrupt", "倒産した、破産者", "16th Century", "banca (bench) + rupta (broken)", "Declared in law unable to pay outstanding debts", "かつて活気にあふれていた商人の「ベンチ（机）が破壊（。され）」、これまでのルールが通用しなくなった、痛みを伴うが不可避な、再起動（リセット）のための静止点。", "人生の「バンクハプト（精神的な破産状態）」に陥った時は、一度すべてを（。手放してみましょう。空っぽになった心には、以前よりもずっと純粋で美しい夢が、また注（。がれ始めますから。"),
    ("insolvent", "Insolvent", "支払い不能の、破産した", "17th Century", "in- (not) + solve (to dissolve, loosen)", "Unable to pay one's debts", "絡み合った負債の糸を「解きほぐす（ソルヴ）」ことができなくなり、身動きが取れなくなった不自由な状態。限界を超えた負担が思考（システム）を麻痺させている時。", "「インソルヴェント（行き詰まり）」を感じているのなら、問題を一つずつ分解して、解き（。ほぐせる小さな糸から丁寧に手をつけてみてください。解決の糸口は必ず見つかります。"),
    ("liquidation", "Liquidation", "清算、整理、解体", "16th Century", "liquidus (fluid, liquid)", "The process of liquidating a business", "固執していた形（かたち）を一度「液体化（リキッド）」して流し去り、残った本質的な価値（。だけを選別して、新しい生命の素材へと再構成するための、浄化のプロセス。", "古いプライドを「リクイデーション（清算）」できた時、あなたの魂の解像度は一気に上がり（。、何が本当に大切で、何がただの虚飾だったのかを、鏡のように鮮明に映し出すことでしょう。"),
    ("dividend", "Dividend", "配当（金）、利益の分け前", "15th Century", "dividere (to divide)", "A sum of money paid regularly by a company to its shareholders out of its profits", "成功の実りを独り占めにせず、参加した全ての者たちに「平等に切り分け（ディバイド）」、喜びを分かち合う（。ことで、社会全体の信頼と活力を高めていく、感謝の分配。", "あなたが誰かに与えた優しさは、いつか必ず人生の「ディヴィデンド（素敵な配当）」となって、思い（。もよらない時に、あなたの元へ最上の笑顔と共に還ってくるはずですよ。"),
    ("interest", "Interest", "利子、興味、権益", "15th Century", "inter- (between) + esse (to be)", "The state of wanting to know or learn about something or someone", "当事者の「間（インター）に存在する（エッセ）」、お互いを繋ぎ止める切実な価値と関心。自分と他者を結びつける、見えない知的、あるいは経済的な（。強い絆。", "「インタレスト（強い関心）」という名の火を絶やさないでください。その好奇心（。という名の利子が、あなたの人生を、複利のように豊かで予測不可能な冒険に変える（。のですから。"),
    ("debt", "Debt", "借金、恩義", "13th Century", "debere (to owe)", "Something, typically money, that is owed or due", "未来の自分、あるいは他者に対して負った「お返し（欠如）」としての義務。一時的に何かを借りる（。ことで得た可能性と、それに伴う返済という名の誠実な責任。", "「デット（恩義）」を負うことを恐れすぎてはいけません。大切なのは、借りたものを何倍にも（。輝かせて、感謝という名前の素晴らしい利息（ギフト）と共に、世界に還していくこと（。なのです。"),
    ("credit", "Credit", "信用、賞賛、クレジット", "16th Century", "credere (to believe, entrust)", "The ability of a customer to obtain goods or services before payment, based on the trust that payment will be made in the future", "あなたの過去の行いの集積の上に築かれた、「この人を信じても大丈夫だ（。クレド）」という形のない、しかし最も強力な、未来への通行証（チケット）。", "人生の「クレジット（信用）」は、失うのは一瞬ですが、築くのには何十年もかかり（。ます。ただ誠実に、ただ実直に、一歩一歩を丁寧に踏みしめる。それだけが、唯一（。の近道なのです。"),
    ("invoice", "Invoice", "請求書、納品書、インボイス", "16th Century", "en- (in) + voie (path, way)", "A list of goods sent or services provided, with a statement of the sum due for these; a bill", "提供された価値が、お互いに合意された「正しい道（ウェイ）」の上にあることを証明（。し、正当なかたちでエネルギー（対価）の循環を促す、信頼の報告書。", "「インボイス（請求書）」を送る時は、単なる数字のやり取りではなく、提供した（。サービスの質に対する『自分の誇り』も一緒に同封する。そんな心意気が、次（。なる最高の仕事を呼び込むのです。"),
    ("rebate", "Rebate", "払い戻し、リベート、還付", "15th Century", "re- (again) + battre (to beat)", "A partial refund to someone who has paid too much money for tax, rent, or a utility", "一度打ち出（。された支払いの波を、正当な理由によって「再び（リ）打ち（バット）返す」ことで、過剰な負担を正し、公平な調和を再構築する、誠実な（。調整。", "税金の「リベート（還付金）」が戻ってきたら、それは国との間での（。、一つの公平な『対話』が完了したのだと捉えてみてください。そこには正義（ジャスティス）という名の清々しさが宿っているはずです。"),
    ("discount", "Discount", "割引、無視する、ディスカウント", "17th Century", "dis- (away) + count", "A deduction from the usual cost of something", "決められた数（カウント）から、いくつかの要素を「取り去（アウェイ）る」ことで、新しい出逢い（。のハードルを下げ、価値の流動性を爆発的に高める、賢明な譲歩。", "他人の価値を安易に「ディスカウント（見くびる）」してはなりません。どんな（。平凡に見える人の中にも、あなたが見逃している、計り知れない黄金の原石が（。必ず眠っているのです。"),
    ("premium", "Premium", "プレミアム、保険料、賞品", "16th Century", "prae- (before) + emere (to take, buy)", "An amount to be paid for a contract of insurance", "手に入れる（。バイ）「前に（プレ）」あらかじめ支払う、未来の安心や、他には（。ない特別な価値を享受するための、勇気と贅沢さに満ちた特別な贈り物（。ギフト。", "あなたの「プレミアム（最高の輝き）」な情熱を浪費しないでください。それを分かって（。くれる、あなた自身の本質を愛してくれる人たちのために、その輝きを大切に（。使い切ってくださいね。"),
    ("revenue", "Revenue", "収益、収入", "15th Century", "re- (again) + venire (to come)", "Income, especially when of a company or organization and of a substantial nature", "社会に価値を提供し続けた結果として、豊かな実りが「再び自分の元へ還（。リ・カム）ってくる」という、信頼と感謝のポジティブなフィードバックの波。", "「レベニュー（利益）」の額は、あなたがどれほどの人を、どれほど深く（。幸せにできたかという、喜びの総量を示す一つの指標に他ならないのです。"),
    ("expense", "Expense", "費用、出費", "15th Century", "ex- (out) + pendere (to weigh, pay)", "The cost required for something; the money spent on something", "新しい価値を産み出す、あるいは自分を磨くという⚖（天秤）の結果、外へと「量り出して（アウト・ペイ）」放たれた、未来への投資という名のエナジーの等価（。交換。", "今の「エクスパンス（出費）」を、失う痛みとしてではなく、自分が新しい（。世界へ羽ばたく（。ための『入場料』だと思って、清々しい気持ちで支払われて（。みてください。"),
    ("markup", "Markup", "値上げ、粗利益、マークアップ", "19th Century", "mark + up", "The amount added to the cost price of goods to cover overhead and profit", "提供された原材料に、あなたの技術、センス、そして愛という名の付加価値を加え（。、目印（マーク）を「一段高く（アップ）」引き上げる、知的な仕事の総称。", "人生にも「マークアップ（付加価値の向上）」が必要です。同じ日常の繰り返しに、あなた（。だけの新しい経験（。という彩りを加えれば、人生の単価は一気に跳ね上がります。"),
    ("ledger", "Ledger", "元帳、台帳、レジャー", "15th Century", "liggen (to lie, stay in place)", "A book or other collection of financial accounts of a particular type", "どんなに激しく社会の海が荒れても、決して動かずにその場に「留まり（。ライ）、真実を記録し続ける」という、揺るぎない信頼の土台となる一冊の重い本。", "あなたの心の中にある「レジャー（魂の台帳）」を、嘘偽りのない言葉で（。埋め尽くしてください。最後の瞬間にそれを見返した時、あなたは自分の人生（。を最高の傑作だったと確信できるはずです。")
]

def run_cycle():
    file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
        if not match:
            print("Error: Could not find WORDS array in data.js")
            return

        prefix, json_array_str, suffix = match.groups()
        existing_words = json.loads(json_array_str)
        existing_ids = {w.get("id") for w in existing_words}
        existing_word_texts = {w.get("word").lower() for w in existing_words}

        added_count = 0
        for item in words_data:
            word_text = item[0]
            word_id = f"{word_text.lower()}_trade"
            
            if word_id not in existing_ids and word_text.lower() not in existing_word_texts:
                new_word = {
                    "id": word_id,
                    "word": word_text,
                    "meaning": item[2],
                    "era": item[3],
                    "etymology": {
                        "components": [item[4]],
                        "original_statement": f"From {item[3]} {item[4]}."
                    },
                    "concept": item[5] + f" ({item[6]})",
                    "thinking": item[6],
                    "aftertaste": item[7] if len(item) > 7 else "価値の交換は、人間の信頼が生んだ最も美しい発明です。",
                    "example": f"We finalized the {word_text} after a long negotiation.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["経済とは、実体としてのモノと、信頼という名の目に見えない糸が織りなす巨大なタペストリーです。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["bargain", "barter", "retail", "wholesale", "monopolize", "compete"] else "verb"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Trade & Value (Cycle 26).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
