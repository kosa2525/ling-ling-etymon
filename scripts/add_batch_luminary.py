import json
import re

word_batch = [
    # Cycle 146: Spark & Vision (Refined)
    {
        "id": "luminary_vision",
        "word": "Luminary",
        "meaning": "著名人、専門家、発光体、天体",
        "era": "15th Century Latin lumen",
        "etymology": {
            "components": ["lumen (light)"],
            "original_statement": "From Old French luminaire (lamp, light), from Late Latin luminare (light, lamp, heavenly body), from Latin lumen (light)."
        },
        "concept": "Source of light (「暗闇（darkness）」を 照らし出す 「光源（source）」 としての 圧倒的な 精神性)",
        "thinking": "単に知識があるだけでなく、その存在自体が周囲に希望や指針を与え、進むべき道を鮮やかに照らし出す、高潔なリーダーシップの象徴. 語源は「光、天体」. それは 地上の些事を超越し、宇宙的な視点から 真理を 伝えようとする 聖なる「灯台」としての あり方です.",
        "aftertaste": "精神の灯台. 誰かの顔色を 窺（うかが）わないで. あなたが自分自身の信念に 忠実に生きる「ルミナリー（発光体）」であるとき 世界は道に迷うことなく 次の時代へと 進むことができるのだから.",
        "example": "He was a leading luminary in the field of theoretical physics, inspiring generations of young scientists.",
        "deep_dive": { "roots": [{"term": "leuk-", "meaning": "light, brightness"}], "points": ["illuminate（照らす）や lucid（明快な）と同じ。闇を切り裂く、知性の矢。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "scintillate_spark",
        "word": "Scintillate",
        "meaning": "きらめく、火花を散らす、(才気が)ほとばしる",
        "era": "17th Century Latin scintilla",
        "etymology": {
            "components": ["scintilla (spark)"],
            "original_statement": "From Latin scintillatus, past participle of scintillare (to sparkle, glitter, gleam), from scintilla (spark)."
        },
        "concept": "Emitting sparks (「命（life）」の 摩擦が 「火花（spark）」となって 激しく 「輝き放たれる（radiate）」こと)",
        "thinking": "淀んだ静止を拒み、常に新しいアイディアや情熱が、火花のように連続的に飛び出している、躍動的で魅力的な精神の状態. 語源は「火花を散らす」. それは 安定した輝きではなく、変化し続ける「一瞬の閃き」の 連続が生み出す、圧倒的な 生命の ダンスです.",
        "aftertaste": "閃きの連鎖. 自分の情熱を 抑え込まないで. あなたが「シンティレイト（煌めく）」し 才気をほとばしらせるとき その輝きは 周囲の人々の心にも 聖なる火を 灯すことになるのだから.",
        "example": "The conversation began to scintillate with wit and brilliant insights as soon as she joined the table.",
        "deep_dive": { "roots": [{"term": "skai-", "meaning": "to shine, gleam (possible root)"}], "points": ["stencil（ステンシル：光を通す型）の語源に関わる説も。闇の中の、確かな光。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "phosphorescent_spark",
        "word": "Phosphorescent",
        "meaning": "青白く光る、(熱を伴わずに)発光する、燐光を放つ",
        "era": "18th Century Greek phos + phoros",
        "etymology": {
            "components": ["phos (light)", "phoros (bearing)"],
            "original_statement": "From Greek phosphoros (bringing light), from phos (light) + phoros (bringing, bearing), from pherein (to carry)."
        },
        "concept": "Bearing light (「外部（outside）」からの 光を 「記憶（remember）」し 暗闇で 静かに 「放ち続ける」 誠実な 輝き)",
        "thinking": "激しい燃焼ではなく、受け取った恩恵や感動を自分の中に蓄え、光が消え去った後も、幽かに、しかし確信を持って照らし続ける、慈悲深い持続性. 語源は「光を運ぶもの」. それは 過去の美しさを 現在の暗闇の中で 再生（リプレイ）し続ける 聖なる「記憶の声」です.",
        "aftertaste": "記憶の残光. 良い影響を 与えられた記憶を 大切にしよう. あなたがその「フォスフォレッセント（燐光）」を 絶やさずにいることで 世界の暗闇は 幽かな 希望の色に 彩られ続けるのだから.",
        "example": "The ocean surface was alive with phosphorescent plankton, glowing emerald green in the dark night.",
        "deep_dive": { "roots": [{"term": "bha-", "meaning": "to shine"}, {"term": "bher-", "meaning": "to carry"}], "points": ["phantom（幻影）や metaphor（隠喩：意味を運ぶもの）と同じ。目に見えない力を運ぶ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "coruscate_spark",
        "word": "Coruscate",
        "meaning": "きらめく、才気が溢れる、(光が)明滅する",
        "era": "18th Century Latin coruscare",
        "etymology": {
            "components": ["coruscare (to flash, vibrate, glitter)"],
            "original_statement": "From Latin coruscatus, past participle of coruscare (to flash, vibrate, quiver, shake, glitter, gleam)."
        },
        "concept": "Vibrant flashing (「震える（vibrate）」 ような 「細かな明滅（glitter）」が 空間に 「リズム（rhythm）」を 与えること)",
        "thinking": "一定の強さではなく、震えながら、揺らぎながら、それでも強く存在を主張し続ける、生命の微細な振動（バイブレーション）. 語源は「閃く、震える」. それは 完璧な静止よりも 遥かに 命を感じさせる 瑞々しい（みずみずしい） 輝きの パルスです. 知性は、リズムを刻みます.",
        "aftertaste": "震える知性. 迷いながら 輝いていい. あなたが「コーラスケイト（煌めく）」し その繊細な 魂の震えを 表現することで 世界は より豊かな 響きを 手にすることができるのだから.",
        "example": "The diamond began to coruscate with a thousand tiny fires under the jeweler's magnifying glass.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["corus（煌びやかな）のルーツ。一瞬一瞬が、新しい「生の誕生」であること。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "perspicacity_vision",
        "word": "Perspicacity",
        "meaning": "洞察力、聡明さ、先見の明",
        "era": "16th Century Latin per- + specere",
        "etymology": {
            "components": ["per- (through)", "specere (to look)"],
            "original_statement": "From Middle French perspicacité, from Late Latin perspicacitatem (sharpness of sight), from Latin perspicax (sharp-sighted), from perspicere (to see through)."
        },
        "concept": "Seeing through (「表層（surface）」を 貫き 「核（core）」にある 真実を 一瞬で 「射抜く」 精神の 透視能力)",
        "thinking": "複雑な 弁明や 飾りに 惑わされるのを やめ 誰もが 見逃している 本質的な 矛盾や 可能性を 静かに 掬い上げる（すくいあげる） 深い 眼差し. 語源は「透かし見る力」. それは 未来を 予言することではなく 今、ここにある 兆しを 誰よりも 正確に 読み解くという 誠実な 知性の 営みです.",
        "aftertaste": "射抜く眼差し. 多くの情報に 流されないで. あなたの「パースピカシティ（洞察力）」という名の 澄んだ瞳で 世界を見つめ直そう. 答えは いつだって あなたの 目の前に 幽かに 浮かび上がっているのだから.",
        "example": "His remarkable perspicacity allowed him to predict the market crash months before it actually occurred.",
        "deep_dive": { "roots": [{"term": "spek-", "meaning": "to observe"}], "points": ["perspective（視点）や suspect（疑う：下から覗く）と同じ。視線の「角度」が運命を決める。"] },
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
        print(f"Success: Added {added} words in Cycle 146.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
