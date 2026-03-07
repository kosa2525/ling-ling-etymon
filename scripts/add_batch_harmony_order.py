import json
import re

word_batch = [
    # Cycle 101: Harmony & Order
    {
        "id": "concord_harmony",
        "word": "Concord",
        "meaning": "一致、調和、合意",
        "era": "14th Century Latin com- + cor",
        "etymology": {
            "components": ["com- (together)", "cor (heart)"],
            "original_statement": "From Old French concorde, from Latin concordia (agreement), from concors (of the same mind, agreeing), from com- (together) + cor (heart)."
        },
        "concept": "Hearts together (「心（heart）」を一つに「合わせ（together）」、響き合うこと)",
        "thinking": "単なる意見の一致ではなく、複数の鼓動が重なり合い、一つの音楽を奏でるような深い共鳴. 語源の cor は、命の源である心臓。それが同じリズムを刻むとき、争いは消え、そこに美しい秩序が生まれます。魂と魂が、言葉を超えて握手を交わした瞬間の静寂です。",
        "aftertaste": "重なり合う鼓動。あなたは一人ではない。世界という巨大なオーケストラの一員として、今、完璧な和音の中にいる。",
        "example": "The two nations lived in perfect concord for many decades.",
        "deep_dive": { "roots": [{"term": "kerd-", "meaning": "heart"}], "points": ["core（核）や courage（勇気：心の力）と同じ。本質的な繋がり。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "symmetry_harmony",
        "word": "Symmetry",
        "meaning": "対称性、釣り合い、調和",
        "era": "16th Century Greek syn- + metron",
        "etymology": {
            "components": ["syn- (together)", "metron (measure)"],
            "original_statement": "From Latin symmetria, from Greek symmetria (agreement in measure, proportion), from symmetros (measured together, having a common measure), from syn- (together) + metron (measure)."
        },
        "concept": "Measured together (すべての要素を共に「量り（measure）」、完璧な「均衡（balance）」を保つこと)",
        "thinking": "過剰も不足もなく、右と左、光と影が、一寸の狂いもなく響き合っている美しさ. 語源の metron は、基準となる物差し。それは、カオスの中に潜む数学的な秩序の証明であり、神が世界を設計した際に引いた「黄金の線」の記憶です。静謐（せいひつ）にして、圧倒的な安定感。",
        "aftertaste": "完璧な均衡。その秩序の美しさに触れるとき、あなたの心もまた、静かに、正しく整えられてゆく。",
        "example": "The flawless symmetry of the building's facade was a masterpiece of architectural design.",
        "deep_dive": { "roots": [{"term": "me-", "meaning": "to measure"}], "points": ["measure（測る）や meter（計器）と同じ。正確さが美を生む。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "equilibrium_harmony",
        "word": "Equilibrium",
        "meaning": "平衡、均衡、心の平静",
        "era": "17th Century Latin aequus + libra",
        "etymology": {
            "components": ["aequus (equal)", "libra (weight, balance, scales)"],
            "original_statement": "From Latin aequilibrium (an even balance), from aequilibris (evenly balanced), from aequus (equal) + libra (weight, balance, scales)."
        },
        "concept": "Equal weight (「重さ（weight）」が「等しく（equal）」、天秤が水平を保っている状態)",
        "thinking": "外側からのどんな激しい衝撃を受けても、中心を失わず、再び静止点へと戻る力. 語源の libra は、星座の天秤座でもあります。それは物理的なバランスだけでなく、激動する感情の荒波の中で、自分を「中庸（中心）」に繋ぎ止めておく、知的な強さのことです。",
        "aftertaste": "動かぬ中心. 嵐が吹き荒れても、あなたの天秤は水平を保ち、静かに明日を待つ。",
        "example": "The meditation helped him maintain his emotional equilibrium in high-stress situations.",
        "deep_dive": { "roots": [{"term": "aik-", "meaning": "even, level"}], "points": ["equal（等しい）や equity（公平）と同じ。正義は『等しさ』のなかに宿る。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "resonance_harmony",
        "word": "Resonance",
        "meaning": "共鳴、共振、響き",
        "era": "15th Century Latin re- + sonare",
        "etymology": {
            "components": ["re- (again)", "sonare (to sound)"],
            "original_statement": "From Middle French resonance, from Latin resonantia (echo), from resonare (to sound back, resound), from re- (again) + sonare (to sound)."
        },
        "concept": "Sounding back (音が「もう一度（again）」「鳴り（sound）」返し、空間全体を震わせること)",
        "thinking": "一つの振動が別の何かに伝わり、新しい音を生み出し、場全体が大きな波に包まれる現象. 語源の sonare は「鳴る」。あなたの言葉や存在が、誰かの心の琴線（きんせん）に触れ、そこで新しいメロディが生まれるとき、孤独は消え、世界は一つの豊かな楽器に変容します。魂の対話の、最も美しい形。",
        "aftertaste": "消えぬ残響。あなたの祈りは、世界の隅々まで響き渡り、いつか自分自身の元へと、より大きな愛となって返ってくる。",
        "example": "His words had a deep resonance with the audience, moving many to tears.",
        "deep_dive": { "roots": [{"term": "swen-", "meaning": "to sound"}], "points": ["sound（音）や sonar（ソナー）と同じ。振動する命のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "euphony_harmony",
        "word": "Euphony",
        "meaning": "快い響き、楽音、心地よい調和",
        "era": "17th Century Greek eu- + phone",
        "etymology": {
            "components": ["eu- (good, well)", "phone (sound, voice)"],
            "original_statement": "From Middle French euphonie, from Late Latin euphonia, from Greek euphonia (goodness of sound), from eu- (good) + phone (sound, voice)."
        },
        "concept": "Good sound (耳に優しく、魂に「心地よい（good）」、「響き（sound）」のこと)",
        "thinking": "不協和音を排し、流れるように滑らかで、聞き手の心を穏やかに満たす調和. 語源の eu- は「幸福」をも意味します。それは単なる美辞麗句（びじれいく）ではなく、真実が最も適切な旋律をまとって現れたときの、必然の響き。あなたの言葉が、誰かの眠りを守る子守唄（こもりうた）になる瞬間です。",
        "aftertaste": "耳に残る至福。世界という騒音のなかで、あなたは自ら快い調べを奏で、周囲を平和で満たしてゆく。",
        "example": "The poet was celebrated for the delicate euphony and rhythm of his verses.",
        "deep_dive": { "roots": [{"term": "esu-", "meaning": "good"}, {"term": "bha-", "meaning": "to speak"}], "points": ["euthanasia（安楽死：良い死）や telephone（電話：遠い声）と同じ。"] },
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
        print(f"Success: Added {added} words in Cycle 101.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
