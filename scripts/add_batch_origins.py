import json
import re

word_batch = [
    # Cycle 78: Origins & Foundations
    {
        "id": "blueprint_origin",
        "word": "Blueprint",
        "meaning": "設計図、青写真、計画の基礎",
        "era": "19th Century English blue + print",
        "etymology": {
            "components": ["blue (color)", "print (impression)"],
            "original_statement": "From the white-on-blue photographic print used for architectural plans, originally produced using the cyanotype process."
        },
        "concept": "A white impression on blue (青地に刻まれた、未来の「形」の記録)",
        "thinking": "建物が建つ前に、そのすべての骨組みと運命が記された場所。単なる図面ではなく、壮大な構想が現実へと降下するための「最初の接点」です。あなたの人生にも、自分では気づかない深い場所に、魂が描いたこの「青写真」が静かに眠っているのかもしれません。",
        "aftertaste": "見えない線。何かが形になるその前に、意志はすでに地図を描き終えている。",
        "example": "The government unveiled a new blueprint for the nation's economic recovery.",
        "deep_dive": { "roots": [{"term": "bhle-", "meaning": "blue (possible)"}, {"term": "premu-", "meaning": "to press"}], "points": ["cyanotype（青写真法）の化学から生まれた、近代の『始まり』のメタファー。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "rudiment_origin",
        "word": "Rudiment",
        "meaning": "基本、基礎、(生物の)痕跡器官",
        "era": "16th Century Latin rudis",
        "etymology": {
            "components": ["rudis (unskilled, rough, raw)"],
            "original_statement": "From Latin rudimentum (early training, first principle), from rudis (unskilled, rough, raw)."
        },
        "concept": "A raw beginning (未加工で「粗い（raw）」ままの、最初の原理)",
        "thinking": "洗練される前の、むき出しの土台。どんな高度な技術や知識も、最初は誰にも理解されないような「粗削り（rough）」な小さな一歩から始まります。それは未熟さの象徴ではなく、無限の成長を内に秘めた、もっとも力強い生命の種子の姿です。",
        "aftertaste": "粗い土。そこからしか、空を突くような大樹は育つことができない。",
        "example": "She quickly mastered the rudiments of the Italian language before her trip to Rome.",
        "deep_dive": { "roots": [{"term": "reud-", "meaning": "to clear land (possible)"}], "points": ["rude（失礼な：粗野な）と同じ。磨かれる前の本質の輝き。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "infrastructure_origin",
        "word": "Infrastructure",
        "meaning": "インフラ、基盤、下層構造",
        "era": "20th Century French/Latin infra- + struere",
        "etymology": {
            "components": ["infra- (below)", "struere (to build, pile up)"],
            "original_statement": "From French infrastructure, from infra- (below) + structure."
        },
        "concept": "Building below (目に見える世界の「下（below）」で築き上げられているもの)",
        "thinking": "華やかな都市の地下で、水を運び、電気を灯し、繋がりを支える、決して表には出ない構造。私たちの思考や感情も、過去の経験や言葉という強固な「インフラ」の上に成り立っています。機能している時はその存在を忘れますが、失われた時、初めてその絶対的な重みを知るのです。",
        "aftertaste": "縁の下の意志。静かなる支え。それがあるから、あなたは今日、空を見上げて歩くことができる。",
        "example": "Investment in transport infrastructure is crucial for the long-term growth of the city.",
        "deep_dive": { "roots": [{"term": "n-dhers-", "meaning": "under"}, {"term": "stere-", "meaning": "to spread"}], "points": ["structure（構造）を下で支える、広大な見えない大地。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "primordial_origin",
        "word": "Primordial",
        "meaning": "原始の、根本的な、根源的な",
        "era": "14th Century Latin primus + ordiri",
        "etymology": {
            "components": ["primus (first)", "ordiri (to begin)"],
            "original_statement": "From Latin primordialis (first of all, original), from primordium (the first beginning), from primus (first) + ordiri (to begin a web, lay a warp)."
        },
        "concept": "First weaving (織物の最初の「経糸（warp）」を張ること)",
        "thinking": "宇宙の始まり、あるいは生命が最初に海から這い上がった時の、あの原初的なエネルギー。語源の ordiri は「機織りを始める」ことを意味します。それは、混沌とした糸の集まりから、世界という物語を織り成す「最初の一筋」を引く、神聖な創造の瞬間です。",
        "aftertaste": "最初の震え。すべてが始まる瞬間の、あの圧倒的な熱量と静寂を、私たちは今も体の奥底に覚えている。",
        "example": "The scientists are studying the primordial gases that existed during the formation of the universe.",
        "deep_dive": { "roots": [{"term": "preis-", "meaning": "before"}, {"term": "ar-", "meaning": "to fit together"}], "points": ["order（秩序）のルーツは『織ること』にあるという、驚くべき符号。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "threshold_origin_2",
        "word": "Genesis",
        "meaning": "創世、起源、発生",
        "era": "Old English Greek gignere",
        "etymology": {
            "components": ["gignesthai (to be born, become)"],
            "original_statement": "From Latin genesis (generation, nativity), from Greek genesis (origin, source, manner of birth), from gignesthai (to be born)."
        },
        "concept": "The act of being born (何かが新しく「生まれる（be born）」、その爆発的なプロセス)",
        "thinking": "何もない空白の中に、突然パチリと光が灯るような始まり。ただの開始（start）ではなく、それが命を宿し、自律的に動き出し、成長してゆく「誕生」のニュアンス。あなたの新しいアイデア、新しい恋、新しい今日。そのすべてが、小さな『ジェネシス』の連続です。",
        "aftertaste": "産声。暗闇を裂いて現れる閃き。それは、世界が再び新しくなるための約束。",
        "example": "The genesis of the idea for his new novel came to him during a long walk in the rain.",
        "deep_dive": { "roots": [{"term": "gene-", "meaning": "to give birth"}], "points": ["genius（天才：生まれ持った精霊）や gene（遺伝子）と同じ、生成の神秘。"] },
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
        print(f"Success: Added {added} words in Cycle 78.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
