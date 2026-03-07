import json
import re

# Theme: The Alchemy of Epoch & Instant (Cycle 56)
words_data = [
    ("duration", "Duration", "持続、期間、デュレーション", "14th Century", "durare (to last, literal: 'hard')", "The time during which something continues", "ただの（。時間（。ではなく（。、困難（。という（。名の（。過酷（。を（。潜（。り（。抜け（。、「硬（。く（。デュラ）耐（。え（。抜（。く（。）」こと（。。（。その（。一瞬（。一瞬（。の（。強（。靭（。な（。る（。持続が（。、世界に（。意味を（。定着（。させる（。の（。ですよ。"),
    ("chronos", "Chronos", "クロノス、時、年代記", "17th Century", "khronos (time)", "The personification of time in Greek mythology", "客観（。的に（。流（。れる（。、「不可逆（。な（。数値（。クロノス）」としての（。時（。。（。それは（。、全（。てを（。等（。しく（。過去へと（。流（。し（。去（。る（。、冷（。徹（。な（。る（。河。"),
    ("kairos", "Kairos", "カイロス、好機、決定的な瞬間", "19th Century", "kairos (right moment)", "A propitious moment for decision or action", "単なる（。数字（。ではなく（。、魂が（。目覚（。め（。る「決定（。的な（。瞬間（。カイロス）」。（。運命の（。矢を（。放つ（。ための（。、たった（。一度きりの（。眩（。し（。い（。臨界（。点。"),
    ("eon", "Eon", "永劫、イーオン、長大な時間", "17th Century", "aion (age, vital force, eternity)", "An indefinite and very long period of time", "人間（。の（。一生（。を（。遥（。かに（。超え（。た（。、「宇宙（。の（。寿命（。アイオーン）」。（。その（。気が（。遠（。く（。なる（。ほどの（。深淵（。の（。前に（。、今（。という（。瞬間の（。重みが（。浮（。き（。彫（。りに（。なり（。ます。"),
    ("nostalgia", "Nostalgia", "郷愁、懐かしさ、ノスタルジー", "18th Century", "nostos (return home) + algos (pain)", "A sentimental longing or wistful affection for the past, typically for a period or place with happy personal associations", "「家へと（。帰（。りたい（。ノスト）」という（。願（。い（。が（。、叶（。わ（。な（。い（。と（。知（。っ（。た（。ときの（。、「切（。な（。い（。痛み（。アルゴス）」。（。過去を（。愛しく（。想（。う（。心は（。、あなたが（。今も（。、心（。の（。故郷を（。持って（。いる（。という（。証（。なのです。"),
    ("reminiscence", "Reminiscence", "追憶、回想、レミニセンス", "16th Century", "re- (again) + mens (mind, literal: 'bring back to mind')", "A story told about a past event remembered by the narrator", "忘（。れ（。去（。られた（。はずの（。記憶を（。、再び（。「心（。メンス）へと（。呼び戻（。す（。リ）」こと（。。（。その（。おぼ（。ろ（。げ（。な（。色彩（。の中に（。、真実（。の（。姿が（。隠（。されて（。いる（。のですよ。"),
    ("antiquity", "Antiquity", "古代、アンティーク、古物", "14th Century", "ante (before) + -ity", "The ancient past, especially the period before the Middle Ages", "今（。より（。も「ずっと（。前（。アンテ）」に（。置（。かれた（。もの（。。（。その（。沈黙（。の（。重厚感（。が（。、現代（。の（。軽（。薄（。さを（。、静（。か（。に（。戒（。め（。て（。いる（。のです。"),
    ("obsolescence", "Obsolescence", "風化、老朽化、時代遅れ", "18th Century", "ob- (away) + solere (to be accustomed)", "The process of becoming obsolete or outdated and no longer used", "かつて（。の（。当たり（。前（。から「遠（。ざ（。か（。っ（。て（。オブ）いく（。）」こと（。。（。忘れ（。去（。られる（。運命（。を（。受け（。入れ（。なが（。ら（。、静（。か（。に（。土へ（。と（。還（。る（。、無（。常（。の（。美（。学。"),
    ("permanence", "Permanence", "永続性、不変、パーマネンス", "15th Century", "per- (through) + manere (to remain)", "The state or quality of lasting or remaining unchanged indefinitely", "時間（。の（。荒波を「最後（。まで（。パー）耐（。え（。抜（。いて（。マン）留（。ま（。る（。）」こと（。。（。移（。ろ（。い（。ゆく（。世界（。の中で（。、たった（。一つ（。の（。不変（。を（。求めて（。、私たちは（。道（。を（。歩む（。のですよ。"),
    ("transient", "Transient", "一時的な、儚い、トランジェント", "16th Century", "trans- (across) + ire (to go)", "Lasting only for a short time; impermanent", "一つの（。場所に（。留（。ま（。ら（。ず（。、ただ「通り（。過（。ぎ（。て（。トランス）行く（。イ）」もの（。。（。その（。消（。え（。去（。る（。間（。際（。の（。美し（。さに（。、魂は（。烈（。しく（。、揺（。さ（。ぶ（。ら（。れる（。のですね。"),
    ("ephemeral", "Ephemeral", "短命な、つかの間の、エフェメラル", "16th Century", "epi- (upon) + hemera (day, literal: 'for a day')", "Lasting for a very short time", "たった「一（。日（。ヘメラ）の（。上（。エピ）に（。だけ（。）」許（。さ（。れた（。命（。。（。その（。余（。り（。にも（。短い（。瞬（。き（。が（。、宇宙（。の（。永劫（。を（。も（。凌（。駕（。する（。輝きを（。放つ（。のです。"),
    ("fleeting", "Fleeting", "流れるような、儚い、フリーティング", "Old English", "flēotan (to float, swim)", "Lasting for a very short time", "掴（。も（。う（。と（。した（。手（。を（。滑（。り（。抜け（。、ただ「流（。れて（。行き（。フリー）」去る（。もの（。。（。その（。感触（。の（。不確か（。さにこそ（。、現在（。という（。名の（。奇跡（。が（。宿（。って（。いる（。のですよ。"),
    ("instantaneous", "Instantaneous", "即座の、瞬時の、インスタンテイニアス", "17th Century", "in- (into, on) + stare (to stand)", "Occurring or done in an instant or instantly", "考え（。る（。暇（。さ（。え（。与（。えず（。、ただ「そこに（。イン）立ち（。現（。れる（。スタ）」こと（。。（。思考（。の（。鎖（。を（。断（。ち（。切り（。、純粋（。な（。直（。感（。へと（。至（。る（。、光速（。の（。飛躍。"),
    ("prompt", "Prompt", "迅速な、刺激する、プロンプト", "15th Century", "pro- (forward) + emere (to take, literal: 'take forward')", "Done without delay", "躊（。躇（。う（。こと（。を（。止め（。、ただ「前へ（。プロ）と（。進み（。出る（。プロ）」こと（。。（。その（。一歩（。の（。速やか（。さが（。、停滞（。の（。闇（。を（。打ち（。破（。り（。、新しい（。地平（。を（。拓（。く（。のだ（。と（。信（。じて（。ください。"),
    ("perpetuate", "Perpetuate", "永続させる、不朽にする", "16th Century", "per- (through) + petere (to seek, aim at, literal: 'seek through')", "Make something, typically an undesirable situation or an unfounded belief, continue indefinitely", "一（。時（。の（。情熱に（。満足（。せ（。ず（。、最後（。まで（。不変の「真理を（。求め（。ペテ）通す（。パー）」こと（。。（。あなた（。の（。意志（。が（。、歴史（。という（。名の（。大河に（。、永遠（。の（。波紋（。を（。刻（。む（。のです。")
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
            word_id = f"{word_text.lower()}_epoch"
            
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
                    "thinking": item[6] if len(item) > 6 else "時間は、魂が自らの成長を噛み締めるために、宇宙が用意した孤独な装置です。",
                    "aftertaste": item[7] if len(item) > 7 else "刹那とは、永遠が耐えきれなくなって、この世界に溢れ出した一滴の雫なのです。",
                    "example": f"The philosopher meditated on the {word_text} of human existence and the fleeting nature of happiness.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["過去とは、失われたものではなく、現在という名の器を形作るための、見えない重力のことです。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["transient", "ephemeral", "fleeting", "instantaneous", "prompt"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Epoch & Instant (Cycle 56).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
