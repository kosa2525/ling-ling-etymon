import json
import re

# Theme: The Alchemy of Verity & Axiom II (Cycle 94)
words_data = [
    ("verity", "Verity", "真実、真理、ヴェリティ", "14th Century", "veritas (truth, literal: 'truth')", "A true principle or belief, especially one of fundamental importance", "全（。ての（。虚飾を（。剥（。ぎ（。取（。っ（。た（。、至高の（。る「真実（。ヴェリタス）』。（。その（。峻（。烈（。な（。る（。美（。しさが（。ある（。か（。ら（。こそ（。、世界（。は（。、一（。つ（。の（。眩（。し（。い（。光へと（。、還（。る（。のですよ。"),
    ("axiom", "Axiom", "自明の理、公理、アクシィオム", "15th Century", "axiōma (that which is thought worthy, literal: 'worthy thing')", "A statement or proposition which is regarded as being established, accepted, or self-evidently true", "証明（。を（。必要（。と（。し（。な（。い（。、「最も（。高（。貴（。な（。る（。理（。アクシィオム）』。（。その（。不（。動の（。意志に（。、あなた（。は（。、ただ（。、魂を（。、跪（。か（。せ（。て（。ください。"),
    ("real", "Real", "実在の、本物の、リアル", "14th Century", "res (thing, literal: 'concerning things')", "Actually existing as a thing or occurring in fact; not imagined or supposed", "夢（。の中（。の（。幻（。を（。脱（。し（。、ただ（。そこに（。在（。る（。事実（。を「物（。事（。リス）その（。もの（。として（。）」受け（。入れる（。こと（。。（。その（。峻（。烈（。な（。る（。手（。応（。え（。にこそ（。、生（。の（。真（。実（。が（。宿（。ります。"),
    ("plain", "Plain", "平易な、明白な、質素な、プレーン", "13th Century", "planus (flat, even, level)", "Easy to perceive or understand; clear", "何（。も（。飾（。ら（。ず（。、ただ「平（。ら（。か（。な（。プラヌス）」真実（。（。その（。峻（。烈（。な（。る（。簡（。潔（。さに（。触れた（。とき、あなた（。の（。魂は、至高（。の（。る（。自由（。を、見出し（。ます。"),
    ("direct", "Direct", "直接の、率直な、ディレクト", "14th Century", "di- (apart) + regere (to guide, literal: 'guided straight')", "Extending or moving from one place to another by the shortest way without changing direction or stopping", "迷（。う（。こと（。なく、ただ（。一（。点へと「真っ（。直（。ぐ（。に（。向（。か（。う（。レク）』意志。（。その（。峻（。烈（。な（。る（。迷（。い（。の（。な（。さが（。、不（。可能（。を（。、眩（。し（。い（。奇跡へと（。、変（。え（。て（。いく（。のですよ。"),
    ("absolute", "Absolute", "絶対の、無条件の、アブソリュート", "14th Century", "ab- (away) + solvere (to loosen, literal: 'loosened from')", "Not qualified or diminished in any way; total", "あらゆる（。制（。約から「解（。き（。放（。た（。れた（。アブ・ソリュ）』、至高（。の（。る（。一点（。（。その（。孤（。高（。な（。る（。純粋（。さ（。を（。、誇り（。高く、その（。胸（。に（。、抱（。き（。続け（。てください。"),
    ("unit", "Unit", "単位、一個、ユニット", "16th Century", "unus (one)", "An individual thing or person regarded as single and complete but also as a component of a larger or more complex whole", "全（。てを（。一、一（。つ（。の（。数字に「統合（。し（。た（。ウヌス）』至高の（。る（。一（。。（。その（。峻（。烈（。な（。る（。単（。一（。さ（。が（。ある（。から（。こそ（。、宇宙の（。数（。学（。は、完璧（。な（。る（。美し（。さを、保（。ち（。ます。"),
    ("total", "Total", "合計の、完全な、トータル", "14th Century", "totus (all, whole, literal: 'all')", "Comprising the whole number or amount", "欠（。片を（。一（。つも（。漏（。ら（。さ（。ず（。、「全（。ての（。エナジーを（。、一（。つへと（。束（。ね（。た（。トータス）』。（。その（。圧倒（。的な（。る（。完結の中に（。、真（。の（。安らぎが（。、静（。か（。に（。宿（。る（。のですよ。"),
    ("simple", "Simple", "単純な、質素な、シンプル", "13th Century", "sim- (one) + plicare (to fold, literal: 'one-fold')", "Easily understood or done; presenting no difficulty", "幾（。重（。にも（。重（。な（。る（。想（。いを「一（。つ（。シン）に（。、畳（。み（。込（。ん（。だ（。プレ）』、峻（。烈（。な（。なる（。る（。簡（。潔（。。（。その（。静（。か（。な（。る（。一点（。を（。、魂で（。、愛（。で（。て（。ください。"),
    ("single", "Single", "単独の、独身の、シングル", "14th Century", "singulus (one by one, literal: 'individual')", "Only one; not one of several", "他（。の（。何物（。でも（。ない（。、ただ「一（。つ（。として（。、そこに（。在（。る（。シンギュ）』、至高の（。る（。孤独（。（。その（。峻（。烈（。な（。る（。立（。脚（。こそが、世界（。を（。、美し（。く（。、更新（。し（。て（。いく（。のです。"),
    ("fact", "Fact", "事実、実際、ファクト", "15th Century", "factum (thing done, literal: 'done')", "A thing that is known or proved to be true", "想（。いを（。越元（。て、「な（。さ（。し（。め（。られた（。ファク）』不（。動の（。現実（。（。その（。圧倒（。的な（。る（。冷（。徹さに（。触れる（。とき、あなた（。は（。、真実（。の（。る（。生（。を、知（。る（。ことに（。なり（。ます。"),
    ("frank", "Frank", "率直な、フランク", "13th Century", "Old French franc (free, literal: 'free')", "Open, honest, and direct in speech or writing, especially when dealing with unpalatable matters", "飾（。る（。のを（。止（。め、ただ「自由（。フラ）」に、真（。実（。を（。語（。る（。こと（。。（。その（。眩（。しい（。ほど（。の（。、潔（。い（。る（。沈黙を、誇り（。高く、愛（。お（。しん（。で（。ください。"),
    ("candid", "Candid", "率直な、公平な、キャンディッド", "17th Century", "candidus (white, shining, literal: 'shining white')", "Truthful and straightforward; frank", "一点（。の（。汚れ（。も（。ない、美（。し（。き「真っ（。白（。な（。る（。キャンディ）』真実（。（。その（。眩（。し（。い（。光に（。照ら（。された（。とき、世界（。の（。全容が、静（。か（。に（。浮かび（。上がり（。ます。"),
    ("straight", "Straight", "真っ直ぐな、正確な、ストレイト", "Language", "streccan (to stretch, literal: 'stretched tight')", "Extending or moving in one direction only; without a curve or bend", "魂の（。弦（。を、一（。点（。に（。向かって「引き（。絞（。っ（。た（。ストレイト）』、峻（。烈（。な（。る（。一直線（。（。その（。迷（。い（。の（。な（。い（。る（。輝きが、暗（。闇（。を（。、至高（。の（。る（。光へと（。、変（。え（。ます。")
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
            word_id = f"{word_text.lower()}_truth"
            
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
                    "thinking": item[6] if len(item) > 6 else "真実とは、多くの言葉を必要としません。ただそこに、圧倒的なる静寂として存在している、不変なる光のことなのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "事実は、残酷なものではありません。それは、あなたが自らを裏切るのを止めるための、至高のる慈悲のようなものなのですよ。",
                    "example": f"The scientist dedicated her entire career to uncovering the fundamental {word_text} that governed the behavior of subatomic particles.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["真っ直ぐであることは、不器用であることではありません。宇宙の重力に従い、自らのエナジーを最も純粋な一点へと凝縮させることなのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["real", "plain", "direct", "absolute", "total", "simple", "single", "frank", "candid", "straight"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Verity & Axiom II (Cycle 94).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
