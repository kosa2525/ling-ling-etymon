import json
import re

# Theme: The Alchemy of Shadow & Cipher (Cycle 67)
words_data = [
    ("mystic", "Mystic", "神秘的、神秘主義者", "14th Century", "mu- (to shut mouth, literal: 'shutting eye/mouth')", "A person who seeks by contemplation and self-surrender to obtain unity with or absorption into the Deity or the absolute, or who believes in the spiritual apprehension of truths that are beyond the intellect", "言葉を（。真理を（。語（。る（。のを（。止め（。、ただ（。静（。かに「口を（。閉（。ざ（。し（。ム）」、心（。の（。眼で（。世界（。を（。視（。る（。者（。。（。その（。沈黙（。の（。深淵（。の中にこそ（。、宇宙（。の（。全記憶（。が（。、美し（。く（。、横（。たわ（。って（。いる（。のですよ。"),
    ("arcane", "Arcane", "難解な、秘密の、アルケイン", "16th Century", "arca (chest, box, literal: 'enclosed in a chest')", "Understood by few; mysterious or secret", "誰（。にでも（。見（。える（。場所（。ではなく（。、分（。厚（。い「箱（。アルカ）の中に（。封印（。さ（。れた（。）」真理（。。（。その（。謎（。を（。解（。く（。鍵（。を（。持（。つ（。者（。だけが（。、時代（。の（。深淵（。へと（。、漕（。ぎ（。出す（。ことが（。できる（。のですよ。"),
    ("occult", "Occult", "神秘（。的な（。）、超自然（。の（。、オカルト", "16th Century", "oc- (up) + celare (to hide, literal: 'hidden over')", "Involving or relating to supernatural, mystical, or magical powers or phenomena", "日常（。の（。光の（。裏（。側（。に「隠（。さ（。れた（。カル）」エナジー。（。目（。に（。見（。える（。ものが（。全（。て（。では（。ない（。と（。知（。っ（。た（。とき（。、あなた（。の（。魂は（。、真（。の（。自由（。を（。、手（。に（。入れ（。ます。"),
    ("esoteric", "Esoteric", "難解（。な（。）、秘（。伝（。の（。、エソテリック", "17th Century", "esotero (inner)", "Intended for or likely to be understood by only a small number of people with a specialized knowledge or interest", "誰（。も（。が（。集（。ま（。る（。場所（。ではなく（。、一（。体の（。深い「内（。側（。エソ）に（。だけ（。）」許（。さ（。れた（。、聖（。なる（。教え（。。（。選（。ば（。れ（。た（。者（。への（。囁（。きが（。、歴史（。の（。深（。層（。で（。、静（。か（。に（。、脈動（。し（。て（。いる（。のですよ。"),
    ("sphinx", "Sphinx", "スフィンクス、謎めいた人", "14th Century", "sphingein (to bind tight, literal: 'strangler')", "An enigmatic person", "立（。ち（。去（。ろ（。う（。と（。する（。者（。を「固く（。繋（。ぎ（。止める（。スフィン）』、謎（。の（。番（。人（。。（。その（。冷（。徹（。な（。る（。問い（。に（。答（。え（。て（。こそ（。、あなた（。は（。、自分（。自身（。の（。限界（。を（。、再（。認識（。する（。のですよ。"),
    ("sybil", "Sybil", "女（。预（。言者、シビル", "14th Century", "Sibulla (prophetess)", "A woman in ancient times supposed to be uttered the oracles and prophecies of a god", "神（。々の（。囁（。きを（。、身（。を（。呈（。し（。て「降（。ろ（。し（。、言葉に（。変える（。シビ）』存在（。。（。その（。恍（。惚（。と（。した（。沈黙（。の中にこそ（。、未来（。という（。名の（。、眩（。し（。い（。光が（。、宿（。って（。いる（。のですよ。"),
    ("warlock", "Warlock", "魔法使い、魔術師、ワーロック", "Old English", "wær (faith, oath) + lēogan (to lie, literal: 'oath-breaker')", "A man who practices witchcraft; a sorcerer", "日常（。の「誓（。い（。ワー）を（。破（。り（。ロ）』、禁（。じ（。ら（。れた（。領域を（。歩（。く（。者（。。（。光（。も（。影（。も（。飲（。み（。込（。み（。、自（。分（。だけ（。の（。真実（。を（。創（。り（。出す（。、孤独（。な（。る（。反逆（。者。"),
    ("adept", "Adept", "熟達した、達人、アデプト", "17th Century", "adipisci (to attain)", "A person who is proficient at something", "修（。行（。を（。究（。め（。、真理に「辿（。り（。着（。いた（。アデプ）」者（。。（。その（。一挙（。手（。一投（。足（。に、宇宙（。の（。全（。法則（。が（。、静（。か（。に（。、凝縮（。さ（。れて（。いる（。のですよ。"),
    ("devotee", "Devotee", "熱愛者、信奉者、デヴォティー", "17th Century", "voveret (to vow)", "A person who is very interested in and enthusiastic about someone or something", "自（。分（。を（。捨て（。、ただ（。一（。点（。に「生涯（。の（。誓（。い（。デ、ヴォ）を（。捧（。げ（。る（。）」者（。。（。その（。狂（。信的（。な（。る（。愛（。が（。、いつか（。、巨大（。な（。山（。を（。、静（。か（。に（。、動（。か（。す（。のですよ。"),
    ("martyr", "Martyr", "殉教者、苦労人、マーター", "Old English", "martus (witness, literal: 'witness')", "A person who is killed because of their religious or other beliefs", "自（。ら（。の（。死を（。通して（。、真実（。の「証（。人（。マーター）』と（。なる（。者（。。（。その（。峻（。烈（。な（。る（。最後（。の（。瞬き（。が（。、歴史（。を（。、永遠（。に（。、変（。え（。て（。しまう（。のですよ。"),
    ("apostle", "Apostle", "使徒、アポストル", "Old English", "apo- (away) + stellein (to send, literal: 'person sent away')", "Particularly any of the twelve chief disciples of Jesus Christ", "真理（。を（。語（。る（。ために、「遠くへと（。アポ）遣（。わ（。さ（。れた（。ストル）」者（。。（。あなた（。は（。、独（。り（。ぼっちの（。旅人（。なの（。ではなく（。、聖（。なる（。エナジーの（。媒介（。な（。のですよ。"),
    ("disciple", "Disciple", "弟子、門徒、ディサイプル", "Old English", "discere (to learn)", "A personal follower of Jesus during his life, especially one of the twelve Apostles", "自（。ら（。の（。エゴ（。を（。捨て（。、ただ「学（。ぶ（。ディシ）こと」を（。選（。んだ（。者（。。（。師（。の（。背中を見（。つ（。め（。な（。がら（。、いつか（。自分（。の（。中（。に（。、眩（。し（。い（。光を（。、見（。出（。す（。のです。"),
    ("nomad", "Nomad", "遊牧民、放浪者、ノマド", "16th Century", "nomas (pasturing, roaming for pasture)", "A member of a people having no permanent abode, and who travel from place to place to find fresh pasture for their livestock", "安（。住（。の（。地を（。拒み（。、ただ「彷徨（。う（。ノマ）こと」を（。生き（。る（。糧（。と（。する（。者（。。（。大地すべて（。を（。、魂の（。座（。敷（。（。と（。し（。て（。、自由（。に（。、駆け抜ける（。のですよ。"),
    ("odyssey", "Odyssey", "オデュッセイア、長期間の放浪", "17th Century", "Odusseus (Odysseus, hero of the Odyssey)", "A long and eventful or adventurous journey or experience", "「オデュッセウス』のように（。、多（。多（。難（。な（。る「冒（。険（。オディ）の（。旅（。）」。（。故郷（。を（。求めて（。彷徨（。う（。こと（。こそ（。、実（。は（。、人生（。の（。真（。実（。な（。の（。か（。も（。しれ（。ません。"),
    ("saga", "Saga", "サーガ、英雄物語", "18th Century", "saga (story, literally: 'what is said')", "A long story of heroic achievement, especially a medieval Icelandic or Norwegian one", "何（。代（。にも（。渡（。っ（。て「語（。り（。継（。が（。れた（。サーガ）」、巨大な（。記憶（。の（。連（。なり。（。あなた（。の（。一（。人（。の（。人生を（。越（。え（。た（。場所（。に、真（。の（。物語が（。、横（。たわ（。って（。いる（。のですよ。")
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
            word_id = f"{word_text.lower()}_mystery"
            
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
                    "thinking": item[6] if len(item) > 6 else "神秘は、理解するためにあるのではなく、身を委ね、魂を震わせるために用意された至高の舞台なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "謎は、答えを見つけるための障害ではなく、問い続けることそのものに価値がある、聖なる誘いなのです。",
                    "example": f"The ancient scrolls were written in an {word_text} script that baffled even the most experienced scholars.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["隠されているということは、そこに何かが無いということではなく、語り尽くせないほどの饒舌な真実が溢れているということなのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["mystic", "arcane", "occult", "esoteric", "obscure", "cryptic", "enigmatic"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Shadow & Cipher (Cycle 67).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
