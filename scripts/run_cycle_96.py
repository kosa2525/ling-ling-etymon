import json
import re

# Theme: The Alchemy of Marvel & Miracle (Cycle 96)
words_data = [
    ("marvel", "Marvel", "驚異、驚く、マーベル", "14th Century", "mirari (to wonder at, literal: 'wonderful thing')", "Be filled with wonder or astonishment", "日常の（。沈黙を（。、至高の（。る「輝き（。ミラリ）』で（。塗り（。替（。える（。こと（。（。その（。圧倒（。的な（。る（。存在（。感に（。、魂は（。、ただ（。、眩（。しい（。ほど（。に（。、震（。え（。る（。のですよ。"),
    ("miracle", "Miracle", "奇跡、ミラクル", "12th Century", "miraculum (object of wonder, literal: 'little wonder')", "A surprising and welcome event that is not explicable by natural or scientific laws and is therefore considered to be the work of a divine agency", "宇宙の（。深（。淵（。から（。、静（。か（。に（。産まれた「峻（。烈（。な（。る（。出来事（。ミラクル）』。（。不可能を（。越元（。た（。その（。一一点（。に、私たちは（。、至高の（。る（。愛を（。、視（。る（。のですよ。"),
    ("surprise", "Surprise", "驚き、不意打ち、サプライズ", "14th Century", "super- (above) + prendre (to take, literal: 'taken from above')", "An unexpected or astonishing event, fact, or thing", "天から（。不（。意に「魂を（。捉元（。た（。サプライ）』至高の（。衝撃（。（。その（。一瞬の（。閃光（。が（。、あなた（。の（。物語を（。、一気に（。、新（。しい（。次元へと（。、押し（。上げ（。ます。"),
    ("tremor", "Tremor", "震え、振動、トレマー", "14th Century", "tremere (to tremble)", "A quavering or vibratory motion, especially in the body of a person", "宇宙の（。鼓動が（。、あなた（。という（。存在を「静（。か（。に（。揺（。さ（。ぶ（。る（。トレマー）』こと（。（。その（。峻（。烈（。な（。る（。共鳴を、魂で（。、一一点の（。曇り（。な（。く（。、感（。じ（。て（。いて（。ください。"),
    ("shiver", "Shiver", "身震い、震える、シバー", "13th Century", "Middle English chiveren (related to Old English ceafl 'jaw', literal: 'chattering jaws')", "Shake slightly and uncontrollably as a result of being cold, frightened, or excited", "峻（。烈（。な（。る（。真実（。に（。触れた（。とき、魂が（。美し（。く「打ち（。震（。え（。る（。シバー）』。（。その（。危（。う（。い（。ほどの（。る（。瑞々（。し（。い（。自覚が、あなた（。を、至（。宝（。へと（。変え（。ます。"),
    ("quiver", "Quiver", "震える、矢筒、クィバー", "14th Century", "Middle English quiveren (to shake)", "Tremble or shake with a slight rapid motion", "一（。点（。を（。貫（。く（。ために、自らを「峻（。烈（。に（。震（。わ（。せ（。る（。クィバー）』エナジー。（。その（。一一点の（。緊張（。が、世界（。を（。、至高（。の（。る（。調和（。へと（。、導（。く（。のですよ。"),
    ("swell", "Swell", "膨らむ、うねり、スウェル", "Old English", "swellan (to swell)", "Become larger or rounder in size, typically as a result of an accumulation of fluid or gas", "宇宙の（。豊饒（。が、一（。気（。に「溢（。れ（。出した（。スウェル）』至高の（。る（。うねり（。（。その（。圧倒（。的な（。る（。る（。豊か（。さに（。、魂を（。、そっと（。、委（。ね（。て（。みて（。ください。"),
    ("surge", "Surge", "急騰、大波、サージ", "15th Century", "surgere (to rise, literal: 'rising up')", "A sudden powerful forward or upward movement, especially by a crowd or by a natural force such as the waves or tide", "地の（。底（。から、峻（。烈（。に「湧（。き（。上が（。っ（。た（。サージ）』、純粋（。な（。る（。エナジー。（。その（。一瞬の（。る（。飛躍が、あなた（。を、至高（。の（。る（。高（。みへと、運（。び（。去（。り（。ます。"),
    ("blast", "Blast", "爆風、突風、ブラスト", "Old English", "blæst (blowing, breeze, literal: 'strong gust')", "A destructive wave of highly compressed air spreading outward from an explosion", "沈黙を（。一（。瞬（。にして（。、「叩（。き（。壊（。す（。ブラスト）』、至高の（。る（。る（。息（。吹（。き（。（。その（。峻（。烈（。な（。る（。る（。激（。動の（。中にこそ（。、真実（。の（。輝きが（。、宿ります。"),
    ("gust", "Gust", "突風、ガスト", "16th Century", "Old Norse gustr (gust, literal: 'breath')", "A sudden strong rush of wind", "宇宙の（。囁（。きが、一（。気（。に「激（。しく（。吹（。き（。抜（。け（。た（。ガスト）』。（。その（。峻（。烈（。な（。る（。る（。余韻を、誇り（。高く、魂で（。、飲み（。干（。し（。て（。ください。"),
    ("breath", "Breath", "息、ブレス", "Old English", "bræth (odor, scent, literal: 'odor, exhalation')", "The air taken into or expelled from the lungs", "宇宙の（。全記憶を、静（。か（。に「吸（。い（。込み（。ブレス）』、命を（。通（。わ（。せる（。こと（。（。その（。一（。つ（。一（。つの（。る（。る（。呼吸の中にこそ（。、至高の（。る（。智慧が、今（。も横（。たわ（。って（。いる（。のです。"),
    ("sigh", "Sigh", "ため息、サイ", "13th Century", "Middle English sighen (related to Old English sican 'to sigh')", "Emit a long, deep, audible exhalation expressing sadness, relief, tiredness, or a similar feeling", "全（。てを（。受け（。入れ、静（。か（。に「吐（。き（。出した（。サイ）』、魂の（。る（。震（。え（。（。その（。幽（。玄な（。る（。響（。きの中に、真実（。の（。る（。解放が（。、宿（。って（。いる（。の（。ですよ。"),
    ("glow", "Glow", "輝き、グロウ", "Old English", "glōwan (to glow)", "Give out steady light without flame", "魂の（。奥底で、静（。か（。に「燃（。え（。続け（。る（。グロウ）』、至高の（。る（。微（。光（。（。その（。絶（。え（。間（。な（。き（。輝きが、世界（。を（。、至高（。の（。る（。聖域へと（。、塗り（。替（。え（。ます。"),
    ("flare", "Flare", "ゆらめく、フレア", "14th Century", "Origin uncertain, possibly imitative", "Burn with a sudden intensity", "沈黙（。の（。中（。で、一瞬（。だけ（。、「激（。しく（。煌（。め（。いた（。フレア）』、情熱の（。る（。る（。破片（。（。その（。峻（。烈（。な（。る（。一瞬にこそ（。、宇宙の（。全（。エナジーが（。、集約（。さ（。れ（。て（。いる（。のですよ。")
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
            word_id = f"{word_text.lower()}_wonder"
            
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
                    "thinking": item[6] if len(item) > 6 else "驚異とは、珍しいものを見ることではありません。当たり前だと思っていた日常の皮を剥ぎ取り、その奥にある深淵な光に気づくことなのです。",
                    "aftertaste": item[7] if len(item) > 7 else "奇跡は、待っている者の元には訪れない。不可能という名の壁を、自らの魂で何度も叩き続けた者の前にだけ、静かに拓かれる扉なのですよ。",
                    "example": f"The biological {word_text} that allowed the tiny seed to grow into a massive redwood tree baffled scientists for generations.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["息を吐くこと。それは、魂が世界と一体になるための、最も根源的なる祈りの形式なのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["glow", "flare"] else "verb"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Marvel & Miracle (Cycle 96).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
