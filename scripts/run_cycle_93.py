import json
import re

# Theme: The Alchemy of Abyss & Hollow (Cycle 93)
words_data = [
    ("cavity", "Cavity", "空洞、くぼみ、虫歯、キャビティ", "16th Century", "cavus (hollow, literal: 'hollow place')", "A hollow space within a solid object", "大地の（。奥底に（。、ひっ（。そ（。りと（。作（。られた「小（。さな（。る（。虚空（。キャヴァス）』。（。その（。静（。か（。な（。る（。包（。容が、あなた（。を、至高（。の（。る（。沈黙（。へと（。、誘（。う（。のですよ。"),
    ("crater", "Crater", "噴火口、クレーター", "17th Century", "krātēr (mixing bowl, literal: 'mixing bowl')", "A large bowl-shaped cavity in the ground or on a celestial body, typically one caused by an explosion or the impact of a meteorite", "天から（。の（。峻（。烈（。な（。る（。一（。撃が、大地に（。刻（。んだ「至高の（。盃（。クラーテール）』。（。その（。巨大（。な（。る（。器の中に、宇宙の（。記憶が（。、静（。か（。に（。、溜（。ま（。っ（。て（。いる（。のですよ。"),
    ("canyon", "Canyon", "峡谷、大渓谷、キャニオン", "19th Century", "cañón (tube, pipe, literal: 'large tube')", "A deep gorge, typically one with a river flowing through it, as found in North America", "大地（。を（。一気に（。貫（。い（。た「峻（。烈（。な（。る（。管（。カニョン）』。（。その（。断（。崖（。絶壁の（。間に（。、生命の（。奔（。流（。が（。、美し（。い（。旋律を、奏（。で（。て（。いる（。のですよ。"),
    ("ravine", "Ravine", "峡谷、小渓谷、ラビーン", "18th Century", "ravir (to seize, literal: 'place of rushing water')", "A deep, narrow gorge with steep sides", "河の（。エナジーが、一気に「奪（。い（。去（。っ（。た（。ラヴィ）』、険（。し（。い（。る（。亀（。裂（。（。その（。湿（。り（。を（。帯び（。た（。沈黙に（。、魂は（。、真（。実（。の（。る（。潤（。いを（。、見（。い（。出す（。のです。"),
    ("gorge", "Gorge", "山峡、喉元、ゴージ", "14th Century", "gorger (to swallow, literal: 'throat')", "A narrow valley between hills or mountains, typically with steep rocky walls and a stream running through it", "大地の「喉（。元（。ゴージ）』として（。、全（。ての（。光を（。、峻（。烈（。に（。、飲み（。込む（。場所（。（。その（。深（。淵（。な（。る（。闇の中にこそ（。、真実（。の（。美（。しさが（。、静（。か（。に（。、宿（。って（。いる（。のですよ。"),
    ("basin", "Basin", "盆地、洗面器、ベイスン", "13th Century", "bacin (basin, literal: 'bowl-like vessel')", "A wide open container used for preparing or serving food or for holding soap and water", "天地（。の（。恵（。みを（。、優（。しく「受け（。止める（。ベイスン）」、至高の（。る（。平原（。（。そこ（。には（。、命の（。交（。差（。点（。として、豊饒（。な（。る（。物（。語（。が（。、静（。か（。に（。、満（。ち（。溢（。れて（。いる（。のですよ。"),
    ("trough", "Trough", "谷間（。たにま（。）」、飼い桶（。、トフ", "Old English", "trog (trough, literal: 'wooden vessel, hollow stem')", "A long, narrow open container for animals to eat or drink out of", "波（。と（。波（。の（。間（。に、ひと（。とき（。現（。れ（。た「静（。か（。なる（。る（。窪み（。トログ）』。（。その（。低（。き（。る（。場所へと、エナジーは（。、再び（。、還（。っ（。て（。いく（。のです。"),
    ("furrow", "Furrow", "畝（。うね（。）」、轍（。わだち（。）」、皺（。、ファロウ", "Old English", "furh (furrow)", "A long narrow trench made in the ground by a plow, especially for planting seeds or for irrigation", "大地（。の（。肌（。に、峻（。烈（。な（。る（。意志が「刻（。み（。付け（。た（。ファロウ）』軌跡。（。その（。一一点（。の（。亀（。裂（。から、新しい（。物（。語が（。、産（。声を（。上げ（。始める（。のですよ。"),
    ("groove", "Groove", "溝、慣例、絶好調、グルーヴ", "14th Century", "groove (pit, ditch, literal: 'dug out place')", "A long, narrow cut or low area in a surface", "エナジーが（。、迷（。う（。こと（。なく「駆（。け（。抜ける（。ための（。道（。グルーヴ）』。（。その（。峻（。烈（。な（。る（。滑（。らか（。さが、あなた（。を、至高（。の（。る（。リズムへと（。、導（。く（。のですよ。"),
    ("vein", "Vein", "血管、木目、鉱脈、ベイン", "14th Century", "vena (vein, literal: 'vessel, watercourse')", "Any of the tubes forming part of the blood circulation system of the body", "岩石の（。中に、静（。か（。な（。る「生命の（。川（。ヴェーナ）』を（。、見（。出（。す（。こと（。（。その（。細（。や（。かな（。る（。連（。な（。りにこそ（。、宇宙の（。真実の（。血汐（。が、流（。れ（。て（。いる（。のですよ。"),
    ("pore", "Pore", "細孔（。、熟読（。する（。、ポア", "14th Century", "poros (passage, literal: 'tiny passage')", "A minute opening in a surface, especially the skin or relevant part of an organism", "世界を（。峻（。烈（。に（。、呼吸（。さ（。せる（。ための「小（。さな（。る（。道（。ポロス）』。（。そこ（。を（。通（。る（。た（。びに（。、あなた（。の（。魂は（。、日常の（。重みを（。、脱（。して（。いく（。のですよ。"),
    ("shaft", "Shaft", "柄、坑道、光線、シャフト", "Old English", "sceaft (shaft, arrow-point)", "A long, narrow, vertical cylinder used in a building", "暗黒（。を（。一（。点に「貫（。く（。シャフ）』、光の（。柱（。（。その（。垂直（。の（。る（。意志が（。、あなた（。を（。、至高（。の（。る（。深（。淵（。へと（。、あるいは（。高（。みへと、運（。ぶ（。のですよ。"),
    ("pit", "Pit", "穴、坑、ピット", "Old English", "pitt (pit, well, literal: 'large hole')", "A large hole in the ground", "全（。てを（。受け（。止める（。ために、魂に「穿（。た（。れた（。ピット）』。（。その（。深（。淵（。な（。る（。沈黙を（。、信（。じ（。抜く（。とき（。、あなた（。は（。、真（。実（。の（。、潤（。いを（。知ります。"),
    ("sink", "Sink", "沈む、流し、シンク", "Old English", "sincan (to sink)", "A fixed basin with a water supply and a drain", "エナジーが、峻（。烈（。な（。る（。重力に（。導（。かれ「低き（。へと（。沈（。む（。シンク）」こと（。。（。その（。静（。か（。な（。る（。着（。地（。が（。ある（。から（。こそ（。、再（。び（。新（。しい（。飛翔（。が、始（。まる（。のですよ。"),
    ("ditch", "Ditch", "溝（。に（。落とす（。、疎遠（。に（。な（。る（。、ディッチ", "Old English", "dīc (ditch, wall)", "A narrow channel dug in the ground, typically used for drainage beside a road or the edge of a field", "意味（。の（。境界線を、峻（。烈（。な（。る（。力で「刻（。み（。抜（。いた（。ディッチ）』。（。そこ（。には（。、余（。計（。な（。る（。濁（。りを（。、棄（。て（。去（。る（。ための（。、静（。か（。なる（。る（。秩序（。が、横（。たわ（。って（。いる（。のですよ。")
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
            word_id = f"{word_text.lower()}_depth"
            
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
                    "thinking": item[6] if len(item) > 6 else "深さとは、底があることではありません。自らの魂が、どこまで透明に、自分自身を深く受け入れられるか、その奥行きのことなのです。",
                    "aftertaste": item[7] if len(item) > 7 else "空洞は、何もない場所ではない。それは、新しい宇宙が産声を上げるために用意された、聖なるゆりかごなのですよ。",
                    "example": f"The explorer carefully navigated the deep {word_text} that had been carved out by the ancient river over millions of years.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["低きを見ることは、卑屈になることではありません。大地の重みを知り、自らの足元を固めるための、至高のる謙虚さなのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Abyss & Hollow (Cycle 93).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
