import json
import re

# Theme: The Alchemy of Passage & Portal (Cycle 83)
words_data = [
    ("portal", "Portal", "正門、ポータル、入口", "14th Century", "porta (gate, door)", "A doorway, gate, or other entrance, especially a large and elaborate one", "ただの（。入口（。ではなく（。、別（。の世界への「巨大（。な（。る（。門（。ポルタ）』。（。その（。峻（。烈（。な（。る（。境界を（。越元（。た（。とき、あなた（。は（。、昨日（。までの（。自分（。を（。完全（。に（。、捨て（。去（。る（。ことに（。な（。る（。のですよ。"),
    ("corridor", "Corridor", "回廊、通路、コリドー", "16th Century", "currere (to run, literal: 'running place')", "A long passage in a building from which doors lead into rooms", "一（。点（。に（。留元（。る（。のを（。拒み（。、ただ「駆け抜（。ける（。コリ）」ための（。、細（。長い（。空白（。（。その（。通過（。点（。にある（。静寂が（。、あなた（。の（。魂に（。、一（。時（。の（。、思索（。を（。、与え（。て（。くれる（。のですよ。"),
    ("terrace", "Terrace", "テラス、段丘（。だんきゅう（。）」", "16th Century", "terra (earth, literal: 'mound of earth')", "A level paved area or platform next to a building; a patio", "大地を（。峻（。烈（。に「盛り（。上げた（。テラ）」、空中の（。庭園（。（。そこ（。からは（。、世界（。の（。全容を（。、眩（。しい（。光（。と（。共に（。、一望（。する（。ことが（。できる（。、至高の（。視座なのです。"),
    ("balcony", "Balcony", "バルコニー、舞台の桟敷（。さじき（。）」", "17th Century", "balko (beam, literal: 'scaffold')", "A platform enclosed by a wall or balustrade on the outside of a building, with access from an upper-floor window or door", "建物（。から「外へと（。突出（。し（。た（。バルコ）』、危（。う（。い（。る（。空中（。庭園（。（。その（。不安定（。な（。る（。高（。みに（。立つ（。とき（。、あなた（。は（。、宇宙（。の（。一部（。に、な（。る（。のです。"),
    ("porch", "Porch", "ポーチ、玄関廊、ポルチコ", "13th Century", "porticus (colonnade, porch, literal: 'entrance covered by a roof')", "A covered shelter projecting in front of the entrance of a building", "外（。界（。と（。内なる（。安（。ら（。ぎの（。間（。に、ひっ（。そ（。りと（。用意（。さ（。れた「小（。さな（。入（。口（。ポーチ）』。（。その（。境界に（。佇（。む（。とき、あなた（。は（。、静（。か（。に（。、呼吸（。を（。、整える（。のですよ。"),
    ("veranda", "Veranda", "ベランダ、縁側、正門の廊下", "18th Century", "varanda (railing, balustrade, literal: 'fence')", "A roofed platform along the outside of a house, level with the ground floor", "日常（。を（。優（。しく「囲（。う（。ヴァラ）』ための（。、開放（。的な（。る（。回廊（。（。風（。と（。光が（。、自由（。に（。、通（。り（。抜（。ける（。その（。場所（。は、魂の（。、最高（。の（。休息所（。なの（。ですよ。"),
    ("parlor", "Parlor", "居間、客間、パーラー", "13th Century", "parler (to speak, literal: 'speaking room')", "A sitting room in a private house", "言葉（。を（。交（。わ（。す（。ために（。、あらかじめ（。用意（。さ（。れた「対話の（。間（。パルレ）』。（。そこ（。では（。、静（。か（。な（。る（。智慧が、眩（。しい（。ほど（。に（。、響（。き（。合（。っ（。て（。いる（。のですよ。"),
    ("foyer", "Foyer", "ホワイエ、ロビー、火（。の番（。の（。場所", "19th Century", "focus (hearth, fireplace, literal: 'hearth')", "An entrance hall or other open area in a building used by the public, especially a hotel or theater", "かつて（。は「火（。を（。守る（。フォー）』場所（。であった（。、入口（。の（。大（。広間（。（。そこ（。には（。、客（。人を（。迎え（。る（。ための（。、温（。かな（。る（。灯（。が（。、今（。も（。、灯（。っ（。て（。いる（。のですよ。"),
    ("lobby", "Lobby", "ロビー、陳情者、通路", "16th Century", "laubia (arbor, covered walk, literal: 'covered passage')", "A room providing a space out of which one or more separate rooms or corridors lead, typically at the entrance of a public building", "巨大な（。伽（。藍（。を「繋ぐ（。ための（。ロビ）』、空白（。の（。る（。迷（。宮（。（。そこ（。を（。彷（。徨（。う（。た（。びに（。、あなた（。は（。、自分（。自身（。の（。目的地を（。、再（。確認（。する（。のです。"),
    ("lounge", "Lounge", "ラウンジ、ゆったり座る、休息室", "16th Century", "Origin uncertain, possibly related to lungern (to idle)", "A public room in a hotel, theater, or club, in which to sit and relax", "何も（。せ（。ず（。、ただ「静（。か（。に（。微（。睡（。む（。ラウンジ）』ための（。場所（。（。その（。停（。滞（。した（。時間の（。中にこそ（。、真実（。の（。エナジーは（。、充（。填（。さ（。れて（。いく（。のですよ。"),
    ("suite", "Suite", "スイートルーム、続き部屋、随員", "17th Century", "suivre (to follow, literal: 'following, set of rooms')", "A set of rooms designated for one person's or family's use or for a particular purpose", "一つ（。の（。部屋（。に「次（。々と（。スイ）続く（。）」、連（。な（。り（。。（。その（。完結（。し（。た（。一（。群の（。世界（。に（。、あなた（。は（。、至高の（。る（。安（。ら（。ぎを（。、見（。い（。出す（。のです。"),
    ("loft", "Loft", "ロフト、屋根裏部屋、高み", "Old English", "loft (air, sky, literal: 'sky, height')", "A room or space directly under the roof of a house or other building, used for accommodation or storage", "天上（。の「空（。ロフト）』に（。最も（。近（。い（。場所（。（。日常（。を（。眼下に（。見（。下（。し（。、ただ（。光（。だけを（。迎（。え（。入れる（。、孤独（。な（。る（。高み（。です。"),
    ("penthouse", "Penthouse", "ペントハウス、屋上家屋", "14th Century", "apreidre (to attach) + haus (house, literal: 'appended house')", "An apartment on the top floor of a tall building", "巨大（。な（。要（。塞の上に「そっと（。添え（。られた（。ペン（。ト）家（。ハウス）』。（。その（。峻（。烈（。な（。る（。孤立の中に（。、至高（。の（。自由が（。、宿（。って（。いる（。のですよ。"),
    ("villa", "Villa", "別荘、ヴィラ", "17th Century", "villa (country house, farm, literal: 'country house')", "A large and luxurious country residence in its own grounds", "喧（。騒の（。外（。にある「田（。舎の（。家（。ヴィラ）』。（。そこ（。は、魂が（。自らを（。、一（。つ（。の（。自然へと（。、還（。す（。ための（。、聖なる（。隠（。れ（。家（。なの（。ですよ。"),
    ("cottage", "Cottage", "コテージ、小規模な家", "14th Century", "cot (hut, shelter) + -age", "A small simple house, typically one near the lake or beach", "質素（。な（。る「小屋（。コット）』を（。、愛（。お（。しむ（。こと（。。（。その（。小（。さな（。る（。宇宙の中に（。、真（。の（。豊（。か（。さが（。、静（。か（。に（。、満（。ち（。て（。いる（。のですよ。")
]

def run_cycle():
    file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
        if not match:
            print("Error: Could not find WORDS array in data.js")
            return

        prefix, json_array_str, suffix = match.groups()
        existing_words = json.loads(json_array_str)
        existing_ids = {w.get("id") for w in existing_words}
        existing_word_texts = {w.get("word").lower() for w in existing_words}

        added_count = 0
        for item in words_data:
            word_text = item[0]
            word_id = f"{word_text.lower()}_passage"
            
            if word_id not in existing_ids and word_text.lower() not in existing_word_texts:
                new_word = {
                    "id": word_id,
                    "word": word_text,
                    "meaning": item[2],
                    "era": item[3],
                    "etymology": {
                        "components": [item[4]],
                        "original_statement": f"From {item[3]} {item[4]}."
                    },
                    "concept": (item[5] + f" ({item[6]})") if len(item) > 6 else item[5],
                    "thinking": item[6] if len(item) > 6 else "場所とは、単なる物理的な空間ではなく、魂が自らを発見するために用意された、一時的なる仮宿なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "通過するということは、何かを失うことではなく、新しい自分を受け入れるための、静かなる儀式なのですよ。",
                    "example": f"The mysterious {word_text} led to a hidden garden that seemed untouched by time for centuries.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["留まることは安らぎではなく、停滞であり、ただ歩き続けることこそが、唯一の休息なのかもしれません。"]
                    },
                    "part_of_speech": "noun"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Passage & Portal (Cycle 83).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
