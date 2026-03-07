import json
import re

word_batch = [
    # Cycle 148: Threshold & Doorway (Refined)
    {
        "id": "liminal_threshold",
        "word": "Liminal",
        "meaning": "境界の、敷居の、どちらともつかない、中間的な",
        "era": "19th Century Latin limen",
        "etymology": {
            "components": ["limen (threshold, lintel)"],
            "original_statement": "From Latin limen (threshold, cross-piece, lintel, sill), from an unknown source."
        },
        "concept": "Of the threshold (「過去（past）」を 離れ 「未来（future）」へと 足を 踏み出す 瞬間の 「浮遊感」)",
        "thinking": "どちらの場所にも属さず、無限の可能性だけが 充満している、聖なる「空白（ポーズ）」の 状態. 語源は「敷居」. それは 不安であると同時に あなたが 何者にも 変容できるという 究極の 自由を 象徴しています. 境界こそが、真の居場所です.",
        "aftertaste": "境界の自由. 早く どこかに 辿り着こうと しなくていい. あなたが「リミナル（境界の）」な 宙づりの状態を 楽しむとき 人生は 最も 豊かで 神秘的な 色彩を 帯びるのだから.",
        "example": "The airport lounge at midnight felt like a strange, liminal space, disconnected from both origin and destination.",
        "deep_dive": { "roots": [{"term": "el-", "meaning": "to bend (possible root)"}], "points": ["eliminate（排除する：敷居の外へ出す）と同じ。境界線という名の、選別の場所。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "portal_doorway",
        "word": "Portal",
        "meaning": "正門、玄関、(Web)ポータルサイト、(SF)瞬間移動の門",
        "era": "14th Century Latin porta",
        "etymology": {
            "components": ["porta (gate, door, entrance)"],
            "original_statement": "From Old French portal, from Medieval Latin portale (city gate, porch), noun use of Latin portalis (of a gate), from porta (gate)."
        },
        "concept": "Grand entrance (「日常（ordinary）」を 越え 「非日常（extraordinary）」へと 魂を 「誘う（invite）」 巨大な 門)",
        "thinking": "単なる通り道ではなく、そこをくぐることで 意識や 運命が 劇的に 書き換えられるような 意志の 結節点. 語源は「門」. それは 新しい知性、新しい人間関係、あるいは 新しい自分へと 接続するための、誇り高い 聖なる 接続端子（インターフェース）です.",
        "aftertaste": "変容の門. 今、あなたの目の前にある 困難は 実は新しい世界への「ポータル（正門）」なのかもしれない. 勇気を持って その門を くぐることで あなたは 全く新しい 輝きを 手にするのだから.",
        "example": "The ancient library was a portal to a world of forgotten wisdom and ancient civilizations.",
        "deep_dive": { "roots": [{"term": "per-", "meaning": "to lead across, pass through"}], "points": ["port（港）や fare（行く）と同じ。移動と越境、および歓迎のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "ingress_doorway",
        "word": "Ingress",
        "meaning": "進入、入場、入り口、(天体)潜入",
        "era": "15th Century Latin in- + gradi",
        "etymology": {
            "components": ["in- (into)", "gradi (to step, go)"],
            "original_statement": "From Latin ingressus (an entering), from ingredi (to go in, enter, step into), from in- (into) + gradi (to step, go, walk)."
        },
        "concept": "Stepping into (「未知（unknown）」の 領域へと 「自らの足（feet）」で 一歩 「踏み出し（step）」 参加すること)",
        "thinking": "受動的な 待機を やめ 自らの意志によって 境界線を 越え 世界の一部へと 溶け込んでいく 力強い アクション. 語源は「中へ歩むこと」. それは 誰かに 招かれるのを 待つのではなく 自らが その場の 主人公として 振る舞い始めるための 誇り高い 儀式です. 踏み込みは、信頼です.",
        "aftertaste": "第一歩の勇気. 境界線の外側で 眺めているだけでは 何も変わらない. あなたが「イングレス（進入）」を決意し 聖なる一歩を 踏み出したとき 世界の全ては あなたを 歓迎し 始めるのだから.",
        "example": "The digital system recorded every ingress and egress to the secure facility in real-time.",
        "deep_dive": { "roots": [{"term": "ghredh-", "meaning": "to walk, go"}], "points": ["grade（等級）や progress（進歩）と同じ。階段を一段昇るような、着実な進化。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "threshold_doorway",
        "word": "Threshold",
        "meaning": "敷居、入り口、(意識の)閾(いき)値、始まり",
        "era": "Pre-12th Century Old English threscan",
        "etymology": {
            "components": ["threscan (to thresh, tread)"],
            "original_statement": "From Old English therscold, thærscold (doorsill, threshold), etymology uncertain, but related to threscan (to thresh, tread)."
        },
        "concept": "Threshing place (「古い殻（old husk）」を 「踏みしだき（thresh）」 真の 「実り（seed）」を 取り出す 荒々しい 境界)",
        "thinking": "単なる平坦な境界ではなく、そこを通る際に 不必要な執着を 脱ぎ捨て、魂を 研磨するための 試練の場所. 語源は「踏み鳴らす場所（脱穀）」. それは 痛みを伴う 変容を 経て 初めて 新しいステージに 立つことが 許されるという 宇宙の 厳格で 優しい 法則です.",
        "aftertaste": "脱皮の儀式. 今、あなたが感じている 苦痛は 古い自分を 脱ぎ捨てるための「スレッシュホールド（敷居）」の 試練なのだ. その後に現れる 純粋な あなたを 世界は 待っているのだから.",
        "example": "Humanity is standing on the threshold of a new era of space exploration and interstellar understanding.",
        "deep_dive": { "roots": [{"term": "ter-", "meaning": "to rub, turn (possible for thresh)"}], "points": ["trite（陳腐な：擦り切れた）と同じ。擦り切れるまで踏みしめた先に、真実がある。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "advent_doorway",
        "word": "Advent",
        "meaning": "到来、降臨、(新しい時代の)幕開け",
        "era": "12th Century Latin ad- + venire",
        "etymology": {
            "components": ["ad- (to)", "venire (to come)"],
            "original_statement": "From Old French advent, from Latin adventus (a coming, approach, arrival), from advenire (to arrive), from ad- (to) + venire (to come)."
        },
        "concept": "Coming to (「向こう側（beyond）」から 「こちら側（here）」へと 「奇跡（miracle）」が 近づいてくる 聖なる 予感)",
        "thinking": "自らが行くのではなく、世界が、あるいは 運命が、大きな音を立てて あなたの元へと 押し寄せ、景色を 一変させてしまうこと. 語源は「やってくること」. それは 待望されていた 救いや 革命が 必然として 現れる、宇宙の 壮大な 贈与の 瞬間を 指しています. 幕開けは、祝福です.",
        "aftertaste": "到来の祝福. あなたが 誠実に 待ち続けてきた その瞬間は 必ず やってくる. 新しい時代の「アドベント（到来）」を 信じて 扉を 大きく開けて おこう. 光は もう すぐそこまで 来ているのだから.",
        "example": "The advent of the internet has fundamentally transformed the way humans communicate and share knowledge.",
        "deep_dive": { "roots": [{"term": "gwa-", "meaning": "to go, come"}], "points": ["venture（冒険）や venue（場所：人が集まる所）と同じ。運命が「出会う」一点。"] },
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
        print(f"Success: Added {added} words in Cycle 148.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
