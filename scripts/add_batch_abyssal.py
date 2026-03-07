import json
import re

word_batch = [
    # Cycle 156: Ocean & Depth (Refined)
    {
        "id": "abyssal_depth",
        "word": "Abyssal",
        "meaning": "深海の、絶望的な、計り知れない、どん底の",
        "era": "17th Century Greek abyssos",
        "etymology": {
            "components": ["a- (without)", "byssos (bottom)"],
            "original_statement": "From Latin abyssus (bottomless pit), from Greek abyssos (bottomless), from a- (without) + byssos (bottom, depth of the sea)."
        },
        "concept": "Bottomless (「光（light）」の 届かない 「極限（limit）」の 深淵において 「純粋な静寂」と 直結すること)",
        "thinking": "表面的な 喧騒を 完全に 断ち切り、宇宙の 根源的な 暗闇（ポーズ）と 同化することで、逆に 全ての 生命の 可能性を 抱卵している、圧倒的な 低周波の 領域. 語源は「底なし」. それは 絶望ではなく 私たちが いかに 深い 精神の 地層を 持っているかという、魂の 巨大さの 証明です.",
        "aftertaste": "深淵の抱擁. 暗闇を 恐れないで. あなたが「アビサル（深海の）」な 静寂の中に 身を委ねるとき 魂は 地上の 摩擦から 解放され 真の 自由と 平穏を 手にするのだから.",
        "example": "The abyssal zone of the ocean remains one of the least explored and most mysterious places on Earth.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["abyss（深淵）の形容詞形。終わりなき 探求のルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "pelagic_ocean",
        "word": "Pelagic",
        "meaning": "遠洋の、外洋の、外洋性の",
        "era": "17th Century Greek pelagos",
        "etymology": {
            "components": ["pelagos (sea)"],
            "original_statement": "From Latin pelagicus, from Greek pelagikos, from pelagos (sea, open sea)."
        },
        "concept": "Of the open sea (「陸地（shore）」の 束縛を 離れ 「無限（infinity）」へと 突き進む 魂の 「遊泳路」)",
        "thinking": "特定の 場所に 留まることなく、広大な 宇宙（海）そのものを 住処（すみか）とし、常に 変化し続ける 流れと 一体化して 生きること. 語源は「海、沖」. それは 狭い 境界線を 捨てて 全体性と 接続しようとする、気高く、果てしない 自由への 憧憬です. 遊泳は、瞑想です.",
        "aftertaste": "外洋の自由. 岸辺の 安全に 固執しないで. あなたが「ペラジック（外洋の）」な 航海へと 漕ぎ出したとき 世界は その広大さを 余すところなく あなたに 開示してくれるのだから.",
        "example": "Pelagic birds like albatrosses can spend months or even years flying over the open ocean without ever touching land.",
        "deep_dive": { "roots": [{"term": "plak-", "meaning": "to be flat, spread out"}], "points": ["plain（平原）や plankton（プランクトン：漂うもの）と同じ。平坦な無限。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "fathom_depth",
        "word": "Fathom",
        "meaning": "測る、見抜く、理解する、(水深を測る単位)",
        "era": "Pre-12th Century Old English fæthm",
        "etymology": {
            "components": ["fæthm (outstretched arms, embrace)"],
            "original_statement": "From Old English fæthm (the length of the outstretched arms, embrace, grasp), from Proto-Germanic fathmaz."
        },
        "concept": "Embracing the depth (「両腕（arms）」を 広げて 「深淵（depth）」を 「抱きしめる（embrace）」ことで その 意味を 理解すること)",
        "thinking": "頭脳で 計算するのではなく、自らの 体を 投げ出し、深淵と 正面から 向き合うことで、その 複雑さや 巨大さを そのまま 受け入れること. 語源は「広げた両腕、抱擁」. それは 知識を 自分の ものにする（理解する）とは 相手を 全力で 愛する（抱きしめる）ことと 同義であるという、聖なる「共感」の 知恵です.",
        "aftertaste": "抱擁의理解. 難しい 理論に 惑わされないで. あなたが 目の前の 出来事を 全身で「ファゾム（抱擁/理解）」しようとするとき 真実は 驚くほど 鮮やかに あなたの 心に 溶け込んでくるのだから.",
        "example": "Try as they might, the scientists could not fathom the true nature of the mysterious signals from space.",
        "deep_dive": { "roots": [{"term": "pet-", "meaning": "to spread"}], "points": ["expand（広がる）や petal（花びら）と同じ。開かれた状態のルーツ。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "thalassic_ocean",
        "word": "Thalassic",
        "meaning": "海の、海洋の、(特に内海や近海の)海洋に関する",
        "era": "19th Century Greek thalassa",
        "etymology": {
            "components": ["thalassa (sea)"],
            "original_statement": "From Greek thalassa (sea), of uncertain origin (possibly Pre-Greek)."
        },
        "concept": "Of the inner sea (「自己（self）」の 内側に 広がる 「内海（inner sea）」のように 温かく 交わりを 「育む」 領域)",
        "thinking": "荒々しい 外洋 ではなく 私たちの 暮らしや 感情に 寄り添い、常に 反射と 変容を 繰り返している、近しい 海の 質感. 語源は「海（ギリシャ語）」. それは 遠い 神秘 ではなく 今、ここにある 命の 源泉（母なる海）への 尽きることのない 感謝と 接続の 表現です.",
        "aftertaste": "母なる海. 孤独な 砂漠に 留まらないで. あなたの内なる「タラシック（海の）」な 豊かさを 思い出すことで 魂は いつでも 潤いと 輝きを 取り戻すことができるのだから.",
        "example": "The Mediterranean is a prime example of a thalassic environment that has shaped human civilization for millennia.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["Thalassa（タラッサ：ギリシャの海の女神）の名を冠する。女性的な包容力。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "estuary_ocean",
        "word": "Estuary",
        "meaning": "河口、(潮の差がある)入り江",
        "era": "16th Century Latin aestuarium",
        "etymology": {
            "components": ["aestus (tide, surge, heat)"],
            "original_statement": "From Latin aestuarium (tidal inlet, marsh), from aestus (tide, surge, heat, boiling)."
        },
        "concept": "Tidal boiling (「真水（pure river）」と 「塩水（salt sea）」が 「沸き立って（boil）」 混ざり合い 豊穣な 「生命」を 産み出す 汽水域)",
        "thinking": "純粋であること（一つの色）に 固執せず 異質なものが 激しく 交じり合うことで 生まれる、圧倒的な 活力と 創造の カオス. 語源は「潮の満ち引き、沸騰、熱」. それは 静止した 安定 ではなく 常に 揺らぎ、沸き立つ 境界線こそが 最も 豊かな 命を 育むという、宇宙の 逆説的な 心理の 隠喩です.",
        "aftertaste": "交わりの沸騰. 自分の 純真さを 守るために 閉じこもらないで. あなたが「エスチュアリー（河口）」のように 異質な他者と 激しく 交じり合うとき その熱の中から 想像もしなかった 壮大な 豊かさが 芽生えるのだから.",
        "example": "The Thames estuary is a vital habitat for countless species of wading birds and marine life.",
        "deep_dive": { "roots": [{"term": "aidh-", "meaning": "to burn"}], "points": ["edifice（大建築物：火を焚く場所）や ether（エーテル：輝く上層気）と同じ。熱という名の、変容のエナジー。"] },
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
        print(f"Success: Added {added} words in Cycle 156.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
