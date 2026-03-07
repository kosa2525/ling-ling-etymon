import json
import re

word_batch = [
    # Cycle 162: Spark & Ignition (Refined)
    {
        "id": "kindle_ignition_fixed",
        "word": "Kindle",
        "meaning": "火をともす、燃え立つ、(感情を)燃え立たせる、(光が)輝く",
        "era": "12th Century Old Norse kynda",
        "etymology": {
            "components": ["kynda (to kindle, set fire to)"],
            "original_statement": "From Old Norse kyndill (torch), from Latin candela (candle), or of separate Germanic origin meaning 'to set fire to'."
        },
        "concept": "Striking the spark (「静止（stillness）」の中に 「摩擦（friction）」を 起こし 「光（light）」と 「熱（heat）」を 誕生させること)",
        "thinking": "大きな 炎になる 前の、最も 小さく、しかし 最も 可能性に 満ちた 動的な 瞬間. 語源は「火を点ける、松明」. それは 外部から 与えられる 刺激 ではなく 自らの 内側で 感情が 沸き立ち（ワクワク感） 存在の 核が 輝き始める 聖なる「始動」の 表現です. 閃きは、熱です.",
        "aftertaste": "内なる点火. 自分の 情熱を 絶やさないで. あなたが 心の中に 小さな「キンドル（点火）」を 起こし続ける限り 人生は いつでも 鮮やかな 輝きと 温もりを 取り戻すことが できるのだから.",
        "example": "His speech was so powerful that it began to kindle a sense of hope in the hearts of the audience.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["candle（キャンドル）や candid（率直な：白く輝く）と同じ。誠実さと 輝きのルーツ。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "ignite_ignition",
        "word": "Ignite",
        "meaning": "火をつける、発火させる、(感情などを)燃え立たせる",
        "era": "17th Century Latin ignis",
        "etymology": {
            "components": ["ignis (fire)"],
            "original_statement": "From Latin ignitus, past participle of ignire (to set on fire), from ignis (fire)."
        },
        "concept": "Encounter with fire (「触媒（catalyst）」の 介入により 「蓄えられたエネルギー」を 一気に 「光と熱」へと 変容させること)",
        "thinking": "単なる 燃焼 ではなく、一瞬の 接触（トリガー）によって 全く 異なる 状態（プラズマ）へと 遷移する、不可逆で 激しい 多幸感の 爆発. 語源は「火（イグニス）」. それは 宿命を 引き受け 自らの 生命を 限界まで 燃焼させようとする 聖なる「決断」の 表現です. 発火は、覚醒です.",
        "aftertaste": "宿命の発火. 自分の 殻に 閉じこもらないで. あなたが 運命の 触媒と 出会い「イグナイト（発火）」したとき あなたは 誰にも 止められない 圧倒的な 輝きとなって 世界を 照らし出すのだから.",
        "example": "The striker's brilliant goal served to ignite the spirit of the entire team and the fans in the stadium.",
        "deep_dive": { "roots": [{"term": "egni-", "meaning": "fire"}], "points": ["Agni（アグニ：インドの火神）と同じ。生命の 根源的な エネルギーのルーツ。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "conflagration_ignition",
        "word": "Conflagration",
        "meaning": "大火、大火災、(戦争などの)突発、激動",
        "era": "16th Century Latin con- + flagrare",
        "etymology": {
            "components": ["con- (with, together)", "flagrare (to burn)"],
            "original_statement": "From Latin conflagratus, from con- (intensive) + flagrare (to burn, blaze, glow)."
        },
        "concept": "Intensive blazing together (「個々の炎（individual flames）」が 「一つ（one）」に 結集し 「世界（world）」を 「刷新（renew）」する 圧倒的な 激動)",
        "thinking": "制御不能に 広がる 破壊 ではなく、古い 秩序や 淀み（よどみ）を 焼き払い、大地を 浄化して 新しい 生命が 芽吹くための スペースを 創り出す、聖なる「激変」. 語源は「共に燃える」. それは 痛みを 伴う 変化 ではなく 私たちが 共有する 情熱が 巨大な 潮流となって 時代を 突き動かす 聖なる「祝祭」の 表現です.",
        "aftertaste": "刷新の劫火. 変化を 恐れて 縮こまらないで. 大いなる「コンフラグレーション（大火）」が あなたの 古い殻を 焼き尽くしたとき そこには 想像もしなかった 鮮やかな 可能性が 芽生えているのだから.",
        "example": "The small dispute between the two nations eventually escalated into a global conflagration.",
        "deep_dive": { "roots": [{"term": "bhel-", "meaning": "to shine, flash, burn"}], "points": ["flame（炎）や fulgent（輝かしい）と同じ。熱き輝きのルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "rekindle_ignition",
        "word": "Rekindle",
        "meaning": "再び火をつける、(感情などを)再燃させる",
        "era": "16th Century Latin re- + kindle",
        "etymology": {
            "components": ["re- (again)", "kindle (to set fire to)"],
            "original_statement": "From re- (again) + kindle (to set on fire)."
        },
        "concept": "Striking again (「灰（ashes）」の中に 残された 「幽かな熱（faint heat）」を 「息吹（breath）」で 呼び戻し 「再び（again）」 輝かせること)",
        "thinking": "一度 消えたように 見える 情熱 も、その 核（コア）にある 真実を 忘れなければ いつでも（何度でも） 新しい 光として 再起 できるという、宇宙の 慈悲深い 周期性の 表現. 語源は「再び点火する」. それは 過去の 執着 ではなく 変わらぬ 愛を 新しい 時代に 合わせて 翻訳し直す 聖なる「再生」のアクションです.",
        "aftertaste": "再生の息吹. 終わったことに 絶望しないで. あなたが「リキンドル（再燃さす）」な 勇気を持って 自分の核に 息を 吹きかけるとき 情熱は かつてない 輝きを持って 再び あなたを 突き動かすのだから.",
        "example": "The trip back to their hometown helped to rekindle their friendship and resolve old misunderstandings.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["灰の中から 蘇る フェニックス（不死鳥）のような、不滅の 魂の ドラマ。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "incendiary_ignition",
        "word": "Incendiary",
        "meaning": "放火の、焼夷(しょうい)性の、煽動(せんどう)的な、扇情的な",
        "era": "17th Century Latin incendium",
        "etymology": {
            "components": ["incendere (to set on fire)"],
            "original_statement": "From Latin incendiarius (causing a fire), from incendium (a fire, conflagration), from incendere (to set on fire, kindle, burn)."
        },
        "concept": "Setting in fire (「言葉（word）」や 「行動（action）」が 「他者の魂（other's soul）」に 「火（fire）」を 放ち 静止を 打ち破ること)",
        "thinking": "物理的な 破壊 ではなく 停滞した 社会や 思考の 殻に 風穴をあけ 人々を 真の意味で 揺さぶり、突き動かすような、危険で 魅力的な 指導力. 語源は「火を点けること」. それは 混乱を 招く 悪意 ではなく 真実を 突きけることで 眠っていた 魂を 強制的に 呼び起こそうとする 聖なる「過激さ」の 表現です.",
        "aftertaste": "魂の点火者. 摩擦を 恐れて 口を 閉じないで. あなたの「インセンディアリー（煽動的な）」な 真実の 言葉が 誰かの 心に 飛び火したとき 世界は 初めて 動きだし 新しい 時代へと 舵（かじ）を 切るのだから.",
        "example": "The politician's incendiary rhetoric led to widespread protests across the major cities.",
        "deep_dive": { "roots": [{"term": "kand-", "meaning": "to shine, glow"}], "points": ["incense（香：燃えるもの）や candle（キャンドル）と同じ。祈りと 輝きのルーツ。"] },
        "part_of_speech": "adjective"
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
        print(f"Success: Added {added} words in Cycle 162.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
