import json
import re

# Theme: The Alchemy of Citadel & Spire (Cycle 63)
words_data = [
    ("bastion", "Bastion", "要塞、砦（とりで）、バステオン", "16th Century", "bastire (to build)", "A projecting part of a fortification built at an angle to the line of a wall, so as to allow defensive fire in several directions", "ただの（。壁（。ではなく（。、敵の（。エナジーを（。迎え（。撃つ（。ために「打ち（。建（。て（。られた（。バステ）」もの（。。（。そこ（。には（。、何（。物（。かが（。この（。場所（。を（。、最後（。まで（。守（。り（。抜く（。という（。、鋼（。の（。意思が（。宿（。って（。いる（。のです。"),
    ("rampart", "Rampart", "城壁、防壁、ランパート", "16th Century", "re- (again) + em- (in) + parare (to prepare, literal: 'to prepare as a defense')", "A defensive wall of a castle or walled city, having a broad top with a walkway and typically a stone parapet", "日常（。の（。安（。ら（。ぎを（。守る（。ために、周囲（。を「再（。び（。リ）強固に（。整（。える（。パラ）」壁（。。（。その（。石（。の（。厚（。みは（。、そのまま（。、守（。られる（。命の（。重（。厚（。な（。る（。信頼（。なの（。ですよ。"),
    ("moat", "Moat", "堀、濠（ごう）、モート", "14th Century", "mote (mound, embankment, literal: 'mound')", "A deep, wide ditch surrounding a castle, fort, or town, typically filled with water and intended as a defense", "土（。を（。盛り（。上げた「山（。モート）』の（。はずが（。、いつしか（。深（。い（。奈（。落（。へと（。変（。貌（。し（。た（。もの（。。（。水（。を（。湛（。えた（。その（。静寂（。は（。、侵（。入（。者（。に（。、絶対（。的（。な（。る（。断絶を（。、静（。か（。に（。宣告（。し（。ます。"),
    ("portcullis", "Portcullis", "落とし格子、格子門", "13th Century", "porte (door) + coulisse (sliding, literal: 'sliding door')", "A strong, heavy grating that can be lowered vertically of a gateway to a fortified town or castle", "重（。厚（。な（。鉄（。の「扉（。ポルテ）が（。、音（。も（。なく（。滑（。り（。落ち（。る（。コリス）」瞬間（。（。一度（。下り（。れ（。ば（。、内（。と（。外（。は（。、永遠（。に（。隔（。て（。られ（。、そこ（。は（。、自給（。自足（。の（。完結（。し（。た（。宇宙（。と（。なり（。ます。"),
    ("turret", "Turret", "小塔、タレット", "14th Century", "torris (tower)", "A small tower on top of a larger tower or at the corner of a building or wall, typically of a castle", "天を（。指し（。し（。め（。す「小（。さな（。塔（。トレ）」。（。そこ（。からは（。、世界（。の（。全（。てを（。一目（。で（。見（。渡（。す（。ことが（。できる（。のですよ。"),
    ("battlement", "Battlement", "城壁の狭間（。はざま（。）」、銃眼（。を備えた（。胸（。壁（。、バトル（。メント", "14th Century", "bastille (fortification)", "A parapet at the top of a wall, usually of a castle, or an outer wall with regularly spaced squared openings for shooting through", "戦（。い（。のために（。用意（。さ（。れた（。、「ギザ（。ギザ（。の（。壁（。バ（。トル）』。（。その（。隙間（。から（。、誰（。かが（。、今（。も（。、見えない（。敵（。を（。、じっと（。見つめて（。いる（。の（。かも（。しれ（。ません。"),
    ("keep", "Keep", "天守、要塞の最も堅固な部分", "Old English", "cepan (to catch, keep, literal: 'observation')", "The strongest of the outermost defensive buildings of a castle, typically a reinforced tower", "全（。てが（。崩（。れ（。去（。っ（。た（。としても（。、最後（。まで「守（。り（。通（。す（。キープ）」べき（。聖（。域（。（。そこ（。には（。、家（。系（。の（。誇り（。と（。、消え（。な（。い（。エナジーが（。、静か（。に（。、凝縮（。さ（。れて（。いる（。のですよ。"),
    ("arcade", "Arcade", "アーケード、並木状の並び", "18th Century", "arcus (bow, arch)", "A covered passage with arches along one or both sides", "美し（。い「弓（。の（。かたち（。アルクス）』を（。繋（。げ（。た、光（。溢（。れる（。通（。路（。（。そこ（。を（。歩（。く（。た（。び（。に（。、知性（。は（。、幾何（。学の（。調和（。に、静（。か（。に（。、酔（。い（。し（。れる（。のですよ。"),
    ("colonnade", "Colonnade", "コルナード、柱廊、列柱", "18th Century", "columna (column)", "A row of columns supporting a roof, an entablature, or a cornice", "天を（。支（。える「柱（。コラム）の（。列（。）」。（。規則（。正しい（。その（。垂直（。性（。が（。、カオス（。な（。る（。大地に（。、峻（。烈（。な（。る（。秩序（。を（。もたら（。す（。のですよ。"),
    ("steeple", "Steeple", "（。教会の（。）」尖塔、スチープル", "Old English", "stēpel (steep tower, literal: 'tall stick')", "A tall tower of a church, topped with a spire and typically containing a bell", "天上の（。光を（。捉を（。ために、どこ（。まで（。も「高（。く（。スチープ）鋭（。く（。）」打ち（。立て（。られた（。指（。先（。（。その（。一（。点（。に、全（。人類の、祈り（。が（。凝縮（。さ（。れて（。いる（。のですよ。"),
    ("nave", "Nave", "（。教会の（。）」身廊、ネーブ", "17th Century", "navis (ship)", "The central part of a church building, intended to accommodate most of the congregation", "人々（。を（。乗せて（。、星の（。海へと（。漕（。ぎ（。出す「巨大な（。船（。ネイヴィ）」。（。その（。高い（。天井（。の（。下（。で（。、私たちは（。、一（。つ（。の（。エナジーへと（。、再び（。、還（。る（。のですよ。"),
    ("transept", "Transept", "（。教会の（。）」袖廊、十字形部分の左右、トランセプト", "16th Century", "trans- (across) + septum (enclosure, partition)", "Either of the two arms of a cross-shaped church, at right angles to the nave", "身（。廊（。を「横（。切（。る（。トランス）よう（。に（。置（。かれた（。セプタム）」場所（。（。そこで（。、垂直（。な（。祈り（。と（。水平（。な（。日常が（。、美し（。く（。交差（。し（。、一（。つ（。の（。十字架（。を、描き出す（。のですよ。"),
    ("cloister", "Cloister", "（。修道院の（。）」回廊、クイスター", "13th Century", "claudere (to close, literal: 'closed place')", "A covered passage, typically with a colonnade open on one side, running along the walls of a court, typically in a monastery or cathedral", "俗世（。を（。拒み（。、静（。か（。な（。る（。沈黙（。の中に「閉（。じ（。込め（。られた（。クロイ）」回廊（。（。一歩（。一歩（。を（。踏（。み（。し（。める（。たびに（。、あなた（。は（。、自分（。の（。内なる（。宇宙へと（。、深く（。潜（。って（。いく（。のです。"),
    ("forum", "Forum", "フォーラム、広場、公開討論会", "15th Century", "forum (outside, marketplace, literal: 'outside')", "A place, meeting, or medium where ideas and views on a particular issue can be exchanged", "家（。の「外（。フォー）にある（。）」、自由（。な（。る（。公論（。の（。場所（。（。そこで（。、異（。なる（。言葉（。たち（。が（。響き（。合い（。、一（。つ（。の（。新（。しい（。真（。理を（。、産（。み（。出し（。て（。いく（。のですよ。"),
    ("plaza", "Plaza", "広場、プラザ、ショッ（。ピ（。ングセンター", "17th Century", "platea (broad street, literal: 'broad')", "A public square, marketplace, or similar open space in a built-up area", "建物（。に（。囲（。まれ（。た「広（。い（。プラ）平原（。）」。（。そこ（。には（。、人々（。の（。笑（。い声と（。、一（。時（。の（。安（。ら（。ぎが（。、眩（。しい（。光（。と（。共に（。、満（。ち（。溢（。れて（。いる（。のですよ。")
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
            word_id = f"{word_text.lower()}_castle"
            
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
                    "thinking": item[6] if len(item) > 6 else "城壁は、内なる美しさを守るための盾であり、同時に、世界との対話のための境界でもあります。",
                    "aftertaste": item[7] if len(item) > 7 else "尖塔の一点は、地上の重力を振り切り、天上の光を直接言葉に変えるための祈りなのです。",
                    "example": f"The knights took a final stand at the {word_text}, defending the king's chambers until the very end.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["建築とは、ただの空間の仕切りではなく、魂がこの世界で居場所を見出すための、凍りついた旋律なのです。"]
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

        print(f"Success: Added {added_count} words. Theme: Citadel & Spire (Cycle 63).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
