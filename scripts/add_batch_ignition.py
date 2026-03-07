import json
import re

word_batch = [
    # Cycle 130: Spark & Ignition
    {
        "id": "kindle_fire",
        "word": "Kindle",
        "meaning": "火をつける、(感情などを)燃え立たせる、輝き始める",
        "era": "12th Century Old Norse kyndill",
        "etymology": {
            "components": ["kyndill (torch)"],
            "original_statement": "From Middle English kindlen, from Old Norse kyndill (torch), from Latin candela (candle)."
        },
        "concept": "To set on fire (小さな 「火種（torch）」から 巨大な 「炎（fire）」を 呼び覚ますこと)",
        "thinking": "冷え切った場所に 最初の一滴の「熱」をもたらし 静かに、しかし確実に 周囲を巻き込んで 燃え広がっていく 創造的なプロセス. 語源は「松明（たいまつ）」. それは 暗闇を照らすだけでなく 眠っていた情熱や 才能という名の「薪（まき）」に 命を吹き込む 聖なる点火です.",
        "aftertaste": "点火の瞬間. あなたの心という暖炉に 今 何の火を灯そうか. 小さな火種を 慈しみ、育むことで やがて世界を暖める 巨大な情熱へと 変えてゆこう.",
        "example": "The teacher's passionate lecture helped to kindle a lifelong interest in history in her students.",
        "deep_dive": { "roots": [{"term": "kand-", "meaning": "to shine"}], "points": ["candle（キャンドル）や candid（率直な：白く光る）と同じ。光の顕現。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "ignite_fire",
        "word": "Ignite",
        "meaning": "点火する、火がつく、(情熱などが)爆発する",
        "era": "17th Century Latin ignis",
        "etymology": {
            "components": ["ignis (fire)"],
            "original_statement": "From Latin ignitus, past participle of ignire (to set on fire), from ignis (fire)."
        },
        "concept": "Action of fire (「火（fire）」そのものが 持つ 爆発的で 瞬間的な 「変容」の力)",
        "thinking": "溜め込まれたエネルギーが 臨界点を超え 閃光とともに 全く別の形態へと 移行する ドラマチックな瞬間. 語源は「火」. それは 迷いを一瞬で焼き尽くし 純粋な意志だけを 結晶化させる 激しい浄化の儀式でもあります. 火がついたとき 世界は二度と元には戻りません.",
        "aftertaste": "爆発の純粋。準備はもうできているはずだ。自分を信じて その「火蓋（イグニッション）」を切ろう。炎が導くその先には あなたがまだ見ぬ 新しい地平が広がっている。",
        "example": "A single spark was enough to ignite the gas and cause a massive explosion.",
        "deep_dive": { "roots": [{"term": "egni-", "meaning": "fire"}], "points": ["igneous（火成の）や Agni（インド神話の火神アグニ）と同じ。宇宙を動かす根源的な熱。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "conflagration_fire",
        "word": "Conflagration",
        "meaning": "大火、(戦争・騒乱などの)大突発、大火災",
        "era": "16th Century Latin con- + flagrare",
        "etymology": {
            "components": ["con- (thoroughly)", "flagrare (to burn)"],
            "original_statement": "From Latin conflagrationem (a burning up), from conflagrare (to burn up), from con- (together, thoroughly) + flagrare (to burn, blaze, glow)."
        },
        "concept": "Burning up thoroughly (「徹底的に（thoroughly）」 「燃え上がる（blaze）」 制御不能な 巨大な 浄化の炎)",
        "thinking": "個人の力の及ばない 時代や社会を 根本から刷新してしまうような 圧倒的な熱量の 噴出. 語源は「完全に燃え尽くす」. それは 全てを灰にする破壊であると同時に 古い秩序を焼き払い 新しい芽が吹くための 肥沃な大地（灰）を 作るための 聖なる暴力でもあります.",
        "aftertaste": "灰からの再生. どんなに激しい炎（困難）も 全てを焼き尽くすことはできない. むしろ 焼き尽くされた後にこそ あなたという存在の 「真の形」が 鮮やかに浮かび上がるのだから.",
        "example": "The small dispute escalated rapidly into a nationwide conflagration of civil unrest.",
        "deep_dive": { "roots": [{"term": "bhleg-", "meaning": "to burn, shine, flash"}], "points": ["flame（炎）や flagrant（目に余る：燃え立っている）と同じ。激越なる光。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "ember_fire",
        "word": "Ember",
        "meaning": "残り火、残り火のような(感情の)残し",
        "era": "Pre-12th Century Old English æmerge",
        "etymology": {
            "components": ["æmerge (ember, ashes)"],
            "original_statement": "From Old English æmerian, from Proto-Germanic aimuzjon (embers), perhaps from ai- (to burn) + muzjon (ashes)."
        },
        "concept": "Glowing ashes (炎が去った後の 「灰（ashes）」の中に 密かに 「息づく（glow）」 静かな熱)",
        "thinking": "華やかな輝きを終え 深い沈黙の中で じっと次の復活を待っている 根源的な命のしるし. 語源は「燃える灰」. それは 激しい情熱（炎）よりも 遥かに長く持続し 絶望の淵にあっても 私たちの心を 深部から温め続ける 慈愛に満ちた熱です.",
        "aftertaste": "静かなる持続. 派手な輝きはなくてもいい. 自分の心の奥底に 決して消えない「残り火（エンバー）」を 絶やさず持ち続けよう. それが あなたの人生を 最後に救う光になるのだから.",
        "example": "The campers gathered around the dying fire, watching the glowing embers in the darkness.",
        "deep_dive": { "roots": [{"term": "ai-", "meaning": "to burn"}], "points": ["ash（灰）とは違う「熱を持っている」という強調。慈悲深い持続。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "pyre_fire",
        "word": "Pyre",
        "meaning": "火葬の薪、(物を焼くための)積み上げられた薪",
        "era": "17th Century Greek pyr",
        "etymology": {
            "components": ["pyr (fire)"],
            "original_statement": "From Latin pyra, from Greek pyra (hearth, funeral pyre), from pyr (fire)."
        },
        "concept": "Tower of fire (「火（fire）」を 捧げるために 「積み上げられた（hearth）」 訣別と 祈りの聖域)",
        "thinking": "過去の栄光や 痛みの記憶を 炎という名の 聖なる浄化へと 委（ゆだ）ねるための 厳粛な儀式の場所. 語源は「火」. それは 執着を捨て去り 魂を肉体の重力から 解き放って 宇宙の円環へと 戻していくための 最後の越境地点です. 全てを燃やし、空（くう）に帰す勇気を.",
        "aftertaste": "訣別の炎. あなたを縛り付けている 古い殻（思い出や後悔）を この「パイル（薪）」の上に置こう. 炎が全てを空へと運ぶとき あなたは本当の自由を 手に入れるのだから.",
        "example": "He decided to build a symbolic pyre for all the letters and photographs of his past life.",
        "deep_dive": { "roots": [{"term": "pur-", "meaning": "fire"}], "points": ["pyrotechnics（花火：火の術）や purity（純粋：火による浄化）と同じ。生命の昇華。"] },
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
        print(f"Success: Added {added} words in Cycle 130.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
