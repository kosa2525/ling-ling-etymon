import json
import re

word_batch = [
    # Cycle 94: Authenticity & Sincerity
    {
        "id": "candor_sincerity",
        "word": "Candor",
        "meaning": "素直さ、誠実、公平、(白く輝くような)純真",
        "era": "14th Century Latin candere",
        "etymology": {
            "components": ["candere (to shine, be white, glow)"],
            "original_statement": "From Latin candor (whiteness, brightness, purity), from candere (to shine, be white, glow)."
        },
        "concept": "Glowing whiteness (一切の汚れがなく、雪のように「白く（white）」「輝いて（shining）」いること)",
        "thinking": "策略や計算を一切含まず、自分の心をそのまま外側へと開放している状態. 語源の candere は、白熱すること。心にやましいことが何一つないとき、その人の言葉は純白の光を帯び、相手の心にまで真っ直ぐに届きます。それは、隠し事という「影」を持たない、魂の透明度です。",
        "aftertaste": "一点の曇りもない光。あなたがそのままでいるとき、世界はあなたの光によって、初めて本当の色を思い出す。",
        "example": "We were all impressed by the refreshing candor with which he admitted his mistakes.",
        "deep_dive": { "roots": [{"term": "kand-", "meaning": "to shine, glow"}], "points": ["candidate（候補者：白い服を着た人）や candle（ろうそく）と同じ、潔白と閃光。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "integrity_sincerity",
        "word": "Integrity",
        "meaning": "誠実、完全な状態、一貫性",
        "era": "15th Century Latin integer",
        "etymology": {
            "components": ["in- (not)", "tangere (to touch)"],
            "original_statement": "From Old French integrite, from Latin integritatem (soundness, wholeness, integrity), from integer (whole, untouched), from in- (not) + root of tangere (to touch)."
        },
        "concept": "Untouched whole (他者によって「触れられ（touch）」ず、損なわれていない「完全（whole）」な状態)",
        "thinking": "どんな誘惑や圧力があっても、自分の中にある道徳的な規律を「損なわれていない全体（Integer）」として守り抜くこと. それは、言っていること、やっていること、そして思っていることが、一つの美しい円（まる）として統合されている状態です。自己への裏切りがない、という究極の誠実。",
        "aftertaste": "一貫した静寂。あなたはもう、自分を説明する必要はない。あなたの全存在が、一つの揺るぎない答えなのだから。",
        "example": "He is a man of great integrity who always stays true to his principles.",
        "deep_dive": { "roots": [{"term": "tag-", "meaning": "to touch"}], "points": ["integer（整数：割れない数）や contact（接触）と同じ、分断を拒む力。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "earnest_sincerity",
        "word": "Earnest",
        "meaning": "真面目な、真剣な、切実な",
        "era": "Old English eornoste",
        "etymology": {
            "components": ["eornoste (zeal, seriousness)"],
            "original_statement": "From Old English eornoste (zealous, serious), related to Old High German ernust (seriousness, struggle)."
        },
        "concept": "Zealous struggle (目的のために、わき目も振らず「懸命に（serious）」闘うこと、ひたむきさ)",
        "thinking": "遊び半分ではなく、自分の全存在を賭けて事に当たる、揺るぎない「真剣さ」. 語源には「闘争（struggle）」や「活力」の意味が含まれており、そこには静止した真面目さではなく、火花を散らしながら何かを成し遂げようとする、熱を帯びた誠実さが宿っています。",
        "aftertaste": "燃える真剣。あなたのひたむきなまなざしは、冷え切った世界に、もう一度だけ奇跡を信じさせる力を持っている。",
        "example": "They made an earnest effort to resolve the dispute before things got out of hand.",
        "deep_dive": { "roots": [{"term": "er-", "meaning": "to set in motion"}], "points": ["run（走る）や rise（昇る）とも遠い関係にあり、能動的に動き出す意志。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "veracity_sincerity",
        "word": "Veracity",
        "meaning": "真真実性、誠実、正確さ",
        "era": "17th Century Latin verus",
        "etymology": {
            "components": ["verus (true, real, actual)"],
            "original_statement": "From Latin veracitatem (truthfulness), from verax (truthful), from verus (true)."
        },
        "concept": "Being true (虚飾を排し、あるがままの「真実（true）」であることを貫くこと)",
        "thinking": "単に「嘘をつかない」という消極的な意味ではなく、物事のありのままの姿を正確に伝えようとする、能動的で妥協のない誠実さ. 語源の verus は「本物の」という意味。事実に忠実であることは、この世界に対する最も基本的な礼儀であり、信頼という名前の魔法の土台です。",
        "aftertaste": "剥き出しの真理。飾られた嘘よりも、震えながら語られる真実のほうが、遥かに美しいことを、あなたは知っている。",
        "example": "We have no reason to doubt the veracity of her eyewitness account.",
        "deep_dive": { "roots": [{"term": "weros-", "meaning": "true, trustworthy"}], "points": ["verify（確認する）や verdict（評決：真実を語ること）と同じ、確信のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "guileless_sincerity",
        "word": "Guileless",
        "meaning": "正直な、裏表のない、あどけない",
        "era": "14th Century Old French guile + -less",
        "etymology": {
            "components": ["guile (deceit, trickery)", "-less (without)"],
            "original_statement": "From guile (deceit) + -less (without). Guile is from Old French guile (deceit, trickery, fraud)."
        },
        "concept": "Without trickery (相手を騙そうとする「企み（trickery）」を「持たない（without）」こと)",
        "thinking": "他者を操作しようとする計算や「毒」が一切ない、透き通った水のような気質. guile は「魔法（wiles）」とも語源を共有しており、自分を大きく見せたり、相手を惑わせたりする「まやかし」を排した状態です。あどけない子供のような、しかし大人の自制に裏打ちされた、究極の「素直さ」。",
        "aftertaste": "計算のない微笑み。あなたの透明なまなざしの前では、どんな複雑な策略も、その意味を失って溶けてゆく。",
        "example": "The child answered with a guileless smile that softened the hearts of everyone in the room.",
        "deep_dive": { "roots": [{"term": "wig-", "meaning": "sorcery (possible root of guile)"}], "points": ["wile（策略）と同じ。-less が加わることで、魔法に頼らない『生の自分』が残る。"] },
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
        print(f"Success: Added {added} words in Cycle 94.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
