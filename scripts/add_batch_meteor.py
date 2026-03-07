import json
import re

word_batch = [
    {
        "id": "meteorology",
        "word": "Meteorology",
        "meaning": "気象学",
        "era": "16th Century Greek meteoron + logia",
        "etymology": {
            "components": ["meteoron (thing high up)", "-logia (study of)"],
            "original_statement": "Coined from Greek meteorologia (treatise on celestial phenomena), from meteoron (thing high up) + -logia (study of)."
        },
        "concept": "The study of things high up (空高くにあるものの探求)",
        "thinking": "天文学（Astronomy）が宇宙の星を描き出すなら、これは自分の頭上から大気圏の果てまでの、雲、雨、雷、そして流星（meteor）など、空のすべての乱痴気騒ぎについて解き明かす学問。気象予報士はこの学問をマスターしています。",
        "aftertaste": "見上げた空には雲と風の言葉が渦巻いている。",
        "example": "Meteorology plays a vital role in understanding climate change.",
        "deep_dive": {
            "roots": [{"term": "aeirein", "meaning": "to lift, raise"}],
            "points": ["『高いところにふわっと持ち上げられた（meteor）もの』という直感的な表現。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "climate",
        "word": "Climate",
        "meaning": "気候、風土、(社会の)風潮",
        "era": "14th Century Old French/Greek klima",
        "etymology": {
            "components": ["klima (inclination, slope, latitude)"],
            "original_statement": "From Old French climat, from Latin clima, from Greek klima (inclination, slope, supposed slope of the earth toward the pole)."
        },
        "concept": "The inclination of the sun (太陽の傾きが作る土地の性格)",
        "thinking": "古代の学者は、地球は球体なので、北や南に行くと『太陽の光が当たる角度が傾いている（klima）』と考え、その傾きの度合いが土地ごとの気候の違いを生むと正確に気付いていました。",
        "aftertaste": "太陽の光があたる角度で、あなたの街の風の色が決まる。",
        "example": "The country has a very mild climate all year round.",
        "deep_dive": {
            "roots": [{"term": "klei-", "meaning": "to lean"}],
            "points": ["cline（傾斜）や decline（下る）、incline（傾く）などと同じ『斜め』のルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "tempest",
        "word": "Tempest",
        "meaning": "大嵐、暴風雨、大騒ぎ",
        "era": "13th Century Old French/Latin tempestas",
        "etymology": {
            "components": ["tempus (time, season, weather)"],
            "original_statement": "From Old French tempeste, from Vulgar Latin *tempesta, from Latin tempestas (storm, weather, season, time), from tempus (time)."
        },
        "concept": "A violent time of weather (激しい天気の時間)",
        "thinking": "フランス語などでは『天気＝時間（temps）』です。元々ラテン語でも『ある季節の天気』を指していた言葉が、次第に『嵐のような最悪の悪天候・大荒れの時期』という激しい意味に限定されていきました。",
        "aftertaste": "時が荒ぶる荒れ狂う天気は神の怒りか。",
        "example": "The ship was tossed around in a violent tempest.",
        "deep_dive": {
            "roots": [{"term": "temp-", "meaning": "to stretch, string (time)"}],
            "points": ["シェイクスピアの戯曲『テンペスト（あらし）』が特に有名です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "hurricane",
        "word": "Hurricane",
        "meaning": "ハリケーン、暴風、(大西洋側の)熱帯低気圧",
        "era": "16th Century Spanish/Taino Huracan",
        "etymology": {
            "components": ["Huracan (god of the storm)"],
            "original_statement": "From Spanish huracán, from Taíno (an extinct Caribbean language) Huracan (god of the storm)."
        },
        "concept": "The god of the storm (西インド諸島の嵐の神)",
        "thinking": "コロンブスがアメリカ周辺に到着した時、大西洋とカリブ海を襲う巨大な暴風を、現地の先住民であるタイノ族の『嵐の神殿・破壊の悪神（フラカン）』からそのまま名前を取って名付けました。",
        "aftertaste": "カリブ海に沈んだ先住民の嵐の神が、今も世界を蹂躙する。",
        "example": "The hurricane devastated the coastal towns.",
        "deep_dive": {
            "roots": [],
            "points": ["太平洋はタイフーン(typhoon)、インド洋はサイクロン(cyclone)と名前が違います。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "typhoon",
        "word": "Typhoon",
        "meaning": "台風、(太平洋北西部の)熱帯低気圧",
        "era": "16th Century Arabic/Greek/Chinese",
        "etymology": {
            "components": ["tu fang (great wind)", "typhon (monster)"],
            "original_statement": "A complex blend of Arabic/Persian tufan (storm), deeply influenced by Greek Typhon (father of the winds), and heavily reinforced by Chinese tai fung (great wind)."
        },
        "concept": "The great wind / The monster of winds (大風、あるいは風の怪物)",
        "thinking": "非常に面白い言葉で、ギリシャ神話で火山の煙を吐く最凶の怪物「テュポーン」と、中国・台湾などで大風を指す「大風（タイフン）」、そしてアラビア語の「強風（トゥーファーン）」が、シルクロードや大航海時代を通してアジアの海でまぜこぜになり、一つの恐ろしい名前になりました。",
        "aftertaste": "東洋の大風と西洋の怪物の名が、荒ぶる太平洋で重なり合った。",
        "example": "The incoming typhoon brought high waves and heavy rain.",
        "deep_dive": {
            "roots": [{"term": "dheub-", "meaning": "deep, hollow"}],
            "points": ["異なる三つの世界の言葉が、全く同じ嵐の現象に対して奇跡的にリンクした世界語。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "monsoon",
        "word": "Monsoon",
        "meaning": "モンスーン、季節風、雨季",
        "era": "16th Century Arabic mawsim",
        "etymology": {
            "components": ["mawsim (season)"],
            "original_statement": "From Dutch monssoen or Portuguese monção, from Arabic mawsim (appropriate season for a voyage), from wasama (to mark)."
        },
        "concept": "The season marked for voyage (航海のために刻まれた季節)",
        "thinking": "夏の半年は海から陸へ、冬の半年は陸から海へ吹く規則正しい季節風。アラブの商人たちは、この夏と冬で完全に真逆の風が吹く『航海に適した季節（マウシム）』を完璧に読み切り、インド洋の交易を支配しました。",
        "aftertaste": "貿易船の帆を膨らます、恵みの季節を刻む風。",
        "example": "Farmers in India absolutely depend on the heavy monsoon rains.",
        "deep_dive": {
            "roots": [{"term": "mawsim", "meaning": "season"}],
            "points": ["日本ではモンスーン気候により、独特の湿潤な夏がもたらされます。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "avalanche",
        "word": "Avalanche",
        "meaning": "雪崩(なだれ)、(質問などの)殺到",
        "era": "18th Century French/Latin panna",
        "etymology": {
            "components": ["lavanche (avalanche)"],
            "original_statement": "From French avalanche, an alteration of earlier lavanche, likely from a pre-Roman Alpine word for 'landslide' or from Vulgar Latin *labina (slipping), confused with avaler (to descend)."
        },
        "concept": "To swallow down or descend (飲み込んで滑り落ちる巨大な塊)",
        "thinking": "アルプス山脈（方言）で生まれた言葉。山の斜面に降り積もった膨大な量の雪や氷が、限界に達して斜面を飲み込みながら轟音とともに崩れ落ちてくる様。「ファンレターの雪崩（殺到）」というようにも使われます。",
        "aftertaste": "静寂を切り裂く轟音。真っ白な暴力が斜面を下る。",
        "example": "Fortunately, the skiers escaped the sudden avalanche.",
        "deep_dive": {
            "roots": [{"term": "sleb-", "meaning": "to slip (possible)"}],
            "points": ["a-val-anche（谷へ＝valleyへと向かう）というフランス語のアナロジーで言葉が変化しました。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "drought",
        "word": "Drought",
        "meaning": "干ばつ、日照り、枯渇",
        "era": "Old English drugath",
        "etymology": {
            "components": ["drugian (to dry up)"],
            "original_statement": "From Old English drugath (continuous dry weather, dryness), from drugian (to dry out), related to dryge (dry)."
        },
        "concept": "A continuous drying out (延々と続く乾燥)",
        "thinking": "農作物を枯らし、大地を不毛のヒビ割れた砂に変えるほどの致命的な「水不足」。生命が生まれる前に、すべての生き物が最も恐れている、水という資源の『完全な枯渇状態』を指すため、アイディアの枯渇などにも使われます。",
        "aftertaste": "大地がひび割れ、空にただ太陽の熱射だけが残る。",
        "example": "The prolonged drought resulted in a severe famine.",
        "deep_dive": {
            "roots": [{"term": "dheug-", "meaning": "to dry"}],
            "points": ["dry（乾燥した）という言葉の名詞形とも言えます（例：high / height の関係性）。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "breeze",
        "word": "Breeze",
        "meaning": "そよ風、微風、(話などで)楽なこと",
        "era": "16th Century Spanish/Portuguese briza",
        "etymology": {
            "components": ["briza (cold northeast wind)"],
            "original_statement": "From Old Spanish or Portuguese briza (a cold northeast wind). The meaning softened in English over the centuries to mean a gentle, pleasant wind."
        },
        "concept": "A gentle and pleasant wind (優しく心地よい風)",
        "thinking": "元々の南欧では『冷たくて鋭い北東の風』を意味していましたが、イギリスの船乗りたちがカリブ海などで出会う『心地よいさわやかな貿易風』にこの言葉を使い始め、穏やかなそよ風という意味に変化しました。",
        "aftertaste": "顔を撫でる涼しい風。海を渡ってきた柔らかい挨拶。",
        "example": "A cool breeze blew through the open window.",
        "deep_dive": {
            "roots": [],
            "points": ["『朝飯前だ、超簡単だ（It's a breeze）』という最高にスマートな熟語の元です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "gale",
        "word": "Gale",
        "meaning": "強風、大風、(笑いなどの)爆発",
        "era": "16th Century Unclear Origin",
        "etymology": {
            "components": ["gale (wind/singing)"],
            "original_statement": "Origin obscure. Possibly related to Old Norse galinn (mad, frantic) or Old English galan (to sing, yell)."
        },
        "concept": "A frantically screaming wind (狂ったように叫ぶ強風)",
        "thinking": "そよ風（breeze）よりはずっと激しく、人を吹き飛ばし木をへし折るが、ハリケーンほどの破壊力を持つ低気圧の手前くらい。気象学的に風力7~10に設定される『とても強い風』。大爆笑の嵐にも例えられます。",
        "aftertaste": "耳元で暴れ狂う風の咆哮。",
        "example": "The sturdy trees lost several branches in the severe gale.",
        "deep_dive": {
            "roots": [{"term": "ghel-", "meaning": "to call, yell"}],
            "points": ["nightingale（ナイチンゲール：夜に『歌う』鳥）と同じく『風の叫び声』がルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "current",
        "word": "Current",
        "meaning": "水流、気流、電流、現在の",
        "era": "14th Century Old French/Latin currere",
        "etymology": {
            "components": ["currere (to run)"],
            "original_statement": "From Old French corant (running), present participle of corre (to run), from Latin currere (to run, flow)."
        },
        "concept": "That which is running or flowing (走っているもの、流れているもの)",
        "thinking": "川や海の水が『走るように流れる帯（海流）』から始まり、空気の気流、電気の電流へと拡大。さらに『今この瞬間にまさに流れている（＝現在の、最新の）』という意味まで獲得しました。",
        "aftertaste": "水も、電気も、時間もすべては『今』を走って流れてゆく。",
        "example": "Be careful fighting the strong ocean current.",
        "deep_dive": {
            "roots": [{"term": "kers-", "meaning": "to run"}],
            "points": ["currency（通貨＝流通して走るもの）や course（コース・進路）と同じ、ダイナミックな語源です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "precipice",
        "word": "Precipice",
        "meaning": "絶壁、(破滅の)危機、がけっぷち",
        "era": "16th Century Middle French/Latin praecipitium",
        "etymology": {
            "components": ["prae- (before)", "caput (head)"],
            "original_statement": "From Middle French précipice, from Latin praecipitium (a steep place), from praeceps (headlong, headfirst), from prae- (before) + caput (head)."
        },
        "concept": "Falling head first (頭から真っ逆さまに落ちるような場所)",
        "thinking": "ただの崖ではありません。「足を滑らせたら最後、真っ逆さま（headfirst）に転落するしかない『断崖絶壁』」です。戦争や破産などの「限界ギリギリの危機的状況・がけっぷち」を指す最高にドラマチックな語彙。",
        "aftertaste": "足の指を少しでも出せば、重力が頭から引きずり込む。",
        "example": "The company is on the precipice of bankruptcy.",
        "deep_dive": {
            "roots": [{"term": "kap-", "meaning": "head"}],
            "points": ["precipitation（降水量/雨）も同じく『真っ逆さまに落ちてくる』という同じ語源です。空から降る水の絶壁ですね。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "precipitation",
        "word": "Precipitation",
        "meaning": "降水(量)、降雨・降雪、(化学の)沈殿、軽率な行動",
        "era": "16th Century Middle French/Latin",
        "etymology": {
            "components": ["prae- (before)", "caput (head)"],
            "original_statement": "From Latin precipitationem (a headlong falling, haste), from praeceps (headlong). Same root as precipice."
        },
        "concept": "Something falling to the ground (頭から地面に真っ逆さまに落ちてくるもの)",
        "thinking": "天から地上へと落ちてくる（＝降る）、雨、雪、あられ、ひょうなど、水分の落下物の総称（降水量）。化学反応でビーカーの底に『沈み落ちる』物質（沈殿物）や、よく考えずに『突っ走る（真っ逆さまに落ちる）』焦燥感にも使われます。",
        "aftertaste": "空の絶壁から、水が頭から真っ逆さまに降る。",
        "example": "The forecast calls for a high probability of precipitation.",
        "deep_dive": {
            "roots": [{"term": "kap-", "meaning": "head"}],
            "points": ["天気予報の『POP (Probability of Precipitation)＝降水確率』として日常的に目にします。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "glacier",
        "word": "Glacier",
        "meaning": "氷河、巨大な氷の塊",
        "era": "18th Century French/Latin glacies",
        "etymology": {
            "components": ["glacies (ice)"],
            "original_statement": "From French glacier, from Franco-Provençal (Alpine) glacier, from Vulgar Latin *glaciarium, from Latin glacies (ice)."
        },
        "concept": "A huge mass of ice (途方もない重さの氷塊)",
        "thinking": "山に降り積もった万年雪が自重で圧縮されて極限の硬い氷になり、重力によって年間わずか数メートルという途方もなく遅い速度で山を下っていく、大自然の彫刻刀（氷のかたまり）。動かないように見える、途方もなく遅い流れ。",
        "aftertaste": "永遠を閉じ込めた氷の河が、静かに山を削り出していく。",
        "example": "The giant glacier completely carved out an entire deep valley.",
        "deep_dive": {
            "roots": [{"term": "gel-", "meaning": "cold, to freeze"}],
            "points": ["gelato（冷たいジェラート）や jelly（固まったゼリー）と同じ冷たいルーツです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "volcano",
        "word": "Volcano",
        "meaning": "火山",
        "era": "17th Century Italian/Roman Vulcan",
        "etymology": {
            "components": ["Vulcanus (Roman God of Fire)"],
            "original_statement": "From Italian vulcano, named after Vulcano, an island off Sicily, derived from Roman Vulcanus, the god of fire and metalworking."
        },
        "concept": "The chimney of the fire god (火の神の煙突)",
        "thinking": "ローマの火と鍛冶の神「ウゥルカーヌス」。地中海の島（現在のヴルカーノ島）は彼が地下でハンマーを叩いて武器を作っている工房であると信じられ、そこから火を噴く山すべての名詞となりました。スター・トレックのバルカン星もここから。",
        "aftertaste": "大地の裂け目で、太古の神がハンマーを振り下ろす。",
        "example": "The active volcano erupted, spewing ash high into the sky.",
        "deep_dive": {
            "roots": [],
            "points": ["ギリシャ神話でいうヘファイストスにあたる、鍛冶職人の神様です。"]
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
        "concept": "The equalizer of day and night (昼と夜の長さを等しくするもの)",
        "thinking": "地球の真ん中を通る仮想の直線。ここでは自転軸の傾きに関わらず、年間を通じて毎日、昼と夜の長さが常に12時間ずつ等しく（equal）なります。地球を北半球と南半球に分かつ、究極のバランスライン。",
        "aftertaste": "二つの半分を等しく分かつ、燃え盛る境界線。",
        "example": "Ecuador is named after the equator that runs straight through it.",
        "deep_dive": {
            "roots": [{"term": "aequus", "meaning": "equal"}],
            "points": ["equal, equation（方程式）と同じ『等しくすること』。前回の一群で出ましたが復習になります。"]
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
        "concept": "The line of midday (真昼を示す線)",
        "thinking": "太陽が真南にきて、一日の真ん中（mid + day）に達した時の空の軌跡。AM/PM（午前/午後＝ante meridiem/post meridiem）のあの「M」のことです。転じて人生や名声の『絶頂・最盛期』という意味に昇華されました。",
        "aftertaste": "太陽が天頂でピタリと止まる、その瞬間の完璧さ。",
        "example": "The Greenwich Meridian is used as the prime meridian for longitude.",
        "deep_dive": {
            "roots": [{"term": "medhyo-", "meaning": "middle"}, {"term": "dyeu-", "meaning": "day, sky"}],
            "points": ["これも素晴らしい概念ですが既出。知識の再確認として。"]
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
        "concept": "Breadth or width (横への広がり、幅広さ)",
        "thinking": "赤道から北極や南極への『横の線の幅』。厳しい規則で縛るのではなく『ある程度の横方向への自由な幅や裁量＝ゆとり』を持たせるという比喩的意味が非常にスマートな単語です。",
        "aftertaste": "枠にとらわれない、あなただけの横の広がり。",
        "example": "The manager gave me considerable latitude in deciding how to finish the project.",
        "deep_dive": {
            "roots": [{"term": "stel-", "meaning": "to put, stand, broad"}],
            "points": ["経度は longitude (long：縦の長さ) です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "tide",
        "word": "Tide",
        "meaning": "潮の満ち引き、風潮、流れ、時期",
        "era": "Old English tid",
        "etymology": {
            "components": ["tid (time, season, hour)"],
            "original_statement": "From Old English tid (time, season, hour), from Proto-Germanic *tidiz (division of time)."
        },
        "concept": "A division of time (区切られた特定の時間)",
        "thinking": "月と太陽の引力によって、海面が規則正しく上下する現象。本来は「海」ではなく『時間そのもの（time）』を指すゲルマン系の言葉でした。世論の風潮など『抗えない時代の大きな流れ』にも使われます。",
        "aftertaste": "時間と重力が織りなす、海の呼吸。",
        "example": "The tide is turning against the current government.",
        "deep_dive": {
            "roots": [{"term": "da-", "meaning": "to divide"}],
            "points": ["time や tidy（きちんとした：時間通りに整理された）と同じルーツです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "ebb",
        "word": "Ebb",
        "meaning": "引き潮、衰退、減退する",
        "era": "Old English ebba",
        "etymology": {
            "components": ["ebba (ebb tide)"],
            "original_statement": "From Old English ebba (ebb tide), perhaps related to ab- (off, away) pointing to a retreat of water."
        },
        "concept": "The going out of the tide (潮が引いていくこと)",
        "thinking": "満ち潮（flow/flood）の逆。海辺で砂浜から波がスルスルと沖へ退いていく様子。潮が引くだけでなく、情熱、体力、名声、富などが『ゆっくりと、確実に衰退し削り取られていく』哀愁を帯びた言葉です。",
        "aftertaste": "波が引いた後の砂浜には、ただ無力な貝殻だけが残る。",
        "example": "His enthusiasm began to ebb as the difficult project dragged on.",
        "deep_dive": {
            "roots": [],
            "points": ["『ebb and flow（潮の満ち引き、盛衰）』というセットフレーズで人生の浮き沈みに多用されます。"]
        },
        "part_of_speech": "noun"
    }
]

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

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
            
    updated_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
    updated_text = text[:match.start()] + prefix + updated_json_str + suffix + text[match.end():]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_text)
    
    print(f"Success: Processed {len(word_batch)} words. Added {added_count} words.")
else:
    print("Failed to find or parse WORDS array in data.js.")
