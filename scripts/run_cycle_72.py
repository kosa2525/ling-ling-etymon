import json
import re

# Theme: The Alchemy of Silk & Steel (Cycle 72)
words_data = [
    ("suede", "Suede", "スエード、裏革（うらがわ）", "19th Century", "Suède (Sweden, literal: 'gants de Suède' gloves of Sweden)", "Leather with the flesh side rubbed to make a velvety nap", "北欧（。の（。冷（。徹（。な（。る（。空気（。から（。届（。いた（。、「スウェーデン（。スエード）の（。贈り物』。（。その（。柔らか（。な（。る（。起（。毛が（。、あなた（。の（。肌（。を（。、優（。しく（。、守（。って（。くれる（。のですよ。"),
    ("corduroy", "Corduroy", "コーデュロイ、コール天", "18th Century", "cord + duroy (a coarse fabric)", "A thick cotton fabric with velvety ribs", "ただの（。布（。ではなく（。、一（。つ（。の（。畝（。（。うね（。）」が（。、「紐（。コード）を（。並（。べ（。た（。）」ような（。、強（。靭（。な（。る（。表情。（。その（。素朴（。な（。る（。温（。か（。みが（。、日常（。に（。安（。ら（。ぎを（。、与（。えて（。くれる（。のですよ。"),
    ("tweed", "Tweed", "ツイード、スコットランド織", "19th Century", "tweel (twill, misread for 'Tweed' river)", "A rough, surfaced woolen cloth, typically of mixed flecked colors, originally manufactured in Scotland", "スコットランド（。の（。荒（。れ（。狂（。う（。海（。の（。ように（。、烈（。し（。く（。織（。り（。上げ（。られた（。、「綾（。織（。ツイール）』。（。その（。不（。均（。一（。な（。色彩（。の中に（。、大地（。の（。記憶（。が（。、宿（。って（。いる（。のですよ。"),
    ("flannel", "Flannel", "フランネル、ネル", "16th Century", "gwlan (wool, literal: 'woolen cloth')", "A kind of soft woven fabric, typically made of wool or cotton and slightly milled and raised", "柔らか（。な（。る（。魂の（。衣（。裳（。、「羊毛（。グランク）その（。もの（。）」。（。その（。優（。し（。い（。起毛が（。、凍（。て（。つく（。季節（。から（。、あなた（。の（。心を（。、静（。か（。に（。、温（。めて（。くれる（。のですよ。"),
    ("denim", "Denim", "デニム、丈夫な綿布", "17th Century", "serge de Nîmes (cloth of Nîmes, city in France)", "A sturdy cotton twill fabric, typically blue, used for jeans, overalls, and other clothing", "フランス（。の「ニームという（。町（。デ・ニーム）』で（。産まれた（。、最強（。の（。る（。盾（。。（。その（。色（。褪（。せ（。る（。こと（。の（。ない（。魂は（。、あなたが（。歩（。ん（。だ（。歴史を（。、そのまま（。、美し（。い（。青（。に（。変える（。のですよ。"),
    ("gossamer", "Gossamer", "蜘蛛の糸、繊細なもの、ゴッサマー", "14th Century", "gos (goose) + sumer (summer, literal: 'goose summer')", "A fine, filmy substance consisting of cobwebs spun by small spiders, which is seen especially in autumn", "まるで（。夏（。に（。舞い（。散る「鳥（。ゴス）の（。羽（。サマー）』のように（。、目（。に（。は（。見（。え（。な（。い（。ほど（。の（。静寂（。。（。その（。壊（。れ（。や（。す（。い（。美し（。さが（。、宇宙の（。深（。淵を（。、そっと（。照（。ら（。し（。て（。いる（。のですよ。"),
    ("matte", "Matte", "つや消しの、マットな", "17th Century", "mat (dull, dead, literal: 'checked, checkmate')", "Of a color, paint, or surface) dull and flat, without a shine", "光を（。拒（。み（。、ただ（。存在（。の（。重（。厚（。さを（。主張（。する「沈（。黙（。の（。マット）』。（。一度（。、眩（。し（。い（。虚飾（。を（。捨て（。去り（。、ただ（。静（。か（。な（。る（。本質（。へと（。還（。る（。ための（。、至高（。の（。質感（。です。"),
    ("porcelain", "Porcelain", "磁器、ポーセリン", "16th Century", "porcellana (cowrie shell, literal: 'little pig')", "A white vitrified translucent ceramic; china", "まるで「宝（。貝（。ポルチェラーナ）』のように（。、透（。き（。通（。り（。輝（。く（。地肌（。。（。土が（。、炎（。という（。名の（。試（。練（。を（。越（。えて（。、宝石（。へと（。、再び（。産まれ（。変わ（。っ（。た（。姿（。なの（。ですよ。"),
    ("obsidian", "Obsidian", "黒耀石（こくようせき）、オブシディアン", "17th Century", "Obsidius (Roman who discovered it)", "A hard, dark, glasslike volcanic rock formed by the rapid solidification of lava without crystallization", "火山（。の（。烈（。し（。い（。エナジーが（。、一瞬（。にして（。静止（。し（。た「暗（。黒（。の（。宝石（。オプシディウス）』。（。その（。鋭（。利な（。る（。光が（。、あなた（。の（。内なる（。闇（。を（。、峻（。烈（。に（。、照（。らし（。出す（。のですよ。"),
    ("quartz", "Quartz", "石英、水晶、クォーツ", "18th Century", "quarz (German, of uncertain origin)", "A hard white or colorless mineral consisting of silicon dioxide, found widely in igneous, sedimentary, and metamorphic rocks and often occurring as hexagonal transparent crystals", "透明な（。幾（。何（。学の（。中で（。、ただ（。ひたすら「静（。か（。に（。眠（。る（。クォーツ）』大（。地（。の（。欠（。片（。。（。その（。一点（。の（。濁（。り（。も（。な（。い（。輝（。きは（。、宇宙の（。全（。純粋（。な（。る（。記憶（。を、物語っ（。て（。いる（。のですよ。"),
    ("emerald", "Emerald", "エメラルド、翠玉", "14th Century", "smaragdos (green gem)", "A bright green precious stone consisting of a chromium-rich variety of beryl", "深い（。森（。の（。奥底（。を（。、一粒（。の（。石に（。閉じ（。込め（。た「緑（。の（。瞳（。スマラグドス）』。（。見（。つ（。める（。たびに（。、あなた（。の（。魂は（。、生命（。の（。源（。へと（。、再び（。還（。る（。のですよ。"),
    ("sapphire", "Sapphire", "サファイア、青玉", "13th Century", "sappheiros (precious stone, blue, literal: 'beloved of Saturn')", "A transparent precious stone, typically blue, which is a variety of corundum (aluminum oxide)", "夜空（。の（。深淵（。を（。、結晶（。さ（。せた「青（。い（。誓（。い（。サフィール）』。（。その（。冷（。徹（。な（。る（。眩（。し（。さが（。、あなた（。に（。、ゆる（。ぎ（。な（。い（。意志（。と（。、静（。か（。な（。る（。調和（。を（。、与（。えて（。くれる（。の（。ですよ。"),
    ("ruby", "Ruby", "ルビー、紅玉", "14th Century", "rubeus (red)", "A precious stone consisting of corundum in color varieties varying from deep crimson or purple to pale rose", "大地（。の（。血汐（。が（。、一（。点（。に（。凝縮（。し（。て（。産まれた「赤（。い（。ルベ）閃光。（。その（。烈（。し（。い（。情熱が（。、凍（。て（。つ（。い（。た（。日常に、眩（。しい（。ほどの（。、希望（。の（。火を（。灯（。す（。のです。"),
    ("bronze", "Bronze", "青銅、ブロンズ", "17th Century", "Brundisium (Brindisi, city in Italy)", "A yellowish-brown alloy of copper with up to one-third tin", "かつて（。の「都市（。ブルンディシウム）』で（。磨（。き（。抜（。かれた（。、黄金（。色（。の（。均衡。（。時（。を（。経（。る（。たび（。に（。、緑青（。という（。名の（。、気高い（。る（。沈黙（。を（。纏（。っ（。て（。いく（。のですよ。"),
    ("alloy", "Alloy", "合金、混ぜ合わせる、アロイ", "14th Century", "ligare (to bind, literal: 'ad-ligare' bind together)", "A metal made by combining two or more metallic elements, especially to give greater strength or resistance to corrosion", "異（。な（。る（。エナジーを、力強（。く「結び（。合わせた（。リガ）」、第（。三（。の（。真理。（。混（。ざ（。り（。合う（。ことで（。、単体（。では（。到底（。辿（。り（。着（。け（。な（。い（。、最強（。の（。る（。均衡を（。、手（。に（。入れる（。の（。ですよ。")
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
            word_id = f"{word_text.lower()}_silk"
            
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
                    "thinking": item[6] if len(item) > 6 else "質感とは、物体が沈黙という名の服を脱ぎ捨てて、直接私たちの魂に触れてくる、眩しい囁きなのです。",
                    "aftertaste": item[7] if len(item) > 7 else "宝石は、宇宙が孤独に耐えきれなくなって、自らの名前を呼ぶために点した、永遠の灯火なのですよ。",
                    "example": f"The artisan chose the finest {word_text} to complete the luxurious and durable upholstery project.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["触れるという行為は、世界を一方的に認識することではなく、自らの肌を通して、世界と愛を交わすことなのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["matte", "metallic", "glossy", "translucent", "opaque"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Silk & Steel (Cycle 72).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
