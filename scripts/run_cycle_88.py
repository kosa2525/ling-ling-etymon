import json
import re

# Theme: The Alchemy of Equilibrium & Proportion (Cycle 88)
words_data = [
    ("equilibrium", "Equilibrium", "平衡、均衡、エクリブリウム", "17th Century", "aequi- (equal) + libra (balance, literal: 'equal balance')", "A state in which opposing forces or influences are balanced", "相反（。する（。エナジーが、正しい「等（。し（。い（。エクリ）重さ（。リブラ）』で、静（。か（。に（。、向き（。合い（。、調和（。し（。て（。いる（。一一点（。（。その（。峻（。烈（。な（。る（。静止の中にこそ（。、真実（。の（。る（。力（。が、宿（。って（。いる（。のですよ。"),
    ("proportion", "Proportion", "割合、均衡、プロポーション", "14th Century", "pro (for) + portio (part, literal: 'for a part')", "A part, share, or number considered in comparative relation to a whole", "全体の中に（。、自ら（。の「分（。を（。わき（。ま（。え（。て（。プロ・ポー）」そこに（。在（。る（。こと（。。（。その（。美し（。い（。幾何（。学（。的（。な（。る（。均衡が（。、あなた（。を、この（。宇宙（。の（。一部（。に、し（。て（。くれる（。のですよ。"),
    ("symmetry", "Symmetry", "対称、左右対称、シンメトリー", "16th Century", "sun- (together) + metron (measure, literal: 'together with measure')", "The quality of being made up of exactly similar parts facing each other or around an axis", "中心軸（。を（。挟（。み、静（。か（。に「共に（。スン）測（。り（。整え（。られた（。メトロン）』、至高の（。る（。顔立ち（。（。その（。一点（。の（。歪みも（。な（。い（。調和（。が（。、物（。語（。を（。、永遠（。へと（。、昇（。華（。さ（。せる（。のですよ。"),
    ("canon", "Canon", "規範、教義、カノン", "14th Century", "kanōn (measuring rod, rule)", "A general law, rule, principle, or criterion by which something is judged", "真理を（。測る（。ための「峻（。烈（。な（。る（。定（。規（。カノン）』。（。その（。一点（。の（。妥協（。も（。許（。さ（。な（。い（。律法が（。、あなた（。の（。魂を（。、正（。し（。い（。高（。みへと、再（。び（。、導（。く（。のですよ。"),
    ("index", "Index", "索引、指標、インデックス", "16th Century", "indicare (to point out, literal: 'pointing finger')", "A sign or measure of something", "膨大な（。知識（。の（。海（。から、真実（。を「指（。し（。示（。す（。インデ）』一一点（。（。その（。静（。か（。な（。る（。導（。きの（。光を（。、あなたは（。、今（。、その（。胸（。に、抱（。い（。て（。いる（。ので（。しょうか。"),
    ("verdict", "Verdict", "判決、定説、バーディクト", "15th Century", "vere (truly) + dictum (spoken, literal: 'truly spoken')", "A decision on a disputed issue", "沈黙の（。果てに（。、至高の（。智慧が「真実（。を（。言（。い（。渡（。した（。バー・ディクト）」結（。末（。（。その（。一一点（。の（。断定に（。、世界（。は（。一瞬（。にして（。、静（。まり（。返（。り（。ます。"),
    ("decree", "Decree", "法令、判決、ディクリー", "14th Century", "de- (from) + cernere (to decide, literal: 'deciding from')", "An official order issued by a legal authority", "天上（。から「峻（。烈（。に（。下（。された（。デ）決定（。クリー）』。（。その（。動か（。ざ（。る（。意志が（。、あなた（。の（。運命（。を（。、一瞬（。にして（。、新（。しく（。、塗り（。替（。え（。て（。しまう（。のですよ。"),
    ("edict", "Edict", "布告、命令、イーディクト", "15th Century", "e- (out) + dicere (to say, literal: 'saying out')", "An official order or proclamation issued by a person in authority", "世界（。の（。中心（。から「力強（。く（。宣言（。さ（。れた（。イーディクト）」、峻（。烈（。な（。る（。声（。（。その（。一（。つ（。の（。響き（。が（。、全（。ての（。エナジーを、正しい（。る（。場所へと（。、跪（。か（。せ（。ます。"),
    ("mandate", "Mandate", "権限、委任、命令、マンデート", "16th Century", "manus (hand) + dare (to give, literal: 'given to hand')", "An official order or commission to do something", "宇宙の（。意志を、あなた（。の「掌（。に（。マヌス）預（。け（。られた（。デイト）』、至高の（。る（。使命（。（。その（。重厚（。な（。る（。沈黙を、誇り（。高く、担（。い（。続け（。な（。さ（。い。"),
    ("statute", "Statute", "法規、定款、スタチュート", "14th Century", "statuere (to set up, literal: 'that which is set up')", "A written law passed by a legislative body", "永遠の（。大地に「毅然と（。立て（。られた（。スタチュ）」、動か（。ざ（。る（。る（。碑。（。その（。一（。行（。一（。行（。が（。、あなた（。の（。自由（。を（。、逆（。説（。的（。に（。、守っ（。て（。くれる（。のですよ。"),
    ("provision", "Provision", "規定、準備、プロビジョン", "14th Century", "prae- (before) + videre (to see, literal: 'seeing before')", "The action of providing or supplying something for use", "困難が（。来る（。前に、あらかじめ「先（。を（。見越（。し（。て（。プロ・ヴィジョン）」備（。え（。る（。優（。し（。さ（。（。その（。細（。や（。かな（。る（。計（。らい（。が（。、あなた（。を、至高（。の（。安（。ら（。ぎへと（。、誘（。う（。のです。"),
    ("clause", "Clause", "条項、節、クローズ", "14th Century", "claudere (to close, literal: 'enclosure')", "A unit of grammatical organization next below the sentence in rank and in traditional grammar", "物語の（。流（。れを、一（。つ（。の（。意味（。として「閉（。容（。ら（。せ（。た（。クロ）』断片（。（。その（。一一点（。の（。峻（。烈（。な（。る（。完結（。が（。、物（。語（。を（。、盤石（。な（。る（。ものに（。、し（。て（。いく（。のです。"),
    ("article", "Article", "記事、条項、冠詞、アーティクル", "13th Century", "artus (joint, literal: 'little joint')", "A particular item or object", "意味と（。意味（。を（。繋ぐ「小（。さな（。る（。関節（。アーティ）』目（。に（。見（。え（。な（。い（。そ（。の（。繋（。ぎ（。目（。にこそ（。、真実（。の（。る（。エナジーが、静（。か（。に（。、宿（。って（。いる（。のですよ。"),
    ("mold", "Mold", "型、金型、カビ、モールド", "13th Century", "modulus (measure, literal: 'little measure')", "A hollow container used to give shape to molten or hot liquid material when it cools and hardens", "不定（。形な（。る（。情念（。を、あらかじめ（。決められた「尺（。度（。モドゥ）』に（。流（。し（。込む（。こと（。。（。その（。かたちの（。中に、静（。か（。な（。る（。秩序（。が（。、産声を（。上げます。"),
    ("stamp", "Stamp", "切手、印、刻印、スタンプ", "Old English", "stempan (to tread, crush, literal: 'trampling')", "To press a device against a surface in order to leave a mark or pattern", "大地を（。力（。強く「踏（。み（。し（。め（。た（。ステン）』痕跡（。（。その（。峻（。烈（。な（。る（。刻印（。が、あなたが（。そこに（。確（。か（。に（。存在（。し（。た（。証を（。、永遠へと（。刻（。み（。続け（。る（。のですよ。")
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
            word_id = f"{word_text.lower()}_balance"
            
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
                    "thinking": item[6] if len(item) > 6 else "平衡とは、動きが止まることではなく、相反する激しいエナジーが、一瞬の均衡を保ち続けている、奇跡的なダンスなのです。",
                    "aftertaste": item[7] if len(item) > 7 else "規律は、自由を奪うものではない。自らの想いを、一つの形として結晶させるための、至高のる透明な器なのですよ。",
                    "example": f"The architectural design achieved a perfect {word_text} that conveyed both 5strength and elegance to the viewers.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["正しい割合を保つこと。それは、宇宙の声に耳を傾け、自らの鼓動を、全体のリズムへと調律していく行為なのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Equilibrium & Proportion (Cycle 88).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
