import json
import re

word_batch = [
    # Cycle 164: Stone & Time (Refined)
    {
        "id": "monolith_stone",
        "word": "Monolith",
        "meaning": "一本石、モノリス、(社会などの)一枚岩的な組織",
        "era": "19th Century Greek monos + lithos",
        "etymology": {
            "components": ["monos (single, alone)", "lithos (stone)"],
            "original_statement": "From French monolithe, from Greek monolithos (made of a single stone), from monos (single, alone) + lithos (stone)."
        },
        "concept": "Single stone (「多（many）」を 「一（one）」へと 「統合（integrate）」し 「永遠（eternity）」の 「普遍性」を 確立すること)",
        "thinking": "散文的な 断片 ではなく、継ぎ目のない（シームレスな）巨大な 一つの 意思として 世界に 屹立し（きつりつし）、流れる 時間に 左右されない 圧倒的な 存在感を 示すこと. 語源は「一つの石」. それは 孤立 ではなく 揺るぎない 密度によって 宇宙の 記憶を 繋ぎ止める 聖なる「楔（くさび）」の 表現です. 重厚さは、真実です.",
        "aftertaste": "永遠の一枚岩. バラバラの 現象に 惑わされないで. あなたが 自らの 想いを「モノリス（一本石）」のような 一貫した 意思へと 鍛え上げたとき その存在は 時代の 荒波を 越えて 永遠に 語り継がれる 輝きを 宿すのだから.",
        "example": "The mysterious black monolith stood silently in the middle of the desert, defying all attempts at explanation.",
        "deep_dive": { "roots": [{"term": "men-", "meaning": "single, alone (for monos)"}], "points": ["lithosphere（岩石圏）と同じ。大地の 土台を 形成する 究極の 安定。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "petrify_stone",
        "word": "Petrify",
        "meaning": "石化させる、(恐怖などで)すくませる、硬直させる",
        "era": "16th Century Latin petra + facere",
        "etymology": {
            "components": ["petra (rock, stone)", "facere (to make)"],
            "original_statement": "From Middle French petrifier, from Latin petra (rock, stone) + facere (to make)."
        },
        "concept": "Making stone (「動的（dynamic）」な 「生命（life）」を 「静止（stillness）」した 「知恵の結晶」へと 変容させ 「永遠」に 留めること)",
        "thinking": "単なる 硬直 ではなく、溢れ出す 感情や 記憶を 石という名の 「普遍的な 記録媒体」へと 移し替えることで 腐敗（忘却）を 免れ 宇宙の 記憶の 一部と させること. 語源は「石にすること」. それは 恐怖 ではなく 瞬間的な 美を 永遠の 彫像へと 昇華させようとする 聖なる「保存」の アクションです. 凍結は、祈りです.",
        "aftertaste": "永遠の凍結. 移ろいゆく 世界の 儚さに 絶望しないで. あなたが 感動の 瞬間を「ペトリファイ（石化/結晶化）」するように 心に 刻んでおくとき その 美しさは 時を 越えて いつまでも あなたを 励まし続けるのだから.",
        "example": "The ancient forest was petrified millions of years ago, turning the wood into colorful stone jewels.",
        "deep_dive": { "roots": [{"term": "per-", "meaning": "to pass through (possible link for petra)"}], "points": ["Peter（ピーター：岩の人）や petroleum（石油：岩の油）と同じ。根源的な 硬度のルーツ。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "lapidary_stone",
        "word": "Lapidary",
        "meaning": "宝石細工の、刻明な、(文体などが)簡潔で格調高い",
        "era": "14th Century Latin lapis",
        "etymology": {
            "components": ["lapis (stone, pebble)"],
            "original_statement": "From Latin lapidarius (of or belonging to stone), from lapis (stone)."
        },
        "concept": "Work of stone (「粗削り（rough）」の 「原石（truth）」を 「粘り強い 研磨（polishing）」に よって 「透徹（clarity）」した 「結晶」に 導くこと)",
        "thinking": "言葉を 費やす 饒舌（じょうぜつ）を 恥じ、贅肉（ぜいにく）を 削ぎ落とし、ただ 一つの 本質的な 輝きだけを 際立たせる、極限の 知性の 選別術. 語源は「石の、宝石細工の」. それは 虚飾 ではなく 叩かれ 磨かれる（研鑽）ことでのみ 辿り着ける 聖なる「純粋さ」と 尊厳の 表現です. 簡潔さは、光です.",
        "aftertaste": "研磨の叡智. 未完成の 自分を 嘆かないで. あなたが 経験という砥石で 自分を「ラピダリー（宝石細工の）」な 忍耐で 磨き続けるとき あなたの 魂は どんな 鉱石よりも まばゆい 真実の 輝きを 放つように なるのだから.",
        "example": "He was known for his lapidary style, able to express profound truths in the fewest possible words.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["lapis lazuli（ラピスラズリ：青い石）と同じ。天の色を宿す、大地の結晶。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "immutable_stone",
        "word": "Immutable",
        "meaning": "不変の、変わらない、不磨の",
        "era": "15th Century Latin in- + mutare",
        "etymology": {
            "components": ["in- (not)", "mutare (to change)"],
            "original_statement": "From Latin immutabilis (unchangeable), from in- (not) + mutabilis (changeable), from mutare (to change)."
        },
        "concept": "Not changeable (「流動（flow）」する 「時（time）」の 荒波に 曝され（さらされ）て なお 「真理」としての 「核」を 断固として 維持し続けること)",
        "thinking": "流行や 他人の 評価に 左右されず、自らの 内側にある 普遍的な 価値（センター）を 信じ抜き、何世紀 も 変わらない 山のように 静かに 存在し続けること. 語源は「変えられない」. それは 頑固 ではなく 時代を 超えて 響き合う 聖なる「不変（エターナル）」への 誠実な 誓いです. 不変は、愛です.",
        "aftertaste": "不変の誓い. 移り変わる 世界の 速度に 焦らないで. あなたが「イミュータブル（不変の）」な 真実を 自分の 核（センター）に 置けたとき あなたは どんな 激動の中でも 決して 揺らぐことのない 平穏を 手にするのだから.",
        "example": "The laws of mathematics are considered immutable, remaining true regardless of the passage of time or culture.",
        "deep_dive": { "roots": [{"term": "mei-", "meaning": "to change, move, go"}], "points": ["mutual（相互の：交換する）や mutation（突然変異）と同じ。変化への 抵抗という名の、存在の 証。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "megalith_stone",
        "word": "Megalithic",
        "meaning": "巨石の、巨石文化の、(社会などが)巨大で変化の乏しい",
        "era": "19th Century Greek megas + lithos",
        "etymology": {
            "components": ["megas (great, large)", "lithos (stone)"],
            "original_statement": "From mega- (great) + lithic (of stone)."
        },
        "concept": "Great stone (「個（individual）」を 越えた 「巨大な 意思（great will）」が 「大地（earth）」に 刻みつけた 「不滅（immortal）」の 叙事詩)",
        "thinking": "一人の 人間の 生涯を 遥かに 越える スケールで 構想され、何世代 もの 祈りと 労働が 結実して 産み出された、圧倒的な 崇高美（サブリミティ）. 語源は「大きな石」. それは 物理的な 重さ ではなく 私たちが 宇宙的な 時間の 中で いかに 壮大な 物語を 紡ごうとしてきたか（紡いできたか）という 聖なる「挑戦」の 表現です.",
        "aftertaste": "巨石の叙事詩. 自分の 非力さに 絶望しないで. あなたの 放つ 小さな祈りが「メガリシック（巨石の）」な 意思の 連鎖の中に 組み込まれたとき それは 永遠に 消えることのない 聖なる 碑（いしぶみ）と なって 世界に 刻まれるのだから.",
        "example": "Stonehenge is perhaps the most famous megalithic monument in the world, its true purpose still debated by scholars.",
        "deep_dive": { "roots": [{"term": "meg-", "meaning": "great"}], "points": ["magnify（拡大する）や master（巨匠）と同じ。偉大さという名の、精神の地平。"] },
        "part_of_speech": "adjective"
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
        print(f"Success: Added {added} words in Cycle 164.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
