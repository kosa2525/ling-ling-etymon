import json
import re

# Theme: The Alchemy of Ultra & Extra II (Cycle 104)
words_data = [
    ("hyper", "Hyper", "超越した、過剰な、ハイパー", "19th Century", "huper (over, above, literal: 'over')", "Over; excessively; above", "限界を（。一（。気へと「越元（。た（。ハイパー）』、至高の（。る（。エナジー。（。その（。眩（。し（。い（。煌（。めきこそが、世界を（。、眩（。しい（。ほど（。に（。、変（。容（。さ（。せ（。て（。いく（。のですよ。"),
    ("hypo", "Hypo", "下の、過少の、ハイポ", "19th Century", "hupo (under, below, literal: 'under')", "Under; below; less than normal", "深淵の（。底（。へと、静（。か（。に「潜（。る（。ハイポ）』こと（。（。その（。目（。に（。見（。え（。な（。い（。沈黙（。の中に、真実（。の（。る（。る（。根源が（。、宿（。って（。いる（。のです。"),
    ("super", "Super", "上の、超越した、スーパー", "15th Century", "super (above, over, literal: 'above')", "Above; over; beyond", "日常を（。優（。し（。く（。、かつ「峻（。烈（。に（。越える（。スーパー）』、至高の（。る（。視座。（。その（。圧倒（。的な（。る（。存在（。感に、人々は、ただ（。、眩（。惑（。さ（。れ（。る（。のですよ。"),
    ("sub", "Sub", "下の、副次的な、サブ", "14th Century", "sub (under, below, literal: 'below')", "Under; below; secondary", "巨大な（。影の（。中に（。、そっと「潜（。ま（。せた（。サブ）』、至高の（。る（。る（。智慧（。（。、日常の（。重みを、静（。か（。に（。、支（。え（。て（。いる（。の（。ですよ。"),
    ("meta", "Meta", "後の、超越した、メタ", "19th Century", "meta (after, beyond, literal: 'after, beyond')", "After, beyond, with, or adjacent to", "物（。語が（。終わ（。っ（。た「後（。に（。も（。在（。る（。メタ）』至高（。の（。る（。余韻（。（。その（。一一点（。の（。客観（。こそが、世界を（。、真（。実（。へと（。導（。き（。ます。"),
    ("para", "Para", "横の、超越した、パラ", "14th Century", "para (beside, beyond, literal: 'beside')", "Beside, beyond, or around", "日常（。の「隣（。に（。在（。る（。パラ）』、至高（。の（。る（。平行（。世界（。（。その（。不（。可（。思議な（。る（。共鳴を、魂で、感（。じ（。て（。ください。"),
    ("dia", "Dia", "通して、横断して、ダイア", "14th Century", "dia (through, across, literal: 'through')", "Through, across, or between", "二つの（。地点を、一（。気へと「貫（。く（。ダイア）』エナジー。（。その（。不（。動の（。る（。一直線が、不（。可能を（。、眩（。しい（。る（。る（。奇跡へと（。、変（。え（。ます。"),
    ("ana", "Ana", "上の、再び、アナ", "15th Century", "ana (up, back, again, literal: 'up')", "Up, back, or again", "命を（。再び「呼び（。覚（。ます（。アナ）』、峻（。烈（。な（。る（。る（。飛躍（。（。その（。瑞々（。し（。い（。る（。始（。ま（。りにこそ、至高の（。真実が宿（。ります。"),
    ("cata", "Cata", "下の、反対の、カタ", "15th Century", "kata (down, away, literal: 'down')", "Down, away, or against", "天（。上の（。エナジーが（。、地へと「降（。り（。下（。る（。カタ）』、峻（。烈（。な（。る（。重力（。（。その（。重厚（。な（。る（。る（。着（。地の（。瞬間に、世界は、盤（。石（。と（。なり（。ます。"),
    ("apo", "Apo", "離れて、超越した、アポ", "15th Century", "apo (away from, separate, literal: 'away')", "Away from, off, or separate", "繋（。が（。りを（。断ち、ただ（。一一人「離（。れ（。て（。在（。る（。アポ）』、至高の（。る（。る（。孤独（。（。その（。峻（。烈（。な（。る（。透明（。さが、あなたを、至光（。へと（。変えます。"),
    ("amphi", "Amphi", "両側の、周囲の、アンフィ", "15th Century", "amphi (on both sides, around, literal: 'on both sides')", "On both sides; around", "二つの（。顔を、美し（。く「同時（。に（。持（。つ（。アンフィ）』至高の（。る（。様（。式（。（。その（。危（。う（。い（。均衡の（。末に、物（。語（。は、完結（。し（。ます。"),
    ("proto", "Proto", "最初の、原始の、プロト", "17th Century", "prōtos (first, literal: 'first')", "First, original, or primary", "全（。ての（。始（。ま（。りの「最初（。プロト）』の一（。点（。（。その（。原（。初（。的（。な（。る（。る（。眩（。し（。い（。咆（。哮（。を、魂で、感（。じ（。て（。みて（。ください。"),
    ("archae", "Archae", "古い、始祖の、アーケオ", "17th Century", "arkhaios (ancient, beginning, literal: 'ancient')", "Beginning, original, or ancient", "遥（。かな（。る（。時の（。回（。廊の「最果て（。アーケ）』至高の（。る（。記憶（。（。その（。重（。厚（。な（。る（。沈黙を、誇り（。高く、担（。い（。な（。さい。"),
    ("paleo", "Paleo", "古い、古代の、パレオ", "19th Century", "palaios (ancient, old, literal: 'old')", "Older, ancient, or prehistoric", "忘れ（。去（。られた「太（。古（。の（。る（。記録（。パレオ）』。（。その（。深い（。沈黙（。の中にこそ、宇宙（。の（。真実の（。る（。鼓動が、静（。か（。に、響（。いて（。いる（。のですよ。"),
    ("neo", "Neo", "新しい、ネオ", "14th Century", "neos (new, young)", "New, recent, or a modified version of something", "日常の（。皮を（。脱（。ぎ（。捨て、再び「新（。し（。く（。在（。る（。ネオ）』こと（。（。その（。眩（。し（。い（。る（。始（。ま（。りに、魂は、喝（。采を（。送（。り（。ます。")
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
            word_id = f"{word_text.lower()}_beyond_ii"
            
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
                    "thinking": item[6] if len(item) > 6 else "超越とは、この世界を去ることではありません。この世界の重力に耐えながら、自らの魂だけを、一点の曇りなく、向こう側の光へと繋ぎ止める行為なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "限界を超えることは、自分を壊すことではない。自分という名の器を、宇宙という名の無限へと、解き放つための、聖なる飛躍なのですよ。",
                    "example": f"The philosopher used various {word_text}-linguistic concepts to describe the state of human consciousness beyond physical limitations.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["外側へと向かおうとするのではなく、内側の沈黙を深めてください。その奥行きの果てに、真の超越は宿っているのですよ。"]
                    },
                    "part_of_speech": "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Ultra & Extra II (Cycle 104).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
