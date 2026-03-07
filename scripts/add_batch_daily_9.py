import json
import re

word_batch = [
    {
        "id": "crystal",
        "word": "Crystal",
        "meaning": "水晶、結晶、透明な",
        "era": "Old English/Greek krrystallos",
        "etymology": {
            "components": ["kryos (frost, ice)"],
            "original_statement": "From Old English cristalla, from Latin crystallus, from Greek krrystallos (ice, rock crystal), from kryos (icy cold, frost)."
        },
        "concept": "Ice-like transparency (氷のような透明感、秩序ある固形)",
        "thinking": "古代ギリシャ人は、水晶のことを「極限まで冷やされて、二度と溶けることがなくなった氷」だと信じていました。それは光を透過し、自分自身の内面を曇りなく保つ、透明な誠実さの象徴。極めて高く秩序立った、静かなる力の結晶体です。",
        "aftertaste": "光を溜め込み、永遠に溶けない凍てついた美学。",
        "example": "His memories of that day were crystal clear.",
        "deep_dive": {
            "roots": [{"term": "krū-", "meaning": "hard, cold, frost"}],
            "points": ["crust（パンの耳/外殻）と同じルーツ。表面が冷えて『固まった』ことを意味します。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "ripple",
        "word": "Ripple",
        "meaning": "さざ波、波及効果",
        "era": "17th Century Onomatopoeic",
        "etymology": {
            "components": ["rip- (mimetic sound of water)"],
            "original_statement": "Probably of imitative origin, mimicking the vibration or motion of small waves on the surface of water."
        },
        "concept": "A gentle vibration of surface (水面の柔らかな振動)",
        "thinking": "湖に小石を投げ入れたときに生まれる、同心円状の小さな波。それは、たった一人の小さな行動や言葉が、誰にも気づかれないほど微かに、しかし確実に世界全体を揺らし、どこまでも広がっていく「目に見える影響力」の物語そのものです。",
        "aftertaste": "誰も見ていなくても、あなたの放った振動は岸辺に届く。",
        "example": "A smile creates ripples of kindness that touch everyone around.",
        "deep_dive": {
            "roots": [{"term": "reip-", "meaning": "to scratch, pull, tear (possible)"}],
            "points": ["rim（縁）や reeve（通す）など、境界線を揺らすことに関係するとされる説もあります。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "thirst",
        "word": "Thirst",
        "meaning": "喉の渇き、渇望",
        "era": "Old English þurst",
        "etymology": {
            "components": ["ters- (to dry)"],
            "original_statement": "From Old English þurst, from Proto-Germanic *thurstuz, from PIE root *ters- (to dry)."
        },
        "concept": "A dry state of being (不毛な乾燥、激しい欲求)",
        "thinking": "水が失われ、喉がカラカラに乾いて痛む「不毛な乾燥（ters-）」。それは肉体的な欲求であると同時に、知識、愛、あるいは成功を狂おしいほどに求める「心の空腹感」でもあります。満たされないことが、人を前へと進ませる、乾いた力。",
        "aftertaste": "足りないこと。それが、真の潤いを探すための唯一の羅針盤。",
        "example": "Her thirst for knowledge was unquenchable.",
        "deep_dive": {
            "roots": [{"term": "ters-", "meaning": "to dry"}],
            "points": ["terrace（テラス：盛土をした乾燥した場所）や torrent（急流：もとは激しい乾燥を伴う炎の奔流）の親戚。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "storm",
        "word": "Storm",
        "meaning": "嵐、荒天、大騒ぎ、奇襲する",
        "era": "Old English storm",
        "etymology": {
            "components": ["ster- (to stiffen, scatter, stir up)"],
            "original_statement": "From Old English storm, from Proto-Germanic *sturmaz (storm), related to *stur- (to stir, move)."
        },
        "concept": "A stirring of the air (大気の狂おしい攪拌)",
        "thinking": "空気が「かき回され（stir）」、平穏が失われた状態。それは自然界の激しい放電や暴風雨を意味すると同時に、隠されていた感情が爆発する「心の嵐」も指します。すべてを破壊する力強さと、その後に訪れる清浄な空気の二面性を持っています。",
        "aftertaste": "吹き荒れる風。破壊することでしか、新しい静寂は生まれない。",
        "example": "He faced the storm of criticism with calm dignity.",
        "deep_dive": {
            "roots": [{"term": "stwer-", "meaning": "to stir, move, make solid (possible)"}],
            "points": ["stir（かき混ぜる）や disturb（邪魔する：共に揺さぶる）と同類の熱き攪拌の語源。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "glance",
        "word": "Glance",
        "meaning": "一目見ること、ちらりと見る、光る",
        "era": "15th Century Old French glacer",
        "etymology": {
            "components": ["glacer (to slip, slide)"],
            "original_statement": "Probably from Old French glacer (to slip, slide), related to glace (ice), originally meaning to 'slip off' or 'glance off' a surface."
        },
        "concept": "A sliding look (表面を滑るような視線、きらりと光る反射)",
        "thinking": "「氷（ice/glace）」の上をツルリと滑り落ちる（sliding）感覚。じっと凝視する（stare/gaze）のではなく、視線が対象の表面を滑り、瞬時に通り抜けていく一瞬の接触。あるいは、何かに当たって「キラリと反射した」一瞬の輝きを意味します。",
        "aftertaste": "深入りはしない。ただ一瞬、その煌めきに触れて通り過ぎるだけ。",
        "example": "I took a quick glance at my watch and realized I was late.",
        "deep_dive": {
            "roots": [{"term": "ghel-", "meaning": "to shine, yellow, gold"}],
            "points": ["glare（ギラギラ光る）や glass（ガラス）と同じく、かつては『光る』ことがルーツでした。"]
        },
        "part_of_speech": "noun"
    }
]

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
    if match:
        prefix = match.group(1)
        json_array_str = match.group(2)
        suffix = match.group(3)
        
        words = json.loads(json_array_str)
        existing_ids = {w.get("id") for w in words}
        
        added_count = 0
        for item in word_batch:
            if item["id"] not in existing_ids:
                words.append(item)
                added_count += 1
                
        new_json_str = json.dumps(words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Success: Added {added_count} words.")
    else:
        print("Error: Could not find WORDS array in data.js.")
except Exception as e:
    print(f"Error: {e}")
