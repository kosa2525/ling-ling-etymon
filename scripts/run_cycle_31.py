import json
import re

# Theme: The Pulse of Energy & Motion (Cycle 31)
words_data = [
    ("momentum", "Momentum", "勢い、はずみ、運動量", "17th Century", "movimentum (movement, motion)", "The quantity of motion of a moving body, measured as a product of its mass and velocity", "一度（。動き（。ムーブ）出したら（。、誰にも（。止められない（。圧倒的な（。エナジーの（。持続（。。（。過去の（。努力（。が（。、未来の（。自分を（。力強く（。押し出す（。、目（。には（。見えない（。風。", "「モメンタム（勢い）」が（。ついている（。うちに（。、もう（。一段（。高い（。場所まで（。一気に（。駆け（。上がって（。ください（。。（。一度（。立ち止まって（。ま（。うと（。、再び（。同じ（。エナジーを（。産む（。のは（。大変な（。ことなの（。ですから。"),
    ("velocity", "Velocity", "速度、速さ", "16th Century", "velox (swift, rapid)", "The speed of something in a given direction", "単なる（。スピード（。ではなく（。、明確な「目的地（。ベクトル）」を（。伴（。った（。、洗練（。された（。速（。さ（。ベロックス）。無駄（。を（。削ぎ落とし（。、一直線（。に（。真理（。へと（。至る（。ための（。知性（。の（。矢。", "仕事の（。質（。とは（。、費（。やした（。時間（。ではなく（。、どれほど（。の（。「ヴェロシティ（意志ある速さ）」で（。、確（。かな（。価値（。を（。産み（。出したか（。、その（。密度（。によって（。決（。まるのです。"),
    ("acceleration", "Acceleration", "加速、促進", "16th Century", "ad- (to) + celerare (to hasten)", "A vehicle's capacity to gain speed within a short time", "今の（。自分を（。安住（。させず（。、さらに「速く（。セーラー）しよう（。と（。アド）」働きかけ（。、限界を（。一瞬ごとに（。書き換えて（。いく（。、意図的な（。飛躍。"),
    ("friction", "Friction", "摩擦、不和", "16th Century", "fricare (to rub)", "The resistance that one surface or object encounters when moving over another", "二つの（。異なる（。存在が（。激しく「擦（。れ（。フリカ）合う」ことで（。生まれる（。、熱（。と（。抵抗（。。（。停滞（。を（。打ち破る（。ための（。、不可避で（。創造的（。な（。痛み。"),
    ("inertia", "Inertia", "慣性、惰性、不活発", "17th Century", "iners (unskilled, inactive)", "A tendency to do nothing or to remain unchanged", "昨日（。と（。同じ（。ままで（。いよう（。とする（。、生命の「眠（。れる（。イナー）力（。）」。（。変化（。を（。拒み（。、静止（。あるいは（。等速（。の（。安心感（。に（。浸（。り（。続けよう（。とする（。、抗（。いがたい（。重力。"),
    ("kinetic", "Kinetic", "運動の、動力的な", "19th Century", "kinesis (movement)", "Relating to or resulting from motion", "静かなる（。沈黙（。の中に（。潜んでいた（。エナジーが（。、ついに「動き（。カネシス）出した（。）」、躍動感（。あふれる（。現実（。の（。手触り。"),
    ("potential", "Potential", "潜在力、可能性", "14th Century", "potis (powerful, able)", "Having or showing the capacity to become or develop into something in the future", "まだ（。目には（。見えない（。けれど（。、内側に（。「力（。パワー）として（。秘（。め（。られて（。いる（。）」、未来（。を（。爆発（。させる（。ための（。静かなる（。火種。"),
    ("voltage", "Voltage", "電圧、ボルテージ", "19th Century", "Alessandro Volta (Italian physicist)", "An electromotive force or potential difference expressed in volts", "エナジーが（。流れようと（。、内側から（。壁面を（。力強く（。押し（。広げて（。いる（。、「圧力（。プレッシャー）」としての（。情熱の（。高まり。"),
    ("current", "Current", "電流、流れ、現代の", "14th Century", "currere (to run)", "A body of water or air moving in a definite direction", "常に（。新しい（。場所を（。求めて「走り（。カー）続けて（。いる（。）」、淀（。みのない（。エナジーの（。連鎖。"),
    ("resistance", "Resistance", "抵抗、反抗", "14th Century", "re- (back) + sistere (to stand)", "The refusal to accept or comply with something; the attempt to prevent something by action or argument", "外部（。からの（。圧力に対し（。、あえて「立ち（。シスト）向（。かい（。リ）」、自らの（。境界（。を（。守（。り（。抜こう（。とする（。、誇り（。高い（。意志の（。壁。"),
    ("conductor", "Conductor", "指揮者、伝導体", "14th Century", "com- (together) + ducere (to lead)", "A person who directs the performance of an orchestra or choir", "バラバラの（。音（。や（。熱（。を（。、「一つへと（。コン）導（。き（。ドゥ）繋げる（。）」ことで（。、調和（。した（。大きな（。うねり（。を（。産み（。出す（。、知的な（。媒介者。"),
    ("insulator", "Insulator", "絶縁体", "18th Century", "insula (island)", "A substance which does not readily allow the passage of heat or sound", "周囲の（。激流（。から（。、自らを「島（。アイランド）のように（。隔離し（。）」、内なる（。静寂（。や（。熱（。を（。大切に（。守（。り（。続ける（。ための（。、静かなる（。障壁。"),
    ("radiation", "Radiation", "放射、放射線", "16th Century", "radius (ray, spoke of a wheel)", "The emission of energy as electromagnetic waves or as moving subatomic particles, especially high-energy particles which cause ionization", "中心から（。四方八方へと「光（。レイ）として（。放たれ（。）」、世界の（。隅々（。まで（。自らの（。影響（。を（。及（。ぼ（。そう（。とする（。、能動的（。な（。発散。"),
    ("convection", "Convection", "対流", "17th Century", "com- (together) + vehere (to carry)", "The movement caused within a fluid by the tendency of hotter and therefore less dense material to rise, and colder, denser material to sink under the influence of gravity", "熱（。という（。エナジーを（。、空間（。全体へと「共に（。コン）運び（。ヴェ）回（。す（。）」ことで（。、全体（。を（。活性化（。させ（。、均一な（。豊かさ（。を（。もたらす（。、調和（。の（。流転。"),
    ("conduction", "Conduction", "伝導", "16th Century", "com- (together) + ducere (to lead)", "The process by which heat or electricity is directly transmitted through a substance when there is a difference of temperature or of electrical potential between adjoining regions", "触（。れ（。合う（。もの（。同士が（。、「一つに（。コン）導（。き（。ドゥ）合う（。）」ことで（。、エナジーを（。手渡し（。で（。確実に（。伝え（。て（。いく（。、誠実（。な（。継承。"),
    ("thermal", "Thermal", "熱の、温度の", "18th Century", "therme (heat)", "Relating to heat", "生命の（。根源に（。ある「熱（。サーム）」。（。氷（。ついた（。沈黙（。を（。溶（。かし（。、全ての（。分子（。を（。躍（。らせ（。、変化（。の（。予感（。を（。周囲に（。解き放つ（。、静かなる（。情熱の（。温度。"),
    ("entropy", "Entropy", "エントロピー、無秩序、衰退", "19th Century", "en- (in) + trope (a turning)", "A thermodynamic quantity representing the unavailability of a system's thermal energy for conversion into mechanical work", "放（。って（。おけば（。、全ての（。エナジーが「内側（。イン）で（。混ざり（。トロピー）合（。い（。）」、やがて（。均質な（。死へと（。辿（。り（。着（。いて（。しまう（。、宇宙の（。非情（。な（。宿命。"),
    ("synergy", "Synergy", "シナジー、相乗効果", "17th Century", "sun- (together) + ergon (work)", "The interaction or cooperation of two or more organizations, substances, or other agents to produce a combined effect greater than the sum of their separate effects", "一人（。では（。決して（。成（。し遂げられ（。ない（。巨大な（。仕事を（。、「共に（。シン）働く（。エルゴン）」ことで（。、魔法（。のように（。何倍（。もの（。成果（。へと（。昇華（。させる（。、奇跡的な（。協力。"),
    ("resonance", "Resonance", "共鳴、響き", "15th Century", "re- (again) + sonare (to sound)", "The quality in a sound of being deep, full, and reverberating", "放たれた（。一粒の（。音が（。、相手の（。魂の（。震（。えと（。重（。なり（。、再び（。「高く（。リ）鳴（。り（。ゾン）響（。く（。）」、心（。と（。心（。の（。不可視の（。握手。"),
    ("oscillation", "Oscillation", "振動、揺れ", "17th Century", "oscillum (a swing)", "Movement back and forth at a regular speed", "二つの（。極端な（。場所を（。、「ブランコ（。スイング）のように（。）」行（。ったり（。来（。たり（。し（。ながら（。、中庸（。の（。調和（。を（。探し（。続け（。、一箇所に（。留（。まらない（。、動的な（。生命。"),
    ("vibration", "Vibration", "振動", "17th Century", "vibrare (to shake, brandish)", "An instance of vibrating; a quiver or tremor", "一瞬（。の（。休み（。もなく「震（。え（。ヴィブ）続ける（。）」こと（。。（。この（。世界（。は（。、一見（。静止（。して（。いる（。ように（。見えても（。、その（。深淵（。では（。常に（。全宇宙が（。歓喜に（。震（。えて（。いる（。のだという（。、生命の（。拍動。"),
    ("frequency", "Frequency", "周波数、頻度", "16th Century", "frequens (crowded, repeated)", "The rate at which something occurs or is repeated over a particular period of time or in a given sample", "何（。度も（。何（。度も（。、「繰（。り（。返し（。フレク）訪（。れる（。）」こと（。。（。あなた（。の（。日々の（。ルーティン（。の中に（。、どれほど（。誠実（。な（。祈り（。を（。込めたか（。、その（。密度の（。こと。"),
    ("amplitude", "Amplitude", "振幅、広さ、豊かさ", "16th Century", "amplus (large, wide)", "The maximum extent of a vibration or oscillation, measured from the position of equilibrium", "魂の（。揺（。れ（。が（。どれほど「深く、大きく（。アンプル）」世界（。へと（。響（。き（。渡（。って（。いるか（。。（。あなたの（。感情の（。ダイナミズム（。が（。描き出す（。、エナジーの（。巨大（。な（。曲線。"),
    ("spectrum", "Spectrum", "分光、スペクトル、範囲", "17th Century", "specere (to look)", "A band of colors, as seen in a rainbow, produced by separation of the components of light by their different degrees of refraction according to wavelength", "一見（。透明で（。無機質な（。光を「透（。かして（。スぺ）見つめる（。）」とき（。、そこ（。には（。無限（。の（。色彩（。が（。隠（。されていた（。ことに（。気づ（。く（。、認識の（。虹。"),
    ("photon", "Photon", "光子、フォトン", "20th Century", "phos (light)", "A particle representing a quantum of light or other electromagnetic radiation", "世界（。を（。照（。らす「光（。フォス）」の（。、最小（。の（。魂（。の（。粒（。。（。この（。一粒（。が（。ある（。から（。こそ（。、私たちは（。愛する（。人の（。笑顔（。を（。、色彩（。として（。抱き（。しめる（。ことが（。できる（。のですよ。"),
    ("electron", "Electron", "電子", "19th Century", "elektron (amber)", "A stable subatomic particle with a charge of negative electricity", "かつて（。人々（。が「琥（。珀（。エレクト）を（。擦（。って（。）」不思議（。な（。力を（。発見（。した（。とき（。の（。、驚（。き（。を（。その（。名に（。宿（。した（。、エナジーの（。最小（。の（。使者。"),
    ("nucleus", "Nucleus", "核、核心", "18th Century", "nux (nut)", "The central and most important part of an object, movement, or group, forming the basis for its activity and growth", "厚（。い（。殻を（。持（。った「木（。の実（。ナッツ）」の（。、一番（。奥底（。に（。守（。られ（。て（。いる（。、生命の（。全記憶（。を（。司（。る（。、不可侵の（。中心。"),
    ("isotope", "Isotope", "同位体", "20th Century", "isos (equal) + topos (place)", "Each of two or more forms of the same element that contain equal numbers of protons but different numbers of neutrons in their nuclei", "見た（。目や（。役割は（。少し（。違（。っても（。、「等（。しい（。アイソ）場所（。トポス）」を（。分け（。合う（。、魂の（。双子（。。（。お互い（。の（。違い（。を（。認（。め（。つつ（。、同（。じ（。本質（。を（。生き（。よう（。とする（。、連帯。"),
    ("fission", "Fission", "分裂、核分裂", "17th Century", "findere (to split)", "The action of dividing or splitting something into two or more parts", "一（。つに（。まとまって（。いた（。ものを（。「引（。き（。裂（。く（。フィス）」ことで（。、封印（。されて（。いた（。巨大な（。エナジーを（。、一気（。に（。解（。放（。する（。、破壊（。と（。誕生（。の（。儀式。"),
    ("fusion", "Fusion", "融合、核融合", "16th Century", "fundere (to pour, melt)", "The process or result of joining two or more things together to form a single entity", "バラバラの（。魂（。を（。「溶（。かし（。フューズ）合わせ（。）」、一（。筋（。の（。巨大な（。河（。として（。流（。し（。込む（。こと（。で（。、宇宙を（。も（。創り（。出す（。、究極の（。連帯。"),
    ("plasma", "Plasma", "プラズマ、血漿（けっしょう）", "19th Century", "plasma (something formed, molded)", "An ionized gas consisting of positive ions and free electrons in proportions resulting in more or less no overall electric charge, typically at very high temperatures from stars or fusion reactors", "物質（。の（。境界（。が（。溶（。け（。去（。り（。、ただ（。光（。り輝（。く「形（。を（。持（。たない（。流（。動体（。プラズマ）」に（。至（。った（。、宇宙の（。原初（。の（。混沌（。と（。生命。"),
    ("turbine", "Turbine", "タービン", "19th Century", "turbo (whirlwind, spinning object)", "A machine for producing continuous power in which a wheel or rotor, typically fitted with vanes, is made to revolve by a fast-moving flow of water, steam, gas, air, or other fluid", "目（。には（。見えない（。風（。や（。水の（。恵みを（。、「旋（。風（。ターボ）」の（。ような（。回転へと（。変（。換し（。、社会（。を（。動かす（。力（。へと（。変（。えゆく（。、エナジーの（。錬金術。"),
    ("engine", "Engine", "エンジン、機関、才略", "14th Century", "ingenium (natural talent, ingenuity)", "A machine with moving parts that converts power into motion", "単なる（。機械（。ではなく（。、内側から（。湧（。き（。上（。がる「天分（。インジェニュイティ）」を（。、世界（。を（。前進（。させる（。動力（。へと（。結（。晶（。させた（。、人間の（。智恵の（。結晶。"),
    ("combustion", "Combustion", "燃焼", "15th Century", "com- (together) + burere (to burn)", "The process of burning something", "蓄（。え（。られた（。エナジーを（。、酸素（。と（。「共に（。コン）一気に（。燃や（。し（。バス）尽くす」ことで（。、一瞬（。の（。閃光（。と（。力強（。い（。前進（。を（。産む（。、魂の（。点火。"),
    ("propellant", "Propellant", "推進剤、プロペラント", "19th Century", "pro- (forward) + pellere (to drive)", "A chemical substance used in the production of energy or gas to provide thrust", "自（。らを（。燃（。やし（。、自分を「前へと（。プロ）力強く（。押し出す（。ペル）」ための（。、孤独（。で（。潔（。い（。覚悟（。の（。エナジー。"),
    ("thrust", "Thrust", "推力、突く", "12th Century", "thrystan (to press, force, stab, thrust)", "Push something or someone suddenly or violently in the specified direction", "迷（。い（。を（。断（。ち（。切（。り（。、一点（。に向かって「突き（。スラスト）進む」ことで（。、重力（。という（。過去（。を（。振り切り（。、宇宙（。の（。深淵（。へと（。飛翔（。する（。ための（。、最初（。の（。力（。）。"),
    ("propulsion", "Propulsion", "推進、推進力", "17th Century", "pro- (forward) + pellere (to drive)", "The action of driving or pushing forward", "一度（。の（。衝撃（。に（。終わ（。らず（。、常に（。自分を「前へと（。プロ）駆（。り（。立て（。ペル）続ける」こと（。。（。何物（。にも（。屈（。しない（。、持続的（。な（。前進（。の（。意志。"),
    ("aerobic", "Aerobic", "有酸素の、エアロビクス", "19th Century", "aer (air) + bios (life)", "Relating to, involving, or requiring free oxygen", "世界（。を（。満（。たす「空気（。エア）」を（。、自ら（。の「命（。ビオス）」へと（。丁寧（。に（。取（。り（。込（。み（。、穏やか（。に（。、そして（。力強く（。燃（。え（。続ける（。、調和（。の（。生命（。）。", "「エアロビック（有酸素の）」な（。運動（。は（。、肺（。の（。隅々（。まで（。宇宙の（。エナジーを（。届（。けて（。くれ（。、あなた（。の（。細胞（。を（。一（。つ（。残（。さず（。祝福（。して（。くれる（。のですよ。"),
    ("anaerobic", "Anaerobic", "無酸素の", "19th Century", "an- (not) + aer (air) + bios (life)", "Relating to, involving, or requiring an absence of free oxygen", "空気（。に（。頼（。らず（。、自ら（。の（。内側に（。蓄（。え（。た（。爆発（。的な（。エナジーだけで（。、限界を（。突（。き（。破（。ろうとする（。、峻烈（。な（。挑戦（。の（。炎。"),
    ("calorie", "Calorie", "カロリー、熱量", "19th Century", "calor (heat)", "The energy needed to raise the temperature of 1 kilogram of water by 1 degree Celsius", "生命（。という（。小さな（。エンジン（。を（。回（。すための「熱（。カロール）」の（。単位（。。（。あなたが（。今日（。一歩（。歩（。く（。ために（。、宇宙（。が（。分（。けて（。くれ（。た（。、エナジー（。の（。ギフト。"),
    ("horsepower", "Horsepower", "馬力", "18th Century", "horse + power", "An imperial unit of power, equivalent to 550 foot-pounds per second", "かつて（。大地を（。力強く（。駆（。け（。抜け（。た（。「馬（。ホース）」の（。エナジーを（。基準に（。、人間が（。手（。に（。入れ（。た（。、物理的（。な（。成功（。の（。スケール。"),
    ("torque", "Torque", "トルク、回転力", "19th Century", "torquere (to twist)", "A twisting force that tends to cause rotation", "真っ直ぐ（。に（。進（。む（。のではなく（。、自らを「ねじ（。切（。る（。トルク）ようにして」回転（。させ（。、粘（。り（。強（。く（。困難（。を（。突破（。しようとする（。、内側（。の（。強力な（。粘り（。腰。"),
    ("potential", "Potential", "潜在力、可能性", "14th Century", "potis (powerful, able)", "Having or showing the capacity to become or develop into something in the future", "まだ（。目には（。見えない（。けれど（。、内側に（。力として（。秘（。め（。られて（。いる（。未来（。を（。爆発（。させる（。ための（。静かなる（。火種（。）。", "あなたの（。中（。に（。ある「ポテンシャル（無限の可能性）」を（。、誰（。にも（。否定（。させ（。ないで（。ください（。。（。それは（。まだ（。開（。いて（。いない（。だけの（。、宝石（。の（。箱（。の（。ような（。もの（。なの（。ですから。"),
    ("synergy", "Synergy", "シナジー、相乗効果", "17th Century", "sun- (together) + ergon (work)", "The interaction or cooperation of two or more organizations, substances, or other agents to produce a combined effect greater than the sum of their separate effects", "一人（。では（。決して（。成（。し遂（。げ（。られ（。ない（。巨大（。な（。仕事（。を（。、共（。に（。働く（。ことで（。、魔法（。のように（。何倍（。もの（。成果（。へと（。昇華（。させる（。、奇跡（。的な（。協力（。）。", "誰（。かと「シナジー（相乗効果）」を（。産（。み（。出す（。秘訣（。は（。、まず（。自分（。の（。弱さ（。を（。素直に（。認める（。勇気（。を（。持つ（。こと（。にある（。のです（。。（。そこ（。から（。真（。の（。結束（。が（。始まり（。ます。"),
    ("resilience", "Resilience", "弾力性、回復力", "17th Century", "re- (again) + salire (to leap, jump)", "The capacity to recover quickly from difficulties; toughness", "困難（。の（。圧力（。に（。押し潰（。されても（。、再び（。「高く（。リ）跳ね（。サリ）起きる」ことのできる（。、魂の（。しなやかな（。バネ。")
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
            word_id = f"{word_text.lower()}_energy"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "静止は死であり、運動こそが生命の証です。",
                    "example": f"The project gained significant {word_text} after the announcement.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["全てのエナジーは、一つの形から別の形へと姿を変えながら、宇宙を旅し続けています。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["kinetic", "thermal", "propellant", "aerobic", "anaerobic"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Energy & Motion (Cycle 31).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
