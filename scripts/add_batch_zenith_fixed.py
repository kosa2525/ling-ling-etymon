import json
import re

word_batch = [
    # Cycle 167: Crown & Peak (Refined II)
    {
        "id": "zenith_peak_fixed",
        "word": "Zenith",
        "meaning": "天頂、絶頂、極致、頂点",
        "era": "14th Century Arabic samt",
        "etymology": {
            "components": ["samt (way, path, direction)", "samt ar-ras (way over the head)"],
            "original_statement": "From Old French zenith, from Medieval Latin cenit, from Arabic samt (way, path, direction), as in samt ar-ras (way over the head)."
        },
        "concept": "Way over head (「主観（subjective）」な 「限界（limit）」を 「垂直（vertical）」に 「超越（transcend）」し 「宇宙（cosmos）」の 「中心」と 繋がること)",
        "thinking": "横に 広がる 成功 ではなく、自らの 精神を 極限まで 研ぎ澄まし（フォーカス）、天（ハイ・プレイス）と 直結した 瞬間に 到達する、孤高で 聖なる 絶頂の状態. 語源は「頭上の道」. それは ゴール ではなく 存在の 密度が 最大化し 宇宙の 意志と 同化した 瞬間の 表現です. 極致は、祈りです.",
        "aftertaste": "頭上の輝き. 目先の 損得（よこみち）に 惑わさないで. あなたが 直向（ひたむ）きな 情熱で 自分の「ゼニス（天頂）」を 目指し続けるとき その 頂（いただき）から 見える 景色は あなたの 人生を 永遠の 祝福で 満たしてくれるのだから.",
        "example": "At the zenith of his power, the emperor controlled a territory that stretched across three continents.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["nadir（天底：足の下の道）と 対になる 概念。垂直方向への 精神の 拡張。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "acme_peak",
        "word": "Acme",
        "meaning": "絶頂、最高点、(病気の)極期",
        "era": "16th Century Greek akme",
        "etymology": {
            "components": ["akme (highest point, peak, edge)"],
            "original_statement": "From Greek akme (highest point, peak, edge), from ake (point)."
        },
        "concept": "Sharpest point (「努力（effort）」が 「針の先（needle point）」のように 「凝縮（condense）」され 「完璧（perfect）」な 「形」を 成した 瞬間)",
        "thinking": "膨大な 蓄積の 果てに 訪れる、これ以上 何も 足せず 何も 引けない（ミニマリズム）、極限の バランス点. 語源は「尖った先端、刃」. それは 安定 ではなく 鋭利な 知性と 緊張感の 果てに 産み出される 聖なる「完成（フィニッシュ）」の 表現です. 絶頂は、刃先です.",
        "aftertaste": "完璧の刃先. 妥協して 途中で 投げ出さないで. あなたが 最後の 磨き（ポリッシュ）を 怠らず 自分の「アクミ（最高点）」に 到達しようと するとき その 鋭い 輝きは どんな 困難な 障壁も 切り裂く 聖なる 力に なるのだから.",
        "example": "The artist felt that this symphony represented the acme of his creative achievements.",
        "deep_dive": { "roots": [{"term": "ak-", "meaning": "sharp, pointed"}], "points": ["acid（酸：鋭い味）や acrobat（アクロバット：高い所の先端を行く人）と同じ。鋭さのルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "apex_peak",
        "word": "Apex",
        "meaning": "頂上、尖端、最高点、(組織の)トップ",
        "era": "16th Century Latin apex",
        "etymology": {
            "components": ["apere (to fasten, tie, join)"],
            "original_statement": "From Latin apex (tip, summit, point, small rod at the top of a priest's cap), related to apere (to fasten, join)."
        },
        "concept": "Fastened tip (「多様な力（diverse forces）」が 「一点（one point）」で 「緊密（tight）」に 「結合（join）」し 「安定」を 司る（つかさどる）こと)",
        "thinking": "ただ 高いだけ ではなく、下支えする 全ての 要素を 代表し、それらを 束ねて（マスタリー） 方向性を 示す、責任ある 頂点. 語源は「結びつけること、神官の帽子の飾り」. それは 支配 ではなく 全体（ホール）の 調和を 守るための 聖なる「楔（くさび）」の 表現です. 頂上は、責任です.",
        "aftertaste": "統合の頂点. 自分の 位置に 誇りを 持とう. あなたが「エイペックス（頂点）」として 周囲の 想いを 束ね（たばね） 誠実に 導き出すとき その 安定感は 多くの 人々に 安心と 希望を 与える 聖なる 標（しるべ）に なるのだから.",
        "example": "As the apex predator in the ecosystem, the wolf plays a crucial role in maintaining the balance of nature.",
        "deep_dive": { "roots": [{"term": "ap-", "meaning": "to reach, fasten"}], "points": ["aptitude（才能：適して結びつく力）や adapt（適応する）と同じ。接続と 完成のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "summit_peak",
        "word": "Summit",
        "meaning": "頂上、最高点、首脳会談",
        "era": "15th Century Latin summus",
        "etymology": {
            "components": ["summus (highest)"],
            "original_statement": "From Old French somete, diminutive of som (top), from Latin summum (highest point, top), neuter of summus (highest)."
        },
        "concept": "Highest total (「これまでの全行程（whole journey）」を 「一つ（one）」に 「集計（sum up）」し 「達成（achievement）」として 「顕現」させること)",
        "thinking": "途中経過の 苦労や 喜びを 全て 包摂し（インクルード）、それらを 輝かしい 成果（リザルト）へと 昇華させる、集大成の 瞬間. 語源は「最高の、合計の」. それは 結果 以前の 歩んできた 道のりそのものが 正しかったことを 証明する 聖なる「目撃」の 表現です. 頂上は、対話です.",
        "aftertaste": "集大成の対話. 苦しい 登り坂（試練）を 厭（いと）わないで. あなたが「サミット（頂上）」に 立ち 自分の 過去と 誠実に 対話（首脳会談）するとき 全ての 苦労は 宝石のような 喜びへと 変わるのだから.",
        "example": "After weeks of preparation, the climbers finally reached the summit and enjoyed the breathtaking view.",
        "deep_dive": { "roots": [{"term": "up-", "meaning": "up, over (possible origin for sub- which summus is derived from)"}], "points": ["sum（合計）や consummate（完成させる：最高の状態にする）と同じ。集約と 昇華のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "culmination_peak",
        "word": "Culmination",
        "meaning": "最高潮、頂点、(天体の)南中、集大成",
        "era": "17th Century Latin culmen",
        "etymology": {
            "components": ["culmen (top, peak, summit)"],
            "original_statement": "From Late Latin culminationem, from culminare (to crown, to peak), from Latin culmen (top, peak, summit, stalk of grain)."
        },
        "concept": "Crowning point (「長い時間（long time）」を かけて 「醸成（brew）」された 「エナジー」が 「王冠（crown）」のような 「威厳」を 持って 「爆発」すること)",
        "thinking": "単なる 終わり ではなく、これまでの 軌跡が 全て 一点に 収束し（コンバージェンス）、歴史的な 意味を 持って 結実する、壮大な フィナーレ. 語源は「頂、南中、穀物の茎」. それは 偶然 ではなく 必然的な 成長の 極点（ピーク）であり 私たちが 宇宙の 運行と 一致した 聖なる「祝祭」の 表現です.",
        "aftertaste": "必然の結実. 今の 努力が 無駄に なると 疑わないで. あなたが 誠実に 想いを 積み重ね「カルミネーション（最高潮）」の 瞬間を 迎えたとき その 結実は 誰にも 否定できない 圧倒的な 尊厳を 宿すのだから.",
        "example": "The award ceremony was the culmination of years of hard work and dedication to the charity.",
        "deep_dive": { "roots": [{"term": "kel-", "meaning": "to rise, be high"}], "points": ["column（柱）や hill（丘）と同じ。上昇し 支える力のルーツ。"] },
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
        print(f"Success: Added {added} words in Cycle 167.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
