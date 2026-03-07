import json
import re

# Theme: The Alchemy of Cooking & Taste (Cycle 21)
words_data = [
    ("saute", "Saute", "ソテーする、さっと炒める", "19th Century", "sauter (to jump)", "Fry quickly in a little hot fat", "熱いフライパンの上で食材を「躍らせる（ジャンプさせる）」ように、短時間で一気に火を通し、旨みを閉じ込める躍動感あふれる調理。", "悩み事も「ソテー（さっと炒める）」するように素早く片付けて、アツアツのうちに次の行動へ移りましょう。"),
    ("simmer", "Simmer", "とろとろ煮込む", "17th Century", "simeren (to simmer)", "Keep (food) just below boiling point", "沸騰の寸前で熱を抑え、時間をかけて食材の芯まで味を「沁み込ませる（煮込む）」、静かで深い対話のようなプロセス。", "焦って答えを出そうとせず、今はただ自分の想いを「シマー（じっくり煮込む）」させておく時期なのです。"),
    ("sear", "Sear", "表面を焼き固める", "Old English", "searian (to wither, dry up)", "Burn or scorch the surface of (something) with a sudden, intense heat", "強火で一気に表面を焦がし、内部の瑞々しい水分を逃がさないように「封印する」という、強引で情熱的な熱の洗礼。", "第一印象で相手の心を「セア（焼き固める）」するような、強烈で魅力的な言葉を一つ用意しておきましょう。"),
    ("poach", "Poach", "（卵などを）落とし煮にする、密猟する", "14th Century", "pochier (to enclose in a pocket)", "Cook (an egg) without its shell in or over gently boiling water", "沸騰させない優しいお湯の中で、中身を壊さぬよう「袋（ポケット）状に」優しく包み込んで火を通す、繊細を極めた愛の調理。", "傷つきやすい誰かの心は、熱すぎる議論よりも「ポーチ（優しく包み込む）」した言葉で温めてあげて。"),
    ("blanch", "Blanch", "（野菜などを）さっとゆでる、青ざめる", "14th Century", "blanc (white)", "Make white or pale by extracting color", "熱湯に潜らせた直後に氷水で締めることで、色を明るく「白く（鮮やかに）」保ち、雑味を抜いて本質を引き出す儀式。", "厳しい現実という熱湯をくぐり抜けた後にこそ、あなたの個性は「ブランチ（鮮やかな発色）」として輝き出すのです。"),
    ("braise", "Braise", "蒸し煮にする", "18th Century", "braise (live coals)", "Fry (food) lightly and then stew it slowly in a closed container", "焼いてから蓋をして、炭火の熱を閉じ込めてゆっくりと「蒸らし煮る」ことで、どんなに硬い素材もとろけるように和らげる魔法。", "頑固なあの人の心も、時間をかけた「ブレイズ（じっくり蒸し煮）」のような共感で、きっと柔らかく解けるはず。"),
    ("roast", "Roast", "ローストする、焼く", "13th Century", "rostir (to roast)", "Cook (food, especially meat) by prolonged exposure to heat in an oven or over a fire", "火の力を直接、あるいは熱風の抱擁として長時間浴びせ続け、素材の香ばしさを極限まで引き出し「香りを高める」王道の調理。", "自分を厳しく「ロースト（鍛錬）」した日々があるからこそ、今のあなたには深い味わいと自信が宿っているのです。"),
    ("glaze", "Glaze", "（料理に）つやを出す、ガラスをはめる", "14th Century", "glas (glass)", "Overlay or cover (food, fabric, etc.) with a smooth, shiny coating", "料理の表面に甘い蜜の「ガラスのような（光沢のある）」膜を張り、視覚的な美しさと多層的な味を一度に与える仕上げの魔法。", "事実に少しの「グレーズ（つや出し）」としてのユーモアを加えれば、退屈な日常も一気に輝き始めます。"),
    ("whisk", "Whisk", "泡立て器で混ぜる、さっと払う", "14th Century", "wisk (brushwood for sweeping)", "Beat or stir (a substance, especially cream or eggs) with a light, rapid movement", "空気という目に見えないスパイスを、高速の回転によって液体の中へと「巻き込み」、ふわふわとした夢のような食感を生み出す魔術。", "停滞した場の空気を、あなたの明るいアイデアで「ウィスク（かき混ぜる）」して、新しいエナジーを吹き込んで。"),
    ("infuse", "Infuse", "（茶などを）出す、吹き込む", "15th Century", "infundere (to pour in)", "Soak (tea, herbs, etc.) in liquid to extract the flavor or healing properties", "温かい液体の中に自らの「エキスを静かに注ぎ込み」、全体を自分の色と香りで満たしていく、境界を越えた浸透の対話。", "良質な本や音楽は、あなたの魂に新しい視点を「インフューズ（吹き込む）」し、人生の風味を豊かにしてくれます。"),
    ("zest", "Zest", "（柑橘類の）皮、熱意", "17th Century", "zeste (orange or lemon peel)", "Great enthusiasm and energy", "果実の表面に隠された「最高の香りと刺激」を削り出し、日常という料理に鮮烈な驚きと、生きる喜びというスパイスを加えること。", "何気ない散歩にも「ゼスト（熱意と風味）」を持って取り組めば、道端の花さえも特別な贈り物に変わります。"),
    ("garnish", "Garnish", "添え物をする、飾る", "14th Century", "garnir (to provide, equip, adorn)", "Decorate or embellish (something, especially food)", "料理の味を決定づけるものではないが、それを「整え守る」という心遣いによって、完成度を一つ上の次元へと高める最後の彩り。", "清潔な靴を一足「ガーニッシュ（彩りとしての仕上げ）」として選ぶだけで、あなたの自信は劇的に向上するでしょう。"),
    ("seasoning", "Seasoning", "調味料、味付け", "15th Century", "season (to ripen, season)", "Salt, herbs, or spices added to food to enhance its flavor", "時が経つ（シーズン）ことで円熟味を増すように、素材の隠れた魅力を「適切に引き出し補う」ためのバランスの調整。", "苦い経験も、後から振り返れば人生を深く味わうための最良の「シーズニング（調味料）」だったと気づくはず。"),
    ("savory", "Savory", "風味の良い、塩気のあるおいしい", "13th Century", "savour (flavor, taste)", "Belonging to the category that is salty or spicy rather than sweet", "ただ甘いだけではない、スパイスや塩、そして素材の旨みが複雑に絡み合った「深い満足感」を与える、大人のための豊かな風味。", "甘いお世辞よりも、時には「セイヴォリー（味わい深く、ピリッとした）」な直言の方が、私たちを成長させてくれます。"),
    ("pungent", "Pungent", "（鼻を突くように）刺激的な、辛辣な", "16th Century", "pungere (to prick)", "Having a sharply strong taste or smell", "針で「突き刺す（プッシュする）」ような強烈な香りが五感を一瞬で覚醒させ、記憶の底に鋭い刻印を刻み込むような挑戦的な刺激。", "彼の「パンジェント（鼻を突くほど鋭い）」な批評は、眠っていた私の知性を力強く突き動かしました。"),
    ("tart", "Tart", "酸っぱい、鋭い", "14th Century", "teart (sharp, severe)", "Sharp or acid in taste", "舌先を「キュッと（鋭く）」締め付けるような爽やかな酸味が、鈍った味覚をリフレッシュさせ、次の展開へと誘う刺激的な予感。", "「タート（ピリッと酸っぱい）」な一言が、ダラダラと続いた長い沈黙を鮮やかに切り裂きました。"),
    ("robust", "Robust", "力強い、たくましい", "16th Century", "robustus (as strong as oak)", "Strong and healthy; vigorous", "オークの木のように「どっしりと（たくましく）」構えた、揺るぎない芯の強さと、口いっぱいに広がる濃厚で力強いエナジーの塊。", "「ロバスト（力強く豊かな）」なコーヒーの香りは、今日という戦いの日のための最高の前奏曲です。"),
    ("succulent", "Succulent", "汁気の多い、瑞々しい", "17th Century", "succus (juice, sap)", "Tender, juicy, and tasty", "噛む（かみしめる）たびに、閉じ込められていた「溢れんばかりの生命の雫（しずく）」がほとばしる、五感を満たす究極の豊穣。", "「サキュレント（瑞々しい）」なライチを口に含めば、灼熱の太陽さえも心地よい祝福に変容します。"),
    ("tender", "Tender", "柔らかい、優しい", "13th Century", "tener (soft, delicate)", "Easy to cut or chew; not tough", "長時間の忍耐や愛情によって、鋭い角が完全に取れ、触れるだけで「心まで溶けてしまいそうな」ほど心地よい柔らかさと慈しみ。", "人の「テンダー（柔らかく傷つきやすい）」な部分を大切に扱える人こそが、真の強者なのです。"),
    ("crisp", "Crisp", "カリッとした、さわやかな", "Old English", "crisp (curled, wavy)", "Firm, dry, and brittle, especially in a way that is pleasant", "指先や歯で触れた瞬間に「小気味よく（ハッキリと）」砕け散り、清々しいリズムと音を周囲に響かせる、淀みのない切れ味。", "「クリスプ（パリッとした）」な朝の空気の中で、新しい真っ白なシャツに袖を通す瞬間の喜び。"),
    ("flaky", "Flaky", "薄切りにした、層状に剥がれる", "16th Century", "flake (fragment, layer)", "Breaking or separating easily into small thin pieces", "極薄の層が幾重にも重なり合い、触れただけで「はかなく崩れて（剥がれて）」いく、繊細な手仕事の積み重ねが生んだ芸術的食感。", "「フレイキー（幾層にも重なり、サクッと崩れる）」なパイ生地のように、人生も多くの地層の上に成り立っているのです。"),
    ("velvety", "Velvety", "ベルベットのような、滑らかな", "16th Century", "velvet (shaggy, silky)", "Having a smooth, soft appearance, feel, or taste", "一切の摩擦を感じさせず、舌の上を「優雅に（シルクのように）」流れていく、極上の心地よさと気品に満ちた滑らかさ。", "「ヴェルヴェッティ（ビロードのようになめらかな）」な赤ワインを一口飲めば、今夜の孤独も上質な時間へと変わります。"),
    ("creamy", "Creamy", "クリーミーな、滑らかな", "16th Century", "cream (chrism, oily substance)", "Resembling or containing cream", "全ての対立を一箇所に溶かし込み、全体を「優しく（濃厚に）」均質に包み込む、まろやかで安心感に満ちた抱擁の食感。", "「クリーミー（真っ白で濃厚な）」なスープは、冷え切った心の一番奥まで優しく温めてくれます。"),
    ("crunchy", "Crunchy", "バリバリとした、歯ごたえのある", "19th Century", "crunch (to crush with the teeth)", "Making a sharp noise when bitten or crushed", "噛み砕くプロセスそのものが「力強いリズム」となり、生命の活力を直接脳へと伝える、健康的で野性的な喜びの響き。", "「クランチー（カリカリと小気味よい）」なグラノーラとともに始める朝は、冒険の始まりの合図です。"),
    ("mellow", "Mellow", "芳醇な、円熟した", "14th Century", "mel (honey)", "Pleasantly smooth or soft; free from harshness", "蜂蜜（ハニー）のように「甘く（穏やかに）」、時間の経過によってトゲが完璧に削ぎ落とされた、心地よい落ち着きと深み。", "「メロウ（芳醇で角がない）」な性格の持ち主は、そこにいるだけで周囲の空気を穏やかに変えてしまいます。"),
    ("tangy", "Tangy", "ピリッとする、刺激的な", "19th Century", "tang (sharp taste, force)", "Having a strong, piquant flavor or smell", "一瞬だけ舌を「鋭く（ピリリと）」刺激し、直後に爽やかな余韻を広げて五感を呼び覚ます、躍動感のある酸味と香りの合わせ技。", "「タンギー（ツンと爽やか）」なレモンドレッシングがあれば、どんなに元気のない野菜も最高のご馳走に。"),
    ("zippy", "Zippy", "ピリッとした、元気の良い", "19th Century", "zip (sharp sound or movement)", "Bright, fresh, or lively", "ジッパーを引くような「素早さと（弾けるような）」エネルギーに満ち、鈍った思考を瞬時に活性化させる、軽快で刺激的な風味。", "「ジッピー（エネルギッシュでピリッとした）」な新しいアイデアで、退屈なミーティングを吹き飛ばしましょう！"),
    ("aromatic", "Aromatic", "芳香のある、香りの良い", "14th Century", "aroma (spice, fragrant herb)", "Having a pleasant and distinctive smell", "目に見える美しさ以上に、空気中に「魔法（香りの粒子）」を振り撒いて、人々の本能と記憶を優雅に揺さぶる不可視の魅力。", "「アロマティック（香りが豊かな）」なハーブティーを飲みながら、自分だけの空想の庭を歩いてみませんか。"),
    ("piquant", "Piquant", "ピリッと辛い、食欲をそそる", "16th Century", "piquer (to prick, sting)", "Having a pleasantly sharp taste or appetizing flavor", "「チクリと（心地よく）」五感を刺激し、もっともっとその先を知りたいと思わせる、知的好奇心と食欲を同時に刺激する魅力の花火。", "「ピカント（食欲をそそるほど鋭い）」なウィットに富んだジョークが、二人の間に新しい火を灯しました。"),
    ("earthy", "Earthy", "土の香りがする、素朴な", "16th Century", "earth (ground, soil)", "Resembling or suggestive of earth or soil", "装飾を一切削ぎ落とし、大地の「本源的な力と（力強い）」湿り気を直接感じさせる、誠実で嘘のない命の重み。", "「アーシー（大地を感じる）」な香りのマッシュルームを食べると、自分も地球の一部であることを思い出します。"),
    ("nutty", "Nutty", "ナッツのような、香ばしい", "19th Century", "nut (fruit of certain trees)", "Having the flavor of nuts", "時間をかけてじっくり煎られたナッツのように、独特の「香ばしさと（深いコク）」を少しずつ解放する、知れば知るほど癖になる味わい。", "「ナッティー（香ばしくて深い）」なコクのあるチーズを味わいながら、今日一日の自分を褒めてあげてください。"),
    ("smoky", "Smoky", "煙の立ち上る、スモーキーな", "14th Century", "smoke (smoky vapor)", "Like smoke in flavor, smell, or appearance", "火の遠い記憶を「煙というベール」に包んで保存し、野生の記憶を呼び覚ましながらも文明の洗練を感じさせる、ミステリアスな深み。", "「スモーキー（移り香のような）」なウイスキーの香りは、忘れていた遠い日の約束をふっと思い出させます。"),
    ("bitter", "Bitter", "苦い、辛辣な", "Old English", "biter (biting, sharp, painful)", "Having a sharp, pungent taste or smell; not sweet", "「噛む（刺入する）」ような痛みから始まり、やがてそれは知性を研ぎ澄ませる高貴な大人だけの哲学的な余韻へと変わる。", "「ビター（ほろ苦い）」な結末だったからこそ、この物語は私たちの心に永遠に消えない傷跡と深い価値を残しました。"),
    ("astringent", "Astringent", "渋い、厳格な", "14th Century", "astringere (to bind fast)", "Causing the contraction of skin cells and other body tissues", "表面を「キュッと（固く引き締める）」ような厳しさによって、緩んだ心を再び正し、凛とした緊張感を与えるストイックな刺激。", "「アストリンゼント（肌や心を引き締める）」な冷たい水で顔を洗えば、迷いも一瞬でどこかへ吹き飛びます。"),
    ("cloying", "Cloying", "鼻につく、しつこい甘さの", "14th Century", "cloy (to stop up, fasten)", "Excessively sweet, rich, or sentimental, especially to a sickening degree", "最初は甘く心地よいが、度を越した過剰さによって出口を「塞ぎ（詰まらせ）」、呼吸を困難にするほど不快で重苦しい執着。", "「クロイング（鼻につくほど甘すぎる）」な甘言に惑わされず、自分自身のクリアな視点を常に保っておきましょう。"),
    ("delectable", "Delectable", "おいしい、喜ばしい", "14th Century", "delectare (to delight)", "Delicious", "ただ「喜び（ディライト）」そのものを形にしたような、全身を幸福感で満たしてくれる、非の打ち所のない調和と悦びの結晶。", "「ディレクタブル（この上なく美味しい）」なデザートを一口食べれば、世界はまだ愛に溢れていると確信できます。"),
    ("scrumptious", "Scrumptious", "（口語）とてもおいしい、すてきな", "19th Century", "scrumpt (skimpy, small) - ironic usage", "Extremely tasty; delicious", "思わず「一口、また一口と（夢中になって）」手が出てしまう、理屈抜きの圧倒的な美味しさと、それを共有する人々の笑顔。", "「スクランプシャス（ほっぺが落ちそうなほど美味しい）」な手作りパイを囲んで、家族の会話に花が咲きました。"),
    ("refreshing", "Refreshing", "爽やかな、元気づける", "16th Century", "re- (again) + fresh (new, vigorous)", "Serving to refresh or reinvigorate someone", "使い古された自分を一度脱ぎ捨て、「再び（フレッシュに）」新しい命を吹き込まれたような、清涼感あふれる再起動の感覚。", "「リフレッシング（生き返るような）」なミントの香りが、午後からの重い気分を鮮やかに一掃してくれます。"),
    ("wholesome", "Wholesome", "健康に良い、健全な", "12th Century", "hal (whole, healthy)", "Conducive to or suggestive of good health and physical well-being", "心、体、そして魂の「全体（ホール）」を健やかに保ち、一切の不純物を含まない太陽の光のような明るさと誠実な滋養。", "「ホールサム（心身に滋養を与える）」な食事と誠実な友情こそが、自分を健やかに保つための最強の特効薬です。"),
    ("organic", "Organic", "有機の、組織的な、本質的な", "16th Century", "organon (instrument)", "Relating to or derived from living matter", "人為的な操作ではなく、生命の「器官が（あるがままに）」自然なリズムで結びつき、成長していくプロセスそのものを尊重する美学。", "「オーガニック（本質的に繋がった）」な成長は時間がかかりますが、その分だけ強靭で揺るぎない根を張るのです。"),
    ("artisanal", "Artisanal", "職人の、伝統的な手法の", "19th Century", "artigiano (artisan)", "Relating to or characteristic of an artisan", "大量生産の匿名性ではなく、一人の「職人の（手触りと魂が）」すべての細部に宿った、世界に一つだけの誠実な物語と誇り。", "「アルティザナル（職人の手仕事による）」なパンを一噛みするたび、作り手の誠実な想いが伝わってきます。"),
    ("gourmet", "Gourmet", "美食家、洗練された料理", "19th Century", "grommes (groom, servant) - related to wine tasters", "A connoisseur of good food; a person with a discerning palate", "ただ食べて満たされることを越え、一皿の中に広がる「微細な（宇宙のような）」差異と調和を読み解こうとする、知的な冒険者。", "時には「グルメ（美食家）」として、一皿の料理に隠された歴史を想像しながら、ゆっくりと時を味わいましょう。"),
    ("palate", "Palate", "上顎、味覚、審美眼", "14th Century", "palatum (palate)", "A person's appreciation of taste and flavor, especially when sophisticated and discriminating", "自分の中に持っている「最高の（美学としての）」フィルター。何を受け入れ、何を拒むかを決定する魂の門番。", "洗練された「パレート（味覚・審美眼）」を磨き続けることで、あなたの人生はより色鮮やかな傑作へと変わります。"),
    ("epicure", "Epicure", "美食家、快楽主義者", "16th Century", "Epicurus (Greek philosopher)", "A person who takes particular pleasure in fine food and drink", "古代の哲学者エピクロスが唱えた「苦しみのない平静な心の平安（快楽）」を、日々の食事という芸術の中に見出そうとする探求者。", "「エピキュア（生活を愉しむ達人）」として生きるとは、自分にとっての本当の豊かさを勇敢に選び取ることなのです。")
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
            word_id = f"{word_text.lower()}_cook"
            
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
                    "example": f"The chef began to {word_text} the ingredients with careful attention.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0], "meaning": " ".join(item[4].split(" ")[1:]).strip("()")}],
                        "points": ["料理のアクションや味覚の表現は、文化の成熟度と人生の味わい深さを映し出します。"]
                    },
                    "part_of_speech": "verb" if item[0] in ["saute", "simmer", "sear", "poach", "blanch", "braise", "roast", "glaze", "whisk", "infuse", "zest", "garnish", "incinerate", "ignite", "kindle", "extinguish", "forge", "smelt", "alloy", "temper", "weld", "solder", "rivet", "grind", "weave", "spin", "knit", "stitch", "sew", "unravel", "embroider"] else "adjective" if item[0] in ["savory", "pungent", "tart", "robust", "succulent", "tender", "crisp", "flaky", "velvety", "creamy", "crunchy", "mellow", "tangy", "zippy", "aromatic", "piquant", "earthy", "nutty", "smoky", "bitter", "astringent", "cloying", "delectable", "scrumptious", "refreshing", "wholesome", "organic", "artisanal"] else "noun"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Cooking & Taste (Cycle 21).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
