import json
import re

# Theme: The Pulse of Mystery & Enigma (Cycle 32)
words_data = [
    ("mystic", "Mystic", "神秘的な、神秘主義者", "14th Century", "mustikos (secret, mystic)", "A person who seeks by contemplation and self-surrender to obtain unity with or absorption into the Deity or the absolute, or who believes in the spiritual apprehension of truths that are beyond the intellect", "目（。に見える（。物理的な（。世界を超え（。、「沈黙（。ミュース）のうちに（。閉じ込められた（。）」神聖な（。真理を（。、魂の（。深い震えで（。捉えようと（。する者。"),
    ("occult", "Occult", "神秘的な、秘儀の、隠された", "15th Century", "occulere (to cover over, hide, conceal)", "Commending to or involving supernatural powers or magic", "白日の（。下（。ではなく（。、厚（。いヴェールで「覆（。い（。オ・クルト）隠（。された（。）」場所にある（。、選ばれた（。者だけが（。触（。れる（。ことを（。許された（。、深淵（。なる（。智恵。"),
    ("esoteric", "Esoteric", "秘儀的な、難解な、奥義の", "17th Century", "esotero (inner)", "Intended for or likely to be understood by only a small number of people with a specialized knowledge or interest", "外側（。への（。虚飾（。ではなく（。、ひたすら「内側（。エソ）へ（。エソ）へと」意識（。を（。潜（。らせ（。た（。果てに（。辿り着く（。、純粋（。で（。峻烈（。な（。真髄の（。場所。"),
    ("arcane", "Arcane", "難解な、秘密の", "16th Century", "arca (chest, box)", "Understood by few; mysterious or secret", "巨大な（。権威や（。歴史の（。荒波から（。守るため（。、「箱（。アーカ）に（。厳重に（。閉じ込められた（。）」、決して（。風化（。することのない（。、硬質な（。古代の（。叡智。"),
    ("cryptic", "Cryptic", "謎めいた、隠伏的な、暗号の", "17th Century", "kruptos (hidden)", "Having a meaning that is mysterious or obscure", "直接（。語る（。代わりに（。、地下（。深く（。掘られた「秘密の（。クリプト）小部屋」に（。そっと（。仕舞（。い（。込まれた（。、解き（。明かされる（。のを（。待つ（。、沈黙の（。メッセージ。"),
    ("enigmatic", "Enigmatic", "謎めいた、不可解な", "17th Century", "ainigma (riddle)", "Difficult to interpret or understand; mysterious", "一筋（。縄（。では（。行（。かない（。、「怪物（。スフィンクス（。が（。出す（。ような（。難問（。エニグマ）」に（。満ち（。て（。おり（。、思考（。の（。限界を（。軽（。やかに（。嘲笑（。する（。ような（。、深（。い（。奥行き。"),
    ("obscure", "Obscure", "不明瞭な、無名の、覆い隠す", "14th Century", "ob- (over, against) + scurus (covered)", "Not discovered or known about; uncertain", "光（。の（。当た（。らない（。、「闇に（。オブ）覆（。われた（。スキュール）」場所（。に（。あり（。、その（。輪郭（。を（。捉（。えようと（。すれば（。するほど（。、霧の（。中に（。霧散（。して（。しまう（。、儚（。い（。真理。"),
    ("nebulous", "Nebulous", "星雲状の、漠然とした", "14th Century", "nebula (cloud, mist)", "In the form of a cloud or haze; hazy", "まだ（。かたち（。を（。持（。た（。ず（。、宇宙の「塵（。ちり）や（。霧（。ネビュラ）」が（。漂（。って（。いる（。だけの（。ような（。状態（。。（。無限（。の（。可能性（。を（。秘（。めた（。、誕生（。直前の（。混沌。"),
    ("ethereal", "Ethereal", "エーテルのような、極めて優美な、天上の", "16th Century", "aither (upper air, pure air)", "Extremely delicate and light in a way that seems too perfect for this world", "地上（。の（。泥（。から（。は（。正反対の（。、「天上の（。清浄な（。エーテル）」で（。満（。た（。された（。ような（。、触（。れ（。た（。瞬間に（。消（。えて（。しまい（。そうな（。、奇跡（。のような（。美しさ。"),
    ("celestial", "Celestial", "天の、天体の", "14th Century", "caelum (sky, heaven)", "Positioned in or relating to the sky, or outer space as observed in astronomy", "私たちの（。足元（。の（。大地（。を（。遥（。かに（。離（。れ（。、「空（。セレス）という（。高み（。）」に（。ある（。全知全能（。の（。光（。と（。視点。"),
    ("cosmic", "Cosmic", "宇宙の、秩序ある、巨大な", "17th Century", "kosmos (order, world, universe)", "Relating to the universe or cosmos, especially as distinct from the earth", "ただの（。広大（。さで（。はなく（。、そこ（。に（。完璧な「秩序（。コスモス）」が（。貫（。かれて（。いる（。ことに（。対（。する（。、畏（。怖（。と（。敬意（。を（。伴（。った（。、巨大（。な（。認識。"),
    ("abyss", "Abyss", "深淵、奈落", "14th Century", "a- (without) + bussos (bottom)", "A deep or seemingly bottomless chasm", "どこ（。まで（。行（。っても「底（。ブッソ）がない（。ア）」、暗黒（。の（。巨大（。な（。穴（。。（。思考（。の（。果（。て（。に（。口（。を開（。けて（。いる（。、飲み込ま（。れる（。ような（。虚無。"),
    ("chasm", "Chasm", "（地面の）裂け目、隔たり", "16th Century", "khasma (yawning hollow)", "A deep fissure in the earth, rock, or other surface", "ただの（。穴（。では（。なく（。、巨大な（。エナジーによって（。、「大きく（。あくびを（。する（。カスマ）ように（。口を（。開けた（。）」、断絶（。と（。隔たり（。の（。深淵。"),
    ("fissure", "Fissure", "裂け目、割れ目", "14th Century", "findere (to split)", "A long, narrow opening or line of breakage made by cracking or splitting, especially in rock or earth", "強固（。な（。岩（。といえ（。ども（。、内部（。からの（。圧力（。によって（。「引き裂（。き（。フィス）割られた（。）」、その（。境界（。の（。痕跡。"),
    ("labyrinth", "Labyrinth", "迷宮、ラビリンス", "14th Century", "labyrinthos (maze of Minotaur)", "A complicated irregular network of passages or paths in which it is difficult to find one's way; a maze", "一度（。入り（。込め（。ば（。、中心（。まで（。辿（。り（。着（。く（。ことさえ（。許（。されない（。、「双（。刃の（。斧（。ラブリュス）が（。守（。る（。禁忌（。の（。場所」。（。出口（。の（。ない（。思索の（。複雑（。さ。"),
    ("cipher", "Cipher", "暗号、ゼロ、取るに足らない人", "14th Century", "sifr (zero, empty)", "A secret or disguised way of writing; a code", "表面（。の（。記述は（。ただの「虚無（。ゼロ・シフル）」で（。あり（。ながら（。、正しい（。鍵（。を（。持（。つ者（。に（。だけ（。は（。、真実（。の（。形を（。あら（。わ（。す（。、二重（。の（。言葉。"),
    ("latent", "Latent", "潜在的な、隠れている", "16th Century", "latere (to lie hidden)", "Existing but not yet developed or manifest; hidden or concealed", "今（。は（。まだ（。時（。を（。待って（。、物陰（。に「静かに（。横た（。わって（。ラテ）隠れている（。）」、爆発（。の（。予感（。を（。孕んだ（。未発の（。力。"),
    ("oracle", "Oracle", "神託、オーラクル", "14th Century", "orare (to speak)", "A priest or priestess acting as a medium through whom advice or prophecy was sought from the gods in classical antiquity", "人間（。の（。言葉（。を（。捨て（。、神々（。の（。意志（。の一部として「語る（。オレ）役目」を（。負っ（。た者（。。（。運命（。の（。扉（。を（。開ける（。ため（。の（。、謎（。めいた（。啓示。"),
    ("prophecy", "Prophecy", "予言、預言", "13th Century", "pro- (before, in place of) + phanai (to speak)", "A prediction of the future", "まだ（。起きて（。いない（。未来の（。ことを（。、神（。に代わって「あらかじめ（。プロ）語（。る（。フェイス）」こと（。。（。時の流れ（。を（。飛び越し（。、真理（。を（。今（。へと（。引き下ろす（。勇気。"),
    ("omen", "Omen", "前兆、予感", "16th Century", "omen (foreboding)", "An event regarded as a portent of good or evil", "静かなる（。日常（。の（。中に（。ふと（。入り（。込ん（。だ（。、未来（。からの（。「耳打ち（。オーメン）」。逃して（。は（。ならない（。、運命の（。風向きの（。変化。"),
    ("talisman", "Talisman", "お守り、タリスマン", "17th Century", "telesma (payment, ceremony, completion)", "An object, typically an inscribed ring or stone, that is thought to have magic powers and to bring good luck", "ただの（。飾り（。では（。なく（。、聖なる（。儀式を（。経て「完成（。テレス）された状態に（。）」ある（。、持ち主（。の（。意志（。を（。増幅（。し（。守り（。抜く（。、形（。を持った（。魔力。"),
    ("amulet", "Amulet", "守護札、アミュレット", "16th Century", "amuletum (an object that protects a person from trouble)", "An ornament or small piece of jewelry thought to give protection against evil, danger, or disease", "災い（。から（。持ち主（。を（。「遠ざけ（。アミュレート）守（。る（。）」ための（。、静かなる（。祈り（。の（。結晶（。。（。肌身（。離（。さず（。持つ（。ことで（。、心に（。聖域（。を作る（。もの。"),
    ("incantation", "Incantation", "呪文、インカンテーション", "14th Century", "in- (into) + cantare (to sing)", "A series of words said as a magic spell or charm", "普通の（。言葉（。に（。魔力（。を「吹き込（。イン）み、歌（。う（。カント）ように（。唱える（。）」こと（。。（。音（。の（。振動（。によって（。、世界（。の（。法則（。を（。一時的に（。ねじ曲げ（。よう（。とする（。試み。"),
    ("alchemy", "Alchemy", "錬金術、アルケミー", "14th Century", "al-kimiya (the chemistry)", "The medieval forerunner of chemistry, based on the supposed transformation of matter", "卑（。金属（。を（。黄金（。へと（。変（。える（。、あるいは（。死（。を（。不老不死（。へと（。変（。えよう（。とした（。、「融合（。キミヤ）」と（。変容（。を（。志（。す（。、魂の（。深淵なる（。実験空間。"),
    ("hermit", "Hermit", "隠者、世捨て人", "12th Century", "eremos (desolate, lonely)", "A person living in solitude as a religious discipline", "社会の（。喧騒（。を（。離（。れ（。、一人「荒野（。エレモス）に（。留まる（。）」こと（。を（。選（。んだ者（。。（。孤独（。という（。厳しい（。修行（。を（。通（。じて（。、内なる（。宇宙（。と（。対話（。し（。続ける（。存在。")
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
            word_id = f"{word_text.lower()}_mystery"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "謎は、明日を夢見るための最も美しいエッセンスです。",
                    "example": f"The old manuscript was written in a {word_text} language that took years to decode.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["神秘とは、知性が沈黙したときに初めて聞こえてくる、宇宙の囁きです。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["mystic", "occult", "esoteric", "arcane", "cryptic", "enigmatic", "obscure", "nebulous", "ethereal", "celestial", "cosmic", "latent"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Mystery & Enigma (Cycle 32).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
