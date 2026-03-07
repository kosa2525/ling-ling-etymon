import json
import re

word_batch = [
    {
        "id": "relish_delight",
        "word": "Relish",
        "meaning": "心ゆくまで楽しむ、味わう、風味、付け合わせ",
        "era": "16th Century Old French relaissier",
        "etymology": {
            "components": ["re- (back)", "laissier (to leave)"],
            "original_statement": "From Old French relaissier (to leave behind), from re- (back) + laissier (to leave), hence 'an aftertaste left behind'."
        },
        "concept": "The aftertaste left behind (後を引く余韻、消えない喜び)",
        "thinking": "ただ食べる（eat）のではなく、その一口が喉を通ったあとに残る「余韻（aftertaste）」をじっくりと慈しむこと。それが転じて、期待した以上の喜びや風味を心から「楽しむ（enjoy）」という意味になりました。消えゆく瞬間にこそ宿る、真の豊かさを捉える言葉です。",
        "aftertaste": "一口の向こう側に、広大な香りの記憶が眠っている。",
        "example": "He relished the rare opportunity to speak with the famous philosopher in person.",
        "deep_dive": {
            "roots": [{"term": "leik-", "meaning": "to leave"}],
            "points": ["release（解放する）や lease（賃貸借）と同じ。後に残すことがキーワード。"]
        },
        "part_of_speech": "verb"
    },
    {
        "id": "delight_delight",
        "word": "Delight",
        "meaning": "歓喜、大いなる喜び、嬉しがらせる",
        "era": "13th Century Old French/Latin delectare",
        "etymology": {
            "components": ["de- (away, intensive)", "lacere (to lure, entice)"],
            "original_statement": "From Old French delit, from Latin delectare (to lure away, entice, charm, please), frequentative of delicere (to lure away), from de- (away) + lacere (to entice)."
        },
        "concept": "To lure away with charm (魅力によって、日常から「誘い出される」ほどの喜び)",
        "thinking": "もともとは、あまりの魅力に抗えず、自分が今いる場所から「誘い出される（lure away）」ほど心を奪われること。それは受動的で抗いがたい甘美な誘惑の結果としての「歓喜」です。我を忘れて、ただその喜びに身を委ねている無垢な状態を指します。",
        "aftertaste": "日常の扉を開けて、光のあふれる場所へと連れ去られるほどの衝撃的な多幸感。",
        "example": "The children's voices were filled with pure delight as they opened their gifts.",
        "deep_dive": {
            "roots": [{"term": "lak-", "meaning": "to snare, trap"}],
            "points": ["delicious（美味しい）や delicate（繊細な）と同じ、逃れられない誘惑のルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "elation_delight",
        "word": "Elation",
        "meaning": "意気揚々、大得意、(精神の)高揚",
        "era": "14th Century Old French/Latin ex- + latus",
        "etymology": {
            "components": ["ex- (out, up)", "latus (carried)"],
            "original_statement": "From Latin elationem (exaltation), from elatus (uplifted, exalted), from ex- (out) + latus (carried)."
        },
        "concept": "Being carried up (心が天に向かって「持ち上げられて」いる状態)",
        "thinking": "自分の足で立っているのではなく、喜びという目に見えない力によって、空高く「運び上げられて（carried up）」しまっている感覚。地上から離れ、精神が最高の高み（peak）へ到達したしたことによる、輝かしい高揚感と満足感のことです。",
        "aftertaste": "重力さえも忘れ、ただ一点的を目指して昇り続ける魂の飛翔。",
        "example": "There was a sense of elation in the air as the team celebrated their victory.",
        "deep_dive": {
            "roots": [{"term": "tol-", "meaning": "to lift, bear"}],
            "points": ["translate（翻訳する：運び渡す）や relate（関連付ける）と同じ『運ぶ』ルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "euphoria_delight",
        "word": "Euphoria",
        "meaning": "幸福感、多幸感、(一時的な)陶酔",
        "era": "17th Century Modern Latin/Greek euphoros",
        "etymology": {
            "components": ["eu- (well)", "pherein (to carry, bear)"],
            "original_statement": "From Greek euphoria (ability to bear easily), from euphoros (well-bearing, patient), from eu- (well) + pherein (to carry)."
        },
        "concept": "The power of bearing well (人生の重みを、「軽やかに」運べる健康的な全快感)",
        "thinking": "本来は、病が癒え、「いかなる重荷も軽々と運べる（bear well）」という生命の快復に伴う感覚。そこから「すべてがうまくいっている」という全能に近いほどの幸福感を指すようになりました。人生という荷物が、羽のように軽く感じられる、魔法のような絶好調。",
        "aftertaste": "どんな嵐の中でも。ただ『生きている』というだけで笑みがこぼれる、究極の全肯定。",
        "example": "The stadium was filled with a sense of pure euphoria after the final goal.",
        "deep_dive": {
            "roots": [{"term": "bher-", "meaning": "to carry"}],
            "points": ["fertile（肥沃な：多くを運ぶ/生む）や prophet（預言者：先に運ぶ/語る）と同類。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "rapture_delight",
        "word": "Rapture",
        "meaning": "有頂天、狂喜、魂が奪われること",
        "era": "16th Century Latin raptus",
        "etymology": {
            "components": ["rapere (to seize, snatch, carry off)"],
            "original_statement": "From Latin raptus (a carrying off, seizing, plundering), from rapere (to seize, hurry away)."
        },
        "concept": "To be seized and hurried away (魂が「ひったくられ」、どこかへ連れ去られること)",
        "thinking": "あまりに強烈な喜びや美しさのために、自分の意識が今の場所から強引に「ひったくられ（snatch）」、別次元へと連れ去られてしまった（ecstasyと同質）状態。もはや自分では制御できない、魂の激しい誘拐のような、圧倒的なる歓喜のクライマックスです。",
        "aftertaste": "もう戻れないかもしれない。その一瞬の閃光に、自分をすべて委ねて果てる。",
        "example": "The audience listened in rapture to the young musician's performance.",
        "deep_dive": {
            "roots": [{"term": "rep-", "meaning": "to snatch"}],
            "points": ["rapid（速い：ひったくるような速さ）や rape（強奪/蹂躙）と同じ、暴力的なまでの力強さ。"]
        },
        "part_of_speech": "noun"
    }
]

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
    if match:
        prefix = match.group(1)
        json_array_str = match.group(2)
        suffix = match.group(3)
        
        words = json.loads(json_array_str)
        existing_ids = {w.get("id") for w in words}
        
        added_count = 0
        for item in word_batch:
            if item["id"] not in existing_ids:
                words.append(item)
                added_count += 1
                
        new_json_str = json.dumps(words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Success: Added {added_count} words.")
    else:
        print("Error: Could not find WORDS array in data.js.")
except Exception as e:
    print(f"Error: {e}")
