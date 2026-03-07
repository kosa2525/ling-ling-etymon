import json
import re

# Theme: The Alchemy of Nucleus & Matrix (Cycle 78)
words_data = [
    ("nucleus", "Nucleus", "核、原子核、中枢、ニュークリアス", "18th Century", "nux (nut, literal: 'little nut')", "The central and most important part of an object, movement, or group, forming the basis for its activity and growth", "巨大な（。物（。語（。の（。真（。ん（。中にある（。、「小（。さな（。木の実（。ヌクス）』。（。その（。一点（。に（。、全（。エナジーが（。、静（。か（。に（。、凝縮（。さ（。れて（。いる（。から（。こそ（。、宇宙は（。、盤石（。な（。る（。均衡を（。、保（。っ（。て（。いる（。のですよ。"),
    ("matrix", "Matrix", "母体、基盤、マトリックス", "14th Century", "mater (mother)", "An environment or material in which something develops; a surrounding medium or structure", "全（。て（。が（。、そこ（。から（。産まれ（。出（。づ（。る（。、「母（。なる（。る（。場所（。マーテル）』。（。その（。豊饒（。な（。る（。暗黒（。の中で（。、命は（。、静（。か（。に（。、自（。分（。だけ（。の（。かたち（。を（。、見（。つけ（。て（。いく（。のですよ。"),
    ("tissue", "Tissue", "組織、テッシュ、織物", "14th Century", "texere (to weave)", "Any of the distinct types of material of which animals or plants are made, consisting of specialized cells and their products", "バラバラ（。の（。細胞（。たちが（。、美し（。い（。秩序（。で「織（。り（。上げ（。られた（。テク）」もの（。たちの（。連（。なり。（。その（。一枚（。の（。布のような（。繋がり（。が（。、あなた（。という（。存在を、底（。知（。れ（。ぬ（。力（。で（。支え（。て（。いる（。のですよ。"),
    ("organ", "Organ", "器官、オルガン、組織", "Old English", "organon (tool, instrument)", "A part of an organism that is typically self-contained and has a specific vital function, such as the heart or liver in humans", "身体という（。名の（。巨大な（。「楽器（。オルガノン）』の（。一（。つ（。の（。部品（。（。その（。一（。つ（。一（。つに（。、自（。律（。的（。な（。る（。意志が（。宿（。り、宇宙の（。旋律を（。、奏（。で（。続け（。て（。いる（。のですよ。"),
    ("vessel", "Vessel", "容器、船、血管", "13th Century", "vas (vase, vessel)", "A ship or large boat", "生命の（。エナジーを、目的地へと（。運ぶ「器（。ヴァス）』。（。血液（。を、あるいは（。言葉（。を（。、たゆ（。た（。わ（。ず（。、絶（。え（。間（。なく（。流（。し（。続ける（。その（。沈黙（。は（。、至高（。の（。愛（。その（。もの（。なの（。ですよ。"),
    ("duct", "Duct", "導管、管（。くだ（。）」、ダクト", "14th Century", "ducere (to lead)", "A channel or tube for conveying something, such as a fluid", "決（。められた（。場所へと（。、静（。か（。に「導（。く（。デュ）」ための（。道（。（。そこ（。を（。通（。る（。た（。びに（。、混（。沌（。は（。、一（。つ（。の（。美（。し（。い（。意思へと（。、純（。化（。さ（。れて（。いく（。のですよ。"),
    ("valve", "Valve", "弁（。べん（。）」、バルブ、真空管", "14th Century", "valva (folding door, literal: 'turning leaf')", "A device for controlling the passage of fluid through a pipe or duct, especially an automatic device that allows movement in one direction only", "逆（。流を（。許（。さ（。な（。い「回転（。する（。扉（。ヴァルヴァ）』。（。その（。峻（。烈（。な（。る（。決断（。が（。、生命（。の（。拍動を（。、一（。方（。向へと（。、力強（。く（。、押し（。出し（。て（。いく（。のですよ。"),
    ("starch", "Starch", "でんぷん、糊、スターチ", "14th Century", "strac (strong, stiff, literal: 'stiffening')", "An odorless, tasteless white substance occurring widely in plant tissue and obtained chiefly from cereals and potatoes", "太陽の（。エナジーを、結晶（。さ（。せて「硬（。く（。固（。め（。た（。スタ）』もの（。たちの（。記憶（。（。その（。素朴（。な（。る（。備（。えが（。、いつか（。、巨大（。な（。る（。飛躍を（。、静（。か（。に（。、支える（。の（。ですよ。"),
    ("protein", "Protein", "タンパク質、プロテイン", "19th Century", "protos (first, primary)", "Any of a class of nitrogenous organic compounds that consist of large molecules composed of one or more long chains of amino acids and are an essential part of all living organisms", "生命（。の（。中で「第一の（。プロト）」優先（。順位を（。持（。つ（。、根源（。の（。る（。建築（。石（。（。あなた（。の（。内（。なる（。伽（。藍（。を（。、精（。密（。に（。、丹念に（。、組（。み（。上げて（。いく（。、聖（。なる（。る（。素材（。です。"),
    ("lipid", "Lipid", "脂質、リピッド", "20th Century", "lipos (fat)", "Any of a class of organic compounds that are fatty acids or their derivatives and are insoluble in water but soluble in organic solvents", "エナジーを（。、一（。時（。の（。微（。睡（。みの中に「蓄（。え（。た（。リポス）』、温（。か（。な（。る（。沈黙（。（。その（。滑（。らかな（。る（。ヴェールが（。、あなた（。を（。、外界の（。荒波から、静（。か（。に（。、守（。って（。くれる（。のですよ。"),
    ("sugar", "Sugar", "砂糖、シュガー、甘言", "13th Century", "sharkara (gravel, sugar, literal: 'pebble')", "A sweet crystalline substance obtained from various plants, especially sugar cane and sugar beet, consisting essentially of sucrose", "大地（。の（。底（。に（。、煌（。め（。く「砂（。石（。シャルカラー）』のような（。、至高の（。甘（。い（。エナジー。（。その（。一粒（。一粒（。には（。、太陽の（。微笑（。みが（。、静（。か（。に（。封印（。さ（。れて（。いる（。のですよ。"),
    ("cause", "Cause", "原因、大義、コーズ", "13th Century", "causa (reason, judicial process, literal: 'origin')", "A person or thing that gives rise to an action, phenomenon, or condition", "全（。て（。の（。結末（。の（。背後に（。ある（。、「根源（。カウザ）という（。名の（。裁き（。』。（。なぜ（。あなた（。に（。それ（。が（。起（。き（。た（。のか、その（。一一点（。を（。視（。つ（。める（。とき（。、暗黒は（。消（。え（。、意味が（。、産（。声を（。上げます。"),
    ("spring", "Spring", "春、泉、バネ、スプリング", "Old English", "springan (to leap)", "A source of water coming from the ground", "大地の（。底（。から、突如（。として「跳（。ね（。出す（。スプリング）』、未知（。なる（。エナジー。（。その（。噴（。き（。出し（。続ける（。一（。点（。に、宇宙の（。全記憶が（。、眩（。し（。く（。弾（。け（。て（。いる（。のですよ。"),
    ("well", "Well", "井戸、泉、健康な、ウェル", "Old English", "well (well, spring)", "A shaft sunk into the ground to obtain water, oil, or gas", "深淵（。の（。喉（。元（。に（。、静（。か（。な（。る「水溜（。ま（。り（。ウェル）』を（。見（。出（。す（。こと（。。（。その（。汲（。め（。ど（。尽（。き（。ぬ（。慈（。し（。み（。が（。、あなた（。を（。、真（。の（。潤（。いへと（。、い（。つ（。ま（。でも（。誘（。う（。のですよ。"),
    ("font", "Font", "泉、洗礼盤、書体、フォント", "Old English", "fons (spring, fountain)", "A receptacle in a church for the water used in baptism", "言（。葉（。が（。産まれ（。ゆ（。く（。、至高（。の「源泉（。フォンス）』。（。その（。清（。廉（。な（。る（。輝（。きの（。下で（。、あなた（。は（。、再（。び（。新（。しい（。名前を（。、手（。に（。入れ（。る（。ことが（。できる（。のですよ。")
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
            word_id = f"{word_text.lower()}_origin"
            
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
                    "thinking": item[6] if len(item) > 6 else "起源とは、過去にある点ではなく、今この瞬間に絶えず湧き出している、生命の源泉のことなのです。",
                    "aftertaste": item[7] if len(item) > 7 else "全ての結末は、最初の一歩に予兆として含まれている。それを読み解くことこそが、知性という名の魔法なのですよ。",
                    "example": f"The scientist investigated the {word_text} of the problem to find a sustainable and effective solution.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["外側の複雑さに見惚れる前に、内側の単純な核を見つめてください。そこにこそ、真の宇宙の縮図があるのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Nucleus & Matrix (Cycle 78).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
