import json
import re

# Theme: The Alchemy of Home & Threshold (Cycle 50)
words_data = [
    ("domestic", "Domestic", "家庭の、国内の、ドメスティック", "15th Century", "domus (house)", "Relating to the running of a home or to family relations", "広い（。世界から（。自ら（。を（。切り（。離（。し（。、「家（。ドムス）の中」へと（。エナジーを（。収（。める（。こと（。。（。そこ（。には（。、誰（。にも（。汚（。さ（。れ（。な（。い（。、密（。かな（。る（。安（。ら（。ぎが（。あります。"),
    ("habitat", "Habitat", "生息地、住処、ハビタット", "18th Century", "habitare (to dwell, live in)", "The natural home or environment of an animal, plant, or other organism", "ただ（。そこに（。居（。る（。だけでなく（。、魂が「住（。ま（。わ（。れ（。る（。ハビ）」場所（。。（。大地と（。響き（。合い（。、命が（。最も（。自分（。らしく（。輝（。ける（。、聖（。なる（。領域。"),
    ("mansion", "Mansion", "大邸宅、館、マンション", "14th Century", "manere (to dwell, remain)", "A large, impressive house", "一時（。の（。宿（。ではなく（。、永遠に「留（。ま（。る（。マン）場所（。）」。（。重厚（。な（。石（。の（。壁が（。、家族（。の（。記憶を（。、何（。世（。代（。にも（。わたって（。、守（。り（。続けて（。いる（。のですよ。"),
    ("cottage", "Cottage", "コテージ、小規模な家", "14th Century", "cote (hut, shelter)", "A small simple house, typically one near the lake or beach", "豪華さ（。を（。捨て（。去（。り（。、ただの「小屋（。コート）」として（。大地と（。戯（。れる（。場所（。。（。質素（。な（。暮らしの（。中（。に（。、真（。の（。豊（。かさを（。見出（。した（。、知性の（。隠（。れ（。家。"),
    ("shelter", "Shelter", "避難所、シェルター、庇護", "16th Century", "shield + troop, shell", "A place giving temporary protection from bad weather or danger", "荒（。れ（。狂（。う（。嵐（。という（。名の（。過酷（。な（。現実から（。、命を「盾（。シールド）で（。守（。る（。）」場所（。。（。そこ（。は（。、傷（。ついた（。魂が（。、再び（。立ち（。上がる（。ための（。聖域。"),
    ("corridor", "Corridor", "回廊、廊下、コリドー", "16th Century", "currere (to run)", "A long passage in a building from which doors lead into rooms", "一つ（。の（。場所にとど（。ま（。ら（。ず（。、風（。の（。ように「駆（。け（。抜（。け（。る（。コリ）」ための（。空間（。。（。部屋（。と（。部屋、現実（。と（。夢を（。繋（。ぐ（。、透明な（。境界。"),
    ("hearth", "Hearth", "暖炉、家庭", "Old English", "heorth (burning place)", "The floor of a fireplace", "家（。の（。中心（。で（。、赤（。々と（。燃（。え（。る「火（。の（。場所（。ハース）」。（。そこ（。には（。、家族（。の（。語（。り（。合い（。と（。、生命（。の（。温（。か（。みが（。、常に（。満ち（。て（。いる（。のですよ。"),
    ("attic", "Attic", "屋根裏部屋、アティック", "17th Century", "Attikos (Athenian architecture style)", "A space or room inside or partly inside the roof of a building", "日常（。の（。目線（。を超え（。、天に（。最も（。近い「アテネ（。アッ（。ティ（。カ）」の（。高（。み（。。（。そこ（。には（。、忘れ（。去（。られた（。過去の（。記憶が（。、静（。か（。な（。る（。埃（。と共に（。眠（。って（。いる（。のです。"),
    ("cellar", "Cellar", "地下室、貯蔵庫、セラー", "13th Century", "cellarium (storehouse, cellar)", "A room below ground level in a house, typically used for storing wine or coal", "大地（。の（。暗闇（。の（。中に（。、密（。か（。に（。用意（。さ（。れた「小さな（。部屋（。セル）」。（。そこ（。では（。、時間（。が（。静（。か（。に（。止（。まり（。、琥珀（。色の（。夢（。が（。、ゆっくり（。と（。熟（。成（。し（。て（。いく（。のです。"),
    ("facade", "Facade", "（建物の）正面、外見", "17th Century", "faccia (face)", "The principal front that looks onto a street or open space", "真（。実（。の（。奥行（。き（。を（。隠（。し（。、ただ（。世界に「顔（。ファサ）を（。向（。ける（。）」こと（。。（。その（。眩（。しい（。仮面（。の（。裏側（。に（。、あなた（。の（。本（。当（。の（。物語が（。息（。づいて（。いる（。の（。ですね。"),
    ("ornament", "Ornament", "装飾品、美化するもの", "14th Century", "ornare (to equip, adorn)", "A thing used or serving to make something look more attractive but usually having no practical purpose, especially a small object kept for its artistic value", "ただ（。そこ（。に（。ある（。だけで（。、生命（。を「輝（。か（。せ（。オーナ）整（。える（。）」もの（。。（。無駄（。の中にこそ（。、魂の（。豊（。かさが（。浮（。き（。彫（。りに（。なる（。のですよ。"),
    ("chalice", "Chalice", "聖杯、酒杯", "13th Century", "calix (cup)", "A large cup or goblet, typically used for drinking wine", "一杯の（。酒を（。、聖なる（。エナジーへと（。変（。える「器（。カリクス）」。（。その（。黄金色（。の（。輝きに（。、魂を（。潤（。す（。ための（。祈り（。を（。捧（。げて（。ください。"),
    ("cuisine", "Cuisine", "料理、台所", "18th Century", "coquina (kitchen, cooking)", "A style or method of cooking, especially as characteristic of a particular country, region, or establishment", "ただ（。食べる（。のではなく（。、素材（。という（。名の（。言葉を「調理（。クイジ）する（。）」芸術（。。（。味（。覚の（。中に（。、歴史（。と（。土（。の（。記憶を（。織（。り（。込（。む（。こと（。です。"),
    ("banquet", "Banquet", "宴（。うたげ（。）」、晩餐", "15th Century", "banco (bench, table)", "An elaborate and formal evening meal for many people, often followed by speeches", "大勢で「テーブル（。バンク）を（。囲（。む（。）」、生命（。の（。再（。確認（。。（。孤独（。な（。エナジーが（。、笑（。い声と（。響き（。合（。い（。、一つの（。巨大（。な（。調和（。へと（。至る（。瞬間。"),
    ("vintage", "Vintage", "ヴィンテージ、時代物、収穫期", "15th Century", "vinum (wine) + demere (to take off)", "The year or place in which wine, especially wine of high quality, was produced", "「葡萄の（。収穫（。ヴィン）を（。取り（。出す（。デ（。）」季節（。。（。過ぎ去（。った（。時間（。が（。、熟（。成（。という（。名の（。魔法を（。かけて（。、現在に（。至宝（。を（。届（。けて（。くれ（。た（。のですよ。"),
    ("perfume", "Perfume", "香水、芳香", "16th Century", "per- (through) + fumare (to smoke)", "A fragrant liquid typically made from essential oils extracted from flowers and spices, used to give a pleasant smell to one's body", "目（。には（。見え（。ない（。けれど（。、「煙を（。通して（。パーフム）」、記憶（。を（。揺（。さ（。ぶ（。る（。見えない（。エッセンス（。。（。あの日（。の（。景色（。が（。、一瞬（。にして（。鼻（。先へと（。蘇（。り（。ます。"),
    ("incense", "Incense", "香、インセンス、激怒させる", "13th Century", "incendere (to set fire to, burn)", "A gum, spice, or other substance that is burned for the smell it produces", "祈り（。の（。ために「火を（。付け（。られた（。インセ）香（。）」。（。その（。静（。かな（。る（。煙（。が（。、天上（。の（。高（。みへと（。、あなた（。の声（。を（。運ん（。で（。行く（。のですよ。"),
    ("attire", "Attire", "服装、装い", "13th Century", "a- (to) + tire (order, row, rank)", "Clothes, especially fine or formal ones", "裸（。の（。魂に（。対して（。、「正（。しい（。順序（。ティア）へと（。導く（。アド）」ための（。装い（。。（。あなた（。が（。何を（。纏（。うか（。、それ（。が（。、今日（。の、あなた（。の（。役割（。を（。決（。める（。のです。"),
    ("leisure", "Leisure", "余暇、ゆとり", "14th Century", "licere (to be permitted)", "Use of free time for enjoyment", "義務（。から（。解放（。され（。、ただ「許（。される（。リセール）」こと（。。（。何（。も（。し（。ない（。贅沢（。の中にこそ（。、魂（。の（。真（。の（。言葉（。が（。、静（。か（。に（。育（。ま（。れる（。のですよ。"),
    ("atrium", "Atrium", "アトリウム、吹き抜け", "16th Century", "ater (black, sooty, literal: 'smoke-filled hearth room')", "An open-roofed entrance hall or central court in an ancient Roman house", "かつて（。は（。火（。の「煙で（。黒（。ず（。んだ（。アター）」場所（。だった（。、光（。溢（。れる（。玄関（。。（。そこ（。から（。、新しい（。エナジーが（。、家（。の（。中（。へと（。舞（。い（。込（。んで（。くる（。のです。")
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
            word_id = f"{word_text.lower()}_home"
            
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
                    "concept": item[5] + f" ({item[6]})",
                    "thinking": item[6],
                    "aftertaste": item[7] if len(item) > 7 else "家は、魂が世界という名の旅から帰り、再び自らを見出すための聖域です。",
                    "example": f"The family gathered around the {word_text} to share stories on a cold winter night.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["境界とは、世界を分断するものではなく、二つの異なる美しさを繋ぎ止めるための接点なのです。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["domestic", "vintage"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Home & Threshold (Cycle 50).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
