import json
import re

# Theme: The Alchemy of Dream & Reality (Cycle 46)
words_data = [
    ("mirage", "Mirage", "蜃気楼、逃げ水、ミラージュ", "15th Century", "mirer (to look at, admire, literally: 'to wonder at')", "An optical illusion caused by atmospheric conditions, especially the appearance of a sheet of water in a desert or on a hot road caused by the refraction of light from the sky by heated air", "砂漠の（。熱気の中に（。、あり（。得ない（。オアシスを「驚（。き（。を（。持って（。眺（。める（。ミラ）」こと（。。（。届（。き（。そうで（。届（。かない（。、現実（。の（。境界（。を（。揺（。さ（。ぶ（。る（。、光（。の（。いた（。ずら。"),
    ("illusion", "Illusion", "錯覚、幻想、幻", "14th Century", "in- (into, at) + ludere (to play)", "A thing that is or is likely to be wrongly perceived or interpreted by the senses", "真実を（。その（。まま（。見る（。のを（。止め（。、心が（。自らと「戯（。れ（。ロード）遊（。ぶ（。）」こと（。。（。その（。眩（。し（。い（。嘘（。は（。、時に（。真実（。その（。もの（。よりも（。美（。しく（。魂を（。救（。う（。ことが（。ある（。のですよ。"),
    ("reverie", "Reverie", "空想、夢想、レヴァリエ", "14th Century", "rever (to dream, speak wildly)", "A state of being pleasantly lost in one's thoughts; a daydream", "昼（。間の（。光を（。遮（。り（。、ただ「夢の（。中を（。彷徨（。う（。レヴ）」こと（。。（。日常の（。義務（。から（。一瞬（。だけ（。羽（。を（。伸ばし（。、無限（。の（。内なる（。宇宙（。へと（。漕（。ぎ（。出す（。、静（。かな（。る（。自己（。逃避。"),
    ("slumber", "Slumber", "眠り、微睡み（まどろみ）", "Old English", "slūma (slumber, sleep)", "Sleep", "意識の（。重い（。鎖（。を（。ほど（。き（。、ただ「静（。か（。に（。沈（。む（。スルー）」こと（。。（。そこ（。は（。、あらゆる（。苦しみ（。や（。色彩（。が（。溶（。け（。去（。り（。、次（。なる（。目覚（。めへの（。エナジーを（。育（。む（。、母（。なる（。闇（。の中。"),
    ("insomnia", "Insomnia", "不眠症、インソムニア", "17th Century", "in- (not) + somnus (sleep)", "Habitual sleeplessness; inability to sleep", "夜が（。連（。れて（。くる（。安（。ら（。ぎの「眠（。り（。ソムヌス）を（。持（。た（。ない（。イン）」という（。不条理（。。（。暗闇（。の（。中に（。瞳を（。開き（。続け（。、答え（。の（。出ない（。問いを（。繰（。り（。返（。す（。、孤独（。な（。思索（。の（。砂漠。"),
    ("vigil", "Vigil", "徹夜の祈り、用心、ヴィジル", "13th Century", "vigil (awake, watchful)", "A period of keeping awake during the time usually spent asleep, especially to keep watch or pray", "全（。世界が（。眠り（。に（。就（。いた（。後（。も（。、ただ一人「目（。を（。覚（。まし（。ヴィジル）守（。り（。続ける（。）」こと（。。（。その（。不眠の（。祈り（。が（。、明日（。の（。朝を（。この（。世界に（。繋（。ぎ（。止（。めて（。いる（。のですよ。"),
    ("awakening", "Awakening", "目覚め、覚醒", "Old English", "awacnan (to arise, originate)", "An act of waking from sleep", "夢の（。ヴェール（。を（。突（。き（。破（。り（。、再び（。「立ち（。上がる（。ワック）」こと（。。（。昨日（。までの（。自分（。を（。脱（。ぎ（。捨て（。、全（。く（。新（。しい（。光の（。中で（。、自ら（。の（。名前を（。、再び（。、思い出す（。のですよ。"),
    ("portent", "Portent", "前兆、驚異", "16th Century", "pro- (before, forward) + tendere (to stretch)", "A sign or warning that something, especially something momentous or calamitous, is likely to happen", "未来（。という（。暗闇（。から（。、何者（。かが（。自（。らの（。意志を「前へと（。プロ）引き（。延（。ばし（。テント）」て（。くる（。影（。。（。それは（。、運命の（。風（。が（。吹（。き（。始（。める（。、最初（。の（。震（。えなのです。"),
    ("seer", "Seer", "預言者、先見の明のある人、シーア", "14th Century", "see + -er", "A person who is supposed to be able, through supernatural insight, to see what the future holds for people", "単に（。眺める（。のではなく（。、目（。には（。見えない（。真実（。の（。かたちを「見（。抜（。く（。シー）者（。）」。（。あなたの（。中（。の（。澄（。み（。渡（。った（。瞳を（。、最後（。まで（。信じ（。て（。あげて（。ください。"),
    ("ghost", "Ghost", "幽霊、面影、ゴースト", "Old English", "gāst (breath, spirit, angel, demon)", "An apparition of a dead person which is believed to appear or become manifest to the living, typically as a nebulous image", "肉体（。を（。捨て（。去（。り（。、ただの「吐息（。ガスト）」と（。なって（。彷徨（。う（。もの（。。（。残（。された（。者の（。記憶（。という（。名の（。檻（。から（。逃（。げ（。られ（。ず（。、今（。も（。そこに（。留（。ま（。って（。いる（。、愛（。お（。しき（。遺残。"),
    ("labyrinth", "Labyrinth", "迷宮、ラビリンス", "14th Century", "labyrinthos (maze of Minotaur)", "A complicated irregular network of passages or paths in which it is difficult to find one's way; a maze", "出口（。を（。求めて（。彷徨（。えば（。彷徨（。う（。ほど（。、さらに「奥（。深く（。へと（。誘（。わ（。れる（。ラブリ）」、思考（。の（。罠（。。（。中心（。へと（。辿（。り（。着（。く（。こと（。を（。止（。めた（。時（。、あなた（。は（。その（。迷宮（。その（。ものと（。な（。る（。のですよ。"),
    ("enigma", "Enigma", "謎、不可解なもの、エニグマ", "16th Century", "ainigma (riddle)", "A person or thing that is mysterious, puzzling, or difficult to understand", "あからさま（。な（。正解を（。拒み（。、ただ「謎（。エニグマ）として（。あり（。続ける（。）」こと（。。（。その（。答えの（。出ない（。奥行きこそが（。、知性（。に（。永遠の（。飢（。えと（。渇（。き（。を（。与（。え（。る（。のですよ。"),
    ("hidden", "Hidden", "隠された、秘密の", "Old English", "hydan (to hide, conceal)", "Kept out of sight; concealed", "光（。の（。当た（。る（。場所（。ではなく（。、厚い（。ヴェールの「内側（。に（。仕（。舞（。い（。込（。ま（。れた（。ハイド）」もの（。。（。隠（。されて（。いる（。からこそ（。、それ（。は（。、あなた（。の（。魂を（。、より（。強（。烈（。に（。惹（。き（。つける（。の（。ですよ。"),
    ("latent", "Latent", "潜在的な、潜伏している", "16th Century", "latere (to lie hidden)", "Existing but not yet developed or manifest; hidden or concealed", "今（。は（。まだ（。時（。を（。待って（。、物陰（。に「静かに（。横たた（。わ（。って（。ラテ）眠（。って（。いる（。）」エナジー（。。（。いつか（。訪（。れる（。臨界（。点（。を（。夢（。見（。ながら（。、静（。か（。に（。牙（。を（。研（。いで（。いる（。の（。ですよ。")
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
            word_id = f"{word_text.lower()}_dream"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "夢は、現実が自らの限界を思い知ったときに、そっと差し出す贈り物です。",
                    "example": f"The entire experience felt like a strange {word_text} from which he couldn't wake up.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["現実は、ただ一つの夢であり、夢は、無数の現実であるのかもしれません。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["hidden", "latent"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Dream & Reality (Cycle 46).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
