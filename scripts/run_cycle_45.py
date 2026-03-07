import json
import re

# Theme: The Alchemy of Sound & Silence (Cycle 45)
words_data = [
    ("melody", "Melody", "旋律、メロディ", "13th Century", "melos (song) + aeidein (to sing)", "A sequence of single notes that is musically satisfying", "心（。を（。震（。わせ（。る「歌（。メロス）」を（。、言葉（。という（。地上に「歌（。い（。エイデ）上げ（。た（。）」もの（。。（。バラバラな（。瞬間に（。、一つの（。美しい（。線（。を（。通す（。、魂の（。軌跡。"),
    ("cadence", "Cadence", "抑揚、終止形、カデンツ", "14th Century", "cadere (to fall)", "A modulation or inflection of the voice", "高（。まっ（。た（。高（。揚（。が（。、静かなる（。着地点へと「落（。ち（。て（。カデ）行く（。）」こと（。。（。その（。終わりの（。美し（。さが（。、次の（。沈黙を（。より（。深（。く（。する（。の（。ですよ。"),
    ("tempo", "Tempo", "テンポ、速度、時代", "17th Century", "tempus (time)", "The speed at which a passage of music is or should be played", "単なる（。速さ（。ではなく（。、今（。という「時間（。テンパス）」の（。刻（。み（。その（。もの（。。（。あなた（。の（。心臓（。の（。鼓動が（。描き出す（。、生命（。の（。固有（。のリズム。"),
    ("reverberation", "Reverberation", "残響、反響、リバーブ", "16th Century", "re- (again) + verberare (to beat, strike)", "Prolongation of a sound; resonance", "放たれた（。音が（。、壁を「激しく（。叩き（。ヴァーブ）再び（。リ）戻って（。くる（。）」こと（。。（。音（。その（。もの（。が（。消（。え（。た（。後（。に（。残（。る（。、不可視の（。余韻。"),
    ("sonic", "Sonic", "音の、音速の、ソニック", "20th Century", "sonus (sound)", "Relating to or using sound waves", "空気（。を（。震（。わせる（。、「響き（。ソヌス）」その（。もの（。。（。目（。には（。見えない（。けれど（。、確（。かに（。世界を（。揺さ（。ぶ（。って（。いる（。、不可視の（。エナジー。"),
    ("acoustic", "Acoustic", "音響の、アコースティック", "17th Century", "akouein (to hear)", "Relating to sound or the sense of hearing", "道具（。に（。頼（。ら（。ず（。、ただ「聴（。く（。アコ）」こと（。を（。通じて（。、相手（。と（。直（。接（。繋（。が（。ろ（。う（。とする（。、誠実（。な（。響き。"),
    ("metronome", "Metronome", "メトロノーム", "19th Century", "metron (measure) + nomos (law)", "A device used by musicians that marks time at a selected rate by giving a regular tick", "時を（。恣意（。的に（。流（。す（。のを（。止め（。、厳格な「秩序（。ノモス）という（。度（。盛り（。メトロン）」に（。自らを（。律（。する（。こと（。。（。正確な（。反復（。が（。、自由な（。芸術（。を（。支（。える（。、静かなる（。背骨。"),
    ("symphonia", "Symphonia", "合奏、調和、シンフォニア", "14th Century", "sun- (together) + phone (voice, sound)", "An instrumental interlude in a large-scale vocal work", "異（。なる（。魂が（。、「共に（。サン）一つの（。響き（。フォン）」を（。奏（。で（。る（。こと（。。（。摩擦（。さえも（。、長い（。物語の（。中で（。、一つ（。の（。美（。しい（。線（。へと（。収束（。し（。て（。いく（。のです。"),
    ("lyric", "Lyric", "歌詞、抒情詩、リリック", "16th Century", "lyra (lyre, a stringed instrument)", "Relating to or denoting a type of poetry that explores the poet's personal interpretation of and feelings about the world", "かつて（。は「竪（。琴（。ライラ）の（。音（。色（。に（。合わせて（。）」語（。ら（。れた（。、魂の（。独白（。。（。言葉（。が（。音楽を（。求（。めて（。、震（。えて（。いる（。状態。"),
    ("stanza", "Stanza", "節、連、スタンザ", "16th Century", "stare (to stand, stop)", "A group of lines forming the basic recurring metrical unit in a poem; a verse", "言葉（。の流れ（。を（。一度「止める（。スタ）場所（。）」。（。そこ（。に（。用意（。さ（。れた（。真空の（。空間（。が（。、次（。に（。来る（。エナジーを（。、より（。強（。烈（。に（。し（。て（。くれる（。のですよ。"),
    ("aria", "Aria", "アリア、独唱曲、詠唱", "18th Century", "aer (air)", "A long accompanied song for a solo voice, typically one in an opera or oratorio", "物語（。を（。中（。断し（。、ただ「空気（。エア）その（。もの」と（。なって（。、自ら（。の（。情熱を（。高（。らかに（。歌（。い（。上げる（。こと（。。（。孤独（。な（。まで（。の（。、至高（。の（。自己（。肯定。"),
    ("ensemble", "Ensemble", "アンサンブル、合議、一揃い", "18th Century", "com- (together) + simul (at same time)", "A group of musicians, actors, or dancers who perform together", "個々の（。エゴ（。を（。手放（。し（。、「同時（。に（。シムル）共に（。コン）在（。る（。）」こと（。。（。そこ（。には（。、一（。人（。では（。辿（。り（。着（。け（。ない（。、巨大（。な（。調和（。の（。頂（。が（。あります。"),
    ("prelude", "Prelude", "前奏曲、プレリュード", "16th Century", "pre- (before) + ludere (to play)", "An introductory piece of music, most commonly an orchestral opening to an act of an opera, the first movement of a suite, or a piece preceding a fugue", "本（。題に（。入る（。前（。に（。、予見（。を（。込めて「あらかじめ（。プレ）奏（。で（。る（。ルード）」遊び（。。（。そこ（。には（。、これから（。始まる（。物語の（。全記憶（。が（。、密（。かに（。宿（。って（。いる（。のですよ。"),
    ("sonata", "Sonata", "ソナタ、奏鳴曲", "17th Century", "sonare (to sound)", "A composition for an instrumental soloist, often with a piano accompaniment, typically in several movements with one or more in sonata form", "言葉（。を（。持（。た（。ず（。、ただ（。純粋（。な「響き（。ソナ）だけ（。）」で（。、宇宙の（。真理を（。語（。ろ（。う（。とする（。、静（。か（。な（。る（。対話。"),
    ("ballad", "Ballad", "バラード、民謡、舞曲", "15th Century", "ballare (to dance)", "A poem or song narrating a story in short stanzas", "ただ（。聴（。く（。のではなく「共に（。踊（。る（。バラ）ために（。）」、人々が（。口（。ず（。さん（。だ（。短い（。物語（。。（。土（。の（。匂（。い（。と（。、消（。え（。な（。い（。愛の（。記憶。"),
    ("lullaby", "Lullaby", "子守唄、ララバイ", "16th Century", "lull (to soothe) + by (bye-bye)", "A quiet, gentle song sung to send a child to sleep", "この（。世界の（。残酷（。さを（。一度（。忘れ（。、「静かに（。ラル）眠（。らせる（。）」ための（。、優（。し（。い（。祈り（。の（。波（。）。", "あなた（。の（。言葉（。が（。、誰（。かの（。魂を（。そっと（。抱き（。し（。める（。、「ララバイ（。子守唄）」に（。なり（。ます（。ように。"),
    ("requiem", "Requiem", "安魂曲、鎮魂歌、レクイエム", "14th Century", "re- (again) + quies (rest, quiet)", "A Mass for the repose of the souls of the dead", "戦（。い（。を（。終（。わ（。らせ（。、魂を「再び（。リ）静寂（。クイエ）へと（。）」誘（。う（。ための（。、最後（。の（。旋律（。。（。悲（。し（。み（。を（。越え（。て（。、命の（。軌跡を（。祝福（。する（。ための（。祈り。"),
    ("dissonance", "Dissonance", "不協和音、不一致、ディソナンス", "15th Century", "dis- (apart) + sonare (to sound)", "A lack of harmony among musical notes; a tension or clash resulting from the combination of two disharmonious or unsuitable elements", "お互いの（。響きが（。「離（。れて（。ディ）鳴（。る（。ソン）」こと（。。（。その（。鋭（。い（。摩擦（。が（。、いつか（。高（。次元な（。調和へと（。至（。る（。ための（。、不可避な（。プロセス（。なの（。ですよ。"),
    ("polyphony", "Polyphony", "多声音楽、ポリフォニー", "19th Century", "polu- (many) + phone (voice, sound)", "The style of simultaneously combining a number of parts, each forming an individual melody and harmonizing with each other", "一（。つの（。正解（。に（。集約（。さ（。れ（。ず（。、「多（。くの（。ポリ）声（。フォン）」が（。バラバラに（。あり（。な（。がら（。、一つの（。タペストリーを（。織（。り（。上げて（。いく（。、自由な（。響き。"),
    ("interval", "Interval", "音程、間隔、インターバル", "14th Century", "inter- (between) + vallum (wall)", "An intervening time or space", "音（。と（。音の（。間に（。用意（。さ（。れた「壁（。ヴァル）の（。間（。インター）」。（。その（。空白（。こそが（。、次（。に（。来る（。音を（。輝（。か（。せ（。、意味を（。産（。み（。出す（。のですよ。"),
    ("chromatic", "Chromatic", "半音階の、色彩豊かな、クロマチック", "17th Century", "khroma (color)", "Relating to or using notes not belonging to the diatonic scale of the key in which a passage is written", "単なる（。白（。と（。黒（。ではなく（。、数（。え（。切（。れ（。ない（。「色彩（。クロマ）」の（。中（。を（。縫（。い（。合わせる（。こと（。。（。全（。て（。の色を（。受け（。入れ（。、一歩（。一歩（。を（。大切に（。刻（。む（。姿勢。"),
    ("crescendo", "Crescendo", "クレッシェンド、次第に大きく", "18th Century", "crescere (to grow)", "A gradual increase in loudness in a piece of music", "エナジーが「育（。ち（。クレセ）行く（。）」が（。ままに（。、世界（。の（。解像度（。を（。上（。げて（。いく（。こと（。。（。小（。さな（。一歩（。が（。、いつしか（。宇宙（。を（。揺（。さ（。ぶ（。る（。うねり（。に（。成（。る（。のですよ。"),
    ("vibrato", "Vibrato", "ビブラート、震え", "19th Century", "vibrare (to shake)", "A rapid, slight variation in pitch in singing or playing some musical instruments, producing a stronger or richer tone", "一点（。に（。固（。執（。せず（。、魂を「震（。え（。ヴィブラ）させる（。）」こと（。。（。その（。ゆら（。ぎの中に（。、この（。世の（。あり（。と（。あらゆる（。情緒が（。宿（。って（。いる（。のですよ。"),
    ("soprano", "Soprano", "ソプラノ、最高音域", "18th Century", "supra (above)", "The highest of the four standard singing voices", "地上（。の（。泥（。から（。遥（。かに「上（。スープラ）の高み」へと（。至（。り（。、天の（。光を（。直（。接（。言葉（。に（。変える（。、純粋（。な（。る（。祈り。", "あなた（。の中（。の（。最も（。高貴（。な（。エッセンスを（。、言葉（。という（。名の「ソプラノ」で（。世界に（。放（。って（。ください。"),
    ("tenor", "Tenor", "テノール、趣旨、持続", "14th Century", "tenere (to hold)", "A singing voice between baritone and alto or countertenor, the highest of the ordinary adult male range", "ただ（。歌う（。のではなく（。、物語（。の（。中核（。を「しっかりと（。把（。持（。して（。テネ）離（。さない（。）」、情熱的（。な（。る（。持続。")
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
            word_id = f"{word_text.lower()}_sound"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "音楽は、言葉が沈黙したときに初めて聞こえてくる、宇宙の囁きです。",
                    "example": f"The orchestra performed a moving {word_text} that touched the hearts of the audience.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["音とは、静止した物質を、再びエナジーへと還すための魔法の振動なのです。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["sonic", "acoustic", "chromatic", "staccato", "legato"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Sound & Silence (Cycle 45).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
