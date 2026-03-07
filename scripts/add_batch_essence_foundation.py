import json
import re

word_batch = [
    # Cycle 100: Essence & Foundation
    {
        "id": "quintessence_essence",
        "word": "Quintessence",
        "meaning": "真髄、典型、第五元素",
        "era": "15th Century Latin quinta essentia",
        "etymology": {
            "components": ["quinta (fifth)", "essentia (essence)"],
            "original_statement": "From Old French quintessence, from Medieval Latin quinta essentia (fifth essence), meaning the pure substance from which the heavenly bodies were composed."
        },
        "concept": "The fifth essence (地・水・火・風の四大元素を超えた、天体を構成する「第五の（fifth）」純粋な「本質（essence）」)",
        "thinking": "不純物を極限まで取り除き、そのものの最も純粋で、最も濃密な「核」だけを取り出した状態. 古代の哲学者たちは、目に見える世界を超えた場所にこの第五元素があると考えました。それは、あなたの人生や魂が、余計なものをすべて削ぎ落としたあとに辿り着く、究極の「自分らしさ」の結晶です。",
        "aftertaste": "純粋な核。それは古びることもなく、失われることもない。あなたのなかで、永遠に黄金の光を放ち続ける一滴。",
        "example": "He was the quintessence of a British gentleman, polite and reserved at all times.",
        "deep_dive": { "roots": [{"term": "penkwe-", "meaning": "five"}, {"term": "es-", "meaning": "to be"}], "points": ["essence（本質）は『在ること』そのもの。存在の再奥にある光。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "fundamental_essence",
        "word": "Fundamental",
        "meaning": "根本的な、基本的な、重要な",
        "era": "15th Century Latin fundus",
        "etymology": {
            "components": ["fundus (bottom, foundation)"],
            "original_statement": "From Middle French fondamental, from Late Latin fundamentalis (pertaining to a foundation), from fundamen (foundation), from fundare (to found, establish), from fundus (bottom)."
        },
        "concept": "Pertaining to the bottom (建物や思想の「底（bottom）」の部分、それを支える揺るぎない「土台（foundation）」)",
        "thinking": "派手な装飾や外面の変化に惑わされず、その存在を底辺で支えている最もシンプルで強力な原理. 語源の fundus は「底」。どんなに高い塔を建てても、この土台がしっかりしていなければ、すべては脆（もろ）く崩れ去ります。あなたの「譲れない価値観」や「生きる目的」という名の、沈まぬ大地です。",
        "aftertaste": "揺るぎなき大地。装飾が剥がれ落ちても、この土台さえあれば、あなたは何度でも立ち上がることができる。",
        "example": "Free speech is a fundamental right that must be protected in any democratic society.",
        "deep_dive": { "roots": [{"term": "bhudhn-", "meaning": "bottom"}], "points": ["profound（深い）や foundation（基礎）と同じ、重力そのものを受け止める強さ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "substrate_essence",
        "word": "Substrate",
        "meaning": "基質、基盤、下層",
        "era": "19th Century Latin sub- + sternere",
        "etymology": {
            "components": ["sub- (under)", "sternere (to stretch out, spread)"],
            "original_statement": "From Latin substratum (laid under), past participle of substernere (to spread under), from sub- (under) + sternere (to spread)."
        },
        "concept": "Spread under (目に見える世界の「下（under）」に、「広げ（spread）」られている目に見えない基礎)",
        "thinking": "表面的な現象が起こるための「舞台」となる、より深い層. 語源の sternere は、布を広げることを意味します。それは母なる大地のように、あらゆる命の営みを支え、養分を与えている広大な基盤です。あなたの意識の下にある、言葉にならない、しかし確かな存在の広がり。",
        "aftertaste": "見えざる舞台. 表舞台がどんなに華やかでも、それを支えるこの静かなる広がりを、あなたは忘れない。",
        "example": "Ancient traditions still form the cultural substrate of modern society in many countries.",
        "deep_dive": { "roots": [{"term": "ster-", "meaning": "to spread"}], "points": ["stratosphere（成層圏）や street（通り：敷かれたもの）と同じ、空間のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "entity_essence",
        "word": "Entity",
        "meaning": "実体、存在物、独立した個体",
        "era": "16th Century Latin ens",
        "etymology": {
            "components": ["ens (thing that is), from esse (to be)"],
            "original_statement": "From Late Latin entitatem (being, existence), from ens (a being), from esse (to be)."
        },
        "concept": "The thing that is (他の何物でもない、ただそこに「在る（to be）」ということの不思議と重み)",
        "thinking": "関係性や属性（名前、職業、地位）をすべて剥ぎ取ったあとに残る、剥き出しの「存在」そのもの. 語源の esse は、呼吸するようにそこに在ること。あなたは「何者か」である前に、まず一つの「実体（Entity）」としてここに在ります。その絶対的な存在の肯定。",
        "aftertaste": "ただ、在ること。それだけであなたは、宇宙という巨大なジグソーパズルの、欠かせない一欠片なのだ。",
        "example": "The two small businesses merged to form a single, more powerful corporate entity.",
        "deep_dive": { "roots": [{"term": "es-", "meaning": "to be"}], "points": ["essence（本質）や absent（不在：離れて在ること）と同じ、存在の原子。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "principle_essence",
        "word": "Principle",
        "meaning": "原則、原理、信念、源泉",
        "era": "14th Century Latin primus + capere",
        "etymology": {
            "components": ["primus (first)", "capere (to take)"],
            "original_statement": "From Old French principe, from Latin principium (a beginning, foundation, origin), from princeps (first), from primus (first) + capere (to take)."
        },
        "concept": "Taken first (すべての思考や行動の「最初（first）」に「置かれる（take）」、揺るぎない出発点)",
        "thinking": "他人に流されるのではなく、自分が自分であるために最初に握りしめた（Capere）最初の（Primus）ルール. それは迷ったときのコンパスであり、嵐の夜の灯台です。原理とは、あなたが世界に対して、どのように関わり、どのように美しく在るかという約束の言葉です。",
        "aftertaste": "最初の誓い。世界がどれほど複雑に絡み合っても、あなたの心はこの最初の一点へと、いつでも戻ることができる。",
        "example": "I refuse to compromise on my principles, even if it makes my life more difficult.",
        "deep_dive": { "roots": [{"term": "per-", "meaning": "forward, first"}, {"term": "kap-", "meaning": "to grasp"}], "points": ["prince（王子：第一の位）や capture（捕らえる）と同じ、主導権のルーツ。"] },
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
        print(f"Success: Added {added} words in Cycle 100.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
