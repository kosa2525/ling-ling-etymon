import json
import re

word_batch = [
    # Cycle 151: Stone & Time (Refined)
    {
        "id": "monolith_stone",
        "word": "Monolith",
        "meaning": "一本石、独石、巨大な一枚岩、巨大な組織",
        "era": "19th Century Greek monos + lithos",
        "etymology": {
            "components": ["monos (single)", "lithos (stone)"],
            "original_statement": "From French monolithe, from Greek monolithos (made of a single stone), from monos (single, alone) + lithos (stone)."
        },
        "concept": "Single stone (「分裂（division）」を 拒み 「唯一無二（unique）」の 威厳を 持って 「永遠（eternity）」に 立ち続けること)",
        "thinking": "周囲の流行や 時代の変化に 左右されず、ただ一本の石として、強固な意志と 静寂を 守り抜き、風景の絶対的な中心となること. 語源は「一つの石」. それは 脆（もろ）い 人間の営みを超越した、宇宙的な 耐久性と 普遍性の 象徴です. 静止は、勝利です.",
        "aftertaste": "不動の尊厳. 周囲に合わせて 自分を 切り刻まないで. あなたが「モノリス（一本石）」のような 揺るぎない 芯を持つとき 世界はあなたの 静寂の中に 真実の強さを 見出すのだから.",
        "example": "The mysterious black monolith stood silently in the desert, reflecting the ancient light of the stars.",
        "deep_dive": { "roots": [{"term": "lith-", "meaning": "stone"}], "points": ["lithography（石版画）や megalith（巨石）と同じ。文明を形作る、重厚な素材。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "petrify_stone",
        "word": "Petrify",
        "meaning": "石化させる、(恐怖で)すくませる、(考えを)硬直させる",
        "era": "16th Century Latin petra + facere",
        "etymology": {
            "components": ["petra (rock)", "facere (to make)"],
            "original_statement": "From French pétrifier, from Latin petra (rock, stone) + facere (to make)."
        },
        "concept": "Making into rock (「流動的な命（fluid life）」を 「硬い永遠（hard eternity）」へと 閉じ込め 「瞬間」を 「固定」すること)",
        "thinking": "あまりに強すぎる感情や 外部の圧力が、柔軟な生命の組織を 凍てつかせ、石のような 静止へと 追い込んでしまうこと. 語源は「石にする」. それは 恐怖であると同時に 過ぎ去る時間を 物質の中に 永遠に 封じ込める（化石化）という 聖なる「記憶の定着」のアクションでもあります.",
        "aftertaste": "永遠の静止. 恐怖に すくむことを 恥じないで. その瞬間の「ペトリファイ（石化）」は あなたの大切な想いを 永遠に 守り抜くための 魂の 防衛反応なのかもしれないのだから.",
        "example": "The campers were petrified by the sudden and loud roar of a bear coming from the darkness of the woods.",
        "deep_dive": { "roots": [{"term": "per-", "meaning": "none"}], "points": ["Peter（ピーター：岩）と同じ。存在の「重み」のルーツ。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "lapidary_stone",
        "word": "Lapidary",
        "meaning": "宝石細工の、刻まれた、(文体が)簡潔で格調高い",
        "era": "14th Century Latin lapideus",
        "etymology": {
            "components": ["lapis (stone)"],
            "original_statement": "From Latin lapidarius (pertaining to stone, a stone-cutter), from lapis (stone)."
        },
        "concept": "Of the stone (「贅肉（excess）」を 削ぎ落とし 「完成された美（polished beauty）」へと 言葉を 「研磨」すること)",
        "thinking": "無駄な飾りを排し、石に刻まれた 碑文のように、永遠の重みに 耐えうる 簡潔で 格調高い 表現を目指すこと. 語源は「石の、石工」. それは 書かれた言葉が、時間という 波に 洗われても なお 輝きを 失わないための 聖なる「研磨」の 技術です.",
        "aftertaste": "研磨された言葉. 饒舌（じょうぜつ）に 語るよりも その一言を 磨こう. あなたの「ラピダリー（格調高い）」な 表現が 誰かの心の深くに 消えない 碑文として 刻まれることになるのだから.",
        "example": "His writing style was admired for its lapidary precision, conveying deep meanings in very few words.",
        "deep_dive": { "roots": [{"term": "lap-", "meaning": "stone"}], "points": ["lapis lazuli（ラピスラズリ：青い石）と同じ。希少性と個性の表現。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "immutable_time",
        "word": "Immutable",
        "meaning": "不変の、変わらない、永劫の",
        "era": "15th Century Latin in- + mutabilis",
        "etymology": {
            "components": ["in- (not)", "mutare (to change)"],
            "original_statement": "From Latin immutabilis (unchangeable), from in- (not) + mutabilis (changeable), from mutare (to change)."
        },
        "concept": "Not changeable (「移ろい（flux）」を 超越した 「絶対的な（absolute）」 領域で 変わらぬ 「真理」を 守ること)",
        "thinking": "表面的な 現象の 変化に 惑わされず その根底にある 揺るぎない 法則（ロゴス）と 一致して 生きること. 語源は「変えられない」. それは 執着としての 固執ではなく 全ての 変化を 包み込みながらも なお 変わらない 宇宙的な 安定と 信頼の 証（あかし）です. 不変は、慈悲です.",
        "aftertaste": "不変の信頼. 周りが どんなに 変わろうとも あなたの内側にある「イミュータブル（不変の）」な 誠実さを 信じて. その 変わらない光こそが 誰かの 帰るべき 港に なるのだから.",
        "example": "The laws of physics are considered immutable, governing the universe with total consistency.",
        "deep_dive": { "roots": [{"term": "mei-", "meaning": "to change, go, move"}], "points": ["mutation（突然変異）や migration（移動）と同じ。動くことの本質。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "memorial_time",
        "word": "Memorial",
        "meaning": "記念碑、追悼の、記憶、記念館",
        "era": "14th Century Latin memoria",
        "etymology": {
            "components": ["memoria (memory)"],
            "original_statement": "From Old French mémorial, from Late Latin memoriale (a reminder, memory, record), from Latin memoria (memory)."
        },
        "concept": "Living memory (「消え去る（vanishing）」 運命の 「魂（soul）」を 「想起（recall）」 させ続けるための 聖なる 錨（いかり）)",
        "thinking": "過去を 埋葬するのではなく 今、ここに 呼び戻し 未来の 糧（かて）として 活性化させるための 意志的な 記憶のアクション. 語源は「記憶」. それは 物理的な石の 建造物を 超えて 私たちが 互いに 語り継ぐことで 命を 永遠化しようとする 慈愛に満ちた 誓いです.",
        "aftertaste": "記憶の錨. 過去を 忘却の海に 沈めないで. あなた自身の 人生の物語を「メモリアル（追悼/記念）」として 大切に 語り継ぐことで あなたの歩みは 誰かの 明日を 照らす 希望の灯に なるのだから.",
        "example": "A simple stone memorial was erected in the park to honor those who had served the community.",
        "deep_dive": { "roots": [{"term": "mer-", "meaning": "to remember, care for"}], "points": ["memory（記憶）や mourn（悼む）と同じ。愛するものを「心に留める」力。"] },
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
        print(f"Success: Added {added} words in Cycle 151.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
