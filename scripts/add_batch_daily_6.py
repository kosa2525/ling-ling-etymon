import json
import re

word_batch = [
    {
        "id": "pillow",
        "word": "Pillow",
        "meaning": "枕、クッション",
        "era": "Old English pyle/Latin pulvīnus",
        "etymology": {
            "components": ["pulvīnus (cushion, swelling)"],
            "original_statement": "From Old English pyle, from Latin pulvīnus (cushion, little pillow), related to pulvīs (dust, powder)."
        },
        "concept": "A soft swelling support (柔らかく膨らんだ支え)",
        "thinking": "もともとはラテン語の「埃（dust：pulvis）」から来ているという説があります。細かなもので満たされた、ふわりと膨らんだ（swelling）袋。それは、一日の疲れから頭を解放し、夢の世界への入り口を支える最もプライベートな道具です。",
        "aftertaste": "重い思考を預け、ただの呼吸に還るためのクッション。",
        "example": "He fluffed up his pillow before drifting off to sleep.",
        "deep_dive": {
            "roots": [{"term": "pel-", "meaning": "to fill, flow"}],
            "points": ["full（満ちた）や plenty（たくさんの）と同じく、中身が『パンパンに詰まっている』様子。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "blanket",
        "word": "Blanket",
        "meaning": "毛布、一面に覆うもの",
        "era": "14th Century Old French blanc",
        "etymology": {
            "components": ["blanc (white)"],
            "original_statement": "From Old French blanquette, from blanc (white), originally meaning a 'white woolen cloth'."
        },
        "concept": "A white woolen covering (白いウールの布、真っ白な覆い)",
        "thinking": "もともとは『白い（blank/blanc）』色のウール地の布を指していました。温和な温かさで体を包み込み、外気を遮断するシェルター。そこから、雪が一面を「毛布のように（blanket coverage）」覆い尽くす比喩表現にもなりました。",
        "aftertaste": "すべてを包み込み、静寂と温もりを与える純白のヴェール。",
        "example": "The child felt safe and warm under the heavy blanket.",
        "deep_dive": {
            "roots": [{"term": "bhel-", "meaning": "to shine, burn, white"}],
            "points": ["bleach（漂白する）や blaze（炎：光るもの）と同じく、『光り輝く白』。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "candle",
        "word": "Candle",
        "meaning": "ろうそく、キャンドル",
        "era": "Old English candel/Latin candēla",
        "etymology": {
            "components": ["candēre (to shine, be white)"],
            "original_statement": "From Old English candel, from Latin candēla (a candle), from candēre (to shine, glow, be white)."
        },
        "concept": "A glowing white light (純粋に輝き、白熱するもの)",
        "thinking": "電気のない時代、闇を切り拓く唯一の友であり、その「白く輝く（candere）」様子が名前となりました。揺らめく炎は、単なる照明ではなく、祈りや瞑想、あるいは短い命の象徴としても人々の心に寄り添い続けています。",
        "aftertaste": "自らを削りながら、暗闇に小さな輪郭を刻む。",
        "example": "The soft flickering of the candle created a cozy atmosphere.",
        "deep_dive": {
            "roots": [{"term": "kand-", "meaning": "to shine, glow"}],
            "points": ["candidate（候補者：かつて選挙で『真っ白い』服を着たから）と兄弟です。誠実さは光なのです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "mirror_daily",
        "word": "Mirror",
        "meaning": "鏡、写し出す、反映する",
        "era": "13th Century Old French mireoir",
        "etymology": {
            "components": ["mirare (to look at, wonder at)"],
            "original_statement": "From Old French mireoir, from Latin mirari (to wonder at, admire, gaze at with amazement)."
        },
        "concept": "An object to behold (驚嘆の目で見つめるもの、不思議な反映)",
        "thinking": "驚きを意味する「ミラクル（miracle）」や「ミラージュ（mirage）」と、もとは同じ語源です。目の前に広がる自分の姿を「不思議の目（mirari）」で見つめること。自分を客観視し、世界をありのままに映し出す、静かな正直者。",
        "aftertaste": "嘘をつかない。ただ、世界の裏側を見せるだけ。",
        "example": "Always try to be the person you want to see in the mirror.",
        "deep_dive": {
            "roots": [{"term": "smeiros", "meaning": "smiling"}],
            "points": ["smile（微笑み）と同じ、喜びに見開かれた目。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "window_breeze",
        "word": "Window",
        "meaning": "窓、(思考などの)機会",
        "era": "13th Century Old Norse vindauga",
        "etymology": {
            "components": ["vindr (wind)", "auga (eye)"],
            "original_statement": "From Old Norse vindauga, literally 'wind-eye'."
        },
        "concept": "An eye for the wind (風の通り道、壁の瞳)",
        "thinking": "北欧の人々は、窓を「風の目（vindr-auga）」と呼びました。単なる光の入り口ではなく、家の中に風を招き入れ、外の空気を知るための感覚器官。内側で守られながら、外の世界という広がりを感じるための、透明な『瞳』なのです。",
        "aftertaste": "透明な境界線。隔たれていながら、世界と繋がっている。",
        "example": "Open the window and let some fresh air into the room.",
        "deep_dive": {
            "roots": [{"term": "okw-", "meaning": "to see"}],
            "points": ["oc-（見る）系のルーツ。壁という静寂に開けられた、一時の視界。"]
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
