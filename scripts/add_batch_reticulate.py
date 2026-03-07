import json
import re

word_batch = [
    # Cycle 147: Web & Entanglement (Refined)
    {
        "id": "reticulate_web",
        "word": "Reticulate",
        "meaning": "網状の、網目のある、(知識などが)交差した",
        "era": "17th Century Latin rete",
        "etymology": {
            "components": ["rete (net)"],
            "original_statement": "From Latin reticulatus (net-like), from reticulum (little net), diminutive of rete (net)."
        },
        "concept": "Net-like structure (「小さな網目（reticulum）」が 隙間なく 「交差（intersect）」し 合理的な 「強靭さ」を 作ること)",
        "thinking": "バラバラに存在する要素が、互いに支え合い、結び付くことで、一つの強固で美しい「意味の網」を形成すること. 語源は「小さな網目」. それは 直線的な思考を離れ、多次元的な繋がり（ネットワーク）の中で、全体像を捉えようとする 知性のあり方です.",
        "aftertaste": "繋がりの美学. 孤独を 恐れないで. あなたが「レティキュレイト（網状）」に 誰かと、あるいは 知識と 結び付くことで あなたという 存在は 決して折れない 強さと 奥行きを 手にするのだから.",
        "example": "The surface of the ancient ceramic bowl was decorated with a delicate reticulate pattern of blue lines.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["reticle（照準線）の語源。焦点を合わせるための、精密な網目。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "plexus_web",
        "word": "Plexus",
        "meaning": "(神経・血管などの)叢(そう)、集合体、複雑なネットワーク",
        "era": "17th Century Latin plectere",
        "etymology": {
            "components": ["plectere (to plait, braid, interweave)"],
            "original_statement": "From Latin plexus (a plaiting, braid), past participle of plectere (to plait, braid, interweave, entwine)."
        },
        "concept": "Interwoven bundle (「複雑に（complexly）」 絡み合いながら 「一つの力（one force）」として 脈動する 生命の 「結節点」)",
        "thinking": "単なる束（集合）ではなく、個々の糸が互いに浸透し合い、不可分な一つの「生命の核」へと変容すること. 語源は「編む、編み込まれたもの」. それは 人生の様々な経験が、一つの「自分」という名の 濃密な ネットワークへと 昇華されていく 聖なる プロセスです.",
        "aftertaste": "編み込まれた魂. 過去の 複雑な経験（糸）を 解（ほど）こうとしなくていい. その全てが「プレクサス（叢）」として あなたの内側で 結び付いているからこそ あなたは 今の 輝きを 放っているのだから.",
        "example": "The solar plexus is a complex network of nerves located in the abdomen, often called the second brain.",
        "deep_dive": { "roots": [{"term": "plek-", "meaning": "to plait"}], "points": ["complex（複雑な）や simple（単純な：一重の）と同じ。存在の「重なり」のドラマ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "mesh_web",
        "word": "Mesh",
        "meaning": "網目、(歯車が)かみ合う、(計画などが)うまくいく",
        "era": "Pre-12th Century Old English max",
        "etymology": {
            "components": ["max (net)"],
            "original_statement": "From Old English max (net), related to Latin macula (spot, mesh)."
        },
        "concept": "Interlocking space (「個（individual）」と 「個」が 正しい 「間隔（space）」で 噛み合い 新しい 「機能」を 生むこと)",
        "thinking": "自分勝手に動くのではなく、隣り合う他者と呼吸を合わせ、一つの大きな仕組み（システム）の一部として、滑らかに回転すること. 語源は「網、斑点」. それは 摩擦を 祝福に変え 共同で 目的を 達成しようとする 誠実な「協働（コラボレーション）」のアクションです.",
        "aftertaste": "噛み合う喜び. 自分の個性（歯車）を 研ぎ澄まそう. 周囲と心地よく「メッシュ（噛み合う）」したとき あなたの力は 何倍にも 増幅され 世界を大きく 動かし始めるのだから.",
        "example": "Our team's diverse skills mesh perfectly, allowing us to tackle even the most complex challenges.",
        "deep_dive": { "roots": [{"term": "mezg-", "meaning": "to knit, plait"}], "points": ["mask（仮面：編み込まれたもの）の語源との説も。隠蔽と結合の二面性。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "tangle_web",
        "word": "Tangle",
        "meaning": "もつれ、混乱、争い、(海藻などの)絡まり",
        "era": "14th Century Scandinavian tang",
        "etymology": {
            "components": ["tang (seaweed)"],
            "original_statement": "From a Scandinavian source, related to Old Norse þöngull (seaweed)."
        },
        "concept": "Chaotic binding (「流れ（flow）」の中で 「無秩序（chaos）」に 絡まり合い 容易には 「解けない（unsolvable）」 状態)",
        "thinking": "意図しない偶然が重なり合い、収集がつかなくなったように見える「カオス」の状態. 語源は「海藻」. しかし、その「タングル（もつれ）」こそが、実は新しい物語や 生命の「豊饒（ほうじょう）」を 育むための 肥沃な 苗床（カオス）でもあります. 混乱は、創造の前奏曲です.",
        "aftertaste": "もつれの愛おしさ. 人生の「もつれ（タングル）」を 無理に解こうとしなくていい. その複雑な 絡まり合いの中にこそ あなたにしか 語れない 唯一無二の 物語が 隠されているのだから.",
        "example": "She found her necklace in a hopeless tangle at the bottom of her jewelry box.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["和製英語の「タングル（パズル）」の語源。混乱という名の、聖なるパズル。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "interlace_web",
        "word": "Interlace",
        "meaning": "編み合わせる、組み合わせる、織り交ぜる",
        "era": "14th Century Latin inter- + laqueus",
        "etymology": {
            "components": ["inter- (between)", "laqueus (noose, snare)"],
            "original_statement": "From Old French entrelacier, from Latin inter- (between) + laqueus (noose, snare, bond)."
        },
        "concept": "Lacing between (「違う糸（different threads）」を 互いに 「潜らせ（pass through）」 交互に 「抱き合う（embrace）」こと)",
        "thinking": "単略的な 横に並ぶ（パラレル）のではなく、相手の懐に深く入り込み、お互いの色や 質感を 溶け合わせることで、一つの 複雑で 美しい 模様（タペストリー）を 作り上げること. 語源は「罠（わな）の間」. それは 自由を 制限する 束縛（罠）を、美しき 結合（レース）へと 昇華させる 聖なる 忍耐の 表現です.",
        "aftertaste": "交差する命. 誰かと「インターレイス（編み合わされる）」ことを 恐れないで. お互いの 違いを 織り交ぜることで あなたの人生は 想像もしなかった 壮大で 美しい 模様（タペストリー）を 完成させてゆくのだから.",
        "example": "The branches of the ancient trees interlace above the path, creating a natural green tunnel.",
        "deep_dive": { "roots": [{"term": "lek-", "meaning": "to bend, twist"}], "points": ["lace（レース、紐）や delicious（美味しい：誘惑する罠）と同じ。人を惹きつける、複雑な美。"] },
        "part_of_speech": "verb"
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
        print(f"Success: Added {added} words in Cycle 147.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
