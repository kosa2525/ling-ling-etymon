import json
import re

# Theme: The Alchemy of Order & Chaos (Cycle 44)
words_data = [
    ("chaos", "Chaos", "混沌、カオス", "15th Century", "khaos (yawning gap, void)", "Complete disorder and confusion", "まだ（。光さえ（。存在（。し（。ない（。）、巨大（。な「口を（。開けた（。カオス）虚無（。）」。（。そこ（。には（。、全（。ての（。エナジーが（。未（。分（。化（。な（。まま（。渦（。巻いて（。いる（。、誕生（。直前の（。胎動（。が（。ある（。のですよ。"),
    ("order", "Order", "秩序、命令、順序", "13th Century", "ordire (to begin to weave)", "The arrangement or disposition of people or things in relation to each other according to a particular sequence, pattern, or method", "混沌（。という（。糸を（。、意図を持って「織（。り（。始（。める（。オーディ）」こと（。。（。バラバラ（。な（。出来事を（。、一つ（。の（。美（。しい（。布（。へと（。変（。え（。て（。いく（。、知性の（。営み。"),
    ("apparatus", "Apparatus", "装置、器具、機構", "17th Century", "ad- (to) + parare (to prepare)", "A complex structure within an organization or system", "目的を（。達成（。する（。ために（。、あらかじめ「準備さ（。れた（。パラ）ものへと（。アド）」。（。複数（。の（。部品が（。、一つの（。意志を（。体現（。する（。ために（。、静（。か（。に（。連結（。さ（。れた（。姿。"),
    ("mechanism", "Mechanism", "仕組み、機構、メカニズム", "17th Century", "mekhane (machine, engine, literal: 'means, expedient')", "A system of parts working together in a machine; a piece of machinery", "目的（。を（。果（。たす（。ための「手段（。メカン）」。（。そこ（。には（。、原因（。と（。結果が（。、歯車（。の（。ように（。冷（。徹（。に（。噛（。み（。合（。って（。いる（。、数学的（。な（。美。"),
    ("technique", "Technique", "手法、技術、テクニック", "19th Century", "tekhne (art, skill, craft)", "A way of carrying out a particular task, especially the execution or performance of an artistic work or a scientific procedure", "ただの（。努力（。ではなく（。、魂を（。磨（。き（。上げ（。た（。果てに（。得（。られる「技（。テクネ）」。（。それは（。、世界と（。対話（。する（。ための（。、洗練（。された（。言葉。"),
    ("procedure", "Procedure", "手順、進め方、手続き", "16th Century", "pro- (forward) + cedere (to go)", "An established or official way of doing something", "闇（。雲に（。進む（。のを（。止め（。、一段（。ずつ「前へと（。プロ）歩（。む（。セド）」ための（。設計図（。。（。正（。しい（。順序（。を（。踏む（。ことが（。、不（。可能（。を（。可能へと（。変（。えゆく（。の（。ですよ。"),
    ("sequence", "Sequence", "連続、配列、シークエンス", "14th Century", "sequi (to follow)", "A particular order in which related events, movements, or things follow each other", "一瞬（。の（。出来事が（。、次に「続く（。セクイ）もの」へと（。エナジーを（。手渡（。し（。て（。いく（。こと（。。（。その（。連鎖（。が（。、壮大（。な（。物語の（。リズム（。を（。産（。み（。出す（。のです。"),
    ("lattice", "Lattice", "格子、ラティス", "14th Century", "latte (lath, thin strip of wood, literal: 'side')", "A structure consisting of strips of wood or metal crossed and fastened together", "境界線の（。糸を（。、縦（。横に（。「積み（。重（。ねた（。ラッテ）」もの（。。（。透（。かして（。見（。え（。ながら（。も（。、確（。かに（。そこ（。に（。ある（。境界。"),
    ("grid", "Grid", "格子、網目、グリッド", "19th Century", "griddle (a heavy platform or frame)", "A network of lines that cross each other to form a series of squares or rectangles", "混沌（。とした（。大地を（。、理性の（。物差し（。で（。分断（。し（。、「枠組み（。グリドル）の中（。）」へと（。収（。める（。こと（。。（。その（。整然（。とした（。正方形の（。中に（。、知性の（。支配（。が（。及（。ぶ（。のです。"),
    ("frame", "Frame", "枠組み、骨組み、フレーム", "Old English", "framod (profitable, forward, bold)", "A rigid structure that surrounds or encloses something such as a door or window", "内側（。にある（。豊（。か（。な（。意味（。を（。守（。る（。ために（。、「前（。に（。フレーム）立ち（。塞（。が（。る（。）」強固（。な（。構造（。。（。枠組み（。が（。ある（。から（。こそ（。、中（。の（。物語（。は（。輝（。く（。ことができる（。のですよ。"),
    ("skeleton", "Skeleton", "骨格、形骸、スケルトン", "16th Century", "skeletos (dried up)", "An internal or external framework of bone, cartilage, or other rigid material embodying or supporting the body of an animal or plant", "華（。やかな（。肉体（。を（。削（。ぎ（。落（。し（。、最後（。まで「乾（。い（。た（。スケロ）まま」残（。った（。本質（。。（。それ（。は（。、あなたが（。誰（。である（。かを（。、最後（。まで（。支（。えて（。くれる（。最後（。の（。砦。"),
    ("chassis", "Chassis", "（車の）車台、シャーシ", "17th Century", "capsa (box, frame)", "The base frame of a motor vehicle or other wheeled conveyance", "心臓（。にあたる（。エンジン（。を（。支（。える（。、「箱（。カプサ）のような（。土台（。）」。（。目（。には（。見え（。ない（。けれど（。、全（。て（。のエナジー（。を（。受け（。止める（。、沈黙（。の（。強（。靭さ。"),
    ("hull", "Hull", "船体、（種子の）殻", "Old English", "hulu (shell, husk)", "The main body of a ship or other vessel, including the bottom, sides, and deck but not the masts, superstructure, engines, or rigging", "過酷（。な（。海（。から（。、命（。を（。守（。る（。ための「外（。殻（。フル）」。（。それ（。は（。、未知（。なる（。領域（。へと（。漕（。ぎ（。出す（。ための（。、孤独（。な（。聖域。"),
    ("shell", "Shell", "貝殻、殻、シェル", "Old English", "sciell (shell, scale)", "The hard protective outer case applied to an animal, plant, etc.", "内側の（。柔らか（。い（。魂を（。、時間（。の（。波から（。守（。る（。ための「硬い（。鱗（。シェル）」。（。いつか（。それを（。脱（。ぎ（。捨てる（。とき（。まで（。、あなたは（。その（。中（。で（。静（。か（。に（。育（。まれる（。の（。ですよ。"),
    ("unit", "Unit", "単位、一個、ユニット", "16th Century", "unus (one)", "An individual thing or person regarded as single and complete, especially for purposes of measurement", "宇宙（。を（。構成（。する（。、最小（。の「一（。つの（。ユニ）」かたち（。。（。その（。小さな（。一（。つ（。が（。、巨大（。な（。全体（。を（。支（。えて（。いる（。という（。、誇（。り（。高い（。存在。"),
    ("fragment", "Fragment", "断片、破片、フラグメント", "15th Century", "frangere (to break)", "A small part broken or separated off something", "かつて（。は（。一（。つ（。だった（。真実が（。、衝撃（。によって「壊（。れ（。た（。フラグ）」欠片（。。（。一つ（。ひとつ（。を（。拾（。い（。集（。める（。とき（。、失わ（。れた（。全体（。像（。が（。、心の中に（。蘇（。り（。ます。"),
    ("textile", "Textile", "織物、テキスタイル", "17th Century", "texere (to weave)", "A type of cloth or woven fabric", "単なる（。糸（。の（。集（。まり（。ではなく（。、意図を持って「織（。り（。上（。げ（。られた（。テクス）」思想（。の（。手触り。"),
    ("pattern", "Pattern", "模様、型、パターン", "14th Century", "pater (father)", "A repeated decorative design", "偶然（。の（。中（。に（。、何度も（。あらわ（。れる「父（。パテール）なる（。規範」。繰り返（。される（。ことで（。、世界（。に（。意味（。を（。与（。える（。、秩序（。の（。ダンス。"),
    ("motif", "Motif", "主題、モチーフ", "19th Century", "movere (to move)", "A decorative design or pattern; a distinctive feature or dominant idea in an artistic or literary composition", "心を（。強く「動か（。し（。ムー）続ける（。）」、物語（。の（。核（。となる（。旋律（。。（。退屈（。な（。風景（。の中に（。、一筋（。の（。光（。を（。通（。す（。、情熱（。の（。欠片。"),
    ("prototype", "Prototype", "原型、試作型、プロトタイプ", "16th Century", "protos (first) + tupos (type, blow)", "A first, typical or preliminary model of something, especially a machine, from which other forms are developed or copied", "完成（。の（。前（。の（。、「最初（。プロト）に（。刻まれ（。た（。トゥポス）型」。未（。完（。成（。の（。輝きが（。、未来（。のあるべき（。形を（。指（。し示して（。いる（。のですよ。"),
    ("collage", "Collage", "コラージュ、貼り合わせ", "20th Century", "kolla (glue)", "A piece of art made by sticking various different materials such as photographs and pieces of paper or fabric on to a backing", "バラバラの（。歴史を（。「糊（。コラ）で（。強引（。に（。貼り（。合わせた（。）」ような（。、暴力（。的な（。までの（。美しさ（。。（。矛盾（。する（。要素が（。、一つの（。画面（。で（。対極（。的（。な（。調和（。を（。産（。み（。出す。"),
    ("mosaic", "Mosaic", "モザイク、寄せ木細工", "13th Century", "mou- (of the Muses)", "A picture or pattern produced by arranging together small colored pieces of hard material, such as stone, tile, or glass", "一（。つひとつは（。無価値（。な（。欠片（。でも（。、「詩の（。女神（。ミューズ）たちが（。集めた（。）」ように（。並べ（。れば（。、巨大（。な（。神の（。顔さえ（。も（。描き出す（。知的な（。奇跡。"),
    ("tapestry", "Tapestry", "タペストリー、つづれ織り", "14th Century", "tapes (carpet, heavy fabric, literal: 'carpet')", "A piece of thick textile fabric with pictures or designs formed by weaving colored weft threads or by embroidering on canvas, used as a wall hanging or furniture covering", "数（。え（。切（。れない（。糸が（。、複雑（。に（。絡（。み（。合い（。ながら（。織り（。上げる「厚い（。布（。タペス）」。（。人類（。の（。全歴史（。が（。一（。枚（。の（。布（。に（。凝縮（。された（。ような（。、重厚（。な（。手触り。"),
    ("monument", "Monument", "記念碑、モニュメント", "13th Century", "monere (to remind, warn)", "A statue, building, or other structure erected to commemorate a famous person or event", "風化（。し（。ゆく（。記憶を（。、現在（。に「留（。め（。（。警告（。する（。モネ）」ための（。石（。。（。過ぎ去（。った（。出来事（。を（。、永遠（。の（。沈黙（。へと（。変（。える（。、言葉（。を（。超（。えた（。彫刻。"),
    ("spire", "Spire", "尖塔、スパイア", "Old English", "spir (stalk, sprout, literal: 'sprout')", "A tapering conical or pyramidal structure on the top of a building, typically a church tower", "大地から（。芽吹（。く「苗木（。スピール）」のように（。、天を（。指し（。示す（。鋭（。い（。祈り（。。（。重力（。という（。過去（。を（。振り切り（。、ひたすら（。高み（。へと（。至（。ろう（。とする（。、精神の（。飛翔。")
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
            word_id = f"{word_text.lower()}_structure"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "秩序は、混沌を愛という名の毛布で包み込んだ結果です。",
                    "example": f"The complex {word_text} of the machine required expert knowledge to understand.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["構造とは、目に見えない巨大なエナジーを、現実というかたちの中に閉じ込めるための檻であり、同時に聖域でもあるのです。"]
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

        print(f"Success: Added {added_count} words. Theme: Order & Chaos (Cycle 44).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
