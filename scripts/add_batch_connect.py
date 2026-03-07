import json
import re

word_batch = [
    # Cycle 75: Connection & Unity
    {
        "id": "nexus_connect",
        "word": "Nexus",
        "meaning": "結びつき、連結、中心、核心",
        "era": "17th Century Latin nectere",
        "etymology": {
            "components": ["nectere (to bind, tie)"],
            "original_statement": "From Latin nexus (a binding, connection), past participle of nectere (to bind, tie)."
        },
        "concept": "A binding point (物事が「結び（bind）」合わされる一点)",
        "thinking": "バラバラな要素が一つに束ねられ、新しい意味（中心）を生み出している場所。それは交通の要所（ハブ）であり、同時に、異なる知識や人々が出会って化学反応を起こす「核心（core）」でもあります。すべてがそこで繋がり、響き合い、動かされてゆく魔法の結び目のような存在です。",
        "aftertaste": "一点。そこを通らずには、何も繋がらない。静かなる引力の中心。",
        "example": "The city has always been the financial nexus of the entire region for decades.",
        "deep_dive": { "roots": [{"term": "ned-", "meaning": "to bind, tie"}], "points": ["connect（繋ぐ：一緒に結ぶ）や annex（別館：繋げられたもの）と同じ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "alliance_connect",
        "word": "Alliance",
        "meaning": "同盟、提携、協調",
        "era": "14th Century Old French/Latin ad- + ligare",
        "etymology": {
            "components": ["ad- (to)", "ligare (to bind)"],
            "original_statement": "From Old French aliance, from alier (to combine, unite), from Latin alligare (to bind to), from ad- (to) + ligare (to bind)."
        },
        "concept": "Binding to each other (互いに「縛り合い（lig-）」、一つの存在になること)",
        "thinking": "利害を超えて、より大きな目的のために「結びつく（alligare/ally）」こと. それは他者との「縛り（lig）」を、自ら進んで受け入れる行為です。共通の敵、あるいは共通の夢。一人の力では届かない場所に手を伸ばすための、生命の社会的な知恵の結晶といえます。",
        "aftertaste": "ほどかぬ約束。自らを縛ることで、一人は自由を超えた『力』を手に入れる。",
        "example": "The two small nations formed a strategic military alliance for mutual self-defense.",
        "deep_dive": { "roots": [{"term": "leig-", "meaning": "to bind"}], "points": ["religion（宗教：神と結び直す）や ligament（靱帯）と同じ、強固な結合。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "harmony_connect",
        "word": "Harmony",
        "meaning": "調和、和声、一致",
        "era": "14th Century Old French/Greek ar-",
        "etymology": {
            "components": ["ar- (to fit together)"],
            "original_statement": "From Old French harmonie, from Latin harmonia, from Greek harmonia (agreement, concord), related to harmos (joint), from root ar- (to fit together)."
        },
        "concept": "Fitting together (バラバラなパーツが「ぴったり（joint）」と重なること)",
        "thinking": "異なる音、異なる魂. それらがぶつかり合うのではなく、精緻なジグソーパズルのように完璧に「咬（か）み合った」瞬間の奇跡。語源の ar- は、大工仕事の「継ぎ目（joint）」を指します。世界は隙間なく、意味ある形で組み合わされているという、美しき秩序の表明です。",
        "aftertaste": "ノイズが消える。完璧な継ぎ目の向こう側に、一つの大きな歌が聞こえてくる。",
        "example": "The colors in her painting were in perfect harmony with the peaceful forest scenery.",
        "deep_dive": { "roots": [{"term": "ar-", "meaning": "to fit together"}], "points": ["art（芸術：合わせる技術）や arithmetic（算術）と同じ、理知的で緻密な結合。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "solidarity_connect",
        "word": "Solidarity",
        "meaning": "結束、連帯、一致団結",
        "era": "18th Century French/Latin solidus",
        "etymology": {
            "components": ["solidus (whole, firm, solid)"],
            "original_statement": "From French solidarité, from solidaire (interdependent), from Latin solidus (whole, firm, solid)."
        },
        "concept": "Making a solid whole (個が溶け合い、一つの「硬い塊（solid）」になること)",
        "thinking": "ただ一緒にいるのではなく、他者の痛みや喜びを「自分自身の重み」として共有し、一欠片の欠けもない一つの「確固たる全体（solidus）」として機能すること。それは、個人の脆弱さを集合の「強固さ」へ、そして共通の運命へと昇華させる、崇高な連帯感です。",
        "aftertaste": "一人ではない。あなたの足跡は、誰かの孤独を埋めるための一つの欠かせない土台。",
        "example": "The workers showed their solidarity by going on strike for better working conditions.",
        "deep_dive": { "roots": [{"term": "sol-", "meaning": "whole"}], "points": ["solid（確かな/立体）や solo（独奏：それ自体で完全なもの）と同じ『全体』。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "tether_connect",
        "word": "Tether",
        "meaning": "つなぎ縄、範囲、限界",
        "era": "14th Century Scandinavian/Old Norse tjóðr",
        "etymology": {
            "components": ["tjóðr (rope, band)"],
            "original_statement": "From Middle English teder, from a Scandinavian source (like Old Norse tjóðr)."
        },
        "concept": "A rope for limit (どこへも行けないように「繋ぎ止める」ための縄、その限界点)",
        "thinking": "家畜を繋ぎ止めておくための「引き綱（rope）」。それは保護であると同時に「移動の限界」をも意味します。思考のテザー、あるいは関係性のテザー。「これ以上先にはいけない」という限界点（end of one's tether）を感じた時、私たちは自らを繋ぎ止めているものの存在を初めて強く意識します。",
        "aftertaste": "繋がれている。けれど。その『守られた限界』の中で、初めて自分の本当の場所が見つかることもある。",
        "example": "After working for eighteen hours without a break, she was at the end of her tether.",
        "deep_dive": { "roots": [{"term": "den-", "meaning": "rope, band (possible)"}], "points": ["tie（結ぶ）や toy（おもちゃ：かつては結び付けられたもの）とも遠い響きの共有。"] },
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
        print(f"Success: Added {added} words in Cycle 75.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
