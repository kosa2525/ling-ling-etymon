import json
import re

# Theme: The Alchemy of Ember & Ignition II (Cycle 112)
words_data = [
    ("ember", "Ember", "残り火、残り香、余韻、エンバー", "Old English", "æmerge (ember)", "A small glowing fragment of coal or wood in a dying fire", "情熱の（。末に（。、静（。か（。に「灯（。り（。続け（。る（。エンバー）』至高の（。る（。る（。余韻（。（。その（。眩（。し（。い（。ほどに（。る（。る（。熱の（。る（。欠片（。を、魂で、誇り（。高く、愛（。で（。て（。ください。"),
    ("ignite", "Ignite", "点火する、火を付ける、イグナイト", "17th Century", "ignis (fire, literal: 'to set on fire')", "Catch fire or cause to catch fire", "沈黙を（。峻（。烈（。に「一（。気へと（。燃（。え（。上が（。らせ（。る（。イグナイト）』こと（。（。その（。一瞬の（。る（。る（。閃光（。が、世界を、至高の（。る（。る（。聖堂へと、塗り（。替（。えます。"),
    ("scald", "Scald", "火傷（。を（。させる（。、熱（。湯を（。かける（。、スカールド", "13th Century", "ex- (out, thoroughly) + calere (to be hot, literal: 'thoroughly hot')", "Injure with very hot liquid or steam", "宇宙の（。熱（。量が、あなたの（。魂を「峻（。烈（。に（。貫（。き、傷（。付ける（。スカールド）』こと（。（。その（。痛み（。の中にこそ、真実の（。る（。生命の（。鼓動が、今（。も、宿（。って（。いる（。のですよ。"),
    ("singe", "Singe", "表面を焼く、焦がす、シンジ", "Old English", "sengan (to singe, burn lightly, literal: 'to cause to sing')", "Burn something superficially or lightly", "エナジーの（。端を、静（。か（。に「焦（。が（。す（。シンジ）』至高の（。る（。る（。技巧（。（。その（。香ば（。し（。い（。る（。る（。時間は、あなたを、真（。理（。へと、誘（。う（。の（。ですよ。"),
    ("char", "Char", "黒焦げにする、炭にする、チャー", "17th Century", "char (charcoal, literal: 'to turn to charcoal')", "Partially burn so as to blacken its surface", "全（。てを（。峻（。烈（。な（。る（。力で「灰（。へと（。変える（。チャー）』、至高の（。る（。純粋（。さ（。（。その（。漆黒の（。る（。る（。沈黙を、魂で、愛（。お（。しん（。で（。ください。"),
    ("parch", "Parch", "乾かす、焙（。る（。、パーチ", "14th Century", "Origin uncertain, possibly related to perish", "Make or become dry through intense heat", "世界（。を、至高（。の（。る「峻（。烈（。な（。る（。る（。乾（。燥（。パーチ）』の中に、閉じ（。込（。め（。る（。こと（。（。その（。渇（。き（。の中にこそ、真実の（。る（。潤（。いが、静（。か（。に、産声を上げます。"),
    ("sear", "Sear", "焦がす、焼き付ける、シアー", "Old English", "searian (to dry up, wither)", "Burn or scorch the surface of something with a sudden, intense heat", "魂（。を、一（。気（。へと「焼き（。付け（。た（。シアー）』至高の（。る（。刻印（。（。その（。峻（。烈（。な（。る（。手（。応（。え（。に、あなたは（。、宇宙（。の（。深（。淵（。を、見出し（。ます。"),
    ("toast", "Toast", "乾杯、焼いたパン、トースト", "14th Century", "torrere (to parch, literal: 'parched')", "Drink to the health or in honor of someone or something by raising one's glass together with others", "命の（。共鳴を、至高の（。る「喜び（。トースト）』として、分（。か（。ち（。合う（。こと（。（。その（。一一点の（。る（。る（。祝福（。を、全身で、誇り（。高く、受け（。止めて（。ください。")
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
            word_id = f"{word_text.lower()}_flame_iv"
            
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
                    "thinking": item[6] if len(item) > 6 else "炎とは、破壊の力ではありません。自らの内側にある不必要なエネルギーを焼き尽くし、純粋な光へと変容させるための、至高のる浄化のプロセスなのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "残り火は、孤独なものではない。それは、かつてそこにあった熱い情熱が、静かに世界へと溶け込んでいくための、聖なる橋渡しなのですよ。",
                    "example": f"The blacksmith used the intense heat of the {word_text}ing coals to forge the intricate patterns into the blade of the legendary sword.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["熱を帯びることは、冷静さを欠くことではありません。自らの中心にある真実の熱を、一点の曇りなく、世界へと放射し続ける誠実さのことなのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] in ["ember", "toast"] else "verb"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Ember & Ignition II (Cycle 112).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
