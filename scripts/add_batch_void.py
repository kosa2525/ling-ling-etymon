import json
import re

word_batch = [
    # Cycle 111: Stillness & Void
    {
        "id": "vacuity_void",
        "word": "Vacuity",
        "meaning": "空虚、空っぽであること、ぼんやりした状態",
        "era": "15th Century Latin vacuus",
        "etymology": {
            "components": ["vacuus (empty, free, clear)"],
            "original_statement": "From Latin vacuitas (an emptying, vacancy), from vacuus (empty, free, clear)."
        },
        "concept": "Empty space (何も「入っていない（empty）」こと 淀みのない「空っぽ（clear）」の状態)",
        "thinking": "形あるものがすべて消え去り 思考さえも停止した 純粋な「空白」. 語源は「空（から）」. それは単なる欠如（Lack）ではなく 次の何かが生まれるための 圧倒的な「可能性の器」でもあります. 意味を追い求めるのをやめたとき あなたの心はこの美しい空虚（バキュイティ）と出会います.",
        "aftertaste": "静かなる空白. 詰め込むことをやめたとき あなたの心は世界をそのまま映し出す 透き通った鏡になる.",
        "example": "There was a certain vacuity in his expression that suggested he wasn't really listening.",
        "deep_dive": { "roots": [{"term": "eue-", "meaning": "to leave, abandon, give out"}], "points": ["vacation（休暇：空けること）や vacuum（真空）と同じ、解放のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "nullity_void",
        "word": "Nullity",
        "meaning": "無効、存在しないこと、無価値なもの",
        "era": "16th Century Latin nullus",
        "etymology": {
            "components": ["nullus (none, not any)"],
            "original_statement": "From Medieval Latin nullitas, from Latin nullus (none, not any, not one), from ne- (not) + ullus (any)."
        },
        "concept": "Not even one (「一（one）」さえも「無い（not）」こと 完全に「ゼロ（zero）」であること)",
        "thinking": "価値判断の基準そのものが消滅し 肯定も否定もできない「無」の状態. 語源は「一つも無い」. 法律用語としては無効を意味しますが 哲学的には 既存のすべての定義から自由になった 究極のゼロ地点を指します. そこには 誰にも汚されない真実の無垢（むく）があります.",
        "aftertaste": "究極のゼロ. あなたを定義するレッテルをすべて剥がしなさい. そこに残るのは 誰にも触れられない純粋な「無」という名の自由だ.",
        "example": "The contract was declared a nullity because it had been signed under duress.",
        "deep_dive": { "roots": [{"term": "ne-", "meaning": "not"}, {"term": "oinos-", "meaning": "one"}], "points": ["null（ヌル）や annul（無効にする）と同じ。無の強靭さ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "abyss_void",
        "word": "Abyss",
        "meaning": "深淵、奈落、地獄、底知れぬ深い穴",
        "era": "14th Century Greek a- + byssos",
        "etymology": {
            "components": ["a- (without)", "byssos (bottom)"],
            "original_statement": "From Latin abyssus, from Greek abyssos (bottomless), from a- (without) + byssos (bottom)."
        },
        "concept": "Without bottom (「底（bottom）」が「無い（without）」ため 永遠に潜り続けられる場所)",
        "thinking": "光さえも届かない 垂直に切り立った未知の深み. 語源は「底なし」. 恐怖を呼び起こす場所であると同時に 表面的な自己を捨て去り 魂の最も暗く 最も神聖な部分と対話するための 巡礼の場所でもあります. 深淵を覗くとき 深淵もまた あなたを覗いています.",
        "aftertaste": "底知れぬ深み. 落ちていくのではなく あなたは今 自分の深海へと静かに潜航（ダイブ）しているのだ.",
        "example": "Looking down into the canyon was like staring into a dark, bottomless abyss.",
        "deep_dive": { "roots": [{"term": "ne-", "meaning": "not (possible for a-)"}, {"term": "bhudhn-", "meaning": "bottom"}], "points": ["profound（深い）の対極としての深み。垂直の宇宙。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "chasm_void",
        "word": "Chasm",
        "meaning": "割れ目、亀裂、(意見などの)深い隔たり",
        "era": "16th Century Greek chasma",
        "etymology": {
            "components": ["chasma (yawning hollow, gulf)"],
            "original_statement": "From Latin chasma, from Greek chasma (yawning hollow, gulf, opening), related to chainein (to gape, yawn)."
        },
        "concept": "Yawning opening (口を大きく「開け（yawn）」 空間に「穴（opening）」が空いたような断絶)",
        "thinking": "一続きだった世界に突如として現れた 回復不能なまでの裂け目. 語源は「あくびをするように開く」. それは物理的な断崖だけでなく 心と心の間に生まれた 埋めようのない理解の空白をも指します. しかし その裂け目からこそ 普段は見えない地の底の真実が 姿を現すことがあります.",
        "aftertaste": "断絶の真実. 隔たりがあるからこそ 私たちは「向こう側」に憧れ 言葉という名の橋を架けようと躍起になれるのだ.",
        "example": "There is a wide chasm between the theories of politicians and the needs of ordinary people.",
        "deep_dive": { "roots": [{"term": "ghei-", "meaning": "to yawn, gape"}], "points": ["chaos（カオス：大きく開いた口）や yawn（あくび）と同じ。宇宙の巨大な欠伸（あくび）。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "void_void",
        "word": "Void",
        "meaning": "空白、空所、欠如、無効な",
        "era": "13th Century Latin vacuus",
        "etymology": {
            "components": ["vacare (to be empty)"],
            "original_statement": "From Old French voide, from Latin vocitus (empty), from vacare (to be empty)."
        },
        "concept": "The empty state (何かが失われた「跡（empty）」 あるいは何も無い「空間」そのもの)",
        "thinking": "何かが「ある」ことの対義語ではなく すべての「ある」を包み込んでいる 巨大で静かな背景. 語源は「空（から）」. それは喪失の悲しみを孕むこともあれば 執着から解放された平安を指すこともあります. あなたが自分を「空（ボイド）」にしたとき 宇宙そのものが あなたの中に流れ込みます.",
        "aftertaste": "静かなる背景. 意味を持たないことに怯えないでごらん. その空白こそが あなたという存在を最も美しく引き立てる 額縁なのだから.",
        "example": "His death left a painful void in the local community that no one could fill.",
        "deep_dive": { "roots": [{"term": "eue-", "meaning": "to leave, abandon"}], "points": ["waste（浪費する：無駄にする）や want（欠乏する）と同じ。欲求の源。"] },
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
        print(f"Success: Added {added} words in Cycle 111.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
