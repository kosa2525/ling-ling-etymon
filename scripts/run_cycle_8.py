import json
import re

words_data = [
    ("drizzle", "Drizzle", "霧雨、しとしと降る雨", "16th Century", "drysian (to fall in drops)", "Light rain", "存在を主張しないほど微細な水滴が、世界を音もなく優しく包み込む穏寂のベール。", "「ドリズル（細かい雨）」の中を傘なしで歩くのも、時々は心が洗われる素敵な体験です。"),
    ("shower", "Shower", "にわか雨", "Old English", "scur (short fall of rain)", "A brief and usually light fall of rain", "突如として訪れるが長引くことはなく、空気を一気に洗い流して去っていく短気な訪問者。", "突然の「シャワー（にわか雨）」に降られても、その後には必ず美しい虹がかかるはず。"),
    ("downpour", "Downpour", "土砂降り", "19th Century", "down + pour", "A heavy fall of rain", "天がバケツをひっくり返したように、容赦なく地上の全てを洗い流そうとする圧倒的な滝。", "激しい「ダウンポア（土砂降り）」の音が、皮肉にも一番心地よい眠りを誘ってくれます。"),
    ("deluge", "Deluge", "大洪水、豪雨", "14th Century", "diluvium (flood)", "A severe flood", "世界の全てを一瞬にして水の底へ沈め、既存の秩序を強制的に初期化してしまう神の怒り。", "仕事の「デリュージ（氾濫）」に溺れる前に、誰かに助けを求めるボートを出して。"),
    ("blizzard", "Blizzard", "猛吹雪", "19th Century", "blizz (violent blow)", "A severe snowstorm", "視界だけでなく、方向感覚や体温までも真っ白な暴力で奪い去ろうとする氷の息吹。", "「ブリザード（猛吹雪）」のような逆境では、無理に進まず、じっと立ち止まる強さも必要です。"),
    ("hail", "Hail", "ひょう、あられ", "Old English", "hægel (hail)", "Pellets of frozen rain", "冬の厳しい寒さが硬い氷の石となり、空から弾丸のように容赦なく地上を打ち付ける砲撃。", "屋根を打つ「ヘイル（ひょう）」の音は、あなたが今、安全な場所にいるという証明です。"),
    ("sleet", "Sleet", "みぞれ", "14th Century", "slete (sleet)", "Rain containing some ice", "雨と雪が互いに妥協し合えず、中途半端に凍りついて中空を漂う、冷たく哀しい結晶の未完成形。", "「スリート（みぞれ）」の降る日は、外出しなくていいという宇宙の優しさかもしれません。"),
    ("squall", "Squall", "突風、スコール", "17th Century", "squall (sudden violent wind)", "A sudden violent gust of wind", "海賊のように突如として現れ、海面を荒らし回っては一瞬にして消えていく通り魔のような風。", "人生には「スコール（突然の嵐）」が付き物。焦らず雨宿りして通り過ぎるのを待ちましょう。"),
    ("gust", "Gust", "突風", "16th Century", "gustr (blast of wind)", "A brief, strong rush of wind", "大気が深く鋭く息を吐き出し、瞬間的に木々を大きく揺さぶって見せる力強い気まぐれ。", "予期せぬ「ガスト（突風）」に帽子を飛ばされたら、それを追いかける新しい冒険の始まりです。"),
    ("draft", "Draft", "すき間風、通風", "Middle English", "draught (drawing of a bow, pulling)", "A current of unpleasantly cold air", "堅牢な部屋のわずかな隙間を見つけ出し、蛇のように這い込んでくる冷たく細い空気の侵入者。", "心の隙間に「ドラフト（すき間風）」を感じたら、温かい言葉の毛布で自分を包んであげて。"),
    ("breeze", "Breeze", "そよ風", "16th Century", "briza (north wind)", "A gentle wind", "頬を優しく撫で、春の訪れや花の香りを囁くように（ささやくように）伝えてくれる目に見えない精霊。", "柔らかい「ブリーズ（そよ風）」に身を委ね、深刻な悩み事を一旦空へ飛ばしてしまいましょう。"),
    ("gale", "Gale", "強風、大風", "16th Century", "gal (crazy, bad)", "A very strong wind", "狂気をはらんだ不可視の壁が猛スピードで押し寄せ、立っていることすら許さない大気の威圧。", "「ゲイル（強風）」に向かって進むのは困難ですが、背に受ければどこまでも早く高く飛べます。"),
    ("typhoon", "Typhoon", "台風", "16th Century", "tai fung (great wind)", "A tropical storm in the region of the Indian or western Pacific oceans", "莫大な熱エネルギーを吸い上げて巨大な螺旋を描き、全てを破壊しながら浄化していく荒ぶる海の神。", "どんなに激しい「タイフーン（台風）」の中心にも、必ず静寂で無風の『目』が存在しています。"),
    ("hurricane", "Hurricane", "ハリケーン", "16th Century", "huracan (god of the storm)", "A storm with a violent wind", "カリブ海で生まれた暴風の神が、海を越え、陸を削り取るほどのエネルギーで暴れ回る恐怖の渦。", "「ハリケーン（暴風雨）」が過ぎ去った後に残る澄み切った空、それこそが真の希望です。"),
    ("cyclone", "Cyclone", "サイクロン、大竜巻", "19th Century", "kukloma (wheel, coil of a snake)", "A system of winds rotating inward", "大気が蛇のような巨大な車輪を作り出し、回転しながら無差別に地上の全てを飲み込んでいく破壊の竜。", "怒りで「サイクロン（渦巻き）」のように荒れ狂う心を、深く静かな呼吸で真っ直ぐに解きほぐして。"),
    ("tornado", "Tornado", "竜巻", "16th Century", "tronada (thunderstorm)", "A mobile, destructive vortex", "空から垂れ下がった破壊の漏斗（ろうと）が、大地を抉りながら不規則に踊り狂う狂気の独楽（こま）。", "突然の「トルネード（竜巻）」のように全てが変わってしまっても、あなた自身の芯は決して飛ばされません。"),
    ("whirlwind", "Whirlwind", "旋風、つむじ風", "Middle English", "whirl + wind", "A column of air moving rapidly around and around", "予測不可能な軌道を描いて駆け抜け、平穏な日常を一瞬のうちにドラマに変える慌ただしい風。", "彼女は「ワールウィンド（つむじ風）」のように現れ、私の心を完全にさらっていきました。"),
    ("maelstrom", "Maelstrom", "大渦巻き、大混乱", "17th Century", "mälen (grind) + strom (stream)", "A powerful whirlpool", "巨大な臼（うす）を回すように、船も人も希望も全てを海底の底知れぬ恐怖へと力強く引きずり込む魔の渦。", "感情の「メールストロム（大混乱）」に飲み込まれないよう、自分自身という錨をしっかり下ろして。"),
    ("vortex", "Vortex", "渦流、旋風", "17th Century", "vertere (to turn)", "A mass of whirling fluid or air", "中心へ向かって全てを吸い寄せ、回転を加速させながら世界を次元の彼方へ導こうとする数学的で美しい引力。", "神秘的な「ボルテックス（渦）」の中心には、時空を超えるエネルギーの通り道があると信じられています。"),
    ("thunder", "Thunder", "雷鳴、雷", "Old English", "thunor (thunder)", "A loud rumbling or crashing noise heard after a lightning flash", "光の後から少し遅れてやってくる、空を引き裂き、地を震わせる神々の怒りの巨大な太鼓の音。", "「サンダー（雷鳴）」が轟く夜は、恐れるのではなく、地球の巨大なエネルギーのコンサートを楽しみましょう。"),
    ("lightning", "Lightning", "稲妻、雷光", "14th Century", "lightnen (to make bright)", "The occurrence of a natural electrical discharge of very short duration", "天のキャンバスに一瞬だけ描かれ、暗闇を暴力的なまでに白日の下に曝け出す電気と光の奇跡の奔流。", "あなたの「ライトニング（稲妻のような）」ひらめきが、この停滞した会議に新しい次元をもたらすはず。"),
    ("bolt", "Bolt", "稲妻、ボルト、急に飛び出す", "Old English", "bolt (arrow)", "A flash of lightning", "天から地上へと一直線に射ち込まれる、絶対的な精度とスピードを持った光の矢の直撃。", "「ボルト（雷の一撃）」に打たれたような衝撃的な出会いが、平凡な人生をドラマチックに変えます。"),
    ("strike", "Strike", "打つ、襲う、ストライク", "Old English", "strican (to pass lightly over, stroke)", "Hit forcibly and deliberately", "圧倒的な力が一点に集中し、明確な意志を持って標的を破壊し、瞬時に沈黙させる暴力的な着弾。", "チャンスという雷がいつ「ストライク（直撃）」してもいいように、自分自身という避雷針を高く磨いておいて。"),
    ("tempest", "Tempest", "大嵐", "13th Century", "tempus (time, season)", "A violent windy storm", "時や季節の神が引き起こした、大気と海が一体となって荒れ狂う、シェイクスピアの悲劇のような壮大なドラマ。", "「テンペスト（嵐）」の中で翻弄されているように感じても、あなたは必ず無事に生還できる強さを秘めています。"),
    ("overcast", "Overcast", "雲で覆われた、どんよりした", "14th Century", "over + cast (thrown over)", "Clouded over", "空全体に灰色の毛布が投げ掛けられ、地上から一切の影と鋭い光を隠蔽した曖昧で憂鬱なベール。", "「オーバーキャスト（どんよりした）」な日は、日焼けを気にせずのんびりと庭で読書を楽しめる日です。"),
    ("clearing", "Clearing", "（森の）空き地、晴れ間", "15th Century", "clear + ing", "An open space in a forest", "鬱蒼（うっそう）とした森や雲の中に突如として開かれた、太陽の光が特別に許された安全で明るい広間。", "真っ暗な森の「クリアリング（切り開かれた空き地）」を見つけた時の安堵は、苦しい受験を終えた時の喜びに似ています。"),
    ("sunny", "Sunny", "晴れた、太陽のように明るい", "Old English", "sunne (sun)", "Bright with sunlight", "雲一つなく、地球全体が無条件の愛と祝福の光によって隅々まで温められている至福の状態。", "「サニー（陽気でのんき）」なあなたの笑顔さえあれば、外がどんなに土砂降りでも私の心は晴れ渡ります。"),
    ("bright", "Bright", "明るい、輝かしい", "Old English", "beorht (bright)", "Giving out or reflecting a lot of light", "闇を完全に払拭し、世界の細部までを希望の色で鮮明に照らし出す、未来への絶対的な肯定の光。", "あなたの「ブライト（賢く輝かしい）」な未来を、他の誰の暗い予想によっても曇らせてはいけません。"),
    ("balmy", "Balmy", "穏和な、さわやかな", "16th Century", "balm (aromatic resin)", "Characterized by pleasantly warm weather", "心を癒やす香油（バルサム）のように柔らかく、傷ついた魂を優しく撫でて治癒するような心地よい温かさ。", "「バルミー（香るように穏やかな）」な春の夜風は、恋人たちの囁きに最も似合うBGMです。"),
    ("muggy", "Muggy", "蒸し暑い", "18th Century", "muggy (damp, mild)", "Unpleasantly warm and humid", "空気に過剰な水分がへばりつき、まるで目に見えない熱帯魚の水槽の中を歩かされているような不快な重苦しさ。", "「マギー（じっとりと蒸し暑い）」な空気をエアコンで一掃した時のあの快感は、夏の密かな楽しみです。"),
    ("humid", "Humid", "湿気のある", "16th Century", "humere (to be moist)", "Marked by a relatively high level of water vapor in the atmosphere", "大気が水分を限界まで含んで膨張し、肌を濡らすことなく肺の底まで重く沈み込んでくる不可視の水の圧力。", "「ヒューミッド（湿度の高い）」な日は肌が潤うのだから、天然のエステだと割り切って楽しんでしまいましょう。"),
    ("sultry", "Sultry", "蒸し暑い、官能的な", "16th Century", "swelter (to be overcome by heat)", "Hot and humid", "強烈な熱と湿度が絡み合い、息苦しさの向こう側に人を狂わせるような気怠い（けだるい）情熱と官能を引き起こす重さ。", "ジャズの流れる「サルトリー（熱く気怠い）」な夜のバーで、冷たいカクテルを傾ける大人の静かな時間。"),
    ("sweltering", "Sweltering", "うだるように暑い", "16th Century", "swelter (faint with heat)", "Uncomfortably hot", "太陽が地上を容赦なくオーブンの中のように熱し、理性も体力も限界まで溶かしてしまいそうな茹で上がる酷暑。", "「スウェルタリング（うだるように熱い）」な真昼は外に出ず、冷たいスイカを食べて涼むのが最も賢い選択です。"),
    ("scorching", "Scorching", "焼け付くような", "15th Century", "scorchen (burn on the surface)", "Very hot", "皮膚を直接炎で炙られているかのように、激しい熱と痛みを伴って全てを極度に乾燥させていく太陽の暴力。", "「スコーシング（焦げるほど熱い）」な砂浜を裸足で駆けて海へ飛び込む瞬間の、あの圧倒的な爽快感。"),
    ("blistering", "Blistering", "水ぶくれができるほど熱い、猛烈な", "16th Century", "blister", "Intense, extreme heat", "少しでも触れれば皮膚に水疱（みずぶくれ）ができるほど、表面を破壊し尽くす超高温や強烈なスピードの極限。", "「ブリスタリング（猛烈な）」な日差しから肌を守るように、他人の鋭すぎる言葉からも自分の心を守って。"),
    ("biting", "Biting", "身を切るように冷たい、辛辣な", "Old English", "bitan (to bite)", "Painfully cold", "冬の冷たい風が物理的な牙を持ち、厚着の隙間をくぐり抜けて直接皮膚を噛みちぎるような鋭い痛覚。", "彼のごまかしのない「バイティング（刺すような）」な批評は時に痛いですが、一番信頼できる声なのです。"),
    ("piercing", "Piercing", "身を刺すような、鋭い", "14th Century", "percer (to pierce)", "Seeming to cut through one", "極小の冷たさや甲高い音が、耳から脳の奥深くまで一瞬で貫通し、全ての機能を麻痺させる鋭利な針の攻撃。", "真冬の「ピアシング（骨まで突き刺さるような）」な寒さの中に見る満天の星空の美しさは、痛みを忘れさせます。"),
    ("freezing", "Freezing", "凍えるほど寒い", "Old English", "freosan (turn to ice)", "Below 0°C", "時間が停止し、生命の活動の全てが硬い氷の中へ閉じ込められ、世界が完全に静寂のガラスに変わる瞬間。", "「フリージング（凍てつくような）」な外から帰り、暖炉の前で飲むホットココアは人生の小さな奇跡の一つ。"),
    ("frigid", "Frigid", "極寒の、冷淡な", "15th Century", "frigidus (cold)", "Very cold in temperature", "ただ寒いだけでなく、他者を一切寄せ付けず、温もりを与えようとする情熱がない、厳しく冷酷な絶対零度の孤立。", "彼の「フリジッド（極めて冷淡）」な態度の裏側には、誰にも知られたくない傷ついた子供の心が隠れています。")
]

words = []
for item in words_data:
    root1 = item[4].split(" ")[0]
    meaning1 = " ".join(item[4].split(" ")[1:]).strip("()")
    w = {
        "id": f"{item[0]}_weather",
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
        "example": f"The weather suddenly turned {item[0]}.",
        "deep_dive": {
            "roots": [{"term": root1, "meaning": meaning1}],
            "points": ["気候の変化は、そのまま私たちの魂の激しさと静けさに対応します。"]
        },
        "part_of_speech": "noun" if item[0] in ["drizzle","shower","downpour","deluge","blizzard","hail","sleet","squall","gust","draft","breeze","gale","typhoon","hurricane","cyclone","tornado","whirlwind","maelstrom","vortex","thunder","lightning","bolt","strike","tempest","clearing"] else "adjective"
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
    print(f"Success: Added {added} words. Theme: Weather (Cycle 8).")
else:
    print("Error parsing data.js")
