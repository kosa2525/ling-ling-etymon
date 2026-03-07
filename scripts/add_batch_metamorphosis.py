import json
import re

word_batch = [
    # Cycle 73: Metamorphosis & Change
    {
        "id": "metamorphosis_change",
        "word": "Metamorphosis",
        "meaning": "変容、変態、劇的な変化",
        "era": "16th Century Greek meta- + morphe",
        "etymology": {
            "components": ["meta- (change, after)", "morphe (form, shape)"],
            "original_statement": "From Latin metamorphosis, from Greek metamorphosis (a transforming, a transformation), from meta- (change) + morphe (form, shape)."
        },
        "concept": "Change of form (「形（form）」を根本から「変える（change）」こと)",
        "thinking": "表面的な修正ではなく、芋虫が蝶になるように、その存在の「形（morphe）」が全く新しい次元へと移行すること。以前の自分を一度解体し、再構築し、過去の殻を脱ぎ捨てるような、痛みを伴うが美しい飛躍。それは静止することへの拒絶であり、無限の自己更新のプロセスです。",
        "aftertaste": "脱ぎ去る。昨日までの私が、新しい私を迎え入れる。その劇的な境界線上の命。",
        "example": "Kafka's 'The Metamorphosis' explores the psychological impact of radical isolation and physical change.",
        "deep_dive": { "roots": [{"term": "mer-", "meaning": "to shine, sparkle (possible)"}], "points": ["morphology（形態学）や amorphous（無定形の：形のない）と同じ『形』のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "volatile_change",
        "word": "Volatile",
        "meaning": "不安定な、揮発性の、変わりやすい",
        "era": "16th Century French/Latin volare",
        "etymology": {
            "components": ["volare (to fly)"],
            "original_statement": "From French volatile, from Latin volatilis (flying), from volare (to fly)."
        },
        "concept": "Likely to fly off (今にも空へと「飛び去り（fly）」そうな、定まらぬ危うさ)",
        "thinking": "地に足をつけず、一瞬で蒸発（変換）してしまうような性質。ただの「気まぐれ」ではなく、周囲の熱や圧力に対してあまりに敏感に反応しすぎ、一瞬で形や位置を失ってしまうさま。その不安定さは恐怖の対象ですが、同時にこの停滞した世界に「閃き」という波紋を起こす、高エネルギーの源泉でもあります。",
        "aftertaste": "捕まえる。けれど、次の瞬間にはもう、あなたの指を抜けてどこかへ消えている。",
        "example": "The political situation in the region remains highly volatile and unpredictable after the recent coup.",
        "deep_dive": { "roots": [{"term": "gwel-", "meaning": "to fly, move (possible)"}], "points": ["volley（バレー：飛び交い）や velocity（速度：空を飛ぶ速さ）と同じ『翔び』の精神。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "transition_change",
        "word": "Transition",
        "meaning": "移行、移り変わり、過渡期",
        "era": "15th Century Old French/Latin trans- + ire",
        "etymology": {
            "components": ["trans- (across, beyond)", "ire (to go)"],
            "original_statement": "From Latin transitionem (a going over, a passing), from trans- (across) + ire (to go)."
        },
        "concept": "A going across (境界を「越え（across）」て、向こう側へ「行く（go）」こと)",
        "thinking": "一つの部屋から別の部屋へ移動（歩行）するように、ある状態を脱して次のフェーズへと染み出していくプロセス。それは目的値への到達よりも、その「間（あいだ）」という不安定で不確かな道のりを意味します。境界線そのものの上にいるとき、意識はもっとも拡張されています。",
        "aftertaste": "あわいに立つ。もう以前の場所には戻れず、まだ次の場所には馴染めていない、静かな宙吊り。",
        "example": "He found the transition from academic studies to his new job challenging but rewarding.",
        "deep_dive": { "roots": [{"term": "ei-", "meaning": "to go"}], "points": ["exit（出口）や initial（始まり：中に踏み出したところ）と同じ『歩み』のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "transmute_change",
        "word": "Transmute",
        "meaning": "変質させる、(錬金術で)変成する、高める",
        "era": "15th Century Middle French/Latin trans- + mutare",
        "etymology": {
            "components": ["trans- (change thoroughly)", "mutare (to change, move)"],
            "original_statement": "From Latin transmutare (change, shift), from trans- (over, beyond) + mutare (to change)."
        },
        "concept": "Changing completely beyond (「変化（mute）」させて、全く別の「向こう側（beyond）」へ至ること)",
        "thinking": "ただの変更ではなく、錬金術（alchemy）のように鉛を金に変える、本質的な「価値の転換」を指す言葉。悲しみを芸術に、怒りを情熱に。それは自分の内側にある重たい材料を使い、より輝かしく、より価値ある魂の形へと昇華させるための、創造的な化学反応です。",
        "aftertaste": "あなたの人生の苦しみも。いつか、眩しく輝く黄金へと姿を変えるために、今その熱に焼かれている。",
        "example": "The great artist can transmute their personal suffering into universal beauty and inspiration.",
        "deep_dive": { "roots": [{"term": "mei-", "meaning": "to change, exchange"}], "points": ["mutation（突然変異）や immutable（不変の）と同じ『交換可能な変化』の魔法。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "malleable_change",
        "word": "Malleable",
        "meaning": "(金属が)可鍛性の、(心が)素直な、順応性のある",
        "era": "14th Century Old French/Latin malleus",
        "etymology": {
            "components": ["malleus (hammer)"],
            "original_statement": "From Old French malleable, from Latin malleus (hammer)."
        },
        "concept": "Able to be hammered (「ハンマー（malleus）」で叩かれても、壊れずに、形を自由に変えられる性癖)",
        "thinking": "打ちのめ（打た）されても、砕け散ることなく、柔軟に形を変えて耐え抜くこと。それは弱さではなく、剛直すぎるがゆえに折れてしまう「硬さ」を超えた、しなやかで強靭な受容性です。人生の打撃一つひとつに応じて、より洗練された器（かたち）へと自分を変えていける、希望に満ちた性質。",
        "aftertaste": "打たれるたびに。あなたは、より強く、よりしなやかな、美しい器へと成形されていく。",
        "example": "Children's young minds are extremely malleable and can be influenced by their environment.",
        "deep_dive": { "roots": [{"term": "mel-", "meaning": "soft"}], "points": ["mallet（木槌）や melt（溶ける）、mellow（熟した：柔らかい）と同じ『柔軟』のルーツ。"] },
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
        print(f"Success: Added {added} words in Cycle 73.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
