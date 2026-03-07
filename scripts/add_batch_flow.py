import json
import re

word_batch = [
    # Cycle 79: Flow & Liquid states
    {
        "id": "confluence_flow",
        "word": "Confluence",
        "meaning": "合流、一致、(人などの)集まり",
        "era": "15th Century Latin con- + fluere",
        "etymology": {
            "components": ["con- (together)", "fluere (to flow)"],
            "original_statement": "From Late Latin confluentia, from Latin confluentem (flowing together), from con- (together) + fluere (to flow)."
        },
        "concept": "Flowing together (別々の流れが、一つの場所で「合流（flow together）」すること)",
        "thinking": "異なる背景を持つ河川が、ある一点で出会い、大きな一つの流れへと変わるダイナミズム。それは地理的な現象だけでなく、複数のアイデアや運命が交差し、予期せぬ大きな力（潮流）を生み出す瞬間のメタファーでもあります。出会いは、常に新しい速度と深さを生み出します。",
        "aftertaste": "混ざり合う。個別の音は消え、そこから雄大な一つの和音が響き始める。",
        "example": "The confluence of technology and art has led to entirely new forms of media.",
        "deep_dive": { "roots": [{"term": "bhleu-", "meaning": "to swell, flow"}], "points": ["fluid（流体）や influence（影響：流れ込むこと）と同じ『流動』のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "effervescence_flow",
        "word": "Effervescence",
        "meaning": "泡立ち、活気、興奮",
        "era": "17th Century Latin ex- + fervere",
        "etymology": {
            "components": ["ex- (out)", "fervere (to boil, glow)"],
            "original_statement": "From Latin effervescentem, from effervescere (to boil up, boil over), from ex- (out) + fervescere, from fervere (to boil)."
        },
        "concept": "Boiling out (内側から「沸き立ち（boil）」、泡となって溢れ出すこと)",
        "thinking": "シャンパンの泡のように、内側にある喜びやエネルギーが抑えきれずにシュワシュワと表面へ飛び出してくる様子。それは「沸騰（boil）」が持つ熱量と、「浮遊」が持つ軽やかさが幸福に同居している状態です。あなたの命が、ただ生きているだけで楽しくてたまらない、あの瑞々しい躍動感。",
        "aftertaste": "弾ける。一瞬の輝き。けれどその泡の一つひとつに、生の悦びが凝縮されている。",
        "example": "Her natural effervescence and charm made her the life of any social gathering.",
        "deep_dive": { "roots": [{"term": "bhreu-", "meaning": "to boil, bubble"}], "points": ["fervent（熱烈な）や brew（醸造する）と同じ、熱を孕んだ変化の予感。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "liquidity_flow",
        "word": "Liquidity",
        "meaning": "流動性、(資産の)換金性、滑らかさ",
        "era": "16th Century Latin liquidus",
        "etymology": {
            "components": ["liquere (to be fluid, be liquid, be clear)"],
            "original_statement": "From Latin liquiditatem, from liquidus (fluid, moist, liquid), from liquere (to be fluid)."
        },
        "concept": "Being clear and fluid (「澄んで（clear）」いて、どこへでも流れていけること)",
        "thinking": "形にこだわらず、器（状況）に応じて自らを自由な姿に変えられる性質。経済における換金性だけでなく、思考の柔軟さ、言葉の淀みない美しさをも含みます。「水」の如くあることは、いかなる障害も包み込み、あるいは受け流して、目的の海へと辿り着くための最強の知恵です。",
        "aftertaste": "執着を捨てる。形を失うことで、あなたは宇宙のあらゆる場所を流れる水になれる。",
        "example": "Maintaining sufficient liquidity is essential for any small business to survive economic downturns.",
        "deep_dive": { "roots": [{"term": "wleik-", "meaning": "to flow"}], "points": ["liquid（液体）や relinquish（手放す：流れに任せる）とも遠い響きを共有。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "meander_flow",
        "word": "Meander",
        "meaning": "曲がりくねって流れる、(話が)あちこち飛ぶ、ぶらぶら歩く",
        "era": "16th Century Greek Maiandros",
        "etymology": {
            "components": ["Maiandros (a river in Phrygia)"],
            "original_statement": "From Latin maeander, from Greek Maiandros, the name of a river in Asia Minor noted for its winding course."
        },
        "concept": "Like the Maiandros river (あの川のように、あえて「遠回り」をして流れること)",
        "thinking": "最短距離（直線）で海を目指すのではなく、景色を楽しみ、寄り道をしながら、ゆったりと蛇行する。それは効率（Efficiency）を重視する現代社会に対する、静かなる抵抗です。話が逸れる、目的なく歩く。その「無駄な回り道」こそが、豊かな土壌を作り、人生に深い陰影と物語を与えてくれます。",
        "aftertaste": "直線にはない豊かさ。迷い、回り道をした者だけが、深い溜まり（淵）に溜まる知恵を手に入れる。",
        "example": "The small stream continues to meander slowly through the green meadows and old forests.",
        "deep_dive": { "roots": [{"term": "place name"}], "points": ["特定の川の名前が、普遍的な『動き』を表す言葉になった珍しい例。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "instill_flow",
        "word": "Instill",
        "meaning": "(思想などを)徐々に教え込む、じわじわと染み込ませる",
        "era": "16th Century Latin in- + stillare",
        "etymology": {
            "components": ["in- (into)", "stillare (to drip)"],
            "original_statement": "From Latin instillare (to drip in, drop by drop), from in- (into, in) + stillare (to drip), from stilla (a drop)."
        },
        "concept": "Dripping into (「一滴（drop）」ずつ、ゆっくりと中へ注ぎ込むこと)",
        "thinking": "力ずくで教えるのではなく、静寂の中で一滴一滴の「水滴（drop）」が岩を穿つように、長時間をかけて価値観や勇気を染み込ませること。それはまるで教育を超えた「浸透」という名の魔法です。急がなくていい。いつかその一滴が、子供の、あるいは友人の心の中で大きな清い泉になるまで。",
        "aftertaste": "静かな一滴。それはいつしか、一人の人間の世界を規定する絶対的な水源に変わる。",
        "example": "It is important to instill a sense of responsibility in children from an early age.",
        "deep_dive": { "roots": [{"term": "stei-", "meaning": "to drip, drop"}], "points": ["distill（蒸留する：滴り落ちる）や still（滴り/静止）の静かな共鳴。"] },
        "part_of_speech": "verb"
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
        print(f"Success: Added {added} words in Cycle 79.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
