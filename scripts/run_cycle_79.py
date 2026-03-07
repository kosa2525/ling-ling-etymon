import json
import re

# Theme: The Alchemy of Torrent & Tide (Cycle 79)
words_data = [
    ("torrent", "Torrent", "激流、急流、連発、トレント", "16th Century", "torrere (to parch, literal: 'burning/roaring stream')", "A strong and fast-moving stream of water or other liquid", "乾（。き（。を（。癒（。し（。、全（。てを（。飲（。み（。込（。む「唸（。り（。を（。上げる（。トル）』、激（。烈（。な（。る（。川の流れ（。（。その（。容赦（。な（。き（。エナジーに（。、魂は（。、一瞬にして（。、全（。身を（。委（。ね（。、新（。しい（。地平へと（。、連（。れ（。去（。ら（。れる（。のですよ。"),
    ("cataract", "Cataract", "大（。瀑（。布（。、白内障、カタラクト", "15th Century", "kata- (down) + arassein (to strike, smash, literal: 'dashing down')", "A large waterfall"),
    ("maelstrom", "Maelstrom", "大渦巻（。、大混乱、メイルストローム", "17th Century", "malen (to grind) + stroom (stream, literal: 'grinding stream')", "A powerful whirlpool in the sea or a river", "地上の（。全（。ての（。記憶を「粉（。々に（。打ち（。砕き（。マール）飲み（。込（。む（。ストローム）」、巨大な（。る（。渦（。（。そこ（。には（。、破壊（。と（。創造（。が（。、美し（。い（。螺旋（。となって（。、永遠（。に（。、踊（。っ（。て（。いる（。のですよ。"),
    ("eddy", "Eddy", "渦、逆（。流（。、エディ", "15th Century", "ed- (back) + ea (water, literal: 'backward water')", "A circular movement of water, counter to a main current, causing a small whirlpool", "本（。流（。に（。抗（。い、静（。か（。に「後ろへへと（。エ）還（。る（。）」、小（。さな（。る（。渦（。（。その（。逆説（。的（。な（。る（。遊（。悦の中にこそ（。、真（。実（。の（。思索が（。、宿（。る（。ことが（。できる（。のですよ。"),
    ("geyser", "Geyser", "間欠泉（。かんけつせん（。）」、ガイザー", "18th Century", "geysa (to gush, literal: 'gusher')", "A hot spring in which water intermittently boils, sending a tall column of water and steam into the air", "地底（。の（。情熱が（。、限界を（。越元（。て（。、「噴（。き（。出す（。ゲイザ）』熱（。き（。る（。柱（。（。その（。峻（。烈（。な（。る（。飛翔（。が（。、停（。滞（。した（。日常に、一（。時（。の（。、目（。覚め（。を（。、与（。えて（。くれる（。のですよ。"),
    ("aquifer", "Aquifer", "帯水層、アクイファー", "19th Century", "aqua (water) + ferre (to bear, literal: 'water-bearing')", "A body of permeable rock which can contain or transmit groundwater", "見（。え（。な（。い（。地底（。に（。、命の（。水を「静か（。に（。運（。び（。、蓄（。え（。る（。ファー）大地（。アクア）」。（。その（。重厚（。な（。る（。沈黙に（。、全（。ての（。地上の（。命は（。、そっと（。支（。え（。られて（。いる（。のですよ。"),
    ("cistern", "Cistern", "水槽、貯水池、シスターン", "13th Century", "cista (box, literal: 'box for water')", "A tank for storing water, especially one supplying taps or as part of a flushing toilet", "命（。の（。エナジーを、そっと「箱（。チスタ）』の中に（。預（。か（。る（。）」場所（。（。そこ（。には（。、次（。なる（。渇（。きを（。癒（。す（。ための（。、静（。か（。な（。る（。準備が（。、幾（。重（。にも（。、満（。ち（。て（。いる（。のですよ。"),
    ("levee", "Levee", "堤防、レビー、朝の接見", "18th Century", "lever (to raise, literal: 'raised')", "An embankment built to prevent the overflow of a river", "河の（。氾（。濫（。を（。防ぐ（。ために、土を「高く（。盛り（。上げた（。レヴェ）』、守（。護（。の（。壁（。（。その（。静（。かな（。る（。境界が（。、あなた（。の（。安（。ら（。ぎを、底（。知（。れ（。ぬ（。力（。で（。守って（。くれる（。のですよ。"),
    ("dike", "Dike", "堤防、溝（。みぞ（。）」、ダイク", "Old English", "dīc (ditch, wall, literal: 'something dug out')", "A long wall or embankment built to prevent flooding from the sea", "大地に（。峻（。烈（。な（。る「溝（。ディック）』を（。刻（。み（。、水（。の（。行（。き（。先を（。変元（。る（。こと（。。（。その（。一（。本の（。線に（。、人間（。の（。知恵（。と（。、自然への（。畏（。敬（。が（。、共（。存（。し（。て（。いる（。のです。"),
    ("weir", "Weir", "堰（せき）、ウィア", "Old English", "wer (weir, literal: 'to cover, defend')", "A low dam built across a river to raise the level of water upstream or regulate its flow", "河の（。呼吸を（。、「優（。しく（。覆（。い（。整える（。ウェル）』ための（。階段（。（。そこ（。を（。越（。え（。て（。流（。れ（。落ち（。る（。水の（。輝きに（。、一（。時（。の（。静寂（。が（。、宿（。る（。のですよ。"),
    ("sluice", "Sluice", "水門、スルース", "14th Century", "ex- (out) + claudere (to close, literal: 'excluding, shutting out')", "A sliding gate or other device for controlling the flow of water, especially one in a lock or dam", "真理の（。奔流を（。、「一時に（。放（。つ（。ス）ために、閉（。ざ（。された（。ルース）」門。（。あなたが（。その（。扉を（。開（。ける（。とき（。、新（。しい（。エナジーは（。、一気に（。、世界へと（。、溢出し（。ます。"),
    ("jetty", "Jetty", "防波堤、桟橋（。さんばし（。）」、ジェッティ", "15th Century", "jetee (thrown out, literal: 'something thrown forth')", "A landing stage or small pier at which boats can dock or be moored", "海へと（。向（。かって（。、身を「投げ（。出さ（。れた（。ジェテ）』、孤独（。な（。る（。最前線（。（。その（。峻（。烈（。な（。る（。指先が、荒（。れ（。狂（。う（。波（。から（。、港（。を（。、静（。か（。に（。守り（。抜く（。のですよ。"),
    ("quay", "Quay", "埠頭（ふとう）、キー", "14th Century", "chai (quay, literal: 'fence, enclosure')", "A concrete, stone, or metal platform lying alongside or projecting into water for loading and unloading ships", "船（。を（。優（。しく「囲（。う（。キ）』ための（。、盤石（。な（。る（。岸辺（。（。そこ（。では（。、遥（。かな（。る（。旅路と（。、日常の（。安（。ら（。ぎが（。、眩（。しい（。光（。の中で（。、一（。瞬（。、交（。差（。し（。ます。"),
    ("wharf", "Wharf", "波止場（。、ワーフ", "Old English", "hwearf (shore, bank, literal: 'turning place')", "A level quayside area to which a ship may be moored to load and unload", "旅の（。エナジーが「再（。び（。回（。帰（。する（。フワ）』、始まり（。の（。場所（。（。そこ（。に（。船が（。繋がる（。た（。びに（。、世界（。の（。どこ（。かの（。物語が（。、また（。一（。つ（。、静か（。に（。、幕（。を（。閉じ（。る（。のですよ。"),
    ("skiff", "Skiff", "小舟、軽舟、スキフ", "16th Century", "schifo (little boat)", "A shallow, flat-bottomed open boat with a sharp bow and square stern", "波間を（。滑（。る（。ように「軽く（。、小（。さな（。る（。船（。スキフ）』。（。その（。危（。う（。い（。ほどの（。軽快（。さが（。、あなた（。を（。、誰も（。辿（。り（。着（。け（。な（。い（。、秘密の（。入り江へと（。、運（。んで（。くれる（。のですよ。")
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
            word_id = f"{word_text.lower()}_liquid"
            
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
                    "thinking": item[6] if len(item) > 6 else "流れとは、形を捨てることで、あらゆる形へと産まれ変わることができる、生命の至高の実践なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "渦巻は、自らを中心へと向かわせながら、同時に世界を外側へと押し広げる、静かなる矛盾の舞いなのですよ。",
                    "example": f"The heavy rainfall turned the small creek into a raging {word_text} that threatened to flood the nearby village.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["止まることは死ではなく、新たな巡りへの準備。流れることは生。その二つが交差する瞬間に、美しさが宿るのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Torrent & Tide (Cycle 79).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
