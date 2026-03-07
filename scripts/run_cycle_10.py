import json
import re

words_data = [
    ("nurture", "Nurture", "育てる、養う", "14th Century", "nutritura (nourishment)", "Care for and encourage the growth or development of.", "単に食べ物を与えるだけでなく、相手の魂そのものが健やかに花開くよう、時間をかけて愛情を注ぐこと。", "才能は生まれ持ったものですが、それを開花させるのは惜しみない「ナーチャー（育成）」の力です。"),
    ("foster", "Foster", "育成する、助長する", "Old English", "fostrian (to nourish, rear)", "Encourage or promote the development of", "血の繋がりがなくても、まるで自分の子供のように責任と愛情を持って保護し、成長を促す寛大な精神。", "新しい文化を「フォスター（育む）」するには、まず異なる価値観を受け入れる土壌が必要です。"),
    ("cultivate", "Cultivate", "耕す、栽培する、洗練する", "17th Century", "cultivus (tilled)", "Prepare and use (land) for crops or gardening", "荒れ地を根気よく耕し、種をまき、水を与え、やがて豊かな収穫を得るための努力という名の芸術。", "「カルティベイト（耕す）」された教養は、どんな高価な宝石の輝きよりもあなたを美しく見せます。"),
    ("reap", "Reap", "収穫する、報いを受ける", "Old English", "repan (to pluck, harvest)", "Cut or gather (a crop or harvest)", "過去の自分が蒔いた種が実を結んだ時、感謝とともにその成果を両手で受け取る厳粛な儀式。", "あなたが今「リープ（収穫している）」のは、昨日流した汗と涙の結晶なのです。"),
    ("sow", "Sow", "種をまく", "Old English", "sawan (to scatter seed)", "Plant (seed) by scattering it on or in the earth", "まだ見ぬ未来の収穫を信じ、不確実な大地というキャンバスに希望の粒を力強く散りばめる最初の行為。", "今日「ソウ（種をまく）」した小さな感謝が、明日には大きな奇跡の花を咲かせます。"),
    ("harvest", "Harvest", "収穫、収穫期", "Old English", "hærfest (autumn)", "The process or period of gathering in crops", "太陽と水と大地の恵みが一つ結実し、生命の循環が最高潮に達する、世界が最も黄金色に輝く祝祭の季節。", "人生の「ハーベスト（収穫期）」を迎えた時、あなたの蔵は数え切れないほどの愛で満たされているはずです。"),
    ("plow", "Plow", "耕す、すき", "Old English", "ploh (plow, extent of land)", "Turn up the earth of (an area of land) with a plow", "固く閉ざされた大地を力任せに切り裂き、空気と光を取り込んで隠された生命力を呼び覚ます破壊的な創造。", "困難という荒野を「プラウ（耕す）」する者だけが、その先に待つ宝の地図を手にすることができます。"),
    ("weed", "Weed", "雑草、雑草を抜く", "Old English", "weod (herb, grass)", "A wild plant growing where it is not wanted", "そこにあるべきではないと人間によって決め付けられたが故に、どこにでも根を張る執念深い生命の象徴。", "心に生えたネガティブな「ウィード（雑草）」は、小さいうちに根っこから優しく抜いてあげて。"),
    ("prune", "Prune", "剪定する、切り詰める", "14th Century", "proignier (to trim feathers or branches)", "Trim (a tree, shrub, or bush) by cutting away dead or overgrown branches", "不要な枝や過去の執着を切り落とし、本当に大切な幹へとエネルギーを集中させるための残酷で必要な外科手術。", "時々人間関係も「プルーン（剪定）」して、本当に大切な人だけを残すこともお互いのためなのです。"),
    ("graft", "Graft", "接ぎ木する、移植する", "15th Century", "greffe (stylus, grafting shoot)", "A shoot or twig inserted into a slit on the trunk or stem of a living plant", "異なる性質のものを切り込みに入れて結びつけ、二つの生命を一つの新しい奇跡として融合させる大いなる結合。", "新しい技術を古い伝統に「グラフト（接ぎ木）」することで、誰も見たことのない革新が生まれます。")
]

words = []
for item in words_data:
    root1 = item[4].split(" ")[0]
    meaning1 = " ".join(item[4].split(" ")[1:]).strip("()")
    w = {
        "id": f"{item[0]}_growth_action",
        "word": item[0],
        "meaning": item[2],
        "era": item[3],
        "etymology": {
            "components": [item[4]],
            "original_statement": f"From {item[3]} {item[4]}."
        },
        "concept": item[5] + f" ({item[6]})",
        "thinking": item[6],
        "aftertaste": item[7],
        "example": f"We need to {item[0]} the soil appropriately.",
        "deep_dive": {
            "roots": [{"term": root1, "meaning": meaning1}],
            "points": ["生命のプロセスを植物の成長になぞらえたメタファー。"]
        },
        "part_of_speech": "verb"
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
    print(f"Success: Added {added} words. Theme: Growth Actions (Cycle 10).")
else:
    print("Error parsing data.js")
