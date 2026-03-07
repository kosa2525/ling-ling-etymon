import json
import re

words_data = [
    ("pillar", "Pillar", "柱、支柱", "12th Century", "pila (pillar, stone)", "A tall vertical structure", "空間を重力から解放し、天を押し広げるために屹立（きつりつ）する孤独で力強い垂直の意志。", "あなたが「ピラー（支柱）」として立っているからこそ、私たちはこの大空を見上げることができます。"),
    ("arch", "Arch", "アーチ、曲線", "13th Century", "arcus (bow, arch)", "A curved symmetrical structure", "二つの別々の力が中心でぶつかり合い、押し合うことで初めて生まれる奇跡の調和と安定。", "異なる意見が衝突する「アーチ（曲線）」の頂点にこそ、最も強固な絆が生まれます。"),
    ("vault", "Vault", "アーチ型の天井、金庫室", "14th Century", "volvita (turned, vaulted)", "A roof in the form of an arch", "空の広がりを自らの手で模倣し、神聖なものを外敵から永遠に守り抜くための石の宇宙。", "あなたの心の中にある「ヴォールト（金庫室）」には、誰にも盗まれない輝く記憶が眠っています。"),
    ("dome", "Dome", "ドーム、丸屋根", "16th Century", "domus (house)", "A rounded vault", "全ての角（限界）を取り払い、世界を一つの完璧な円として包み込む究極の母なる空間。", "「ドーム（丸屋根）」のようなあなたの大きな愛は、どんな傷ついた魂も優しく包み込みます。"),
    ("column", "Column", "円柱、コラム", "15th Century", "columna (pillar)", "An upright pillar", "装飾性と機能性を極限まで高め、歴史の重みを無言で支え続ける威厳に満ちた背骨。", "「コラム（円柱）」のようにまっすぐなあなたの信念は、どんな時代の波にも揺るぎません。"),
    ("facade", "Facade", "正面、外見", "17th Century", "faccia (face)", "The face of a building", "外部の世界に向けて最も美しく、最も虚飾に満ちた「顔」を見せる自己防衛の絶対的な仮面。", "時に立派な「ファサード（建物の正面顔）」を作ることも、大人としての礼儀であり優しさです。"),
    ("portal", "Portal", "入り口、正門", "14th Century", "porta (gate)", "A doorway, gate", "日常の世界から、特別な意味を持った異界へと足を踏み入れるための通過儀礼となる境界線。", "この「ポータル（正門）」をくぐるとき、あなたは昨日までの古い自分を捨て去るのです。"),
    ("threshold", "Threshold", "敷居、出発点", "Old English", "therscwold (to process corn)", "A strip of wood or stone forming the bottom of a doorway", "内と外、過去と未来を分け隔て、次の一歩を踏み出す者に覚悟を問う神聖なしるし。", "新しい挑戦への「スレッショルド（敷居）」をまたぐ瞬間は、いつだって足がすくむものです。"),
    ("foundation", "Foundation", "土台、基礎", "14th Century", "fundare (to lay a base for)", "The lowest load-bearing part of a building", "決して人目には触れることなく、泥の中で全ての重みを無言で引き受ける究極の献身。", "見えない「ファウンデーション（基礎）」の深さだけ、高く美しい塔を建てることができます。"),
    ("basement", "Basement", "地下室", "18th Century", "basis (base)", "The floor of a building which is partly or entirely below ground level", "光が届かない深い場所で、建物の最も本源的な欲望と秘密、そして配管（血脈）を隠し持つ器官。", "人間の「ベースメント（地下室）」には、表には出せない強烈な情熱や狂気が眠っているのです。"),
    ("attic", "Attic", "屋根裏部屋", "16th Century", "Attikos (Athenian)", "A space or room just below the roof", "天井と空のわずかな隙間に挟まれ、忘れ去られた過去の記憶と埃だけがひっそりと眠るノスタルジーの聖域。", "心の「アティック（屋根裏）」に古い写真をしまっておくことで、私たちは明日へ進めます。"),
    ("cellar", "Cellar", "地下貯蔵庫", "13th Century", "cellarium (storehouse)", "A room below ground level", "時間という名の最高のスパイスを用いて、ワインや魂をゆっくりと成熟させるための暗く冷たい揺りかご。", "怒りや悲しみも、「セラー（地下貯蔵庫）」で寝かせれば、いずれ芳醇な愛へと変わります。"),
    ("corridor", "Corridor", "廊下、回廊", "16th Century", "currere (to run)", "A long passage in a building", "空間と空間を繋ぐためだけに存在し、誰の所有にもならない「移動」という動性を宿した空白の道。", "人生という果てしない「コリドー（廊下）」を歩く過程こそが、真の目的そのものなのです。"),
    ("balcony", "Balcony", "バルコニー", "17th Century", "balcone (scaffold)", "A platform enclosed by a wall", "内なる安全地帯にいながらにして、外の世界の風と光を貪欲に取り込もうとする贅沢な特等席。", "「バルコニー（展望台）」から見下ろす世界は、あんなにも小さく、そして愛おしく見えます。"),
    ("terrace", "Terrace", "テラス、台地", "16th Century", "terra (earth)", "A level paved area or platform", "自然の傾斜を人間の意志で切り開き、空と大地の境界に造り上げられた平穏で開放的な舞台。", "「テラス（高台の庭）」で飲む一杯のコーヒーは、日常の重力をすべて洗い流してくれます。"),
    ("courtyard", "Courtyard", "中庭", "16th Century", "cohors (yard) + yard", "An unroofed area", "建物の壁によって外部の騒音を遮断し、自分たちだけの閉じられた空を切り取る秘密の楽園。", "「コートヤード（中庭）」に降り注ぐ光は、外のどこよりも優雅で親密な温かさを持っています。"),
    ("patio", "Patio", "パティオ、中庭", "19th Century", "Spanish (court)", "A paved outdoor area", "内と外の中間地点に位置し、自然の恵みを生活の一部としてカジュアルに楽しむための交差点。", "天気の良い日は「パティオ（中庭）」に出て、ただ風の音に耳を傾けるだけで十分です。"),
    ("porch", "Porch", "ポーチ、玄関廊", "13th Century", "porticus (colonnade)", "A covered shelter", "外の世界へ出る前の最後の避難所であり、お客様を招き入れるための最初の安らぎの空間。", "雨の日に「ポーチ（玄関先の屋根の下）」で雨宿りをする時間は、不思議な一体感を与えてくれます。"),
    ("canopy", "Canopy", "天蓋（てんがい）", "14th Century", "konopeion (mosquito net)", "An ornamental cloth covering", "王座や寝台を覆い、そこに居る者を神聖な力で保護しているかのように見せる優雅で権威あるベール。", "森の木々が織りなす「キャノピー（緑の天蓋）」の下を歩けば、自然の神々からの祝福を感じます。"),
    ("awning", "Awning", "日よけ、雨よけ", "17th Century", "Unknown (sail)", "A sheet of canvas on a frame", "過酷な日差しや雨の刃から、道行く人たちを一時的に守るために張り出された布の小さな慈悲。", "カフェの「オーニング（日よけ）」の下で雨宿りした偶然が、最高の恋の始まりになるかもしれません。"),
    ("scaffolding", "Scaffolding", "足場", "14th Century", "escadafaut (scaffold)", "A temporary structure", "完成した美しさを生み出すために不可欠でありながら、完成後には跡形もなく撤去される運命にある無名の英雄たち。", "子どもが自立するまでの間、親はただ見守るための「スキャフォールディング（足場）」となるのです。"),
    ("framework", "Framework", "枠組み、骨組み", "16th Century", "frame + work", "An essential supporting structure", "物事の全体像を決定づけ、そこへ後から肉付けしていくための、不可視だが最も強固な論理的構造。", "どんなに美しい理想も、確かな「フレームワーク（骨組み）」がなければすぐに崩れ去ります。"),
    ("blueprint", "Blueprint", "設計図、青写真", "19th Century", "blue + print", "A design plan", "まだこの世に存在していない巨大な夢を、誰にでも分かるように青と白の二色に翻訳した正確な希望。", "人生の「ブループリント（青写真）」を何度書き直しても構いません。あなただけの傑作のために。"),
    ("layout", "Layout", "配置、間取り", "19th Century", "lay + out", "The way in which parts are arranged", "空間や情報の各要素が互いにどう機能し合うかを俯瞰の視点で最適化し、美しい調和を生み出すデザインの核。", "部屋の「レイアウト（配置）」を変えるだけで、驚くほど心が軽く、新しい自分に出会えます。"),
    ("edifice", "Edifice", "大建築物、堂々とした建物", "14th Century", "aedificare (to build)", "A building, especially a large, imposing one", "ただの建物であることを越え、何世紀にもわたって人々に畏敬の念を抱かせる社会や宗教の巨大なモニュメント。", "先人たちが残した「エディフィス（大建築物）」の前に立つと、人間の意志の強大さに圧倒されます。"),
    ("monument", "Monument", "記念碑、遺跡", "14th Century", "monere (to remind)", "A statue, building, to commemorate a person", "忘却という時間の冷酷な流れに抗い、特定の記憶や栄光を石や金属に刻み込んで永遠に留めようとする祈り。", "誰かに愛されたという記憶こそが、あなたの心の中に建つ最も美しい「モニュメント（記念碑）」です。"),
    ("shrine", "Shrine", "神社、聖地", "Old English", "scrinium (chest for books)", "A place regarded as holy", "神聖なものや遺物を保護するための箱が拡大し、空間全体を現世から隔離した清浄なアンタッチャブル・ゾーン。", "あなたの内なる平和を守る「シュライン（聖域）」には、どんな土足の侵入者も入れてはいけません。"),
    ("sanctuary", "Sanctuary", "聖域、避難所", "14th Century", "sanctus (holy)", "A place of refuge or safety", "世俗の法律や暴力が一切及ばない、弱き者たちが最後に逃げ込むことができる無条件の安全地帯。", "彼にとって絵を描くアトリエは、この狂った世界から逃れる唯一の「サンクチュアリ（聖なる避難所）」でした。"),
    ("altar", "Altar", "祭壇", "Old English", "altare (high place)", "The table in a Christian church", "神と人間の交信のために高所に設けられた、究極の供犠（くぎ）と祈りが捧げられる聖なる結節点。", "愛という名の「オルター（祭壇）」の前では、誰もが自分の最も大切なものを喜んで捧げるのです。"),
    ("spire", "Spire", "尖塔（せんとう）", "Old English", "spir (tall grass)", "A tapering conical or pyramidal structure", "教会の屋根から空へ向かって鋭く突き出し、人々の祈りを天へと導くための針のような道標。", "遠くに見える教会の「スパイア（尖塔）」は、迷子になった旅人に帰るべき方角を教えてくれます。"),
    ("steeple", "Steeple", "（教会などの）尖塔", "Old English", "stepel (tower)", "A church tower and spire", "高い塔と尖塔が組み合わさり、街のどこからでも神の存在を見上げるための圧倒的な垂直のモニュメント。", "夕焼けに染まる「スティープル（背の高い教会の塔）」を見上げると、一日のすべての罪が赦された気がします。"),
    ("belfry", "Belfry", "鐘楼（しょうろう）", "15th Century", "berfroi (siege tower)", "The part of a bell tower", "もとは敵を監視する塔であったが、やがて平和を告げ、時間を知らせる平和的な音の響きを空から降らす場所へと変容した。", "「ベルフリー（鐘楼）」から響く鐘の音は、悲しみの中にある街のすべての人々に平等に降り注ぐ音の光です。"),
    ("cloister", "Cloister", "回廊、修道院", "13th Century", "claudere (to close)", "A covered walk in a convent", "外界の誘惑から完全に「閉ざされた」中庭をぐるりと囲み、神との対話だけをひたすらに繰り返すためのストイックな歩行路。", "時には「クロイスター（回廊）」のように心を世間から切り離し、自分の内面の声だけを聴く散歩をしましょう。"),
    ("labyrinth", "Labyrinth", "迷宮、迷路", "14th Century", "labyrinthos (maze)", "A complicated irregular network of passages", "方向感覚を失わせる無数の分岐を持ちながらも、実は中心へと確実に向かっているという究極の一本道。", "一見複雑に見える人生の「ラビリンス（迷宮）」も、一歩一歩進めば必ず真実の中心へと到達するようにできています。"),
    ("maze", "Maze", "迷路", "13th Century", "masen (to confuse)", "A network of paths and hedges", "複数の正解と無数の行き止まりを用意して、あえて挑戦者を「混乱」させ、知性を試すための厄介なゲーム。", "終わりの見えない「メイズ（迷路）」の真ん中で立ち尽くした時は、無理に進まず、空を見上げる余裕を。"),
    ("catacomb", "Catacomb", "地下墓地", "Old English", "catacumbae (underground cemetery)", "An underground cemetery", "生者たちの賑やかな街の地下に、死者たちが永遠の眠りにつきながら静かに広がり続ける見えないもう一つの都市。", "歴史の光が当たらない「カタコンベ（地下墓地）」にこそ、その時代の真実が生々しく保存されているものです。"),
    ("dungeon", "Dungeon", "地下牢、どんじょん", "14th Century", "dominus (lord)", "A strong underground prison", "城の最も防御が固い主塔であったものが、やがて敵を二度と光を見せない深い闇の底に幽閉する絶望の牢獄へと姿を変えた。", "心の「ダンジョン（地下牢）」にトラウマを押し込めて鍵をかけると、それは闇の中でますます巨大なモンスターに育ちます。"),
    ("fortress", "Fortress", "要塞、砦", "14th Century", "fortis (strong)", "A military stronghold", "絶対に陥落しないという強固な意志（強さ）で塗り固められ、あらゆる外敵の攻撃から内部の命を守り抜く孤高の山。", "どれほど分厚い「フォートレス（要塞）」を心の周りに築いても、愛だけは音もなくその壁をすり抜けてきます。"),
    ("citadel", "Citadel", "防塞、とりで", "16th Century", "civitas (city)", "A fortress, typically on high ground", "街全体が敵に略奪されようとも、市民たちが最後に立てこもり決死の抵抗を試みる最も神聖で強固な最終防衛ライン。", "あなたの誇りという「シタデル（最後の砦）」だけは、誰に何を言われても決して明け渡してはいけません。"),
    ("bastion", "Bastion", "稜堡（りょうほ）、防塞", "16th Century", "bastire (to build)", "A projecting part of a fortification", "城壁から外へ突き出し、側面から敵を容赦なく攻撃するための、攻撃的な防御を担う鋭い角。", "伝統と文化を守り抜く強固な「バスティオン（突出した砦）」として、彼は一人で時代の波に逆らい続けています。")
]

words = []
for item in words_data:
    root1 = item[4].split(" ")[0]
    meaning1 = " ".join(item[4].split(" ")[1:]).strip("()")
    w = {
        "id": f"{item[0]}_architecture",
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
        "example": f"The ancient {item[0]} stood tall against the changing seasons.",
        "deep_dive": {
            "roots": [{"term": root1, "meaning": meaning1}],
            "points": ["空間を区切り、目的を与える「建築」という名の人間の意志表現。"]
        },
        "part_of_speech": "noun"
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
    print(f"Success: Added {added} words. Theme: Architecture (Cycle 6).")
else:
    print("Error parsing data.js")
