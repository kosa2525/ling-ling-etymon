import json
import re

word_batch = [
    {
        "id": "bridge",
        "word": "Bridge",
        "meaning": "橋、架け橋",
        "era": "Old English brycg",
        "etymology": {
            "components": ["brycg (bridge)"],
            "original_statement": "From Old English brycg, from Proto-Germanic *brugjō."
        },
        "concept": "A connecting path over a gap (断絶を繋ぐ道)",
        "thinking": "川や谷などの、歩いて渡れない「裂け目」を飛び越えるための装置。物理だけでなく、心と心の距離を埋めること、あるいは異なる文化の間を繋ぐことも、すべて『橋』を架けることに例えられます。分断された世界を結ぶ、希望の線です。",
        "aftertaste": "二つの岸を、一本の木が、石が、あるいは想いが結ぶ。",
        "example": "Let's build a bridge to understanding between our two communities.",
        "deep_dive": {
            "roots": [{"term": "bhru-", "meaning": "brow, bridge, log"}],
            "points": ["眉毛（brow）と同じルーツを持つという説があります。目の上のアーチと、川の上のアーチの共通性です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "flower",
        "word": "Flower",
        "meaning": "花、開花する、全盛期",
        "era": "13th Century Old French/Latin flōs",
        "etymology": {
            "components": ["flōs (flower)"],
            "original_statement": "From Old French flor, from Latin flōrem (flower, blossom)."
        },
        "concept": "The blossoming peak (開花の絶頂、生命の美の追求)",
        "thinking": "生命が次世代へ繋ぐために、持てるエネルギーをすべて注ぎ込んで作り出した最高に美しい「表現」。そこから、才能が満開になる「全盛、フィジカルな美」を指します。いつか散るという儚さも、この言葉に含まれる美の一部です。",
        "aftertaste": "一瞬の輝き。それが種子へ至るために必要な、命の乱舞。",
        "example": "Spring is the season when all the flowers begin to bloom.",
        "deep_dive": {
            "roots": [{"term": "bhel-", "meaning": "to bloom, flourish, swell"}],
            "points": ["flourish（栄える）や blade（葉/刀の身）と同じく、豊かに広がる『膨らみ』がルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "river",
        "word": "River",
        "meaning": "川、河川、多量",
        "era": "12th Century Old French/Latin ripa",
        "etymology": {
            "components": ["ripa (bank, shore)"],
            "original_statement": "From Old French riviere, from Vulgar Latin *riparia (riverbank), from Latin ripa (bank)."
        },
        "concept": "That which has banks (岸辺を持っているもの)",
        "thinking": "もともとは『流れている水』ではなく、『その流れている水を支えている岸（ripa）』を指していました。岸があるからこそ、水は散逸せずに一本の奔流となれるのです。人生の急流から、涙の河まで、一定の方向を向いた膨大な「流れ」を意味します。",
        "aftertaste": "留まらないこと。岸を削りながら、ただ海へと急ぐ。",
        "example": "The river flows gently through the quiet valley village.",
        "deep_dive": {
            "roots": [{"term": "rei-", "meaning": "to scratch, tear, cut"}],
            "points": ["write（書く：削って記す）や rival（ライバル：川の岸の住人同士）と同根の『削った跡（岸）』。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "forest",
        "word": "Forest",
        "meaning": "森、森林",
        "era": "13th Century Old French/Latin foris",
        "etymology": {
            "components": ["foris (outside, out of doors)"],
            "original_statement": "From Old French forest, from Late Latin forestis (silva) (the outside wood), from Latin foris (outside, outdoors)."
        },
        "concept": "The space outside the fence (柵の向こう側の、手付かずの外部領域)",
        "thinking": "単に木が生えているだけではなく、人間が管理する居住区（城内や農園）の「外側（outside：foris）」にある、野生と神秘が支配する未開の領域。昔の人にとって森は、いつだって文明への扉の『外』に広がる未知の暗闇でした。",
        "aftertaste": "一歩踏み出せば、文明の法（ルール）が届かない緑の迷宮。",
        "example": "Deep in the forest, ancient trees told their silent stories.",
        "deep_dive": {
            "roots": [{"term": "dhwer-", "meaning": "door"}],
            "points": ["foreign（外国の、外からの）や door（ドア：外への出口）のファミリーです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "shadow",
        "word": "Shadow",
        "meaning": "影、日陰、暗い部分",
        "era": "Old English sceadu",
        "etymology": {
            "components": ["sceadu (shadow, shade, darkness)"],
            "original_statement": "From Old English sceadu (shadow, shade, darkness), from Proto-Germanic *skadwaz."
        },
        "concept": "A protection from the light (光からの遮蔽、守り、日陰)",
        "thinking": "不気味な暗がりという意味よりも、強烈な日差しを遮ってくれる涼しい「日陰（shade）」としての守りの意味がベース。しかし、物に付きまとう切っても切れない鏡像としての影もあり、心の中の認められない暗部（ユング的シャドウ）としても使われます。",
        "aftertaste": "光を遮った場所にしか存在し得ない、あなたという静かな実像。",
        "example": "The long shadows stretched across the lawn at sunset.",
        "deep_dive": {
            "roots": [{"term": "skot-", "meaning": "shadow, darkness"}],
            "points": ["ske-（覆う）という語根から。スカイ（sky）や靴（shoe）と同じ『覆うもの』の仲間。"]
        },
        "part_of_speech": "noun"
    }
]

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
    if match:
        prefix = match.group(1)
        json_array_str = match.group(2)
        suffix = match.group(3)
        
        words = json.loads(json_array_str)
        existing_ids = {w.get("id") for w in words}
        
        added_count = 0
        for item in word_batch:
            if item["id"] not in existing_ids:
                words.append(item)
                added_count += 1
                
        new_json_str = json.dumps(words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Success: Added {added_count} words.")
    else:
        print("Error: Could not find WORDS array in data.js.")
except Exception as e:
    print(f"Error: {e}")
