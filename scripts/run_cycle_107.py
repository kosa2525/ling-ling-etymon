import json
import re

# Theme: The Alchemy of Brilliance & Luster (Cycle 107)
words_data = [
    ("brilliance", "Brilliance", "光輝、才気、卓越、ブリリアンス", "17th Century", "brillare (to shine, literal: 'sparkling')", "Intense brightness of light", "眩（。し（。い（。智慧が、峻（。烈（。に「溢（。れ（。出した（。ブリリア）』至高の（。る（。一点（。（。その（。圧倒（。的な（。る（。る（。輝きに（。照ら（。さ（。れる（。とき（。、暗黒は、一（。瞬にして、眩（。し（。い（。祝（。祭（。へと、変わります。"),
    ("luster", "Luster", "光沢、艶、ラスター", "16th Century", "lustrare (to illuminate, literal: 'shining light')", "A gentle sheen or soft glow, especially that of a partly reflective surface", "表面（。を、至高の（。る「潤（。い（。ルストラ）』で、美し（。く（。包（。む（。こと（。（。その（。静（。か（。な（。る（。反射が、あなた（。の（。魂に、宇宙（。の（。真実（。を、静（。か（。に（。、囁（。く（。のですよ。"),
    ("gloss", "Gloss", "光沢、注釈、グロス", "16th Century", "glōssa (tongue, word requiring explanation, literal: 'explanation')", "A shiny substance applied to the surface of something to give it a pleasing or attractive appearance", "意味（。の（。皮（。膜を、峻（。烈（。な（。る「解（。釈（。グロス）』で、美し（。く（。装飾（。する（。こと（。（。その（。眩（。し（。い（。ほど（。に（。る（。滑（。らか（。さが、あなた（。を、真理（。へと（。導（。き（。ます。"),
    ("sheen", "Sheen", "輝き、しらべ、シーン", "Old English", "scēne (beautiful, bright, literal: 'beautiful')", "A soft luster on a surface", "エナジーが、静（。か（。に「面（。を（。撫（。で（。る（。シーン）』至高の（。る（。微（。光（。（。その（。瑞々（。し（。い（。る（。反射を、魂で、誇り（。高く、愛（。お（。しん（。で（。ください。"),
    ("polish", "Polish", "磨く、洗練、ポリッシュ", "13th Century", "polire (to smooth, literal: 'to make smooth')", "Make the surface of something smooth and shiny by rubbing it", "日常の（。濁（。りを、峻（。烈（。な（。る（。る「研（。磨（。ポリ）』で、一（。つ（。ずつ、削（。ぎ（。落（。と（。す（。こと（。（。その（。静（。か（。な（。る（。る（。一一点の（。透明（。をを、誇り（。高く、手（。に（。入れて（。ください。"),
    ("glaze", "Glaze", "釉薬、上塗り、グレイズ", "14th Century", "glass (glass, literal: 'to cover with glass')", "A vitreous substance fused on to the surface of pottery to form an impervious decorative coating", "魂（。を、至高（。の（。る「硝（。子（。グレイズ）』で、美し（。く（。閉じ（。込（。め（。る（。こと（。（。その（。不（。変の（。る（。輝きが、世界（。を、永遠（。な（。る（。聖域へと（。、塗り（。替（。え（。ます。")
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
            word_id = f"{word_text.lower()}_radiance_ii"
            
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
                    "thinking": item[6] if len(item) > 6 else "煌めきとは、外見の美しさではありません。自らの内側にある真実が、限界を越えて溢れ出したときに生まれる、瑞々しい魂の余韻なのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "艶を磨くことは、自分を偽ることではない。自らがこの宇宙の一部として、どれほど美しく調和できるかという、至高のる挑戦なのですよ。",
                    "example": f"The historical artifacts were carefully restored to their original {word_text}, revealing the intricate craftsmanship of the ancient artisans.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["磨き抜かれた一点は、宇宙全体の光を反射します。あなたという存在も、一滴の雫のように、世界を美しく写しだすことができるのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["polish"] else "verb"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Brilliance & Luster (Cycle 107).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
