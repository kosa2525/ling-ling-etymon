import json
import re

words_data = [
    ("valley", "Valley", "谷", "13th Century", "vallis (valley)", "A low area of land", "二つの高い山に挟まれることで生じた謙虚な窪みに、豊かな水と生命が集まる豊穣の地。", "高い山を目指して疲れた時は、「バレー（谷）」の静けさの中で魂の休息を。"),
    ("canyon", "Canyon", "峡谷", "19th Century", "canon (tube)", "A deep gorge", "途方もない時間をかけて水滴が強固な大地を切り裂き、深くまで彫り込んだ偉大な地球の傷跡。", "どんなに固い壁も、情熱の川がいつかは「キャニオン（深い峡谷）」へと変えてくれます。"),
    ("gorge", "Gorge", "山峡、喉", "14th Century", "gorge (throat)", "A narrow valley", "まるで山が巨大な口を開けたかのような、急斜面で切り立った圧迫感と生命の喉笛。", "自然の中の「ゴージ（喉・渓谷）」を抜ける風の音は、地球そのものの呼吸です。"),
    ("ravine", "Ravine", "峡谷、深い谷", "18th Century", "rapere (to seize)", "A deep, narrow gorge", "水流によって強引に大地が「奪い取られ」、えぐり出されるように形成された急峻な亀裂。", "人生に突然「ラヴィーン（深い溝）」が現れても、それは新しい道を作るための試練です。"),
    ("plateau", "Plateau", "高原、台地", "18th Century", "plat (flat)", "An area of relatively level high ground", "険しい上昇を終え、たどり着いた先に広がる、重力から解放されたような高所の平穏無事。", "学習が「プラトー（停滞期）」に達しても焦らないで。そこは見晴らしの良い高原なのです。"),
    ("ridge", "Ridge", "尾根", "Old English", "hrycg (back of man or beast)", "A long narrow hilltop", "二つの異なる斜面を隔てる境界線として大地が背筋を伸ばし、空気を鋭く切り裂く背骨。", "「リッジ（山の背）」を歩く時は、絶景と同時に両側へ落ちる危険というスリルを楽しんで。"),
    ("cliff", "Cliff", "崖", "Old English", "clif (cliff, rock)", "A steep rock face", "海や陸地の端に突如として現れ、それ以上進むことを物理的かつ圧倒的に拒絶する垂直の断絶。", "絶望の「クリフ（崖）」の端に立たされた時こそ、魂が空へ舞い上がるチャンスかもしれません。"),
    ("precipice", "Precipice", "絶壁、危機", "16th Century", "praeceps (headlong)", "A very steep rock face or cliff", "一歩間違えれば「真っ逆さまに」落ちていく極限の境界線であり、重大な決断を迫る運命の淵。", "人生の「プレシピス（絶壁）」に立ったなら、恐怖に目を背けず、飛ぶ覚悟を決めましょう。"),
    ("crag", "Crag", "険しい岩山", "13th Century", "Unknown (Celtic)", "A steep or rugged cliff", "長い風化と浸食に耐え抜き、骨だけがむき出しになったように荒々しくそびえ立つ大地の老兵。", "彼の顔に刻まれた「クラッグ（険しい岩）」のような深いシワは、誇り高い戦いの歴史です。"),
    ("peak", "Peak", "頂上、尖峰", "16th Century", "pic (sharp point)", "The pointed top of a mountain", "全ての道が最後に収束し、それ以上登る場所のない完全なる孤立と最高の勝利が交差する「頂」。", "若さの「ピーク（頂点）」を過ぎても、山を降りる過程の夕焼けはまた格別に美しいのです。"),
    ("summit", "Summit", "頂上、最高首脳", "15th Century", "summus (highest)", "The highest point of a hill or mountain", "地球上で最も宇宙に近い場所であり、すべてを見下ろすことのできる物理的かつ精神的な最高到達点。", "リーダーたちが「サミット（頂上決戦）」で握手を交わす時、世界に新たな風が吹きます。"),
    ("crest", "Crest", "頂上、トサカ、波頭", "14th Century", "crista (tuft, plume)", "The top of a mountain or hill", "山の頂上や波の頂点に現れる「羽飾り」。存在が最も美しく、そして最も激しくエナジーを放つ瞬間。", "押し寄せる問題の波の「クレスト（波頭）」をサーフィンのように華麗に乗りこなして。"),
    ("meadow", "Meadow", "牧草地、草地", "Old English", "mæd (meadow)", "A piece of grassland", "樹木が入り込むことを許されず、草花だけが太陽の光を全身に浴びて乱舞する優しく開かれた広間。", "心が疲れた夜は、頭の中で満開の「メドウ（牧草地）」に寝転び、星を数えてください。"),
    ("pasture", "Pasture", "牧草地、放牧場", "13th Century", "pascere (to feed)", "Land covered with grass suitable for grazing", "動物たちの命を養うための「食卓」として神が用意した、尽きることのない緑の絨毯（じゅうたん）。", "厳しい都会の現実に疲れた動物たち（私たち）にも、時々は「パスチャー（放牧地）」が必要です。"),
    ("grove", "Grove", "小さな森、木立ち", "Old English", "graf (grove)", "A small wood, orchard", "大森林ほどの恐怖や闇を含まず、人間に親密で優しく調和の取れたスケールで存在する木の精が集う場所。", "古代の哲学者は、静かな「グローヴ（木立ち）」を歩きながら宇宙の真理を語り合いました。"),
    ("thicket", "Thicket", "茂み、藪", "Old English", "thiccet (dense group of trees)", "A dense group of bushes or trees", "幹や枝が複雑に絡み合い、「分厚い」壁をつくりだして外部からの視線を完全に遮断する秘密の隠れ家。", "人生の「シケット（複雑に絡み合った藪）」に迷い込んでも、強引に進めば必ず抜けられます。"),
    ("marsh", "Marsh", "沼地、湿地", "Old English", "mersc (marsh, swamp)", "An area of low-lying land which is flooded", "大地と水が曖昧に混ざり合い、確かな足場を奪う代わりに豊かな多様性を育む混沌とした生命の子宮。", "「マーシュ（沼地）」には足を取られますが、そこには泥の中でしか咲かない美しい花があります。"),
    ("swamp", "Swamp", "沼地、圧倒する", "17th Century", "Unknown (sponge, fungus)", "An area of waterlogged ground", "水が完全に土を支配し、歩みに応じて重く泥がまとわりつく、生命の活力と死の腐敗が同時に進行する場所。", "仕事の量に「スワンプ（圧倒されて沈む）」する前に、一度岸に上がって深呼吸を。"),
    ("bog", "Bog", "泥炭地、湿原", "16th Century", "bogach (soft, boggy)", "Wet muddy ground too soft to support", "長年にわたって蓄積された枯れ草が沈んで泥炭となり、足を踏み入れる者を柔らかく、だが確実に飲み込む深い穴。", "後悔という「ボグ（泥沼）」に足を踏み入れると、抜け出すのに途方もないエネルギーを使います。"),
    ("moor", "Moor", "荒野、ヒースの生い茂る荒れ地", "Old English", "mor (morass, swamp)", "A tract of open uncultivated upland", "強風が吹きすさび、華やかな花など一切育たないが、そこには孤独と誇りだけが延々と広がる厳しい荒野。", "ヒースクリフのように「ムーア（荒れ野）」に立ち、狂おしい愛を叫ぶ情熱も時には美しい。"),
    ("heath", "Heath", "荒れ地、ヒース", "Old English", "hæth (untilled land)", "An area of open uncultivated land", "痩せた（やせた）土地でもたくましく根を張り、紫の小さな花を咲かせる低木が群生する、荒涼とした美。"),
    ("tundra", "Tundra", "ツンドラ、凍原", "19th Century", "tundar (treeless mountain tract)", "A vast, flat, treeless Arctic region", "一年のほとんどを氷と雪に閉ざされながらも、短い夏には爆発的な生命力で花を咲かせる究極の耐久地帯。"),
    ("dune", "Dune", "砂丘", "18th Century", "dune (sand hill)", "A mound or ridge of sand", "風の意志によって毎日その姿を変え、永遠に同じ形を保つことのない金色の流動的な彫刻。"),
    ("oasis", "Oasis", "オアシス", "17th Century", "oasis (dwelling place)", "A fertile spot in a desert", "絶対的な死の空間（砂漠）に奇跡のように現れ、無条件で全ての渇きを癒やす命の幻影。"),
    ("mirage", "Mirage", "蜃気楼、幻影", "19th Century", "mirari (to look at, wonder)", "An optical illusion", "焦燥と渇望が生み出した脳のバグでありながら、あまりにも美しく「不思議な」希望を与える光のイタズラ。"),
    ("glacier", "Glacier", "氷河", "18th Century", "glacies (ice)", "A slowly moving mass of river of ice", "何万年という時間をかけ、地球の歴史そのものを凍結させながら押し流していく圧倒的に寡黙な氷の河。"),
    ("avalanche", "Avalanche", "雪崩", "18th Century", "avalance (descent)", "A mass of snow, ice, and rocks falling", "微小な限界点の突破が引き金となり、溜め込まれた全ての重みが一瞬にして「谷へ」崩落する大自然の破壊衝動。"),
    ("crater", "Crater", "クレーター、火口", "17th Century", "krater (mixing bowl)", "A large, bowl-shaped cavity", "天体同士の凄惨な衝突や大地の爆発によって形成された、星が身につけている「混ぜ鉢」のような巨大な傷跡。"),
    ("geyser", "Geyser", "間欠泉", "18th Century", "geysa (to gush)", "A hot spring in which water intermittently boils", "大地の奥底に鬱積（うっせき）したマグマの手による熱エネルギーが限界まで達し、「噴出」する熱狂のリズム。"),
    ("tide", "Tide", "潮、潮流", "Old English", "tid (time)", "The alternate rising and falling of the sea", "地球と月の無言の引力の対話によって、海が「時間」とともに正確に呼吸し続ける壮大なリズム。"),
    ("current", "Current", "水流、海流", "14th Century", "currere (to run)", "A body of water or air moving in a definite direction", "大海原や大気の中を「走る」ように突き進み、生命や気候を循環させる見えない地球の血管。"),
    ("ripple", "Ripple", "さざ波", "18th Century", "Unknown", "A small wave or series of waves", "静かな水面に一滴の出来事がもたらした微かな動揺が、丸い輪となってどこまでも優しく広がっていく現象。"),
    ("wave", "Wave", "波", "Old English", "wagian (to move back and forth)", "A long body of water curling into an arched form", "風のエネルギーを水が受け取り、その「揺れ動く」力を岸へと運んで最終的に白く砕け散らせる劇的な配達劇。"),
    ("surge", "Surge", "大波、急増", "15th Century", "surgere (to rise)", "A sudden powerful forward or upward movement", "通常の波の限界を超え、水や感情が抑えきれない力で一気に「跳ね上がる」暴力的なまでの急加速。"),
    ("abyss", "Abyss", "深淵、どん底", "14th Century", "a- + bussos (without bottom)", "A deep or seemingly bottomless chasm", "光が届くことを許されず、「底がない」と錯覚するほどの無限の深さで全てを飲み込んでしまう恐怖と神秘の暗黒。"),
    ("pebble", "Pebble", "小石", "Old English", "papolstan (pebble stone)", "A small stone made smooth and round", "川の流れと途方もない摩擦によって全ての角を削り取られ、丸く完璧で愛らしい姿になった大地の欠片。"),
    ("boulder", "Boulder", "大きな岩", "17th Century", "bulder (noise, roar)", "A large rock", "氷河や大洪水が「轟音を立てて」転がしてきた、人間の力では到底動かすことのできない威圧的な大地の置物。"),
    ("dust", "Dust", "ほこり、ちり", "Old English", "dust (dust, ashes)", "Fine, dry powder", "物質がこれ以上砕けない極小の粉末であり、最後は空へ舞い上がってすべてを平等の無に帰すための素材。"),
    ("ash", "Ash", "灰", "Old English", "æsce (ash)", "The powdery residue left after burning", "火という激しい情熱が全てを焼き尽くし、形あったものが魂を天空へ放ったのちに残される、静寂と浄化の結晶。"),
    ("ember", "Ember", "残り火", "Old English", "æmerge (embers)", "A small piece of burning or glowing coal", "炎は消えても、自分自身の内側に強い熱を持ったまま静かに「輝き」続ける、執念のごとき見えない情熱。")
]

words = []
for item in words_data:
    meaning1 = "known origin"
    root1 = item[4]
    w = {
        "id": f"{item[0]}_nature",
        "word": item[0],
        "meaning": item[2],
        "era": item[3],
        "etymology": {
            "components": [item[4]],
            "original_statement": f"From {item[3]} {item[4]}."
        },
        "concept": item[5] + f" ({item[6]})",
        "thinking": item[6],
        "aftertaste": item[7] if len(item) > 7 else "深い地球の営みに心を委ねてみよう。",
        "example": f"We looked out over the vast {item[0]}.",
        "deep_dive": {
            "roots": [{"term": root1, "meaning": meaning1}],
            "points": ["自然の中に自らの感情や人生を映し出すメタファーの世界。"]
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
    print(f"Success: Added {added} words. Theme: Nature (Cycle 7).")
else:
    print("Error parsing data.js")
