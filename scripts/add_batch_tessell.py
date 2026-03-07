import json
import re

word_batch = [
    # Cycle 136: Pattern & Symmetry
    {
        "id": "tessellation_pattern",
        "word": "Tessellation",
        "meaning": "テセレーション、モザイク模様、空間充填",
        "era": "17th Century Latin tessella",
        "etymology": {
            "components": ["tessella (small square piece of stone)"],
            "original_statement": "From Latin tessellatus (checkered, mosaic), from tessella (small square stone or tile used in mosaics), diminutive of tessera (a square piece), from Greek tessera (four)."
        },
        "concept": "Checkered mosaic (「四角い石（tessella）」を 隙間なく 「敷き詰める（fill）」 完璧な 幾何学美)",
        "thinking": "個々の要素が 完璧な規律を持って 隣り合うものと 結びつき 巨大で 淀みのない 模様（パターン）を 作り出すこと. 語源は「小さな四角い石」. それは バラバラな経験や 知識が 自分の人生という 壁画（モザイク）の中に 欠かせないピースとして 収まっていく 充足のプロセスです.",
        "aftertaste": "完璧な調和. どんな小さな出来事も 決して無駄ではない. それは あなたという 壮大な人生のテセレーションを 完成させるための 唯一無二の かけら（ピース）なのだから.",
        "example": "The floors of the Roman villa were covered in stunning tessellations that had survived for centuries.",
        "deep_dive": { "roots": [{"term": "kwetwer-", "meaning": "four"}], "points": ["quarter（四分の一）や table（テーブル：平らなもの）と同じ。安定と構造。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "fractal_pattern",
        "word": "Fractal",
        "meaning": "フラクタル、自己相似形、断片的な",
        "era": "20th Century Latin frangere",
        "etymology": {
            "components": ["frangere (to break)"],
            "original_statement": "Coined by Benoit Mandelbrot in 1975, from Latin fractus (interrupted, broken), past participle of frangere (to break)."
        },
        "concept": "Self-similarity (「断片（fragment）」の中に 全体の 「形（form）」が 永遠に 繰り返される 神秘)",
        "thinking": "ミクロとマクロが 同じ構造を持ち どこまで 掘り下げても 同じ「美（真理）」が 現れる 宇宙の 驚異的な 統一性. 語源は「壊れた」. それは 断片であることを 否定せず むしろ その一滴（断片）の中に 大海（全体）が 宿っていることを 肯定する 知性の視点です.",
        "aftertaste": "断片の中の宇宙. 目の前の小さな作業（細部）を 疎かにしないで. あなたがそこに 込めた愛は 巡り巡って あなたの人生全体の 輝き（フラクタル）として 結実してゆくのだから.",
        "example": "Clouds, coastlines, and snowflakes are all examples of complex fractal patterns found in nature.",
        "deep_dive": { "roots": [{"term": "bhreg-", "meaning": "to break"}], "points": ["fraction（分数）や fragile（壊れやすい）と同じ。不規則性の中に潜む、真理。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "rhythm_pattern",
        "word": "Rhythm",
        "meaning": "リズム、韻律、周期的な運動",
        "era": "16th Century Greek rhein",
        "etymology": {
            "components": ["rhein (to flow)"],
            "original_statement": "From Old French rithme, from Latin rhythmus, from Greek rhythmos (measured flow or movement, proportion), related to rhein (to flow)."
        },
        "concept": "Measured flow (「流れる（flow）」 命に 「形（measure）」を 与え 周期的な 「心地よさ」を 生むこと)",
        "thinking": "静止することのない 生命（エネルギー）が 一定の周期を持って 繰り返されることで 生まれる 聖なる「脈動（パルス）」. 語源は「流れる」. それは 宇宙が刻む 壮大な鼓動であり 私たちがそのリズム（流体）に 身を委ねるとき 魂は 深い安らぎと 活力を 取り戻します.",
        "aftertaste": "命の拍動. 焦って 自分のリズムを 崩さないで. 宇宙の流れるような 旋律（リズム）に 呼吸を合わせることで あなたの人生は より心地よく、豊かなものに 変わってゆくのだから.",
        "example": "The rhythmic sound of the waves crashing against the shore felt deeply soothing to his tired mind.",
        "deep_dive": { "roots": [{"term": "sreu-", "meaning": "to flow"}], "points": ["stream（小川）や rheology（流動学）と同じ。絶え間なき生成の歩幅。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "symmetry_pattern",
        "word": "Symmetry",
        "meaning": "対称、均衡、釣り合い、美しさ",
        "era": "16th Century Greek syn- + metron",
        "etymology": {
            "components": ["syn- (together)", "metron (measure)"],
            "original_statement": "From Latin symmetria, from Greek symmetria (agreement in dimensions, due proportion), from syn- (together) + metron (measure)."
        },
        "concept": "Measuring together (「左右（both sides）」を 「等しく（equally）」 計ることで 生まれる 崇高な 「バランス」)",
        "thinking": "一方に偏ることのない 完璧な 釣り合いから生み出される 淀みのない 「美（調和）」. 語源は「共に測る」. それは 静止した形ではなく 対立する二つの力が 中央の一点（センター）で 完璧に 手を携え合っているという 動的な「平和」の状態を 指します.",
        "aftertaste": "静かなる均衡。あなたの心の中に 聖なる「点（センター）」を 保ち続けよう。善と悪、光と影の 両方を等しく 抱きしめる（対称）ことで 魂は初めて 揺るぎない 美しさを手にできるのだから。",
        "example": "The symmetry of the Taj Mahal's architecture is a testament to the incredible skill of its builders.",
        "deep_dive": { "roots": [{"term": "sem-", "meaning": "one, as one"}, {"term": "mē-", "meaning": "to measure"}], "points": ["same（同じ）や meter（計器）と同じ。多様性を一つに纏める力。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "matrix_pattern",
        "word": "Matrix",
        "meaning": "基盤、母体、行列、金型",
        "era": "14th Century Latin mater",
        "etymology": {
            "components": ["mater (mother)"],
            "original_statement": "From Latin matrix (breeding-animal, source, origin), from mater (mother)."
        },
        "concept": "The womb (「母体（mother）」の ように あらゆる 「形（form）」を 育み、規定する 聖なる 「仕組み」)",
        "thinking": "それ自体は 目に見えなくても あらゆる現象を 背後で支え 秩序（パターン）を 与え続けている 根源的な「格子（枠組み）」. 語源は「母親」. 私たちが生きる 社会や 概念の仕組み（マトリックス）を 理解することは その「産みの親」の 意志に触れる 旅でもあります.",
        "aftertaste": "孵化の器. 今 あなたが立っている その場所（基盤）を 丁寧に 観察してごらん. 宇宙という 巨大な母体（マトリックス）が あなたという 唯一の命を 育むために 用意した 壮大な物語の舞台なのだから.",
        "example": "Europe's cultural matrix was deeply influenced by the traditions of ancient Rome and Greece.",
        "deep_dive": { "roots": [{"term": "māter-", "meaning": "mother"}], "points": ["matter（物質：万物の母）や material（材料）と同じ。存在を裏支えする力。"] },
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
        print(f"Success: Added {added} words in Cycle 136.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
