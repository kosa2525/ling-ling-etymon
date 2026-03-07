import json
import re

# Theme: The Alchemy of Bond & Bridge (Cycle 92)
words_data = [
    ("bond", "Bond", "絆、契約、債券、ボンド", "13th Century", "band (band, fetter, literal: 'binding')", "A relationship between people or groups based on shared feelings, interests, or experiences", "目（。に（。見（。え（。な（。い（。魂の「紐（。バンド）』によって、峻（。烈（。に（。繋（。が（。れた（。者たちの（。誓（。い（。（。その（。不（。動の（。る（。信頼（。が（。ある（。から（。こそ（。、宇宙の（。荒波（。を（。、あなた（。は（。、誇（。り（。高く、渡（。り（。歩（。け（。る（。のですよ。"),
    ("hinge", "Hinge", "蝶番（ちょうつがい）、要点、ヒンジ", "13th Century", "hangian (to hang)", "A movable joint or mechanism on which a door, gate, or lid swings as it opens and closes, or which connects linked objects", "二つ（。の（。境界を「吊（。る（。し（。、繋（。ぎ（。止（。める（。ヒンジ）」、至高（。の（。る（。支（。点（。（。その（。静（。か（。な（。る（。回（。転が（。ある（。から（。こそ（。、扉は（。、真（。実（。の（。世界（。へと（。、拓（。か（。れ（。る（。のですよ。"),
    ("pivot", "Pivot", "旋（。回（。軸、中心人物、ピボット", "14th Century", "piva (pipe, literal: 'turning point')", "The central point, pin, or shaft on which a mechanism turns or oscillates", "全（。てのエナジーが（。、静（。か（。に（。、その（。一点を「中心（。に（。回る（。ピボ）』場所（。（。あなたが（。その（。軸（。を（。、魂で（。、峻（。烈（。に（。自（。覚する（。とき、運命（。の（。歯（。車（。は（。、新（。し（。く（。、動き（。出（。し（。ます。"),
    ("net", "Net", "網、ネット、正味、純粋な", "Old English", "net (net, literal: 'something knotted')", "A piece of open-meshed material made of twined cord, rope, or thread", "バラバラ（。の（。欠片（。を（。、峻（。烈（。に「搦（。め（。捕（。る（。ネット）』ための（。、目（。に（。見（。え（。な（。い（。秩序（。（。その（。幾（。何（。学（。的（。な（。る（。連（。な（。りにこそ（。、真実（。の（。、純粋（。な（。る（。エナジーが（。、宿（。り（。ます。"),
    ("weave", "Weave", "織る、編み上げる、ウィーヴ", "Old English", "wefan (to weave)", "Form fabric by interlacing long threads passing in one direction with others at a right angle to them", "一（。本（。の（。糸（。が（。、峻（。烈（。な（。る（。意志で「交（。差（。し（。、響（。き（。合う（。ウィーヴ）」、至高（。の（。る（。行為（。（。その（。丹（。念（。なる（。る（。作業の（。果てに（。、世界（。は（。一枚の（。、眩（。しい（。衣（。裳（。と（。な（。る（。のですよ。"),
    ("fiber", "Fiber", "繊維、質、ファイバー", "14th Century", "fibra (fiber, filament, literal: 'filament')", "A thread or filament from which a vegetable tissue, mineral substance, or textile is formed", "物体の（。底（。知（。れ（。ぬ（。力（。を（。支（。え（。る（。、「根源（。的な（。る（。糸（。フィブラ）』。（。一（。つ（。一（。つの（。粒子が（。、峻（。烈（。な（。る（。均衡で（。、あなた（。を、美し（。い（。構造（。へと（。、導（。い（。て（。いる（。のですよ。"),
    ("cord", "Cord", "索、紐（。、コード", "13th Century", "khorde (string, gut, literal: 'gut string')", "Thin, flexible string or rope made from several twisted strands", "魂（。と（。魂を、至高（。の（。る（。力で（。繋ぐ「強（。靭（。な（。る（。紐（。コード）』。（。その（。一（。本の（。連（。な（。りが（。ある（。から（。こそ（。、あなた（。の（。想（。いは（。、遥（。かな（。る（。場所へと、届（。く（。ことができる（。のです。"),
    ("knot", "Knot", "結び目、難題、ノット", "Old English", "cnotta (knot)", "A fastening made by tying a piece of string, rope, or something similar", "想（。いが（。一（。点（。に（。集中（。し（。、峻（。烈（。に「絡（。み（。合った（。ノット）』、重厚（。な（。る（。沈黙（。（。その（。複雑（。な（。る（。真実（。を（。、一（。つ（。ずつ（。、優（。しく（。、解（。い（。て（。い（。く（。ことが、智慧なの（。ですよ。"),
    ("tie", "Tie", "結ぶ、絆、同点、タイ", "Old English", "tēgan (to tie, literal: 'to bind')", "Attach or fasten with string or similar cord", "バラバラ（。の（。エナジーを、一（。つ（。の（。意志へと「結（。び（。付ける（。タイ）』、至高の（。る（。調和（。（。その（。繋（。が（。って（。いる（。という（。る（。瑞々（。し（。い（。自覚が、あなた（。を、至（。宝（。へと（。変え（。ます。"),
    ("pact", "Pact", "協約、盟約、パクト", "15th Century", "pactum (agreement, literal: 'something fixed/agreed')", "A formal agreement between individuals or parties", "魂（。と（。魂が（。、峻（。烈（。に「合（。意（。し（。た（。パクト）』、不（。動の（。る（。真実（。（。何（。も（。言（。わ（。ず（。と（。も（。、その（。一点（。において（。、世界（。は（。盤（。石（。な（。る（。る（。均衡を、保（。っ（。て（。いる（。のですよ。"),
    ("accord", "Accord", "一致、合意、アコード", "12th Century", "ad- (to) + cor (heart, literal: 'to the heart')", "Give or grant someone (power, status, or recognition)", "あなた（。の「心（。コル）へと（。導（。かれた（。）」、至高（。の（。る（。共鳴（。（。あらゆる（。矛盾（。を（。脱（。し（。、ただ（。一（。つ（。の（。調べへと（。、溶（。け（。合（。う（。その（。瞬間を（。、静（。か（。に（。、愛（。で（。て（。ください。")
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
            word_id = f"{word_text.lower()}_bond"
            
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
                    "thinking": item[6] if len(item) > 6 else "繋がりとは、お互いに依存することではなく、自らの独立を保ちながら、相手という名の宇宙を祝福する行為なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "結び目は、解けないことが目的ではない。一瞬の結合によって、新しいエナジーを産み出すための、聖なる拠点なのですよ。",
                    "example": f"The strong {word_text} between the two survivors helped them overcome the immense challenges of the frozen wasteland.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["糸が織り重なることで一枚の布になるように、私たちの孤独な祈りも、重なり合うことで一つの世界を紡ぎ出すのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Bond & Bridge (Cycle 92).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
