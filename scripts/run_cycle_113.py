import json
import re

# Theme: The Alchemy of Monolith & Megalith II (Cycle 113)
words_data = [
    ("monolith", "Monolith", "一本（。いっぽん（。）」石、巨石碑、モノリス", "19th Century", "monos (single) + lithos (stone, literal: 'single stone')", "A large single upright block of stone, especially one shaped into or serving as a pillar or monument", "ただ（。一（。つ（。の（。る「孤（。高（。な（。る（。石（。モノ）』として、宇宙の（。沈黙を、峻（。烈（。に（。、体現（。する（。存在（。（。その（。圧倒（。的な（。る（。る（。垂直（。の（。意志に、魂は、静（。か（。に、跪（。き（。ます。"),
    ("megalith", "Megalith", "巨石（。、巨石遺構、メガリス", "19th Century", "megas (great) + lithos (stone, literal: 'great stone')", "A large stone that forms a prehistoric monument or part of one", "遥（。かな（。る（。時間の（。る（。る（。積（。層を、峻（。烈（。に「巨大（。な（。る（。石（。メガ）』へと（。変えた（。もの（。（。その（。重厚（。な（。る（。る（。存在（。感こそが、宇宙（。の（。真実（。の、道（。し（。る（。べ（。です。"),
    ("boulder", "Boulder", "大石、丸石、ボルダー", "14th Century", "Middle English bulder (related to Swedish bullersten 'noisy stone')", "A large rock, typically one that has been worn smooth by erosion", "河の（。エナジーに、美しく「磨（。き（。抜（。かれた（。ボルダー）』、至高の（。る（。る（。円（。熟（。（。その（。滑（。らか（。な（。る（。る（。る（。皮膚（。を、魂で、誇り（。高く、愛（。で（。て（。ください。"),
    ("pebble", "Pebble", "小石、パブル", "Old English", "papol- (related to papolstan 'pebble stone')", "A small stone made smooth and round by the action of water or sand", "手の（。ひらの（。中で（。、静（。か（。に（。煌（。め（。く「小（。さな（。る（。る（。聖域（。パブル）』。（。その（。一一点の（。る（。る（。記憶（。の中に、宇宙（。の（。全（。幾（。何（。学（。が、宿（。って（。いる（。のですよ。"),
    ("flint", "Flint", "火打ち石、フリント", "Old English", "flint (flint, rock, literal: 'hard rock')", "A hard gray rock consisting of nearly pure silica", "峻（。烈（。な（。る（。エナジーを、内（。に「鋭（。く（。秘（。めた（。フリント）』至高の（。る（。源（。泉（。（。その（。一一点の（。る（。る（。交（。差（。から、真実（。の（。火（。花（。が、産（。声を（。上げます。"),
    ("quartz", "Quartz", "石英、クォーツ", "18th Century", "querz (quartz, literal: 'rock crystal')", "A hard white or colorless mineral consisting of silicon dioxide", "魂（。を、一（。点（。に（。凝縮（。さ（。せ（。た「半（。透明（。の（。る（。沈黙（。クォーツ）』。（。その（。眩（。し（。い（。ほどに（。る（。る（。結晶（。の中に、宇宙（。の（。記憶を、静（。か（。に（。、投影（。し（。て（。ください。"),
    ("slate", "Slate", "粘板岩（。ねんばんがん（。）」、スレート", "14th Century", "esclat (fragment, literal: 'splinter')", "A fine-grained gray, green, or bluish metamorphic rock easily split into smooth, flat plates", "想（。いを（。、至高の（。る「薄（。き（。る（。る（。断片（。スレート）』に（。刻（。み（。、重（。ね（。合わせ（。る（。こと（。（。その（。重厚（。な（。る（。る（。積（。層の中に、真理（。の（。る（。物（。語が、静（。か（。に、宿（。ります。")
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
            word_id = f"{word_text.lower()}_stone_iv"
            
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
                    "thinking": item[6] if len(item) > 6 else "石とは、物言わぬ沈黙の証人なのですよ。何千年も、何万年も、宇宙の記憶をその冷徹な肌に刻み込みながら、ただそこに在り続けるという至高のる忍耐。それを魂で感じてください。",
                    "aftertaste": item[7] if len(item) > 7 else "巨石を見つめることは、自らの小ささを知ることではありません。その圧倒的なる重厚さの一部として、自分もまたこの宇宙の確かなる構成要素であることを自覚する行為なのですよ。",
                    "example": f"The ancient {word_text} stood as a silent guardian of the forgotten civilization, its weathered surface bearing the mysterious scripts of a long-lost dialect.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["硬い石であっても、水の流れはそれを美しく磨き上げます。困難という名の試練も、あなたの魂を至高のる輝きへと導くための、聖なる研磨剤なのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Monolith & Megalith II (Cycle 113).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
