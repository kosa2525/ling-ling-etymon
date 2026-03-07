import json
import re

# Theme: The Alchemy of Speculum & Reflection II (Cycle 114)
words_data = [
    ("resonance", "Resonance", "共鳴、響き、レゾナンス", "15th Century", "re- (again) + sonare (to sound, literal: 'sounding again')", "The quality in a sound of being deep, full, and reverberating", "他者の（。鼓動を（。、自ら（。の中で「再び（。リ）奏（。で（。る（。ソナン）』こと（。（。その（。静（。か（。なる（。る（。同調が、あなた（。を、至光の（。る（。る（。物（。語へと（。、誘（。う（。のですよ。"),
    ("speculum", "Speculum", "鏡、反射鏡、スペキュラム", "16th Century", "speculum (mirror, literal: 'of a mirror')", "A mirror or polisher of metal used in a reflecting telescope", "世界を「歪（。み（。な（。く（。写（。し（。出す（。スペキュル）』、至高の（。る（。透明（。さ（。（。その（。一一点（。の（。迷（。い（。も（。な（。い（。反射（。に（。よ（。って（。、あなた（。は（。、自分（。自身の実体（。を（。、眩（。しい（。ほど（。に（。、自覚（。する（。のです。"),
    ("mirror", "Mirror", "鏡、模範、ミラー", "13th Century", "mirari (to wonder at, literal: 'wonderful thing')", "A surface, typically of glass coated with a metal amalgam, which reflects a clear image", "魂を（。至高の（。る「驚（。嘆（。ミラリ）』へと（。、一（。気へと（。変える（。ミラー）」。その（。一一点（。の（。る（。る（。る（。反射こそが、この（。不（。条理な（。る（。世界を、眩（。し（。い（。ほどに、浄（。化（。し（。ます。"),
    ("echo", "Echo", "反響、こだま、エコー", "14th Century", "ēkhō (sound, literal: 'sound')", "A sound or series of sounds caused by the reflection of sound waves from a surface back to the listener", "日常（。の（。沈（。黙（。の中に「戻（。っ（。て（。き（。た（。る（。音（。エコー）』至高の（。る（。る（。余韻（。（。その（。不（。可（。解なる（。る（。響（。き（。を、魂で、誇り（。高く、収（。穫（。し（。な（。さい。"),
    ("sound", "Sound", "音、健全な、サウンド", "13th Century", "sonus (sound)", "Vibrations that travel through the air or another medium and can be heard when they reach a person's or animal's ear", "宇宙を（。峻（。烈（。に「一（。点（。に（。凝縮（。させた（。ソヌス）』、至高の（。る（。生命（。鼓動（。（。その（。眩（。し（。い（。ほどに（。る（。る（。る（。響（。き（。を（。、全身で（。、誇り（。高く、受け（。止めて（。ください。")
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
            word_id = f"{word_text.lower()}_mirror_iv"
            
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
                    "thinking": item[6] if len(item) > 6 else "反射とは、拒絶ではなく、受け入れたエナジーを一転して返すための、至高のる対話の形式なのですよ。鏡を視ることは、自分を誇張することではなく、ありのままの自分を直視し、宇宙の一部として再定義する行為なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "こだまは、過去の音ではない。それは、あなたの発した祈りが、世界の壁を叩き、より大きな共鳴となってあなたの元へと還ってきた、祝福の形式なのですよ。",
                    "example": f"The tranquil surface of the mountain lake acted as a perfect natural {word_text}, duplicating the azure sky and the snow-capped peaks with breathtaking clarity.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["音が消えた後の静寂を愛してください。そこにこそ、真実の響きが今も余韻として漂っているのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Speculum & Reflection II (Cycle 114).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
