import json
import re

# Theme: The Alchemy of Gravitas & Levity (Cycle 106)
words_data = [
    ("gravitas", "Gravitas", "重厚さ、品位、端厳、グラヴィタス", "16th Century", "gravitas (weight, heaviness, literal: 'weight')", "Dignity, seriousness, or solemnity of manner", "魂の（。奥底に、底（。知（。れ（。ぬ（。深（。さで「溜（。め（。置（。いた（。重み（。グラヴィ）』。（。その（。峻（。烈（。な（。る（。る（。品（。格（。が、日常を（。、至高の（。る（。る（。神（。殿（。へと、変（。え（。る（。のですよ。"),
    ("levity", "Levity", "軽率、軽薄、軽やかさ、レヴィティ", "16th Century", "levis (light, literal: 'lightness')", "Humor or frivolity, especially the treatment of a serious matter with humor or in a manner lacking due respect", "峻（。烈（。な（。る（。る（。現実（。を、至高の（。る「軽（。やかさ（。レヴィ）』で（。、美し（。く（。裏（。切（。る（。こと（。（。その（。眩（。し（。い（。ほど（。の（。る（。る（。遊（。び（。心が、世界を（。、光へと（。、還（。し（。ます。"),
    ("dense", "Dense", "密な、濃い、デンス", "15th Century", "densus (thick, crowded)", "Closely compacted in substance", "エナジーが、一（。点（。に（。峻（。烈（。に「凝縮（。さ（。れた（。デンス）』至高の（。部（。厚さ（。（。その（。目（。に（。見（。え（。な（。い（。る（。る（。密度（。を、魂で、噛（。み（。締（。め（。て（。ください。"),
    ("firmament", "Firmament", "大空、蒼（。穹（。、ファーマメント", "13th Century", "firmamentum (support, strengthening, literal: 'strengthening support')", "The heavens or the sky, especially when regarded as a tangible thing", "宇宙を（。峻（。烈（。に「支（。え（。る（。ための（。る（。土台（。ファマ）』としての、至高の（。る（。る（。天空（。（。その（。不（。動の（。る（。広野に、あなた（。の（。物語（。を、投影（。し（。て（。ください。"),
    ("mass", "Mass", "質量、固まり、大衆、マス", "14th Century", "massa (kneaded dough, lump, literal: 'lump')", "A large body of matter with no definite shape", "何（。も（。語（。ら（。ず、ただ（。そこに（。在（。る「至高の（。塊（。マッサ）』。（。その（。圧倒（。的な（。る（。存在（。感に、魂は、静（。か（。に、跪（。き（。ます。"),
    ("bulk", "Bulk", "大部分、巨体、バルク", "15th Century", "bolkr (heap, beam, literal: 'heap')", "The mass or magnitude of something large", "小（。さな（。る（。作為（。をを（。越元（。た「峻（。烈（。なる（。る（。る（。巨大（。さ（。バルク）』。（。その（。重厚（。な（。る（。る（。沈黙（。が、世界（。を（。、眩（。しい（。ほどに、規定（。し（。て（。いく（。のです。")
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
            word_id = f"{word_text.lower()}_gravity_ii"
            
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
                    "thinking": item[6] if len(item) > 6 else "重みとは、物質の量ではありません。どれだけ深く、自らの中心軸をこの宇宙に打ち込んだかという、魂の覚悟の深さのことなのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "軽やかに生きることは、不真面目であることではありません。絶望という名の重力に屈せず、一瞬の微笑みで世界を塗り替えようとする、至高のる反逆なのですよ。",
                    "example": f"The ambassador's {word_text} and dignified presence in the international summit successfully bridged the gap between the conflicting nations.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["天空を支える土台があるように、あなたの日常を支える見えない祈りがあることに、静かに気づいてください。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["dense", "bulk"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Gravitas & Levity (Cycle 106).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
