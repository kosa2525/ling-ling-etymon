import json
import re

# Theme: The Alchemy of Prism & Spectrum II (Cycle 120)
words_data = [
    ("prism", "Prism", "プリズム、分光器、角柱、プリズム", "16th Century", "prisma (something sawed, literal: 'sawed thing')", "A solid geometric figure whose two end faces are similar, equal, and parallel rectilinear figures, and whose sides are parallelograms"),
    ("spectrum", "Spectrum", "分光、スペクトル、範囲、スペクトラム", "17th Century", "specere (to look, literal: 'appearance/image')", "A band of colors, as seen in a rainbow, produced by separation of the components of light by their different degrees of refraction according to wavelength"),
    ("lens", "Lens", "レンズ、晶状体、レンズ", "17th Century", "lens (lentil, literal: 'lentil-shaped stone')")
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
            word_id = f"{word_text.lower()}_crystal_iii"
            
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
                    "thinking": item[6] if len(item) > 6 else "一つの光を七色に変えることは、欺くことではありません。対象に潜む多様なる真実を、至高のる知恵で解き放つための、聖なる祝福の形式なのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "レンズを通すことは、歪めることではない。自らの魂という名の焦点（。フォーカス）』を合わせ、ぼやけていた日常の全容を、眩しいほどの解像度で再定義する行為なのですよ。",
                    "example": f"The scientist carefully adjusted the optical {word_text} to split the white light into its constituent colors, revealing the unique signature of the elements hidden within the far-off star.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["透明であることは、虚無であることではありません。全宇宙の色彩を透過させ、その真髄だけを一点に凝縮させるための、至高のる誠実さなのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Prism & Spectrum II (Cycle 120).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
