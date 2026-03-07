import json
import re

# Theme: The Alchemy of Introspection & Void (Cycle 66)
words_data = [
    ("introspection", "Introspection", "内省（ないせい）、自己観察", "17th Century", "intro- (into) + specere (to look)", "The examination or observation of one's own mental and emotional processes", "外部の（。喧（。騒（。を（。止（。め（。、「内（。側を（。イントロ）見（。つ（。め（。る（。スペク）」こと（。。（。その（。鏡（。のような（。静（。止（。の中に、あなた（。の（。魂の（。本（。質（。が（。、静（。か（。に（。、浮（。き（。彫（。りに（。なり（。ます。"),
    ("subconscious", "Subconscious", "潜在意識（。せんざいいしき（。）」、サブラシャス", "19th Century", "sub- (under) + conscius (knowing, aware)", "Of or concerning the part of the mind of which one is not fully aware but which influences one's actions and feelings", "意識の（。光が（。届（。か（。な（。い「下（。側（。に（。サブ）隠（。れ（。た（。知（。覚（。シャス）」。（。そこ（。には（。、未（。だ（。言葉に（。なら（。ない（。巨大な（。エナジーが（。、静（。か（。に（。、横（。たわ（。って（。いる（。のですよ。"),
    ("unconscious", "Unconscious", "無意識（。むいしき（。）」、アンコンシャス", "18th Century", "un- (not) + conscius (knowing)", "Not conscious; especially done or existing without one's realizing", "ただ（。「知（。ら（。な（。い（。アン、コン）」だけ（。では（。なく（。、自（。分（。を（。動か（。して（。いる（。、もう（。一（。人の（。自分（。の（。存在（。。（。その（。深（。淵（。の（。深（。さにこそ（。、真（。の（。自由が（。眠（。って（。いる（。のですよ。"),
    ("repressed", "Repressed", "抑圧（。よくあつ（。）」された、リプレスト", "17th Century", "re- (back) + premere (to press, literal: 'pressed back')", "Oppressed or inhibited", "表（。に（。出（。よう（。と（。する（。想いを「後ろへ（。リ）押（。し（。込（。め（。る（。プレス）」こと（。。（。抑（。え（。込（。まれた（。エナジーは（。、いつか（。美し（。い（。芸術へと（。、昇（。華（。さ（。せる（。べき（。、聖なる（。種（。子（。なのです。"),
    ("inhibition", "Inhibition", "抑制、禁忌、インヒビション", "14th Century", "in- (in) + habere (to hold, literal: 'holding in')", "A feeling that makes one self-conscious and unable to act in a relaxed and natural way", "自（。ら（。の「内（。側（。イン）に（。留（。め（。置（。く（。ハビ）」こと（。。（。その（。戒（。めが（。ある（。から（。こそ（。、あなた（。の（。表現（。は（。、一（。き（。わ（。、峻（。烈（。な（。る（。気高さ（。を（。放（。つの（。ですよ。"),
    ("euphoria", "Euphoria", "幸福感、多幸感、ユーフォリア", "17th Century", "eu- (well) + pherein (to bear, literal: 'bearing well')", "A feeling or state of intense excitement and happiness", "全（。て（。の（。重力を（。忘（。れ（。、「良（。い（。ユー）状態（。を（。運（。ぶ（。フォリア）」こと（。。（。その（。眩（。し（。い（。陶（。酔（。の（。中に（。、宇宙（。の（。全（。てとの（。調和を（。、感（。じる（。ことが（。できる（。のですよ。"),
    ("ecstasy", "Ecstasy", "忘我、狂喜、エクスタシー", "14th Century", "ek- (out) + histanai (to stand, literal: 'standing outside')", "An overwhelming feeling of great happiness or joyful excitement", "自分（。という（。名の（。檻の「外（。エク）に（。立つ（。スタ）」こと（。。（。個（。の（。領域を（。完全（。に（。脱（。し（。、ただ（。光（。その（。もの（。に（。なる（。、至高（。の（。飛躍。"),
    ("equanimity", "Equanimity", "平静、落ち着き、エクアニミティ", "17th Century", "aequux (equal) + animus (mind)", "Mental calmness, composure, and evenness of temper, especially in a difficult situation", "どんな（。嵐の（。中でも、「平等（。平等（。な（。エクア）心（。アニムス）」を（。保（。つ（。こと（。。（。その（。一点（。の（。静寂が（。、世界（。の（。大（。混（。沌（。を（。、調和へと（。導（。く（。のですよ。"),
    ("fortitude", "Fortitude", "不屈の精神、堅忍（。けんにん（。）」、フォーティチュード", "14th Century", "fortis (strong)", "Courage in pain or adversity", "ただの（。強さ（。ではなく（。、困難（。な（。季節（。を「強（。い（。フォルティ）意思」で（。、耐え（。抜（。く（。こと（。。（。その（。折（。れ（。な（。い（。魂（。が（。、あなたを（。、新た（。な（。る（。勝利へと（。、誘（。う（。のですよ。"),
    ("fervor", "Fervor", "熱烈、情熱、ファーバー", "14th Century", "fervere (to boil)", "Intense and passionate feeling", "心（。の（。底から（。魂を「沸（。き（。立（。た（。せ（。る（。ファーヴ）」こと（。。（。その（。烈（。し（。い（。熱量（。だけが（。、不可能（。を（。可能（。にし（。、世界を（。、一変（。さ（。せる（。ことが（。でき（。る（。のですよ。"),
    ("zeal", "Zeal", "熱意、献身、ジール", "14th Century", "zelos (jealousy, fervor, literal: 'boiling')", "Great energy or enthusiasm in pursuit of a cause or an objective", "静（。かな（。る「沸（。騰（。ゼロス）』を（。持（。っ（。て（。、一点（。を見（。つめる（。こと（。。（。あなた（。の（。その（。純粋（。な（。る（。献身（。が（。、閉（。ざ（。された（。門（。を（。、静（。か（。に（。、開（。ける（。のですよ。"),
    ("benevolence", "Benevolence", "慈愛、善行、ベネボレンス", "14th Century", "bene (well) + velle (to wish, literal: 'well-wishing')", "The quality of being well meaning; kindness", "他受（。者の（。ために「良（。い（。ベネ）ことを（。願（。う（。ヴォル）」こと（。。（。その（。無（。償（。の（。慈（。し（。みが（。、巡（。り（。巡（。って（。、世界（。を（。、優（。し（。い（。光で（。、満（。た（。して（。いく（。のですよ。"),
    ("integrity", "Integrity", "誠実、整合性、インテグリティ", "15th Century", "integer (intact, whole)", "The quality of being honest and having strong moral principles; moral uprightness", "断（。片（。では（。なく（。、全（。てを「一（。つ（。に（。整（。え（。た（。インテー）」潔（。白さ、。（。自（。分（。に（。対（。し（。て（。つく（。嘘を（。捨て（。去（。っ（。た（。とき（。、あなた（。は（。、真（。の（。強（。さを（。手（。に（。入れ（。る（。のです。"),
    ("intuition", "Intuition", "直感（。ちょっかん（。）」、インテュイション", "15th Century", "in- (in, towards) + tueri (to watch, guard, literal: 'watching inside')", "The ability to understand something immediately, without the need for conscious reasoning", "論理を（。思考を（。越え（。て（。、自（。ら（。の「内（。側（。イン）を（。見つめる（。テュイ）」こと（。。（。その（。一瞬の（。眩（。し（。い（。閃（。きこそ（。、魂が（。捉を（。た（。、至高（。の（。真実（。なの（。ですよ。"),
    ("resilience", "Resilience", "弾力性、復元力、レジリエンス", "17th Century", "re- (again) + salire (to leap, literal: 'leaping back')", "The capacity to recover quickly from difficulties; toughness", "困難（。に（。打（。ち（。の（。め（。さ（。れて（。も（。、再（。び（。高く「跳（。ね（。返（。る（。リ、サリ）」こと（。。（。その（。し（。な（。やかな（。る（。強（。さが（。、あなた（。の（。魂を（。、どこ（。までも（。遠（。くに（。、運（。んで（。くれ（。る（。のです。")
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
            word_id = f"{word_text.lower()}_mind"
            
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
                    "thinking": item[6] if len(item) > 6 else "心は、宇宙が自分自身を観察するために用意した、眩しい鏡なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "直感は、思考が追いつけないほどの速度で、真実という名の光を捉える能力なのです。",
                    "example": f"The therapist encouraged the patient to engage in {word_text} to better understand their emotional triggers.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["内省とは、過去を悔いることではなく、現在という名の扉を、自らの手で開けることなのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["repressed", "euphoric", "ecstatic"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Introspection & Void (Cycle 66).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
