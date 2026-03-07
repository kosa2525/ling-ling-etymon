import json
import re

word_batch = [
    # Cycle 149: Spark & Ignition (Refined)
    {
        "id": "kindle_ignition",
        "word": "Kindle",
        "meaning": "(火を)つける、燃え上がらせる、(感情・興味を)あおる",
        "era": "12th Century Old Norse kyndill",
        "etymology": {
            "components": ["kyndill (candle, torch)"],
            "original_statement": "From Old Norse kyndill (candle, torch), related to Latin candela (candle)."
        },
        "concept": "Starting the fire (「冷たい静止（cold stillness）」に 「最初の一撃（first strike）」を 与え 「命の熱（life heat）」を 呼び覚ますこと)",
        "thinking": "無理やり燃やすのではなく、そこにある小さな可能性（火種）を優しく見守り、酸素（興味）を送り込むことで、自発的な輝きを促すこと. 語源は「ロウソク、松明」. それは 暗闇の中に 幽かな 秩序（光）を 導入し 停滞していた 運命（薪）を 生命の 躍動へと 変容させる 聖なる「着火」のアクションです.",
        "aftertaste": "情熱の火種. 自分の冷めた心に 絶望しないで. あなたが「キンドル（点火）」の 勇気を持つとき その小さな火は やがて 世界を温める 巨大な 情熱の炎へと 成長してゆくのだから.",
        "example": "His speech was designed to kindle a sense of hope and purpose in the hearts of the young listeners.",
        "deep_dive": { "roots": [{"term": "kand-", "meaning": "to shine"}], "points": ["candid（率直な：白く光る）や candidate（候補者：白い服を着た人）と同じ。偽りのない輝き。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "instigate_ignition",
        "word": "Instigate",
        "meaning": "扇動する、(計画などを)着手させる、(事件を)引き起こす",
        "era": "16th Century Latin in- + stigare",
        "etymology": {
            "components": ["in- (into)", "stigare (to prick)"],
            "original_statement": "From Latin instigatus, past participle of instigare (to urge on, incite), from in- (into, toward) + stigare (to prick, goad)."
        },
        "concept": "Pricking into action (「境界（boundary）」を 鋭く 「突き破り（prick）」 停滞した 現状を 「強制的に」 動かし始めること)",
        "thinking": "穏やかな説得ではなく、鋭い刺激（痛みや驚き）を与えることで、もはや後戻りできない変化の連鎖を始動させること. 語源は「突き分ける、駆り立てる」. それは 社会の淀みを 打ち破り 新しい歴史の ページを めくるための、荒々しくも 必要な「最初の一突き」です. 刺激は、覚醒です.",
        "aftertaste": "覚醒の一突き. 周りと同じ 眠りの中に 留まらないで. あなたが「インスティゲイト（扇動/着手）」し 最初の 変化を 起こすとき 止まっていた 運命の歯車は 爆発的な 勢いで 回り始めるのだから.",
        "example": "He was accused of trying to instigate a peaceful protest against the government's new environmental policy.",
        "deep_dive": { "roots": [{"term": "steig-", "meaning": "to prick, stick"}], "points": ["distinct（明瞭な：突き分けられた）や instinct（本能：内に刻まれたもの）と同じ。消せない痕跡. "] },
        "part_of_speech": "verb"
    },
    {
        "id": "provoke_ignition",
        "word": "Provoke",
        "meaning": "引き起こす、刺激する、怒らせる、(興味を)そそる",
        "era": "14th Century Latin pro- + vocare",
        "etymology": {
            "components": ["pro- (forth)", "vocare (to call)"],
            "original_statement": "From Old French provoquer, from Latin provocare (call forth, challenge, appeal), from pro- (forth) + vocare (to call)."
        },
        "concept": "Calling forth (「沈黙（silence）」を 「呼び出し（call forth）」 真実を 「曝け出させる（reveal）」 挑発的な 対話)",
        "thinking": "相手の奥深くに眠っている本音や、宇宙の隠された法則を、あえて「揺さぶる」ことで表面化させる、ダイナミックな交信術. 語源は「前へ呼び出す」. それは 単なる怒りの誘発ではなく 停滞した均衡を 壊し より高次な 真実へと 辿り着くための 聖なる「挑戦」のアクションです.",
        "aftertaste": "真実の呼び出し. 予定調和の 安寧に 浸らないで. あなたが 自分自身を、そして 世界を「プロヴォーク（刺激/挑発）」し続けることで 魂は 常に 瑞々しい 驚きと 成長を 手にするのだから.",
        "example": "The artist's controversial performance was intended to provoke critical thinking about societal norms.",
        "deep_dive": { "roots": [{"term": "wekw-", "meaning": "to speak"}], "points": ["voice（声）や advocate（擁護者：呼び寄せる人）と同じ。言葉による「現実への干渉」. "] },
        "part_of_speech": "verb"
    },
    {
        "id": "ignite_ignition",
        "word": "Ignite",
        "meaning": "点火する、火がつく、(情熱などを)燃え上がらせる",
        "era": "17th Century Latin ignis",
        "etymology": {
            "components": ["ignis (fire)"],
            "original_statement": "From Latin ignitus, past participle of ignire (to set on fire), from ignis (fire)."
        },
        "concept": "Becoming fire (「物質（matter）」を 「エネルギー（energy）」へと 一気に 「昇華（sublime）」させる 極限の 状態変化)",
        "thinking": "摩擦や熱が限界点（クリティカル・ポイント）を超えた瞬間、全く別の質の存在（炎）へと変貌を遂げる、不可逆の奇跡. 語源は「火」. それは 理論（薪）が 確信（炎）へと 変わる 決定的な瞬間であり あなたの人生が 宇宙の活力と 直結する 聖なる「点火」です.",
        "aftertaste": "変貌の瞬間. 準備ばかりして 終わらないで. あなたの情熱が「イグナイト（点火）」したとき 長い間 溜め込んできた 全ての経験が あなたを 輝かせるための 無限の 燃料に 変わるのだから.",
        "example": "The news of the discovery ignited a wave of excitement throughout the entire global scientific community.",
        "deep_dive": { "roots": [{"term": "egni-", "meaning": "fire"}], "points": ["igneous（火成の）や Agni（アグニ：インドの火の神）と同じ。生命を活性化させる、根源的な力. "] },
        "part_of_speech": "verb"
    },
    {
        "id": "detonate_ignition",
        "word": "Detonate",
        "meaning": "爆発させる、爆発する、急激に引き起こす",
        "era": "18th Century Latin de- + tonare",
        "etymology": {
            "components": ["de- (down)", "tonare (to thunder)"],
            "original_statement": "From Latin detonatus, past participle of detonare (to thunder down, thunder forth), from de- (down, forth) + tonare (to thunder)."
        },
        "concept": "Thundering down (「鬱積した力（built-up power）」を 「雷鳴（thunder）」と共に 一気に 「地上へと（down）」 解き放つこと)",
        "thinking": "徐々に燃えるのではなく、音速を超えて膨張し、周囲の風景を一瞬で塗り替えてしまう、圧倒的な解放と破壊のエネルギー. 語源は「雷を轟かせる」. それは 抑圧されていた真実が、システムの限界を 打ち破り 世界に 激震を 与える 聖なる「浄化」の 衝撃波です.",
        "aftertaste": "雷鳴の解放. 力を 溜め込みすぎて 苦しまないで. あなたの内なる真実を「デトネイト（爆発）」させるとき その衝撃は 古い固定観念を 吹き飛ばし 新しい自由の 広野を 創り出すのだから.",
        "example": "One simple question from the student was enough to detonate a long-overdue debate about ethics in the classroom.",
        "deep_dive": { "roots": [{"term": "ten-", "meaning": "to stretch, thunder"}], "points": ["thunder（雷）や tension（緊張）と同じ。張り詰めた糸が、ついに音を立てて 弾ける瞬間. "] },
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
        print(f"Success: Added {added} words in Cycle 149.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
