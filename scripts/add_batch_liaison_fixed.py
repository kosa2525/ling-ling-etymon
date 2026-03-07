import json
import re

word_batch = [
    # Cycle 166: Bridge & Path (Refined II)
    {
        "id": "liaison_bridge_fixed",
        "word": "Liaison",
        "meaning": "連絡、提携、(料理)つなぎ、情事",
        "era": "17th Century Latin ligare",
        "etymology": {
            "components": ["ligare (to bind)"],
            "original_statement": "From French liaison (a binding, connection), from Late Latin ligationem (a binding), from Latin ligare (to bind, tie)."
        },
        "concept": "Binding connection (「孤立（isolation）」した 「領域（realms）」を 「聖なる糸（holy thread）」で 「縫い合わせ（stitch）」 意味を 「通奏（resonate）」させること)",
        "thinking": "二つの 異質な 存在の 間に 立ち、情報を 媒介し、調和を 産み出す、透明で 強靭な 繋ぎ役. 語源は「縛ること、結ぶこと」. それは どちらか への 従属 ではなく 両者の 尊厳を 保ったまま 一つの 巨大な 物語（コンテクスト）を 織り上げようとする 聖なる「触媒」の 表現です. 連絡は、愛です.",
        "aftertaste": "聖なる繋ぎ役. 自分が 誰の役にも 立っていない と 嘆かないで. あなたが「リエゾン（連絡）」として 誰かと 誰かの 想いを 繋いでいるとき この 世界には 孤独を 越えた 壮大な 智慧の 織物が 完成してゆくのだから.",
        "example": "She served as a military liaison, ensuring smooth communication between the allied forces during the operation.",
        "deep_dive": { "roots": [{"term": "leig-", "meaning": "to bind"}], "points": ["religion（宗教：再び結ぶもの）や rely（信頼する：頼りに結ぶ）と同じ。魂の 繋がりのルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "itinerary_path",
        "word": "Itinerary",
        "meaning": "旅行計画、旅程表、旅の記録",
        "era": "15th Century Latin iter",
        "etymology": {
            "components": ["iter (a journey, way)"],
            "original_statement": "From Late Latin itinerarium (account of a journey, road map), from Latin itineris, genitive of iter (a journey, way, road), from ire (to go)."
        },
        "concept": "Plan for going (「未知（unknown）」の 「空間（space）」を 「意味（meaning）」のある 「時間（time）」の 「連鎖」へと 変容させること)",
        "thinking": "行き当たりばったり ではなく、自らの 目的地（インテンション）を 定め、一歩一歩の 歩みに 聖なる 順序と 意味を 与える、知的な 冒険の 羅針盤. 語源は「旅、道、行くこと」. それは 自由を 制限する 鎖 ではなく 宇宙という 広大な 迷宮の中で 自分自身を 見失わないための 聖なる「航跡図」の 表現です.",
        "aftertaste": "冒険の航跡図. 迷うことを 恐れないで. あなたが 自分だけの「アイティネラリ（旅程）」を 描き 自分の 足跡（過去）を 愛し続けるとき あらゆる 寄り道は 最高の 答えへと 辿り着くための 聖なる 伏線に なるのだから.",
        "example": "Our detailed itinerary included a three-day hike through the ancient ruins and a visit to the local temple.",
        "deep_dive": { "roots": [{"term": "ei-", "meaning": "to go"}], "points": ["exit（出口）や transit（通過）と同じ。移動することそのものが、存在の証。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "conduit_bridge",
        "word": "Conduit",
        "meaning": "導管、(情報の)伝達路、噴水、水路",
        "era": "14th Century Latin con- + ducere",
        "etymology": {
            "components": ["con- (together)", "ducere (to lead)"],
            "original_statement": "From Old French conduit, from Medieval Latin conductus (a defense, escort, pipe), from Latin conducere (to lead together)."
        },
        "concept": "Leading together (「源泉（source）」から 溢れ出す 「エナジー」を 「目的地（target）」へと 「純粋（pure）」なまま 「運ぶ（transport）」 聖なる 器)",
        "thinking": "自らを 主張（ノイズ）する のではなく、ただ 聖なる 流れ（インスピレーション）を 通すための 透明な 器（パイプ）として 徹すること. 語源は「共に導くこと」. それは 空虚 ではなく 宇宙の 豊かさを 渇いた 場所へと 届けるための 聖なる「奉仕（サービス）」のアクションです. 導管は、慈愛です.",
        "aftertaste": "透明な奉仕. 「自分には 何もない」と 悲しまないで. あなたが「コンジット（導管）」として 誰かの 想いさや 優しさを そのまま 次の人へと 手渡すとき あなたは 世界を 潤す 聖なる 水脈の 一部に なっているのだから.",
        "example": "He acted as a conduit for the local artisans, helping them reach a much larger global market.",
        "deep_dive": { "roots": [{"term": "deuk-", "meaning": "to lead"}], "points": ["educate（教育する：引き出す）や produce（生産する：前に導く）と同じ。導きという名の、文明의ルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "viaduct_bridge",
        "word": "Viaduct",
        "meaning": "高架橋、陸橋",
        "era": "19th Century Latin via + ducere",
        "etymology": {
            "components": ["via (way, road)", "ducere (to lead)"],
            "original_statement": "From Latin via (way, road) + -duct, on the model of aqueduct (water-bridge)."
        },
        "concept": "Way-lead (「障壁（obstacle）」を 「上空（above）」から 「超越（transcend）」し 「断絶（disconnection）」を 「永遠」の 「架け橋」へと 変えること)",
        "thinking": "谷や 裂け目（ディビジョン）に 絶望する のではなく、自らが 壮大な 構造物（ストラクチャー）となって、その上を 平然と 渡りきり、不可能を 可能に する 意志の 建築学. 語源は「道の導き、道の架け橋」. それは 困難 への 回避 ではなく 視座を 高める（ハイ・プレイス）ことで 全く新しい 繋がりを 創造しようとする 聖なる「飛躍」の 表現です.",
        "aftertaste": "超越の架け橋. 目の前の 深い谷（孤独）に 立ちすくまないで. あなたの 築き上げた「ヴァイアダクト（高架橋）」のような 高い 理想と 勇気が 誰かの 絶望を 希望へと 繋ぐ 聖なる 道に なるのだから.",
        "example": "The magnificent Victorian viaduct swept across the valley, carrying trains high above the river below.",
        "deep_dive": { "roots": [{"term": "wegh-", "meaning": "to go, transport (for via)"}], "points": ["way（道）や vehicle（車両）と同じ。移動を 支える 意志のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "traverse_path",
        "word": "Traverse",
        "meaning": "横断する、詳しく検討する、反対する、(壁などを)横切る",
        "era": "14th Century Latin trans- + vertere",
        "etymology": {
            "components": ["trans- (across)", "vertere (to turn)"],
            "original_statement": "From Old French traverser (to cross, thwart), from Late Latin transversare, from Latin transversus (turned across), from trans- (across) + vertere (to turn)."
        },
        "concept": "Turning across (「安住（status quo）」の 地を 離れ 「未知（unknown）」の 「広がり」を 「縦走（cross）」することで 魂を 「拡張」すること)",
        "thinking": "定められた 道を なぞる のではなく、自らの 意志で 垂直な 壁や 未踏の 荒野を 横切り、世界の あらゆる 側面を 実感として 獲得してゆく、野性的な 知性の 躍動. 語源は「横へ向く、横切る」. それは 逃避 ではなく 宇宙の 全体性（ホリスティック）に 触れようとする 聖なる「巡礼」のアクションです.",
        "aftertaste": "未知の縦走. 安全な 場所に 留まっている 自分を 卒業しよう. あなたが 未知の 領域を「トラヴァース（横断）」し 自分の 限界を 超えてゆくとき 世界は かつてない 広がりと 輝きを持って あなたを 迎え入れてくれるのだから.",
        "example": "The team had to traverse a treacherous glacier to reach the summit of the mountain.",
        "deep_dive": { "roots": [{"term": "wer-", "meaning": "to turn"}], "points": ["universe（宇宙：一つに回転するもの）や introvert（内向的な）と同じ。方向性という名の、存在の 証。"] },
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
        print(f"Success: Added {added} words in Cycle 166.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
