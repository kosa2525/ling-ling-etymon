import json
import re

word_batch = [
    {
        "id": "companion",
        "word": "Companion",
        "meaning": "仲間、連れ、コンパニオン",
        "era": "12th Century Old French/Late Latin companiō",
        "etymology": {
            "components": ["com- (with)", "panis (bread)"],
            "original_statement": "From Late Latin companiō, through Old French compagnon. Literally 'with bread', meaning one who shares bread with another."
        },
        "concept": "One who shares bread (パンを分かち合う者)",
        "thinking": "ただの友人ではなく、生活の糧である「パン（panis）」を「共に（com-）」食べる仲。衣食住の核心を共有し、リスクも喜びも等分にする深い信頼関係の呼称です。会社（company）もこの言葉から生まれました。",
        "aftertaste": "一つのパンをちぎり、無言で渡す。それが真の信頼。",
        "example": "His dog was his constant companion during the long journey.",
        "deep_dive": {
            "roots": [{"term": "pa-", "meaning": "to feed, nourish"}],
            "points": ["pantry（パントリー：パンを置く場所）や pasture（牧草地：飼料を与える場所）と同族です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "courage",
        "word": "Courage",
        "meaning": "勇気、度胸",
        "era": "13th Century Old French/Latin cor",
        "etymology": {
            "components": ["cor (heart)", "-aticum (action/state)"],
            "original_statement": "From Old French corage (heart, spirit, courage), from cor (heart)."
        },
        "concept": "The spirit of the heart (心の力、心臓の鼓動の強さ)",
        "thinking": "単に「怖くない」ことではなく、恐怖に震えながらも、自分の内なる一番核心である「心（cor）」の命じるままに踏み出すこと。元々は知性や精神性よりも、胸騒ぎや魂の熱さを指す言葉でした。",
        "aftertaste": "震える心。それでも一歩前に出る、熱い血の叫び。",
        "example": "It takes a lot of courage to stand up for what you believe in.",
        "deep_dive": {
            "roots": [{"term": "ker-", "meaning": "heart"}],
            "points": ["cardiac（心臓の）や cordial（心からの）と同じ情熱の源泉です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "journey",
        "word": "Journey",
        "meaning": "旅、旅路、道のり",
        "era": "13th Century Old French journee",
        "etymology": {
            "components": ["diurnus (of the day)"],
            "original_statement": "From Old French journee (a day's work, a day's travel), from Latin diurnus (daily), from dies (day)."
        },
        "concept": "A day's travel (一日の旅、一日の行程)",
        "thinking": "本来は「一生の旅」のような長いものではなく、「一日（day：jour）」で移動できる距離、あるいは「一日分」の仕事そのものを指しました。その一日分の『一歩』を積み重ねていく姿が、今の『人生という旅路』に繋がっています。",
        "aftertaste": "目的地は遠くとも、今日一日分の歩みに意味を込めて。",
        "example": "The journey of a thousand miles begins with a single step.",
        "deep_dive": {
            "roots": [{"term": "dyeu-", "meaning": "to shine, day"}],
            "points": ["diary（日記）や journal（雑誌：日々の記録）と同じく『一日の光』の物語。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "treasure",
        "word": "Treasure",
        "meaning": "宝物、財産、大事にする",
        "era": "12th Century Old French/Greek thesauros",
        "etymology": {
            "components": ["tithenai (to put, set, place)"],
            "original_statement": "From Old French tresor, from Latin thesaurus, from Greek thesauros (a treasure, treasury, storehouse), originally a place where things are put."
        },
        "concept": "A place where things are put away (大切にしまわれた場所、保管所)",
        "thinking": "もともとは金銀財宝そのものではなく、「大切なものをしまっておく『隠し場所（storehouse）』」を指していました。そこから、中にしまわれた「光り輝く価値あるもの」へと意味が転じていった、ワクワクするような秘密の響きを持つ言葉です。",
        "aftertaste": "誰も知らない場所。あなただけに輝く、しまっておきたい何か。",
        "example": "Life's most precious treasures are our memories.",
        "deep_dive": {
            "roots": [{"term": "dhe-", "meaning": "to set, put"}],
            "points": ["thesis（論文：ある地点に置かれた定立）の thes- は同じルーツです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "wisdom",
        "word": "Wisdom",
        "meaning": "知恵、分別、賢明さ",
        "era": "Old English wisdom",
        "etymology": {
            "components": ["wis (wise)", "-dom (state, condition)"],
            "original_statement": "From Old English wisdom (wise, learned property, cunning), from wis (wise)."
        },
        "concept": "The state of being wise (賢いという状態)",
        "thinking": "Knowledge（知識）が集めるだけの情報の断片なら、Wisdomはそれらを人生の視点（vision）をもって使いこなす力。語源の wis は「見る（vision）」に関係し、表面だけではなく「物事の深層を正しく見抜く力」を意味しています。",
        "aftertaste": "ただ知るのではない。瞳で捉えたその先を、見通す力。",
        "example": "He had the wisdom to walk away when the situation became dangerous.",
        "deep_dive": {
            "roots": [{"term": "weid-", "meaning": "to see"}],
            "points": ["history（歴史：知って見ること）の -tory や vision（視界）と同じ『目』の源流。"]
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
