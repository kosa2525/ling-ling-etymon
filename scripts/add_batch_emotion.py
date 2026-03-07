import json
import re

word_batch = [
    {
        "id": "nostalgia_kin",
        "word": "Nostalgia",
        "meaning": "郷愁、過去への憧れ、ノスタルジア",
        "era": "17th Century Modern Latin/Greek nostos + algos",
        "etymology": {
            "components": ["nostos (return home)", "algos (pain, grief)"],
            "original_statement": "Coined in 1688 by Swiss physician Johannes Hofer as a medical term for homesickness, from Greek nostos (homecoming) + algos (pain)."
        },
        "concept": "The pain of returning home (帰郷への疼き、切ない想い)",
        "thinking": "もともとは、故郷から遠く離れて戦う兵士たちが患う「病気（homesickness）」として医学的に定義された言葉です。「家へと帰ること（nostos）」への、喉を掻きむしるような「痛み（algos）」。それは、二度と戻れない過去や場所に対する、甘く、そして鋭い心の疼きです。",
        "aftertaste": "今はもうない、あの光の場所へ。心だけが時を遡る。",
        "example": "Looking at old school photos often triggers a sense of nostalgia.",
        "deep_dive": {
            "roots": [{"term": "nes-", "meaning": "to return home safely"}, {"term": "alghi-", "meaning": "to hurt"}],
            "points": ["Odyssey（オデッセイ）の主題である『帰還（nostos）』が語源の核です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "empathy_kin",
        "word": "Empathy",
        "meaning": "共感、感情移入",
        "era": "20th Century Greek en + pathos",
        "etymology": {
            "components": ["en- (in)", "pathos (feeling)"],
            "original_statement": "Coined in 1908 as a translation of German Einfühlung (feeling into), from Greek en- (in) + pathos (feeling)."
        },
        "concept": "Feeling into another (他者の「中」に入って感じること)",
        "thinking": "同情（Sympathy：共に感じる）よりも一歩踏み込み、相手の心という器の「中（en-）」に自らを滑り込ませ、相手の「痛みや喜び（pathos）」を自分のこととして再体験すること。美学用語から心理学用語へと発展した、他者と魂を重ね合わせるための高度な能力です。",
        "aftertaste": "境界線が消える。あなたの涙が、私の頬を伝う。",
        "example": "Empathy is essential for building strong, supportive communities.",
        "deep_dive": {
            "roots": [{"term": "kwent-", "meaning": "to suffer, endure"}],
            "points": ["pathos（情熱/苦痛）は、受け身の『耐える』という感覚が根底にあります。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "influence_kin",
        "word": "Influence",
        "meaning": "影響(力)、感化、及ぼす",
        "era": "14th Century Old French/Latin influere",
        "etymology": {
            "components": ["in- (into)", "fluere (to flow)"],
            "original_statement": "From Old French influence, from Medieval Latin influentia (a flowing in), from Latin influere (to flow into)."
        },
        "concept": "A flowing into (中へと流れ込む力)",
        "thinking": "占星術において、星々から「見えない力が人間に向かって流れ込んでくる（in-flow）」と考えられていたことに由来します。力ずくで動かすのではなく、水が浸透するように、相手の精神や行動の中に静かに、しかし確実に自分のエッセンスを染み込ませていく力のこと。",
        "aftertaste": "言葉や背中が、誰かの未来へと静かに注ぎ込まれてゆく。",
        "example": "The young musician was heavily influenced by the work of David Bowie.",
        "deep_dive": {
            "roots": [{"term": "bhleu-", "meaning": "to swell, gush, flow"}],
            "points": ["fluent（流暢な）や fluid（流体）と同じ、淀みのない流れのルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "dialogue_kin",
        "word": "Dialogue",
        "meaning": "対話、ダイアログ",
        "era": "12th Century Old French/Greek dialogos",
        "etymology": {
            "components": ["dia- (across, through)", "logos (word, reason)"],
            "original_statement": "From Old French dialogue, from Latin dialogus, from Greek dialogos (conversation, discourse), from dialegesthai (converse with)."
        },
        "concept": "Reason flowing through (言葉/理性が（二人の間を）通り抜けること)",
        "thinking": "「二人（di-）」という意味だと誤解されがちですが、本来は「通過して（dia-）」＋「言葉/理性（logos）」。二人の人間の間を、真理や意味が風のように通り抜けていくダイナミックなプロセス。一方が話す（ソロ）のではなく、言葉を橋にして二つの魂が連結される試みです。",
        "aftertaste": "言葉という橋を、意味が往復するたびに、新しい世界が生まれる。",
        "example": "The two countries opened a dialogue to resolve their border dispute.",
        "deep_dive": {
            "roots": [{"term": "leg-", "meaning": "to collect, speak"}],
            "points": ["logic（論理）と同じ logos が核。単なるお喋りではなく、理の交換です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "charity_kin",
        "word": "Charity",
        "meaning": "慈善、思いやり、チャリティ",
        "era": "12th Century Old French/Latin caritas",
        "etymology": {
            "components": ["carus (dear, precious, costly)"],
            "original_statement": "From Old French charité, from Latin caritas (costliness, high price, dearness, love), from carus (dear)."
        },
        "concept": "Treating something as dear (対象を『愛おしいもの』として扱うこと)",
        "thinking": "見返りを求める親切ではなく、対象を「かけがえのない、高価で大切なもの（dear）」として慈しむ心。ギリシャ語の「アガペー（無償の愛）」の訳語として定着しました。他者の存在そのものの価値を認め、そっと手を差し伸べる、静かで深い利他精神の極致。",
        "aftertaste": "あなたは尊い。その一言を、行動という形に変えて贈る。",
        "example": "She devoted her entire life to works of charity for the poor.",
        "deep_dive": {
            "roots": [{"term": "ka-", "meaning": "to desire, help"}],
            "points": ["caress（愛撫する）や cherish（慈しむ）と同じ『愛おしさ』の根源。"]
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
