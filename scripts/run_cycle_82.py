import json
import re

# Theme: The Alchemy of Mirror & Echo III (Cycle 82)
words_data = [
    ("silhouette", "Silhouette", "シルエット、影絵", "18th Century", "Étienne de Silhouette (French minister, literal: 'cheaply made shadow')", "The dark shape and outline of someone or something visible against a lighter background, especially in dim light", "細（。部を（。捨て（。去（。り（。、ただ（。存在（。の「峻（。烈（。な（。る（。輪郭（。シルエット）』だけを（。際（。立（。た（。せ（。た（。姿（。（。其処（。には（。、語（。り（。過（。ぎ（。な（。い（。から（。こそ（。の（。真実（。の（。眩（。し（。さが（。、静（。か（。に（。脈動（。し（。て（。いる（。のですよ。"),
    ("reverse", "Reverse", "逆、背面、リバース", "14th Century", "re- (back) + vertere (to turn, literal: 'turning back')", "Move backward", "光を（。放（。つ（。のを（。止（。め（。、再び（。自分の「内（。側（。へ（。と（。リ）向き（。を（。変える（。ヴェルス）」こと（。。（。その（。反転（。の（。一瞬に、あなたは（。、自分（。自身（。の（。深（。淵（。という（。名の（。、新（。しい（。世界（。に（。、出会（。う（。のですよ。"),
    ("inverse", "Inverse", "逆の、反対の、インバース", "16th Century", "in- (towards) + vertere (to turn, literal: 'turning inwards')", "Opposite in luck, nature, or effect", "日常（。の「内（。側（。に（。イン）向き（。を（。変え（。た（。ヴェル）』、鏡（。の（。向（。こう（。側の（。真実（。（。順（。序（。を（。逆向き（。に（。視（。つ（。める（。とき（。、あなた（。は（。、一（。つ（。の（。巨大（。な（。る（。調和（。の（。設計図に（。、気づ（。く（。のですよ。"),
    ("ultra", "Ultra", "超、過激な、ウルトラ", "19th Century", "ultra (beyond)", "To an extreme degree; very", "限界（。を「越（。え（。て（。ウルトラ）」行く（。、未知（。なる（。エナジー。（。目（。に（。見える（。ものを（。完全（。に（。脱（。し（。、ただ（。光の（。粒子（。その（。ものに（。な（。る（。、至高（。の（。る（。飛躍。"),
    ("extra", "Extra", "余分な、特別の、エキストラ", "17th Century", "extra (outside, beyond)", "Added to an existing or usual amount or object; additional", "定められた（。範囲の「外（。側（。エキストラ）』に（。溢（。れ（。出した（。、豊饒（。な（。る（。エナジー。（。その（。過（。剰（。さが（。ある（。から（。こそ（。、宇宙（。は（。これ（。ほど（。までに（。、美し（。い（。色彩を（。、放（。ち（。続け（。る（。のですよ。"),
    ("intra", "Intra", "内の、内部の、イントラ", "19th Century", "intra (inside, within)", "On the inside; within", "遠（。くに（。求（。め（。る（。のを（。止め（。、ただ（。ひたすら「内（。側（。イントラ）へと（。）」潜（。る（。こと（。。（。あなた（。の（。中にこそ（。、全（。宇宙の（。全記憶が（。、静（。か（。に（。、横（。たわ（。って（。いる（。の（。ですよ。"),
    ("retro", "Retro", "懐古的、過去の、レトロ", "14th Century", "retro (backwards)", "Looking back on or dealing with the past", "未来（。を（。追う（。のを（。止め（。、再び（。「後ろへと（。レトロ）」視（。を（。向（。け（。る（。こと（。。（。その（。懐（。か（。し（。い（。沈黙の中にこそ（。、今を（。生き（。る（。ための（。、真（。実（。の（。る（。光が（。、宿ります。"),
    ("peri", "Peri", "周辺の、周囲、周（。、ペリ", "15th Century", "peri (around, about)", "Around, about", "中心（。からの（。想（。いを（。、静（。か（。に「囲（。う（。ペリ）』境界（。。（。その（。周囲（。を（。、そっと（。、撫（。で（。る（。ように、意味（。が（。、環（。流（。し（。て（。いる（。のですよ。"),
    ("epi", "Epi", "上の、後の、エピ", "15th Century", "epi (upon, at)", "Upon, at, in addition to", "全（。てが（。終わ（。っ（。た（。こと（。の「後（。に（。エピ）上（。に（。）」現れる（。、静（。か（。な（。る（。余韻（。（。その（。一瞬の（。閃（。き（。が（。、物（。語（。に、盤石（。な（。る（。完成（。を（。、与えて（。くれる（。のです。"),
    ("profile", "Profile", "側面、横顔、プロファイル", "17th Century", "pro- (before) + filum (thread, literal: 'drawing with a thread')", "An outline of something, especially a person's face, as seen from one side", "あなた（。の（。魂の（。輪郭（。を、美し（。い「一本（。の（。糸（。フィル）で（。前（。へ（。プロ）描き（。出す（。）」こと（。。（。正面より（。も、その（。鋭（。利な（。側面にこそ（。、隠（。さ（。れ（。た（。る（。真実（。が（。宿（。ります。"),
    ("copy", "Copy", "写し、模倣、コピー", "14th Century", "copia (plenty, abundance, literal: 'to give plenty of transcripts')", "A thing made to be similar or identical to another", "真実を「豊か（。に（。コピア）広（。め（。る（。）」ために、幾（。重（。にも（。繰（。り（。返（。さ（。れる（。、美し（。き（。残像（。（。その（。反（。復（。の中に（。、本来（。の（。煌（。めきが（。、永遠（。に（。保存（。さ（。れて（。いく（。のです。"),
    ("dual", "Dual", "二重の、二元的な、デュアル", "16th Century", "duo (two)", "Consisting of two parts, elements, or aspects", "「二つ（。デュオ）のエナジーを（。、同時（。に（。体（。現（。する（。）」こと（。。（。光（。と（。影（。、静（。と（。動（。、その（。二つの（。鼓動（。が、あなた（。という（。存在（。の（。、一（。つ（。の（。物語を（。、紡（。い（。で（。いる（。のですよ。"),
    ("opposite", "Opposite", "反対の、対立する、オポジット", "14th Century", "op- (against) + ponere (to place, literal: 'placed against')", "Situated on the other or further side in as to face that which is specified", "自（。ら（。の（。存在を、峻（。烈（。に「向か（。い（。合って（。オポ）置く（。ジト）」こと（。。（。その（。対（。峙（。の中にこそ（。、真（。実（。の（。自覚が（。、静（。か（。に（。、産（。声を（。上げる（。のですよ。"),
    ("contra", "Contra", "逆に、対抗して、コントラ", "14th Century", "contra (against)", "Against, opposite", "流れ（。を（。拒み（。、ただ（。ひたすら「抗（。う（。コントラ）こと（。）」。（。その（。峻（。烈（。な（。る（。負（。のエナジーが、世界（。を（。、新（。しい（。均衡へと（。、押し（。上げ（。て（。いく（。の（。ですよ。"),
    ("anti", "Anti", "反、対、アンチ", "Old English", "anti (against)", "Against, opposite", "既存の（。る（。秩序（。に「向か（。い（。打（。つ（。アンチ）」、静（。か（。な（。る（。反逆（。。（。否定（。する（。こと（。でしか（。視（。え（。な（。い（。、至高（。の（。真実（。が（。、其処（。には（。、横（。たわ（。って（。いる（。のですよ。")
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
            word_id = f"{word_text.lower()}_reflect"
            
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
                    "thinking": item[6] if len(item) > 6 else "反射とは、世界をそのまま写し取ることではなく、自らのフィルターを通して、世界を再定義する行為なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "鏡は、自分を映すための道具ではありません。自分という名の深淵を覗き込み、無限という名の孤独に耐えるための窓なのですよ。",
                    "example": f"The spy used various {word_text} identities to infiltrate the secret compound undetected.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["反対の方向に目を向けることは、逃避ではなく、真実という名のコインの裏側を確認する勇気なのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["reverse", "inverse", "ultra", "extra", "intra", "retro", "dual", "opposite"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Mirror & Echo III (Cycle 82).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
