import json
import re

words_data = [
    ("moment", "Moment", "瞬間、少しの間", "14th Century", "momentum (movement, brief time)", "A very brief period of time", "永遠という無限の川の流れから、神がまばたきするほどのわずかな長さだけ切り取られた奇跡の欠片。", "幸せな「モーメント（瞬間）」は、砂時計からこぼれ落ちる前に深く深呼吸して味わうものです。"),
    ("interval", "Interval", "間隔、合間", "15th Century", "intervallum (space between palisades)", "An intervening time or space", "二つの出来事や壁の間に横たわり、次の展開のために沈黙が主役となる計算された休止符。", "激しい雨と雨の「インターバル（隙間）」にこそ、一番力強い太陽の光が差し込みます。"),
    ("duration", "Duration", "持続期間", "14th Century", "durare (to last)", "The time during which something continues", "ある存在や状態が、時間の浸食に耐えてその形と意味を保ち続けるための、目に見えない忍耐の長さ。", "辛い時期の「デュレーション（持続）」は長く感じますが、それはあなたの魂を強固に鍛えている証です。"),
    ("epoch", "Epoch", "新時代、画期的な出来事", "17th Century", "epokhe (stoppage, fixed point of time)", "A period of time in history or a person's life", "古い歴史が一旦立ち止まり、そこから全く新しい価値観による世界が始まること高らかに宣言する天の刻印。", "スマートフォンの発明は、間違いなく人類のコミュニケーションにおける「エポック（新時代）」をもたらしました。"),
    ("era", "Era", "時代、年代", "17th Century", "aera (counters, an item of account)", "A long and distinct period of history", "単なる時間の連続ではなく、特定の支配者や出来事によって明確な色付けがされた、歴史の大きなページ。", "新しい「エラ（時代）」の幕開けには、いつも古い価値観の崩壊という痛みが伴います。"),
    ("aeon", "Aeon", "永劫、無限の長い期間", "17th Century", "aion (age, eternity)", "An indefinite and very long period of time", "人間の理解という小さな器では到底測り知ることのできない、星々が生まれそして死んでいくほどの茫漠（ぼうばく）たる時の流れ。", "私があなたを再び見つけるのに、たとえ「イーオン（何億年）」かかろうとも必ず探し出します。"),
    ("chronicle", "Chronicle", "年代記、記録", "14th Century", "chronika (annals)", "A factual written account of important or historical events", "バラバラに散らばった無数の歴史の破片を、時間という絶対的な糸で紡ぎ合わせ、後世に正しく引き継ぐための聖なる織物。", "どんな偉大な王の「クロニクル（年代記）」も、最初は名もない農民の小さな一歩から始まっています。"),
    ("anachronism", "Anachronism", "時代錯誤", "17th Century", "ana- (against) + khronos (time)", "A thing belonging to a period other than that in which it exists", "時間という厳格なパズルのピースが間違った場所にはめ込まれ、周囲の時代から完全に孤立してしまった愛おしくも滑稽な迷子。", "現代社会で騎士道を重んじる彼は、まさに「アナクロニズム（時代錯誤）」ですが、誰よりも紳士です。"),
    ("synchronize", "Synchronize", "同期する、時間を合わせる", "17th Century", "syn- (together) + khronos (time)", "Cause to occur or operate at the same time or rate", "二つの異なる歯車が互いの魂の歩幅を完璧に理解し合い、運命のように寸分違わず共に時を刻み始める奇跡。", "二人の呼吸が「シンクロナイズ（同調）」した時、どんな言葉よりも深くお互いを理解できました。"),
    ("temporary", "Temporary", "一時的な、仮の", "16th Century", "tempus (time)", "Lasting for only a limited period of time; not permanent", "永遠ではないという冷酷な条件付きだからこそ、その短い瞬間に全ての輝きと価値を凝縮させる究極の美しさ。", "この苦しみは「テンポラリー（一時的）」なものだと信じて、嵐が過ぎ去るのを心静かに待ちましょう。")
]

words = []
for item in words_data:
    root1 = item[4].split(" ")[0]
    meaning1 = " ".join(item[4].split(" ")[1:]).strip("()")
    w = {
        "id": f"{item[0]}_time",
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
        "example": f"This marking clearly denotes a specific {item[0]}.",
        "deep_dive": {
            "roots": [{"term": root1, "meaning": meaning1}],
            "points": ["時（時空）をどう捉えるかは、人生への向き合い方を規定します。"]
        },
        "part_of_speech": "noun" if item[0] not in ["synchronize", "temporary"] else "verb" if item[0] == "synchronize" else "adjective"
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
    print(f"Success: Added {added} words. Theme: Time (Cycle 11).")
else:
    print("Error parsing data.js")
