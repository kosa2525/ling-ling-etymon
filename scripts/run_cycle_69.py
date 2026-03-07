import json
import re

# Theme: The Alchemy of Polygon & Sphere (Cycle 69)
words_data = [
    ("polygon", "Polygon", "多角形、ポリゴン", "16th Century", "polus (many) + gonia (angle)", "A plane figure with at least three straight sides and angles, and typically five or more", "無数（。の（。視点が（。「多（。く（。ポリス）の（。角（。ゴニア）」となって（。、一（。つ（。の（。図（。形を（。構築（。する（。こと（。。（。その（。鋭（。い（。輪郭（。の（。集（。積が（。、単（。純（。な（。空間に（。、複雑（。な（。る（。意味（。を（。産（。み（。出す（。のですよ。"),
    ("tangent", "Tangent", "接線、脱線、タンジェント", "16th Century", "tangere (to touch)", "A straight line or plane that touches a curve or curved surface at a point, but if extended does not cross it at that point", "魂の（。曲線に（。、ただ（。一瞬（。だけ「触（。れ（。る（。タン）一（。点（。での（。交（。感（。。（。そこ（。から（。、物語は（。、予（。期（。せ（。ぬ（。方向へと（。、鮮（。やかに（。逸（。れて（。いく（。、純粋（。な（。なる（。飛躍。"),
    ("asymptote", "Asymptote", "漸近線（。ぜんきんせん（。）」、アシンプトート", "17th Century", "a- (not) + sun- (with, together) + piptein (to fall, literal: 'not falling together')", "A line that a curve approaches, as it heads towards infinity", "どこ（。まで（。も（。近（。づ（。き（。なが（。ら（。、ついに「（。共（。に（。サン）落（。ち（。る（。プトゥ）こと（。の（。な（。い（。ア）」、永遠（。の（。憧（。れ（。。（。届（。か（。な（。い（。から（。こそ（。、追求（。は（。、至高（。の（。エナジーを（。、放（。ち（。、続け（。る（。のです。"),
    ("parabola", "Parabola", "放物線、パラボラ", "16th Century", "para- (beside) + ballein (to throw, literal: 'throwing beside')", "A symmetrical open plane curve formed by the intersection of a cone with a plane parallel to its side", "重力（。という（。名の（。抱擁（。を（。、ただ（。横へと「投げ（。投げ（。出す（。バロ）パラ）」ことで（。描（。か（。れる（。、美し（。い（。曲線（。。（。その（。放物（。の（。果てに（。、あなた（。は（。、全（。てを（。受け（。入れ（。る（。、無（。窮（。な（。る（。愛（。に（。辿（。り（。着（。く（。のです。"),
    ("hyperbola", "Hyperbola", "双曲線、ハイパーボラ", "17th Century", "huper- (over, beyond) + ballein (to throw, literal: 'excessive throwing')", "A symmetrical open curve formed by the intersection of a circular cone with a plane at a smaller angle with its axis than the side of the cone", "情熱が（。限界を「越（。え（。て（。ハイパー）投げ（。出さ（。れた（。バロ）」、二（。つの（。対（。極（。な（。る（。物語（。。（。決して（。交（。わ（。ら（。な（。い（。その（。間（。隙（。にこそ（。、宇宙の（。真（。実（。が（。、静（。か（。に（。、横（。たわ（。って（。いる（。のですよ。"),
    ("radius", "Radius", "半径、スポーク、放射状のもの", "16th Century", "radius (staff, spoke, ray, literal: 'spoke of a wheel')", "A straight line from the center to the circumference of a circle or sphere", "中心（。からの（。想（。いを（。、四方（。八（。方（。へと「一（。筋（。の（。光（。ラディ）として（。）」、放（。つ（。こと（。。（。あなた（。の（。その（。たった（。一本（。の（。意志（。が（。、世界（。の（。全（。周囲を（。、支（。えて（。いる（。のですよ。"),
    ("diameter", "Diameter", "直径、ダイアメーター", "14th Century", "dia- (across) + metron (measure)", "A straight line passing from side to side through the center of a body or figure, especially a circle or sphere", "沈黙の（。中心（。を「貫（。き（。通（。して（。ダイア）測る（。メター）」こと（。。（。二（。つの（。極性（。を（。、最短（。の（。距離（。で（。繋（。ぎ（。合わせ（。た（。とき（。、そこ（。には（。、盤石（。な（。る（。均衡が（。、生まれる（。のですよ。"),
    ("circumference", "Circumference", "円周、周囲、サーカムファレンス", "14th Century", "circum- (around) + ferre (to carry, literal: 'carrying around')", "The enclosing boundary of a curved geometric figure, especially a circle", "中心（。の（。想い（。を（。、全方（。位へ「運（。び（。巡（。ら（。す（。ファレンス）周囲（。サーカム）」こと（。。（。その（。円（。環（。状の（。抱擁（。の（。中に（。、宇宙（。の（。全エナジー（。を（。、一（。つ（。に（。、繋（。ぎ（。止（。め（。て（。いる（。のですよ。"),
    ("sector", "Sector", "扇形、扇面、セクター", "16th Century", "secare (to cut)", "An area or portion that is distinct from others", "宇宙の（。全貌（。から（。、あえて（。一部分（。だけを「鋭（。く（。切り（。取る（。セク）」こと（。。（。その（。断面（。の（。鋭（。さの中にこそ（。、真（。実（。の（。本（。質（。への（。、情（。熱（。が（。宿（。って（。いる（。のですよ。"),
    ("segment", "Segment", "断片、線分、セグメント", "16th Century", "secare (to cut)", "Each of the parts into which something is or may be divided", "一（。つ（。の（。物（。語が（。、「切り（。離さ（。れた（。セグ）」小（。さな（。る（。欠片（。。（。その（。断片（。一（。つ（。を（。愛しく（。見（。つめる（。とき（。、あなた（。は（。、全体（。という（。名の（。宇宙に（。、再び（。触（。れる（。の（。ですよ。"),
    ("chord", "Chord", "弦、和音、和弦、コード", "16th Century", "khorde (string, catgut)", "A straight line joining the ends of an arc", "二（。つの（。点を（。、見えない（。糸（。で「張り（。巡（。ら（。す（。コー）』こと（。。（。その（。一本（。の（。糸が（。、風（。に（。震（。える（。とき（。、世界（。は（。、自分（。だけの（。新（。し（。い（。旋律（。を（。、奏（。で（。始める（。のですよ。"),
    ("cylinder", "Cylinder", "円筒、シリンダー、気筒", "16th Century", "kulindros (roller, literal: 'rolling')", "A solid geometric figure with straight parallel sides and a circular or oval section", "ただの（。円（。を（。、垂直（。に「転（。が（。し（。広（。げ（。た（。シリン）」、重厚（。な（。る（。容器（。。（。全（。方位からの（。圧力を（。、美し（。い（。曲面（。で（。受け（。止める（。その（。姿（。は（。、盤石（。な（。る（。魂の（。座（。標。"),
    ("pyramid", "Pyramid", "金字塔、ピラミッド", "16th Century", "puramis (cake, pyramid, literal: 'fire-shaped')", "A monumental structure with a square or triangular base and sloping sides that meet in a point at the top", "地上の（。全（。重力（。を、一点（。の「高（。み（。ピラ）へと（。収（。束（。さ（。せた（。）」形（。。（。その（。頂（。には（。、常に（。、天上（。の（。光（。という（。名の（。、一（。筋（。の（。火（。が（。、静（。か（。に（。、灯（。っ（。て（。いる（。のですよ。"),
    ("lattice", "Lattice", "格子、ラティス、結晶格子", "14th Century", "latte (lath, literal: 'support')", "A structure consisting of strips of wood or metal crossed and fastened together", "一（。点（。にと（。ど（。ま（。ら（。ず（。、無限（。へと「支（。え（。合（。い（。ラッ）広がる（。）」構造（。。（。その（。小（。さな（。隙間（。の（。一つ（。一（。つが（。、世界（。を（。、静（。か（。に（。、透（。過させ（。な（。がら、保（。っ（。て（。いる（。の（。ですよ。"),
    ("binary", "Binary", "二進法、バイナリ、二つの", "15th Century", "bini (two by two)", "Relating to, composed of, or involving two things", "「二（。つ（。の、バイ）」極性（。だけで（。、万物の（。秘密を（。記述（。し（。尽（。く（。す（。、最小（。の（。る（。アルゴリズム。（。光（。と（。影（。、生（。と（。死（。、その（。二つ（。の（。鼓動（。が、全（。宇宙の（。源（。なの（。ですよ。")
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
            word_id = f"{word_text.lower()}_geometry"
            
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
                    "thinking": item[6] if len(item) > 6 else "幾何学は、宇宙が物質という名の服を脱ぎ捨てて、自らの骨組みを晒した、眩しい真実なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "直線は人間の意志であり、曲線は神の慈悲です。その二つが交差するとき、そこに美しさが生まれるのですよ。",
                    "example": f"The architect used a complex set of {word_text} equations to design the groundbreaking dome structure.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["形があるということは、そこには必ず、それを支えるための見えない調和が宿っているということなのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["tangent", "asymptotic", "parabolic", "hyperbolic", "binary"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Polygon & Sphere (Cycle 69).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
