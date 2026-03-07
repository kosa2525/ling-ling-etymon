import json
import re

word_batch = [
    # Cycle 110: Connection & Web
    {
        "id": "nexus_connection",
        "word": "Nexus",
        "meaning": "結合、連結、中心、核心",
        "era": "17th Century Latin nectere",
        "etymology": {
            "components": ["nectere (to bind, tie)"],
            "original_statement": "From Latin nexus (a binding, tying together), from nectere (to bind, tie, fasten)."
        },
        "concept": "A binding connection (複数の糸を「結び合わせ（bind）」、一つの強力な「中心（core）」を作ること)",
        "thinking": "バラバラに存在していた要素が ある一点で交差し 互いに切り離せない関係になること. 語源は「結ぶ」. それは単なる接触ではなく 運命や論理が複雑に絡み合い そこから新しい宇宙が始まっていくような 重たい繋がりです. あなたが誰かと出会い 何かが始まる その「結節点」.",
        "aftertaste": "響き合う結節点. あなたの人生のあらゆる出来事は 見えない糸で結ばれ 今という奇跡の中心（ネクサス）へと繋がっている.",
        "example": "The city center is the nexus of all the major transportation routes in the region.",
        "deep_dive": { "roots": [{"term": "ned-", "meaning": "to bind, tie"}], "points": ["connect（繋ぐ）や annex（併合する）と同じ、結束のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "network_connection",
        "word": "Network",
        "meaning": "網、ネットワーク、放送網、人脈",
        "era": "16th Century net + work",
        "etymology": {
            "components": ["net (woven fabric)", "work (something created)"],
            "original_statement": "From net (noun) + work (noun). Meaning 'complex, interlocking system' is from 1839."
        },
        "concept": "Net-like work (網の目のように「編み上げ（work）」られた、終わりなき「繋がり（net）」)",
        "thinking": "個々の点（ノード）が糸で結ばれ その糸がさらに別の点へと広がり 巨大でしなやかな「全体」を作り出している状態. 語源は「網の仕事」. それは獲物を捕らえるための道具でしたが 今では情報を運び 誰かを支え 世界を一つの有機体にするための 最も洗練された構造となりました. ",
        "aftertaste": "網の目の囁き. あなたが放った一言は 見えない網を伝わり 地球の裏側で誰かの心を温める光になるかもしれない. ",
        "example": "She built a vast professional network that helped her advance in her career quickly.",
        "deep_dive": { "roots": [{"term": "ned-", "meaning": "to bind (for net)"}, {"term": "werg-", "meaning": "to do (for work)"}], "points": ["織物のように繊細で、鋼のように強い。繋がることの強靭さ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "interface_connection",
        "word": "Interface",
        "meaning": "界面、境界面、接点、インターフェース",
        "era": "19th Century inter- + face",
        "etymology": {
            "components": ["inter- (between)", "face (surface)"],
            "original_statement": "From inter- (between) + face (noun). Originally in fluid mechanics, 'a surface forming a common boundary between two bodies'."
        },
        "concept": "Surface between (異なる世界が「境目（between）」を共有し、互いに「顔（face）」を突き合わせること)",
        "thinking": "全く異なる二つの存在が 互いの境界線を溶かし 対話や交換を始めるための「窓」. 語源は「顔の間」. 機械と人間 内側と外側 現実と理（ことわり）. そこは摩擦が起きる場所でもありますが 同時に 理解と翻訳が生まれる唯一の場所でもあります. 触れ合うことで 境界は意味を持ちます.",
        "aftertaste": "触れ合う境界. あなたが世界に触れるその指先こそが 新しい可能性が流れ込むインターフェースなのだ.",
        "example": "The user interface should be intuitive and easy for people of all ages to use.",
        "deep_dive": { "roots": [{"term": "enter-", "meaning": "between"}, {"term": "dhwer-", "meaning": "door (possible for face)"}], "points": ["境界は壁ではなく、入り口（扉）であるという思想。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "intertwine_connection",
        "word": "Intertwine",
        "meaning": "絡み合わせる、密接に結びつく",
        "era": "14th Century inter- + twine",
        "etymology": {
            "components": ["inter- (between)", "twine (to twist, double)"],
            "original_statement": "From inter- (between) + twine (verb). From Old English twin (double-twisted thread)."
        },
        "concept": "Twisting between (二本の糸を「ねじり（twist）」合わせ、もはや一本に「溶け合う（inter-）」こと)",
        "thinking": "別々の人生や出来事が 螺旋（らせん）状に深く絡み合い どちらがどちらかわからないほど密接になること. 語源の twine は「二つ（two）」から. 二つの孤独が合わさり より太く より強い一本の絆になる. それは お互いの弱さを補い合い 一つの物語を共に生きるという 静かな共生です.",
        "aftertaste": "二重螺旋の祈り. 絡み合った糸が解けないのは そこに愛と時間が 魔法のように塗り込められているからだ.",
        "example": "The fate of the two families had been intertwined for generations.",
        "deep_dive": { "roots": [{"term": "dwo-", "meaning": "two"}], "points": ["twist（ねじる）や twin（双子）と同じ。補完し合う関係性。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "mesh_connection",
        "word": "Mesh",
        "meaning": "網目、かみ合い、調和、メッシュ",
        "era": "14th Century Middle Dutch maesche",
        "etymology": {
            "components": ["maesche (knot, loop)"],
            "original_statement": "From Middle English messhe, from Middle Dutch maesche, from Proto-Germanic maskwon."
        },
        "concept": "The interlocking loop (糸が「輪（loop）」となり、互いに「かみ合う（interlock）」ことで、全体を支えること)",
        "thinking": "歯車が完璧に噛み合い エネルギーが滞りなく伝わっていくような 機能的で美しい調和. 語源は「結び目」. 一つひとつのパーツは小さくても それらが「メッシュ」として統合されたとき どんな衝撃も分散させて受け止める強さが生まれます. バラバラな個性が 共通の目的で結ばれる美しさ.",
        "aftertaste": "完璧な噛み合い. 歯車が回り出す. あなたの才能が誰かの必要にフィットしたとき 世界は静かに加速を始める.",
        "example": "Their ideas mesh perfectly, allowing them to collaborate more effectively than anyone else.",
        "deep_dive": { "roots": [{"term": "mezg-", "meaning": "to knit, plait"}], "points": ["marry（結婚する：結び合う）と同じルーツ。解けぬ契り。"] },
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
        print(f"Success: Added {added} words in Cycle 110.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
