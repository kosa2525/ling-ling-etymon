import json
import re

# Theme: The Alchemy of Cipher & Seal (Cycle 85)
words_data = [
    ("sigil", "Sigil", "記号、印章、シジル", "16th Century", "sigillum (seal, sign, literal: 'little sign')", "An inscribed or painted symbol considered to have magical power", "宇宙の（。エナジーを、美し（。い（。幾何学（。の中に「封印（。し（。た（。シジル）』。（。その（。一一点（。の（。紋様にに、誰（。にも（。汚（。さ（。れ（。な（。い（。、至高（。の（。真実（。が（。、静（。か（。に（。、横（。たわ（。って（。いる（。のですよ。"),
    ("amulet", "Amulet", "お守り、アミュレット", "16th Century", "amuletum (object that protects)", "An ornament or small piece of jewelry thought to give protection against evil, danger, or disease", "災い（。から（。あなた（。を「守（。り（。抜（。く（。アミュレ）』ための（。、小（。さな（。る（。意志。（。その（。一点（。の（。煌（。めきが（。、不（。確実な（。る（。日常（。を（。、至高（。の（。安（。ら（。ぎへと（。、変（。え（。て（。くれる（。のですよ。"),
    ("talisman", "Talisman", "タリスマン、護符", "17th Century", "telesma (payment, initiation, literal: 'consecrated object')", "An object, typically an inscribed ring or stone, that is thought to have magic powers and to bring good luck", "聖なる（。儀式を（。越元（。て「完（。成さ（。れた（。タリス）』至高の（。る（。力（。（。その（。石に（。刻まれた（。記憶に（。、あなた（。は（。、何（。を（。、誓（。う（。の（。でしょうか。"),
    ("relic", "Relic", "遺物、聖遺物、レリック", "13th Century", "re- (back) + linquere (to leave, literal: 'that which is left behind')", "An object surviving from an earlier time, especially one of historical or sentimental interest", "遥（。かな（。る（。過去から「残（。さ（。れた（。レリ）』、静（。か（。な（。る（。亡（。骸（。（。けれど（。、その（。一（。つ（。一（。つの（。破片（。には（。、未だ（。冷（。め（。ぬ（。情熱が（。、宿（。って（。いる（。のですよ。"),
    ("crypt", "Crypt", "地下聖堂、暗号、クリプト", "15th Century", "kruptein (to hide)", "An underground room or vault beneath a church, used as a chapel or burial place", "光を（。拒（。み、ただ「隠（。さ（。れた（。クリプ）』至高の（。場所（。（。そこ（。には（。、沈黙が（。、最（。も（。深く（。、最（。も（。美し（。く（。、横（。たわ（。って（。いる（。のですよ。"),
    ("cache", "Cache", "隠し場所、キャッシュ", "18th Century", "cacher (to hide)", "A collection of items of the same type stored in a hidden or inaccessible place", "大切（。な（。ものを、そっと「隠（。し（。置（。いた（。キャッシュ）』。（。その（。見（。え（。な（。い（。場所に（。、あなた（。は（。、今日（。何（。を（。、預（。け（。て（。き（。た（。の（。でしょうか。"),
    ("hoard", "Hoard", "蓄え、死蔵、ホード", "Old English", "hord (treasure, hidden place, literal: 'hidden board')", "A stock or store of money or valued objects, typically one that is secret or carefully guarded", "誰（。にも（。見（。つ（。か（。ら（。な（。い（。ように、「蓄（。え（。ら（。れた（。ホード）』、孤独（。な（。る（。財宝（。（。その（。閉じ（。られた（。豊饒（。さが（。、いつか（。、世界（。を（。、美し（。く（。裏（。切（。る（。のですよ。"),
    ("treasury", "Treasury", "宝物庫、財務省、トレジャリー", "14th Century", "thesauros (storehouse, treasure, literal: 'place where it is put')", "A place or building where treasure is stored", "至高（。の（。る「至（。宝（。テザウロス）』を（。、そっと（。仕（。舞（。う（。ための（。、静（。かな（。る（。館（。（。そこ（。に（。足（。を（。踏（。み（。入（。る（。とき（。、あなた（。は（。、宇宙の（。真実と、出会（。い（。ます。"),
    ("chronicle", "Chronicle", "年代記、記録、クロニクル", "14th Century", "khronos (time, literal: 'time-book')", "A factual written account of important or historical events in the order of their occurrence", "流（。れ（。ゆ（。く「時間（。クロノ）』の（。一一点（。を（。、峻（。烈（。に（。、刻（。み（。付け（。た（。物語。（。その（。一（。行（。一（。行が（。、静（。か（。に（。、歴史（。を（。、創り（。上げ（。て（。いく（。のです。"),
    ("saga", "Saga", "サーガ、一族の物語、英雄記", "12th Century", "segja (to say, literal: 'what is said')", "A long story of heroic achievement, especially a medieval Icelandic or Norwegian prose narrative", "北欧（。の（。風（。の（。中（。で「語（。り（。継（。が（。れた（。サガ）』、峻（。烈（。な（。る（。意志。（。その（。物（。語（。にこそ（。、人間（。の（。真実（。の（。る（。輝（。きが（。、宿（。って（。いる（。のですよ。"),
    ("lore", "Lore", "伝承、知識、ロア", "Old English", "lār (instruction, lore, literal: 'learning')", "A body of traditions and knowledge on a particular subject, typically held by a particular group or transferred from person to person by word of mouth", "声（。と（。声（。の（。間（。で「学び（。継（。が（。れた（。ロア）』、静（。か（。な（。る（。真実。（。そこ（。には（。、文字（。を（。越（。え（。た（。、至高（。の（。る（。智慧（。が（。、満（。ち（。て（。いる（。のですよ。"),
    ("fable", "Fable", "寓話（。、作り事（。、フェイブル", "13th Century", "fabula (story, literal: 'that which is told')", "A short story, typically with animals as characters, conveying a moral", "真実を（。、美し（。い「物語（。ファブラ）』の中に（。、そっと（。、潜（。ま（。せ（。た（。もの（。（。その（。小（。さな（。る（。嘘の中に（。、誰（。にも（。汚（。さ（。れ（。な（。い（。、至光（。の（。真理（。が（。ある（。のです。"),
    ("arcane", "Arcane", "神秘的な、秘密の、アルケイン", "16th Century", "arca (chest, box, literal: 'shut up in a chest')", "Understood by few; mysterious or secret", "巨大な（。「箱（。アルカ）』の中に（。、峻（。烈（。に（。閉（。じ（。込め（。られた（。）」叡智。（。その（。深（。淵に（。触れる（。とき、あなた（。は（。、全（。く（。新（。しい（。光を（。、視（。る（。のです。"),
    ("esoteric", "Esoteric", "秘儀の、深遠な、エソテリック", "17th Century", "esotero- (inner, literal: 'further within')", "Intended for or likely to be understood by only a small number of people with a specialized knowledge or interest", "誰（。も（。辿（。り（。着（。け（。ぬ「最も（。内（。側（。エソテロ）』へと（。、静（。か（。に（。、導（。かれた（。）」智慧。（。その（。至高の（。る（。孤独（。が（。、あなた（。という（。存在（。を（。、至（。宝（。へと（。変え（。ます。"),
    ("cryptic", "Cryptic", "秘密の、不可解な、クリプティック", "17th Century", "kruptein (to hide)", "Having a meaning that is mysterious or obscure", "何（。も（。語（。ら（。ず、ただ「隠（。さ（。れた（。クリプト）』、沈黙の（。物（。語（。（。その（。不（。可（。解な（。る（。囁（。きを（。読み（。解く（。とき、世界（。の（。真（。実（。が（。、あなた（。の（。前に（。、現（。れ（。る（。のですよ。")
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
                    "thinking": item[6] if len(item) > 6 else "神秘とは、答えがないことではなく、問いそのものが光り輝いている状態なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "秘密は、誰にも言わないことで守られるのではない。誰も理解できない場所に置くことで、初めて永遠になるのですよ。",
                    "example": f"The ancient scrolls were written in a {word_text} script that baffled historians for generations until the discovery of the Rosetta Stone.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["隠すという行為は、拒絶ではなく、真実を時間という名の劣化から守るための、至高の愛なのかもしれません。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["arcane", "esoteric", "cryptic"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Cipher & Seal (Cycle 85).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
