import json
import re

# Theme: The Alchemy of Archive & Legend (Cycle 71)
words_data = [
    ("annals", "Annals", "年代記、史料、アナルズ", "16th Century", "annus (year)", "A record of events year by year"),
    ("memoirs", "Memoirs", "回顧録、手記、メモワール", "15th Century", "memoria (memory, literal: 'mindful')", "A historical account or biography written from personal knowledge or special sources", "過ぎ（。去（。った（。日々を（。、「記憶（。メモリア）の（。中に（。）」静（。か（。に（。、留（。め（。置（。いた（。）」もの（。たちの（。連（。なり。（。そこ（。には（。、生（。き（。た（。証（。が（。、眩（。しい（。ほど（。の（。熱量を（。、今（。だ（。に（。、放（。っ（。て（。いる（。のですよ。"),
    ("biography", "Biography", "伝記、経歴、バイオグラフィー", "17th Century", "bios (life) + graphein (to write, literal: 'life-writing')", "An account of someone's life written by someone else", "一（。人（。の「人生（。ビオス）を（。、言葉（。グラフ）で（。）」、紙（。の（。上に（。定着（。させる（。こと（。。（。その（。一（。行（。一（。行が（。、他（。者（。の（。魂と（。、時（。を（。越（。え（。て（。、響（。き（。合う（。ための（。、聖なる（。架（。け（。橋。"),
    ("genealogy", "Genealogy", "系図、家系、ジェネアロジー", "14th Century", "genea (race, family) + logos (word)", "A line of descent traced continuously from an ancestor", "命（。という（。名の（。巨大な（。連鎖（。を（。「言葉（。ロゴス）で（。説（。く（。）」こと（。。（。あなた（。が（。今（。そこに（。在（。る（。こと（。の（。理由（。を（。、血信（。の（。記憶から、静（。か（。に（。、あぶり（。出す（。のですよ。"),
    ("millenary", "Millenary", "千年紀の、千人の、ミレナリー", "16th Century", "mille (thousand)", "Of, relating to, or consisting of a thousand", "「千（。ミレ）という（。名の（。、長大（。な（。る（。過（。酷（。を（。越えて（。）」。（。その（。膨（。大な（。時間の（。集（。積が（。、現代（。の（。軽（。薄（。さを（。、重（。厚（。な（。る（。沈黙（。で（。、戒（。めて（。くれる（。のですよ。"),
    ("narrative", "Narrative", "物語、語り口、ナラティブ", "15th Century", "gnarus (knowing, literal: 'to make known')", "A spoken or written account of connected events; a story", "バラバラ（。な（。出来事を（。、一（。つ（。の「意味（。グナルス）として（。）」、繋（。ぎ（。合わせ（。て（。、伝（。え（。る（。こと（。。（。あなた（。の（。人生を（。、誰（。にも（。奪（。わ（。れ（。な（。い（。自（。分（。だけ（。の（。物語へと（。、編（。み（。上げ（。て（。ください。"),
    ("artifact", "Artifact", "工芸品、人工物、アーティファクト", "19th Century", "ars (art) + factum (fact, made, literal: 'made by art')", "An object made by a human being, typically one of cultural or historical interest", "自然（。の（。中（。には（。存在（。し（。な（。い（。、人間の「知性（。アルス）が（。産（。み（。出した（。ファクト）』。（。その（。一（。つ（。の（。道具（。に（。、かつて（。の（。人々の（。祈り（。と（。、技術（。が（。、静（。か（。に（。封印（。さ（。れて（。いる（。のですよ。"),
    ("memorial", "Memorial", "記念（。碑（。、記念の（。、メモリアル", "14th Century", "memoria (memory)", "A statue or structure established to remind people of a person or event", "忘（。れ（。去（。ら（。れ（。よ（。う（。と（。する（。記憶を、再び（。「心（。メモリア）へ（。と（。呼び戻す（。）」ための（。装置（。。（。その（。不（。動（。の（。石（。の（。姿に（。、私たちは（。、永遠（。という（。名の（。、一（。瞬（。を（。、見（。出（。す（。のですよ。"),
    ("ruins", "Ruins", "廃墟、遺跡、ルインズ", "14th Century", "ruere (to fall)", "The remains of a building, typically an old one, that has suffered much damage or disintegration", "かつて（。の（。栄（。華（。が（。、ただ「崩（。れ（。落ち（。た（。ルイ）」場所（。。（。その（。欠（。片一（。つ（。一（。つ（。が（。、時間（。の（。残酷（。さと（。、それ（。でも（。消（。え（。な（。い（。美（。し（。さ（。を（。、雄弁に（。物語っ（。て（。いる（。のですよ。"),
    ("eternity", "Eternity", "永遠、永劫、エターニティ", "14th Century", "aivus (age, age, literal: 'age-lasting')", "Infinite or unending time", "一（。時（。の（。瞬（。き（。を（。越（。え（。て（。、ただ（。存在（。が「永（。劫に（。エヴァ）留（。ま（。る（。）」こと（。。（。その（。静（。かな（。る（。深（。淵の中に（。、魂（。は（。、終（。わり（。の（。な（。い（。、自由を（。見（。出（。す（。のですよ。"),
    ("archive", "Archive", "記録保管所、公文書、アーカイブ", "17th Century", "arkhe (government, origin, literal: 'magistrate's house')", "A collection of historical documents or records providing information about a place, institution, or group of people", "バラバラ（。の（。記憶に（。、「統治（。アルケ）という（。名の（。秩序（。）」を（。与（。え（。、静（。か（。に（。眠（。ら（。せる（。場所（。。（。そこ（。を開（。け（。放（。つ（。とき（。、歴史（。は（。、再び（。新（。しい（。命を（。、宿（。し（。始める（。ので（。すよ。"),
    ("chronicle", "Chronicle", "年代記、物語、クロニクル", "14th Century", "khronos (time)", "A factual written account of important or historical events in the order of their occurrence", "時間（。という（。名の（。冷（。徹（。な（。河を「文字（。クロノス）として（。）」、一（。巻（。の（。書（。物（。に（。定着（。させる（。こと（。。（。その（。記述が（。ある（。から（。こそ（。、私たちは（。過去（。を（。、今（。として（。生き（。る（。ことが（。でき（。る（。のですよ。"),
    ("lineage", "Lineage", "血統、系譜、リネージ", "13th Century", "linea (line)", "Linear descent from an ancestor; ancestry or pedigree", "命（。が（。一（。つ（。の「線（。リネア）となって（。）」、時代を（。貫（。い（。て（。いく（。こと（。。（。その（。細（。い（。一（。本の（。糸に（。、無（。数（。の（。先祖（。たちの（。祈り（。が（。、結（。ば（。れて（。いる（。のですよ。"),
    ("legacy", "Legacy", "遺産、受け継いだもの、レガシー", "15th Century", "legare (to send as a representative, literal: 'commissioned')", "An amount of money or property left to someone in a will", "全（。てを（。精算（。し、ただ「託（。さ（。れ（。た（。レガ）もの」として（。、後世へと（。、送（。り（。出す（。こと（。。（。あなた（。の（。生（。き（。様（。その（。ものが（。、いつか（。誰（。かの（。魂を（。、静（。か（。に（。支える（。、至高の（。光（。と（。なる（。のです。"),
    ("heritage", "Heritage", "遺産、継承物、ヘリテージ", "13th Century", "heres (heir)", "Property that is or may be inherited; an inheritance", "過去から（。現代へと（。、「受け（。継（。ぐ（。ヘレス）べき（。）」、至高（。の（。記憶（。。（。石（。の（。壁（。にも（。、一枚（。の（。布（。にも（。、先祖（。たちの（。祈り（。が（。刻ま（。れて（。いる（。のですよ。")
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
            word_id = f"{word_text.lower()}_legend"
            
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
                    "thinking": item[6] if len(item) > 6 else "歴史は、過去に起きた出来事の羅列ではなく、魂が未来へ向けて放った、たった一つの祈りの集積なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "記録は、忘却という名の広大な海に対抗するために、私たち人類が築き上げた、静かなる防波堤なのですよ。",
                    "example": f"The historian carefully examined the ancient {word_text} to reconstruct the timeline of the forgotten dynasty.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["昨日までの自分が、今の自分という名の鏡に映るとき、そこには必ず、受け継がれたエナジーが宿っているのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Archive & Legend (Cycle 71).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
