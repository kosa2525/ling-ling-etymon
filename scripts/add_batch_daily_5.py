import json
import re

word_batch = [
    {
        "id": "mirror",
        "word": "Mirror",
        "meaning": "鏡、反映、写し出す",
        "era": "13th Century Old French/Latin mirari",
        "etymology": {
            "components": ["mirari (to wonder at, admire)"],
            "original_statement": "From Old French mireoir, from Latin mirari (to wonder at, look at with amazement)."
        },
        "concept": "Something to wonder at (驚きの目で見つめるもの)",
        "thinking": "鏡の語源は「驚嘆する（mirari）」こと。初めて自分の姿を客観的に見た時のあの不思議な感覚。それは自分自身の内面を冷静に映し出す「誠実さの象徴」でもあり、反対に「自惚れ（vanity）」の象徴でもあります。対象を等身大に写し取る装置です。",
        "aftertaste": "二つの目が、もう二つの目に出会う奇跡。",
        "example": "His eyes in the mirror were tired but determined.",
        "deep_dive": {
            "roots": [{"term": "smeiros", "meaning": "to smile"}],
            "points": ["smile（微笑み）や miracle（奇跡）と同じく、心が思わず動くきらめきの源泉。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "window",
        "word": "Window",
        "meaning": "窓、(思考などの)機会",
        "era": "13th Century Old Norse vindauga",
        "etymology": {
            "components": ["vindr (wind)", "auga (eye)"],
            "original_statement": "From Old Norse vindauga, literally 'wind-eye' (wind + eye)."
        },
        "concept": "The eye of the wind (風の目)",
        "thinking": "ガラスが普及する前、窓は単なる「壁に開いた穴」であり、そこから風が家の中に入り込む場所でした。それを「風の目（eye of the wind）」と呼んだ北欧の人々の感性がこの言葉に宿っています。内なる安全な場所から、外の世界という広がりを覗き見るための、透明な境界です。",
        "aftertaste": "閉めれば自分を守る壁になり、開ければ空を繋ぐ道になる。",
        "example": "A single window can change the entire feel of a room.",
        "deep_dive": {
            "roots": [{"term": "okw-", "meaning": "to see"}],
            "points": ["eye（目）のルーツ、オフト（oc-）が隠れています。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "garden",
        "word": "Garden",
        "meaning": "庭、庭園",
        "era": "14th Century Old French/Germanic gart",
        "etymology": {
            "components": ["gart (enclosure)"],
            "original_statement": "From Old North French gardin, from Germanic gart (enclosure, yard)."
        },
        "concept": "An enclosed space (囲い込まれた神聖な場所)",
        "thinking": "むき出しの野生の森（forest）とは対極にある、人間が柵で「囲い（enclosure）」を作って慈しみ育てた自然の断片。管理された美しさと、そこから生まれる心の安らぎ。自分だけの小さな楽園（paradise）を意味します。",
        "aftertaste": "柵の向こうに。手なづけられた、穏やかな宇宙の断片。",
        "example": "She grows beautiful roses in her small town garden.",
        "deep_dive": {
            "roots": [{"term": "gher-", "meaning": "to grasp, enclose"}],
            "points": ["yard（ヤード/中庭）や court（法廷/宮廷：四角い囲み）と同じ一族。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "village",
        "word": "Village",
        "meaning": "村、集落",
        "era": "14th Century Old French/Latin villa",
        "etymology": {
            "components": ["villa (country house, farm)"],
            "original_statement": "From Old French village, from ville (farmhouse, villa), from Latin villa (country house, estate)."
        },
        "concept": "A collection of farmhouses (別荘や農園の集まり)",
        "thinking": "都会（City）のような巨大な仕組みではなく、もともとは田舎の「一軒の農家（villa）」が集まってできた小さな集団。お互いの顔が見える範囲での、最も原初的で強固な相互扶助のコミュニティ。どこか懐かしく温かい共同体の響きを持っています。",
        "aftertaste": "歩いて渡れる距離の信頼。小さな灯火の寄り合い。",
        "example": "He grew up in a small, peaceful fishing village by the sea.",
        "deep_dive": {
            "roots": [{"term": "weik-", "meaning": "clan, house"}],
            "points": ["vicinity（近隣）や viceroy（副王：かつての別邸の主）と同じく『家』をベースとしたつながり。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "path",
        "word": "Path",
        "meaning": "小道、進路、生き方",
        "era": "Old English path",
        "etymology": {
            "components": ["paþ (way, path)"],
            "original_statement": "From Old English paþ, from West Germanic patha- (way, path, footway)."
        },
        "concept": "A trodden way (踏み固められた足跡)",
        "thinking": "立派な舗装道路よりも、誰かが歩いたことで自然と出来上がった「踏み跡」を意味します。最初の一人が歩き、次の人がそれをなぞったことでできた線。それは、私たちが選び取っていく「独自の人生の歩み」そのものです。",
        "aftertaste": "誰もいない草原に、昨日の一歩が道を作る。",
        "example": "Focus on your own path, not those of others around you.",
        "deep_dive": {
            "roots": [{"term": "pent-", "meaning": "to go, tread, find a way"}],
            "points": ["find（見つける）や bridge（橋）に近い遠い語源を持つ、探索と発見の歩み。"]
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
