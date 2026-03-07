import json
import re

# Theme: The Alchemy of Quiddity & Respiration (Cycle 109)
words_data = [
    ("respiration", "Respiration", "呼吸、一服、レスピレーション", "14th Century", "re- (again) + spirare (to breathe, literal: 'breathing again')", "The action of breathing", "宇宙（。の（。全記憶を、再び「吸（。い（。込み（。スピラ）』、命を（。通（。わ（。せる（。こと（。（。その（。一（。つ（。一（。つの（。る（。る（。呼吸（。の中にこそ（。、至高の（。る（。る（。智慧が、今（。も、静（。か（。に（。、横（。たわ（。って（。いる（。の（。ですよ。"),
    ("inspiration", "Inspiration", "霊感、インスピレーション", "14th Century", "in- (into) + spirare (to breathe, literal: 'breathing into')", "The process of being mentally stimulated to do or feel something, especially to do something creative", "魂に（。峻（。烈（。な（。る（。真実が「入（。り（。込（。ん（。だ（。イン）』、至高の（。る（。る（。瞬間（。（。その（。眩（。し（。い（。ほどに（。る（。る（。煌（。めきが、あなたを、真（。実（。の（。る（。る（。物（。語へと、導（。き（。ます。"),
    ("expiration", "Expiration", "満了、吐き出し、エクスピレーション", "14th Century", "ex- (out) + spirare (to breathe, literal: 'breathing out')", "The ending of the period of time when something is valid", "全（。てを（。受け（。入れ、至高（。の（。る（。力で「吐（。き（。出した（。エクス）』、物（。語（。の（。終（。わり（。（。その（。静（。か（。な（。る（。る（。沈黙こそが、宇宙（。の（。る（。る（。答え（。なの（。ですよ。"),
    ("aspiration", "Aspiration", "志向、熱望、アスピレーション", "14th Century", "ad- (to) + spirare (to breathe, literal: 'breathing towards')", "A hope or ambition of achieving something", "至高（。の（。る「高（。みへと（。息（。吹（。く（。アス・スピラ）』、峻（。烈（。な（。る（。る（。意志。（。その（。一一点（。を（。視（。つ（。め（。続（。け（。る（。とき、運（。命（。は（。、新（。しく、動き（。出（。し（。ます。"),
    ("perspiration", "Perspiration", "発汗、努力の成果、パースピレーション", "17th Century", "per- (through) + spirare (to breathe, literal: 'breathing through')", "The process of sweating", "魂の（。エナジーが、峻（。烈（。な（。る（。る（。行為をを「突き（。抜（。け（。て（。溢（。れ（。出した（。パース）』至高の（。る（。る（。雫（。（。その（。眩（。しい（。ほどに、透明（。な（。る（。る（。る（。証を、誇り（。高く、愛（。で（。て（。ください。")
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
            word_id = f"{word_text.lower()}_essence_iv"
            
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
                    "thinking": item[6] if len(item) > 6 else "呼吸とは、命の最も根源的なる対話の形式なのですよ。外側の世界を自らの中に取り込み、自らの内側の熱を世界へと還していく、その繰り返される聖なる循環を、魂で感じてください。",
                    "aftertaste": item[7] if len(item) > 7 else "志を持つことは、遠くの何かを追い求めることではありません。今、この一呼吸を、どれほど純粋に、自らの真実へと捧げられるかという挑戦なのですよ。",
                    "example": f"The young artist found profound {word_text} for her latest masterpiece in the quiet, reflective moments spent watching the dawn light dance across the lake.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["息を吐ききる勇気を持ってください。空っぽになった瞬間にこそ、宇宙からの新しい煌めきが、あなたの内側へと満たされるのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Quiddity & Respiration (Cycle 109).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
