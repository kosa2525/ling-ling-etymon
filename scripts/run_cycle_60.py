import json
import re

# Theme: The Alchemy of Pendulum & Balance (Cycle 60)
words_data = [
    ("pendulum", "Pendulum", "振り子、ペンデュラム", "17th Century", "pendere (to hang)", "A weight hung from a fixed point so that it can swing freely backward and forward, especially a rod with a weight at the end that regulates the mechanism of a clock", "一（。点（。に（。留（。ま（。ら（。ず（。、ただ（。重力（。という（。名の（。運命に「吊（。る（。さ（。れ（。て（。ペン）揺（。れ（。動き（。続ける（。）」こと（。。（。その（。左右の（。往（。復（。の中（。にこそ（。、現在（。とい（。う（。名の（。、静（。か（。な（。る（。ゼロ（。点（。が（。あります。"),
    ("oscillation", "Oscillation", "振動、発振、オシレーション", "17th Century", "oscillum (a little mask of Bacchus hung from a tree, literal: 'little mouth')", "Movement back and forth at a regular speed", "風（。に（。揺（。れる「小さな（。仮面（。オシルム）」のような（。、絶（。え（。間（。ない（。往復運動（。。（。その（。規則（。正しい（。震（。えが（。、静止（。し（。た（。世界に（。、新しい（。時間（。の（。波紋（。を（。投（。げ（。込む（。の（。ですよ。"),
    ("frequency", "Frequency", "頻度、周波数、フリクエンシー", "16th Century", "frequens (crowded, repeated)", "The rate at which something occurs or is repeated over a particular period of time or in a given sample", "バラバラ（。では（。なく（。、「密（。に（。フリク）繰（。り（。返（。さ（。れる（。）」こと（。。（。その（。波の（。激（。し（。さが（。、あなた（。の（。エナジーが（。、今（。どれ（。ほど（。高（。揚（。し（。て（。いる（。かを（。、雄弁に（。語（。り（。ます。"),
    ("wavelength", "Wavelength", "波長、ウェーブレングス", "19th Century", "wave + length", "The distance between successive crests of a wave, especially points in a sound wave or electromagnetic wave", "響き（。が（。一（。つ（。の「ピークを（。越えて（。ウェーブ）次に（。至（。る（。までの（。距離（。レングス）」。（。誰（。か（。と（。波長が（。合う（。なら（。、それ（。は（。、魂（。の（。歩（。幅（。が（。同（。じ（。と（。いう（。こと（。なの（。ですよ。"),
    ("amplitude", "Amplitude", "振幅、豊かさ、アンプリチュード", "16th Century", "amplus (large, wide)", "The maximum extent of a vibration or oscillation, measured from the position of equilibrium", "ただ（。揺（。れる（。だけ（。では（。なく（。、いかに「大きく（。アンプ）広（。が（。る（。）」か（。という（。度合い（。。（。その（。烈（。しい（。振幅（。だけが（。、世界（。の（。壁（。を（。打（。ち（。破（。る（。、真（。実（。の（。力（。と（。なる（。のですよ。"),
    ("trough", "Trough", "波の谷、水槽、苦境、トラフ", "Old English", "trog (hollow vessel, literal: 'tree')", "A long, narrow open container for animals to eat or drink out of", "波が（。最も（。引（。き（。、深（。く「沈（。み（。込（。ん（。だ（。トロ）」場所（。。（。けれど（。、その（。深（。い（。谷（。がある（。から（。こそ（。、次（。には（。、より（。眩（。しい（。頂（。が（。、あなた（。を（。待（。って（。いる（。の（。ですよ。"),
    ("drift", "Drift", "漂流、趣旨、ドリフト", "13th Century", "drīfan (to drive)", "A continuous slow movement from one place to another", "自ら（。の（。意志（。を（。手放し（。、ただ（。何（。物（。か（。に「駆（。り（。立て（。ら（。れて（。ドリ）彷徨（。う（。）」こと（。。（。その（。あて（。の（。ない（。旅の（。果てに（。、予期せ（。ぬ（。真（。実（。が（。、あなたを（。迎（。えて（。くれる（。のですよ。"),
    ("flood", "Flood", "洪水、溢れる、フラッド", "Old English", "flōd (flowing water, flood)", "An overflowing of a large amount of water beyond its normal confines, especially over what is normally dry land", "抑（。え（。切（。れ（。ない（。エナジーが（。、「溢（。れ（。出し（。フロ）押し寄（。せる（。）」こと（。。（。全（。てを（。押し流（。す（。その（。峻烈（。さ（。は（。、古い（。執（。着（。を（。消（。し（。去（。り（。、大地（。を（。浄（。化（。する（。ための（。祈り。"),
    ("ebb", "Ebb", "引き潮、衰退、エブ", "Old English", "ebba (ebb, low tide)", "The movement of the tide out to sea", "あれほど（。烈（。しか（。った（。波（。が（。、静（。かに「引（。いて（。去（。る（。エブ）」こと（。。（。その（。寂（。び（。し（。い（。沈黙（。の（。中に（。、私たちは（。、自分（。の（。本（。当（。の（。輪郭（。を（。、再び（。見（。出（。す（。のですよ。"),
    ("vortex", "Vortex", "渦、渦巻き、ボルテックス", "17th Century", "vertere (to turn)", "A mass of whirling fluid or air, especially a whirlpool or whirlwind", "全（。てを（。中心（。へと「回転（。させ（。ヴォル）巻き（。込む（。）」巨大（。な（。力（。。（。一度（。捕ら（。え（。られたら（。、もう（。抗（。う（。こと（。は（。でき（。ない（。けれど（。、その（。深淵（。の（。先に（。、真（。実（。が（。ある（。のですよ。"),
    ("ripple", "Ripple", "小波、さざ波、リップル", "14th Century", "rimpel (wrinkle)", "A small wave or series of waves on the surface of water, caused by an object as a slight breeze", "静（。止し（。た（。水面（。に（。、不（。意に現れ（。た「小（。さな（。皺（。リンプ）」。（。一つ（。の（。小（。さな（。出来事（。が（。、いつしか（。全（。世界（。を（。揺（。さ（。ぶ（。る（。大きな（。波（。へと（。、繋（。が（。って（。いく（。のです。"),
    ("surge", "Surge", "急（。上昇（。）、うねり、サージ", "15th Century", "surgere (to rise)", "A sudden powerful forward or upward movement, especially by a crowd or by a natural force such as the waves or tide", "内（。側か（。ら（。溢（。れ（。出し（。、一気に「立ち（。上がる（。サージ）」こと（。。（。その（。圧倒（。的な（。エナジーの（。奔流（。に（。身（。を（。委（。ね（。、あなた（。の（。限界（。を、今（。一度（。、突（。き（。抜（。けて（。ください。"),
    ("swell", "Swell", "膨らむ、うねり、素晴らしい", "Old English", "swellan (to swell)", "Become larger or rounder in size, typically by absorbing water or as the result of an injury", "満ち（。足り（。て（。、「大きく（。膨ら（。む（。スウェル）」こと（。。（。海（。の（。底から（。湧（。き（。上がる（。巨大な（。うねり（。は（。、大地（。の（。重力（。さえ（。も（。、軽（。やかに（。越（。えて（。いく（。のです。"),
    ("zephyr", "Zephyr", "そよ風、西風、ゼファー", "14th Century", "Zephuros (Greek god of the west wind)", "A soft gentle breeze", "「西（。か（。ら（。吹（。く（。神の（。愛（。ゼフ）」のような（。、優（。し（。い（。風（。。（。あなた（。の（。頬（。を（。撫（。で（。る（。その（。温（。か（。な（。響（。き（。が（。、孤独（。な（。魂（。を、静（。か（。に（。癒（。し（。て（。くれる（。のですよ。"),
    ("phase", "Phase", "段階、位相、フェーズ", "16th Century", "phasis (appearance, literal: 'shining')", "A distinct period or stage in a series of events or a process of change or development", "月（。が（。満ち（。欠け（。るように（。、真理（。が「姿を（。変えて（。現れる（。フェイ）」こと（。。（。どの（。瞬間（。も（。一つの（。真実（。であり（。、それで（。いて（。全（。て（。ではない（。、流（。動（。的（。な（。る（。美し（。さ。")
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
            word_id = f"{word_text.lower()}_pendulum"
            
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
                    "thinking": item[6] if len(item) > 6 else "均衡とは、静止することではなく、二つの極端なエナジーの間で永遠に揺れ続ける勇気のことです。",
                    "aftertaste": item[7] if len(item) > 7 else "振り子は、時間がただの数字ではなく、宇宙の拍動そのものであることを、無言で物語っています。",
                    "example": f"The scientist observed the regular {word_text} of the device to calculate the gravitational force.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["揺れ動くことの中にこそ、生命の真実があり、動かないものは、もはや命を失っているのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Pendulum & Balance (Cycle 60).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
