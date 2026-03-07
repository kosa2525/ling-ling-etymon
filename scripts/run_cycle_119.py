import json
import re

# Theme: The Alchemy of Cipher & Silhouette II (Cycle 119)
words_data = [
    ("silhouette", "Silhouette", "輪郭、影法師、シルエット", "18th Century", "Étienne de Silhouette (French politician, literal: 'cheap/scanty portrait')", "The dark shape and outline of someone or something visible against a lighter background"),
    ("cipher", "Cipher", "暗号、数字、無（。む（。）」、サイファー", "14th Century", "sifr (empty, nothing, literal: 'zero/empty')")
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
            word_id = f"{word_text.lower()}_shadow_v"
            
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
                    "thinking": item[6] if len(item) > 6 else "影とは、光の不在ではありません。対象がそこに在るという事実を、逆説的に、かつ峻烈に証明するための至高のる様式なのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "暗号を解くことは、秘密を暴くことではない。隠された沈黙の中に宿る宇宙の響きを、自らの魂で丁寧に手繰り寄せる行為なのですよ。",
                    "example": f"The mysterious {word_text} of the figure moved slowly along the dark corridor, disappearing into the shadows before anyone else could react.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["詳細が見えないからこそ、想像力という名の光が、その空白を眩しい物語で満たしていくことができるのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Cipher & Silhouette II (Cycle 119).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
