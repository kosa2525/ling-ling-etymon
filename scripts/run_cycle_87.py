import json
import re

# Theme: The Alchemy of Virtue & Excellence (Cycle 87)
words_data = [
    ("excellence", "Excellence", "卓越、優秀、エクセレンス", "14th Century", "ex- (out) + cellere (to rise, literal: 'rising out')", "Outstanding quality", "誰（。も（。が（。見上げる（。、「峻（。烈（。な（。る（。高（。み（。へと（。、自ら（。を（。、押し（。上げ（。た（。姿（。エクセル）』。（。それは（。、ただ（。一一点（。を（。追求（。し（。続け（。た（。、魂の（。、至高（。の（。る（。均衡の（。、果て（。に（。ある（。のですよ。"),
    ("dignity", "Dignity", "尊厳、威厳、ディグニティ", "13th Century", "dignus (worthy)", "The state or quality of being worthy of honor or respect", "あなたという（。存在（。その（。もの（。に（。、あらかじめ（。備（。わ（。っ（。て（。いる（。、「至高の（。価値（。ディグヌス）』。（。何（。物（。にも（。汚（。さ（。れ（。な（。い（。その（。気高い（。る（。沈黙を（。、静（。か（。に（。、守（。り（。抜く（。のですよ。"),
    ("renown", "Renown", "名声、リナウン", "14th Century", "re- (again) + nommer (to name, literal: 'named again')", "Condition of being known by many", "幾（。重（。にも（。繰（。り（。返（。し「その（。名前を（。呼ば（。れる（。リナウン）」こと（。。（。その（。眩（。し（。い（。余韻が（。、世界（。の（。すみ（。ず（。み（。に（。まで、響（。き（。渡（。っ（。ている（。、物語（。の（。証（。です。"),
    ("prestige", "Prestige", "威信、名声、プレステージ", "17th Century", "praestigiae (juggler's tricks, illusion, literal: 'dazzling')", "Widespread respect and admiration", "世界（。を（。一瞬にして（。、「眩（。惑（。さ（。せる（。プレスティ）』、至高（。の（。る（。輝き。（。その（。圧倒（。的な（。る（。存在（。感に（。、人々は（。、畏（。敬（。の（。念を（。抱（。き（。、静（。か（。に（。、跪（。く（。のですよ。"),
    ("scheme", "Scheme", "計画、体系、スキーム", "16th Century", "skhema (form, figure, literal: 'the way it is')", "A systematic plan or arrangement", "ただの（。計画を（。越（。え（。た（。、「至高の（。設計（。図（。スキーム）』。（。その（。緻（。密（。な（。る（。繋（。が（。りの中に（。、宇宙の（。数学（。的（。な（。美（。し（。さが（。、静（。かに（。、宿（。って（。いる（。のですよ。"),
    ("method", "Method", "方法、秩序、メソッド", "16th Century", "meta- (after) + hodos (way, literal: 'way after')", "A systematic way of doing something", "真理を（。追い（。求（。め（。て（。、正しい「道（。ホドス）の（。後（。メタ）を（。行く（。）」こと（。。（。その（。峻（。烈（。な（。る（。秩序（。が（。、あなた（。を（。、不（。確実な（。る（。日常（。から（。、救（。い（。出す（。のですよ。"),
    ("manner", "Manner", "方法、態度、マナー", "13th Century", "manus (hand, literal: 'handling')", "A way in which a thing is done", "あなたの（。魂が（。、世界（。を「手（。マヌス）で（。扱う（。）」、優（。し（。い（。所（。作（。（。一（。つ（。一（。つ（。の（。振（。る（。舞（。いの中に（。、あなた（。の（。本当の（。る（。品格（。が（。、静（。か（。に（。、宿（。る（。のですよ。"),
    ("mode", "Mode", "様式、方法、モード", "14th Century", "modus (measure, literal: 'measure')", "A way or manner in which something occurs", "日常（。を（。正しい「尺（。度（。モード）』で（。、調（。節（。し（。、奏（。で（。る（。こと（。。（。その（。眩（。し（。い（。共鳴（。が（。ある（。か（。ら（。こそ（。、あなた（。の（。命は、これ（。ほど（。に（。、眩（。しい（。の（。ですよ。"),
    ("figure", "Figure", "図形、姿、フィギュア", "13th Century", "fingere (to form, fashion, literal: 'shaped thing')", "A number or shape", "魂の（。エナジーを、美し（。い「かたち（。フィギュラ）』に（。落（。と（。し（。込（。ん（。だ（。姿（。（。その（。一一点（。の（。輪郭にこそ（。、真（。実（。の（。メッセージが（。、刻ま（。れて（。いる（。のですよ。"),
    ("frame", "Frame", "枠組み、構造、フレーム", "Old English", "framian (to progress, construct, literal: 'to prepare')", "A structure that surrounds something", "全（。てを（。一（。つ（。の（。秩序（。に「整（。え（。る（。ための（。枠（。フレミ）』。（。その（。盤（。石（。な（。る（。土台（。が（。ある（。から（。こそ（。、あなた（。の（。想（。いは（。、遥（。かな（。る（。高（。みへと、昇（。る（。ことができる（。のですよ。"),
    ("fabric", "Fabric", "織物、構造、ファブリック", "15th Century", "fabrica (workshop, construction, literal: 'skilled work')", "Cloth or other material produced by weaving", "宇宙（。の（。全記憶を（。、丹（。念（。に「織（。り（。上げ（。た（。ファー）構造（。。（。その（。精（。密（。な（。る（。肌触（。りに（。、魂が（。触れた（。とき、日常（。は（。、至高（。の（。る（。神殿（。へと（。変元（。り（。ます。"),
    ("status", "Status", "地位、ステータス", "17th Century", "stare (to stand, literal: 'standing position')", "Social or professional standing", "あなたが（。今、誇り（。高く「立（。っ（。て（。いる（。ステイ）』、一（。点（。（。その（。峻（。烈（。な（。る（。存在（。感（。が（。、世界（。を（。、美し（。く（。、規定（。し（。て（。いく（。のですよ。"),
    ("system", "System", "体系、システム", "17th Century", "sun- (together) + histanai (to stand, literal: 'placed together')", "A set of parts working as a whole", "バラバラ（。の（。エナジーを「共（。に（。シン）立（。た（。せ（。た（。テム）』、巨大な（。る（。秩序（。（。その（。一（。つ（。の（。幾何学が（。、停（。滞（。し（。た（。世界に（。、命（。を（。、吹き（。込む（。のですよ。"),
    ("structure", "Structure", "構造、ストラクチャー", "15th Century", "struere (to build, literal: 'building')", "The arrangement of parts or elements", "欠（。片を（。一（。つ（。一（。つ「組（。み（。上げて（。いく（。ストル）』、至高の（。る（。建築（。（。その（。内部（。に（。、あなた（。は（。、今日（。何（。色（。の（。、光を（。、灯（。し（。た（。の（。でしょうか。")
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
            word_id = f"{word_text.lower()}_virtue"
            
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
                    "thinking": item[6] if len(item) > 6 else "卓越とは、他人に勝つことではなく、昨日の自分という名の影を、眩しい光で塗り替えていく行為なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "尊厳は、誰かに与えられるものではない。自らの魂の純粋さを信じ抜いた者の背中に、静かに宿る光の輪なのですよ。",
                    "example": f"The architectural {word_text} of the ancient temple was a testament to the advanced engineering skills of the civilization.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["かたちを整えることは、魂を整えること。メソッドとは、真理へと至るための、美しき巡礼の道なのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Virtue & Excellence (Cycle 87).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
