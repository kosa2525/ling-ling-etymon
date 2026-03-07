import json
import re

# Theme: The Alchemy of Myth & Symbol (Cycle 42)
words_data = [
    ("archetype", "Archetype", "原型、典型、アーキタイプ", "16th Century", "arkhe- (original) + tupos (type, blow)", "A very typical example of a certain person or thing", "全（。人類の（。無意識の（。底（。に（。共通して（。刻まれ（。た（。、「最初（。アーク）の（。刻印（。トゥポス）」。時（。も（。場所（。も（。越え（。て（。、私たちは（。常に（。同（。じ（。物語の（。型の中で（。、命（。を（。踊（。ら（。せて（。いる（。のですよ。"),
    ("symbol", "Symbol", "象徴、シンボル", "15th Century", "sun- (together) + ballein (to throw)", "A mark or character used as a conventional representation of an object, function, or process", "バラバラの（。世界を（。一つの（。意味へと（。、「共に（。サン）投げ（。合わ（。せる（。ボール）」こと（。。（。目（。には（。見え（。ない（。巨大（。な（。エナジー（。を（。、この（。小さな（。記号の（。中に（。封印（。した（。もの。"),
    ("myth", "Myth", "神話、架空の出来事、神話学", "19th Century", "muthos (word, speech, story)", "A traditional story, especially one concerning the early history of a people or explaining some natural or social phenomenon, and typically involving supernatural beings or events", "理屈（。を（。超え（。、ただ「語（。り（。継（。が（。れる（。ムトス）」べき（。巨大（。な（。物語（。。（。嘘（。では（。なく（。、真実（。その（。もの（。よりも（。深く（。魂に（。訴（。えかける（。、宇宙の（。隠（。れた（。設計図。"),
    ("legend", "Legend", "伝説、言い伝え、レジェンド", "14th Century", "legere (to read)", "A traditional story sometimes popularly regarded as historical but unauthenticated", "かつて（。は「読（。ま（。れる（。レゲ）べき（。聖徒（。の（。物語」だった（。もの（。。（。歴史（。の（。荒波を（。越え（。、黄金（。の（。尾（。を（。引（。く（。ようにして（。、現代（。へと（。辿（。り（。着いた（。、英雄（。たちの（。残り（。香（。）。", "あなた（。自身（。の（。人生を（。、たった一（。つの（。美（。しい「レジェンド（。伝説）」に（。仕（。立てて（。あげて（。ください。"),
    ("fable", "Fable", "寓話、たとえ話、寓意", "14th Century", "fari (to speak)", "A short story, typically with animals as characters, conveying a moral", "子供（。たちに「語（。り（。かける（。ファー）」ために（。、真理を（。ユーモア（。の（。オブラート（。で（。包（。んだ（。短い（。物語（。。（。そこ（。には（。、毒（。と（。愛（。が（。、絶妙な（。バランスで（。混ざり（。合（。って（。いる（。のですよ。"),
    ("allegory", "Allegory", "寓意、アレゴリー", "14th Century", "allos (other) + agoreuein (to speak in assembly)", "A story, poem, or picture that can be interpreted to reveal a hidden meaning, typically a moral or political one", "正面（。から（。ではなく（。、「他（。の（。アロス）言葉で（。語（。る（。アゴ）」こと（。。（。ヴェール（。を（。一枚（。隔（。てる（。ことで（。、真実（。の（。眩（。しさを（。あり（。の（。ままに（。受け（。入れる（。ための（。知的な（。装置。"),
    ("parable", "Parable", "比喩、たとえ話、パラブル", "13th Century", "para- (beside) + ballein (to throw)", "A simple story used to illustrate a moral or spiritual lesson, as told by Jesus in the Gospels", "言葉（。を（。、相手の（。人生の「隣（。パラ）に（。そっと（。投げ（。る（。ボール）」こと（。。（。無理（。強い（。する（。のではなく（。、ただ（。寄り添（。う（。ことで（。、自ず（。と（。気づ（。き（。を（。促（。す（。、愛の（。叙事詩。"),
    ("satire", "Satire", "風刺、サタイア", "16th Century", "satura (full, medley, literal: 'a dish full of various fruits')", "The use of humor, irony, exaggeration, or ridicule to expose and criticize people's stupidity or vices, especially in the context of contemporary politics and other topical issues", "権威（。や（。偽善に（。対して（。、様々な（。毒（。と（。笑（。いを「盛（。り（。込（。んだ（。大皿（。サトゥラ）」を（。差（。し（。出（。す（。こと（。。（。その（。鋭（。い（。味（。わ（。いが（。、思考（。の（。停滞（。を（。打ち破（。る（。のです。"),
    ("rite", "Rite", "儀式、祭式、恒例行事", "14th Century", "rite (carefully, in a proper manner)", "A religious or other solemn ceremony or act", "ただの（。習慣（。を（。越え（。、魂を「正しい（。ライト）状態（。）」へと（。導（。く（。ための（。聖（。なる（。段取り（。。（。反復（。する（。こと（。で（。、昨日（。までの（。自分（。を（。脱（。ぎ（。捨て（。、新しい（。時間へと（。参入（。する（。ための（。門。"),
    ("sacrament", "Sacrament", "聖餐、秘跡、サクラメント", "12th Century", "sacer (holy)", "A religious ceremony or act of the Christian Church which is regarded as an outward and visible sign of inward and spiritual divine grace", "日常の（。食事（。や（。行為の中に（。、「聖（。なる（。サケル）もの（。）」を（。招（。き（。入れ（。、自（。ら（。の（。命を（。宇宙の（。恩寵（。へと（。繋（。げる（。、至高（。の（。儀式。"),
    ("divinity", "Divinity", "神性、神学、神々しさ", "14th Century", "divus (god, or shining)", "The state or quality of being divine", "決して（。汚（。れる（。ことのない（。、魂の（。奥底（。で「眩（。い（。ばかりに（。光（。り輝く（。ディヴ（。）」もの（。。（。それは（。、あなた（。の中（。にも（。、そして（。路傍（。の（。一輪の（。花の中（。にも（。、等（。しく（。宿（。って（。いる（。のですよ。"),
    ("deity", "Deity", "神、女神、尊称", "14th Century", "deus (god)", "A god or goddess", "天上（。の高（。みに（。あり（。、世界を「支配（。デウス）する」絶対（。的な（。エナジー（。。（。その（。影（。を（。私たちは（。神々（。と（。呼（。び（。、その（。深遠（。な（。囁（。きを（。神話（。として（。綴（。って（。きた（。のです。"),
    ("shrine", "Shrine", "神社、聖堂、シュライン", "Old English", "scrin (case or box for valuables)", "A place regarded as holy because of its associations with a divinity or a sacred person or relic", "聖なる（。記憶を（。大切に「仕（。舞（。い（。込（。む（。ための（。箱（。スクリーン）」。（。そこ（。には（。、目（。には（。見えない（。けれど（。、確（。かに（。世界を（。支（。える（。エナジー（。が（。、静（。かに（。息（。を（。潜（。めて（。いる（。の（。ですよ。"),
    ("cathedral", "Cathedral", "大聖堂、カテドラル", "13th Century", "kathedra (seat, chair, literally: 'down' + 'sit')", "The principal church of a diocese, containing the bishop's throne", "ただの（。巨大な（。建築物（。では（。なく（。、聖職者（。が「座（。る（。エドラ）場所（。カテ）」を（。中心（。とした（。、宇宙の（。権威（。の（。地上における（。投影。"),
    ("sanctuary", "Sanctuary", "聖域、避難所、サンクチュアリ", "14th Century", "sanctus (holy)", "A place of refuge or safety", "外部の（。暴力（。から（。、命を（。守（。り（。抜く（。ための「聖（。なる（。サン（。）」場所（。。（。誰（。にも（。汚（。さ（。れ（。ない（。、あなた（。の（。中（。の（。静（。かな（。る（。沈黙（。の（。場所。"),
    ("devotee", "Devotee", "愛好家、信奉者、熱中する人", "17th Century", "de- (away, intensive) + vovere (to vow)", "A person who is very interested in and enthusiastic about someone or something", "自（。ら（。の（。全（。てを「捧げる（。ヴォート）ことを（。誓（。った（。）」者（。。（。対象（。と（。同化（。する（。ほどまでに（。、エゴ（。を（。捨て（。去（。った（。果てに（。、真（。の（。歓喜を（。見出（。す（。のです。"),
    ("shaman", "Shaman", "シャーマン、祈祷師", "17th Century", "saman (monk, literally 'one who knows')", "A person regarded as having access to, and influence in, the world of good and evil spirits", "目（。に（。見え（。ない（。異世界（。と（。こちら（。を（。結ぶ（。、静（。かな（。な（。る「知（。る者（。サマン）」。（。魂の（。震（。えを（。言葉（。に（。変（。え（。、調和（。を（。取（。り（。戻（。そう（。とする（。、境界（。の（。守り（。人。"),
    ("wizard", "Wizard", "魔法使い、ウィザード、達人", "15th Century", "wys (wise)", "A man who has magical powers, especially in legends and fairy tales", "単なる（。マジシャン（。では（。なく（。、世界（。の（。法則（。を「賢（。く（。ワイズ）知（。り（。尽（。く（。し（。た（。）」者（。。（。智恵（。が（。究極（。まで（。高ま（。れば（。、それは（。奇跡（。と（。見（。分け（。が（。つか（。ない（。ものに（。なる（。のですよ。"),
    ("sorcerer", "Sorcerer", "魔術師、魔法使い", "15th Century", "sors (lot, fate, share)", "A person who claims or is believed to have magical powers; a wizard", "自分（。に（。分け（。与え（。られた「宿命（。ソルス）」に（。立ち向（。かい（。、それを（。自ら（。の（。意志で（。ねじ曲（。げ（。よう（。とする（。、孤独（。な（。挑戦者。"),
    ("apostle", "Apostle", "使徒、アポストル、主唱者", "Old English", "apo- (away) + stellein (to send)", "Each of the twelve chief disciples of Jesus Christ", "自（。ら（。を（。主張（。する（。のではなく（。、遥（。か（。な（。る（。使命の（。ために「遠（。くへと（。アポ）送（。り（。出（。さ（。れた（。ステ）」者（。。（。その（。足取（。りには（。、委（。ね（。る（。こと（。の（。強さが（。宿（。って（。い（。ます。"),
    ("lineage", "Lineage", "血統、家柄、リネージ", "13th Century", "linea (line)", "Direct descent from an ancestor; ancestry or pedigree", "太（。古の（。昔から（。、絶（。える（。こと（。なく（。引（。かれ（。て（。きた「一本の（。糸（。リネア）」。あなた（。の（。今日（。の（。呼吸（。は（。、無数（。の（。先祖（。たちの（。命の（。結晶（。なのです。"),
    ("covenant", "Covenant", "契約、誓約、カヴェナント", "13th Century", "com- (together) + venire (to come)", "An agreement", "利（。害（。関係（。を（。越（。え（。、魂（。が「共に（。コン）一つの（。場所へと（。辿（。り（。着く（。ヴェニ）」ことを（。約（。した（。もの（。。（。言葉（。による（。契約（。を（。超え（。、存在（。その（。もの（。で（。結（。ば（。れた（。絆。"),
    ("commandment", "Commandment", "戒律、命令、十戒", "13th Century", "com- (intensive) + mandare (to entrust, commit to one's hand)", "A divine rule, especially one of the Ten Commandments", "自（。由を（。奪う（。鎖（。では（。なく（。、自（。らを（。正（。しく（。導く（。ための（。聖（。なる「手（。マヌス）委（。ね（。）」。（。正しい（。不（。自由（。こそが（。、真（。の（。自由を（。産（。み（。出す（。のですよ。"),
    ("scripture", "Scripture", "聖典、聖書、スクリプト", "13th Century", "scribere (to write)", "The sacred writings of Christianity contained in the Bible", "一（。時（。の（。感情（。ではなく（。、永遠（。に（。語（。り（。継（。が（。れる（。べき（。真理を「書（。き（。残し（。た（。スクリプト）」もの（。。（。一（。文字（。一（。文字（。の（。中に（。、人類（。の（。全（。祈り（。が（。込め（。られて（。いる（。の（。ですよ。"),
    ("benediction", "Benediction", "祝福、祝祷", "14th Century", "bene (well) + dicere (to speak)", "The utterance or bestowing of a blessing, especially at the end of a religious service", "相手（。に（。対して（。、ただ「良（。く（。ベネ）語（。る（。ディクション）」こと（。。（。その（。一言（。の（。慈愛（。が（。、凍（。り（。ついた（。心（。を（。溶（。か（。し（。、新しい（。朝を（。連（。れて（。くる（。の（。ですよ。")
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
            word_id = f"{word_text.lower()}_myth"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "神話は、魂が宇宙という巨大な夢を見るための、共通の言語です。",
                    "example": f"The hero's journey is a classic {word_text} that appears in cultures all around the world.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["象徴とは、目に見えない巨大な真理を、目に見える小さな欠片の中に封印する行為です。"]
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

        print(f"Success: Added {added_count} words. Theme: Myth & Symbol (Cycle 42).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
