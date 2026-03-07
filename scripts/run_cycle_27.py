import json
import re

# Theme: The Pulse of Law & Ethics (Cycle 27)
words_data = [
    ("justice", "Justice", "正義、裁判、公正", "12th Century", "justus (upright, equitable, right)", "Just behavior or treatment", "揺るぎない「正しさ（ジャスト）」に基づき、すべての存在をあるべき正しい位置へと戻そうとする、文明社会の究極の均衡点。", "たとえ世界中が暗闇に包まれても、心の中に「ジャスティス（不朽の正義）」という小さな火を灯し続けてください。"),
    ("equity", "Equity", "公平、公正、純資産", "14th Century", "aequus (even, level, equal)", "The quality of being fair and impartial", "単なる平等（イコール）を越え、個々の状況の違いを汲み取って「真（まこと）に平らな状態」へと調整しようとする、慈愛に満ちた正しさ。", "本当の「エクイティ（真の公平性）」とは、みんなに同じ靴を配ることではなく、みんなが（。歩きやすいように、一人ひとりの足に合った靴を用意してあげることなのです。"),
    ("statute", "Statute", "法令、定款", "14th Century", "statutum (something set up, decree)", "A written law passed by a legislative body", "社会の秩序を守るために「高く掲げられた（セットアップ）」、誰もが従うべき不変の掟（おきて）。言葉によって固定された（。、揺るぎない統治の石碑。", "法律という「スタチュート（成文法）」を暗記するよりも、なぜその法が生まれたのかという『人の心の叫び』に想いを馳せることこそが、真の学問なのです。"),
    ("decree", "Decree", "法令、布告", "14th Century", "decernere (to decide, determine, judge)", "An official order issued by a legal authority", "混乱した事態に終止符を打ち、進むべき方向をあらかじめ「決定（ディサイド）して」宣言される、神々や王の力強い意志の表明。", "運命という名の「ディクリー（非情な宣告）」が下されても、あなたの魂の自由までが（。奪われることは決してありません。"),
    ("mandate", "Mandate", "権限、委任、命令", "16th Century", "mandatum (something put into one's hand, commission)", "An official order or commission to do something", "人々の信頼という名のバトンを「手に託され（マンド）」、その重みを背負って公的な任務を遂行しようとする、高潔な責任の所在。", "選挙で得た「マンデート（民意の負託）」は、権力を行使するための道具ではなく、社会を（。より良く変えるための重い約束（プロミス）なのです。"),
    ("protocol", "Protocol", "外交儀礼、プロトコル、記録", "16th Century", "protokollon (first leaf glued into a manuscript)", "The official procedure or system of rules-governing affairs of state or diplomatic occasions", "混乱や誤解を避けるために、あらかじめ合意された「最初のページ（プロト）」に記（しる）された、対話と交流をスムーズにするための聖なる手順書。", "「プロトコル（儀礼）」とは、形式を重んじることではなく、相手への最大級（。の敬意を、誰にでも分かる『動作』として翻訳して伝えることなのです。"),
    ("sanction", "Sanction", "制裁、是認", "16th Century", "sancire (to confirm, make sacred)", "A threatened penalty for disobeying a law or rule", "不正や背信行為（。に対して、社会の「神聖なルール（セイクレッド）」を守るために敢然と行われる、厳格な処罰と意志の境界線。", "過酷（。な「サンクション（経済制裁）」のニュースを聴くたび、私たちは対話の難しさと、平和という脆い均衡の尊さを改めて（。痛感するのです。"),
    ("penalty", "Penalty", "刑罰、罰金、ペナルティ", "15th Century", "poena (punishment, pain)", "A punishment imposed for breaking a law, rule, or contract", "ルールを破った代償として支払わねばならない「痛み（ペイン）」を伴う教訓。二度と同じ過ちを繰り返さないように（。、自らと世界に刻むための反省の印。", "失敗への「ペナルティ（罰則）」を恐れて（。挑戦を止めてはなりません。真に恐れるべきなのは、一度も転ばずに、臆病なまま安全な場所に留まり続けることなのです。"),
    ("verdict", "Verdict", "（陪審の）評決、意見、断定", "15th Century", "vere (truly) + dictum (said)", "A decision on a disputed issue in a civil or criminal case", "多くの議論を尽くした果てに、ただ「真実（ヴェーレ）を語る（ディクト）」という勇気をもって下された、揺るぎない正義の最終判断。", "世間があなたにどんな「ヴァーディクト（一方的な判定）」を下そうとも、あなたの価値は（。、あなたのこれまでの誠実な生き方が証明している。今は胸を張っていてください。"),
    ("amnesty", "Amnesty", "恩赦、大赦", "16th Century", "amnestia (forgetting)", "An official pardon for people who have been convicted of political offenses", "過去の過ちをあえて「忘れ去る（アムネスティ）」ことで、新しい時代への歩みを共に始めようとする、文明社会の究極の寛容（。と許しの形式。", "自分自身に対する「アムネスティ（許しのアムネスティ）」を宣言（。してください。昨日の自分を許して初めて、あなたは今日、新しい自分として呼吸できる（。のですから。"),
    ("advocacy", "Advocacy", "擁護、弁護、アドボカシー", "14th Century", "ad- (to) + vocare (to call)", "Public support for or recommendation of a particular cause or policy", "声なき者の隣に寄り添い、彼らの想いを「呼び覚（わ）かし（ヴォーカル）」、社会全体に向かってその正当性を力強く主張しようとする、勇敢な代弁。", "誰かの権利を守るための「アドボカシー（擁護活動）」に、専門家（プロフェッショナル）である必要はありません。目の前の理不尽に『ノー』と言える（。、あなたのその正義感こそがすべての出発点なのです。"),
    ("counsel", "Counsel", "助言、相談、弁護人", "13th Century", "consilium (consultation, plan)", "Advice, especially that given formally", "一人で悩むのではなく、他者の知恵と「共に（コン）計画を練り（シリアン）」、最も賢明な出口を一緒に探し出そうとする、深い信頼に基づいた知的な伴走。", "「カウンセル（賢明な助言）」とは、相手に命令することではなく、相手が自分自身の内なる（。答えに自ら辿り着けるよう、暗闇の中でそっと足元を照らしてあげることなのです。"),
    ("tribunal", "Tribunal", "法廷、裁きの場", "16th Century", "tribunus (tribune, leader of a tribe)", "A court of justice or relevant body", "かつて一族の長（トライブ）が正義の名の下に人々の争いを裁いたように、文明社会の「最高度の知性」が終結し、真理を決定しようとする（。神聖な審判の場。", "心の中の「トライブュナル（良心の法廷）」で、毎日自分を見つめ直してください。他（。の誰を欺けても、自分自身の瞳（。は決して欺くことはできないのですから。"),
    ("jurisdiction", "Jurisdiction", "管轄（権）、司法権", "14th Century", "jus (law, right) + dicere (to say)", "The official power to make legal decisions and judgments", "法（。に基づき、正しさを「語る（ディクト）」ことが許された神聖な領域。秩序という網の目が、正しく（。、そして確実に機能し得る責任の限界点。", "あなたの「ジュリスディクション（力の及ぶ範囲）」の限界（ボーダー）を知ることは、自分にできること（フォーカス）に集中し、無駄な焦りから自分を解放する（。ための第一歩なのです。"),
    ("ordinance", "Ordinance", "条例、布告、儀式", "14th Century", "ordinare (to put in order, arrange)", "An authoritative order; a decree", "日々の生活というカオス（混沌）を、「整然とした（オーダー）」美しさの中へと導くために定められた、地域や魂の微細な調整ルール。", "街の小さな「オーディナンス（条例）」の一つひとつに、そこに住む（。人々の安全を願う、何世代にもわたる切実な祈りが込められている（。ことに、ふと気づく時があります。"),
    ("breach", "Breach", "（法・義務などの）違反、不義、侵害", "14th Century", "brecan (to break)", "An act of breaking or failing to observe a law, agreement, or code of conduct", "約束という名の美しい橋を「叩（たた）き壊し（ブレイク）」、信頼という名の防壁に穴を開けてしまった、悲しくも取り返しのつかない裏切りの痕跡。", "一度の「ブリーチ（信頼の破綻）」を修復するには、壊す時（。の何百倍もの時間と、誠実な積み重ねが必要になるのです。失う前に（。、その重みを想い返せますか？"),
    ("tort", "Tort", "不法行為", "13th Century", "torquere (to twist, wring)", "A wrongful act or an infringement of a right", "真っ直ぐであるべき「正義の道を（。ツイスト）ねじ曲げ」て、他者に不当な苦しみを与えてしまった、理不尽で歪んだ（ゆがんだ）行為の総称。", "法律用語の「トート（不法行為）」という言葉の響きには、ねじ曲げられた（。人の心の痛みと、それを元に戻そうとする正義の執念が（。、同時に込められているのです。"),
    ("felony", "Felony", "重罪", "13th Century", "felen (evil, wicked, treacherous)", "A crime, typically one involving violence", "人々の信頼を完膚なき（。までに「裏切り（フェロン）」、社会の調和を根底から揺るがしてしまった、取り返しのつかない大きな悪業の刻印。", "犯した罪は「フェロニー（重罪）」として記録されますが、その後のあなたの（。歩みが、いつかその汚れを拭い去れるほど、光に満ちたものに（。なることを、私は密かに願わずにはいられません。"),
    ("misdemeanor", "Misdemeanor", "軽罪、不作法", "15th Century", "mis- (badly) + de- (from) + mener (to lead)", "A minor wrongdoing", "悪意というよりは、つい道を見失い、「好ましくない（ミス）振る舞い（ミーナー）」へと導かれてしまった、人間としての弱さと甘さのあらわれ。", "人生の「ミスデミーナー（些細な過ち）」を数え上げて自分を責めるのをやめてください。失敗は、あなたがまだ『より良い生き方』を知るための教材（レッスン（。にすぎないのです。"),
    ("litigation", "Litigation", "訴訟", "16th Century", "lis (dispute, lawsuit) + agere (to drive, incite)", "The process of taking legal action", "言葉の剣（。をもって、争い（。を情報の戦場へと「駆り立て（アジテート）」、どちらが真理に近いかを公の場で証明しようとする、知的な戦い。", "「リティゲーション（訴訟）」による解決は最後の手段です。互いに同じテーブルに座り、まだ（。心が通い合ううちに解決できる道（アヴェニュー）がないか、もう（。一度だけ探ってみませんか。"),
    ("witness", "Witness", "目撃者、証人、証言する", "Old English", "witt (knowledge, wit)", "A person who sees an event, typically a crime or accident, take place", "自らの「知性（ウィット・知）」をもって真実を捉え、自分の目が捉えた（。ありのままの光景を、社会の正義のために勇気を持って語り出す者。", "あなたは自分自身の人生の最高の「ウィットネス（真実の目撃者）」です。他（。の誰があなたの価値を否定しても、あなたが自分自身を（。最後まで見捨てないでいて（。ください。"),
    ("testimony", "Testimony", "証言、証拠", "14th Century", "testis (witness)", "A formal written or spoken statement, especially one given in a court of law", "一人の人間の魂が、良心という名の下に「証人（テスティス）」として差し出した、改ざん（。のできない純粋で重みのある言葉の贈り物。", "あなたのこれまでの「テスティモニー（誠実な歩みの証（）」が、今、困難（。な状況にあるあなたを救い出すための、何よりも雄弁で（。最強の証拠になるはずですよ。"),
    ("exhibit", "Exhibit", "展示物、証拠物件、示す", "15th Century", "ex- (out) + habere (to hold, have)", "An object or collection of objects on public display", "隠されていた真実を白日の下に「抱き出し（ホールド）、外へと（アウト）呈示した」もの。言葉の装飾を脱ぎ捨て、その存在のみで真実を語る証拠。", "新しい「エキシビット（提示された証拠）」が見つかるたび、これまでの（。思い込みという名の厚い壁が、音を立てて崩れ去って（。いく。これこそが、真理を志す者の醍醐味（だいごみ）なのです。"),
    ("brief", "Brief", "短い、要約、弁論趣意書", "14th Century", "brevis (short)", "A concise statement or summary", "膨大な事実や感情の中から、最も重要なエッセンスだけを「短く（ブレイヴ）」抽出し、誰にでも一瞬で伝わるように結晶化させた、知性の輝き。", "「ブリーフ（要約・簡潔な書面）」の中にこそ、書き手の真の教養と、相手（。への深い配慮が凝縮されています。冗長（。な言葉の森を抜け出し、この一行の真実を（。届けましょう。"),
    ("petition", "Petition", "請願（書）、願い事", "14th Century", "petere (to strive for, seek, rush at)", "A formal written request, typically one signed by many people", "一人（。では小さすぎる声を束ね、より高い理想や変革を求めて（。、力強く「当局（フェア）へと向かっていく」ための、切実な祈りの声明。", "あなたの「ペティション（熱烈な願い）」が、たとえ今は誰にも届かない（。としても、その『求め続ける』という純粋なエネルギー（。は、確実に世界を正しい方向へと動かし始めているのです。"),
    ("grievance", "Grievance", "不満、苦情、不当な扱い", "13th Century", "gravare (to weigh down)", "A real or imagined wrong or other cause for complaint or protest, especially unfair treatment", "理不尽な重荷（。を負わされ、その「あまりの重さ（グレイヴ）」に、魂が押し潰（。されそうになりながらも、平穏を求めて叫ぶ不条理の訴え。", "心に溜まった「グリーヴァンス（心のしこり）」を、毒のまま自分（。の中に留め（。おかないでください。正しい言葉（。の形へと変換して、外へと解き放つことが、真の癒しの（。始まりなのです。"),
    ("arbitration", "Arbitration", "仲裁、調停", "15th Century", "arbitrari (to judge, decide, observe)", "The use of an arbitrator to settle a dispute", "中立的な立場の者が、両者の間に入り、冷静な「観察者（アービター）」として公正な判断を下すことで、争いの炎を静かに鎮（しず）めようとする対話の知恵。", "「アービトレーション（第三者による仲裁）」は、負けること（。を認めることではありません。お互いの尊厳を守りながら、共に（。幸せになれる新しい着地点を見つけ出すための、知的な（。戦略（ストラテジー）なのです。"),
    ("mediation", "Mediation", "仲介、調停", "14th Century", "mediare (to divide in the middle, be in the middle)", "Intervention in a dispute in order to resolve it; arbitration", "感情の激流の「真ん中（ミドル）」に立ち、両方の声を等しく聴くことで、分断された心と心の間に、再び（。対話の橋を架けようとする慈愛に満ちた（。介入。", "あなたが「メディエーション（中間に立つ者）」として放つ、穏やかで（。温かい一言が、憎しみの連鎖を断ち切り、凍りついた（。場の空気を劇的に溶かしていく（。魔法になることもあるのです。"),
    ("compliance", "Compliance", "従順、遵守、コンプライアンス", "17th Century", "complere (to fill up, finish, fulfill)", "The action or fact of complying with a wish or command", "社会や倫理の期待を、自らの行動によって「完全に満たし（フリフィル）」、秩序という名のパズルを完成させようとする、誠実さと調和の姿勢。", "「コンプライアンス（法令遵守）」とは、形だけのルールに従うこと（。ではなく、そのルールの向こう側にある『人々の安全と幸せ（。』を、心から願い続けるという誠実さ（インテグリティ）そのものなのです。"),
    ("integrity", "Integrity", "誠実、清廉、完全性", "14th Century", "integer (whole, intact)", "The quality of being honest and having strong moral principles; moral uprightness", "外部（。からの圧力があっても、自らの信念を決して曲げ（。ず、一貫性を持った「完全な一つ（インテジャー）」であり続けようとする、魂の高貴な頑固さ。", "あなたの「インテグリティ（誠実な一貫性）」は、誰にも奪うこと（。のできない黄金の財産です。その輝きを失わない（。限り、あなたはどんな暗闇の中でも、自分を見失わずに歩いて（。いけるでしょう。"),
    ("virtue", "Virtue", "徳、美徳、長所", "12th Century", "virtutem (force, power, bravery)", "Behavior showing high moral standards", "単（。なる優しさではなく、困難の中でも正しいことを選び（。抜く「力強い魂（パーソナル・パワー）」のあらわれ。人間を高みに（。引き上げる、内なる神聖な力。", "「ヴァーチュ（不朽の美徳）」は、隠れて行う善行の中にこそ宿ります（。、誰（。の目にも触れず、ただ自分自身の良心（。にだけ恥じない生き方。それこそが、究極の美学（。なのです。"),
    ("conscience", "Conscience", "良心、罪悪感", "13th Century", "com- (with) + scire (to know)", "An inner feeling or voice viewed as acting as a guide to the rightness or wrongness of one's behavior", "他の誰も（。知らない真実を、自分だけは「共に（コン）知って（サイエンス）いる」という、決して逃げられない内なる審判の声（インナー・ボイス）。", "夜、一人（。静かに目を閉じた時。あなたの「コンシャス（研ぎ澄まされた良心）」があなたに（。囁く（。言葉。それこそが、あなたが明日を生きるための、唯一の（。正しいコンパスになるはずです。"),
    ("scrutinize", "Scrutinize", "精査する、じろじろ見る", "17th Century", "scruta (trash, rags, remnants)", "Examine or inspect closely and thoroughly", "表面的な（。美しさに惑わされず、あえて「ゴミや屑（スクルー）」の山をかき分けるように、細部まで徹底的に疑い、真実を暴き出（。そうとする妥協なき眼差し。", "自分自身の心を、勇気を持って「スクルーティナイズ（徹底的に精査）」して（。みてください。そこに隠れた小さなエゴを見つけた時、あなたは（。また一歩、真の強者（。への階段を登ることになるのですから。"),
    ("validate", "Validate", "有効にする、確認する、認める", "16th Century", "valere (to be strong, be worth)", "Check or prove the validity or accuracy of", "曖昧（。な疑念を、確かな証拠（エヴィデンス）によって「強固（。な価値（ヴァリュー）を持つもの」へと昇華させ、正式に命の色を与える認証（ライセンス）のプロセス。", "誰かの痛みを「バリデート（その通りだと認める）」してあげること。それ（。だけで、その人はどれほど救われる（。か。否定する前に、まず『あなたの苦しみを私は信じる（。』という言葉を届けてください。"),
    ("rectify", "Rectify", "是正する、直す", "14th Century", "rectus (straight) + facere (to make)", "Put right; correct", "曲がってしまった（。現実を、勇気を持って「真っ直ぐな（レク）形へと作り直（。す（フィス）」こと。間違いを認め、正しい軌道へ力強く引き戻す、再生の修正（リペア）。", "過ちを犯（。すことを恐れる必要はありません。大切なのは、それを発見（。した瞬間に、即座に「レクティファイ（正しく修正）」する勇気と（。スピード、そして誠実さを（。持ち合わせていることなのです。"),
    ("justify", "Justify", "正当化する、弁明する", "14th Century", "justus (just) + facere (to make)", "Show or prove to be right or reasonable", "自らの行動や（。意志を、正義（ジャスティス）という鏡に照らし合わせ、それが「正しいものであると（。形作る（フィス）」ための、論理的な証明と魂の宣言。", "他人に対する（。「ジャスティファイ（弁明による正当化）」を急がないでください。あなたが（。真実を誠実に生きている（。なら、いずれ時間という最高に厳格な執行官が（。、あなたの正しさを（。証明してくれるはずですから。"),
    ("impartial", "Impartial", "公平な、偏らない", "16th Century", "in- (not) + partial (favoring one side)", "Treating all rivals or disputants equally; fair and just", "特定の（。利害や感情という「一方（。パート）への加担」を完全に拒否（。し、透明で穏やかな湖面のように、すべての存在を平等に映し出す（。冷静なる俯瞰（ふかん）。", "「インパーシャル（何者にも偏らない）」な視点を持つことは、孤独（。になる勇気を持つことでもあります。誰の顔色もうかがわ（。ず、ただ真理（。の声にだけ耳を澄ませる。それが賢者の（。義務（デューティー）なのです。"),
    ("ethical", "Ethical", "倫理的な、道徳上の", "16th Century", "ethos (habit, character, custom)", "Relating to moral principles or the branch of knowledge dealing with these", "一瞬の（。感情に流されず、長い年月をかけて育まれた「魂の正しい習慣（。エトス）」に基づき、他者と世界に対して誠実に（。あろうとする（。、最も人間らしい生き方の形式。", "「エシカル（倫理的である）」な選択は、一見（。損をしているように見える（。かもしれませんが、それはあなたの魂の品格（。を高め、一生揺るぎない（。自信という名の最高の富を（。もたらしてくれるのです。"),
    ("legitimate", "Legitimate", "合法的な、正当な", "15th Century", "lex (law)", "Conforming to the laws or rules", "単（。にルールに従っているだけでなく、その根源にある「法（。レックス）の精神」を完璧に体現（。しており、誰の目にも疑いようのない（。正しさと輝きを纏（まと）っている状態。", "あなたが心（。の底からワクワク（。すること。それが、あなたの人生において最も「レジティメイト（正当な）」権利（。であり、果たすべき使命（ミッション）であることに（。、早く気づいてくださいね。"),
    ("sovereign", "Sovereign", "主権者、君主、至上の、独立した", "13th Century", "super (above)", "A supreme ruler, especially a monarch", "何者（。にも支配されず、自らの意志のみが「最高位（。スーパー）にある」ことを宣言（。する、究極の自律（。と自由を体現する、誇り高く（。孤独なる王者の魂。", "あなたは自分自身（。の人生という王国の、唯一無二の「ソブリン（至高の主権者）」なのです。他（。の誰にも、あなたの玉座（。を明け渡しては（。絶対に（。なりませんよ。"),
    ("secular", "Secular", "世俗的な、非宗教的な、1世紀の", "13th Century", "saeculum (age, generation, century)", "Not connected with religious or spiritual matters", "神聖（。な領域に逃げ込むのではなく、今の時代（サーキュラム）という「目の前の現実（。の荒野」を、自分の足で（。泥にまみれ（。ながら突き進もう（。とする、地に足の着いた（。誠実な歩み。", "「セキュラー（世俗的な日常）」の中にこそ、真の修行（。の場があります。特別な場所（。へ行かなくても、目の前の仕事や家族（。との関わりを丁寧に扱う（。こと（。が（。、最高の祈りになるのです。"),
    ("universal", "Universal", "普遍的な、宇宙の、全般的な", "14th Century", "unus (one) + vertere (to turn)", "Of, affecting, or done by all people or things in the world or in particular", "特定の（。場所や時間を越え、全ての存在を「一つの方向へと（。回転させて）結びつける」ことができる（。、ダイヤモンドのような（。硬質で（。輝かしい不変の真理。", "「ユニバーサル（普遍的な）」な価値観とは、他（。から押し付けられ（。るものではなく、あなたの心の奥底（。を深く深く深く掘（。っていった先で（。、人類全員が共有している（。黄金の泉に辿り着く（。プロセスそのものなのです。"),
    ("fundamental", "Fundamental", "根源的な、基本的な", "15th Century", "fundamentum (foundation, bottom)", "Forming a necessary base or core", "表面的な（。変化に惑わされず、その建物を支える「最も深い底（。ファンド）」に横たわっている、一切（。の妥協が許されない（。、存在そのものを規定する（。絶対的な重み。", "「ファンダメンタル（根源的）」な原則を（。疎か（おろそか）に（。していては、どんなに華やかな城も一瞬で崩れ去り（。ます。まずは足元の（。土台を、一粒の砂（。に至るまで誠実に（。固めることから始めて（。ください。"),
    ("inherent", "Inherent", "固有の、本来備わっている", "16th Century", "in- (in) + haerere (to stick)", "Existing in something as a permanent, essential, or characteristic attribute", "外部（。から付け足されたものではなく、あなたの魂の細胞壁（。に「最初から（。ピッタリと）張り付いている」、あなたという人間（。を構成する（。不可避で聖なる特質そのもの。", "あなた（。に「インヒーレント（本来備わっている）」な才能は、他（。の誰とも競争（。する必要のない、あなただけの（。ギフトです。その種（。を信じて（。、ただ静かに、そして力強く（。芽吹かせて（。あげてください。"),
    ("duty", "Duty", "義務、職務、関税", "13th Century", "debere (to owe)", "A moral or legal obligation; a responsibility", "自分がここにある理由として、社会や未来から「借りて（。デュー）いる」エナジーを、誠実な行動（。というかたちで正しく（。お返ししよう（。とする、人間としての気高き（。負債（義務）。", "「デューティ（果たすべき義務）」を重荷（。としてではなく、この世界（。に自分が存在を（。許されていることへの（。、最高の『恩返し』だと思って（。向き合って（。みてください。その時（。、義務は喜びに変わります。")
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
            word_id = f"{word_text.lower()}_law"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "正義とは、他者を愛することの別の名前です。",
                    "example": f"The court was established to ensure that {word_text} prevailed in the aftermath of the conflict.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["倫理は形式ではなく、心の奥底で鳴り響く共鳴の音楽です。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["impartial", "ethical", "legitimate", "secular", "universal", "fundamental", "inherent"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Law & Ethics (Cycle 27).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
