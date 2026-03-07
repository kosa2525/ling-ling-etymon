import json
import re

word_batch = [
    {
        "id": "biology",
        "word": "Biology",
        "meaning": "生物学",
        "era": "18th Century Greek bios + logia",
        "etymology": {
            "components": ["bios (life)", "-logia (study of)"],
            "original_statement": "Coined independently by several scientists, derived from Greek bios (life) + -logia (study of)."
        },
        "concept": "The study of life (生命の探求)",
        "thinking": "星々の動き（天文学）から始まった科学が、やがて自分たち自身の『生きているという現象（bios）』の解明へと向き直った言葉です。",
        "aftertaste": "命が命を知ろうとする、果てしない自己言及。",
        "example": "Biology reveals the immense complexity of even a single cell.",
        "deep_dive": {
            "roots": [{"term": "gwei-", "meaning": "to live"}],
            "points": ["バイオハザードやバイオテクノロジーの『バイオ』です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "organism",
        "word": "Organism",
        "meaning": "有機体、生物、小さな組織",
        "era": "17th Century Greek organon",
        "etymology": {
            "components": ["organon (instrument, tool, organ)", "-ism"],
            "original_statement": "From French organisme, from Greek organon (instrument, tool, organ of sense or apprehension)."
        },
        "concept": "A complex structure of interdependent instruments (相互依存する道具の複雑な集合体)",
        "thinking": "心臓も肺も胃も、生命を維持するための精巧な『道具・楽器（organon）』。それらが完璧なオーケストラのように統合されたのが有機体（organism）です。",
        "aftertaste": "数億の細胞が奏でる、生命という名の交響曲。",
        "example": "A single-celled organism can adapt to extreme environments.",
        "deep_dive": {
            "roots": [{"term": "werg-", "meaning": "to work"}],
            "points": ["orgasm, organ, energy など『働く・機能する』という太古の語根に由来します。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "cell",
        "word": "Cell",
        "meaning": "細胞、小部屋、電池",
        "era": "12th Century Old French/Latin cella",
        "etymology": {
            "components": ["cella (small room, store room)"],
            "original_statement": "From Latin cella (small room, store room, hut). Robert Hooke applied it in 1665 to biological cells because they resembled monks' quarters."
        },
        "concept": "A small enclosed room (小さく区切られた個室)",
        "thinking": "コルクの顕微鏡写真を見たフックが、それが修道士たちの『小さな個室（cell）』に似ていることから名付けました。生命の最小単位は、小さな部屋だったのです。",
        "aftertaste": "生命はこの小さな部屋から、無限の増築を繰り返す。",
        "example": "Red blood cells carry oxygen throughout the body.",
        "deep_dive": {
            "roots": [{"term": "kel-", "meaning": "to cover, conceal"}],
            "points": ["conceal（隠す）や hell（地獄：隠された場所）と同じルーツを持ちます。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "nucleus",
        "word": "Nucleus",
        "meaning": "核、中心、(細胞)核",
        "era": "17th Century Latin",
        "etymology": {
            "components": ["nux (nut)", "-culus (diminutive)"],
            "original_statement": "From Latin nucleus (kernel, core), literally 'little nut', from nux (nut)."
        },
        "concept": "The little nut inside (内側にある小さな木の実)",
        "thinking": "果実を割った時に出てくる『硬い種（kernel/nut）』。そこから、細胞の中心でありDNAを格納する中枢、あるいは原子核という意味へ広がりました。",
        "aftertaste": "全てを決定づける設計図は、硬いクルミの中に。",
        "example": "The nucleus controls all the cellular activities.",
        "deep_dive": {
            "roots": [{"term": "nux", "meaning": "nut"}],
            "points": ["nuclear（原子核の）という強力な言葉の元ですが、元々はかわいい『小さなクルミ』です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "membrane",
        "word": "Membrane",
        "meaning": "細胞膜、薄膜",
        "era": "15th Century Latin membrana",
        "etymology": {
            "components": ["membrum (limb, member of the body)"],
            "original_statement": "From Latin membrana (skin, parchment, membrane covering parts of the body), from membrum (limb, part of the body)."
        },
        "concept": "Skin covering a member (器官を覆い包む薄い皮)",
        "thinking": "内なる世界（細胞内）と外なる世界を隔てる『薄く柔軟な境界線』。すべてを遮断する壁ではなく、必要な物だけを通す（半透膜）という極めて知的な門番です。",
        "aftertaste": "内と外を分かつ、柔らかで厳格な国境線。",
        "example": "The cell membrane regulates what enters and exits the cell.",
        "deep_dive": {
            "roots": [{"term": "mems-", "meaning": "flesh, meat"}],
            "points": ["member（メンバー/手足）と同じ語源です。構成員という意味もここから。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "mitochondria",
        "word": "Mitochondria",
        "meaning": "ミトコンドリア(細胞のエネルギー工場)",
        "era": "19th Century Greek mitos + chondrion",
        "etymology": {
            "components": ["mitos (thread)", "chondrion (little granule)"],
            "original_statement": "Coined in 1898 by Carl Benda from Greek mitos (thread) + chondrion (little granule), as they looked like threads and granules under a microscope."
        },
        "concept": "Thread-like granules (糸と粒)",
        "thinking": "顕微鏡で見えたそのままの『糸（mito）と粒（chondria）』という名前。しかし彼らは元々別の細菌であり、大昔に私たちの細胞に侵入（共生）して、エネルギー工場として働くようになった異邦人です。",
        "aftertaste": "細胞の奥に潜む、太古からの異星の住民。",
        "example": "Mitochondria are often referred to as the powerhouses of the cell.",
        "deep_dive": {
            "roots": [{"term": "mei-", "meaning": "to tie, bind"}],
            "points": ["母親からのみ遺伝する『ミトコンドリア・イブ』というロマンチックな概念でも知られます。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "genetics",
        "word": "Genetics",
        "meaning": "遺伝学",
        "era": "19th Century Greek genesis",
        "etymology": {
            "components": ["genesis (origin)", "-ics (science of)"],
            "original_statement": "Coined by William Bateson in 1905, from Greek genno (to give birth), related to genesis (origin)."
        },
        "concept": "The science of origin and generation (起源と誕生の科学)",
        "thinking": "親から子へ、何がどのように『生まれ（genesis）』伝わっていくのかの法則を探る学問。運命の暗号を解読する科学です。",
        "aftertaste": "らせん階段を登って、生命の起源へ。",
        "example": "Genetics has revolutionized our understanding of inherited diseases.",
        "deep_dive": {
            "roots": [{"term": "gene-", "meaning": "to give birth, beget"}],
            "points": ["generate（生成する）や generous（気前の良い：血筋が良い）もご先祖は一緒です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "chromosome",
        "word": "Chromosome",
        "meaning": "染色体",
        "era": "19th Century German Chromosom/Greek",
        "etymology": {
            "components": ["khroma (color)", "soma (body)"],
            "original_statement": "Coined by Wilhelm von Waldeyer-Hartz in 1888 from Greek khroma (color) + soma (body), because they were heavily stained by colorful dyes in experiments."
        },
        "concept": "The colored body (色に染まる物体)",
        "thinking": "細胞分裂の時に現れるＸやＹの形をした構造体。実験で「よく色（khroma）に染まる物体（soma）」だったという、観察結果に由来する率直なネーミング。",
        "aftertaste": "染料に浮き上がったのは、運命の文字列。",
        "example": "Humans typically have 23 pairs of chromosomes.",
        "deep_dive": {
            "roots": [{"term": "ghreu-", "meaning": "to rub"}],
            "points": ["chrome（クロム・色彩）と psychosomatic（心身の：soma）の組み合わせです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "genome",
        "word": "Genome",
        "meaning": "ゲノム、全遺伝情報",
        "era": "20th Century German Genom",
        "etymology": {
            "components": ["gen (gene)", "-ome (mass/chromosome)"],
            "original_statement": "Coined by Hans Winkler in 1920, portmanteau of gene and chromosome."
        },
        "concept": "The complete set of genes (遺伝子の総体)",
        "thinking": "一つ一つの遺伝子（gene）の働きではなく、その生物が持つ遺伝情報の『すべて（-ome）』のセット。全図鑑。人間という存在をコードで書き表した絶対的な辞書。",
        "aftertaste": "三十億文字で書かれた、あなたの取扱説明書。",
        "example": "The Human Genome Project mapped all human genes.",
        "deep_dive": {
            "roots": [{"term": "gene-", "meaning": "give birth"}],
            "points": ["biome（バイオーム/生物群系）などの -ome と同じ『全体・総体』の意です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "photosynthesis",
        "word": "Photosynthesis",
        "meaning": "光合成",
        "era": "19th Century Greek photo- + synthesis",
        "etymology": {
            "components": ["photo- (light)", "syn- (together)", "thesis (putting)"],
            "original_statement": "Coined from Greek phos (light) + synthesis (a putting together)."
        },
        "concept": "Putting together with light (光を使って合成すること)",
        "thinking": "無機物である二酸化炭素と水から、太陽の「光」のエネルギーを使って、生命の源である「ブドウ糖（有機物）」を「組み立てる（synthesis）」地球最大の錬金術。",
        "aftertaste": "葉は光を食べる沈黙の錬金術師。",
        "example": "Plants absorb energy from the sun during photosynthesis.",
        "deep_dive": {
            "roots": [{"term": "bha-", "meaning": "to shine"}, {"term": "dhe-", "meaning": "to put"}],
            "points": ["photo- は photograph（光の絵＝写真）などでお馴染みです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "respiration",
        "word": "Respiration",
        "meaning": "呼吸、(細胞の)呼吸作用",
        "era": "14th Century Latin respiratio",
        "etymology": {
            "components": ["re- (again)", "spirare (to breathe)"],
            "original_statement": "From Latin respirationem, from respirare (to breathe again, breathe in and out), from re- (again) + spirare (to breathe)."
        },
        "concept": "Breathing continuously (絶え間なく息をすること)",
        "thinking": "空気を吸って吐く行為。しかし細胞レベルでの呼吸（Cellular respiration）は、有機物を燃やしてエネルギーを取り出すダイナミックな燃焼のことを指します。",
        "aftertaste": "一息ごとに、細胞の中で小さな火が燃える。",
        "example": "Cellular respiration produces ATP, the energy currency of cells.",
        "deep_dive": {
            "roots": [{"term": "spirare", "meaning": "to breathe"}],
            "points": ["spirit（魂＝息）や inspire（息を吹き込む）、expire（息を引き取る）の兄弟です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "metabolism",
        "word": "Metabolism",
        "meaning": "代謝、新陳代謝",
        "era": "19th Century French/Greek metabole",
        "etymology": {
            "components": ["meta- (change, over)", "ballein (to throw)"],
            "original_statement": "From French métabolisme, from Greek metabolē (change, transition), from metaballein (to change, turn about), from meta- (over) + ballein (to throw)."
        },
        "concept": "Throwing over into something new (投げて新しいものに変える)",
        "thinking": "食べたものを壊してエネルギーに投げ変えたり、古い細胞を捨てて新しい姿に作り変えたりし続けること。生命とは固定された物体ではなく、代謝という『絶え間ない川の流れ』のような現象です。",
        "aftertaste": "昨日の私は、今日の私ではない。",
        "example": "Exercise can help speed up your metabolism.",
        "deep_dive": {
            "roots": [{"term": "gwele-", "meaning": "to throw"}],
            "points": ["メタ（meta-: 変化・超越）とボール（ball: 投げる）の組み合わせ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "symbiosis",
        "word": "Symbiosis",
        "meaning": "共生",
        "era": "19th Century Greek",
        "etymology": {
            "components": ["syn- (together)", "bios (life)", "-osis (process)"],
            "original_statement": "From Greek symbiōsis (a living together), from syn- (together) + bios (life)."
        },
        "concept": "Living together (共に生きること)",
        "thinking": "異なる種類の生物が、お互いに影響を与え合いながら密接に一緒に暮らすこと。助け合う場合（相利）も、片方が奪う場合（寄生）も含めた広い概念です。",
        "aftertaste": "ひとりでは、到底生きられないように設計されている。",
        "example": "The clownfish and the sea anemone live in perfect symbiosis.",
        "deep_dive": {
            "roots": [{"term": "gwei-", "meaning": "to live"}],
            "points": ["シンフォニー（symphony: 共に響く）や シリアス（syn-）と同じ『一緒に』です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "mutualism",
        "word": "Mutualism",
        "meaning": "相利共生",
        "era": "19th Century French mutualisme",
        "etymology": {
            "components": ["mutuus (reciprocal, done in exchange)"],
            "original_statement": "From French mutualisme, from Latin mutuus (reciprocal, borrowed), related to mutare (to change, exchange)."
        },
        "concept": "Reciprocal exchange of life benefits (生存の利益を相互に交換すること)",
        "thinking": "ミツバチが花の蜜をもらう代わりに花粉を運ぶように、全く違う種族がお互いに『Win-Win』の関係を築く奇跡。自然界の美しいギブアンドテイク。",
        "aftertaste": "花は蜜を準備し、蜂の羽ばたきを待つ。",
        "example": "The relationship between bees and flowers is a classic example of mutualism.",
        "deep_dive": {
            "roots": [{"term": "mei-", "meaning": "to change, exchange"}],
            "points": ["migrate（移動する）や mutate（変化する）と同根の『交換・変化』がベースです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "commensalism",
        "word": "Commensalism",
        "meaning": "片利共生(一方が利益を得て、片方は害も益も受けない関係)",
        "era": "19th Century Latin",
        "etymology": {
            "components": ["com- (together)", "mensa (table)"],
            "original_statement": "From Medieval Latin commensalis (sharing a table), from com- (together) + mensa (table)."
        },
        "concept": "Eating at the same table (同じ食卓について食べる)",
        "thinking": "一方は利益を得るが、もう一方は特に迷惑をしていない関係（サメのおこぼれをもらうコバンザメなど）。『同じテーブルについてご飯を食べる（けど別に相手の分は奪わない）』というおだやかな語源。",
        "aftertaste": "同じテーブルで、静かにおこぼれを頂戴する。",
        "example": "Barnacles riding on a whale's skin is a form of commensalism.",
        "deep_dive": {
            "roots": [{"term": "mensa", "meaning": "table"}],
            "points": ["『同じ釜の飯を食う』の西洋版です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "parasite",
        "word": "Parasite",
        "meaning": "寄生生物、居候",
        "era": "16th Century Latin/Greek parasitos",
        "etymology": {
            "components": ["para- (beside)", "sitos (grain, food)"],
            "original_statement": "From Latin parasitus, from Greek parasitos (one who eats at the table of another), from para- (beside) + sitos (food)."
        },
        "concept": "One who eats beside you (隣に座って他人の食べ物を食べる者)",
        "thinking": "元々は古代ギリシャで、富裕層の食事に「横槍を入れてタダ飯を食う取り巻き（居候）」のことでした。それが生物学で、宿主の栄養を奪い取る無慈悲な侵入者の名前に変わりました。",
        "aftertaste": "他者の命を削り、我が命を太らせる。",
        "example": "The tick is a parasite that feeds on the blood of its host.",
        "deep_dive": {
            "roots": [{"term": "sitos", "meaning": "food"}],
            "points": ["パラレル（parallel: 平行・隣り合う）の para（横）です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "host",
        "word": "Host",
        "meaning": "宿主、(パーティーなどの)主催者",
        "era": "13th Century Old French/Latin hospes",
        "etymology": {
            "components": ["hospes (guest, host, stranger)"],
            "original_statement": "From Old French oste (host, guest), from Latin hospes (guest, stranger, host), from PIE *ghos-ti- (stranger, guest, host)."
        },
        "concept": "One who receives strangers (よそ者を受け入れる者)",
        "thinking": "パラサイト（寄生虫）やウイルスに「住み着かれる側」の生物を生物学ではホストと呼びます。語源は『見知らぬ客をもてなす主人』。ウイルスさえも客として受け入れざるを得ない体の悲劇。",
        "aftertaste": "望まぬ客でさえ、体内（ホテル）に招き入れてしまう。",
        "example": "A virus needs a host cell to replicate.",
        "deep_dive": {
            "roots": [{"term": "ghosti-", "meaning": "stranger, guest, host"}],
            "points": ["guest（客）と host（主人）は実は全く同じ語源。ホスピタリティ（hospitality）もここからです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "ecosystem",
        "word": "Ecosystem",
        "meaning": "エコシステム、生態系",
        "era": "20th Century English eco- + system",
        "etymology": {
            "components": ["oikos (house, environment)", "system"],
            "original_statement": "Coined in 1935 by British ecologist Arthur Tansley from eco- (from Greek oikos 'house, habitat') + system."
        },
        "concept": "The household system (自然という家計・システム)",
        "thinking": "ただ生物が集まっているだけでなく、光や水や土という『非生物』も含めて、一つの大きな『経済（家計）』みたいに完璧にエネルギーが循環しているシステム。IT業界などの『巨大な経済圏』の比喩としても使われます。",
        "aftertaste": "すべてが繋がり、無駄なものは一つもない完璧な家。",
        "example": "The rainforest is the most complex ecosystem on Earth.",
        "deep_dive": {
            "roots": [{"term": "weik-", "meaning": "clan, house"}],
            "points": ["economic（経済）の eco- と同じく『家計・家の管理』が語源です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "habitat",
        "word": "Habitat",
        "meaning": "生息地、居住地",
        "era": "18th Century Latin",
        "etymology": {
            "components": ["habitare (to dwell, inhabit)"],
            "original_statement": "From Latin habitat (it inhabits), third person singular present indicative of habitare (to live, dwell)."
        },
        "concept": "It inhabits (彼が『住み着く場所』)",
        "thinking": "元々は植物図鑑などで「この種は水辺に habitare（住む）」とラテン語で書かれていたのがそのまま名詞化しました。その生物が生きるための条件が揃った自然の「住所」。",
        "aftertaste": "住所を持たない生物など、存在しない。",
        "example": "Deforestation is destroying the habitat of many endangered species.",
        "deep_dive": {
            "roots": [{"term": "ghabh-", "meaning": "to give or receive (have)"}],
            "points": ["habit（習慣：心に住み着いたもの）や inhabitant（住民）と同根です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "niche",
        "word": "Niche",
        "meaning": "ニッチ、(生態的)地位、最適な場所、隙間市場",
        "era": "17th Century French niche",
        "etymology": {
            "components": ["nidus (nest)"],
            "original_statement": "From French niche (recess for a dog or a statue), probably from Old French nichier (to make a nest), from Latin nidus (nest)."
        },
        "concept": "A small nest or recess (小さな巣、あるいは壁の窪み)",
        "thinking": "元々は壁に彫像を飾るための「くぼみ」。生物学では、その環境の中で『その種が果たす独自の役割・居場所』のこと。「ニッチな趣味」とは、大きな壁の小さな窪みのように、狭いが確実にハマる場所を指します。",
        "aftertaste": "どんな生物にも、必ずパズルのピースのようにハマる窪みがある。",
        "example": "The species evolved to fill a specific ecological niche.",
        "deep_dive": {
            "roots": [{"term": "nizdo-", "meaning": "nest"}],
            "points": ["nest（鳥の巣）と同じ語源です。自分の役割の『巣』ですね。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "predator",
        "word": "Predator",
        "meaning": "捕食者、天敵",
        "era": "20th Century Latin praedator",
        "etymology": {
            "components": ["praeda (booty, prey)"],
            "original_statement": "From Latin praedator (plunderer), from praedari (to rob, catch as prey), from praeda (booty, prey)."
        },
        "concept": "A plunderer (略奪する者)",
        "thinking": "他の生物を捉えて餌にする生き物。元々のラテン語では『戦利品を略奪する者（泥棒）』という非常に人間くさい（軍事的な）言葉でした。生態系のバランスを保つ頂点に立つ者たち。",
        "aftertaste": "命を略奪すること。それは連鎖の頂点に課せられた業。",
        "example": "The lion is the apex predator of the savanna.",
        "deep_dive": {
            "roots": [{"term": "ghend-", "meaning": "to seize, take"}],
            "points": ["prey（獲物・戦利品）を狩る者、という意味構造です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "prey",
        "word": "Prey",
        "meaning": "獲物、犠牲者",
        "era": "13th Century Old French/Latin praeda",
        "etymology": {
            "components": ["praeda (booty, plunder)"],
            "original_statement": "From Old French preie (booty, animal taken in hunting), from Latin praeda (booty, plunder)."
        },
        "concept": "Booty or plunder (狩りや戦の戦利品)",
        "thinking": "捕食者（predator）の対義語。残酷な自然界において、強者の胃袋に収まることを運命づけられた存在。人間社会でも、詐欺などの「食い物にされる犠牲者」として用いられます。",
        "aftertaste": "牙を向けられた瞬間、すべての命は等しく戦利品となる。",
        "example": "The eagle swooped down to catch its prey.",
        "deep_dive": {
            "roots": [{"term": "ghend-", "meaning": "to seize"}],
            "points": ["pray（祈る）と発音は同じですが、全く関係ありません。祈っても彼らは逃げられないのです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "evolution",
        "word": "Evolution",
        "meaning": "進化、発展、展開",
        "era": "17th Century Latin evolutio",
        "etymology": {
            "components": ["ex- (out)", "volvere (to roll)"],
            "original_statement": "From Latin evolutionem (an unrolling, of a book), from evolvere (to unroll), from ex- (out) + volvere (to roll)."
        },
        "concept": "The unrolling of a scroll (巻物を展開すること)",
        "thinking": "元々の意味は「巻物をコロコロと広げて読んでいくこと」。つまり、生物が持っている内なる可能性の種（暗号）を、長い時間をかけて外に広げていき、新しい姿を展開させていくという美しい語源です。",
        "aftertaste": "数億年かけて巻物を開き、命の続きを書き足す。",
        "example": "Darwin's theory of evolution explains the diversity of life.",
        "deep_dive": {
            "roots": [{"term": "wel-", "meaning": "to turn, roll"}],
            "points": ["revolve（回転する）や volume（巻物の量）と同じく『巻いたものを転がす』ことが起源です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "mutation",
        "word": "Mutation",
        "meaning": "突然変異、変化",
        "era": "14th Century Latin mutatio",
        "etymology": {
            "components": ["mutare (to change)"],
            "original_statement": "From Latin mutationem (a changing, alteration), from mutare (to change)."
        },
        "concept": "A sudden genetic change (遺伝的な急激な変化)",
        "thinking": "DNAのコピーミスという偶然の「変更（mutare）」。しかしそのミスの積み重ねこそが、劇的な環境の変化を乗り越えて新しい種を生み出す（進化する）唯一の原動力なのです。失敗こそが進歩の鍵。",
        "aftertaste": "神の書き間違いが、新しい翼を作る。",
        "example": "A genetic mutation causes the disease.",
        "deep_dive": {
            "roots": [{"term": "mei-", "meaning": "to change, exchange"}],
            "points": ["mutual（相互の）や commute（通勤する: 場所を変える）と同じ根です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "adaptation",
        "word": "Adaptation",
        "meaning": "適応、順応、脚色",
        "era": "17th Century French/Latin adaptatio",
        "etymology": {
            "components": ["ad- (to, toward)", "aptare (to fit, join)"],
            "original_statement": "From Late Latin adaptationem, from Latin adaptare (to fit, adjust), from ad- (to) + aptare (to fit)."
        },
        "concept": "Fitting towards an environment (環境に向けてぴったりと適合させること)",
        "thinking": "冷たい海や乾燥した砂漠など、与えられた過酷な環境に合わせて、自らの肉体のデザインを『ピタリと継ぎ合わせる（aptare）』こと。映画の「脚色」も、原作を映画という環境に合わせることです。",
        "aftertaste": "生き残るために、世界の一部に自分を削る。",
        "example": "The camel's hump is an adaptation for surviving in the desert.",
        "deep_dive": {
            "roots": [{"term": "ap-", "meaning": "to grasp, take, reach"}],
            "points": ["aptitude（適性）や apt（適切な）と同じく『ピタリとハマる』というルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "extinction",
        "word": "Extinction",
        "meaning": "絶滅、消滅、(火や光の)消灯",
        "era": "15th Century Latin extinctio",
        "etymology": {
            "components": ["ex- (out)", "stinguere (to prick, quench)"],
            "original_statement": "From Latin extinctionem (a quenching, putting out), from extinguere (put out, destroy), from ex- (out) + stinguere (to quench). "
        },
        "concept": "The extinguishing of a flame (火が完全に消し止められること)",
        "thinking": "元々は「ろうそくなどの火を（水をかけて）ジュッと消す」という意味。ある生物種の最後の生き残りが死に絶え、地球の歴史上からその命の「火がプツンと消えて永遠の闇になる」こと。",
        "aftertaste": "最後の一匹の火が消え、冷たい図鑑に記録される。",
        "example": "Dinosaurs faced a mass extinction 65 million years ago.",
        "deep_dive": {
            "roots": [{"term": "steig-", "meaning": "to stick, prick"}],
            "points": ["火を消す extinguisher（消火器）と同じ言葉です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "species",
        "word": "Species",
        "meaning": "種(しゅ)、種類",
        "era": "14th Century Latin species",
        "etymology": {
            "components": ["specere (to look at, see)"],
            "original_statement": "From Latin species (appearance, form, kind), from specere (to look at, see, behold)."
        },
        "concept": "A specific appearance or kind (見た目の違いによる種類)",
        "thinking": "交配して子孫を残せるかどうかの生物分類上の基本単位。元々は「見て（specere）パッと分かる外見のデザイン・種類」のことでした。見るという人間の視覚から生まれた分類法。",
        "aftertaste": "見た目が違う。だから違う名前を付ける。",
        "example": "There are estimated to be over 8 million species on Earth.",
        "deep_dive": {
            "roots": [{"term": "spek-", "meaning": "to observe"}],
            "points": ["special（特別な）、spectacle（光景）、inspect（調べる）などの『見る・視界』の王道ファミリーです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "genus",
        "word": "Genus",
        "meaning": "属(ぞく)、部類",
        "era": "16th Century Latin genus",
        "etymology": {
            "components": ["genus (birth, descent, origin)"],
            "original_statement": "Directly from Latin genus (birth, descent, origin, kind, family)."
        },
        "concept": "Family or descent group (生まれ・血筋によるグループ)",
        "thinking": "Species（種）の一つ上の分類。見た目の違い（外見）であるspeciesに対し、Genusは「同じ血筋・生まれ（birth）である親戚の集まり」という、より深いルーツに着目した言葉です。",
        "aftertaste": "見た目が違えど、遠き祖先を同じくする兄弟。",
        "example": "Humans belong to the genus Homo.",
        "deep_dive": {
            "roots": [{"term": "gene-", "meaning": "to give birth, beget"}],
            "points": ["general（一般的な：全体に共通する）や generate（発生する）などの、あらゆる誕生の源流です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "taxonomy",
        "word": "Taxonomy",
        "meaning": "分類学、分類",
        "era": "19th Century French taxonomie",
        "etymology": {
            "components": ["taxis (arrangement)", "-nomia (method)"],
            "original_statement": "Coined in French in 1813 by A.P. de Candolle from Greek taxis (arrangement, order) + -nomia (method, law)."
        },
        "concept": "The law of arrangement (秩序立てて並べる法則)",
        "thinking": "何百万という生物たちを、似たもの同士でフォルダ分けして名前をつけ、宇宙の混沌に「人間としての秩序（Taxis）とルール（Nomos）」をもたらす学問。名前を与えるという知の極致。",
        "aftertaste": "混沌としたジャングルに、本棚のラベルを貼る行為。",
        "example": "In taxonomy, organisms are classified into hierarchical groups.",
        "deep_dive": {
            "roots": [{"term": "tag-", "meaning": "to set in order"}, {"term": "nem-", "meaning": "assign, allot"}],
            "points": ["タクシー（taxi）は税金など『決められた料金（taxis）』から来ており、遠い親戚です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "fossil",
        "word": "Fossil",
        "meaning": "化石、古臭い人や物",
        "era": "16th Century French/Latin fossilis",
        "etymology": {
            "components": ["fodere (to dig)"],
            "original_statement": "From French fossile, from Latin fossilis (obtained by digging), from fodere (to dig)."
        },
        "concept": "Something obtained by digging (掘り出されたもの)",
        "thinking": "元々は石炭から鉱石まで、とにかく「地中から掘り出された（fodere）面白いもの」を全て意味しました。それが何千万年も石の下で眠っていた古代の生き物の痕跡（化石）を指すようになりました。",
        "aftertaste": "岩になった時間は、ハンマーで叩くまで目を覚まさない。",
        "example": "The dinosaur fossil provided new insights into prehistoric life.",
        "deep_dive": {
            "roots": [{"term": "bhedh-", "meaning": "to pierce, dig"}],
            "points": ["fossilize（化石化する・考えなどが硬直化する）という比喩表現も面白いです。"]
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
