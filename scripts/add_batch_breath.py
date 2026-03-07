import json
import re

word_batch = [
    # Cycle 109: Essence & Breath
    {
        "id": "spirit_essence",
        "word": "Spirit",
        "meaning": "精神、魂、気質、生気",
        "era": "13th Century Latin spiritus",
        "etymology": {
            "components": ["spirare (to breathe)"],
            "original_statement": "From Old French espirit, from Latin spiritus (a breathing, breath, spirit), from spirare (to breathe)."
        },
        "concept": "Breath of life (「呼吸（breath）」すること、肉体に命を吹き込む不可視の「生気」)",
        "thinking": "形を持たないけれど、私たちが生き、感じ、考えるための最も根源的な原動力. 語源は「呼吸」。息を吸い、吐き出すという最もシンプルな行為の中に、宇宙の一部である私たちが命を繋ぎ止めている神秘が宿っています。それは、肉体が滅んでも消えることのない、あなたの内なる純粋な風です。",
        "aftertaste": "永遠の呼吸. あなたが今、この世界で吸い込んでいる空気は、あなたの魂という器の中で、唯一無二の光に変わる。",
        "example": "The team showed great spirit despite their defeat in the final match.",
        "deep_dive": { "roots": [{"term": "speis-", "meaning": "to blow"}], "points": ["inspire（霊感を与える：息を吹き込む）や expire（息を引き取る）と同じ、命のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "anima_essence",
        "word": "Anima",
        "meaning": "魂、生命、アニマ(男性の深層心理にある女性的側面)",
        "era": "Latin anima",
        "etymology": {
            "components": ["anima (air, breath, life, soul)"],
            "original_statement": "From Latin anima (air, breath, life, soul), from PIE root ane- (to breathe)."
        },
        "concept": "Animating breath (物体に「動き」と「命」を与える、根源的な「魂（soul）」)",
        "thinking": "単なる静止した物体に、喜びや悲しみという「色彩」を与え、世界と対話させる力. 語源は「風」や「息」。アニメーション（Animation）が静止画に命を与えるように、アニマはあなたの肉体を、物語を紡ぐ「生きた存在」へと変容させます。それは、内なる生命の核です。",
        "aftertaste": "躍動する命. あなたはただ細胞の集合体なのではない。宇宙の風が、あなたという楽器を通って美しい音楽を奏でているのだ。",
        "example": "In Jungian psychology, the anima represents the inner feminine part of a man.",
        "deep_dive": { "roots": [{"term": "ane-", "meaning": "to breathe"}], "points": ["animal（動物：息をするもの）や animate（活気づける）と同じ、躍動のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "pneuma_essence",
        "word": "Pneuma",
        "meaning": "霊、気、プネウマ、精（せい）",
        "era": "Greek pneuma",
        "etymology": {
            "components": ["pneuma (wind, breath, spirit)"],
            "original_statement": "From Greek pneuma (wind, air; spirit), from pnein (to blow, breathe)."
        },
        "concept": "Cosmic breath (宇宙全体を満たし、万物を繋ぎ合わせている「聖なる気（spirit）」)",
        "thinking": "個人の魂を超えて、森羅万象（しんらばんしょう）を貫く知的なエネルギーの流れ. 古代ギリシャの哲学者たちは、これが世界を構成する最も重要な要素だと考えました。それは、あなたの肺を満たす空気であり、木々を揺らす風であり、思想を運ぶ見えない波でもあります。分離のない、宇宙の呼吸。 ",
        "aftertaste": "繋がる全一. あなたが吐いた息は、いつか風となり、星となり、誰かの魂の一部として再び生まれ変わる。",
        "example": "In ancient Greek philosophy, pneuma was the vital breath that animated the universe.",
        "deep_dive": { "roots": [{"term": "pneu-", "meaning": "to breathe"}], "points": ["pneumonia（肺炎）や pneumatic（空気圧の）と同じ。実体なき力のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "inspiration_essence",
        "word": "Inspiration",
        "meaning": "インスピレーション、霊感、鼓舞するもの、吸気",
        "era": "14th Century Latin in- + spirare",
        "etymology": {
            "components": ["in- (into)", "spirare (to breathe)"],
            "original_statement": "From Old French inspiracion, from Late Latin inspirationem (a breathing into, inspiration), from inspirare (to inspire, inflame, blow into)."
        },
        "concept": "Breathed into (神聖な風が、あなたの心の「中へ（into）」「吹き込まれる（breathe）」こと)",
        "thinking": "努力して掴み取るものではなく、ある瞬間に「訪れる」もの. それは、あなたが心という窓を大きく開いたとき、外の世界の豊かさが呼吸（spirare）のように流れ込んでくる現象です。アイデアが閃くとき、あなたは自分以上の力と繋がっています。それは、宇宙からの贈り物です。",
        "aftertaste": "訪れる光. あなたもう、一人で頑張らなくていい。ただ深く息を吸い込み、世界があなたを愛するままに任せてごらん。",
        "example": "Nature has always been a primary source of inspiration for her poetry.",
        "deep_dive": { "roots": [{"term": "speis-", "meaning": "to blow"}], "points": ["conspire（共謀する：共に息をする）と同じ、交流のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "aspire_essence",
        "word": "Aspire",
        "meaning": "熱望する、切望する、向上心を持つ",
        "era": "15th Century Latin ad- + spirare",
        "etymology": {
            "components": ["ad- (to, towards)", "spirare (to breathe)"],
            "original_statement": "From Middle French aspirer, from Latin aspirare (to breathe upon, pant after, favor), from ad- (to) + spirare (to breathe)."
        },
        "concept": "Breathe towards (高みにある理想に「向かって（towards）」、切実な「息を吐く（breathe）」こと)",
        "thinking": "現状に甘んじることなく、まだ見ぬ自分や理想の場所に向かって、憧れの吐息を漏らすこと. 語源の ad- は方向、spirare は呼吸。それはまるで、遥か遠くの星に向かって自分の命の風を送り出すような、純粋で、少し苦しいほどの情熱です。あなたの願いは、あなたの魂が向かいたい方角を指し示しています。",
        "aftertaste": "憧れの旋律. その熱望の苦しさは、あなたが今、自分の可能性という山を力強く登っているという確かな証明だ。",
        "example": "Many young artists aspire to exhibit their work in a major museum one day.",
        "deep_dive": { "roots": [{"term": "speis-", "meaning": "to blow"}], "points": ["aspirin（アスピリン）とは無関係（歴史的偶然）。呼吸は情熱の源。"] },
        "part_of_speech": "verb"
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
        print(f"Success: Added {added} words in Cycle 109.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
