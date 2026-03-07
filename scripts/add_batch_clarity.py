import json
import re

word_batch = [
    # Cycle 99: Clarity & Light
    {
        "id": "lucidity_light",
        "word": "Lucidity",
        "meaning": "明晰、透明、正気",
        "era": "16th Century Latin lux",
        "etymology": {
            "components": ["lux (light)"],
            "original_statement": "From Latin luciditatem, from lucidus (light, bright, clear), from lucere (to shine), from lux (light)."
        },
        "concept": "Full of light (「光（light）」に満ち溢れ、何もかもが「はっきり（clear）」見えること)",
        "thinking": "霧が晴れ、複雑に絡み合っていた思考が一本の絹糸のように整い、真実が純粋な姿で立ち現れる状態. 語源の lux は、すべての根源的な光です。説明が不要なほどの圧倒的な「わかりやすさ」と、物事の本質を貫く鋭い透明感。それは、暗闇を照らす知性の勝利です。",
        "aftertaste": "透き通る思考。迷いは光の中に溶け、あなたは今、進むべき道を誰よりもはっきりと見ている。",
        "example": "He write with such lucidity that even complex scientific theories become easy to understand.",
        "deep_dive": { "roots": [{"term": "leuk-", "meaning": "light, brightness"}], "points": ["lucid（明快な）や translucent（半透明の）と同じ、純粋な視界のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "luminescence_light",
        "word": "Luminescence",
        "meaning": "冷光、発光、(熱を伴わない)光",
        "era": "19th Century Latin lumen",
        "etymology": {
            "components": ["lumen (light)"],
            "original_statement": "From Latin lumen (light) + -escence (beginning to be, becoming), from lux (light)."
        },
        "concept": "Becoming light (熱さを持たず、静かに「光（light）」そのものに「成っていく（become）」こと)",
        "thinking": "燃える火のような激しい熱を伴わず、深海の生物や月の光のように、静寂の中で自ら淡い光を放つこと. 語源の lumen は、光の源。それは外からの刺激に反応するのではなく、内側に蓄えられたエネルギーが、静かに溢れ出した、神秘的で慈愛に満ちた輝きです。",
        "aftertaste": "静かなる微光。あなたの内側にあるその優しさは、暗闇の中で誰かの足元を、密やかに照らしている。",
        "example": "The ocean was filled with the blue luminescence of microscopic organisms.",
        "deep_dive": { "roots": [{"term": "leuk-", "meaning": "light, brightness"}], "points": ["illuminate（照らす）や luminous（光り輝く）同じ。静かな生命の証明。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "transparency_light",
        "word": "Transparency",
        "meaning": "透明、明白、透過性",
        "era": "16th Century Latin trans- + parere",
        "etymology": {
            "components": ["trans- (through)", "parere (to appear, show oneself)"],
            "original_statement": "From Medieval Latin transparentia, from Latin transparentem, from trans- (through) + parere (to appear, come in sight)."
        },
        "concept": "Appearing through (光が「突き抜け（through）」、向こう側の真実が「見える（appear）」こと)",
        "thinking": "自分という存在を消し去り、背後にある真実や光をそのまま通過させる誠実さ. 語源の parere は、姿を現すこと。隠そうとする意志がゼロになったとき、存在は透明になり、最も美しい光を伝播させることができます。それは、嘘や秘密という「不純物」を排除した、究極の信頼の形です。",
        "aftertaste": "純粋な透過。あなたはもう、自分を飾る必要はない。あなたの透明さが、世界の美しさをそのまま映し出している。",
        "example": "The government promised full transparency in their handling of the financial crisis.",
        "deep_dive": { "roots": [{"term": "per-", "meaning": "to produce, bring forth (possible for parere)"}], "points": ["appear（現れる）や parent（親：生むもの）同じ、顕現のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "radiance_light",
        "word": "Radiance",
        "meaning": "輝き、光輝、(幸福などが)溢れ出ていること",
        "era": "17th Century Latin radius",
        "etymology": {
            "components": ["radius (staff, spoke of a wheel, beam of light)"],
            "original_statement": "From radiant (adjective), from Latin radiantem, from radiare (to beam, shine), from radius (staff, spoke of a wheel, beam of light)."
        },
        "concept": "Beaming rays (車輪の「スポーク（spoke）」のように、中心から四方八方へ「光（ray）」を放つこと)",
        "thinking": "一点に留まるのではなく、爆発的な喜びや生命力が、中心から周囲へと勢いよく放射されている状態. 語源の radius は、中心から伸びる一本の線を指します。それは、あなたが幸福の源泉となり、触れるものすべてを黄金色に染め上げていく、圧倒的なエネルギーの伝播です。",
        "aftertaste": "放射される喜び。あなたの微笑みは、中心から放たれる光の束となって、凍えた誰かの心を溶かしてゆく。",
        "example": "The bride radiated happiness, her face glowing with extraordinary radiance.",
        "deep_dive": { "roots": [{"term": "re-", "meaning": "to spread"}], "points": ["radio（ラジオ）や ray（光線）と同じ。見えない波となって世界を震わせる力。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "clarity_light",
        "word": "Clarity",
        "meaning": "明快、透明、(精神の)純粋さ",
        "era": "14th Century Latin clarus",
        "etymology": {
            "components": ["clarus (clear, bright, distinct, manifest)"],
            "original_statement": "From Old French clarte, from Latin claritatem (clearness, brightness), from clarus (clear, bright, distinct)."
        },
        "concept": "Clear and distinct (一点の汚れもなく「澄み渡って（clear）」おり、輪郭が「はっきり（distinct）」していること)",
        "thinking": "混じり気（Impurity）が一切なく、そのもの本来の姿が完璧に現れている状態. 語源の clarus は、明るい音（声）をも意味しました。それは、視覚的な透明さだけでなく、意志や言葉が一点の淀みもなく相手に届く「潔さ」を指します。シンプルであることの、究極の到達点。",
        "aftertaste": "淀みのない響き. あなたの人生から余分なものを削ぎ落としたとき、そこにはクリスタルのような純粋な輝きが残る。",
        "example": "The manager's instructions were characterized by remarkable clarity and precision.",
        "deep_dive": { "roots": [{"term": "kel-", "meaning": "to shout"}], "points": ["claim（主張する）や declare（宣言する）と同じ、『はっきりした声』のルーツ。"] },
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
        print(f"Success: Added {added} words in Cycle 99.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
