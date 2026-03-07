import json
import re
import os
from datetime import datetime

# 45 real English words related to cosmos & nature phenomena
# Must match strict JSON schema for the existing objects

word_batch = [
    {
        "id": "zenith",
        "word": "Zenith",
        "meaning": "天頂、頂点、絶頂",
        "era": "14th Century Middle English/Arabic samto",
        "etymology": {
            "components": ["samt (path)"],
            "original_statement": "From Arabic samt (path, road), originally in samt ar-ras (the path over the head)."
        },
        "concept": "The point exactly above (頭上の道の極み)",
        "thinking": "星や太陽が空で達する最も高い場所。それが転じて人の人生や文明の絶頂期を指すようになりました。光が最も強大になる瞬間。",
        "aftertaste": "全てが見渡せる場所。",
        "example": "He reached the zenith of his career.",
        "deep_dive": {
            "roots": [{"term": "samt", "meaning": "path"}],
            "points": ["天文学由来の言葉が比喩的に使われる典型例です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "nadir",
        "word": "Nadir",
        "meaning": "天底、どん底",
        "era": "15th Century Middle French/Arabic nadir",
        "etymology": {
            "components": ["nazir (opposite)"],
            "original_statement": "From Arabic nazir as-samt (opposite the zenith)."
        },
        "concept": "The lowest point (最下点)",
        "thinking": "天球上で観測者の真下に位置する点。希望や力が完全に失われた最も暗い時期。しかし、ここからは上昇するしかない地点でもあります。",
        "aftertaste": "暗闇の底で、重力に逆らう準備をする。",
        "example": "Company profits have reached their nadir.",
        "deep_dive": {
            "roots": [{"term": "nazir", "meaning": "opposite"}],
            "points": ["zenithと対をなす重要な概念です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "horizon",
        "word": "Horizon",
        "meaning": "地平線、水平線、視野",
        "era": "14th Century Old French/Greek horizein",
        "etymology": {
            "components": ["horos (boundary)", "-izein (to limit)"],
            "original_statement": "From Greek horizein (to bound, limit), from horos (boundary, landmark)."
        },
        "concept": "The bounding line (視界の境界線)",
        "thinking": "空と大地の境界線であり、人間の認識の限界。そこから転じて、可能性や知識の広がりを意味します。常に一歩先へ進もうとする探求の象徴。",
        "aftertaste": "線の向こう側に思いを馳せる。",
        "example": "Broaden your horizons by exploring new fields.",
        "deep_dive": {
            "roots": [{"term": "horos", "meaning": "boundary"}],
            "points": ["水平（horizontal）の語源でもあります。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "eclipse",
        "word": "Eclipse",
        "meaning": "日食、月食、影を落とすこと、力を失うこと",
        "era": "13th Century Old French/Greek ekleipsis",
        "etymology": {
            "components": ["ek- (out)", "leipein (to leave)"],
            "original_statement": "From Greek ekleipsis (a forsaking, quitting, failing), from ek- (out) + leipein (to leave)."
        },
        "concept": "A quitting or failing of light (光が去ること)",
        "thinking": "日常の当然の光が奪われる現象は、古代の人々に恐れられましたが、同時に宇宙の規則的なリズムでもあります。",
        "aftertaste": "一時の影。だが光は必ず戻る。",
        "example": "The moon passed into an eclipse.",
        "deep_dive": {
            "roots": [{"term": "leipein", "meaning": "leave"}],
            "points": ["『力や名声が衰える』という意味への拡張が面白い単語です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "nebula",
        "word": "Nebula",
        "meaning": "星雲",
        "era": "17th Century Latin",
        "etymology": {
            "components": ["nebula (mist, little cloud)"],
            "original_statement": "Directly from Latin nebula (mist, vapor, cloud)."
        },
        "concept": "A hazy cloud of gas and dust (星々のゆりかご)",
        "thinking": "かすんだ霧のような天体。新しい星が生まれる場所であり、また星が寿命を終えた残骸でもある、宇宙の生と死のサイクルが可視化された空間。",
        "aftertaste": "霞のなかに隠された星の胎動。",
        "example": "The Orion Nebula is visible to the naked eye.",
        "deep_dive": {
            "roots": [{"term": "nebh-", "meaning": "cloud"}],
            "points": ["ラテン語の雲から来ていますが、星の誕生という意味が内包されました。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "galaxy",
        "word": "Galaxy",
        "meaning": "銀河、華々しい集まり",
        "era": "14th Century Old French/Greek galaxias",
        "etymology": {
            "components": ["gala (milk)"],
            "original_statement": "From Greek galaxias (milky), referring to the Milky Way."
        },
        "concept": "The milky circle (乳の道)",
        "thinking": "夜空を流れるかすかに白い星の帯を、古代の人々は神々の「乳」と見立てました。現在では数百億の星の集団を指す巨大なスケールの言葉となっています。",
        "aftertaste": "夜空にこぼされた神話の痕跡。",
        "example": "Our solar system is located in the Milky Way galaxy.",
        "deep_dive": {
            "roots": [{"term": "gala", "meaning": "milk"}],
            "points": ["ラクトース（lactose）などの『乳』に関する言葉と語源を共有します。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "meteor",
        "word": "Meteor",
        "meaning": "流星、隕石",
        "era": "15th Century Middle French/Greek meteoron",
        "etymology": {
            "components": ["meta- (beyond)", "aeirein (to lift)"],
            "original_statement": "From Greek meteoron (thing high up), from meta- (over, beyond) + aeirein (to lift)."
        },
        "concept": "Suspended high in the air (高く持ち上げられたもの)",
        "thinking": "元々は空中の現象全般（雨や雪なども含む）を指していました。気象学（meteorology）という言葉にその名残があります。一瞬の輝きで空を駆ける石。",
        "aftertaste": "消えゆく閃光が、網膜の奥に焼き付く。",
        "example": "We saw a brilliant meteor streak across the sky.",
        "deep_dive": {
            "roots": [{"term": "meta-", "meaning": "beyond"}],
            "points": ["流星としての意味に限定されたのは後代のことです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "comet",
        "word": "Comet",
        "meaning": "彗星",
        "era": "12th Century Old English/Greek kometes",
        "etymology": {
            "components": ["kome (hair of the head)"],
            "original_statement": "From Greek kometes (long-haired), referring to the tail of the comet."
        },
        "concept": "The long-haired star (髪を長く伸ばした星)",
        "thinking": "尻尾を引くように現れる彗星の姿を、古代のギリシャ人は「長い髪の毛をなびかせている」と表現しました。畏怖の対象でもありました。",
        "aftertaste": "氷と塵がなびかせる、宇宙の長い髪。",
        "example": "Halley's Comet returns every 76 years.",
        "deep_dive": {
            "roots": [{"term": "kome", "meaning": "hair"}],
            "points": ["星の尾を髪に例えるという詩的な語源を持っています。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "asteroid",
        "word": "Asteroid",
        "meaning": "小惑星",
        "era": "19th Century Greek asteroeides",
        "etymology": {
            "components": ["aster (star)", "-oid (form, resembling)"],
            "original_statement": "From Greek asteroeides (star-like), from aster (star) + eidos (form, shape)."
        },
        "concept": "Star-like (星のような存在)",
        "thinking": "天体望遠鏡で見たときに、惑星のような「円盤」ではなく、恒星のような「点」にしか見えなかったため、星に似たものと名付けられました。",
        "aftertaste": "完全な星にはなれなかった、孤独な岩塊。",
        "example": "The asteroid belt lies between Mars and Jupiter.",
        "deep_dive": {
            "roots": [{"term": "aster", "meaning": "star"}],
            "points": ["android（人間に似たもの）等の -oid と同じ接尾辞です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "orbit",
        "word": "Orbit",
        "meaning": "軌道、活動範囲",
        "era": "14th Century Latin orbita",
        "etymology": {
            "components": ["orbis (circle, ring)"],
            "original_statement": "From Latin orbita (track, rut, path), from orbis (ring, circle, wheel)."
        },
        "concept": "The circular path (円形の轍)",
        "thinking": "引力に捉えられた天体が描く終わりのない円環。それは支配であり、同時に秩序の証でもあります。",
        "aftertaste": "見えない糸で引かれた、永遠の輪舞。",
        "example": "The satellite went into orbit around the Earth.",
        "deep_dive": {
            "roots": [{"term": "orbis", "meaning": "circle"}],
            "points": ["馬車の轍（わだち）という意味が、天体の軌道へと進化しました。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "gravity",
        "word": "Gravity",
        "meaning": "重力、引力、重大さ、真面目さ",
        "era": "16th Century Middle French/Latin gravitas",
        "etymology": {
            "components": ["gravis (heavy)"],
            "original_statement": "From Latin gravitas (weight, heaviness, dignity), from gravis (heavy)."
        },
        "concept": "The state of being heavy or serious (重さ、あるいはその威厳)",
        "thinking": "物理的な「重さ」だけでなく、態度の「重々しさ（真面目さ）」や事態の「重大さ」といったメンタルな重さまで表現する、人間の深い認識を反映する言葉。",
        "aftertaste": "全てを惹きつける、逃れられない法則。",
        "example": "The law of gravity holds the universe together.",
        "deep_dive": {
            "roots": [{"term": "gravis", "meaning": "heavy"}],
            "points": ["grave（深刻な）とも同根。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "vacuum",
        "word": "Vacuum",
        "meaning": "真空、空白",
        "era": "16th Century Latin",
        "etymology": {
            "components": ["vacuus (empty)"],
            "original_statement": "Directly from Latin vacuum (an empty space), neuter of vacuus (empty)."
        },
        "concept": "Empty space (何もない空間)",
        "thinking": "物質が一切存在しない空間。しかし現代物理学では、真空は単なる「無」ではなく、エネルギーが沸き立つダイナミックな場であるとされています。完全なる不在は、あらゆる存在の背景です。",
        "aftertaste": "無という名のキャンバス。",
        "example": "Sound cannot travel in a vacuum.",
        "deep_dive": {
            "roots": [{"term": "vac-", "meaning": "empty"}],
            "points": ["vacant（空の）や vacation（休暇で空っぽの時間）と同じ源流です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "stellar",
        "word": "Stellar",
        "meaning": "星の、見事な、傑出した",
        "era": "17th Century Late Latin stellaris",
        "etymology": {
            "components": ["stella (star)"],
            "original_statement": "From Late Latin stellaris (pertaining to a star), from stella (star)."
        },
        "concept": "Of or relating to stars (星に属するもの)",
        "thinking": "恒星のような自ら輝く存在であることを意味します。「星のように傑出した」という称賛のニュアンスを持つのは、人間の光への憧れを示しています。",
        "aftertaste": "自ら燃える者の放つ、強烈な輝き。",
        "example": "She gave a stellar performance in her debut film.",
        "deep_dive": {
            "roots": [{"term": "ster-", "meaning": "star"}],
            "points": ["interstellar（恒星間の）という派生も有名です。"]
        },
        "part_of_speech": "adjective"
    },
    {
        "id": "lunar",
        "word": "Lunar",
        "meaning": "月の",
        "era": "15th Century Latin lunaris",
        "etymology": {
            "components": ["luna (moon)"],
            "original_statement": "From Latin lunaris (of the moon), from luna (moon)."
        },
        "concept": "Pertaining to the moon (月にまつわる)",
        "thinking": "夜の支配者であり、潮の満ち引きや生命のリズムを刻む月の属性。狂気（lunatic）という言葉もここから生まれるほど、人の深層に影響を与えると考えられました。",
        "aftertaste": "柔らかな光と、潮騒の記憶。",
        "example": "We observed the lunar eclipse last night.",
        "deep_dive": {
            "roots": [{"term": "leuk-", "meaning": "light"}],
            "points": ["輝くものを意味する印欧語根から派生。"]
        },
        "part_of_speech": "adjective"
    },
    {
        "id": "solar",
        "word": "Solar",
        "meaning": "太陽の",
        "era": "15th Century Latin solaris",
        "etymology": {
            "components": ["sol (sun)"],
            "original_statement": "From Latin solaris (of the sun), from sol (sun)."
        },
        "concept": "Pertaining to the sun (太陽の属性)",
        "thinking": "生命の源であり、全ての惑星を従える中心。絶対的な熱と光の象徴であり、エネルギーの究極の供給源を表します。",
        "aftertaste": "万物を照らす、不屈の燃焼。",
        "example": "Solar power is a key renewable energy source.",
        "deep_dive": {
            "roots": [{"term": "sawel-", "meaning": "sun"}],
            "points": ["ヘリオス（ギリシャ語）とも遠い親戚関係にあります。"]
        },
        "part_of_speech": "adjective"
    },
    {
        "id": "cosmos",
        "word": "Cosmos",
        "meaning": "宇宙、秩序",
        "era": "17th Century Greek kosmos",
        "etymology": {
            "components": ["kosmos (order, good order, ornament)"],
            "original_statement": "From Greek kosmos (order, good order, ornament), which Pythagoras is said to have applied to the universe."
        },
        "concept": "The universe as an ordered system (秩序ある美しい体系としての宇宙)",
        "thinking": "単なる空間（space）や宇宙全体（universe）ではなく、そこに「美しい調和と法則がある」とみなす古代ギリシャ人の世界観が込められています。",
        "aftertaste": "混沌すらも取り込んだ、完璧な調和。",
        "example": "The intricate laws of the cosmos fascinated him.",
        "deep_dive": {
            "roots": [{"term": "kosmos", "meaning": "order"}],
            "points": ["化粧品（cosmetics）も同じく『整える・美しくする』という語源を持ちます。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "universe",
        "word": "Universe",
        "meaning": "宇宙、全世界",
        "era": "14th Century Old French/Latin universus",
        "etymology": {
            "components": ["uni- (one)", "versus (turned)"],
            "original_statement": "From Latin universum (all things, as a whole), from universus (combined into one, whole), from uni- (one) + versus (turned)."
        },
        "concept": "Turned into one (一つにまとめられたもの)",
        "thinking": "無数の星や銀河、時間も空間も、その全てが「一つの全体へと向けられている（向かっている）」という壮大な包括性を示す言葉。",
        "aftertaste": "無限に広がりながらも、それは常に『一つ』。",
        "example": "The universe is expanding at an accelerating rate.",
        "deep_dive": {
            "roots": [{"term": "vertere", "meaning": "to turn"}],
            "points": ["文字通り『一つに向かっている』という意味がすべてを内包します。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "dimension",
        "word": "Dimension",
        "meaning": "寸法、次元、側面",
        "era": "14th Century Latin dimensio",
        "etymology": {
            "components": ["dis- (apart)", "metiri (to measure)"],
            "original_statement": "From Latin dimensionem (a measuring), from dimensus, past participle of dimetiri (to measure out), from dis- (apart) + metiri (to measure)."
        },
        "concept": "Measuring out (測り出された広がり)",
        "thinking": "単なる大きさだけでなく、物事を測るための「軸」。一次元、二次元、三次元といった物理的な軸から、思考の新たな「側面」まで、世界をどう測るかという枠組み。",
        "aftertaste": "新しい切り口が、見えなかった世界を現す。",
        "example": "Adding time as the fourth dimension changes the equation.",
        "deep_dive": {
            "roots": [{"term": "me-", "meaning": "to measure"}],
            "points": ["meter（メートル）や metric（測定の）と同根。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "aurora",
        "word": "Aurora",
        "meaning": "オーロラ、極光、暁",
        "era": "14th Century Latin Aurora",
        "etymology": {
            "components": ["aurora (dawn)"],
            "original_statement": "From Latin Aurora (the goddess of dawn), conceptually meaning the dawn or the morning light."
        },
        "concept": "The goddess of dawn / light at the poles (夜明けの女神の光)",
        "thinking": "本来は夜が明けるときの光の筋を指し、ローマ神話の女神の名でもありました。高緯度地域で夜空に揺らめく磁気嵐の光も、神秘的な夜明けに見立てられました。",
        "aftertaste": "空を漂う、女神の衣の切れ端。",
        "example": "We traveled to Iceland to see the aurora borealis.",
        "deep_dive": {
            "roots": [{"term": "aus-", "meaning": "to shine"}],
            "points": ["east（東）もこの『光る方向』という語源から来ています。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "twilight",
        "word": "Twilight",
        "meaning": "夕暮れ、薄明、衰退期",
        "era": "14th Century Middle English twilght",
        "etymology": {
            "components": ["twi- (half/two)", "light"],
            "original_statement": "From Middle English twilght, from twi- (half, double, two) + light."
        },
        "concept": "Half-light (半分だけの光)",
        "thinking": "昼と夜の間の曖昧な時間。光と闇が混ざり合う境界の時であり、転じて文明や人生の終わりの静かな衰退期をも意味します。",
        "aftertaste": "昼間が溶け出し、夜に染まる束の間。",
        "example": "We sat on the porch in the twilight.",
        "deep_dive": {
            "roots": [{"term": "dwo-", "meaning": "two"}],
            "points": ["二つの間、あるいは半分の光という美しい成り立ちです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "dawn",
        "word": "Dawn",
        "meaning": "夜明け、始まり、(事実が)わかり始める",
        "era": "12th Century Old English dagian",
        "etymology": {
            "components": ["dagian (to become day)"],
            "original_statement": "From Old English dagian (to become day), related to dæg (day)."
        },
        "concept": "To become day (一日が生まれること)",
        "thinking": "真っ暗な夜から最初の一筋の光が差し込む瞬間。新しい時代や出来事の「幕開け」、そして突然真実を「悟る」瞬間にも使われます。",
        "aftertaste": "冷たい空気が、青白い光に温度を借る。",
        "example": "The reality of the situation began to dawn on her.",
        "deep_dive": {
            "roots": [{"term": "agh-", "meaning": "a day"}],
            "points": ["英語の day（日）と深く結びついています。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "dusk",
        "word": "Dusk",
        "meaning": "夕暮れ、薄暗がり",
        "era": "12th Century Old English dox",
        "etymology": {
            "components": ["dox (dark, swarthy)"],
            "original_statement": "From Old English dox (dark, swarthy, obscure), evolved into meaning the darkening stage of twilight."
        },
        "concept": "The darkening stage (次第に暗闇へと沈みゆくさま)",
        "thinking": "光が終わろうとする時間帯。twilightよりも少し暗く、夜が完全に支配を始める直前の、輪郭が全てぼやけていく時間帯を指します。",
        "aftertaste": "すべての形が、影へと溶けてゆく。",
        "example": "The streetlights flickered on at dusk.",
        "deep_dive": {
            "roots": [{"term": "dus-", "meaning": "bad, dark"}],
            "points": ["本来は『色が黒っぽい』という形容詞でした。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "equinox",
        "word": "Equinox",
        "meaning": "昼夜平分時(春分・秋分)",
        "era": "14th Century Old French/Latin aequinoctium",
        "etymology": {
            "components": ["aequus (equal)", "nox (night)"],
            "original_statement": "From Latin aequinoctium (equality of night and day), from aequus (equal) + nox (night)."
        },
        "concept": "Equal night (昼と夜の長さが等しくなる時)",
        "thinking": "太陽が赤道の真上を通過し、世界中で昼と夜が同じ長さになる天文学的瞬間。自然界の完璧なバランス、そして季節の大きな転換点。",
        "aftertaste": "一瞬だけ訪れる、光と影の完璧な均衡。",
        "example": "The vernal equinox marks the beginning of spring.",
        "deep_dive": {
            "roots": [{"term": "aequus", "meaning": "equal"}],
            "points": ["noc-, nox- は夜を意味し、nocturnal（夜行性の）と同根。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "solstice",
        "word": "Solstice",
        "meaning": "至、至点(夏至・冬至)",
        "era": "13th Century Old French/Latin solstitium",
        "etymology": {
            "components": ["sol (sun)", "sistere (to stand still)"],
            "original_statement": "From Latin solstitium (point at which the sun seems to stand still), from sol (sun) + sistere (to come to a stop, stand still)."
        },
        "concept": "The sun stands still (太陽が立ち止まる時)",
        "thinking": "太陽の高度が最も高く（または低く）なり、日の長さの増減が反転する地点。「太陽がそこで一旦停止して引き返す」という古代人の観察が込められています。",
        "aftertaste": "天頂での停止。反転の合図。",
        "example": "The summer solstice is the longest day of the year.",
        "deep_dive": {
            "roots": [{"term": "sta-", "meaning": "to stand"}],
            "points": ["stopやstandと同じ語根から派生した言葉です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "constellation",
        "word": "Constellation",
        "meaning": "星座、光り輝く集まり",
        "era": "14th Century Old French/Latin constellatio",
        "etymology": {
            "components": ["com- (together)", "stella (star)"],
            "original_statement": "From Latin constellationem (set with stars), from com- (together) + stella (star)."
        },
        "concept": "Stars acting together (共に並ぶ星々)",
        "thinking": "無秩序に散らばる星々を線で結び、そこに物語や形を見出した人間の想像力の結晶。バラバラの情報を結びつけて意味を引き出すことの比喩にもなります。",
        "aftertaste": "点と点を結ぶ、人間の想像力の糸。",
        "example": "Orion is one of the most recognizable constellations.",
        "deep_dive": {
            "roots": [{"term": "stella", "meaning": "star"}],
            "points": ["美しい人物や才能のある人々の集団を指す時にもおしゃれに使われます。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "planetary",
        "word": "Planetary",
        "meaning": "惑星の、地球規模の、放浪する",
        "era": "16th Century Latin planetarius",
        "etymology": {
            "components": ["planeta (wandering star)"],
            "original_statement": "From Latin planetarius (pertaining to planets), from Greek planetes (wanderer)."
        },
        "concept": "Of the wanderers (放浪者に関する)",
        "thinking": "恒星のように空に固定されず、独自の軌道で動く星を彼らは「迷子」「放浪者」と呼びました。現在ではそのスケールの大きさから「地球規模の」という意味を帯びています。",
        "aftertaste": "夜空を巡る、永遠の旅人。",
        "example": "Climate change is a planetary crisis.",
        "deep_dive": {
            "roots": [{"term": "pele-", "meaning": "flat, to spread"}],
            "points": ["語源は『ふらふらと広がる・歩き回る』というイメージから来ています。"]
        },
        "part_of_speech": "adjective"
    },
    {
        "id": "celestial",
        "word": "Celestial",
        "meaning": "天職の、天体の、神聖な",
        "era": "14th Century Old French/Latin caelestis",
        "etymology": {
            "components": ["caelum (heaven, sky)"],
            "original_statement": "From Latin caelestis (heavenly, pertaining to the sky), from caelum (heaven, sky)."
        },
        "concept": "Heavenly (天に属するもの)",
        "thinking": "地表（terrestrial）から見上げた美しい空にあるものすべてに冠される形容詞。物理的な宇宙空間だけでなく、宗教的・精神的な「天上世界」の高潔さも示唆します。",
        "aftertaste": "見上げた先にある、手の届かぬ静寂。",
        "example": "Telescopes help us study celestial bodies.",
        "deep_dive": {
            "roots": [{"term": "kaid-", "meaning": "bright, clear"}],
            "points": ["『澄み切ったもの』という古い印欧語根が背景にあります。"]
        },
        "part_of_speech": "adjective"
    },
    {
        "id": "terrestrial",
        "word": "Terrestrial",
        "meaning": "地球の、地上の、陸生の",
        "era": "15th Century Latin terrestris",
        "etymology": {
            "components": ["terra (earth, land)"],
            "original_statement": "From Latin terrestris (of the earth, on land), from terra (earth)."
        },
        "concept": "Of the earth (大地に属するもの)",
        "thinking": "空高く光る者たち（celestial）に対して、我々が重力によって縛り付けられているこの泥と岩の球体（terra）に根付くもの。土の匂いがする言葉。",
        "aftertaste": "足の裏で確かに感じる、大地の鼓動。",
        "example": "Mars is a terrestrial planet like Earth.",
        "deep_dive": {
            "roots": [{"term": "ters-", "meaning": "to dry"}],
            "points": ["terraの語源は『乾いた土地』であり、水（海）と対比されていました。"]
        },
        "part_of_speech": "adjective"
    },
    {
        "id": "atmosphere",
        "word": "Atmosphere",
        "meaning": "大気、雰囲気、環境",
        "era": "17th Century Modern Latin atmosphaera",
        "etymology": {
            "components": ["atmos (vapor)", "sphaira (sphere)"],
            "original_statement": "From Modern Latin atmosphaera, from Greek atmos (vapor, steam) + sphaira (sphere)."
        },
        "concept": "The sphere of vapor (蒸気の球体)",
        "thinking": "地球の周囲を覆うガスの層ですが、日常的には「部屋の空気」や「人や場所が醸し出すムード」を指すために使われます。私たちは見えない空気に常に浸っています。",
        "aftertaste": "呼吸と共に、空間の感情まで吸い込む。",
        "example": "The old library has a very peaceful atmosphere.",
        "deep_dive": {
            "roots": [{"term": "awet-", "meaning": "to blow"}],
            "points": ["物理的な気圏という専門用語が、日常の感情空間を表現するようになりました。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "stratosphere",
        "word": "Stratosphere",
        "meaning": "成層圏、最上層、最高段階",
        "era": "20th Century French stratosphère",
        "etymology": {
            "components": ["stratus (spread out, layer)", "sphere"],
            "original_statement": "Coined by French meteorologist Teisserenc de Bort from Latin stratus (layer) + -sphere."
        },
        "concept": "The layered sphere (重なり合う層の圏)",
        "thinking": "大気が層状に安定し、気象擾乱がほとんどない静かな高空。そこから転じて、「手の届かない超高レベルの状態（価格や名声）」の比喩としても使われます。",
        "aftertaste": "乱気流を超越した、冷たく静かな高度。",
        "example": "Real estate prices in the city have entered the stratosphere.",
        "deep_dive": {
            "roots": [{"term": "stere-", "meaning": "to spread"}],
            "points": ["ストリート（street / 舗装された層）と同根です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "troposphere",
        "word": "Troposphere",
        "meaning": "対流圏",
        "era": "20th Century French troposphère",
        "etymology": {
            "components": ["tropos (turn, change)", "sphere"],
            "original_statement": "Coined by Teisserenc de Bort from Greek tropos (turn, turn of direction) + -sphere, referring to upper convective currents."
        },
        "concept": "The turning sphere (かき混ぜられる変化の圏)",
        "thinking": "私たち生き物が呼吸し、雲ができ、雨が降り、風が渦巻く、最もドラマチックで変化（tropos）に富んだ層。すべての地球上のドラマはここで起きます。",
        "aftertaste": "混ざり合う大気、生命の舞台。",
        "example": "Weather phenomena occur primarily in the troposphere.",
        "deep_dive": {
            "roots": [{"term": "trep-", "meaning": "to turn"}],
            "points": ["熱帯（tropics）も同じ『回転・変化』の語源を持っています。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "ionosphere",
        "word": "Ionosphere",
        "meaning": "電離層",
        "era": "20th Century English",
        "etymology": {
            "components": ["ion (going)", "sphere"],
            "original_statement": "Coined by Robert Watson-Watt from 'ion' + 'sphere', describing the upper region ionized by solar radiation."
        },
        "concept": "The sphere of wandering particles (彷徨う粒子の圏)",
        "thinking": "紫外線によって空気の分子が電気を帯びた粒子（イオン）に分かれる層。ここで電波が反射されるおかげで、人類は地球の裏側と通信することができました。",
        "aftertaste": "目に見えない波が、空の鏡で反射する。",
        "example": "Radio waves can bounce off the ionosphere.",
        "deep_dive": {
            "roots": [{"term": "ei-", "meaning": "to go"}],
            "points": ["イオンの語源はギリシャ語の『行くもの・歩き回るもの』です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "mesosphere",
        "word": "Mesosphere",
        "meaning": "中間圏",
        "era": "20th Century English",
        "etymology": {
            "components": ["mesos (middle)", "sphere"],
            "original_statement": "Coined from Greek mesos (middle) + sphere."
        },
        "concept": "The middle sphere (真ん中の圏)",
        "thinking": "成層圏と熱圏の間に挟まれた、極寒の層。大気圏の中で最も温度が低く、ここで多くの流星（メテオ）が燃え尽きます。地球の防護盾の最前線。",
        "aftertaste": "燃え尽きる星屑たちを受け止める、冷たい壁。",
        "example": "Meteors burn up when they enter the mesosphere.",
        "deep_dive": {
            "roots": [{"term": "medhyo-", "meaning": "middle"}],
            "points": ["メソポタミア（真ん中の川の土地）のメソと同根です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "exosphere",
        "word": "Exosphere",
        "meaning": "外気圏",
        "era": "20th Century English",
        "etymology": {
            "components": ["exo- (outside)", "sphere"],
            "original_statement": "Coined from Greek exo- (outside, outer) + sphere."
        },
        "concept": "The outermost sphere (一番外側の圏)",
        "thinking": "大気が極端に薄くなり、空気の分子同士が衝突することなく、一部は重力を振り切って宇宙へ逃げていく脱出限界線。地球と宇宙の曖昧な溶け合い。",
        "aftertaste": "分子たちが、静かに宇宙の海へ漕ぎ出す。",
        "example": "Satellites orbit Earth in the exosphere.",
        "deep_dive": {
            "roots": [{"term": "eghs", "meaning": "out"}],
            "points": ["exit や exotic など、外へ向かう言葉と共通。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "lithosphere",
        "word": "Lithosphere",
        "meaning": "岩石圏、リソスフェア",
        "era": "19th Century German Lithosphäre",
        "etymology": {
            "components": ["lithos (stone)", "sphere"],
            "original_statement": "From Greek lithos (stone) + sphere, denoting the rigid outer part of the earth."
        },
        "concept": "The stone sphere (石の球体)",
        "thinking": "地球の固い外殻を示す言葉。地殻とマントル最上部のプレートのこと。私たちの文明はこの硬い岩石の上に建てられています。",
        "aftertaste": "途方もない圧力を秘めた、沈黙の岩盤。",
        "example": "Tectonic plates are fragments of the lithosphere.",
        "deep_dive": {
            "roots": [{"term": "lithos", "meaning": "stone"}],
            "points": ["モノリス（monolith）やリチウム（lithium）と同根。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "hydrosphere",
        "word": "Hydrosphere",
        "meaning": "水圏",
        "era": "19th Century English",
        "etymology": {
            "components": ["hydro- (water)", "sphere"],
            "original_statement": "From Greek hydor (water) + sphere, encompassing all the earth's water."
        },
        "concept": "The water sphere (水の球界)",
        "thinking": "海、川、湖、地下水、果ては雲の中の水蒸気まで。地球の表面を覆い、生命の維持に不可欠な絶えず循環する液体の層。",
        "aftertaste": "常に姿を変えながら、地球を潤す脈動。",
        "example": "The oceans make up the vast majority of the hydrosphere.",
        "deep_dive": {
            "roots": [{"term": "wed-", "meaning": "water, wet"}],
            "points": ["hydration（水分補給）と同じ由来。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "biosphere",
        "word": "Biosphere",
        "meaning": "生物圏",
        "era": "19th Century German Biosphäre",
        "etymology": {
            "components": ["bios (life)", "sphere"],
            "original_statement": "Coined by geologist Eduard Suess from Greek bios (life) + sphere."
        },
        "concept": "The life sphere (生命の広がる層)",
        "thinking": "大気圏、水圏、岩石圏が交わるごくわずかな薄い膜の中で、微生物から人間までの全生命がひしめき合っている。奇跡的に複雑なネットワーク。",
        "aftertaste": "地球という球体を包む、極薄き呼吸の層。",
        "example": "Human activities are profoundly altering the biosphere.",
        "deep_dive": {
            "roots": [{"term": "gwei-", "meaning": "to live"}],
            "points": ["biology（生物学）と同じ根です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "cryosphere",
        "word": "Cryosphere",
        "meaning": "雪氷圏",
        "era": "20th Century English",
        "etymology": {
            "components": ["kryos (cold, frost)", "sphere"],
            "original_statement": "From Greek kryos (icy cold, frost) + sphere."
        },
        "concept": "The icy sphere (凍れる球界)",
        "thinking": "氷河、氷山、永久凍土など、水が固体として存在するエリア。地球の温度を調節する巨大な鏡であり、気候変動を一番敏感に察知するセンサーです。",
        "aftertaste": "何万年もの時間を閉じ込めた、白い記憶の貯蔵庫。",
        "example": "Melting of the cryosphere contributes to sea-level rise.",
        "deep_dive": {
            "roots": [{"term": "kru-", "meaning": "frozen"}],
            "points": ["cryogenics（極低温学）や crystal（結晶/氷）と同源です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "hemisphere",
        "word": "Hemisphere",
        "meaning": "半球",
        "era": "14th Century Latin hemisphaerium",
        "etymology": {
            "components": ["hemi- (half)", "sphere"],
            "original_statement": "From Late Latin hemisphaerium, from Greek hemisphairion, from hemi- (half) + sphaira (sphere)."
        },
        "concept": "Half of a sphere (球の半分)",
        "thinking": "地球を北と南、あるいは東と西に二分するだけでなく、人間の脳の右半球・左半球のようにも用いられます。二元性を現す幾何学的な表現。",
        "aftertaste": "丸い世界を分かつ、見えない一本の刃。",
        "example": "The Northern Hemisphere experiences summer in July.",
        "deep_dive": {
            "roots": [{"term": "semi-", "meaning": "half"}],
            "points": ["ラテン系の semi- に対して、ギリシャ系の hemi- です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "latitude",
        "word": "Latitude",
        "meaning": "緯度、(思想や行動の)自由、許容範囲",
        "era": "14th Century Latin latitudo",
        "etymology": {
            "components": ["latus (broad, wide)"],
            "original_statement": "From Latin latitudo (breadth, width, extent, size), from latus (wide, broad)."
        },
        "concept": "Breadth or width (幅の広さ)",
        "thinking": "赤道から北や南への「広がり」。そこから比喩的に、規則でガチガチではない「行動や思考の自由な幅・ゆとり」という意味に使われるのが非常に詩的です。",
        "aftertaste": "横への広がりは、心のゆとりの広がり。",
        "example": "Employees are given a lot of latitude in how they complete their tasks.",
        "deep_dive": {
            "roots": [{"term": "stel-", "meaning": "to put, stand, broad"}],
            "points": ["航海時代、横（赤道からの距離・緯度）を図るのは比較的簡単でした。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "longitude",
        "word": "Longitude",
        "meaning": "経度",
        "era": "15th Century Latin longitudo",
        "etymology": {
            "components": ["longus (long)"],
            "original_statement": "From Latin longitudo (length, duration), from longus (long)."
        },
        "concept": "Length (縦の長さ)",
        "thinking": "地球を縦に割る線。「緯度」が北極星などの角度から調べられたのに対して、「経度」を正確に測るには高精度な時計（クロノメーター）が必要であり、大航海時代最大の難問でした。",
        "aftertaste": "時間を計らなければ、自分の縦位置は分からない。",
        "example": "The prime meridian is at zero degrees longitude.",
        "deep_dive": {
            "roots": [{"term": "longus", "meaning": "long"}],
            "points": ["longevity（長寿）などと同じ語源を持っています。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "meridian",
        "word": "Meridian",
        "meaning": "子午線、経線、絶頂期",
        "era": "14th Century Old French/Latin meridianus",
        "etymology": {
            "components": ["meridies (midday, south)"],
            "original_statement": "From Latin meridianus (of midday, of noon), from meridies (midday), from medius (middle) + dies (day)."
        },
        "concept": "Midday or the point of highest noon (真昼、太陽が最も高く昇る線)",
        "thinking": "太陽が真南にきて、一日の真ん中（昼の12時）を指し示す線。転じて、zenith同様に人生や国家の「最盛期」「絶頂」を意味します。AM/PM の M です。",
        "aftertaste": "影が最も短くなる、眩しい頂点。",
        "example": "He published his greatest novel at the meridian of his career.",
        "deep_dive": {
            "roots": [{"term": "medhyo-", "meaning": "middle"}, {"term": "dyeu-", "meaning": "to shine, day"}],
            "points": ["ante meridiem (AM: 午前) / post meridiem (PM: 午後) の語源です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "equator",
        "word": "Equator",
        "meaning": "赤道",
        "era": "14th Century Latin aequator",
        "etymology": {
            "components": ["aequare (to make equal)"],
            "original_statement": "From Medieval Latin aequator, from Latin aequare (to make equal), referring to the circle that equalizes day and night."
        },
        "concept": "The equalizer of day and night (昼と夜を等しくするもの)",
        "thinking": "地球の真ん中を通る線。ここでは年間を通じて毎日、昼と夜の長さが常に12時間ずつ等しく（equal）なります。世界のバランスを取る中心線。",
        "aftertaste": "地球を半分に分かつ、平等なる灼熱の帯。",
        "example": "Ecuador is named after the equator that runs through it.",
        "deep_dive": {
            "roots": [{"term": "aequus", "meaning": "equal"}],
            "points": ["equation（方程式・等しくすること）から来た言葉です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "tropics",
        "word": "Tropics",
        "meaning": "熱帯地方",
        "era": "14th Century Late Latin/Greek tropikos",
        "etymology": {
            "components": ["tropos (a turn, solstice)"],
            "original_statement": "From Late Latin tropicus (of the solstice), from Greek tropikos (of or pertaining to a turn or change or the solstice)."
        },
        "concept": "The regions of the turn (引き返す領域)",
        "thinking": "太陽が真上を通過し、夏至・冬至に到達して「進行方向をUターンする」緯度（回帰線）の間の地域。常夏の暑い楽園のイメージを持つようになりました。",
        "aftertaste": "太陽が踵を返す、光の満ちる場所。",
        "example": "They went on vacation to the tropics to escape the winter.",
        "deep_dive": {
            "roots": [{"term": "trep-", "meaning": "to turn"}],
            "points": ["トロピカルフルーツの『トロピカル』は、天文学の方向転換から来ています。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "polar",
        "word": "Polar",
        "meaning": "極の、正反対の",
        "era": "16th Century Middle French/Latin polaris",
        "etymology": {
            "components": ["polus (end of an axis, pole)"],
            "original_statement": "From Medieval Latin polaris (heavenly) and Latin polus, from Greek polos (pivot, axis of the sky)."
        },
        "concept": "Pertaining to the pole or pivot (天の軸、あるいは極端な対立)",
        "thinking": "地球の自転軸の末端という氷と雪の極地を意味するだけでなく、N極とS極のように「完全に相反する、対極的な」性質を表す言葉としても使われます。",
        "aftertaste": "相容れない二極。だが、軸一つで繋がっている。",
        "example": "Their political views are polar opposites.",
        "deep_dive": {
            "roots": [{"term": "kwel-", "meaning": "to revolve, move around"}],
            "points": ["polarity（極性）、polarize（二極化させる）などの元です。"]
        },
        "part_of_speech": "adjective"
    }
]

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 既存の WORDS のリストを正規表現で探して編集する
match = re.search(r'(const WORDS = )(\[.*\])(;)', text, re.DOTALL)
if match:
    prefix = match.group(1)
    json_array_str = match.group(2)
    suffix = match.group(3)
    
    existing_words = json.loads(json_array_str)
    existing_ids = {w.get("id", "") for w in existing_words}
    
    added_count = 0
    for new_word in word_batch:
        if new_word["id"] not in existing_ids:
            existing_words.append(new_word)
            added_count += 1
            
    # 新しい JSON 文字列に変換
    updated_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
    
    # テキストを置き換えて保存
    updated_text = text[:match.start()] + prefix + updated_json_str + suffix + text[match.end():]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_text)
    
    print(f"Success: Processed {len(word_batch)} words. Added {added_count} words.")
else:
    print("Failed to find or parse WORDS array in data.js.")
