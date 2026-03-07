import json
import re

# Theme: The Alchemy of Specular & Speculum (Cycle 101)
words_data = [
    ("specularity", "Specularity", "鏡面性、反射性、スペキュラリティ", "19th Century", "speculum (mirror)", "Quality of being mirror-like", "至高（。の（。る「鏡（。スペキュル）』のように（。、世界を（。歪（。み（。な（。く（。写（。し（。出す（。こと（。（。その（。峻（。烈（。な（。る（。透明（。さ（。を（。、魂で（。、誇り（。高く、自覚（。し（。て（。ください。"),
    ("specular", "Specular", "反射的な、鏡のような、スペキュラー", "14th Century", "speculum (mirror)", "Mirror-like", "外（。界の（。ノイズを（。、至高の（。る（。力（。で「跳（。ね（。返（。し（。、一（。つ（。の（。像へと（。凝縮（。さ（。せ（。る（。スペキュ）』。（。その（。眩（。し（。い（。光に（。照ら（。さ（。れる（。とき、日常は（。聖堂へと（。変わり（。ます。"),
    ("resonance", "Resonance", "共鳴、響き、レゾナンス", "15th Century", "re- (again) + sonare (to sound)", "Quality of being deep, full, and reverberating", "他者の（。鼓動を（。、自ら（。の中で「再び（。リ）奏（。で（。る（。ソナン）』こと（。（。その（。静（。か（。なる（。る（。同調が、あなた（。を、至光の（。る（。る（。物（。語へと（。、誘（。う（。のですよ。"),
    ("symmetry", "Symmetry", "対称、左右対称、シンメトリー", "16th Century", "sun- (together) + metron (measure)", "Similarity of parts on either side of an axis", "中心軸（。を（。挟（。み（。、美し（。く「共に（。スン）測（。り（。整え（。られた（。メトロン）』、至高の（。る（。調和（。（。その（。一点（。の（。不（。動の（。均衡にこそ（。、真（。実（。の（。美（。しさが（。宿（。ります。")
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
            word_id = f"{word_text.lower()}_reflect_ii"
            
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
                    "thinking": item[6] if len(item) > 6 else "反射とは、拒絶ではなく、受け入れたエナジーを一転して返すための、至高のる対話の形式なのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "鏡の中の自分を視つめることは、孤独を深めることではなく、宇宙という名のもう一人の自分を見出すことなのですよ。",
                    "example": f"The high {word_text} of the crystal surface made it difficult to see the underlying structure without polarizing filters.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["調和を求めることは、自分を殺すことではない。自分という名の音を、宇宙という名の調べの中に、正しく配置することなのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["specular"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Specular & Speculum (Cycle 101).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
