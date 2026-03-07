import json
import re

word_batch = [
    # Cycle 105: Paradox & Multiplicity
    {
        "id": "paradox_multiplicity",
        "word": "Paradox",
        "meaning": "逆説、パラドックス、矛盾しているようで真実を突いた言葉",
        "era": "16th Century Greek para- + doxa",
        "etymology": {
            "components": ["para- (contrary to)", "doxa (opinion)"],
            "original_statement": "From Latin paradoxum, from Greek paradoxon (contrary to expectation, incredible), from para- (contrary to) + doxa (opinion)."
        },
        "concept": "Contrary to opinion (一般的な「常識（opinion）」に「反して（contrary）」いるが、そこに深い真実があること)",
        "thinking": "一見、不合理で矛盾しているように見えるけれど、その矛盾を受け入れたときにだけ立ち現れる、より高次元の真実. 語源の doxa は、人々の思い込みとしての「意見」。真理は、私たちの小さな期待を裏切り、矛盾という名の鎧（よろい）をまとって現れます。急がば回れ、負けるが勝ち、といった深淵な智慧です。",
        "aftertaste": "矛盾の美学。反対のものを同時に抱きしめたとき、あなたの魂は、世界の複雑さをそのまま愛せるようになる。",
        "example": "The idea that less is more is a classic paradox of modern minimalist design.",
        "deep_dive": { "roots": [{"term": "deic-", "meaning": "to show, pronounce (possible for doxa)"}], "points": ["dogma（教義）や orthodox（正統な）と同じ。思い込みを超える視座。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "ambivalence_multiplicity",
        "word": "Ambivalence",
        "meaning": "両義性、ためらい、相反する感情が共存すること",
        "era": "20th Century Latin ambi- + valentia",
        "etymology": {
            "components": ["ambi- (both)", "valentia (strength)"],
            "original_statement": "Coined in German as Ambivalenz by psychologist Eugen Bleuler, from Latin ambi- (both) + valentia (strength)."
        },
        "concept": "Strength in both (「両方（both）」の感情が同じ「強さ（strength）」で綱引きをしている状態)",
        "thinking": "愛しているけれど憎い、去りたいけれど留まりたい. どちらかが偽物なのではなく、どちらも本気であるからこそ引き裂かれる、人間らしい心の葛藤。語源の valentia は「力」。二つの力が拮抗（きっこう）するその「宙ぶらりん」の場所で、私たちは自分の心の多層性と出会うことになります。",
        "aftertaste": "揺れる天秤。白黒つけられないそのグレーゾーンの中に、あなたの魂の最も純粋な震えが隠されている。",
        "example": "She felt a deep ambivalence towards her promotion, as it meant less time with her children.",
        "deep_dive": { "roots": [{"term": "ambhi-", "meaning": "around, both"}, {"term": "wal-", "meaning": "to be strong"}], "points": ["value（価値）や prevail（打ち勝つ）と同じ。矛盾した価値の共存。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "myriad_multiplicity",
        "word": "Myriad",
        "meaning": "無数、星の数ほどの、一万",
        "era": "16th Century Greek myrias",
        "etymology": {
            "components": ["myrias (ten thousand, a countless number)"],
            "original_statement": "From Greek myrias (number of ten thousand), from myrios (countless, infinite)."
        },
        "concept": "Ten thousand (「一万（ten thousand）」という具体的な数を超えた、気が遠くなるほどの「無限（infinite）」)",
        "thinking": "数えきれないほどの星、数えきれないほどの可能性、数えきれないほどの命. 語源もともとは「一万」を指す最大の単位でした。人間が把握できる限界を超えた、圧倒的な豊穣（ほうじょう）さ。世界は、あなたが思っているよりも遥かに多くの選択肢と、色彩に満ちています。",
        "aftertaste": "無限の選択肢. 一億の光。あなたは、その無数の選択肢のなかから、自分だけのたった一つの光を選び取っていく。",
        "example": "The city offers a myriad of opportunities for young professionals in every field.",
        "deep_dive": { "roots": [{"term": "meu-", "meaning": "damp, many (possible root)"}], "points": ["具体数から無限へ. 言葉が知性の限界を押し広げた例。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "plurality_multiplicity",
        "word": "Plurality",
        "meaning": "複数、多様性、(選挙などの)得票数第一位、大多数",
        "era": "14th Century Latin plus",
        "etymology": {
            "components": ["plus (more)"],
            "original_statement": "From Old French pluralite, from Latin pluralitatem (multiplicity, plurality), from plus (more)."
        },
        "concept": "Being more (単一（one）ではなく、「もっと多い（more）」こと、共存する多くの存在)",
        "thinking": "世界は唯一の解に向かうのではなく、異なる多くの意見や存在が「複数（Plural）」であること自体に価値があるという考え方. 語源の plus は「さらに多く」。一つの中心があるのではなく、分散した多くの輝き。それは、他者を消し去ることなく、共存させようとする、成熟した文明の眼差しです。",
        "aftertaste": "響き合う他者。あなたが一人でいないということ、それは世界が、より豊かな和音を求めているということだ。",
        "example": "The legal system must respect the plurality of cultures within our modern society.",
        "deep_dive": { "roots": [{"term": "pleu-", "meaning": "to flow, many"}], "points": ["plus（プラス）や surplus（余剰：より多く超えるもの）と同じ。溢れ出す豊かさ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "dichotomy_multiplicity",
        "word": "Dichotomy",
        "meaning": "二分法、対立、真っ二つに分かれること",
        "era": "16th Century Greek dicha- + tomos",
        "etymology": {
            "components": ["dicha- (in two, asunder)", "tomos (cutting)"],
            "original_statement": "From Greek dichotomia (a cutting in two), from dicha- (in two) + temnein (to cut)."
        },
        "concept": "Cutting in two (全体を「真っ二つ（in two）」に「切り分け（cutting）」、対比を鮮明にすること)",
        "thinking": "光と影、善と悪、男と女. 複雑な現実を理解するために、敢（あ）えて刀を入れて二つの対立軸に分けること。語源の tomos は切断。その切れ味の鋭さゆえに、世界は明快に見えますが、同時に、切り捨てられた「境界線」にこそ、真実が隠されていることも忘れてはなりません。",
        "aftertaste": "鋭い境界線。分けることで見えるものがあり、分けないことで守られるものがある。あなたは今、どちらの視点を求めているだろうか。",
        "example": "There is a false dichotomy between the arts and the sciences; both require creativity.",
        "deep_dive": { "roots": [{"term": "tem-", "meaning": "to cut"}], "points": ["anatomy（解剖：切り分けること）や atom（原子：切れないもの）と同じ、分析の極致。"] },
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
        print(f"Success: Added {added} words in Cycle 105.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
