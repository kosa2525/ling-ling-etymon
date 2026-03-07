import json
import re

# Theme: The Alchemy of Echo & Resonance (Cycle 70)
words_data = [
    ("reverberation", "Reverberation", "残響（ざんきょう）、反響、リバーブ", "17th Century", "re- (again) + verberare (to beat, literal: 'beating back again')", "Prolongation of a sound; resonance", "声が（。闇を「再び（。リ）打（。つ（。ヴァー）」ことで（。生まれる（。、静（。かな（。る（。余韻（。。（。その（。消（。え（。入（。る（。まで（。の（。時間の（。中に（。、私たちは（。、過去の（。エナジーを（。、今も（。、感（。じ（。取（。る（。ことが（。できる（。のですよ。"),
    ("cadence", "Cadence", "抑揚（。よくよう（。）」、韻律（。、カデンツ", "14th Century", "cadere (to fall, literal: 'falling')", "A modulation or inflection of the voice", "言葉が（。、美し（。い（。終止（。に向かって「落（。ち（。て（。カデ）行く（。）」リズム。（。その（。一瞬の（。沈黙（。への（。着（。地が（。、物（。語（。に、盤石（。な（。る（。完成（。を（。、与（。えて（。くれる（。のですよ。"),
    ("timbre", "Timbre", "音色、音質、ティンバー", "19th Century", "tympanon (drum)", "The character or quality of a musical sound or voice as distinct from its pitch and intensity", "ただの（。波長（。ではなく（。、魂の（。厚（。みを「太（。鼓（。ティンパン）の（。ように（。）」伝える（。もの（。。（。あなた（。固有（。の（。その（。響（。き（。が（。、世界（。に（。、た（。った（。一（。つの（。存在（。の（。証（。を（。刻（。む（。のですよ。"),
    ("discord", "Discord", "不協和音、不一致、ディスコード", "13th Century", "dis- (apart) + cor (heart, literal: 'hearts apart')", "Lack of harmony between notes sounded together", "二（。つの「心（。コル）が（。離（。れ（。離（。れ（。ディ）」になって（。奏（。で（。る（。、鋭（。い（。響（。き（。。（。その（。不（。均（。衡（。の（。刺（。激（。が、時に（。、新しい（。調和（。を（。産（。み出す（。ための（。、エナジーと（。な（。る（。の（。ですよ。"),
    ("overtone", "Overtone", "倍音（ばいおん）、含み、オーバートーン", "19th Century", "over + tone", "A musical tone that is a part of the harmonic series above a fundamental note and may be heard with it", "主（。な（。旋律の「上（。オーバー）に（。う（。っ（。す（。ら（。と（。）」重（。な（。る（。、見（。え（。な（。い（。響（。き（。。（。そこ（。には（。、語（。ら（。れ（。な（。い（。真実（。が（。、密（。かに（。、宿（。って（。いる（。のですよ。"),
    ("harmonic", "Harmonic", "倍音、和声的な、ハーモニック", "14th Century", "harmos (joint, literal: 'fitting together')", "Relating to or characterized by musical harmony", "バラバラ（。な（。響（。きが（。、美し（。く「結（。び（。合（。わ（。さ（。れ（。ハルモ）」た（。もの（。。（。その（。整（。合（。性（。が（。、世界（。を（。、一（。つ（。の（。巨大（。な（。祈り（。へと（。、変（。え（。て（。いく（。のですよ。"),
    ("ensemble", "Ensemble", "合奏、アンサンブル、総体", "18th Century", "insul (together, at the same time, literal: 'at once')", "A group of musicians, actors, or dancers who perform together", "異（。な（。る（。意志が「一（。斉（。に（。アン（。ス）奏（。で（。る（。）」こと（。。（。個（。を（。捨て（。去（。り（。、ただ（。一（。つ（。の（。調（。和の中（。に（。溶（。け（。る（。とき（。、あなた（。は（。宇宙の（。一部（。に（。な（。る（。のです。"),
    ("recital", "Recital", "独（。奏（。会（。、暗（。唱（。、リサイタル", "16th Century", "re- (again) + citare (to cite, literal: 'summon again')", "The performance of a program of music by a soloist or small group", "かつて（。の（。旋律を（。、再び（。「呼び（。起こ（。す（。サイタル）」儀（。式（。。（。あなた（。の（。その（。真（。摯（。な（。る（。復（。唱（。が（。、停（。滞（。し（。た（。時間（。に、美（。し（。い（。脈動（。を（。与（。える（。のです。"),
    ("hymn", "Hymn", "賛美歌、ヒム、聖歌", "Old English", "humnos (song of praise, literal: 'song')", "A religious song or poem, typically of praise to God or a god", "天上の（。光を（。、地上（。の「言葉（。ヒム）に（。変（。えた（。）」歌（。。（。その（。清（。廉（。な（。る（。響（。き（。は（。、孤独（。な（。魂（。を（。、静（。か（。に（。、癒（。し（。て（。くれる（。のですよ。"),
    ("whisper", "Whisper", "囁（ささや）き、耳打ち、ウィスパー", "Old English", "hwisprian (to whisper)", "A soft or confidential way of speaking, typically using the breath with the lips and tongue", "空気（。を（。震（。わ（。す（。、一（。瞬（。の「吐（。息（。ウィスパー）』。（。大（。声（。では（。到底（。伝わ（。ら（。な（。い（。、真実（。の（。想（。いが、そこには（。、宿（。って（。いる（。のですよ。"),
    ("murmur", "Murmur", "ざわめき、つぶやき、マーマー", "14th Century", "murmure (murmur, literal: 'soft sound')", "A soft, indistinct sound made by a person or group of people speaking quietly or at a distance", "遠（。く（。の（。川（。の（。流れ（。の（。ように（。、静（。か（。に「重（。な（。り（。合う（。マーマー）」声（。。（。その（。曖（。昧（。な（。響（。きの中に（。、宇宙（。の（。全（。ての（。エナジーが（。、溶（。け（。込（。んで（。いる（。のですよ。"),
    ("song", "Song", "歌、歌曲、ソング", "Old English", "sang (song)", "A short poem or other set of words set to music or meant to be sung", "言葉（。が（。、重力を（。振り切り（。、「飛翔（。サング）し（。始（。めた（。）」かたち（。。（。あなた（。が（。声（。を（。放（。つ（。とき（。、世界（。は（。、今（。一度（。、新（。しく（。産まれ（。変わる（。のですよ。"),
    ("echo", "Echo", "山（。び（。こ、こだま、エコー", "14th Century", "Ekho (mountain nymph who pined away for love until only her voice remained)", "A sound or series of sounds caused by the reflection of sound waves from a surface back to the listener", "自（。分（。を（。失（。い（。、ただ「声（。エコー）だけ（。が（。残（。った（。）」女神（。の（。嘆（。き（。。（。その（。反射（。の（。中に（。、あなた（。は（。、忘（。れ（。去（。っ（。た（。はず（。の（。、自分（。自身（。の（。魂に（。出会（。う（。の（。ですよ。"),
    ("resonance", "Resonance", "共鳴、レゾナンス", "15th Century", "re- (again) + sonare (to sound, literal: 'sounding back')", "The quality in a sound of being deep, full, and reverberating", "一（。つ（。の（。響（。きが（。、全（。て（。の（。場所に「再び（。リ）響（。き（。渡（。る（。ソナ）」こと（。。（。魂（。と（。魂が（。、見（。え（。な（。い（。境界（。を（。越（。えて（。、一（。つ（。に（。な（。る（。、至高（。の（。交（。感（。点。"),
    ("silence", "Silence", "沈黙、静寂、サイレンス", "12th Century", "silere (to be silent)", "The complete absence of sound", "全（。て（。を（。飲み（。込み（。、ただ「静（。まり（。返る（。シレ）」こと（。。（。音（。の（。な（。い（。その（。海（。の中にこそ（。、真（。実（。の（。言葉（。が（。、静（。か（。に（。、育（。ま（。れて（。いる（。のですよ。")
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
            word_id = f"{word_text.lower()}_echo"
            
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
                    "thinking": item[6] if len(item) > 6 else "響きは、魂がこの世界に触れた瞬間の震えであり、沈黙はその震えを永遠にするための器なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "こだまは、過去の自分が今の自分に問いかけている、静かなる囁きなのですよ。",
                    "example": f"The long {word_text} in the ancient cathedral enhanced the sacred and mystical atmosphere of the service.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["聴くという行為は、単に音を捉えることではなく、自分自身を静止させて、世界の拍動を迎え入れることなのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["harmonic", "melodic"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Echo & Resonance (Cycle 70).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
