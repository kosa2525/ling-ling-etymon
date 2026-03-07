import json
import re

word_batch = [
    {
        "id": "serene_calm",
        "word": "Serene",
        "meaning": "穏やかな、晴れ渡った、平静な",
        "era": "16th Century Latin serenus",
        "etymology": {
            "components": ["serenus (clear, bright, fair)"],
            "original_statement": "From Latin serenus (peaceful, calm, clear, unclouded)."
        },
        "concept": "A clear, cloudless sky (一点の曇りもない青空)",
        "thinking": "嵐が去った後の、どこまでも広がる澄み切った空のこと。それは、心が外側の混乱に乱されず、内側から静かな光を放っている状態を指します。平和（peace）よりもさらに深い、透き通るような静寂の境地。感情が凪（なぎ）になったその先に、この美しい透明感があります。",
        "aftertaste": "ただ静かなだけでなく。澄み渡る視界の先に、真実の輪郭が見えてくる。",
        "example": "Beneath her serene appearance, she was deeply thoughtful.",
        "deep_dive": {
            "roots": [{"term": "tsero-", "meaning": "dry (possible)"}],
            "points": ["serum（血清：澄んだ液体）と同じく『余計なものが混じっていない』純粋さ。"]
        },
        "part_of_speech": "adjective"
    },
    {
        "id": "tranquil_calm",
        "word": "Tranquil",
        "meaning": "閑静な、穏やかな、静かな",
        "era": "17th Century Latin tranquillus",
        "etymology": {
            "components": ["trans- (over, across)", "quies (rest, peace)"],
            "original_statement": "From Latin tranquillus (quiet, calm, still, serene), possibly from trans- (over) + quies (rest)."
        },
        "concept": "Crossing over to rest (静寂を「通り抜けて」、安らぎへ至ること)",
        "thinking": "表面的な静かさではありません。心の「向こう側（trans-）」にまで「静止（quies）」が浸透している状態。深い湖の底のように、外界の波風が一切届かない、完璧なる不動の沈黙。そこには、慌ただしい日常を忘れさせるような、永遠の時間の一部が漂っています。",
        "aftertaste": "時が止まったような錯覚。そこでは、自分の鼓動さえも音楽になる。",
        "example": "The village early in the morning was incredibly tranquil.",
        "deep_dive": {
            "roots": [{"term": "kweie-", "meaning": "to rest, be quiet"}],
            "points": ["quiet（静かな）や quit（辞める：安らぐために離れる）と同類。"]
        },
        "part_of_speech": "adjective"
    },
    {
        "id": "solitude_calm",
        "word": "Solitude",
        "meaning": "孤独、ひとりでいること、寂寥",
        "era": "14th Century Old French/Latin solus",
        "etymology": {
            "components": ["solus (alone, single)"],
            "original_statement": "From Old French solitude, from Latin solitudo (loneliness, being alone), from solus (alone)."
        },
        "concept": "The state of being alone (ひとりであるということ、唯一の存在であること)",
        "thinking": "寂しい「loneliness（孤立）」とは違い、あえて一人であることを選び、自らの中に静寂を確保することの気高さ。自分自身という唯一の対話相手と共に過ごす贅沢な時間。それは、他人の視線から解放され、真の自己へと還るためのかけがえのない避難所となります。",
        "aftertaste": "一人は欠乏ではない。それは、自分の全体を取り戻すための聖域。",
        "example": "He often sought the solitude of the ancient library to read.",
        "deep_dive": {
            "roots": [{"term": "swo-", "meaning": "self"}],
            "points": ["sole（唯一の）や solitary（独りきりの）のファミリー。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "stillness_calm",
        "word": "Stillness",
        "meaning": "静止、静寂、平穏",
        "era": "Old English stille",
        "etymology": {
            "components": ["stille (fixed, motionless)"],
            "original_statement": "From Old English stillnes, from stille (fixed, motionless), related to stellan (to place, fix)."
        },
        "concept": "Being fixed in place (その場に固定され、動かない状態)",
        "thinking": "単なる無音ではなく、あらゆる動きがピタリと「固定（fixed）」され、空気さえも微動だにしない状態。それは嵐の前の静けさであり、あるいは瞑想の極致です。止まっているからこそ、世界の一滴（ひとしずく）の音が、心に劇的な響きをもたらすのです。",
        "aftertaste": "ゼロの状態。そこには、すべての可能性が静かにエネルギーを蓄えている。",
        "example": "The uncanny stillness of the lake was like a dark glass mirror.",
        "deep_dive": {
            "roots": [{"term": "stel-", "meaning": "to put, stand"}],
            "points": ["stall（牛舎：置く場所）や install（設置する）と同類。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "composure_calm",
        "word": "Composure",
        "meaning": "落ち着き、平静、沈着",
        "era": "16th Century French/Latin componere",
        "etymology": {
            "components": ["com- (together)", "ponere (to put, set)"],
            "original_statement": "From French composer, from Latin componere (to put together, collect, settle, calm), from com- (together) + ponere (to put)."
        },
        "concept": "Putting parts together (バラバラの自分を「一箇所に」集めて置くこと)",
        "thinking": "パニックになって自分の心や冷静さが散り散りになってしまった時、それらを再びギュッと「一緒に（com-）」集めて、元の正常な位置に「置く（ponere）」こと。それは、自分の内なる中心を再び定義し、混乱を整理整頓した穏やかな強さの状態です。",
        "aftertaste": "パーツを拾い集める。再び、自分という全体が静かに座を占める。",
        "example": "She maintained her composure despite the heavy pressure of the trial.",
        "deep_dive": {
            "roots": [{"term": "apo-", "meaning": "off, away (possible)"}],
            "points": ["pose（姿勢：置かれた形）や position（位置）と同じルーツ。"]
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
