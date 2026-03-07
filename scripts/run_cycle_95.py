import json
import re

# Theme: The Alchemy of Speculum & Specularity (Cycle 95)
words_data = [
    ("specularity", "Specularity", "鏡面性、反射性、スペキュラリティ", "19th Century", "speculum (mirror, literal: 'of a mirror')", "The quality or state of being specular; the power or property of reflecting light or images as a mirror does", "世界を「歪（。み（。な（。く（。写（。し（。出す（。スペキュラ）』、至高の（。る（。透明（。さ（。（。その（。一一点（。の（。迷（。い（。も（。な（。い（。反射（。に（。よ（。って（。、あなた（。は（。、自分（。自身の実体（。を（。、眩（。しい（。ほど（。に（。、自覚（。する（。のです。"),
    ("specular", "Specular", "反射的な、鏡のような、スペキュラー", "14th Century", "speculum (mirror, literal: 'mirror-like')", "Relating to or having the properties of a mirror", "魂（。を、美し（。い「鏡（。スペキュ）』へと（。変える（。こと（。（。外界の（。ノイズを（。完全（。に（。脱（。し（。、ただ（。一（。点（。の（。真実（。を（。、至高（。の（。る（。輝き（。で（。、跳（。ね（。返（。し（。て（。ください。"),
    ("resonance", "Resonance", "共鳴、響き、レゾナンス", "15th Century", "re- (again) + sonare (to sound, literal: 'sounding again')", "The quality in a sound of being deep, full, and reverberating", "他者の（。鼓動（。を（。、自らの（。内で「再び（。リ）奏（。で（。る（。ソナン）」こと（。。（。その（。静（。か（。な（。る（。同調が（。、孤独（。な（。る（。祈（。りを、眩（。し（。い（。る（。シンフォニーへと、変（。え（。る（。のですよ。"),
    ("icon", "Icon", "偶像、聖像、アイコン", "16th Century", "eikōn (image, likeness, literal: 'image')", "A representative symbol of something", "目（。に（。見（。え（。な（。い（。真理を、一（。つ（。の「かたち（。アイコン）』に（。落（。と（。し（。込（。ん（。だ（。もの（。（。その（。一点（。の（。象（。徴から、宇宙の（。全記憶が、静（。か（。に（。、溢（。れ（。出し（。ます。"),
    ("idol", "Idol", "偶像、アイドル", "13th Century", "eidōlon (image, phantom)", "An image or representation of a god used as an object of worship", "自ら（。の（。情熱を（。投（。影（。し（。た、峻（。烈（。な（。る「幻（。像（。アイドル）』。（。その（。眩（。し（。い（。残像に（。、人々は（。、何（。を（。、祈（。る（。の（。でしょうか。"),
    ("token", "Token", "しるし、形見、トークン", "Old English", "tācn (sign, mark, literal: 'sign')", "A thing serving as a visible or tangible representation of a fact, quality, feeling, etc.", "想（。いを（。、一（。枚の（。貨幣（。の（。ように「峻（。烈（。に（。刻（。んだ（。し（。る（。し（。トークン）』。（。その（。小（。さな（。る（。断片が（。、真実（。の（。る（。証として（。、静（。か（。に（。、輝（。き続（。け（。る（。のです。"),
    ("trait", "Trait", "特徴、特性、トレイ（。ト", "16th Century", "trahere (to draw, literal: 'drawn line')", "A distinguishing quality or characteristic, typically one belonging to a person", "あなた（。の（。本質（。を、至高（。の（。る（。一本の（。糸（。で「描（。き（。出し（。た（。トレイ）』輪郭（。（。その（。峻（。烈（。な（。る（。個性が（。、世界（。を（。、新（。しく（。、塗り（。替（。え（。て（。いく（。のですよ。"),
    ("habit", "Habit", "習慣、癖、ハビット", "13th Century", "habere (to have, hold, literal: 'condition, appearance')", "A settled or regular tendency or practice, especially one that is hard to give up", "自（。らが「持（。ち（。続け（。（。ハビ）』て（。き（。た（。、日常の（。連（。な（。り（。（。その（。静（。か（。な（。る（。反（。復の（。中（。で（。、魂は（。、自分（。自身（。の（。定（。義（。を、再（。確認（。し（。て（。いく（。のです。"),
    ("custom", "Custom", "慣習、習慣、カスタム", "12th Century", "con- (together) + suescere (to become accustomed, literal: 'familiarity')", "A traditional and widely accepted way of behaving or doing something that is specific to a particular society, place, or time", "人々が（。共（。に（。、「歩（。み（。寄り（。、慣（。れ（。親（。し（。んだ（。カスト）』秩序（。（。その（。温（。かな（。る（。る（。時間の（。積（。層に（。、あなた（。の（。物語を（。、そっと（。、重ね（。て（。ください。"),
    ("use", "Use", "使用、有用、ユース", "13th Century", "uti (to use)", "The action of using something or the state of being used for a purpose", "与（。え（。られた（。エナジーを、正しい（。る「目的へと（。向ける（。ユティ）』、至高の（。る（。智慧（。（。その（。一一点（。の（。実践にこそ（。、真実（。の（。価値（。が（。宿（。ります。"),
    ("mark", "Mark", "印、目標、マーク", "Old English", "mearc (boundary, sign, literal: 'boundary sign')", "A small area on a surface having a different color from its surroundings, typically one caused by an accident or damage", "宇宙の（。広（。野に、峻（。烈（。に「打ち（。込ま（。れた（。し（。る（。し（。マーク）』。（。その（。一一点（。の（。境界にこそ（。、真実（。の（。る（。自覚が、産（。声を（。上げます。"),
    ("sign", "Sign", "しるし、合図、サイン", "13th Century", "signum (mark, token, literal: 'mark')", "An object, quality, or event whose presence or occurrence indicates the probable presence or occurrence of something else", "意味（。を、峻（。烈（。な（。る「定（。位（。シグヌム）』に（。変える（。こと（。（。その（。一（。つ（。一（。つの（。断片が（。、世界（。の（。真実（。を、静（。か（。に（。、指（。し（。示（。し（。て（。いる（。のですよ。"),
    ("seal", "Seal", "印章、封印、シエル", "13th Century", "sigillum (little sign, literal: 'little sign')", "A device or substance used to join two things together so as to prevent them from coming apart or to prevent anything from passing between them", "至光（。の（。る（。真実を、美し（。い（。「閉じ（。込（。め（。た（。シエル）』至（。高の（。る（。定（。点（。（。その（。封（。印を（。解（。く（。とき（。、あなた（。は（。、宇宙の（。深（。淵（。な（。る（。記憶と（。、出会（。い（。ます。"),
    ("stamp", "Stamp", "切手、刻印、スタンプ", "Old English", "stempan (to tread)", "To press a device against a surface in order to leave a mark or pattern", "大地を（。力（。強く「踏（。み（。し（。め（。た（。スタンプ）』痕跡（。（。その（。峻（。烈（。な（。る（。存在（。感に（。、世界（。は（。、一瞬にして（。、静（。まり（。返（。り（。ます。"),
    ("trace", "Trace", "痕跡、線、トレース", "14th Century", "trahere (to draw, literal: 'drawing')", "A mark, object, or other indication of the existence or passing of something", "過ぎ（。去（。っ（。た（。時間の（。、「かす（。か（。な（。る（。る（。線（。トレ）』。（。その（。美（。し（。い（。幾（。何（。学（。を（。読み（。解（。く（。とき（。、絶（。望は、最高（。の（。る（。希望へと（。、変（。わ（。る（。のですよ。")
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
            word_id = f"{word_text.lower()}_reflect_v"
            
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
                    "thinking": item[6] if len(item) > 6 else "反射とは、拒絶ではなく、受け入れたエナジーを一転して返すための、至高のる対話の形式なのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "鏡の中の自分を視つめることは、孤独を深めることではなく、宇宙という名のもう一人の自分を見出すことなのですよ。",
                    "example": f"The high {word_text} of the crystal surface made it difficult to see the underlying structure without polarizing filters.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["しるしを残すことは、名前を残すことではない。自分がここに在ったという、宇宙への静かなる感謝を刻み込むことなのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["specular"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Speculum & Specularity (Cycle 95).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
