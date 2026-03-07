import json
import re

word_batch = [
    # Cycle 161: Threshold & Doorway (Refined)
    {
        "id": "liminal_threshold_fixed",
        "word": "Liminal",
        "meaning": "境界の、しきい値の、中間の、潜在的な",
        "era": "19th Century Latin limen",
        "etymology": {
            "components": ["limen (threshold)"],
            "original_statement": "From Latin liminalis, from limen (threshold, lintel, sill)."
        },
        "concept": "Between states (「過去（past）」を 離れ 「未来（future）」へと 到る 前の 「静止（stillness）」した 「空白」の 只中（ただなか）に 在ること)",
        "thinking": "定義されること（特定の役割）を 拒絶し、あらゆる 可能性が 揺らいでいる、極めて 繊細で、しかし 強大な エネルギーを 秘めた 境界の 状態. 語源は「しきい、門の横木」. それは 漂う（サスペンド）すること ではなく 全く新しい 自己へと 生まれ変わるための 聖なる「孵化（ふか）」の プロセスです.",
        "aftertaste": "境界の静寂. 今、どちらにも 行けずに 立ち止まっている 自分を 責めないで. その「リミナル（境界的な）」な 空白の中にこそ あなたの 魂が 真に 飛躍するための 聖なる インスピレーションが 眠っているのだから.",
        "example": "The dawn and dusk are liminal times of the day, when the world seems to belong to neither day nor night.",
        "deep_dive": { "roots": [{"term": "el-", "meaning": "to bend (possible for limen)"}], "points": ["eliminate（排除する：しきいの外へ出す）と同じ。境界線を引く力。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "portal_doorway",
        "word": "Portal",
        "meaning": "正門、玄関、入り口、(インターネットの)ポータル",
        "era": "14th Century Latin porta",
        "etymology": {
            "components": ["porta (gate)"],
            "original_statement": "From Old French portal, from Medieval Latin portale (city gate, porch), from Latin porta (gate, door, entrance)."
        },
        "concept": "Majestic entrance (「日常（routine）」から 「非日常（extraordinary）」へと 魂を 「運ぶ（carry）」 壮大な 「装置」)",
        "thinking": "単なる 壁の穴 ではなく、そこを 通り抜けることで 世界の 見え方や 自分自身の 存在そのものが 一変してしまうような、儀式的な 転換点. 語源は「門」. それは 守り（シールド）であると同時に 未知への 招待状（インビテーション）であり 私たちが 勇気を持って 新しい 領域へと 踏み出すための 聖なる「決断」の 表現です.",
        "aftertaste": "変容の門. いつもの 慣れ親しんだ 道を 離れることを 恐れないで. あなたが 目の前の「ポータル（門）」を 潜り（くぐり）抜けたとき 人生は かつてない 壮大で 美しい 景色を あなたに 見せてくれるのだから.",
        "example": "The ancient stone portal was covered in mysterious carvings that seemed to tell the story of a lost civilization.",
        "deep_dive": { "roots": [{"term": "per-", "meaning": "to lead across, pass through"}], "points": ["port（港：入り口）や portable（持ち運びできる）と同じ。移動と 接続のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "threshold_doorway",
        "word": "Threshold",
        "meaning": "しきい、入り口、境界、(刺激の)最低値",
        "era": "Pre-12th Century Old English threscan",
        "etymology": {
            "components": ["threscan (to tread, thresh)"],
            "original_statement": "From Old English therscwold, threscold, probably meaning 'the place where the corn is trodden or threshed'."
        },
        "concept": "Treading place (「足（feet）」で 「踏み固められた（trodden）」 境界であり そこを 越えることで 「新しい 段階（new level）」が 始まること)",
        "thinking": "頭で 考える 境界 ではなく、実際に 足（ステップ）を踏み出し、摩擦や 抵抗を 乗り越えて 辿り着く、具体的な 変化の 起点. 語源は「脱穀する、踏む」. それは 激しい 試練（踏まれること）の 果てに 不純物を 削ぎ落とし 魂の 「核」だけが 新しい 世界へと 踏み出すための 聖なる「選別」の 表現です.",
        "aftertaste": "始まりの足音. 変化に伴う 痛み（摩擦）を 嫌わないで. あなたが その「スレショルド（しきい）」を 踏み越えたとき あなたは 確実に 前の自分とは 違う より高い 精神の 段階へと 辿り着いているのだから.",
        "example": "He stood on the threshold of a brilliant career in international diplomacy.",
        "deep_dive": { "roots": [{"term": "ter-", "meaning": "to rub, turn"}], "points": ["thresh（脱穀する）や thrash（激しく動く）と同じ。摩擦という名の、進化のエナジー。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "initiate_doorway",
        "word": "Initiate",
        "meaning": "始める、開始する、伝授する、(秘密の会などに)入会させる",
        "era": "16th Century Latin in- + ire",
        "etymology": {
            "components": ["in- (into)", "ire (to go)"],
            "original_statement": "From Latin initiatus, past participle of initiare (to begin, originate), from initium (a beginning), from in- (into) + ire (to go)."
        },
        "concept": "Going into (「未知（unknown）」の 内部へと 「自ら（self）」 踏み込み 「真理」の 「一部」に なること)",
        "thinking": "単なる スタート ではなく、秘められた 知識や 共同体の 核へと 迎え入れられ、自分自身の アイデンティティが 更新される、重厚な 儀式的 アクション. 語源は「中へ行く」. それは 外側から 眺める 傍観者（オブザーバー）を 卒業し 世界の 意志の 担い手へと 変容しようとする 聖なる「覚醒」の 表現です.",
        "aftertaste": "未知への一歩. 「自分には まだ早い」と 謙遜（けんそん）しないで. あなたが 自らの 意思で「イニシエイト（開始/伝授）」し その扉を 叩くとき 隠されていた 知恵の 全ては あなたの 元へと 流れ出してくるのだから.",
        "example": "The program was designed to initiate students into the complex world of quantum computing.",
        "deep_dive": { "roots": [{"term": "ei-", "meaning": "to go"}], "points": ["exit（出口）や transit（通過）と同じ。移動することそのものが、存在の証。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "vestibule_doorway",
        "word": "Vestibule",
        "meaning": "玄関の間、前庭、(解剖)前庭",
        "era": "17th Century Latin vestibulum",
        "etymology": {
            "components": ["vestis (garment, clothing)"],
            "original_statement": "From Latin vestibulum (forecourt, entrance court), possibly related to vestis (clothing, garment), meaning 'the place where one puts on or takes off clothes'."
        },
        "concept": "Place of garments (「外面（outside mask）」を 「脱ぎ捨て（take off）」 「本来の自分（true self）」に 戻るための 「準備の間」)",
        "thinking": "メインの 空間へと 入る前に 自分の 状態を 整え（チューニング）、外の 喧騒を 振り払い（浄化）、静寂へと 心を 移し替えるための、聖なる「猶予（ゆうよ）」の 空間. 語源は「衣服、身なり」. それは 飾る ことではなく むしろ 余計なものを 脱ぎ捨て 本質へと 戻るための 聖なる「リセット」の アクションです.",
        "aftertaste": "浄化の空間. すぐに 結論を 出そうと 急がないで. あなた自身の 心の「ヴェスティビュール（前庭）」で じっくりと 自分の想いを 整理し 本来の 自分を 取り戻してから 進めばいいのだから.",
        "example": "He waited in the quiet vestibule, gathering his thoughts before entering the grand ballroom.",
        "deep_dive": { "roots": [{"term": "wes-", "meaning": "to dress"}], "points": ["vest（ベスト：衣服）や invest（投資する：服を着せる）と同じ。存在を纏う（まとう）こと。"] },
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
        print(f"Success: Added {added} words in Cycle 161.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
