import json
import re

word_batch = [
    # Cycle 157: Pattern & Symmetry (Refined)
    {
        "id": "tessellation_pattern",
        "word": "Tessellation",
        "meaning": "テセレーション、モザイク模様、隙間なく並べること",
        "era": "17th Century Latin tessella",
        "etymology": {
            "components": ["tessella (little square stone)"],
            "original_statement": "From Latin tessellatus (made of small square stones or tiles), from tessella (small square piece), diminutive of tessera (a square piece)."
        },
        "concept": "Tiling without gaps (「個（individual）」が 「境界線（boundary）」を 分かち合い 「全体（whole）」としての 「一貫性」を 築くこと)",
        "thinking": "自分勝手な形（エゴ）を 追求するのではなく、隣り合う他者と 完全に 噛み合うように 自らを 律することで、終わりなき 美しい 秩序（宇宙）を 形成すること. 語源は「小さな四角い石」. それは 無秩序（カオス）の中に、同一の リズムを 敷き詰めることで 混沌を 聖なる 曼荼羅（まんだら）へと 変容させる 意志のアクションです.",
        "aftertaste": "重なりの調和. 自分という ピースを 無理に 変えようと しなくていい. あなたが そのままの形で 誰かと「テセレーション（敷居なく並ぶ）」したとき そこには 宇宙の 壮大な 模様が 描き出されるのだから.",
        "example": "M.C. Escher is famous for his incredible drawings that use complex tessellation of animals and birds.",
        "deep_dive": { "roots": [{"term": "kwetwer-", "meaning": "four"}], "points": ["quarter（四分の一）や square（正方形）と同じ。四角という名の、安定の象徴。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "isometric_symmetry",
        "word": "Isometric",
        "meaning": "等尺性の、等距離の、アイソメトリックな",
        "era": "19th Century Greek isos + metron",
        "etymology": {
            "components": ["isos (equal)", "metron (measure)"],
            "original_statement": "From Greek isometros (of equal measure), from isos (equal) + metron (measure)."
        },
        "concept": "Equal measure (「視点（perspective）」に よる 「歪み（distortion）」を 排し 全てを 「公平（fair）」に 捉え直すこと)",
        "thinking": "手前が大きく 奥が小さいという 主観的な 印象（パース）を 捨て、あらゆる要素を 同じ重み、同じスケールで 平行に 並べるという、冷徹で 公平な 知性の 視座. 語源は「等しい尺度」. それは 感情的な 偏りを 廃し 真実を 幾何学的な 正確さをもって 記述しようとする、聖なる「誠実さ」の 表現です.",
        "aftertaste": "公平な眼差し. 自分の 都合だけで 世界を 歪めて 見ないで. あなたが「アイソメトリック（等尺的）」な 冷静さを 持つとき どんな複雑な 葛藤も 明快な 構造（パターン）として 整理されるのだから.",
        "example": "The engineer provided an isometric drawing of the new bridge to show its precise structural dimensions.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["isosceles（二等辺三角形）や isolated（隔離された：島のような単一の）の語源に関わる説も。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "recurrence_pattern",
        "word": "Recurrence",
        "meaning": "再発、回帰、繰り返し、循環",
        "era": "17th Century Latin re- + currere",
        "etymology": {
            "components": ["re- (again)", "currere (to run)"],
            "original_statement": "From Latin recurrens, past participle of recurrere (to run back, hasten back, return), from re- (again, back) + currere (to run)."
        },
        "concept": "Running back (「時間（time）」が 「直線（line）」を 離れ 「円環（circle）」へと 戻ることで 意味を 「深める」こと)",
        "thinking": "一度きりの 出来事として 消費するのではなく、何度も 同じ場所に 戻ってくる（回帰する）ことで、その 本質を より高い 螺旋（スパイラル）の 段階で 理解し直すこと. 語源は「再び走る」. それは 飽き（マンネリ）ではなく 絶え間ない 復習（リフレッシュ）を通じて 存在を 永遠化しようとする 聖なる「リズム」の 営みです.",
        "aftertaste": "回帰の螺旋. 同じ失敗を 繰り返していると 嘆かないで. あなたが「リカレンス（回帰）」するたびに 魂はその 経験の 核へと 確実に 近付いているのだから.",
        "example": "The recurrence of themes in the composer's late symphonies suggests a deep preoccupation with memory and time.",
        "deep_dive": { "roots": [{"term": "kers-", "meaning": "to run"}], "points": ["current（現在の：流れている）や course（進路）と同じ。流動する命의ルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "bilateral_symmetry",
        "word": "Bilateral",
        "meaning": "左右両側の、二国間の、双方向の",
        "era": "18th Century Latin bi- + latus",
        "etymology": {
            "components": ["bi- (two)", "latus (side)"],
            "original_statement": "From French bilatéral, from Latin bi- (two) + lateralis (pertaining to the side), from latus (side)."
        },
        "concept": "Two-sided (「中心（center）」を 挟んで 「対等（equal）」な 「双子（twins）」が 鏡像のように 向かい合うこと)",
        "thinking": "一方的な 支配を やめ 鏡のように 互いを 参照し合うことで 全体の 均衡（バランス）を 保ち、一つの 完結した 美しさを 創り出すこと. 語源は「二つの側面」. それは 自己と 他者が まったく 同じ権利と 重みを持って 存在しているという 宇宙の 根源的な「平等」の 幾何学的な 証明です.",
        "aftertaste": "対等な鏡像. 他者を 自分より 低く見るのも 高く見るのも やめよう. あなたが「バイラテラル（双方向的）」な 誠実さを 持つとき 世界との 関係は 完璧に 調和し 美しい 均衡を 保ち始めるのだから.",
        "example": "The butterfly is a perfect example of bilateral symmetry, with its wings mirror-imaging each other perfectly.",
        "deep_dive": { "roots": [{"term": "stela-", "meaning": "to spread, extend (possible for latus)"}], "points": ["latitude（緯度：広がり）や relate（関係づける：持ち帰る）と同じ。繋がりのルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "synchrony_pattern",
        "word": "Synchrony",
        "meaning": "同時性、共時性、タイミングの一致",
        "era": "19th Century Greek syn- + chronos",
        "etymology": {
            "components": ["syn- (together)", "chronos (time)"],
            "original_statement": "From Greek synchronos (happening at the same time), from syn- (together, with) + chronos (time)."
        },
        "concept": "Together in time (「個々の時計（individual clocks）」が 「宇宙の鼓動（universal beat）」に 合わせて 「一つ（one）」に 響き合うこと)",
        "thinking": "偶然の一致 を超え 背後にある 巨大な 意図や 流れが 複数の 現象を 一点に 収束させる、聖なる「タイミング」の 奇跡. 語源は「時を共にする」. それは 孤独な 努力が 世界の 必然と 出会う 祝福の 瞬間であり 私たちが 宇宙という 大きな 楽器の 一部であることを 実感する アクションです.",
        "aftertaste": "時を共にする奇跡. 焦って 自分の時計を 進めすぎないで. あなたが「シンクロニー（共時性）」の 流れに 身を任せたとき 全ての 出会いは 完璧な タイミングで あなたの元へと 届けられるのだから.",
        "example": "The rhythmic synchrony of the flock of birds flying across the sunset was a breathtaking sight.",
        "deep_dive": { "roots": [{"term": "sm-", "meaning": "together (for syn-)"}, {"term": "ghre-", "meaning": "to time (possible for chronos)"}], "points": ["sympathy（同情：苦しみを共にする）や chronicle（年代記）と同じ。時の共有。"] },
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
        print(f"Success: Added {added} words in Cycle 157.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
