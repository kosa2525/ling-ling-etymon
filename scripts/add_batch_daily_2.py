import json
import re

word_batch = [
    {
        "id": "morning",
        "word": "Morning",
        "meaning": "朝、午前中",
        "era": "13th Century Old English morwen",
        "etymology": {
            "components": ["morgen (morning)"],
            "original_statement": "From Old English morewen, from morwen, from Proto-Germanic *murgan- (morning, break of day)."
        },
        "concept": "The break of day (一日の始まり、夜明け)",
        "thinking": "「明日」を意味する tomorrow（to + morrow）と同じ語源から生まれました。夜の闇が終わり、新しい時間が少しずつ「形を成してくる（form）」という明るい兆しの時間。もともとは『夜明け』という一点の瞬間を指していました。",
        "aftertaste": "昨日をリセットする、最初の光の粒。",
        "example": "I enjoy the quiet of the early morning.",
        "deep_dive": {
            "roots": [{"term": "mer-", "meaning": "to shimmer, glisten"}],
            "points": ["『きらきら光る（shimmer）』という言葉に繋がっています。朝露が光るイメージ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "lunch",
        "word": "Lunch",
        "meaning": "昼食、ランチ",
        "era": "16th Century Spanish lonja",
        "etymology": {
            "components": ["lonja (slice)"],
            "original_statement": "Probably from Spanish lonja (a slice of ham), originally meaning a 'thick piece, hunk'."
        },
        "concept": "A thick piece or hunk (厚く切ったかたまり)",
        "thinking": "もともとは『昼の食事』という名前ではなく、パンやハムの『分厚い一切れ（hunk）』を意味する言葉でした。仕事の合間にパクっと食べる軽食（luncheon）が短縮され、現代の『ランチ』という優雅な響きになりました。始まりは無骨な肉の塊だったのです。",
        "aftertaste": "ひと塊のエネルギー。午後へ向かうための燃料。",
        "example": "Let's meet for lunch at the usual cafe.",
        "deep_dive": {
            "roots": [],
            "points": ["lump（かたまり）と同類で、お腹を満たす確かな重みを感じさせる言葉。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "evening",
        "word": "Evening",
        "meaning": "夕方、晩、宵",
        "era": "Old English æfnung",
        "etymology": {
            "components": ["æfen (eve, evening)"],
            "original_statement": "From Old English æfnung (the coming of evening), from æfen (evening)."
        },
        "concept": "The coming of the eve (一日の終わりの始まり)",
        "thinking": "「等しい（even）」という言葉と関係があるとされる興味深い単語。一日と夜の境界が曖昧になり、光が「フラット（even）」になっていく時間。あるいは昼間に騒がしく動いていたすべてを平らにならす、静寂への準備。クリスマスイブの『イブ（eve）』と同じルーツです。",
        "aftertaste": "輪郭がぼやけ、すべてが等しく影へと溶けてゆく。",
        "example": "They took a walk along the river in the cool evening.",
        "deep_dive": {
            "roots": [{"term": "epi-", "meaning": "on, near"}],
            "points": ["after（後の）に近い語源という説もあります。一日の後の時間です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "neighbor",
        "word": "Neighbor",
        "meaning": "隣人、近所の人",
        "era": "Old English neahgebur",
        "etymology": {
            "components": ["neah (near)", "gebur (dweller, farmer)"],
            "original_statement": "From Old English neahgebur, from neah (near) + gebur (dweller, freeholder, farmer)."
        },
        "concept": "A farmer living nearby (近くに住む農夫)",
        "thinking": "「近く（near：neah）」に住み、「土地を耕す人（dweller：gebur）」という意味の合体語です。お互いの生活圏が見える場所に、自分の家と同じように地面に根を張って生きている人。物理的な距離だけでなく、生活の共有を静かに示す言葉です。",
        "aftertaste": "柵の向こうに。一番近い、違う人生の灯火。",
        "example": "Our new neighbor brought us some cookies as a greeting.",
        "deep_dive": {
            "roots": [{"term": "near-", "meaning": "high, near"}, {"term": "bheu-", "meaning": "to be, exist, dwell"}],
            "points": ["be（ある）や build（建てる）のルーツである bheu- が隠されています。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "kitchen",
        "word": "Kitchen",
        "meaning": "台所、キッチン",
        "era": "Old English cycene",
        "etymology": {
            "components": ["coquus (cook)"],
            "original_statement": "From Latin coquina (kitchen), from coquere (to cook)."
        },
        "concept": "A place for cooking (調理する場所)",
        "thinking": "ラテン語で「料理する（coquere）」という動詞から派生。火を使い、命（食材）を糧（料理）へと変える魔法の工房。家族のエネルギーが生み出される中心地であり、そこには常に温かな「火（hearth）」の気配があります。",
        "aftertaste": "湯気に包まれた、最も正直な自分に帰る場所。",
        "example": "The family gathered in the kitchen while dinner was cooking.",
        "deep_dive": {
            "roots": [{"term": "pekw-", "meaning": "to cook, ripen"}],
            "points": ["cook（料理人）や concoct（でっち上げる：混ぜて作る）のルーツです。"]
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
