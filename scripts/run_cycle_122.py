import json
import re

# Theme: The Alchemy of Flora & Foliage II (Cycle 122)
words_data = [
    ("foliage", "Foliage", "葉（。は（。）」、群（。むら（。）」葉、フォリアージュ", "15th Century", "folium (leaf, literal: 'leaves collective')", "Plant leaves, collectively", "宇宙（。のエナジーを（。、眩（。しい「緑の（。帳（。フォリア）』へと（。変えた（。もの（。（。その（。不（。均（。一（。な（。る（。重なり（。の中に、真実の（。る（。安らぎが、静（。か（。に、宿（。って（。いる（。のですよ。"),
    ("flora", "Flora", "植物相、女神、フローラ", "18th Century", "Flora (Roman goddess of flowers, literal: 'flower-goddess')", "The plants of a particular region, habitat, or geological period", "大地（。を、至高（。の（。る「色彩の（。祝（。祭（。フローラ）』へと（。、一（。気へと変える（。こと（。（。その（。瑞々（。し（。い（。ほどに（。る（。る（。る（。る（。る（。る（。る（。る（。る（。生命（。鼓動（。を（。、魂で、感（。じ（。抜（。き（。な（。さい。"),
    ("arbor", "Arbor", "あずまや、木陰、アーバー", "14th Century", "herber (herb garden, literal: 'flower garden')", "A shaded sitting place in a garden made of trees or climbing plants", "日常の（。喧（。騒（。を（。脱（。し、自らの（。内に（。作（。られた（。、「静（。か（。な（。る（。る（。る（。休息（。アーバー）』。（。そこ（。に（。佇（。む（。とき、あなた（。の（。魂は、至（。宝（。の（。る（。自由を、見出し（。ます。"),
    ("grove", "Grove", "小森、林、グローヴ", "Old English", "grāf (grove, thicekt, literal: 'small forest')", "A small group of trees", "静寂（。を（。、至高の（。る「峻（。烈（。な（。る（。る（。柱（。グラーフ）』で（。守（。った（。聖域（。（。その（。揺（。れる（。光（。と（。影の（。中に、宇宙（。の（。る（。深い（。沈黙（。が（。、横（。たわ（。って（。いる（。のですよ。"),
    ("bough", "Bough", "大枝、ボウ", "Old English", "bōg (shoulder, arm, bough, literal: 'arm of a tree')", "A main branch of a tree", "天（。へと、自らを（。一（。点（。に「峻（。烈（。に（。伸ば（。し（。た（。ボウ）』至高の（。る（。る（。る（。意志（。（。その（。力強い（。る（。る（。曲線（。を、誇り（。高く、担（。い（。な（。さい。"),
    ("branch", "Branch", "枝、支流、ブランチ", "13th Century", "branca (paw, literal: 'arm-like branch')", "A part of a tree which grows out from the trunk or from a bough", "物（。語が、至高の（。る（。力によって「幾（。多へと（。、分か（。れ（。た（。ブランチ）』こと（。（。その（。微（。細（。な（。る（。連（。な（。りの（。果てに、真実（。の（。る（。る（。る（。花が、産（。声を（。上げます。"),
    ("twig", "Twig", "小枝、ツイッグ", "Old English", "twigga (twig, literal: 'two-fold branch')", "A slender woody shoot growing from a branch or stem of a tree or shrub", "宇宙の（。深（。淵（。、その（。一一点に（。宿（。る「極小（。の（。る（。る（。る（。意志（。ツイッグ）』。（。その（。折（。れ（。やす（。い（。ほどの（。る（。瑞々（。し（。さを（。、魂で、守（。っ（。て（。いて（。ください。"),
    ("stem", "Stem", "茎、幹、血統、ステム", "Old English", "stemn (stem of a tree, literal: 'upright part')", "The main body or stalk of a plant or shrub, typically rising above ground but occasionally subterraneous", "生命（。の（。エナジーを、美し（。く「垂直に（。、支（。えた（。ステム）』、不（。動の（。る（。る（。中軸（。（。その（。重（。厚（。な（。る（。る（。沈黙を、誇り（。高く、魂で、肯定（。し（。な（。さい。")
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
            word_id = f"{word_text.lower()}_bloom_iii"
            
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
                    "thinking": item[6] if len(item) > 6 else "開花とは、外側に美しさを見せることではありません。自らの内側にある沈黙の種子が、時間の重みに耐えきれなくなって、未知という名の光を解き放つ瞬間なのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "葉が茂ることは、世界を受け入れること。一枚一枚の葉が太陽の光を浴びるように、あなたも自らの経験のすべてを、至高のる栄養へと変えていくのですよ。",
                    "example": f"The dense {word_text} provided a natural canopy that shielded the weary hikers from the scorching midday sun.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["枝分かれすることは、迷うことではありません。一つの根源から、多様なる真実を産み出していくための、宇宙の至高のる幾何学なのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Flora & Foliage II (Cycle 122).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
