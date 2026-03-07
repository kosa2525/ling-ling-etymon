import json
import re

words_data = [
    ("ponder", "Ponder", "熟考する", "14th Century", "ponderare (to weigh)", "Think about carefully", "見えない精神の天秤に複数の選択肢を乗せ、それぞれの重みをゆっくりと量り比べること。", "焦って出た答えより、湖畔で「ポンダー（熟考）」して導き出した結論の方が深く輝きます。"),
    ("contemplate", "Contemplate", "沈思黙考する、凝視する", "16th Century", "contemplari (to clear an open space for observation)", "Look thoughtfully", "神聖な空間を切り開き、そこに宇宙の意志を降ろすようにして対象を深く、静かに観察し続けること。", "夜空の星を「コンテンプレート（深く見つめ考える）」する時間は、魂の休息です。"),
    ("muse", "Muse", "物思いにふける", "14th Century", "muser (to ponder, dream)", "Absorbed in thought", "理性の手綱を緩め、芸術や詩の神々（ミューズ）が囁くインスピレーションの海に心を漂わせる甘美な時間。", "「ミューズ（物思い）」の中を漂う時、あなたは日常の重力から完全に解放されています。"),
    ("meditate", "Meditate", "瞑想する", "16th Century", "meditari (to think over, consider)", "Focus one's mind", "外部の喧騒を遮断し、自分自身の内なる深淵へと潜り込み、本来の透明な自己と再会するための訓練。", "一日５分、「メディテイト（瞑想）」するだけで、あなたの心に小さなオアシスが生まれます。"),
    ("ruminate", "Ruminate", "反芻する、思い返す", "16th Century", "ruminare (to chew the cud)", "Think deeply about something", "牛が草を噛み返すように、過去の出来事や言葉を二度も三度も噛み砕き、その真意を自らの血肉へと変えること。", "他人から投げられたトゲのある言葉を「ルミネート（ずっと反芻）」して自分を傷つけるのはやめましょう。"),
    ("deliberate", "Deliberate", "よく考える、意図的な", "15th Century", "deliberare (to weigh well)", "Engage in long consideration", "感情の波に流されず、全ての起こり得る結果を客観的かつ冷徹に計算し尽くして石橋を叩くこと。", "「デリバレイト（慎重で意図的）」な優しさは、時に天然の優しさよりも相手を深く救います。"),
    ("deduce", "Deduce", "推論する、演繹する", "16th Century", "deducere (to lead down)", "Arrive at a fact by reasoning", "既に存在している巨大な真理の大前提から、目の前の小さな事実を「下へと引き下ろして」結論を導き出す知的なパズル。", "名探偵のように、わずかな証拠から真実を「ディデュース（推測・演繹）」する快感を。"),
    ("infer", "Infer", "推測する、ほのめかす", "16th Century", "inferre (to bring in)", "Deduce from evidence", "目の前に提示された断片的な事実（証拠）たちを「内に運び込み」、そこから見えない全体像を描き出す想像力。", "言葉の裏にある相手の本当の気持ちを「インファー（推し量る）」できるのが、大人の知性です。"),
    ("surmise", "Surmise", "推測する、推測", "15th Century", "surmise (an accusation)", "Suppose something is true without evidence", "確たる証拠が何もない荒野の中に、直感と経験だけを頼りに真実の城を「打ち立てる」勇敢な（あるいは無謀な）仮説。", "「サーマイズ（憶測）」だけで他人を裁くのは、自らの器の小ささを示す行為です。"),
    ("conjecture", "Conjecture", "推測、憶測", "14th Century", "conjectura (a conclusion)", "Form an opinion on incomplete information", "バラバラのピースを「共に投げ集め」、全体としてどう見えるかを強引にまとめ上げる、粗削りだが力強い思考実験。", "いくら「コンジェクチャー（あてずっぽうの推量）」を重ねても、一歩踏み出す行動には敵いません。"),
    ("speculate", "Speculate", "推測する、投機する", "16th Century", "speculari (to spy out, examine)", "Form a theory without firm evidence", "高い塔の上（見張り台）から遠くを見渡し、これから起こり得る未来の地形を予測・賭けようとする野心的な観察。", "不確かな未来を心配して「スペキュレイト（思い巡らす）」するより、今の幸せを味わって。"),
    ("reckon", "Reckon", "計算する、推測する", "Old English", "gerecenian (to explain, recount)", "Consider or think", "直感と理性を両立させ、自分の中の「計算書」と照らし合わせて最終的な判断を下す、地に足の着いた判断。", "私は彼が絶対にやり遂げると「レコン（信じて見なす）」しています。"),
    ("evaluate", "Evaluate", "評価する", "19th Century", "evaluer (to find the value of)", "Form an idea of the amount, number, or value of", "対象が内包している「真の価値」を、私情を挟まずに客観的な秤（はかり）にかけて引き出すこと。", "自分の才能を低く「エヴァリュエイト（評価）」せず、もっと誇りを持って堂々と生きましょう。"),
    ("appraise", "Appraise", "鑑定する、評価する", "16th Century", "apprisen (to set a value on)", "Assess the value or quality of", "美術品や宝石の価値を見定めるように、対象の稀少性や真贋を専門的な眼差しで的確に見極める高い知性。", "あなたという存在の価値は、誰かに「アプレイズ（査定）」される筋合いのものではありません。"),
    ("assess", "Assess", "評価する、査定する", "15th Century", "assessare (to fix a tax upon)", "Evaluate or estimate the nature, ability, or quality of", "対象の隣に「座り込んで」、その性質や影響力を時間をかけてじっくりと感じ取り、正確に見積もること。", "自分に何ができるかを冷静に「アセス（見積もる）」できれば、不要な失敗は避けられます。"),
    ("discern", "Discern", "見分ける、識別する", "14th Century", "discernere (to separate, set apart)", "Perceive or recognize", "複雑に絡み合った混沌の中から、物事の本質や真実を「より分けて」見出す、研ぎ澄まされた魂の視力。", "表面的な優しさと本当の愛を「ディサーン（識別する）」するのは、人生における最高の技術です。"),
    ("comprehend", "Comprehend", "理解する、包容する", "14th Century", "comprehendere (to catch, grasp)", "Grasp mentally; understand", "断片的な知識を全て「共に掴み取り」、一つの巨大な全体（パノラマ）として完全に飲み込む圧倒的な理解力。", "壮大な宇宙の神秘をすべて「コンプリヘンド（完全に理解）」することは、誰にもできません。"),
    ("intellect", "Intellect", "知性、理力", "14th Century", "intellectus (understanding)", "The faculty of reasoning and understanding objectively", "感情の濁りに邪魔されず、物事の行間を「読み取り」、そこにある真理を白日の下に晒す（さらす）絶対的な光。", "「インテレクト（知能）」が高いことと、人を愛せるかどうかは全くの別問題です。"),
    ("intuition", "Intuition", "直感", "15th Century", "intueri (to look at, consider)", "The ability to understand immediately", "論理による証明や段階的な思考を一切すっ飛ばし、真実を「内側から見抜いて」しまう、魂の神業。", "迷ったときは、最初の「イントゥイション（直感）」に従うのが一番後悔しない選択です。"),
    ("instinct", "Instinct", "本能", "15th Century", "instingere (to incite, impel)", "Innate, typically fixed pattern of behavior", "遺伝子の奥深くに刻み込まれた、生命を維持・繁栄させるために「内側から突き動かしてくる」野性の衝動。", "人間社会のルールに縛られすぎると、「インスティンクト（本能）」の叫びが聞こえなくなります。"),
    ("insight", "Insight", "洞察力、見識", "12th Century", "in- + sight (seeing into)", "Capacity to gain an accurate and deep intuitive understanding", "表面的な現象の壁を透過し、事物の本質や隠された原因の「内側を真っ直ぐに視る」心眼の深さ。", "彼のアドバイスには、物事の確信を突く素晴らしい「インサイト（洞察力）」があります。"),
    ("hindsight", "Hindsight", "後知恵、あとになっての判断", "19th Century", "hind + sight", "Understanding of a situation or event only after it has happened", "すべての結果が出揃った後から「後ろを振り返って」初めて見える、遅すぎて時に残酷な真実の視界。", "「ハインドサイト（後知恵）」で過去の自分を責めるのは不公平です。あの時は最善を尽くしたのだから。"),
    ("foresight", "Foresight", "先見の明", "14th Century", "fore + sight", "Ability to predict what will happen or be needed in the future", "まだ見ぬ未来の出来事を、現在から「前方に視線を投げて」正確に予測し、備えを整える賢者の視力。", "「フォーサイト（先見性）」のあるリーダーは、嵐が来る前に静かに船の補強を終えています。"),
    ("premise", "Premise", "前提", "14th Century", "praemittere (to send before)", "A previous statement from which another is inferred", "すべての論理的な推論を組み上げるために、一番「前に送られて（置かれて）」いる揺るぎない基礎となる約束事。", "「愛されている」という「プレミス（前提）」が崩れると、どんな優しい言葉も嘘に聞こえてしまいます。"),
    ("hypothesis", "Hypothesis", "仮説", "16th Century", "hupotithenai (to place under)", "A supposition or proposed explanation", "証明されていない未知の現象を説明するために、土台の「下に置かれた」一時的で大胆な想像の足場。", "不可能を可能にするのは、クレイジーな「ハイポセシス（仮説）」を信じて検証し続ける情熱です。"),
    ("empirical", "Empirical", "経験的な、実証的な", "16th Century", "empeirikos (experienced)", "Based on observation or experience", "机上の空論を鼻で笑い、自らの「経験」と「五感」で実際に確かめられたことだけを真実と認める泥臭いリアリズム。", "「エンピリカル（経験に基づく）」な知恵は、どれほど美しい理論よりも、人生の荒波では役に立ちます。"),
    ("rational", "Rational", "理にかなった、理性的な", "14th Century", "rationalis (of or belonging to reason)", "Based on or in accordance with reason or logic", "感情の暴走を許さず、すべての行動や判断を「計算可能な比率」や論理によってコントロールしようとする冷徹な美しさ。", "恋に落ちた人間に「ラショナル（理性的）」に振る舞えと要求するのは、火に冷たくなれと言うのと同じです。"),
    ("irrational", "Irrational", "不合理な、理性を失った", "15th Century", "irrationalis (without reason)", "Not logical or reasonable", "論理や計算を打ち破って噴出する、理解不能で混沌としているからこそ圧倒的なエネルギーを持つ生命の叫び。", "人間は「イラショナル（理屈に合わない）」な行動をするからこそ、ロボットより愛おしいのです。"),
    ("sane", "Sane", "正気な、まともな", "17th Century", "sanus (healthy)", "Of sound mind; not mad or mentally ill", "極端な狂気や幻想に陥らず、現実社会と「健康」な関係を保ち続けることができるバランスの取れた精神状態。", "この狂った世界で「セイン（まとも）」であり続けるためには、時には適度に狂ってみせる柔軟さも必要です。"),
    ("insane", "Insane", "狂気の、常軌を逸した", "16th Century", "insanus (unhealthy, mad)", "In a state of mind which prevents normal perception, behavior", "現実の鎖を完全に断ち切り、「健康」という常識概念を超越して果てしない妄想や狂熱の宇宙へと旅立ってしまった魂。", "天才と呼ばれる人たちの発想は、ほとんどの場合、凡人から見れば「インセイン（狂っている）」ものです。"),
    ("naive", "Naive", "世間知らずの、無邪気な", "17th Century", "nativus (native, natural)", "Showing a lack of experience, wisdom, or judgment", "社会の悪意や複雑さにまだ染まっていない、生まれつきの「自然のまま」の無防備で透き通った美しさと脆さ。", "「ナイーブ（純真で無防備）」な心を持っている人は傷つきやすいですが、世界を一番美しく見ることができます。"),
    ("gullible", "Gullible", "だまされやすい", "19th Century", "gull (to cheat)", "Easily persuaded to believe something", "相手（あるいは鳥のヒナ）のように、喉に見せられたものを何の疑いもなく丸ごと飲み込んでしまう、悲しいほどの素直さ。", "「ガリブル（騙されやすい）」なのは愚かだからではなく、他者を信じたいという優しい願いの現れです。"),
    ("skeptical", "Skeptical", "懐疑的な", "17th Century", "skeptikos (inquiring, reflecting)", "Not easily convinced; having doubts", "安易に信じることを拒否し、自ら深く「探求し、観察する」ことでのみ真実に到達しようとする厳しい知性の姿勢。", "新しい情報には常に「スケプティカル（懐疑的）」にかまえることで、騙されるリスクを最小限に抑えられます。"),
    ("cynical", "Cynical", "皮肉な、冷笑的な", "16th Century", "kynikos (dog-like, churlish)", "Believing that people are motivated by self-interest", "人間の善意や理想を一切信じず、すべては利己的な欲望で動いているとする「犬のように」冷たく荒んだ見方。", "「シニカル（ねじくれた冷笑的）」な態度を取り続けていると、本当に美しい愛が目の前に現れても気づけません。"),
    ("pragmatic", "Pragmatic", "実用的な、現実的な", "17th Century", "pragmatikos (fit for action)", "Dealing with things sensibly and realistically", "実現不可能な理想を語るよりも、「行動や実務」を通して目の前の問題をどう解決するかを最優先する地に足のついた知性。", "夢を語るのも大事ですが、それを実現するためには「プラグマティック（超現実的）」な計画が不可欠です。"),
    ("shrewd", "Shrewd", "抜け目のない、鋭い", "14th Century", "shrewe (evil person, scolding woman)", "Having or showing sharp powers of judgment", "かつては「悪意のある」とされたほど、状況や人間の弱点を鋭く見抜き、自らの利益のために完璧に状況を操る鋭敏さ。", "ビジネスの世界を生き抜くには、時には「シュルード（抜け目がなく鋭い）」な判断力を持たなければなりません。"),
    ("astute", "Astute", "機敏な、抜け目のない", "17th Century", "astutus (clever, cunning)", "Having an ability to accurately assess situations", "都市の狡猾さを生き抜く力。周囲の微細な変化を誰よりも早く察知し、自分に最も有利な一手を一瞬で導き出す洗練された感覚。", "彼女の「アスチュート（本質を見抜いて素早い）」な洞察力のおかげで、チームは重大な危機を回避できました。"),
    ("ignorant", "Ignorant", "無知な、知らない", "14th Century", "ignorare (not to know)", "Lacking knowledge or awareness", "真実が「分からない、知らない」状態。しかしそれは罪ではなく、これから無限に学び成長できる余白があるという可能性の裏返し。", "「イグノラント（物を知らない状態）」であることを恥じる必要はありません。知らないふりをする方がよほど愚かです。"),
    ("oblivious", "Oblivious", "忘れている、気付かない", "15th Century", "oblivisci (to forget)", "Not aware of or not concerned about what is happening", "目の前で起こっていることや重要な事実に対して、完全に「忘れ去って」しまったかのように意識のシャッターを下ろしている無頓着さ。", "彼は他人の感情に対していつも「オブリビアス（全く無頓着）」で、気づかずに相手を傷つけてしまいます。")
]

words = []
for item in words_data:
    root1 = item[4].split(" ")[0]
    meaning1 = " ".join(item[4].split(" ")[1:]).strip("()")
    w = {
        "id": f"{item[0]}_mind",
        "word": item[0],
        "meaning": item[2],
        "era": item[3],
        "etymology": {
            "components": [item[4]],
            "original_statement": f"From {item[3]} {item[4]}."
        },
        "concept": item[5] + f" ({item[6]})",
        "thinking": item[6],
        "aftertaste": item[7],
        "example": f"It is important to {item[0]} deeply on this matter.",
        "deep_dive": {
            "roots": [{"term": root1, "meaning": meaning1}],
            "points": ["私たちが世界を認識し、理解するための心のフィルターの数々。"]
        },
        "part_of_speech": "verb" if item[0] in ["ponder","contemplate","muse","meditate","ruminate","deliberate","deduce","infer","surmise","conjecture","speculate","reckon","evaluate","appraise","assess","discern","comprehend"] else "adjective" if item[0] in ["empirical","rational","irrational","sane","insane","naive","gullible","skeptical","cynical","pragmatic","shrewd","astute","ignorant","oblivious"] else "noun"
    }
    words.append(w)

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
if match:
    prefix, json_array_str, suffix = match.groups()
    existing_words = json.loads(json_array_str)
    existing_ids = {w.get("id") for w in existing_words}
    existing_word_texts = set(w.get("word").lower() for w in existing_words)
    
    added = 0
    for w in words:
        if w["id"] not in existing_ids and w["word"].lower() not in existing_word_texts:
            existing_words.append(w)
            added += 1
            existing_word_texts.add(w["word"].lower())
            
    new_content = content[:match.start()] + prefix + json.dumps(existing_words, ensure_ascii=False, indent='\t') + suffix + content[match.end():]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Success: Added {added} words. Theme: Mind & Intelligence (Cycle 5).")
else:
    print("Error parsing data.js")
