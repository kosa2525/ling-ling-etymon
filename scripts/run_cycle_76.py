import json
import re

# Theme: The Alchemy of Zenith & Nadir (Cycle 76)
words_data = [
    ("zenith", "Zenith", "天頂、頂点、ゼニス", "14th Century", "samt (path, literal: 'path over head')", "The time at which something is most powerful or successful", "自分自身を（。越元（。た（。、至高の「道（。ザンプ）』の（。最頂点（。（。そこ（。には（。、地上の（。喧（。騒が（。届（。か（。な（。い（。、峻（。烈（。な（。る（。沈黙（。と（。、眩（。しい（。ほどの（。光が（。、静（。か（。に（。、横（。たわ（。って（。いる（。のですよ。"),
    ("nadir", "Nadir", "どん底、天底、ネイディア", "15th Century", "nazir (opposite, literal: 'opposite the zenith')", "The lowest point in the fortunes of a person or organization", "天頂（。とは「反対（。ナズィール）にある（。）」、絶対（。的（。な（。る（。深（。淵（。（。けれど（。、その（。どん底を（。知（。っ（。た（。者（。だけが（。、真（。実（。の（。高（。み（。へと（。、再び（。、飛（。翔（。する（。ことができる（。のですよ。"),
    ("altitude", "Altitude", "標高、高度、アルチュード", "14th Century", "altus (high)", "The height of an object or point in relation to sea level or ground level", "大地から（。どこ（。まで（。も「高（。く（。アルト）」至（。る（。こと（。。（。空気（。が（。薄（。く（。な（。る（。た（。びに（。、あなた（。の（。魂は（。、日常（。の（。濁（。り（。を（。脱（。し（。、至高（。の（。透明（。さを（。、手（。に（。入れ（。る（。のですよ。"),
    ("chasm", "Chasm", "割れ目、隔たり、キャズム", "16th Century", "khaskhein (to gape)", "A deep fissure in the earth, rock, or another surface", "静（。かな（。る（。大地に（。突如（。として「口を（。開（。け（。た（。キャズム）』。（。その（。暗（。黒（。の（。断絶が（。、二（。つの（。世界（。を（。、峻（。烈（。に（。、引き（。裂（。き（。続け（。る（。のですよ。"),
    ("rift", "Rift", "裂け目、不和、リフト", "14th Century", "rifta (rift, splitting)", "A crack, split, or break in something", "一（。つ（。だ（。っ（。た（。ものが「引き（。裂（。か（。れ（。た（。リフト）』痕跡（。（。その（。小（。さな（。亀（。裂（。から、未知の（。エナジーが（。、静（。かに（。、漏（。れ（。出し（。始め（。て（。いる（。の（。かも（。しれ（。ません。"),
    ("hollow", "Hollow", "空洞、くぼみ、ホロウ", "Old English", "holh (hollow)", "Having a hole or empty space inside", "中（。身を（。捨て（。去り（。、ただ「う（。つ（。ろ（。な（。ホール）』にな（。っ（。た（。姿（。（。けれど（。、その（。空虚（。がある（。から（。こそ（。、新しい（。宇宙を（。、受け（。入れる（。ことが（。でき（。る（。のですよ。"),
    ("cavern", "Cavern", "洞窟、大洞穴（。だいどうけつ（。）」、キャバーン", "14th Century", "cavus (hollow, literal: 'hollow place')", "A cave, or a chamber in a cave, typically a large one", "大地（。の（。胎（。内（。に（。隠された（。「深（。い（。空洞（。キャヴァス）』。（。そこ（。には（。、目（。に（。見（。え（。な（。い（。歴史（。の（。響きが（。、静（。か（。に（。、反乱（。し（。て（。いる（。のですよ。"),
    ("alcove", "Alcove", "凹（。おう（。）」室、アルコーブ", "17th Century", "al-qubba (the vault, dome, literal: 'the arch')", "A recess, typically in the wall of a room or of a garden", "壁に（。そ（。っ（。と（。作（。られた「小（。さな（。る（。円（。蓋（。クッバ）』のある（。場所（。（。そこ（。は、全（。ての（。喧（。騒から（。、あなた（。を（。優（。しく（。隔（。て（。て（。くれる（。、聖なる（。小（。宇宙なの（。ですよ。"),
    ("recess", "Recess", "休憩、奥まった所、リセス", "16th Century", "re- (back) + cedere (to go, literal: 'going back')", "A small hollow space in a wall", "全（。ての（。活動（。を（。止め（。、ただ「後ろへへと（。リ）下（。がる（。セス）」こと（。。（。その（。静（。か（。な（。る（。停（。滞（。の中にこそ（。、真実（。の（。休息が（。、宿（。る（。の（。でしょう。"),
    ("niche", "Niche", "適所、壁龕（。へきがん（。）」、ニッチ", "17th Century", "nidus (nest)", "A specialized segment of the market for a particular kind of product or service", "あなたに（。だけ（。に（。許（。さ（。れた「居（。場所（。ニッチ）』、命の（。巣（。箱（。（。そこ（。には（。、誰（。にも（。侵（。さ（。れ（。な（。い（。、自（。分（。だけ（。の（。真（。実が（。、静（。か（。に（。、満（。ち（。て（。いる（。の（。ですよ。"),
    ("margin", "Margin", "余白、縁、マージン", "14th Century", "margo (border, edge)", "The edge or border of something", "意味（。の（。中心（。ではなく（。、静（。か（。なる「境界（。マルゴ）』に（。留（。まる（。こと（。。（。その（。余（。白（。にある（。豊（。か（。な（。る（。沈（。黙（。が（。、物（。語（。を（。、より（。深（。く（。、して（。くれる（。のですよ。"),
    ("frontier", "Frontier", "辺境、最前線、フロンティア", "14th Century", "frons (forehead, front)", "A line or border separating two countries", "知（。ら（。れ（。ざ（。る（。未知なる「前面（。フロント）』。（。そこ（。を（。越え（。る（。た（。び（。に（。、あなた（。は（。、全（。く（。新（。し（。い（。宇宙の（。一部（。に、な（。る（。の（。ですよ。"),
    ("realm", "Realm", "領域、王国、レルム", "13th Century", "regimen (government, system, literal: 'rule')", "A kingdom", "ただ一（。つ（。の（。秩序（。に「支配（。レギ）さ（。れた（。）」、峻（。烈（。な（。る（。空間。（。あなた（。は（。、今（。、何（。色（。の（。法則（。に（。、身（。を（。委（。ね（。て（。いる（。の（。でしょうか。"),
    ("volume", "Volume", "音量、容積、巻、ボリューム", "14th Century", "volu- (roll, literal: 'scroll, roll')", "The amount of space that a substance or object occupies, or that is enclosed within a container", "かつて（。は（。一（。巻の「巻（。物（。ヴォル）』だ（。っ（。た（。もの（。たちの（。、重（。厚（。な（。る（。存在（。感（。（。その（。豊（。か（。な（。る（。厚（。みの（。中に（。、宇宙の（。歴史が（。、幾（。重（。にも（。、織（。り（。込ま（。れて（。いる（。のですよ。"),
    ("bulk", "Bulk", "大部分、かさ、バルク", "14th Century", "bulke (heap, cargo ship's hold)", "The mass or magnitude of something large", "一（。つ（。の（。点（。に（。は（。収まり（。き（。ら（。ぬ（。、「巨大（。な（。る（。積み（。荷（。バルク）』。（。その（。圧倒（。的（。な（。物質（。性（。に（。、魂は（。、時（。に、畏（。敬（。の（。念を（。、抱（。か（。ざ（。る（。を（。得（。ない（。のですよ。")
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
            word_id = f"{word_text.lower()}_space"
            
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
                    "thinking": item[6] if len(item) > 6 else "空間は、魂が自由に羽ばたくために用意された、広大なキャンバスなのです。",
                    "aftertaste": item[7] if len(item) > 7 else "頂点に立つということは、同時に広大な虚空を見つめる勇気を持つということなのですよ。",
                    "example": f"The rocket reached its {word_text} and began its descent back to Earth, providing stunning views of the cosmos.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["外側の境界を押し広げることよりも、内側の奥行きを深めることの方が、真の旅に近いのかもしれません。"]
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

        print(f"Success: Added {added_count} words. Theme: Zenith & Nadir (Cycle 76).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
