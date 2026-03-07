import json
import re

# Theme: The Alchemy of Vacany & Vacuum II (Cycle 111)
words_data = [
    ("zero", "Zero", "零（。れい（。）」、無、原点、ゼロ", "17th Century", "sifr (empty, literal: 'empty')", "No quantity or number; nil; the numerical symbol 0"),
    ("null", "Null", "無効の、空（。から（。）」の、ヌル", "16th Century", "nullus (none, literal: 'not any')", "Having no legal or binding force; invalid"),
    ("naught", "Naught", "無し、虚無、ノート", "Old English", "nāwiht (nothing, literal: 'no-thing')", "Nothing"),
    ("blank", "Blank", "空白の、無記名の、ブランク", "13th Century", "blanc (white, literal: 'shining white')", "A space in a document to be filled in"),
    ("clear", "Clear", "明快な、透明な、クリア", "13th Century", "clarus (shining, bright, literal: 'bright')", "Easy to perceive, understand, or interpret"),
    ("plain", "Plain", "明白な、簡素な、プレーン", "13th Century", "planus (flat, even, level)", "Easy to perceive or understand; clear"),
    ("bare", "Bare", "むき出しの、露骨な、ベア", "Old English", "bær (bare, naked)", "Not clothed or covered"),
    ("naked", "Naked", "裸の、ありのままの、ネイキッド", "Old English", "nacod (nude, bare)", "Without clothes; not covered by any clothing")
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
            word_id = f"{word_text.lower()}_still_v"
            
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
                    "thinking": item[6] if len(item) > 6 else "静寂とは、何もないことではありません。全宇宙の可能性が、その一瞬の沈黙の中に凝縮され、産声を上げるのを待っている、最も瑞々しい状態のことなのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "ありのままの自分を晒すことは、弱さではありません。自らを飾ることを止め、ただそこに在るという事実の圧倒的なる輝きを、信じ抜くということなのですよ。",
                    "example": f"The explorer stared into the vast {word_text} of the desert, feeling the weight of the absolute silence that seemed to swallow all light and sound.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["空白を埋めようとしないでください。その何もない場所が、あなたの内側へと、無限の宇宙を呼び込むための、聖なる回路になるのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] in ["zero", "naught"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Vacany & Vacuum II (Cycle 111).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
