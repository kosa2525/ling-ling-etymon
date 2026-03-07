import json
import re

# Theme: The Pulse of Philosophy & Existence (Cycle 28)
words_data = [
    ("essence", "Essence", "本質、エッセンス", "14th Century", "esse (to be)", "The intrinsic nature or indispensable quality of something", "あらゆる虚飾や装飾を「削ぎ落と（。した）」果てに残る、その存在を（。その存在たらしめている）唯一無二の輝き。魂の指紋。", "あなたが何を持っている（。ハヴ）かではなく、あなたが何者である（。ビー）か。それこそがあなたの「エッセンス（本質）」の（。香（かぐわ）しさを（。決定するのです。"),
    ("substance", "Substance", "物質、実体、内容", "13th Century", "sub- (under) + stare (to stand)", "A particular kind of matter with uniform properties", "表面的な（。変化の「下（サブ）で（。どっしりと）立ち続けている」もの。空虚な言葉ではなく、重みと手触りを伴った揺るぎない（。真実の塊。", "どれほど華やかな「サブスタンス（実体）」を持たない成功も、時の（。一吹きで霧のように消え去って（。しまうでしょう。まずは中身（。コア）を（。磨き上げてください。"),
    ("attribute", "Attribute", "属性、象徴、帰する", "14th Century", "ad- (to) + tribuere (to assign, give)", "A quality or feature regarded as a characteristic or inherent part of someone or something", "その対象に「割り当てられた（。トリビュート）」固有の特質や美徳。全体の調和の中に（。、その存在を位置づけるための（。色彩豊かな（。レッテル。", "誠実さ（。という「アトリビュート（属性）」は、あなたの（。すべての行動（。に輝きを与え、周囲の人々を惹きつける（。磁石（マグネット）のような役割を果たすのです。"),
    ("category", "Category", "範疇、カテゴリー", "16th Century", "kata (down) + agoreuein (to speak openly, harangue)", "A class or division of people or things regarded as having particular shared characteristics", "広場（。アゴラ）において「声高（。に語り（。仕分け）られた」こと。混沌（カオス）とした世界（。に知性の網を投げ、秩序という名の（。箱（ボックス）へ（。収めていく行為（。）。", "あなたという（。「カテゴリー（既存の枠組み）」の中に（。あなたを（。閉じ込めようとする（。他人の言葉（。に耳を貸して（。はなりません。あなたは定義される者ではなく、定義を作り出す者（。クリエイター）なのですから。"),
    ("concept", "Concept", "概念、コンセプト", "16th Century", "com- (together) + capere (to take, seize)", "An abstract idea; a general notion", "バラバラの経験を一箇所に「集めて（コン）鷲掴（。み（センプト）にした」もの。複雑な現実を一言の（。知恵（。へと（。凝縮した、思考の（。強力な（。武器。", "新しい「コンセプト（概念）」を手に入れることは、世界を見るための（。新しいメガネ（。をかけるのと（。同じです。今まで（。見えていなかった（。輝きが、一瞬にして目の前に溢れ出す（。でしょう。"),
    ("premise", "Premise", "前提、根拠", "14th Century", "pre- (before) + mittere (to send)", "A previous statement or proposition from which another is inferred or follows as a conclusion", "議論や行動を始める「前に（プレ）送り出される（ミス）」、全ての思考の出発点となる確信の種火。", "議論が平行線をたどる（。のなら、一度「プレミス（前提）」に立ち返ってみましょう。私たちは同じ場所からスタートしようとしていますか？"),
    ("logic", "Logic", "論理、理屈", "14th Century", "logos (reason, idea, word)", "Reasoning conducted or evaluated according to strict principles of validity", "言葉（。ロゴス）の鎖を一段ずつ（。、そして正確に繋ぎ合わせ（。、感情という名の嵐の中でも（。、真実というゴールへと（。真っ直ぐ（。に（。辿り着くための（。知性の地図。", "どんなに精緻（。な「ロジック（論理）」も、人の（。心を（。動かすのは『共感』という名の温度（。パッション）なのです。冷たい（。論理（。を（。、愛という名の毛布（。で（。優しく（。包んで（。あげてください。"),
    ("syllogism", "Syllogism", "三段論法", "14th Century", "sun- (together) + logizesthai (to reckon)", "An instance of a form of reasoning in which a conclusion is drawn from two given or assumed premises", "二つの（。真実を「共に（シン）計算（ロジ）し直す」ことで、誰も疑いようのない（。第三の出口を（。力強く（。押し出す（。、数学的な美しさを（。備えた（。思考の（。ステップ。", "「AはB、BはC。ゆえにAはC」。そんな美しい「シロジズム（三段論法）」であっても、最初（。のAという一歩が間違って（。いれば、結末は（。悲劇（。にしかならない（。のです。"),
    ("paradigm", "Paradigm", "模範、パラダイム、理論的枠組み", "15th Century", "para- (beside) + deiknunai (to show)", "A typical example or pattern of something; a model", "人々の（。横（パラ）に「示された（。ダイム）」絶対的な模範。ある時代（。において、全員が（。何の（。疑いもなく（。共有している（。、見えない（。世界の解釈の枠組み。", "古い「パラダイム（既存の枠組み）」が崩れ去る時（。、そこには（。大きな（。混乱（コンフュージョン）が（。生まれます。しかし、それ（。こそが新しい（。希望（。を（。発見する（。ための、最良の（。チャンス（。でもあるのです。"),
    ("dualism", "Dualism", "二元論", "18th Century", "duo (two)", "The division of something conceptually into two opposed or contrasted aspects, such as good and evil or mind and matter", "世界（。を（。、光と影、心と体、善と悪のように「二つの（デュオ）」要素に分けて（。解釈しようとする（。（。、シンプルでありながら（。強力な（。対立の（。論理（。）。", "「デュアリズム（二元論）」の罠（トラップ）に（。嵌（。まっては（。なりません。世界は（。、白か（。黒か（。ではなく、無限（。に近い（。豊かな（。グラデーション（。で（。満たされている（。のですから。"),
    ("monism", "Monism", "一元論", "19th Century", "monos (single, alone)", "A theory or doctrine that denies the existence of a distinction or duality in some sphere, such as that between matter and mind, or God and the world", "対立する（。二つのものを（。越え、全ての（。根源は「唯一（モノ）である」と（。宣言する（。、宇宙の（。深遠な（。調和（ハーモニー）を見出そうとする（。、愛（。に（。満ちた（。世界観。", "「モニズム（一元論）」の視点（。から（。見れば（。、あなた（。と（。私を（。隔（。てる壁（。など（。、本来は（。どこにも（。存在しない（。ことが（。理解（。できる（。はずです。"),
    ("nihilism", "Nihilism", "ニヒリズム、虚無主義", "19th Century", "nihil (nothing)", "The rejection of all religious and moral principles, in the belief that life is meaningless", "全ての（。価値を否定し、世界の根源に「虚無（ニヒル）」という名の（。絶対的な砂漠を（。見出してしまう（。（。、冷徹（。で（。孤独な（。知性の（。絶望（。）。", "「ニヒリズム（虚無主義）」の底（。まで（。沈み込んだ（。あなた（。は（。、そこ（。で（。初めて（。、自分自身の（。意志で（。新しい（。価値（。を（。産み出す（。という（。、本当の（。自由（。を（。手に入れる（。ことに（。なるのです。"),
    ("existentialism", "Existentialism", "実存主義", "20th Century", "ex- (out) + sistere (to stand)", "A philosophical theory or approach which emphasizes the existence of the individual person as a free and responsible agent determining their own development through acts of the will", "あらかじめ（。決められた（。ラベル（。を（。拒否し（。、今（。ここで「外へ（。エクス）自ら（。を立たせる（。シスト）」という（。、自律（。と責任（。を（。引き受けた（。、最も（。力強い（。人間の（。生き方。", "「実存主義（エグジステンシャリズム）」とは、あなたが（。今（。この（。瞬間（。の選択（。によって（。、あなた（。自身を（。彫刻（。し（。続けて（。いる（。という（。、気高く（。も（。孤独な（。宣言（。なのです。"),
    ("phenomenology", "Phenomenology", "現象学", "18th Century", "phainesthai (to appear) + logos (study)", "An approach that concentrates on the study of consciousness and the objects of direct experience", "先入観（。を（。一度捨て（。、目の前に「あらわれている（。フェイネ）現象」そのもの（。に（。、驚き（。と（。敬意（。を持って（。耳（。を（。澄ませようとする（。、謙虚（。な（。知性の（。営み。", "「フェノメノロジー（現象学）」のメガネ（。で（。世界（。を（。眺めれば（。、退屈（。な（。日常（。の一コマ一コマが（。、眩（。いばかりの（。奇跡（。の（。連続（。として（。、立ち上がって（。くる（。はずですよ。"),
    ("metaphysics", "Metaphysics", "形而上学", "16th Century", "meta (after, beyond) + physika (physics)", "The branch of philosophy that deals with the first principles of things, including abstract concepts such as being, knowing, substance, cause, identity, time, and space", "目に見える（。物理的な（。世界（フィジカ）の「向こう側（メタ）」にある（。、存在や（。時間という名の（。見えない（。根源的な（。光に（。触れようとする（。、知性の（。果て（。なき冒険。", "「メタフィジックス（形而上学）」という名の（。山（。を（。登ることは（。、日々の（。小さな（。悩み（。を（。遥か下（。に見下ろし（。、永遠（。という名の（。澄み切った（。空気（。を（。吸う（。こと（。なのです。"),
    ("ontology", "Ontology", "存在論", "17th Century", "on (being) + logos (study)", "The branch of metaphysics dealing with the nature of being", "「在（。あ）る（。オント）」とは（。一体（。どういう（。ことか（。、その（。根源的（。で（。究極的（。な（。深淵（。を見つめ（。、存在の（。重み（。を（。測り直（。そうとする（。、静か（。で（。重厚な（。思索の（。底流（。）。", "あなたの「オントロジー（存在のあり方）」は、言葉（。ではなく（。、あなたの（。静かな（。眼差し（。や（。、何気（。ない（。仕草（。の中に（。こそ（。、最も（。雄弁（。に（。宿って（。いる（。もの（。なのです。"),
    ("epistemology", "Epistemology", "認識論", "19th Century", "episteme (knowledge) + logos (study)", "The theory of knowledge, especially with regard to its methods, validity, and scope, and the distinction between justified belief and opinion", "私たちは「知る（エピステーメー）」という（。ことを、どう（。やって（。成し遂（。げて（。いる（。のか（。、その（。知の（。限界（。と（。可能性（。を（。、冷徹（。に（。解（。き（。明かそうとする（。、知性の（。自画像（。）。", "「エピステモロジー（認識論）」を学ぶことは、自分の（。脳（。の（。中（。にある（。バイアス（。という名の（。曇り（。を（。一つずつ（。拭い（。拭（。い、世界（。を（。より（。透明（。に（。見つめる（。ための（。訓練（。なのです。"),
    ("aesthetics", "Aesthetics", "美学、感性", "18th Century", "aisthesis (perception by the senses)", "A set of principles concerned with the nature and appreciation of beauty, especially in art", "ただ見（。る（。こと（。を超え（。、五感（。を通じて（。世界を「深く（。感じ取り（。アイステー）理解する」という、魂の（。研ぎ澄（。まされた（。繊細（。な（。羅針盤（。）。", "あなたの「エスセティクス（美学）」は、日常（。の（。些細（。な（。選択（。の（。中に（。あらわれます（。。何を（。美しい（。と感じ（。、何を（。醜（。いと（。退ける（。か（。、それ（。が（。あなたという（。人間（。のかたち（。を（。決めるのです。"),
    ("rationality", "Rationality", "合理性、理性", "17th Century", "rationalis (belonging to reason)", "The quality of being based on or in accordance with reason or logic", "感情の（。激流（。に（。飲み込まれ（。ず、冷徹（。な（。秤（。で（。価値（。を（。推し量（。り、最適（。な（。道筋（。を（。選び取（。ろうとする（。、知性の（。強靭（。な（。骨格（。）。", "「ラショナリティ（合理性）」は、人生を（。冷酷（。にするための（。道具（。ではなく（。、あなた（。の（。大切な（。情熱（。を（。、正しい（。ゴール（。へと（。導く（。ための（。安全（。な（。レール（。なのです。"),
    ("intuition", "Intuition", "直感、直観", "15th Century", "in- (into) + tueri (to look at, watch)", "The ability to understand something immediately, without the need for conscious reasoning", "論理（。を（。飛び越し（。、対象の（。核心（。を（。一瞬（。で（。心の（。目（。が「見抜（。き（。イントゥ）捉える」という、生命（。に（。備わった（。野生（。の（。叡智（。）。", "あなたの「イントゥイション（直感）」を（。信じて（。あげてください。それは、あなたの（。過去（。の（。すべての（。経験（。が（。、一瞬（。の（。閃（。き（。に変容（。して（。降り（。て（。きた（。、神聖（。な（。導き（。なのですから。"),
    ("empirical", "Empirical", "経験的な、実証的な", "16th Century", "en- (in) + peira (trial, experiment)", "Based on, concerned with, or verifiable by observation or experience rather than theory or pure logic", "本（。の（。上の（。知識（。ではなく（。、自ら（。の手（。で（。触れ（。、自ら（。の（。目（。で（。確かめた（。「試練（。ペイラ）」という（。名の（。、裏切り（。ようのない（。手触り（。のある（。真実（。の（。断片（。）。", "「エンピリカル（経験に基づく）」な知恵（。は（。、嵐（。の（。夜（。にも（。あなた（。を（。支える（。、揺るぎ（。ない（。大地（。になります（。。（。抽象的（。な（。理論（。よりも（。、一欠片（。の（。実体験（。を（。大切（。に（。（。育んで（。ください（。）。"),
    ("abstract", "Abstract", "抽象的な、要約、取り出す", "14th Century", "ab- (away) + trahere (to draw)", "Existing in thought or as an idea but not having a physical or concrete existence", "雑多な（。ディテール（。を（。一度「引き剥（。がし（。アブ・トラ）」て、その奥（。にある（。本質（。的な（。かたち（。を（。、思考（。の中（。へと（。取り出す（。知的な（。抽出（。）。", "「アブストラクト（抽象的）」な思考（。が（。できる（。ように（。なれば（。、あなた（。は（。一見（。全く（。無関係（。に（。見える（。事象（。の中に（。、深く（。美しい（。繋がり（。を（。発見する（。ことが（。できる（。ように（。なるのです。"),
    ("concrete", "Concrete", "具体的な、コンクリート", "14th Century", "com- (together) + crescere (to grow)", "Existing in a material or physical form; real or solid; not abstract", "多く（。の見えない（。エナジー（。が（。、一つの（。場所へと「共に（。コン）凝縮（。して（。成長（。した）」、重み（。と（。硬さ（。を（。伴った（。、否定（。の（。しようのない（。現実（。の（。手触り（。）。", "「コンクリート（具体的）」な一歩を（。踏み出（。さない（。限り（。、どんな（。美しい（。理想（。も（。、ただの（。蜃気楼（。として（。（。消え去（。って（。しまいます（。。（。まずは（。、目の前（。の（。小さな（。石（。を（。一つ（。積み上げる（。ことから（。始めて（。ください。"),
    ("objective", "Objective", "客観的な、目的、対象", "17th Century", "ob- (against, in front of) + jacere (to throw)", "Of a person or their judgment not influenced by personal feelings or opinions in considering and representing facts", "自分（。の（。感情（。から（。（。対象を（。一度「外へと（。オブ）投げ出し（。ジェト）」て（。、第三者（。の（。目（。で（。公平（。に（。（。眺め（。直そうとする（。、誠実（。な（。知性の（。距離感（。）。", "「オブジェクティブ（客観的）」である（。ことは（。、冷徹（。になる（。こと（。ではなく（。、あなた（。が（。一番（。大切（。に（。している（。真実（。を（。、誰（。の（。目（。にも（。見える（。（。かたち（。で（。守り抜（。くための（。、賢明（。な（。戦略（。なのです。"),
    ("subjective", "Subjective", "主観的な、主語の", "15th Century", "sub- (under) + jacere (to throw)", "Based on or influenced by personal feelings, tastes, or opinions", "世界（。という（。キャンバス（。を（。、自ら（。の（。意識（。の「下（。サブ）へと（。投げ入れ（。ジェト）」て（。、自分（。だけの（。色彩（。で（。自由に（。（。塗り（。替え（。ていく（。、かけ（。がえ（。のない（。個人の（。真実（。）。", "世界（。が（。どれほど（。あなた（。に（。冷たく（。当た（。ったとしても（。、あなた（。の「サブジェクティブ（主観的な幸福）」の領域（。だけ（。は（。、誰（。にも（。冒（。される（。こと（。（。のない（。、あなた（。だけの（。聖域（。なのです。"),
    ("absolute", "Absolute", "絶対的な、完全な", "14th Century", "ab- (away) + solvere (to loosen, set free)", "Viewed or existing independently and not in relation to anything else; not relative or comparative", "他（。との（。比較（。という（。鎖（。を「全て（。解（。き（。放（。し（。アブ・ソルヴ）」た、それ（。単独（。で（。完結（。して（。いる（。、揺るぎ（。ない（。究極（。の（。全能（。と（。真理（。）。", "誰（。かの（。評価（。に関係（。なく（。、あなた（。が（。自分（。を「アブソルート（絶対的に肯定）」できれば（。、それだけで（。世界（。は（。一瞬（。にして（。黄金（。の（。輝き（。を（。取り戻す（。こと（。（。ができる（。のです。"),
    ("relative", "Relative", "相対的な、親戚", "14th Century", "re- (back) + ferre (to bring, carry)", "Considered in relation or in proportion to something else", "それ（。単体（。では（。存在（。できず（。、常に（。何か（。別の（。ものと「結び（。つけ（。戻（。され（。リ・フェリー）」て（。初めて（。意味（。が（。立ち上がる（。、流動（。的（。で（。繊細（。な（。存在の（。様態（。）。", "幸福（。も（。不幸（。も（。、すべては「レラティブ（相対的なもの）」に（。すぎません（。。（。暗闇（。が（。ある（。から（。こそ（。、あなたは（。小さな（。光（。の（。ありがた（。み（。を（。、誰よ（。り（。も（。深く（。味わう（。ことが（。できる（。のですから。"),
    ("finite", "Finite", "有限の、限定された", "14th Century", "finis (end, limit)", "Having limits or bounds", "始まり（。が（。あり（。、終わり（。という（。境界線（。が「定（。め（。フィニス）」られている（。こと（。。（。いつか（。（。消え去（。る（。から（。こそ（。、今（。この（。瞬間（。の（。命（。の（。輝き（。が（。（。永遠（。の（。価値（。を（。持つ（。、高貴（。な（。制約（。）。", "時間（。という「フィナイト（有限の財産）」を（。、誰（。かの（。ための（。お世辞（。や（。（。愚痴（。で（。浪費（。しては（。なりません（。。（。あなた（。自身の（。魂（。が（。喜ぶ（。こと（。（。のために（。、その（。一分一秒（。を（。大切（。に（。使い（。切って（。ください。"),
    ("infinite", "Infinite", "無限の、莫大な", "14th Century", "in- (not) + finis (end, limit)", "Limitless or endless in space, extent, or size; impossible to measure or calculate", "どこ（。まで（。行（。っても「終わり（。フィニス）がない」こと（。。（。想像力（。という（。翼（。を（。広げれ（。ば（。、あなた（。は（。肉体（。という（。檻（。を（。越え（。て（。、宇宙（。の（。隅々（。（。まで（。一瞬（。で（。辿（。り（。着ける（。（。、自由（。な（。エナジー（。の（。海（。）。", "あなた（。の（。中に（。は「インフィニット（無限の可能性）」が（。眠（。ってい（。ます（。。（。一度や（。二度（。の（。失敗（。で（。（。自分の（。限界（。を（。勝手に（。決め（。て（。しまう（。のは（。、自分（。という（。宇宙（。に（。対する（。、最大（。の（。冒涜（。なのですよ。"),
    ("transcendence", "Transcendence", "超越、卓越", "16th Century", "trans- (across, beyond) + scandere (to climb)", "Existence or experience beyond the normal or physical level", "今（。いる（。場所（。を（。「越え（。トランス）、高く（。登（。り（。スカンド）」て、既存（。の（。ルール（。や（。限界（。を（。遥か（。下（。に見下ろす（。（。、精神（。の（。劇的（。な（。飛翔（。）。", "「トランセンデンス（超越）」とは（。、特別な（。人間（。だけに（。許された（。行為（。では（。ありません（。。（。今の（。自分（。を（。（。さらに（。更新（。しつづ（。けよう（。とする（。あなたの（。情熱（。の中に（。こそ（。、超越（。の（。種（。は（。（。宿っている（。のです。"),
    ("immanence", "Immanence", "内在、偏在", "17th Century", "in- (in) + manere (to remain, stay)", "The state of being immanent; divine presence in the world", "遠く（。へ（。行く（。のではなく（。、今（。ここ（。にある（。全ての（。もの（。の「中心（。に（。イン）留まり（。マネー）」続けている（。、目（。には（。見えない（。けれど（。（。確かな（。命（。の（。輝き（。）。", "神様（。を（。空の上（。に（。探（。す必要（。は（。ありません（。。（。あなたの（。目の前（。に（。ある（。（。コップ（。や（。、隣（。で（。笑って（。いる（。人（。の（。瞳（。の中に（。、美しき「イマネンス（内在する聖性）」は（。（。満ち（。満ちている（。のです（。から。"),
    ("dichotomy", "Dichotomy", "二分法、二分すること", "16th Century", "dikho- (in two, asunder) + temnein (to cut)", "A division or contrast between two things that are or are represented as being opposed or entirely different", "複雑（。な（。現実（。を（。「真っ二つ（。ディコ）に（。切り（。トム）裂く」ことで（。、対立（。を（。鮮明（。に（。（。浮き彫り（。に（。する（。知性（。の（。外科手術（。）。", "「ダイコトミー（二分法）」による（。整理（。は（。便利（。ですが（。、それ（。によって（。（。削ぎ落（。されて（。しまった（。、豊かな（。矛盾（。（。の（。中に（。こそ（。、人間（。の（。本当（。の（。美しさ（。（。は（。潜（。んでいる（。ものなのです。"),
    ("synthesis", "Synthesis", "総合、合成、シンセシス", "17th Century", "sun- (together) + tithenai (to place, put)", "The combination of ideas to form a theory or system", "対立（。する（。二つの（。要素（。を（。、より高い（。次元（。へと「共に（。シン）配置（。し（。セシス）直す」ことで（。、全く（。新しい（。（。調和（。を（。産み（。出す（。、知性の（。最高（。の（。マリアージュ（。）。", "争い（。を（。争い（。のまま（。終わら（。せては（。なりません（。。（。お互い（。の（。違い（。を（。（。「シンセシス（統合）」し（。、今（。まで（。誰も（。見た（。こと（。のない（。、より（。豊かな（。解（。を（。（。導（。き（。出す（。、その（。プロセス（。を（。楽し（。んで（。ください。"),
    ("paradox", "Paradox", "逆説、パラドックス", "16th Century", "para- (contrary to) + dokein (to think, seem)", "A seemingly absurd or self-contradictory statement or proposition that when investigated or explained may prove to be well founded or true", "常識（。という（。道から（。あえて「外（。パラ）れた（。思考（。ドックス）」を（。することで（。、一見（。矛盾（。して（。（。いる（。けれど（。、その（。奥に（。隠された（。巨大（。な（。真理（。を（。引き（。ずり（。出す（。言葉（。の（。手品（。）。", "「急がば回れ（。）」という（。美しい「パラドックス（逆説）」。最短（。距離（。ばかり（。を（。追い（。求め（。る（。のを（。止（。めた（。時（。、あなたは（。不思議（。と（。、一番（。大切（。な（。ゴール（。の（。（。目の前（。に（。立（。って（。いる（。はずですよ。"),
    ("irony", "Irony", "皮肉、アイロニー", "16th Century", "eirōneia (dissembled ignorance)", "The expression of one's meaning by using language that normally signifies the opposite, typically for humorous or emphatic effect", "本当（。の（。想い（。を（。胸（。に（。秘（。め（。ながら（。、あえて「正反対（。の（。こと（。を（。語る（。）」ことで（。、世界（。の（。滑稽（。さや（。（。まま（。なら（。なさ（。を（。、優雅（。に（。笑い（。飛ばそう（。とする（。知的な（。余裕（。）。", "「アイロニー（皮肉）」は（。、誰（。かを（。傷つける（。ため（。の（。武器（。では（。なく（。、残酷（。な（。運命（。を（。（。軽やか（。な（。ステップ（。で（。かわ（。す（。ための（。、知性（。の（。最後の（。盾（。（。なのだ（。と（。私は（。思い（。ます。"),
    ("ambiguity", "Ambiguity", "曖昧さ、多義性", "14th Century", "ambi- (both) + agere (to drive, lead)", "The quality of being open to more than one interpretation; inexactness", "一つの（。意味（。へと（。無理に（。絞（。り（。込ま（。ず（。、「両方（。アンビ）の（。方向（。へ（。誘（。い（。アグ）込む」ことで（。、意味（。が（。（。たゆた（。い（。、豊か（。な（。余白（。を（。残（。して（。いる（。贅沢（。な（。状態（。）。", "世界（。を（。無理に「アーティキュレート（明確化）」しないで（。ください（。。（。その「アンビギュイティ（曖昧さ）」の霧の中に（。こそ（。、あなた（。が（。（。自由（。に（。夢（。を見（。（。想像（。する（。ための（。（。無限（。の（。キャンバス（。が（。（。広が（。って（。いる（。（。のですから。"),
    ("subtle", "Subtle", "微妙な、繊細な、巧妙な", "14th Century", "sub- (under) + tela (web, warp of a fabric)", "So delicate or precise as to be difficult to analyze or describe", "大雑把な（。分類（。の「下（。サブ）に（。隠された（。、極薄（。の（。織物（。テーラ）」のように（。、注意（。深く（。（。澄（。ませた（。感性（。に（。だけ（。（。あらわれる（。、震（。える（。ような（。美しさの（。微差（。）。", "あなたの（。心（。の（。中の「サトル（微細な）」な（。変化（。を（。、もっと（。大切（。に（。（。拾（。い（。上げ（。て（。あげて（。ください（。。（。誰（。にも（。気（。づか（。（。れない（。ような（。小さな（。（。光（。の中に（。こそ（。、本物（。の（。（。奇跡（。は（。潜（。んで（。いる（。のですよ。"),
    ("sacred", "Sacred", "神聖な、不可侵の", "14th Century", "sancire (to make sacred, confirm)", "Connected with God or a god or dedicated to a religious purpose and so deserving veneration", "日々の（。喧騒（。から（。「切り離れ（。セパレート）、固く（。守（。られ（。サンク）」た（。、一切（。の（。汚れ（。を（。（。寄せ付け（。ない（。、澄み（。切った（。崇高（。な（。静寂（。の（。領域（。）。", "あなた（。の（。中に（。ある（。、自分（。を（。信じる（。心（。。（。それ（。は（。誰（。にも（。汚（。す（。こと（。の（。できない「セイクレッド（神聖な）」な場所（。なのです（。。（。土足（。で（。踏み（。込（。（。もうと（。する（。（。他人の（。言葉（。から（。、あなた（。の（。大切な（。場所（。を（。（。守り（。抜いて（。ください。"),
    ("profane", "Profane", "世俗的な、不敬な、冒涜する", "14th Century", "pro- (before, outside) + fanum (temple)", "Relating or devoted to that which is not sacred or biblical; secular rather than religious", "神殿（。ファーヌ）の「外（。プロ）側（。の（。、土（。埃（。に（。まみれた（。現実の世界」。泥臭（。（。く（。も（。（。逞（。（。しく（。、生命力（。に（。溢れ（。た（。、飾（。り（。のない（。剥き出しの（。日常（。）。", "「プロフェイン（世俗の）」な日常（。を（。嫌（。わないで（。ください（。。（。汗（。を（。かき（。、悩み（。、（。笑い（。合う（。、その（。ありふれた（。時間（。の中に（。こそ（。、真（。の（。神聖（。さは（。（。宿（。るもの（。なのですから。"),
    ("eternal", "Eternal", "永遠の、不滅の", "14th Century", "aevum (age, eternity)", "Lasting or existing forever; without end or beginning", "時間の（。波（。に（。洗（。われて（。も（。、決して（。形（。を（。失わず（。、宇宙の「始まり（。から（。終わり（。まで（。在（。り（。続ける）」こと（。。（。星の（。瞬き（。よりも（。（。確かな（。、魂（。の（。不滅（。の（。輝き（。）。", "「エターナル（永遠）」を（。探（。して（。遠く（。へ（。行く（。必要（。は（。ありません（。。（。あなた（。が（。誰か（。を（。心（。から（。愛（。した（。その（。一瞬（。の中に（。、永遠（。は（。（。確（。かに（。（。息づいて（。いる（。のですよ。"),
    ("temporal", "Temporal", "一時的な、時の、世俗の", "14th Century", "tempus (time)", "Relating to worldly as opposed to spiritual affairs; secular", "「時間（テンパス）」という（。流れ（。の中に（。置かれた（。、はかなく（。移（。ろ（。い（。ゆく（。もの（。。（。いずれ（。消えゆく（。宿命（。だから（。こそ（。、今（。ここ（。で（。（。触（。れる（。（。ことのできる（。喜び（。が（。（。愛お（。しく（。輝く（。、時の（。宝石（。）。", "私たちの（。肉体（。は「テンポラル（一時的）」な（。器（。に（。すぎません（。。（。しかし（。、その（。限られた（。時間（。の（。中で（。（。どんな（。美しい（。調べ（。を（。奏（。でる（。か（。、それ（。が（。魂（。の（。本当（。の（。仕事（。なのです。"),
    ("void", "Void", "空虚、空白、空の、無効にする", "13th Century", "vacare (to be empty)", "A completely empty space", "何一つ（。存在（。しない（。ように（。見える（。けれど（。、実は（。全ての（。可能性（。が「空（。バカ）」として（。（。満たされて（。いる（。、深遠（。な（。静寂（。の（。器（。）。", "心の中の「ヴォイド（空白）」を（。、無理に（。何（。かで（。埋（。めよう（。と（。しないで（。ください（。。（。その（。静寂（。に（。（。耐（。えて（。、ただ（。じっと（。（。見つめて（。いる（。うちに（。、新しい（。宇宙（。が（。そこから（。（。生まれて（。くる（。のです。"),
    ("solitude", "Solitude", "孤独、独り居", "14th Century", "solitudo (loneliness, alone)", "The state or situation of being alone", "他者との強制的な関わりから離れ、自分自身と「心地よく（自発的に）」対話するために用意された、静寂と知性に満ちた聖なる独りの時間。", "「ソリチュード（独りを楽しむ時間）」を持つことで初めて、私たちは他者を真に尊重し、愛するための力を蓄えることができます。")
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
            word_id = f"{word_text.lower()}_phi"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "存在の深淵を見つめることは、自分自身を愛することの始まりです。",
                    "example": f"We pondered the very {word_text} of our shared humanity.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["哲学は問いかける（。クエスチョン）技術であり、答えを出すこと（。アンサー）そのものが目的（。ゴール）ではありません。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["empirical", "abstract", "concrete", "objective", "subjective", "absolute", "relative", "finite", "infinite", "subtle", "sacred", "profane", "eternal", "temporal"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Philosophy & Existence (Cycle 28).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
