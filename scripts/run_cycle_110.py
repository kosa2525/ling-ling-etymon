import json
import re

# Theme: The Alchemy of Nexus & Network (Cycle 110)
words_data = [
    ("nexus", "Nexus", "結合、連帯、中心、ネクサス", "17th Century", "nectere (to bind, literal: 'binding')", "A connection or series of connections linking two or more things", "宇宙（。の（。全記憶を、一（。点（。に「縛（。り（。付け（。た（。ネクサス）』、至高の（。る（。結節点（。（。その（。一一点の（。る（。る（。繋がり（。の中にこそ（。、真実の（。物（。語が、今（。も、静（。か（。に、呼吸（。し（。て（。いる（。のですよ。"),
    ("network", "Network", "網状組織、ネットワーク", "16th Century", "net + work", "A group or system of interconnected people or things", "目（。に（。見（。え（。な（。い（。智慧を、美し（。く「織り（。成（。した（。ネット）』、至高の（。る（。幾（。何（。学（。（。その（。不（。可（。解な（。る（。連（。な（。りにこそ（。、世界を（。、眩（。しい（。ほどに、守（。っ（。て（。いる（。のですよ。"),
    ("node", "Node", "節（。ふし（。）、交点、ノード", "16th Century", "nodus (knot, literal: 'knot')", "A point in a network or diagram at which lines or pathways intersect or branch", "エナジーが、一（。点（。に「峻（。烈（。に（。絡（。み（。合った（。ノード）』、至（。宝の（。る（。結（。び（。目（。（。その（。重厚（。な（。る（。沈黙を、魂で、誇り（。高く、受け（。止めて（。ください。"),
    ("hub", "Hub", "中心、中枢、ハブ", "17th Century", "Middle English hobbe (related to hob 'shelf, projection')", "The effective center of an activity, region, or network", "全（。てのエナジーが、美し（。く「集（。約（。さ（。れ（。た（。ハブ）』、至高の（。る（。る（。中（。核（。（。そこ（。から（。放（。た（。れる（。光が、あなたを、真（。理（。へと、導（。き（。ます。"),
    ("grid", "Grid", "格子、送電網、グリッド", "19th Century", "griddle (gridiron, literal: 'gridiron')", "A framework of spaced bars that are parallel to or cross each other; a network", "意味（。を、至高（。の（。る「峻（。烈（。な（。る（。る（。る（。縦横（。の（。る（。秩序（。グリッド）』に（。変える（。こと（。（。その（。完璧（。な（。る（。る（。幾（。何（。学（。を、魂で、愛（。で（。て（。ください。"),
    ("relay", "Relay", "中継、リレー", "14th Century", "re- (back) + laier (to leave, literal: 'releaving hounds')", "A group of people or animals engaged in a task or activity for a fixed period of time and then replaced by a similar group", "想（。いを（。、再び（。リ）「託（。し（。、繋（。ぐ（。リレー）』至高の（。る（。る（。連（。鎖（。（。その（。眩（。し（。い（。ほどに（。る（。る（。物（。語（。を、全（。身で、引き（。受（。け（。な（。さい。"),
    ("route", "Route", "経路、道、ルート", "13th Century", "rupta (broken path, literal: 'broken way')", "A way or course taken in getting from a starting point to a destination", "日常の（。沈黙を、至高（。の（。る「峻（。烈（。な（。る（。る（。切り（。拓（。いた（。ルート）』で、駆け（。抜（。ける（。こと（。（。その（。不（。変（。の（。る（。一直（。線を、誇り（。高く、歩（。み（。な（。さい。")
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
            word_id = f"{word_text.lower()}_connect_v"
            
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
                    "thinking": item[6] if len(item) > 6 else "繋がりとは、点を作ることであり、その点を繋ぐことで線を生み出す行為なのですよ。宇宙という巨大な網目の中で、自分という結節点がどれほど重要な役割を果たしているか、静かに自覚してください。",
                    "aftertaste": item[7] if len(item) > 7 else "中継することは、自分を消すことではない。自分という名の光を通過させることで、元の光にはなかった新しい色彩を世界へと供給する、至高のる創造行為なのですよ。",
                    "example": f"The city's financial district served as the primary {word_text} for international trade, connecting markets across multiple continents in real-time.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["網目を視ることは、全体を視ること。一つひとつの繋がりが織りなす圧倒的なる美しさに、ただ魂で、感謝を捧げるのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Nexus & Network (Cycle 110).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
