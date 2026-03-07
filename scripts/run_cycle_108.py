import json
import re

# Theme: The Alchemy of Portal & Passage II (Cycle 108)
words_data = [
    ("corridor", "Corridor", "回廊、通路、コリドー", "16th Century", "correre (to run, literal: 'running place')", "A long passage in a building from which doors lead into rooms", "宇宙（。の（。時間を、峻（。烈（。に「駆（。け（。抜ける（。ための（。る（。る（。道（。コリ）』。（。その（。不（。変の（。る（。連（。な（。り（。を歩（。む（。とき、あなた（。は（。、真実（。の（。る（。自分自身へと（。、還（。る（。のですよ。"),
    ("hallway", "Hallway", "玄関、廊下、ホールウェイ", "19th Century", "hall + way", "An interior passage or corridor onto which rooms open", "物語（。と（。物語の（。間に（。作（。られた、至高の（。る「中（。間領域（。ホール）』。（。そこを（。通（。る（。た（。びに、魂は（。、日常の（。重みを、静（。か（。に（。脱（。して（。いく（。のです。"),
    ("porch", "Porch", "ポーチ、玄関、車寄せ", "13th Century", "porticus (colonnade, porch, literal: 'entrance')", "A covered shelter projecting in front of the entrance of a building", "外界（。と（。内（。界を、優（。しく「隔（。て（。る（。ポルティ）』至高の（。る（。境界（。（。そこ（。に（。佇（。む（。とき（。、あなた（。は（。、宇宙の（。囁（。きを、最も（。、美し（。く（。聴く（。ことができる（。のですよ。"),
    ("patio", "Patio", "パティオ、中庭、裏庭", "19th Century", "patio (inner courtyard, literal: 'lying open')", "A paved outdoor area adjoining a house", "天（。上の（。光を、自（。らの（。内に「受け（。入れた（。パティオ）』至高の（。る（。聖域（。（。その（。開（。か（。れた（。る（。る（。沈黙を、魂で、誇り（。高く、享受（。して（。ください。"),
    ("deck", "Deck", "デッキ、甲板、舞台、デキ", "15th Century", "decken (to cover, literal: 'covering, roof')", "A structure of planks or metal sections forming the floor of a ship or boat", "荒波を（。峻（。烈（。に「覆（。い（。隠（。す（。デキ）』、至高の（。る（。舞台（。（。その（。一一点（。に（。立ち、あなた（。は（。、自（。らの（。運命（。という（。名の（。、舵を（。、引き（。受ける（。のですよ。"),
    ("balcony", "Balcony", "バルコニー、露台、バルコニー", "17th Century", "balcone (scaffold, literal: 'large beam')", "A platform enclosed by a wall or balustrade on the outside of a building, with access from an upper-floor window or door", "高（。みへと、自らを（。峻（。烈（。に「押し（。上げ（。た（。バルコニー）』至高の（。る（。視点（。（。そこから（。、世界を（。視（。る（。とき、全ては、美し（。い（。る（。る（。る（。光の（。粒（。へと、還（。ります。")
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
            word_id = f"{word_text.lower()}_threshold_ii"
            
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
                    "thinking": item[6] if len(item) > 6 else "境界とは、分断ではなく、二つの異なる宇宙が出会い、新しい旋律を産み出すための、聖なる共鳴の場所なのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "廊下を歩くことは、移動ではありません。昨日までの自分から明日の自分へと、徐々に魂の色を塗り替えていくための、至高のる儀式なのですよ。",
                    "example": f"The long, dimly lit {word_text} seemed to echo with the whispers of the past, guiding the lone traveler toward the hidden library.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["扉を叩くことを恐れないでください。その向こう側には、あなたがまだ知らない、眩しいほどに新しいあなたが待っているのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Portal & Passage II (Cycle 108).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
