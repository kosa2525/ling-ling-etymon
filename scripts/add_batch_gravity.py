import json
import re

word_batch = [
    # Cycle 106: Gravity & Weight
    {
        "id": "gravity_weight",
        "word": "Gravity",
        "meaning": "重力、引力、真剣さ、重大さ",
        "era": "16th Century Latin gravis",
        "etymology": {
            "components": ["gravis (heavy)"],
            "original_statement": "From Middle French gravite, from Latin gravitatem (weight, heaviness, pressure), from gravis (heavy, weighty, burdened, pregnant)."
        },
        "concept": "State of being heavy (「重たい（heavy）」こと、万物を中心へと引き寄せる不可抗力的な「重み」)",
        "thinking": "ただの物理法則ではなく、物事の「重大さ」や、人が何かに真剣に向き合うときの「厳粛さ」そのもの. 語源の gravis は、妊娠（pregnant）している重みをも意味しました。それは、新しい命や価値を孕んでいるがゆえの、心地よくも厳しい重圧です。浮ついた心を地面に繋ぎ止める、魂の重石。",
        "aftertaste": "清冽なる重み。あなたが背負っているその責任は、あなたがこの世界で、確かな足取りで歩むための導きとなる。",
        "example": "We slowly began to understand the full gravity of the situation.",
        "deep_dive": { "roots": [{"term": "gweru-", "meaning": "heavy"}], "points": ["grave（墓：重い場所）や grieve（悲しむ：重荷を感じる）と同じ、存在の重さ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "gravitas_weight",
        "word": "Gravitas",
        "meaning": "威厳、重厚さ、落ち着き",
        "era": "Latin gravis",
        "etymology": {
            "components": ["gravis (heavy)"],
            "original_statement": "From Latin gravitas (weight, heaviness, dignity, presence), from gravis (heavy)."
        },
        "concept": "Dignified weight (品格を伴った性格の「重み（weight）」、周囲を沈黙させる「存在感（presence）」)",
        "thinking": "軽薄さを排し、自分の言葉と行動に責任を持つ大人の「落ち着き」. 語源はローマ時代の美徳の一つで、困難な状況でも動じない、精神の揺るぎなさを指します。それは、長年の経験と深い思索によって磨かれた、沈黙そのものが雄弁に語り出すような、静かなる迫力です。",
        "aftertaste": "静かなる迫力。あなたが語らなくても、あなたの背中が、真実という名の重みを世界に示している。",
        "example": "The young leader spoke with a surprising amount of gravitas, commanding the room's attention.",
        "deep_dive": { "roots": [{"term": "gweru-", "meaning": "heavy"}], "points": ["aggravate（悪化させる：さらに重くする）と同じ、影響力のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "ponderous_weight",
        "word": "Ponderous",
        "meaning": "重苦しい、重厚な、退屈なほど重い",
        "era": "14th Century Latin pondus",
        "etymology": {
            "components": ["pondus (weight)"],
            "original_statement": "From Old French pondereus, from Latin ponderosus (of great weight), from pondus (weight, weightiness), from root of pendere (to hang, cause to hang, weigh)."
        },
        "concept": "Full of weight (あまりにも「重厚（weighty）」すぎて、動かすのに「労力（effort）」を要すること)",
        "thinking": "軽やかさとは無縁の、圧倒的な物質感. 語源の pendere は「吊るす」こと。天秤に吊るしたとき、ぐんと沈み込むその重みは、時に退屈や鈍重さを感じさせますが、同時に、決して流されない「歴史」や「伝統」の重みでもあります。軽薄な時代を押し留める、巨大な碇のような言葉です。",
        "aftertaste": "動かぬ重厚. 軽やかに舞うこともいいけれど、時にはその重苦しさに身を任せ、地の底の真実に触れていたい。",
        "example": "The book's ponderous style made it difficult to read, despite its important subject matter.",
        "deep_dive": { "roots": [{"term": "pend-", "meaning": "to hang, weigh"}], "points": ["ponder（熟考する：重さを量る）や depend（依存する：ぶら下がる）と同じ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "burden_weight",
        "word": "Burden",
        "meaning": "重荷、負担、(歌の)折り返し、要旨",
        "era": "Old English berthan",
        "etymology": {
            "components": ["berthan (to bear)"],
            "original_statement": "From Old English byrthen (load, weight, charge, duty), from Proto-Germanic burthinnia, from root of berthan (to bear)."
        },
        "concept": "What is borne (背中に負い、運ばなければならない「荷物（load）」、逃れられない「義務（duty）」)",
        "thinking": "自分以外の誰かや何かのために、自らの肩を貸し、共に歩むという決意の重さ. 語源は「運ぶこと」。それは痛みであると同時に、自分が誰かのために役立っているという、生きる手応えそのものでもあります。歌の折り返しを意味するのは、何度も繰り返される「主題」の重みからです。",
        "aftertaste": "愛する重荷。あなたがその荷を下ろさないのは、それがあなたを、この世界に繋ぎ止めている唯一の愛だからだ。",
        "example": "The responsibility of leadership can be a heavy burden to carry.",
        "deep_dive": { "roots": [{"term": "bher-", "meaning": "to carry"}], "points": ["birth（誕生：産み出す重み）や ferry（フェリー：運ぶもの）と同じ。生命の運搬。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "anchor_weight",
        "word": "Anchor",
        "meaning": "錨、支え、心の拠り所",
        "era": "Old English ancor",
        "etymology": {
            "components": ["ank- (to bend)"],
            "original_statement": "From Latin ancora, from Greek ankyra (anchor, hook), from PIE root ank- (to bend)."
        },
        "concept": "The bent hook (「曲がった鉤（hook）」を地の底に深く突き刺し、自分を「固定（fix）」すること)",
        "thinking": "激しい潮流の中でも、自分を見失わずに踏みとどまるための、最後の防衛線. 語源の ank- は「曲がること」。その粘り強さが、形のない水の上で、確かな「安定」を作り出します。あなたが困難な夜を越えるために、その心の一点を深く鎮（しず）める場所。それは信頼であり、愛であり、信念です。",
        "aftertaste": "深海の静寂。地の底にこの一点がある限り、どんな嵐が海面を揺らしても、あなたは決して流されることはない。",
        "example": "Her faith was an anchor for her during the darkest times of her life.",
        "deep_dive": { "roots": [{"term": "ank-", "meaning": "to bend"}], "points": ["angle（角度：曲がり）や ankle（足首）と同じ。柔軟でありながら、強い保持力。"] },
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
        print(f"Success: Added {added} words in Cycle 106.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
