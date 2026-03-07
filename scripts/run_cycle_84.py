import json
import re

# Theme: The Alchemy of Quiddity & Haecceity (Cycle 84)
words_data = [
    ("quiddity", "Quiddity", "何性、本質、クィディティ", "14th Century", "quid (what, literal: 'what-ness')", "The inherent nature or essence of someone or something", "その（。ものの（。、何（。たる（。かを（。決定（。する「何性（。クィディティ）』。（。表面（。的な（。かたち（。を（。越え（。た（。、峻（。烈（。な（。る（。一点（。。（。それ（。が（。あなた（。の（。魂に（。触れた（。とき、宇宙の（。全記憶（。が（。、静（。か（。に（。、産声を（。上げ（。ます。"),
    ("haecceity", "Haecceity", "これ性、個別性、エクセイティ", "17th Century", "haec (this, literal: 'this-ness')", "The property or quality of a thing by virtue of which it is unique or particular", "他の（。誰（。でも（。ない（。、今ここに（。ある「これ性（。エクセイティ）』。（。その（。代（。え（。の（。き（。か（。な（。い（。、絶対（。的（。な（。る（。個別（。性（。こそ（。が（。、あなた（。という（。存在を、至高の（。光へと（。、変（。える（。のですよ。"),
    ("substance", "Substance", "実体、物質、サブスタンス", "13th Century", "sub- (under) + stare (to stand, literal: 'standing under')", "The real physical matter of which a person or thing consists and which has a tangible existence", "属性の（。変化を（。、底（。知（。れ（。ぬ（。力（。で（。支える「実体（。サブスタンス）』。（。何（。が（。変わ（。っ（。ても（。、変わ（。る（。こと（。の（。ない（。その（。峻（。烈（。な（。る（。沈黙に、あなた（。は（。、何（。を（。、視（。て（。いる（。の（。でしょうか。"),
    ("accident", "Accident", "（。哲学的な（。意味での（。）」偶性（。、事故、アクシデント", "14th Century", "ad- (to) + cadere (to fall, literal: 'falling to')", "A property that is not essential to the nature of something", "形（。成される（。本質（。に、そっと「降（。り（。かかっ（。た（。アクシ）』偶（。然（。の（。着（。物（。。（。その（。不（。確定（。な（。る（。ゆらぎが（。ある（。から（。こそ（。、世界（。は（。これ（。ほど（。に（。、眩（。しく（。、多様（。なの（。ですよ。"),
    ("attribute", "Attribute", "属性、特質、アトリビュート", "14th Century", "ad- (to) + tribuere (to assign, literal: 'assigning to')", "A quality or feature regarded as a characteristic or inherent part of someone or something", "本質に（。向（。かって「捧（。げ（。られた（。アトリ）」、静（。か（。な（。る（。特質（。（。その（。一（。つ（。一（。つが（。、あなた（。という（。存在（。を（。、眩（。しい（。色彩（。で（。、彩（。っ（。て（。いく（。のですよ。"),
    ("property", "Property", "特性、財産、プロパティ", "14th Century", "proprius (one's own)", "An attribute, quality, or characteristic of something", "誰（。にも（。奪（。わ（。れ（。な（。い（。、「自分（。独自（。の（。もの（。プロプリ）」。（。その（。固有（。な（。る（。煌（。めきこそ（。、あなたが（。この（。宇宙で（。ただ（。大人一（。人（。で（。ある（。、誇り高（。き（。証（。なの（。ですよ。"),
    ("quality", "Quality", "質、良質、クオリティ", "13th Century", "qualis (of what kind, literal: 'how-ness')", "The standard of something as measured against other things of a similar kind; the degree of excellence of something", "単（。なる（。量（。を（。越（。え（。た（。、「どの（。ような（。クアリ）姿（。か（。）」という（。本質（。（。その（。内実（。の（。豊饒（。さを（。、静（。か（。に（。、魂で（。噛（。み（。締（。め（。て（。ください。"),
    ("quantity", "Quantity", "量、クオンティティ", "14th Century", "quantus (how great, literal: 'how-much-ness')", "The amount or number of a material or immaterial thing not usually estimated by spatial measurement", "「どれ（。ほど（。クアン）巨大（。か（。）」という（。、数（。値（。の（。連（。なり（。（。けれど（。、その（。無（。限（。の（。増（。殖（。の中にこそ（。、宇宙の（。数（。学（。的（。な（。美（。し（。さが（。、静（。かに（。、宿（。って（。いる（。のですよ。"),
    ("relation", "Relation", "関係、親族、リレーション", "14th Century", "re- (back) + latus (carried, literal: 'carried back')", "The way in which two or more concepts, objects, or people are connected; a thing's effect on or relevance to another", "一（。つ（。の（。事物が（。、他（。者へと（。想（。いを「再び（。リ）運（。び（。返（。す（。ラト）」こと（。。（。その（。目（。に（。見（。え（。な（。い（。糸（。が（。、世界（。を（。、至高（。の（。る（。一（。体（。感（。へと（。、繋（。ぎ（。止（。めて（。いる（。のですよ。"),
    ("logos", "Logos", "ロゴス、言葉、理性、論理", "16th Century", "logos (word, reason)", "The Word of God, or principle of divine reason and creative order", "混沌（。とした（。宇宙を、一（。つ（。の「言葉（。ロゴス）』で（。貫（。く（。）、至高（。の（。理性。（。その（。峻（。烈（。な（。る（。論理が（。、あなた（。を（。、真（。理（。の（。彼方へ（。と（。、誘（。う（。のですよ。"),
    ("mythos", "Mythos", "ミュトス、神話、物語、体系", "18th Century", "mythos (word, speech, story)", "A set of beliefs or assumptions about something", "論理（。を（。越え（。た「語（。り（。ミュトス）』の（。中に（。、静（。か（。に（。息（。づ（。く（。、魂の（。記憶（。（。その（。物（。語（。を（。紡（。ぐ（。とき、あなた（。は（。、忘（。れ（。去（。ら（。れた（。宇宙の（。鼓動（。を（。、再（。び（。聴（。く（。のです。"),
    ("telos", "Telos", "テロス、目的、終焉", "19th Century", "telos (end, goal)", "An ultimate object or aim", "全（。て（。が（。向（。かう（。べき「終（。端（。テロス）』であり、かつ（。最（。高（。の（。る（。完成（。（。その（。一一点（。を（。視（。つ（。める（。とき、あらゆる（。苦（。難（。は、美し（。い（。階（。段（。へと（。変（。わ（。る（。のですよ。"),
    ("psyche", "Psyche", "プシュケ、魂、精神", "17th Century", "psukhe (breath, soul, spirit)", "The human soul, mind, or spirit", "肉（。体（。と（。いう（。名の（。檻（。の（。中で（。、今も（。眩（。し（。く「呼吸（。プシュケ）』し（。続け（。る（。、火花（。（。その（。静（。か（。な（。る（。震（。えが（。、あなた（。を、至高（。の（。る（。生へと（。、駆（。り（。立て（。る（。のですよ。"),
    ("pneuma", "Pneuma", "プネウマ、霊気、息", "17th Century", "pneuma (wind, breath, spirit)", "The vital spirit, soul, or creative force of a person", "宇宙を（。満（。た（。し（。、全（。てに（。命を（。通（。わ（。せる「風（。プネウマ）』。（。あなたが（。その（。息（。吹（。きを（。吸（。い（。込む（。とき（。、あなた（。の（。魂は、全（。存在（。と（。、一（。つ（。に（。、溶（。け（。合い（。ます。"),
    ("soma", "Soma", "ソーマ、身体、肉体", "19th Century", "soma (body)", "The parts of an organism other than the reproductive cells", "魂が（。この（。地上で（。装（。う（。ための「衣（。裳（。ソーマ）』。（。その（。峻（。烈（。な（。る（。物質（。性（。に（。、感謝（。を（。捧（。げ（。る（。とき、生命（。は（。、新（。しい（。輝（。きを（。、放（。ち（。始め（。る（。のですよ。")
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
            word_id = f"{word_text.lower()}_essence"
            
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
                    "thinking": item[6] if len(item) > 6 else "本質とは、削ぎ落とすことの果てに見出される、ただ一点の動かざる真実なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "実体は、目に見える形に依存しているのではない。それを支える、見えない意志にこそ宿っているのですよ。",
                    "example": f"The philosopher spent his entire life contemplating the {word_text} of human existence and the nature of reality.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["『これ』というかけがえのなさを愛することから、真実の対話は始まるのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["quidditative", "haecceitic", "substantial", "accidental"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Quiddity & Haecceity (Cycle 84).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
