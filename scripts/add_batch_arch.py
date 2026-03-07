import json
import re

word_batch = [
    {
        "id": "architecture",
        "word": "Architecture",
        "meaning": "建築、構造、アーキテクチャ",
        "era": "16th Century Latin/Greek arkhitektōn",
        "etymology": {
            "components": ["arkhi- (chief)", "tektōn (builder)"],
            "original_statement": "From Latin architectura, from Greek arkhitektōn (master builder, director of works), from arkhi- (chief) + tektōn (builder, carpenter)."
        },
        "concept": "The work of the master builder (大工の長の仕事)",
        "thinking": "単なる家づくり（building）ではなく、「最高の技術と思想を束ねて、一つの秩序ある空間を組み上げる（architecture）」こと。転じて、複雑なシステムやソフトウェアの思想的骨組みをも意味する言葉となりました。",
        "aftertaste": "石を積むのではない。空間に意味を積むのだ。",
        "example": "He admired the classical architecture of the museum.",
        "deep_dive": {
            "roots": [{"term": "tek-", "meaning": "to make, build"}],
            "points": ["テクノロジー（technology）の『テク（技術）』と同じ語根です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "structure",
        "word": "Structure",
        "meaning": "構造、建造物、体系",
        "era": "15th Century Latin structura",
        "etymology": {
            "components": ["struere (to build, assemble)"],
            "original_statement": "From Latin structura (a fitting together, building), from struere (to pile up, build, assemble)."
        },
        "concept": "A piling up or assembling (積み上げられたもの、組み立てられたもの)",
        "thinking": "部分と部分がしっかりと組み合わさり（fitting together）、一つの全体として重力を支え合う仕組み。目に見えるビルディングだけでなく、組織や文章の『骨組み』を支える最も重要な基盤です。",
        "aftertaste": "重力に抗するための、要素の美しい結びつき。",
        "example": "The cell is the basic structure of all living organisms.",
        "deep_dive": {
            "roots": [{"term": "stere-", "meaning": "to spread, solid"}],
            "points": ["construct（建設する）や destroy（破壊する：構造を崩す）の中心にある木材（根）です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "foundation",
        "word": "Foundation",
        "meaning": "基礎、土台、設立、財団",
        "era": "14th Century Old French/Latin fundatio",
        "etymology": {
            "components": ["fundus (bottom)"],
            "original_statement": "From Latin fundationem (a founding), from fundare (to lay the bottom or foundation of something), from fundus (bottom)."
        },
        "concept": "The bottom upon which something is built (何かが建てられる一番底)",
        "thinking": "地中に埋まっていて目には見えないけれど、全ての重さを無言で引き受けている「一番下の部分（bottom）」。転じて思想の根拠や、社会を支える基金（財団）を指します。",
        "aftertaste": "見えない底が、すべてを支えている。",
        "example": "Trust is the foundation of a good relationship.",
        "deep_dive": {
            "roots": [{"term": "bhudh-", "meaning": "bottom"}],
            "points": ["profound（深い: 前+底）や fundamental（根本的な）と同じ最も深い語源です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "pillar",
        "word": "Pillar",
        "meaning": "柱、大黒柱、中心人物",
        "era": "13th Century Old French/Latin pila",
        "etymology": {
            "components": ["pila (pillar, stone barrier)"],
            "original_statement": "From Old French piler, from Vulgar Latin *pilare, from Latin pila (pillar, pier)."
        },
        "concept": "A vertical support (垂直の支え)",
        "thinking": "ただ重さを支えるだけでなく、神殿の柱のように天と地を繋ぐ象徴でもあります。そのため、「社会の柱（＝なくてはならない中心的な人・信念）」という強い賛辞として使われます。",
        "aftertaste": "重圧に耐え、天を突く一本の軸。",
        "example": "She has been a pillar of the community for decades.",
        "deep_dive": {
            "roots": [{"term": "pila", "meaning": "pillar"}],
            "points": ["column（円柱）よりも少し太く、支える役割の『柱』としての意味合いが強い言葉です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "column",
        "word": "Column",
        "meaning": "円柱、縦の列、(新聞などの)コラム",
        "era": "15th Century Latin columna",
        "etymology": {
            "components": ["columen (top, summit, pillar)"],
            "original_statement": "From Latin columna (pillar), related to columen (summit, top), from PIE root *kel- (to project, be prominent)."
        },
        "concept": "A prominent projecting support (突き出た支え)",
        "thinking": "元々はそびえ立つ建築の円柱。それが紙に並ぶ「縦の列（新聞の縦長の寄稿文）」へと転じ、さらには軍隊の縦長の「隊列」をも意味する、縦方向に強く伸びる言葉です。",
        "aftertaste": "視線を上へと導く、威厳ある垂直線。",
        "example": "He writes a weekly column for the local newspaper.",
        "deep_dive": {
            "roots": [{"term": "kel-", "meaning": "to project, be prominent"}],
            "points": ["エクセルなどの『行（row）』に対する『列（column）』としておなじみです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "arch",
        "word": "Arch",
        "meaning": "アーチ(門)、弧、(主要な、最大の)",
        "era": "14th Century Old French/Latin arcus",
        "etymology": {
            "components": ["arcus (a bow, arch)"],
            "original_statement": "From Old French arche, from Latin arcus (a bow, arch)."
        },
        "concept": "A curved structure (弓なりに曲がった構造)",
        "thinking": "石を弓形に積むことで重さを横に逃がし、真下に柱がなくても空間を支えられる大発明。そこから、敵の放つ弓（archer）や、すべてをまたぐ『主要な（arch-）』という意味にも発展しました。",
        "aftertaste": "しなやかな弧が、何トンもの重力を魔法のように逃がす。",
        "example": "The triumph arch was built to commemorate the victory.",
        "deep_dive": {
            "roots": [{"term": "arcus", "meaning": "bow"}],
            "points": ["arc（弧）と同じ起源を持ちます。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "vault",
        "word": "Vault",
        "meaning": "アーチ型天井、地下金庫、跳躍する",
        "era": "14th Century Old French/Latin volvere",
        "etymology": {
            "components": ["volvere (to roll, turn)"],
            "original_statement": "From Old French voute (arch, vaulted roof), from Vulgar Latin *volvita, from Latin volutus, past participle of volvere (to roll, turn)."
        },
        "concept": "A rolled or curved roof (丸められた天井)",
        "thinking": "アーチを横に引き伸ばしたような蒲鉾型の天井。空のように丸く包み込むこの構造から派生して、頑丈に守られた「地下金庫」や、手をついてアーチ状に飛び越える「跳躍」という意味にもなりました。",
        "aftertaste": "丸く閉ざされた、絶対の安全圏。",
        "example": "Valuable artifacts are kept securely in the bank vault.",
        "deep_dive": {
            "roots": [{"term": "wel-", "meaning": "to turn, roll"}],
            "points": ["revolve（回転する）や volume（巻物・量）と同じ『丸める』というルーツです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "dome",
        "word": "Dome",
        "meaning": "ドーム、丸天井",
        "era": "16th Century French/Latin domus",
        "etymology": {
            "components": ["domus (house)"],
            "original_statement": "From French dôme, from Italian duomo (cathedral), from Latin domus (house, household) specifically domus dei (house of God)."
        },
        "concept": "The house of God (神の家)",
        "thinking": "元々はイタリアの『ドゥオーモ（大聖堂＝神の家）』を指す言葉でした。大聖堂に巨大な丸天井があったことから、いつしか建物の丸い屋根そのものを『ドーム』と呼ぶようになりました。",
        "aftertaste": "天井を開け、天球を模倣する。",
        "example": "The observatory has a large metal dome.",
        "deep_dive": {
            "roots": [{"term": "dem-", "meaning": "house, household"}],
            "points": ["domestic（家庭の、国内の）や domain（領地）と同じく『家』という根幹を持ちます。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "facade",
        "word": "Facade",
        "meaning": "建物の正面、見せかけ、外見",
        "era": "17th Century French/Italian facciata",
        "etymology": {
            "components": ["faccia (face)"],
            "original_statement": "From French façade, from Italian facciata (front of a building), from faccia (face), from Latin facies."
        },
        "concept": "The face of the building (建物の顔)",
        "thinking": "道行く人に向けて最も装飾が施される「建築の顔」。そこから転じて、人間が他人に見せるための「取り繕った立派な外観（裏ではボロボロかもしれないけれど）」という文学的な皮肉として使われます。",
        "aftertaste": "綺麗な壁の裏側には、何があるのか。",
        "example": "Behind his cheerful facade, he was deeply depressed.",
        "deep_dive": {
            "roots": [{"term": "dhe-", "meaning": "to set, put"}],
            "points": ["face（顔）と語源は全く同じ。顔とはつまり『外から見える正面』です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "scaffold",
        "word": "Scaffold",
        "meaning": "足場、(処刑の)断頭台",
        "era": "14th Century Old Northern French",
        "etymology": {
            "components": ["eschafaut (platform)"],
            "original_statement": "From Old Northern French escafaut (a platform), possibly from ex- + catafalicum (viewing stage)."
        },
        "concept": "A temporary elevated platform (一時的に高く組まれた木組み)",
        "thinking": "建築の際に建物の周りに組まれる「一時的な支え」。本丸が完成すれば撤去されるもの。また、公開処刑のために急ごしらえで作られた「高い舞台（断頭台）」も意味する、少し血の匂いのする建設用語です。",
        "aftertaste": "完成とともに取り壊される、影の立役者。",
        "example": "Workers erected a scaffold to repair the roof.",
        "deep_dive": {
            "roots": [{"term": "catafalque", "meaning": "wooden framework"}],
            "points": ["教育で『学習者の支援（スキャフォールディング）』という用語でも使われます。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "blueprint",
        "word": "Blueprint",
        "meaning": "青写真、詳細な計画",
        "era": "19th Century English",
        "etymology": {
            "components": ["blue", "print"],
            "original_statement": "Coined in the 1850s from the photographic process that produces white lines on a blue background."
        },
        "concept": "A detailed design or plan (詳細な設計図)",
        "thinking": "フェリシアン化鉄を用いた古い複写技術で、青い紙の上に白い線で図面が浮かび上がったことから。現在では真っ白な紙に印刷されますが、言葉だけが『綿密な将来の計画』として残り続けています。",
        "aftertaste": "未来の形を、青い夜空に白い線で描く。",
        "example": "DNA is the blueprint of life.",
        "deep_dive": {
            "roots": [],
            "points": ["技術革新によって消えたものが、言葉の比喩として永遠に生き残る典型例です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "edifice",
        "word": "Edifice",
        "meaning": "(大がかりな)建築物、(複雑な)体系",
        "era": "14th Century Old French/Latin aedificium",
        "etymology": {
            "components": ["aedes (building, temple)", "facere (to make)"],
            "original_statement": "From Latin aedificium (building), from aedificare (to build, construct), from aedes (dwelling, temple, hearth) + facere (to make)."
        },
        "concept": "Making a dwelling or temple (神殿や住居を作ること)",
        "thinking": "単なるbuilding（建物）ではなく、大聖堂や宮殿のように「威厳があり、堂々とそびえ立つ複雑で巨大な構造物」。概念的な「巨大な思想体系」にも使われます。",
        "aftertaste": "畏敬の念を抱かせる、荘厳なる塊。",
        "example": "The library is an imposing edifice from the 19th century.",
        "deep_dive": {
            "roots": [{"term": "aid-", "meaning": "to burn, hearth"}],
            "points": ["aedes（神殿・家）の元々の意味は『火を燃やす場所（囲炉裏）』でした。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "monument",
        "word": "Monument",
        "meaning": "記念碑、記念建造物、不朽の業績",
        "era": "13th Century Old French/Latin monumentum",
        "etymology": {
            "components": ["monere (to remind, warn)"],
            "original_statement": "From Latin monumentum (a monument, memorial, record), from monere (to remind, warn)."
        },
        "concept": "Something serving to remind (思い出させるためのもの)",
        "thinking": "過去の偉大なこと（または悲惨なこと）を、後の世代が「忘れないように心に留めさせる（monere）」ために石で刻んだ装置。物理的な建造物でありながら、実は時間の忘却に抗うための「記憶の装置」です。",
        "aftertaste": "忘却というエントロピーに抗う、記憶の楔。",
        "example": "The statue stands as a monument to the fallen soldiers.",
        "deep_dive": {
            "roots": [{"term": "men-", "meaning": "to think"}],
            "points": ["memory（記憶）や mental（精神の）と同じ『心に留める』ルーツから来ています。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "sanctuary",
        "word": "Sanctuary",
        "meaning": "聖域、避難所、(鳥獣の)保護区",
        "era": "14th Century Old French/Latin sanctuarium",
        "etymology": {
            "components": ["sanctus (holy, sacred)"],
            "original_statement": "From Late Latin sanctuarium (a sacred place, shrine), from Latin sanctus (holy)."
        },
        "concept": "A holy place of refuge (神聖なる逃げ場)",
        "thinking": "世俗の権力や剣が届かない「神聖な空間」。昔は教会の敷地に逃げ込めば逮捕されない権利（アジール）がありました。そこから現代では、弱者を守るための「絶対の安全地帯（保護区）」に拡大されました。",
        "aftertaste": "追っ手の刃を弾き返す、不可視の結界。",
        "example": "My garden has become a wildlife sanctuary.",
        "deep_dive": {
            "roots": [{"term": "sak-", "meaning": "to sanctify"}],
            "points": ["sacred（神聖な）や saint（聖人）と同じ根元の言葉です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "asylum",
        "word": "Asylum",
        "meaning": "亡命、保護、(昔の)精神病院",
        "era": "15th Century Latin/Greek asylon",
        "etymology": {
            "components": ["a- (without)", "sylon (right of seizure)"],
            "original_statement": "From Latin asylum (sanctuary), from Greek asylon (refuge, sanctuary), neuter of asylos (inviolable), from a- (without) + sylon (right of seizure)."
        },
        "concept": "A place without seizure (略奪や逮捕されない不可侵の場所)",
        "thinking": "Sanctuaryと同じく不可侵の逃げ場を意味しますが、より政治的な「亡命の保護」の色が強い言葉。19世紀には社会から切り離された『精神病院』の呼称としても使われ、悲しい響きも帯びています。",
        "aftertaste": "捕まることのない、冷たくて静かな避難場所。",
        "example": "The political refugee sought asylum in a neighboring country.",
        "deep_dive": {
            "roots": [{"term": "sylon", "meaning": "seizure"}],
            "points": ["文字通り『奪い取られる心配がない（a-sylon）場所』という意味です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "arcade",
        "word": "Arcade",
        "meaning": "アーケード、(アーチ型の)連続した通路、ゲームセンター",
        "era": "18th Century French/Latin arcus",
        "etymology": {
            "components": ["arcus (arch, bow)"],
            "original_statement": "From French arcade, from Italian arcata (arch of a bridge), from Latin arcus (bow, arch)."
        },
        "concept": "A series of arches (連なるアーチ)",
        "thinking": "元々は柱とアーチがずっと連続して続く回廊のこと。屋根がつくことで商店街となり、そこにある機械式ゲームが「アーケードゲーム」と呼ばれるようになるという、一風変わった進化を遂げた建築用語です。",
        "aftertaste": "石のアーチの下を抜けた先に鳴り響く、電子音。",
        "example": "We walked through the shopping arcade to stay out of the rain.",
        "deep_dive": {
            "roots": [{"term": "arcus", "meaning": "bow"}],
            "points": ["arch（アーチ）と同じ語源ですが、連続しているのが特徴です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "corridor",
        "word": "Corridor",
        "meaning": "廊下、回廊、(空路などの)通過帯",
        "era": "16th Century French/Italian correre",
        "etymology": {
            "components": ["correre (to run)"],
            "original_statement": "From French corridor, from Italian corridore (a long passage, literally 'a runner'), from correre (to run)."
        },
        "concept": "A place for running (走るための場所)",
        "thinking": "部屋と部屋を繋ぐただの通路ではなく、語源的には使者や兵士が迅速に「走って（correre）」メッセージを届けるための長い一直線の空間。移動の効率化を極めた建築装置。",
        "aftertaste": "目的地へ直行するための、乾いた直線の管。",
        "example": "Her office is just down the hallway corridor.",
        "deep_dive": {
            "roots": [{"term": "kers-", "meaning": "to run"}],
            "points": ["current（流れ）、course（コース）、car（走る車）と同じ『走る』というルーツの集まり。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "atrium",
        "word": "Atrium",
        "meaning": "アトリウム、吹き抜けの中庭、(心臓の)心房",
        "era": "16th Century Latin atrium",
        "etymology": {
            "components": ["atrum (black, darkly stained)"],
            "original_statement": "From Latin atrium (central court of a Roman house), historically thought to be from ater (black), because the roof was blackened by the smoke from the central hearth."
        },
        "concept": "The central black room (黒く煤けられた中央の部屋)",
        "thinking": "古代ローマの家で、天井に煙抜きの穴が開いていた中央の吹き抜け広場。料理の煙で天井が黒く煤（すす）けていた（atrum）ことから。今は明るいガラス張りの吹き抜けを指します。血が集まる心房という比喩にもなりました。",
        "aftertaste": "煤けた煙の記憶が、現代のガラス張りの光に上書きされる。",
        "example": "The hotel features a stunning glass-walled atrium.",
        "deep_dive": {
            "roots": [{"term": "ater", "meaning": "black"}],
            "points": ["黒い（ater）が、現代の最も明るい空間（アトリウム）を意味するという皮肉な逆転です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "vestibule",
        "word": "Vestibule",
        "meaning": "玄関ホール、前室",
        "era": "17th Century French/Latin vestibulum",
        "etymology": {
            "components": ["vestibulum (forecourt, entrance)"],
            "original_statement": "From Latin vestibulum (forecourt, entrance court), of uncertain origin but referring to the enclosed space in front of an entrance."
        },
        "concept": "An enclosed entrance area (外と内を区切る玄関の前室)",
        "thinking": "完全に外でもなく、完全に室内でもない「緩衝地帯」。寒い空気を遮断したり、靴についた泥を落としたりする場所。オンとオフを切り替える心のバッファ空間。",
        "aftertaste": "外の風を払い落とし、ゆっくりと扉を開ける。",
        "example": "Please leave your wet umbrellas in the vestibule.",
        "deep_dive": {
            "roots": [],
            "points": ["『服（vest）を着替える場所』だったという民間語源説もあります。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "threshold",
        "word": "Threshold",
        "meaning": "敷居、境界、出発点、限界値",
        "era": "Old English þerscold",
        "etymology": {
            "components": ["þerscan (to thresh, tread)", "wald (wood)"],
            "original_statement": "From Old English þerscold, where the first element is related to thresh (tread, trample), the exact origin of the second part is obscure, meaning the piece of wood trampled on when entering."
        },
        "concept": "The piece of wood trampled on (足で踏みつけられる戸口の木)",
        "thinking": "ドアの真下にある一段高い敷居。これを跨ぐことで「あちら側」から「こちら側」へと次元が変わります。そこから、痛みの「限界値（pain threshold）」や、新しい人生の「出発点」という哲学的な意味を持ちました。",
        "aftertaste": "またぐ。ただそれだけで世界が変わる。",
        "example": "We are on the threshold of a new technological era.",
        "deep_dive": {
            "roots": [{"term": "tere-", "meaning": "to rub, turn"}],
            "points": ["『ここを超えたら反応が変わる閾値（いきち）』として科学分野でも多用されます。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "boundary",
        "word": "Boundary",
        "meaning": "境界(線)、限界",
        "era": "17th Century English",
        "etymology": {
            "components": ["bound (limit)", "-ary (pertaining to)"],
            "original_statement": "Formed from bound (limit) + -ary, from Old French bodne (limit, marker)."
        },
        "concept": "A line marking a limit (限界を示す線)",
        "thinking": "あなたの領土と私の領土、あなたの権利と私の権利を厳格に切り分ける線。自己と他者を分ける心理的な境界線（healthy boundaries）としても非常に重要な概念です。",
        "aftertaste": "引かれた線。踏み越えれば摩擦熱が生じる。",
        "example": "A river forms the natural boundary between the two countries.",
        "deep_dive": {
            "roots": [{"term": "bodne", "meaning": "limit"}],
            "points": ["border（国境などの幅のある境界）に対し、より厳密で数学的な『線』のニュアンス。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "perimeter",
        "word": "Perimeter",
        "meaning": "周囲、周辺、(城などの)防衛線",
        "era": "16th Century Latin/Greek perimetros",
        "etymology": {
            "components": ["peri- (around)", "metron (measure)"],
            "original_statement": "From Latin perimetros, from Greek perimetron (circumference), from peri- (around) + metron (measure)."
        },
        "concept": "Measuring around (ぐるりと測った周囲)",
        "thinking": "対象を囲む「外縁部の長さ」という数学用語ですが、転じて軍事やセキュリティで「（侵入を防ぐために）ぐるりと警戒すべき外側の防衛線」という意味で使われます。",
        "aftertaste": "外側の殻を守り切れ。内壁は脆い。",
        "example": "Security guards patrolled the perimeter of the estate.",
        "deep_dive": {
            "roots": [{"term": "me-", "meaning": "to measure"}],
            "points": ["peri-（周囲）は periscope（潜望鏡）や periphery（周縁部）と同じ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "bastion",
        "word": "Bastion",
        "meaning": "稜堡(りょうほ)、要塞、(思想などの)最後の砦",
        "era": "16th Century French/Italian bastione",
        "etymology": {
            "components": ["bastire (to build)"],
            "original_statement": "From French bastion, from Italian bastione (part of a fortress), from bastire (to build)."
        },
        "concept": "A built projection (突き出して建てられた防衛設備)",
        "thinking": "城の側壁から外に三角形に突き出た部分。ここから敵の側面を攻撃し、城本体への接近を防ぐという極めて実用的な防御構造。転じて、「ある信念や権利を守る最後の難攻不落の砦」として使われます。",
        "aftertaste": "突き出し、迎え撃つ。最後の一人になっても。",
        "example": "The university is a bastion of academic freedom.",
        "deep_dive": {
            "roots": [{"term": "bast-", "meaning": "to build"}],
            "points": ["baste（縫いつける）と同根という説もあります。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "citadel",
        "word": "Citadel",
        "meaning": "城塞、要塞、最後の拠り所",
        "era": "16th Century French/Italian cittadella",
        "etymology": {
            "components": ["città (city)", "-ella (diminutive)"],
            "original_statement": "From Middle French citadelle, from Italian cittadella (little city), diminutive of città (city)."
        },
        "concept": "The little city (小さな都市＝都市を見下ろす要塞)",
        "thinking": "都市の中心の高台に作られ、都市全体が敵に占領されても、指導者たちが最後に立てこもるための強固な「小都市」。絶対的権力や、思想の最終防衛ラインの象徴。",
        "aftertaste": "街が燃えても、この高台だけは明け渡さない。",
        "example": "They retreated to the citadel after the outer walls fell.",
        "deep_dive": {
            "roots": [{"term": "kwi-", "meaning": "rest, quiet, citizen"}],
            "points": ["city（都市）や citizen（市民）と同じ語源から派生した『強固な小都市』です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "fortress",
        "word": "Fortress",
        "meaning": "要塞、大規模な城塞、安全な場所",
        "era": "13th Century Old French/Latin fortis",
        "etymology": {
            "components": ["fortis (strong)"],
            "original_statement": "From Old French forteresse, from Medieval Latin forteritia (fortress), from Latin fortis (strong)."
        },
        "concept": "A stronghold (強さの結晶)",
        "thinking": "単なる建物というよりは、一つの町が丸ごと軍事用に武装された巨大な防御施設（ストロングホールド）。心理的に自分を守るための「心の壁を高くした状態」の比喩にもなります。",
        "aftertaste": "強さ（力）を石で包み込み、外界を拒絶する。",
        "example": "The Flying Fortress was a famous bomber plane in WWII.",
        "deep_dive": {
            "roots": [{"term": "bhergh-", "meaning": "high, to protect"}],
            "points": ["force（力）や fort（砦）、comfort（安心させる）と同じ『力・強い』という根拠です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "lintel",
        "word": "Lintel",
        "meaning": "まぐさ(窓やドアの上の水平な梁)",
        "era": "14th Century Old French/Latin limentum",
        "etymology": {
            "components": ["limen (threshold)"],
            "original_statement": "From Old French lintel, from Vulgar Latin *limitare, from Latin limen (threshold, crossing)."
        },
        "concept": "The upper threshold (上部の敷居)",
        "thinking": "ドアの真上で開口部を支え、上部の壁の重さを左右の柱に逃がす一本の横木（梁）。地味ながら、これがないと空間を切り開く（ドアを作る）ことができない不可欠な水平パーツ。",
        "aftertaste": "頭上で静かに、建築の重みに耐える力持ち。",
        "example": "The carved stone lintel above the entrance is 800 years old.",
        "deep_dive": {
            "roots": [{"term": "limen", "meaning": "threshold"}],
            "points": ["threshold（足元の敷居）と対になる、頭上の限界線（limit）です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "keystone",
        "word": "Keystone",
        "meaning": "要石(かなめいし)、要旨、最も重要な部分",
        "era": "17th Century English",
        "etymology": {
            "components": ["key", "stone"],
            "original_statement": "A compound of key + stone, literally the wedge-shaped stone at the apex of an arch."
        },
        "concept": "The stone that locks an arch (アーチを止める鍵の石)",
        "thinking": "アーチを両側から組み上げていき、最後に一番てっぺんに強めにパズルのように打ち込まれるクサビ型の石。これがはまることで全ての石の重力がロックされ自立する。つまり『欠けたらすべてが崩壊する最重要部分』。",
        "aftertaste": "最後に落ちる一つが、すべてを完璧に固定する。",
        "example": "Trust is the keystone of their business partnership.",
        "deep_dive": {
            "roots": [],
            "points": ["動物学でも、生態系を支える最重要種を『キーストーン種』と呼びます。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "buttress",
        "word": "Buttress",
        "meaning": "控え壁(バットレス)、支える、補強する",
        "era": "14th Century Old French/Old French boter",
        "etymology": {
            "components": ["boter (to strike, thrust, push)"],
            "original_statement": "From Old French boteresse, from boter (to strike, push, thrust)."
        },
        "concept": "A pushing support (外側から押し返す支え)",
        "thinking": "重たい石のアーチが開いて崩れないよう、ゴシック建築では建物の外側から「巨大なナナメの突っかい棒（壁）」で押し返しました。ここから「自論を外側の証拠で強固に『補強する』」という強力な動詞になりました。",
        "aftertaste": "外側から全力で踏ん張る、ナナメの擁護者。",
        "example": "He used statistics to buttress his argument.",
        "deep_dive": {
            "roots": [{"term": "bhau-", "meaning": "to strike"}],
            "points": ["button（ボタン: 押し出すもの）や beat（叩く）と同じルーツです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "canopy",
        "word": "Canopy",
        "meaning": "天蓋(てんがい)、(森の)林冠",
        "era": "14th Century Old French/Greek kōnōpeion",
        "etymology": {
            "components": ["kōnōps (mosquito)"],
            "original_statement": "From Medieval Latin canopeum (net), from Greek kōnōpeion (bed with mosquito net), from kōnōps (mosquito)."
        },
        "concept": "A bed covering to keep off mosquitoes (元々は蚊帳)",
        "thinking": "なんと語源は「蚊除けのネット」。それが王様の玉座やベッドを覆う豪華な布の「天蓋」になり、パラシュートの傘の部分や、アマゾンの熱帯雨林を覆う「葉の茂みの天井（林冠）」という壮大な広がりを見せました。",
        "aftertaste": "玉座を飾る天蓋も、始まりはただの蚊帳だった。",
        "example": "The jungle canopy blocks out most of the sunlight.",
        "deep_dive": {
            "roots": [{"term": "kōnōps", "meaning": "mosquito"}],
            "points": ["建築物を覆い隠す布、あるいは自然の天井というロマンチックな使われ方をします。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "turret",
        "word": "Turret",
        "meaning": "小塔(タレット)、(戦車などの)砲塔",
        "era": "14th Century Old French/Latin turris",
        "etymology": {
            "components": ["turris (tower)", "-et (diminutive)"],
            "original_statement": "From Old French torete, diminutive of tor, from Latin turris (tower)."
        },
        "concept": "A small tower (小さな塔)",
        "thinking": "城の角に壁から突き出すように作られた小さな塔。ここから見張りや射撃を行いました。その回転して攻撃できる性質から、現代の戦車の「旋回用の砲塔部分」もタレットと呼ばれます。",
        "aftertaste": "壁の角から睨みを効かせる、小さな監視眼。",
        "example": "The medieval castle featured round turrets at each corner.",
        "deep_dive": {
            "roots": [{"term": "turris", "meaning": "tower"}],
            "points": ["tower（巨大な塔）に対して、屋根などにポコッと生えたちょっとかわいい小塔です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "parapet",
        "word": "Parapet",
        "meaning": "胸壁(きょうへき)、欄干(らんかん)",
        "era": "16th Century French/Italian parapetto",
        "etymology": {
            "components": ["parare (to cover, shield)", "petto (breast)"],
            "original_statement": "From Italian parapetto, from parare (to cover, defend) + petto (breast)."
        },
        "concept": "Shield for the breast (胸を守るもの)",
        "thinking": "城の屋上や橋に作られた、胸の高さまでの低い壁。兵士が後ろに身を隠し、そこから銃や矢を撃ちました。「落ちない手すり」である前に「心臓（胸）を守る盾」だったという生々しい語源。",
        "aftertaste": "胸の下の石壁が、命のリミッターになる。",
        "example": "Soldiers crouched behind the parapet to avoid enemy fire.",
        "deep_dive": {
            "roots": [{"term": "per-", "meaning": "to produce, procure"}, {"term": "peg-", "meaning": "breast"}],
            "points": ["ペクトラル（pectoral: 胸筋）のpettoと、パラソル（parasol: 太陽を防ぐ）のparaです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "spire",
        "word": "Spire",
        "meaning": "尖塔(せんとう)、(教会の)尖り屋根",
        "era": "Old English spir",
        "etymology": {
            "components": ["spir (tall, slender stem of a plant)"],
            "original_statement": "From Old English spir (long, tall, slender stem of a plant), meaning expanded to a tapering roof or tower."
        },
        "concept": "A slender tapering upper part (細長く細まっていく頂部)",
        "thinking": "植物の細く伸びる「茎」が語源。ゴシック教会の屋根の上に、そこからさらに空に向かって突き刺さるように乗せられた細長い尖塔。天へ到達したいという人々の宗教的渇望の形です。",
        "aftertaste": "天へ。ただひたすらに、細く、高く。",
        "example": "The cathedral's spire can be seen from miles away.",
        "deep_dive": {
            "roots": [{"term": "spei-", "meaning": "sharp point"}],
            "points": ["spike（スパイク・トゲ）や spit（串）と同じ『尖ったもの』のルーツです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "pinnacle",
        "word": "Pinnacle",
        "meaning": "頂点、絶頂、小尖塔",
        "era": "14th Century Old French/Late Latin pinnaculum",
        "etymology": {
            "components": ["pinna (wing, point)", "-culum (diminutive)"],
            "original_statement": "From Late Latin pinnaculum (gable, peak), diminutive of Latin pinna (wing, point, feather)."
        },
        "concept": "A small pointed wing or peak (小さな尖った翼、頂点)",
        "thinking": "建築のてっぺんを飾る小さな尖った装飾部分。そこから、物理的な高さだけでなく、名声や能力が「もうこれ以上行けない究極のピーク」に達した状態を指します。",
        "aftertaste": "全てを登り切った者だけが立つ、針の先。",
        "example": "Winning the championship was the pinnacle of his career.",
        "deep_dive": {
            "roots": [{"term": "pet-", "meaning": "to rush, fly"}],
            "points": ["pen（ペン、元は羽ペン）や pin（ピン）と同じ『尖ったもの・羽』の源流です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "apex",
        "word": "Apex",
        "meaning": "頂点、最高潮",
        "era": "17th Century Latin",
        "etymology": {
            "components": ["apex (summit, tip)"],
            "original_statement": "Directly from Latin apex (summit, peak, tip), originally a small rod at the top of a priest's cap."
        },
        "concept": "The tip or highest point (ある形状の一番上の角)",
        "thinking": "三角形やピラミッドなどの幾何学的な「頂角」。転じて、食物連鎖の頂点（apex predator）のように、ある階層の完全に一番上のポジションに君臨することを意味します。",
        "aftertaste": "三角形の最も鋭い頂。そこに立つのは一人だけ。",
        "example": "The great white shark is an apex predator.",
        "deep_dive": {
            "roots": [{"term": "ap-", "meaning": "to grasp, take, reach"}],
            "points": ["pinnacle が『到達点』なら、apex は『幾何学・構造的なピラミッドの最後の一点』という理系的な鋭さがあります。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "vertex",
        "word": "Vertex",
        "meaning": "頂点、(頭の)頂、交点",
        "era": "16th Century Latin vertex",
        "etymology": {
            "components": ["vertere (to turn)"],
            "original_statement": "From Latin vertex (highest point, pole of the sky, whirlpool), from vertere (to turn)."
        },
        "concept": "The point around which something turns (何かが回転する中心の極み)",
        "thinking": "天球が星空を回転させる中心の極（つむじ）、あるいは頭頂部。数学では二つの線が交わって方向転換（ターン）する「角（頂点）」という意味。数学やCGモデリングの基礎用語。",
        "aftertaste": "線と線がぶつかり、新しい次元へ向きを変えるゼロ地点。",
        "example": "A square has four vertices.",
        "deep_dive": {
            "roots": [{"term": "wer-", "meaning": "to turn, bend"}],
            "points": ["universe（宇宙: 一つにターンする）や reverse（反転する）と同じ vertere 族です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "cornice",
        "word": "Cornice",
        "meaning": "軒蛇腹(のきじゃばら)、コーニス、雪庇(せっぴ)",
        "era": "16th Century French/Italian cornice",
        "etymology": {
            "components": ["korōnis (curved line, crown)"],
            "original_statement": "From Italian cornice, probably from Latin coronis, from Greek korōnis (a curved line, flourish), related to korōnē (crown)."
        },
        "concept": "A crowning curve (建物の最上部を冠する曲線の装飾)",
        "thinking": "建物の壁の最上部、屋根のすぐ下を横に走る出っ張った帯状の装飾部分（頭の冠）。また、冬山で稜線から雪が庇のようにせり出した危険な「雪庇（せっぴ）」もコーニスと呼びます。",
        "aftertaste": "壁を見下ろす、石の王冠。",
        "example": "The ancient Greek temple has a beautifully carved cornice.",
        "deep_dive": {
            "roots": [{"term": "sker-", "meaning": "to turn, bend"}],
            "points": ["crown（王冠）や corona（光冠）と同じ『丸く囲うもの』という源流です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "frieze",
        "word": "Frieze",
        "meaning": "フリーズ(彫刻などで装飾された帯状の横壁)",
        "era": "16th Century French frise",
        "etymology": {
            "components": ["frise (border, decoration)"],
            "original_statement": "From French frise (border, decoration), of uncertain origin, perhaps related to Phrygian embroidery or Latin Phrygium (work in gold and silver)."
        },
        "concept": "A broad horizontal band of sculpted decoration (横に長く続く装飾的な帯)",
        "thinking": "パルテノン神殿の壁上部にぐるりと彫られている、兵士や馬のパレードのような連続した浮き彫りの装飾面。建築の一部でありながら、巨大なキャンバスでもありました。",
        "aftertaste": "石の壁に彫られた、永遠に終わらないパレード。",
        "example": "The museum displays a replica of the Parthenon frieze.",
        "deep_dive": {
            "roots": [],
            "points": ["freeze（凍る）と発音は同じですが、全く関係ありません。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "pediment",
        "word": "Pediment",
        "meaning": "破風(はふ)、ペディメント(古代建築の三角形の切妻部分)",
        "era": "16th Century Renaissance Latin/English",
        "etymology": {
            "components": ["periment (corruption of pyramid)"],
            "original_statement": "An alteration of earlier periment, which itself was a corruption of pyramid, referring to its triangular shape."
        },
        "concept": "A triangular upper part (三角形の上部構造)",
        "thinking": "ギリシャ神殿の正面の一番上にある、大きな三角形の壁面部分。この中には神々の巨大な彫刻がギュッと詰め込まれました。実は『ピラミッド（pyramid）』が訛った英語という面白い歴史を持ちます。",
        "aftertaste": "神話が詰め込まれた、空に浮かぶ偉大な三角形。",
        "example": "The pediment of the building features a sculpture of Justice.",
        "deep_dive": {
            "roots": [{"term": "pyramid", "meaning": "triangle shape"}],
            "points": ["意外にも ped-（足）とは関係なく、ピラミッドの親戚でした。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "portico",
        "word": "Portico",
        "meaning": "ポルティコ(列柱のある玄関のポーチ)",
        "era": "17th Century Italian portico",
        "etymology": {
            "components": ["porticus (porch, colonnade)"],
            "original_statement": "From Italian portico, from Latin porticus (porch, covered walk), from porta (gate, door)."
        },
        "concept": "A roofed porch with columns (柱で支えられた屋根付きの玄関)",
        "thinking": "建物の玄関の前に作られた、円柱（柱廊）が並ぶ屋根付きの威厳あるアプローチ。ホワイトハウスなどの立派な建物の入り口を想像してください。ポーチ（porch）の豪華版。",
        "aftertaste": "扉を開く前の、柱と影のプロローグ。",
        "example": "The senator gave his speech from the portico of the capitol.",
        "deep_dive": {
            "roots": [{"term": "per-", "meaning": "to lead, pass over"}],
            "points": ["porta（門）、port（港/扉）、portal（入り口）とすべて同じ『通り抜ける道』です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "pavilion",
        "word": "Pavilion",
        "meaning": "パビリオン、展示館、東屋、大型テント",
        "era": "13th Century Old French/Latin papilio",
        "etymology": {
            "components": ["papilio (butterfly, tent)"],
            "original_statement": "From Old French paveillon (tent), from Latin papilio (butterfly, tent), reflecting the flapping of the tent's canvas looking like a butterfly's wings."
        },
        "concept": "A tent resembling a butterfly (蝶の羽ばたきに似たテント)",
        "thinking": "万博の「パビリオン」の語源は、なんと「蝶々」。中世の兵士が野営で張った大きなテントの布が風にバサバサと煽られる様を蝶の羽に見立てたという、非常にロマンチックなルーツです。",
        "aftertaste": "風に舞う布の蝶が、いつしか鋼鉄の展示館になった。",
        "example": "The Japanese pavilion at the Expo was a major attraction.",
        "deep_dive": {
            "roots": [{"term": "papilio", "meaning": "butterfly"}],
            "points": ["パピヨン（papillon: フランス語で蝶・犬の品種）と同じ言葉です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "obelisk",
        "word": "Obelisk",
        "meaning": "オベリスク、方尖塔(ほうせんとう)",
        "era": "16th Century Late Latin/Greek obeliskos",
        "etymology": {
            "components": ["obelos (a spit, pointed pillar)"],
            "original_statement": "From Latin obeliscus, from Greek obeliskos (small spit, pointed pillar), diminutive of obelos (pointed pillar, roasting spit)."
        },
        "concept": "A little pointed spit (小さな串焼き用の尖った棒)",
        "thinking": "古代エジプトで太陽神のシンボルとして建てられた巨大な一本石の記念碑。ギリシャ人がそれを見て「お肉を焼く長い鉄串（obelos）みたいだね」と呼んだのが定着してしまったという、意外と俗っぽい命名。",
        "aftertaste": "太陽を貫く神聖なる石を、ギリシャ人は串焼き棒と呼んだ。",
        "example": "The Washington Monument is the world's tallest obelisk.",
        "deep_dive": {
            "roots": [{"term": "obelos", "meaning": "spit, needle"}],
            "points": ["文章校正で使う剣のマーク記号（†）のことも obeliscus と呼びます（刺して消すため）。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "pyramid",
        "word": "Pyramid",
        "meaning": "ピラミッド、金字塔、ピラミッド型のもの",
        "era": "16th Century Latin/Greek pyramis",
        "etymology": {
            "components": ["pyramis (pyramid, wheat-cake)"],
            "original_statement": "From Latin pyramis, from Greek pyramis. Believed by some to be altered from Egyptian 'pimar', or related to a Greek conical wheat-cake."
        },
        "concept": "A monumental structure with a square base (四角い土台の上に立つ巨大なモニュメント)",
        "thinking": "古代エジプトの王の墓。ギリシャ人が日常食べていたピラミッド型の「小麦のパン」に由来するという説が有力です。オベリスクの「串焼き」と同様、ギリシャ人はエジプトの神秘をキッチン用品で命名しました。",
        "aftertaste": "何トンもの石積みが作り出す、究極に安定した永遠の幾何学。",
        "example": "The food pyramid represents a healthy diet.",
        "deep_dive": {
            "roots": [{"term": "pyros", "meaning": "wheat (possibly)"}],
            "points": ["現代では組織の構造や『ヒエラルキー』の完璧な比喩として使われます。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "maze",
        "word": "Maze",
        "meaning": "迷路、迷宮、複雑に絡み合ったもの",
        "era": "13th Century Middle English mased",
        "etymology": {
            "components": ["masen (to confuse, bewilder)"],
            "original_statement": "From Middle English mase (confused state, delusion), from masen (to confuse, daze), of obscure origin."
        },
        "concept": "A confusing network of paths (人を混乱させる道のネットワーク)",
        "thinking": "Labyrinthが「中に入って神聖な体験をする一本道の回廊」だったのに対し、Mazeは「行き止まりや分岐があり、騙して迷わせる（amaze）ためのパズル」。遊園地などの「迷路」はアミューズメントとしてのMazeです。",
        "aftertaste": "行き止まりと錯覚で作られた、知恵の檻。",
        "example": "The laboratory mice ran through the maze to find cheese.",
        "deep_dive": {
            "roots": [{"term": "maze", "meaning": "delusion, bewilderment"}],
            "points": ["『めっちゃ驚く、感嘆させる（amazing）』は、この『頭を混乱させる・迷宮に入れる』という感覚から来ています。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "balcony",
        "word": "Balcony",
        "meaning": "バルコニー、(劇場などの)階上席",
        "era": "17th Century Italian balcone",
        "etymology": {
            "components": ["balcone (scaffold, balcony)", "balk (beam, log)"],
            "original_statement": "From Italian balcone, from a Germanic source *balko (beam, log, ridge)."
        },
        "concept": "A platform built on wooden beams (木の梁で作られた張り出し舞台)",
        "thinking": "元々は「木の丸太や太い梁（balk）」が壁を突き抜けて支えている構造。建物の外側に空中に張り出すロマンチックな場所ですが、ルーツはゲルマン系の無骨な「丸太ん棒」です。",
        "aftertaste": "壁の外の世界に一歩踏み出すための、空中の小さな舞台。",
        "example": "Romeo stood below Juliet's balcony.",
        "deep_dive": {
            "roots": [{"term": "bhelg-", "meaning": "beam, plank"}],
            "points": ["balk（ためらう/障害になる）と同じゲルマン系の『丸太』がルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "terrace",
        "word": "Terrace",
        "meaning": "テラス、(斜面の)段丘、階段状の構造",
        "era": "16th Century French terrasse",
        "etymology": {
            "components": ["terra (earth, land)"],
            "original_statement": "From French terrasse (a raised level place), from Old Occitan terrassa, from Latin terra (earth)."
        },
        "concept": "A raised and leveled earth (平らに盛り上げられた土)",
        "thinking": "大地（terra）に土を盛って作られた平らで少し高くなった場所。山の斜面の「段々畑（terraced fields）」や、家から庭に続く高台のこと。木で作られたデッキや空中バルコニーとは違い、ルーツは「土」です。",
        "aftertaste": "大地を平らに削り、人間が歩くためのステージにする。",
        "example": "We sat on the terrace sipping coffee and watching the sunset.",
        "deep_dive": {
            "roots": [{"term": "ters-", "meaning": "to dry (terra means dry land)"}],
            "points": ["地球（terrestrial）や領土（territory）と同じ『土（terra）』ファミリーです。"]
        },
        "part_of_speech": "noun"
    }
]

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'(const WORDS = )(\[.*\])(;)', text, re.DOTALL)
if match:
    prefix = match.group(1)
    json_array_str = match.group(2)
    suffix = match.group(3)
    
    existing_words = json.loads(json_array_str)
    existing_ids = {w.get("id", "") for w in existing_words}
    
    added_count = 0
    for new_word in word_batch:
        if new_word["id"] not in existing_ids:
            existing_words.append(new_word)
            added_count += 1
            
    updated_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
    updated_text = text[:match.start()] + prefix + updated_json_str + suffix + text[match.end():]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_text)
    
    print(f"Success: Processed {len(word_batch)} words. Added {added_count} words.")
else:
    print("Failed to find or parse WORDS array in data.js.")
