import json
import re

word_batch = [
    # Cycle 83: Transition & Threshold
    {
        "id": "threshold_transition",
        "word": "Threshold",
        "meaning": "敷居、入り口、境界、(刺激の)閾値",
        "era": "Old English threscan + fald",
        "etymology": {
            "components": ["threscan (to thresh, beat)", "fald (fold, floor)"],
            "original_statement": "From Old English threscold, related to threscan (to thresh, beat) + fald (floor, fold), originally the place where grain was threshed."
        },
        "concept": "Treading floor (脱穀のために足で「踏みつける（thresh）」場所、そこから一歩踏み出す境界線)",
        "thinking": "二つの世界の境界線。かつては脱穀をするための床であり、そこを踏み越えることは新しいステージへの突入を意味しました。肉体的な痛みや、知的な限界（閾値）を越える瞬間。そこは、過去の自分が解体され、新しい自分が再構成されるための一時的な停滞と飛躍の場所です。",
        "aftertaste": "最初の一歩。靴底に伝わるその感触が、あなたの運命を永遠に分かつ境界線となる。",
        "example": "She stood on the threshold of a brilliant career in international law.",
        "deep_dive": { "roots": [{"term": "ter-", "meaning": "to rub, turn"}], "points": ["thresh（脱穀する）は摩擦のルーツ。境界線は、常に葛藤（こすれ合い）を孕んでいる。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "liminal_transition",
        "word": "Liminal",
        "meaning": "境界の、中間段階の、どちらともつかない",
        "era": "19th Century Latin limen",
        "etymology": {
            "components": ["limen (threshold, cross-piece)"],
            "original_statement": "From Latin limen (threshold, lintel)."
        },
        "concept": "On the threshold (「敷居（threshold）」の上に立っている、宙吊りの状態)",
        "thinking": "前の部屋を離れたが、まだ次の部屋に入っていない、その「あいだ」の不確かな空間。それは「所属」を失う恐怖であると同時に、まだ何者でもないという究極の自由を意味します. 人生の変革期に訪れる、あわいに漂うような感覚。そこは、もっとも魔法が起きやすい聖域です。",
        "aftertaste": "あわいの時間。どちらでもなく、どこでもない場所にいるとき、あなたは初めて自分自身の本当の形を見る。",
        "example": "The period between leaving high school and starting university is a liminal space of growth.",
        "deep_dive": { "roots": [{"term": "lei-", "meaning": "to bend, incline (possible)"}], "points": ["limit（限界）や eliminate（排除する：敷居の外に出す）と同じルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "passage_transition",
        "word": "Passage",
        "meaning": "通路、一節、(時の)経過、移り変わり",
        "era": "13th Century Old French/Latin passus",
        "etymology": {
            "components": ["passus (step, pace)"],
            "original_statement": "From Old French passage, from passer (to pass), from Latin passus (step, pace)."
        },
        "concept": "A series of steps (一歩一歩「歩み（step）」を重ね、向こう側へ抜けていくこと)",
        "thinking": "点から点への瞬間的な移動ではなく、自らの足で歩みを進める「プロセス」としての時間や空間。本の「一節」もまた、物語という広大な空間を一歩ずつ進むための足跡です。時という「通路」を通り抜けることで、私たちはいつの間にか別の自分へと変貌を遂げています。",
        "aftertaste": "歩みの集積。あなたは今、この瞬間も、昨日とは違う自分へと続く長い廊下を歩いている。",
        "example": "The passage of time has a way of healing even the deepest emotional wounds.",
        "deep_dive": { "roots": [{"term": "pete-", "meaning": "to spread, stretch"}], "points": ["pace（歩調）や pass（合格する/通り過ぎる）と同じ、前進のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "metamorphosis_transition",
        "word": "Metamorphosis",
        "meaning": "変容、変態、劇的な変化",
        "era": "16th Century Greek meta- + morphe",
        "etymology": {
            "components": ["meta- (change)", "morphe (form, shape)"],
            "original_statement": "From Latin metamorphosis, from Greek metamorphosis (a transforming), from meta- (change) + morphe (form, shape)."
        },
        "concept": "Change of form (「形（shape）」を根本から「変える（change）」こと)",
        "thinking": "表面的な修正ではなく、芋虫が蝶になるように、その存在の「形（morphe）」が全く新しい次元へと移行すること. 以前の自分を一度解体し、再構築し、過去の殻を脱ぎ捨てるような飛躍。それは静止することへの拒絶であり、無限の自己更新のプロセスです。(重複を避けつつ深掘り)",
        "aftertaste": "脱ぎ去る。昨日までの私が、新しい私を迎え入れる。その劇的な境界線上の命。",
        "example": "Kafka's 'The Metamorphosis' explores the psychological impact of radical isolation and physical change.",
        "deep_dive": { "roots": [{"term": "mer-", "meaning": "to shine, sparkle (possible)"}], "points": ["morphology（形態学）や amorphous（無定形の：形のない）と同じ『形』のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "culmination_transition",
        "word": "Culmination",
        "meaning": "最高潮、絶頂、終着点",
        "era": "17th Century Latin culmen",
        "etymology": {
            "components": ["culmen (summit, peak, top)"],
            "original_statement": "From Latin culmen (top, summit, peak, roof), related to columen (pillar)."
        },
        "concept": "The highest peak (「頂上（peak）」に達し、すべてが一つに結実すること)",
        "thinking": "コツコツと積み上げてきた努力や時間が、ついにその「頂（いただき）」へと到達し、最も純粋な形として顕現する瞬間。それは終わりであると同時に、これまでの全プロセスを肯定する祝福です. すべての「一歩」は、この最高潮の瞬間のためにあったのだという深い納得感。",
        "aftertaste": "頂からの眺め。長く険しい道のりさえも、今はただ美しく輝く一筋の軌跡に見える。",
        "example": "The successful launch was the culmination of years of hard work and dedication.",
        "deep_dive": { "roots": [{"term": "kel-", "meaning": "to rise, be high"}], "points": ["column（柱）や hill（丘）、excell（卓越する）と同じ『高み』のルーツ。"] },
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
        print(f"Success: Added {added} words in Cycle 83.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
