import json
import re

# Theme: The Alchemy of Pontiff & Passage (Cycle 115)
words_data = [
    ("pontiff", "Pontiff", "司教、教皇、ポンティフ", "16th Century", "pons (bridge) + facere (to make, literal: 'bridge-maker')", "The Pope; a prelate", "天（。と（。地を（。繋（。ぐ「架け（。橋を（。作る（。者（。ポンス・ファカーレ）』、至高の（。る（。媒介（。者（。（。その（。峻（。烈（。な（。る（。る（。祈りが（。、宇宙の（。深（。淵（。を、美し（。き（。る（。秩序へと（。、還（。し（。ます。"),
    ("viaduct", "Viaduct", "高架橋、ビアダクト", "19th Century", "via (way) + ducere (to lead, literal: 'leading a way')", "A long bridge-like structure, typically a series of arches, carrying a road or railroad across a valley or other low ground", "遥（。かな（。る（。高（。みへと、峻（。烈（。に「道（。を（。導（。く（。ヴィア・ドゥ）』、至高の（。る（。空中（。回廊（。（。そこ（。を（。駆（。け（。抜ける（。とき、日常（。の（。重みを、あなたは（。、完全（。に（。脱（。し（。ます。"),
    ("aqueduct", "Aqueduct", "導水路、アケダクト", "16th Century", "aqua (water) + ducere (to lead, literal: 'leading water')", "An artificial channel for conveying water, typically in the form of a bridge across a valley or other gap", "生命の（。潤（。いを「導（。き（。寄（。せ（。る（。アクア・ドゥ）』至高の（。る（。る（。る（。管（。（。その（。静（。か（。な（。なる（。る（。る（。る（。奔流（。の中にこそ、宇宙（。の（。記憶は（。、永遠に、刻（。ま（。れ（。て（。いる（。のですよ。"),
    ("causeway", "Causeway", "築き道、土手道、コーズウェイ", "15th Century", "caucie (raised way) + way", "A raised road or track across low or wet ground", "困難な（。る「湿（。地をを、峻（。烈（。に（。突き（。抜ける（。ための（。る（。土手（。道（。コーズウェイ）』。（。その（。不（。動の（。意志に、魂は、静（。か（。に、安（。らぎを（。、見（。出し（。ます。"),
    ("jetty", "Jetty", "防波堤、桟橋、ジェッティ", "14th Century", "jeter (to throw, literal: 'something thrown out')", "A landing stage or small pier at which boats can dock or be moored", "海（。へと、峻（。烈（。に「投（。げ（。出（。さ（。れた（。ジェッティ）』至高の（。る（。最（。先端（。（。その（。潮（。風に、あなた（。は（。、真実（。の（。る（。る（。る（。る（。予感を、抱（。き（。な（。さい。"),
    ("pier", "Pier", "桟橋、ピア", "12th Century", "pera (stone, pillar, literal: 'stone structure')", "A structure leading out from the shore into a body of water, in particular", "波（。をを「峻（。烈（。に（。受（。け（。止める（。ピア）』、至高の（。る（。る（。柱（。（。その（。不（。変（。の（。る（。る（。る（。る（。る（。忍耐（。をを、誇り（。高く、魂で、肯定（。し（。て（。ください。"),
    ("dock", "Dock", "ドック、船渠（。せんきょ（。）」、格納庫", "14th Century", "Middle Dutch docke (related to Latin ducere 'to lead')", "A structure extending from the shore over water, used as a landing place for ships and boats", "旅（。を終（。え、エナジーを、静（。か（。に「収（。容（。する（。ドック）』、至高の（。る（。休息（。（。その（。重（。厚（。な（。る（。る（。沈黙（。の中にこそ、次（。なる（。飛躍の（。る（。種子が、宿（。ります。"),
    ("wharf", "Wharf", "埠頭、ワーフ", "Old English", "hwearf (shore, bank, literal: 'embankment')", "A level quayside area to which a ship may be moored to load and unload", "大地の（。峻（。烈（。な（。る「淵（。源（。ワーフ）』、至高の（。る（。る（。境界（。（。そこ（。には、物（。資と（。共に、宇宙（。の（。る（。記憶が（。、静（。か（。に、集積（。さ（。れ（。て（。いる（。のですよ。")
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
            word_id = f"{word_text.lower()}_bridge_iv"
            
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
                    "thinking": item[6] if len(item) > 6 else "架け橋とは、分断された世界を繋ぎ止めるための、魂の至高のる挑戦なのですよ。それを作る者は、自らがその橋の一部になるという覚悟を持たなければなりません。",
                    "aftertaste": item[7] if len(item) > 7 else "埠頭に立つことは、境界を知ること。自分がどこから来て、どこへ行こうとしているのか、波の音を聴きながら、静かに自らに問いかけてみてください。",
                    "example": f"The majestic {word_text} spanned across the narrow valley, providing a vital transportation link between the isolated mountain villages and the bustling coastal city.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["道を導くことは、自分を誇示することではありません。他者がそこを安全に渡れるように、自らが不変なる土台となる、至高のる慈悲の形式なのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Pontiff & Passage (Cycle 115).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
