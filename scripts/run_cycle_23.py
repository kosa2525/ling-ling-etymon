import json
import re

# Theme: The Pulse of the City & Movement (Cycle 23)
words_data = [
    ("commute", "Commute", "通勤する、交換する", "16th Century", "commutare (to change, exchange)", "Travel some distance between one's home and place of work on a regular basis", "家という安らぎの地と、仕事という社会の最前線の間を、毎日欠かさず「往復（交換）」し続ける、現代人の最も静かなる巡礼行為。", "退屈な「コミューン（通勤）」の時間も、お気に入りの本があれば、それは自分を深めるための特別な移動書斎へと変わります。"),
    ("congestion", "Congestion", "混雑、密集、鬱血", "15th Century", "congerere (to bring together, heap up)", "The state of being crowded and full of traffic", "あまりにも多くの要素が一箇所に「集まりすぎて」身動きが取れなくなり、都市という巨大な生命体の流れを完全に止めてしまう鬱滞（うったい）。", "道路の「コンジェスチョン（渋滞）」に巻き込まれたら、焦るのをやめて、今日の空の色がこんなに綺麗であることに気づくチャンスだと思いましょう。"),
    ("bottleneck", "Bottleneck", "狭い通路、障害、ボトルネック", "19th Century", "bottle + neck", "A situation that causes delay in a process or system", "ボトルの「細い首の部分」のように、どんなに広い道を用意しても、そこを通らざるを得ないことで全体の流れを決定づけ、遅延させてしまう宿命的な隘路。", "効率ばかりを求めるのをやめて、このプロジェクトの「ボトルネック（目詰まり）」がどこにあるのか、静かに鳥の目で眺めてみましょう。"),
    ("transit", "Transit", "通過、移送、交通機関", "15th Century", "transire (to go across)", "The carrying of people, goods, or materials from one place to another", "ある点から別の点へと「横切り、移動し続ける」という純粋な運動。目的地そのものよりも、その過程において流れる景色を楽しむ心の余裕。", "「トランジット（乗り換え）」の空港で過ごす数時間は、まるで日常から切り取られた、どこにも属さない自由な空白の時間です。"),
    ("hub", "Hub", "中心、ハブ", "17th Century", "hus (house, casing)", "The effective center of an activity, region, or network", "あらゆるネットワークの糸が一本の点へと収束し、そこから再び世界へと四方八方に拡散していく、都市機能の「心臓部であり、家」のような場所。", "古い港町が、今では最新テクノロジーの「ハブ（中核拠点）」として、世界中から若き才能を強力に引き寄せています。"),
    ("interchange", "Interchange", "交換、インターチェンジ", "14th Century", "entre- (between) + changier (to change)", "A junction of roads on different levels", "二つの道が交差するだけでなく、高さや角度を変えて「お互いの軌道へと入り混じる」こと。情報の交換や運命の交差が、流れるような曲線を描いて行われる場所。", "異なる分野の人間が「インターチェンジ（情報交換）」することで、思いも寄らない素晴らしいアイデアが火花を散らすのです。"),
    ("boulevard", "Boulevard", "並木道、ブルバール", "18th Century", "bolwerc (bulwark, defense wall)", "A wide street in a town or city, typically one lined with trees", "かつての防御壁（ブルワーク）が、やがて人々が優雅に歩き、自然と都市が調和して「呼吸する」ための、並木が美しい広い大通りへと変貌（へんぼう）を遂げた姿。", "夕暮れ時の「ブルバード（大通り）」を、好きな人とゆっくり歩く。それだけで、人生のすべての価値を証明したような気分になれます。"),
    ("avenue", "Avenue", "大通り、手段、並木道", "17th Century", "avenir (to come, arrive)", "A broad road in a town or city, typically having trees at regular intervals along its sides", "目的地へ向かって真っ直ぐに伸び、その先に何かが待っているという「訪れ（到着）」の予感を人々に抱かせる、堂々としていて希望に満ちた道。", "解決策は一つとは限りません。まだ誰も試していない新しい「アヴェニュー（道筋・手段）」が、あなたの目の前には無限に広がっています。"),
    ("alley", "Alley", "路地、裏通り", "14th Century", "aler (to go, walk)", "A narrow passage or way in a city between buildings", "巨大なビルの隙間に隠され、迷い込んだ者にだけ一瞬の静寂と、都市の「本当の素顔」をこっそりと見せてくれる、細く曲がりくねった秘密の通り道。", "きらびやかなメインストリートよりも、一本入った「アレイ（路地）」の古いブックカフェこそが、私の本当の居場所だったのです。"),
    ("pavement", "Pavement", "舗装道路、歩道", "13th Century", "pavare (to beat, ram down)", "A raised paved or asphalted path for pedestrians at the side of a road", "荒々しい大地を力強く打ち据え（パタレート）、平らで強固な「人間のための足場」へと作り変えた、文明の第一歩となる硬い皮膚。", "雨上がりの「ペイヴメント（舗道）」が街灯を反射して銀色に輝く。そんな何気ない一瞬に、私たちは都会の美しさを見出します。"),
    ("gravel", "Gravel", "砂利、ジャリ", "13th Century", "grave (sand, shore)", "A loose aggregation of small water-worn or pounded stones", "長い年月をかけて水に洗われ、小さく「角が丸くなった石の粒」。一歩踏みしめるたびに、小気味よい音を響かせて自分の存在を教えてくれる。"),
    ("cobblestone", "Cobblestone", "小石、石畳", "15th Century", "cob (round lump) + stone", "A small, round stone which is used to cover road surfaces", "丸っこい（コブのような）石を一つ一つ手作業で敷き詰め、ガタガタとした不便な「リズム」を刻むことで、過去の歴史と馬車の振動を現代へと繋ぐノスタルジーの路面。"),
    ("bridge", "Bridge", "橋、橋渡し", "Old English", "brycg (bridge)", "A structure carrying a road, path, railroad, or canal across a river, ravine, road, railroad, or other obstacle", "深い谷や川という「断絶」の向こう側へと命を運ぶために、空中に放たれた勇気ある希望の架け橋。"),
    ("tunnel", "Tunnel", "トンネル、地下道", "15th Century", "tonnelle (cask, vault)", "An artificial underground passage, especially one built through a hill or under a building", "山や街の重みをその身に引き受け、本来は進めないはずの「暗黒の中心を貫き通す」ことで、新しい世界へと抜け出すための地下の通路。"),
    ("viaduct", "Viaduct", "陸橋、高架橋", "19th Century", "via (way) + ductu (leading)", "A long bridge-like structure, typically a series of arches, carrying a road or railroad across a valley or other low ground", "地上という迷宮から、高架の上の「真っ直ぐな最短距離」へと人々を導き出し、都市を立体的な動脈へと繋ぎ変える、空を行く導路。"),
    ("overpass", "Overpass", "跨線橋（こせんきょう）、歩道橋", "19th Century", "over + pass", "A bridge by which a road or railroad passes over another", "交差する矛盾を「上下に切り離して」解決し、誰の邪魔もすることなく、また誰にも邪魔されることなく、高みの視点から世界を通過させるための知恵。"),
    ("pedestrian", "Pedestrian", "歩行者、平凡な", "18th Century", "pes (foot)", "A person walking rather than traveling in a vehicle", "機械の力を借りず、自らの「足（フット）」の力だけで大地を踏みしめ、自分の心拍と同じスピードで世界を味わおうとする、最も自由で脆弱な人間。", "「ペデストリアン（歩行者のための空間）」を歩けば、車窓からでは決して気づけなかった路端の小さな花の香りに、ふと心を奪われます。"),
    ("strolling", "Strolling", "散歩する、ぶらぶら歩く", "16th Century", "strole (to wander)", "Walking in a leisurely way", "何一つ急ぐ理由もなく、ただ自分の心拍数と「歩調を合わせ」、流れる雲や風の音を楽しみながら、あてもなく空間を漂う贅沢。", "休日の午後は、スマホを家に置いて「ストローリング（のんびり散歩）」に出かけましょう。世界がどれほど饒舌（じょうぜつ）に語りかけてくるか、きっと驚くはず。"),
    ("wandering", "Wandering", "放浪、迷走", "14th Century", "wandrian (to roam, go astray)", "Traveling aimlessly from place to place", "正しい道（メインルート）からあえて「外れ」、迷うことそのものを目的としながら、未知の風景や自分自身の深淵を探し求める、あてのない心の旅。", "「ワンダリング（彷徨う）」した先で見た夕日は、地図通りに進んでいては見ることのできなかった、あなただけの秘密の宝物です。"),
    ("roaming", "Roaming", "徘徊、周遊、ローミング", "13th Century", "romen (to wander, travel)", "Moving about or traveling aimlessly or unsystematically", "特定の境界に縛られず、好奇心の赴くままに「広大な領域を駆け巡り」、世界のあらゆる断片を自由に吸収して回る、野生と知性の融合した移動。", "彼の瞳はいつも、まだ見ぬフロンティアを「ローミング（自由に周遊）」する、冒険家の輝きを湛（たた）えていました。"),
    ("surging", "Surging", "押し寄せる、急増する", "15th Century", "surgere (to rise)", "Moving suddenly and powerfully forward or upward", "一つの意志を持った巨大な波のように、個々人が溶け合い、圧倒的な力で特定の方向へと「一気に突き進む」ダイナミックな群衆のエネルギー。", "「サージング（押し寄せる波のような）」な群衆の熱気の中で、私は自分一人の存在が宇宙の一部であることを、激しさと共に再認識しました。"),
    ("swerving", "Swerving", "急にそれる", "Old English", "sweorfan (to rub, file, depart from)", "Change or cause to change direction abruptly", "予期せぬ障害物を回避するため、あるいは直感的な決断を下した瞬間に、これまでの軌道を「鋭く、滑るように」一瞬で転換させる、生存のための俊敏な動き。", "目の前の壁にぶつかる直前に、彼は見事なテクニックで人生を「スワーヴ（急旋回）」させ、新しい道を見事に切り拓きました。"),
    ("speeding", "Speeding", "スピードを出す、成功する", "Old English", "spedan (to succeed, prosper, hurry)", "Moving very quickly", "時間の密度を圧縮し、風を切り裂きながら「速く、そして成功へと近づく」ために、生命のエナジーを回転数へと変換しようとする野心的な疾走。", "「スピーディング（加速）」しすぎると、本当に大切な景色はすべて流れて見えなくなってしまいますよ。時にはブレーキを踏む勇気を。"),
    ("slowing", "Slowing", "減速、ゆるやかさ", "Old English", "slaw (dull, sluggish)", "Reducing speed", "外部の喧騒や過剰な情報の波が収まり、時間そのものが「本来の穏やかなリズム」へと回帰していく、安らぎと再発見のための減速のプロセス。", "夕暮れの街が「スローイング（速度を落とす）」していく時間帯は、私たちもまた、自分の内面の声に耳を傾けるべき聖なる時間です。"),
    ("halting", "Halting", "停止、ためらい、たどたどしい", "Old English", "healt (lame)", "Bringing to a stop", "自信満々に進んでいた足取りを一旦「止め」、そこにある矛盾や新しい事実に気づくための、勇気ある一時停止と深い思索の瞬間。", "彼女の「ホールティング（たどたどしい）」な話し方の節々には、言葉にできないほどの深い誠実さが、たしかに宿っていました。"),
    ("merging", "Merging", "合流、併合", "17th Century", "mergere (to dip, immerse)", "Combining or being combined into a single entity", "異なる二つの流れが、一つの「大きな川へと深く潜り込み」、互いの境界を融解させて一つの目的へと向かい始める、強力で調和の取れた統合。", "異なる二つの会社が「マージング（合併）」した時、そこには今までにない全く新しい化学反応が生まれ、業界の地図は塗り替えられました。"),
    ("branching", "Branching", "枝分かれ、分岐", "14th Century", "branche (twig, branch of a tree)", "Dividing into one or more subdivisions", "一つの可能性の幹から、いくつもの新しい運命が「枝を伸ばす」ように分かれ出し、無限に広がる選択肢の中から自分だけの道を選び取っていく自由と不確実性の展開。", "「ブランチング（分岐）」した道のどちらを選ぶべきか迷ったら、より難しく、より胸が躍る方を選んでみてはいかがでしょうか。"),
    ("diverging", "Diverging", "分岐する、逸脱する", "17th Century", "dis- (apart) + vergere (to bend)", "Tending to be different or develop in different directions", "これまで同じ志を持っていた者たちが、考え方の違い（曲がり方の違い）によって、それぞれの「信じる道へと分かれて進み出す」という、寂しくも誇り高い自律の瞬間。", "かつての親友と意見が「ダイヴァージング（分岐）」しても、それは二人がそれぞれの人生を誠実に生きようとしている証拠です。"),
    ("intersection", "Intersection", "交差点、共通部分", "16th Century", "inter- (between) + secare (to cut)", "A point at which two or more things intersect", "異なる二つの方向性を持った道が「お互いを切り裂き（セクション）」ながら接触し、一瞬だけ同じ時空間を共有する、都市の中で最もドラマチックな出逢いと別れの結節点。", "この「インターセクション（交差点）」で信号を待っている間に出逢ったその人は、あなたのその後の人生を決定づける運命の人かもしれません。"),
    ("crossroad", "Crossroad", "交差点、十字路、岐路", "16th Century", "cross + road", "A point where two roads cross each other", "神聖な十字の形を作り、人生における「重大な決断」を迫る場所。どちらへ進むかで、その後の物語が全く別のものへと変容してしまう、運命の分岐点。", "あなたが今立っているのは、長い人生の中でも滅多にない「クロスロード（重要な岐路）」です。後悔のないよう、自分の心に正直に選んでください。"),
    ("corner", "Corner", "角、曲がり角、コーナー", "13th Century", "cornu (horn)", "A place or angle where two or more sides or edges meet", "二つの面がぶつかって鋭い「角（つの）」を作り、視界が遮られる場所。その向こう側に何が待っているか分からないという、不安と期待の隠れ蓑。", "人生の「コーナー（曲がり角）」を曲がった直後に、それまでのすべての苦労が報われるような、最高の出逢いが待っていることも珍しくありません。"),
    ("landmark", "Landmark", "目印、画期的な出来事", "Old English", "land + mearc (boundary, mark)", "An object or feature of a landscape or town that is easily seen and recognized from a distance", "広大な世界の中で自分を見失わないための「確かなしるし」。迷った時に立ち返るべき心の羅針盤であり、歴史に刻まれた重要な境界線。", "その研究は、科学の歴史において後世まで語り継がれる「ランドマーク（画期的な出来事）」として、人々の記憶に深く刻み込まれました。"),
    ("skyline", "Skyline", "スカイライン、地平線", "19th Century", "sky + line", "An outline of land and buildings defined against the sky", "人間の傲慢（ごうまん）さと文明の美しさが、鋭い輪郭を持って「空という無限の上に境界線を引いた」時、初めて立ち上がる都市という名の巨大な彫刻。", "夜の摩天楼が作り出す「スカイライン（都市の輪郭）」を見下ろすと、人間たちの無数の営みが、まるで光り輝く星の瞬きのように見えます。"),
    ("sprawl", "Sprawl", "広がること、不規則に広がる", "Old English", "spreawlian (to move the limbs convulsively)", "The disorganized and unattractive expansion of an urban area adjoining a town or city", "意志を持って拡大したのではなく、まるで手足をバタバタと無秩序に「広げてしまった」かのような、都市の際限なき膨張と、それに伴う自然の浸食の不協和音。", "「スプロール（不規則な都市拡大）」の波に飲み込まれそうな古い農園を守り抜く。それが、この街の伝統を愛する彼の誇りなのです。"),
    ("bustle", "Bustle", "賑わい、せわしなく動く", "16th Century", "busken (to prepare, get ready, make haste)", "Move in an energetic or noisy manner", "明日のための「準備（ビジー）」に全員が参加しているかのような、休むことのない都市の喧騒と、生命が脈打つ活気あふれるざわめき。", "駅前の「バッスル（賑わい）」を抜けて静かな公園に辿り着いた時、都会のスピードから解き放たれ、自分自身を取り戻す感覚になれます。"),
    ("vibration", "Vibration", "振動、感動、バイブス", "17th Century", "vibrare (to shake)", "A person's emotional state, the atmosphere of a place, or the associations of an object", "目には見えないけれど、空気を媒介として伝わってくる微細な「震え」。物理的な音だけでなく、人の心が放つオーラや場の空気という名の目に見えない共鳴。", "この古い教会の「ヴァイブレーション（神聖な空気の震え）」は、何世紀にもわたる人々の祈りが、今も壁に染み込んでいるからに違いありません。"),
    ("rhythm", "Rhythm", "リズム、律動", "16th Century", "rhuthmos (measured flow or movement)", "A strong, regular, repeated pattern of movement or sound", "バラバラで無秩序な動きの中に、一定の「測られた流れ」を見出す知性の設計図。宇宙や生命、そして都市が共有する最も心地よい生命の拍動（ビート）。", "都会の「リズム（拍動）」が早すぎると感じた時は、深呼吸をして、自分自身の鼓動のリズムに集中する時間を一日の中に作りましょう。"),
    ("tempo", "Tempo", "テンポ、速度、時期", "17th Century", "tempus (time)", "The speed at which a passage of music is or should be played", "「時間」という名の指揮者が、その場の出来事をどれくらいの速さで進めるかを決定するタクト。速すぎれば熱狂を生み、遅すぎれば沈黙と深い思索を強いる。", "人生の「テンポ（速度）」を自分自身でコントロールできるようになれば、あなたはどんな慌ただしい環境でも、自分を失わずにいられるはず。"),
    ("momentum", "Momentum", "勢い、はずみ、弾み", "17th Century", "momentum (movement, moving force)", "The quantity of motion of a moving body", "一度動き出したものが、「さらに加速（ムーヴ）」していこうとする、目に見えない力。過去の努力が蓄積され、一つの大きなエネルギーの潮流となった、止めることのできない推進力。", "このプロジェクトは今、最高の「モメンタム（勢い）」に乗っています。この弾みを最大限に活かして、誰も見たことのない高みまで一気に駆け抜けましょう。"),
    ("acceleration", "Acceleration", "加速、促進", "16th Century", "accelerare (to hasten to something)", "A vehicle's capacity to gain speed within a short time", "現状に甘んじることなく、目標に向かってより速く、より高く「急ぎ足で」変化のスピードを上げ、重力を振り切って未来を自らの手で手繰り寄せること。", "「アクセラレーション（加速）」する時代の波に翻弄されないためには、自分の中に揺るぎない一つの『核（コア）』を持ち続けることが不可欠なのです。"),
    ("friction", "Friction", "摩擦、不和、フリクション", "16th Century", "fricare (to rub)", "The resistance that one surface or object encounters when moving over another", "二つの面が「擦れ合う（フリクション）」ことで発生する、熱と抵抗。スムーズな進行を妨げる厄介な邪魔者でありながら、前進するために不可欠なグリップ（足がかり）そのもの。", "組織の中に多少の「フリクション（意見の衝突・摩擦）」があるのは、健全な証拠です。それがなければ、誰も本気で前に進もうとしていないのと同じなのです。"),
    ("resistance", "Resistance", "抵抗、反抗、レジスタンス", "14th Century", "resistere (to stand back, withstand)", "The refusal to accept or comply with something", "押し寄せる外部の圧力に対し、しっかりと「踏みとどまって（立ち止まって）」、自分の意志を貫き、不当な支配から自らの尊厳を守り抜こうとする強靭な反発心。", "水面を滑るように進むボートが、水の「レジスタンス（抵抗）」を感じるように、何かに挑戦する時には、必ず反対する勢力が現れるものなのです。"),
    ("trajectory", "Trajectory", "軌道、弾道、生き方", "17th Century", "traicere (to throw across)", "The path followed by a projectile flying or an object moving under the action of given forces", "放たれた矢や人工衛星が、重力と初速の計算によって作り出す「空間を横切る曲線」。過去の選択が点と点を繋ぎ、未来へと向かう必然的で美しい放物線。", "今の苦労も、後から振り返れば、あなたの成功という名のゴールへと向かうための完璧な「トラジェクトリー（運命の軌跡）」の一部であったことが分かるでしょう。"),
    ("destination", "Destination", "目的地、運命", "14th Century", "destinare (to make firm, establish)", "The place to which someone or something is going or being sent", "旅の終わりである「確立された（揺るぎない）」場所。あらゆる不安や移動が、そこへ到達することで平安へと変わる、約束された再会と休息の地。", "「デスティネーション（目的地）」に辿り着くことだけを考えず、窓の外に流れる名もなき風景のひとつひとつを、もっと大切に愛（いと）しんでみませんか。"),
    ("departure", "Departure", "出発、離別、逸脱", "14th Century", "departir (to divide, distribute)", "The action of leaving, especially to start a journey", "慣れ親しんだ過去の領域を「切り離（デパート）」し、未知の世界という荒野へと最初の一歩を踏み出す、期待と一抹の寂しさが混ざり合った聖なる訣別の時間。", "新しい自分に生まれ変わるための「デパーチャー（出発）」の朝。あなたはもう、昨日までの自分を優しく許し、新しい船に乗る準備ができているはず。")
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
            word_id = f"{word_text.lower()}_city"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "都市の鼓動は、私たちの血液の流れと同じリズムを刻んでいます。",
                    "example": f"The daily {word_text} shaped the lives of everyone in the metropolitan area.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["移動と都市の秩序は、人間の拡張された意志の現れです。"]
                    },
                    "part_of_speech": "verb" if item[0] in ["commute", "transit", "stroll", "wander", "roam", "surge", "swerve", "speed", "slow", "halt", "merge", "branch", "diverge"] else "noun"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Pulse of the City (Cycle 23).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
