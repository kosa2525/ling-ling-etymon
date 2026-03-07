import json
import re

word_batch = [
    # Cycle 160: Web & Entanglement (Refined)
    {
        "id": "reticulate_web",
        "word": "Reticulate",
        "meaning": "網目状の、網目を作る、絡み合った",
        "era": "16th Century Latin rete",
        "etymology": {
            "components": ["rete (net)"],
            "original_statement": "From Latin reticulum (small net), diminutive of rete (net)."
        },
        "concept": "Net-like structure (「個（individual）」が 「糸（thread）」となって 「他者（others）」と 「交差（cross）」し 合うことで 巨大な 「知（wisdom）」を 織り上げること)",
        "thinking": "孤立した 点 ではなく、無数の 交点（ノード）を 持つ ネットワークとして 世界を 捉えること. 語源は「小さな網」. それは 偶然の 出会い ではなく 必然的な 繋がりによって 宇宙の 複雑な 模様が 描き出されているという、聖なる「連関」の 表現です. 網目は、力です.",
        "aftertaste": "連関の網目. 一人で 全てを 背負い込まないで. あなたが「レティキュレイト（網目状の）」な 意識で 誰かと 手を取り合うとき その 繋がりの中から 想像もしなかった 壮大な 智慧が 湧き上がってくるのだから.",
        "example": "The leaves of the plant had a beautiful reticulate vein pattern, directing nutrients to every cell.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["reticle（照準線：網目）や retina（網膜：光を捉える網）と同じ。情報を 収集する 仕組み。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "imbricate_web",
        "word": "Imbricate",
        "meaning": "重なり合った、鱗状に重なる、(屋根瓦のように)並べる",
        "era": "17th Century Latin imbrex",
        "etymology": {
            "components": ["imbrex (roof tile)", "imber (rain)"],
            "original_statement": "From Latin imbricatus, from imbrex (a hollow roof tile for shedding rain), from imber (a rain shower)."
        },
        "concept": "Overlapping tiles (「過去（past）」の 経験を 「瓦（tile）」のように 「重ね合わせ（overlap）」 魂の 「屋根（protection）」を 築くこと)",
        "thinking": "バラバラに 存在する 経験 を、隙間なく（シームレスに）重ね合わせることで、外部からの 攻撃（雨）を 防ぎ、内側の 温もりを 守り抜く、聖なる「積み重ね」の 営み. 語源は「雨除けの瓦」. それは 連続した 時間が 織りなす 圧倒的な 層（レイヤー）の 美しさであり 私たちが 歴史の 一部であることを 実感する アクションです.",
        "aftertaste": "積み重ねの守護. 日々の 小さな 努力を 軽んじないで. それらが「インブリケイト（重なり合った）」な 瓦となって あなたの 魂を 守る 頑丈な 屋根を 築き上げ、どんな 嵐からも あなたを 守り抜くのだから.",
        "example": "The scales of the pangolin are imbricate, providing a nearly impenetrable armor against predators.",
        "deep_dive": { "roots": [{"term": "emb-", "meaning": "moisture, rain (for imber)"}], "points": ["imbue（染み込ませる）と同じ。恵みの雨と共にある、守りの形。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "plexus_web",
        "word": "Plexus",
        "meaning": "(血管や神経の)網、叢(くさむら)、錯綜",
        "era": "17th Century Latin plectere",
        "etymology": {
            "components": ["plectere (to plait, weave)"],
            "original_statement": "From Latin plexus (a weaving, plaiting), from plectere (to plait, weave, braid)."
        },
        "concept": "Braided network (「情報（information）」と 「生命（life）」が 「複雑（complex）」に 「絡み合い（braid）」 意志の 「中枢（center）」を 形成すること)",
        "thinking": "直線的な 伝達 ではなく 複数の 流れが 縺れ（もつれ）合い、一つの 新しい 力や 意味を 生成する、生命の 深奥にある ネットワーク. 語源は「織ること、編むこと」. それは 私たちの 精神が 孤独な 思考 ではなく 無数の インスピレーションが 編み合わされた 聖なる「叢（くさむら）」であることの 表現です.",
        "aftertaste": "錯綜の知性. 複雑であることに 混乱しないで. あなたの 内なる「プレクサス（網）」が あらゆる 経験を 編み合わせてゆくとき そこには 唯一無二の 壮大な 智慧の 織物が 完成してゆくのだから.",
        "example": "The solar plexus is a complex network of nerves located in the abdomen, often called the 'second brain'.",
        "deep_dive": { "roots": [{"term": "plek-", "meaning": "to plait"}], "points": ["complex（複雑な：共に編まれた）や multiply（倍にする：折り畳む）と同じ。重層性のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "tangle_web",
        "word": "Entangle",
        "meaning": "絡ませる、巻き込む、困らせる",
        "era": "16th Century Middle English en- + tangle",
        "etymology": {
            "components": ["en- (in, into)", "tangle (seaweed)"],
            "original_statement": "From en- + tangle, probably of Scandinavian origin (related to seaweed or twisted mass)."
        },
        "concept": "Into the seaweed (「自由な意志（free will）」が 「運命（destiny）」の 「海藻（seaweed）」に 「囚われ（catch）」 深い 繋がりを 結ぶこと)",
        "thinking": "表面的な 交わり ではなく 自らが 世界の 複雑な 構造の中に 深く 埋没し、他者と 切り離せない 関係に なってしまうこと. 語源は「海藻の中へ」. それは 厄介な 事態 ではなく 私たちが 独りでは 生きられず 世界という 巨大な 生命の 循環の中に 組み込まれているという 聖なる「絆」の 逆説的な 表現です. 絡み合いは、愛です.",
        "aftertaste": "絆の深淵. 誰かと 深く 関わることを 恐れないで. あなたが 他者の 人生と「エンタングル（絡み合う）」とき そこには 孤独を 越えた 聖なる 一体感が 芽生え 人生は 潤いと 輝きを 宿すのだから.",
        "example": "He found himself entangled in a complex legal dispute that took years to resolve.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["quantum entanglement（量子もつれ）という 宇宙の 究極の 繋がりの 名にも 冠されている。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "texture_web",
        "word": "Texture",
        "meaning": "質感、手触り、きめ、構造、筋合い",
        "era": "15th Century Latin texere",
        "etymology": {
            "components": ["texere (to weave)"],
            "original_statement": "From Latin textura (a web, texture, construction), from textus, past participle of texere (to weave)."
        },
        "concept": "Woven result (「無数の糸（countless threads）」が 「交差（cross）」した 「結果（result）」として 現れる 固有の 「手触り」)",
        "thinking": "見かけの 形 ではなく その 表面の デコボコや 微細な 重なり合いが 産み出す、独特の 存在の 質感. 語源は「織ること、構築すること」. それは 人生の 一つ一つの 経験（糸）が 誠実に 編み合わされた 証拠であり 私たちが どんな 魂の 織物（テキスト）を 綴って（つづって）きたかという 聖なる「履歴」の 表現です.",
        "aftertaste": "存在の手触り. 効率ばかりを 求めないで. あなたが 丁寧に 日々の 糸を 紡ぎ（つむぎ）「テクスチャー（質感）」を 豊かに していくことで あなたの 存在は 誰にも 真似できない 唯一無二の 輝きを 放つように なるのだから.",
        "example": "The composer used a variety of instruments to create a rich polyphonic texture in his music.",
        "deep_dive": { "roots": [{"term": "teks-", "meaning": "to weave, fabricate"}], "points": ["text（文章：織り上げられたもの）や technology（技術：織る力）と同じ。文明のルーツ。"] },
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
        print(f"Success: Added {added} words in Cycle 160.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
