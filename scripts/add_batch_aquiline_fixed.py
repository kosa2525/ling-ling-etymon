import json
import re

word_batch = [
    # Cycle 170: Bird & Sky (Refined II)
    {
        "id": "aquiline_bird_fixed",
        "word": "Aquiline",
        "meaning": "ワシのような、(鼻が)ワシ鼻の、勇壮な",
        "era": "17th Century Latin aquila",
        "etymology": {
            "components": ["aquila (eagle)"],
            "original_statement": "From Latin aquilinus (of or pertaining to an eagle), from aquila (eagle)."
        },
        "concept": "Eagle-like (「高所（high place）」から 「全体（whole）」を 「鋭く（sharp）」 見渡し 「一気（one stroke）」に 「確信（certainty）」へと 飛び込むこと)",
        "thinking": "地上（詳細）に 囚われる のではなく、上昇気流（インスピレーション）を 捉えて 高く 舞い上がり（アセンド）、そこから 本質（ターゲット）を 射抜く、威厳ある 知性の 視座. 語源は「ワシ、鷲」. それは 暴力 ではなく あらゆる 葛藤を 俯瞰（ふかん）し、一息に 解決へと 導く 聖なる「決断」の 表現です. 視座は、力です.",
        "aftertaste": "高潔な眼差し. 目の前の 些細な（ささいな）争いに 巻き込まれないで. あなたが「アクイライン（ワシのような）」な 気高さで より高い 精神の 階層へと 舞い上がるとき 全ての 悩みは 小さな 砂粒のように 消え去ってゆくのだから.",
        "example": "His aquiline nose and sharp, penetrating eyes gave him an air of commanding authority.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["Aquila（アクィラ：ワシ座）と同じ。天の 覇者としての 誇り。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "halcyon_bird",
        "word": "Halcyon",
        "meaning": "穏やかな、平和な、幸福な、(伝説の鳥)カワセミ",
        "era": "14th Century Greek halkyon",
        "etymology": {
            "components": ["hals (sea)", "kyon (conceiving)"],
            "original_statement": "From Latin halcyon, from Greek halkyon, a variant of alkyon (kingfisher). According to legend, a bird that nested at sea and churned the waves into a calm."
        },
        "concept": "Sea-calming (「嵐（storm）」の 荒れ狂う 「海（ocean）」の ど真ん中で 「奇跡的（miracle）」な 「静寂（stillness）」を 「現出」させること)",
        "thinking": "外部の 状況が 穏やかである ことではなく、激動の 只中（ただなか）に 在りながら、その 中心に 揺るぎない 平穏と 慈愛を 保持し続ける、聖なる「魂の 治癒力（ちゆりょく）」. 語源は「カワセミ、海で子を成すもの」. それは 逃避 ではなく 世界を 宥め（なだめ） 調和へと 引き戻す 聖なる「祈り」の 表現です. 平穏は、奇跡です.",
        "aftertaste": "静寂の治癒. 逆境の 嵐の中に 独りで 立っているように 感じても 絶望しないで. あなたの 内なる「ハルシオン（カワセミ）」が 翼を 広げ 祈りを 捧げるとき 荒れ狂う 世界は 魔法のように 静まり返り 祝福の 光で 満たされるのだから.",
        "example": "She often reminisced about the halcyon days of her youth, when life seemed simple and full of wonder.",
        "deep_dive": { "roots": [{"term": "al-", "meaning": "to bloom (possible for alkyon)"}], "points": ["冬至（Winter Solstice）の頃の「ハルシオン・デイズ（小春日和）」の伝説。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "pinnate_bird",
        "word": "Pinnate",
        "meaning": "羽状の、羽のある、(葉が)羽状複葉の",
        "era": "18th Century Latin pinna",
        "etymology": {
            "components": ["pinna (feather, wing)"],
            "original_statement": "From Latin pinnatus (feathered, winged), from pinna (feather, wing)."
        },
        "concept": "Feather-like symmetry (「一つ（one）」の 「軸（axis）」から 「無数（infinite）」の 「小さな 翼（small wings）」を 「展開（expand）」し 「飛行（flight）」を 可能にすること)",
        "thinking": "巨大な 一枚の 羽 ではなく、微細な 要素が 完璧な 秩序（フラクタル）を 持って 並び、それらが 協力して 風（チャンス）を 捉える、緻密な 生命の デザイン. 語源は「羽、翼」. それは 孤立 ではなく 個々の 役割が 統合される ことで 初めて 壮大な 飛躍（ジャンプ）が 可能に なるという 聖なる「共同」の 表現です.",
        "aftertaste": "繊細な連帯. 自分の 役割が 小さく 思えても 嘆かないで. あなたが「ピネイト（羽状の）」な 秩序の 一部として 誠実に 自分の 場所で 輝くとき その 連なりは 宇宙を 翔け（かけ）抜ける 巨大な 翼となって 新しい 世界へと 辿り着くのだから.",
        "example": "The fern leaves are characteristically pinnate, displaying a complex and beautiful fractal structure.",
        "deep_dive": { "roots": [{"term": "pet-", "meaning": "to rush, fly"}], "points": ["pen（ペン：羽ペン）や petition（請願：求めること）と同じ。上昇を 志向する 力。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "soar_bird",
        "word": "Soar",
        "meaning": "高く上がる、舞い上がる、急騰する、(精神が)高揚する",
        "era": "14th Century Latin ex- + aura",
        "etymology": {
            "components": ["ex- (out)", "aura (breeze, air)"],
            "original_statement": "From Old French essorer (to fly up), from Vulgar Latin exaurare (to expose to the air), from ex- (out) + aura (breeze, air)."
        },
        "concept": "Out of the breeze (「重力（gravity）」や 「打算（calculation）」を 「脱ぎ捨て（take off）」 「純粋（pure）」な 「上昇（ascent）」そのものに 「魂」を 預けること)",
        "thinking": "羽ばたき（努力）による 上昇 を超え、世界の 巨大な 流れ（風）に 自らを 同調させ、最小限の 抵抗で 高みへと 到達する、聖なる「信頼」の 運動. 語源は「空気に 当てる、外の風へ」. それは 執着 ではなく 自らを 虚（むな）しく することで 初めて 到達できる 精神の 自由な 飛翔の 表現です. 上昇は、委ね（ゆだね）です.",
        "aftertaste": "自由な飛翔. 自分の 羽ばたき だけで 全てを 解決しようと 焦らないで. あなたが「ソア（舞い上がる）」な 信頼を 持って 宇宙の 潮流に 身を 任せたとき あなたは 想像もしなかった 最高の 高みへと 軽やかに 運ばれてゆくのだから.",
        "example": "The eagle began to soar high above the mountains, using the thermal currents to glide effortlessly through the sky.",
        "deep_dive": { "roots": [{"term": "wer-", "meaning": "to lift, raise (possible link for aura)"}], "points": ["aura（オーラ：微風）と同じ。存在の 周囲に 漂う（ただよう） 聖なる 輝き。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "plumage_bird",
        "word": "Plumage",
        "meaning": "羽毛、(集合的に)羽、(派手な)衣装",
        "era": "15th Century Latin pluma",
        "etymology": {
            "components": ["pluma (feather, soft hair)"],
            "original_statement": "From Old French plumage, from Latin pluma (feather, soft hair)."
        },
        "concept": "Feather garment (「冷徹な 真実（cold truth）」を 「美的な 装飾（aesthetic decoration）」で 「保護（protect）」し 「誇り（pride）」を 「顕現」させること)",
        "thinking": "内部を 隠すための 化粧 ではなく、自らの 内なる 尊厳や 生命力が、そのまま 外部へと 結晶（アウトプット）した、聖なる「存在の 輝き」. 語源は「羽毛、柔らかい毛」. それは 虚栄 ではなく 自らが 宇宙の 一部として いかに 美しく 調和しているか（完璧であるか）を 証明するための 聖なる「身だしなみ」の 表現です.",
        "aftertaste: "尊厳の輝き. 自分を 卑下して（ひげして） 地味に 振る舞う（ふるまう） 必要はない. あなたが 自らの「プリュマージュ（羽毛/装い）」としての 才能を 堂々と 披露し 輝くとき 世界はその 美しさに 圧倒され 新しい 時代の 幕開けを 祝福し始めるのだから. ",
        "example": "The peacock displayed its magnificent iridescent plumage to attract a mate during the spring season.",
        "deep_dive": { "roots": [{"term": "pleu-", "meaning": "to flow (possible link for pluma as something fluid and light)"}], "points": ["plume（羽飾り、噴煙）と同じ。空へと 立ち昇る（たちのぼる） 魂の 軌跡。"] },
        "part_of_speech": "noun"
    }
]

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
    if match:
        prefix, json_array_str, suffix = match.groups()
        words = json.loads(json_array_str)
        existing_ids = {w.get("id") for w in words}
        
        added = 0
        for item in word_batch:
            if item["id"] not in existing_ids:
                words.append(item)
                added += 1
        
        new_content = content[:match.start()] + prefix + json.dumps(words, ensure_ascii=False, indent='\t') + suffix + content[match.end():]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Success: Added {added} words in Cycle 170.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
