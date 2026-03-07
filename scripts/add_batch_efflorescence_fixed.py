import json
import re

word_batch = [
    # Cycle 169: Potential & Blossom (Refined II)
    {
        "id": "efflorescence_bloom_fixed",
        "word": "Efflorescence",
        "meaning": "開花、開花期、(才能などの)発現、(化学)風解",
        "era": "17th Century Latin ex- + florere",
        "etymology": {
            "components": ["ex- (out)", "florere (to bloom)"],
            "original_statement": "From French efflorescence, from Latin efflorescere (to blossom, bloom), from ex- (out) + florescere (to begin to bloom), from florere (to bloom)."
        },
        "concept": "Blooming out (「内部（inside）」に 秘められた 「可能性（potential）」が 「極限（limit）」まで 「成熟（mature）」し 「一気（all at once）」に 「外部」へと 「顕現」すること)",
        "thinking": "ただの 開花 ではなく、全存在を 賭けた（ステーク） 圧倒的な 自己表現であり、その 瞬間にしか 存在し得ない、極限の 美しさと 儚さの 幸福な 一致. 語源は「咲き出でること」. それは 誰かのため ではなく 自らの 生命の 必然として 世界を 彩ろうとする 聖なる「祝祭」の 表現です. 開花は、勝利です.",
        "aftertaste": "才能の祝祭. 自分の タイミングを 誰かと 比べないで. あなたが 誠実に 自己を 耕し（カルティベート）「エフロレッセンス（開花）」の 瞬間を 迎えたとき その 輝きは 宇宙の 全ての 祝福を 独占するほどに まばゆいものに なるのだから.",
        "example": "The 1920s saw a magnificent efflorescence of literature and art in the heart of Paris.",
        "deep_dive": { "roots": [{"term": "bhlo-", "meaning": "to bloom"}], "points": ["flower（花）や flourish（繁栄する）と同じ。生命力の 最高の 到達点。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "anthesis_bloom",
        "word": "Anthesis",
        "meaning": "(植物)開花、開花期、(病気の)全盛期",
        "era": "19th Century Greek anthos",
        "etymology": {
            "components": ["anthos (flower)"],
            "original_statement": "From Greek anthesis (a blossoming), from antheein (to blossom), from anthos (flower)."
        },
        "concept": "Flowering process (「蕾（bud）」という 「秘密（secret）」が 「開示（disclosure）」され 「宇宙の 旋律（cosmic melody）」と 「完全（perfect）」に 「再構築」されること)",
        "thinking": "開花という 結果 だけでなく、その 花びらが 一枚一枚 ほどけてゆく（アンフォールド）、繊細で 不可逆な 時間の 経過そのものに 宿る 神聖さ. 語源は「開花、花」. それは 沈黙 ではなく 生命が 自らの 秘密を 宇宙へと 歌い上げる（シンギング）ような、聖なる「告白」の 表現です. 開花は、開示です.",
        "aftertaste": "秘密の開示. 自分の 想いを 隠し通そうと しなくていい. あなたが「アンテシス（開花）」の 精神で 心を 開き 真実を 語り始めたとき 世界は その 香り（メッセージ）に 酔いしれ あなたを 深く 受容してくれるのだから.",
        "example": "Biologists carefully monitored the timing of anthesis in the local flora to study the effects of climate change.",
        "deep_dive": { "roots": [{"term": "andh-", "meaning": "to bloom"}], "points": ["anthology（選集：花を集めたもの）や chrysanthemum（キク：金の華）と同じ。美の集積。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "burgeon_bloom",
        "word": "Burgeon",
        "meaning": "急成長する、芽吹く、急速に発展する",
        "era": "14th Century Old French burjon",
        "etymology": {
            "components": ["burjon (a bud, shoot, pimple)"],
            "original_statement": "From Old French burjoner, from burjon (a bud, shoot, pimple), of uncertain origin, perhaps from Frankish."
        },
        "concept": "Vibrant budding (「停滞（stagnation）」を 「暴力的なまでの 活力（vitality）」で 「打破（breakthrough）」し 「加速度的（accelerated）」に 「拡張」すること)",
        "thinking": "緩やかな 成長 ではなく、抑えきれない 衝動が 次々と 新しい 形を 産み出し、一晩で 世界を 塗り替えてしまうような、圧倒的な 生命の 奔流（フラッド）. 語源は「芽、出芽」. それは 計画 以前の 宇宙の 意志そのものが あなたを 通じて 噴出している 聖なる「爆発」の 表現です. 成長は、奔流です.",
        "aftertaste": "活力の奔流. 変化の 速度に 怯（ひる）まないで. あなたの 魂が「バージョン（急成長する）」し 始めたとき その 勢いは 過去の 全ての 後悔を 押し流し 未知の 輝かしい 未来へと あなたを 一気に 運んでくれるのだから.",
        "example": "The small tech startup began to burgeon into a global empire within just a few years of its launch.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["溢れ出す エナジー。制御を 超えた 先に 産み出される、新しい 秩序の 予兆。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "prolific_potential",
        "word": "Prolific",
        "meaning": "多産の、多作の、豊かな、実り多い",
        "era": "17th Century Latin proles + facere",
        "etymology": {
            "components": ["proles (offspring)", "facere (to make)"],
            "original_statement": "From French prolifique, from Medieval Latin prolificus, from Latin proles (offspring) + facere (to make)."
        },
        "concept": "Offspring-making (「自我（ego）」を 「他者（others）」へと 「無限（infinite）」に 「分け与え（share）」 世界を 「自分の一部」として 「満たして」ゆくこと)",
        "thinking": "単なる 数の 多さ ではなく、自らの 存在が 源泉（ソース）となって、次から 次へと 新しい 命や 意味を 産み出し続ける、宇宙を 肯定する 圧倒的な 創造性. 語源は「子孫を 作ること」. それは 枯渇（こかつ）の 恐怖 ではなく 無限の 豊かさを 信じ抜く 聖なる「信頼」の 表現です. 豊かさは、信頼です.",
        "aftertaste": "無限の創造. 惜しみ（おしみ）なく 与え続けよう. あなたが「プロリフィック（多作な）」な 精神で 自分の ギフト（才能）を 世界に 放ち続けるとき 宇宙は 更なる 智慧と エナジーを あなたに 注ぎ込み続けるのだから.",
        "example": "Picasso was an incredibly prolific artist, creating thousands of works across many different mediums during his long career.",
        "deep_dive": { "roots": [{"term": "al-", "meaning": "to grow, nourish (possible link for proles)"}], "points": ["proletariat（プロレタリア：子供しか持たない者）と同じ。生命を 繋ぐという、究極の 財産。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "gestate_potential",
        "word": "Gestate",
        "meaning": "妊娠期間を過ごす、(考えなどを)練り上げる、(ゆっくりと)育つ",
        "era": "19th Century Latin gerere",
        "etymology": {
            "components": ["gerere (to bear, carry)"],
            "original_statement": "From Latin gestatus, past participle of gestare (to bear, carry, gestate), frequentative of gerere (to bear, carry)."
        },
        "concept": "Carrying inside (「外部の 喧騒（external noise）」から 「隔離（isolated）」された 「聖なる 深淵（sacred depth）」で 「真理」を 「静かに」 「醸成」すること)",
        "thinking": "すぐに 成果（アウトプット）を 求める 焦りを 捨て、自分自身の 内なる 暗闇（子宮）の中で、新しい 命や 智慧が 完璧な 形に なるまで 慈しみ（いつくしみ） 守り抜く、聖なる「猶予（ゆうよ）」の プロセス. 語源は「運ぶ、身ごもる」. それは 沈黙 ではなく 生命が 宇宙と 密かに 交信している 聖なる「対話」の 表現です.",
        "aftertaste": "静かなる醸成. 焦って 答えを 出そうと しなくていい. あなたの 中で 構想が「ジェステイト（練り上げられる）」な 深い 静寂の中に 在るとき 魂は 真の 完成（トータル）へと 確実に 近付いているのだから.",
        "example": "The novel gestated in her mind for over a decade before she finally put pen to paper.",
        "deep_dive": { "roots": [{"term": "ges-", "meaning": "to carry"}], "points": ["gesture（身振り：運ぶこと）や suggest（示唆する：下に運ぶ）と同じ。意味を 運ぶ 力。"] },
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
        print(f"Success: Added {added} words in Cycle 169.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
