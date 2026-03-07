import json
import re

word_batch = [
    # Cycle 129: Threshold & Doorway
    {
        "id": "liminal_doorway",
        "word": "Liminal",
        "meaning": "境界の、閾(しきい)の、どちらともつかない中間状態",
        "era": "19th Century Latin limen",
        "etymology": {
            "components": ["limen (threshold)"],
            "original_statement": "From Latin limen (threshold, lintel, sill; entrance, beginning)."
        },
        "concept": "Of the threshold (「しきい（threshold）」の 上に 立ち 「どちらでもない（neither）」 中間的な 移行の状態)",
        "thinking": "過去を捨て去り、しかし未来へもまだ辿り着いていない 宙ぶらりんな「空白の時間（エアー・ポケット）」. 語源は「しきい」. そこは 不安と 圧倒的な可能性が 同居する場所であり 魂が本当の意味で 生まれ変わるための 聖なる待合室です. 曖昧さを 恐れずに留まる勇気を.",
        "aftertaste": "夜明けの境界. 明確な答えを 急がないで. この「リミナル（中間的）」な揺らぎの中にこそ あなたがまだ気づいていない 新しい自分という名の扉が 隠されているのだから.",
        "example": "The period between graduation and starting a new job can feel like a strange, liminal space.",
        "deep_dive": { "roots": [{"term": "el-", "meaning": "to bend (possible for limen)"}], "points": ["eliminate（排除する：しきいの外に出す）や preliminary（予備の：しきいの前の）と同じ。越境のルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "portal_doorway",
        "word": "Portal",
        "meaning": "正門、堂々とした入口、(他世界への)入り口、ポータル",
        "era": "14th Century Latin porta",
        "etymology": {
            "components": ["porta (gate)"],
            "original_statement": "From Old French portal, from Medieval Latin portale (city gate, porch), from Latin porta (gate, door, entrance)."
        },
        "concept": "Grand entrance (「門（gate）」を 通り抜け 「別世界（another world）」へと 移行するための 象徴的な 入口)",
        "thinking": "単なる通り道ではなく それを潜り抜けることで 意識や環境が 劇的に変化することを約束する 尊厳ある入口. 語源は「門」. それは 覚悟を持って潜るべき場所であり その門の向こう側には 今までとは全く違う 輝かしい（あるいは未知の）風景が 広がっています.",
        "aftertaste": "決意の正門. あなたの目の前にある その「変化」という名のポータルを 恐れずに潜り抜けよう. その先には あなたが夢見ていた 新しい宇宙が 待っているのだから.",
        "example": "The ancient stone portal was adorned with mysterious symbols of a lost civilization.",
        "deep_dive": { "roots": [{"term": "per-", "meaning": "to go over, cross"}], "points": ["port（港：入り口）や opportunity（機会：港の前で風を待つこと）と同じ。運命の越境。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "initiation_doorway",
        "word": "Initiation",
        "meaning": "開始、入会式、通過儀礼、伝授",
        "era": "16th Century Latin in- + ire",
        "etymology": {
            "components": ["in- (into)", "ire (to go)"],
            "original_statement": "From Latin initiationem (a beginning), from initiare (to begin, originate), from initium (a beginning, a going in), from in- (into, in) + ire (to go)."
        },
        "concept": "Going into (「中へと（into）」 「踏み出す（go）」 ことで 新しい 世界の 「秘密（secret）」に 触れること)",
        "thinking": "受動的に始まるのではなく 自らの意志で 境界線を越え 未知の秩序（コミュニティや智慧）へと 参入していく 厳粛なプロセス. 語源は「中へ行くこと」. それは 痛みや試練を伴うこともありますが 潜り抜けた後には 以前の自分とは 決定的に違う「新しい命」が 宿っています.",
        "aftertaste": "新生の儀式. あなたが今 直面している困難も また一つの「イニシエーション（通過儀礼）」なのだ. それを潜り抜けたとき あなたはより深く、より強く 世界と結ばれることになる.",
        "example": "The young warrior had to undergo a series of difficult tests as part of his initiation into the tribe.",
        "deep_dive": { "roots": [{"term": "ei-", "meaning": "to go"}], "points": ["initial（最初の）や exit（出口）と同じ「進む」のルーツ。始まりとは、常に「参入」である。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "lintel_doorway",
        "word": "Lintel",
        "meaning": "まぐさ、(ドア・窓の)横木",
        "era": "14th Century Latin limen",
        "etymology": {
            "components": ["limen (threshold, lintel)"],
            "original_statement": "From Old French lintel, from Vulgar Latin lintellus, diminutive of Latin limen (threshold, lintel, sill)."
        },
        "concept": "Upper threshold (「しきい（threshold）」と 対になる 「上部の横木（top beam）」 として 空間の 「重み」を 支えるもの)",
        "thinking": "常に私たちの頭上にあり 空間を支え、境界（扉）を形作っている 縁の下ならぬ「縁の上」の実力者. 語源は「しきい」. それは 静かな守護者であり 私たちがその下を潜り抜けるたびに 聖なる場所へと 招き入れてくれる 慈愛に満ちた構造体です.",
        "aftertaste": "守護の天蓋. あなたの頭上には 常にあなたを支え、守ってくれる「リンテル（横木）」があることを 忘れないで. 安心して その扉を 潜り抜けてゆけばいい.",
        "example": "The ornate stone lintel above the cathedral door depicted scenes from ancient scriptures.",
        "deep_dive": { "roots": [{"term": "el-", "meaning": "to bend"}], "points": ["liminal（境界の）と同じルーツ。上下から空間を縁取り、物語を完成させる。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "ingress_doorway",
        "word": "Ingress",
        "meaning": "進入、入り口、(天体の)食の開始",
        "era": "15th Century Latin in- + gradi",
        "etymology": {
            "components": ["in- (into)", "gradi (to step, walk)"],
            "original_statement": "From Latin ingressus (an entering, a going in), from ingredi (to go into, enter), from in- (into, in) + gradi (to step, walk, go)."
        },
        "concept": "Stepping into (「中へ（into）」向かって 「一歩を踏み出す（step）」 物理的・知的な 「参入」)",
        "thinking": "傍観者として留まるのをやめ 自らの足で 境界の内側へと「踏み込む」 具体的で 力強いアクション. 語源は「中へ歩くこと」. 天文学では 星が他の天体の影に入ることを指すように それは 自分の運命が 他の何かと 重なり合い、溶け合っていく 運命的な瞬間でもあります.",
        "aftertaste": "踏み出しの一歩. 外側で眺めているだけでは 真実は見えてこない. 勇気を持って その場所へ「イングレス（進入）」しよう. その一歩が 全てを変える 始まりになるのだから.",
        "example": "High security measures were put in place to control the ingress and egress of the building.",
        "deep_dive": { "roots": [{"term": "ghredh-", "meaning": "to walk, go"}], "points": ["grade（等級：階段の一段）や progress（進歩：前へ歩く）と同じ。一歩の積み重ね。"] },
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
        print(f"Success: Added {added} words in Cycle 129.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
