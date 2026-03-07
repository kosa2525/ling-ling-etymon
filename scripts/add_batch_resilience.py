import json
import re

word_batch = [
    # Cycle 95: Resilience & Endurance
    {
        "id": "fortitude_resilience",
        "word": "Fortitude",
        "meaning": "不撓不屈の精神、忍耐、勇気",
        "era": "14th Century Latin fortis",
        "etymology": {
            "components": ["fortis (strong, brave)"],
            "original_statement": "From Old French fortitude, from Latin fortitudo (strength, force, firmness), from fortis (strong, brave, powerful)."
        },
        "concept": "Strength in pain (痛みや困難の最中にあっても、心が「強く（strong）」あり続けること)",
        "thinking": "一時的な爆発力ではなく、長い間、静かに逆境に耐え抜き、決して信念を曲げない「心の背骨」. 語源の fortis は要塞（Fort）をも指します。攻撃を仕掛けるための強さではなく、自分という内なる城壁を守り抜き、嵐が過ぎ去るのを凛として待つための、静かなる強靭さです。",
        "aftertaste": "折れない背骨。世界があなたを押し潰そうとしても、あなたの内なる要塞は、一寸の綻びも見せることはない。",
        "example": "The family showed incredible fortitude during the difficult months after the accident.",
        "deep_dive": { "roots": [{"term": "bhergh-", "meaning": "high, mountain (possible for fort)"}], "points": ["force（力）や comfort（慰める：共に強くする）と同じ、支えとなる強さのルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "tenacity_resilience",
        "word": "Tenacity",
        "meaning": "粘り強さ、固執、頑強",
        "era": "16th Century Latin tenere",
        "etymology": {
            "components": ["tenere (to hold)"],
            "original_statement": "From Latin tenacitatem (a holding fast), from tenax (holding fast, gripping, tenacious), from tenere (to hold)."
        },
        "concept": "Holding fast (一度掴（つか）んだものを、決して「離さない（hold）」こと)",
        "thinking": "犬が獲物に食らいついて離さないように、目的や夢に対してどこまでも執念深く、泥臭くしがみつき続ける力. 語源の tenere は「保つ」。たとえ周りが諦めても、あなただけはその糸の端を握りしめている。その一見、頑固で融通の利かない執着こそが、不可能な壁に穴を開けるのです。",
        "aftertaste": "離さぬ指先. あなたが握りしめているその小さな希望は、いつかあなた自身を、高みへと引き上げる。",
        "example": "His tenacity in pursuing his goal eventually led to a breakthrough in the research.",
        "deep_dive": { "roots": [{"term": "ten-", "meaning": "to stretch, pull"}], "points": ["tension（緊張）や contain（含む）と同じ、張り詰めた保持のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "perseverance_resilience",
        "word": "Perseverance",
        "meaning": "忍耐、根気、不屈の努力",
        "era": "14th Century Latin per- + severus",
        "etymology": {
            "components": ["per- (very, thoroughly)", "severus (strict, serious, severe)"],
            "original_statement": "From Old French perseverance, from Latin perseverantia (steadfastness, constancy), from perseverare (to continue steadfastly), from per- (very) + severus (strict, serious, severe)."
        },
        "concept": "Thoroughly severe (自らに対して「徹底的に（thoroughly）」「厳しく（severe）」あり続けること)",
        "thinking": "結果が見えない暗闇の中でも、怠けることなく、自分に課した規律を淡々と守り、一歩ずつ進み続けること. 語源の severus は「厳格さ」。それは他者への攻撃性ではなく、自分という素材を最高のものに鍛え上げるための、慈しみのある厳しさです。その継続こそが、やがて岩をも穿（うが）つ水滴となります。",
        "aftertaste": "淡々とした歩み. 派手な勝利はいらない。ただ、昨日よりも一歩だけ前で、明日の朝を迎えよう。",
        "example": "Success in writing requires not just talent, but enormous amounts of perseverance.",
        "deep_dive": { "roots": [{"term": "se-", "meaning": "without"}, {"term": "vuer-", "meaning": "respect, observe (possible for severe)"}], "points": ["severe（厳しい）の根。自分を甘やかさない、透明な規律。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "indomitable_resilience",
        "word": "Indomitable",
        "meaning": "不撓不屈の、屈服しない、負けない",
        "era": "15th Century Latin in- + domitare",
        "etymology": {
            "components": ["in- (not)", "domitare (to tame)"],
            "original_statement": "From Latin indomitabilis (untameable), from in- (not) + domitare (to tame), frequency of domare (to tame)."
        },
        "concept": "Cannot be tamed (誰にも、どんな運命にも「手懐け（tame）」られず、野生のままであること)",
        "thinking": "鎖に繋がれても、翼をもがれても、その魂の誇りだけは誰にも支配させない、猛々（たけだけ）しく気高い意志. 語源は「手懐けられない（untameable）」。あなたは世界の家畜ではなく、自らの運命の王であること。屈服することを知らないその精神は、暗闇の中で最も眩しく輝く星となります。",
        "aftertaste": "野性の誇り。世界はあなたを閉じ込めることはできても、あなたの魂を飼い慣らすことはできない。",
        "example": "The rescue workers showed an indomitable spirit in the face of overwhelming odds.",
        "deep_dive": { "roots": [{"term": "dem-", "meaning": "to house, tame"}], "points": ["dominate（支配する）や domestic（家的な）の反対側。飼いならされぬ生。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "resilience_core",
        "word": "Resilience",
        "meaning": "回復力、弾性、立ち直る力",
        "era": "17th Century Latin re- + salire",
        "etymology": {
            "components": ["re- (back)", "salire (to jump, leap)"],
            "original_statement": "From Latin resiliens, from resilire (to leap back, recoil), from re- (back) + salire (to jump, leap)."
        },
        "concept": "Leaping back (押し潰されても、元の形へと「跳ね（leap）」「戻る（back）」こと)",
        "thinking": "柳のように、しなやかに風を受け流し、折れることなく再び空に向かって立ち上がる力. 語源は「跳ね返る」。傷つかないことではなく、傷ついたあとに、その経験をバネにして以前よりも強く、高く跳び上がること。それは、魂が持つ自己回復のダイナミズムです。",
        "aftertaste": "しなやかな復元。痛みさえも力に変えて、あなたは何度でも、より美しい空へと跳躍する。",
        "example": "Small businesses have shown great resilience in adapting to the changing economic landscape.",
        "deep_dive": { "roots": [{"term": "sel-", "meaning": "to jump"}], "points": ["result（結果：跳ね返り）や salient（顕著な：飛び出した）と同じ、跳躍のルーツ。"] },
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
        print(f"Success: Added {added} words in Cycle 95.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
