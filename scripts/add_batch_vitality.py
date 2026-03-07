import json
import re

word_batch = [
    # Cycle 89: Vitality & Spirit
    {
        "id": "vitality_spirit",
        "word": "Vitality",
        "meaning": "生命力、活力、活気",
        "era": "16th Century Latin vita",
        "etymology": {
            "components": ["vita (life)"],
            "original_statement": "From Latin vitalitatem (vital force, life), from vitalis (pertaining to life), from vita (life)."
        },
        "concept": "The power of life (生きることそのものが持つ、根源的な「力（force）」)",
        "thinking": "単に「生きている」という状態を超えて、内側から溢れ出し、周囲を巻き込んでいくような能動的なエネルギー. 語源は「命（life）」。それは心臓を動かし、傷を癒し、困難に立ち向わせる「熱」の源泉です。存在することの喜びが、そのまま力へと変換された状態。",
        "aftertaste": "脈打つ光。あなたの内側にあるその熱は、宇宙が誕生した瞬間の火花と、今も繋がっている。",
        "example": "Despite her age, she possesses a remarkable vitality that inspires everyone around her.",
        "deep_dive": { "roots": [{"term": "gwei-", "meaning": "to live"}], "points": ["vivid（鮮やかな）や vivify（活気づける）と同じ、躍動する生のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "animation_spirit",
        "word": "Animation",
        "meaning": "活気、動画、生命の吹き込み",
        "era": "16th Century Latin anima",
        "etymology": {
            "components": ["anima (breath, soul, life)"],
            "original_statement": "From Latin animationem (a bestowing of life), from animatus, past participle of animare (to give life to), from anima (breath, soul, life)."
        },
        "concept": "Giving breath (「息（breath）」を吹き込み、魂を宿らせて「動かす」こと)",
        "thinking": "静止していたものに、温かな吐息を吹き込み、自分の意志で動き出させること. 語源の anima は「魂（Soul）」でもあります。アニメーションとは、単なる技術ではなく、物質に命を吹き込もうとする、私たちの切実な祈りの形なのです。",
        "aftertaste": "動き出す影。あなたの情熱が触れるとき、冷たい世界は息を吹き返し、躍動を始める。",
        "example": "She spoke with great animation, her eyes sparkling as she described her travels.",
        "deep_dive": { "roots": [{"term": "ane-", "meaning": "to breathe"}], "points": ["animal（動物：息づくもの）や animism（アニミズム）と同じ、生命の息吹。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "enthuasiam_spirit",
        "word": "Enthusiasm",
        "meaning": "熱狂、熱意、情熱",
        "era": "16th Century Greek en- + theos",
        "etymology": {
            "components": ["en- (in)", "theos (god)"],
            "original_statement": "From Greek enthousiasmos (divine inspiration, enthusiasm), from enthousiazein (to be inspired by a god), from enthous (inspired, possessed by a god), from en- (in) + theos (god)."
        },
        "concept": "God within (自分の内側に「神（god）」を「宿して（in）」いるかのような、忘我の熱狂)",
        "thinking": "外からの刺激に反応するのではなく、自分の内側にある「超越的な何か」に突き動かされている状態. それは一種の予言的なトランス状態であり、自分を超えた大きな力が自分を通して流れている感覚です。情熱とは、自分の中に神聖な火を灯し続けることなのです。",
        "aftertaste": "宿る炎。あなたはもう、自分一人の力で走っているのではない。神聖な風が、背中を押している。",
        "example": "The audience responded with great enthusiasm to the musician's virtuoso performance.",
        "deep_dive": { "roots": [{"term": "dhes-", "meaning": "root of words for religious concepts"}], "points": ["theory（理論：神を見ること）や theology（神学）と同じ、高みへの接続。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "elan_spirit",
        "word": "Elan",
        "meaning": "鋭気、活気、熱情",
        "era": "19th Century French elancer",
        "etymology": {
            "components": ["e- (out)", "lancer (to hurl, throw a lance)"],
            "original_statement": "From French élan (momentum, rush), from élancer (to hurl, fling, dart), from é- (out) + lancer (to hurl, throw a lance)."
        },
        "concept": "Hurling forth (「槍（lance）」を「投げ放つ（hurl）」ような、鋭く力強い前進)",
        "thinking": "ただの「速さ」ではなく、明確な意志と美学を持って、一点を突破しようとする鋭い躍動感. 語源の lancer は、騎士が槍を放つ動作です。迷いを断ち切り、自分という全存在を目的へと投げ出す瞬間の、閃光のような鮮やかさと力強さ。",
        "aftertaste": "放たれた矢。迷いはもうない。あなたの全存在は、今、その一点へと鋭く突き進んでいる。",
        "example": "The orchestra played the final movement with incredible élan and precision.",
        "deep_dive": { "roots": [{"term": "Unknown source for lancia"}], "points": ["lance（槍）と同じルーツ。生きることは、常に何かを射抜こうとする挑戦である。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "sprightly_spirit",
        "word": "Sprightly",
        "meaning": "陽気な、活発な、元気に満ちた",
        "era": "16th Century English sprite",
        "etymology": {
            "components": ["sprite (spirit, elf, fairy)"],
            "original_statement": "From sprite + -ly, from spiritus (breath, spirit)."
        },
        "concept": "Like a spirit (妖精や「精霊（spirit）」のように、軽やかで不思議な生命力に満ちていること)",
        "thinking": "重力に縛られた肉体の重さを感じさせない、羽が生えたような軽妙な活気. 語源の sprite は、目に見えないが確かに世界を動かしている「精霊」を指します。老化や疲労を寄せ付けない、魂のみずみずしさが外側に溢れ出した、いたずらっぽくも気高いエネルギーです。",
        "aftertaste": "軽やかな跳躍。日常の重みのなかで、あなたの心だけは、精霊のように自由に踊り続けている。",
        "example": "The sprightly old man danced with his granddaughter at the wedding party.",
        "deep_dive": { "roots": [{"term": "speies-", "meaning": "to breathe"}], "points": ["spirit（精神）や sprite（小妖精）と同じ『息』の変奏曲。生の軽やかさ。"] },
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
        print(f"Success: Added {added} words in Cycle 89.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
