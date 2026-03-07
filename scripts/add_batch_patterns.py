import json
import re

word_batch = [
    # Cycle 71: Patterns & Repetition
    {
        "id": "tessellation_pattern",
        "word": "Tessellation",
        "meaning": "テセレーション、モザイク状の模様、敷き詰め",
        "era": "18th Century Latin tessella",
        "etymology": {
            "components": ["tessella (little square stone)"],
            "original_statement": "From Latin tessellatus (checkered), from tessella (little square stone, diminutive of tessera)."
        },
        "concept": "Tiny squares (小さな「四角い石（tessella）」を、隙間なく敷き詰めること)",
        "thinking": "バラバラの破片を、数学的な正確さで並べ直し、全体として一つの巨大で美しい模様（パズル）へと昇華させること。個別の「石」に過ぎなかったものが、他者とぴったりと重なり合うことで、新しい「宇宙（cosmos）」を描き出します。それは世界のパーツが完璧に咬（か）み合った瞬間の、論理的な感動を指しています。",
        "aftertaste": "隙間はない。すべては神聖な数学という名の方程式に導かれ、収まるべき場所へと還る。",
        "example": "M.C. Escher is famous for his incredible artistic tessellations of animals and birds.",
        "deep_dive": { "roots": [{"term": "kwetwer-", "meaning": "four"}], "points": ["quarter（1/4）や square（正方形）と同じく、安定の数『4』のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "reiteration_pattern",
        "word": "Reiteration",
        "meaning": "反復、繰り返し、(強調のための)再三の言明",
        "era": "15th Century Latin re- + iterum",
        "etymology": {
            "components": ["re- (again)", "iterum (again, a second time)"],
            "original_statement": "From Latin reiterationem, from reiteratus, past participle of reiterare, from re- (again) + iterum (again)."
        },
        "concept": "To go over again (同じ場所を、もう一度「何度も（iterum）」なぞること)",
        "thinking": "単なる繰り返し（repeat）ではなく、そこに意志を込めて「二重、三重に」言葉や行動を重ねること。語源の iterum は「もう一度」という、歩き慣れた道に戻る安堵と重みを含みます。一度では伝わらない真理を、執拗なまでの正確さで再び定義し、世界に刻みつけようとする情熱の姿です。",
        "aftertaste": "言葉を重ねる。それがいつしか、揺るぎない確信という名の岩の層になる。",
        "example": "The success of the experiment was due to the careful reiteration of initial procedures.",
        "deep_dive": { "roots": [{"term": "i-", "meaning": "this, that (possible)"}], "points": ["iterate（繰り返す）や item（箇条書き：もう一つのこと）と同類。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "symmetry_pattern",
        "word": "Symmetry",
        "meaning": "対称、釣り合い、美しき均衡",
        "era": "16th Century Greek syn- + metron",
        "etymology": {
            "components": ["sun- (together)", "metron (measure)"],
            "original_statement": "From Latin symmetria, from Greek symmetria (agreement in dimensions), from syn- (together) + metron (measure)."
        },
        "concept": "Measured together (一つの尺度（measure）を「共有（syn-）」していること)",
        "thinking": "左右が鏡合わせのように対等であることの美。それは別々の場所にあるものが、実は同じ一つの中心（軸）を持っているという「合意（agreement）」の表明です。自然界の結晶から蝶の羽根、あるいは人間の顔の美しさ。尺度が一つに重なったとき、カオスは静かなる美に変わります。",
        "aftertaste": "一対の翼。その間の見えない線にこそ、世界の完璧な調和が隠れている。",
        "example": "He admired the perfect symmetry of the snowflakes captured under the microscope.",
        "deep_dive": { "roots": [{"term": "me-", "meaning": "to measure"}], "points": ["geometry（幾何学：地を測る）や meter（計り）と同じ、秩序のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "constellation_pattern",
        "word": "Constellation",
        "meaning": "星座、星の集まり、(輝かしいものの)集団",
        "era": "14th Century Latin con- + stella",
        "etymology": {
            "components": ["com- (together)", "stella (star)"],
            "original_statement": "From Late Latin constellationem, from Latin com- (with, together) + stella (star)."
        },
        "concept": "Stars together (孤独な星々を「一緒に（com-）」結んで、形を描くこと)",
        "thinking": "夜空に散在する点（ドット）を、人間の想像力が一本の線で結び、意味のある形（物語）として捉えること。バラバラな出来事が一つの「不吉な予兆」や「輝かしい運命」へと統合されるプロセス。私たちは物語の中にいたいという本能を、この「星の集い（com-stella）」に投影し続けてきました。",
        "aftertaste": "ただの星。それを星座（ことば）に変えるのは、いつだってあなたの眼差し。",
        "example": "A stunning constellation of international stars gathered for the charity event.",
        "deep_dive": { "roots": [{"term": "ster-", "meaning": "star"}], "points": ["stellar（星の）や asteroid（小惑星：星のようなもの）と同じ『輝き』の連帯。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "mosaic_pattern",
        "word": "Mosaic",
        "meaning": "モザイク、寄せ集めの模様、ミューズの芸術",
        "era": "15th Century Old French/Greek mouseios",
        "etymology": {
            "components": ["mousa (muse, goddess of inspiration)"],
            "original_statement": "From Middle French mosaïque, from Italian mosaico, from Medieval Latin musaicum (work of the Muses), from Greek mouseios (belonging to the Muses)."
        },
        "concept": "Belonging to the Muses (芸術を司る「ミューズ」たちに捧げられた神聖な技法)",
        "thinking": "欠けた破片、色とりどりの石。それ自体は形を持たないガラクタでさえも、ミューズ（Muses）が導けば、壮大な叙事詩の一節へと変貌（変容）します。細かな記憶、感情、挫折。それらを一つも捨てずに敷き詰めて、人生という大きなモザイクを完成させる、その神聖な執念の美学。",
        "aftertaste": "どんな小さな欠片も無駄ではない。いつか、すべてがあの女神に祝福される模様の一部になる。",
        "example": "His new novel is a brilliant mosaic of historical facts and fictional characters.",
        "deep_dive": { "roots": [{"term": "men-", "meaning": "to think"}], "points": ["museum（博物館：ミューズの家）や music（音楽：ミューズの術）と同じ。"] },
        "part_of_speech": "noun"
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
        print(f"Success: Added {added} words in Cycle 71.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
