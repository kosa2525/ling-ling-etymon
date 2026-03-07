import json
import re
import uuid

words_data = [
    ("stroll", "Stroll", "散歩する、ぶらぶら歩く", "17th Century Germanic", "strollen (to roam, wander)", "Walking slowly", "「目的（goal）」を持たず、ただ「空間（space）」の豊かさを味わうために足を運ぶ贅沢な時間の使い方。", "生産性から離れ、「ストロール（散歩）」する時間こそが、心をリセットする最大の魔法です。"),
    ("gaze", "Gaze", "じっと見つめる、凝視する", "14th Century Scandinavian", "gapa (to gape, stare)", "Looking intently", "「対象（object）」の奥底にある「真実（truth）」を読み取ろうとする、静かで深い魂の交信。", "表面だけでなく、「ゲイズ（見つめる）」することで、相手の本当の姿が見えてきます。"),
    ("nod", "Nod", "うなずく、会釈する", "14th Century Middle English", "nodden (to bow the head)", "Bowing head slightly", "「相手（other）」の存在や言葉を「受容（accept）」し、肯定のサインを送る最小にして最強の仕草。", "言葉が出なくても、あなたの小さな「ノッド（うなずき）」が誰かの心を救います。"),
    ("sigh", "Sigh", "ため息をつく", "13th Century Old English", "sican (to sigh, yearn)", "Exhaling deeply", "「心（heart）」に溜まった「重圧（pressure）」を息と共に手放し、再び軽さを取り戻すための浄化。", "疲れたときは我慢せず、「サイ（ため息）」をついて心の換気をしましょう。"),
    ("shrug", "Shrug", "肩をすくめる", "15th Century Unknown", "shruggen (to draw up the shoulders)", "Raising shoulders", "「言葉（words）」では表現しきれない「曖昧さ（ambiguity）」や「無頓着（indifference）」を身体で示すこと。", "全てを理解できなくても、「シュラッグ（肩をすくめる）」して受け流す余裕を持ちましょう。"),
    ("grasp", "Grasp", "つかむ、理解する、把握する", "14th Century Old English", "græspan (to reach out, feel around)", "Holding tightly", "「物理的（physical）」に手で掴むことから転じ、「抽象的（abstract）」な概念を心でしっかりと捉えること。", "形のない思いも、しっかり「グラスプ（把握）」すれば確かな絆に変わります。"),
    ("toss", "Toss", "軽く投げる、放り投げる", "16th Century Unknown", "tossen (to throw, pitch)", "Throwing lightly", "「重さ（weight）」を感じさせず、「気軽（casual）」に何かを手放す、あるいは相手に委ねること。", "重く考えすぎず、時には「トス（軽く投げる）」するように運命に任せてみて。"),
    ("swap", "Swap", "交換する、取り替える", "14th Century Middle English", "swappen (to strike hands in agreement)", "Exchanging things", "「お互い（mutual）」の持ち物を交し合い、「新しい価値（new value）」を共有する平和的な取引。", "自分にないものを嘆くより、友人と「スワップ（交換）」して豊かさを分け合いましょう。"),
    ("peek", "Peek", "のぞき見する、ちらっと見える", "14th Century Middle English", "piken (to look quickly)", "Looking briefly", "「隠された（hidden）」ものに対する「好奇心（curiosity）」が、隙間からそっと顔を出す瞬間。", "ほんの少し「ピーク（のぞき見）」するだけで、日常に隠された魔法が見つかります。"),
    ("chat", "Chat", "おしゃべりする、雑談する", "15th Century Middle English", "chateren (to chatter)", "Talking informally", "「意味（meaning）」よりも「繋がっている（connecting）」こと自体を楽しむ、軽やかな言葉の交わし合い。", "特別な内容がなくても、毎日の「チャット（雑談）」が心の栄養になります。"),
    ("greet", "Greet", "挨拶する、歓迎する", "Old English", "gretan (to welcome, approach)", "Welcoming someone", "「他者（other）」の存在を認め、自分の領域に「平和的（peaceful）」に迎え入れる最初の儀式。", "「グリート（挨拶）」は、見知らぬ人との間に橋を架ける魔法の言葉です。"),
    ("wander", "Wander", "さまよう、歩き回る", "Old English", "wandrian (to move aimlessly)", "Moving without purpose", "「目的地（destination）」を持たず、「過程（process）」そのものを冒険として楽しむ自由な魂の動き。", "たまには道を外れて「ワンダー（さまよう）」することで、本当の自分に出会えるかもしれません。"),
    ("craft", "Craft", "手作りする、巧みに作る", "Old English", "cræft (strength, skill)", "Making with skill", "「素材（material）」に「技巧（skill）」と「魂（soul）」を注ぎ込み、新しい価値を創造すること。", "自分の人生も、丁寧に「クラフト（手作り）」していくことで美しい作品になります。"),
    ("drift", "Drift", "漂う、流される", "13th Century Old Norse", "drift (snowdrift, something driven)", "Floating aimlessly", "「流れ（flow）」に身を任せ、「抵抗（resistance）」することをやめて自然の引力に委ねる状態。", "無理に逆らわず、海のような運命に「ドリフト（漂う）」する勇気も必要です。"),
    ("skip", "Skip", "スキップする、軽く跳ぶ", "14th Century Old Norse", "skopa (to skip, run)", "Moving lightly", "「重力（gravity）」を一時的に忘れ、「喜悅（joy）」を全身の弾むような動きで表現すること。", "心が沈んだときは、子どもの頃のように「スキップ」して心を軽くしましょう。"),
    ("lean", "Lean", "もたれる、傾く", "Old English", "hleonian (to recline, lie down)", "Resting against", "「自立（independence）」の緊張を解き、信頼できる「支え（support）」に自らの重みを預けること。", "一人で立てないときは、誰かの肩に「リーン（もたれる）」してもいいのです。"),
    ("blend", "Blend", "混ぜる、溶け込む", "Old Norse", "blanda (to mix)", "Mixing together", "「異なる（different）」要素が互いの境界を無くし、「一つの調和（harmonic whole）」を創り出すこと。", "周囲と無理に合わせるのではなく、自分らしさを保ちながら「ブレンド（溶け込む）」しましょう。"),
    ("fade", "Fade", "色あせる、消えていく", "14th Century Old French", "fade (pale, weak)", "Disappearing slowly", "「存在（existence）」が徐々に薄れ、「記憶（memory）」の領域へと静かに移行していく美しい過程。", "痛みが「フェード（薄れる）」していくように、悲しみもやがて美しい記憶に変わります。"),
    ("glow", "Glow", "ボーッと光る、白熱する", "Old English", "glowan (to shine as if red-hot)", "Shining warmly", "「内側（inside）」から滲み出るような「温かい光（warm light）」が、周囲を優しく照らす状態。", "あなたの内なる「グロウ（輝き）」は、暗闇の中で誰かの道標になります。"),
    ("dip", "Dip", "ちょっと浸す、下がる", "Old English", "dyppan (to plunge)", "Entering slightly", "「未知（unknown）」の領域に、「少しだけ（a little bit）」触れて感触を確かめる慎重な行動。", "恐れずに、少しだけ足先を「ディップ（浸す）」して新しい世界を体験してみて。"),
    ("wipe", "Wipe", "拭く、ぬぐう", "Old English", "wipian (to cleanse, map)", "Cleaning surface", "「表面（surface）」の「汚れ（dirt）」を拭き取り、「純粋（pure）」な本来の姿を取り戻すこと。", "涙を「ワイプ（拭う）」した後は、きっと心もスッキリと晴れ渡るはずです。"),
    ("sweep", "Sweep", "掃く、一掃する", "Old English", "swapan (to sweep)", "Cleaning broad area", "「広範囲（broad area）」の障害や不要なものを、「一気（all at once）」に取り除き浄化すること。", "悩み事はほうきで「スイープ（一掃）」するように、頭の中から追い出しましょう。"),
    ("fold", "Fold", "折る、畳む", "Old English", "fealdan (to fold)", "Bending over", "「広がり（expansion）」を「コンパクト（compact）」にまとめ、内側に守り込むような行動。", "思いを丁寧に「フォールド（折り畳む）」して胸の奥にしまっておくのも一つの愛です。"),
    ("stack", "Stack", "積み重ねる", "13th Century Old Norse", "stakkr (haystack)", "Piling up", "「一つ一つ（one by one）」を「垂直（vertical）」に積み上げ、新しい構造を作り出すこと。", "小さな努力を毎日「スタック（積み重ね）」すれば、やがて大きな山になります。"),
    ("peel", "Peel", "皮をむく", "Old English", "pilian (to strictly peel, plunder)", "Removing outer layer", "「覆い（covering）」を取り除き、「核心（core）」にある真実の姿を露わに（あらわに）すること。", "心についた見栄の皮を「ピール（むく）」して、本当の自分を見つめ直しましょう。"),
    ("pour", "Pour", "注ぐ、流れ出る", "14th Century Unknown", "pouren (to empty out)", "Flowing heavily", "「容器（container）」から「中身（content）」を惜しみなく全て出し切る、豊かな流出。", "あなたの愛情を、渇いた心を持つ人へたっぷりと「ポア（注ぐ）」してあげて。"),
    ("spill", "Spill", "こぼす、あふれ出る", "Old English", "spillan (to destroy, waste)", "Flowing accidentally", "「制御（control）」を超えて、「予期せず（unexpectedly）」感情や物質が外へ溢れ出ること。", "我慢できずに「スピル（こぼれ落ちた）」涙は、心が生きている証拠です。"),
    ("stir", "Stir", "かき混ぜる、かすかに動く", "Old English", "styrian (to move, agitate)", "Mixing dynamically", "「停滞（stagnation）」した状態に「動き（motion）」を与え、新しい変化を促すこと。", "穏やかな毎日に少しの変化を「ステア（かき混ぜる）」することで、人生の味が深まります。"),
    ("chew", "Chew", "噛む、よく考える", "Old English", "ceowan (to bite, chew)", "Masticating", "「固い（hard）」ものを何度も「細かく（finely）」砕き、自分の血肉へと消化しやすくすること。", "難しい問題も、時間をかけて「チュー（よく噛んで/考えて）」すれば必ず消化できます。"),
    ("sip", "Sip", "ちびちび飲む", "14th Century Old English", "sypian (to drink in small quantities)", "Drinking slowly", "「一気（at once）」に飲み込まず、「少しずつ（little by little）」味わいながら取り入れること。", "人生の喜びは、極上のワインのように「シップ（ちびちび飲む）」してゆっくり味わうべきです。"),
    ("hum", "Hum", "鼻歌を歌う、ブンブンいう", "14th Century Imitative", "hummen (to make a murmuring sound)", "Singing without words", "「言葉（words）」を介さず、「純粋な旋律（pure melody）」だけで内なる平和を表現すること。", "心が静かなときは、自然と「ハム（鼻歌）」が出てくるような穏やかな時間を大切に。"),
    ("whisper", "Whisper", "ささやく、ひそひそ話す", "Old English", "hwisprian (to mutter)", "Speaking softly", "「大きな音（loud noise）」を避け、「親密（intimate）」な空間だけで秘密の想いを伝えること。", "本当に大切なことは、大声ではなく「ウィスパー（ささやき）」で伝える方が心に届きます。"),
    ("yell", "Yell", "叫ぶ、大声をあげる", "Old English", "giellan (to sound, shout)", "Shouting loudly", "「限界（limit）」を超えた感情が、抑えきれずに「声（voice）」となって爆発すること。", "どうしようもない怒りや哀しみは、誰もいない海に向かって「イェル（叫ぶ）」して解放しましょう。"),
    ("applaud", "Applaud", "拍手する、称賛する", "16th Century Latin", "applaudere (to clap the hands at)", "Clapping in approval", "「他者（other）」の努力や美しさに対し、「手（hands）」を打ち鳴らして敬意を表現すること。", "他人の成功を心から「アプロード（拍手称賛）」できる余裕こそが、本当の豊かさです。"),
    ("cheer", "Cheer", "応援する、励ます", "12th Century Anglo-French", "chere (face, expression)", "Encouraging loudly", "「顔（face）」を明るくし、声援を送ることで「相手（other）」に生命力を注入すること。", "落ち込んでいる友人を「チアー（応援）」することは、自分自身の心も明るく灯します。"),
    ("yawn", "Yawn", "あくびする", "Old English", "geonian (to open wide, gape)", "Opening mouth wide", "「退屈（boredom）」や「疲労（fatigue）」によって、体が無意識に空気を求める自然な反応。", "無理をせず、大きな「ヨーン（あくび）」が出たら、それは休息を求めるサインです。"),
    ("blink", "Blink", "まばたきする、点滅する", "13th Century Middle English", "blinken (to gleam, glance softly)", "Closing eyes briefly", "「一瞬（moment）」だけ境界を閉じ、再び目を開くことで「視界（vision）」を新しくリセットすること。", "「ブリンク（まばたき）」するその一瞬の間に、世界は思いがけない変化を遂げているかもしれません。"),
    ("stare", "Stare", "じっと見る、凝視する", "Old English", "starian (to look fixedly)", "Looking persistently", "「対象（object）」から目を離さず、「執念（obsession）」にも似た強さで見つめ続けること。", "過去の傷跡を「ステア（凝視）」しすぎるのはやめて、前を向く勇気を持ちましょう。"),
    ("glare", "Glare", "にらみつける、ギラギラ光る", "13th Century Middle English", "glaren (to shine fiercely)", "Looking angrily", "「怒り（anger）」や「敵意（hostility）」を込めて、刺すような視線で相手を射抜くこと。", "心を閉ざしたままの「グレア（睨み）」は、相手だけでなく自分自身の魂をもすり減らします。"),
    ("glance", "Glance", "ちらっと見る", "15th Century Old French", "glacier (to slip, slide)", "Looking quickly", "「視線（gaze）」を滑らせ、「わずかな時間（short time）」で対象の全体像を捉えること。", "ほんの「グランス（一瞥）」しただけで恋に落ちるような、直感の鋭さを信じてみて。"),
    ("frown", "Frown", "眉をひそめる、しかめっ面をする", "14th Century Old French", "froignier (to snort, scowl)", "Wrinkling brow", "「不満（dissatisfaction）」や「疑問（doubt）」が、顔の筋肉のわずかな緊張として表れること。", "「フラウン（しかめっ面）」が多い日は、空を見上げて顔の筋肉を緩めましょう。"),
    ("grin", "Grin", "にやっと笑う、歯を見せて笑う", "Old English", "grennian (to bare the teeth)", "Smiling broadly", "「抑えきれない喜び（uncontainable joy）」が、顔いっぱいに広がって歯を見せるほどの笑みになること。", "言葉が通じなくても、最高の「グリン（満面の笑み）」があれば心は通じ合います。"),
    ("chuckle", "Chuckle", "くすくす笑う", "16th Century Imitative", "chuckle (making sounds of quiet amusement)", "Laughing quietly", "「内側（inside）」で湧き上がる「おかしみ（amusement）」を、外に漏らさないよう静かに楽しむこと。", "人生の不条理には、怒るよりも「チャックル（くすくす笑い）」でやり過ごすのが賢明です。"),
    ("giggle", "Giggle", "クスクス笑う", "16th Century Imitative", "gigglen (making quick high-pitched laughs)", "Laughing excitedly", "「無邪気さ（innocence）」と「高揚感（excitement）」が混ざり合った、子どもみたいな純粋な笑い。", "大人になっても、友人と「ギグル（クスクス笑う）」できる時間はかけがえのない宝物です。"),
    ("weep", "Weep", "泣く、すすり泣く", "Old English", "wepan (to cry, bewail)", "Shedding tears", "「深い悲しみ（deep sorrow）」が水となって溢れ出し、魂の奥底を「浄化（purify）」すること。", "強がらなくていい。一人きりで「ウィープ（涙を流す）」夜が、明日を生きる強さを作ります。")
]

words = []
for item in words_data:
    root1 = item[4].split(" ")[0]
    meaning1 = " ".join(item[4].split(" ")[1:]).strip("()")
    w = {
        "id": f"{item[0]}_action",
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
        "example": f"He paused to {item[0]} for a moment.",
        "deep_dive": {
            "roots": [{"term": root1, "meaning": meaning1}],
            "points": ["日常の些細な動作に宿る人間の本質。"]
        },
        "part_of_speech": "verb" if "する" in item[2] or "く" in item[2] else "noun"
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
    print(f"Success: Added {added} words. Theme: Everyday Actions (Cycle 1).")
else:
    print("Error parsing data.js")
