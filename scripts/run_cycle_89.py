import json
import re

# Theme: The Alchemy of Impetus & Momentum (Cycle 89)
words_data = [
    ("stimulus", "Stimulus", "刺激、激励、スティミュラス", "17th Century", "stimulus (goad, literal: 'pointed stick')", "A thing or event that evokes a specific functional reaction in an organ or tissue", "魂の（。微（。睡（。みを（。奪（。い（。去（。る（。、「峻（。烈（。な（。る（。一（。突き（。スティミュ）』。（。その（。鋭（。利な（。る（。痛（。みが（。ある（。か（。ら（。こそ（。、あなた（。は（。、真（。実（。の（。世界（。へと（。、再び（。、目（。覚め（。る（。ことが（。できる（。のですよ。"),
    ("reflex", "Reflex", "反射、跳ね返り、リフレックス", "16th Century", "re- (back) + flectere (to bend, literal: 'bending back')", "An action that is performed as a response to a stimulus and without conscious thought", "世界（。からの（。想（。い（。を、思考を（。越元（。て「跳（。ね（。返（。した（。リフレ）』、峻（。烈（。な（。る（。返答（。（。その（。一瞬の（。煌（。めきにこそ（。、あなた（。という（。存在（。の（。、原（。初（。的（。な（。る（。美（。し（。さが（。、宿ります。"),
    ("stride", "Stride", "大股（。の（。歩（。み（。、進歩、ストライド", "Old English", "strīdan (to straddle)", "Walk with long, decisive steps in a specified direction", "大地を（。力（。強く「跨（。ぎ（。越（。す（。ストリ）』、壮大（。な（。る（。歩調（。（。その（。一歩一歩（。が（。、不（。確実な（。る（。日常（。を（。、眩（。しい（。物（。語（。へと（。、変（。え（。て（。いく（。のですよ。"),
    ("dash", "Dash", "突進、ダッシュ、一（。滴（。、不（。純（。物（。", "13th Century", "Old French dacier/dachier (to strike, clash)", "An act of running somewhere suddenly and hastily", "一（。点（。に（。向かって、自らの（。魂を「叩（。き（。付ける（。ダッシュ）」、至高（。の（。る（。加速（。（。その（。峻（。烈（。な（。る（。一瞬の中に、宇宙（。の（。全エナジー（。が（。、集約（。さ（。れ（。て（。いる（。のですよ。"),
    ("bounce", "Bounce", "跳ねる、弾む、バウンス", "13th Century", "Old French bondir (to leap, echo, literal: 'to rebound')", "Move quickly up, back, or away from a surface after hitting it", "地上の（。重力（。を（。、美し（。く「裏（。切（。る（。バウン）』一瞬の（。る（。跳躍（。（。その（。軽（。快な（。る（。余韻が（。ある（。か（。ら（。こそ（。、魂は（。、永遠（。に（。、若々（。し（。く（。在（。り（。続け（。る（。のですよ。"),
    ("swirl", "Swirl", "渦巻、スワール", "15th Century", "Old Norse svirla (to whirl, spin)", "Move in a twisting or spiraling pattern", "流（。れ（。る（。時間を（。、美し（。い「螺旋（。へと（。変える（。スワル）』、静（。か（。な（。る（。舞（。い（。（。その（。不（。均（。一（。な（。る（。煌（。めきを、ただ（。、魂で（。、感（。じ（。て（。いて（。ください。"),
    ("drift", "Drift", "漂流、趣（。旨（。、ドリフト", "13th Century", "drīfan (to drive, literal: 'driven')", "Be carried slowly by a current of air or water", "自（。らの（。意志を（。捨て（。去（。り（。、ただ「流（。さ（。れ（。る（。まま（。ドリ）』に（。在（。る（。こと（。。（。その（。不（。測（。の（。る（。安（。ら（。ぎこそ（。、あなた（。を（。、未だ（。見（。ぬ（。真（。実（。へと（。、運（。ん（。で（。くれる（。のですよ。"),
    ("impetus", "Impetus", "衝動、はずみ、インペタス", "17th Century", "in- (towards) + petere (to seek, literal: 'rushing towards')", "The force or energy with which a body moves", "一（。点（。を（。追い（。求（。め（。、「激（。烈（。に（。駆け（。出す（。イン・ペタス）』、至高（。の（。る（。衝動（。（。あなたが（。その（。エナジーを（。信（。じ（。抜く（。とき、運（。命（。の（。扉は、一瞬（。にして（。、叩（。き（。開け（。られ（。ます。"),
    ("momentum", "Momentum", "勢い、はずみ、モメンタム", "17th Century", "movēre (to move, literal: 'movement')", "The quantity of motion of a moving body, measured as a product of its mass and velocity", "一（。つ（。の（。方向へと（。、「止（。ま（。る（。こと（。の（。な（。い（。る（。美し（。き（。推（。進（。モメン）』。（。その（。峻（。烈（。な（。る（。加（。速（。が（。、あなた（。を（。、中（。庸（。という（。名の（。停（。滞（。から、救（。い（。出す（。のです。"),
    ("inertia", "Inertia", "慣性、惰性、イナーシャ", "17th Century", "iners (unskilled, inactive, literal: 'lack of art')", "A tendency to do nothing or to remain unchanged", "変（。容する（。のを（。拒み（。、ただ（。静（。か（。に「そのまま（。で（。在（。ろ（。う（。イナ）』と（。する（。、峻（。烈（。な（。る（。沈黙（。（。その（。不（。動の（。意志にこそ（。、真実（。の（。重（。厚（。さが（。宿（。ります。"),
    ("friction", "Friction", "摩擦、不和、フリクション", "16th Century", "fricare (to rub)", "The resistance that one surface or object encounters when moving over another", "異（。な（。る（。エナジーが「擦（。れ（。合（。わ（。さ（。れる（。フリ）」ことで産ま（。れる、眩（。し（。い（。熱（。（。その（。峻（。烈（。な（。る（。抵（。抗（。の中にこそ（。、魂の（。火（。は、静（。か（。に（。灯る（。のですよ。"),
    ("tension", "Tension", "緊張、張力、テンション", "16th Century", "tendere (to stretch, literal: 'stretching')", "The state of being stretched tight", "魂の（。弦（。を（。、限界まで「張り（。詰めた（。テンシ）』、峻（。烈（。な（。る（。静止。（。その（。危（。う（。い（。ほどの（。美（。し（。い（。均衡に、宇宙の（。真（。実（。が、宿（。って（。いる（。のです。"),
    ("stress", "Stress", "強調、ストレス、苦渋", "14th Century", "strictus (tight, drawn, literal: 'tightness')", "A state of mental or emotional strain or tension resulting from adverse or very demanding circumstances", "外（。界の（。重みを、自ら（。の（。内で「引き（。締（。め（。た（。ストレ）』、峻（。烈（。な（。る（。圧力（。（。その（。痛（。みの（。中に、あなた（。は（。、真（。の（。強さを（。、再（。発見（。する（。のです。"),
    ("vigor", "Vigor", "活力、勢い、ビガー", "14th Century", "vigere (to be lively)", "Physical strength and good health", "宇宙の（。エナジーが（。、あなた（。という（。存在を「力強（。く（。目（。覚め（。さ（。せる（。ビガ）』こと（。。（。その（。煌（。めきに（。、一切（。の（。濁（。りは（。、存在（。し（。ない（。のですよ。"),
    ("stamina", "Stamina", "スタミナ、根気", "18th Century", "stamen (thread, literal: 'threads/support of life')", "The ability to sustain prolonged physical or mental effort", "魂の（。物（。語（。を（。、どこ（。まで（。も（。遠くへ（。と「繋（。ぎ（。続（。け（。る（。一（。本の（。糸（。スタミナ）』。（。その（。静（。か（。な（。る（。忍（。耐（。が（。、あなた（。を、至高（。の（。る（。完成へと、導（。く（。のです。")
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
            word_id = f"{word_text.lower()}_impetus"
            
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
                    "thinking": item[6] if len(item) > 6 else "衝動とは、理由があるから湧き出すものではありません。宇宙が沈黙に耐えきれなくなって、自らを投げ出した瞬間の叫びなのです。",
                    "aftertaste": item[7] if len(item) > 7 else "勢いを保つことは、速く動くことではありません。自らの中心軸を、一瞬たりとも揺るがさないという、峻烈なる意志のことなのですよ。",
                    "example": f"The sudden {word_text} of creativity led to a series of remarkable artworks that redefined the modern era.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["抵抗とは、妨げではなく、自らの存在を熱く自覚するための、世界からの抱擁のようなものなのかもしれません。"]
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

        print(f"Success: Added {added_count} words. Theme: Impetus & Momentum (Cycle 89).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
