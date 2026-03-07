import json
import re

# Theme: The Alchemy of Chord & Cadence II (Cycle 121)
words_data = [
    ("melody", "Melody", "旋律、旋法、流麗、メロディ", "13th Century", "melos (song) + aeidein (to sing, literal: 'singing songs')", "A sequence of single notes that is musically satisfying; a tune", "宇宙（。の（。時間を、美し（。い（。螺旋（。へと（。変える「歌（。メロス）』至高の（。る（。る（。連（。な（。り（。（。その（。一一点（。の（。瑞々（。し（。い（。る（。輝きを、ただ、魂で、肯定（。し（。て（。ください。"),
    ("chorus", "Chorus", "合唱、合奏、コーラス", "16th Century", "khoros (dance, ring of dancers and singers, literal: 'dance')", "A large organized group of singers, especially one that performs together with an orchestra or opera company", "バラバラ（。の（。鼓動が、一（。つ（。の（。円（。環（。へと「結（。ば（。れた（。ホロス）』至高の（。る（。共（。鳴（。（。その（。眩（。し（。い（。ほどに（。る（。る（。調和（。が、世界を、至光の（。る（。聖域へと、塗り（。替（。えます。"),
    ("verse", "Verse", "詩、韻文、バース", "Old English", "versus (line of writing, literal: 'turning of the plow')", "Writing arranged with a metrical rhythm, typically having a rhyme", "意味（。を、峻（。烈（。な（。る（。る「折（。り（。返し（。バース）』の中で（。、再（。定義（。する（。こと（。（。その（。不（。動の（。る（。る（。る（。幾（。何（。学（。を（。、魂で（。、誇り（。高く、愛（。で（。て（。ください。"),
    ("tune", "Tune", "旋律、調律、チューン", "14th Century", "Old French ton (sound, tone, literal: 'sound')", "A melody, especially one which is characteristic of a piece of music", "エナジーの（。弦を、美し（。く「整（。えた（。トン）』至高の（。る（。る（。る（。振動（。（。その（。不（。可（。解なる（。る（。る（。響（。き（。を（。、全身で（。受け（。止めて（。ください。")
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
            word_id = f"{word_text.lower()}_music_iv"
            
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
                    "thinking": item[6] if len(item) > 6 else "音楽とは、音を並べることではありません。音と音の間の沈黙。その空白の中に宿る、宇宙の深淵な響きを、自らの魂で紡ぎ出す行為なのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "合唱することは、自分を消すことではない。自分という名の音を、仲間という名の調べの中に正しく配置し、より大きな美しさの一部として再定義する、至高のる調和の形式なのですよ。",
                    "example": f"The hauntingly beautiful {word_text} drifted through the rainy streets, its delicate notes intertwining with the sound of the evening city like a forgotten prayer.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["旋律を口ずさむことは、自らの命を祝祭すること。その喜びの響きが、いつか誰かの孤独な夜を、静かに照らし出す希望となるのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Chord & Cadence II (Cycle 121).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
