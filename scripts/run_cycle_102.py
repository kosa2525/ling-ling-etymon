import json
import re

# Theme: The Alchemy of Momentum & Inertia II (Cycle 102)
words_data = [
    ("whirl", "Whirl", "渦巻、回転、ワール", "15th Century", "Middle English whirlen (to spin)", "Move or cause to move rapidly round and round", "流（。れ（。る（。時間を、美し（。い（。螺旋（。へと（。変える（。ワール）』、至高の（。る（。舞（。い（。（。その（。一一点（。の（。不（。均（。一（。な（。る（。煌（。めきを、ただ、魂で、感（。じ（。て（。いて（。ください。"),
    ("glide", "Glide", "滑る、滑走、グライド", "Old English", "glidan (to slip, slide, literal: 'smooth movement')", "Move with a smooth continuous motion, typically with little noise"),
    ("soar", "Soar", "舞い上がる、滑空する、ソアー", "14th Century", "ex- (out) + aura (air, literal: 'rising into the air')", "Fly or rise high in the air"),
    ("puff", "Puff", "ひと吹き、パフ", "13th Century", "Origin imitative of the sound of a short blast of air"),
    ("rush", "Rush", "突進、ラッシュ", "14th Century", "Middle English russhen (to move with speed)", "Move with urgent haste"),
    ("slip", "Slip", "滑る、スリップ", "13th Century", "Middle English slippen (to glide, slide)", "Lose one's footing and slide unintentionally for a short distance"),
    ("slide", "Slide", "滑る、削（。、スライド", "Old English", "slidan (to glide, slip)", "Move along a smooth surface while maintaining continuous contact with it"),
    ("roll", "Roll", "転がる、ロール", "14th Century", "rotulare (to roll, literal: 'little wheel')", "Move by turning over and over on an axis"),
    ("spin", "Spin", "回る、スピン", "Old English", "spinnan (to draw out and twist fibers)", "Turn or cause to turn or whirl round quickly")
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
            word_id = f"{word_text.lower()}_move_ii"
            
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
                    "thinking": item[6] if len(item) > 6 else "動きとは、目的地にたどり着くための手段ではありません。その一瞬一瞬の変化を、魂で享受するための、聖なる旅路の形式なのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "滑るように生きることは、逃げることではありません。世界との摩擦を最小に抑え、自らの純粋なるエナジーを、どこまで遠くへ運べるかという挑戦なのですよ。",
                    "example": f"The eagle continued to {word_text} effortlessly above the mountain peaks, using the thermal currents to maintain its high vantage point.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["天空を舞う鳥のように、自らの魂を高く持ち上げて。その視座の高さが、日常の些細な苦悩を、眩しい喜びに変えてくれるのですよ。"]
                    },
                    "part_of_speech": "verb"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Momentum & Inertia II (Cycle 102).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
