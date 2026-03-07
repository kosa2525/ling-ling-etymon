import json
import re

word_batch = [
    {
        "id": "parody_art",
        "word": "Parody",
        "meaning": "パロディ、滑稽な模倣",
        "era": "16th Century Latin/Greek paroidia",
        "etymology": {
            "components": ["para- (beside, along side)", "oide (song, chant)"],
            "original_statement": "From Latin parodia, from Greek paroidia (burlesque song), from para- (beside) + oide (song)."
        },
        "concept": "A song sung alongside another (本物の「横（para-）」で歌われる歌)",
        "thinking": "本来は、厳かな「歌（ode）」を、あえてその「すぐ横（para-）」で少し調子を狂わせて歌い、ユーモアを引き出す技法。それはオリジナルの価値を認めた上での、知的な遊び心であり、茶目っ気たっぷりの模倣です。",
        "aftertaste": "本物への敬意を、少しの毒と笑いに変えて、横から歌う。",
        "example": "The movie is a hilarious parody of classic spy films.",
        "deep_dive": {
            "roots": [{"term": "aweid-", "meaning": "to sing"}],
            "points": ["ode（頌歌）や melody（メロディー：歌われるもの）と同じ、歌の系譜。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "sketch_art",
        "word": "Sketch",
        "meaning": "スケッチ、下書き、寸劇",
        "era": "17th Century Dutch/Greek skhedios",
        "etymology": {
            "components": ["skhedios (temporary, done on the spur of the moment)"],
            "original_statement": "From Dutch schets, from Italian schizzo, from Latin schedium, from Greek skhedios (temporary, casual, done offhand)."
        },
        "concept": "Something done on the spur of the moment (その場の勢いで描かれた、一時的なもの)",
        "thinking": "完成品ではなく、その瞬間の躍動感や本質を「パッと思い立って（offhand）」捉えた断片。それは、作り込まないからこそ宿る、嘘のない生（なま）のリアリティ。未完成であることに美徳を置く、軽やかな表現の形式です。",
        "aftertaste": "時間は止まらない。その一瞬の震えを、ただ線で留めておく。",
        "example": "He made a quick charcoal sketch of the woman on the train.",
        "deep_dive": {
            "roots": [{"term": "segh-", "meaning": "to hold"}],
            "points": ["scheme（計画：持っている形）と同じ。ある形を『保持する』努力。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "sculpture_art",
        "word": "Sculpture",
        "meaning": "彫刻、彫像",
        "era": "14th Century Latin sculptus",
        "etymology": {
            "components": ["sculpere (to carve, cut out)"],
            "original_statement": "From Latin sculptura (art of carving), from sculpere (to carve, engrave)."
        },
        "concept": "The art of carving out (外部を削り取って、真の姿を「切り出す」こと)",
        "thinking": "何かを付け足すのではなく、余分なものを「削り取る（carve）」ことで、中に隠れていた形を露わにする芸術。ミケランジェロが「石の中に閉じ込められていた天使を救い出しただけだ」と言ったように、マイナスの作業から生まれる、究極の存在美。",
        "aftertaste": "石の中に眠る魂。不要なすべてを削ぎ落として、真髄へと至る。",
        "example": "The museum features an impressive collection of ancient Greek sculptures.",
        "deep_dive": {
            "roots": [{"term": "skelp-", "meaning": "to cut"}],
            "points": ["scalpel（メス：切る道具）や shell（貝：切り離された殻）と同族の、鋭い切断の情熱。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "gallery_art",
        "word": "Gallery",
        "meaning": "ギャラリー、回廊、画廊",
        "era": "15th Century Old French/Latin galilaea",
        "etymology": {
            "components": ["Galilee (region in the Holy Land) - perhaps as a porch or entrance"],
            "original_statement": "Possibly from Medieval Latin galilaea (Galilee), often used as a name for a church porch or entrance-hall."
        },
        "concept": "A porch or porch-like walkway (屋根のある回廊、教会への入り口)",
        "thinking": "もともとは、教会の入り口付近にある「細長い通路（porch）」のこと。やがて、その壁に美しい絵が並べられるようになり、芸術を鑑賞するための静かな空間としての「ギャラリー」になりました。一歩ずつ歩きながら、異世界に触れるための聖域への助走通路。",
        "aftertaste": "静寂の中、壁に並んだ数百の視線を浴びながら歩く道。",
        "example": "The art gallery in the city center has free admission on Sundays.",
        "deep_dive": {
            "roots": [],
            "points": ["聖地ガリラヤ（Galilee）の名前から。未信者が待機する『外側』の場所という説もあります。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "curator_art",
        "word": "Curator",
        "meaning": "キュレーター、学芸員、管理者",
        "era": "14th Century Latin curare",
        "etymology": {
            "components": ["curare (to take care of)"],
            "original_statement": "From Latin curator (overseer, manager), from curatus, past participle of curare (to take care of)."
        },
        "concept": "One who takes care of things (慈しみ、世話をする者)",
        "thinking": "展示の企画者というだけでなく、本来は「心を込めて世話をする（care）」人。放置すれば風化し、忘れ去られる文化の欠片を、愛をもって保護し、価値を再定義し、未来へと健康なまま届けるための「魂の番人（guardian）」です。",
        "aftertaste": "散らばった点に、ケアと愛を注いで一本の物語として繋ぐ。",
        "example": "The curator spent months organizing the modern sculpture exhibition.",
        "deep_dive": {
            "roots": [{"term": "koizu-", "meaning": "care"}],
            "points": ["cure（治療する）や accurate（正確な：しっかり手入れされた）の cur- です。"]
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
