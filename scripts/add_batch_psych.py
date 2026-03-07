import json
import re

word_batch = [
    {
        "id": "nostalgia",
        "word": "Nostalgia",
        "meaning": "郷愁、過去への憧れ、ノスタルジア",
        "era": "17th Century Modern Latin/Greek nostos + algos",
        "etymology": {
            "components": ["nostos (return home)", "algos (pain)"],
            "original_statement": "Coined in 1688 by Swiss medical student Johannes Hofer from Greek nostos (return home) + algos (pain, suffering)."
        },
        "concept": "The pain of wanting to return home (故郷への帰還を望む痛み)",
        "thinking": "元々は、遠く離れた兵士たちが故郷を思って心身を病む「ホームシックの重症（病気）」として作られた医学用語でした。それが、帰る場所（あるいは過ぎ去った美しい時代）を強烈に想って胸が締め付けられるあの甘美な感情を指すようになりました。",
        "aftertaste": "永遠に手の届かなくなった過去が、甘い痛みとなって胸を刺す。",
        "example": "Hearing that old song filled her with nostalgia.",
        "deep_dive": {
            "roots": [{"term": "nes-", "meaning": "to return safely to home"}, {"term": "algein", "meaning": "to feel pain"}],
            "points": ["鎮痛剤（analgesic）の alg-（痛み）と同じ後半部を持ちます。痛みなのです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "melancholy",
        "word": "Melancholy",
        "meaning": "憂鬱、ふさぎ込み、物悲しさ",
        "era": "14th Century Old French/Greek melankholia",
        "etymology": {
            "components": ["melan- (black)", "kholē (bile)"],
            "original_statement": "From Old French melancolie, from Late Latin melancholia, from Greek melankholia (sadness), literally 'black bile', from melan- (black) + kholē (bile)."
        },
        "concept": "Black bile (黒い胆汁)",
        "thinking": "古代ギリシャ医学では、人間の体液のうち「黒い胆汁」が多くなりすぎると、人は理由もなく深く沈み込み、うつ病になると考えられていました。体液説は否定されましたが、この美しく物悲しい響きの言葉だけが残りました。",
        "aftertaste": "心の中に静かに染み渡る、黒いインクの一滴。",
        "example": "He stared out the window in a state of deep melancholy.",
        "deep_dive": {
            "roots": [{"term": "melan-", "meaning": "black"}],
            "points": ["メラニン色素（melanin）のメラ（黒）と語源を共有します。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "empathy",
        "word": "Empathy",
        "meaning": "共感、感情移入",
        "era": "20th Century English/Greek empatheia",
        "etymology": {
            "components": ["en- (in)", "pathos (feeling, suffering)"],
            "original_statement": "Coined in 1909 by Edward Titchener as a translation of German Einfühlung (feeling into), from Greek empatheia (passion, partiality), from en- (in) + pathos (feeling)."
        },
        "concept": "Feeling into (相手の内側に入り込んで感じること)",
        "thinking": "単なる同情（かわいそうだと思うこと）ではなく、相手の靴を履いて、相手の目線で、相手の中の『痛みや感情（pathos）』をまさに自分事として追体験し、内側に「入る（en）」という高度な知的・感情的行為です。",
        "aftertaste": "あなたの中に降り立ち、あなたの目で世界を見る。",
        "example": "Empathy allows us to build deep connections with others.",
        "deep_dive": {
            "roots": [{"term": "kwent(h)-", "meaning": "to suffer"}],
            "points": ["パトス（情念）やパッション（情熱/受難）と同じ、感情の激しい波のルーツです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "sympathy",
        "word": "Sympathy",
        "meaning": "同情、思いやり、共鳴",
        "era": "16th Century Late Latin/Greek sympatheia",
        "etymology": {
            "components": ["syn- (together)", "pathos (feeling, suffering)"],
            "original_statement": "From Late Latin sympathia, from Greek sympatheia (fellow-feeling, community of feeling), from syn- (together) + pathos (feeling)."
        },
        "concept": "Feeling together (共に感じること)",
        "thinking": "Empathy（相手の中に入る）と似ていますが、Sympathyは自分の立ち位置から相手の不幸や感情に対して「一緒に（syn）気持ちを寄せる」「寄り添う」距離感。かわいそうだね、と思う温かい心の動きです。",
        "aftertaste": "横に座り、共に痛みの響きを聞く。",
        "example": "I have a lot of sympathy for his difficult situation.",
        "deep_dive": {
            "roots": [{"term": "syn-", "meaning": "together"}],
            "points": ["シンボルの（syn-：一緒に）とパッション（pathos：感情）の組み合わせです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "apathy",
        "word": "Apathy",
        "meaning": "無関心、無感情、アパシー",
        "era": "17th Century Greek apatheia",
        "etymology": {
            "components": ["a- (without)", "pathos (feeling)"],
            "original_statement": "From Greek apatheia (freedom from suffering, impassibility), from a- (without) + pathos (feeling, emotion)."
        },
        "concept": "Without feeling (感情がないこと)",
        "thinking": "「共に（sym）」でも「中に（em）」でもなく、感情そのものが「無い（a-）」こと。ストア派の哲学では『苦悩に振り回されない悟りの境地（不動心）』というプラスの意味でしたが、現代では単なる『無気力・無関心』という病的な状態を指します。",
        "aftertaste": "悲しみも喜びも、すべての波が消えた凪の水面。",
        "example": "Voter apathy is a growing problem in modern democracies.",
        "deep_dive": {
            "roots": [{"term": "a-", "meaning": "without"}],
            "points": ["atheist（無神論者）や amnesia（記憶喪失）の a- と同じ『無・否定』です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "solitude",
        "word": "Solitude",
        "meaning": "孤独、独りであること、(ポジティブな)一人きりの時間",
        "era": "14th Century Old French/Latin solitudo",
        "etymology": {
            "components": ["solus (alone)"],
            "original_statement": "From Old French solitude, from Latin solitudo (being alone, loneliness), from solus (alone)."
        },
        "concept": "The state of being alone (ひとりである状態)",
        "thinking": "Loneliness（寂しさ）が『疎外感から来るネガティブで痛みを伴う孤独』であるのに対し、Solitudeは『自分自身の内面と向き合うための、穏やかで自発的・ポジティブな孤独の内省時間』として使い分けられます。",
        "aftertaste": "ひとりは寂しいことではない。静寂という贅沢だ。",
        "example": "He enjoyed the peace and solitude of the mountain cabin.",
        "deep_dive": {
            "roots": [{"term": "s(w)e-", "meaning": "oneself, apart"}],
            "points": ["sole（唯一の）や solo（ソロ）と同じ語源です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "isolation",
        "word": "Isolation",
        "meaning": "孤立、分離、隔離",
        "era": "19th Century French/Latin insula",
        "etymology": {
            "components": ["insula (island)"],
            "original_statement": "From French isolation, from isoler (to isolate), from Italian isolato (separated like an island), from Latin insula (island)."
        },
        "concept": "Made into an island (島のように切り離されること)",
        "thinking": "島（island / insula）のように、陸地（社会や集団）から物理的、あるいは精神的に完全に切り離されて海にポツンと浮かんでいる状態。感染症の隔離（quarantine）時などにも使われます。",
        "aftertaste": "見渡す限りの海。橋はもう落ちた。",
        "example": "Prolonged social isolation can damage mental health.",
        "deep_dive": {
            "roots": [{"term": "insula", "meaning": "island"}],
            "points": ["peninsula（半島）や insulation（断熱/絶縁）と同じ『島』ファミリーです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "anxiety",
        "word": "Anxiety",
        "meaning": "不安、心配、切望",
        "era": "16th Century Latin anxietas",
        "etymology": {
            "components": ["angere (to choke, squeeze)"],
            "original_statement": "From Latin anxietas (anxiety, anxiousness), from anxius (deeply troubled), from angere (to choke, squeeze tightly)."
        },
        "concept": "A feeling of being choked or squeezed (喉が締め付けられるような感覚)",
        "thinking": "未来への不確実性からくる恐怖感や心配。その感情のルーツは心理的なものではなく、文字通り「首を絞められて（angere）息が詰まる」というパニック時の強烈な肉体的な痛み・息苦しさから来ています。",
        "aftertaste": "実体のない手が、静かに喉を絞めあげる。",
        "example": "Waiting for the test results caused her great anxiety.",
        "deep_dive": {
            "roots": [{"term": "angh-", "meaning": "tight, painfully constricted"}],
            "points": ["anger（怒り）や anguish（苦悩・激痛）と同じ『苦しいほどの締め付け』の語源です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "trauma",
        "word": "Trauma",
        "meaning": "トラウマ、心的外傷、深刻なショック",
        "era": "17th Century Greek trauma",
        "etymology": {
            "components": ["trauma (a wound)"],
            "original_statement": "From Medical Latin trauma, from Greek trauma (a wound, a hurt), related to titroskein (to wound, pierce)."
        },
        "concept": "A physical or psychological wound (物理的、あるいは精神的な深い傷)",
        "thinking": "本来は肉体的な「外傷（刃物などで刺された深い傷）」を意味する純粋な外科医学用語でした。それがフロイト以降の心理学において、心の奥深くまで切り裂かれ、跡が残ってしまった「心的外傷」を意味するようになりました。",
        "aftertaste": "血は止まっても、見えない傷口が開いたまま。",
        "example": "The victim needed counseling to overcome the trauma of the accident.",
        "deep_dive": {
            "roots": [{"term": "tere-", "meaning": "to rub, turn, pierce"}],
            "points": ["throw（投げる）や turn（回す）など、力を加える古い動作の根から派生。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "therapy",
        "word": "Therapy",
        "meaning": "療法、治療、セラピー",
        "era": "19th Century Modern Latin/Greek therapeia",
        "etymology": {
            "components": ["therapeuein (to cure, treat, attend to)"],
            "original_statement": "From Modern Latin therapia, from Greek therapeia (curing, healing, service), from therapeuein (to cure, wait upon), from therapon (attendant)."
        },
        "concept": "Attending to or serving the sick (病人に仕え、付き添うこと)",
        "thinking": "神をも恐れぬ外科手術のような物理的排除よりは、「付き添って（therapon）、丁寧に世話をして、本来の機能が回復するのを手助けする」という、より寄り添う形での治癒・手当の概念を強く持ちます。",
        "aftertaste": "治すのではない。治るための時間に付き添うのだ。",
        "example": "Music therapy is known to be effective for cognitive disorders.",
        "deep_dive": {
            "roots": [{"term": "dher-", "meaning": "to hold, support"}],
            "points": ["firm（固い）や throne（王座）と同じく『支える・保つ』という優しいベースがあります。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "psychology",
        "word": "Psychology",
        "meaning": "心理学、心理",
        "era": "17th Century Modern Latin/Greek",
        "etymology": {
            "components": ["psykhe (breath, spirit, soul)", "-logia (study of)"],
            "original_statement": "From Modern Latin psychologia, coined from Greek psykhe (breath, spirit, soul) + -logia (study of)."
        },
        "concept": "The study of the soul or breath (魂・呼吸の科学)",
        "thinking": "ギリシャ語の『プシュケー』は、ギリシャ神話の美しい少女の名であるとともに、『人間の熱い呼吸、魂そのもの、そして蝶』を意味しました。目に見えない心の動きを、蝶の羽ばたきや吐息に見立てたのです。",
        "aftertaste": "蝶の羽ばたきを追いかけて、心という迷宮へ。",
        "example": "She is studying psychology to better understand human behavior.",
        "deep_dive": {
            "roots": [{"term": "bhes-", "meaning": "to blow, to breathe"}],
            "points": ["精神異常（psychopath）など、すべてのサイコ-（心/精神）の親玉です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "consciousness",
        "word": "Consciousness",
        "meaning": "意識、自覚",
        "era": "17th Century English",
        "etymology": {
            "components": ["con- (with, together)", "scire (to know)"],
            "original_statement": "Formed from conscious + -ness. Conscious is from Latin conscius (knowing with others, feeling with oneself), from con- + scire (to know)."
        },
        "concept": "Knowing with oneself (自分自身と共に知っていること)",
        "thinking": "自分が「存在している」こと、そして周囲の環境や自分自身の思考を「分かっている」という、自己言及的な知覚状態。人工知能に芽生えるかどうかが常に議論される、哲学と科学の最大のミステリー。",
        "aftertaste": "『私がここに居る』という、宇宙で一番静かな奇跡。",
        "example": "The patient regained consciousness a day after the operation.",
        "deep_dive": {
            "roots": [{"term": "skei-", "meaning": "to cut, split"}],
            "points": ["science（科学・知ること）と同じ『知る』系の頂点。知覚によって自己と他者を『切り分ける（skei-）』からです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "perception",
        "word": "Perception",
        "meaning": "知覚、認識、見方",
        "era": "14th Century Latin perceptio",
        "etymology": {
            "components": ["per- (thoroughly)", "capere (to grasp, take)"],
            "original_statement": "From Latin perceptionem (a gathering in, obtaining), from perceptus, past participle of percipere (obtain, gather, seize entirely), from per- (thoroughly) + capere (to grasp)."
        },
        "concept": "Seizing thoroughly (完全に掴み取ること)",
        "thinking": "光や音という物理的なデータ（感覚: sensation）を、脳が処理して「あれは赤い看板だ」と『全体像をガッチリと掴み取る（per-capere）』こと。物理世界の情報を、自分だけの意味ある現実に書き換える作業です。",
        "aftertaste": "感覚という名の網で、世界をすくい上げる。",
        "example": "His perception of the problem was completely different from mine.",
        "deep_dive": {
            "roots": [{"term": "per-", "meaning": "thoroughly"}, {"term": "kap-", "meaning": "to grasp"}],
            "points": ["capture（捕獲する）や capacity（容量）と同じ『掴む力』の語源です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "illusion",
        "word": "Illusion",
        "meaning": "錯覚、幻想、思い違い",
        "era": "14th Century Old French/Latin illusio",
        "etymology": {
            "components": ["in- (at, upon)", "ludere (to play)"],
            "original_statement": "From Old French illusion, from Latin illusionem (a mocking, ironing), from illudere (to mock at, play with), from in- (at, upon) + ludere (to play)."
        },
        "concept": "A playful mocking of the senses (感覚をからかって遊ぶこと)",
        "thinking": "脳や光の屈折が、私たちの認識を「からかって遊んで（in + ludere）」騙すこと。そこに何かがあるように『感じさせる』マジックや、うまくいっているという『思い込み』のこと。",
        "aftertaste": "現実は、脳がからかい半分に見せる幻。",
        "example": "Mirages are optical illusions caused by hot air.",
        "deep_dive": {
            "roots": [{"term": "leid-", "meaning": "to play, jest"}],
            "points": ["ludicrous（滑稽な）や elusive（逃げをうつ/捉えどころのない）と同根の『遊び』です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "hallucination",
        "word": "Hallucination",
        "meaning": "幻覚",
        "era": "17th Century Latin hallucinatio",
        "etymology": {
            "components": ["alucinari (to wander in mind, dream)"],
            "original_statement": "From Latin hallucinationem, from hallucinatus, past participle of hallucinari or rather alucinari (wander in mind, ramble, dream)."
        },
        "concept": "Wandering in the mind (心がさまよい、夢をみること)",
        "thinking": "Illusion（錯覚）が「外にあるものを読み間違える」のに対して、こちらは「外には何もないのに、脳のネットワークが暴走して（さまよって）本物として完全に見てしまう」状態。AIの嘘も現在こう呼ばれます。",
        "aftertaste": "誰もいない部屋に、声が満ちる。",
        "example": "High fever can sometimes cause visual hallucinations.",
        "deep_dive": {
            "roots": [{"term": "alucinari", "meaning": "to wander in mind"}],
            "points": ["AIがしれっと嘘をつく『ハルシネーション（幻覚）』はこの言葉。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "delusion",
        "word": "Delusion",
        "meaning": "妄想、思い込み、欺瞞",
        "era": "15th Century Latin delusio",
        "etymology": {
            "components": ["de- (down, away)", "ludere (to play)"],
            "original_statement": "From Latin delusionem (a deceiving), from delusus, past participle of deludere (to play false, mock, deceive), from de- (down, to one's detriment) + ludere (to play)."
        },
        "concept": "Playing false (嘘で完全に遊び騙すこと)",
        "thinking": "Illusion（物理的な錯覚）でもHallucination（脳が見せる幻覚）でもなく、「自分が王族である」とか「狙われている」といった、論理的証拠を提示されても頑なに信じて疑わない『病的なまでに強固に騙された思考体系（妄想）』。",
        "aftertaste": "崩れない妄信。それが狂気の城の石垣。",
        "example": "He has a delusion that everyone is trying to poisoning his food.",
        "deep_dive": {
            "roots": [{"term": "leid-", "meaning": "to play"}],
            "points": ["Illusionと同じ『ludere（遊ぶ）』系統ですが、de- がつくことで『徹底的に悪質に騙す』ニュアンス。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "subconscious",
        "word": "Subconscious",
        "meaning": "潜在意識",
        "era": "19th Century English/French",
        "etymology": {
            "components": ["sub- (under)", "conscious"],
            "original_statement": "Formed from the prefix sub- (under, below) + conscious. Popularized mainly via psychological theory."
        },
        "concept": "Beneath the conscious awareness (意識より少し下の層)",
        "thinking": "普段は意識していないけれど、記憶や感情が蓄えられていて、何かの拍子にスッと意識に上がってくることができる（あるいは夢に現れる）心の領域。氷山の水面下にある巨大な塊。",
        "aftertaste": "あなたの選択は、水面下のあなたが既に決めている。",
        "example": "Our fears are often rooted deep within the subconscious.",
        "deep_dive": {
            "roots": [{"term": "upo", "meaning": "under"}],
            "points": ["unconscious（無意識/気絶）とは区別され、『引き出そうと思えば引き出せる心の裏側』を指します。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "ego",
        "word": "Ego",
        "meaning": "自我、利己心、自尊心",
        "era": "19th Century Latin ego",
        "etymology": {
            "components": ["ego (I)"],
            "original_statement": "From Latin ego (I). Popularized in psychoanalysis in 1914 by Joan Riviere's translation of Freud's 'Das Ich' (The 'I')."
        },
        "concept": "The 'I' or self (「私」そのもの)",
        "thinking": "フロイトが「エス（本能）」と「超自我（理性）」の板挟みになって調整する『調整役の現実機能』を（翻訳で）エゴと名付けました。現在では「プライドが高い（egoが強い）」などと否定的な利己志向を指すことが多いです。",
        "aftertaste": "二つの巨人の間でバランスを取る、弱々しい調停者。",
        "example": "Taking the criticism personally was a matter of his own ego.",
        "deep_dive": {
            "roots": [{"term": "eg-", "meaning": "I"}],
            "points": ["『エゴイスティック（利己的な）』の元の存在。全ての『自分』の主語です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "persona",
        "word": "Persona",
        "meaning": "ペルソナ、(他者に見せる)仮面、外向きの顔",
        "era": "20th Century Latin persona",
        "etymology": {
            "components": ["personare (to sound through)"],
            "original_statement": "From Latin persona (theatrical mask, character played by an actor), possibly from Etruscan phersu (mask), or related to Latin personare (to sound through)."
        },
        "concept": "A theatrical mask (劇などで被る仮面)",
        "thinking": "古代ローマの演劇で、役者が被って声を「通り抜けさせた（per-sonare）」仮面。ユング心理学では、人間が「社会生活を円滑に送るために、その場その場でつけ替えている外向きの自分自身」を指します。",
        "aftertaste": "私闘、親、部下。我々は常に仮面を着け替える役者である。",
        "example": "His public persona is quite different from his private self.",
        "deep_dive": {
            "roots": [{"term": "swen-", "meaning": "to sound"}],
            "points": ["person（人・人間）や personality（人格）の直接の先祖であり、人間とは仮面をかぶった存在という哲学です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "narcissism",
        "word": "Narcissism",
        "meaning": "自己愛、ナルシシズム、うぬぼれ",
        "era": "20th Century Greek Narkissos",
        "etymology": {
            "components": ["Narkissos (Narcissus)"],
            "original_statement": "From German Narzissismus, coined in 1899 by Paul Näcke, based on the Greek myth of Narkissos, a beautiful youth who fell in love with his own reflection."
        },
        "concept": "Self-love, like Narcissus (水鏡に映る自分を愛した少年のように)",
        "thinking": "ギリシャ神話で、水面に映る美しすぎる「自分自身」に恋をしてしまい、身動きが取れなくなって死んでしまった（そしてスイセンの花になった）美少年ナルキッソス。他者を愛さず自分だけを特別視する病的な自己愛。",
        "aftertaste": "水面の自分からは、永遠に愛は返ってこない。",
        "example": "His narcissism prevented him from making genuine friendships.",
        "deep_dive": {
            "roots": [{"term": "narke", "meaning": "numbness, stupor"}],
            "points": ["彼がスイセン（narcissus）になったことから、麻薬（narcotic：感覚を麻痺させる）とも語源が通じます。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "hypnosis",
        "word": "Hypnosis",
        "meaning": "催眠、催眠状態",
        "era": "19th Century Greek hypnos",
        "etymology": {
            "components": ["hypnos (sleep)", "-osis (condition)"],
            "original_statement": "Coined in 1841 by Scottish physician James Braid, from Greek hypnos (sleep) + -osis (condition)."
        },
        "concept": "A sleep-like condition (睡眠状態のようなもの)",
        "thinking": "暗示をかけて意識の一部を手放させる医療やショーの技法。「睡眠（hypnos）」という言葉を使っていますが、実際には脳が起きているまま一部の集中力が極限に高まった非常に特異な変性意識状態です。",
        "aftertaste": "起きながら夢を見る、強制ハッキング。",
        "example": "The therapist used hypnosis to help him quit smoking.",
        "deep_dive": {
            "roots": [{"term": "swep-", "meaning": "to sleep"}],
            "points": ["ギリシャの眠りの神『ヒュプノス』から。不眠症（insomnia）のsomniaと同じ印欧語根から分かれました。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "euphoria",
        "word": "Euphoria",
        "meaning": "陶酔感、多幸感、幸福感",
        "era": "18th Century Modern Latin/Greek euphoria",
        "etymology": {
            "components": ["eu- (well, good)", "pherein (to bear, carry)"],
            "original_statement": "From Medical Latin euphoria, from Greek euphoria (power of enduring easily), from euphoros (bearing well), from eu- (well) + pherein (to bear)."
        },
        "concept": "Bearing well (物事をうまく耐え抜く心地よさ、転じて極度の多幸感)",
        "thinking": "元々は「病気の痛みがスッと消え、快適に耐えられる」という医学用語。そこから、何らかの理由（スポーツで勝った時や薬物の影響など）で、強烈な快楽と幸福感に包まれる「ハイな状態（陶酔）」を指すようになりました。",
        "aftertaste": "重力が消え、光に包まれる絶対の快楽。",
        "example": "The marathon runner experienced a wave of euphoria near the finish line.",
        "deep_dive": {
            "roots": [{"term": "bher-", "meaning": "to carry, bear"}],
            "points": ["eulogy（賛辞）や euthanasia（安楽死）の『eu-（良い）』が使われています。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "destiny",
        "word": "Destiny",
        "meaning": "運命、宿命",
        "era": "14th Century Old French/Latin destinare",
        "etymology": {
            "components": ["de- (completely)", "stare (to stand)"],
            "original_statement": "From Old French destinee (purpose, intent, destiny), from Latin destinare (to make firm, establish), from de- (completely) + *stanare (from stare, to stand)."
        },
        "concept": "That which is firmly established (完全に固定された結末)",
        "thinking": "Fate（悲劇的な運命）と違い、神や宇宙によって「しっかりと立たされ、動かせない（stare）」ように仕向けられたポジティブな最終到達点。「これは私のデスティー（果たすべき真の目的）だ」という前向きな響きを持ちます。",
        "aftertaste": "最初からそこにあった、輝ける結末への引力。",
        "example": "He believed it was his destiny to become a great leader.",
        "deep_dive": {
            "roots": [{"term": "sta-", "meaning": "to stand, set down"}],
            "points": ["destination（目的地）と同じく、『あそこに行くことが決まっている場所』というニュアンス。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "fate",
        "word": "Fate",
        "meaning": "運命、避けられない悲運、死",
        "era": "14th Century Latin fatum",
        "etymology": {
            "components": ["fari (to speak)"],
            "original_statement": "From Latin fatum (that which has been spoken; prophetic declaration, destiny), neuter past participle of fari (to speak)."
        },
        "concept": "That which has been spoken (すでに語られたこと)",
        "thinking": "Destinyが自分の手で掴む「到達点」なら、Fateは神々の口から「こうなる」と『既に宣言されてしまった（fari）』覆しようのない決定事項。ギリシャ神話で運命の糸を断ち切る女神のイメージ通り、逃れられない死や悲運を指します。",
        "aftertaste": "神の口が動いた時、あなたの結末は終わっている。",
        "example": "They were separated by a cruel twist of fate.",
        "deep_dive": {
            "roots": [{"term": "bha-", "meaning": "to speak"}],
            "points": ["fairy（妖精＝神の使い/運命を告げる者）や fatal（致命的な）と同じ源流の言葉です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "serendipity",
        "word": "Serendipity",
        "meaning": "思わぬ幸運な発見、セレンディピティ",
        "era": "18th Century English Serendip",
        "etymology": {
            "components": ["Serendip (old name for Sri Lanka)"],
            "original_statement": "Coined by Horace Walpole in 1754, from the Persian fairy tale 'The Three Princes of Serendip', whose heroes were always making discoveries, by accidents, of things they were not in quest of."
        },
        "concept": "Unexpected happy discoveries (探していなかったのに見つけた、幸運な偶然)",
        "thinking": "「セレンディップの三人の王子」という古いおとぎ話の王子たちが、いつも「全く別のものを探していたのに、偶然に素晴らしい別の発見をする」ことから作られた非常に新しい英語。ペニシリンや電子レンジの発明などが典型例です。",
        "aftertaste": "寄り道で拾った石が、ダイヤモンドだった。",
        "example": "Finding that rare book in the small shop was pure serendipity.",
        "deep_dive": {
            "roots": [],
            "points": ["英語の中で最も美しい言葉の一つとされ、科学分野での『偶然の偉大な発見』を指す重要な教養語です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "coincidence",
        "word": "Coincidence",
        "meaning": "偶然の暗合、同時発生、単なる偶然",
        "era": "17th Century Medieval Latin coincidentia",
        "etymology": {
            "components": ["com- (together)", "in- (upon)", "cadere (to fall)"],
            "original_statement": "From Medieval Latin coincidentia, from coincidere (to fall upon together), from com- (together) + in- (upon) + cadere (to fall)."
        },
        "concept": "Falling together upon the same spot (同じ場所に一緒に落ちること)",
        "thinking": "全く無関係な二つの出来事が、偶然にも『全く同じ場所・同じ時間にヒュッと落ちてきて（incide）ピッタリ重なる（co-）』こと。そこに運命的な意味はなく、ただの確率的ないたずら（Mere coincidence）として使われます。",
        "aftertaste": "二つの矢が、偶然同じマトを射抜いただけ。",
        "example": "It was just a coincidence that we both wore blue shirts today.",
        "deep_dive": {
            "roots": [{"term": "kad-", "meaning": "to fall"}],
            "points": ["incident（出来事：落ちてきたこと）や accident（事故）と同じく『コントロールできずに落ちてくるもの』です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "synchronicity",
        "word": "Synchronicity",
        "meaning": "シンクロニシティ、意味のある偶然の一致、共時性",
        "era": "20th Century Greek syn- + chronos",
        "etymology": {
            "components": ["syn- (together)", "chronos (time)"],
            "original_statement": "Coined in the 1950s by Swiss psychologist Carl Jung from synchrony (simultaneous occurrence), from Greek synchronos (happening at the same time)."
        },
        "concept": "Meaningful coincidence in time (時間軸で共に起きる、意味ある偶然)",
        "thinking": "Coincidenceが「無意味な確率の結果」であるのに対し、ユングが提唱した「因果関係はないのに、まるでお互いが見えない集合的無意識で繋がっているかのように、同時に（syn-）時間（chronos）を共有して起きる深い意味を持った一致」。",
        "aftertaste": "世界に響き渡る、見えない波長の共鳴。",
        "example": "Thinking of an old friend right before they call is a common experience of synchronicity.",
        "deep_dive": {
            "roots": [{"term": "chronos", "meaning": "time"}],
            "points": ["chronicle（年代記）や chronic（慢性の：時間がかかる）の『時間（クロノス神）』です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "ephemeral",
        "word": "Ephemeral",
        "meaning": "つかの間の、儚い、一日限りの",
        "era": "16th Century Greek ephemeros",
        "etymology": {
            "components": ["epi- (on, for)", "hemera (day)"],
            "original_statement": "From Greek ephemeros (short-lived, lasting but a day), from epi- (on, for) + hemera (day)."
        },
        "concept": "Lasting only for a single day (ただ一日だけの長さ)",
        "thinking": "元々はカゲロウという昆虫や、一日でしおれる花など「寿命が一日（hemera）しかない命」を指す言葉でした。そこから、美しくも儚く、すぐに消え去ってしまう人間の栄華や青春の美しさを表現する最高級の形容詞となりました。",
        "aftertaste": "一日で終わるからこそ、その瞬間の完璧さが際立つ。",
        "example": "Fashion trends are often ephemeral, changing every season.",
        "deep_dive": {
            "roots": [{"term": "hemera", "meaning": "day"}],
            "points": ["diaryの代わりに ephemeris（日々の記録）という単語もあります。"]
        },
        "part_of_speech": "adjective"
    },
    {
        "id": "eternal",
        "word": "Eternal",
        "meaning": "永遠の、不変の、果てしない",
        "era": "14th Century Old French/Latin aeternalis",
        "etymology": {
            "components": ["aevum (age, timespan, eternity)"],
            "original_statement": "From Old French eternel, from Late Latin aeternalis, from Latin aeternus (everlasting), a contraction of aeviternus, from aevum (age)."
        },
        "concept": "Having an infinite timespan (無限の時代・時間)",
        "thinking": "Ephemeral（一日）とは対極にある、始まりもなければ終わりもない（あるいは途方もなく長く続く）時間の広がり。「時代（aevum）」というものが永遠に積層しているようなスケール感で、神の属性や不滅の愛などに使われます。",
        "aftertaste": "時という川が干上がった後も、ただそこに在るもの。",
        "example": "She promised him her eternal love.",
        "deep_dive": {
            "roots": [{"term": "aiw-", "meaning": "vital force, life, long life, eternity"}],
            "points": ["medieval（中世の：medi+aevum）の ae や e（時代）と同じ源で、永遠の若さというニュアンスも含みます。"]
        },
        "part_of_speech": "adjective"
    },
    {
        "id": "amnesia",
        "word": "Amnesia",
        "meaning": "記憶喪失、健忘症",
        "era": "18th Century Modern Latin/Greek amnesia",
        "etymology": {
            "components": ["a- (without)", "mnasthai (to remember)"],
            "original_statement": "From Modern Latin amnesia, from Greek amnesia (forgetfulness), from a- (not, without) + mnasthai (to remember)."
        },
        "concept": "Without memory (記憶がないこと)",
        "thinking": "脳の損傷やショックによって引き起こされる、過去が完全に「失われた（a-）」状態。アイデンティティは記憶の積み重ねであるため、記憶喪失は『自分が誰であるかの中核の崩壊』という深い哲学的恐怖を含みます。",
        "aftertaste": "白紙になったノート。私が何者かなんて、もう誰も知らない。",
        "example": "After the crash, he suffered from temporary amnesia.",
        "deep_dive": {
            "roots": [{"term": "men-", "meaning": "to think"}],
            "points": ["amnesty（恩赦：罪を『忘却』してあげること）と同じルーツです。"]
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
