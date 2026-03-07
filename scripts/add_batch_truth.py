import json
import re

word_batch = [
    # Cycle 74: Authenticity & Truth
    {
        "id": "candid_truth",
        "word": "Candid",
        "meaning": "率直な、ありのままの、公平な",
        "era": "17th Century Latin candidus",
        "etymology": {
            "components": ["candidus (shining white)"],
            "original_statement": "From French candide, from Latin candidus (shining white, clear, bright, fair, spotless)."
        },
        "concept": "Shining white (一点の汚れもない「真っ白に」輝くこと)",
        "thinking": "装飾や嘘を一切削ぎ落とし、ただ純粋な「白（white）」としてそこに存在すること。語源の candidus は、自分を偽らず光り輝いている様を指し、政治の候補者（candidate）がかつて白いトガを着て潔白を示したことに由来します。ありのままの自分を晒け出す勇気。それが真の率直さです。",
        "aftertaste": "濁りのない言葉。それは、鏡のように相手の心をも透明にしてゆく。",
        "example": "To be perfectly candid, I don't think his plan is going to work as expected.",
        "deep_dive": { "roots": [{"term": "kand-", "meaning": "to shine"}], "points": ["candle（キャンドル）や incense（お香：燃えて輝くもの）と同じ『白く光る』ルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "sincere_truth",
        "word": "Sincere",
        "meaning": "誠実な、心からの、偽りのない",
        "era": "16th Century Middle French/Latin sincerus",
        "etymology": {
            "components": ["sine- (without)", "cera (wax) - traditional folk etymology"],
            "original_statement": "From Middle French sincere, from Latin sincerus (whole, clean, pure, sound, not spoiled, unadulterated), traditionally said to be from sine cera (without wax)."
        },
        "concept": "Without wax (「蝋（wax）」で傷を隠していない、純粋なままであること)",
        "thinking": "（諸説ありますが）彫刻の傷やひび割れを蝋で隠さず、そのまま（pure）であることに由来するという説があります。欠点を隠そうとする作為がなく、内側と外側が一致している状態。それは技術ではなく、全存在をかけた「純度（unadulterated）」の証明です。",
        "aftertaste": "混ぜ物のない心。そのままのあなたでいることが、世界にとっての最高の誠実さ。",
        "example": "Please accept our sincere apologies for the delay and any inconvenience caused.",
        "deep_dive": { "roots": [{"term": "sim-", "meaning": "one, original"}, {"term": "ker-", "meaning": "to grow (possible)"}], "points": ["simple（単純な：一つの層）と同じく、元々の姿のまま成長していること。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "veracity_truth",
        "word": "Veracity",
        "meaning": "真実性、誠実、正確さ",
        "era": "17th Century French/Latin verus",
        "etymology": {
            "components": ["verus (true)"],
            "original_statement": "From French véracité, from Latin veracitatem, from verax (truthful), from verus (true)."
        },
        "concept": "The state of being true (物事が「真実（true）」そのものであるという確かな属性)",
        "thinking": "単なる情報の正確さだけでなく、その人が常に真実を語ろうとする「本質的な誠実さ」。語源の verus は「真の」を意味し、揺るぎない確固たる基盤を指します。複雑な解釈や物語で飾る前の、むき出しの事実そのものが放つ、重厚な説得力。",
        "aftertaste": "真実という名の石。それは、長い年月を経ても風化することなく、そこにあり続ける。",
        "example": "The committee began to question the veracity of her testimony after new evidence surfaced.",
        "deep_dive": { "roots": [{"term": "wer-", "meaning": "true, trustworthy"}], "points": ["verify（検証する）や verdict（評決：真実を言うこと）と同じ『誓い』のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "integrity_truth_2",
        "word": "Authenticity",
        "meaning": "真正であること、本物であること、自分らしさ",
        "era": "17th Century Greek authentes",
        "etymology": {
            "components": ["autos (self)", "hentes (doer, being)"],
            "original_statement": "From Greek authentikos (original, genuine, principal), from authentes (one who acts with his own authority), from autos (self) + hentes (doer, executor)."
        },
        "concept": "A self-doer (他者の指示ではなく、自らの「自己（self）」によって成されること)",
        "thinking": "他人のコピーでも、社会に求められた役割でもなく、純粋に自らの「内なる権威」から生じたものであること。それが「本物」の証明です。自分が自分の人生の「実行者（doer）」であることの、剥き出しの輝き。それは模倣できない、唯一無二の命のサインです。",
        "aftertaste": "あなた以外には成し得ない何か。それこそが、この世界が必要としている唯一の『正解』。",
        "example": "The restaurant is well known for the authenticity of its traditional Japanese cuisine.",
        "deep_dive": { "roots": [{"term": "sen-", "meaning": "to accomplish, prepare"}], "points": ["self（自己）が主体となって何かを『完成させる』ことへの、古代からの敬意。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "naive_truth",
        "word": "Naive",
        "meaning": "純真な、素朴な、世間知らずの",
        "era": "17th Century French/Latin nativus",
        "etymology": {
            "components": ["nativus (innate, natural, native)"],
            "original_statement": "From French naïve, feminine of naïf, from Old French naif (natural, native, simple, raw), from Latin nativus (innate, natural)."
        },
        "concept": "Native and natural (生まれたままの「素（raw）」のままであること)",
        "thinking": "現代では「世間知らず」という否定的なニュアンスもありますが、本来は「生まれたまま（native）」の純粋さを保っていることへの賛辞でした。教育や経験によって「加工」される前の、野生のままの瑞々しい感性。それは世界を初めて見る子供のような、もっとも神聖に近い眼差しです。",
        "aftertaste": "汚れなき初期衝動。常識を身につける前の、真っさらな驚きという名の宝物。",
        "example": "I was very naive back then, thinking I could change the whole world in just a year.",
        "deep_dive": { "roots": [{"term": "gene-", "meaning": "to give birth"}], "points": ["nature（自然）や nation（国家：生まれた場所）と同じ『誕生』の系譜。"] },
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
        print(f"Success: Added {added} words in Cycle 74.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
