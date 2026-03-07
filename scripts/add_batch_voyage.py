import json
import re

word_batch = [
    {
        "id": "frontier_unseen",
        "word": "Frontier",
        "meaning": "辺境、国境、最前線、未知の領域",
        "era": "14th Century Old French/Latin frons",
        "etymology": {
            "components": ["frons (forehead, front)"],
            "original_statement": "From Old French frontier, from Latin frontem (forehead, front, brow), hence 'the part that faces something'."
        },
        "concept": "The part that faces forward (何かに「対面」している最前部分)",
        "thinking": "もともとは、敵や未知の土地と向き合っている「額（forehead/frons）」のような場所。そこは既知と未知の境界線であり、勇気を持って「向き合う（face）」者だけが到達できる一線です。科学、思考、心のフロンティア。それは、常に新しい風が吹き荒れる場所です。",
        "aftertaste": "額を上げ、まだ誰も知らない、見果てぬ地平をただ真っ直ぐに見据える。",
        "example": "Scientific research is constantly pushing the frontiers of human knowledge.",
        "deep_dive": {
            "roots": [{"term": "bhren-", "meaning": "to project, stand out"}],
            "points": ["front（正面）や confront（対峙する）と同類。体当たりで挑む場所。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "voyage_unseen",
        "word": "Voyage",
        "meaning": "航海、長旅、人生の旅路",
        "era": "13th Century Old French/Latin viaticum",
        "etymology": {
            "components": ["via (way, road)", "viaticum (provisions for a journey)"],
            "original_statement": "From Old French voiage, from Latin viaticum (a journey, also the money/provisions for a journey), from via (road, way)."
        },
        "concept": "What you need for the road (道（旅路）の上で必要なもの、その行為)",
        "thinking": "ただの短期的な旅行（trip）ではなく、十分な準備と覚悟（viaticum）を伴う「長大かつ未知への旅」。語源の「道（via）」が示すように、定まったゴールよりも、その「プロセスそのもの」に重きを置く言葉。波を越え、星を読み、人生という大きな海を渡り続けること。",
        "aftertaste": "地図なき航海へ。持てるものすべてを携えて、ただ道を行け。",
        "example": "The great explorer set out on a long voyage to find the South Pole.",
        "deep_dive": {
            "roots": [{"term": "wegh-", "meaning": "to move, go, ride"}],
            "points": ["way（道）や vehicle（乗り物）と同類。常に動いている生命の姿。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "vision_unseen",
        "word": "Vision",
        "meaning": "視力、視覚、洞察力、将来への展望",
        "era": "13th Century Old French/Latin videre",
        "etymology": {
            "components": ["videre (to see)"],
            "original_statement": "From Old French vision, from Latin visionem (the act of seeing, a sight, thing seen), from visus, past participle of videre (to see)."
        },
        "concept": "The act of seeing truly (真実を「見る」こと、見えている景色)",
        "thinking": "物理的な目ではなく、「心の目」で見ている景色。まだ形になっていない未来を、あたかも目の前に存在するように鮮明に描き出せる（videre）能力。それが洞察力（insight）であり、リーダーシップ（visionary）の源泉です。真に「見る」ことは、明日を創ることと同じなのです。",
        "aftertaste": "まだそこにないものを、誰よりも強く見つめ、現実に召喚せよ。",
        "example": "A true leader must possess a clear vision for the long-term future of the team.",
        "deep_dive": {
            "roots": [{"term": "weid-", "meaning": "to see, know"}],
            "points": ["wise（賢い）や wit（知恵）と同じルーツ。知ることは、見ること。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "horizon_unseen",
        "word": "Horizon",
        "meaning": "地平線、水平線、視野の限界",
        "era": "14th Century Old French/Greek horizein",
        "etymology": {
            "components": ["horos (boundary, limit)"],
            "original_statement": "From Old French orizon, from Latin horizon, from Greek horizon (kyklos) (limiting circle), from horizein (separate, divide, bound)."
        },
        "concept": "A limiting circle (世界を区切る、究極の境界の輪)",
        "thinking": "地上（あるいは海上）で視線が届く限界の「境界線（horos）」のこと。それは、今の自分にとっての「世界の終わり」であり、同時に新しい世界への「入り口」でもあります。そこを目指して進めば、地平線もまた遠ざかり、あなたの世界は無限に拡張され続けてゆく。",
        "aftertaste": "追いかけても届かない。けれど、そこがあるからこそ、歩みは止まらない。",
        "example": "As we sailed further south, new stars appeared on the dark horizon.",
        "deep_dive": {
            "roots": [{"term": "wer-", "meaning": "to cover, protect, enclose (possible)"}],
            "points": ["horoscope（星占い：時horoを見るscopy）の horo とは別ですが、境界線として。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "discovery_unseen",
        "word": "Discovery",
        "meaning": "発見、発見されたもの",
        "era": "14th Century Old French/Latin de- + discooperire",
        "etymology": {
            "components": ["dis- (opposite of)", "couvrir (to cover)"],
            "original_statement": "From Old French descovrir (uncover), from Late Latin discooperire, from dis- (reversal prefix) + cooperire (to cover over)."
        },
        "concept": "To take away the cover (「覆い」を取り去り、隠されていたものを現すこと)",
        "thinking": "何かをゼロから作り出す（invent）のではなく、最初から「そこにあったけれど、隠されていたもの（cover）」の覆い（dis-）を剥ぎ取り、その姿を露わにすること。世界は最初から驚異に満ちている。ただ私たちは、それを見つけるための手を、まだ伸ばしていないだけなのです。",
        "aftertaste": "あなたの足元にさえ。ただ覆いを取り去るだけで、宇宙が顔を出す。",
        "example": "The discovery of gravity changed our fundamental understanding of the universe forever.",
        "deep_dive": {
            "roots": [{"term": "wer-", "meaning": "to cover"}],
            "points": ["cover（覆う）と同じ。それを反転させるエキサイティングな行為。"]
        },
        "part_of_speech": "noun"
    }
]

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
    if match:
        prefix = match.group(1)
        json_array_str = match.group(2)
        suffix = match.group(3)
        
        words = json.loads(json_array_str)
        existing_ids = {w.get("id") for w in words}
        
        added_count = 0
        for item in word_batch:
            if item["id"] not in existing_ids:
                words.append(item)
                added_count += 1
                
        new_json_str = json.dumps(words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Success: Added {added_count} words.")
    else:
        print("Error: Could not find WORDS array in data.js.")
except Exception as e:
    print(f"Error: {e}")
