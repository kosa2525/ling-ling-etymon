import json
import re

words_data = [
    ("crisp", "Crisp", "ぱりっとした", "Old English", "crisp (curly, frizzy)", "Sharp and fresh", "余分なものが何もない、研ぎ澄まされた清々しさ。", "冬の朝の「クリスプ（ぱりっとした）」な空気を深呼吸すれば、心まで透き通ります。"),
    ("fluffy", "Fluffy", "ふわふわの", "16th Century", "flue (down, nap)", "Light and soft", "空気を含み、重力から解放されたような優しい感触。", "「フラッフィー（ふわふわ）」の毛布に包まれる時間は、最高の癒やしです。"),
    ("sticky", "Sticky", "べたべたする", "Old English", "stician (to stick, adhere)", "Adhesive", "対象から離れたくても離れられない、強い執着と引力。", "人間関係も、時には「スティッキー（べたつく）」な執着を手放すことが大切です。"),
    ("slippery", "Slippery", "滑りやすい", "Old English", "slidor (slippery)", "Hard to catch", "確かなものが何もなく、すぐに手の中からスルリと抜け落ちてしまう儚さ。", "「スリッパリー（滑りやすい）」な真実を無理に捕まえようとせず、時には見守る勇気を。"),
    ("damp", "Damp", "湿った", "Middle Low German", "damp (vapor, steam)", "Slightly wet", "完全に濡れているわけではなく、空気中に水分（エナジー）が満ちている状態。", "雨上がりの「ダンプ（湿った）」な土の匂いは、命の芽吹きを教えてくれます。"),
    ("brittle", "Brittle", "もろい", "14th Century", "breoten (to break)", "Easily broken", "硬さはあるものの、内なる柔軟性を欠いているため、衝撃に弱い様。", "強がるばかりで「ブリトル（もろく）」なる前に、弱さを認めるしなやかさを。"),
    ("sleek", "Sleek", "なめらかな", "Middle English", "slik (smooth)", "Smooth and glossy", "摩擦を極限まで減らし、周囲の抵抗を受け流す洗練された美。", "「スリーク（なめらか）」な振る舞いは、どんな荒波も美しく乗り越えます。"),
    ("coarse", "Coarse", "粗い", "14th Century", "cours (ordinary, common)", "Rough texture", "過剰な装飾のない、本質そのものがむき出しになった野性味。", "表面が「コース（粗く）」ても、その奥にある本当の優しさを見抜いてください。"),
    ("bumpy", "Bumpy", "でこぼこの", "16th Century", "bump (a swell, bulge)", "Uneven surface", "平坦ではなく、変化に富んだ道のりが生み出す豊かなリズム。", "「バンピー（でこぼこ）」な人生だからこそ、予想外の美しい景色に出会えます。"),
    ("jagged", "Jagged", "ギザギザの", "14th Century", "jag (a sharp projection)", "Uneven and sharp", "整えられていない、刃のような不規則さが放つ強烈な個性。", "「ジャグド（ギザギザ）」な感情も、あなたのユニークな魅力の一部です。"),
    ("rough", "Rough", "ざらざらした", "Old English", "ruh (rough, hairy)", "Not smooth", "洗練される前の、原石そのものが持つ計り知れないエネルギー。", "「ラフ（ざらざらした）」なくらいが、人間らしくてちょうどいいのかもしれません。"),
    ("stiff", "Stiff", "堅い", "Old English", "stif (rigid, inflexible)", "Hard to bend", "外部からの力に屈服しない強さと、変化を恐れる硬直性の同居。", "時には「スティフ（堅い）」な思考を柔らかくほぐす時間も必要です。"),
    ("flexible", "Flexible", "柔軟な", "15th Century", "flectere (to bend)", "Able to bend", "外的要因に合わせて自分を自在に変化させ、本質を守り抜く強さ。", "「フレキシブル（柔軟）」な心を持つ人は、どんな状況でも決して折れません。"),
    ("tender", "Tender", "柔らかい", "13th Century", "tener (soft, delicate)", "Soft and gentle", "傷つきやすさを内包した、他者への深い思いやりと共感。", "誰かの弱さに触れるときは、「テンダー（優しく）」に包み込んであげて。"),
    ("fuzzy", "Fuzzy", "ぼやけた", "16th Century", "fuzz (loose fibers)", "Indistinct", "境界線が曖昧で、すべてがゆるやかに繋がっている暖かい状態。", "答えが出ない日は、「ファジー（曖昧）」なまま眠りについても大丈夫です。"),
    ("grainy", "Grainy", "粒状の", "14th Century", "granum (seed)", "Containing grains", "一つ一つの小さな粒子（経験）が寄り集まって作られる確かな質感。", "「グレイニー（粒状の）」な日々の積み重ねが、あなたの歴史を豊かにします。"),
    ("sheer", "Sheer", "透き通るような", "Middle English", "skere (bright, clear)", "Transparently thin", "向こう側が透けて見えるほどの、隠し事を持たない絶対的な純粋さ。", "「シアー（透き通る）」な心で世界を見れば、すべてが美しく輝いて見えます。"),
    ("dense", "Dense", "密集した", "15th Century", "densus (thick, crowed)", "Closely compacted", "情報や物質が高い密度で圧縮され、圧倒的な存在感を放つ状態。", "「デンス（密集した）」なスケジュールをこなし終えた後の達成感は格別です。"),
    ("hollow", "Hollow", "空洞の", "Old English", "holh (a hole)", "Empty inside", "中身が何もないからこそ、新しいものを無限に受け入れることができる器。", "心に「ホロウ（空洞）」を感じたときは、そこへ新しい愛を満たす準備ができたサインです。"),
    ("solid", "Solid", "固体の", "14th Century", "solidus (firm, whole)", "Firm and stable", "中身が詰まっており、揺るぐことのない絶対的な信頼と安定感。", "「ソリッド（確かな）」な友情は、どれだけ時間が経っても色褪せません。"),
    ("liquid", "Liquid", "液体の", "14th Century", "liquidus (fluid)", "Flowing freely", "形を固定せず、与えられた器や状況に完璧に適応する水の性質。", "「リキッド（液体）」のように形を変えながら、人生という川を流れていきましょう。"),
    ("porous", "Porous", "多孔性の", "14th Century", "porus (a pore, passage)", "Full of holes", "無数の小さな穴（窓）を開け、外部と絶えず呼吸を交わし続ける開かれた状態。", "「ポーラス（隙間のある）」な心を持てば、新しいインスピレーションが絶えず流れ込みます。"),
    ("flaky", "Flaky", "剥がれやすい", "14th Century", "flake (a large snowflake)", "Breaking into flakes", "薄く層になり、はらはらと崩れ落ちていく美しさと儚さ。", "「フレイキー（剥がれ落ちる）」な過去の殻を捨てて、新しい自分へと生まれ変わりましょう。"),
    ("spongy", "Spongy", "スポンジ状の", "15th Century", "spongia (sponge)", "Compressible and absorbent", "柔らかく反発し、どんな経験も吸収しては元に戻る驚異の復元力。", "「スポンジー（吸収力のある）」な心で、世界中の美しいものを吸い込んで。"),
    ("lush", "Lush", "青々とした", "15th Century", "lasche (soft, loose)", "Luxuriant and abundant", "生命力が溢れ（あふれ）、豊潤な恵みを惜しみなく与える深い緑の世界。", "「ラッシュ（青々と茂った）」な森に迷い込んだような、豊かなインスピレーションをあなたに。"),
    ("sparse", "Sparse", "まばらな", "18th Century", "spargere (to scatter)", "Thinly dispersed", "要素が少なく、一つ一つの存在が際立つ洗練されたミニマリズム。", "情報が「スパース（まばら）」な場所ほど、本当の自分の声がクリアに聴こえます。"),
    ("opaque", "Opaque", "不透明な", "15th Century", "opacus (shaded, dark)", "Not transparent", "光を通さないことで、内部の神秘と秘密を厳重に守り抜く盾。", "「オペイク（不透明）」な他者の心への不可解さを愛することが、真の共感の始まりです。"),
    ("translucent", "Translucent", "半透明の", "16th Century", "translucere (to shine through)", "Allowing light but not detailed shapes", "光だけを柔らかく通し、真実は見せないミステリアスなベール。", "「トランスルーセント（半透明の）」な朝の霧のように、現実と夢は常に重なり合っています。"),
    ("muted", "Muted", "音を消した、和らげた", "16th Century", "mutus (silent)", "Not bright or loud", "強さを抑えることで、かえって奥ゆかしい響きを際立たせる美的感覚。", "「ミューテッド（和らげられた）」な色彩は、どんな激しい感情も静かに包み込みます。"),
    ("vivid", "Vivid", "鮮やかな", "17th Century", "vivere (to live)", "Intense and brightly colored", "生命力が直接視覚に訴えかけ、今この瞬間を強烈に意識させる輝き。", "「ヴィヴィッド（鮮烈な）」な記憶は、どんなに時間が経ってもあなたの魂を熱くします。"),
    ("fragile", "Fragile", "壊れやすい", "16th Century", "frangere (to break)", "Easily broken or damaged", "繊細さが故に、取り扱いには最大限の愛と注意を必要とする尊さ。", "人は誰でも「フラジャイル（壊れやすい）」な部分を持っています。思いやりを忘れずに。"),
    ("sturdy", "Sturdy", "頑丈な", "13th Century", "estordi (dazed, violent)", "Solidly built", "幾多の試練を耐え抜き、深く大地に根を下ろした不動の精神。", "「スターディ（頑丈な）」な土台さえあれば、どんな高い理想の塔も築くことができます。"),
    ("resilient", "Resilient", "弾力のある、回復力のある", "17th Century", "resilire (to leap back)", "Able to spring back", "どれだけ押しつぶされても、再び元の形へと跳ね返る不屈のエネルギー。", "何度転んでも起き上がる「レジリエント（回復力のある）」な姿勢こそが、最大の才能です。"),
    ("plump", "Plump", "ふっくらした", "15th Century", "plump (blunt, rounded)", "Full and rounded", "内側から豊かなエナジーが満ち溢れ、幸せの形となった丸み。", "「プランプ（ふっくらとした）」な果実の甘さは、太陽の愛を一身に浴びた証です。"),
    ("scant", "Scant", "乏しい", "14th Century", "skamt (short)", "Barely sufficient", "ギリギリの量しかなく、だからこそ一滴の価値が際立つ貴重さ。", "「スカント（乏しい）」な言葉から、背語に隠れた深い海のような思いを汲み取ってください。"),
    ("ample", "Ample", "十分な", "15th Century", "amplus (large, wide)", "Plentiful", "制限を気にせず、全てを包み込んでなお余りある宇宙の豊かさ。", "あなたには「アンプル（十分過ぎる）」な時間が残されています。焦らずゆっくり進みましょう。"),
    ("frigid", "Frigid", "極寒の", "15th Century", "frigidus (cold)", "Extremely cold", "すべての活動を停止させ、時間を凍結させる圧倒的な静寂の低温。", "「フリジッド（凍てつくような）」な厳しい冬の後には、必ず美しい春の光が訪れます。"),
    ("tepid", "Tepid", "なまぬるい", "14th Century", "tepidus (lukewarm)", "Slightly warm", "熱狂も絶望もない、平熱のまま進行する穏やかで残酷な停滞期。", "時には「テピッド（なまぬるい）」な日常を抜け出し、心を燃やす冒険へと出かけましょう。"),
    ("scalding", "Scalding", "熱湯の", "13th Century", "excaldare (to wash in warm water)", "Extremely hot", "触れるものすべてを痛めつけるほどの、過剰な情熱と怒りの沸点。", "「スコーディング（焼け付くような）」な情熱は、劇薬のように取り扱いに注意が必要です。"),
    ("crispy", "Crispy", "サクサクした", "16th Century", "crisp (curly)", "Firm and brittle", "水分のない乾いた状態が作り出す、軽快で小気味良いリズム。", "「クリスピー（サクサクの）」な落ち葉を踏む音で、世界の小さな変化を感じ取って。"),
    ("soggy", "Soggy", "水浸しの", "16th Century", "sog (a swamp)", "Heavy with moisture", "水分を吸いすぎて重くなり、形を保てなくなった悲しい飽和状態。", "涙で「ソギー（水浸し）」になった心のスポンジは、一度ぎゅっと絞って天日干ししましょう。"),
    ("brisk", "Brisk", "活発な", "16th Century", "brusque (fierce)", "Active and fast", "迷いのない足取りと冷たい風が織りなす、精神を覚醒させるスピード感。", "「ブリスク（きびきびした）」な行動力は、淀んだ空気を一瞬で吹き飛ばします。"),
    ("sluggish", "Sluggish", "怠惰な", "15th Century", "slugge (lazy person)", "Slow-moving", "重力に逆らえず、泥の中を進むような精神と肉体の重い疲労感。", "「スラギッシュ（のろのろした）」な日は、宇宙があなたに休息を命じている日です。"),
    ("buoyant", "Buoyant", "浮力のある", "16th Century", "boya (a buoy)", "Able to float or rise", "どんな重荷を背負っても、最終的には上へと浮かび上がる底抜けの明るさ。", "「ボイアント（浮き上がる）」なユーモアのセンスは、絶望の海でもあなたを沈めません。"),
    ("leaden", "Leaden", "鉛色の、重たい", "Old English", "lead (heavy metal)", "Heavy like lead", "心が鉛のように重く沈み、光さえも届かない魂のどん底。", "心が「レドゥン（鉛のように重い）」時は、無理に浮かび上がろうとせず、底で静かに息を潜めて。")
]

words = []
for item in words_data:
    root1 = item[4].split(" ")[0]
    meaning1 = " ".join(item[4].split(" ")[1:]).strip("()")
    w = {
        "id": f"{item[0]}_texture",
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
        "example": f"The sensation felt remarkably {item[0]}.",
        "deep_dive": {
            "roots": [{"term": root1, "meaning": meaning1}],
            "points": ["私たちが物理世界（物質）と接する境界線の手触り。"]
        },
        "part_of_speech": "adjective"
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
    print(f"Success: Added {added} words. Theme: Textures & Sensations (Cycle 2).")
else:
    print("Error parsing data.js")
