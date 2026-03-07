import json
import re

word_batch = [
    {
        "id": "yearning_emotion",
        "word": "Yearning",
        "meaning": "切望、あこがれ、思慕",
        "era": "Old English giernan",
        "etymology": {
            "components": ["georn (eager, desirous)"],
            "original_statement": "From Old English giernan (to strive, be eager, desire), from Proto-Germanic *gernjan, from *gernaz (eager)."
        },
        "concept": "A striving from the heart (心の底からの、熱心でひたむきな渇望)",
        "thinking": "ただ「欲しい（want）」のではなく、何かに向かって「奮闘（strive）」するような重厚な思い。自分の中に欠けている何かを埋めるために、魂が手足を伸ばそうとするエネルギー。それは切なく、苦しいけれど、自分を遠くの光へと導いてくれる純粋な加速装置のような感情です。",
        "aftertaste": "届かないけれど、手を伸ばさずにはいられない。その痛みこそが、人間であるという証。",
        "example": "He had a deep yearning for the mountains of his native land.",
        "deep_dive": {
            "roots": [{"term": "gher-", "meaning": "to desire"}],
            "points": ["greedy（欲張りな）や eager（熱心な）と同じ『熱烈に求める』ルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "infatuation_emotion",
        "word": "Infatuation",
        "meaning": "のぼせ上がること、盲目的な恋",
        "era": "16th Century Latin fatuus",
        "etymology": {
            "components": ["in- (into)", "fatuus (foolish)"],
            "original_statement": "From Latin infatuatus, past participle of infatuare (to make a fool of), from in- (into) + fatuus (foolish)."
        },
        "concept": "Falling into folly (愚かさ（愚者）の「中」へとはまり込むこと)",
        "thinking": "あまりの情熱によって、本来の賢さを失い、「愚か者（fatuus）」の領域に足を踏み入れてしまった状態。自分を失い、相手という幻影に心を奪われ、理性という灯りが消えてしまった、一時的な眩（くら）みの物語。それは人生における熱烈で、しかし儚い真夏の夜の出来事です。",
        "aftertaste": "愚かで、狂おしい。だからこそ、その盲目の時間は、永遠から盗み取った魔法のように輝く。",
        "example": "His intense infatuation with the famous actress was the talk of the town.",
        "deep_dive": {
            "roots": [{"term": "bhwa-", "meaning": "to speak, blow, light (possible)"}],
            "points": ["fatuous（愚か/バカげた）や fatuity、あるいは fatuous（火の玉：鬼火）とも関連がある、理性の欠如のルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "remorse_emotion",
        "word": "Remorse",
        "meaning": "後悔、自責の念",
        "era": "14th Century Old French/Latin remordere",
        "etymology": {
            "components": ["re- (again)", "mordere (to bite)"],
            "original_statement": "From Old French remors, from Medieval Latin remorsus, from Latin remordere (to bite again, vex), from re- (again) + mordere (to bite)."
        },
        "concept": "Biting again (良心が何度も自分を「噛み」続けること)",
        "thinking": "過去の過ちを思い出すたびに、良心の呵責（かしゃく）が「もう一度（re-）」自分の心を「ガブリと噛じ（mordere）」続けてくる苦しみ。一度では終わらず、静かな夜の闇と共に、何度も繰り返される内なる痛み。それは、自分の誠実さを取り戻そうとするための、激しい自浄作用かもしれません。",
        "aftertaste": "噛み跡から。痛みと共に、新しい生き方が静かに流れ出してゆく。",
        "example": "He felt a wave of deep remorse for the harsh words spoken in anger.",
        "deep_dive": {
            "roots": [{"term": "merd-", "meaning": "to rub, crush, bite"}],
            "points": ["mordant（毒舌な/腐食性の）や mordant（噛じるもの）のルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "serendipity_emotion",
        "word": "Serendipity",
        "meaning": "素敵な偶然、掘り出し物を見つける才能",
        "era": "18th Century coined by Horace Walpole",
        "etymology": {
            "components": ["Serendip (old name for Sri Lanka)"],
            "original_statement": "Coined by Horace Walpole in a letter to a friend, based on the Persian fairy tale 'The Three Princes of Serendip'."
        },
        "concept": "Finding what you were not looking for (探していなかった「もっと良いもの」を見つける旅の喜び)",
        "thinking": "物語の中で王子たちが、意図せずとも、英知と偶然によって常に価値あるものを発見し続けたことに由来します。計画通りにいかないことを嘆くのではなく、予定外の出来事こそが宝物だったと気づく「受容と発見の才能」。不意打ちの幸運を愛する心です。",
        "aftertaste": "目的地への迷路。その途中の失敗こそが、世界からの最高のプレゼントかもしれない。",
        "example": "Finding the rare old book in a random bookstore was a pure serendipity.",
        "deep_dive": {
            "roots": [],
            "points": ["完全なる造語ですが、現在は世界で最も翻訳が困難で美しい言葉の一つとして認知されています。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "solace_emotion",
        "word": "Solace",
        "meaning": "慰め、安らぎ、心地よい静寂",
        "era": "13th Century Old French/Latin solari",
        "etymology": {
            "components": ["solari (to console, soothe)"],
            "original_statement": "From Old French solas, from Latin solacium (a soothing, comforting, solace), from solari (to console)."
        },
        "concept": "A soothing for the soul (傷ついた魂を優しく撫で、沈めること)",
        "thinking": "嵐のような悲しみや疲れが引いた後、たった一つの穏やかな光や音楽によって得られる、静かで深い和らぎ。それは解決策（solution）ではなく、ただ寄り添ってくれる「癒やし（solace）」。何も言わずに隣に座っていてくれるような、そんな温もりの感覚のことです。",
        "aftertaste": "何も変わらなくても、心がふわりと軽くなる。ただそれだけで、救いになる。",
        "example": "She found solace in the quiet pages of the old family journals.",
        "deep_dive": {
            "roots": [{"term": "sel-", "meaning": "to reconcile, satisfy (possible)"}],
            "points": ["console（慰める）と同じ。共に座って安泰を築くこと。"]
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
