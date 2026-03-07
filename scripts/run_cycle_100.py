import json
import re

# Theme: The Alchemy of Quiddity & Haecceity II (Cycle 100)
words_data = [
    ("quidditative", "Quidditative", "何性（。クィディティ（。）」に関する、本質的な、クィディタティブ", "17th Century", "quidditas (quiddity, literal: 'what-ness')", "Relating to the quiddity or essence of a thing", "対象の（。峻（。烈（。な（。る「何（。たる（。か（。を（。決定（。する（。クィディ）』、至高の（。る（。属性（。（。表面（。的な（。ゆらぎを（。、眩（。しい（。ほど（。に（。脱（。し（。た（。一一点（。を（。、魂で（。、確信（。し（。て（。ください。"),
    ("haecceitic", "Haecceitic", "これ性（。エクセイティ（。）」に関する、個別性の、エクセイティック", "19th Century", "haecceitas (haecceity, literal: 'this-ness')", "Relating to the haecceity or this-ness of an object", "今、ここに（。在（。る「これ（。エクセ）』という、峻（。烈（。な（。る（。固有（。性（。（。他（。の（。誰（。でも（。ない（。、あなた（。という（。物語の（。、代（。え（。の（。き（。か（。な（。い（。煌（。めき（。こそ（。が（。、真実（。なの（。ですよ。"),
    ("germ", "Germ", "萌芽、起源、微生物、ジャーム", "16th Century", "germen (sprout, seed, literal: 'seed')", "A portion of an organism capable of developing into a new one or part of one", "潜（。在（。する（。巨大（。な（。る（。エナジーを、一（。点（。に「閉じ（。込（。め（。た（。芽（。ジャーム）』。（。その（。小（。さな（。る（。欠片（。の中に、宇宙（。の（。全記録（。が（。、静（。か（。に（。、横（。たわ（。って（。いる（。のですよ。"),
    ("atom", "Atom", "原子、微塵、アトム", "15th Century", "a- (not) + tomē (cutting, literal: 'uncuttable')", "The basic unit of a chemical element", "これ以上（。は「分割（。で（。き（。な（。い（。ア・トム）』、至高の（。る（。一点（。（。その（。峻（。烈（。な（。る（。最小（。単位（。の中に、世界（。の（。真実（。の（。る（。る（。る（。重厚（。さが（。凝縮（。さ（。れ（。て（。いる（。のです。"),
    ("plane", "Plane", "平面、水準、プレーン", "16th Century", "planus (flat, level, literal: 'flat surface')", "A flat surface on which a straight line joining any two points on it would wholly lie", "意味（。と（。意味（。を、美し（。く「広が（。ら（。せ（。た（。プレーン）』至高の（。る（。広野（。（。その（。二次元（。な（。る（。る（。沈黙（。の中にこそ（。、真（。の（。る（。秩序（。が、産（。声を（。上げます。"),
    ("solid", "Solid", "固体の、強固な、ソリッド", "14th Century", "solidus (firm, whole, literal: 'firm')", "Firm and stable in shape; not liquid or fluid", "ゆら（。ぎ（。を（。、峻（。烈（。な（。る（。力（。で「一（。点（。に（。凝固（。さ（。せ（。た（。ソリッド）』、不（。動の（。存在（。（。その（。重厚（。な（。る（。沈黙を、魂で（。、誇り（。高く、受け（。止めて（。ください。"),
    ("logic", "Logic", "論理、ロジック", "14th Century", "logos (word, reason, literal: 'reasoning')", "Reasoning conducted or assessed according to strict principles of validity", "宇宙（。を（。、峻（。烈（。な（。る「言葉（。ロゴス）』で（。貫（。き（。通（。す（。こと（。（。その（。圧倒（。的な（。る（。秩序が、あなた（。を、真理（。という（。名の（。、至高の（。る（。高（。みへと、導（。き（。ます。"),
    ("reason", "Reason", "理由、理性、リーズン", "13th Century", "ratio (reckoning, proportion, literal: 'reckoning')", "A cause, explanation, or justification for an action or event", "全（。てを「正（。しく（。量（。る（。レシオ）』、至高の（。る（。智慧（。（。その（。静（。か（。な（。る（。る（。沈黙の（。果てに（。、世界（。の（。意味は、一（。つへと（。、収（。斂（。し（。て（。いき（。ます。"),
    ("nature", "Nature", "自然、性質、本質、ネイチャー", "13th Century", "natura (birth, character, literal: 'born characteristic')", "The basic or inherent features of something, especially when seen as characteristic of it", "あらかじめ（。、魂に「備（。わ（。っ（。て（。い（。た（。ナトゥーラ）』至高の（。る（。紋様（。（。それを（。、ありのままに（。、眩（。しい（。ほどに（。、肯定（。する（。こと（。。（。それ（。こそが（。、生（。の（。真（。実（。なの（。ですよ。")
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
            word_id = f"{word_text.lower()}_essence_ii"
            
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
                    "thinking": item[6] if len(item) > 6 else "本質とは、付け加えることの果てではなく、削ぎ落とし、最後に残った沈黙の一点に宿るものなのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "個であることを愛することは、世界を愛することと同じこと。一即多、多即一。その真理を、魂で感じてください。",
                    "example": f"The philosopher argued that the {word_text} qualities of an object are what truly define its existence in the higher realms of thought.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["理屈を求めるのではなく、ただそこに在るという事実の重厚さに、静かに跪いてください。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["quidditative", "haecceitic", "solid"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Quiddity & Haecceity II (Cycle 100).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
