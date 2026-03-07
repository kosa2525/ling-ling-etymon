import json
import re

words_data = [
    ("clatter", "Clatter", "カタカタ鳴る", "Old English", "clatrung (noise)", "Loud rattling", "硬いもの同士がぶつかり合い、静寂を乱す不規則で攻撃的なリズム。", "心の中の「クラッター（カタカタ鳴る音）」を鎮め、深い静寂を取り戻しましょう。"),
    ("rustle", "Rustle", "カサカサ鳴る", "Middle English", "roustle (susurrate)", "Soft crackling", "乾いた葉が触れ合うような微細な摩擦音に宿る、気配という名のメッセージ。", "風の「ラッスル（かすかな絹鳴り）」に耳を澄ませば、不可視の存在を感じ取れます。"),
    ("groan", "Groan", "うめく、きしむ", "Old English", "granian (to murmur, groan)", "Deep moan of pain", "声帯を通さずとも、内なる苦痛や軋み（きしみ）が物理的な重みを持って世界へ漏れ出ること。", "古い床が「グローン（きしむ）」ように、あなたの心の歪みも時には音を立てて悲鳴を上げます。"),
    ("creak", "Creak", "きしむ", "14th Century", "kreken (to make a harsh noise)", "Harsh squeaking", "長年の負荷に耐えきれなくなった物質が発する、限界と悲鳴の交差点。", "「クリーク（きしむ音）」は、それが休む間もなくあなたを支え続けてきたという愛の証明です。"),
    ("hiss", "Hiss", "シューッという音", "Middle English", "hissen (to make a sibilant sound)", "Sibilant sound", "蒸気や怒りが、狭い隙間をこじ開けて噴出する暴力的な警告音。", "ヘビの「ヒス（威嚇音）」は恐怖ではなく、不用意に近づくなという明確で親切な境界線です。"),
    ("sizzle", "Sizzle", "ジュージュー鳴る", "17th Century", "sizzlen (imitative)", "Hissing while frying", "熱と油という異なるエネルギーが衝突し、破壊と再生を繰り返す歓喜の叫び。", "美味しい料理の「シズル（ジュージュー焼ける音）」は、命をいただく本能的な祝福です。"),
    ("thud", "Thud", "ドスッという音", "Old English", "thoden (a violent wind)", "Dull heavy sound", "重力の法則に従い、質量を持った存在が容赦なく大地と激突する絶望的な響き。", "失望が「サッド（鈍い音）」と共に落ちてきても、いずれその上に新しい花が咲きます。"),
    ("splash", "Splash", "バシャッという音", "18th Century", "plash (puddle)", "Sound of liquid scattering", "液体の表面張力が打ち砕かれ、無数の飛沫（しぶき）となって四方八方に拡散すること。", "「スプラッシュ（水しぶき）」を上げて、停滞した日常の水面に大きな波紋を起こしましょう。"),
    ("trickle", "Trickle", "したたる、ちょろちょろ流れる", "Middle English", "triklen (to flow in drops)", "Flow in thin stream", "細く、途切れそうになりながらも、決して止まることのない粘り強い生命の脈動。", "「トリックル（滴り）」ほどの小さな進歩でも、岩を穿つ（うがつ）だけの力を秘めています。"),
    ("gurgle", "Gurgle", "ゴボゴボ鳴る", "15th Century", "gurgulio (windpipe, gullet)", "Bubbling sound", "空気が液体を通り抜ける際に生じる、無邪気で生々しい身体的な共鳴。", "小川の「ガーグル（うがいをするような音）」は、大地が楽しそうに笑っている声です。"),
    ("rumble", "Rumble", "ゴロゴロ鳴る", "Middle English", "rumblen (to make a low heavy noise)", "Deep resonant sound", "遠くの雷や地面の底から伝わってくる、抗うことのできない巨大な力の予兆。", "お腹の「ランブル（腹の虫が鳴く音）」には、宇宙があなたに空腹を知らせる壮大な意志が宿ります。"),
    ("roar", "Roar", "吠える、轟く", "Old English", "rarian (to wail, lament)", "Loud deep cry", "獣の王が自らの存在を誇示し、世界中の弱いものを服従させる圧倒的な音波の暴力。", "「ロア（咆哮）」する海のように、時には自らの巨大なエネルギーを解放させてください。"),
    ("bellow", "Bellow", "怒鳴る", "Old English", "bylgan (to bluster)", "Shout in deep voice", "言葉の形をとる前の、純粋な怒りや苦痛を肺の底から絞り出した原始的な叫び。", "理性を無くして「ベロウ（怒鳴り続ける）」する前に、一度深く息を吸い込んで。"),
    ("squeak", "Squeak", "チューチュー鳴る、キーキーきしむ", "14th Century", "squeken (imitative)", "Short high sound", "取るに足らない小さな存在が、世界に対して必死に発している可憐なSOS。", "ドアの「スクィーク（きしみ）」をうるさがらずに、油（愛情）を注いで癒やしを与えてください。"),
    ("screech", "Screech", "金切り声を出す", "16th Century", "scriken (to shriek)", "Harsh piercing cry", "金属が擦れ合うような破壊的な高音が、聴覚を通して大脳を直接ひっかく不快感。", "車のタイヤの「スクリーチ（ブレーキ音）」は、あなたを致命的な危険から引き戻す神の警告です。"),
    ("shriek", "Shriek", "悲鳴を上げる", "16th Century", "schriken (to scream)", "High-pitched scream", "恐怖や狂気が極限に達し、声帯を限界まで引き裂くように発せられる絶望の響き。", "悪夢の中で「シュリーク（悲鳴）」を上げても、目覚めれば必ず静寂があなたを守ってくれます。"),
    ("wail", "Wail", "泣き叫ぶ", "Old Norse", "veila (to weep)", "Prolonged mournful cry", "愛するものを失った喪失感が、終わりのない旋律となっていつまでも大気を震わせること。", "悲しみの夜は、無理に声をおさえずに心ゆくまで「ウェイル（泣き叫んで）」してください。"),
    ("moan", "Moan", "うめく、嘆く", "Old English", "manan (to complain)", "Low sound of grief", "押し殺された苦痛が、低く波打つような持続音となって口から漏れ出ること。", "風の「モーン（低いうめき声）」は、世界があなたの代わりに哀しみを肩代わりしている音です。"),
    ("gasp", "Gasp", "息をのむ、あえぐ", "Old Norse", "geispa (to yawn)", "Catch breath sharply", "驚愕や恐怖により、世界から空気を吸い込むことすら一瞬忘れて硬直する無防備な状態。", "美しい風景に出会ったときの「ギャスプ（息をのむ瞬間）」こそが、魂の深呼吸です。"),
    ("pant", "Pant", "あえぐ、息を切らす", "15th Century", "pantaisier (to be breathless)", "Breathe heavily", "肉体の限界点に達した肺が、燃え尽きる前により多くの酸素を求めて行う無慈悲なピストン運動。", "犬の無邪気な「パント（あえぎ声）」は、喜びというエネルギーへの純粋なアクセスです。"),
    ("puff", "Puff", "シュッシュッと吐く", "Middle English", "puffen (imitative)", "Short explosive burst", "頬を膨らませて空気をため込み、一気に小さな爆発を伴ってそれを外世界へ解放すること。", "タバコの煙を「パフ（ふかす）」ように、嫌な過去も肺の奥から遠くへ吹き飛ばして。"),
    ("snort", "Snort", "鼻を鳴らす", "14th Century", "snorten (imitative)", "Force breath through nose", "鼻腔を通して荒々しく空気を噴射し、言葉にならない軽蔑や苛立ちを表現すること。", "「スノート（鼻息荒く）」して怒ってばかりいないで、馬のように草原への解放を夢見てみては？"),
    ("sniff", "Sniff", "匂いをかぐ、鼻をすする", "14th Century", "snuffen (to draw mucus)", "Inhale through nose", "大気中に漂う微小な情報分子を、鋭敏な感覚器官を用いて探り当てようとする好奇心。", "花束に顔を近づけて「スニフ（匂いを嗅ぐ）」する仕草は、生命への最も優雅なアプローチです。"),
    ("sneeze", "Sneeze", "くしゃみをする", "Old English", "fneosan (to sneeze)", "Expel air suddenly", "外部からの侵入者を、意志の力とは無関係に暴力的かつ圧倒的なスピードで排除する自己防衛。", "「スニーズ（くしゃみ）」は、不要な悪意を内側から吹き飛ばす健康の証です。"),
    ("cough", "Cough", "咳をする", "Old English", "cohhian (imitative)", "Expel air from lungs", "喉に詰まった異物を排出するための、胸の奥底から込み上げる激しく乾いた震動。", "「カフ（咳払い）」で気まずい空気を誤魔化すのは、不器用な優しさの裏返しです。"),
    ("hiccup", "Hiccup", "しゃっくり", "16th Century", "hickop (imitative)", "Involuntary spasm", "横隔膜の痙攣が生み出す、リズムを無視した愛嬌のある予測不可能なノイズ。", "厄介な「ヒカップ（しゃっくり）」も、あなたの身体が一生懸命に働いている証拠です。"),
    ("burp", "Burp", "げっぷをする", "1930s", "burp (imitative)", "Eructation", "胃の中に溜まった過剰な空気を、社会的なマナーを無視して解放してしまう本能的な安堵。", "赤ちゃんが「バープ（げっぷ）」する姿は、どんな立派な言葉よりも安心と平和の象徴です。"),
    ("mumble", "Mumble", "もごもご言う", "Middle English", "momelen (to mutter)", "Speak indistinctly", "内容を明確に伝えることを放棄し、口ごもったまま自己完結する内向性の極み。", "自信のない「マンブル（もごもごとした話し方）」をやめれば、世界はもっとクリアにあなたの言葉を受け入れます。"),
    ("mutter", "Mutter", "つぶやく", "14th Century", "moteren (imitative)", "Speak in low voice", "他者には聞こえない低いトーンで、不平不満や密かな真実を呪文のように反芻すること。", "怒りで「マター（ぶつぶつ言う）」する言葉は、あなたの奥底にある本当の願いを裏返したものです。"),
    ("grumble", "Grumble", "不平を言う", "16th Century", "grommelen (to murmur, mutter)", "Complain in bad-tempered way", "腹の底でくすぶった不満が、低周波の唸りとなっていつまでも周囲を不穏にする状態。", "空腹時の「グランブル（腹の虫）」と同様に、心の不満も適切な栄養を与えれば静まります。"),
    ("growl", "Growl", "うなる", "Old French", "groler (to grumble)", "Low guttural sound", "喉の奥で震える振動音が、警告と剥き出しの敵意を伴って響き渡る野性のサイン。", "心の中の獣が「グロウル（低い唸り声）」を上げたときは、自分の領域が侵害されているサインです。を守って。"),
    ("snarl", "Snarl", "歯をむき出して怒る", "16th Century", "snar (to bind, entangle)", "Growl showing teeth", "歯をむき出しにして牙を誇示しながら、攻撃の意思を隠そうともしない極限の敵対。", "糸が絡まった「スナール（もつれ）」のように、怒りはあなたの思考を複雑に縛り付けます。ほどく努力を。"),
    ("whine", "Whine", "哀れっぽい声を出す", "Old English", "hwinan (to whiz, squeak)", "Long, high-pitched complaining", "高い周波数で延々と続く、同情を買うためや要求を通すための不愉快な哀願のノイズ。", "「ワイン（泣き言）」で現状を変えることはできません。毅然とした態度こそが鍵です。"),
    ("whimper", "Whimper", "すすり泣く、クンクン鳴く", "16th Century", "whymper (imitative)", "Series of low, feeble sounds", "恐怖や痛みに屈し、もはや抵抗する気力すら失った無力で哀れな生命の残響。", "傷ついた子犬の「ウィンパー（弱々しい鳴き声）」を無視しない優しさが、世界に平和をもたらします。"),
    ("guffaw", "Guffaw", "大笑いする", "18th Century", "gawf (to laugh loud)", "Loud and boisterous laugh", "理性や品格の一切をかなぐり捨て、腹の底から馬鹿馬鹿しさを全身で肯定する痛快な爆発。", "上品に微笑むのも良いけれど、時には「ガフォー（高笑い）」で人生の悩みを吹き飛ばしましょう。"),
    ("cackle", "Cackle", "カハカハ笑う", "13th Century", "kakelen (imitative)", "Shrill laugh", "魔女が呪いをかけるような、あるいはニワトリが卵を産んだような、甲高く乾いた非日常感のある笑い。", "少し意地悪な「キャックル（嫌な笑い声）」を聞いたら、あなたは自分を信じてその場を立ち去るべきです。"),
    ("snicker", "Snicker", "忍び笑いする", "17th Century", "snick (to cut, clip)", "Smothered laugh", "相手を見下し、その失敗を密かに嘲笑しながらも表には出さない、卑屈で冷たい優越感。", "誰かに対する「スニッカー（忍び笑い）」は、いずれあなた自身の魂の気高さを切り刻んでしまいます。"),
    ("smirk", "Smirk", "ニヤニヤ笑う", "Old English", "smearcian (to smile)", "Smile smugly", "自惚れ（うぬぼれ）や小賢しい優越感を隠しきれず、顔の片隅に不自然に作られた歪んだ「笑顔」の偽物。", "勝利の後の「スマーク（ドヤ顔）」を控え、敗者への敬意を持つことこそが本当の勝者の姿です。"),
    ("buzz", "Buzz", "ブンブンうなる", "17th Century", "buzzen (imitative)", "Continuous humming noise", "無数の羽をもつ昆虫が空間を埋め尽くすような、焦燥感と熱気を含んだ途絶えることのない羽音。", "頭の中の過剰な情報の「バズ（羽音）」を一旦ストップして、静かな森を歩きましょう。"),
    ("drone", "Drone", "単調な音を立てる", "Old English", "dran (male honeybee)", "Continuous low humming", "変化のない低い周波数が延々と鳴り響き、自我を麻痺させ眠りへと誘う没個性的なノイズ。", "「ドローン（単調な低い音）」のように退屈な講義も、目を閉じて瞑想の時間として有効活用できます。"),
    ("purr", "Purr", "のどをゴロゴロ鳴らす", "17th Century", "purren (imitative)", "Low continuous vibratory sound", "恐怖や緊張から完全に解放され、極上の悦楽と満足感に満ちた時にだけ発動する内なる平和のエンジンの振動音。", "猫が膝の上で「パー（ゴロゴロ鳴る）」している間、この世のすべての不幸は一時停止ボタンを押されている。"),
    ("chirp", "Chirp", "チュンチュン鳴く", "Middle English", "chirpen (imitative)", "Short high sound", "世界は美しいという絶対的な確信を、短く鋭いリズムで無限に空へと放ち続ける小さな天使の歌声。", "小鳥の「チャープ（さえずり）」は、毎朝無条件で与えられる自然からの最高にハッピーなモーニング・コール。")
]

words = []
for item in words_data:
    root1 = item[4].split(" ")[0]
    meaning1 = " ".join(item[4].split(" ")[1:]).strip("()")
    w = {
        "id": f"{item[0]}_sound",
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
        "example": f"We could hear the {item[0]} in the distance.",
        "deep_dive": {
            "roots": [{"term": root1, "meaning": meaning1}],
            "points": ["音の響き（擬音語）がそのまま言葉の魂へ直結する世界。"]
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
    print(f"Success: Added {added} words. Theme: Sound & Silence (Cycle 3).")
else:
    print("Error parsing data.js")
