import json
import re

word_batch = [
    # Cycle 85: Mystery & The Unknown
    {
        "id": "enigma_mystery",
        "word": "Enigma",
        "meaning": "謎、不可解なもの、エニグマ",
        "era": "16th Century Greek ainigma",
        "etymology": {
            "components": ["ainos (fable, riddle, tale)"],
            "original_statement": "From Latin aenigma, from Greek ainigma (a dark saying, riddle), from ainissesthai (to speak in riddles), from ainos (fable, riddle, speech)."
        },
        "concept": "Speaking in riddles (寓話やなぞなぞとして「語る（speak）」、正体不明のもの)",
        "thinking": "答えを隠した問いそのものとして、そこに存在すること。語源の ainos は「寓話」であり、表面的な意味の背後に、より深く、より解読困難な真実が潜んでいることを示唆します。解こうとすればするほど深まる謎。それは、世界が持つ「底知れなさ」への敬意の別名です。",
        "aftertaste": "微笑む問い。あなたはそれを解くことはできない。ただ、その美しき不可解さの前で立ち止まることしか。",
        "example": "His sudden disappearance remains an enigma that investigators are still trying to solve.",
        "deep_dive": { "roots": [{"term": "Unknown source"}], "points": ["暗号機『エニグマ』の名の由来。解読されることを拒む、沈黙の知性。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "abyss_mystery",
        "word": "Abyss",
        "meaning": "底知れぬ深い穴、深淵、混沌",
        "era": "14th Century Greek a- + byssos",
        "etymology": {
            "components": ["a- (without)", "byssos (bottom)"],
            "original_statement": "From Late Latin abyssus, from Greek abyssos (bottomless), from a- (without) + byssos (bottom, bottom of the sea)."
        },
        "concept": "Bottomless (「底（bottom）」が「ない（without）」、果てしない暗闇)",
        "thinking": "どれだけ深い知恵の光を投げ入れても、決して底に届かない場所。それは恐怖の対象であると同時に、あらゆるものが生まれてくる原初的な「混沌（Chaos）」でもあります. 深淵（abyss）を覗き込むとき、深淵もまたあなたを覗き込んでいる。そこには、絶対的な他者としての宇宙が口を開けています。",
        "aftertaste": "終わりのない落下。けれど、底がないということは、あなたは永遠に『自由』のなかに浮遊しているということでもある。",
        "example": "Standing on the edge of the canyon, he looked down into the dark abyss below.",
        "deep_dive": { "roots": [{"term": "Unknown source"}], "points": ["byssos はヘブライ語やシュメール語に由来するという説もあり、古の海への畏怖が刻まれている。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "cryptic_mystery",
        "word": "Cryptic",
        "meaning": "隠れた、神秘的な、謎めいた",
        "era": "17th Century Greek kryptos",
        "etymology": {
            "components": ["kryptos (hidden, concealed)"],
            "original_statement": "From Late Latin crypticus, from Greek kryptikos, from kryptos (hidden, concealed)."
        },
        "concept": "Hidden away (人目に触れないように「隠された（hidden）」状態)",
        "thinking": "地下室（crypt）に隠された宝物のように、意図的に、あるいは本質的に「秘められている」こと。それは単に「秘密」なのではなく、解読するための「鍵」を必要とする知的な挑戦です。世界があなたに送っている暗号メッセージ。その意味を読み解くのは、あなたという受信者だけです。",
        "aftertaste": "秘密の部屋。閉じられた扉の向こう側で、真実はあなたが鍵を差し込むその瞬間を待っている。",
        "example": "He left a cryptic note on the table before leaving the house at midnight.",
        "deep_dive": { "roots": [{"term": "kra-", "meaning": "to hide"}], "points": ["crypt（地下聖堂）や cryptography（暗号学）と同じ。隠すことは、守ることでもある。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "arcane_mystery",
        "word": "Arcane",
        "meaning": "秘密の、難解な、不可解な",
        "era": "16th Century Latin arca",
        "etymology": {
            "components": ["arca (chest, box, source of secret)"],
            "original_statement": "From Latin arcanus (secret, hidden, private), from arcere (to shut up, enclose), from arca (chest, box)."
        },
        "concept": "Inside a chest (「箱（chest）」の中に閉じ込められ、限られた者にしか知らされないこと)",
        "thinking": "選ばれた少数の専門家や修行者にしか理解できない、古（いにしえ）の知恵や儀式。それは単なる「難しい知識」ではなく、箱の中に守られ、汚されることを拒む「神聖な秘密」です。それを知ることは、特別な領域へと足を踏み入れる「許可」を得ることに等しいのです。",
        "aftertaste": "守られた智慧. 箱を開ける者は、その知識の重みに耐えうる魂を持たねばならない。",
        "example": "The professor's lecture on arcane medieval rituals fascinated the small group of students.",
        "deep_dive": { "roots": [{"term": "ark-", "meaning": "to hold, contain, guard"}], "points": ["ark（聖櫃：方舟）や archive（記録保管所）同じ『守る箱』のルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "occult_mystery",
        "word": "Occult",
        "meaning": "神秘的な、超自然的な、隠された",
        "era": "16th Century Latin ob- + celare",
        "etymology": {
            "components": ["ob- (over)", "celare (to hide)"],
            "original_statement": "From Latin occultus (hidden, concealed, secret), past participle of occulere (cover over, conceal), from ob- (over) + a derivative of the root of celare (to hide)."
        },
        "concept": "Hidden over (上から蓋をして「隠し（hide）」ていること、目に見えない領域)",
        "thinking": "五感で捉えられる物理的な世界の背後（あるいは上方）に隠されている、超自然的な力や法則。語源の celare は「隠す」であり、暗闇を意味します。目に見えるものがすべてではないという、この世界に対する謙虚な認識、あるいは目に見えない次元への積極的な探求心の表明です。",
        "aftertaste": "不可視の力. あなたの背後で、目に見えない幾千の糸が、運命という機織りを進めている。",
        "example": "He had a lifelong interest in the occult and studied ancient esoteric texts.",
        "deep_dive": { "roots": [{"term": "kel-", "meaning": "to hide"}], "points": ["cell（小部屋）や conceal（隠す）、hell（隠された場所/冥府）と同じ『隠蔽』の系譜。"] },
        "part_of_speech": "adjective"
    }
]

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
    if match:
        prefix, json_array_str, suffix = match.groups()
        words = json.loads(json_array_str)
        existing_ids = {w.get("id") for w in words}
        
        added = 0
        for item in word_batch:
            if item["id"] not in existing_ids:
                words.append(item)
                added += 1
        
        new_content = content[:match.start()] + prefix + json.dumps(words, ensure_ascii=False, indent='\t') + suffix + content[match.end():]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Success: Added {added} words in Cycle 85.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
