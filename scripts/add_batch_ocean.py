import json
import re

word_batch = [
    # Cycle 124: Ocean & Depth
    {
        "id": "maritime_ocean",
        "word": "Maritime",
        "meaning": "海の、海事の、沿岸の、海に面した",
        "era": "16th Century Latin mare",
        "etymology": {
            "components": ["mare (sea)"],
            "original_statement": "From Middle French maritime, from Latin maritimus (of the sea, maritime), from mare (sea)."
        },
        "concept": "Of the sea (命の母なる 「海（sea）」に 関連する あらゆるところ)",
        "thinking": "広大で、深く、容赦のない「海」という存在と 人との関わりを示す知の領域. 語源は「海」. それは 貿易や航海といった実務的な側面だけでなく 私たちの魂が 冒険と未知への憧れを持って 荒波へと乗り出していく 勇敢な記憶をも指します.",
        "aftertaste": "潮風の記憶. あなたの心の中にも また広大な「海（マリタイム）」が広がっている. 凪（なぎ）の日も嵐の日も その深さを愛し 誇り高く航海を続けよう.",
        "example": "The city has a rich maritime history, having been a major port for centuries.",
        "deep_dive": { "roots": [{"term": "mori-", "meaning": "sea, lake"}], "points": ["marine（海の）や mermaid（人魚）と同じ。母なる水のルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "pelagic_ocean",
        "word": "Pelagic",
        "meaning": "遠洋の、外洋の、水層の(底にいない)",
        "era": "17th Century Greek pelagos",
        "etymology": {
            "components": ["pelagos (sea, open sea)"],
            "original_statement": "From Latin pelagicus, from Greek pelagikos, from pelagos (sea, open sea)."
        },
        "concept": "Of the open sea (岸の見えない 「外洋（open sea）」を 漂いながら 生きる 自由な孤独)",
        "thinking": "地に足をつける場所（底）を持たず 360度どこまでも続く 青い垂直の世界を自由に遊泳すること. 語源は「外洋」. それは 誰の助けも届かない 厳しくも圧倒的な自由を象徴しています. 群れを離れ 深い孤独の中でこそ 見つかる真理があります.",
        "aftertaste": "青い孤独. 頼るべき「岸辺」が見えなくても 不安にならないで. あなたは今 魂の最も深い「外洋（ペラジック）」を 誰にも邪魔されず 悠々と泳いでいるのだから.",
        "example": "Pelagic birds spend most of their lives at sea, returning to land only to breed.",
        "deep_dive": { "roots": [{"term": "plak-", "meaning": "flat, broad (possible root for pelagos)"}], "points": ["plankton（プランクトン：漂うもの）と同じ。平らで広大な領域。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "abyssal_ocean",
        "word": "Abyssal",
        "meaning": "深海の、深淵の、底知れぬ",
        "era": "17th Century Greek a- + byssos",
        "etymology": {
            "components": ["a- (without)", "byssos (bottom)"],
            "original_statement": "From abyss (noun) + -al. Abyss from Greek abyssos (bottomless)."
        },
        "concept": "Of the bottomless (「底（bottom）」が 「無い（without）」 永遠に 潜り続けられる 深み)",
        "thinking": "光さえも屈服する 圧倒的な水圧と静寂に包まれた 宇宙に最も近い場所. 語源は「底なし」. そこには 表層の喧騒（ノイズ）は一切届きません. あなたが 自分の心の最も深い「深淵（アピサル）」へと潜ったとき そこでしか出会えない 宝石のような真実に気づくはずです.",
        "aftertaste": "静寂の深層. 深く潜ることを 恐れないで. 暗闇の先には あなたの魂が放つ 独自の光（発光現象）が 最も美しく輝く場所が 待っているのだから.",
        "example": "Scientists are still discovering bizarre new species in the abyssal plains of the ocean.",
        "deep_dive": { "roots": [{"term": "ne-", "meaning": "not"}, {"term": "bhudhn-", "meaning": "bottom"}], "points": ["abyss（アビス）の形容詞形。垂直の孤独の極致。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "estuary_ocean",
        "word": "Estuary",
        "meaning": "河口、入り江、潮の干満する場所",
        "era": "16th Century Latin aestus",
        "etymology": {
            "components": ["aestus (tide, surge, heat)"],
            "original_statement": "From Latin aestuarium (tidal inlet, estuary), from aestus (tide, surge, boiling, heat)."
        },
        "concept": "Tidal surge (海から 「潮（tide）」が 勢いよく 「沸き立つ（surge）」 交わりの場所)",
        "thinking": "川の真水と 海の塩水が 激しく混ざり合い 豊かな多様性を生み出す 命の交差点. 語源は「潮の沸き立ち」. それは 異なる価値観がぶつかり合い 新しいエネルギーが生まれる 混沌としていながらも 肥沃な領域です. 境界線は 不透明だからこそ 美しい.",
        "aftertaste": "交わりの入り江. 自分の殻に閉じこもらず 世界という名の「海」を招き入れてごらん. 混ざり合う瞬間の戸惑いこそが 新しい命を育む 豊かな栄養になるのだから.",
        "example": "The river estuary provides a crucial habitat for migratory birds and young fish.",
        "deep_dive": { "roots": [{"term": "aidh-", "meaning": "to burn"}], "points": ["edifice（建築物）や heat（熱）と同じ。潮の満ち引きは、地球が持つ「熱量」の現れ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "archipelago_ocean",
        "word": "Archipelago",
        "meaning": "列島、諸島、多島海",
        "era": "15th Century Greek arkhi- + pelagos",
        "etymology": {
            "components": ["arkhi- (chief)", "pelagos (sea)"],
            "original_statement": "From Italian arcipelago, from Greek arkhi- (chief) + pelagos (sea)."
        },
        "concept": "Chief sea (「王たる（chief）」 「海（sea）」に 浮かぶ 無数の 「島々の連なり（islands）」)",
        "thinking": "一つに繋がっているのではなく 独自の個性を保った島々が 緩やかに、しかし確かな関係性を持って 点在している状態. 語源は「主要な海」. それは 絆はあっても隷属はしない 理想的なコミュニティの形でもあります. 孤独な島たちは 海によって隔てられ 海によって繋がっています.",
        "aftertaste": "多島海の調和. 私たちは皆 孤独な島だ. しかし その間を流れる情熱という名の「海」が 私たちを一つの美しい物語（諸島）として 繋いでくれていることを 忘れないで.",
        "example": "The Indonesian archipelago consists of thousands of islands stretching across two oceans.",
        "deep_dive": { "roots": [{"term": "age-", "meaning": "to begin, lead"}, {"term": "plak-", "meaning": "flat, broad"}], "points": ["architect（建築家）と同じ「主要な」のルーツ。秩序ある集合体。"] },
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
        print(f"Success: Added {added} words in Cycle 124.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
