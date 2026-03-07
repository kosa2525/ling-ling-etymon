import json
import re

word_batch = [
    # Cycle 108: Threshold & Liminality
    {
        "id": "threshold_liminality",
        "word": "Threshold",
        "meaning": "敷居、境界線、始まり、閾値",
        "era": "Old English threshhold",
        "etymology": {
            "components": ["therscan (to thresh)", "haldan (to hold)"],
            "original_statement": "From Old English threscold, threscwald, related to threscan (to thresh) + perhaps a word for tread or wood."
        },
        "concept": "The place of threshing (穀物を「脱穀（thresh）」する場所のように、古い自分を振り落とし、新しい扉を「跨ぐ（tread）」こと)",
        "thinking": "ある状態から別の状態へ移り変わる瞬間の、あの震えるような境界線. 語源は「脱穀する場所」。そこは家と外、聖と俗を分かつ場所であり、同時にそれらが交差する最もエネルギーの強い場所です。あなたが「決意」という名の敷居を跨ぐとき、過去は脱穀され、純粋な意志だけが未来へと運ばれます。",
        "aftertaste": "震える一歩。敷居を越える前の恐怖は、あなたが今、未知という名の美しい宇宙に迎え入れられようとしている証だ。",
        "example": "He stood on the threshold of a new era in his professional life.",
        "deep_dive": { "roots": [{"term": "ter-", "meaning": "to thresh, rub"}, {"term": "kwel-", "meaning": "to turn, dwell"}], "points": ["thresh（脱穀する）と hold（保つ）の融合。境界を守り、耕す力。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "liminal_liminality",
        "word": "Liminal",
        "meaning": "境界の、閾値の、中間状態の",
        "era": "19th Century Latin limen",
        "etymology": {
            "components": ["limen (threshold, lintel)"],
            "original_statement": "From Latin limen (threshold, lintel) + -al."
        },
        "concept": "Of the threshold (「敷居（threshold）」の上に立っているような、どちらでもない「中道（middle）」の、宙ぶらりんな状態)",
        "thinking": "昨日を捨て去ったけれど、明日にはまだ辿り着いていない、あの奇妙な「エアポケット」のような時間. 語源の limen は「敷居」。それは社会的な役割を剥ぎ取られ、ただの「魂」として立ち尽くす瞬間です。しかし、この不安定な「中間の場所」でこそ、私たちは本当の変容を遂げることができます。",
        "aftertaste": "宙ぶらりんの自由。目的地に着くことよりも、この「どちらでもない自分」を味わうことに、深い知性が宿る。",
        "example": "The hotel hallway had a strange, liminal quality at three in the morning.",
        "deep_dive": { "roots": [{"term": "el-", "meaning": "to bend, bow (possible for limen)"}], "points": ["limit（限界）や eliminate（排除する：敷居の外へ出す）と同じ境界のルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "portal_liminality",
        "word": "Portal",
        "meaning": "正門、入り口、(大規模な)扉、ポータルサイト",
        "era": "14th Century Latin porta",
        "etymology": {
            "components": ["porta (gate)"],
            "original_statement": "From Old French portal, from Medieval Latin portale (city-gate, porch), from Latin porta (gate, door, entrance)."
        },
        "concept": "The great gate (都市や宇宙といった、巨大な領域へと踏み出すための「偉大なる扉（gate）」)",
        "thinking": "単なる出入り口ではなく、その向こう側に「全く別の世界」が広がっていることを予感させる、威厳ある構造物. 語源の porta は「門」。それは招待された者だけが通ることを許される、儀式的な境界です。あなたが新しい知識や愛に出会うとき、あなたの心は常に、目に見えないポータルを潜っています。",
        "aftertaste": "未知への招待. 扉を潜るたびに、あなたは少しずつ「以前の自分」を脱ぎ捨て、より大きな存在へと書き換えられてゆく。",
        "example": "The ancient library was a portal to centuries of forgotten human wisdom.",
        "deep_dive": { "roots": [{"term": "per-", "meaning": "to lead across, pass through"}], "points": ["export（輸出）や opportunity（機会：港への入り口）と同じ、通過のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "verge_liminality",
        "word": "Verge",
        "meaning": "縁、端、瀬戸際、(変化の)直前、権杖",
        "era": "14th Century Latin virga",
        "etymology": {
            "components": ["virga (shoot, rod, twig)"],
            "original_statement": "From Old French verge (twig, branch; measuring rod; wand), from Latin virga (shoot, rod, twig)."
        },
        "concept": "The edge marked by a rod (権威の「杖（rod）」で示された「境界線（boundary）」の、ちょうど「端（edge）」にあること)",
        "thinking": "今にも何かが起ころうとしている、極限の緊迫感. 語源の virga は「小枝」や「杖」。杖で地面に線を引いた、そのギリギリの場所。あなたは今、崖っぷちに立っているのではなく、新しい空へ飛び出すための踏み切り板の上に立っています。その緊張感こそが、未来を切り拓く刃になります。",
        "aftertaste": "極限の輝き。瀬戸際に立たされたとき、あなたの魂は最も鋭く、最も真正に、この世界に名乗りを上げる。",
        "example": "The company was on the verge of bankruptcy before the new investment arrived.",
        "deep_dive": { "roots": [{"term": "wei-", "meaning": "to turn, bend"}], "points": ["verge（変化する：傾く）と語源的に融合。杖で指し示された、運命の曲がり角。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "brink_liminality",
        "word": "Brink",
        "meaning": "崖っ縁、(水際の)縁、(重大な事態の)瀬戸際",
        "era": "13th Century Middle Dutch brink",
        "etymology": {
            "components": ["brink- (edge, slope, shore)"],
            "original_statement": "From Middle Dutch brinc (edge, slope, grassland at the edge of a village)."
        },
        "concept": "The village edge (村の「はずれ（edge）」の、「斜面（slope）」のように、日常が終わり、深淵が始まる場所)",
        "thinking": "安全な平地が終わり、その先には広大な海や深い谷が広がっている、危うくも美しい場所. 語源は「村の外れの草地」。それは共同体の守りから外れ、孤独な冒険が始まる地点です。あなたが Brink に立つとき、あなたはもはや誰の保護も受けていませんが、同時に誰よりも自由です。",
        "aftertaste": "断崖の自由. 足元が崩れそうな不安は、あなたが今、重力からの解放を夢見ている魂であることの証（あかし）だ。",
        "example": "The two countries were on the brink of war for several tence weeks.",
        "deep_dive": { "roots": [{"term": "bhreg-", "meaning": "to break"}], "points": ["break（壊れる）や bridge（橋：断絶を越えるもの）同じ。境界は、出会いの場所。"] },
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
        print(f"Success: Added {added} words in Cycle 108.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
