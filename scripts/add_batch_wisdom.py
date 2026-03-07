import json
import re

word_batch = [
    # Cycle 87: Wisdom & Enlightenment
    {
        "id": "sagacity_wisdom",
        "word": "Sagacity",
        "meaning": "明敏、賢明、鋭い判断力",
        "era": "16th Century Latin sagax",
        "etymology": {
            "components": ["sagax (quick-scented, acute, sagacious)"],
            "original_statement": "From Latin sagacitatem (closeness of scent, acuteness of senses), from sagax (quick-scented, keen-scented), related to sagire (to perceive quickly or keenly)."
        },
        "concept": "Quick-scented (獲物の「匂（scent）」をいち早く嗅ぎ分ける猟犬のように、本質を察知すること)",
        "thinking": "単なる知識量（Knowledge）ではなく、経験に基づいた直感的な「鼻の良さ」。語源の sagax は、見えない獲物の匂いを追う猟犬の鋭敏さを指します。誰もが混乱する状況の中で、目に見えない「真実の香り」を嗅ぎ取り、正しい方向を指し示す。それは生き抜くための、野性的で気高い知性です。",
        "aftertaste": "嗅ぎ分ける。理屈の後ろに隠された、剥き出しの真実が放つかすかな匂いを、あなたの魂はすでに捉えている。",
        "example": "The diplomat's sagacity was instrumental in preventing a major international conflict.",
        "deep_dive": { "roots": [{"term": "sag-", "meaning": "to seek out, track"}], "points": ["sage（賢者）や seek（探す）と同じ、真理を『追跡する』ルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "prudence_wisdom",
        "word": "Prudence",
        "meaning": "慎重、思慮分別、倹約",
        "era": "14th Century Latin providentia",
        "etymology": {
            "components": ["pro- (forward)", "videre (to see)"],
            "original_statement": "From Old French prudence, from Latin prudence (a foreseeing, foresight, practical wisdom), a contraction of providentia (foresight), from pro- (forward) + videre (to see)."
        },
        "concept": "Seeing forward (未来を「予見（foresee）」し、今なすべき最善を判断すること)",
        "thinking": "ただ臆病であることではなく、未来に起こりうる変化をあらかじめ見通し（Providentia）、そこから逆算して「今、この瞬間の行動」を律すること。それは時間という荒波を乗り越えるための、優れた精神の舵取り。賢明さとは、常に未来の自分に対する「責任」を負うことでもあります。",
        "aftertaste": "先見の明. あなたの今日の一歩は、まだ見ぬ明日のあなたを守るための、静かなる誓い。",
        "example": "In times of economic uncertainty, financial prudence becomes more important than ever.",
        "deep_dive": { "roots": [{"term": "pro-", "meaning": "before"}, {"term": "weid-", "meaning": "to see"}], "points": ["provide（提供する：前もって見る）や vision（視覚）と同じ、支配的な視線のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "erudition_wisdom",
        "word": "Erudition",
        "meaning": "博学、該博、学問的知識",
        "era": "15th Century Latin ex- + rudis",
        "etymology": {
            "components": ["ex- (out of, away from)", "rudis (rough, raw, unskilled)"],
            "original_statement": "From Latin eruditionem (an instructing, knowledge), from eruditus, past participle of erudire (to polish, instruct, teach), literally 'to bring out of the rough,' from ex- (out) + rudis (rough, unskilled)."
        },
        "concept": "Polishing out of the rough (「粗野（rough）」な状態から抜け出し、磨き上げられること)",
        "thinking": "単に本をたくさん読むことではなく、磨かれていない原石（rudis）のような自分を、知性によって丁寧に磨き上げ（polish）、洗練させていくプロセス. 教養とは、自分の内側にある野蛮さを、他者への深い理解と慈しみに変えるための、終わりのない彫刻のような行為です。",
        "aftertaste": "磨き上げる。言葉を知るたびに、あなたは自分という原石を削り、世界の光をより純粋に反射する鏡へと変わってゆく。",
        "example": "The scholar's deep erudition won him great respect throughout the academic community.",
        "deep_dive": { "roots": [{"term": "reud-", "meaning": "to clear land (possible)"}], "points": ["rudiment（基本）や rude（失礼な：粗野な）の反対側。知性による文明化。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "enlightenment_wisdom",
        "word": "Enlightenment",
        "meaning": "啓蒙、悟り、解脱",
        "era": "17th Century English en- + light",
        "etymology": {
            "components": ["en- (cause to be)", "light (brightness)"],
            "original_statement": "From enlighten (verb), from Old English in+ lihtan (to light up)."
        },
        "concept": "Bringing light into (暗闇の中に「光（light）」を注ぎ込み、すべてを明らかにすること)",
        "thinking": "偏見、無知、迷い. それらが作り出す暗い霧の中に、理知や悟りの光を差し込ませること。光が届いた瞬間、幽霊に見えていた影はただの古着であり、壁に見えていたものはただの扉であったことに気づきます。世界が変わるのではなく、あなたの「光の総量」が世界を新しく定義するのです。",
        "aftertaste": "夜明け. 知ることは、目を開けること。その眩（まぶ）しさのなかで、恐怖は静かに溶けて消える。",
        "example": "The 18th century is often referred to as the Age of Enlightenment in European history.",
        "deep_dive": { "roots": [{"term": "leuk-", "meaning": "light, brightness"}], "points": ["luxury（贅沢：光り輝くもの）や lucid（明快な）と同じ、闇を払う意志の勝利。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "sophistication_wisdom",
        "word": "Sophistication",
        "meaning": "洗練、世慣れていること、複雑化",
        "era": "14th Century Greek sophos",
        "etymology": {
            "components": ["sophos (wise, clever)"],
            "original_statement": "From Medieval Latin sophisticationem, from sophisticare (to adulterate), from Latin sophisticus (sophistic), from Greek sophistikos, from sophistēs (a master of one's craft, a wise man)."
        },
        "concept": "Mastery and complexity (職人の「智慧（wisdom）」が重なり、より「複雑」で高度なものになること)",
        "thinking": "かつては「混ぜ物をして本質を歪める」という否定的な意味もありましたが、現代では、経験を経て磨かれ、単純な白黒では語れない「奥行き」と「複雑さ」を身につけた美しさを指します. 世の酸いも甘いも噛み分けた、静まり返った大人の知性。それは、純粋さを捨てたのではなく、より深い次元で純粋さを再定義した状態です。",
        "aftertaste": "奥行きのある影. 単純なことなど何もない。震えるような複雑さのなかにこそ、真理は隠れている。",
        "example": "The new operating system offers a level of sophistication previously unknown to home users.",
        "deep_dive": { "roots": [{"term": "Unknown source"}], "points": ["philosophy（哲学：知を愛すること）と同じ『sophos』の根。知恵は時に人を迷わせ、導く。"] },
        "part_of_speech": "noun"
    }
]

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
    if match:
        prefix, json_array_str, suffix = match.groups()
        words = json.loads(json_array_str)
        existing_ids = {w.get("id") for w in words}
        
        added = 0
        for item in word_batch:
            if item["id"] not in existing_ids:
                words.append(item)
                added += 1
        
        new_content = content[:match.start()] + prefix + json.dumps(words, ensure_ascii=False, indent='\t') + suffix + content[match.end():]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Success: Added {added} words in Cycle 87.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
