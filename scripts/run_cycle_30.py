import json
import re

# Theme: The Alchemy of Art & Aesthetics (Cycle 30)
words_data = [
    ("easel", "Easel", "画架、イーゼル", "17th Century", "ezel (donkey)", "A wooden frame for holding an artist's work while it is being painted", "重いキャンバスを黙々と（。しぶとく）支え続け（。、一歩も引かない頑丈さ。画家の（。魂の（。冒険を（。背負（。う、忠実な（。ロバ（。のような（。道具（。）。", "真っ白な「イーゼル（画架）」の（。前に（。立った（。とき（。、あなたは（。世界で（。一番（。孤独（。で（。、そして（。一番（。自由（。な（。創造主（。になれるのですよ。"),
    ("palette", "Palette", "調色板、パレット", "16th Century", "pala (spade, shovel)", "A thin board or slab on which an artist lays and mixes colors", "色（。という（。エナジー（。を（。、まるで（。シャベル（。で（。掘り起こす（。ように（。力強く（。、そして（。繊細に（。混ぜ（。合わせる（。、可能性（。が（。渦巻く（。虹色の（。ゆりかご（。）。", "あなたの（。心という「パレット（調色板）」には（。、まだ（。名前の（。ない（。色が（。たくさん（。眠って（。います（。。（。悲しみ（。という（。青に（。、勇気（。という（。赤を（。そっと（。混ぜて（。みてください。"),
    ("canvas", "Canvas", "キャンバス、帆布", "13th Century", "cannabis (hemp)", "A strong, coarse unbleached cloth made from hemp, flax, or a similar yarn, used to make items such as sails and tents and as a surface for oil painting", "嵐（。の（。海（。を（。突き進む（。帆（。と同じ（。強靭な（。麻（。の（。布（。。（。未知（。の（。景色（。を（。描き込（。む（。ための（。、揺るぎ（。ない（。精神の（。大地（。）。", "真っさらな「キャンバス（帆布）」を（。恐れないで（。ください（。。（。最初（。の（。一筆（。が（。、あなた（。を（。新しい（。世界（。へと（。連（。れ出して（。くれる（。唯一の（。パスポート（。になる（。のですから。"),
    ("fresco", "Fresco", "フレスコ画", "16th Century", "fresco (fresh)", "A painting done rapidly in watercolor on wet plaster on a wall or ceiling", "漆喰（しっくい）が「新鮮（。フレッシュ）」な（。うちに（。、一気（。に（。魂（。を（。叩き込（。む（。技術（。。（。やり直しの（。きかない（。緊張感（。が（。、不滅（。の（。輝き（。を（。生み出す（。刹那（。の（。魔法（。）。", "「フレスコ（鮮やかな真実）」のように（。、今（。この（。瞬間（。の（。感動（。を（。逃さ（。ず（。に（。言葉（。に（。して（。ください（。。（。時間が（。経（。てば（。、その（。熱（。は（。二度と（。戻（。っては（。こない（。のです。"),
    ("mosaic", "Mosaic", "モザイク、寄せ絵", "15th Century", "muse (muses - goddesses of inspiration)", "A picture or pattern produced by arranging together small colored pieces of hard material, such as stone, tile, or glass", "バラバラの（。破片（。を（。寄せ集め（。、女神（。ミューズ）の（。導きの（。ままに（。、一つの（。巨大な（。美（。へと（。結晶（。させ（。た（。、細部（。と（。全体（。が（。響き合う（。奇跡（。）。", "あなたの（。これまでの（。挫折（。や（。涙（。の（。破片（。も（。、長い（。目で見れば（。、一つの（。美しい「モザイク（寄せ絵）」の一部に（。すぎません（。。（。完成（。した（。とき（。、全ての（。傷（。は（。輝（。く（。星座（。に（。変わる（。でしょう。"),
    ("tapestry", "Tapestry", "タペストリー、織り絵", "14th Century", "tapes (carpet, rug)", "A piece of thick textile fabric with pictures or designs formed by weaving colored weft threads or by embroidering on canvas, used as a wall hanging or furniture covering", "経糸（。たていと）と（。緯糸（。よこいと）が（。複雑（。に（。絡み合う（。、手触りの（。ある（。歴史（。（。一針一針（。に（。込められた（。祈り（。が（。、壁（。を（。物語（。に変える（。織物（。）。", "人生（。は（。巨大な「タペストリー（織り絵）」の（。ようです（。。（。苦しみ（。の（。暗（。い（。糸（。が（。ある（。から（。こそ（。、喜び（。の（。黄金（。の（。糸（。が（。、目（。も（。眩（。む（。ほど（。に（。美しく（。映える（。のですよ。"),
    ("sculpture", "Sculpture", "彫刻", "14th Century", "sculpere (to carve, engrave)", "The art of making two- or three-dimensional representative or abstract forms, especially by carving stone or wood or by casting metal or plaster", "荒々（。しい（。石（。の（。塊（。の中から（。、その（。奥に（。眠る「真実の（。生命）」を（。、削り（。出す（。（。スカーヴ）ことで（。解放（。する（。、引き算（。の（。美学（。）。", "不必要な（。見栄（。や（。虚飾（。を（。毎日少しずつ（。「スカルプチャー（彫刻）」して（。みてください（。。（。最後に（。残（。った（。あなたが（。、真（。に（。美しい（。あなた（。なの（。ですから。"),
    ("statue", "Statue", "彫像、スタチュー", "14th Century", "stare (to stand)", "A carved or cast figure of a person or animal, especially one that is life-size or larger", "時の（。洗礼（。に（。耐（。え（。、そこ（。に（。「不動（。に（。立ち（。スタ）続ける（。）」こと（。を（。許された（。、人間（。の（。尊厳（。と（。不変性（。を（。体現（。する（。石（。の（。沈黙（。）。", "どんなに（。批判（。の（。嵐（。が（。吹き荒れ（。ても（。、自分（。の（。正義（。の（。上に「スタチュー（彫像）」のように（。毅然（。として（。立っていて（。ください（。。（。その（。姿（。が（。、いつか（。新しい（。時代の（。道標（。になる（。のです。"),
    ("monument", "Monument", "記念碑、モニュメント", "13th Century", "monere (to remind, advise, warn)", "A statue, building, or other structure erected to commemorate a famous person or event", "過去の（。偉大（。な（。出来事（。を（。、忘れ（。ない（。ように（。と（。、「警告（。モニター）」し（。続ける（。記憶（。の（。装置（。。（。石（。となって（。、死者（。の（。意志（。を（。今（。へと（。繋ぐ（。楔（くさび）。", "あなたの（。小さな（。善行（。は（。、誰（。かの（。心（。の中に（。、目（。に見えない「モニュメント（記念碑）」として（。永遠（。に（。残り（。続けます（。。（。歴史（。に（。名を（。残（。すより（。、ずっと（。素敵な（。こと（。だと思（。いませんか。"),
    ("relief", "Relief", "浮き彫り、安堵、リリーフ", "14th Century", "re- (back) + levare (to raise, lift)", "A sculptural technique where the sculpted elements remains attached to a solid background of the same material", "平坦な（。背景（。から（。、一部（。を「再び（。リ）持ち上げる（。レヴェ）」ことで（。、影（。と（。奥行き（。を（。産み出し（。、平面（。に（。命（。を（。吹き込（。む（。技法（。）。", "苦（。し（。み（。から（。解放（。された（。瞬間の「リリーフ（安堵）」は（。、あなたの（。人生の（。物語（。に（。、深（。い（。深（。い（。奥行き（。を（。与えて（。（。くれる（。、最高の（。贈り物（。なのですよ。"),
    ("ceramics", "Ceramics", "陶磁器、セラミックス", "19th Century", "keramos (potter's clay)", "Pots and other articles made from clay hardened by heat", "柔らかい（。泥（。ケラモス）が（。、火（。の（。試練（。を（。受けて（。、宝石（。のような（。硬度（。と（。輝き（。を（。手（。に入（。れた（。、元素（。の（。錬金術（。）。", "あなた（。の（。心（。の（。傷（。も（。、経験（。という（。火（。にく（。べ（。（。られ（。、長い（。時間（。を（。かければ（。、いつか（。「セラミックス（陶器）」のように（。、強くて（。美しい（。誇（。りに（。変わ（。ります。"),
    ("glaze", "Glaze", "釉薬（うわぐすり）、光沢", "14th Century", "glas (glass)", "A vitreous substance fused on to the surface of pottery to form a hard, impervious decorative coating", "土（。の（。器（。を（。、「ガラス（。グラス）」のような（。透明な（。膜（。で（。覆い（。、光（。を（。乱反射（。させて（。、内側（。の（。色彩（。を（。永遠（。に（。守（。り（。抜（。く（。聖なる（。コーティング（。）。", "あなたの（。瞳（。の「グレーズ（美しい煌めき）」を（。曇（。らせない（。で（。ください（。。（。その（。光（。が（。ある（。限り（。、世界（。の（。どんな（。汚れ（。も（。、あなた（。を（。傷つける（。こと（。は（。できない（。のですよ。"),
    ("perspective", "Perspective", "遠近法、見通し、観点", "14th Century", "per- (through) + specere (to look)", "The art of drawing solid objects on a planar surface so as to give the right impression of their height, width, depth, and position in relation to each other when viewed from a particular point", "網の目を「透（。かして（。パー）見る（。スぺ）」ことで（。、平面（。の中に（。無限（。の（。奥行き（。を（。発見する（。知性（。の（。発見（。。（。どこに（。立ち（。、どこを（。見つめる（。か（。という（。自由の（。宣言（。）。", "「パースペクティブ（見通し）」を（。変える（。だけで（。、絶望（。の（。壁（。は（。一瞬（。にして（。、新しい（。世界（。へと（。続く（。扉（。へと（。変貌（。する（。のです。"),
    ("silhouette", "Silhouette", "シルエット、輪郭", "18th Century", "Étienne de Silhouette (French minister)", "The dark shape and outline of someone or something visible against a lighter background, especially in dim light", "細部（。の（。虚飾（。を（。削（。ぎ（。落（。し（。、光（。に（。抗（。う「かたち（。フォルム）」だけ（。を（。強調（。した（。、存在（。の（。最も（。純粋（。で（。抽象的（。な（。影（。）。", "言葉（。を（。尽くさ（。なくて（。も（。、背中（。の「シルエット（輪郭）」だけで（。、その（。人の（。孤独（。や（。覚悟（。が（。伝わ（。って（。くる（。ことが（。あります（。。（。存在（。そのもの（。の（。力を（。信じ（。て（。ください。"),
    ("caricature", "Caricature", "風刺画、カリカチュア", "18th Century", "caricare (to load, exaggerate)", "A picture, description, or imitation of a person or thing in which certain striking characteristics are exaggerated in order to create a comic or grotesque effect", "真実（。の（。重荷（。を（。、あえて「過剰に（。チャージ）積み込む」ことで（。、その（。人の（。本質（。を（。ユーモア（。と（。皮肉（。の（。中に（。描き（。出す（。、ゆがんだ（。鏡の（。魔法（。）。", "他人の（。描いた「カリカチュア（歪んだ人物像）」に（。振り回（。されない（。で（。ください（。。（。鏡（。の（。中の（。自分（。に（。ニカッと（。笑い（。かければ（。、それ（。だけで（。呪い（。は（。解ける（。のですよ。"),
    ("ornament", "Ornament", "装飾品、オーナメント", "13th Century", "ornare (to equip, adorn)", "A thing used to make something look more attractive but having no practical purpose, especially a small object such as a figurine", "ただ（。飾（。る（。だけでなく（。、その（。存在を「完全（。に（。装備（。オーナ）する」ための（。、矜持（。と（。祝福（。の（。欠片（。。（。日常（。を（。聖なる（。時間（。へと（。変（。え（。る（。ための（。微差（。）。", "あなたの（。優しい（。笑顔（。は（。、社会（。という（。殺伐（。とした（。空間を（。彩（。る（。、最高（。の「オーナメント（心の宝飾）」なのです（。。（。それ（。を（。決して（。絶やさ（。ないで（。ください。"),
    ("symmetry", "Symmetry", "対称、シンメトリー", "16th Century", "sun- (together) + metron (measure)", "The quality of being made up of exactly similar parts facing each other or around an axis", "中心点（。から（。左右（。を「共に（。シン）測（。る（。メトリー）」ことで（。、完璧な（。均衡（。と（。静寂（。を（。産み出す（。、宇宙の（。数学的（。な（。美（。の方程式（。）。", "心（。の（。中に「シンメトリー（静かなる対称性）」を（。保（。って（。ください（。。（。怒（。り（。の（。波（。が（。来たら（。、同じ（。だけの（。静寂（。を（。対（。に（。置く（。。（。そう（。すれば（。、あなたは（。どんな（。嵐（。にも（。流（。され（。ません。"),
    ("proportion", "Proportion", "比率、均衡、プロポーション", "14th Century", "pro- (for, according to) + portio (part, share)", "A part, share, or number considered in comparative relation to a whole", "全体（。の（。中で（。、一つ（。ひとつの「部分（。部分）」を（。どのように（。割り振（。るかという（。、黄金（。の（。分配（。の（。智慧（。。（。調和（。を（。もたらす（。重さの（。リズム（。）。", "「プロポーション（正しい比率）」を（。見極（。めて（。ください（。。（。仕事（。と（。休息（。、（。理想（。と（。現実（。。（。その（。バランス（。の（。中に（。こそ（。、真（。に（。美（。しい（。人生（。は（。宿（。る（。もの（。なのです。"),
    ("composition", "Composition", "構成、作曲、構図", "14th Century", "com- (together) + ponere (to place, put)", "The nature of something's ingredients or constituents; the way in which a whole or mixture is made up", "バラバラの（。要素（。を（。、意図を持って「一箇所（。に（。コン）配置（。ポーズ）する」ことで（。、新しい（。意味（。と（。エナジー（。を（。産み（。出す（。、知的な（。編集（。の（。行為（。）。", "今日（。という（。日は（。、あなた（。が（。自由に（。描（。ける「コンポジション（未完成の構図）」です（。。（。どんな（。色（。を（。置き（。、どんな（。余白（。を（。残（。すか（。。（。すべては（。あなた（。の（。センス（。に（。委（。ね（。られて（。います。"),
    ("texture", "Texture", "手触り、質感、テクスチャ", "15th Century", "texere (to weave)", "The feel, appearance, or consistency of a surface or a substance", "ただ（。眺める（。だけでなく（。、指先（。が（。捉（。える「織（。り（。テクス）なされた（。）」複雑（。な（。凹凸（。。（。物質（。の（。奥底（。に（。潜（。む、微細な（。物語（。の（。手触り（。）。", "言葉（。にも「テクスチャ（温かな質感）」が（。あります（。。（。冷たい（。メール（。（。の（。文字（。の（。中にも（。、相手（。への（。想い（。を（。織り込め（。ば（。、それは（。確（。かな（。温（。もり（。として（。伝わ（。る（。はず（。ですよ。"),
    ("brushstroke", "Brushstroke", "筆致、タッチ", "Old English", "brush + stroke", "A mark made by a paintbrush drawn across a surface", "画家の（。筋肉（。の（。震（。え（。や（。、その（。時（。の（。呼吸（。が（。、そのまま（。物質（。として（。定着（。した（。、魂の（。筆跡（。。（。一筆（。の中に（。、全人格（。が（。宿る（。）。", "あなた（。の一生（。懸（。命な（。「筆致（ブラッシュストローク）」を（。誰も（。（。見て（。いない（。と（。嘆（。かない（。で（。ください（。。（。世界（。という（。キャンバス（。には（。、あなた（。が（。描（。き（。残（。した（。勇気（。の（。跡（。が（。、確（。かに（。刻（。まれて（。いる（。のです。"),
    ("varnish", "Varnish", "ワニス、上塗り、光沢", "14th Century", "veronice (sandarac resin)", "Resin dissolved in a liquid for applying on wood, metal, or other materials to form a hard, clear, shiny surface when dry", "完成（。した（。努力（。の（。結晶（。を（。、外部（。の（。酸化（。から（。守り（。、深（。い（。光輝（。を（。与（。える（。ための（。、最後（。の（。透明な（。ヴェール（。）。", "丁寧（。な（。仕上（。げ（。こそが（。、作品（。に「ヴァニッシュ（永遠の光）」を（。灯（。します（。。（。最後の（。一（。手間（。を（。惜（。しまない（。その（。誠実（。さが（。、あなた（。を（。本物（。に（。する（。のです。"),
    ("lacquer", "Lacquer", "漆（うるし）、ラッカー", "16th Century", "laksha (one hundred thousand - referring to many insects)", "A liquid made of shellac dissolved in alcohol, or of synthetic substances, that dries to form a hard protective coating for wood, metal, etc.", "無数（。の（。命（。が（。紡（。ぎ（。出（。した（。樹脂（。を（。、何層（。にも（。塗（。り（。重（。ねる（。ことで（。、闇（。の（。中から（。最高（。の（。艶（。を（。引き出す（。、東洋の（。神秘（。的な（。被膜（。）。", "漆（。のように（。、人生（。の（。苦（。し（。み（。を（。何度（。も「ラッカー（。漆）」として（。塗（。り（。重（。ねて（。ください（。。（。その（。厚（。み（。が（。、いつか（。鏡（。のように（。美（。しく（。、何物（。にも（。傷（。つか（。ない（。誇（。りに（。なり（。ます。"),
    ("antique", "Antique", "骨董品、アンティーク", "16th Century", "antiquus (former, ancient)", "A collectible object such as a piece of furniture or work of art that has a high value because of its considerable age", "単に（。古い（。だけでなく（。、過ぎ去（。った（。「前の（。アンティ）時代（。）」の（。精神（。が（。、美し（。い（。形の（。まま（。保存（。され（。て（。いる（。、時（。の（。琥珀（。）。", "あなた（。の（。中（。の「アンティーク（古（。き良き信念）」を（。、時代（。遅（。れ（。だと（。捨て（。ないで（。ください（。。（。新（。しい（。もの（。が（。一瞬（。で（。古（。び（。る（。中で（。、変わらない（。本物（。だけ（。が（。、最後（。まで（。価値（。を（。持（。ち（。続ける（。のですよ。"),
    ("baroque", "Baroque", "バロック、歪んだ真珠、過度に装飾的な", "18th Century", "barocco (irregularly shaped pearl)", "Relating to or denoting a style of European architecture, music, and art of the 17th and 18th centuries that used exaggerated motion and clear, easily interpreted detail to produce drama, tension, exuberance, and grandeur", "完璧（。な（。球体（。から（。「歪（。んだ（。バロック）真珠」のように（。、過剰（。な（。装飾（。と（。劇的（。な（。明暗（。を（。持って（。、世界（。の（。力強（。さを（。謳（。い（。上げ（。ようと（。する（。、圧倒的（。な（。情熱（。の（。奔流（。）。", "あなたの（。個性（。が（。他人（。に（。とって（。は「バロック（歪（。な（。もの）」に（。見（。えて（。も（。、それ（。こそが（。あなた（。を（。輝（。か（。せる（。、世界で（。唯一（。の（。宝石（。なの（。ですよ。"),
    ("gothic", "Gothic", "ゴシック、野蛮な、高貴な暗闇", "17th Century", "Goths (Germanic tribe)", "Relating to a style of architecture which prevailed in Europe roughly from the 12th to the 16th centuries, characterized by pointed arches, rib vaults, and flying buttresses, together with large windows and elaborate tracery", "かつて（。野蛮（。と（。された（。部族の精神が（。、天を突く（。尖塔（。と（。光り輝く（。ステンドグラス（。へと（。変貌（。した（。もの（。。（。暗闇（。と（。光（。が（。激しく（。交錯（。する（。、魂の（。峻烈（。な（。祈り（。）。", "あなた（。の（。（。中に（。ある「ゴシック（高貴な暗闇）」を（。否定（。しないで（。ください（。。（。本当（。の（。光（。は（。、底（。無（。し（。の（。深い（。闇（。を（。知（。る（。者（。に（。だけ（。、その（。美（。しさ（。を（。あら（。わ（。す（。のですよ。"),
    ("classic", "Classic", "古典の、一流の、クラシック", "17th Century", "classicus (belonging to the highest class of citizens)", "Judged over a period of time to be of the highest quality and outstanding of its kind", "時代（。の（。荒波（。に（。洗（。われ（。て（。も（。、決して（。古（。び（。ず（。、常に「最高順位（。クラス）」の（。座（。に（。留（。まり（。続ける（。、美（。と（。知性（。の（。不変（。の（。模範（。）。", "「クラシック（古典）」に（。触（。れる（。こと（。は（。、千（。年前（。の（。天才（。と（。、今（。この（。瞬間（。に（。対話（。する（。こと（。です（。。（。時（。の（。壁（。を（。軽（。やか（。に（。越（。える（。、その（。魔法（。を（。体験（。して（。ください。"),
    ("modern", "Modern", "現代の、最新の", "16th Century", "modo (just now)", "Relating to the present or recent times as opposed to the remote past", "過去（。の（。遺産（。に（。頼（。らず（。、「たった今（。モド）」の（。感（。性（。と（。技術（。で（。、世界（。を（。ゼロ（。から（。定義（。し（。直（。そう（。とする（。、瑞（。々（。しく（。も（。残酷（。な（。最前線（。）。", "常に「モダン（今を生きる視点）」を（。忘れ（。ないで（。ください（。。（。過去（。に（。安住（。せず（。、絶（。えず（。変化（。し（。つづ（。ける（。こと（。。（。それ（。（。こそが（。、あなた（。が（。生き（。て（。いる（。という（。、最大（。の（。証拠（。なの（。ですよ。"),
    ("surreal", "Surreal", "超現実的な", "20th Century", "sur- (over) + real", "Having the qualities of surrealism; bizarre", "平凡（。な「現実（。リアル）の（。上（。シュール）」に（。、無意識（。や（。夢（。の（。エナジー（。を（。溢（。れ（。出（。させ（。、世界（。の（。真（。の（。不気味（。さと（。美（。しさ（。を（。一露（。わ（。にする（。、覚醒（。への（。衝撃（。）。", "「シュール（超現実的）」な（。景色（。に（。出遭（。った（。ら（。、それは（。あなた（。の（。心が（。、今（。までの（。窮屈（。な（。常識（。を（。脱（。ぎ（。捨て（。よう（。と（。して（。いる（。合図（。な（。の（。かも（。し（。れません。"),
    ("sublime", "Sublime", "崇高な、卓越した", "14th Century", "sub- (under) + limen (threshold)", "Of such excellence, grandeur, or beauty as to inspire great admiration and awe", "日常（。の「敷居（。リメン）の（。下（。サブ）」を（。越え（。、人間の（。理解（。を（。遥（。かに（。（。凌（。駕（。する（。ような（。、畏（。怖（。に（。満（。ち（。た（。巨大（。な（。美（。の（。深淵。"),
    ("elegant", "Elegant", "優雅な、洗練された", "15th Century", "ex- (out) + legere (to choose)", "Pleasingly graceful and stylish in appearance or manner", "余計（。な（。ものを（。全て（。削（。ぎ（。落（。し（。、真髄（。だけを「選び（。レクト）出した（。エクス）」、一切（。の（。澱（。みのない（。、しなやか（。で（。知性（。溢れる（。美しさの（。極致（。）。", "「エレガント（洗練）」とは（。、たくさん（。持（。って（。いる（。こと（。では（。なく（。、自分（。に（。本当に（。必要（。な（。ものを（。、一つ（。だけ（。知（。って（。いる（。こと（。なのです。"),
    ("ornate", "Ornate", "装飾の多い、派手な", "14th Century", "ornare (to equip, adorn)", "Made in an intricate shape or decorated with complex patterns", "隅々（。まで（。手（。を（。尽くして「飾（。り（。オーナ）立てられ（。）」、空白（。を（。美（。の（。エナジー（。で（。埋め尽くそうとする（。、生命（。の（。躍動（。と（。豊穣（。の（。あらわれ（。）。", "シンプル（。な（。生き方（。も（。良い（。ですが（。、たまには「オーネイト（装飾的）」な（。冒険（。に（。身（。を（。任せて（。みて（。ください（。。（。デコレーション（。を（。楽（。しむ（。心（。が（。、人生（。に（。彩（。り（。を（。与えて（。くれる（。の（。ですから。"),
    ("vivid", "Vivid", "鮮やかな、生き生きとした", "17th Century", "vivere (to live)", "Producing powerful feelings or strong, clear images in the mind", "単に（。色が（。濃（。い（。だけでなく（。、まるで（。それ（。自体（。が「生命（。ヴィヴィ）を持って（。）」、今（。にも（。動（。き（。出し（。そうな（。、眩（。い（。ばかりの（。鮮烈（。な（。輝き（。）。", "あなた（。の（。夢（。を「ヴィヴィッド（鮮烈）」な（。色彩（。で（。描き（。続（。けて（。ください（。。（。その（。鮮やか（。さが（。、退屈（。な（。日常（。を（。打（。ち（。破（。り（。、未来（。を（。手（。繰（。り（。寄（。せる（。鍵（。に（。なる（。のですよ。"),
    ("radiant", "Radiant", "光り輝く、輻射（ふくしゃ）の", "15th Century", "radius (ray, spoke of a wheel)", "Sending out light; shining or glowing brightly", "中心（。から（。車輪の（。「スポーク（。ラディウス）」のように（。、あらゆる（。方向（。へと（。光（。のエナジーを（。真っ直ぐに（。放（。って（。いる（。、溢（。れ（。出（。る（。喜びの（。オーラ（。）。", "「ラディアント（光り輝く）」な（。笑顔（。を（。、今日（。は（。一回（。だけ（。、大切な（。人（。に（。向（。けて（。みてください（。。（。その（。一筋（。の（。光（。が（。、相手（。の（。凍（。り（。ついた（。心を（。一瞬（。で（。溶（。かして（。しまう（。はずです。"),
    ("incandescent", "Incandescent", "白熱する、光り輝く", "18th Century", "in- (in) + candere (to glow, to be white-hot)", "Emitting light as a result of being heated", "内側（。から（。極限まで（。加熱（。され（。、「白（。熱（。キャン）した状態に（。イン）至った」輝き（。。（。自らの（。魂（。を（。燃（。やし（。尽（。くす（。覚悟（。が（。、周囲（。をも（。照（。らし出（。す。"),
    ("translucent", "Translucent", "半透明の", "16th Century", "trans- (through) + lucere (to shine)", "Allowing light, but not detailed shapes, to pass through; semitransparent", "光（。を（。完全に（。跳（。ね返（。さず（。、その（。身を「透（。かして（。トランス）通（。す（。ルー）」ことで（。、柔らか（。で（。幻想（。的な（。諧調（。を（。産み出す（。、謙虚（。で（。神秘（。的な（。美学（。）。", "「トランスルーセント（半透明の）」な（。優（。し（。さを（。持（。って（。ください（。。（。自分（。の（。正解（。を（。他（。人に（。押し付け（。ず（。、ただ（。光（。が（。透（。き（。通（。る（。（。余白（。を（。残（。して（。おく（。こと（。。（。それ（。こそが（。、真（。の（。知性（。なのですよ。"),
    ("opaque", "Opaque", "不透明な、分かりにくい", "14th Century", "opacus (shaded, dark, shadowy)", "Not able to be seen through; not transparent", "光（。を（。一切（。通（。さず（。、深く（。「陰（。っている（。オパック）」状態（。。（。表面（。の（。質感（。と（。色彩（。だけに（。徹（。することで（。、内側（。の（。神秘（。を（。頑（。なに（。に（。守（。り（。抜（。く（。、拒絶（。と（。神秘の（。美（。）。", "時には（。「オピーク（不透明）」な（。仮面（。を（。被（。って（。、自分（。の（。大切な（。感情（。を（。、世界（。の（。野次馬（。から（。守（。って（。あげる（。ことも（。必要（。な（。のです（。。（。ミステリアス（。な（。まま（。で（。、いい（。のですよ。"),
    ("sketch", "Sketch", "写生、スケッチ、概要", "17th Century", "skhedios (temporary, done extempore)", "A rough or unfinished drawing or painting, often made to assist in making a more finished product", "完璧（。な（。完成（。を（。目指（。さず（。、ただ「その場（。で（。スケ）一時的（。に」捉（。えた（。、対象（。の（。最も（。瑞々しい（。エッセンス（。の（。記録（。）。", "人生（。は（。絶望（。的な（。完成品（。ではなく（。、一連の（。終わり（。なき「スケッチ（草稿）」の（。連続（。な（。のだと（。思（。えば（。、失敗（。は（。ただの（。面白（。い（。線（。の一本（。に（。過（。ぎ（。なく（。なり（。ます。"),
    ("portrait", "Portrait", "肖像画、描写", "16th Century", "pro- (forth) + trahere (to draw)", "A painting, drawing, photograph, or engraving of a person, especially one depicting only the face or head and shoulders", "一人の（。人間（。が（。纏（。って（。いる（。不可視の（。空気（。を（。、言葉（。や（。色彩（。によって（。外部（。へと「引（。き（。トラ）き出す（。プロ）」こと（。。（。外見（。では（。なく（。、魂の（。輪郭（。を（。描く（。行為（。）。", "あなた（。に（。しか（。描け（。ない「ポートレート（真実の描写）」が（。あります（。。（。誰（。かの（。美（。しさを（。、あなた（。だけ（。の（。言葉（。で（。引き（。出して（。伝（。えて（。あげる（。こと（。。（。それは（。世界（。に（。対（。する（。、最大（。の（。貢献（。なのですよ。"),
    ("landscape", "Landscape", "風景、風景画", "16th Century", "land + -scape (shape, condition)", "All the visible features of an area of countryside or land, often considered in terms of their aesthetic appeal", "単なる（。土地（。ランド）では（。なく（。、人間（。の（。眼差し（。が（。入り（。込（。む（。ことで（。、一つの「かたち（。スケープ）」として（。立ち上が（。って（。きた（。、意味（。を（。持（。った（。世界（。の（。断片（。）。", "あなた（。の（。前（。に（。広が（。って（。いる「ランドスケープ（心象風景）」を（。、悲しみ（。の（。色（。だけで（。塗（。り（。潰（。さないで（。ください（。。（。一歩（。歩（。けば（。、景色（。は（。かならず（。新（。しい（。表情（。を（。見（。せて（。くれる（。はず（。ですから。")
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
            word_id = f"{word_text.lower()}_art"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "美は、魂が世界に触れるための最も繊細な指先です。",
                    "example": f"The museum houses a magnificent {word_text} that dates back to the Renaissance.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["創造とは、沈黙の中から光を引き出す行為です。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["sublime", "elegant", "ornate", "vivid", "radiant", "incandescent", "translucent", "opaque"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Art & Aesthetics (Cycle 30).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
