import json
import re

# Theme: The Alchemy of Prism & Spectrum II (Cycle 81)
words_data = [
    ("refraction", "Refraction", "屈折、リフラクション", "16th Century", "re- (again) + frangere (to break, literal: 'breaking back')", "The fact or phenomenon of light, radio waves, etc. being deflected in passing obliquely through the interface between one medium and another or through a medium of varying density", "光（。が（。日常（。を（。越元（。る（。とき、境界（。で「再び（。リ）砕（。か（。れ（。る（。フラ）」こと（。。（。その（。歪（。みの中にこそ（。、真（。実（。の（。色彩が（。、静（。か（。に（。、産声を（。上げ（。て（。いる（。のですよ。"),
    ("diffraction", "Diffraction", "回折（。かいせつ（。）」、ディフラクション", "17th Century", "dis- (apart) + frangere (to break, literal: 'breaking apart')", "The process by which a beam of light or other system of waves is spread out as a result of passing through a narrow aperture or across an edge", "障害（。物に（。突き（。当たり（。、エナジーが「離（。れ（。離（。れ（。に（。ディ）砕（。け（。広（。がる（。フラ）」こと（。。（。その（。回り（。込む（。優（。し（。い（。眩（。し（。さが（。、暗黒（。の（。すみ（。ず（。み（。までを（。、静（。か（。に（。満た（。す（。のですよ。"),
    ("interference", "Interference", "干渉、妨害、インターフェレンス", "16th Century", "inter- (between) + ferire (to strike, literal: 'striking between')", "The combination of two or more electromagnetic waveforms to form a resultant wave in which the displacement is either reinforced or canceled", "二（。つの（。エナジーが「間（。インター）で（。ぶ（。つ（。か（。り（。合う（。フェレ）」こと（。。（。その（。衝突（。が（。、一き（。わ（。、美し（。い（。虹（。の（。文様を（。、この（。世（。に（。、描き（。出（。す（。のですよ。"),
    ("polarization", "Polarization", "偏光、偏極、ポラリゼーション", "19th Century", "polus (pole, axis, literal: 'axis-making')", "The action of restricting the vibrations of a transverse wave, especially light, wholly or partially to one direction", "全（。方位へと（。散（。っ（。て（。いた（。光を、「一（。つ（。の（。軸（。ポラ）へと（。整える（。）」こと（。。（。その（。峻（。烈（。な（。る（。意志（。が（。、世界（。を（。、透明（。な（。る（。秩序（。へと（。導（。く（。のですよ。"),
    ("luster", "Luster", "光沢、つや、ラスター", "16th Century", "lustrare (to illuminate, literal: 'brightness')", "A gentle sheen or soft glow, especially that of a partly reflective surface", "物体の（。奥底（。から、静（。かに「滲（。み（。出（。た（。ラス）」輝き。（。その（。控え（。め（。な（。煌（。めきは（。、あなたが（。そこに（。、確（。かな（。る（。エナジーを（。持（。っ（。て（。生き（。て（。いる（。、証（。なの（。ですよ。"),
    ("sheen", "Sheen", "光沢、美しさ、シーン", "14th Century", "sciene (bright, beautiful)", "A soft luster on a surface", "表面（。を（。優（。しく（。滑（。る（。、「美（。し（。い（。シーン）光（。の（。衣（。裳（。。（。その（。滑（。らかな（。る（。陶（。酔（。が（。、見（。慣（。れ（。た（。日常を（。、一瞬（。にして（。、神殿（。へと（。変元（。て（。しまう（。の（。ですよ。"),
    ("glint", "Glint", "きらめき、反射、グリント", "18th Century", "glentan (to flash, literal: 'flash')", "Give out or reflect small flashes of light", "沈黙の（。暗黒（。を、一（。瞬だけ「切り（。裂（。く（。グリン）」、鋭（。利な（。る（。火花（。（。その（。一一点（。の（。瞬きにこそ（。、魂（。の（。叫（。びが（。、静（。か（。に（。、宿（。って（。いる（。のですよ。"),
    ("twinkle", "Twinkle", "きらめき、またたき、トゥインクル", "Old English", "twinclin (to twinkle)", "Shine with a gleam that varies repeatedly between bright and faint", "遠（。い（。星の（。ように、優しく「震（。え（。続け（。る（。トゥイン）」光。（。その（。不（。安（。定（。な（。る（。美し（。さが（。、あなた（。を（。、永遠（。という（。名の（。、微（。睡（。みへと（。、誘（。う（。のですよ。"),
    ("nimbus", "Nimbus", "後光、光輪、ニンバス、雲", "17th Century", "nimbus (rain cloud, cloud of light)", "A luminous cloud or a halo surrounding a supernatural being or object", "頭（。上に（。、静か（。に（。漂（。う「光の（。雲（。ニンパス）』。（。その（。眩（。し（。い（。ヴェールが、あなた（。を、凡（。庸（。な（。る（。大地から（。、そっと（。、浮（。か（。せ（。て（。くれる（。のですよ。"),
    ("photon", "Photon", "光子、フォトン", "20th Century", "phos (light) + -on (particle)", "A particle representing a quantum of light or other electromagnetic radiation", "光という（。名の「根源（。の（。欠片（。フォト）』。（。一（。つ（。の（。粒子（。の中に（。、全（。宇宙の（。エナジーが（。、幾（。何（。学（。的（。な（。る（。美（。しさ（。で（。、封印（。さ（。れて（。いる（。のですよ。"),
    ("particle", "Particle", "粒子、微（。量（。、パーティクル", "14th Century", "pars (part, literal: 'little part')", "A minute portion of matter", "全（。体（。を（。構成する（。、小（。さな（。なる「部分（。パル）』。（。その（。一粒（。一粒（。を（。愛（。お（。しむ（。とき（。、あなた（。は（。、巨大（。な（。る（。物（。語（。の、真実（。の（。肌（。触（。りに（。、触（。れる（。のです。"),
    ("galaxy", "Galaxy", "銀河、銀河系、ギャラクシー", "14th Century", "gala (milk, literal: 'Milky Way')", "A system of millions or billions of stars, together with gas and dust, held together by gravitational attraction", "夜空を（。流（。れ（。る「母（。なる（。乳（。ガラ）の（。河）』。（。その（。膨（。大な（。る（。光の（。集（。積が（。、私たち（。に（。、孤独（。な（。祈り（。の（。行（。き（。先（。を、静（。か（。に（。指（。し（。し（。め（。し（。て（。いる（。のですよ。"),
    ("brilliance", "Brilliance", "光沢、才気、ブリリアンス", "17th Century", "berillus (beryl, jewel, literal: 'jewel-like')", "Intense brightness of light", "宝石（。ベリル（。のように（。、目（。も（。眩（。む（。ほど（。の「煌（。め（。き（。ブリリ）』。（。その（。圧倒（。的な（。る（。光が、あなた（。の（。内（。なる（。宇宙を（。、今（。一度（。、新（。しく（。、目（。覚め（。さ（。せる（。のですよ。"),
    ("flash", "Flash", "閃光、ひらめき、フラッシュ", "16th Century", "Middle English flasken (to sprinkle/dash water, of uncertain origin)", "A sudden brief burst of bright light", "一（。瞬にして（。、全（。てを（。塗り（。替（。える「光の（。飛沫（。フラッシュ）』。（。その（。峻（。烈（。な（。る（。一（。点（。に（。、全（。真実（。が（。、美し（。く（。凝縮（。さ（。れて（。いる（。のですよ。"),
    ("glow", "Glow", "輝き、白熱、グロウ", "Old English", "glōwan (to glow)", "A steady radiance of light or heat", "内（。側の（。情熱が（。、絶（。え（。間（。なく「滲（。み（。出し（。続け（。る（。グロウ）」こと（。。（。その（。温（。か（。な（。る（。余韻が（。、あなた（。の（。周囲（。を、静（。か（。に（。、愛（。で（。満た（。し（。て（。い（。く（。のですよ。")
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
            word_id = f"{word_text.lower()}_prism"
            
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
                    "thinking": item[6] if len(item) > 6 else "光は、宇宙が沈黙という名の服を脱ぎ捨てて、自らを発見しようとした瞬間のエナジーなのです。",
                    "aftertaste": item[7] if len(item) > 7 else "虹は、光が自らの限界を認めて、世界と和解した瞬間の祝福なのですよ。",
                    "example": f"The scientist used a powerful laser to study the {word_text} of atoms in the vacuum chamber.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["眩しすぎる光は、時として真実を隠してしまいます。微かなきらめきの中にこそ、真の物語が宿っているのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Prism & Spectrum II (Cycle 81).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
