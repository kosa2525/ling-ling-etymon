import json
import re

# Theme: The Alchemy of Ghost & Shadow (Cycle 52)
words_data = [
    ("specter", "Specter", "亡霊、スペクター、不気味なもの", "16th Century", "specere (to look)", "A ghost; a haunting fear of future trouble", "肉体（。を（。失い（。ながら（。も（。、ただ（。相手に「見（。られる（。スペ）こと（。）」を（。求めて（。彷徨（。う（。もの（。。（。過去（。の（。暗（。い（。情熱が（。、今（。も（。そこに（。留（。ま（。って（。いる（。、不（。気（。味（。な（。残（。像。"),
    ("phantom", "Phantom", "幻、幽霊、ファントム", "13th Century", "phaintesthai (to appear)", "A ghost; a figment of the imagination", "そこに（。存在（。する（。のでは（。なく（。、ただ（。光（。の（。迷（。い（。によって「現（。れ（。た（。ファン）」影（。。（。その（。危（。うい（。眩（。しさが（。、真実（。を（。隠（。し（。去（。る（。のですよ。"),
    ("apparition", "Apparition", "出現、亡霊、離現（。りげん（。）」", "15th Century", "ad- (to) + parere (to come forth, appear)", "A ghost or ghostlike image of a person", "何（。も（。ない（。場所（。から（。、不（。意に「現（。れ（。て（。パラ）来る（。アド）」こと（。。（。それは（。、宇宙の（。深淵（。から（。届いた（。、一通（。の（。無（。言（。の（。手紙（。の（。ような（。存在。"),
    ("residue", "Residue", "残余、かす、レジデュー", "14th Century", "re- (back) + sedere (to sit)", "A small amount of something that remains after the main part has gone or been taken or used", "全（。てが（。去（。り（。行（。っ（。た（。後（。に（。、ただ（。そこに「後ろ向きに（。リ）座（。り（。続（。け（。て（。いる（。セド）」沈黙（。。（。それが（。、かつての（。烈（。しい（。情熱の（。、最後（。の（。証言（。なのです。"),
    ("haunt", "Haunt", "（幽霊が）出没する、つきまとう、たまり場", "13th Century", "ham (home) + et (little)", "Of a ghost manifest itself at a place regularly; be persistently in the mind of someone", "かつて（。は（。安（。ら（。ぎの「小さな（。エ）家（。ハム）」だった（。はずの（。場所（。。（。今（。では（。、逃（。げ（。られ（。ない（。記憶（。の（。檻（。として（。、あなた（。を（。捕（。ら（。え（。続け（。て（。いる（。のですね。"),
    ("wraith", "Wraith", "生き霊、幽霊、生霊", "16th Century", "Origin uncertain, possibly related to guardian", "A ghost or ghostlike image of someone, especially one seen shortly before or after their death", "透明（。で（。、風（。の（。ように（。希薄（。な（。存在（。。（。けれど（。、その（。眼差し（。には（。、生者（。を（。も（。圧倒（。する（。、「守護（。する（。）」ほどの（。強力な（。意志が（。宿（。って（。いる（。のですよ。"),
    ("complex", "Complex", "複雑な、コンプレックス、複合体", "17th Century", "com- (together) + plectere (to weave, entwine)", "Consisting of many different and connected parts", "バラバラ（。の（。感情が（。、「共に（。コン）固く（。絡（。み合（。わ（。された（。プレク）」場所（。。（。それを（。解（。く（。のは（。容易（。ではない（。けれど（。、その（。中にこそ（。、あなたの（。真（。実（。の（。物語が（。眠（。って（。いる（。のです。"),
    ("fixation", "Fixation", "固執、固定、フィクセーション", "14th Century", "figere (to fasten, fix)", "An obsessive interest in or feeling about someone or something", "時間（。の（。流れ（。を（。止め（。、ただ一（。点（。に「心（。を（。釘付け（。に（。する（。フィク）」こと（。。（。その（。凍（。り付（。いた（。情熱が（。、あなた（。の（。成長（。を（。、静（。か（。に（。阻（。んで（。いる（。の（。かも（。しれ（。ません。"),
    ("trauma", "Trauma", "トラウマ、心の傷", "17th Century", "trauma (wound)", "A deeply distressing or disturbing experience", "かつて（。魂に（。刻まれた（。、「深（。い（。傷（。トラウマ）」。（。その（。痛み（。は（。、過去からの（。鳴（。り（。止（。ま（。ない（。鐘（。の（。ように（。、今（。も（。あなたの（。中（。で（。、響き（。続け（。て（。いる（。のですよ。"),
    ("relic", "Relic", "遺物、聖遺物、名残", "13th Century", "re- (back, behind) + linquere (to leave)", "An object surviving from an earlier time, especially one of historical or sentimental interest", "全（。てを（。捨て（。去（。った（。後に（。、ただ一つ「後ろ（。リ）に（。残さ（。れた（。リン）」もの（。。（。その（。小さな（。欠片（。には（。、時を（。超えた（。巨大な（。祈り（。が（。、封印（。されて（。いる（。のですよ。"),
    ("ruin", "Ruin", "廃墟、破滅、ルイン", "14th Century", "ruere (to fall down, rush)", "The physical destruction or disintegration of something or the state of disappearing or falling to pieces", "かつて（。の（。栄（。光（。が（。、重力（。という（。名の（。運命に（。抗（。え（。ず（。、「崩（。れ（。落ち（。た（。ルエ）」姿（。。（。その（。沈黙（。の（。中に（。、私たちは（。時間（。の（。残酷（。さと（。慈愛（。を（。同時（。に（。見（。る（。のですよ。"),
    ("discard", "Discard", "捨てる、見捨てる、ディスカード", "16th Century", "dis- (away) + card (playing card)", "Get rid of someone or something as no longer useful or desirable", "自分（。という（。名の（。勝負から（。、不要（。な「札（。カード）を（。遠くへと（。ディ）投げ（。出す（。）」こと（。。（。手（。放す（。勇気（。が（。、新（。しい（。カード（。を（。引く（。ための（。、スペース（。を（。創（。る（。のです。"),
    ("hollow", "Hollow", "空洞の、空虚な、うつろな", "Old English", "hol (hole, hollow place)", "Having a hole or empty space inside", "表面（。は（。立派（。でも（。、内側（。が「空（。っぽ（。ホル）」な（。存在（。。（。けれど（。、その（。虚無（。だからこそ（。、世界（。の（。全（。ての（。響き（。を（。、増幅（。し（。て（。受け（。止（。める（。ことが（。できる（。のですよ。"),
    ("matrix", "Matrix", "基盤、母体、計量、マトリックス", "14th Century", "mater (mother)", "An environment or material in which something develops; a surrounding medium or structure", "あら（。ゆる（。命（。を（。育（。む「母（。パテール）なる（。子（。宮（。）」。（。そこ（。には（。、宇宙（。の（。目（。に見え（。ない（。秩序（。が（。、網（。の（。目の（。ように（。、静（。か（。に（。張り（。巡らさ（。れて（。いる（。のです。"),
    ("scar", "Scar", "傷跡、スカー", "14th Century", "eskhara (scab, fireplace)", "A mark left on the skin or within body tissue where a wound, burn, or sore has not healed completely and fibrous connective tissue has developed", "烈（。しい（。火（。に（。焼（。かれ（。た（。後の「燃（。え（。残り（。エス）」。（。痛み（。は（。消えても（。、そこ（。には（。、あなたが（。生き（。抜（。いた（。という（。、誇（。り（。高い（。勲（。章（。が（。刻ま（。れて（。いる（。のですよ。")
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
            word_id = f"{word_text.lower()}_ghost"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "影は、光が存在するというたった一つの証明であり、同時に魂の休息場所です。",
                    "example": f"The old manor was said to be haunted by a quiet {word_text} that appeared during the full moon.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["不在とは、単なる欠落ではなく、そこに何かが存在したという強烈な記憶のことなのです。"]
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

        print(f"Success: Added {added_count} words. Theme: Ghost & Shadow (Cycle 52).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
