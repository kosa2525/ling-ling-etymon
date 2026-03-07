import json
import re

# Theme: The Alchemy of Archetype & Mask (Cycle 58)
words_data = [
    ("archetype", "Archetype", "原型、典型、アーキタイプ", "16th Century", "arkhe- (first) + tupos (type, model, literal: 'strike')", "A very typical example of a certain person or thing"),
    ("persona", "Persona", "ペルソナ、社会的仮面", "18th Century", "persona (mask, character, literal: 'personare' sound through)", "The aspect of someone's character that is presented to or perceived by others", "真（。実（。の（。自分を（。隠（。し（。、ただ（。世界に「響（。き（。渡（。る（。ソナ）声（。）」だけを（。通（。して（。、自ら（。を（。演じ（。る（。こと（。。（。その（。眩（。しい（。仮面（。の（。裏側（。に（。、あなた（。の（。本（。当（。の（。魂が（。息づいて（。いる（。のですよ。"),
    ("mythos", "Mythos", "神話、物語の体系、ミュトス", "18th Century", "muthos (word, story)", "A traditional or recurrent narrative theme or plot structure", "単なる（。フィクションではなく（。、民族（。の（。魂が（。紡（。ぎ（。出した「原初（。の（。言葉（。ミュトス）」。（。そこ（。には（。、宇宙の真理（。が（。、象徴（。という（。名の（。衣（。を（。纏（。い（。、静（。か（。に（。息（。づ（。いて（。いる（。のですよ。"),
    ("ethos", "Ethos", "特質、風土、エートス", "17th Century", "ethos (character, nature, habit, literal: 'custom')", "The characteristic spirit of a culture, era, or community as manifested in its beliefs and aspirations", "その（。集い（。が（。守り（。続けて（。きた「習慣（。エートス）」の（。堆（。積（。。（。空気（。の（。ように（。、そこに（。ある（。だけで（。、人（。々（。の（。振る舞（。い（。を（。、気高く（。律（。し（。続けて（。いる（。、静（。か（。な（。る（。秩序。"),
    ("pathos", "Pathos", "感銘、哀愁、パトス", "17th Century", "pathos (suffering, feeling)", "A quality that evokes pity or sadness", "言葉（。を（。超えて（。、魂を（。烈（。しく「震（。わせ（。る（。パト）情動（。）」。（。その（。切（。な（。い（。美し（。さに（。、私たちは（。自らの（。人間（。的な（。脆（。さと（。尊（。さを（。、同時（。に（。想（。い（。出す（。のです。"),
    ("motif", "Motif", "主題、動機、モチーフ", "19th Century", "motivus (serving to move)", "A decorative design or pattern", "物語を（。、見えない（。場所から「突き（。動かす（。モティ）もの（。）」。（。繰（。り（。返し（。現れる（。その（。かたちが（。、バラバラ（。な（。出来事を（。、一つの（。美し（。い（。運命（。へと（。、繋（。ぎ（。止（。めて（。いる（。のですよ。"),
    ("allegory", "Allegory", "寓話（。ぐうわ（。）」、比喩、アレゴリー", "14th Century", "allos (other) + agoreuein (to speak, literal: 'other-speaking')", "A story, poem, or picture that can be interpreted to reveal a hidden meaning, typically a moral or political one", "真実を（。その（。まま（。語（。る（。のを（。止め（。、「別（。の（。アロス）言葉（。アゴレ）を（。通して（。）」、そっと（。伝（。える（。こと（。。（。その（。眩（。し（。い（。嘘（。は（。、時に（。、残酷（。な（。現実（。よりも（。深く（。、魂（。の（。本（。質（。を（。照（。ら（。し（。出し（。ます。"),
    ("parable", "Parable", "譬（。たと（。え（。）」話、パラブル", "13th Century", "para- (beside, beside) + ballein (to throw, literal: 'comparison')", "A simple story used to illustrate a moral or spiritual lesson, as told by Jesus in the Gospels", "言葉を（。、現実（。という（。名の（。大地に「横へと（。パラ）投げ（。出す（。バロ）」こと（。。（。その（。小（。さな（。物語（。が（。、いつか（。あなた（。の（。中（。で（。、巨大（。な（。気づ（。きの（。木（。へと（。、育（。つの（。ですよ。"),
    ("fable", "Fable", "童話、寓話、フェイブル", "14th Century", "fari (to speak, literal: 'talk, saying')", "A short story, typically with animals as characters, conveying a moral", "動物たちの（。姿を（。借り（。て（。、人間（。の（。愚か（。さと（。愛（。お（。し（。さを「語（。り（。出す（。ファ）」もの（。。（。そこ（。には（。、時（。を（。超（。え（。て（。、子供（。たちの（。瞳が（。、いつ（。までも（。、輝（。きを（。保（。って（。いる（。のですよ。"),
    ("folklore", "Folklore", "民間伝承、フォークロア", "19th Century", "folk + lore (learning)", "The traditional beliefs, customs, and stories of a community, passed through the generations by word of mouth", "名（。も（。な（。い（。人々が「学（。び（。ロア）伝えて（。きた（。）」、大地の（。智（。恵。（。風（。や（。土（。の（。匂（。いに（。、密（。かに（。宿る（。、その（。場所（。に（。生き（。た者（。たちの（。、無（。数（。の（。囁（。き。"),
    ("totem", "Totem", "トーテム、守護神", "18th Century", "ototeman (his kinship group)", "A natural object or animal believed by a particular society to have spiritual significance and adopted by it as an emblem", "その（。族が「共に（。生きる（。テマン）絆（。）」の（。象徴（。。（。動（。物（。という（。名の（。兄弟が（。、あなた（。を（。、孤独（。な（。る（。荒野（。から（。、静（。か（。に（。守（。って（。くれて（。いる（。のですよ。"),
    ("talisman", "Talisman", "お守り、タリスマン", "17th Century", "telos (end, result, completion, literal: 'result')", "An object, typically an inscribed ring or stone, that is thought to have magic powers and to bring good luck", "祈り（。の「果て（。テロス）として（。）」完成（。さ（。れた（。、聖なる（。欠片（。。（。その（。小（。さな（。石（。一（。つ（。に、運命（。を（。、最（。良（。の（。結末（。へと（。、導（。く（。ための（。、エナジーが（。封印（。さ（。れて（。いる（。のです。"),
    ("scepter", "Scepter", "王笏（おうしゃく）、権威", "13th Century", "skeptron (staff, literally: 'stick for leaning on')", "An ornamented staff carried by rulers on ceremonial occasions as a symbol of sovereignty", "一人（。では（。到底（。支（。え（。き（。れ（。ない（。巨大な（。責任（。を（。、支（。えるための「杖（。スケプ）」。（。そこ（。には（。、人（。々（。の（。願（。い（。と（。、統（。治（。という（。名の（。、重（。厚（。な（。る（。沈黙が（。宿（。って（。いる（。のですよ。"),
    ("deity", "Deity", "神、神格、ディーティ", "13th Century", "deus (god, literal: 'shining one')", "A god or goddess", "天上（。から「眩（。し（。く（。輝き（。デ）放（。つ（。）」存在（。。（。その（。光（。の（。前（。では（。、言葉（。は（。、ただの（。塵（。と（。なって（。舞（。い（。散（。る（。けれど（。、心（。の（。中で（。、全（。て（。を（。祝福（。し（。続け（。て（。いる（。のです。"),
    ("sacrifice", "Sacrifice", "犠牲、生け贄、サクリファイス", "13th Century", "sacer (holy) + facere (to make)", "An act of slaughtering an animal or person or surrendering a possession as an offering to God or to a divine or supernatural figure", "惜（。し（。い（。もの（。を（。手（。放（。し（。、ただの「物質を（。聖なる（。サク）ものへと（。変える（。ファ）」儀（。式（。。（。その（。痛み（。を（。越（。え（。た（。場所（。にのみ（。、真（。の（。価値（。という名の（。、高（。次元（。な（。エナジーが（。、降（。り（。て（。くる（。のですよ。")
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
            word_id = f"{word_text.lower()}_mask"
            
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
                    "thinking": item[6] if len(item) > 6 else "象徴とは、目に見えない巨大な真実が、かりそめの姿を借りてこの世界に現れたものです。",
                    "aftertaste": item[7] if len(item) > 7 else "仮面は、自らを守るための盾であり、同時に、別の自分を生きるための翼でもあります。",
                    "example": f"The story uses the {word_text} of a hero's journey to explore the deeper aspects of human psychology.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["神話は、古い伝説ではなく、今もあなたの中で脈動している、原初のエナジーなのです。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["profane", "sacred", "archetypal"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Archetype & Mask (Cycle 58).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
