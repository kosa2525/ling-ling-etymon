import json
import re

word_batch = [
    # Cycle 119: Shadow & Depth
    {
        "id": "penumbra_shadow",
        "word": "Penumbra",
        "meaning": "半影、薄暗い部分、境界領域",
        "era": "17th Century Latin paene + umbra",
        "etymology": {
            "components": ["paene (almost)", "umbra (shadow)"],
            "original_statement": "Coined by astronomer Johannes Kepler, from Latin paene (almost) + umbra (shadow)."
        },
        "concept": "Almost shadow (「影（shadow）」に 「なりかけている（almost）」 光と闇が 溶け合う 「中間の場所」)",
        "thinking": "光と闇が明確に分かれるのではなく 曖昧に混ざり合い 表情を変えていく 幻想的な境界領域. 語源は「ほとんど影」. それは 直視できないほど眩しい真実と 全てを隠す闇の間に横たわる 唯一私たちが「安らげる」場所です. 曖昧さの中にこそ 真実の情緒が宿っています.",
        "aftertaste": "重なる淡い闇. 白黒つけられない現実に 疲れてしまったなら. この穏やかな「半影（ペナンブラ）」に身を委ね 輪郭の溶けた静寂を 慈しんでみよう.",
        "example": "We sat in the cool penumbra of the large oak tree, hidden from the harsh midday sun.",
        "deep_dive": { "roots": [{"term": "paene-", "meaning": "almost"}, {"term": "andho-", "meaning": "dark (possible for umbra)"}], "points": ["umbrella（傘：小さな影）と同じ。闇は、守りの象徴でもある。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "umbrage_shadow",
        "word": "Umbrage",
        "meaning": "気分を害すること、憤慨、日陰、木陰",
        "era": "15th Century Latin umbra",
        "etymology": {
            "components": ["umbra (shadow, shade)"],
            "original_statement": "From Old French ombrage (shade, shadow), from Latin umbraticum (of or in the shade), from umbra (shade, shadow)."
        },
        "concept": "The cast shadow (「日陰（shade）」が 「投げかけられた（cast）」かのような 心の「曇り（offense）」)",
        "thinking": "誰かの不用意な一言や態度によって 心にふっと「陰り（影）」が差してしまう その繊細なプライドの反応. 語源は「木陰」。冷涼な場所を意味していましたが のちに「不信」や「憤慨」といった心の不透明さを指すようになりました. あなたの心が陰ったとき それはあなたが何かを 大切にしているという証です.",
        "aftertaste": "心の陰り. 憤慨することは 悪いことではない. それはあなたの誇りという光が 外からの風によって 揺らめいた瞬間の影に過ぎないのだから.",
        "example": "He took umbrage at the suggestion that his work was anything less than perfect.",
        "deep_dive": { "roots": [{"term": "andho-", "meaning": "dark"}], "points": ["somber（薄暗い：影の下の）と同じ。光の不在が感情を形作る。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "obscurity_shadow",
        "word": "Obscurity",
        "meaning": "無名、不明瞭、暗がり、世に知られないこと",
        "era": "15th Century Latin ob- + scurus",
        "etymology": {
            "components": ["ob- (over)", "scurus (covered, dark)"],
            "original_statement": "From Old French obscurite, from Latin obscuritatem (darkness, obscurity), from obscurus (dark, dusky, shady), from ob- (over) + -scurus (covered)."
        },
        "concept": "Covered over (厚い「幕（cover）」で 「覆い隠され（over）」 人々の目から 「見えなくなっている（dark）」こと)",
        "thinking": "世間の喧騒から 遠く離れた場所で 誰にも知られずに 自分の本質を磨き上げることのできる 贅沢な隠れ家. 語源は「覆われた」. それは 孤独であると同時に 最大の自由でもあります. 知られないことの静けさの中でこそ 魂は真実の声を 取り戻すことができます.",
        "aftertaste": "静かなる隠遁. 有名であることよりも 誰にも邪魔されぬ「無名（オブスキュリティ）」であることを 誇りに思おう. そこにこそ あなただけの 聖なる宇宙が広がっているのだから.",
        "example": "The poet lived in total obscurity for decades, only to be discovered after his death.",
        "deep_dive": { "roots": [{"term": "epi-", "meaning": "over (possible for ob-)"}, {"term": "skeu-", "meaning": "to cover"}], "points": ["sky（空：覆うもの）や shoe（靴：足を覆うもの）と同じ、守護のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "adumbrate_shadow",
        "word": "Adumbrate",
        "meaning": "概説する、予兆を示す、(輪郭を)描く、影を落とす",
        "era": "16th Century Latin ad- + umbra",
        "etymology": {
            "components": ["ad- (to, towards)", "umbra (shadow)"],
            "original_statement": "From Latin adumbratus, past participle of adumbrare (to cast a shadow, outline, overshadow, represent in outline), from ad- (to) + umbra (shadow)."
        },
        "concept": "Represent by shadow (「影（shadow）」を 「投げかける（to）」ことで 実体の「予兆（outline）」を 示すこと)",
        "thinking": "すべてを明快に語るのではなく その輪郭や影を そっと示すことで 相手の想像力を 遥か高みへと誘（いざな）うこと. 語源は「影を落とすこと」. それは 控えめでありながら 核心を突く表現です. 予感の中にこそ 最も豊かな物語が 眠っています.",
        "aftertaste": "予感のデッサン. 全てを説明し尽くす必要はない. あなたが落とした そのわずかな「影（アダンブレート）」が 誰かの心の中で 巨大な希望へと 育っていくのだから.",
        "example": "The initial sketches only briefly adumbrate the complex architectural masterpiece that was to come.",
        "deep_dive": { "roots": [{"term": "andho-", "meaning": "dark"}], "points": ["outline（輪郭）の詩的な表現。存在しないものを、影で証明する。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "tenebrous_shadow",
        "word": "Tenebrous",
        "meaning": "暗い、薄暗い、陰鬱な、不可解な",
        "era": "15th Century Latin tenebrae",
        "etymology": {
            "components": ["tenebrae (darkness)"],
            "original_statement": "From Old French tenebreus, from Latin tenebrosus (full of darkness), from tenebrae (darkness, gloom, place of shadows)."
        },
        "concept": "Full of darkness (重苦しい「闇（darkness）」に 「満ちている（full）」 秘密めいた 深い影)",
        "thinking": "陽光を頑なに拒み 独自の沈黙と秘密を 守り続けているような 濃密で神秘的な暗がり. 語源は「闇そのもの」. それは 時に不安を誘いますが 同時に あなたの最も深い知性と 原始的な本能を 揺さぶり呼び覚ます 聖域でもあります. 闇を愛する勇気が 闇を超えた光を生みます.",
        "aftertaste": "闇の聖域. 明るい場所だけが 世界ではない. この「薄暗さ（テネブラス）」の中にこそ あなたという物語の 最も重要な 秘密の鍵が隠されているのだ.",
        "example": "The ancient cave system was filled with tenebrous passages that had never been mapped.",
        "deep_dive": { "roots": [{"term": "teme-", "meaning": "dark"}], "points": ["temerity（向こう見ず：闇に飛び込むこと）と同じ。闇への挑戦。"] },
        "part_of_speech": "adjective"
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
        print(f"Success: Added {added} words in Cycle 119.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
