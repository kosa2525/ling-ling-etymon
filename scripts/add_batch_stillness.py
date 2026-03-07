import json
import re

word_batch = [
    # Cycle 77: Stillness & Tranquility
    {
        "id": "serenity_peace",
        "word": "Serenity",
        "meaning": "静穏、平穏、晴朗",
        "era": "15th Century Latin serenus",
        "etymology": {
            "components": ["serenus (clear, bright, calm)"],
            "original_statement": "From Latin serenitatem (clearness, serenity), from serenus (clear, bright, fair, calm, quiet)."
        },
        "concept": "Clear and bright (雲一つなく「晴れ渡り（clear）」、静まり返っていること)",
        "thinking": "嵐が去ったあとの空のように、一切の濁りや騒がしさが消え去った、究極の透明な静寂。それは外部の状況に左右されない、魂の奥底の「晴天」です。何が起きても、あなたの内側にあるこの青空を誰も奪うことはできない。その静かなる勝利の別名です。",
        "aftertaste": "心の晴天。どんな嵐も、この深く、澄み渡った青さを汚すことはできない。",
        "example": "He practiced meditation every morning to maintain his inner serenity throughout the busy day.",
        "deep_dive": { "roots": [{"term": "ksero-", "meaning": "dry (possible)"}], "points": ["serene（静かな）は、かつては『乾燥して雲がない』状態を指したという説。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "placidity_peace",
        "word": "Placid",
        "meaning": "穏やかな、平穏な、落ち着いた",
        "era": "17th Century Latin placidus",
        "etymology": {
            "components": ["placere (to please)"],
            "original_statement": "From French placide, from Latin placidus (gentle, quiet, gentle, calm, peaceful), from placere (to please)."
        },
        "concept": "Pleasingly calm (心地よく「満たされ（please）」、静まっていること)",
        "thinking": "波一つない湖面のように、滑らかで、見る者を安らぎへと誘う静けさ。語源の placere は「喜ばせる」を意味し、周囲との摩擦がなく、ただそこにあるだけで心地よい調和を生み出している状態を指します。抗うのではなく、すべてを受け容れ、包み込むような優しき静止。",
        "aftertaste": "鏡のような湖面。世界をありのままに映し出しながら、自分自身は決して揺れない。",
        "example": "She had a placid nature and was rarely disturbed by the everyday chaos of city life.",
        "deep_dive": { "roots": [{"term": "plak-", "meaning": "to be flat"}], "points": ["plane（平面）や plateau（高原）と同じ、平らで安定したルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "tranquility_peace",
        "word": "Tranquil",
        "meaning": "静かな、穏やかな、安らかな",
        "era": "14th Century Latin trans- + quies",
        "etymology": {
            "components": ["trans- (beyond)", "quies (rest, quiet)"],
            "original_statement": "From Old French tranquille, from Latin tranquillus (quiet, calm, still), probably from trans- (beyond, over) + an adjectival form from the root of quies (rest, quiet)."
        },
        "concept": "Beyond the noise (騒音を「越えた（beyond）」先にある、深い休息)",
        "thinking": "ただ静かであるだけでなく、喧騒や混乱を「通り抜けた」果てに辿り着く、より高い次元の静寂。語源の quies は「休息（quiet）」であり、そこには深い安らぎと解放感が伴います。世界が寝静まった深夜、あるいは瞑想の果てに訪れる、神聖なまでの静止の瞬間。",
        "aftertaste": "境界を越えた休息。すべての戦いが終わり、ただ存在することの喜びだけが残る場所。",
        "example": "The small cabin offered a tranquil escape from the pressures of modern life.",
        "deep_dive": { "roots": [{"term": "kwi-", "meaning": "rest, quiet"}], "points": ["quit（辞める：安らぎに入る）や quiet（静かな）と同じ、終止符のルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "halcyon_peace",
        "word": "Halcyon",
        "meaning": "穏やかな、平和な、黄金時代の",
        "era": "14th Century Greek halkyon",
        "etymology": {
            "components": ["hals (sea)", "kyon (conceiving)"],
            "original_statement": "From Latin halcyon, from Greek halkyon (kingfisher), from hals (sea) + kyon (conceiving), from the myth that the bird nested on the sea during winter solstice."
        },
        "concept": "Calming the sea (冬至の荒れる海を「鎮めて（calm）」巣を作る伝説の鳥)",
        "thinking": "ギリシャ神話に登場するカワセミ（halcyon）が、海の上に卵を孵す間、神々が海を静めたという伝説に由来します。一年で最も暗い季節（冬至）に訪れる、奇跡のような「穏やかな日々（halcyon days）」。それは嵐の真っなか一瞬の、しかし永遠のような平和の象徴です。",
        "aftertaste": "奇跡の静寂。あなたが心に巣を作るなら、荒れ狂う海さえも鏡のように静まり返るだろう。",
        "example": "He often recalled the halcyon days of his childhood spent in that quiet village.",
        "deep_dive": { "roots": [{"term": "sal-", "meaning": "salt, sea"}], "points": ["伝説に基づく叙情的な言葉。平和とは『環境の鎮まり』であるという古代の直感。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "stagnant_peace",
        "word": "Stagnant",
        "meaning": "(水が)滞っている、不活発な",
        "era": "17th Century Latin stagnare",
        "etymology": {
            "components": ["stagnon (standing water, pond)"],
            "original_statement": "From Latin stagnantem, from stagnare (to stagnate, form a pool of standing water), from stagnum (pond, pool, standing water)."
        },
        "concept": "Standing water (流れを失い、その場に「留まって（standing）」いる水)",
        "thinking": "「平和」の影の部分。流れ（変化）が止まり、腐敗や倦怠（けんたい）が始まりつつある状態。静寂は時として、死の予兆にもなり得ます。生命とは動き続けること。この言葉は、私たちに「心地よい停滞」という罠を警告し、再び流れ出すことの重要性を思い出させてくれます。",
        "aftertaste": "淀（よど）み。安らぎがいつしか、あなたを縛る鎖へと変わらないように。常に新しい一滴を注ぎ込め。",
        "example": "The lack of new investments has caused the local economy to become stagnant.",
        "deep_dive": { "roots": [{"term": "stag-", "meaning": "to seep, drip"}], "points": ["stag（雄鹿：力強く立ち入るもの）とは対照的に、水が『しみ出す』程度の動きの無さ。"] },
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
        print(f"Success: Added {added} words in Cycle 77.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
