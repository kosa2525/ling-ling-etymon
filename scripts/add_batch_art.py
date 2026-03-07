import json
import re

word_batch = [
    {
        "id": "aesthetic",
        "word": "Aesthetic",
        "meaning": "美的な、審美的な、美学",
        "era": "18th Century German Ästhetisch/Greek aisthetikos",
        "etymology": {
            "components": ["aisthanesthai (to perceive, feel)"],
            "original_statement": "Coined in 1750 by German philosopher Alexander Baumgarten from Greek aisthetikos (sensitive, perceptive), from aisthanesthai (to perceive by the senses or mind)."
        },
        "concept": "Perceiving through the senses (感覚を通して知覚すること)",
        "thinking": "元々のギリシャ語では単なる「感覚」を意味していましたが、ドイツの哲学者が「感覚を通して美を感じ取る学問（美学）」として使い始めました。麻酔（anesthesia：感覚がないこと）の反対語であり、心が美に対して『敏感に疼くこと』です。",
        "aftertaste": "美とは論理ではなく、感覚の震えである。",
        "example": "The new building has little aesthetic appeal.",
        "deep_dive": {
            "roots": [{"term": "au-", "meaning": "to perceive"}],
            "points": ["anesthesia（麻酔：an- 否定 + esthesia 感覚）と完全に裏返しの関係です。"]
        },
        "part_of_speech": "adjective"
    },
    {
        "id": "muse",
        "word": "Muse",
        "meaning": "ミューズ(芸術の女神)、インスピレーションの源",
        "era": "14th Century Old French/Latin/Greek Mousa",
        "etymology": {
            "components": ["Mousa (Muse)"],
            "original_statement": "From Old French muse, from Latin musa, from Greek Mousa (the Muses, goddesses of inspiration, poetry, and art), possibly related to *men- (to think)."
        },
        "concept": "The goddess of inspiration (インスピレーションの女神)",
        "thinking": "ギリシャ神話で、芸術家たちに突如として素晴らしいアイデアを吹き込む九柱の女神たち。転じて、芸術家が「創作活動の源・インスピレーションの対象とする実在の人物（しばしば恋人など）」を指します。",
        "aftertaste": "彼女が微笑んだ時、キャンバスに色が落ちた。",
        "example": "The young artist considered his wife to be his primary muse.",
        "deep_dive": {
            "roots": [{"term": "men-", "meaning": "to think"}],
            "points": ["museum（博物館：ミューズの神殿）や music（音楽：ミューズの芸術）の語源です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "canvas",
        "word": "Canvas",
        "meaning": "キャンバス、油絵の具用の画布、テント生地",
        "era": "13th Century Old North French/Latin cannabis",
        "etymology": {
            "components": ["cannabis (hemp)"],
            "original_statement": "From Old North French canevas, from Vulgar Latin *cannapaceus (made of hemp), from Latin cannabis (hemp)."
        },
        "concept": "Made of hemp (大麻の繊維で作られたもの)",
        "thinking": "驚くべきことに、テントや絵を描く『キャンバス』の語源は、マリファナでお馴染みの『大麻（cannabis）』です。大麻の茎の繊維から作られた、非常に丈夫で破れにくい粗い布だったのです。",
        "aftertaste": "すべての名画は、丈夫な麻の布の上に描かれた。",
        "example": "He stared at the blank canvas, waiting for inspiration.",
        "deep_dive": {
            "roots": [{"term": "cannabis", "meaning": "hemp"}],
            "points": ["選挙の『遊説、票集め（canvass）』も、元は粗いキャンバス布で篩（ふるい）にかけるところから。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "palette",
        "word": "Palette",
        "meaning": "パレット(絵の具の調色板)、(使用する)色彩の範囲",
        "era": "17th Century French/Latin pala",
        "etymology": {
            "components": ["pala (spade, shovel)"],
            "original_statement": "From French palette, diminutive of pale (spade, shovel), from Latin pala (spade)."
        },
        "concept": "A small flat spade (小さな平たいシャベル)",
        "thinking": "絵の具を混ぜ合わせるための平らな板。元々は土を掘る『小さな平たいシャベル（shovel/spade）』を意味しました。転じて、その画家が好んで使う『色彩の組み合わせセット全体』や、料理人の『味覚の幅』という意味でも用いられます。",
        "aftertaste": "シャベル一杯の絵の具から、無限の宇宙が広がる。",
        "example": "The designer chose a cool color palette for the winter collection.",
        "deep_dive": {
            "roots": [{"term": "pala", "meaning": "spade"}],
            "points": ["palate（口蓋：味覚の好み）と発音が同じですが、全く別の言葉です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "pigment",
        "word": "Pigment",
        "meaning": "顔料、色素",
        "era": "14th Century Latin pigmentum",
        "etymology": {
            "components": ["pingere (to paint)"],
            "original_statement": "From Latin pigmentum (color, paint, dye), from pingere (to paint, decorate), from PIE root *peig- (to cut, mark by incision)."
        },
        "concept": "Something used to paint (塗るために使われるもの)",
        "thinking": "鉱物や植物から抽出された、世界に『色』を与えるための魔法の粉。細胞に含まれるメラニンなどの「色素」も指します。古代の絵画は「彫り込む・刻み込む（peig-）」行為と等しかったという古い印欧語の記憶を残しています。",
        "aftertaste": "砕かれた鉱物が、壁の上に永遠の青を刻む。",
        "example": "Many ancient pigments were derived from crushed rocks and minerals.",
        "deep_dive": {
            "roots": [{"term": "peig-", "meaning": "to mark by incision, paint"}],
            "points": ["paint（塗る）や picture（絵）と同じルーツから生まれた『顔料』です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "fresco",
        "word": "Fresco",
        "meaning": "フレスコ画(漆喰が乾ききらないうちに描く壁画)",
        "era": "16th Century Italian affresco",
        "etymology": {
            "components": ["fresco (fresh)"],
            "original_statement": "From Italian (dipinto) a fresco (painted 'in the fresh'), referring to painting on wet, freshly laid plaster."
        },
        "concept": "Painted on the fresh plaster (新鮮な漆喰の上に描かれたもの)",
        "thinking": "壁に塗られた漆喰（セメントのようなもの）が、まだ乾かずに「新鮮（fresh）」で濡れているうちに急いで色（pigment）を染み込ませて描く最高難度の技法。壁そのものが絵になるため、何百年も色が落ちません。",
        "aftertaste": "壁が乾く前に、神々の命を染み込ませよ。",
        "example": "Michelangelo's frescoes in the Sistine Chapel are world-renowned.",
        "deep_dive": {
            "roots": [{"term": "fresco", "meaning": "fresh"}],
            "points": ["まさに fresh（新鮮な）と同じゲルマン系の源流です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "mosaic",
        "word": "Mosaic",
        "meaning": "モザイク(多数の小片を寄せ合わせて絵や模様としたもの)",
        "era": "14th Century Old French/Medieval Latin musaicus",
        "etymology": {
            "components": ["Mousa (Muse)"],
            "original_statement": "From Old French mosaïque, from Medieval Latin musaicus (work of the Muses), an alteration of Late Latin musivum (opus) (mosaic work), ultimately from Greek Mousa (Muse)."
        },
        "concept": "Work of the Muses (ミューズの芸術作品)",
        "thinking": "小さなガラスや石の破片を無数に並べて作られた絵。驚くことに、語源は美術館（museum）や音楽（music）と同じく、芸術の女神「ミューズ（Mousa）」の御業（みわざ）という言葉です。",
        "aftertaste": "砕かれた数万の石が、集まって女神の顔になる。",
        "example": "The bathhouse was decorated with an intricate Roman mosaic.",
        "deep_dive": {
            "roots": [{"term": "men-", "meaning": "to think"}],
            "points": ["全く関係ない言葉に見えて、music と姉妹だというのが言語の面白さです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "portrait",
        "word": "Portrait",
        "meaning": "肖像画、(人物の)描写",
        "era": "16th Century French/Latin protrahere",
        "etymology": {
            "components": ["pro- (forth)", "trahere (to draw, drag)"],
            "original_statement": "From French portrait, past participle of portraire (to portray, draw), from Latin protrahere (to draw forth, reveal, expose), from pro- (forth) + trahere (to drag, draw)."
        },
        "concept": "Something drawn forth (引き出されたもの、暴かれたもの)",
        "thinking": "ただ顔の形を写し取る（copy）のではなく、その人の内面にある性格や魂、隠された本質などを線の力で『外に引きずり出して（pro-trahere）定着させる』という、恐るべき芸術行為。",
        "aftertaste": "絵筆とは、魂の輪郭を外界に引きずり出す釣り針だ。",
        "example": "Mona Lisa is perhaps the most famous portrait in the world.",
        "deep_dive": {
            "roots": [{"term": "tragh-", "meaning": "to draw, drag, move"}],
            "points": ["tractor（引っ張る車）や attract（惹きつける）の『引く』という物理的な力が語源です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "caricature",
        "word": "Caricature",
        "meaning": "風刺画、カリカチュア、デフォルメされた絵",
        "era": "18th Century Italian caricatura",
        "etymology": {
            "components": ["caricare (to load, exaggerate)"],
            "original_statement": "From Italian caricatura (a satirical picture, an overloading), from caricare (to load, exaggerate), from Late Latin carricare (to load a cart), from carrus (wagon, cart)."
        },
        "concept": "An overloaded picture (荷物が積みすぎられた絵＝誇張された絵)",
        "thinking": "その人の特徴的なパーツ（大きな鼻やりんかく等）の情報を、馬車に荷物を積みすぎるように『これでもかと過剰に詰め込んで（caricare）誇張した』絵や文章。風刺やユーモアの強力な武器です。",
        "aftertaste": "笑いという名の、過酷な荷物を背負わされた肖像。",
        "example": "The newspaper published a cruel caricature of the prime minister.",
        "deep_dive": {
            "roots": [{"term": "kers-", "meaning": "to run (car)"}],
            "points": ["charge（荷物/充電/突撃）や car（車/荷車）と同じく『重く積む』という意味です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "grotesque",
        "word": "Grotesque",
        "meaning": "グロテスクな、奇怪な、異様な",
        "era": "16th Century Middle French/Italian grottesca",
        "etymology": {
            "components": ["grotta (cave, grotto)"],
            "original_statement": "From Middle French grotesque, from Italian (pittura) grottesca ('cave painting'), from grotta (cave, excavation)."
        },
        "concept": "Cave painting style (洞窟風の、地下から掘り出された奇妙な壁画風の)",
        "thinking": "元々は、ローマ帝国の遺跡の「洞窟（ルネサンス期に発掘された地下遺跡）」から見つかった、人間と動物と植物が奇妙に融合した不気味な古代の装飾模様を指す美術用語。そこから『奇怪で不気味なもの』を意味する一般語になりました。",
        "aftertaste": "地下の暗がりで、ツル草と獣が奇妙に絡み合う。",
        "example": "The gargoyles on the cathedral are famously grotesque.",
        "deep_dive": {
            "roots": [{"term": "krupto", "meaning": "hidden (Greek)"}],
            "points": ["grotto（小さな洞窟）や crypt（地下室）と同じ『地下の隠された場所』というルーツ。"]
        },
        "part_of_speech": "adjective"
    },
    {
        "id": "sublime",
        "word": "Sublime",
        "meaning": "崇高な、荘厳な、(美や感動が)極まった",
        "era": "16th Century French/Latin sublimis",
        "etymology": {
            "components": ["sub- (up to)", "limen (threshold, lintel)"],
            "original_statement": "From Latin sublimis (uplifted, high, exalted), possibly from sub- (up to) + limen (threshold, the lintel above a door)."
        },
        "concept": "Up to the threshold (鴨居の高さまで、極致まで)",
        "thinking": "美しい（Beautiful）という言葉では表現できない、「門の上の高い鴨居（リンテル）にギリギリ届くほどの高さ」。そびえ立つ断崖絶壁や星空を見た時の、少し恐怖すら混じるような『圧倒的で荘厳な感動・畏敬』を指す美学用語です。",
        "aftertaste": "美しすぎて、少しだけ恐ろしい。",
        "example": "The symphony's final movement was truly sublime.",
        "deep_dive": {
            "roots": [{"term": "limen", "meaning": "threshold"}],
            "points": ["limit（限界）と同根。人間のリミット（限界）まで感情が引き上げられた状態です。"]
        },
        "part_of_speech": "adjective"
    },
    {
        "id": "symphony",
        "word": "Symphony",
        "meaning": "交響曲",
        "era": "13th Century Old French/Greek symphonia",
        "etymology": {
            "components": ["syn- (together)", "phone (voice, sound)"],
            "original_statement": "From Old French simphonie, from Latin symphonia, from Greek symphonia (harmony, concert), from syn- (together) + phone (voice, sound)."
        },
        "concept": "Sounding together (共に響き合うこと)",
        "thinking": "何十種類もの全く違う楽器。バイオリンの絹の音色、トランペットの金管の咆哮、ティンパニーの雷鳴。それらがステージの上で完全に『一緒に（syn-）自らの声（phone）を一つに響かせる』オーケストラの奇跡。",
        "aftertaste": "混沌と鳴る百の音が、一本の巨大な光の柱になる。",
        "example": "Beethoven's Ninth Symphony is a masterpiece.",
        "deep_dive": {
            "roots": [{"term": "bha-", "meaning": "to speak, tell, say"}],
            "points": ["telephone（遠くの音）や phonetic（音声の）の『phone』です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "harmony",
        "word": "Harmony",
        "meaning": "調和、和音、協調",
        "era": "14th Century Old French/Greek harmonia",
        "etymology": {
            "components": ["harmos (joint, shoulder)"],
            "original_statement": "From Old French armonie, from Latin harmonia, from Greek harmonia (agreement, concord of sounds), from harmos (joint, fastening)."
        },
        "concept": "A fitting together or a joint (ぴったりとハマる関節)",
        "thinking": "音楽の「和音」だけでなく、人と人との「調和」。語源はなんと『骨の関節（ジョイント）』や釘などの接合部分。でこぼことした二つの骨が、まるで図っていたかのようにピタリと噛み合うその完璧な構造的フィット感が、音の美しい響き合いに例えられました。",
        "aftertaste": "異なるもの同士が、まるで関節のように心地よく噛み合う。",
        "example": "The choir sang in perfect harmony.",
        "deep_dive": {
            "roots": [{"term": "ar-", "meaning": "to fit together"}],
            "points": ["art（芸術）や arm（腕：関節に繋がるもの）、article（関節のようにはまる項目）全ての源流『ar-（ぴったりはまる）』から来ています。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "melody",
        "word": "Melody",
        "meaning": "旋律、メロディー、美しい調べ",
        "era": "13th Century Old French/Greek meloidia",
        "etymology": {
            "components": ["melos (song, tune)", "oide (song, chant)"],
            "original_statement": "From Old French melodie, from Late Latin melodia, from Greek meloidia (singing, chanting), from melos (song, musical phrase) + aeidein (to sing)."
        },
        "concept": "A sung tune (歌われる歌の調べ)",
        "thinking": "Harmony（和音＝縦の重なり）や Rhythm（リズム＝打撃の刻み）とは違い、人間の声に出して『歌い流れる（melos）』単一の美しい音の連続の線（横の広がり）のこと。音楽の「顔」です。",
        "aftertaste": "鼻歌で口ずさめるもの。それが音楽の命の線。",
        "example": "The melody of that song is very catchy.",
        "deep_dive": {
            "roots": [{"term": "melos", "meaning": "limb, musical phrase"}, {"term": "aweid-", "meaning": "to sing"}],
            "points": ["comedy（喜劇）、tragedy（悲劇）、parody（パロディ）の『-dy（歌）』という兄弟たちと血が繋がっています。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "rhythm",
        "word": "Rhythm",
        "meaning": "リズム、律動、(言葉の)韻律",
        "era": "16th Century Middle French/Greek rhythmos",
        "etymology": {
            "components": ["rhein (to flow)"],
            "original_statement": "From Middle French rhythme, from Latin rhythmus, from Greek rhythmos (measured flow, movement), from rhein (to flow)."
        },
        "concept": "Measured flow (規則正しく区切られた流れ)",
        "thinking": "心臓の鼓動も、波の音も、ダンスのステップも。すべては川が『流れる（rhein）』ように、一定の規則的なパルスをもって流れていく。水流の連続性を一定の間隔で区切る数学的な「拍動」のこと。",
        "aftertaste": "トクトクと流れる血液のような、宇宙の基礎鼓動。",
        "example": "He tapped his foot to the rhythm of the music.",
        "deep_dive": {
            "roots": [{"term": "sreu-", "meaning": "to flow"}],
            "points": ["stream（川）や rheumatic（リウマチ：体液が流れる病気）と同じ『流れる』という源泉。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "chorus",
        "word": "Chorus",
        "meaning": "コーラス、合唱、(劇などの)コロス、サビ",
        "era": "16th Century Latin/Greek khoros",
        "etymology": {
            "components": ["khoros (dance, band of dancers and singers)"],
            "original_statement": "From Latin chorus, from Greek khoros (dance in a ring, band of dancers and singers), perhaps related to khoros (enclosed place)."
        },
        "concept": "A band of dancers and singers (踊り歌う人々の集団)",
        "thinking": "元々古代ギリシャの演劇で、円になって踊りながら劇の背景や神の意志を『一斉に歌う集団』のことでした。そのため、みんなで一斉に歌う合唱や、ポップスの『みんなで歌い上げる一番盛り上がる箇所（サビ）』をコーラスと呼びます。",
        "aftertaste": "一人の声が十人に、百人に。円陣になって歌う。",
        "example": "Everybody joined in singing the chorus.",
        "deep_dive": {
            "roots": [{"term": "gher-", "meaning": "to enclose"}],
            "points": ["choreography（振り付け・ダンスの記譜）という言葉にもこの『踊りの円（khoros）』が含まれています。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "rhetoric",
        "word": "Rhetoric",
        "meaning": "修辞学、美辞麗句、説得力",
        "era": "14th Century Old French/Greek rhetorike",
        "etymology": {
            "components": ["rhetor (orator, public speaker)"],
            "original_statement": "From Old French rethorique, from Latin rhetorica, from Greek rhetorike tekhne (art of an orator), from rhetor (public speaker), from eirein (to say, speak)."
        },
        "concept": "The art of the public speaker (演説家の技術)",
        "thinking": "古代ギリシャにおいて、広場で群衆を説得・扇動するための『雄弁術（人に言葉をどう届けるかという技術）』。転じて現在では「（中身を伴わない）言葉の飾り、ごまかしの美辞麗句」という少し皮肉な意味でも使われます。",
        "aftertaste": "剣よりも人を動かす、舌という名の装飾武器。",
        "example": "The politician's speech was full of empty rhetoric.",
        "deep_dive": {
            "roots": [{"term": "were-", "meaning": "to speak"}],
            "points": ["word（言葉）や verb（動詞）と同根の『話す』の最高峰の技術です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "metaphor",
        "word": "Metaphor",
        "meaning": "隠喩、メタファー、比喩",
        "era": "16th Century Middle French/Greek metaphora",
        "etymology": {
            "components": ["meta- (over, across)", "pherein (to carry, bear)"],
            "original_statement": "From Middle French metaphore, from Latin metaphora, from Greek metaphora (a transfer), from metapherein (to transfer, carry over), from meta- (over) + pherein (to carry)."
        },
        "concept": "Carrying across (ある意味を、全く別の言葉に「運び越える」こと)",
        "thinking": "「時」は「金（お金）」である。このように、ある概念（時間）の特徴を、全く別の領域の言葉（金）へと『意味を橋渡しして運ぶ（meta-phor）』という、人間の想像力が生んだ最高の思考・言語ツールです。",
        "aftertaste": "言葉から言葉へ、意味が海を渡って引越しをする。",
        "example": "He used a metaphor to explain the complex concept.",
        "deep_dive": {
            "roots": [{"term": "bher-", "meaning": "to carry"}],
            "points": ["euphoria（多幸感）の phoria や ferry（フェリー）と同じ『運ぶ』を含みます。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "irony",
        "word": "Irony",
        "meaning": "皮肉、風刺、(運命の)皮肉",
        "era": "16th Century Latin/Greek eironeia",
        "etymology": {
            "components": ["eiron (dissembler, someone who feigns ignorance)"],
            "original_statement": "From Latin ironia, from Greek eironeia (dissimulation, assumed ignorance), from eiron (dissembler), a character in Greek comedy who feigned stupidity to outwit arrogant counterparts."
        },
        "concept": "Feigned ignorance (わざと無知を装って相手を出し抜くこと)",
        "thinking": "ソクラテスのように、自分は「何も知らないフリ（eiron）」をして質問し、相手の驕りや矛盾を突く高度なユーモア・知性。自分が思っていることと『真逆のこと』を言って笑わせる知的な皮肉（例：大雨の日に「最高の天気だ！」）。",
        "aftertaste": "あえて逆を言う。その隙間に挟まった真実の鋭さ。",
        "example": "It is an irony that the fire station burned down.",
        "deep_dive": {
            "roots": [{"term": "wer-", "meaning": "to speak, say"}],
            "points": ["ただの悪口（sarcasm）とは違い、文字通りの意味と本音が『逆』になる文学的装置です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "satire",
        "word": "Satire",
        "meaning": "風刺、皮肉、諷刺文学",
        "era": "16th Century French/Latin satira",
        "etymology": {
            "components": ["satur (full, sated)"],
            "original_statement": "From Middle French satire, from Latin satira or satura (a poetic medley, a dish of mixed fruits), later associated with literary criticism, from satur (full, sated)."
        },
        "concept": "A mixed dish full of various things (いろんな果物が雑多に詰まったてんこ盛りの皿)",
        "thinking": "元々はローマ時代、様々な愚かな行いなどを「神々の祭りの供え物のように、色々と混ぜ合わせた（satura）雑多な詩・ごった煮」のこと。そこから、権力者や人間の愚かさを笑い飛ばして批判する『強烈な風刺』へと特化しました。",
        "aftertaste": "愚かさを煮詰め、笑いの皿に盛って権力者に食わせる。",
        "example": "The novel is a biting satire of the political system.",
        "deep_dive": {
            "roots": [{"term": "sa-", "meaning": "to satisfy"}],
            "points": ["satisfy（満たす/満足する）や saturate（飽和する）と同じ『満杯・ごった煮』のサトゥル（satur）が語源です。"]
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
