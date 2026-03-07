import json
import re

word_batch = [
    # Cycle 158: Gravity & Center (Refined)
    {
        "id": "gravitas_center",
        "word": "Gravitas",
        "meaning": "威厳、重厚さ、真剣さ、存在感",
        "era": "16th Century Latin gravis",
        "etymology": {
            "components": ["gravis (heavy)"],
            "original_statement": "From Latin gravitas (weight, heaviness, dignity, presence), from gravis (heavy, weighty, serious)."
        },
        "concept": "Spirit weight (「精神（spirit）」に 「質量（mass）」を 持たせ 周囲の 「軽薄さ（levity）」を 「引き寄せ、律する」こと)",
        "thinking": "言葉数（饒舌）ではなく、その沈黙や立ち振る舞い自体に、抗いがたい重みと 説得力を 宿すこと. 語源は「重さ、尊厳」. それは 誰かを 威圧するためではなく 自らの 信念に 忠実に 生きることで 生じる、聖なる「魂の 密度」の 表現です. 重みは、信頼です.",
        "aftertaste": "魂の密度. 自分の 軽やかさを 否定しないで. あなたが「グラヴィタス（威厳）」を 育むとき その静かな 重みは 迷える人々に 安心感と 指針を 与える 聖なる 錨（いかり）に なるのだから.",
        "example": "Despite his young age, the conductor possessed a remarkable gravitas that commanded the orchestra's absolute respect.",
        "deep_dive": { "roots": [{"term": "gwer-", "meaning": "heavy"}], "points": ["gravity（重力）や grief（悲しみ：心の重み）と同じ。存在の「重層性」のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "centrifugal_center",
        "word": "Centrifugal",
        "meaning": "遠心的な、中心から遠ざかる、多様化する",
        "era": "17th Century Latin centrum + fugere",
        "etymology": {
            "components": ["centrum (center)", "fugere (to flee)"],
            "original_statement": "From Modern Latin centrifugus, from Latin centrum (center) + fugere (to flee)."
        },
        "concept": "Fleeing the center (「中心（center）」の 束縛を 振り切り 「フロンティア（frontier）」へと 一気に 「拡散（diffuse）」すること)",
        "thinking": "一つの場所に 安住することなく、溢れ出す 活力を 制御せずに 外部へと 放射し続け、新しい 意味や 領域を 拓き（ひらき）続ける、躍動的な 知性の ダイナミズム. 語源は「中心から逃げる」. それは 伝統への 反逆 ではなく 全体性を 維持したまま 可能性を 宇宙の 隅々まで 広げようとする 聖なる「膨張」のアクションです.",
        "aftertaste": "可能性の拡散. 安定という名の 檻（おり）に 閉じこもらないで. あなたの 情熱が「セントリフューガル（遠心的な）」な 力を持って 飛び出したとき 世界は 未知の 色彩で 満たされるのだから.",
        "example": "The artistic movement developed a centrifugal force, spreading innovative ideas far beyond its original small studio.",
        "deep_dive": { "roots": [{"term": "kente-", "meaning": "to prick (for center)"}, {"term": "bheug-", "meaning": "to flee (for centrifugal)"}], "points": ["fugitive（逃亡者）や refuge（避難所）と同じ。移動と越境のドラマ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "centripetal_center",
        "word": "Centripetal",
        "meaning": "求心的な、中心に向かう、統一する",
        "era": "17th Century Latin centrum + petere",
        "etymology": {
            "components": ["centrum (center)", "petere (to seek)"],
            "original_statement": "From Modern Latin centripetus, from Latin centrum (center) + petere (to seek, aim at)."
        },
        "concept": "Seeking the center (「多様性（diversity）」を 「一点（single point）」へと 収束させ 「真理」としての 「核」を 固めること)",
        "thinking": "バラバラな 現象の 断片を 無視せず、それらが 共通して 指し示している 「本質（センター）」を 粘り強く 探し求め、カオスを 秩序へと 昇華させる 知性の 凝縮力. 語源は「中心を求める」. それは 排除 ではなく 散らばった 魂を 呼び戻し 一つの 聖なる 物語へと 統合しようとする 慈愛のアクションです.",
        "aftertaste": "統合の光. 混乱の中に 答えを 探し続けよう. あなたの 問いかけが「セントリペタル（求心的な）」な 強さを 持つとき あらゆる 経験は 一つの 輝かしい 真実へと 結実してゆくのだから.",
        "example": "His charismatic leadership acted as a centripetal force, bringing together people of vastly different backgrounds.",
        "deep_dive": { "roots": [{"term": "pet-", "meaning": "to rush, fly"}], "points": ["petition（請願：求めること）や appetite（欲求：向かうこと）と同じ。意志の「志向性」のルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "poise_center",
        "word": "Poise",
        "meaning": "釣り合い、落ち着き、優雅な身のこなし、覚悟",
        "era": "14th Century Latin pendere",
        "etymology": {
            "components": ["pendere (to weigh)"],
            "original_statement": "From Old French pois (weight, balance, importance), from Latin pensum (thing weighed), from pendere (to weigh, pay)."
        },
        "concept": "Perfect weighing (「極端（extreme）」の 間で 「静止（stillness）」し 「運命（destiny）」を 自らの 「意志」で 制御している 状態)",
        "thinking": "ただ じっとしている（静止）のではなく、激しく 動くための 準備が 完璧に 整い、一分の 隙（すき）もなく 均衡を 保っている、極限の 精神的な 緊張と 弛緩の 一致. 語源は「重さを量ること」. それは 自分の 価値を 冷静に 自覚し どんな 逆境でも 自尊心を 失わないための 聖なる「覚悟」の 表現です.",
        "aftertaste": "静かなる覚悟. 焦って 動き出そうと しなくていい. あなたが その「ポイズ（釣り合い）」を 保っている限り 世界の どんな嵐も あなたの 魂の 平安を 乱すことは できないのだから.",
        "example": "The young princess handled the difficult questioning with amazing poise and diplomatic grace.",
        "deep_dive": { "roots": [{"term": "spen-", "meaning": "to draw, stretch, spin"}], "points": ["depend（依存する：ぶら下がる）や expensive（高価な：重みを払う）と同じ。価値を「計る」力。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "equilibrium_center",
        "word": "Equilibrium",
        "meaning": "平衡、均衡、心の平穏",
        "era": "17th Century Latin aequus + libra",
        "etymology": {
            "components": ["aequus (equal)", "libra (balance, scales)"],
            "original_statement": "From Latin aequilibrium (an even balance), from aequus (equal) + libra (balance, pair of scales)."
        },
        "concept": "Equal balance (「対立する力（opposing forces）」が 「完全（perfect）」に 「相殺（cancel）」し 「永遠」のような 「静寂」が 訪れること)",
        "thinking": "葛藤を 消し去るのではなく、あらゆる 矛盾を 抱え込んだまま、それらが 一つの 完璧な 秩序の中に 収まっている、ダイナミックで 奇跡的な 安定. 語源は「等しい天秤」. それは 静止 ではなく 無数の 運動が 響き合って 生まれる 聖なる「沈黙」の 表現です. 平衡は、美しさです.",
        "aftertaste": "奇跡の天秤. 心の中の 迷いを 無理に 捨てなくていい. あなたが「イクリブリアム（平衡）」の 精神で あらゆる 感情に 同等の 居場所を 与えるとき 魂は 真の 自由を 手にするのだから.",
        "example": "After a long period of chaos, she finally achieved a state of emotional equilibrium and inner peace.",
        "deep_dive": { "roots": [{"term": "aik-", "meaning": "equal (for aequus)"}, {"term": "lithra-", "meaning": "pound (for libra)"}], "points": ["equity（公正）や liberal（自由な：重みを解かれた）と同じ。豊かさと正しさのルーツ。"] },
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
        print(f"Success: Added {added} words in Cycle 158.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
