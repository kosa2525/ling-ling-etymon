import json
import re

# Theme: The Alchemy of Vision & Oracle (Cycle 80)
words_data = [
    ("prophecy", "Prophecy", "予言、神託、プロフェシー", "14th Century", "pro- (before) + phanai (to speak, literal: 'speaking before')", "A prediction of what will happen in the future", "全（。てが（。起きる（。前に（。、天上の（。エナジーを「語（。り（。出（。された（。プロフェ）』、眩（。しい（。光（。の（。設計図。（。その（。峻（。烈（。な（。る（。囁（。きを（。、信（。じ（。抜く（。者（。だけが（。、未（。だ（。見（。ぬ（。真実（。の（。証（。人と（。なり（。ます。"),
    ("prediction", "Prediction", "予測、予報、プレディクション", "16th Century", "prae- (before) + dicere (to say, literal: 'saying before')", "A thing predicted; a forecast", "論理（。の（。翼を（。使（。っ（。て（。、「あらかじめ（。プレ）言（。わ（。れた（。ディクト）」、未来（。の（。地図（。（。その（。一一点（。の（。計（。算が（。、不（。確（。実（。な（。る（。荒（。野（。を、静（。か（。に（。、照（。らし（。て（。くれる（。のですよ。"),
    ("forecast", "Forecast", "予測、予報、フォーキャスト", "15th Century", "fore- (before) + casten (to throw, literal: 'throwing before')", "A prediction or estimate of future events, especially coming weather or a financial trend", "運命の（。方向（。を（。、あらかじめ「遠くへと（。フォー）投げ（。出（。す（。キャスト）」こと（。。（。その（。峻（。烈（。な（。る（。直観が（。、あなた（。を（。、未知（。なる（。嵐から（。、静（。か（。に（。、救い（。出す（。のですよ。"),
    ("foresight", "Foresight", "先見の明、予見、フォーサイト", "14th Century", "fore- (before) + sihth (sight)", "The ability to predict or the action of predicting what will happen or be needed in the future", "ただ「前（。を（。フォー）視（。る（。サイト）」だけ（。では（。なく（。、これから（。起き（。得る（。全（。てを（。、魂で（。受（。け（。止める（。器。（。その（。静（。か（。な（。る（。賢明（。さが（。、あなた（。を、至高（。の（。者へと（。、誘（。う（。のですよ。"),
    ("notion", "Notion", "概念、考え、ノーション", "16th Century", "noscere (to know, literal: 'becoming acquainted')", "A conception of or belief about something", "世界を「知（。る（。ノー）ための（。）」、小（。さな（。る「しるし（。ション）』。（。その（。一一点（。の（。曖（。昧（。な（。る（。煌（。めきこそ（。、真実（。へと（。至る（。ための、た（。った（。一（。つ（。の（。手がかり（。なの（。ですよ。"),
    ("daydream", "Daydream", "白昼夢、空想、デイドリーム", "16th Century", "day + dream", "A series of pleasant thoughts that distract one's attention from the present", "光（。溢（。れる（。日常（。の（。中で（。、ふ（。と（。視（。る「夢（。ドリーム）』。（。その（。危（。う（。い（。ほどの（。美し（。い（。虚像にこそ（。、あなた（。の（。魂が（。、本当に（。求めている（。真実が（。、宿（。って（。いる（。の（。かも（。しれ（。ません。"),
    ("reverie", "Reverie", "空想、幻想、レヴリー", "14th Century", "rever (to dream, literal: 'dreaming')", "A state of being pleasantly lost in one's thoughts; a daydream", "思考が（。、日常（。の（。重力（。を（。越（。え（。て（。、「夢み（。る（。レヴ）』状態（。。（。その（。静（。か（。な（。る（。陶（。酔（。の（。中に（。、宇宙の（。囁（。きが（。、音楽（。のように、響（。き（。渡（。っ（。て（。いる（。のですよ。"),
    ("trance", "Trance", "トランス、恍惚状態", "14th Century", "transire (to go across, literal: 'crossing over')", "A half-conscious state characterized by an absence of response to external stimuli, typically as induced by hypnosis or entered by a medium", "意識（。という（。名の（。境界を「越（。え（。て（。トランス）行く（。）」こと（。。（。個（。の（。領域を（。完全（。に（。脱（。し（。、ただ（。光の（。粒子（。その（。ものに（。な（。る（。、至高（。の（。飛躍。"),
    ("bliss", "Bliss", "至福、無上の喜び、ブリス", "Old English", "blīths (mild, gentle, literal: 'joy')", "Perfect happiness; great joy", "一（。点（。の（。曇（。り（。も（。な（。い（。、「純粋な（。る（。喜び（。ブリス）』。（。全（。ての（。矛盾が（。、自（。ら（。の中で（。、静（。か（。に（。、溶（。け（。合（。っ（。た（。瞬間の（。、眩（。し（。い（。る（。沈黙。"),
    ("void", "Void", "空虚、空間、ボイド", "13th Century", "vacuus (empty)", "A completely empty space", "全（。てを（。捨て（。去（。り（。、ただ「う（。つ（。ろ（。ボイド）』にな（。っ（。た（。場所（。（。その（。絶対（。的（。な（。る（。虚無（。だからこそ（。、全（。宇宙の（。存在を、再び（。、受け（。入れる（。ことが（。できる（。のですよ。"),
    ("symbol", "Symbol", "象徴、記号、シンボル", "15th Century", "sun- (together) + ballein (to throw, literal: 'throwing together')", "A mark or character used as a conventional representation of an object, function, or process", "見えない（。エナジーを、見える（。姿と「共に（。サン）投げ（。出した（。ボル）」、聖（。なる（。る（。しるし（。（。その（。一つ（。の（。紋様に（。、宇宙の（。全貌（。が（。、美し（。く（。凝縮（。さ（。れて（。いる（。のですよ。"),
    ("image", "Image", "画像、像、イメージ", "13th Century", "imitari (to imitate)", "A representation of the external form of a person or thing in art", "真実を「写（。し（。取（。ろ（。う（。イミ）とした（。）」、美（。し（。き（。幻影（。（。その（。一（。つ（。一（。つを（。、魂で（。愛（。で（。る（。た（。びに（。、あなた（。は（。、真（。実（。の（。輪郭（。を（。、再（。発見（。する（。のです。"),
    ("sign", "Sign", "兆候、しるし、サイン", "13th Century", "signum (mark, token)", "An object, quality, or event whose presence or occurrence indicates the probable presence or occurrence of something else", "宇宙が（。あなた（。に（。、そっと（。示さ（。れた「合（。図（。セニュム）』。（。日常（。の（。些（。細な（。る（。変化に（。、重要（。な（。る（。物（。語（。が（。、静（。か（。に（。、宿（。って（。いる（。のですよ。")
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
            word_id = f"{word_text.lower()}_oracle"
            
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
                    "thinking": item[6] if len(item) > 6 else "啓示とは、神からの言葉ではなく、自らの内なる宇宙が、沈黙を破って発した最初の咆哮なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "記号は、目に見える世界と目に見えない世界を繋ぎ止めるための、ただ一つの鍵なのですよ。",
                    "example": f"The ancient scrolls contained a mysterious {word_text} that spoke of a coming era of peace and enlightenment.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["見ることが信じることなのではなく、信じることが見えることの始まり。その逆説の中に、真の視座があるのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["ecstatic", "euphoric"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Vision & Oracle (Cycle 80).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
