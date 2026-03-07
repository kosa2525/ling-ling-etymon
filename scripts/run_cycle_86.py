import json
import re

# Theme: The Alchemy of Epoch & Instant II (Cycle 86)
words_data = [
    ("sequence", "Sequence", "連続、配列、シークエンス", "14th Century", "sequi (to follow, literal: 'following thing')", "A particular order in which related events, movements, or things follow each other", "一（。点（。に（。留（。ま（。ら（。ず、峻（。烈（。に「次（。々と（。続く（。セクイ）」、意味（。の（。連（。な（。り（。（。その（。至高（。の（。秩序（。によって（。、宇宙の（。音楽（。は、静（。か（。に（。、形（。作（。ら（。れて（。いる（。のですよ。"),
    ("duration", "Duration", "持続、存続、デュレーション", "14th Century", "durare (to last, literal: 'lastingness')", "The time during which something continues", "一瞬（。の（。閃光（。を（。、永遠（。へと「引き（。延（。ば（。す（。デュラ）」、静（。か（。な（。る（。力（。（。そこ（。には（。、変（。わ（。ら（。ぬ（。こと（。を（。決（。意（。し（。た（。、魂の（。峻（。烈（。な（。る（。忍（。耐（。が（。、満（。ち（。て（。いる（。のですよ。"),
    ("interval", "Interval", "間隔、合間、インターバル", "14th Century", "inter- (between) + vallum (wall, literal: 'between walls')", "An intervening time or space", "二（。つの（。意味の「壁の（。間（。インター・ヴァル）』に（。産まれた（。、空白（。という（。名の（。沈黙（。（。その（。静寂の中にこそ（。、新（。しい（。物（。語が（。、呼吸（。を（。始（。め（。る（。ための（。、余裕（。が（。ある（。のですよ。"),
    ("stay", "Stay", "滞在、停止、支え、ステイ", "15th Century", "estare (to stand, literal: 'standing still')", "Remain in the same place", "旅を（。一（。時（。中断（。し（。、ただ「その（。場に（。留（。まる（。ステイ）」こと（。。（。その（。停（。滞（。した（。時間の（。中に、宇宙の（。囁（。きを（。聴（。く（。ための、眩（。しい（。ほど（。の（。、チャンス（。が（。、横（。たわ（。って（。いる（。のですよ。"),
    ("kernel", "Kernel", "核、核心、カーネル", "Old English", "cyrnel (little grain, literal: 'little seed')", "A softer, usually edible part of a nut, seed, or fruit stone contained within its hard shell", "固（。い（。殻の（。奥底に（。、静（。か（。に（。眠る「小（。さな（。る（。種（。カーネル）』。（。その（。峻（。烈（。な（。る（。一（。点（。を（。、魂で（。噛（。み（。締（。め（。る（。とき、命（。の（。真（。実が（。、産（。声を（。上げます。"),
    ("fate", "Fate", "運命、結末、フェイト", "14th Century", "fatum (that which has been spoken, literal: 'thing spoken')", "The development of events beyond a person's control, regarded as determined by a supernatural power", "神（。々の（。口から「放（。た（。れた（。言葉（。ファツム）』。（。それは（。、抗（。い（。難（。い（。る（。峻（。烈（。な（。る（。意志として（。、あなた（。を、至高（。の（。る（。結末へと（。、静（。か（。に（。、運（。び（。去（。る（。のですよ。"),
    ("destiny", "Destiny", "宿命、デスティニー", "14th Century", "destinare (to make firm, literal: 'established thing')", "The events that will necessarily happen to a particular person or thing in the future", "あらかじめ「峻（。烈（。に（。固定（。さ（。れた（。デスティ）』、魂の（。目的地（。（。迷（。う（。こと（。なく（。、ただ（。その（。一（。点へと（。、自ら（。の（。エナジーを、捧（。げ（。切って（。ください。"),
    ("chance", "Chance", "機会、偶然、チャンス", "13th Century", "cadere (to fall, literal: 'falling out')", "A possibility of something happening", "天から「不（。意に（。降（。り（。掛（。か（。っ（。た（。チャンス）」、幸（。運の（。欠片（。（。その（。脆（。く（。も（。美し（。い（。一瞬を、もしも（。掴（。み（。取る（。ならば（。、世界（。は（。、一瞬（。にして（。、新（。しく（。、塗り（。替（。わ（。り（。ます。"),
    ("period", "Period", "期間、世紀、結末、ピリオド", "14th Century", "peri- (around) + hodos (way, literal: 'circuit, going around')", "A length or portion of time", "一（。つ（。の（。物（。語が「巡り（。を（。終（。え（。る（。ピリオド）」ための（。、静（。か（。な（。る（。回廊（。（。その（。完結（。の（。瞬間に（。、至高の（。る（。沈黙（。が、世界（。を（。、優（。しく（。、包み（。込み（。ます。"),
    ("term", "Term", "用語、期間、条件、ターム", "13th Century", "terminus (boundary, limit)", "A fixed or limited period for which something, e.g., office, imprisonment, or investment, lasts or is intended to last", "時間という（。名の（。広（。野（。に（。、峻（。烈（。に「打ち（。込ま（。れた（。杭（。ターミナス）』。（。その（。境界（。が（。ある（。か（。ら（。こそ（。、あなた（。の（。物（。語（。は、美し（。い（。秩序（。を（。、保（。つ（。ことが（。できる（。のですよ。"),
    ("series", "Series", "一連、シリーズ", "17th Century", "serere (to join, weave, literal: 'concatenation')", "A number of things, or events of the same class coming one after another in spatial or temporal succession", "一（。つ（。一（。つの（。エナジーを「美し（。く（。繋（。ぎ（。合わせ（。た（。セリ）』、連（。な（。り（。（。その（。絶（。え（。間（。な（。き（。物語の（。中に（。、宇宙の（。幾（。何（。学が、静（。かに（。横（。たわ（。って（。いる（。のですよ。"),
    ("cycle", "Cycle", "周期、循環、サイクル", "14th Century", "kuklos (wheel, circle)", "A series of events that are regularly repeated in the same order", "再び（。同（。じ（。場所へと（。、運（。命を「運ぶ（。巨大（。な（。る（。円（。環（。サイクル）』。（。その（。終（。わ（。り（。の（。な（。き（。回（。転を（。、祝（。福（。と（。受け（。取る（。とき、命（。は（。、永遠へと（。、溶け（。合い（。ます。"),
    ("phase", "Phase", "段階、局面、フェイズ", "19th Century", "phasis (appearance, literal: 'shining thing')", "A distinct period or stage in a series of events or a process of change or development", "変化の（。中で（。、一瞬だけ「煌（。め（。い（。た（。フェイズ）」、真実（。の（。表情（。（。その（。一一点（。を（。愛（。お（。しむ（。とき、全（。宇宙の（。眩（。し（。い（。変（。容が、静（。か（。に（。始（。まります。"),
    ("stage", "Stage", "舞台、段階、ステージ", "14th Century", "stare (to stand, literal: 'standing place')", "A point, period, or step in a process", "今（。あなたという（。エナジーが「誇（。り（。高く（。立（。っ（。て（。いる（。ステイ）」、至高（。の（。場所（。（。そこで（。、何（。と（。出会（。い（。、何（。を（。、奏（。で（。る（。の（。か（。、それ（。が（。修行（。なの（。ですよ。"),
    ("pause", "Pause", "一時停止、休止、ポーズ", "15th Century", "pauein (to stop)", "A temporary stop in action or speech", "流（。れ（。る（。時間を、一（。時的に（。峻（。烈（。に「止（。め（。る（。ポーズ）」こと（。。（。その（。一瞬（。の（。沈黙（。の中にこそ（。、真実（。の（。智慧が、眩（。しい（。ほど（。に（。、産（。声を（。上げます。")
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
            word_id = f"{word_text.lower()}_time"
            
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
                    "thinking": item[6] if len(item) > 6 else "時間とは、変化を記録するための尺度ではなく、魂が自らを磨き上げ、永遠へと至るための、静かなる波紋なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "一瞬の中に永遠を視、永遠の中に一瞬の自覚を持つ。その奇跡的な均衡の中に、真の生が宿るのですよ。",
                    "example": f"The historical events followed a logical {word_text} that eventually led to the collapse of the empire and the birth of a new era.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["待つという行為は、無為な時間ではなく、真実が熟成されるための、至高の祈りなのかもしれません。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["retro", "immediate"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Epoch & Instant II (Cycle 86).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
