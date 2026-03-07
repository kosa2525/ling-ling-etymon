import json
import re

word_batch = [
    # Cycle 159: Spark & Vision (Refined)
    {
        "id": "luminary_vision",
        "word": "Luminary",
        "meaning": "指導者、権威、天体、発光体",
        "era": "15th Century Latin lumen",
        "etymology": {
            "components": ["lumen (light)"],
            "original_statement": "From Old French luminarie, from Late Latin luminare (light, lamp, heavenly body), from Latin lumen (light)."
        },
        "concept": "Source of light (「自ら（self）」が 「光源（source）」となり 闇に 迷う 「他者（others）」を 「導く（guide）」 聖なる 存在)",
        "thinking": "他人の光（評価）を 反射するのではなく、自らの 内側から 湧き上がる 知恵や 情熱によって 周囲を 照らし、進むべき 道を 示すこと. 語源は「光、天体」. それは 卓越した 才能だけでなく その存在 自体が 世界に 希望を 与えるという、聖なる「使命」の 表現です. 光は、導きです.",
        "aftertaste": "自ら放つ光. 誰かの 許可を 待たないで. あなたが「ルミナリー（発光体）」として 自分の 信じる 真実を 語り始めるとき その輝きは 遠く離れた 誰かの 心に 届き 確かな 勇気に なるのだから.",
        "example": "Einstein remains a luminary in the world of physics, inspiring countless scientists with his revolutionary theories.",
        "deep_dive": { "roots": [{"term": "leuk-", "meaning": "light, brightness"}], "points": ["lucid（明快な）や lunar（月の）と同じ。闇を 払い 意味を 与える力。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "scintillate_vision",
        "word": "Scintillate",
        "meaning": "火花を発する、きらめく、才気がほとばしる",
        "era": "17th Century Latin scintilla",
        "etymology": {
            "components": ["scintilla (spark)"],
            "original_statement": "From Latin scintillatus, past participle of scintillare (to sparkle, glitter, gleam), from scintilla (a spark)."
        },
        "concept": "Sparking vitality (「静止（stillness）」を 拒絶し 「瞬間的（instant）」な 「輝き（spark）」を 連続させることで 「生命」を 躍動させること)",
        "thinking": "単調な 輝き ではなく、常に 変化し、瞬き（まばたき）、見る者の 視線を 釘付けにするような、知的な 躍動感. 語源は「火花」. それは 安定した 燃焼 ではなく 衝突や 摩擦から 生まれる 聖なる「閃き（インスピレーション）」の 連続であり 私たちが 常に 新鮮な 自我であり続けるための アクションです. きらめきは、命です.",
        "aftertaste": "閃きの連続. 退屈な 日常に 埋没しないで. あなたの 知性が「シンティレイト（きらめく）」し 鋭い ユーモアや 発想を 放ち続けるとき 人生は 文字通り まばゆい 祝祭へと 変容してゆくのだから.",
        "example": "Her conversation scintillated with wit and intelligence, making her the center of attention at every party.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["scintilla（微量、火花）の動詞形。最小の輝きが、最大の意味を 産むルーツ。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "phosphorescent_vision",
        "word": "Phosphorescent",
        "meaning": "青白く光る、燐光を発する、(外部光なしで)光る",
        "era": "18th Century Greek phos + phoros",
        "etymology": {
            "components": ["phos (light)", "phoros (bearing)"],
            "original_statement": "From phosphorus (the element) + -escent, from Greek phosphoros (bringing light), from phos (light) + phoros (bringing), from pherein (to carry)."
        },
        "concept": "Bearing persistent light (「外側（outside）」の 光が 「消えた（vanished）」後も 「内側（inside）」に 蓄えた 「光（vision）」を 放ち続けること)",
        "thinking": "太陽（他者）の 輝きを そのまま 反射する のではなく、受け取った エネルギーを 自らの 内側で 醸成し、深い 闇の中で 誰にも 頼らずに 自ら 光り輝くこと. 語源は「光を運ぶもの」. それは 困難な 状況でも 決して 絶やさない、聖なる「魂の 蓄熱」と 長い 余韻の 表現です. 光は、記憶です.",
        "aftertaste": "内なる蓄光. 逆境の 闇に 絶望しないで. あなたが「フォスフォレッセント（燐光を放つ）」な 精神で これまでの 経験（光）を 抱きしめ続けるとき その 静かな 輝きは 闇を 抜けるための 確かな 道標に なるのだから.",
        "example": "The waves were alive with phosphorescent plankton, creating a magical glow along the nighttime shore.",
        "deep_dive": { "roots": [{"term": "bha-", "meaning": "to shine (for phos)"}, {"term": "bher-", "meaning": "to carry (for phoros)"}], "points": ["photography（写真）や transfer（移転：運ぶこと）と同じ。光の運命。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "perspicacious_vision",
        "word": "Perspicacious",
        "meaning": "洞察力のある、明敏な、先見の明がある",
        "era": "17th Century Latin per- + specere",
        "etymology": {
            "components": ["per- (through)", "specere (to look)"],
            "original_statement": "From Latin perspicax (sharp-sighted), from per- (through) + specere (to look at)."
        },
        "concept": "Looking through (「表面（surface）」の 霧を 「貫き（pierce）」 「深層（depth）」に 隠された 「本質（essence）」を 射貫くこと)",
        "thinking": "見えているものに 騙される（だまされる）ことなく、その 背後にある 動機、構造、未来の予兆を、透明な 意識で 捉えること. 語源は「透かして見る」. それは 知識の 量 ではなく 視線の「純度（シャープネス）」によって 世界を 再定義しようとする 聖なる「目撃」の 表現です. 洞察は、祈りです.",
        "aftertaste": "透徹した眼差し. 複雑な 説明に 惑わされないで. あなたが「パースピケイシャス（洞察力のある）」な 視点で 対象を じっと 見つめるとき 隠されていた 美しい 秩序（パターン）が 鮮やかに 浮かび上がってくるのだから.",
        "example": "Her perspicacious analysis of the market trends allowed the company to stay ahead of its competitors for years.",
        "deep_dive": { "roots": [{"term": "spek-", "meaning": "to observe"}], "points": ["perspective（遠近法、視点）や spectacle（壮景）と同じ。見ることによる、世界への介入. "] },
        "part_of_speech": "adjective"
    },
    {
        "id": "fulgent_vision",
        "word": "Fulgent",
        "meaning": "光り輝く、まばゆい、才気に満ちた",
        "era": "15th Century Latin fulgere",
        "etymology": {
            "components": ["fulgere (to shine)"],
            "original_statement": "From Latin fulgens, present participle of fulgere (to shine, flash, gleam)."
        },
        "concept": "Intense flashing (「真理（truth）」の 一端が 「稲光（lightning）」のように 「爆発的」に 「顕現」する 圧倒的な 輝き)",
        "thinking": "静かな 光 ではなく 目を開けていられないほどの 強烈な 視覚的・知的な インパクトを 周囲に Given こと. 語源は「光る、閃く」. それは 言い訳や 妥協を 許さない 聖なる「純粋さ」の 放射であり 私たちが 宇宙の 無限の エナジーと 直結した 瞬間に 放たれる 聖なる「叫び」の 輝きです. 輝きは、勝利です.",
        "aftertaste": "圧倒的な顕現. 自分を 小さく 見せようと しないで. あなたが「フルジェント（輝かしい）」な 情熱を そのまま 解き放つとき 世界はその 眩しさに 圧倒され 新しい 時代の 幕開けを 祝福し始めるのだから.",
        "example": "The cathedral was bathed in the fulgent light of the setting sun, making the stained glass shimmer like jewels.",
        "deep_dive": { "roots": [{"term": "bhel-", "meaning": "to shine, flash, burn"}], "points": ["flame（炎）や flagrant（目に余る：燃え盛る）と同じ。熱き輝きのルーツ。"] },
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
        print(f"Success: Added {added} words in Cycle 159.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
