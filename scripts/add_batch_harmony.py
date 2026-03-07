import json
import re

word_batch = [
    # Cycle 88: Balance & Harmony
    {
        "id": "equilibrium_balance",
        "word": "Equilibrium",
        "meaning": "平衡、均衡、心の平穏",
        "era": "14th Century Latin aequus + libra",
        "etymology": {
            "components": ["aequus (equal)", "libra (weight, balance, scales)"],
            "original_statement": "From Latin equilibrium, from aequus (equal) + libra (weight, balance, scales)."
        },
        "concept": "Equal weight (天秤の「重さ（weight）」が「等しく（equal）」なり、水平に保たれること)",
        "thinking": "激しく揺れ動く感情や、矛盾する二つの価値観。それらが綱渡りのように危ういバランスを保ち、一瞬の「静止」へと辿り着く状態。語源の libra は星座の天秤座でもあり、そこには宇宙的な正義と秩序への憧憬が込められています。中心を見つけ、そこに留まることの強さ。",
        "aftertaste": "完全な水平。喧騒（けんそう）の真ん中で、あなたは自分という天秤がピタリと止まる、その中心点を知っている。",
        "example": "Yoga helped her regain her physical and emotional equilibrium after the stressful project.",
        "deep_dive": { "roots": [{"term": "aik-", "meaning": "even, level"}, {"term": "lithra-", "meaning": "unit of weight"}], "points": ["equation（方程式）や level（水平）と同じ、等価であることの美学。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "symmetry_balance",
        "word": "Symmetry",
        "meaning": "対称、均衡、調和",
        "era": "16th Century Greek syn- + metron",
        "etymology": {
            "components": ["syn- (together)", "metron (measure)"],
            "original_statement": "From Latin symmetria, from Greek symmetria, from syn- (together) + metron (measure)."
        },
        "concept": "Measured together (複数のものが「共に（together）」同じ「尺度（measure）」で配置されていること)",
        "thinking": "左右が鏡合わせのように整っていること。それは単なる外見上の美しさではなく、宇宙の深淵にあるロゴス（理法）が、視覚的な形として現れたものです。黄金比、木の葉の葉脈、私たちの体。万物が「あるべき場所」に収まっているという感覚が、魂に深い安らぎを与えます。",
        "aftertaste": "響き合う形。右が左を呼び、左が右を補う。その完成された円環。",
        "example": "The interior design of the temple was characterized by perfect symmetry and elegant proportions.",
        "deep_dive": { "roots": [{"term": "sem-", "meaning": "one, as one"}, {"term": "me-", "meaning": "to measure"}], "points": ["synchronize（同期する）や meter（計器）と同じ、調和した計量のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "poise_balance",
        "word": "Poise",
        "meaning": "均衡、落ち着き、優雅な身のこなし",
        "era": "14th Century Old French pois",
        "etymology": {
            "components": ["pensum (something weighed, weight)"],
            "original_statement": "From Old French pois (weight, balance), from Latin pensum (something weighed, portion of wool weighed out to be spun), from pendere (to weigh)."
        },
        "concept": "Weighed and held (「重さ（weight）」を正確に量り、制御して「保持」すること)",
        "thinking": "外からの衝撃やプレッシャーを受けても、自分を失わず、凛としてそこに立ち続ける精神的な「重心」。語源の pendere は「吊（つる）す」や「量る」を意味します。それは自分自身の価値や責任の重さを正しく知り、それを一点の迷いもなく支えきっている人の、静かなる威厳です。",
        "aftertaste": "凛とした静止。嵐が吹き荒れても、あなたの指先は微塵（みじん）も揺れることはない。",
        "example": "She handled the difficult interview with remarkable poise and self-confidence.",
        "deep_dive": { "roots": [{"term": "pend-", "meaning": "to hang, weigh"}], "points": ["pendant（ペンダント）や spend（費やす：重さを量って支払う）と同じルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "consensual_harmony",
        "word": "Consensus",
        "meaning": "合意、意見の一致、世論",
        "era": "17th Century Latin con- + sentire",
        "etymology": {
            "components": ["con- (together)", "sentire (to feel)"],
            "original_statement": "From Latin consensus (agreement, accord), past participle of consentire (to agree), literally 'to feel together,' from con- (together) + sentire (to feel)."
        },
        "concept": "Feeling together (バラバラの個体が、一つのことを「共に（together）」「感じる（feel）」こと)",
        "thinking": "論理的に納得させること（Agreement）よりも深く、沈黙や共感を通じて、いつの間にか全員が「同じ空気」に包まれている状態. 語源の sentire は「感じる」。言葉を積み重ねる以上に、互いの心の波長が調和し、一つの大きな「意志のうねり」に変わる、奇跡的な一致の瞬間です。",
        "aftertaste": "響き合う心。誰が言い出したわけでもない。けれど、私たちは同じ夢を見ていることを知っている。",
        "example": "After hours of discussion, the committee finally reached a consensus on the new policy.",
        "deep_dive": { "roots": [{"term": "sent-", "meaning": "to go, to perceive"}], "points": ["sense（感覚）や sentiment（感情）と同じ。知性よりも『感覚』が先立つ一致。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "attunement_harmony",
        "word": "Attunement",
        "meaning": "同調、調律、適応",
        "era": "16th Century Latin ad- + tonus",
        "etymology": {
            "components": ["ad- (to)", "tonus (sound, tone, tension)"],
            "original_statement": "From attune (verb), from ad- (to) + tune (sound), a variant of tone."
        },
        "concept": "Matching the tone (相手、あるいは環境の「音（tone）」に、自分の弦を「合わせる（to）」こと)",
        "thinking": "自分が正しいと主張するのをやめ、世界が奏でているかすかな旋律に耳を澄ませ、自らの振動数をそれに合わせていくこと. それは、自分の「音」を失うことではなく、世界という巨大なオーケストラの一部として、より美しい共鳴を生み出すための、謙虚で高度な変容のプロセスです。",
        "aftertaste": "澄み渡る響き。自分と世界を隔てていた壁が消え、あなたは一つの大きな音楽の一部になる。",
        "example": "Effective therapy requires a deep emotional attunement between the patient and the counselor.",
        "deep_dive": { "roots": [{"term": "ten-", "meaning": "to stretch"}], "points": ["tone（音色）は弦の『張り具合』。attunement とは、自分という楽器の『張り』を整えること。"] },
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
        print(f"Success: Added {added} words in Cycle 88.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
