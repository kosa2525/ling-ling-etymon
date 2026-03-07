import json
import re

words_data = [
    ("see", "See", "見る、見える", "Old English", "seon (to see)", "Perceive with the eyes; discern visually", "眼球というレンズを通して光を受け取り、ただ無意識に、受動的に、目の前の世界の表層を脳へと「入力させる」最も原始的な知覚。", "目を開けてただ「シー（見ている）」だけでは、真実は絶対にあなたの心には届きません。"),
    ("look", "Look", "見る、目を向ける", "Old English", "locian (to look)", "Direct one's gaze toward someone or something or in a specified direction", "視線を自らの強い意志で「特定の一点に向けて」動かし、対象の存在や状態を意図的に確認しようとする能動的なアクション。", "他人の意見など気にせず、自分が信じた道を真っ直ぐに「ルック（見据え）」ればいいのです。"),
    ("watch", "Watch", "じっと見る、見守る", "Old English", "wæccan (to keep awake, stay awake)", "Look at or observe attentively typically over a period of time", "対象が動いたり変化したりするのを見逃さないよう、文字通り「徹夜して起きている」ように、時間と労力をかけて監視し続ける忍耐。", "大人が子どもにできる最高のサポートは、手を出さずにただ「ウォッチ（見守って）」あげることです。"),
    ("stare", "Stare", "じっと見つめる、凝視する", "Old English", "starian (to look fixedly)", "Look fixedly or vacantly at someone or something with one's eyes wide open", "対象の持つ力に圧倒されたか、逆に相手を「威圧して屈服させようという意志」を持って、瞬きもせずに無遠慮に視線を固定すること。", "鏡の中の自分を「ステア（凝視）」するのはやめましょう。欠点ばかりが目についてしまいますから。"),
    ("gaze", "Gaze", "見つめる", "14th Century", "gapa (to gape, stare)", "Look steadily and intently, especially in admiration, surprise, or thought", "攻撃的な意図はなく、まるで美しい絵や神聖なものに魂を奪われたかのように、深い愛情や驚きをもって対象を「包み込むように」見つめる静寂。", "星空を「ゲイズ（うっとり見つめる）」しながら、私たちは遠い銀河と無言の会話を交わしているのです。"),
    ("glance", "Glance", "ちらっと見る", "15th Century", "glacier (to slip, slide)", "Take a brief or hurried look", "対象に視線を投げかけるが、決して深くは立ち入らず、表面を「滑るように」一瞬かすめてすぐに違う場所へと逃げていく臆病な確認。", "時計を「グランス（一瞥）」ばかりしていると、目の前の大切な人との時間を失ってしまいますよ。"),
    ("glimpse", "Glimpse", "ちらりと見えること", "15th Century", "glimsen (to shine faintly)", "A momentary or partial view", "見ようとする意志とは反して、対象の全体ではなくただ「ほんの一部」だけが、まるで幻のように一瞬だけ目に飛び込んでくる幸運（あるいは無念）。", "彼女の心の奥底にある悲しみを、あのふとした瞬間に「グリンプス（垣間見）」してしまった気がしました。"),
    ("peep", "Peep", "のぞき見する", "14th Century", "pipen (to pipe, chirp)", "Look quickly and furtively at something, especially through a narrow opening", "自分が安全な場所（隠れ家）にいることを確信しながら、壁の小さな穴から外の禁じられた世界を「こっそりと盗み見る」罪悪感と猛烈な好奇心。", "ドアの隙間から「ピープ（覗き見）」したプレゼントの山のことで、朝まで興奮して一睡もできませんでした。"),
    ("peer", "Peer", "じっと見る、見を凝らす", "16th Century", "piren (to look narrowly)", "Look keenly or with difficulty at someone or something", "暗闇や濃霧の中など、極めて視界が悪い状況において、対象の形をなんとか捉えようと「目を細めて必死に」限界の知覚を試みること。", "どれほど分厚い老眼鏡の奥から「ピア（目を凝らす）」しても、彼にはもう昔の笑顔は見えませんでした。"),
    ("scan", "Scan", "ざっと見る、スキャンする", "14th Century", "scandere (to climb, read poetry)", "Look at all parts of something carefully in order to detect some feature", "文字や風景などの広範囲な情報を、まるで機械のように規則正しく「端から端までなぞって」、特定の意味や危険を一気に探し出そうとする検索。", "混雑したパーティー会場を「スキャン（素早く見回す）」して、たった一人を探す時のあの切実な気持ち。")
]

words = []
for item in words_data:
    root1 = item[4].split(" ")[0]
    meaning1 = " ".join(item[4].split(" ")[1:]).strip("()")
    w = {
        "id": f"{item[0]}_vision",
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
        "example": f"Take a close {item[0]} at this photograph.",
        "deep_dive": {
            "roots": [{"term": root1, "meaning": meaning1}],
            "points": ["「見る」という行為のグラデーションこそが、世界の解像度を決定します。"]
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
    print(f"Success: Added {added} words. Theme: Vision (Cycle 19).")
else:
    print("Error parsing data.js")
