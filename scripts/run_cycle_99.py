import json
import re

# Theme: The Alchemy of Aura & Nimbus (Cycle 99)
words_data = [
    ("nimbus", "Nimbus", "光輪、後光、雲、ニンバス", "17th Century", "nimbus (cloud, cloud of light, literal: 'cloud')", "A luminous cloud or a halo surrounding a supernatural being or a saint", "至高の（。る（。魂（。から（。一（。気へと（。溢（。れ（。出した「光の（。雲（。ニンバス）』。（。その（。眩（。しい（。ほど（。に（。柔らかな（。る（。輝きが、あなた（。という（。存在（。の（。真実（。を、静（。か（。に（。、物語（。っ（。て（。いる（。のですよ。"),
    ("corona", "Corona", "コロナ、冠、光環", "16th Century", "corona (crown)", "The rarefied gaseous envelope of the sun and other stars", "宇宙の（。中心（。から（。峻（。烈（。に（。広（。が（。る「至高の（。王（。冠（。コロナ）』。（。その（。圧倒（。的（。な（。る（。エナジーの（。余韻を、魂で（。、一一点の（。曇り（。な（。く、感（。じ（。て（。いて（。ください。"),
    ("aurora", "Aurora", "オーロラ、暁、女神", "14th Century", "aurora (dawn, literal: 'dawn')", "A natural electrical phenomenon characterized by the appearance of streamers of reddish or greenish light in the sky, especially near the northern or southern magnetic pole", "暗黒（。の（。夜を（。、至高（。の（。色彩で（。塗り（。替（。える「夜（。明け（。の（。女神（。アウロラ）』。（。その（。不（。可（。解な（。る（。旗図（。の中に、宇宙（。の（。全（。情熱が、静（。か（。に（。、横（。たわ（。って（。いる（。のです。"),
    ("beacon", "Beacon", "灯台、標識、ビーコン", "Old English", "beacen (sign, signal, literal: 'sign')", "A fire or light set up in a high or prominent position as a warning, signal, or celebration", "迷（。い（。の中（。で（。、一（。点（。を（。指（。し（。示（。す「眩（。しい（。標識（。ビーコン）』。（。その（。峻（。烈（。な（。る（。道（。標を、あなたは（。、信（。じ（。抜く（。ことが、でき（。る（。の（。でしょうか。"),
    ("lantern", "Lantern", "ランタン、灯籠（。とうろう（。）」", "13th Century", "lanterna (lamp, lantern)", "A typical portable source of lighting, typically comprising a protective case of glass or metal surrounding a candle or a flame etc.", "暗闇を（。、掌（。の（。中（。で（。、そっと（。照（。ら（。す「小（。さな（。る（。る（。聖域（。ランタン）』。（。その（。揺（。れる（。灯の（。中に（。、あなた（。の（。魂は、真実（。の（。る（。安らぎを、見（。出し（。ます。"),
    ("torch", "Torch", "たいまつ、トーチ", "13th Century", "torqua (twisted thing, literal: 'twisted thing made of hemp/tow')", "A portable means of illumination such as a piece of wood or cloth soaked in tallow or other fat and ignited", "意志という（。名の（。紐を（。、峻（。烈（。に「捻（。り（。合わせ（。た（。トーチ）』。（。その（。燃（。え（。盛（。る（。情熱の（。る（。る（。一一点（。を（。、誇り（。高く、掲（。げ（。な（。さい。")
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
            word_id = f"{word_text.lower()}_light"
            
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
                    "thinking": item[6] if len(item) > 6 else "輝きとは、強さではありません。自らの内側にある情熱を、一点の曇りなく、外側へと溢れさせ続けている、魂の誠実さのことなのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "オーラは、自分を飾るためのものではない。自らの存在そのものが、光の源泉であることを、世界へと静かに宣言しているのですよ。",
                    "example": f"The artist successfully captured the ethereal {word_text} that seemed to emanate from the ancient artifacts in the dimly lit gallery.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["暗闇を恐れることはありません。光は、暗闇が深ければ深いほど、その真実の美しさを増していくものなのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Aura & Nimbus (Cycle 99).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
