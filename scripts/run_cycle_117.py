import json
import re

# Theme: The Alchemy of Nucleus & Matrix II (Cycle 117)
words_data = [
    ("grain", "Grain", "穀物、木目、微粒子、グレイン", "12th Century", "granum (seed, literal: 'seed, kernel')", "A single fruit or seed of a cereal"),
    ("speck", "Speck", "小さな斑点、微塵、スペック", "Old English", "specca (speck, spot, literal: 'spot')", "A small spot or patch of color"),
    ("particle", "Particle", "微粒子、小片、パーティクル", "14th Century", "pars (part, literal: 'little part')", "A minute portion of matter")
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
            word_id = f"{word_text.lower()}_seed_ii"
            
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
                    "thinking": item[6] if len(item) > 6 else "極小であることは、無価値であることではありません。宇宙の巨大な幾何学も、結局は一つの微粒子の連なりから生まれている、至高のる事実を、魂で感じてください。",
                    "aftertaste": item[7] if len(item) > 7 else "一粒の種の中には、森全体の記憶が眠っている。あなたの中にある小さな想いも、いつか巨大な物語を紡ぎ出すための、聖なる核なのですよ。",
                    "example": f"The scientist used an electron microscope to observe the fine {word_text}s of dust that had been collected from the surface of the asteroid during the space mission.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["微小なものに目を向けることは、細部を愛でること。そこに宿る宇宙の全記憶を、静かに読み解いていくのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Nucleus & Matrix II (Cycle 117).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
