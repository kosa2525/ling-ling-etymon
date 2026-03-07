import json
import re

words_data = [
    ("vast", "Vast", "広大な、莫大な", "16th Century", "vastus (empty, immense)", "Of very great extent or quantity; immense", "端を探そうと目を凝らしても、ただ無力感と圧倒的な美しさだけが視界を埋め尽くす果てしない虚空。", "夜空の「ヴァスト（見渡す限りの広大さ）」を見上げれば、自分の悩みがチリのようにちっぽけに思えます。"),
    ("spacious", "Spacious", "広々とした", "14th Century", "spatium (space)", "Having ample space", "息苦しい制約や障害物が一切存在せず、魂が手足をいっぱいに伸ばして深呼吸できる無条件の自由。", "心が淀んだときは、天井が高く「スペーシャス（広々とした）」な美術館で深呼吸を。"),
    ("capacious", "Capacious", "容積の大きい、包容力のある", "17th Century", "capax (able to hold)", "Having a lot of space inside; roomy", "どれだけ多くの異なる感情や出来事を次々と放り込んでも、全てを静かに飲み込んでくれる深い大きな器。", "彼女の「ケイペイシャス（許容量の大きな）」な心は、どんな理不尽な怒りも優しく受け止めてくれます。"),
    ("commodious", "Commodious", "広くて便利な", "15th Century", "commodus (convenient)", "Roomy and comfortable", "単に広いだけでなく、そこにいる者が一切の不自由を感じず、完璧な安らぎを享受できるように計算された完璧な調和。", "古き良き時代の「コモディアス（ゆったりと快適な）」なホテルでは、時間そのものがゆったり流れています。"),
    ("cramped", "Cramped", "窮屈な、狭苦しい", "16th Century", "crampe (cramp)", "Feeling or causing someone to feel uncomfortably confined", "物理的な狭さ以上に、そこから逃げ出せないという精神的な圧迫感が肺を押し潰そうとする息苦しい閉塞感。", "「クランプト（身動きも取れないほど窮屈な）」な通勤電車の中でこそ、心の中の広い空を想像して。"),
    ("narrow", "Narrow", "狭い、細い", "Old English", "nearwe (closely, narrowly)", "Of small width", "余裕や遊びの部分を極限まで削り落とし、一つの明確な目標を目指して真っ直ぐに突き進むストイックな集中線。", "「ナロー（細く険しい）」な道を選ぶ人間だけが、誰も見たことのない美しい頂からの景色を知っています。"),
    ("confined", "Confined", "限られた、閉じ込められた", "16th Century", "confinis (bordering)", "Restricted in area or volume; cramped", "見えない境界線によって「共に境界を引かれ」、自由な拡張を許されずにその場に留まることを強制された孤独。", "古い価値観に「コンファインド（閉じ込められた）」な状態から抜け出し、自分だけの新しい枠を作りましょう。"),
    ("infinite", "Infinite", "無限の", "14th Century", "in- (not) + finis (boundary)", "Limitless or endless in space, extent, or size", "「終わり」という概念そのものを否定し、人間の小さく脆弱な論理では決して測りきれない絶対的な拡大。", "あなたの中に眠る「インフィニット（限界のない）」な可能性を、誰の言葉にも制限させないでください。"),
    ("boundless", "Boundless", "境界のない、無制限の", "16th Century", "bound + less", "Unlimited; immense", "「ここから先は禁止」という見えないロープをすべて引きちぎり、好きなだけ遠くへ行けるという圧倒的な解放感。", "子どもの頃に感じた「バウンドレス（どこまでも自由な）」な好奇心を、大人になっても忘れないで。"),
    ("limitless", "Limitless", "無制限の", "16th Century", "limit + less", "Without end, limit, or boundary", "能力や資源が尽きるという不安がなくなり、ただひたすらに前へ前へと挑戦を続けることを許された神々の領域。", "「リミットレス（限界を知らない）」な情熱の前では、どんな高い壁もただの通過点にすぎません。")
]

words = []
for item in words_data:
    meaning1 = "known origin"
    root1 = item[4]
    w = {
        "id": f"{item[0]}_space",
        "word": item[0],
        "meaning": item[2],
        "era": item[3],
        "etymology": {
            "components": [item[4]],
            "original_statement": f"From {item[3]} {item[4]}."
        },
        "concept": item[5] + f" ({item[6]})",
        "thinking": item[6],
        "aftertaste": item[7] if len(item) > 7 else "限界を決めるのは、いつだって自分自身です。",
        "example": f"He stared into the {item[0]} darkness.",
        "deep_dive": {
            "roots": [{"term": root1, "meaning": meaning1}],
            "points": ["空間認識は、心の状態や可能性と深く連動しています。"]
        },
        "part_of_speech": "adjective"
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
    print(f"Success: Added {added} words. Theme: Space (Cycle 12).")
else:
    print("Error parsing data.js")
