import json
import re

# Theme: The Whispers of Health & Vitality (Cycle 24)
words_data = [
    ("stamina", "Stamina", "スタミナ、精力、根気", "18th Century", "stamen (threads of the warp)", "The ability to sustain prolonged physical or mental effort", "運命の女神が紡ぐ経糸（スタメン）のように、途切れることなく続いていく「生命の力強い継続」。", "明日の成功という名の布を織り上げるためには、今日という日の「スタミナ（根気強い糸）」を一本ずつ丁寧に紡（つむ）いでいくしかありません。"),
    ("vigor", "Vigor", "活力、精気", "14th Century", "vigere (to be lively / be strong)", "Physical strength and good health", "内側からあふれ出す、抑えきれない「生き生きとした力」。世界を自分の手で変えようとする、若々しいエナジーの爆発。", "「ヴィガー（溢れる活力）」に満ちたあなたの笑顔は、周囲の沈んだ空気をも一瞬で塗り替えてしまう、魔法の光線（レイ）なのです。"),
    ("agility", "Agility", "敏捷性、機敏さ", "15th Century", "agere (to do, act, drive)", "Ability to move quickly and easily", "思考と行動の間に一切の澱（よど）みがなく、猫のように「しなやかに、素早く」環境の変化に対応しようとする生存の知恵。", "この不確実な時代の荒波を乗り越えるために必要なのは、重い鎧ではなく、自分自身を軽やかに変容させる「アジリティ（機敏さ）」なのです。"),
    ("flexibility", "Flexibility", "柔軟性、しなやかさ", "17th Century", "flectere (to bend)", "The quality of bending easily without breaking", "折れることなく、風のままに「自らを曲げる（ベンド）」ことで、強大な圧力さえも受け流し、再び立ち上がるための強靭なしなやかさ。", "「フレキシビリティ（柔軟な思考）」を持つことで初めて、あなたは自分とは全く異なる価値観を持つ他者と、真に理解し合うことができるのです。"),
    ("equilibrium", "Equilibrium", "平衡、均衡", "17th Century", "aequus (equal) + libra (balance, scales)", "A state in which opposing forces or influences are balanced", "相反する二つの力が「天秤（リブラ）のように」等しく釣り合い、完全な静寂と安定を保っている、心身の理想的な調和状態。", "心の「エクイリブリアム（中庸のバランス）」を保つことは、嵐の海を安全に航行するための、不動のセンターパネルを確立することに等しいのです。"),
    ("metabolism", "Metabolism", "代謝、新陳代謝", "19th Century", "metabolismos (change)", "The chemical processes that occur within a living organism in order to maintain life", "古い自分を勇気を持って壊し、新しい自分へと「変化（チェンジ）」させ続けることで、命の輝きを絶え間なく更新していく生命の根源的なリズム。", "社会という有機体にも「メタボリズム（新陳代謝）」が必要。古いルールを手放し、新しい感性を受け入れることで、街は再び活気を取り戻します。"),
    ("digestion", "Digestion", "消化", "14th Century", "di- (apart) + gerere (to carry)", "The process of breaking down food in the stomach into substances that the body can use", "受け取った情報をバラバラに分解し（ディバイド）、自分の栄養となる本質だけを「運び込み（キャリー）」蓄積していく、知的な吸収のプロセス。", "難解な哲学書を一読して分かったつもりにならず、自分の人生という胃袋で、じっくりと「ダイジェスチョン（消化）」して、自分の血肉にしてください。"),
    ("circulation", "Circulation", "循環、流通、血行", "15th Century", "circulare (to form a circle, go around)", "The movement of blood through the vessels of the body", "心臓という中心から送り出されたエナジーが、隅々までを「巡り（サークル）」、再び中心へと回帰していく、永遠に滞ることのない命の連鎖。", "お金も愛情も、握りしめて独占するのではなく、社会の中に「サーキュレーション（循環）」させることで、初めて真の豊かさとなってあなたに還ってきます。"),
    ("immunity", "Immunity", "免疫、免除", "14th Century", "im- (not) + munia (duties, tasks)", "The ability of an organism to resist a particular infection or toxin", "外部からの不当な支配や攻撃に対し、「義務（負担）を免除される」という形での絶対的な自己防衛。自らの純粋性を守り抜くための、内面的な聖域。", "批判というウイルスに負けない「イミュニティ（心の免疫）」を持つ秘訣は、自分自身の価値を、他者の承認なしに100％信じることなのです。"),
    ("vaccine", "Vaccine", "ワクチン", "18th Century", "vacca (cow)", "A substance used to stimulate the production of antibodies", "毒をもって毒を制す。微量の痛みを受け入れることで、将来の「巨大な崩壊から身を守る」ための、先制的な防衛の叡智。", "読書という「ワクチン（精神の予防接種）」を若いうちに受けておけば、いずれ遭遇する人生の荒波さえも、あなたは余裕を持って乗り越えられるでしょう。"),
    ("therapy", "Therapy", "療法、セラピー", "19th Century", "therapeia (curing, waiting on, service)", "Treatment intended to relieve or heal a disorder", "傷ついた誰かのそばに寄り添い、ただ「仕える（サービス）」ようにして回復を助け、本来の自分へと戻るための静かなる治癒の伴走。", "「セラピー（癒しの時間）」とは、特別な薬ではなく、ただ誰かに自分の話を遮られずに（しゃべられずに）聴いてもらうことで始まる奇跡なのです。"),
    ("remedy", "Remedy", "治療（法）、救済（策）", "13th Century", "re- (again) + mederi (to heal)", "A medicine or treatment for a disease or injury", "不均衡に陥った現在の状態を、再び「本来の正常な姿へと癒し直す（リ・メディケート）」ための、具体的で効果的な解決の処方箋（テ。"),
    ("prescription", "Prescription", "処方箋、規定", "16th Century", "pre- (before) + scribere (to write)", "An instruction written by a medical practitioner", "事態が悪化する「前に（プレ）」あらかじめ書き記された（スクライブ）、正しい方向へと導くための指針と地図。", "他人の人生の「プレスクリプション（規定の生き方）」に従う必要はありません。自分だけの幸せのレシピを、自分の手で書き記（かきしる）してください。"),
    ("dosage", "Dosage", "服用量、適量", "19th Century", "dosis (giving)", "A size or frequency of a dose of medicine", "多すぎれば毒になり、少なすぎれば無意味になる、神が定めた絶妙な「与え方（ディスペンシング）」のバランス。", "成功という甘美な薬の「ドセージ（適量）」を間違えると、あなたは傲慢（ごうまん）という名の不治の病に侵されてしまうかもしれません。"),
    ("symptom", "Symptom", "症状、兆候", "14th Century", "sun- (together) + piptein (to fall)", "A physical or mental feature which is regarded as indicating a condition of disease", "内なる不協和音の破片が「共に（シン）」崩れ落ちる（フォール）ように、目に見える形で表面にあらわれた、魂からの切実なSOS。", "小さな「シンプトム（兆候）」を見逃さないで。それは、本当のあなたが「今の生き方を変えてほしい」と、叫んでいる声なのです。"),
    ("diagnosis", "Diagnosis", "診断", "17th Century", "dia- (apart, through) + gignoskein (to know)", "The identification of the nature of an illness", "表面的な現象を「透過して（スルー）」その本質を見極める（ノウ）知性。曖昧な苦しみに名前を与え、克服の対象として確定させること。", "自分の欠点という悩みに正しい「ダイアグノーシス（診断）」を下せれば、それはもはや恥ずべきことではなく、磨くべき『個性』へと変わります。"),
    ("prognosis", "Prognosis", "予後、見通し", "17th Century", "pro- (before) + gignoskein (to know)", "The likely course of a disease or ailment", "過去のデータと現在の状態から、これから起こるであろう未来を「あらかじめ（プレ）知る（ノウ）」という、希望と覚悟の予言。", "どれほど厳しい「プログノーシス（今後の見通し）」を聞かされても、未来の1ページ目を描くペンは、常にあなたの手の中にあります。"),
    ("hygiene", "Hygiene", "衛生", "16th Century", "Hygieia (Greek goddess of health)", "Conditions or practices conducive to maintaining health and preventing disease", "汚れを物理的に払うだけでなく、心身の「清浄さ（ホーリー）」を保つことで、神々から祝福されるような健やかな人生の基盤。"),
    ("sanitation", "Sanitation", "公衆衛生", "19th Century", "sanitas (health)", "Conditions relating to public health", "個人の健康を越えて、社会全体が「健全（サニティー）」でいられるような循環（めぐり）を整え、誰もが安心して暮らせる土壌を整備すること。"),
    ("holistic", "Holistic", "全体論的な、ホリスティックな", "20th Century", "holos (whole)", "Characterized by the belief that the parts of something are intimately interconnected", "一部の不具合を単独で見るのではなく、心、体、魂、そして環境を一つの「大きな繋がり（ホール）」として捉え、本質的な調和を求める智慧。", "「ホリスティック（全体を見据えた）」な視点で自分を愛してあげてください。一つのミスであなたの誇り（全人格）が傷つくことなど、あり得ないのです。"),
    ("wellness", "Wellness", "ウェルネス、健康であること", "17th Century", "well + -ness", "The state of being in good health", "ただ病気でないという消極的な状態ではなく、心も体も満たされて、自らの可能性を最大限に引き出せているという「最高に良い（ウェル）」感触。", "「ウェルネス（心身の輝き）」を追求することは、自分という楽器を毎日丁寧にチューニングし、人生という名曲を最高の音色で奏でる準備をすることです。"),
    ("longevity", "Longevity", "長寿、寿命", "17th Century", "longus (long) + aevum (age)", "Long life", "時間の荒野をどこまでも「長く（ロング）」歩き続け、多くの季節と叡智をその身に刻み込んだ、命という名のマラソンランナーの栄光。", "「ロンジェビティ（長い人生）」の意味は、単に長く生きることにあるのではなく、どれほど深く人を愛し、どれほど多くの知恵を後世に遺せたかにあります。"),
    ("nourishing", "Nourishing", "滋養のある、育む", "14th Century", "nutrire (to feed, cherish)", "Providing the substances picked up from food that are necessary for growth", "ただお腹を膨らませる（ふくらませる）だけでなく、その人の「芯となる部分」にまで染み渡り、成長と癒しを力強くサポートする深い愛情と栄養。", "あなたの温かい「ナリッシング（魂を育む）」な言葉の一つ一つが、自信を失った彼の心の中で、新しい勇気の種を育てています。"),
    ("stimulating", "Stimulating", "刺激的な、元気づける", "16th Century", "stimulus (goad, incentive)", "Encouraging or arousing interest or enthusiasm", "眠っていた五感や好奇心を「鋭い針（スティムルス）」で突くように呼び覚まし、心地よい興奮とともに新しい世界へと送り出してくれる活気。", "「スティミュレイティング（知的な刺激を受けた）」な会話のあとは、今までの自分では思いつかなかったような、眩いばかりの未来の地図（マップ）が見えてきます。"),
    ("soothing", "Soothing", "なだめるような、心地よい", "Old English", "sothian (to confirm, satisfy)", "Having a gently calming effect", "ささくれ立った神経や傷口に優しく触れ、そこが「真実（ソス）の安らぎ」であると確信させてくれる、母親の抱擁のような絶対的な鎮静。", "雨の降る音は、騒がしい都会で疲れきった私たちの脳を優しく「スージング（癒して）」し、再び静かな自分を取り戻させてくれます。"),
    ("sedative", "Sedative", "鎮静剤、落ち着かせる", "15th Century", "sedatus (calmed, quieted)", "Promoting calm or inducing sleep", "荒れ狂う感情の波を「座らせ（セダレート）」、静かな水平線へと変えることで、心地よい眠りと安息の淵へと導く、夜の魔法。", "あまりに深く傷ついた時は、無理に明るく振る舞わず、哀しい音楽という名の「セダティヴ（鎮静薬）」に身を任せる時間も必要です。"),
    ("vigorous", "Vigorous", "精力的な、力強い", "14th Century", "vigere (to be lively)", "Strong, healthy, and full of energy", "自分の信念に向かって、一切のためらいなく「力強く（ヴィガーを持って）」突き進む、生命の躍動感あふれるエネルギッシュな姿。", "「ヴィゴラス（若々しく精力的な）」なあなたの挑戦し続ける姿勢は、それ自体が周囲の若者たちにとっての、最高の「生きる教科書」になるはずです。"),
    ("frail", "Frail", "脆い、弱々しい", "14th Century", "frangere (to break)", "Weak and delicate", "触れればすぐに「壊れて（フレイク）」しまいそうなほど儚げだが、だからこそ守り抜きたいと願わせる、繊細で高貴な命の危うさ。", "「フレイル（脆く弱った）」な古い建物の柱を支えるように、困っている他者の肩にそっと手を添えられる、そんな優しい人でありたい。"),
    ("fatigue", "Fatigue", "疲労、疲れ", "17th Century", "fatigare (to tire out)", "Extreme tiredness", "蓄えられたエナジーが「限界（ファティ）まで」放出され、一時的に世界との関わりを遮断して、純粋な休息を求める生命の防衛本能。", "「ファティーグ（心身の疲弊）」は、あなたが一生懸命に生きて、誰かのために力を尽くしたという、誇り高い戦いの勲章（メダル）なのです。"),
    ("exhaustion", "Exhaustion", "消耗、疲労困憊", "17th Century", "ex- (out) + haurire (to draw water)", "A state of extreme physical or mental fatigue", "井戸の水を「一滴残らず汲み出して（アウト）」しまったかのように、ゼロになった状態で横たわる、静かなる再充填（リチャージ）の前触れ。", "「エグゾースチョン（心身の枯渇）」の果てに見る夢は、普段は隠されているあなたの本当の願いを、優しく映し出してくれる鏡になります。"),
    ("recovery", "Recovery", "回復、取り戻す", "14th Century", "re- (again) + cuperare (to get, catch)", "A return to a normal state of health, mind, or strength", "一度手放してしまった健康や誇りを、時間の海から「再び（リ）手に入（カヴァー）れる」プロセス。傷跡が智慧（ちえ）へと変わる再生の軌跡。", "「リカバリー（復活への旅路）」の途中で立ち止まってもいい。あなたは一歩進むたびに、以前よりも強くてしなやかな自分に近づいているのですから。"),
    ("healing", "Healing", "治癒、癒やし", "Old English", "hælan (to make whole)", "The process of making or becoming sound or healthy again", "欠けてしまった心や体の破片を再び繋ぎ合わせ、元の「完全な（ホール）」状態へと戻していく、生命に本来備わった魔法の修復力。", "他人を「ヒーリング（癒やす）」力を持とうとするなら、まずは自分自身の内なる傷口を、慈愛の目で見つめ直すことから始めてください。"),
    ("convalescence", "Convalescence", "回復期、静養", "15th Century", "con- (with) + valescare (to grow strong)", "Time spent recovering from an illness or medical treatment", "病と戦うフェーズを終え、徐々に自分の中の強さが「戻り（ヴァレス）」、新しい自分として再び立ち上がるための、静かで清浄な余白の時間。", "「コンヴァレッセンス（静かな回復の時）」に聴く鳥の声は、今まで気づけなかった世界の繊細な彩（いろどり）を教えてくれる、特別な音楽になります。"),
    ("restoration", "Restoration", "修復、復元", "14th Century", "restaurare (to repair)", "The action of returning something to a former owner, place, or condition", "時の荒波で風化した記憶や建物を、丁寧な手仕事によって「元の（レストア）輝き」へと戻し、歴史の重みを再び今へと呼び覚ます行為。", "古い家具の「リストレーション（修復）」を通じて、私たちはモノに宿る魂と、それを使い続けてきた人々の愛着という名の歴史を受け継ぐのです。"),
    ("rejuvenation", "Rejuvenation", "若返り、活力を取り戻す", "17th Century", "re- (again) + juvenis (young)", "The action or process of making someone or something look or feel better, younger, or more vital", "過去の栄光を懐かしむのではなく、今この瞬間に、心の中に「瑞々しい若さ（ジュヴナイル）」の種を再び（リ）呼び覚まし、新しい生命の帆を張ること。", "新しい学問に挑戦することは、脳にとって最高の「リジュベネーション（若返りの秘薬）」であり、あなたの瞳に永遠の知的好奇心を灯します。"),
    ("fitness", "Fitness", "健康、適合、フィットネス", "16th Century", "fit (suitable, proper)", "The condition of being physically fit and healthy", "自分の命という器が、この世界の要求に対して「完璧に適合（フィット）」し、淀みのない力を発揮できているという、力強い肯定感。", "「フィットネス（心身の適応力）」を磨くことは、自分の人生の操縦桿（グリップ）を、自分自身でしっかりと握り続けるための訓練そのものです。"),
    ("endurance", "Endurance", "忍耐、耐久力", "14th Century", "durare (to last)", "The fact or power of enduring an unpleasant or difficult process or situation without giving way", "どれほどの時が流れても、どれほどの苦痛が襲おうとも、その「持続（デュレーション）」という盾を捨てずに立ち続ける、魂の頑強な筋肉。", "「エンデュランス（持久力）」勝負の人生。一瞬の華やかな勝利よりも、最後までコースに残り続けたという事実こそが、あなたを真の強者（ヒーロー）にするのです。"),
    ("strength", "Strength", "強さ、力", "Old English", "strengthu (force, power, vigor)", "The quality or state of being physically strong", "重力や困難という圧力に「真っ直ぐに（ストレート）」対抗し、自分の意志で自分を支え、大切なものを守り抜くための、揺るぎない内なる基盤。", "真の「ストレングス（強さ）」とは、筋肉の太さではなく、絶望の中でどれだけ優しく笑えるか、という魂の柔軟性に宿っているのです。"),
    ("pulse", "Pulse", "脈拍、鼓動、パルス", "14th Century", "pulsus (beating)", "A rhythmical throbbing of the arteries", "あなたが生きてここにあることを、一定の「ビート（鼓動）」で絶え間なく世界へと打ち鳴らし続けている、生命の最も正直な信号。", "都会の「パルス（鼓動）」に疲れたなら、自分の静かな脈動（しゅくどう）に指を当ててみて。そこには宇宙と同じ、一環したリズムが流れています。"),
    ("breath", "Breath", "呼吸、息", "Old English", "bræth (scent, smell, loud sound)", "The air taken into or expelled from the lungs", "外の世界と自分を直結する「唯一の出入り口」。古い自分を吐き出し、宇宙の新鮮なエナジーを吸い込むことで、一瞬ごとに生まれ変わる聖なる行為。", "深い「ブレス（呼吸）」を一つするだけで、世界は一変します。酸素の一粒子一粒子が、あなたの細胞を優しく目覚めさせてくれるのを感じてください。"),
    ("heartbeat", "Heartbeat", "心拍、鼓動", "Old English", "heort (heart) + beatan (to beat)", "The pulsation of the heart", "生まれてから死ぬまで、一秒の休みもなく走り続ける「愛のエンジン」が奏でる、あなたという唯一無二の存在を讃（たた）える凱旋のドラム。", "誰かのために「ハートビート（胸の鼓動）」が早くなる。そんな瞬間があるだけで、この不自由な人生を生きる価値は十分にあると思いませんか。"),
    ("anatomy", "Anatomy", "解剖学、構造", "14th Century", "ana- (up) + temnein (to cut)", "The branch of science concerned with the bodily structure of humans, animals, and other living organisms", "生命という神秘のヴェールを「切り開き（カットアップ）」、その精緻で美しい調和の仕組みを一つずつ明らかにしようとする、知的な敬意の形。", "事件の「アナトミー（詳細な分析・解剖）」を試みることで、私たちは絡み合った偏見の中から、一つの冷徹な真実（エヴィデンス）を救い出すのです。"),
    ("skeleton", "Skeleton", "骨格、骸骨", "16th Century", "skeletos (dried up, withered)", "An object like a skeleton used as a memento mori", "全ての贅肉や虚飾が「削ぎ落とされ（乾燥し）」た後に残る、存在を最小限に支え続ける究極の合理と、死を越えた不変の形（かたち）。", "組織の「スケルトン（基本構造）」を簡素化することで、情報はもっとスムーズに、もっと力強く、末端（すみずみ）まで行き渡るようになります。"),
    ("muscle", "Muscle", "筋肉", "14th Century", "musculus (little mouse)", "A band or bundle of fibrous tissue", "皮膚の下で「小さなネズミ（マウス）」のように、しなやかに、力強く蠢（うごめ）き、あなたのイメージを行動へと変換する、意志の物理的装置。", "新しい知識を習得するのも「マッスル（脳の筋肉）」の訓練です。最初は辛くても、続ければ必ず、それはあなたの揺るぎない翼へと変わります。"),
    ("nerve", "Nerve", "神経、勇気、厚かましさ", "14th Century", "nervus (sinew, tendon)", "A whitish fiber or bundle of fibers that transmits impulses of sensation to the brain or spinal cord", "世界からの刺激を一瞬で「脳という中枢（コア）」へと運び、瞬時に反応を指令し、命の調和を保ち続ける、不可視の高速ネットワーク。", "「ナーヴ（勇気・度胸）」を持ってステージに立ってください。あなたの繊細な神経（ふるえ）は、そのまま観客の心と共鳴（シンクロ）する力になるのですから。")
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
            word_id = f"{word_text.lower()}_health"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "命の輝きは、日々の微細なケアから生まれます。",
                    "example": f"The focus on {word_text} has become increasingly important in modern life.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["健康とは、肉体と精神と宇宙が完璧なリズムで共鳴している状態を指します。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["nourishing", "stimulating", "soothing", "vigorous", "frail"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Health & Vitality (Cycle 24).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
