import json
import re

# Theme: The Threads of Knowledge & Skill (Cycle 25)
words_data = [
    ("expertise", "Expertise", "専門知識、熟練", "19th Century", "expertus (tried, tested, experienced)", "Expert skill or knowledge in a particular field", "幾多の実験（テスト）と失敗という荒野を「潜り抜け（エクスペリエンスト）」た者だけが身に纏える、確固たる知の鎧（よろい）。", "あなたの「エクスパティーズ（専門性）」は、誰にも真似できないあなただけの最強の武器。磨き続けることを決して忘れないでください。"),
    ("proficiency", "Proficiency", "熟達、堪能", "16th Century", "proficere (to make progress, go forward)", "A high degree of skill; competence or expertise", "ただ立ち止まっているのではなく、常に一段上を目指して「前へと進み続ける（プログレス）」ことで獲得される、洗練された技の練度。", "「プロフィシェンシー（熟達の域）」に達するまでには、地道な反復（リピート）という名の、黄金の忍耐が不可欠なのです。"),
    ("mastery", "Mastery", "習熟、支配、精通", "13th Century", "magister (master, teacher)", "Comprehensive knowledge or skill in a subject or accomplishment", "ある分野において他者に教えることができる最高位（マギステル）に立ち、自らの意志でその全てを「自在に操れる」ようになった完全なる調和。", "自分という楽器の「マスタリー（完璧な習得）」を成し遂げた時、人生のあらゆる不協和音は、美しい旋律（メロディ）へと昇華されるでしょう。"),
    ("dexterity", "Dexterity", "器用さ、機敏さ", "16th Century", "dexter (right-handed)", "Skill in performing tasks, especially with the hands", "迷いのない「右手の如き（デクスター）」正確さとスピードで、複雑なパズルを目にも止まらぬ速さで解き、新しい形を鮮やかに生み出す驚異の技術。", "職人の「デクスタリティ（卓越した器用さ）」は、指先にまで宿った彼の誇り高き魂が、物理的な世界を彫刻している姿なのです。"),
    ("ingenuity", "Ingenuity", "独創性、巧妙さ、器用さ", "16th Century", "ingenuus (native, natural, free-born)", "The quality of being clever, original, and inventive", "外部から与えられたものではなく、自らの内側から湧き出す「生まれ持った（ネイティブ）」自由な発想によって、誰もが諦めた困難を軽やかに突破する魔法のような智恵。", "資源が足りない時こそ、あなたの「インジェニュイティ（独創的な巧妙さ）」を輝かせる絶好のステージになるのです。"),
    ("creativity", "Creativity", "創造性、独創力", "19th Century", "creare (to bring forth, produce, build)", "The use of the imagination or original ideas", "無（ゼロ）の状態から、想像力という名のエネルギーを物質化し、新しい「意味のある命（クリエイト）」を世界というキャンバスに力強く産み落とす（アウト）神聖な行為。", "「クリエイティビティ（創造性）」は選ばれた天才だけの特権ではありません。昨日とは違う道を選ぼうとする、あなたの勇気の中にこそ宿っているのです。"),
    ("innovation", "Innovation", "革新、刷新", "16th Century", "in- (into) + novare (to make new)", "A new method, idea, or product", "既存の古い秩序の中に、全く「新しい（ノヴァ）」概念を大胆に差し込み、世界というシステム全体を劇的にアップデートしようとする勇気ある挑戦。", "「イノベーション（革新）」の成功は、他人の「無理だ」という言葉を聴いても、なお微笑み、自分の『新しさ』を信じ続けた者だけに微笑むのです。"),
    ("wisdom", "Wisdom", "知恵、賢明さ", "Old English", "wis (wise, prudent)", "The quality of having experience, knowledge, and good judgment", "単なる知識の蓄積を超え、時と状況の「本質を見極める（ワイズ）」審美眼を持ち、最善の道を選び取れる、長い人生の果てに獲得される魂の芳醇な香り。", "「ウィズダム（真の知恵）」を学ぶとは、答えを覚えることではなく、自分自身に「問い続ける」ことの重要さを悟ることなのです。"),
    ("sagacity", "Sagacity", "賢明、洞察力", "16th Century", "sagax (quick-witted, keen-scented)", "The quality of being sagacious; keen mental discernment and good judgment", "獲物の匂いを遠くから察知する猟犬のように、目に見えない「真実の香り（サガクス）」を瞬時に嗅ぎ分け、本質へと一直線に突き進む、鋭敏な精神の嗅覚。", "リーダーに求められるのは、データの分析力以上に、危機の中で一瞬の好機を嗅ぎ分ける「サガシティ（鋭い洞察力）」なのです。"),
    ("prudence", "Prudence", "慎重、思慮分別", "14th Century", "providentia (foresight, precaution)", "The quality of being prudent; cautiousness", "目先の誘惑に溺れず、遠い未来をあらかじめ「見通す（プロヴィデンス）」ことで、最もリスクの少ない、しかし最も確実な一歩を選び取る大人の賢明さ。", "「プルーデンス（賢明な慎重さ）」は臆病とは違います。真の勇者が目的地へ辿り着くために、最後まで決して手放さない盾（シールド）なのです。"),
    ("scholarship", "Scholarship", "学問、奨学金", "16th Century", "scholare (to school)", "Academic study or achievement; learning of a high level", "真理という名の巨大な山を、謙虚な姿勢で一段ずつ「登り続ける（スクール）」ことの積み重ね。特定の分野を極めんとするストイックな献身の証。", "「スカラシップ（学術的な追求）」という名の灯台の明かりが、この暗い時代を生きる私たちの、唯一の信頼できる道標になるのです。"),
    ("curriculum", "Curriculum", "教育課程、履修課程", "17th Century", "currere (to run)", "The subjects comprising a course of study in a school or college", "知の広野を目的地へと向かって「走り抜ける（カー）」ための、あらかじめ設計された道筋と地図。学びの全体像を俯瞰する設計図。", "人生という広大な「カリキュラム（履修課程）」には、無駄な単位など一つもありません。挫折も成功も、全てがあなたを完成させるための必須課題なのですから。"),
    ("lecture", "Lecture", "講義、講演", "14th Century", "lectus (reading)", "An educational talk to an audience, especially one of students in a university", "価値ある知恵を「読み上げ（リード）」、それを共有することで、他者の魂に新しい知識の種を蒔き、一斉に発芽させようとする情報のギフト。", "本を読み飛ばす（スキップ）だけでは、決して届かない深淵な知恵。優れた「レクチャー（講修）」は、あなたの脳のOSを根底から書き換えてくれるでしょう。"),
    ("seminar", "Seminar", "ゼミナール、演習", "19th Century", "seminarium (seedbed, nursery)", "A conference or other meeting for discussion or training", "互いの意見をぶつけ合うことで、未熟な知識を「苗床（セミナリウム）」で共に育て上げ、大きな収穫である結論へと導く知的な保育園（ナースリー）。", "少人数の「セミナー（演習）」に参加して、他人の異なる視点に触れること。それは、自分の世界の壁を押し広げる、最も効率的で刺激的な方法です。"),
    ("workshop", "Workshop", "作業場、ワークショップ", "Middle English", "work + shop", "A room or building in which goods are manufactured or repaired", "理論を語るだけでなく、自らの手で物理的に「作り上げる（ワーク）」ことで、身体知として技術を魂に刻み込む、動的な学びの聖域。", "心の中の「ワークショップ（精神の作業場）」で、毎日少しずつ自分の理想を彫刻してください。いつか必ず、目に見える形として結実するはずです。"),
    ("mentor", "Mentor", "メンター、指導者、助言者", "18th Century", "Mentor (character in Odyssey)", "An experienced and trusted adviser", "未知の航路で迷った時、自らの経験というコンパスを貸してくれ、あなたの「本質（メント）」を正しく見定め、成長へと導く太陽のような導師。", "優れた「メンター（心の師）」との出逢いは、あなたの人生を加速させます。彼らの成功よりも、彼らの『失敗への向き合い方』をこそ学ぶべきなのです。"),
    ("apprentice", "Apprentice", "見習い、徒弟", "13th Century", "apprendere (to learn, seize)", "A person who is learning a trade from a skilled employer", "巨匠の技を盗む（アプレヘンド）ために、その背中をじっと「捉え（セイズ）」、謙虚に、そして強欲にその知恵を自分のものにしようとする若き野心。", "一生「アプレンティス（学び続ける者）」であり続けること。それが、あなたが一生古びることなく、常に最前線で輝き続けるための唯一の絶対条件です。"),
    ("pedigree", "Pedigree", "家系、血統、経歴", "15th Century", "pied de grue (crane's foot - appearance of genealogical diagrams)", "The record of descent of an animal, showing it to be purebred", "連綿（れんめん）と続く先祖たちの足跡が、まるで「ツルの足跡（パイ・ド・グリュ）」のように複雑に、しかし美しく繋がってきた、純粋な命と知識の履歴書。", "あなたの「ペディグリー（血統・経歴）」とは、家柄のことではなく、あなたがこれまでどれほど真剣に、どれほど多くの壁を乗り越えてきたかという、その努力の集積を指すのです。"),
    ("lineage", "Lineage", "血統、系統", "14th Century", "linea (line)", "Linear descent from an ancestor; ancestry or pedigree", "過去から未来へと「一本の線（ライン）」のように、途切れることなく受け継がれてきた、生命と志のバトンリレーの軌道。", "自分たちの「リニエージ（系統）」を誇りに思うのは良いですが、そこに安住せず、あなた自身が新しい線の出発点（スタート）になる気概を持ってください。"),
    ("legacy", "Legacy", "遺産、継承物", "15th Century", "legatus (ambassador, envoy, person with a mission)", "An amount of money or property left to someone in a will", "自分がこの世を去った後も、誰かの心や社会の中に「使者（レガトゥス）」として、生き続けるために遺された、価値ある思考や愛の贈り物。", "「レガシー（遺産）」を築くとは、死後のことを心配することではなく、今、この瞬間、未来の誰かのために自分の命を「何に（なにに）使い果たすか」を決めることです。"),
    ("doctrine", "Doctrine", "教義、主義、ドクトリン", "14th Century", "doctrina (teaching, instruction)", "A belief or set of beliefs held and taught by a Church, political party, or other group", "ある集団が、自律的な「教え（ドクト）」として確立させ、揺るぎない世界の解釈として共有・防衛しようとする、論理の要塞（ようさい）。", "既存の「ドクトリン（教義）」を盲信するのではなく、常にそれを疑い、自分の実感を伴った『個のドクトリン』を構築していくことが、真の教養なのです。"),
    ("theory", "Theory", "理論、説", "16th Century", "theoria (contemplation, spectacle, looking at)", "A system of ideas intended to explain something", "バラバラの現象を一つにまとめ、客観的な「高みから見つめる（シア）」ことで、そこに普遍的な規則性を発見しようとする、知性の展望台。", "どれほど美しい「セオリー（理論）」であっても、一つひとつの具体例の重みを無視すれば、それは冷たい石像のように死んだ言葉に成り下がってしまいます。"),
    ("hypothesis", "Hypothesis", "仮説", "16th Century", "hupo- (under) + thesis (placing)", "A proposed explanation made on the basis of limited evidence", "真実という名の重厚な石垣の「下（ハイポ）に配置（テーゼ）」される、最初の頼りない、しかし最も自由な可能性への賭け（ベット）。", "「ハイポセシス（仮説）」を立てることを恐れないで。すべての偉大な科学は、「もしこれが真実だとしたら？」という、子どものような無邪気な一言から始まったのです。"),
    ("axiom", "Axiom", "自明の理、公理", "15th Century", "axios (worthy, fitting)", "A statement or proposition that is regarded as being established, accepted, or self-evidently true", "証明するまでもなく「ふさわしい（ワージー）」と誰もが認めざるを得ない、思考という建物を建てるための、絶対に動かない土台となる真実。", "あなたが自分自身を尊重（リスペクト）することは、人生を構築する上での「アクシオム（不可侵の公理）」であるべきです。ここからすべての論理は始まります。"),
    ("premise", "Premise", "前提、根拠", "14th Century", "pre- (before) + mittere (to send)", "A previous statement or proposition from which another is inferred or follows as a conclusion", "議論や行動を始める「前に（プレ）送り出される（ミス）」、全ての思考の出発点となる確信の種火。", "議論が平行線をたどる（。のなら、一度「プレミス（前提）」に立ち返ってみましょう。私たちは同じ場所からスタートしようとしていますか？"),
    ("conclusion", "Conclusion", "結論、結末", "14th Century", "con- (together) + claudere (to close)", "A judgment or decision reached by reasoning", "多くの分岐した可能性を「一つにまとめ、完全に閉じる（クローズ）」ことで、次のアクションのための明確なスタートラインへと変える、知性の収束。", "あなたが下した「コンクルージョン（結論）」を他人に説明する必要はありません。その結果としてあなたが歩み出す『最初の一歩』が、何よりも饒舌（じょうぜつ）に真実を語るからです。"),
    ("inference", "Inference", "推論、推測", "16th Century", "in- (into) + ferre (to carry)", "A conclusion reached on the basis of evidence and reasoning", "断片的な証拠という名の点と点を、想像力の糸で繋ぎ、未だ見ぬ真実の内容へと「持ち込む（フェリー）」知的な連想の魔法。", "事実は一つ。しかしそこから生まれる「インファレンス（推論）」は無限です。より優雅で、より人々に希望を与えるような推測を、あなたは選んでください。"),
    ("deduction", "Deduction", "控除、推論（演繹法）", "15th Century", "de- (down) + ducere (to lead)", "The inference of particular instances from a general law", "全体という高みにある真理から、個別の事例へと論理を正確に「引き下ろして（リード）」いくことで、必然という名の正解を導き出す知性の下降線。", "シャーロック・ホームズのように、鋭い「ディダクション（演繹的推論）」を駆使すれば、泥靴の汚れ一つからでも、一人の男の人生（ヒストリー）を読み解けるのです。"),
    ("induction", "Induction", "誘導、推論（帰納法）", "14th Century", "in- (into) + ducere (to lead)", "The inference of a general law from particular instances", "無数に散らばる小さな事実の断片から、それらを貫く一本の法則へと視点を「引き上げて（リード）誘い込む」ことで獲得される、新しい経験則の確立。", "「インダクション（帰納的推論）」を繰り返すことで、私たちは過去の偶然を、未来を生き抜くための確かな知恵（ナレッジ）へと変えていくことができるのです。"),
    ("dialectic", "Dialectic", "弁証法、対話術", "14th Century", "dia- (through, across) + legein (to speak)", "The art of investigating or discussing the truth of opinions", "正反対の意見がぶつかり合い、矛盾を通じて（ダイア）「語り合う（レゴ）」ことで、元の二つよりも遥かに高い次元の真実に到達しようとする、魂の進化の螺旋（らせん）。", "対立を恐れず、根気強い「ダイアレクティック（弁証法的対話）」を続けましょう。争いがある場所には、必ずそれを越えた新しい地平への入り口が隠されています。"),
    ("rhetoric", "Rhetoric", "修辞学、レトリック、雄弁術", "14th Century", "rhētor (speaker, orator)", "The art of effective or persuasive speaking or writing", "言葉をただの情報の運び手から、人々の魂を激しく揺さぶり、世界という現実を思い通りに塗り替えるための「強力な楽器（ウェポン）」へと磨き上げる術。", "美しすぎる「レトリック（修辞法）」は、時に真実から目を逸らさせ（そらせ）ますが、絶望した人を勇気付けるためには、この魔法ほどの強力な薬は存在しません。"),
    ("eloquent", "Eloquent", "雄弁な、説得力のある", "14th Century", "ex- (out) + loqui (to speak)", "Fluent or persuasive in speaking or writing", "心の内にある熱いマグマが、完璧に洗練された「言葉となって外へと溢れ出した（アウト）」、一切の淀みがない流麗で美しい意思表明。", "「エロクエント（雄弁な）」なあなたのプレゼンテーションの前に、疑いの壁は音を立てて崩れ落ち（。、聴衆は一斉に新しい未来の夢を見始めました。"),
    ("articulate", "Articulate", "（考えなどを）はっきりと述べる、歯切れの良い", "16th Century", "articulus (joint)", "Having or showing the ability to speak fluently and coherently", "節々（関節、ジョイント）を明確に定め、曖昧な感情を「一つひとつの言葉に、ハッキリと、正確に分解して」繋ぎ直す、知的な翻訳能力。", "自分の痛みを「アーティキュレート（明確な言葉にする）」できるようになれば、あなたはもはやその痛みの奴隷ではなく、それを克服する物語の主人公（ヒーロー）なのです。"),
    ("precise", "Precise", "正確な、厳密な", "16th Century", "prae- (before) + caedere (to cut)", "Marked by exactness and accuracy of expression or detail", "議論を始める「前に（プレ）、一切の余計なノイズを完璧に切り捨てる（カット）」ことで、真実だけを一点の曇りもなく抽出しようとする極限の純度。", "「プリサイズ（精密な）」な言葉遣いは、相手への最高の敬意です。曖昧さという甘えを捨て、一文字一文字に、あなた自身の魂の解像度（。を刻み込んでください。"),
    ("concise", "Concise", "簡潔な、簡明な", "16th Century", "con- (together) + caedere (to cut)", "Giving a lot of information clearly and in a few words; brief but comprehensive", "無駄な装飾や虚飾を「全て切り刻み（カット）、一つに凝縮する（トゥゲザー）」ことで、ダイヤモンドのような強固な密度と輝きを持った、短くも深い言葉の結晶。", "長い手紙よりも、たった三文字の「コンサイス（簡潔な）」な『ありがとう』が、冷え切った相手の心を一瞬で温めることも（。あるのです。"),
    ("profound", "Profound", "深い、深遠な", "14th Century", "pro- (before, forth) + fundus (bottom)", "Very great or intense", "表面のさざ波に惑わされず、その「遥か前（プレ）にある底（ファンド）」までを一気に貫き、暗黒の中にある真理の核を捉えようとする、知性のダイビング。", "「プロファウンド（深遠な）」な思索の果てに見出した答えは、流行の波に流されることなく、あなたの人生という航海の、揺るぎない錨（いかり）となるでしょう。"),
    ("erudite", "Erudite", "博学な、学識のある", "15th Century", "ex- (out) + rudis (rude, rough, unpolished)", "Having or showing great knowledge or learning", "荒削りで野蛮な（ルード）自分から、学びという研磨剤によって「脱け出し（アウト）」、歴史のあらゆる叡智を体細胞に刻み込んだ、知性の芳醇な香りを纏う者。", "「エルダイド（博学な）」な彼が語る歴史は、単なる過去の記録ではなく、今を生きる私たちのための、最高のサバイバル・ガイドのように聞こえる（。のです。"),
    ("versatile", "Versatile", "多才な、多目的に使える", "17th Century", "vertere (to turn)", "Able to adapt or be adapted to many different functions or activities", "一つの場所に留まらず、状況に合わせて「自在に（ヴァース・回転）」役割を変え、どんな環境下でも価値を発揮し続ける、しなやかで力強い多面性。", "一つの技能を究めるのも良いですが、これからの時代は「ヴァーサタイル（多角的な才能）」を育むことが、あなたの可能性を無限に広げる翼になるでしょう。"),
    ("adept", "Adept", "熟達した、名人", "17th Century", "adeptus (having attained, achieved)", "Very skilled or proficient at something", "過酷な修行の果てに、目指していた聖なる知恵を「獲得（アテイン）」し、完全に自分のものとして手足のように操れるようになった、至高の到達者。", "特定の分野の「アデプト（熟達者）」になることは、その分野を通じて、宇宙全体の調和と真理を理解する窓を手に入れることに他なりません。"),
    ("novice", "Novice", "初心者、修練者", "14th Century", "novus (new)", "A person new to and inexperienced in a job or situation", "偏見を持たず、全てを「新しく（ノヴァ）」見つめることができる、特権的な自由を持った出発者。無限の可能性を秘めた、未来の設計図そのもの。", "「ノーヴィス（初心者）」であることを恥じることはありません。その『分からない』という新鮮な感性こそが、停滞した業界を劇的に変える、台風（タイフーン）の目になるのですから。"),
    ("veteran", "Veteran", "ベテラン、退役軍人、経験豊富な", "16th Century", "vetus (old)", "A person who has had long experience in a particular field", "幾多の戦場と季節を駆け抜け、その体に「古い（ヴェトゥス）傷跡と叡智」を刻み込んだ、どんな嵐にも揺らぐことのない、都市の歴史そのものと呼べる存在。", "「ヴェテラン（百戦錬磨の勇者）」の言葉が重いのは、それが本の中の知識ではなく、彼が実際に流した汗と涙の結晶から紡ぎ出された（。からなのです。"),
    ("authority", "Authority", "権威、権力、当局", "13th Century", "auctor (author, originator, model)", "The power or right to give orders, make decisions, and enforce obedience", "他人の言葉の引用ではなく、自分自身が「最初の一行（著者・オーサー）」として人生を描き始め、その確固たる意志によって周囲に模範と正義を示すこと。", "本当の「オーソリティ（権威）」とは、地位や肩書きで人を従わせることではなく、あなたの存在そのものから滲み出る、圧倒的な誠実さ（インテグリティ）によって生み出されるものなのです。"),
    ("source", "Source", "源、情報源、ソース", "14th Century", "surgere (to rise, spring up)", "A place, person, or thing from which something comes or can be obtained", "大地から滾々と「湧き上がる（サージ）」泉のように、全ての知恵や力が最初に溢れ出した（。、最も純粋で、最も活力に満ちた原点の場所。"),
    ("reference", "Reference", "言及、参照、リファレンス", "16th Century", "re- (back) + ferre (to bring, carry)", "The action of mentioning or alluding to something", "目の前の小さな事象を、より巨大で偉大な歴史の物語へと「持ち帰り（バック・フェリー）」、その意味を広大な系譜の中に正しく配置し直すこと。"),
    ("database", "Database", "データベース", "20th Century", "data + base", "A structured set of data held in a computer", "バラバラの情報の断片を、計算可能な「基盤（ベース）」の上に整然と並べ、瞬時にアクセスして未来を予測するための、人類の共有される記憶の巨大な貯蔵庫。")
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
            word_id = f"{word_text.lower()}_skill"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "知の連鎖は、人類が未来へと繋ぐ最も強固な鎖です。",
                    "example": f"Her level of {word_text} impressed all the judges.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["知識は力であり、それを正しく使いこなす技能こそが、自由への翼です。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["eloquent", "articulate", "precise", "concise", "profound", "erudite", "versatile", "adept"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Knowledge & Skill (Cycle 25).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
