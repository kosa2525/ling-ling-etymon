import json
import re

word_batch = [
    # Cycle 139: Wind & Motion
    {
        "id": "zephyr_wind",
        "word": "Zephyr",
        "meaning": "そよ風、西風、心地よい風",
        "era": "Pre-12th Century Greek Zephyros",
        "etymology": {
            "components": ["Zephyros (west wind)"],
            "original_statement": "From Latin zephyrus, from Greek zephyros (the west wind), also personified as a god."
        },
        "concept": "Gentle west wind (春の 「訪れ（arrival）」を 告げる 慈愛に満ちた 「柔らかな（soft）」 吐息)",
        "thinking": "激しい嵐ではなく、頬をなでるような微細な空気の揺らぎが、閉ざされた心（冬）を優しく開き、新しい命の予感（春）を運んでくること. 語源は「西風の神」. それは 物理的な力による強制ではなく、その「心地よさ」によって世界を動かしていく、洗練された影響力の象徴です.",
        "aftertaste": "吐息の癒やし. 強くあろうとしなくていい. あなたが「ゼファー（そよ風）」のように 軽やかで 優しくあることで 誰かの凍てついた心を 溶かしてあげることができるのだから.",
        "example": "A soft zephyr blew in from the sea, bringing the scent of salt and summer blossoms.",
        "deep_dive": { "roots": [{"term": "gwebh-", "meaning": "to dip (possible root)"}], "points": ["和らげる、浸透するというニュアンス。境界を越える柔らかな力。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "agitation_motion",
        "word": "Agitation",
        "meaning": "動揺、興奮、攪拌(かくはん)、世論の喚起",
        "era": "16th Century Latin agere",
        "etymology": {
            "components": ["agere (to set in motion, drive, do)"],
            "original_statement": "From Latin agitationem (a moving, agitation), from agitare (to set in motion, drive), frequentative of agere (to set in motion, drive, do)."
        },
        "concept": "Frequent driving (淀んだ 「沈黙（silence）」を 「何度も揺さぶり（drive repeatedly）」 生気を取り戻させる 激しい 運動)",
        "thinking": "現状に甘んじることを拒み 内部から 激しく 掻き乱す（かきみだす）ことで 新しい秩序や 変化への欲求を 爆発させる 躍動的なプロセス. 語源は「激しく動かす」. それは 不安という名の 揺らぎであると同時に 魂が 目覚めるために 避けて通れない 聖なる「葛藤」の形でもあります.",
        "aftertaste": "目覚めの揺らぎ。心が「アジテーション（動揺）」しているときは 変化（チャンス）が 訪れている証拠だ。その波を 恐れずに受け入れることで あなたは 新しい自分へと 脱皮してゆくのだから。",
        "example": "The political agitation in the capital eventually led to significant reforms in the government.",
        "deep_dive": { "roots": [{"term": "ag-", "meaning": "to drive, draw out, move"}], "points": ["active（活動的な）や agent（代理人：動く者）と同じ。生命の能動性。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "gust_wind",
        "word": "Gust",
        "meaning": "突風、一吹きの風、(感情などの)突発",
        "era": "16th Century Old Norse gustr",
        "etymology": {
            "components": ["gustr (a puff of wind)"],
            "original_statement": "From Old Norse gustr (a puff, cold blast), related to geysa (to gush, rush)."
        },
        "concept": "A sudden gush (「溜まった（accumulated）」 熱量を 「一気に吹き放つ（rush out）」 瞬間的な 噴出)",
        "thinking": "予測不能なタイミングで 空間を切り裂くように 訪れる 力強い「生のエネルギー」の 塊（かたまり）. 語源は「噴出」. それは 迷いを一瞬で 吹き飛ばし 停滞した空気を 刷新する 荒々しい 浄化の力です. 風が吹き抜けた後 世界の彩（いろ）は 変わっています.",
        "aftertaste": "一瞬の決断. 長い沈黙もいいけれど 時には「ガスト（突風）」のように 自分の情熱を 一気に噴出させてごらん. その一吹きの風が 運命の帆を 大きく動かす 始まりになるのだから.",
        "example": "A sudden gust of wind nearly knocked him off his bicycle as he turned the corner.",
        "deep_dive": { "roots": [{"term": "gheu-", "meaning": "to pour"}], "points": ["geyser（間欠泉）や gush（噴出する）と同じ。生命の「溢れ出し」のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "fluctuate_motion",
        "word": "Fluctuate",
        "meaning": "(価格・感情などが)変動する、上下する、揺れ動く",
        "era": "17th Century Latin fluere",
        "etymology": {
            "components": ["fluere (to flow)"],
            "original_statement": "From Latin fluctuatus, past participle of fluctuare (to undulate, hesitate, waver), from fluctus (a wave, a tide), from fluere (to flow)."
        },
        "concept": "Action of wave (「波（wave）」のように 「一定の形（form）」に 定まらず 常に 移ろい続ける 宿命)",
        "thinking": "安定という名の 死を拒み 生きている証拠としての 「不規則な揺らぎ」を 全身で表現すること. 語源は「流れる、波立つ」. それは 弱さではなく 万物と呼応し、変化し続けるという 宇宙の ダイナミックな 誠実さの 形です. 揺れ動くことは、適応することです.",
        "aftertaste": "揺らぎのダイナミズム。一喜一憂しなくていい。あなたの心が「フラクチュエイト（変動）」しているのは あなたが世界を 敏感に感じ取り 豊かに生きている証拠なのだから。",
        "example": "Oil prices tend to fluctuate wildly depending on global political and economic stability.",
        "deep_dive": { "roots": [{"term": "bhleu-", "meaning": "to swell, well up, flow"}], "points": ["fluid（流体）や fluent（流暢な）と同じ。生命の「流れ」そのもの。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "propel_motion",
        "word": "Propel",
        "meaning": "(船などを)進ませる、推進する、(人を)駆り立てる",
        "era": "15th Century Latin pro- + pellere",
        "etymology": {
            "components": ["pro- (forward)", "pellere (to drive, push)"],
            "original_statement": "From Latin propellere (to drive forward or away), from pro- (forward) + pellere (to drive, push)."
        },
        "concept": "Driving forward (「背後（back）」からの 強い 「意志（push）」によって 未知の 「前方（forward）」へと 突き進むこと)",
        "thinking": "重力や 摩擦に 打ち勝ち 自分の存在（ベクトル）を 目的の場所へと 向かって 力強く 射出する アクション. 語源は「前へ押す」. それは 誰かに言われるからではなく 自らの情熱という名の エンジンによって 人生を 加速させていく 輝かしく 孤独な 決意の現れです.",
        "aftertaste": "推進の意志. 立ち止まっている時間を 終わりにしよう. あなたの奥底にある その「プロペル（推進）」の 力（エンジン）を信じて 未来という名の 大海原へ 漕ぎ出してゆくのだから.",
        "example": "His insatiable curiosity helped to propel him to the forefront of scientific research.",
        "deep_dive": { "roots": [{"term": "pel-", "meaning": "to thrust, strike, drive"}], "points": ["pulse（脈拍）や appeal（訴える：心を動かす）と同じ。衝撃と運動。"] },
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
        print(f"Success: Added {added} words in Cycle 139.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
