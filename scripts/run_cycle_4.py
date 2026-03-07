import json
import re

words_data = [
    ("glimmer", "Glimmer", "かすかな光、微光", "14th Century", "glimmerien (to shine faintly)", "Faint wavering light", "完全な闇から逃れようとする、頼りなくもはにかむような希望の瞬き。", "絶望の淵に立っても、必ずどこかで「グリマー（かすかな光）」があなたを導いてくれます。"),
    ("glitter", "Glitter", "きらきら光る、きらめき", "14th Century", "gliteren (to shine, be brilliant)", "Sparkle brightly", "無数の小さな光跡が織り成す、派手で冷たい人工的な華やかさ。", "「グリッター（きらめき）」する全てが本物の黄金とは限りません。本質を見極めて。"),
    ("glisten", "Glisten", "きらきら輝く、光る", "Old English", "glisnian (to gleam, glisten)", "Shine with a wet surface", "涙や濡れた路面が反射する光のように、悲しみや感傷を含んだ艶やかな輝き。", "「グリスン（濡れて光る）」な瞳を持つ人は、世界中の優しさを知っている人です。"),
    ("gleam", "Gleam", "きらりと光る、かすかな光", "Old English", "glam (bright light, joy)", "Brief flash of light", "厚い雲の切れ間から一瞬だけ差し込む太陽のような、意志の強さと温もり。", "一筋の「グリーム（差し込む光）」が放たれれば、どんな厚い疑念の雲も晴れ渡ります。"),
    ("dazzle", "Dazzle", "目を眩ませる、幻惑する", "15th Century", "dasen (to grow dark, be dizzy)", "Blind temporarily with light", "あまりの美しさや強烈な光で、理性や判断力を一時的に麻痺させてしまう狂気。", "彼女の「ダズル（眩いほどの）」な笑顔に、誰もが世界を愛おしく感じてしまうでしょう。"),
    ("sparkle", "Sparkle", "火花を散らす、きらどく", "13th Century", "sparkle (little spark)", "Shine with small flashes", "内側から湧き上がる生命力や喜びが、抑えきれずに小さな光の粒として弾ける様子。", "「スパークル（弾ける光）」なあなたのアイデアは、退屈な日常に魔法をかけます。"),
    ("flash", "Flash", "ぴかっと光る、閃光", "13th Century", "flaschen (to splash)", "Sudden burst of light", "永遠の闇を暴力的なまでに切り裂き、瞬間的に真実の全貌を暴き出す神の怒り。", "インスピレーションは常に「フラッシュ（閃光）」のように現れ、そしてすぐに消え去ります。捕まえて。"),
    ("flicker", "Flicker", "ちらちらする、またたく", "Old English", "flicorian (to flutter)", "Burn unsteadily", "風前の灯火のように、消えそうになりながらも必死に存在を主張する命のゆらぎ。", "蝋燭の「フリッカー（ゆらめく光）」は、不安定だからこそ神秘的で美しいのです。"),
    ("flare", "Flare", "ぱっと燃え上がる、炎", "16th Century", "flara (to flutter, stream in the wind)", "Sudden brief blaze", "隠していた情熱や抑圧された怒りが、酸素を得て一気に燃え広がる危険な上昇気流。", "怒りの「フレア（燃え上がり）」に我を忘れる前に、ゆっくりとその炎を観察する余裕を。"),
    ("shimmer", "Shimmer", "ちらちら光る、揺らめき", "Old English", "scimerian (to gleam, shine)", "Shine with a tremulous light", "陽炎（かげろう）のように、現実の輪郭をあいまいにぼかしながら魅了する幽玄な光。", "水面の「シマー（揺らめき）」を見つめていると、世界と自分が溶け合っていくのがわかります。"),
    ("shine", "Shine", "輝く、光る", "Old English", "scinan (to shed light, be radiant)", "Give out bright light", "自らが光源となり、他の存在の闇を払い、世界を無条件で照らし出す愛と肯定。", "あなたが笑えば、太陽のように「シャイン（輝いて）」周囲のすべてを明るくします。"),
    ("beam", "Beam", "光を放つ、ニコニコする", "Old English", "beam (tree, ray of light)", "Emit a line of light", "的確に方向を定められ、対象に向かって一直線に突き進む力強く頼もしい光の柱。", "赤ちゃんの「ビーム（に向けた満面の笑み）」は、どんな堅物な老人の心も貫きます。"),
    ("illuminate", "Illuminate", "照らす、解明する", "15th Century", "illuminare (to light up)", "Light up", "闇に覆われた無知や秘密に光を当て、輪郭と意味をクリアに浮かび上がらせる知性の勝利。", "真実は、暗い部屋を「イルミネイト（明るく照らす）」した瞬間にだけその姿を現します。"),
    ("radiate", "Radiate", "四方に放つ、放射する", "17th Century", "radiare (to emit rays)", "Send out rays", "中心からのエネルギーが同心円状に広がり、あらゆるものを拒まず包み込んでいく無償の愛。", "彼女から「レイディエイト（純粋に放射される）」な優しさは、植物さえも生き生きとさせます。"),
    ("blare", "Blare", "鳴り響く、まぶしく光る", "14th Century", "bleren (to wail, cry)", "Loud harsh sound or light", "デリカシーのかけらもなく、自己顕示欲によって他者の感覚器官を暴力的に制圧する強引さ。", "サイレンの「ブレア（やかましい響き）」は、日常の眠りから私たちを叩き起こす使者です。"),
    ("dull", "Dull", "鈍い、どんよりした", "Old English", "dol (stupid, dull)", "Lacking brightness", "研磨を怠った刃や光を失った瞳のように、刺激を受け流し麻痺してしまった悲しい平穏。", "心が「ダル（どんより重い）」な日は、何を感じてもいい。感じなくてもいい。ただ休んで。"),
    ("murky", "Murky", "暗い、濁った", "14th Century", "mirke (dark)", "Dark and gloomy", "泥が混ざり合い、底知れぬ恐怖や隠蔽された嘘が渦巻いている、不吉で近づきがたい領域。", "「マーキー（薄暗く濁った）」な人間関係からは、泥に足を取られる前に速やかに離脱して。"),
    ("dim", "Dim", "薄暗い、かすむ", "Old English", "dimm (dark, obscure)", "Not bright or clear", "光芒（こうぼう）を失い、すべてが灰色の影となって過去の記憶の中へ沈んでいく静寂なる衰退。", "視界が「ディム（薄暗く）」になっても、心の目はより敏感に真実を捉え始めます。"),
    ("gloomy", "Gloomy", "憂鬱な、薄暗い", "16th Century", "glom (twilight)", "Dark and depressing", "光を拒絶し、重苦しい空気をまとってすべてを自身の悲しみに巻き込む内向的な闇。", "「グルーミー（憂鬱な）」な天気の日こそ、温かい紅茶を入れて自分への最高のご褒美を。"),
    ("obscure", "Obscure", "不明瞭な、無名の", "15th Century", "obscurus (dark, dusk)", "Not clearly expressed", "自ら進んで意味を隠し、安易な理解を拒絶することで本質を守ろうとする孤高の盾。", "誰にも見つからない「オブスキュア（名もなき）」な花こそが、世界で最も美しいのです。"),
    ("shadowy", "Shadowy", "影の多い、実体のない", "Old English", "sceadwig (shady)", "Full of shadows", "光があるからこそ生まれる、実体を持たないが故に永遠に傷つくことのない自由な幻影。", "「シャドウイ（影に包まれた）」な路地裏には、大通りにはない特別な魅力が潜んでいます。"),
    ("brilliant", "Brilliant", "光り輝く、見事な", "17th Century", "brillare (to sparkle)", "Exceptionally bright", "ダイヤモンドのように多面的な反射を放ち、他者の追随を許さない圧倒的で完璧な知性。", "あなたの「ブリリアント（見事な）」な才能は、隠そうとしても隙間から光が漏れてしまいます。"),
    ("lustrous", "Lustrous", "光沢のある", "17th Century", "lustre (gloss, radiance)", "Having a shine", "内面から磨き上げられた自信と品格が、なめらかな光沢となって表面を覆っている豊かな輝度。", "丁寧な手入れを受けた「ラストラス（光沢のある）」な家具は、時間そのものが美しく結晶化したものです。"),
    ("radiant", "Radiant", "光を放つ、晴れやかな", "15th Century", "radians (emitting rays)", "Sending out light", "生命の最高潮に達し、内なる太陽が喜びとともに外部へと溢れ出ている至福のオーラ。", "「レイディアント（喜びに満ちて輝く）」な花嫁の姿は、周囲のすべてを幸福で包み込みます。"),
    ("luminous", "Luminous", "光る、明るい", "15th Century", "luminosus (shining, full of light)", "Emitting light", "闇の中でも決して消えることなく、自ら発光して静寂の中に神秘的な空間を創り出す聖なる灯り。", "「ルミナス（ぼんやり光る）」なクラゲの優雅な泳ぎは、深海という宇宙の奇跡です。"),
    ("phosphorescent", "Phosphorescent", "青白く光る、燐光を発する", "18th Century", "phosphorus (light-bringing)", "Emitting light without heat", "熱を伴わずに発光し、生と死の境界線を妖しく彩る、時間を超えて残存する幽霊のような光。", "「フォスフォレッセント（燐光を放つ）」な夜光虫の光跡に、私たちは永遠のロマンを見出します。"),
    ("transparent", "Transparent", "透明な", "15th Century", "transparere (to show light through)", "Allowing light to pass", "隠し事の存在を完全に否定し、向こう側の景色まで歪めずに真っ直ぐ届ける究極の誠実さ。", "「トランスペアレント（透明な）」な嘘をつかずに生きていくことは、人間にとって一番難しい挑戦です。"),
    ("lucid", "Lucid", "明快な、澄んだ", "16th Century", "lucidus (light, bright)", "Expressed clearly", "混濁した狂気や夢から覚醒し、事物の論理と関係性を水のようにクリアに把握している透徹した精神。", "熱が下がった後の「ルーシッド（明快な）」な思考は、かつてないほど鋭利に世界を捉えます。"),
    ("pellucid", "Pellucid", "透明な、明瞭な", "17th Century", "pellucidus (transparent)", "Translucently clear", "一滴の濁りも許さない、水晶の奥底まで見通せるような畏怖さえ感じるほどの極限の純度。", "山の湧き水のように「ペルーシッド（どこまでも澄んだ）」な魂を持つ人は、決して嘘をつきません。"),
    ("glaring", "Glaring", "ぎらぎら光る、目立つ", "16th Century", "glaren (to shine brightly)", "Highly conspicuous", "不快なほどに強烈で、無視したくても無視できない、欠点や痛烈な真実を突きつける残酷な光。", "「グレアリング（ぎらぎらとした）」な間違いは、誰よりも先に自分自身で気づいて直しましょう。"),
    ("blinding", "Blinding", "目をくらませるほどの", "15th Century", "blinden (to make blind)", "So bright as to obscure vision", "感覚の許容量を超えた光によって、逆説的に何も見えなくなる、悟りや狂気に近い強烈な体験。", "「ブラインディング（目の眩むような）」な恋に落ちて、真実が見えなくなってしまわないように。"),
    ("twinkling", "Twinkling", "きらきら光る、瞬く", "14th Century", "twinkelen (to wink, blink)", "Shining with a flickering light", "星や無邪気な瞳が、暗闇の中で「ここにいるよ」とささやき続けるリズミカルな愛のサイン。", "夜空の「トゥインクリング（瞬く）」な星々は、何千光年も昔からあなたにウィンクを送り続けています。"),
    ("hazy", "Hazy", "もやのかかった", "17th Century", "haze (fog, thick mist)", "Covered by a haze", "記憶や視界が熱や霧に覆われ、はっきりとした輪郭を失って白昼夢の中を漂うようなまどろみ。", "真夏の「ヘイジー（もやのかかった）」な蜃気楼の中で、過去の幻想が蘇ります。"),
    ("foggy", "Foggy", "霧の深い、ぼんやりした", "16th Century", "fog (thick mist)", "Full of or characterized by fog", "湿気を含んだ分厚いベールが全方位の視界を遮り、孤独と迷いを強制的に突きつける自然の檻。", "「フォギー（濃霧の）」な日は無理に進もうとせず、足元をしっかり見つめ直すための時間です。"),
    ("misty", "Misty", "かすみのかかった", "Old English", "mistig (misty)", "Full of, covered with, or accompanied by mist", "空気中の細かな水分が光を乱反射させ、世界を悲しげでノスタルジックなヴェールで包み込む優しさ。", "涙で「ミスティ（かすんだ）」な瞳で見る景色は、いつもより少しだけ優しく感じられます。"),
    ("cloudy", "Cloudy", "曇った、不透明な", "Old English", "cludig (rocky, later cloudy)", "Covered with or characterized by clouds", "明確な答えを出さずに、さまざまな思いが複雑に絡み合い、光と影の狭間で揺れ動く優柔不断な心。", "心が「クラウディ（曇り空）」な日でも、雲の向こうには必ず太陽が待っています。決して消えません。"),
    ("blurry", "Blurry", "ぼやけた", "19th Century", "blur (to smear)", "Not clearly visible", "ピントが合わず、形や色が滲み合いながら混ざり合っていく、論理を超えた感情のグラデーション。", "疲れ切った「ブラリー（ぼやけた）」な視界を無理に凝らさず、目を閉じて眠りに落ちて。"),
    ("bleary", "Bleary", "かすんだ、疲れた", "16th Century", "blere (having watery eyes)", "Looking or feeling dull and unfocused", "疲労や悲しみによって目元が重く沈み、現実を直視する気力を搾り取られてしまった痛々しい疲弊状態。", "ひとしきり泣いて「ブリアリー（目の赤い）」な顔になったら、冷たい水で洗い流して出直しましょう。"),
    ("dusky", "Dusky", "薄暗い、浅黒い", "16th Century", "dusk (twilight)", "Darkish in color", "日が沈みかけた空や影のように、完全に闇に呑まれる直前の、最も妖艶で謎めいた魅力を放つ色合い。", "「ダスキー（薄暗がり）」な時間帯は、人々の心の仮面が少しだけ外れるマジックアワーです。"),
    ("twilight", "Twilight", "夕暮れ、薄明かり", "15th Century", "twi- + light (half light)", "Soft glowing light", "昼の喧騒と夜の静寂が交差する、生と死、現実と夢想の境界線が溶け合う魔法の黄昏時。", "人生の「トワイライト（夕暮れ時）」を迎えたとき、過去のすべてが金色に輝き始めます。"),
    ("dawn", "Dawn", "夜明け、黎明", "Old English", "dagian (to become day)", "The first appearance of light", "長く苦しい夜の終わりを告げ、冷たい空気を切り裂いて新しい希望の太陽が顔を出す奇跡の始まり。", "どんなに辛く長い夜の後にも、必ず「ドーン（夜明け）」の光があなたを迎えに来ます。"),
    ("dusk", "Dusk", "夕暮れ", "Old English", "dox (dark, swarthy)", "The darker stage of twilight", "労働の終焉と安息の訪れを静かに告げ、世界がゆっくりとその目を閉じていく穏やかな帰還の時間。", "「ダスク（夕闇）」が世界を包むとき、すべての争いは一時休戦し、家路につくためのチャイムが鳴ります。"),
    ("eclipse", "Eclipse", "日食、月食、影を薄くする", "13th Century", "ekleipsis (abandonment, failing)", "Obscuring of light", "圧倒的な強さを持つ存在が別の存在を完全に覆い隠し、光を奪い去ってしまう抗えない天体のドラマ。", "偉大な先人の「エクリプス（影に隠れる）」にならず、あなた自身の光を放つ場所を探しましょう。"),
    ("silhouette", "Silhouette", "シルエット、影絵", "18th Century", "Étienne de Silhouette (French minister)", "Dark shape and outline", "ディテール（細部）をすべて削ぎ落とし、その存在の最も本質的なフォルム（外枠）だけを浮かび上がらせた影。", "言葉ではなく、背中の「シルエット」だけで全てを語れるような、美しい歳の重ね方をしたいものです。")
]

words = []
for item in words_data:
    root1 = item[4].split(" ")[0]
    meaning1 = " ".join(item[4].split(" ")[1:]).strip("()")
    w = {
        "id": f"{item[0]}_light",
        "word": item[0],
        "meaning": item[2],
        "era": item[3],
        "etymology": {
            "components": [item[4]],
            "original_statement": f"From {item[3]} {item[4]}."
        },
        "concept": item[5] + f" ({item[6]})",
        "thinking": item[6],
        "aftertaste": item[7],
        "example": f"The beautiful {item[0]} caught my eye immediately.",
        "deep_dive": {
            "roots": [{"term": root1, "meaning": meaning1}],
            "points": ["光と闇をどう捉えるかは、私たちの心の状態の投影です。"]
        },
        "part_of_speech": "noun" if "暮れ" in item[2] else "adjective" if "な" in item[2] else "verb"
    }
    words.append(w)

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
if match:
    prefix, json_array_str, suffix = match.groups()
    existing_words = json.loads(json_array_str)
    existing_ids = {w.get("id") for w in existing_words}
    existing_word_texts = set(w.get("word").lower() for w in existing_words)
    
    added = 0
    for w in words:
        if w["id"] not in existing_ids and w["word"].lower() not in existing_word_texts:
            existing_words.append(w)
            added += 1
            existing_word_texts.add(w["word"].lower())
            
    new_content = content[:match.start()] + prefix + json.dumps(existing_words, ensure_ascii=False, indent='\t') + suffix + content[match.end():]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Success: Added {added} words. Theme: Light & Vision (Cycle 4).")
else:
    print("Error parsing data.js")
