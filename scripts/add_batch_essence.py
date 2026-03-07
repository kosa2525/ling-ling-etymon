import json
import re

word_batch = [
    # Cycle 84: Essence & Core
    {
        "id": "quintessence_essence",
        "word": "Quintessence",
        "meaning": "精髄、神髄、第五元素",
        "era": "15th Century Latin quinta + essentia",
        "etymology": {
            "components": ["quinta (fifth)", "essentia (essence, being)"],
            "original_statement": "From Old French quinte essence, from Medieval Latin quinta essentia (fifth essence), the substance of which the heavenly bodies were thought to be composed."
        },
        "concept": "The fifth element (四大元素を超えた先にある、もっとも純粋な「第五（fifth）」の「本質（essence）」)",
        "thinking": "地・水・火・風という地上の物質を超えた、天体を構成する第五の元素。それは不純物を一切取り除いたあとに残る、物事の「最も純粋な核心」を指します。あなたの人生を形作るエピソードをすべて削ぎ落としたとき、最後に残る輝き。それがあなたの『神髄』です。",
        "aftertaste": "純度。すべてを失った後に、どうしても消すことのできなかった、たった一つの答え。",
        "example": "To many, the small village represents the quintessence of English country life.",
        "deep_dive": { "roots": [{"term": "penkwe-", "meaning": "five"}, {"term": "es-", "meaning": "to be"}], "points": ["essential（本質的な）や entity（実体）と同じ、存在の根源。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "pith_essence",
        "word": "Pith",
        "meaning": "髄、核心、中身、(話の)眼目",
        "era": "Old English pitha",
        "etymology": {
            "components": ["pitha (marrow, internal part)"],
            "original_statement": "From Old English pitha (pith of plants, marrow), from West Germanic pithan."
        },
        "concept": "Internal part (植物の茎の中心にある「柔組織（marrow）」、転じて物事の本質)",
        "thinking": "装飾的で派手な外側ではなく、その生命を支えている「もっとも柔らかく、しかし最も重要な中心部」。言葉のピス（Pith）は、余計な飾りを省いた、むき出しの真実を指します。核心を突く（pithy）表現とは、一滴で人を酔わせるほど濃縮された、命のエッセンスです。",
        "aftertaste": "むき出しの言葉。飾りを脱ぎ捨てて、ただ一つの『真実』だけを差し出す潔さ。",
        "example": "He managed to capture the pith of the argument in just a few, well-chosen sentences.",
        "deep_dive": { "roots": [{"term": "Unknown source"}], "points": ["ゲルマン語由来の古い言葉。植物の生命が集中する中心点。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "marrow_essence",
        "word": "Marrow",
        "meaning": "骨髄、核心、活力の源",
        "era": "Old English mearg",
        "etymology": {
            "components": ["mearg (pith, marrow)"],
            "original_statement": "From Old English mearg (marrow), from Proto-Germanic mazga (internal fat, marrow)."
        },
        "concept": "Internal fat (骨の奥深くにある「脂肪（fat）」、命を育む根源的な場所)",
        "thinking": "硬い骨によって守られた、生命の創造主. 血を作り、命を繋ぎ、凍える夜に体温を支える「奥底の熱」。思考の骨髄（to the marrow）にまで届くとは、表面的な理解を通り抜け、あなたという存在の根っこが震えるほどの深い共鳴を意味します。",
        "aftertaste": "奥底の熱. 決して人には見えない場所で、あなたは静かに、最も大切なものを育み続けている。",
        "example": "The winter cold seemed to chill him to the very marrow of his bones.",
        "deep_dive": { "roots": [{"term": "moz-go-", "meaning": "marrow, brain"}], "points": ["brain（脳）とも語源的に繋がりがあり、身体と精神の『中心』を指す。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "crux_essence",
        "word": "Crux",
        "meaning": "決定的な点、難問、十字形",
        "era": "19th Century Latin crux",
        "etymology": {
            "components": ["crux (cross, torture instrument)"],
            "original_statement": "From Latin crux (cross, stake, gallows), of unknown origin."
        },
        "concept": "The crossing point (二つの糸が「交差（cross）」し、もつれ、最も解決が困難で重要な場所)",
        "thinking": "複雑に絡み合った問題の、たった一つの結び目。そこを解けばすべてが解決し、そこを外せばすべてが崩壊する、恐るべき「急所」。語源の crux は「十字架」であり、苦渋の決断や、逃れられない運命の交差点を象徴しています. 最も辛く、最も光り輝く分岐点。",
        "aftertaste": "交差点。そこを通り過ぎる時、あなたの人生は永遠に書き換えられる。",
        "example": "The crux of the matter is that we simply don't have enough data to proceed safely.",
        "deep_dive": { "roots": [{"term": "kreuk-", "meaning": "to bend, curve (possible)"}], "points": ["cross（十字）や crucial（決定的な）と同じ。運命を曲げるポイント。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "nucleous_essence",
        "word": "Nucleus",
        "meaning": "(原子・細胞の)核、中心、(発展の)基礎",
        "era": "18th Century Latin nux",
        "etymology": {
            "components": ["nux (nut)", "nucleus (kernel)"],
            "original_statement": "From Latin nucleus (kernel), from nuculeus (little nut), from nux (nut)."
        },
        "concept": "Kernel of a nut (硬い殻の中にある「小さな実（little nut）」、生命の設計図)",
        "thinking": "外側の殻（形）がどれほど巨大であっても、そのすべての情報を司り、求心力を持って全体を束ねている、極小の「司令塔」。最初の一粒. あらゆる壮大な計画も、最初はあなたの頭の中に生まれた、この小さな「核（nucleus）」から放射状に広がっていったのです。",
        "aftertaste": "最初の一粒。小さく、けれどそこには宇宙を再構成するほどの力が凝縮されている。",
        "example": "A small group of enthusiastic workers formed the nucleus of the new research project.",
        "deep_dive": { "roots": [{"term": "kneu-", "meaning": "nut"}], "points": ["nuclear（原子力の）や newel（階段の親柱）と同じ、回転と安定の中心。"] },
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
        print(f"Success: Added {added} words in Cycle 84.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
