import json
import re

word_batch = [
    # Cycle 123: Bird & Sky
    {
        "id": "soar_sky",
        "word": "Soar",
        "meaning": "高く舞い上がる、急上昇する、(希望などが)膨らむ",
        "era": "14th Century Latin ex- + aura",
        "etymology": {
            "components": ["ex- (out)", "aura (breeze, air)"],
            "original_statement": "From Old French sorer, from Vulgar Latin exaurare (to rise into the air), from Latin ex- (out) + aura (breeze, air)."
        },
        "concept": "Rising into the air (「空気（air）」の 中へと 「舞い上がる（rise）」 自由で 雄大な飛翔)",
        "thinking": "羽ばたきを止め 風の流れそのものに身を任せながら どこまでも高く 視界を広げていくこと. 語源は「風の中へ出る」. それは 物理的な高さだけでなく 魂が日常の重力から解放され 理想の空へと 解き放たれる瞬間を指します. 視点が高まれば 悩みは小さくなります.",
        "aftertaste": "自由の翼. あなたを縛る地上（現実）の糸を 一時（いっとき）だけ解いてごらん. 宇宙の息吹（風）を感じながら あなたの魂を 好きなだけ高く 舞い上がらせよう.",
        "example": "The eagle began to soar gracefully above the mountain peaks, searching for prey.",
        "deep_dive": { "roots": [{"term": "wer-", "meaning": "to raise, lift (possible for aura)"}], "points": ["aura（オーラ：漂う気配）と同じ。存在が空気へと溶け出す瞬間の美。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "ethereal_sky",
        "word": "Ethereal",
        "meaning": "この世のものとは思えない、空気のような、極めて優美な",
        "era": "16th Century Greek aither",
        "etymology": {
            "components": ["aither (upper air; pure, bright air)"],
            "original_statement": "From Latin aetherius, from Greek aitherios, from aither (upper air; pure, bright air)."
        },
        "concept": "Of the upper air (神々が住む 「高天（upper air）」の ように 澄み切った 「非物質的な（pure）」 美しさ)",
        "thinking": "重さや汚れを一切持たず 光と空気だけで編み上げられたかのような 神秘的で 捉えがたい存在感. 語源は「純粋な空気」. それは 手に取ることはできなくても 私たちの魂を 根源的な平穏へと 誘（いざな）う 聖なる気配です. 繊細にして 永遠なる輝き.",
        "aftertaste": "光のヴェール. 現実の泥にまみれても あなたの心の奥底には 決して汚されることのない「エセリアル（優美）」な光が 常に静かに 輝き続けているのだから.",
        "example": "The music had an ethereal quality that transported the listeners to a dreamlike world.",
        "deep_dive": { "roots": [{"term": "aidh-", "meaning": "to burn"}], "points": ["edifice（大建築物：燃え立つ情熱の結実）と同じ。天上の空気は「燃えるほどに明るい」という直感。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "plumage_sky",
        "word": "Plumage",
        "meaning": "羽毛、(鳥の)全身の羽",
        "era": "14th Century Latin pluma",
        "etymology": {
            "components": ["pluma (feather, down)"],
            "original_statement": "From Old French plumage, from plume (feather), from Latin pluma (feather, down, soft feather)."
        },
        "concept": "Collection of soft feathers (「柔らかな羽（soft feather）」が 幾重にも 「重なった（collection）」 命の装い)",
        "thinking": "空を飛ぶための実用的な道具でありながら 同時に 誰よりも美しくありたいという 生命の誇りを象徴する 色彩豊かな装飾. 語源は「羽」. 厳しい寒さから身を守り 風を捉える その一枚一枚の羽は 孤独な飛行を支える 唯一の「連帯」でもあります.",
        "aftertaste": "誇りの羽衣. あなたという鳥が纏（まと）う その「言葉」や「思想」という名の羽を 毎日丁寧に磨き上げよう. それが あなたをより高く、より遠くへと 運んでいくのだから.",
        "example": "The peacock displayed its magnificent plumage to attract a mate in the garden.",
        "deep_dive": { "roots": [{"term": "pleus-", "meaning": "to pluck, feather (possible root)"}], "points": ["plume（羽飾り）と同じ。軽さと美しさが同居する、空の美学。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "celestial_sky",
        "word": "Celestial",
        "meaning": "天の、天空の、神々しい、天国の",
        "era": "14th Century Latin caelum",
        "etymology": {
            "components": ["caelum (heaven, sky)"],
            "original_statement": "From Old French celestiel, from Latin caelestis (heavenly, celestial), from caelum (heaven, sky)."
        },
        "concept": "Of the heavens (「空（sky）」の さらに向こう側にある 「神聖なる場所（heaven）」の 響き)",
        "thinking": "地上のあらゆる喧騒や 汚れを超越した 星々が奏でる 永遠の秩序と 静寂の世界. 語源は「天の」. それは 私たちの理解を遥かに超えた 巨大なリズムの一部であることを 思い出させてくれる 崇高な美しさです. 夜空を見上げるとき 私たちは自分の中の「天（セレスティアル）」と出会います.",
        "aftertaste": "星辰の導き. あなたの人生の物語は この小さな地球だけでなく 壮大な宇宙の「天」の一部として 描かれている. その広大さを信じて 今日も胸を張って歩もう.",
        "example": "The telescope allowed us to observe the celestial bodies with incredible detail.",
        "deep_dive": { "roots": [{"term": "kaid-lo-", "meaning": "bright, clear (possible root for caelum)"}], "points": ["Ceiling（天井）と同じ。私たちの視線を惹きつけ、守ってくれる「上方の極致」。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "volant_sky",
        "word": "Volant",
        "meaning": "飛んでいる、飛べる、機敏な、すばしこい",
        "era": "14th Century Latin volare",
        "etymology": {
            "components": ["volare (to fly)"],
            "original_statement": "From Old French volant, from Latin volantem, from volare (to fly)."
        },
        "concept": "Able to fly (重力を振り切り 「自由に（free）」 「空を行く（fly）」 軽やかで 機敏な状態)",
        "thinking": "一つの場所に縛り付けられることを拒み 思考も肉体も 常に「移動」と「飛翔」の中に置いている その野生的な自由. 語源は「飛ぶこと」. それは 安定を捨てる勇気であり 風の向きに合わせて 瞬時に軌道修正できる 究極の柔軟性でもあります. 飛んでいるとき 人は最も自分に近づきます.",
        "aftertaste": "疾風の思考. 一箇所に立ち止まって 泥沼に沈まないで. あなたの魂を常に「ヴォラント（機動的）」に保ち 変わり続ける世界を 軽快に飛び越えてゆこう.",
        "example": "The tiny bird was volant even in the strongest winds, showing remarkable agility.",
        "deep_dive": { "roots": [{"term": "gwel-", "meaning": "to fly (possible related)"}], "points": ["volley（ボレー：一斉射撃、一斉の飛び）や volatile（揮発性の：飛び散りやすい）と同じ、拡散するエネルギー。"] },
        "part_of_speech": "adjective"
    }
]

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
    if match:
        prefix, json_array_str, suffix = match.groups()
        words = json.loads(json_array_str)
        existing_ids = {w.get("id") for w in words}
        
        added = 0
        for item in word_batch:
            if item["id"] not in existing_ids:
                words.append(item)
                added += 1
        
        new_content = content[:match.start()] + prefix + json.dumps(words, ensure_ascii=False, indent='\t') + suffix + content[match.end():]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Success: Added {added} words in Cycle 123.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
