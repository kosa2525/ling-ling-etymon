import json
import re

# Theme: The Alchemy of Reticence & Taciturnity (Cycle 90)
words_data = [
    ("reticence", "Reticence", "寡黙、遠慮、秘密、レティセンス", "17th Century", "re- (back) + tacere (to be silent, literal: 'keeping silent back')", "The quality of being reticent; reserve", "語（。り（。過（。ぎ（。る（。のを（。拒（。み（。、ただ「静（。か（。に（。、口を（。噤（。む（。レティ）』こと（。。（。その（。峻（。烈（。な（。る（。控え（。め（。な（。る（。沈黙の中にこそ（。、真実（。の（。る（。重（。み（。が（。宿（。って（。いる（。のですよ。"),
    ("taciturnity", "Taciturnity", "黙り（。、無口、タシターニティ", "18th Century", "tacitus (silent, literal: 'being silent')", "The state or quality of being reserved or reticent in conversation", "言葉（。を（。、魂の（。奥底に（。仕（。舞（。い（。込み（。、「沈（。黙（。タシ）を（。貫（。く（。ター）』。その（。不（。動の（。意志に（。、世界（。は（。、畏（。敬（。の（。念を（。抱（。き、静（。まり（。返（。り（。ます。"),
    ("discretion", "Discretion", "思慮、分別、裁量、ディスクレション", "14th Century", "dis- (apart) + cernere (to separate, literal: 'separating apart')", "The quality of behaving or speaking in such a way as to avoid causing offense or revealing private information", "真実と（。虚構（。を（。、峻（。烈（。に「見（。分（。け（。る（。ディスクレ）」こと（。。（。その（。静（。か（。な（。る（。洞（。察（。が（。、あなた（。を、余（。計（。な（。る（。騒乱から（。、守（。って（。くれる（。のですよ。"),
    ("shyness", "Shyness", "内気、臆病、シャイネス", "15th Century", "skiah (shy, literal: 'frightened away')", "The quality of being shy; timidity", "眩（。し（。い（。光に（。、魂が（。不（。意に「怯（。え（。て（。身を（。引く（。シャイ）』、繊（。細な（。る（。震え（。（。その（。壊（。れ（。や（。す（。い（。美し（。さが（。、あなた（。を、孤独（。という（。名の（。、聖域へと（。、誘う（。のですよ。"),
    ("dread", "Dread", "恐怖、畏怖、ドレッド", "Old English", "drǣdan (to advise, consult, literal: 'to fear')", "Anticipate with great apprehension or fear", "深淵（。の（。底（。から、静（。か（。に（。這（。い（。寄る「氷のような（。恐（。れ（。ドレッド）』。（。その（。峻（。烈（。な（。る（。震（。えが、魂を（。、今（。一度（。、峻（。別（。さ（。せる（。のですよ。"),
    ("horror", "Horror", "恐怖、戦慄、ホラー", "14th Century", "horrere (to bristle, literal: 'shuddering')", "An intense feeling of fear, shock, or disgust", "魂の（。産（。毛（。が「一斉に（。逆（。立（。つ（。ホラー）』ような、峻（。烈（。な（。る（。閃光（。（。その（。戦（。慄（。の中に、宇宙の（。、目（。に（。見（。え（。な（。い（。る（。深（。淵（。が（。、静（。か（。に（。横（。たわ（。っている（。のです。"),
    ("panic", "Panic", "狼狽、パニック", "17th Century", "Pan (Greek god of nature, literal: 'fear caused by Pan')", "Sudden uncontrollable fear or anxiety, often causing wildly unthinking behavior", "森（。の（。神（。パンが（。、突如（。として（。放（。っ（。た（。、「原（。初（。的な（。る（。る（。咆（。哮（。パニック）』。（。その（。理（。性を（。越（。え（。た（。る（。衝（。動が（。、世界を（。、一（。瞬で（。、白（。紙へと（。、戻（。す（。のですよ。"),
    ("latch", "Latch", "掛け金（。、ラッチ", "Old English", "læccan (to seize, literal: 'seizing')", "A metal bar with a catch and lever used for fastening a door or gate", "扉を（。峻（。烈（。な（。る（。力（。で「捉（。え（。て（。離（。さ（。な（。い（。ラッチ）」、一一点（。の（。意志。（。その（。静（。か（。な（。る（。拒絶が、内（。側（。の（。る（。安（。ら（。ぎを、底（。知（。れ（。ぬ（。深（。さで（。、守っ（。て（。くれ（。る（。のですよ。"),
    ("bolt", "Bolt", "かんぬき、稲妻、ボルト", "Old English", "bolt (arrow, missile, literal: 'heavy arrow')", "A bar that slides into a socket to fasten a door or window", "一（。点（。を「貫（。く（。ように（。、放（。た（。れた（。矢（。ボルト）』。（。その（。峻（。烈（。な（。る（。定（。位が、物（。語（。に、一（。時（。の（。、断（。絶（。と（。調和を、与（。える（。のですよ。"),
    ("bar", "Bar", "棒、法廷、酒場、バー", "12th Century", "barra (bar, fence, literal: 'obstruction')", "A long rigid piece of wood, metal, or similar material, typically used as an obstruction, weapon, or part of a frame", "道（。を（。塞（。ぎ、拒（。み（。、「峻（。烈（。な（。る（。一（。本の（。境界（。バー）』を（。引くこと（。。（。その（。拒絶（。が（。ある（。か（。ら（。こそ（。、世界（。は（。、一（。つ（。の（。美し（。い（。秩序（。を、保（。つ（。ことが（。でき（。る（。のですよ。"),
    ("fence", "Fence", "垣根、柵、フェンス", "14th Century", "defens (defense, literal: 'defense')", "A structure, typically of posts and wire or wood, enclosing an area of ground to mark a boundary, control access, or prevent escape", "自分（。の（。領域を、至高（。の（。る（。力（。で「守（。り（。抜く（。フェンス）』、静（。か（。な（。る（。る（。砦（。（。その（。境界線の（。中にこそ（。、真実（。の（。る（。安（。ら（。ぎが（。、静（。か（。に（。、満（。ち（。て（。いる（。のですよ。"),
    ("wall", "Wall", "壁、障壁、ウォール", "Old English", "wall (rampart, literal: 'palisade of stakes')", "A continuous vertical brick or stone structure that encloses or divides an area of land", "大（。地に「突き（。立て（。られた（。ウォール）』、峻（。烈（。な（。る（。意志の（。化身（。（。それが（。あなた（。を、外界の（。喧（。騒から（。、眩（。しい（。ほど（。に（。、隔（。て（。て（。くれ（。る（。の（。ですよ。"),
    ("reserve", "Reserve", "予約、蓄え、遠慮、リザーブ", "14th Century", "re- (back) + servare (to keep, literal: 'keeping back')", "Retain for future use", "今、全（。てを（。使い（。果（。た（。さ（。ず（。、再び「後ろに（。備（。置（。いた（。リザーブ）』、エナジーの（。宝庫（。（。その（。静（。かな（。る（。る（。余韻が（。、あなた（。を（。、真（。の（。豊饒（。へと（。、誘（。う（。のですよ。"),
    ("caution", "Caution", "慎重、警告、コーション", "14th Century", "cavere (to beware, literal: 'being on one's guard')", "Care taken to avoid danger or mistakes", "物語（。の（。先を（。、峻（。烈（。に「見張り（。続ける（。コーシャ）』、静（。か（。な（。る（。智慧。（。その（。一一点（。の（。謙虚（。さが（。、不（。思（。議（。な（。る（。る（。幸運（。を（。、呼び（。込（。む（。のですよ。"),
    ("awe", "Awe", "畏怖、荘厳、オー", "Old English", "ege (fear, dread)", "A feeling of reverential respect mixed with fear or wonder", "巨大（。な（。る（。存在（。の（。前に（。、魂が（。静（。か（。に「打ち（。震（。え（。る（。オー）』、至高の（。る（。瞬間（。（。その（。圧倒（。的（。な（。る（。光の（。中（。で（。、あなた（。は（。、自（。分（。を（。、再（。発見（。する（。の（。ですよ。")
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
            word_id = f"{word_text.lower()}_silence"
            
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
                    "thinking": item[6] if len(item) > 6 else "沈黙とは、音が消えることではありません。あらゆる言葉が、その意味の限界を超えて、一つの祈りへと昇華された瞬間のことなのです。",
                    "aftertaste": item[7] if len(item) > 7 else "恐怖は、敵ではありません。それは、あなたが未知という名の光に、あまりにも近づきすぎたことへの、魂の健全なる反応なのですよ。",
                    "example": f"The witness maintained a state of {word_text} despite the intense questioning from the prosecution team in the courtroom.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["境界を作ることは、孤立することではありません。自らの魂が、何者であるかを、峻烈に自覚するための、聖なる儀式なのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Reticence & Taciturnity (Cycle 90).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
