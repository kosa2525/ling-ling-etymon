import json
import re

# Theme: The Alchemy of Serenity & Solace (Cycle 77)
words_data = [
    ("solace", "Solace", "慰め、安らぎ、ソラス", "13th Century", "solari (to console)", "Comfort or consolation in a time of distress or sadness", "凍（。て（。つ（。く（。孤独（。の中に（。、そっと分（。け（。与え（。られた「灯火（。ソラーリ）』。（。その（。優（。し（。い（。温（。か（。みが（。、あなた（。の（。魂の（。傷（。を（。、静（。か（。に（。、癒（。し（。て（。くれる（。のですよ。"),
    ("temperance", "Temperance", "節制、自制、テンペランス", "14th Century", "temperare (to mix, restrain, literal: 'proportioning')", "Abstinence from alcoholic drink", "烈（。し（。す（。ぎ（。る（。情念（。を、正しい「比（。率（。テンペ）で（。整える（。）」こと（。。（。その（。峻（。烈（。な（。る（。自（。制（。の中にこそ（。、真（。実（。の（。自由が（。、宿（。る（。のですよ。"),
    ("prudence", "Prudence", "慎重、思慮分別、プルードンス", "14th Century", "providentia (foresight, literal: 'seeing ahead')", "The quality of being prudent; cautiousness", "目の（。前の（。誘惑（。を（。越（。え（。て（。、遥（。かな（。る「未来を（。見通す（。プルー）』力（。（。その（。静（。かな（。る（。慧（。眼が（。、あなた（。を、思（。わ（。ぬ（。深淵（。から（。、守っ（。て（。くれる（。のですよ。"),
    ("gratitude", "Gratitude", "感謝、グラティチュード", "15th Century", "gratus (pleasing, grateful)", "The quality of being thankful; readiness to show appreciation for and to return kindness", "宇宙から（。届（。いた（。、至高（。の「贈り物（。グラ」を（。、魂で（。受け（。取る（。こと（。。（。その（。謙虚（。な（。る（。喜びが（。、あなた（。の（。エナジーを、さら（。なる（。豊饒（。へと（。、誘（。う（。のです。"),
    ("humility", "Humility", "謙虚、卑下、ヒュミリティ", "14th Century", "humus (earth, ground, literal: 'of the ground')", "A modest or low view of one's own importance; humbleness", "傲（。慢（。な（。る（。翼を（。畳（。み（。、ただ「大地（。ヒュム）の（。上（。に（。）」静（。か（。に（。跪（。く（。こと（。。（。低（。く（。低（。く（。身を（。処（。す（。とき（。、あなた（。は（。、全（。宇宙の（。重（。み（。を（。、知（。る（。のですよ。"),
    ("modesty", "Modesty", "謙遜、中庸、モデスティ", "16th Century", "modus (measure)", "The quality or state of being unassuming or moderate in the estimation of one's relevant abilities", "自（。らを（。誇示（。せ（。ず（。、正しい「尺（。度（。モドゥス）』を（。保（。つ（。こと（。。（。その（。控え（。め（。な（。る（。佇（。まい（。の（。中に（。、計（。り（。知（。れ（。な（。い（。真実（。の（。高貴（。さが（。、宿（。って（。いる（。のですよ。"),
    ("sincerity", "Sincerity", "誠実、偽りのなさ、シンセリティ", "16th Century", "sine (without) + cera (wax, literal: 'without wax')", "The quality of being free from pretense, deceit, or hypocrisy", "不純（。な（。る（。混ざり（。物（。を（。捨て（。、「蜜（。蝋（。ケラ）を（。持（。た（。な（。い（。シン）」、透明な（。魂（。（。その（。一点（。の（。曇り（。も（。な（。い（。輝（。きが（。、他者の（。心を（。、静（。か（。に（。、震（。わ（。せる（。のですよ。"),
    ("awareness", "Awareness", "意識、自覚、アウェアネス", "Old English", "gewær (aware, watchful)", "Knowledge or perception of a situation or fact", "眠（。り（。から（。醒（。め（。、今（。ここ（。に（。在（。る（。こと（。を「峻（。烈（。に（。見張り（。続ける（。ウェア）』こと（。（。その（。一瞬一瞬（。の（。煌（。めきこそ（。、命（。が（。、自（。分（。を（。呼び（。覚（。ます（。、至高の（。儀式なのです。")
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
            word_id = f"{word_text.lower()}_still"
            
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
                    "thinking": item[6] if len(item) > 6 else "安らぎとは、活動が止まることではなく、あらゆる矛盾が自らの中で、静かに溶け合っていった瞬間のことなのです。",
                    "aftertaste": item[7] if len(item) > 7 else "感謝は、足りないものを嘆くのではなく、今ここにある豊かさを、魂で噛み締めるための、たった一つの作法なのですよ。",
                    "example": f"The quiet garden provided a sense of {word_text} that allowed the weary traveler to recover their strength.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["低く身を処することと、魂を卑下することは違います。真の謙虚さは、全宇宙との対等な繋がりに気づくことなのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["sincere", "aware"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Serenity & Solace (Cycle 77).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
