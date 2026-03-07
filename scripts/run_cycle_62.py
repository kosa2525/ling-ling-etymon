import json
import re

# Theme: The Alchemy of Brush & Canvas (Cycle 62)
words_data = [
    ("pigment", "Pigment", "顔料（がんりょう）、ピグメント", "14th Century", "pingere (to paint)", "The natural coloring matter of animal or plant tissue", "ただの（。泥（。や（。石（。を（。、「描（。く（。ピン）こと（。）」を（。通して（。、魂の（。色彩（。へと（。変えた（。もの（。。（。その（。一粒（。一粒（。が（。、あなた（。の（。内なる（。宇宙を（。、現実に（。留め（。て（。くれる（。のですよ。"),
    ("palette", "Palette", "調色板、パレット、色彩感覚", "17th Century", "pala (spade, shovel, literal: 'little blade')", "A thin board or slab on which an artist lays and mixes colors", "色（。と（。色が「出会（。い（。パラ）混ざり（。合う（。）」、小（。さな（。る（。舞台（。。（。そこ（。に、あなた（。は（。、自分（。だけの（。新（。しい（。世界（。の（。設計図を（。、描き（。出して（。いく（。のですよ。"),
    ("easel", "Easel", "画架、イーゼル", "17th Century", "ezel (donkey)", "A wooden frame for holding an artist's work while it is being painted or drawn", "重（。い（。キャンバスを、文句（。一（。つ（。言（。わず（。に「背負（。い（。続ける（。エーゼル）』、従順（。な（。る（。従者（。。（。制作（。という（。名の（。過酷（。な（。旅路を（。、静（。か（。に（。支えて（。くれる（。存在（。です。"),
    ("canvas", "Canvas", "帆布、キャンバス、油絵", "14th Century", "cannabis (hemp)", "A strong, coarse unbleached cloth made from hemp, flax, or a similar yarn, used to make items such as sails and tents and as a surface for oil painting", "「麻（。カンナ）で（。織（。られた（。）」、質素（。な（。る（。布（。。（。けれど（。、その（。ざら（。つ（。いた（。表面（。に（。、魂が（。一（。筆（。置（。いた（。とき（。、そこ（。は（。、宇宙（。の（。全（。てを（。受け（。止める（。聖域と（。なり（。ます。"),
    ("fresco", "Fresco", "フレスコ画、壁画", "16th Century", "fresco (fresh)", "A painting done rapidly in watercolor on wet plaster on a wall or ceiling, so that the colors penetrate the plaster and become fixed as it dries", "壁（。が（。まだ「新（。し（。く（。フレスコ）濡（。れて（。いる（。）」間（。に、一気に（。描き（。上げる（。こと（。。（。後（。戻（。り（。の（。でき（。ない（。その（。一瞬（。の（。決断（。が（。、歴史（。と（。一体化（。し（。て（。いく（。のですよ。"),
    ("mosaic", "Mosaic", "モザイク画、寄せ集め", "14th Century", "Mousa (Muse, museum, literal: 'belonging to Muses')", "A picture or pattern produced by arranging together small colored pieces of hard material, such as stone, tile, or glass", "バラバラ（。な（。石の（。欠片（。を（。、「美（。の（。神（。ムーサ）に（。捧（。げる（。）」ように（。、一（。つ（。ずつ（。並（。べる（。こと（。。（。その（。不（。均（。一（。な（。集（。積（。が（。、遠目（。には（。、壮大（。な（。物語を（。創（。り出（。す（。のですよ。"),
    ("glaze", "Glaze", "光沢（。を（。出す（。）、上薬（。、グレイズ", "14th Century", "glas (glass)", "A vitreous substance fused on to the surface of pottery to form a hard, impervious decorative coating", "表面（。に「ガラス（。グラ）の（。ような（。）」透明感（。を（。纏（。わ（。せる（。こと（。。（。その（。眩（。し（。い（。ヴェール（。を（。通して（。、下にある（。色彩（。は（。、より（。深（。く、宝石（。の（。ように（。、震（。え（。始め（。ます。"),
    ("tint", "Tint", "淡（。い（。色合（。い（。）、色合（。い（。、ティント", "18th Century", "tinctus (dipped, dyed, literal: 'tingere' to dye)", "A slight or pale coloration; a shade or variety of a color", "色彩（。の（。海に「そっと（。浸（。し（。た（。ティン）」だけの（。、消（。え（。入る（。ような（。色合（。い（。。（。その（。危（。うい（。薄（。さの中にこそ（。、言（。葉（。に（。なら（。ない（。情緒が（。宿（。って（。いる（。のですよ。"),
    ("hue", "Hue", "色合い、色彩、ヒュー", "Old English", "hīw (form, color, appearance)", "A color or shade", "単（。なる（。波長（。ではなく（。、生命（。が（。まと（。う「かたち（。ヒュー）その（。もの（。）」。（。あなた（。が（。今日（。、何（。色の（。影（。を（。引（。く（。のか、それ（。が（。あなた（。の（。存在（。の（。理由（。なの（。ですよ。"),
    ("saturation", "Saturation", "彩度、飽和、サチュレーション", "16th Century", "satur (full, sated)", "The intensity of a color, expressed as the degree to which it differs from white", "これ（。以上（。入（。ら（。ない（。ほど（。、「満（。た（。さ（。れ（。た（。サチュ）」状態（。。（。その（。烈（。しい（。色彩の（。咆（。哮（。に（。、魂（。が（。、一瞬（。にして（。捕ら（。え（。られて（。しまう（。のですよ。"),
    ("contrast", "Contrast", "対比、コントラスト", "17th Century", "contra- (against) + stare (to stand)", "The state of being strikingly different from something else in juxtaposition or close association", "光（。と（。影（。が「向か（。い（。合って（。コントラ）立つ（。スタ）」こと（。。（。対立する（。二（。つの（。極性（。が（。、互（。いを（。輝（。か（。せ（。、意味（。を（。産（。み出す（。のですよ。"),
    ("virtuoso", "Virtuoso", "（。演奏（。などの（。）」大家（。、巨匠（。、バーチュオーゾ", "17th Century", "virtus (virtue, skill, manliness)", "A person highly skilled in music or another artistic pursuit", "技（。術（。を（。究（。め（。、「高貴（。な（。る（。徳（。バー）を（。備（。えた（。）」者（。。（。その（。一瞬の（。筆（。さば（。きに（。、何（。十年（。という（。時間の（。結晶（。が（。、美し（。く（。、昇（。華（。し（。て（。いる（。のです。"),
    ("masterpiece", "Masterpiece", "傑作、マスターピース", "17th Century", "master + piece (literal: 'the piece that makes one a master')", "A work of outstanding artistry, skill, or workmanship", "ギルド（。の（。中で「親（。方（。マスター）として（。認（。め（。られる（。ための（。）」至高の一（。品（。ピース）』。（。それは（。、たった一人（。の（。人間が（。、神（。の領域（。に（。触（。れた（。瞬間の（。、眩（。しい（。記録。"),
    ("curator", "Curator", "学芸員、キュレーター、管理者", "14th Century", "curare (to take care of)", "A keeper or custodian of a museum or other collection", "自ら（。を（。表現（。する（。のではなく（。、ただ美を「愛（。しみ（。守り（。抜く（。キュラ）」者（。。（。あなた（。の（。その（。誠実（。な（。る（。眼差し（。が（。、時代（。の（。荒波から、至宝（。を（。守（。って（。いる（。のですよ。"),
    ("aesthetic", "Aesthetic", "美学、美的感覚、エステティック", "18th Century", "aisthanesthai (to perceive, feel)", "Concerned with beauty or the appreciation of beauty", "ただ（。の（。知識（。を（。超え（。、魂で「感（。じ（。る（。エステ）」こと（。。（。美（。し（。さ（。とは（。、宇宙（。の（。囁（。きを（。、あなた（。が（。どう（。受け（。止める（。か（。という（。、至高（。の（。対話（。なのです。")
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
            word_id = f"{word_text.lower()}_art"
            
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
                    "thinking": item[6] if len(item) > 6 else "芸術は、言葉が沈黙したときに初めて聞こえてくる、魂の囁きです。",
                    "aftertaste": item[7] if len(item) > 7 else "筆の一振りは、一瞬の情熱を、永遠という名の時間に刻み込むための、静かなる闘いです。",
                    "example": f"The artist carefully selected each {word_text} to create a harmonious and moving composition.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["描くとは、世界をそのまま写し取ることではなく、自らの内なる宇宙を、キャンバスという大地に投影することなのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["aesthetic", "still-life", "caricature"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Brush & Canvas (Cycle 62).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
