import json
import re

# Theme: The Alchemy of Reason & Emotion (Cycle 49)
words_data = [
    ("objective", "Objective", "客観的な、目的", "17th Century", "ob- (against) + jacere (to throw)", "Of a person or their judgment not influenced by personal feelings or opinions in considering and representing facts", "自（。らの（。感情（。を（。横に（。置き（。、真実を（。自分（。の「目の（。前へと（。オブ）投げ（。出す（。ジェ）」こと（。。（。偏（。り（。の（。ない（。透明な（。瞳が（。、世界を（。あり（。の（。ままに（。映（。し（。出（。す。"),
    ("subjective", "Subjective", "主観的な、主観の", "15th Century", "sub- (under) + jacere (to throw)", "Based on or influenced by personal feelings, tastes, or opinions", "世界を（。自分（。の「足下（。サブ）へと（。投げ（。込む（。ジェ）」こと（。。（。あなた（。に（。しか（。見えない（。色彩（。や（。熱（。が（。、世界に（。命を（。吹き（。込む（。、唯一（。無二（。の（。物語。"),
    ("abstract", "Abstract", "抽象的な、抽出する", "14th Century", "ab- (away) + trahere (to draw)", "Existing in thought or as a idea but not having a physical or concrete existence", "具体（。的な（。かたち（。を（。捨（。て（。去（。り（。、「本質（。だけ（。を（。遠（。くへと（。アブ）引き（。出（。し（。トラ）た（。）」もの（。。（。目（。には（。見えない（。けれど（。、確（。かに（。世界を（。支（。えて（。いる（。、純粋（。な（。る（。概念。"),
    ("concrete", "Concrete", "具体的な、コンクリート", "14th Century", "com- (together) + crescere (to grow)", "Existing in a material or physical form; real or solid", "バラバラ（。の（。エナジーが（。、「共に（。コン）育（。ち（。クレ）固（。ま（。った（。）」もの（。。（。触（。れる（。ことが（。できる（。重厚（。な（。存在感（。が（。、精神の（。大地を（。形（。作（。る（。のですよ。"),
    ("dualism", "Dualism", "二元論、二元性", "18th Century", "duo (two)", "The division of something conceptually into two opposed or contrasted aspects, or the state of being so divided", "全（。て（。を「二（。つ（。デュオ）」に（。分（。け（。て（。考え（。よう（。とする（。、知性の（。誘惑（。。（。光（。と（。影（。、善（。と（。悪（。の（。狭（。間（。で（。、私たちは（。常に（。揺（。れ（。動き（。ながら（。真実を（。求（。める（。のですよ。"),
    ("monism", "Monism", "一元論", "19th Century", "monos (single, alone)", "A theory or doctrine that denies the existence of a distinction or duality in some sphere, such as that between matter and mind, or God and the world", "二（。つの（。側面（。を（。越（。え（。、全（。ては「一（。つ（。モノ）である」と（。信（。じる（。こと（。。（。宇宙の（。深淵（。なる（。沈黙（。の中に（。、全（。ての（。矛盾（。を（。溶（。かし（。去（。る（。、静（。かな（。る（。調和。"),
    ("stoicism", "Stoicism", "ストイシズム、禁欲的", "14th Century", "stoa (porch)", "The endurance of pain or hardship without a display of feelings and without complaint", "かつて「柱（。廊（。ストア）」の下で（。、哲学者（。たちが（。静（。かに（。真理を（。説（。い（。た（。こと（。を（。記憶（。する（。言葉（。。（。運命の（。荒波に（。翻（。弄（。さ（。れ（。ず（。、ただ（。自（。ら（。の（。内（。側（。を（。律（。する（。、誇（。り（。高い（。孤独。"),
    ("nihilism", "Nihilism", "ニヒリズム、虚無主義", "19th Century", "nihil (nothing)", "The rejection of all religious and moral principles, in the belief that life is meaningless", "全（。て（。の（。意味（。や（。価値（。を（。捨て（。去（。り（。、「無（。ニヒル）」の（。深淵（。を（。見つめる（。こと（。。（。その（。絶（。望（。の（。果（。てにのみ（。、真（。実（。の（。自由（。が（。芽吹（。く（。の（。かも（。しれ（。ません。"),
    ("rationalism", "Rationalism", "合理主義、理性主義", "17th Century", "ratio (reason, literal: 'reckoning, account')", "A belief or theory that opinions and actions should be based on reason and knowledge rather than on religious belief or emotional response", "感情（。の（。揺（。ら（。ぎを（。捨て（。、ひたすら「計算（。比率（。ラシオ）」に（。よって（。世界（。を（。解（。き（。明か（。そう（。とする（。、冷（。徹（。な（。る（。知性の（。牙。"),
    ("empiricism", "Empiricism", "経験論、経験主義", "17th Century", "em- (in) + peira (trial, experiment)", "The theory that all knowledge is derived from sense-experience", "抽象（。的な（。理屈を（。信じ（。ず（。、自ら（。の（。身体で「試みる（。経験（。ペイラ）こと（。を（。信（。じ（。る（。）」こと（。。（。泥（。に（。まみれ（。、汗を（。流（。して（。得（。た（。実（。感（。だけが（。、真（。実（。の（。力と（。なる（。のです。"),
    ("axiom", "Axiom", "公理、自明の理、アクシオム", "15th Century", "axios (worthy)", "A statement or proposition which is regarded as being established, accepted, or self-evidently true", "証明（。を（。必要（。と（。し（。ない（。、それ自身が「価値（。ある（。アキ）正しい（。）」もの（。として（。置（。かれた（。出発点（。。（。あなた（。の（。魂が（。信（。じ（。て（。離（。さ（。ない（。、揺（。る（。ぎ（。ない（。第一（。原理。"),
    ("fallacy", "Fallacy", "誤謬（ごびゅう）、謬説", "15th Century", "fallere (to deceive)", "A mistaken belief, especially one based on unsound argument", "真実（。の（。ように（。見え（。て（。、実は（。思考の（。罠（。によって「欺（。く（。ファラ）もの（。）」。（。甘（。い（。誘（。惑（。に（。満（。ち（。た（。論理の（。歪（。みに（。、気づ（。ける（。誠実（。さを（。持（。って（。ください。"),
    ("synthesis", "Synthesis", "総合、合成、シンセシス", "17th Century", "sun- (together) + tithenai (to place, put)", "The combination of ideas to form a theory or system", "二（。つの（。対（。立（。する（。要素（。を（。、より（。高い（。次元で「共（。に（。サン）置（。く（。セシス）」こと（。。（。矛盾（。を（。受け（。入れ（。、全（。く（。新（。しい（。真（。実（。を（。産（。み（。出す（。、知性の（。錬金術。"),
    ("dialectic", "Dialectic", "弁証法、対話術", "14th Century", "dia- (across, between) + legein (to speak)", "The art of investigating or discussing the truth of opinions", "ただの（。議論（。を（。越（。え（。、相手（。と（。自（。らの（。間（。を「言葉（。レゲ）が（。飛び交（。う（。ディ）」こと（。。（。対立を（。糧（。に（。して（。、共（。に（。未知（。なる（。高（。み（。へと（。昇（。って（。いく（。プロセス。"),
    ("analog", "Analog", "アナログ、相似のもの", "19th Century", "ana- (according to) + logos (word, reason, ratio)", "A person or thing seen as comparable to another", "デジタル（。の（。不連続（。性を（。拒（。み（。、「ことば（。ロゴス）に従（。って（。アナ）」、滑（。らかに（。繋（。が（。る（。連続（。体（。。（。そこ（。には（。、曖昧（。さという（。名の（。、無限（。の（。豊（。かさが（。宿（。って（。いる（。の（。ですよ。")
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
            word_id = f"{word_text.lower()}_reason"
            
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
                    "concept": item[5] + f" ({item[6]})",
                    "thinking": item[6],
                    "aftertaste": item[7] if len(item) > 7 else "理性は、感情という名の荒波を渡るための、唯一の羅針盤なのです。",
                    "example": f"The philosopher argued that human {word_text} is flawed and limited by our senses.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["客観とは、世界を他人の目線で見るのではなく、愛を持って世界を突き放すことなのです。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["objective", "subjective", "abstract", "concrete", "stoic"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Reason & Emotion (Cycle 49).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
