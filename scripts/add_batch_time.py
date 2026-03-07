import json
import re

word_batch = [
    {
        "id": "eon_time",
        "word": "Eon",
        "meaning": "永久、果てしない時間、地質学の累代",
        "era": "17th Century Greek aion",
        "etymology": {
            "components": ["aion (age, vital force, eternity)"],
            "original_statement": "From Greek aion (age, vital force, eternity), from PIE root *aiw- (vital force, life, long life, eternity)."
        },
        "concept": "The vital force of time (生命力そのものとしての、永劫の時間)",
        "thinking": "ただのカレンダー的な時間ではなく、生命が脈打ち、宇宙が呼吸し続ける「永劫の発露」そのもの。一人の人間の一生を「age」とするならば、無数の生と死が折り重なって形成される巨大な時間の織物が「eon」です。個人を超えた、計り知れない厚みの物語。",
        "aftertaste": "一瞬の瞬き。その中に、全宇宙の累代（eon）が宿っている。",
        "example": "The landscape has remained virtually unchanged for eons.",
        "deep_dive": {
            "roots": [{"term": "aiw-", "meaning": "vital force, life, long life"}],
            "points": ["ever（永遠に）や age（時代）と同じ。生きている時間の強さ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "ephemeral_time",
        "word": "Ephemeral",
        "meaning": "一日限りの、儚い、短命な",
        "era": "16th Century Greek epi- + hemera",
        "etymology": {
            "components": ["epi- (upon)", "hemera (day)"],
            "original_statement": "From Greek ephemeros (lasting only a day), from epi- (upon) + hemera (day)."
        },
        "concept": "Upon a single day (たった「一日（hemera）」の上に置かれた命)",
        "thinking": "カゲロウのように、朝日と共に生まれ、夕日と共に消えてゆく命の宿命。それは「儚さ（fragility）」の象徴ですが、一日という限られた時間にすべてを注ぎ込む「瞬間の密度」をも意味します。永遠ではないからこそ、その一瞬は宝石よりも輝かしい。",
        "aftertaste": "明日がないからこそ、今、この光にすべてを捧げる美しさ。",
        "example": "Instagram 'Stories' are the modern version of ephemeral communication.",
        "deep_dive": {
            "roots": [{"term": "amer-", "meaning": "day (possible)"}],
            "points": ["ephemera（一過性のもの/カゲロウ）そのものの根源。"]
        },
        "part_of_speech": "adjective"
    },
    {
        "id": "interim_time",
        "word": "Interim",
        "meaning": "中間、暫定的な、合間",
        "era": "16th Century Latin inter + im",
        "etymology": {
            "components": ["inter (between)", "im (that, there - archaic)"],
            "original_statement": "From Latin interim (in the meantime), from inter (between) + im (that)."
        },
        "concept": "In between that (あのことと、このことの「間」にあるとき)",
        "thinking": "何かが終わり、次の何かが始まるまでの「宙ぶらりん」な時間。それは、不確かで不安定な期間ですが、同時に何にでもなれる「可能性の隙間」でもあります。完成品（permanent）ではないからこその、しなやかな適応と、期待に満ちた静止。",
        "aftertaste": "準備の季節。空白があるからこそ、新しい旋律を書き込める。",
        "example": "He served as the interim manager until a successor was found.",
        "deep_dive": {
            "roots": [{"term": "en-ter-", "meaning": "between"}],
            "points": ["internal（内部の）や international（国際的な：間の）と同類の境界のルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "synchronicity_time",
        "word": "Synchronicity",
        "meaning": "共時性、シンクロニシティ、意味のある偶然の一致",
        "era": "20th Century coined by C.G. Jung/Greek syn- + khronos",
        "etymology": {
            "components": ["syn- (together)", "khronos (time)"],
            "original_statement": "Coined by psychologist Carl Jung, from Greek syn- (together, with) + khronos (time)."
        },
        "concept": "Happening together in time (同じ「時間」に、意味が寄り添うこと)",
        "thinking": "原因と結果（因果律）では説明できないけれど、心の内側で思っていたことが、外の世界で現実として同時に（syn-）起こる不思議な一致。時間はただ流れる川ではなく、時として複数の出来事が一つの「意味」という渦の中で出会う場所であることを教えてくれます。",
        "aftertaste": "世界はバラバラではない。見えない糸が、同じ瞬間の深みで繋がっている。",
        "example": "Jung believed that synchronicity was a clue to the deeper order of the universe.",
        "deep_dive": {
            "roots": [{"term": "gher-", "meaning": "to grasp, enclose (possible)"}],
            "points": ["chronicle（年代記）や chronic（慢性の）の chron- は、時間を『掴み、区切る』もの。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "legacy_time",
        "word": "Ancestry",
        "meaning": "祖先、系譜、家系",
        "era": "14th Century Old French/Latin ante- + cedere",
        "etymology": {
            "components": ["ante- (before)", "cedere (to go)"],
            "original_statement": "From Old French ancesserie, from ancestre, from Latin antecessor (predecessor), from ante- (before) + ceder (to go)."
        },
        "concept": "Those who went before (自分より先に「道（cede）」を歩いた人々)",
        "thinking": "ただの過去の記録ではありません。今のあなたの指の形、声の響き、そして思考の癖の中にさえ、かつて「前（ante-）」を歩いていた人々の足跡が刻まれています。途方もない時間のバトンリレーの最前線に、今のあなたが立っているという壮大な継続の物語です。",
        "aftertaste": "何千もの人生を背負って。一歩踏み出すたび、彼らの意志が共に動く。",
        "example": "She felt a profound connection to her Irish ancestry while visiting Cork.",
        "deep_dive": {
            "roots": [{"term": "anti-", "meaning": "facing, before"}, {"term": "ked-", "meaning": "to go, yield"}],
            "points": ["predecessor（前任者）や proceed（進む）と同類の、前進する魂の系譜。"]
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
