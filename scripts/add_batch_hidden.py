import json
import re

word_batch = [
    # Cycle 69: Hidden & Secret things
    {
        "id": "cryptic_hidden",
        "word": "Cryptic",
        "meaning": "謎めいた、秘密の、隠れた",
        "era": "17th Century Greek kryptos",
        "etymology": {
            "components": ["kryptos (hidden, concealed)"],
            "original_statement": "From Latin crypticus, from Greek kryptikos, from kryptos (hidden, concealed)."
        },
        "concept": "Hidden from view (視界から隠され、秘密にされていること)",
        "thinking": "表面（surface）からは見えない場所に、大事な何かが隠されている状態。語源の kryptos は「地下室（crypt）」と同じ。ただ単にわからないのではなく、解読されるのを待っている「意図的な秘密」の香りがします。真実は常に、わかりやすい言葉の裏側に潜んでいるのかもしれません。",
        "aftertaste": "誰もが読める言葉で、誰にも読めない真実を綴る。その一筋縄ではいかない奥行き。",
        "example": "He left a cryptic message on my desk that I couldn't understand at all.",
        "deep_dive": { "roots": [{"term": "krãu-", "meaning": "to hide"}], "points": ["cryptography（暗号学）や apocrypha（外典：隠されたもの）と同じ。見せない美学。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "latent_hidden",
        "word": "Latent",
        "meaning": "潜在的な、潜伏している、見えない",
        "era": "15th Century Latin latere",
        "etymology": {
            "components": ["latere (to lie hidden, lurk, be concealed)"],
            "original_statement": "From Latin latentem, from latere (to lie hidden, lurk)."
        },
        "concept": "Lurking in shadows (影の中に潜み、現れるのを待っている状態)",
        "thinking": "今はまだ目に見えないけれど、条件が整えばいつでも爆発的に現れる準備ができている力。冬の土の下の種子、あるいは人の心に眠る才能。「潜在能力」という言葉が示すように、表に出ていないからこそ、そこには計り知れないエネルギーが凝縮されています。",
        "aftertaste": "見えないことは、存在しないことではない。それは、最高の瞬間のために牙を研いでいる静寂。",
        "example": "The latent heat of evaporation for water is surprisingly high.",
        "deep_dive": { "roots": [{"term": "lā-", "meaning": "to be hidden"}], "points": ["lethargy（無気力：忘却が隠れている状態）とも遠い親戚という説。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "occult_hidden",
        "word": "Occult",
        "meaning": "神秘的な、超自然的な、隠された、オカルト",
        "era": "16th Century Latin occulere",
        "etymology": {
            "components": ["ob- (over)", "celare (to hide)"],
            "original_statement": "From Latin occultus (hidden, concealed, secret), from occulere (to cover over, conceal), from ob- (over) + celare (to hide)."
        },
        "concept": "Covered over from sight (上から何かを被せて、隠し去ること)",
        "thinking": "「隠す（celare）」という言葉に、上から覆う（ob-）が加わった言葉。宇宙の裏側にある秘密の法則や、目に見えない力。ただ見えないだけでなく、何らかの意志によって「隠蔽されている」ニュアンス。それは畏怖と憧れを同時に抱かせる、禁断の知識の香りです。",
        "aftertaste": "開けてはならない扉の向こう。世界は、説明可能な理屈よりも遥かに深い闇で作られている。",
        "example": "The old bookstore specialized in rare manuscripts about the occult sciences.",
        "deep_dive": { "roots": [{"term": "kel-", "meaning": "to hide, cover"}], "points": ["cellar（地下室）や conceal（隠す）、hell（地獄：隠された場所）と同類。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "furtive_hidden",
        "word": "Furtive",
        "meaning": "こっそりした、人目を忍ぶ、泥棒のような",
        "era": "15th Century Latin fur",
        "etymology": {
            "components": ["fur (thief)"],
            "original_statement": "From French furtif, from Latin furtivus (stolen), from furtum (theft), from fur (thief)."
        },
        "concept": "Like a thief (「泥棒」のように人目を盗んで動くこと)",
        "thinking": "見つかることを恐れ、物音を立てずに素早く、しかし怪しく動く様子。誰にも知られたくない欲望や、秘密の行動。語源が「泥棒（fur）」であることから、そこには単なる内気さ（shy）ではなく、規律や視線から逃れようとする、少しスリリングで背徳的な緊張感が漂います。",
        "aftertaste": "視線を盗む。世界がまどろんでいる間に。あなただけの隠れた真実が完成する。",
        "example": "They exchanged a furtive glance across the crowded room.",
        "deep_dive": { "roots": [{"term": "bhor-", "meaning": "to carry (possible)"}], "points": ["ferry（渡し船）と同じ語源から『（盗品を）運び去る』へと派生したという説。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "clandestine_hidden",
        "word": "Clandestine",
        "meaning": "秘密の、内密の、裏の",
        "era": "16th Century Latin clam",
        "etymology": {
            "components": ["clam (secretly)"],
            "original_statement": "From Latin clandestinus (secret, hidden), from clam (secretly, in private)."
        },
        "concept": "Done in private (公ではない「密室」で行われること)",
        "thinking": "「公（public）」の対極にある、ごく限られた人々の間だけで共有される秘密の計画や集まり。語源の clam は「秘密に」という副詞。それは社会のルールや秩序の下に隠れ、歴史を裏側から動かしているかのような、静かで濃密な共謀のニュアンスを含んでいます。",
        "aftertaste": "ささやき声だけの聖域。そこでは、公式の言葉よりも重い約束が交わされる。",
        "example": "The resistance movement held several clandestine meetings in the basement.",
        "deep_dive": { "roots": [{"term": "kel-", "meaning": "to hide, cover"}], "points": ["occult と同じ『隠す（kel-）』の系譜に連なる、闇の言葉の一つ。"] },
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
        print(f"Success: Added {added} words in Cycle 69.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
