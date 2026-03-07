import json
import re

# Theme: The Alchemy of Prism & Spectrum (Cycle 59)
words_data = [
    ("prism", "Prism", "プリズム、分光器、角柱", "16th Century", "prisma (something sawed, literal: 'sawing')", "A glass or other transparent object in the form of a prism, especially one that is triangular with refracting surfaces at an acute angle with each other and that separates white light into a spectrum of colors", "一つ（。に（。見えた（。光を「挽（。き（。切（。る（。プリズマ）」ように（。、色（。鮮（。やかに（。分（。解（。する（。こと（。。（。その（。透明な（。幾（。何（。学の（。中に（。、宇宙の（。全色彩の（。秘密が（。、隠されて（。いる（。のですよ。"),
    ("spectrum", "Spectrum", "分光、スペクトル、範囲", "17th Century", "specere (to look)", "A band of colors, as seen in a rainbow, produced by separation of the components of light by their different degrees of refraction according to wavelength", "ただ（。眺める（。のではなく（。、そこに（。ある（。全（。てを「一（。目（。で見（。抜（。く（。スペク）」ための（。、光（。の（。帯（。。（。美しい（。色彩から（。、見えない（。エナジーまで（。、全（。ては（。一つの（。連続（。体な（。のです。"),
    ("refraction", "Refraction", "屈折、屈折率", "16th Century", "re- (back) + frangere (to break)", "The fact or phenomenon of light, radio waves, etc. being deflected in passing obliquely through the interface between one medium and another or through a medium of varying density", "境界線を（。越える（。とき（。、光（。が「後ろ向きに（。リ）折（。り（。曲（。げ（。られる（。フラク）」こと（。。（。その（。鋭（。い（。変化（。が（。、世界に（。奥行（。き（。と（。、眩（。しい（。多様（。性を（。産（。み（。出す（。のですよ。"),
    ("diffraction", "Diffraction", "回折（。かいせつ（。）」、ディフラクション", "17th Century", "dis- (apart) + frangere (to break)", "The process by which a beam of light or other system of waves is spread out as a result of passing through a narrow aperture or across an edge, typically accompanied by interference between the wave forms produced", "障害物（。に（。ぶ（。つ（。かり（。、光（。が「バラバラに（。ディ）砕（。け（。散（。る（。フラク）」こと（。。（。回り（。込み（。、滲（。み（。出す（。その（。エナジーは（。、目（。には（。見えない（。場所（。にも（。、愛（。を（。届（。けて（。くれ（。る（。のですよ。"),
    ("opacity", "Opacity", "不透明さ、不透明度", "16th Century", "opacus (shaded, dark)", "The condition of lacking transparency or translucence; opaqueness", "光（。を（。通さ（。ず（。、ただ「影を（。作（。る（。オパ）」こと（。。（。その（。強（。烈（。な（。遮（。断が（。、物体（。に（。確（。かな（。る（。実（。態（。と（。、触（。れる（。こと（。のできる（。重みを（。与（。えて（。いる（。のですね。"),
    ("translucency", "Translucency", "半透明さ、半透明性", "17th Century", "trans- (across) + lucere (to shine)", "The quality of allowing light, but not detailed images, to pass through; semitransparency", "全（。てを（。見せ（。ず（。、ただ「光だけを（。向こう（。側へと（。トランス）通（。す（。ルス）」こと（。。（。曖昧（。な（。その（。向こう（。側に（。、私たちは（。宇宙の（。深遠（。な（。夢を（。見（。る（。のですよ。"),
    ("brilliance", "Brilliance", "輝き、明密、卓越", "18th Century", "berillus (beryl, a precious stone)", "Intense brightness of light", "磨（。き（。抜（。かれた（。、「宝石（。ベリル）」のような（。、峻烈（。な（。る（。閃（。光（。。（。あなた（。の（。魂が（。、最高（。の（。密度（。へと（。至（。った（。とき（。、世界（。は（。その（。眩（。し（。さに（。、息（。を（。呑（。む（。のです。"),
    ("luster", "Luster", "光沢、艶、輝き", "16th Century", "lustrare (to illuminate, purify, literal: 'purification ceremony')", "A gentle sheen or soft glow, especially that of a partly reflective surface", "ただの（。反射（。ではなく（。、内側（。から「浄（。化さ（。れた（。ルスト）」ような（。、穏（。や（。かな（。る（。輝き（。。（。その（。静（。かな（。る（。気高さこそ（。、真（。の（。知性（。の（。証（。とい（。え（。る（。で（。しょ（。う。"),
    ("shimmer", "Shimmer", "微かな光、ゆらめく光、シマー", "Old English", "scimerian (to shine, glitter)", "Shine with a soft tremulous light", "一（。点（。に（。留（。ま（。ら（。ず（。、風（。の（。ように「ゆら（。ゆら（。と（。震（。える（。シム）」光（。。（。その（。危（。うい（。ゆら（。ぎの中にこそ（。、この（。世（。の（。あり（。と（。あらゆる（。情緒（。が（。宿（。って（。いる（。のですよ。"),
    ("dazzle", "Dazzle", "幻惑する、眩ませる、ダズル", "15th Century", "daze + -le", "Brightness that confuses someone's vision", "光（。の（。強（。烈（。な（。一（。閃（。によって（。、思考（。を「麻（。痺（。さ（。せる（。デイズ）」こと（。。（。一度（。、全（。て（。を（。見失（。っ（。て（。こそ（。、あなた（。は（。、新（。しい（。世界を（。視（。る（。ことが（。できる（。のですよ。"),
    ("glare", "Glare", "ぎらつく光、睨みつける", "14th Century", "glāren (to shine, glare)", "Strong and dazzling light", "優（。し（。さを（。捨て（。、ひたすら「鋭（。く（。輝く（。グレア）」こと（。。（。その（。挑（。戦（。的な（。眩（。しさは（。、停（。滞（。し（。た（。日常に（。、風（。穴を（。空（。ける（。ための（。、峻烈（。な（。る（。意志。"),
    ("iris", "Iris", "虹彩、虹、アイリス", "14th Century", "iris (rainbow)", "A flat, colored, ring-shaped membrane behind the cornea of the eye, with an adjustable circular opening (pupil) in the center", "目（。の中に（。宿る「虹（。イーリス）」のかけ（。ら（。。（。それは（。、外（。界の（。エナジーを（。、あなた（。固有（。の（。色彩へと（。変（。え（。て（。、内なる（。宇宙へと（。届（。けて（。くれ（。る（。、聖（。なる（。門（。なの（。ですよ。"),
    ("pupil", "Pupil", "瞳孔、生徒、ピューピル", "14th Century", "pupilla (little doll, doll in the eye, literal: 'little girl')", "The dark circular opening in the center of the iris of the eye, varying in size to regulate the amount of light reaching the retina", "瞳（。の（。奥底に（。映（。り（。込（。んだ（。、「小さな（。自分（。パピラ）』。（。あなた（。が（。世界を（。見（。つめる（。とき（。、世界（。も（。また（。、あなた（。を（。愛しく（。見（。つめ（。返（。して（。いる（。の（。ですよ。"),
    ("vista", "Vista", "眺望、見通し、ヴィスタ", "17th Century", "visto (seen)", "A pleasing view, especially one seen through a long, narrow opening", "遮（。る（。もの（。を（。捨て（。去り（。、ただ「見（。渡（。さ（。れた（。ヴィスタ）」果（。て（。。（。その（。広（。大な（。広（。がりの中に（。、あなた（。の（。魂は（。、再び（。自由な（。翼（。を（。取り（。戻（。す（。の（。ですよ。"),
    ("twilight", "Twilight", "薄明、夕暮れ、トワイライト", "14th Century", "twi- (two) + light", "The soft glowing light from the sky when the sun is below the horizon, caused by the refraction and scattering of the sun's rays from the atmosphere", "昼（。と（。夜、二（。つの「光（。の（。間（。トワイ）」に（。横たわ（。る、曖（。昧（。な（。時間（。。（。そこ（。には（。、全（。ての（。境（。界が（。溶け（。去り（。、精（。霊（。たちが（。囁（。き（。始める（。、磁（。力的な（。る（。調和が（。あります。")
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
                    "thinking": item[6] if len(item) > 6 else "光とは、宇宙が自らを知るための、眩しい実験なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "色彩は、透明な真理が耐えきれなくなって、この世界に溢れ出した喜びの歌なのです。",
                    "example": f"The scientist used a {word_text} to decompose the white light into its spectral components.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["見るという行為は、世界を一方的に観察することではなく、光を通して世界と愛を交わすことなのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["translucent", "transparent", "focal"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Prism & Spectrum (Cycle 59).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
