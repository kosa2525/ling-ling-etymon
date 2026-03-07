import json
import re

word_batch = [
    # Cycle 154: Bloom & Garden (Refined)
    {
        "id": "efflorescence_bloom",
        "word": "Efflorescence",
        "meaning": "開花、真っ盛り、(化学)風解",
        "era": "17th Century Latin ex- + florescere",
        "etymology": {
            "components": ["ex- (out)", "florescere (to begin to flower)"],
            "original_statement": "From Latin efflorescere (to bloom out), from ex- (out) + florescere (to begin to flower), from flor- (flower)."
        },
        "concept": "Blooming out (「内部（inside）」に 秘められた 「美（beauty）」が 限界を 越えて 「外部（outside）」へと 溢れ出すこと)",
        "thinking": "単なる 成長ではなく、溜め込んできた エネルギーが 一気に 結晶化し、色鮮やかな 生命の 輝きとして 世界に 顕現すること. 語源は「外へ咲きこぼれる」. それは 誰かに 見せるためではなく 自らの 生命の 必然として 最高潮（ピーク）に 辿り着く 聖なる「完成」の 瞬間です.",
        "aftertaste": "溢れ出す命. あなたが 誠実に 育んできた 想いは 今、まさに「エフロレッセンス（開花）」の 時を 迎えようとしている. その美しさを 世界に向けて 誇り高く 解き放ってごらん.",
        "example": "The artistic career of the young painter reached its full efflorescence during his years in Paris.",
        "deep_dive": { "roots": [{"term": "bhlo-", "meaning": "to flower"}], "points": ["flourish（繁栄する）や floral（花の）と同じ。生命の「上昇気流」のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "germinate_bloom",
        "word": "Germinate",
        "meaning": "発芽する、(考えなどが)芽生える、成長を始める",
        "era": "16th Century Latin germen",
        "etymology": {
            "components": ["germen (seed, sprout)"],
            "original_statement": "From Latin germinatus, past participle of germinare (to sprout, bud, germinate), from germen (sprout, bud, germ, seed)."
        },
        "concept": "Becoming a sprout (「硬い殻（hard shell）」に 守られていた 「可能性（potential）」が 「土（earth）」を 突き破り 動き出すこと)",
        "thinking": "目に見える 劇的な 変化が 起こる前の 静かで、しかし 不可逆な 生命の 始動. 語源は「芽、種子」. それは 巨大な 森林も 最初は 一つの 幽かな「ジャーミネイト（発芽）」から 始まったという、宇宙の 偉大な 連鎖の 起点です. 芽生えは、奇跡です.",
        "aftertaste": "芽生えの勇気. 今、あなたの心に 幽かに浮かんだ そのアイディアを 無視しないで. それが「ジャーミネイト（芽生え）」したとき あなたの人生は 全く新しい 物語へと 枝分かれ してゆくのだから.",
        "example": "The seeds of the revolution began to germinate in the hearts of the oppressed people decades ago.",
        "deep_dive": { "roots": [{"term": "gene-", "meaning": "to give birth, beget"}], "points": ["generation（世代）や genius（天才：宿る霊）と同じ。内なる力の「顕現」。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "burgeon_bloom",
        "word": "Burgeon",
        "meaning": "急成長する、芽吹く、急速に発展する",
        "era": "14th Century Old French burjon",
        "etymology": {
            "components": ["burjon (bud, sprout, pimple)"],
            "original_statement": "From Old French bourgeonner (to bud, sprout), from bourgeon (a bud)."
        },
        "concept": "Rapid budding (「環境（environment）」の 恩恵を 存分に 受け 「爆発的（explosive）」な 勢いで 「存在感」を 増してゆくこと)",
        "thinking": "慎重な 歩みを やめ 溢れ出す 活力を 制御することなく 空間へと 押し広げていく 圧倒的な 躍動感. 語源は「蕾（つぼみ）」. それは 制約を 打ち破り 世界の 隅々まで 自らの 輝きを 届けようとする、聖なる「繁栄」の アクションです. 成長は、輝きです.",
        "aftertaste": "急成長の予感. あなたの 努力が 正しい「土壌（場所）」に 出会ったとき 魂は「ヴァージャン（急成長）」し 誰も 止めることのできない 圧倒的な 輝きを 放ち始めるのだから.",
        "example": "The tech industry began to burgeon in the small city, attracting talent from all over the world.",
        "deep_dive": { "roots": [{"term": "bher-", "meaning": "to swell (possible root)"}], "points": ["berry（ベリー）や burst（破裂する）と同じ。内側からの「膨張」のドラマ。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "horticulture_bloom",
        "word": "Horticulture",
        "meaning": "園芸、園芸学",
        "era": "17th Century Latin hortus + cultura",
        "etymology": {
            "components": ["hortus (garden)", "cultura (tilling, cultivation)"],
            "original_statement": "From Latin hortus (garden) + cultura (cultivation, tilling), from colere (to till)."
        },
        "concept": "Cultivating the garden (「野生（wild）」を 「愛（love）」によって 「秩序（order）」へと 導き 聖なる 楽園を 築くこと)",
        "thinking": "自然を 征服するのではなく 命の 声を 聞き 共に 歩むことで この 地上に 最高の 美（庭園）を 現出させる、誠実な 献身の 知恵. 語源は「庭の耕作」. それは 私たちが 自らの 心という名の 「庭」を いかに 慈しみ、豊かに 育てていくかという、聖なる「魂の 園芸」の 隠喩です.",
        "aftertaste": "心の庭師. あなたの 内側にある 感受性を 野放しにしないで. 「ホーティカルチャー（園芸）」を 学ぶように 自分の心を 丁寧に 耕し続けることで あなたの 人生は いつも 花の香りで 満たされるのだから.",
        "example": "She decided to study horticulture to better understand the complex needs of her organic vegetable garden.",
        "deep_dive": { "roots": [{"term": "gher-", "meaning": "to grasp, enclose (for hortus)"}, {"term": "kwel-", "meaning": "to revolve, dwell (for culture)"}], "points": ["court（中庭）や wheel（車輪：耕作の巡り）と同じ。守られた空間のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "anthology_bloom",
        "word": "Anthology",
        "meaning": "名詩選、選集、(一般に)アンソロジー",
        "era": "17th Century Greek anthos + logia",
        "etymology": {
            "components": ["anthos (flower)", "logia (collecting)"],
            "original_statement": "From Greek anthologia (a flower-gathering), from anthos (flower) + logia (collection), from legein (to gather)."
        },
        "concept": "Gathering flowers (「魂の結晶（flower）」としての 言獲を 「厳選（select）」し 一つの 聖なる 「花束（bouquet）」へと 編むこと)",
        "thinking": "単なる 記録の 集積 ではなく 最も 美しく 輝いている 瞬間（言葉）だけを 掬い上げ、それらを 響き合わせることで、新しい 物語を 創り出す、極めて 知的な「蒐集（しゅうしゅう）」の 営み. 語源は「花の蒐集」. それは 人生の 最高の瞬間を 永遠に 留め置くための 聖なる「記憶の花束」です.",
        "aftertaste": "言葉の花束. あなたの 人生の 途上で見つけた 小さな感動を 忘れないで. それらを「アンソロジー（選集）」のように 心の中に 集めておくことで あなたの 魂は どんな時も 美しく 飾り立てられているのだから.",
        "example": "This anthology of 20th-century poetry includes some of the most influential works of the modern era.",
        "deep_dive": { "roots": [{"term": "andh-", "meaning": "to bloom"}, {"term": "leg-", "meaning": "to gather, collect"}], "points": ["legend（伝説：集められた話）や lecture（講義）と同じ。価値を「拾い上げる」力。"] },
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
        print(f"Success: Added {added} words in Cycle 154.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
