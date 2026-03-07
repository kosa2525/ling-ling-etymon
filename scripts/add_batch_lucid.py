import json
import re

word_batch = [
    # Cycle 132: Crystal & Transparency
    {
        "id": "lucid_transparency",
        "word": "Lucid",
        "meaning": "明快な、分かりやすい、頭がはっきりした、透明な",
        "era": "16th Century Latin lux",
        "etymology": {
            "components": ["lux (light)"],
            "original_statement": "From Latin lucidus (light, bright, clear), from lucere (to shine), from lux (light)."
        },
        "concept": "Full of light (「光（light）」が 全てを 貫き 闇や 混乱を 完全に 「追い払った（clear）」 状態)",
        "thinking": "複雑な事象や 混乱した思考が 光に射抜かれ 一つの 無駄のない 理論（カタチ）として 立ち現れること. 語源は「光り輝く」. それは 誰にでも理解できる 圧倒的な「明快さ」であり 迷いの霧を 瞬時に晴らす 知性の輝きです. 明晰であることは 慈悲でもあります.",
        "aftertaste": "知性の夜明け. 難しく考えすぎて 迷宮にはまり込まないで. あなたの思考から 不純物を削ぎ落とし ただ「光（ルシッド）」を 通すことで 答えは自ずと 目の前に現れるのだから.",
        "example": "Despite his advanced age, he remained lucid and could recall every detail of his childhood.",
        "deep_dive": { "roots": [{"term": "leuk-", "meaning": "light, brightness"}], "points": ["light（光）や luxury（贅沢：眩いもの）と同じ。真理を照らす力のルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "transparent_transparency",
        "word": "Transparent",
        "meaning": "透明な、透き通った、見え透いた、明白な",
        "era": "15th Century Latin trans- + parere",
        "etymology": {
            "components": ["trans- (through)", "parere (to appear, come in sight)"],
            "original_statement": "From Latin transparentem, from transparere (to show through), from trans- (through) + parere (to come in sight, appear)."
        },
        "concept": "Appearing through (「向こう側（through）」が そのまま 「見える（appear）」 邪気のない 潔さ)",
        "thinking": "自分自身の存在（エゴ）を 主張するのではなく 訪れる光や 風景を そのまま「通す」 媒介としての美学. 語源は「透けて見える」. それは 隠し事がないという誠実さであり 同時に 世界と自分を 隔てる壁を なくしていくという 究極の「解放」の状態です.",
        "aftertaste": "媒介の静寂. あなたが何者かである必要はない. ただ「透明（トランスパレント）」であることで 世界の美しさを そのまま誰かに伝える 最高の鏡に なることができるのだから.",
        "example": "The company promised a more transparent decision-making process to regain public trust.",
        "deep_dive": { "roots": [{"term": "trans-", "meaning": "across"}, {"term": "pre-", "meaning": "to appear (possible root)"}], "points": ["appear（現れる）や parent（親：現れたもの）と同じ。真実の顕現。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "crystallize_transparency",
        "word": "Crystallize",
        "meaning": "結晶させる、具体化する、(考えなどが)固まる",
        "era": "16th Century Greek krystallos",
        "etymology": {
            "components": ["krystallos (ice)"],
            "original_statement": "From French cristalliser, from cristal (crystal), from Latin crystallum, from Greek krystallos (ice, rock-crystal)."
        },
        "concept": "To become ice (液状の 「曖昧さ（liquid）」を 規則正しい 「幾何学的な形（form）」へと 固定すること)",
        "thinking": "揺れ動く感情や 抽象的なアイデアが 長い時間をかけて 純化され 揺るぎない一つの「真理」として 凝縮すること. 語源は「氷になる」. それは 痛みを伴う 冷却（試練）を経て 初めて辿り着ける 完璧な秩序と 強さを持った 美しさです.",
        "aftertaste": "本質の凝縮. 迷いの時間を 恐れないで. その混沌（カオス）の中を 彷徨（さまよ）い続けた先にこそ あなただけの 輝く「結晶（クリスタライズ）」が 待っているのだから.",
        "example": "Her vague ideas for the novel finally began to crystallize after her long trip to Europe.",
        "deep_dive": { "roots": [{"term": "kruos-", "meaning": "icy cold, frost"}], "points": ["crystal（水晶）と同じ。凍結することで得られる、永遠の秩序。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "limpid_transparency",
        "word": "Limpid",
        "meaning": "澄んだ、透明な、(文体などが)明快な",
        "era": "17th Century Latin limpidus",
        "etymology": {
            "components": ["limpidus (clear, bright)"],
            "original_statement": "From Latin limpidus (clear, bright, transparent), related to lympha (clear water, water goddess)."
        },
        "concept": "Like clear water (「清らかな水（clear water）」のように 淀みがなく 「静謐な（quiet）」 透明感)",
        "thinking": "生まれたての泉や 邪気のない子供の瞳のように 濁りを一切知らない 根源的な平穏. 語源は「澄んだ水」. 知性による明快さというよりは 魂そのものが持っている 「純真さ」が生み出す 透明度です. この「リンピッド（澄明）」な視点から見れば 世界は喜びに満ちています.",
        "aftertaste": "原生の泉. 知識を積み上げるよりも その汚れを「洗い流す」ことを 大切にしよう. あなたの心が 澄み切った水（リンピッド）であるとき 世界の全ての輝きは あなたの中に映り込むのだから.",
        "example": "The limpid waters of the mountain lake reflected the snow-capped peaks perfectly.",
        "deep_dive": { "roots": [{"term": "limpa-", "meaning": "clear water"}], "points": ["lymph（リンパ）の語源。生命を浄化し、潤す聖なる水のルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "elucidate_transparency",
        "word": "Elucidate",
        "meaning": "解明する、明快に説明する、はっきりさせる",
        "era": "16th Century Latin ex- + lux",
        "etymology": {
            "components": ["ex- (out)", "lux (light)"],
            "original_statement": "From Late Latin elucidatus, past participle of elucidare (to make light or clear), from ex- (out) + lucidus (light, bright, clear), from lux (light)."
        },
        "concept": "To bring out light (暗闇の中に 「光（light）」を 運び込み 隠されていた 真実を 「引き出す（bring out）」こと)",
        "thinking": "難解な謎や 誤解の闇を 誠実な探究（光）によって 照らし出し 誰もが納得できる 「地平」へと 導き出すこと. 語源は「光を外へ出す」. それは 自分の知識を ひけらかすことではなく 他者の歩む足元に 灯を灯すような 献身的な知性のアクションです.",
        "aftertaste": "導きの光。あなたの言葉で 誰かの不安（闇）を 照らしてあげよう。その「解明（エルシデイト）」の先に 共に歩むべき 新しい道が はっきりと浮かび上がってゆくのだから。",
        "example": "The scientist's job is to elucidate the complex mechanisms behind natural phenomena.",
        "deep_dive": { "roots": [{"term": "leuk-", "meaning": "light, brightness"}], "points": ["illuminate（照らす）の兄弟語。外（ex）に向かって光を放つ、強い意志。"] },
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
        print(f"Success: Added {added} words in Cycle 132.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
