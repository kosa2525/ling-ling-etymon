import json
import re

word_batch = [
    # Cycle 143: Ocean & Depth (Refined)
    {
        "id": "maritime_ocean",
        "word": "Maritime",
        "meaning": "海の、海事の、海沿いの、海軍の",
        "era": "16th Century Latin mare",
        "etymology": {
            "components": ["mare (sea)"],
            "original_statement": "From Latin maritimus (of or belonging to the sea), from mare (sea)."
        },
        "concept": "Of the sea (「海（sea）」に 根ざした 「文化（culture）」と 「冒険（adventure）」の 記憶)",
        "thinking": "陸の論理（固定）を離れ、波と風という流動的な法則に従って生きる、壮大なフロンティア・スピリット. 語源は「海に属するもの」. それは 物理的な場所だけでなく 未知への 恐怖を 乗り越え 水平線の 彼方へと 漕ぎ出そうとする 私たちの 勇敢な 知性の 営みを 指しています.",
        "aftertaste": "水平線の誘惑. 安定した 港に 留まらないで. あなたの内側にある その「マリタイム（海の）」情熱を 解き放つことで 人生は 測り知れない 輝きと 奥行きを 手にするのだから.",
        "example": "The city has a long and rich maritime history, having once been a dominant trading port in the region.",
        "deep_dive": { "roots": [{"term": "mori-", "meaning": "sea, lake"}], "points": ["marine（海の）や mermaid（人魚）と同じ。母なる水の記憶。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "fathom_depth",
        "word": "Fathom",
        "meaning": "ひろ(約1.8m)、(奥行きを)測る、(謎を)見抜く",
        "era": "Pre-12th Century Old English fæðm",
        "etymology": {
            "components": ["fæðm (outstretched arms, embrace)"],
            "original_statement": "From Old English fæðm (outstretched arms, embrace, grasp, protection)."
        },
        "concept": "Outstretched arms (「両腕（arms）」を 広げて 「抱きしめる（embrace）」ように 深淵の 「重み」を 捉えること)",
        "thinking": "表面を撫でるのではなく、自らの身体（尺度）を使って、暗闇という名の深淵を「抱き込み」、その本質を理解しようとする、愛に満ちた知のアクション. 語源は「広げた両腕」. それは 謎を 解体することではなく その深さを そのまま 慈しむように 理解することを 意味しています.",
        "aftertaste": "理解の抱擁. 答えを 急がないで. 目の前の謎を「ファゾム（抱擁/理解）」しようと 誠実に 向き合い続けることで あなたの魂は 誰よりも 深い 知恵を 宿すことになるのだから.",
        "example": "The mystery of the vanish ship was so complex that no one could truly fathom what had happened.",
        "deep_dive": { "roots": [{"term": "pet-", "meaning": "to spread"}], "points": ["expand（広がる）や paten（聖皿）と同じ。自己を広げて、世界を受け入れる力。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "abyssal_depth",
        "word": "Abyssal",
        "meaning": "深海の、深淵の、測り知れない",
        "era": "17th Century Greek a- + byssos",
        "etymology": {
            "components": ["a- (without)", "byssos (bottom)"],
            "original_statement": "From Late Latin abyssimus, from Greek abyssos (bottomless), from a- (without) + byssos (bottom)."
        },
        "concept": "Of the bottomless (「底（bottom）」が なく 「永遠に（eternally）」 降りてゆける 意識の 最深部)",
        "thinking": "光すら届かない 圧倒的な 静寂と 圧力の中で 命の根源が 幽かに 脈動している 聖なる 揺籃（ようらん）. 語源は「底なしの」. それは 絶望であると同時に 私たちの 表面的な 意識を超えた 場所にある 宇宙的な 静止と 統一の 領域を 指しています. 深淵こそが、故郷です.",
        "aftertaste": "最深部の対話. 孤独という名の「アビサル（深海）」へ 降りてゆこう. その絶対的な 静寂の中でしか 聞き取ることができない 宇宙の 真実のささやきが きっと あるはずだから.",
        "example": "Strange and luminous creatures inhabit the abyssal zones of the ocean, adapted to extreme pressure.",
        "deep_dive": { "roots": [{"term": "bhudh-", "meaning": "bottom"}], "points": ["fundamental（根本的な）と同じ。最も深い場所こそが、全ての支え。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "inundate_ocean",
        "word": "Inundate",
        "meaning": "氾濫(はんらん)させる、浸水させる、(仕事などで)殺到する",
        "era": "17th Century Latin in- + unda",
        "etymology": {
            "components": ["in- (into, upon)", "unda (wave)"],
            "original_statement": "From Latin inundatus, past participle of inundare (to overflow, flood), from in- (into, upon) + undare (to rise in waves), from unda (wave)."
        },
        "concept": "Moving in waves (「波（wave）」が 境界を 越えて 「溢れ出し（overflow）」 全てを 飲み込む 圧倒的な エネルギー)",
        "thinking": "小さな堤防（エゴ）を軽々と飛び越え、世界を自らの色（水）で塗り替えていく、制御不能なほどの豊溢（ほういつ）. 語源は「波立つ」. それは 破壊であると同時に 淀んだ現状を 押し流し 新しい肥沃な大地（可能性）を もたらすための 荒々しい 祝福の儀式でもあります.",
        "aftertaste": "溢れ出す情熱. 適度な 量に 留まらないで. 時には「イヌンデイト（殺到）」するほどの 圧倒的な エネルギーを 社会に 放ってごらん. その奔流が 古い壁を壊し 新しい時代を 創るのだから.",
        "example": "We were inundated with thousands of applications for the single job opening within the first week.",
        "deep_dive": { "roots": [{"term": "wed-", "meaning": "water, wet"}], "points": ["water（水）や redundant（余分な：再び波立つ）と同じ。溢れ出る生命の源。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "pelagic_ocean",
        "word": "Pelagic",
        "meaning": "遠洋の、外洋の、大洋を泳ぐ",
        "era": "17th Century Greek pelagos",
        "etymology": {
            "components": ["pelagos (sea, open sea)"],
            "original_statement": "From Late Latin pelagicus, from Greek pelagikos, from pelagos (sea, open sea)."
        },
        "concept": "Of the open sea (「岸辺（shore）」を 捨て 「際限のない（limitless）」 蒼（あお）の 只中（ただなか）へ 躍進すること)",
        "thinking": "浅瀬（ありきたりな日常）の安寧を拒み、島影すら見えない大海原を棲家（すみか）とする、誇り高く孤独な魂のあり方. 語源は「大海の」. それは 誰の支援も期待できない場所で、自らの力（ヒレ）だけを頼りに、宇宙という名の巨大な流れと共生する、究極の自立です.",
        "aftertaste": "蒼き自立. 岸（過去）を 振り返らないで. あなたが「ペラジック（外洋の）」な 生き方を選んだとき 世界はあなたにとって どこまでも 自由で、美しい 可能性の遊び場に 変わるのだから.",
        "example": "Tuna and swordfish are masterful pelagic predators, traveling vast distances across the open ocean.",
        "deep_dive": { "roots": [{"term": "plak-", "meaning": "to be flat (possible for pelagos)"}], "points": ["plan（平らな図）や plain（平原）と同じ。無限に広がる水平線。"] },
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
        print(f"Success: Added {added} words in Cycle 143.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
