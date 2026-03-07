import json
import re

# Theme: The Alchemy of Paradox & Truth (Cycle 40)
words_data = [
    ("paradox", "Paradox", "逆説、パラドックス", "16th Century", "para- (contrary to) + doxa (opinion)", "A seemingly absurd or self-contradictory statement or proposition that when investigated or explained may prove to be well founded or true", "一見（。常識（。という「正しき（。ドクサ）の見解に（。反して（。パラ）」いる（。ように（。見えて（。、その（。深淵（。では（。より（。大きな（。真理を（。指（。し示して（。いる（。、知性の（。迷宮。"),
    ("irony", "Irony", "皮肉、アイロニー", "16th Century", "eironeia (dissimulation, feigned ignorance)", "The expression of one's meaning by using language that normally signifies the opposite, typically for humorous or emphatic effect", "真実を（。直接（。語る（。代わりに（。、あえて「無知を（。装（。う（。エイロン）」ことで（。、世界（。の（。矛盾（。を（。鮮やかに（。浮（。き（。彫（。りに（。する（。、知的な（。微笑（。み。"),
    ("oxymoron", "Oxymoron", "撞着語法、矛盾語法、オクシモロン", "17th Century", "oxus (sharp) + moros (dull, foolish)", "A figure of speech in which apparently contradictory terms appear in conjunction", "「鋭（。さ（。オクス）」と（。「愚か（。さ（。モロス）」を（。一（。つに（。繋（。げる（。ように（。、正反対の（。言葉を（。衝突（。させる（。ことで（。、一瞬（。の（。閃光（。と（。深（。い（。余韻（。を（。産む（。、言葉の（。錬金術。"),
    ("ambiguity", "Ambiguity", "曖昧さ、多義性", "14th Century", "ambi- (both) + agere (to drive, do)", "The quality of being open to more than one interpretation; inexactness", "一つの（。正解に（。辿（。り（。着く（。のを（。止め（。、「両（。方の（。アンビ）意味へと（。心を（。駆（。り（。立て（。アグ）る（。）」こと（。。（。その（。揺（。ら（。ぎ（。の中にこそ（。、真実（。の（。豊（。かさが（。潜（。んで（。いる（。のですよ。"),
    ("nuance", "Nuance", "ニュアンス、微妙な差異", "18th Century", "nuer (to shade, cloud)", "A subtle difference in or shade of meaning, expression, or sound", "白（。か（。黒（。かで（。割り（。切れ（。ない（。、色彩（。の「影（。雲・ニュー）」のような（。微妙（。な（。変化（。。（。その（。繊細（。（。な（。震（。えに（。気づ（。ける（。か（。どうか（。が（。、魂の（。解像度（。を（。決める（。のです。"),
    ("subtle", "Subtle", "微妙な、繊細な", "14th Century", "sub- (under) + tela (web)", "So delicate or precise as to be difficult to analyze or describe", "あからさま（。な（。表現の（。、「ヴェール（。網・テラ）の（。下（。サブ）に（。隠（。された（。）」、極めて（。小さな（。、けれど（。決定（。的な（。違い（。。（。静（。かな（。観察（。だけを（。許（。す（。、精神の（。洗練。"),
    ("profound", "Profound", "深い、深遠な", "14th Century", "pro- (before, forward) + fundus (bottom)", "Very great or intense", "表面（。を（。滑（。る（。のを（。止め（。、はるか「底（。フンド）まで（。突き（。抜（。け（。プロ）て（。行く（。）」こと（。。（。そこ（。には（。、日常（。の（。喧騒（。が（。届（。かない（。、永遠（。の（。静寂（。が（。広が（。って（。いる（。の（。ですよ。"),
    ("fabricated", "Fabricated", "捏造された、組み立てられた", "15th Century", "fabrica (craft, trade, workshop)", "Constructed or manufactured, especially from prepared components", "自然（。に（。生まれた（。もので（。はなく（。、「工房（。ファブリカ）で（。意図的に（。作ら（。れた（。）」、偽り（。か（。、あるいは（。高度（。な（。技術の（。結晶（。か。"),
    ("simulated", "Simulated", "模造の、シミュレートされた", "17th Century", "similis (like, similar)", "Manufactured in imitation of some other material", "本物（。と「似（。て（。いる（。シミリス）」けれど（。、そこ（。には（。魂（。の（。拍動が（。欠（。落（。して（。いる（。、数学的（。で（。冷（。徹（。な（。複製。"),
    ("replicate", "Replicate", "複製する、繰り返す", "16th Century", "re- (again) + plicare (to fold)", "Make an exact copy of; reproduce", "一度（。作ら（。れた（。歴史を（。、「再び（。リ）折り（。畳（。み（。プリカ）重（。ねる（。）」ことで（。、同（。じ（。かたち（。を（。産（。み（。出し（。続ける（。こと（。。（。永遠（。の（。反復（。。"),
    ("finite", "Finite", "有限の、限定された", "14th Century", "finire (to finish, limit)", "Having limits or bounds", "いつか（。必ず（。終（。わり（。フィニ）が（。来る（。）」という（。、残酷（。な（。までに（。美しい（。制約（。。（。限り（。が（。ある（。から（。こそ（。、この（。一瞬（。は（。、これ（。ほどまでに（。眩（。しい（。のですよ。"),
    ("knot", "Knot", "結び目、難題、ノット", "Old English", "cnotta", "A fastening made by tying a piece of string, rope, or something similar", "バラバラの（。糸（。が（。、運命の（。いた（。ずら（。によって「固く（。絡（。み（。合った（。）」場所（。。（。解（。く（。か（。、あるいは（。アレク（。サ（。ンダーの（。ように（。一（。閃（。する（。か。"),
    ("grain", "Grain", "穀物、木目、質感", "13th Century", "granum (seed, kernel)", "Wheat or any other cultivated cereal crop used as food", "厚い（。皮の（。奥底に（。秘め（。られた「種子（。グラナム）」の（。ように（。、物質（。や（。物語の（。最小（。の（。単位（。。（。その（。小さな（。ざら（。つき（。こそが（。、存在の（。手触り。"),
    ("eclipse", "Eclipse", "食、日食、月食、失墜", "14th Century", "ek- (out) + leipein (to leave)", "An obscuring of the light from one celestial body by the passage of another between it and the observer or between it and its source of illumination", "輝かしい（。光が（。、運命の（。影に（。よって「一時的に（。立ち去（。る（。ライプ）外（。エ）」こと（。。（。その（。暗闇（。の中で（。、私たちは（。本当（。の（。光の（。ありが（。たみ（。を（。知（。る（。のですよ。"),
    ("zenith", "Zenith", "天頂、絶頂、ゼニス", "14th Century", "samt ar-ras (way of the head)", "The time at which something is most powerful or successful", "自分（。の（。真（。上（。、頭上（。「頭（。ラス）の（。方向（。サント）」に（。ある（。、運命（。の（。最高（。点（。。（。届（。き（。そうで（。届（。かない（。、光（。り（。輝（。く（。一瞬。"),
    ("nadir", "Nadir", "どん底、天底、ナディア", "15th Century", "nazir (opposite)", "The lowest point in the fortunes of a person or organization", "絶頂の「真反対（。ナジル）」に（。位置（。する（。、深淵（。なる（。底（。。（。そこ（。は（。、絶望の（。場所である（。と（。同時に（。、上向きの（。上昇（。が（。始まる（。、聖なる（。出発点。"),
    ("pinnacle", "Pinnacle", "尖塔、頂上、絶頂", "14th Century", "pinna (wing, point)", "The most successful point; the culmination", "ただ（。高い（。だけでなく（。、まるで「翼（。ピンナ）の（。尖（。端（。）」のように（。、鋭（。く（。天（。を（。突（。く（。、孤高（。な（。高み。"),
    ("vortex", "Vortex", "渦、渦巻き、ヴォルテックス", "17th Century", "vertere (to turn)", "A mass of whirling fluid or air, especially a whirlpool or whirlwind", "エナジーが「激しく（。回転し（。ヴァ）続ける（。）」ことで（。、周囲（。の（。全（。てを（。中心（。へと（。飲（。み（。込（。んで（。いく（。、深淵（。なる（。引力。"),
    ("spiral", "Spiral", "螺旋、スパイラル", "16th Century", "speira (coil, twist)", "Winding in a continuous and gradually widening (or tightening) curve, either around a central point on a flat plane or about an axis so as to form a cone", "同じ（。場所を（。回（。って（。いる（。ようで（。いて（。、実は（。常に向こう側へと「ねじ（。れ（。スペイラ）ながら（。）」進み（。続けて（。いる（。、進化（。という（。名の（。曲線。"),
    ("helix", "Helix", "螺旋、ヘリックス", "16th Century", "helissein (to roll, twist)", "An object having a three-dimensional shape like that of a wire wound uniformly in a single layer around a cylinder or cone, as in a corkscrew or a spiral staircase", "生命の（。根源（。の（。設計図。二つの（。糸が「ねじれ（。ヘリッ）ながら（。）」一つに（。なる（。ことで（。、永遠（。に（。続く（。物語。"),
    ("tangent", "Tangent", "接線、タンジェント", "16th Century", "tangere (to touch)", "A straight line or plane that touches a curve or curved surface at a point, but if extended does not cross it at that point", "本（。質（。を（。追いこす（。のではなく（。、ただ一瞬だけ（。優しく「触（。れ（。タン）る（。）」こと（。。（。その（。触（。れ（。合い（。が（。、思（。わ（。ぬ（。方向（。へと（。思索（。を（。導（。く（。のです。"),
    ("converge", "Converge", "収束する、一点に集まる", "17th Century", "com- (together) + vergere (to incline, turn)", "Tend to meet at a point", "バラバラの（。意志が（。、いつしか「一つに（。コン）向（。き（。ヴァ）揃（。う（。）」こと（。。（。混沌（。から（。一つの（。真実（。が（。浮（。き（。彫（。りに（。なる（。、調和の（。瞬間。"),
    ("diverge", "Diverge", "分岐する、逸れる", "17th Century", "di- (apart) + vergere (to incline, turn)", "Tend to be different or develop in different directions", "一つの（。正解を（。捨て（。、あえて「離れた（。ディ）方向へと（。向（。く（。ヴァ）」こと（。。（。そこ（。から（。新しい（。冒険（。と（。個性（。が（。始（。まる（。の（。ですよ。"),
    ("intersect", "Intersect", "交差する、横切る", "16th Century", "inter- (between) + secare (to cut)", "Divide by passing or lying across it", "違う（。時間（。を（。生きて（。いた（。者同士が（。、不意に（。相手の「道（。インター）を（。切（。る（。セク）ように（。）」交（。わる（。こと（。。（。その（。交（。点（。に（。、運命（。の（。火花（。が（。散（。る（。のです。"),
    ("crystallize", "Crystallize", "結晶化する、具体化する", "16th Century", "krustallos (ice)", "Form or cause to form crystals", "形（。の（。ない（。思考（。や（。熱が（。、冷徹な（。理性に（。よって「氷（。クリス）の（。ように（。固（。ま（。る（。）」こと（。。（。透明で（。硬度な（。、揺るぎ（。ない（。確信（。への（。変容。")
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
            word_id = f"{word_text.lower()}_truth"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "真実は、常に矛盾という名の美しいドレスを纏っています。",
                    "example": f"The story is filled with {word_text} that keep the readers thinking for days.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["矛盾を受け入れること、それが本当の知性の始まりです。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["paradox", "irony", "ambiguity", "nuance", "subtle", "profound", "fabricated", "simulated", "finite"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Paradox & Truth (Cycle 40).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
