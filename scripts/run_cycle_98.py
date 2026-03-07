import json
import re

# Theme: The Alchemy of Mutation & Transmutation (Cycle 98)
words_data = [
    ("mutation", "Mutation", "突然変異、変化、ミューテーション", "14th Century", "mutare (to change, literal: 'changing')", "The action or process of mutating; the changing of the structure of a gene", "日常（。の（。る（。均衡を（。、峻（。烈（。に「組み（。替（。えた（。ミュー）』、至高の（。る（。飛躍。（。その（。不（。可（。思議な（。る（。変容（。の中に、宇宙の（。新（。しい（。物（。語が（。、静（。か（。に（。、産声を（。上げた（。のですよ。"),
    ("transmutation", "Transmutation", "錬金（。変容、変換、トランスミューテーション", "14th Century", "trans- (across) + mutare (to change, literal: 'changing across')", "The action of changing or the state of being changed into another form", "一（。つ（。の（。次元を（。越元（。て、「至高（。のへと（。、組み（。替（。える（。トランス）』こと（。（。鉛を（。金へと（。変（。え（。る（。ように、あなた（。の（。魂は、この（。不（。条理な（。る（。世界を、眩（。し（。い（。智慧へと（。変（。える（。のですよ。"),
    ("alchemy", "Alchemy", "錬金術、アルケミー", "14th Century", "al- (the) + khēmia (pouring, literal: 'the art of pouring/infusing')", "The medieval forerunner of chemistry, based on the supposed transformation of matter", "物質を（。峻（。烈（。に「溶（。かし（。合せ（。る（。アルケミ）』至高の（。る（。技法（。（。その（。静（。か（。な（。る（。坩（。堝（。の中で、真実（。の（。る（。精霊（。が（。、静（。か（。に（。、姿を（。現し（。ます。")
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
            word_id = f"{word_text.lower()}_change"
            
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
                    "thinking": item[6] if len(item) > 6 else "変容とは、自分を捨てることではありません。自分という名の種子が、時間の重みに耐えきれなくなって、未知という名の花を咲かせる瞬間なのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "錬金術は、外側に金を求めるための技術ではない。自らの内側にある不純な想いを、透明な祈りへと昇華させるための、至高のる道のりなのですよ。",
                    "example": f"The scientist observed a rare genetic {word_text} that had occurred spontaneously in the experimental population of fruit flies.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["昨日までの自画像に固執しないでください。一瞬ごとに新しく生まれ変わることこそが、宇宙の唯一の法則なのですから。"]
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

        print(f"Success: Added {added_count} words. Theme: Mutation & Transmutation (Cycle 98).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
