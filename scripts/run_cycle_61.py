import json
import re

# Theme: The Alchemy of Paradox & Truth (Cycle 61)
words_data = [
    ("satire", "Satire", "風刺、皮肉、サタイア", "16th Century", "satura (mixture, literal: 'full dish')", "The use of humor, irony, exaggeration, or ridicule to expose and criticize people's stupidity or vices, particularly in the context of contemporary politics and other topical issues", "真実を（。その（。まま（。語（。る（。のを（。止め（。、笑（。い声と（。いう（。名の「混（。ぜ（。合（。わ（。せ（。サトゥス）」で（。煮（。込（。む（。こと（。。（。その（。鋭（。い（。味（。覚が（。、淀（。んだ（。社会（。に（。、静（。か（。な（。る（。風（。穴を（。空（。ける（。のですよ。"),
    ("parody", "Parody", "パロディ、模倣、滑稽な作り替え", "16th Century", "para- (beside) + oide (song, literal: 'beside-song')", "An imitation of the style of a particular writer, artist, or genre with deliberate exaggeration for comic effect", "既（。に（。ある「歌（。アイデ）の（。隣（。パラ）に（。）」、あえて（。歪（。んだ（。鏡（。を（。置く（。こと（。。（。その（。滑（。稽（。な（。ずれ（。の中にこそ（。、人間（。の（。真（。実（。の（。愛（。お（。し（。さが（。、浮（。き（。彫（。りに（。なり（。ます。"),
    ("emblem", "Emblem", "象徴、紋章、エンブレム", "15th Century", "em- (in) + ballein (to throw, literal: 'thrown in, inlaid')", "A heraldic device or symbolic object as a distinctive badge of a nation, organization, or family", "内（。側に（。烈（。しい（。情熱を「投（。げ（。込（。み（。エンバル）」、静（。止さ（。せた（。かたち（。。（。その（。一（。点（。の（。図（。案（。に、宇宙（。の（。全エナジー（。を（。封印（。した（。、誇（。り（。高い（。証（。なのです。"),
    ("token", "Token", "しるし、代用貨幣、トークン", "Old English", "tācen (sign, symbol, literal: 'to teach')", "A thing serving as a visible or tangible representation of a fact, quality, feeling, etc.", "言葉（。を（。超え（。て（。、何かを「知（。ら（。し（。める（。トーカン）」ための（。、小（。さな（。欠片（。。（。そ（。の（。一（。つ（。を（。手（。渡（。す（。とき（。、あなた（。の（。真（。実（。の（。想（。いが（。、静（。か（。に（。、相手に（。届（。く（。のですよ。"),
    ("signal", "Signal", "信号、合図、シグナル", "16th Century", "signum (mark, token)", "A gesture, action, or sound that is used to convey information or instructions, typically by prearrangement between the parties concerned", "宇宙（。の（。沈黙（。を（。打ち（。破（。り（。、ただ「しるし（。シグナ）」として（。放た（。れた（。エナジー。（。その（。鋭（。い（。瞬（。きだけが（。、決定（。的な（。瞬間（。を（。、あなた（。に（。教えて（。くれる（。のですよ。"),
    ("indicator", "Indicator", "指標、計器、インジケーター", "17th Century", "in- (towards) + dicare (to proclaim, literal: 'point out')", "A thing that indicates the state or level of something", "真実を（。指（。し「示（。す（。ジク）」ための（。、静（。かな（。る（。指（。先（。。（。あなた（。の（。内（。なる（。計器が（。、今（。どこ（。を（。見つめて（。いる（。か（。、それ（。だけを（。最後（。まで（。信じ（。て（。あげて（。ください。"),
    ("index", "Index", "索引、指標、インデックス", "14th Century", "in- (towards) + deik- (to show, literal: 'forefinger')", "An alphabetical list of names, subjects, etc., with references to the places where they occur, typically found at the end of a book", "巨大な（。物語の中から（。、真理を「指（。し（。し（。め（。す（。ディク）」ための（。人（。差し（。指（。。（。その（。一（。行（。一（。行を（。辿（。る（。ことで（。、あなた（。は（。、自分（。の（。中（。にある（。真実（。の（。頁に（。辿（。り（。着（。く（。のです。"),
    ("prototype", "Prototype", "原型、試作品、プロトタイプ", "16th Century", "protos (first) + tupos (type, model)", "A first, typical or preliminary model of something, especially a machine, from which other forms are developed or copied", "全（。て（。において「最初（。プロト）に（。打ち（。立（。て（。られた（。タイプ）」光（。。（。不（。完（。全（。だからこそ（。、そこ（。には（。、未（。だ（。何者（。にも（。汚さ（。れ（。て（。い（。ない（。、純粋（。な（。る（。エナジーが（。宿（。って（。いる（。のです。"),
    ("doctrine", "Doctrine", "教義、主義、ドクトリン", "14th Century", "docere (to teach)", "A belief or set of beliefs held and taught by a church, political party, or other group", "ただ（。の（。知識（。ではなく（。、魂を「導く（。ドク）ための（。教え（。）」。（。その（。峻（。烈（。な（。る（。規範（。の中（。に、自（。ら（。を（。投（。じ（。る（。ことで（。、あなた（。は（。、一（。人（。では（。辿（。り（。着（。け（。ない（。高（。みへと（。至（。る（。のです。"),
    ("creed", "Creed", "信条、クリード", "Old English", "credo (I believe, literal: 'cor' heart + 'do' place, 'place my heart')", "A system of Christian or other religious belief; a faith", "自分（。の「心（。コル）を（。そこに（。置く（。ド）」こと（。。（。何を（。信（。じ（。る（。か（。、それ（。が（。あなた（。の（。魂の（。座（。標を（。、永遠（。に（。決定（。づける（。のですよ。"),
    ("skepticism", "Skepticism", "懐疑主義、スケプティシズム", "17th Century", "skeptikos (thoughtful, literally: 'to look out')", "A skeptical attitude; doubt as to the truth of something", "ただ（。信じる（。のを（。止め（。、真実を「じっと（。見つめ（。スケプ）続け（。る（。）」こと（。。（。その（。冷（。徹（。な（。る（。疑（。い（。だけが（。、偽（。り（。の（。光を（。剥（。ぎ（。取（。り（。、真（。実（。の（。輝きを（。、あぶり（。出す（。のです。"),
    ("sarcasm", "Sarcasm", "皮肉、嫌味、サーカズム", "16th Century", "sarkasmos (sneer, literally: 'to strip off flesh')", "The use of irony to mock or convey contempt", "言葉の（。仮面を（。剥ぎ取り（。、む（。き（。出し（。の「肉（。サルカス）を（。露（。わ（。に（。する（。）」ような（。、峻烈（。な（。る（。嘲（。笑（。。（。その（。痛み（。を（。、真実（。を（。直視（。するための（。、エナジーへと（。変（。えて（。ください。"),
    ("sophist", "Sophist", "詭弁家（きべんか）、ソフィスト", "15th Century", "sophizesthai (to become wise)", "A paid teacher of philosophy and rhetoric in ancient Greece, associated in popular thought with specious reasoning", "あから（。さま（。な（。正解ではなく（。、言葉（。を（。操る（。ことで「賢（。く（。見（。え（。る（。ソフィ）者（。）」。（。論理（。の（。迷宮を（。渡る（。ときは（。、常に（。、その（。虚飾（。の（。裏側（。を（。見（。抜（。いて（。ください。"),
    ("paradox", "Paradox", "逆説、パラドックス", "16th Century", "para- (contrary to) + doxa (opinion)", "A seemingly absurd or self-contradictory statement or proposition that when investigated or explained may prove to be well founded or true", "一般（。的な「常識（。ドクサ）の（。横へと（。パラ）外れる（。）」こと（。。（。その（。矛盾（。の（。中に（。、言葉（。では（。到底（。語（。り（。尽（。く（。せ（。ない（。、巨大（。な（。真実（。が（。、静（。か（。に（。息づいて（。いる（。のですよ。"),
    ("irony", "Irony", "皮肉、アイロニー", "16th Century", "eironeia (dissimulation, literal: 'dissembler in speech')", "The expression of one's meaning by using language that normally signifies the opposite, typically for humorous or emphatic effect", "本当（。の（。こと（。を（。直（。接（。語る（。のを（。止め（。、あえて「無知（。を（。装う（。エイロン）」こと（。。（。その（。沈黙（。と（。言葉の（。ずれの（。中に（。、最高（。の（。知性（。の（。飛躍が（。宿（。って（。いる（。の（。ですよ。")
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
                    "thinking": item[6] if len(item) > 6 else "真実は、常に矛盾という名の美しいドレスを纏って、私たちの前に現れるのです。",
                    "aftertaste": item[7] if len(item) > 7 else "言葉は、真実を語るための道具ではなく、真実がそこにあることを示すための、たった一つの指先なのです。",
                    "example": f"The author uses {word_text} to reveal the hidden complexities of human nature.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["信じることと疑うことは、一枚のコインの表裏であり、どちらが欠けても、真実へと辿り着くことはできません。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["paradoxical", "ironic"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Paradox & Truth (Cycle 61).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
