import json
import re

word_batch = [
    # Cycle 93: Depth & Profundity
    {
        "id": "fathom_depth",
        "word": "Fathom",
        "meaning": "推し量る、理解する、水深の単位",
        "era": "Old English fæthm",
        "etymology": {
            "components": ["fæthm (outstretched arms, embrace)"],
            "original_statement": "From Old English fæthm (outstretched arms, embrace), from Proto-Germanic fathmaz."
        },
        "concept": "Outstretched arms (両腕を「広げて（embrace）」包み込むこと、そこから深さを測ること)",
        "thinking": "海や心の底. あまりにも深すぎて目には見えないものを、自分の体を極限まで広げ、その「抱擁（embrace）」の距離で必死に推し量ろうとすること。語源は「両腕の広がり」。理解するとは、冷たい論理ではなく、全身を使って対象を包み込み、その存在の大きさを肌で感じることなのです。",
        "aftertaste": "腕のなかの闇。わからないけれど、必死に手を伸ばす。その痛烈なまでの希求が、いつか理解という光を連れてくる。",
        "example": "He found it difficult to fathom the reasons behind her sudden decision to leave.",
        "deep_dive": { "roots": [{"term": "pete-", "meaning": "to spread"}], "points": ["expand（広がる）や patent（明白な：開かれた）と同じ、開放のルーツ。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "profound_depth",
        "word": "Profound",
        "meaning": "深い、深遠な、心からの",
        "era": "14th Century Latin pro- + fundus",
        "etymology": {
            "components": ["pro- (forward, forth)", "fundus (bottom, foundation)"],
            "original_statement": "From Old French profond, from Latin profundus (deep, vast), from pro- (forth) + fundus (bottom, foundation)."
        },
        "concept": "Forward to the bottom (どこまでも「底（bottom）」に向かって、突き抜けるように深いこと)",
        "thinking": "表面的なレベルを遥かに通り越し、存在の「基礎（Foundation）」にまで達している状態. 語源の fundus は農地や底を意味します。深い悲しみ、深い知恵。それは、あなたが築き上げた人生という建物の、最も強固で最も見えにくい「地下室」に触れるような体験です。",
        "aftertaste": "底知れぬ沈黙。深く潜るほど、言葉は重力に耐えかねて消えてゆき、ただ存在の重みだけが残る。",
        "example": "The discovery of the ancient ruins had a profound impact on our understanding of history.",
        "deep_dive": { "roots": [{"term": "bhudhn-", "meaning": "bottom"}], "points": ["fundamental（根本的な）や foundation（基礎）と同じ、揺るぎなき『底』のルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "abstruse_depth",
        "word": "Abstruse",
        "meaning": "難解な、深遠な、秘められた",
        "era": "16th Century Latin ab- + trudere",
        "etymology": {
            "components": ["ab- (away)", "trudere (to push, thrust)"],
            "original_statement": "From Latin abstrusus (hidden, concealed), past participle of abstrudere (to push away, hide), from ab- (away) + trudere (to push)."
        },
        "concept": "Pushed away (人目に触れないように「遠くへ（away）」「押し込む（push）」こと)",
        "thinking": "わざと隠されたわけではないけれど、そのあまりの奥深さゆえに、日常の理解から遠く「押し分けられて」しまっている知識や理論. 語源の trudere は「突き刺す」ような強い力を意味します。理解するためには、あなた自身もまた、思考の森を力強く「突き進む」必要があるのです。",
        "aftertaste": "遠い智慧。それは容易には触れられない。けれど、手を伸ばし続ける者にだけ、その深淵は静かに扉を開く。",
        "example": "The professor's lectures on abstruse mathematical theories were famous but difficult to follow.",
        "deep_dive": { "roots": [{"term": "treud-", "meaning": "to press, push"}], "points": ["intrude（侵入する）や thrust（突き出す）と同じ、抵抗を排除する力のルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "recondite_depth",
        "word": "Recondite",
        "meaning": "深遠な、難解な、あまり知られていない",
        "era": "17th Century Latin re- + condere",
        "etymology": {
            "components": ["re- (back)", "condere (to put together, store, hide)"],
            "original_statement": "From Latin reconditus (hidden, sequestered, concealed), past participle of recondere (to put away, store up, hide), from re- (back) + condere (to put together)."
        },
        "concept": "Put back into storage (一度バラバラにし、誰も知らない奥の部屋に「隠し（hide）」ておくこと)",
        "thinking": "日常の使い古された言葉の棚から一度取り外され、思考の深層にある「秘密の収蔵庫」に保管された知恵. abstruse（押し込まれた）よりも、さらに「大切に守られ、埋没している」ニュアンスが強まります。それは忘れられた古文書の中に眠る、真理の枯れ葉のような知識です。",
        "aftertaste": "埋もれた秘宝。埃をかぶった沈黙のなかで、その知恵は、正しく読み解かれるその時を何世紀も待っている。",
        "example": "He spent years researching recondite points of medieval canon law.",
        "deep_dive": { "roots": [{"term": "dhe-", "meaning": "to set, put"}], "points": ["condition（条件：共に置くもの）や abscond（逃亡する：隠れる）同じ、場所と存在のルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "unfathomable_depth",
        "word": "Unfathomable",
        "meaning": "計り知れない、不可解な、底知れぬ",
        "era": "17th Century English un- + fathom",
        "etymology": {
            "components": ["un- (not)", "fæthm (outstretched arms)"],
            "original_statement": "From un- (not) + fathomable, from fathom."
        },
        "concept": "Cannot be embraced (どんなに両腕を「広げても（embrace）」、決して届かないこと)",
        "thinking": "人間の知性というちっぽけな物差しでは、決してその全貌（ぜんぼう）を捉えることができない、宇宙や運命の巨大さ. 語源の un- は「拒絶」でもあります。測ろうとすればするほど、その深淵はどこまでも遠ざかっていく。それは「知る」ことを諦め、ただ「驚嘆」することだけを許された神域です。",
        "aftertaste": "届かない指先。けれど、届かないからこそ、あなたは星を見上げるように、その深淵に焦がれ続けることができる。",
        "example": "The complexity of the human brain's neural network remains largely unfathomable to scientists.",
        "deep_dive": { "roots": [{"term": "pete-", "meaning": "to spread"}], "points": ["fathom の否定形。限界を知ることが、真の謙虚さと知恵を生む。"] },
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
        print(f"Success: Added {added} words in Cycle 93.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
