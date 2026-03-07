import json
import re

# Theme: The Architecture of Emotions (Cycle 22)
words_data = [
    ("affection", "Affection", "愛情、愛着", "13th Century", "affectio (influence, state of mind)", "A gentle feeling of fondness or liking", "激しい情熱というよりは、時間をかけて育まれた、静かに心に染み渡るような「穏やかな好意」の状態。", "古いぬいぐるみへの「アフェクション（愛着）」は、共に過ごした時間が魔法となって宿っている証拠です。"),
    ("adoration", "Adoration", "崇拝、深い愛", "14th Century", "adorare (to pray to)", "Deep love and respect", "ただ愛するだけでなく、相手を尊いものとして仰ぎ見る「祈りのような」究極の献身と尊敬。", "赤ちゃんの無垢な寝顔を見つめる母親の瞳には、言葉を超えた「アドラシオン（深い慈しみと崇拝）」が宿っています。"),
    ("bliss", "Bliss", "至福、無上の喜び", "Old English", "blis (joy, happiness, grace)", "Perfect happiness; great joy", "一点の曇りもなく、世界のすべてが祝福に満ちていると感じられる「魂の絶頂」における静かな法悦。", "波の音だけが聞こえる砂浜で目を閉じれば、そこには完璧な「ブリス（至福）」の瞬間が待っています。"),
    ("contentment", "Contentment", "満足、安らぎ", "15th Century", "continentia (restraint, self-control)", "A state of happiness and satisfaction", "欲望を無理に広げるのではなく、今あるものの中に十分な豊かさを見出し「自らの心を制御し満たしている」穏やかな静止状態。", "温かいお茶を一杯飲むだけで、心は深い「コンテントメント（足るを知る満足）」に包まれることがあります。"),
    ("euphoria", "Euphoria", "幸福感、陶酔感", "17th Century", "euphoria (power of enduring easily)", "A feeling or state of intense excitement and happiness", "まるで重力から解放されたかのように、すべてが上手くいき、心の中に「心地よい熱狂」が渦を巻く最高潮の肯定感。", "マラソンを完走した瞬間の「ユーフォリア（圧倒的な高揚感）」は、これまでの苦しみすべてを黄金の記憶に変えてくれます。"),
    ("ecstasy", "Ecstasy", "無我夢中、恍惚", "14th Century", "ekstasis (standing outside oneself)", "An overwhelming feeling of great happiness or joyful excitement", "自分の意識という殻を突き破り、魂が一時的に「外へと飛び出してしまう」ほどの、言語を絶する烈しい法悦。", "コンサートの熱狂の中で、聴衆は自らを忘れ、音楽という名の「エクスタシー（恍惚）」の淵へと沈んでいきました。"),
    ("yearning", "Yearning", "切ない思い、憧憬", "Old English", "giernan (to desire, strive)", "A feeling of intense longing for something", "手が届かないものを求め、胸の奥がきゅっと締め付けられるような「切実な渇望」と、それゆえの美しい痛み。", "故郷の海を想う「ジャーニング（切ない憧憬）」は、どんなに遠くへ行っても魂の羅針盤となってあなたを支えます。"),
    ("nostalgia", "Nostalgia", "郷愁、追憶", "18th Century", "nostos (return home) + algos (pain)", "A sentimental longing or wistful affection for the past", "二度と戻れない過去の場所や時間への、甘く切ない「帰還への痛み」を伴う、時空を超えた愛おしい記憶の旅。", "古い写真の匂いを嗅ぐだけで、一瞬にして子ども時代の「ノスタルジア（郷愁）」の魔法にかかってしまいます。"),
    ("melancholy", "Melancholy", "憂鬱、哀愁", "14th Century", "melas (black) + khole (bile)", "A feeling of pensive sadness, typically with no obvious cause", "原因は不明だが、心の中に「黒い胆汁（沈殿物）」が溜まっていくように、静かに、そして思慮深く沈み込む、秋の夕暮れのような悲しみ。", "雨の午後にふと感じる「メランコリー（哀愁）」は、自分自身の内面と深く対話するための大切な鍵となります。"),
    ("sorrow", "Sorrow", "悲しみ、嘆き", "Old English", "sorh (care, anxiety, grief)", "A feeling of deep distress caused by loss, disappointment, or other misfortune", "喪失や痛みという鋭い刃によって心が深く傷つき、重い「苦悩の衣」を纏ってしまったかのような、震えるような哀しみ。", "今は立ち上がれなくても、その「ソロウ（深い悲しみ）」の底には、いつか芽吹く新しい強さの種が眠っています。"),
    ("grief", "Grief", "深い悲しみ、苦悩", "13th Century", "gravare (to weigh down)", "Deep sorrow, especially that caused by someone's death", "耐え難いほどの「重みが魂にのしかかり」、呼吸することさえ困難にさせるほど、誰かの死や別れを悼む重厚な悲哀。", "失ったものを悼む「グリーフ（深い嘆き）」の時間は、愛した記憶を自分の一部へと変えていくための神聖なプロセスです。"),
    ("anguish", "Anguish", "苦悩、激痛", "13th Century", "angustia (tightness, narrowness)", "Severe mental or physical pain or suffering", "出口のない狭い隙間（アングスティア）に「締め付けられ」、心身が引き裂かれるような激烈な苦しみと絶望の発露。", "選択の余地がないという「アンギッシュ（激しい苦悶）」の中で、彼は自分の本当の信念を見出すことになります。"),
    ("despair", "Despair", "絶望", "14th Century", "de- (without) + sperare (to hope)", "The complete loss or absence of hope", "希望という光の粒子が完全に「失われ（除去され）」、目の前の道も、自分自身の存在理由さえも見えなくなってしまった精神の暗黒。", "「デスペア（絶望）」の淵で見た小さな星屑こそが、次の新しい朝を連れてくる最初の一歩になるはずです。"),
    ("resentment", "Resentment", "憤慨、恨み", "17th Century", "re- (again) + sentire (to feel)", "Bitter indignation at having been treated unfairly", "人から受けた不当な扱いや痛みを、心の中で「何度も繰り返し感じ直す」ことで自分を毒し続ける、冷たく不自由な怒り。", "過去の「リゼントメント（恨み）」を手放すことは、相手を許すのではなく、自分自身をその呪縛から解放することなのです。"),
    ("indignation", "Indignation", "憤り、義憤", "14th Century", "in- (not) + dignus (worthy)", "Anger or annoyance provoked by what is perceived as unfair treatment", "不正や卑劣な行為に対し、自分の尊厳が「ふさわしくない（不当である）」と叫ぶ、知性に基づいた正義の炎。", "理不尽な差別に対する「インディグネーション（高潔な憤り）」こそが、この不完全な世界を少しずつ良くしていく力です。"),
    ("wrath", "Wrath", "激怒、憤怒", "Old English", "wraith (wroth, angry)", "Extreme anger", "理性の制御を完全に超え、雷（いかずち）のように全てを焼き尽くし破壊しようとする「神罰の如き」強烈な怒りの奔流。", "あなたの「ラス（激しい怒り）」を破壊の道具ではなく、困難を突破するためのエナジーへと昇華させてください。"),
    ("fury", "Fury", "猛烈な怒り、復讐の女神", "14th Century", "furere (to be mad, rage)", "Wild or violent anger", "髪を振り乱して踊り狂う女神のように、自分でも制御できない「狂気的な激しさ」を伴った爆発的な怒りの嵐。", "嵐のあとの静寂のように、その猛烈な「フューリー（憤怒）」が過ぎ去れば、また新しい風景が見えてくるでしょう。"),
    ("apprehension", "Apprehension", "懸念、不安、理解", "14th Century", "apprehendere (to seize, take hold of)", "Anxiety or fear that something bad or unpleasant will happen", "まだ見ぬ未来の出来事を、今の自分の心が「ぎゅっと掴んでしまい（捉えてしまい）」、その重さに身をすくませる不安の影。", "新しい挑戦への「アプレヘンション（不安と期待の入り混じった懸念）」は、あなたが真剣であるという最高の証です。"),
    ("dread", "Dread", "恐怖、畏怖", "12th Century", "drædan (to fear greatly)", "Anticipate with great apprehension or fear", "避けられない恐ろしい何かが刻一刻と近づいてくるのを、体全体の「震えと寒気」をもって予感している極限の恐怖心。", "誰もいない暗い廊下で感じる「ドレッド（底知れぬ恐怖）」は、人間の本能があなたを守るために発している警報です。"),
    ("terror", "Terror", "恐怖、テロ", "14th Century", "terrere (to frighten)", "Extreme fear", "あまりにも強烈な恐怖によって、思考や肉体が完全に「凍りつき（麻痺し）」、ただ震えることしかできない絶対的な脅威。", "「テラー（戦慄）」のような恐怖のどん底にあっても、あなたの心にある勇気という小さな灯火だけは消えません。"),
    ("bewilderment", "Bewilderment", "当惑、狼狽", "17th Century", "be- (thoroughly) + wildern (lead astray, lure into the wild)", "A feeling of being perplexed and confused", "まるで知識の及ばない「野生の森（荒野）のど真ん中に」放り出されたように、進むべき方向も意味も完全に見失った混乱。", "人生のあまりの複雑さに「ビウィルダーメント（当惑）」した時は、一度立ち止まって、ただ足元の花を愛でてください。"),
    ("amazement", "Amazement", "驚き、感嘆", "16th Century", "amaze (to stun, stupefy, bewilder)", "A feeling of great surprise or wonder", "あまりにも予期せぬ出来事の輝きに、一瞬だけ思考が「迷宮（メイズ）へと誘われ」一時停止してしまうほどの純粋な驚愕。", "子どもの瞳に宿る「アメイズメント（混じり気のない驚き）」は、この世界が魔法に満ちていることを教えてくれます。"),
    ("awe", "Awe", "畏敬、恐れ", "13th Century", "agi (fright, fear)", "A feeling of reverential respect mixed with fear or wonder", "ただ恐ろしいだけでなく、あまりに巨大で神聖なもの（宇宙や大自然）を前にして、自分自身の「小ささを喜びとともに悟る」崇高な感情。", "満天の星空の下で感じる「オー（畏敬の念）」は、私たちが大きな生命の循環の一部であることを思い出させます。"),
    ("reverence", "Reverence", "尊敬、崇拝", "13th Century", "revereri (to fear, respect)", "Deep respect for someone or something", "表面的な敬意を超え、そこに宿る高貴な魂や歴史の重みに対し、心から「畏れ（うやまい）」、跪くような静かな敬虔さ。", "古い木々や先人たちの知恵に対し、深い「レヴェランス（敬虔な尊敬）」を持って接すること。それが学びの第一歩です。"),
    ("humility", "Humility", "謙虚、卑下", "14th Century", "humus (ground, soil)", "A modest or low view of one's own importance", "自らが「大地（土）と同じ低さに」あることを自覚し、傲慢さを捨てて他者の声や真理をありのままに受け入れようとする、最も気高い知性の姿勢。", "真の強者は「ヒュミリティ（謙虚さ）」を纏っています。自らの価値を証明する必要など、もはやないからです。"),
    ("pride", "Pride", "誇り、自尊心", "Old English", "pryde (proude, arrogant)", "A feeling or deep pleasure or satisfaction derived from one's own achievements", "自分が成し遂げたこと、あるいは自分という存在そのものに対する「真っ直ぐな自負」であり、困難の中で自分自身を支える最後の砦。", "「プライド（誇り）」は、他人に勝つための道具ではなく、自分が自分であることを絶対に諦めないための強さです。"),
    ("arrogance", "Arrogance", "傲慢、不遜", "14th Century", "arrogare (to claim for oneself)", "The quality of being arrogant", "他者の価値を認めず、全ての功績や権利を「自分だけのものだと不当に主張」し、天を仰ぐことを忘れてしまった心の肥大化。", "「アロガンス（傲慢）」という名の重い鎧を捨てない限り、あなたは誰からも、そして自分自身からも真に愛されることはありません。"),
    ("contempt", "Contempt", "軽蔑、蔑み", "14th Century", "contemnere (to slight, despise)", "The feeling that a person or a thing is beneath consideration, worthless, or deserving scorn", "相手を単に嫌うのではなく、そこに「一瞥の価値もない（考慮に値しない）」と断じ、自らの視界から完全に消し去ろうとする冷酷な心理的抹殺。", "誰かを「コンテンプト（軽蔑）」することは、自分の心の器をその分だけ汚していることに他なりません。"),
    ("disdain", "Disdain", "軽蔑、拒絶", "14th Century", "de- (not) + dignari (deem worthy)", "The feeling that someone or something is unworthy of one's consideration or respect", "自分自身の高貴さを守るために、相手を「自分に相応しくない（値しない）」とみなして、意識的に冷たく距離を置く拒絶の姿勢。", "高慢な「ディスデイン（蔑み）」を持って他者を跳ね除けるなら、あなたは一生、孤独という名の王室に閉じ込められるでしょう。"),
    ("empathy", "Empathy", "共感、感情移入", "20th Century", "en- (in) + pathos (feeling)", "The ability to understand and share the feelings of another", "他者の心の中に「入り込み」、相手が感じている喜びや痛みを、まるで自分のことのように（あるいはそれ以上に）震えながら感じ取ること。", "「エンパシー（共感）」とは、他人の靴を履いて歩くこと。その痛みを理解したとき、世界はもっと優しくなれるはず。"),
    ("compassion", "Compassion", "慈悲、深い同情", "14th Century", "com- (together) + pati (to suffer)", "Sympathetic pity and concern for the sufferings or misfortunes of others", "相手の苦しみを「共に受け（苦しむ）」し、何とかしてその重荷を分け合いたいと願う、行動を伴う深い慈しみと愛情。", "あなたの「コンパッション（慈悲）」という温かい手が、孤独に震える誰かの魂にとっての最後の避難所になるのです。"),
    ("altruism", "Altruism", "利他主義", "19th Century", "altri (others)", "The belief in or practice of disinterested and selfless concern for the well-being of others", "自らの利益を度外視し、ただ「他者の幸福（喜び）」を唯一の目的として行動する、人間の魂が到達できる最高に美しい献身の極地。", "「アルトルイズム（利他心）」を持って差し出されたパンは、どんな豪華な晩餐よりも多くの人を満たし、幸福にします。"),
    ("loneliness", "Loneliness", "孤独感、寂しさ", "16th Century", "alone + -ly + -ness", "Sadness because one has no friends or company", "どれほど多くの人に囲まれていても、自分の本質が「ただ一人（独り）」であり、誰とも繋がれていないと感じる精神の空洞と寒気。", "夜の「ロンリネス（孤独感）」に負けそうなときは、月を見上げて。同じ月を、同じ気持ちで見ている誰かが必ずどこかにいます。"),
    ("solitude", "Solitude", "孤独、独り居", "14th Century", "solitudo (loneliness, alone)", "The state or situation of being alone", "他者との強制的な関わりから離れ、自分自身と「心地よく（自発的に）」対話するために用意された、静寂と知性に満ちた聖なる独りの時間。", "「ソリチュード（独りを楽しむ時間）」を持つことで初めて、私たちは他者を真に尊重し、愛するための力を蓄えることができます。"),
    ("tranquility", "Tranquility", "静寂、平穏", "14th Century", "tranquillitas (calmness, quietness)", "The quality or state of being tranquil; calm", "一切の激しい波風が立ち去り、湖面のように「静まり返った（平穏な）」心。あらゆる雑音から解放された極上の平和。", "森の奥深くで「トランキリティ（しじま）」に身を委ねれば、都会で削り取られた魂の欠片がゆっくりと再生していきます。"),
    ("serenity", "Serenity", "平穏、落ち着き", "14th Century", "serenus (clear, bright)", "The state of being calm, peaceful, and untroubled", "嵐のあとの空のように、雲一つなく「澄み渡り（明るい）」、どんな外部からの妨害にも揺らぐことのない不動の静寂と落ち着き。", "自分の力で変えられることと、変えられないことを見極める知恵。それが真の「セレニティ（心の平安）」を連れてきます。"),
    ("patience", "Patience", "忍耐、根気", "13th Century", "pati (to suffer)", "The capacity to accept or tolerate delay, trouble, or suffering without getting angry or upset", "痛みに耐えながら、時期が来るのをじっと「待ち続ける」こと。自らの感情を制御し、時の流れに魂を委ねる静かなる闘争。", "「ペイシェンス（忍耐）」とは、ただ待つことではありません。待っている間、ずっと未来を信じ続け、準備を怠らないことです。"),
    ("resilience", "Resilience", "回復力、弾力性", "17th Century", "resilire (to recoil, rebound)", "The capacity to recover quickly from difficulties; toughness", "どれだけ過酷な状況に押し潰されようとも、本来の形を失うことなく「再び跳ね上がる（跳ね返る）」魂のしなやかな反発力。", "「レジリエンス（折れない心）」を持った人は、失敗を経験するたびに、前よりも高く高く飛ぶためのバネを手に入れるのです。"),
    ("fortitude", "Fortitude", "不屈の精神、勇気", "14th Century", "fortis (strong)", "Courage in pain or adversity", "単なる蛮勇ではなく、苦難や誘惑の中で自らの信念を「強固に（強く）」守り抜き、最後まで歩みを止めない大人の高潔な勇気。", "逆境という暗闇を抜ける唯一の松明（たいまつ）は、あなたの「フォーチュチュード（不屈の精神）」という光だけです。"),
    ("zeal", "Zeal", "熱意、熱情", "14th Century", "zelos (jealousy, fervor)", "Great energy or enthusiasm in pursuit of a cause or an objective", "まるで嫉妬のような猛烈な激しさを持って、一つの理想や目標に「魂を燃焼させ」、周囲をも巻き込んでいく圧倒的な前向きなエネルギー。", "あなたの「ジール（情熱）」という炎が、冷え切ったこの社会のどこかに、新しい希望の明かりを灯すかもしれません。"),
    ("fervor", "Fervor", "熱烈な、熱情", "14th Century", "fervere (to boil)", "Intense and passionate feeling", "内側から「沸き立つ（沸騰する）」ような、抑えきれない激しい情熱と信念。真実を求める心が放つ黄金色の熱気。", "「ファーヴァー（熱烈な情熱）」を持って語られる言葉は、どんなに洗練された理論よりも力強く、聴く者の心を打ち震わせます。"),
    ("apathy", "Apathy", "無関心、冷淡", "17th Century", "a- (without) + pathos (feeling)", "Lack of interest, enthusiasm, or concern", "喜びも悲しみも、もはや「感じること（パトス）を放棄」し、世界との繋がりを完全に断ち切ってしまった魂の灰色の中立状態。", "怒りよりも悲しいのは「アパシー（無関心）」です。あなたが世界に関心を持つのを止めた時、世界もあなたを見失ってしまう。"),
    ("detachment", "Detachment", "切り離し、超然", "17th Century", "de- (not) + attachier (to attach, join)", "The state of being objective or aloof", "特定の感情や結果に「執着するのをやめ」、少し離れた場所から自分自身や出来事を冷静に眺めることで得られる自由な視点。", "深い愛を持っていながら、同時に冷静な「デタッチメント（超然とした客観性）」を保つこと。それが真の自由への入り口です。"),
    ("ambivalence", "Ambivalence", "両価性、ためらい", "20th Century", "ambi- (both) + valentia (strength)", "The state of having mixed feelings or contradictory ideas about something or someone", "相反する二つの強い想いが「同じ力で（等価に）」引き合い、どちらにも進めないまま魂が戸惑っている、人間らしい繊細な葛藤。", "愛しているのに憎いという「アンビバレンス（ためらいと葛藤）」こそが、人間という深遠なドラマの最も美しいシーンなのです。"),
    ("equanimity", "Equanimity", "平静、落ち着き", "17th Century", "aequus (even, equal) + animus (mind)", "Mental calmness, composure, and evenness of temper, especially in a difficult situation", "どんなに外部が荒れ狂っていても、内側は常に「平らで（均等な）」状態を保ち、理性を失うことのない、賢者の究極の安定感。", "嵐の海を航海する船長のように、心の中に「エクアニミティ（平静の極地）」という不動のコンパスを持っておきましょう。")
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
            word_id = f"{word_text.lower()}_emotion"
            
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
                    "aftertaste": item[7],
                    "example": f"He felt a profound sense of {word_text} wash over him.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["感情の語源を探ることは、人間という多層的な構造を理解することに繋がります。"]
                    },
                    "part_of_speech": "noun"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Architecture of Emotions (Cycle 22).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
