import json
import re

word_batch = [
    # Cycle 76: Expansion & Space
    {
        "id": "expansion_space",
        "word": "Expansion",
        "meaning": "拡大、拡張、膨張",
        "era": "15th Century Old French/Latin ex- + pandere",
        "etymology": {
            "components": ["ex- (out)", "pandere (to spread, stretch)"],
            "original_statement": "From Latin expansionem, from expandere (to spread out, stretch out), from ex- (out) + pandere (to spread)."
        },
        "concept": "Spreading out (外に向かって「広げ（spread）」ていくこと)",
        "thinking": "閉じ込められていたエネルギーが、境界を押し広げて外へと溢れ出していくプロセス。宇宙の膨張、あるいは意識の拡大。それは単に大きくなることではなく、未知の領域へと自分の「場所」を拡張し、新しい可能性を空間に書き込んでいく、生命の呼吸のような動きです。",
        "aftertaste": "際限のない渇望。境界線は、あなたがそこへ辿り着いた瞬間に、さらに遠くへと退（しりぞ）く。",
        "example": "The expansion of the universe is accelerating according to the latest observations.",
        "deep_dive": { "roots": [{"term": "pete-", "meaning": "to spread"}], "points": ["expand（広げる）や span（期間/幅）と同じ、空間を掌握するルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "amplitude_space",
        "word": "Amplitude",
        "meaning": "広さ、振幅、豊かさ",
        "era": "16th Century Latin amplus",
        "etymology": {
            "components": ["amplus (large, wide, spacious)"],
            "original_statement": "From Latin amplitudinem (wide extent, width), from amplus (large, spacious)."
        },
        "concept": "The quality of being large (「広い（large）」こと、その豊かさの度合い)",
        "thinking": "物理的な波動の「大きさ」を指すと同時に、精神的な「懐（ふところ）の深さ」や、思考の「壮大さ」をも意味します。語源の amplus は、単に巨大であるだけでなく、そこにある種の「余裕」や「豊穣さ」が満ちているニュアンス。世界をまるごと受け入れる、器（うつわ）の大きさです。",
        "aftertaste": "静かなる充足。あなたが大きく揺れるたび、世界の密度がより深く、濃くなっていく。",
        "example": "The amplitude of the sound waves determines the loudness of the music we hear.",
        "deep_dive": { "roots": [{"term": "am-", "meaning": "around (possible)"}], "points": ["ample（十分な）や amplify（増幅する）と同じ『満たされた広がり』。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "dimension_space",
        "word": "Dimension",
        "meaning": "寸法、次元、特質",
        "era": "14th Century Latin dis- + metiri",
        "etymology": {
            "components": ["dis- (apart)", "metiri (to measure)"],
            "original_statement": "From Latin dimensionem (a measuring), from dimensus, past participle of dimetiri (to measure out), from dis- (apart) + metiri (to measure)."
        },
        "concept": "Measuring apart (空間を「計測（measure）」して切り分けること)",
        "thinking": "混沌とした広がりの中に、長さ、幅、高さという「尺度（measure）」を導入し、意味のある空間として切り取ること。次元が増えるたびに、世界は全く新しい姿を見せ始めます。人間関係や芸術においても「新しい次元（dimension）」が加わるとき、それは物事の見方を根本から変えてしまいます。",
        "aftertaste": "視点の獲得。線を面に、面を立体に変えるのは、いつだってあなたの『計測』という意識。",
        "example": "His discovery added a whole new dimension to our understanding of the problem.",
        "deep_dive": { "roots": [{"term": "me-", "meaning": "to measure"}], "points": ["measure（測る）や symmetry（対称）と同じ、理知的な秩序。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "void_space",
        "word": "Void",
        "meaning": "空白、虚空、無効な",
        "era": "13th Century Old French/Latin vacare",
        "etymology": {
            "components": ["vacuus (empty, free, waste)"],
            "original_statement": "From Anglo-French voide, from Latin vocivos (empty, free), related to vacare (to be empty)."
        },
        "concept": "Being empty (中身がなく「空っぽ（empty）」であること、その自由さ)",
        "thinking": "何も存在しない、底知れぬ暗闇や空白。それは恐怖を呼び起こす「欠落」であると同時に、まだ何にも染まっていない「究極の自由」でもあります。芸術家が白いキャンバスを目の前にする時、そこにあるのは「虚空（void）」であり、同時にすべての可能性の源泉（Matrix）なのです。",
        "aftertaste": "完璧な静寂。空っぽであるからこそ、あなたは世界中のどんな色も、どんな響きも受け入れられる。",
        "example": "The decision was declared null and void by the high court after the investigation.",
        "deep_dive": { "roots": [{"term": "wak-", "meaning": "empty"}], "points": ["vacuum（真空）や vacation（休暇：仕事を空にする時間）と同じ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "vastness_space",
        "word": "Vast",
        "meaning": "広大な、莫大な、空虚な",
        "era": "16th Century Latin vastus",
        "etymology": {
            "components": ["vastus (empty, waste, unoccupied, enormous)"],
            "original_statement": "From French vaste, from Latin vastus (empty, waste, unoccupied, desolated, enormous)."
        },
        "concept": "Empty and immense (あまりに「空虚（empty）」であるがゆえに、果てしなく巨大に見えること)",
        "thinking": "ただ大きい（big）のではなく、そこに人間的な尺度を拒絶するような「底知れぬ空（から）っぽさ」と「巨大さ」が同居している状態。荒野や大宇宙。それは美しさ（sublime）であると同時に、自分という存在の小ささを突きつける、暴力的なまでの広がりです。",
        "aftertaste": "のみ込まれる。その広大さの前で、あなたの言葉も、あなたの痛みも、星屑の一つとなって消えてゆく。",
        "example": "Looking out at the vast ocean, he felt a strange mix of peace and insignificance.",
        "deep_dive": { "roots": [{"term": "wak-", "meaning": "empty"}], "points": ["void と同じ『空（wak-）』のルーツから。巨大さは常に、空白を孕んでいる。"] },
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
        print(f"Success: Added {added} words in Cycle 76.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
