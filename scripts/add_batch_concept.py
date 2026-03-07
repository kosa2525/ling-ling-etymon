import json
import re

word_batch = [
    {
        "id": "epiphany",
        "word": "Epiphany",
        "meaning": "突然のひらめき、直感的な真理の把握",
        "era": "14th Century Latin/Greek epiphaneia",
        "etymology": {
            "components": ["epi- (on, to)", "phainein (to show)"],
            "original_statement": "From Greek epiphaneia (manifestation, appearance), from epi- (on, to) + phainein (to show)."
        },
        "concept": "A sudden manifestation or showing (突然の現れ)",
        "thinking": "本来は神が人の前に姿を現す「顕現」を意味した宗教用語。そこから転じて、日常の何気ない瞬間に、突然真理や隠された意味が「パッと目の前に現れる」ような強烈なひらめき体験を指します。",
        "aftertaste": "世界が突然、意味を持って網膜に焼き付く。",
        "example": "He had an epiphany about his true purpose in life.",
        "deep_dive": {
            "roots": [{"term": "bha-", "meaning": "to shine"}],
            "points": ["現象（phenomenon）や幽霊（phantom）とも同根、つまり『見えるもの』という源流です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "revelation",
        "word": "Revelation",
        "meaning": "啓示、暴露、驚くべき新事実",
        "era": "14th Century Old French/Latin revelatio",
        "etymology": {
            "components": ["re- (back)", "velare (to cover, veil)"],
            "original_statement": "From Latin revelationem, from revelare (unveil, uncover), from re- (opposite) + velare (to cover)."
        },
        "concept": "Drawing back the veil (ベールを引き剥がすこと)",
        "thinking": "覆い隠されていた真実の布（ベール）をサッと引き剥がし（Re-）、初めて全貌があらわになる瞬間。これも神の啓示から日常の驚きへとスケールダウンした言葉です。",
        "aftertaste": "布が落ち、隠されていた真実が冷たく輝く。",
        "example": "The book was a revelation to me.",
        "deep_dive": {
            "roots": [{"term": "weg-", "meaning": "to weave"}],
            "points": ["reveal（明らかにする）の名詞形であり、文字通り『覆いの向こう側』を意味します。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "insight",
        "word": "Insight",
        "meaning": "洞察、見抜く力、直感",
        "era": "12th Century Middle English innsight",
        "etymology": {
            "components": ["in- (in, inner)", "sight (vision)"],
            "original_statement": "From Middle English innsight (inner sight, sight with the eyes of the mind)."
        },
        "concept": "Seeing inward (内側を見通す力)",
        "thinking": "物理的な目ではなく、「心の目（sight）」で物事の内側（in-）深くまで見通すこと。表面的なデータではなく、パターンの本質を捉える知性の眼差しです。",
        "aftertaste": "外見の殻を透過して、骨組みを捉える眼。",
        "example": "Her book provides profound insights into human nature.",
        "deep_dive": {
            "roots": [{"term": "sekw-", "meaning": "to see"}],
            "points": ["外を見るのではなく内側を見る、というシンプルな組み合わせが強力な意味を持ちます。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "intuition",
        "word": "Intuition",
        "meaning": "直感、勘、直観",
        "era": "15th Century Late Latin intuitio",
        "etymology": {
            "components": ["in- (at, on)", "tueri (to look, watch over)"],
            "original_statement": "From Late Latin intuitionem (a looking at), from intueri (to look at, consider)."
        },
        "concept": "Looking at internally (じっと見据えることによる把握)",
        "thinking": "論理的な思考ステップを踏まずに、ただ「じっと見つめる（tueri）」だけで、一瞬にして全体像や正解を掴み取る能力。経験と無意識が織りなす高速の計算結果です。",
        "aftertaste": "理性が追いつく前に、細胞が既に知っている。",
        "example": "I trusted my intuition and chose the left path.",
        "deep_dive": {
            "roots": [{"term": "teue-", "meaning": "to pay attention to"}],
            "points": ["tutor（家庭教師/見守る人）や tuition（授業料/見守り）と同じ語源です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "instinct",
        "word": "Instinct",
        "meaning": "本能、直感",
        "era": "15th Century Latin instinctus",
        "etymology": {
            "components": ["in- (in)", "stinguere (to prick, pique)"],
            "original_statement": "From Latin instinctus (instigation, impulse), from instinguere (to incite, impel)."
        },
        "concept": "Pricked or goaded from within (内側からチクッと刺されること)",
        "thinking": "外からの論理や学習ではなく、自分自身の内なるＤＮＡに「こうしろ！」と鋭く刺され（stinguere）、駆り立てられるように促される衝動。理性を超えた生命の原動力。",
        "aftertaste": "遺伝子が内側から放つ、回避不可能な命令。",
        "example": "Birds build nests by instinct.",
        "deep_dive": {
            "roots": [{"term": "steig-", "meaning": "to stick, prick"}],
            "points": ["スティグマ（stigma）やスティック（stick）と同じく『刺す・突き刺す』という語源です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "impulse",
        "word": "Impulse",
        "meaning": "衝動、はずみ、推進力",
        "era": "17th Century Latin impulsus",
        "etymology": {
            "components": ["in- (into, on)", "pellere (to drive, push)"],
            "original_statement": "From Latin impulsus (a pushing against, a shock), from impellere (to drive against, push into)."
        },
        "concept": "A pushing forward (前方への激しい押し出し)",
        "thinking": "内なる物理的な「力」や感情の爆発によって、背中をドンと押される（Pellere）こと。計画性なく行動に出てしまう衝動買い（impulse buy）などにも使われます。",
        "aftertaste": "考える間もなく、背中を蹴飛ばされるような駆動。",
        "example": "He had a sudden impulse to travel to Paris.",
        "deep_dive": {
            "roots": [{"term": "pel-", "meaning": "to thrust, strike"}],
            "points": ["プロペラ（propeller）の『ペル（推す）』と同根。推進力そのものです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "sensation",
        "word": "Sensation",
        "meaning": "感覚、大評判、感動",
        "era": "17th Century Late Latin sensatio",
        "etymology": {
            "components": ["sensus (feeling, perception)"],
            "original_statement": "From Late Latin sensationem, from Latin sensus (feeling, sense, understanding)."
        },
        "concept": "The faculty of feeling (感じ取ることの働き)",
        "thinking": "五感を通じて世界の一部を自分の中に「取り込む」こと。そして、ある事象が社会全体の感覚（感情）を一気に揺さぶり、虜にするような大事件を「センセーション」と表現します。",
        "aftertaste": "神経を駆け抜ける、世界との直接的な接触。",
        "example": "The new movie caused a sensation at the box office.",
        "deep_dive": {
            "roots": [{"term": "sent-", "meaning": "to feel"}],
            "points": ["sense, sentiment, consent など『感じる・理解する』系の親玉です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "paradigm",
        "word": "Paradigm",
        "meaning": "パラダイム、理論的枠組み、模範",
        "era": "15th Century Late Latin/Greek paradeigma",
        "etymology": {
            "components": ["para- (beside)", "deiknunai (to show)"],
            "original_statement": "From Greek paradeigma (pattern, model), from paradeiknunai (exhibit, represent), from para- (beside) + deiknunai (to show)."
        },
        "concept": "A pattern shown beside (横に置いて見せる模範)",
        "thinking": "何かを説明する時に「ほら、こういうことだよ」と横に提示される（para + deik-）見本。そこから、ある時代の科学や社会全体を支配する『世界をどう見るかという巨大な共通の型（レンズ）』を意味するようになりました。",
        "aftertaste": "私たちが無意識につけている、時代という名の眼鏡。",
        "example": "The discovery of DNA was a paradigm shift in biology.",
        "deep_dive": {
            "roots": [{"term": "deik-", "meaning": "to show, pronounce solemnly"}],
            "points": ["パラダイムシフト（枠組みの転換）という強力な表現でおなじみです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "prototype",
        "word": "Prototype",
        "meaning": "原型、試作品",
        "era": "16th Century Late Latin/Greek prototypon",
        "etymology": {
            "components": ["proto- (first)", "typos (impression, mold)"],
            "original_statement": "From Greek prototypon (a first or primitive form), from proto- (first) + typos (impression, mold, pattern)."
        },
        "concept": "The first impression or mold (最初に打たれた型)",
        "thinking": "製品が量産される前、最初に（Proto）叩き出された（Typos）ただ一つの原初の形。全ての完成品が帰属すべき大元のモデルであり、アイディアが初めて物理的な形状を得た瞬間。",
        "aftertaste": "泥の中に刻まれた、完璧な最初の足跡。",
        "example": "They built a working prototype of the new machine.",
        "deep_dive": {
            "roots": [{"term": "per-", "meaning": "forward, through (proto)"}, {"term": "teu-", "meaning": "to strike (typos)"}],
            "points": ["タイプ（type）の語源は『叩いてつけた型や刻印』です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "archetype",
        "word": "Archetype",
        "meaning": "元型、典型",
        "era": "16th Century Latin archetypum",
        "etymology": {
            "components": ["arkhe- (first, chief)", "typos (mold, model)"],
            "original_statement": "From Latin archetypum (original), from Greek arkhetypon (pattern, model), from arkhein (to begin, rule) + typos (mold)."
        },
        "concept": "The original reigning mold (支配的な大元の型)",
        "thinking": "人類のどの文化の神話にも『英雄』や『賢者』が登場するように、人間の深層心理の奥底に最初から刻印（Typos）されていて、全ての物語の支配者（Arkhe）となっている根源的なパターンのこと。",
        "aftertaste": "すべての人の無意識で眠る、永遠の登場人物たち。",
        "example": "The hero's journey is a universal archetype in storytelling.",
        "deep_dive": {
            "roots": [{"term": "arkhein", "meaning": "to begin, rule"}],
            "points": ["心理学者ユングが『集合的無意識の元型』として提唱し広まりました。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "stereotype",
        "word": "Stereotype",
        "meaning": "固定観念、ステレオタイプ",
        "era": "18th Century French stéréotype",
        "etymology": {
            "components": ["stereo- (solid)", "type (impression, mold)"],
            "original_statement": "Coined in French as stéréotype, literally 'solid type', referring to a method of printing from a solid metal plate."
        },
        "concept": "A solid metal impression (固められた印刷の型)",
        "thinking": "元々は印刷技術の用語（鉛で固めた活版）。一度作ると変更がきかず、全く同じものを大量に印刷できることから、人間の思考においても『柔軟性を失って固まりきった（stereo）、型にはまった大量生産の他者認識』を意味するようになりました。",
        "aftertaste": "個性を塗りつぶす、冷たい鉛の活字。",
        "example": "He doesn't fit the stereotype of an accountant at all.",
        "deep_dive": {
            "roots": [{"term": "ster-", "meaning": "stiff, solid"}],
            "points": ["ステレオ（立体音響）も『立体的で硬い・ソリッドな』という源流を持っています。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "paradox",
        "word": "Paradox",
        "meaning": "逆説、パラドックス、矛盾しているようで真理を含むもの",
        "era": "16th Century Latin/Greek paradoxon",
        "etymology": {
            "components": ["para- (contrary to)", "doxa (opinion)"],
            "original_statement": "From Latin paradoxum, from Greek paradoxon (contrary to expectation), from para- (contrary to) + doxa (opinion)."
        },
        "concept": "Contrary to common opinion (一般的な意見に逆らうもの)",
        "thinking": "一見すると世間の常識（Doxa）に反して（Para-）いて論理が破綻しているように見えながら、深く考察すると実は恐るべき真理を突いている言説。真理はしばしば、常識の裏側に潜んでいます。",
        "aftertaste": "常識の網の目をすり抜ける、真実の矛盾。",
        "example": "It is a paradox that computers need maintenance to keep making our lives easier.",
        "deep_dive": {
            "roots": [{"term": "dek-", "meaning": "to take, accept"}],
            "points": ["orthodox（正統派/正しい意見）の対義語的な立ち位置です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "dilemma",
        "word": "Dilemma",
        "meaning": "ジレンマ、板挟み、進退両難",
        "era": "16th Century Latin/Greek dilemma",
        "etymology": {
            "components": ["di- (two)", "lemma (premise, proposition)"],
            "original_statement": "From Latin dilemma, from Greek dilemma (double proposition), from di- (two) + lemma (premise, proposition)."
        },
        "concept": "A double proposition (二つの前提の板挟み)",
        "thinking": "修辞学や論理学で、どちらの選択肢（Lemma）を選んでも好ましくない結果になる『ふたつの角（ツノ）』の間で身動きが取れなくなる状態。人生の究極の苦悩の形。",
        "aftertaste": "二つの選択肢が、等しい重さで魂を引き裂く。",
        "example": "She faced a moral dilemma over whether to report the incident.",
        "deep_dive": {
            "roots": [{"term": "lab-", "meaning": "to take (lemma)"}],
            "points": ["『ジレンマの角』という言葉があるように、両方とも突き刺さる選択です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "enigma",
        "word": "Enigma",
        "meaning": "謎、不可解なこと",
        "era": "15th Century Latin/Greek aenigma",
        "etymology": {
            "components": ["ainissesthai (to speak darkly)", "ainos (fable, tale)"],
            "original_statement": "From Latin aenigma, from Greek ainigma (a dark saying, riddle), from ainissesthai (speak obscurely, speak in riddles)."
        },
        "concept": "A dark or mysterious saying (暗く謎めいた言葉)",
        "thinking": "ただわからない（unknown）のではなく、わざと暗号のように隠されたり、本質が複雑すぎて容易には解き明かせない崇高な謎。第二次大戦のドイツの暗号機のエニグマもここからです。",
        "aftertaste": "解読の鍵を拒絶する、美しい沈黙。",
        "example": "The origin of the manuscript remains an enigma.",
        "deep_dive": {
            "roots": [{"term": "ainos", "meaning": "tale, story"}],
            "points": ["パズル（解ける前提）とは格が違う深い謎を指します。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "labyrinth",
        "word": "Labyrinth",
        "meaning": "迷宮、迷路、入り組んだ状態",
        "era": "15th Century Latin/Greek labyrinthos",
        "etymology": {
            "components": ["labyrinthos (maze)"],
            "original_statement": "From Latin labyrinthus, from Greek labyrinthos, the name of the mythological maze built by Daedalus."
        },
        "concept": "A complex structure designed to confuse (混乱させる複雑な構造)",
        "thinking": "ギリシャ神話でミノタウロスを閉じ込めるために作られた出られない迷宮。単なる遊びの迷路（maze）ではなく、精神的・官僚的などうにもならない複雑怪奇なシステムさえも表現します。",
        "aftertaste": "中心に何かが潜む、無限の回廊。",
        "example": "Navigating the legal labyrinth took years.",
        "deep_dive": {
            "roots": [{"term": "labrys", "meaning": "double-headed axe"}],
            "points": ["ミノア文明の象徴である『双刃の斧（ラブリュス）の館』が語源とする説が有力。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "mystery",
        "word": "Mystery",
        "meaning": "神秘、謎、不可解なこと",
        "era": "14th Century Old French/Latin mysterium",
        "etymology": {
            "components": ["myein (to close the eyes/lips)"],
            "original_statement": "From Latin mysterium (secret service, secret rite), from Greek mysterion (secret rite or doctrine), from myein (to close, shut)."
        },
        "concept": "A secret rite where eyes and lips are closed (目と口を閉ざすべき秘密の儀式)",
        "thinking": "元々は古代ギリシャの密儀宗教。一般の人には明かされておらず、参加者には「口外しない（唇を閉じる=myein）」ことが求められました。転じて日常では解明不可能な出来事を指すようになりました。",
        "aftertaste": "真実を前にして、口を閉ざすことの美学。",
        "example": "The universe is full of unsolved mysteries.",
        "deep_dive": {
            "roots": [{"term": "mu-", "meaning": "echoic of muttering or closed lips"}],
            "points": ["mute（無言の）や mumble（つぶやく）など、唇を閉じた『ムー』という音が起源です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "rumor",
        "word": "Rumor",
        "meaning": "噂、流言",
        "era": "14th Century Old French/Latin rumor",
        "etymology": {
            "components": ["rumor (noise, murmur)"],
            "original_statement": "From Latin rumor (noise, clamor, hearsay), related to ravus (hoarse)."
        },
        "concept": "A low murmuring noise (ざわめく低い声)",
        "thinking": "事実かどうかはともかく、人々の間で低い声でヒソヒソと交わされ（murmur）、やがて全体に広がっていくざわめき。社会という大きな生き物が発する羽音。",
        "aftertaste": "誰のものでもない声が、大気を震わせる。",
        "example": "There is a rumor that the company will merge.",
        "deep_dive": {
            "roots": [{"term": "reu-", "meaning": "to bellow, mutter"}],
            "points": ["roar（咆哮）や murmur（ざわめき）など、音を表す古い擬音語的ルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "legend",
        "word": "Legend",
        "meaning": "伝説、言い伝え、偉人",
        "era": "14th Century Old French/Medieval Latin legenda",
        "etymology": {
            "components": ["legere (to read)"],
            "original_statement": "From Medieval Latin legenda (things to be read), originally the stories of saints' lives, from legere (to read)."
        },
        "concept": "Things to be read (読まれるべきもの)",
        "thinking": "本来は、修道院の食事中などに「教訓として必ず読まれるべき（聖人たちの）記録」でした。それが時を経て、少し誇張された偉大な英雄譚や、地図の「凡例（読み方）」へと意味を広げました。",
        "aftertaste": "声に出して読まれる間に、人は神話に昇華される。",
        "example": "The legend of King Arthur is famous worldwide.",
        "deep_dive": {
            "roots": [{"term": "leg-", "meaning": "to collect, gather, speak"}],
            "points": ["lecture（講義/読書）や legible（読める）と同じ根です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "myth",
        "word": "Myth",
        "meaning": "神話、作り話、根拠のない俗説",
        "era": "19th Century Modern Latin/Greek mythos",
        "etymology": {
            "components": ["mythos (speech, thought, story)"],
            "original_statement": "From Modern Latin mythus, from Greek mythos (word, speech, story, fiction)."
        },
        "concept": "A traditional story or speech (伝統的な物語、あるいは言葉そのもの)",
        "thinking": "ギリシャ語で「ロゴス（論理・理性的な言葉）」に対して、「物語や伝承として語り継がれる言葉」。世界の成り立ちを説明する崇高な神話でありながら、現代では「都市伝説や根拠のない嘘」という意味でも使われます。",
        "aftertaste": "論理（ロゴス）が届かない領域を埋める、物語（ミュートス）の力。",
        "example": "It is a myth that lightning never strikes the same place twice.",
        "deep_dive": {
            "roots": [{"term": "meudh-", "meaning": "to reflect, think over (tentative)"}],
            "points": ["ロゴスと対比される太古の哲学的な対概念でした。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "narrative",
        "word": "Narrative",
        "meaning": "物語、語り、話術",
        "era": "16th Century Middle French/Latin narrativus",
        "etymology": {
            "components": ["narrare (to tell, relate)"],
            "original_statement": "From Middle French narratif, from Latin narrativus (telling a story), from narrare (to relate, tell) which is related to gnarus (knowing)."
        },
        "concept": "Telling what is known (知っていることを語ること)",
        "thinking": "単なる時間の羅列（ストーリー）ではなく、「誰の視点から、どういう意図で語るのか（知らしめるのか）」という構造や見せ方を含んだ言葉。世界をどうパッケージ化して伝えるかという力（ナラティブ）。",
        "aftertaste": "出来事に文脈という名の魔法をかける。",
        "example": "The author used a first-person narrative to build intimacy.",
        "deep_dive": {
            "roots": [{"term": "gno-", "meaning": "to know"}],
            "points": ["語源的には know や ignore などと同じ『知る』系の言葉です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "metaphor",
        "word": "Metaphor",
        "meaning": "隠喩、比喩、メタファー",
        "era": "15th Century Middle French/Latin/Greek metaphora",
        "etymology": {
            "components": ["meta- (across, transfer)", "pherein (to carry)"],
            "original_statement": "From Latin metaphora, from Greek metaphora (a transfer), from metapherein (to transfer, carry over)."
        },
        "concept": "Carrying meaning across (意味を別のものへ運び移すこと)",
        "thinking": "ある物事の意味を、全然違う別の物事に「運び移して（meta + pherein）」表現すること。「人生は旅だ」のように、二つの異なる領域をスパークさせて新しい認識を生み出す、人間の最高の知的活動の一つです。",
        "aftertaste": "無関係な二つの概念が、火花を散らして結びつく。",
        "example": "He used a sailing metaphor to describe the business strategy.",
        "deep_dive": {
            "roots": [{"term": "bher-", "meaning": "to carry, bear"}],
            "points": ["フェリー（ferry）など『運ぶ』系と同じ語源です。メタファーは思考の輸送船なのです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "irony",
        "word": "Irony",
        "meaning": "皮肉、反語、(運命の)皮肉",
        "era": "16th Century Latin/Greek eironeia",
        "etymology": {
            "components": ["eiron (dissembler, one who feigns ignorance)"],
            "original_statement": "From Latin ironia, from Greek eironeia (dissimulation, assumed ignorance), from eiron (dissembler)."
        },
        "concept": "Feigned ignorance (わざと無知を装うこと)",
        "thinking": "古代ギリシャの喜劇で、わざと馬鹿なフリ（eiron）をして賢そうな相手を打ち負かすキャラクターが語源。言葉の表面の意味と、裏の真意（あるいは現実）が逆転している面白さや残酷さを指します。",
        "aftertaste": "笑い飛ばしながら、知性で相手の背後をとる。",
        "example": "The irony of the situation was entirely lost on him.",
        "deep_dive": {
            "roots": [{"term": "wer-", "meaning": "to speak"}],
            "points": ["ソクラテスの『無知の知（わざと知らないフリをして問い詰める・ソクラテス的アイロニー）』が有名です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "allegory",
        "word": "Allegory",
        "meaning": "寓意(物語)、アレゴリー",
        "era": "14th Century Old French/Latin/Greek allēgoria",
        "etymology": {
            "components": ["allos (other)", "agoreuein (to speak openly)"],
            "original_statement": "From Latin allegoria, from Greek allēgoria (figurative language), from allos (other) + agoreuein (speak openly, speak in the assembly)."
        },
        "concept": "Speaking otherwise (別の言い方をすること)",
        "thinking": "動物の物語の形を借りて政治や教訓を語る（「動物農場」など）ように、表面のストーリーとは「全く別の隠された意味（allos）」を語る手法。検閲を逃れるための知恵でもありました。",
        "aftertaste": "動物たちの影が、人間の愚かさを描き出す。",
        "example": "The novel is a dark allegory of the modern political system.",
        "deep_dive": {
            "roots": [{"term": "al-", "meaning": "beyond, other"}],
            "points": ["エイリアン（alien: 他の者）の全て（allos）とも関連しています。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "symbol",
        "word": "Symbol",
        "meaning": "象徴、記号、シンボル",
        "era": "15th Century Latin/Greek symbolon",
        "etymology": {
            "components": ["syn- (together)", "ballein (to throw)"],
            "original_statement": "From Latin symbolum (token, mark), from Greek symbolon (token, watchword), from syn- (together) + ballein (to throw)."
        },
        "concept": "Thrown together (一緒に投げ合わされたもの)",
        "thinking": "古代ギリシャで、契約の証拠として粘土板などを二つに割り、後で二つを「一緒に投げて（syn-ballein）」ピタリと合うかを確認した割符が語源。そこから、目に見えない概念（平和など）と、目に見える形（鳩など）をピタリと結びつけるものを指すようになりました。",
        "aftertaste": "二つに割れた破片が、再び出会って意味を成す。",
        "example": "The dove is a universal symbol of peace.",
        "deep_dive": {
            "roots": [{"term": "gwele-", "meaning": "to throw, reach"}],
            "points": ["ball（ボール・投げるもの）や bullet（弾丸）と同じ根です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "ideology",
        "word": "Ideology",
        "meaning": "イデオロギー、観念形態、(政治・社会上の)根本的な思想",
        "era": "18th Century French idéologie",
        "etymology": {
            "components": ["idea", "-logy (study of)"],
            "original_statement": "Coined in French as idéologie by Antoine Destutt de Tracy at the time of the French Revolution, literally 'the science of ideas'."
        },
        "concept": "The science of ideas (観念の科学)",
        "thinking": "元々は「人間の観念はどう生まれるか」という中立的な哲学分野の名称でした。しかしナポレオンがそれを「空論」と嘲笑し、その後マルクスが「支配階級を正当化する虚偽の意識」と呼んだことで、集団を動かす強烈で固定化された思想体系という意味に変わりました。",
        "aftertaste": "思想が刃となり、人々を分断する。",
        "example": "Capitalism and communism are two opposing economic ideologies.",
        "deep_dive": {
            "roots": [{"term": "weid-", "meaning": "to see"}, {"term": "leg-", "meaning": "to collect, speak"}],
            "points": ["元々はプラトンのイデア（Idea: 見える姿・原型）から派生した言葉です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "dogma",
        "word": "Dogma",
        "meaning": "教義、ドグマ、独断的意見",
        "era": "16th Century Latin/Greek dogma",
        "etymology": {
            "components": ["dokein (to seem good, think)"],
            "original_statement": "From Latin dogma (philosophical tenet), from Greek dogma (opinion, tenet, decree), from dokein (to seem good, think)."
        },
        "concept": "That which seems good or is established (正しいとみなされたもの)",
        "thinking": "元は哲学者が「これが良い（正しい）と思う」という意見や原則を指していましたが、それが宗教界に入ると「絶対に疑ってはならない絶対的な教義」となり、転じて現代では「凝り固まった柔軟性のない思考」の代名詞となりました。",
        "aftertaste": "思考を停止させる、石に刻まれた絶対の法。",
        "example": "Science must constantly challenge established dogma.",
        "deep_dive": {
            "roots": [{"term": "dek-", "meaning": "to take, accept"}],
            "points": ["docile（従順な）や doctor（教える人）と同じルーツを持ちます。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "axiom",
        "word": "Axiom",
        "meaning": "公理、自明の理、格言",
        "era": "15th Century Middle French/Latin/Greek axioma",
        "etymology": {
            "components": ["axioun (to consider worthy)", "axios (worthy)"],
            "original_statement": "From Latin axioma, from Greek axiōma (that which is thought fit or worthy; a self-evident principle), from axios (worthy)."
        },
        "concept": "That which is considered worthy (価値があるとして認められたもの)",
        "thinking": "証明する必要がないほど「自明に正しい価値がある」として、議論や数学（幾何学）の出発点・大前提となる命題。全ての論理のピラミッドの最下層を支える、最も頑丈な基礎石です。",
        "aftertaste": "論理の巨大な城を支える、証明のない一つの事実。",
        "example": "It's an axiom of economics that supply and demand determine price.",
        "deep_dive": {
            "roots": [{"term": "ag-", "meaning": "to drive, weigh"}],
            "points": ["『重さがある（＝価値がある）』という視点が語源にあります。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "theorem",
        "word": "Theorem",
        "meaning": "定理",
        "era": "16th Century Late Latin/Greek theorema",
        "etymology": {
            "components": ["theorein (to look at, consider)"],
            "original_statement": "From Late Latin theorema, from Greek theōrēma (spectacle, object of contemplation, principle), from theōrein (to look at)."
        },
        "concept": "Something to be looked at or proved (じっと眺め、考察し、証明されるべきもの)",
        "thinking": "Axiom（公理＝証明不要の大前提）の上に立って論理を積み上げ、最終的に「観照・証明された」真理や法則。ピタゴラスの定理（Pythagorean theorem）など、数学的な確固たる結論です。",
        "aftertaste": "公理という土台に組み上げられた、論理の芸術作品。",
        "example": "He spent years trying to prove Fermat's Last Theorem.",
        "deep_dive": {
            "roots": [{"term": "dheie-", "meaning": "to see, look"}],
            "points": ["theory（理論）や theater（劇場）と同じ『見る場』という語源です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "hypothesis",
        "word": "Hypothesis",
        "meaning": "仮説、前提、憶測",
        "era": "16th Century Late Latin/Greek hypothesis",
        "etymology": {
            "components": ["hypo- (under)", "tithenai (to put)"],
            "original_statement": "From Late Latin hypothesis, from Greek hypothesis (base, basis of an argument, supposition), from hypo- (under) + tithenai (to put)."
        },
        "concept": "Putting under (下に置くこと、思考の土台となるもの)",
        "thinking": "実験や議論を始めるために、一応そこに「下敷きとして置いてみる（hypo + thesis）」仮ごとの考え。これが実験で証明されると、theory（理論）へと昇格します。",
        "aftertaste": "まだ脆い足場。しかしそこから未踏の探求が始まる。",
        "example": "The scientists set up an experiment to test their hypothesis.",
        "deep_dive": {
            "roots": [{"term": "dhe-", "meaning": "to set, put"}],
            "points": ["テーマ（theme）、thesis（学位論文/主題）と同じ『置く』系です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "theory",
        "word": "Theory",
        "meaning": "理論、学説、持論",
        "era": "16th Century Late Latin/Greek theoria",
        "etymology": {
            "components": ["theoria (contemplation, speculation, a looking at)"],
            "original_statement": "From Late Latin theoria, from Greek theōria (contemplation, watching), related to theōros (spectator)."
        },
        "concept": "A looking at or contemplation (じっと観想すること、全体を見渡すこと)",
        "thinking": "単なる当てずっぽう（guess）や仮説（hypothesis）とは違い、多くの証拠によって裏付けられ、現象の世界を「高い視座から全体を見渡して筋道だてて説明する（見る）」強固な枠組み。相対性理論など。",
        "aftertaste": "混沌とした世界を俯瞰し、一つの美しい網目で覆う。",
        "example": "Darwin's theory of evolution revolutionized biology.",
        "deep_dive": {
            "roots": [{"term": "dheie-", "meaning": "to see"}],
            "points": ["定理（theorem）と同じく『見る（観想する）』という知的行為の極致です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "principle",
        "word": "Principle",
        "meaning": "原理、原則、主義、信条",
        "era": "14th Century Old French/Latin principium",
        "etymology": {
            "components": ["prīmus (first)", "capere (to take)"],
            "original_statement": "From Middle French principe, from Latin principium (beginning, foundation), from princeps (first man, chief), from prīmus (first) + capere (to take)."
        },
        "concept": "That which is taken first (最初に取られる大元)",
        "thinking": "行動や思考を組み立てる時、常に「真っ先に取らなければならない」根本的なルールのこと。科学の法則（アルキメデスの原理）から、個人の道徳的信条（私は原則として曲がったことはしない）まで、軸となるもの。",
        "aftertaste": "激流の中で絶対に手放さない、最初に掴んだ杭。",
        "example": "She is a woman of strong moral principles.",
        "deep_dive": {
            "roots": [{"term": "per-", "meaning": "forward, first"}, {"term": "kap-", "meaning": "to grasp"}],
            "points": ["プリンス（prince: 最初の/第一の地位を取る者）や principal（校長/主要な）と同根です。"]
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
