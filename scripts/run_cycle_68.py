import json
import re

# Theme: The Alchemy of Expedition & Horizon (Cycle 68)
words_data = [
    ("expedition", "Expedition", "遠征、探検、エクスペディション", "15th Century", "ex- (out) + pes (foot, literal: 'free the feet')", "A journey undertaken by a group of people with a particular purpose, especially that of exploration, scientific research, or war", "停（。滞（。という（。名の（。鎖（。から、「足（。ペディ）を（。解（。き（。放（。つ（。エクス）」こと（。。（。未知（。なる（。領域（。へと（。、自分（。自身を（。投げ（。出す（。、誇（。り（。高い（。冒（。険（。の（。始まり。"),
    ("caravan", "Caravan", "隊商、キャラバン、移動住宅", "16th Century", "karwan (caravan, camel train)", "A group of people, especially traders or pilgrims, traveling together across a desert in Asia or North Africa", "孤独（。な（。る（。荒野（。を（。、一つ（。の「群（。れ（。キャラバン）』となって（。進（。む（。こと（。。（。絶（。え（。間（。ない（。砂塵（。の（。中に（。、人（。々（。の（。絆（。が（。、美（。し（。い（。旋律（。を（。奏（。で（。て（。いる（。のですよ。"),
    ("itinerary", "Itinerary", "旅行日程、巡回、アイティナラリー", "15th Century", "iter (journey, way, literal: 'going')", "A planned route or journey", "ただの（。移動（。ではなく（。、あらかじめ（。決（。められた「道（。アイティ）の（。順（。序（。）」。（。そこ（。を（。辿（。る（。ことで（。、あなた（。は（。、予（。期（。せ（。ぬ（。真理（。へと（。、漕（。ぎ（。出す（。ことが（。でき（。る（。のですよ。"),
    ("waypoint", "Waypoint", "経由地、ウェイポイント", "20th Century", "way + point", "A reference point in physical space used for purposes of navigation, otherwise known as a landmark", "果て（。しない「道（。ウェイ）』の（。途中に（。、そっと（。置（。かれた「しるし（。ポイント）』。（。全（。ての（。通過（。点（。に、意味（。が（。宿（。って（。いる（。と（。知（。っ（。た（。とき（。、旅は（。至高の（。もの（。へと（。変（。わ（。り（。ます。"),
    ("transit", "Transit", "通過、移り変わり、トランジット", "15th Century", "trans- (across) + ire (to go, literal: 'going across')", "The carrying of people, goods, or materials from one place to another", "一つの（。場所に（。留（。ま（。る（。のを（。止め（。、ただ（。世界を「横（。切（。る（。トランス）よう（。に（。行く（。イ）」こと（。。（。その（。移（。ろ（。い（。ゆ（。く（。眩（。し（。さ（。を（。、魂は（。、いつ（。までも（。、噛（。み（。締（。め（。る（。のですよ。"),
    ("embark", "Embark", "乗船する、乗り出す、エンバーク", "16th Century", "en- (in) + barca (bark, boat)", "Go on board a ship, aircraft, or other vehicle", "不（。確かな（。日常（。を（。捨て（。、一つの「船（。バルカ）の中（。エン）へと（。）」一（。歩（。踏（。み（。出す（。こと（。。（。その（。決断（。が（。、昨日（。までの（。あなた（。を（。、遥（。かな（。る（。新（。世（。界へと（。誘（。う（。のです。"),
    ("port", "Port", "港、ポルテ、左舷", "Old English", "portus (harbor, entrance, literal: 'passage')", "A town or city with a harbor where ships load or unload, especially one where customs officers are stationed", "荒（。れ（。狂（。う（。大海原（。を（。越（。え（。た（。先にある（。、「入口（。ポルタ）」。（。そこ（。には（。、束の（。間（。の（。安（。ら（。ぎと（。、次（。な（。る（。旅立ちの（。予感が（。、静（。か（。に（。、満（。ち（。溢（。れて（。いる（。のですよ。"),
    ("dock", "Dock", "ドック、船渠（。せんきょ（。）」、着（。艦（。する（。、ドック", "14th Century", "dokke (trough, channel)", "A structure extending from the shore into a body of water to which a boat is tied", "旅の（。疲れ（。を（。癒（。し（。、自（。ら（。を（。整（。え（。る（。ための「深く（。静（。かな（。る（。場所に（。の（。ドック）』。（。そこ（。で（。、あなた（。は（。強個（。に（。な（。る（。再（。生を（。得（。て（。、再び（。宇宙へと（。、漕（。ぎ（。出す（。のですよ。"),
    ("helm", "Helm", "舵（かじ）、兜、管理", "Old English", "helma (handle, helm)", "A tiller or wheel and any associated equipment for steering a ship or boat", "巨大（。な（。船（。の（。行（。く（。末を（。、ただ「一（。つ（。の（。手（。で（。の（。握（。り（。ヘラム）』で（。決（。定（。する（。こと（。。（。責任（。の（。重（。厚（。な（。る（。沈黙が（。、あなた（。の（。指（。先に（。、静か（。に（。宿（。って（。いる（。のですよ。"),
    ("buoy", "Buoy", "ブイ、浮標（。ふひょう（。）」、浮（。か（。せる（。、ブイ", "13th Century", "boye (buoy, signal, literal: 'fetter, chain')", "An anchored float serving as a navigation mark, to show reefs or other hazards, or for mooring", "深淵（。の（。底（。に（。、静（。かな（。る「鎖（。ボイ）』で（。繋（。留（。さ（。れ（。た（。）」、光（。の（。シグナル。（。どんな（。荒（。波の中（。でも（。、浮か（。び（。続ける（。その（。姿に（。、旅人（。は（。一瞬の（。希（。望を（。見（。出（。す（。のですよ。"),
    ("abyss", "Abyss", "深淵、奈（。落（。の（。底（。、アビス", "14th Century", "a- (without) + bussos (bottom, literal: 'bottomless')", "A deep or seemingly bottomless chasm", "「底（。ブッソス）が（。な（。い（。ア）」ほど（。の（。、巨大（。な（。虚無（。（。その（。暗黒（。の（。中を（。、ただ（。一（。筋（。の（。光（。として（。、貫（。き（。抜（。く（。こと（。。（。それ（。こそ（。が（。、至高（。の（。エナジー（。なの（。ですよ。"),
    ("isthmus", "Isthmus", "地峡（ちきょう）、イスムス", "16th Century", "isthmos (neck, passage)", "A narrow strip of land with sea on either side, forming a link between two larger areas of land", "二（。つの（。大陸を（。、ギリギリ（。の（。ところで（。繋（。ぎ（。止める「首（。イスモス）』のような（。場所（。（。その（。危（。うい（。細（。道にこそ（。、世界を（。一（。つ（。に（。する（。ための（。、真（。実（。の（。架（。け（。橋が（。あります。"),
    ("archipelago", "Archipelago", "列島、群島、多島海", "16th Century", "arkhi- (chief) + pelagos (sea, literal: 'chief sea, Aegean Sea')", "A group of islands", "「母（。なる（。海（。ペラゴス）』の中心（。に（。、バラバラ（。に（。煌（。め（。く（。島々（。。（。その（。不（。連続（。な（。連（。なりが（。、目（。に（。は（。見（。え（。な（。い（。一（。つ（。の（。巨大（。な（。意志（。を（。、物（。語（。って（。いる（。のですよ。"),
    ("altitude", "Altitude", "高度、標高、アルチュード", "14th Century", "altus (high)", "The height of an object or point in relation to sea level or ground level", "大地から（。どこ（。まで（。も「高（。く（。アルト）」至（。る（。こと（。。（。空気（。が（。薄く（。な（。る（。た（。び（。に（。、あなた（。の（。視座（。は（。、より（。透（。き（。通（。っ（。た（。、高（。次元（。な（。る（。もの（。へと（。変（。わ（。り（。ます。"),
    ("sextant", "Sextant", "六分儀（。ろくぶんぎ（。）」、セクスタント", "18th Century", "sextans (a sixth part)", "An instrument with a graduated arc of 60° and a sighting mechanism, used for measuring the angular distances between objects and especially for taking altitudes in navigation", "宇宙（。の（。全（。てを「六（。つ（。の（。一（。つ（。セクスタ）」として（。切り（。取り（。、自分（。の（。場所を（。知（。る（。ための（。秤（。（。星（。と（。海（。の（。間（。に、揺（。る（。ぎ（。な（。い（。一点を（。、見（。つけ（。て（。ください。")
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
            word_id = f"{word_text.lower()}_horizon"
            
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
                    "thinking": item[6] if len(item) > 6 else "旅とは、目的地にたどり着くことではなく、歩む道そのものに魂を刻み込んでいく行為なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "水平線は、この世の終わりではなく、無限という名の未知の始まりを、静かに指し示しているのですよ。",
                    "example": f"The scientific {word_text} discovered several new species in the uncharted reaches of the deep ocean.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["留まることは安らぎではなく、停滞であり、ただ歩き続けることこそが、唯一の休息なのかもしれません。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["expedient", "transient"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Expedition & Horizon (Cycle 68).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
