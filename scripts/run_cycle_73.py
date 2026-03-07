import json
import re

# Theme: The Alchemy of Metamorphosis & Change III (Cycle 73)
words_data = [
    ("mutation", "Mutation", "突然変異、ミューテーション", "14th Century", "mutare (to change)", "The action or process of mutating"),
    ("transfiguration", "Transfiguration", "変容、変貌、トランスフィギュレーション", "14th Century", "trans- (across) + figura (figure, shape)", "A complete change of form or appearance into a more beautiful or spiritual state", "今（。ある（。かたち（。を「越えて（。トランス）別（。の（。姿（。フィギュラ）へと（。変（。える（。）」こと（。。（。その（。眩（。し（。い（。光の（。中（。で（。、魂は（。、真（。実（。の（。美（。しさを（。、手（。に（。入れ（。る（。のですよ。"),
    ("conversion", "Conversion", "転換、改宗、コンバージョン", "14th Century", "com- (together) + vertere (to turn)", "The process of changing or causing something to change from one form to another", "向（。き（。を「一つに（。コン）向（。き（。変える（。ヴェルテ）』こと（。。（。昨日（。までの（。自分（。を（。脱ぎ（。捨（。て（。、全（。く（。新（。し（。い（。真（。理へと（。、身（。を（。投（。じ（。る（。、勇気（。ある（。決断（。です。"),
    ("adaptation", "Adaptation", "適応、順応、アダプテーション", "17th Century", "ad- (to) + aptare (to fit, literal: 'to join')", "The action or process of adapting or being adapted", "生（。き（。延（。び（。る（。ために、状況に「自（。分（。を（。合（。わ（。せ（。て（。いく（。アダプ）」こと（。。（。その（。し（。な（。やかな（。る（。変（。容だけが（。、あなた（。を（。、不（。毛（。な（。る（。大地（。から（。、救（。い（。出す（。の（。ですよ。"),
    ("revision", "Revision", "改訂、修正、レヴィジョン", "16th Century", "re- (again) + videre (to see, literal: 'to look again')", "The action of revising", "書き（。終（。わ（。った（。と思（。っ（。た（。物語（。を、再び（。「視（。つ（。め（。直（。す（。リ・ヴィジョ）」こと（。。（。その（。謙虚（。な（。る（。眼（。差しの中に（。、真実（。の（。完（。成が（。、静（。か（。に（。、始（。まる（。のですよ。"),
    ("reform", "Reform", "改革、改善、リフォーム", "14th Century", "re- (again) + formare (to form)", "The action or process of reforming an institution or practice", "崩（。れ（。た（。秩序（。を、再び（。「かたち（。づ（。くる（。リ・フォーム）」こと（。。（。古い（。殻（。を（。打ち（。破（。り（。、生命（。の（。鼓動（。を（。、再（。び（。呼び（。覚（。ます（。、峻（。烈（。な（。る（。意志。"),
    ("innovation", "Innovation", "革新、イノベーション", "15th Century", "in- (into) + novus (new)", "The action or process of innovating", "既（。成の（。概念の「中（。に（。イン）新（。し（。い（。ノヴァ）光を（。投げ（。込む（。）」こと（。。（。その（。一一点（。の（。閃光（。が（。、停（。滞（。した（。世界（。を（。、鮮（。やかに（。、塗り（。替（。えて（。いく（。のですよ。"),
    ("revolution", "Revolution", "革命、回転、回転周期", "14th Century", "re- (back, again) + volvere (to roll, literal: 'rolling back')", "A forcible overthrow of a government or social order, in favor of a new system", "円（。環（。を「再び（。回（。る（。ヴォル）』こと（。であり（。、かつて（。の（。場所へと（。新（。しく（。還（。る（。こと（。。（。その（。巨大（。な（。回（。転が（。、運命（。を、烈（。し（。く（。一（。変（。さ（。せる（。のですよ。"),
    ("evolution", "Evolution", "進化、発展、エボリューション", "17th Century", "ex- (out) + volvere (to roll, literal: 'rolling out')", "The process by which different kinds of living organisms are thought to have developed and diversified from earlier forms during the history of the earth", "内（。側に（。秘（。めた（。可能（。性を「外（。へと（。エ）転（。が（。し（。出す（。ヴォル）」こと（。。（。数（。億（。年（。という（。時間の（。大河（。を（。、ただ（。ひたすら（。、美し（。い（。高（。みへと（。昇（。る（。、命（。の（。軌跡。"),
    ("precious", "Precious", "貴重な、高価な、プレシャス", "13th Century", "pretium (price)", "Of great value; not to be wasted or treated carelessly", "単（。なる（。数値（。を（。越（。え（。た（。、「至高（。の（。価値（。プレティ）」を（。持（。った（。もの（。。（。その（。煌（。めきは（。、あなたが（。そ（。れ（。を（。、どれ（。ほど（。愛（。して（。いる（。か（。を（。、物（。語（。って（。いる（。のですよ。"),
    ("tariff", "Tariff", "関税、料金表、タリフ", "16th Century", "ta'rif (notification, literal: 'to make known')", "A tax or duty to be paid on a particular class of imports or exports", "国（。境（。を（。越える（。とき（。、その（。存在（。の「価値（。を（。知（。ら（。せ（。る（。タリフ）」ため（。の（。、峻（。烈（。な（。る（。儀（。式（。。（。そこ（。には（。、交易（。という（。名の（。、文明（。の（。知恵（。が（。、刻ま（。れて（。いる（。のですよ。"),
    ("duty", "Duty", "義務、職務、関税", "13th Century", "debere (to owe, literal: 'due-ty')", "A moral or legal obligation; a responsibility", "借り（。て（。いた（。エナジーを、宇宙に「お（。返（。し（。する（。デュー）』、誇（。り（。高い（。誓（。い（。。（。その（。責任（。の（。重厚（。な（。る（。沈黙（。が（。、あなた（。を（。、気高い（。る（。者へと（。、育（。つの（。ですよ。"),
    ("debt", "Debt", "借金、負債、デット", "13th Century", "debere (to owe)", "Something, typically money, that is owed or due", "自（。分の（。力（。では（。ない（。ものを「預（。か（。り（。持って（。いる（。デ）』状態（。。（。その（。重（。荷（。を（。、いかに（。誠実（。に（。、光（。へと（。変（。え（。て（。いく（。か（。、それ（。が（。あなた（。の（。修練（。なの（。ですよ。"),
    ("loan", "Loan", "貸付、ローン", "Old English", "læn (loan, gift, literally: 'to leave')", "A thing that is borrowed, especially a sum of money that is expected to be paid back with interest", "誰（。かの（。手を（。離（。れ（。て（。、あなた（。の（。元に「残（。さ（。れ（。た（。レン）」もの（。。（。その（。一時（。的な（。る（。恵（。みを（。、ただ（。奪（。う（。のではなく（。、生（。か（。し（。、育（。む（。こと（。を（。（。学（。んで（。ください。"),
    ("credit", "Credit", "信用、名誉、クレジット", "16th Century", "credere (to believe, literal: 'to place heart')", "The ability of a customer to obtain goods or services before payment, based on the trust that payment will be made in the future", "自（。分の「心（。コル）を（。預（。ける（。デ）』こと（。。（。目（。に（。見（。え（。な（。い（。信（。頼（。の（。連（。なりが（。、世界（。を（。、一（。つ（。の（。巨大（。な（。エナジーへと（。、繋（。ぎ（。止めて（。いる（。のですよ。")
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
            word_id = f"{word_text.lower()}_change"
            
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
                    "thinking": item[6] if len(item) > 6 else "変容とは、自分を失うことではなく、本当の自分に出会うための、眩しい脱皮なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "価値は、価格が決めるのではなく、あなたがそれをどれほど必要としているか、という魂の叫びが決めるのですよ。",
                    "example": f"The biological process of {word_text} allows organisms to survive in rapidly changing environments.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["昨日までの自分が、今の自分を裏切るたびに、世界は新しく産まれ変わるのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["precious", "modern", "novel"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Metamorphosis & Change III (Cycle 73).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
