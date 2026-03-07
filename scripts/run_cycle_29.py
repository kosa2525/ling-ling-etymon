import json
import re

# Theme: The Pulse of Literature & Narrative (Cycle 29)
words_data = [
    ("narrative", "Narrative", "物語、語り", "15th Century", "gnarus (knowing, skilled)", "A spoken or written account of connected events; a story", "ただの（。出来事（。の羅列ではなく、意味（。を知る（。グナルス）者が、出来事の点と点を（。意図を持って）繋ぎ合わせ、一つの（。美しい（。星座（。へと仕立て上げた、魂の（。報告書。", "あなたの人生という「ナラティブ（物語）」の執筆を（。他人に（。任せて（。はいけません。絶望（。という名の（。一章（。を、希望（。という名の（。クライマックス（。へと塗り替える（。ペン（。は、今もあなたの手の中に（。あるのです。"),
    ("allegory", "Allegory", "寓話、譬え話", "14th Century", "allos (other) + agoreuein (to speak openly)", "A story, poem, or picture that can be interpreted to reveal a hidden meaning, typically a moral or political one", "広場（。アゴラ）において、ある（。ことを「別の（。アロス）形（。を（。借りて）語る」ことで、直接（。語るにはあまりに（。巨大な（。、あるいは危険（。な（。真実（。を（。そっと（。伝える、知的な（。ヴェール（。）。", "歴史の（。荒波（。を生き抜いて（。きた「アレゴリー（寓話）」の（。中には（。、現代（。を生きる（。私たちのための（。、時（。を超えた（。サバイバル・ガイド（。が（。隠されて（。いるのです。"),
    ("metaphor", "Metaphor", "隠喩、メタファー", "16th Century", "meta (across, over) + pherein (to carry)", "A figure of speech in which a word or phrase is applied to an object or action to which it is not literally applicable", "ある（。概念の（。重みを、別の（。全く（。違う（。場所へと「運び（。フェリー）越える（。メタ）」ことで、理解（。を一瞬（。にして（。爆発的（。に加速（。させる（。、思考（。の（。ワープ航法（。）。", "「人生は（。旅である（。）」という（。使い古された「メタファー（隠喩）」でさえも、あなたが（。今（。迷っている（。森の中で（。思い出せば（。、それは（。確かな（。北極星（。の（。輝きに（。変わるはずです。"),
    ("protagonist", "Protagonist", "主人公、主役", "17th Century", "protos (first) + agonistes (actor, combatant, contender)", "The leading character or one of the major characters in a drama, movie, novel, or other fictional text", "運命の舞台に一番（。最初に放り込まれ、自らの（。信じる（。正義（。のために、誰よりも（。激しく「戦い（。アゴニスト）続ける」こと（。を選んだ、孤独で（。瑞々しい（。勇者の（。魂（。）。", "あなたが自分の（。「プロタゴニスト（主人公）」であることを（。止めた（。時（。、世界（。はただの（。記号（。の（。羅列に（。成り下がって（。しまいます（。。（。どんなに（。脇役（。に見えても（。、あなたの（。物語（。の（。主役（。は、あなた（。しか（。いないのです。"),
    ("antagonist", "Antagonist", "敵対者、ライバル", "16th Century", "anti- (against) + agonistes (actor, combatant, contender)", "A person who actively opposes or is hostile to someone or something; an adversary", "主人公の（。行く手を（。阻み（。、自らの（。信念を持って（。「反対（。アンチ）の（。立場（。から（。激しく戦う（。アゴニスト）」者（。。（。彼（。がいなければ（。、英雄（。は（。決して（。誕生（。しない、闇の世界のかけがえのない（。パートナー（。）。", "「アンタゴニスト（敵対者）」との（。争い（。に（。消耗（。しないで（。ください（。。（。彼（。の（。執拗な（。攻撃（。は（。、あなたの（。中に（。眠る（。（。ダイヤモンド（。を（。磨き（。上げるための（。、神様（。からの（。試練（。であり（。研磨剤（。（。ポリッシュ（。なのですよ。"),
    ("climax", "Climax", "頂点、山場、クライマックス", "16th Century", "klimax (ladder, staircase)", "The most intense, exciting, or important point of something; a culmination or apex", "物語（。の（。緊張（。が（。極限（。まで（。高まり（。、全ての（。伏線（。が（。回収（。され（。て（。、「黄金（。の（。階段（。クリマックス）」の（。最高位（。に（。辿（。り（。着いた（。、エナジー（。の（。絶頂点（。）。", "人生の「クライマックス（絶頂期）」は（。、一度だけ（。では（。ありません（。。（。あなたが（。新しい（。階段（。を（。登り始め（。、その（。一歩一歩を（。踏みしめて（。いる（。とき（。、あなたは（。何度（。でも（。自分史上（。最高の（。自分に出逢（。えるのです。"),
    ("denouement", "Denouement", "大団円、結末、解決", "18th Century", "de- (un-) + nouer (to tie, knot)", "The final part of a play, movie, or narrative in which the strands of the plot are drawn together and matters are explained or resolved", "複雑（。に（。絡（。み合（。った（。運命の（。「結び（。目（。ノーウ）」を（。、慈愛に満ちた（。手つき（。で（。一つずつ「解（。き（。ディ）ほぐし（。）」、全ての（。さざ波（。が（。静かな（。湖面（。へと（。還（。り（。ゆく（。、安らぎの（。結末（。）。", "激しい（。戦い（。の（。後（。に（。訪れる（。「デヌーマン（大団円）」の（。静寂（。の中で（。、あなたは（。自分の（。傷跡（。さえも（。、美しい（。物語（。の（。一部として（。、優しく（。愛（。せる（。ように（。なる（。でしょう。"),
    ("pastoral", "Pastoral", "牧歌的な、田園詩の", "14th Century", "pastor (shepherd)", "Associated with country life, typically in a romanticized or idealized way", "都会の（。喧騒（。を（。離れ（。、一人の「羊飼い（。パストール）」となって（。、自然の（。リズム（。と（。一体（。に（。なって（。呼吸（。する（。ような（。、穏やかで（。ノスタルジックな（。魂の（。休息所（。）。", "たまには（。自分の中の「パストラル（牧歌的情緒）」に（。耳（。を（。傾けて（。みませんか（。。（。忙（。し（。さの（。中で（。忘（。れて（。しま（。った（。、自分の（。本当（。の（。声（。が（。、風（。の（。中から（。聞こえて（。くる（。かもしれませんよ。"),
    ("satire", "Satire", "風刺、サタイア", "16th Century", "satura (poetic medley, dish of mixed fruits)", "The use of humor, irony, exaggeration, or ridicule to expose and criticize people's stupidity or vices", "社会の（。矛盾（。を（。、「色々な（。果物（。が（。盛られた（。皿（。サトゥーラ）」のように（。、笑い（。と（。毒（。を（。絶妙に（。ブレンド（。して（。提示（。することで（。、凝り（。固まった（。正義（。を（。激しく（。揺さぶる（。（。、知的な（。嘲笑（。の（。饗宴（。）。", "権力（。（。を（。もっとも（。（。恐れ（。させる（。のは（。、暴力（。ではなく（。、一本（。の（。鋭（。い「サタイア（風刺）」による（。、本質（。を（。射（。抜（。く（。笑い（。なのです。"),
    ("tragedy", "Tragedy", "悲劇", "14th Century", "tragos (goat) + oide (song)", "An event causing great suffering, destruction, and distress, such as a serious accident, crime, or natural catastrophe", "運命の（。不条理（。に（。抗い（。、そして（。美しく（。散（。って（。いく（。者の（。ために（。、「安物（。の（。ヤギ（。トラーゴス）を（。生贄（。として（。歌わ（。れた（。詩（。）」。（。絶望（。の（。淵（。で（。（。、人間の（。尊厳（。を（。最も（。（。高く（。謳い（。上げる（。、魂の（。鎮魂歌（。）。", "あなたの（。身に（。起きた「トラジディ（悲劇）」は（。、あなたが（。それ（。を（。誰か（。の（。ための（。物語（。として（。語（。り（。始めた（。瞬間（。、世界（。を（。癒（。す（。ため（。の（。聖なる（。薬（。に（。変わる（。のです。"),
    ("comedy", "Comedy", "喜劇、コメディ", "14th Century", "komos (revel, merry-making) + oide (song)", "Professional entertainment consisting of jokes and satirical sketches, intended to make an audience laugh", "どんなに（。悲惨（。な（。状況（。であっても（。、「陽気な（。酒宴（。コーモス）」のように（。、失敗（。を（。笑い飛ばし（。、再生（。と（。祝祭（。の（。予感（。を（。世界（。に（。解き放つ（。、生命の（。不屈（。な（。肯定感（。）。", "悲劇（。は（。クローズアップ（。で（。撮れば（。、それ（。は（。喜劇（。になる（。。（。あなたの（。悩み（。を（。「コメディ（喜劇）」として（。（。眺める（。ことのできる（。知的な（。距離（。を（。、常に（。心（。の（。ポケット（。に（。忍ばせて（。おいて（。ください。"),
    ("drama", "Drama", "演劇、ドラマ", "16th Century", "draein (to do, act)", "A play for theater, radio, or television", "ただ（。眺める（。のではなく（。、自らが（。舞台（。の（。真ん中（。で「行動し、演（。じ（。ドライン）切る」こと（。。（。葛藤（。を（。抱え（。ながら（。も（。、一歩（。前へ（。踏み出そう（。とする（。、意志（。の（。物理的（。な（。軌跡（。）。", "「ドラマ（劇的な展開）」を（。期待して（。（。待つ（。のは（。止め（。ましょう（。。（。あなたが（。今（。ここで（。下（。す（。小さな（。決断（。と（。行動（。こそが（。、世界（。の（。脚本（。を（。書き換える（。、最高の（。演目（。な（。（。のです。"),
    ("epic", "Epic", "叙事詩、壮大な、エピック", "16th Century", "epos (word, song, speech)", "A long poem, typically one derived from ancient oral tradition, narrating the deeds and adventures of heroic or legendary figures or the history of a nation", "一人の（。英雄（。の（。物語（。を超え（。、民族（。や（。文明（。の（。記憶（。を「言葉（。エポス）」に（。よって（。、永遠（。の（。石碑（。のように（。壮大（。に（。刻（。み（。上げた（。、時（。の（。巨大な（。うねり（。）。", "たとえ（。今は（。名もなき（。生活（。の一コマ（。であっても（。、あなたが（。歩んで（。きた（。歴史（。は（。、私（。に（。とっては（。何物（。にも（。代えがたい「エピック（壮大な詩）」の（。ように（。、気高く（。（。眩（。く（。見える（。（。もの（。なのです。"),
    ("lyric", "Lyric", "叙情詩、歌詞、リリック", "16th Century", "lyra (lyre - a musical instrument)", "Expressing the writer's emotions in an imaginative and beautiful way", "外部（。の（。出来事（。を（。追う（。のではなく（。、自らの（。内なる（。繊細（。な（。感情（。を「竪琴（。リラ）の（。調べ」に乗せて（。、宇宙（。の（。微細（。な（。振動（。と（。共鳴（。させよう（。とする（。、魂の（。モノローグ（。）。", "言葉（。に（。ならない（。痛（。み（。を（。、無理に（。論理（。で（。固め（。ないで（。ください（。。（。その（。痛みを「リリック（叙情詩）」として（。、ただ（。静かに（。歌い（。上げる（。だけで（。、心（。の（。棘（。は（。消えて（。ゆく（。のですよ。"),
    ("motif", "Motif", "標語、主題、モチーフ", "19th Century", "movere (to move)", "A distinctive feature or dominant idea in an artistic or literary composition", "物語（。や（。絵画（。の（。中で（。何度も（。繰り返し（。登場し（。、観る（。者の（。心を「動か（。し（。ムーブ）導く」ための（。、象徴（。的な（。イメージ（。の（。断片（。）。", "あなたの（。これまでの（。人生（。に（。通底（。（。する「モチーフ（主題）」は（。何（。ですか（。？（。それ（。を（。見つけ出した（。とき（。、今まで（。の（。バラバラの（。経験（。の意味（。が（。、一気（。に（。鮮明に（。浮かび上がって（。くる（。はずです。"),
    ("theme", "Theme", "主題、テーマ", "14th Century", "tithenai (to place, put)", "The subject of a talk, a piece of writing, a person's thoughts, or an exhibition; a topic", "あらゆる（。エピソード（。の（。中心（。に「配置（。さ（。ティ）れた」こと（。。（。その（。物語（。が（。、結局（。何を（。世界（。に（。問いかけ（。ようと（。している（。のか（。という（。、作者（。の（。魂の（。叫び（。の（。中心点（。）。", "他人が（。決めた「テーマ（既成の主題）」に（。沿（。って（。生きる（。必要（。は（。ありません（。。（。自分（。の（。人生（。という（。キャンバス（。に（。、あなた（。だけの（。問い（。を（。、あなた（。だけの（。言葉（。で（。配置（。して（。（。ください。"),
    ("plot", "Plot", "筋書き、陰謀、プロット", "16th Century", "plat (flat surface, area of land)", "The main events of a play, novel, movie, or similar work, devised and presented by the writer as an interrelated sequence", "広大（。な（。事実の（。荒野（。（。の上に（。、ある（。特定の（。意図を持って（。「区画（。プラット）」を（。整理（。し（。、出来事（。の（。因果関係（。を（。、ダイナミック（。に（。繋ぎ合わ（。せた（。、物語（。の（。設計図（。）。", "人生（。の「プロット（筋書き）」が（。思い通り（。に（。進（。まない（。ときこそ（。、新しい（。キャラクター（。や（。、意外（。な（。伏線（。を（。投入する（。チャンス（。な（。（。のです（。。（。物語（。を（。面白く（。する（。のは（。、いつ（。だって（。予期（。せぬ（。トラブル（。な（。（。のです。"),
    ("fiction", "Fiction", "フィクション、虚構", "14th Century", "fingere (to shape, mold, feign)", "Literature in the form of prose, especially short stories and novels, that describes imaginary events and people", "ただの（。嘘（。ではなく（。、想像力（。の（。粘土（。を「丹念（。に（。捏（。ね（。、かたち（。作（。った（。フィンジール）」もの（。。（。泥臭（。い（。現実（。から（。は（。決して（。辿（。り（。着（。けない（。、もう（。一つの（。真実（。の（。姿（。）。", "「フィクション（虚構）」とは（。、真実（。を（。隠（。すための（。ものでは（。なく（。、あまりに（。巨大（。すぎて（。直視（。できない（。真実（。を（。、唯一（。語る（。ことのできる（。魔法（。な（。のだと（。私は（。思い（。ます。"),
    ("anecdote", "Anecdote", "逸話、アネクドート", "17th Century", "an- (not) + ekdidonai (publish)", "A short and amusing or interesting story about a real incident or person", "公的（。な（。歴史（。の（。中で（。「出版（。され（。ていない（。アン・エク）」、ちょっと（。した（。裏（。話（。や（。、個人的（。な（。こぼれ話（。。（。公式（。記録（。よりも（。（。雄弁（。に（。、その（。人の（。本質（。を（。照（。らし出（。す（。、温（。かな（。エピソード（。）。", "歴史（。の（。年表（。を（。覚える（。より（。、無名（。の（。民衆（。の（。小さな「アネクドート（逸話）」に（。心を（。寄（。せて（。みて（。ください（。。（。そこ（。に、今（。を生きる（。私たち（。への（。本当（。の（。励（。ましが（。隠（。されている（。はず（。ですから。"),
    ("chronicle", "Chronicle", "年代記、記録", "14th Century", "khronos (time)", "A factual written account of important or historical events in the order of their occurrence", "移（。ろ（。い（。ゆく（。出来事（。を（。、「時間（。クロノス）」の（。川の流れに（。沿（。って（。、淡々と（。、そして（。誠実（。に（。書き留（。めた（。、文明（。が（。未来（。へ（。託（。した（。記憶（。の（。回廊（。）。", "あなたの（。日々の（。日記（。は（。、あなた（。だけの「クロニクル（年代記）」です（。。（。何気（。ない（。今日（。の（。一行（。が（。、十年（。後の（。あなた（。に（。とっては（。、かけがえ（。のない（。救（。いの（。言葉（。に（。なる（。かもしれませんよ。"),
    ("anthology", "Anthology", "選集、アンソロジー", "17th Century", "anthos (flower) + legein (to gather)", "A published collection of poems or other pieces of writing", "荒野（。に（。咲（。く（。無数（。の（。言葉（。の（。中から（。、最も（。美しい（。色彩（。を（。放つ（。ものを（。「集めた（。レゲ）花束（。アンソ）」。（。多様（。な（。才能（。が（。響き合い（。、一つの（。新しい（。風景（。を（。形作る（。、瑞々しい（。知性の（。饗宴（。）。", "世界（。は（。悲（。し（。みに（。満（。ちて（。いる（。ように（。見えます（。が（。、喜び（。の（。瞬間（。を（。集（。めて「アンソロジー（花束）」に（。すれば（。、まだまだ（。人生（。は（。、うっとり（。する（。ほど（。美し（。い（。もの（。に（。なる（。はずです。"),
    ("biography", "Biography", "伝記", "17th Century", "bios (life) + graphein (to write)", "An account of someone's life written by someone else", "一人の（。人間（。の「命（。ビオス）」の（。火が（。、どのように（。燃え（。、どのように（。消えて（。いったか（。。（。その（。軌跡（。を（。、言葉（。によって（。「刻（。み（。グラフ）遺した（。）」、不滅（。の（。肖像画（。）。", "他人の「バイオグラフィー（伝記）」を（。読む（。のは（。、その（。人と（。人生（。を（。一瞬（。だけ（。交換（。（。する（。こと（。です（。。（。成功（。の（。方法（。ではなく（。、彼（。が（。その（。絶望（。を（。（。どう（。やって（。飼（。い（。慣（。らした（。か（。、それ（。を（。（。読み取（。って（。ください。"),
    ("prologue", "Prologue", "冒頭、プロローグ", "14th Century", "pro- (before) + logos (word, discourse)", "A separate introductory section of a literary or musical work", "物語（。の（。本編（。が（。始まる「前（。プロ）に（。語られる（。ロゴス）」言葉（。。（。日常（。という（。岸辺（。から（。、物語（。という（。幻想（。の（。海へと（。漕（。ぎ（。出す（。ための（。、静かな（。入江（。のような（。儀式（。）。", "朝（。の（。コーヒー（。一杯（。は（。、今日（。という（。未知（。の（。物語（。への最高（。の「プロローグ（前口上）」ですね（。。（。さあ（。、今日（。は（。どんな（。美しい（。一行（。を（。書き（。加（。え（。ましょうか。"),
    ("epilogue", "Epilogue", "結びの言葉、エピローグ", "14th Century", "epi- (upon, in addition) + logos (word)", "A section or speech at the end of a book or play that serves as a comment on or a conclusion to what has happened", "全ての（。ドラマ（。が（。終わった「後（。エピ）に（。付け加えられた（。ロゴス）」言葉（。。（。余韻（。を（。味わい（。、現実（。の世界（。へと（。再び（。戻（。って（。いく（。ための（。、魂の（。減圧（。の（。時間（。）。", "失敗（。し（。た（。と思（。える（。一日（。に（。も（。、必ず（。美しい「エピローグ（結びの言葉）」を（。探して（。ください（。。（。眠り（。につ（。く（。直前（。に（。、自分（。の（。今日を（。許して（。あげる（。一言（。を（。、そっと（。添（。えて（。）。"),
    ("manuscript", "Manuscript", "草稿、原稿、マニュスクリプト", "16th Century", "manus (hand) + scribere (to write)", "A book, document, or piece of music written by hand rather than typed or printed", "冷たい（。印刷（。技術（。の（。介入（。を（。受ける（。前（。の（。、作者（。の（。「手（。マヌス）」で直接「書き（。スクリプト）遺された」もの（。。（。インク（。の（。滲（。み（。の中に（。、魂の（。震（。え（。が（。剥き出し（。で（。息づいている（。（。貴重な（。痕跡（。）。", "あなた（。の（。人生（。という「マニュスクリプト（手書きの原稿）」は（。、まだ（。インク（。が（。乾い（。て（。（。い（。ません（。。（。何（。度（。でも（。描き（。直し（。、何（。度（。でも（。新しい（。ページ（。を（。めくる（。こと（。が（。できる（。のですよ。"),
    ("poetic", "Poetic", "詩的な", "16th Century", "poiein (to make, create)", "Of, relating to, or used in poetry", "ただの（。情報の（。伝達（。を（。超え（。、世界（。を（。全く（。新しく「作り（。ポイ）直す」ような（。、瑞々しく（。（。、心震（。える（。言葉（。の（。調べ（。）。", "夕暮れ（。の（。空の色（。を（。、ただの（。光波（。だと（。思わず（。、一言の「ポエティック（詩的）」な（。驚き（。で（。受け止める（。こと（。。（。それ（。だけで（。、あなた（。の（。世界（。は（。一瞬（。にして（。祝福（。に（。満たされる（。のです。"),
    ("prose", "Prose", "散文、散文体", "14th Century", "pro- (forward) + vertere (to turn)", "Written or spoken language in its ordinary form, without metrical structure", "飾り（。の（。リズム（。に（。頼らず（。、ただ「真っ直ぐ（。プロ・ヴァース）に（。真実へと（。突き進む）」、地の文（。。（。日常（。の（。手触り（。と（。、実直（。な（。観察（。が（。生み出す（。、飾（。り（。のない（。美しさ（。）。", "あなたの（。誠実（。な（。生き方（。は（。、どんな（。華やかな（。詩（。よりも（。、重み（。のある（。美しい「プロース（散文）」の（。ように（。、人々の（。心（。に（。静かに（。染み（。渡って（。いく（。はずです。"),
    ("stanza", "Stanza", "（詩の）節、スタンザ、部屋", "16th Century", "stare (to stand)", "A group of lines forming the basic recurring metrical unit in a poem; a verse", "詩（。という（。建物（。の中に（。用意された（。、一時の（。休息（。のための「留ま（。り（。スタン）立つ（。ザ）部屋」。意味（。と（。情緒（。が（。一つの（。窓（。から（。差し込む（。、光の（。区画（。）。", "苦しい（。とき（。は（。、自分（。の（。人生（。という（。長い（。詩（。の中に（。、小さな「スタンザ（安らぎの小部屋）」を（。作って（。みてください（。。（。そこ（。で（。一（。息（。つけば（。、また（。次（。の一行（。を（。力強く（。踏み出（。せる（。ように（。なり（。ます。"),
    ("rhythm", "Rhythm", "リズム、韻律", "16th Century", "rhein (to flow)", "A strong, regular, repeated pattern of movement or sound", "淀（。む（。ことなく（。、「流（。れ（。リュ）」続ける（。命の（。拍動（。。（。宇宙（。の（。鼓動（。と（。、あなたの（。心臓（。の（。震（。えが（。、一つの（。美しい（。旋律（。として（。重なり合う（。、生命の（。基本的な（。速度（。）。", "都会の（。忙（。し（。い「リズム（拍動）」に（。飲ま（。れ（。すぎないで（。ください（。。（。自分（。だけの（。心地よい（。流れ（。を（。（。取り戻（。した（。とき（。、世界（。は（。一変（。して（。、あなた（。と（。優しく（。踊（。り（。始め（。ます。"),
    ("imagery", "Imagery", "比喩的描写、イメージ", "14th Century", "imago (copy, likeness, image)", "Visually descriptive or figurative language, especially in a literary work", "言葉（。を（。使って（。、読者の（。脳裏（。に（。鮮明な「虚像（。イマゴ）」を（。結ばせる（。技術（。。（。文字（。という（。冷たい（。粒子（。が（。、一瞬（。にして（。体温（。と（。色彩（。を持った（。生きた（。光景（。へと（。変貌する（。魔法（。）。", "あなたの（。脳裏（。に（。浮かぶ（。、最高の（。未来（。の「イメージリー（図像群）」を（。（。決して（。手放（。さない（。で（。ください（。。（。その（。イメージ（。が（。強（。ければ（。強い（。ほど（。、現実（。は（。磁石（。に（。吸（。（。き寄せ（。られる（。ように（。、その（。かたち（。へ（。と（。変わり（。始め（。ます。"),
    ("allusion", "Allusion", "ほのめかし、典拠、アリュージョン", "16th Century", "ad- (to) + ludere (to play)", "An expression designed to call something to mind without mentioning it explicitly; an indirect or passing reference", "直接（。語る（。代わりに（。、過去（。の（。巨大（。な（。物語（。の（。破片（。へと「ちょっと（。遊び（。リュ）に（。行く」ような（。仕草（。。（。共有（。された（。記憶（。を（。、目配せ（。するように（。、そっと（。呼び覚（。ます（。、知的な（。悪戯（。）。", "彼（。の（。言葉（。の（。端々（。に（。隠された（。小さな「アリュージョン（ほのめかし）」に（。気づいた（。とき（。、あなた（。と（。彼（。の（。間（。には（。、何物（。にも（。代（。え（。がたい（。、秘密（。の（。友情（。の（。絆（。が（。生まれる（。のですよ。"),
    ("dialogue", "Dialogue", "対話、ダイアログ", "13th Century", "dia- (through, across) + logos (word)", "Conversation between two or more people as a feature of a book, play, or movie", "お互い（。の（。世界（。を（。「横断（。ダイア）する（。ロゴス）」こと（。。（。自分（。という（。殻（。を（。破（。り（。、他者（。という（。未知（。の（。真実（。の（。中を（。、言葉（。の（。糸（。を（。手繰（。り（。ながら（。旅する（。、知的な（。交感（。）。", "「ダイアログ（対話）」とは（。、相手（。を（。説得（。する（。ことでは（。ありません（。。（。相手（。と（。自分（。の（。違い（。を（。、一つの（。新しい（。音楽（。として（。楽しむ（。、その（。心の（。余裕（。の（。こと（。を（。いう（。のです。"),
    ("soliloquy", "Soliloquy", "独白、自問自答", "17th Century", "solus (alone) + loqui (to speak)", "An act of speaking one's thoughts aloud when by oneself or regardless of any hearers, especially by a character in a play", "観客（。を（。忘れ（。、暗い（。舞台（。の（。隅（。で「独り（。ソロ）で（。語る（。ロキー）」こと（。。（。他者（。への（。お世辞（。や（。虚飾（。を（。剥（。ぎ（。取（。った（。、自分（。自身の（。魂（。へ（。の（。最も（。残酷（。で（。誠実（。な（。告白（。）。", "真夜中（。に（。ふと（。口（。を（。突いて（。出た「ソリロキー（独白）」。それ（。こそが（。、あなた（。が（。一番（。大切（。に（。する（。べき（。、あなたの（。本心（。からの（。メッセージ（。な（。（。のかも（。しれません。"),
    ("monologue", "Monologue", "一人芝居、独白", "17th Century", "monos (alone, single) + logos (word, speech)", "A long speech by one actor in a play or movie, or as part of a theatrical or broadcast program", "周囲（。との（。繋がり（。を（。遮断（。し（。、ただ「一人の（。モノ）言葉（。ロゴス）」を（。世界（。の（。中心（。へと（。響（。かせ（。続ける（。こと（。。（。孤独（。な（。英雄（。が（。、自ら（。の（。正義（。を（。確信（。する（。ための（。、孤独（。な（。凱旋の（。ドラム（。）。", "「モノローグ（一人語り）」の（。時間を（。大切（。に（。して（。ください（。。（。他人の（意見（。を（。黙（。らせて（。、自分（。自身の（。物語（。を（。一気に（。語（。り（。明かす（。、その（。爽快感（。が（。あなた（。を（。また（。強く（。する（。のです。"),
    ("sonnet", "Sonnet", "ソネット、14行詩", "16th Century", "sonus (sound)", "A poem of fourteen lines using any of a number of formal rhyme schemes, in English typically having ten syllables per line", "厳格（。な（。ルール（。に（。縛（。られ（。ながら（。も（。、その（。中で（。極限（。の（。美（。を（。追求（。する「小（。さな（。調べ（。ソン）」。（。制約（。が（。ある（。から（。こそ（。、言葉（。は（。ダイヤモンド（。の（。ように（。鋭く（。、（。輝（。（。（。く（。の（。です。"),
    ("haiku", "Haiku", "俳句", "19th Century", "hai- (play) + -ku (phrase)", "A Japanese poem of seventeen syllables, in three lines of five, seven, and five, traditionally evoking images of the natural world", "遊び（。ハイ）の（。（。句（。ク）」。（。極限（。まで（。削（。ぎ（。落（。された（。十七音（。。（。世界（。の（。一瞬（。の（。煌（。めきを（。、たった（。三行（。に（。（。凝縮（。して（。永遠（。に（。変える（。、言葉（。による（。瞬（。間の（。写真。"),
    ("ballad", "Ballad", "バラード、叙事歌、民謡", "15th Century", "ballare (to dance)", "A poem or song narrating a story in short stanzas", "かつて（。人々（。が「踊り（。バラ）ながら」口（。ず（。さんだ（。、名もなき（。者（。たち（。の（。喜び（。と（。悲しみ（。の（。物語（。。（。時（。の（。洗礼（。を（。受（。け（。て（。残（。った（。、エッセンス（。の（。ような（。優（。し（。い（。旋律。"),
    ("ode", "Ode", "頌歌（しょうか）、オード", "16th Century", "oide (song, chant)", "A lyric poem in the form of an address to a particular subject, often elevated in style or manner and written in varied or irregular meter", "ある（。特定（。の（。存在（。や（。理想（。を（。、心（。から（。「讃える（。歌（。オード）」。称賛（。と（。敬意（。を（。、格調（。高く（。、そして（。情熱的（。に（。（。謳（。い（。上げる（。、魂の（。祝辞。"),
    ("parody", "Parody", "パロディ、替え歌、下手な模倣", "16th Century", "para- (beside, along side) + oide (song)", "An imitation of the style of a particular writer, artist, or genre with deliberate exaggeration for comic effect", "偉大な（。作品（。の「横（。パラ）で（。歌われる（。詩（。）」。（。硬（。い（。正義（。を（。、ユーモア（。の（。力（。で（。相対化（。し（。、違（。った（。角度（。から（。光（。を（。当（。て（。直す（。、知的な（。悪戯（。の（。精神。")
]

def run_cycle():
    file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
        if not match:
            print("Error: Could not find WORDS array in data.js")
            return

        prefix, json_array_str, suffix = match.groups()
        existing_words = json.loads(json_array_str)
        existing_ids = {w.get("id") for w in existing_words}
        existing_word_texts = {w.get("word").lower() for w in existing_words}

        added_count = 0
        for item in words_data:
            word_text = item[0]
            word_id = f"{word_text.lower()}_lit"
            
            if word_id not in existing_ids and word_text.lower() not in existing_word_texts:
                new_word = {
                    "id": word_id,
                    "word": word_text,
                    "meaning": item[2],
                    "era": item[3],
                    "etymology": {
                        "components": [item[4]],
                        "original_statement": f"From {item[3]} {item[4]}."
                    },
                    "concept": item[5] + f" ({item[6]})",
                    "thinking": item[6],
                    "aftertaste": item[7] if len(item) > 7 else "物語は、絶望を希望へと変える世界で唯一の魔法です。",
                    "example": f"The author crafted a compelling {word_text} that resonated with readers worldwide.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["文学とは、言葉の檻（おり）の中で、真実の翼を羽ばたかせる行為です。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["poetic", "pastoral", "epic", "lyric"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Literature & Narrative (Cycle 29).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
