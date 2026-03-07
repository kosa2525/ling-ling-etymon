import json
import re

words_data = [
    ("sphere", "Sphere", "球体、天体、領域", "14th Century", "sphaira (ball, globe)", "A round solid figure, or an area of activity, interest, or expertise", "全ての表面の中心からの距離が等しく、尖った部分を排除して自己完結している最も美しく穏やかな「完璧な調和」。", "自分だけの狭い「スフィアー（影響圏）」から一歩外へ踏み出すことで、全く新しい可能性の星が見えます。"),
    ("globe", "Globe", "球、地球、地球儀", "16th Century", "globus (round mass, sphere)", "The earth, or a spherical representation of the earth", "ただの丸い物体ではなく、無数の生命と複雑な歴史をその表面に張り付けながら、宇宙を航海し続ける「青い奇跡の船」。", "「グローブ（地球）」は誰かの所有物ではなく、私たち全員が一時的に間借りしている巨大なキャンバスです。"),
    ("orb", "Orb", "球、宝珠、天体", "16th Century", "orbis (ring, circle, globe)", "A spherical body, typically an astronomical one or a royal emblem", "太陽や月のように、暗闇の中で自らの意志で輝き、神秘的で呪術的な力すら帯びているように感じられる「聖なる玉」。", "夜空に浮かぶ銀色の「オーブ（月）」は、古来より人々の祈りを一身に集める静かな宝石。"),
    ("cylinder", "Cylinder", "円柱", "16th Century", "kulindros (roller)", "A solid geometric figure with straight parallel sides and a circular or oval cross section", "上下の完璧な円と、それらを真っ直ぐに繋ぐ直線要素が織りなす「回転と前進」のための効率的なデザイン。", "レコード盤の溝は「シリンダー（円筒状）」の回転によって、過去の空気ごと今に再生します。"),
    ("cone", "Cone", "円錐、松ぼっくり", "16th Century", "konos (pine cone)", "A solid or hollow object that tapers from a circular or roughly circular base to a point", "強固で安定した底面を持ちながらも、天の一点に向かって「永遠の上昇」と収束を目指す、力強く集中したベクトル。", "「コーン（円錐形）」のアイスクリームは、終わりの尖った先っぽの一口が一番美味しいのです。"),
    ("pyramid", "Pyramid", "ピラミッド、角錐", "16th Century", "puramis (Egyptian pyramid)", "A monumental structure with a square or triangular base and sloping sides that meet in a point at the top", "地球の重量に逆らわず、自らの重みを安定の基盤としながら、王の魂を「一直線に星空へと送る」石の階段。", "どんな権力の「ピラミッド（頂点構造）」も、底辺の数多の犠牲なしには決して成立しません。"),
    ("cube", "Cube", "立方体、3乗", "16th Century", "kubos (cube, die)", "A symmetrical three-dimensional shape, either solid or hollow, contained by six equal squares", "全ての角が含まれ、面と長さが完全に均等であるという「不自然なまでの四角い論理」が支配する、人間の作り出した究極の秩序。", "人生は「キューブ（サイコロ）」のよう。出た目を受け入れ、それを使って最善のゲームをするしかないのです。"),
    ("prism", "Prism", "プリズム、角柱", "16th Century", "prisma (something sawed)", "A solid geometric figure whose two end faces are similar, equal, and parallel rectilinear figures", "単なる透明な石の壁ではなく、平凡な白い光を「七色の鮮やかなスペクトル」へと解剖し分解して世界を塗り替える魔法のレンズ。", "「プリズム（分光器）」のように、一つの視点だけでなく多角的に相手を見れば、隠れた魅力が溢れ出ます。"),
    ("spiral", "Spiral", "らせん、渦巻き", "16th Century", "spira (coil)", "Winding in a continuous and gradually widening curve, either around a central point on a flat plane or about an axis so as to form a cone", "全く同じ場所をグルグル回っているようでいて、実は「わずかずつ高く、あるいは深く」移動を続けているダイナミックな進化（または堕落）の軌跡。", "「スパイラル（螺旋的）」な成長こそが本物。時には後戻りしたように感じても、階層は確実に上がっています。"),
    ("helix", "Helix", "らせん状のもの", "16th Century", "helix (spiral)", "An object having a three-dimensional shape like that of a wire wound uniformly in a single layer around a cylinder", "生命の設計図であるDNAにも刻み込まれ、単独ではなく「二重になって互いに絡み合いながら」永遠に情報を繋いでいく聖なる螺旋の鎖。", "「ヘリックス（螺旋構造）」が示すように、私たちの人生も誰かの人生と美しく絡み合いながら進むのです。")
]

words = []
for item in words_data:
    meaning1 = "known origin"
    root1 = item[4]
    w = {
        "id": f"{item[0]}_shape",
        "word": item[0],
        "meaning": item[2],
        "era": item[3],
        "etymology": {
            "components": [item[4]],
            "original_statement": f"From {item[3]} {item[4]}."
        },
        "concept": item[5] + f" ({item[6]})",
        "thinking": item[6],
        "aftertaste": item[7] if len(item) > 7 else "形には、それぞれのエネルギーの方向があります。",
        "example": f"He modeled a perfect {item[0]}.",
        "deep_dive": {
            "roots": [{"term": root1, "meaning": meaning1}],
            "points": ["幾何学は、無秩序な世界に秩序を与えるための最も美しい言語。"]
        },
        "part_of_speech": "noun"
    }
    words.append(w)

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
if match:
    prefix, json_array_str, suffix = match.groups()
    existing_words = json.loads(json_array_str)
    existing_ids = {w.get("id") for w in existing_words}
    existing_word_texts = set(w.get("word").lower() for w in existing_words)
    
    added = 0
    for w in words:
        if w["id"] not in existing_ids and w["word"].lower() not in existing_word_texts:
            existing_words.append(w)
            added += 1
            existing_word_texts.add(w["word"].lower())
            
    new_content = content[:match.start()] + prefix + json.dumps(existing_words, ensure_ascii=False, indent='\t') + suffix + content[match.end():]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Success: Added {added} words. Theme: Shapes (Cycle 18).")
else:
    print("Error parsing data.js")
