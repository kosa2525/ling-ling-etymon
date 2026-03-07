import json
import re

word_batch = [
    # Cycle 90: Silence & Stillness
    {
        "id": "serenity_stillness",
        "word": "Serenity",
        "meaning": "静穏、平穏、落ち着き",
        "era": "15th Century Latin serenus",
        "etymology": {
            "components": ["serenus (clear, fair, bright, calm)"],
            "original_statement": "From Old French serenite, from Latin serenitatem (clearness, serenity), from serenus (clear, bright, calm)."
        },
        "concept": "Clear sky (雲一つない「晴れ渡った空（clear sky）」のような、澄み切った静けさ)",
        "thinking": "激しい感情の波が去ったあと、湖の表面が鏡のように滑らかになり、空の青さをそのまま映し出している状態. 語源の serenus は、天候の良さを指します。外側の世界がどれほど騒がしくても、あなたの内側には、誰にも汚すことのできない、澄み切った青空の領域があるのです。",
        "aftertaste": "澄み切った心。嵐のなかでさえ、あなたの中心には、一筋の光が差し込む静寂の場所がある。",
        "example": "He found great serenity in the early morning walks through the forest.",
        "deep_dive": { "roots": [{"term": "ksero-", "meaning": "dry (possible)"}], "points": ["dry（乾いた）は、雲（湿気）がないことの象徴。曇りのない知性。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "quiescence_stillness",
        "word": "Quiescence",
        "meaning": "静止、休止、沈黙",
        "era": "17th Century Latin quies",
        "etymology": {
            "components": ["quies (rest, quiet)"],
            "original_statement": "From Latin quiescentem, from quiescere (To rest, to be quiet), from quies (rest)."
        },
        "concept": "In a state of rest (活動を止め、深い「安息（rest）」の状態にあること)",
        "thinking": "ただ動かない（Stop）のではなく、生命が次の飛躍に向けて力を蓄え、静かに息を潜めている状態. 氷の下の魚や、冬の土の中の種子。語源の quies は「安らぎ」を意味します。沈黙（Silence）は、雄弁な行動を生むための、神聖な孵化（ふか）の時間なのです。",
        "aftertaste": "休止する命。静けさのなかで、あなたの内なる情熱は、静かに、しかし確実に育まれている。",
        "example": "The stadium was filled with a strange quiescence before the opening whistle blew.",
        "deep_dive": { "roots": [{"term": "kweie-", "meaning": "to rest, be quiet"}], "points": ["quiet（静かな）や quit（辞める：安息に入る）と同じ、停止の美学。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "tacit_stillness",
        "word": "Tacit",
        "meaning": "暗黙の、言わず語らずの",
        "era": "17th Century Latin tacere",
        "etymology": {
            "components": ["tacere (to be silent)"],
            "original_statement": "From Latin tacitus (silent, hidden, secret), past participle of tacere (to be silent)."
        },
        "concept": "Left unspoken (言葉にすることを避け、「沈黙（silent）」のなかに秘めておくこと)",
        "thinking": "言葉にすれば安っぽくなってしまうような、深い信頼や了解. 意味を知る者同士、説明は不要。目はすべてを語り、沈黙が答えを知っている。語源の tacere は、声を殺すこと。あえて語らないことで、コミュニケーションは最も純粋で、最も強固な形（暗黙の了解）へと昇華されます。",
        "aftertaste": "言わずもがなの絆。言葉の届かない深い場所で、私たちはすでに強く結ばれている。",
        "example": "There was a tacit agreement among the team members to never discuss the sensitive incident.",
        "deep_dive": { "roots": [{"term": "tak-", "meaning": "to be silent"}], "points": ["taciturn（無口な）や reticent（控えめな）と同じ。沈黙は武器であり、盾でもある。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "tranquility_stillness",
        "word": "Tranquility",
        "meaning": "静寂、平穏、落ち着き",
        "era": "14th Century Latin trans- + quies",
        "etymology": {
            "components": ["trans- (exceedingly, beyond)", "quies (rest, quiet)"],
            "original_statement": "From Old French tranquilite, from Latin tranquillitatem (quietness, stillness), from tranquillus (quiet, calm, still), probably from trans- (over) + second element from root of quies (rest)."
        },
        "concept": "Beyond all rest (あらゆる安息を「超える（beyond）」ほどの、究極の静けさ)",
        "thinking": "揺らぐことのない、不動の平穏. 語源の trans- が「超越」を意味するように、それは一時的な休みではなく、世界の根底にある永遠の静止に触れている状態です。月面にある「静かの海（Sea of Tranquility）」のように、重力や時間さえも忘れさせる、圧倒的な平安。",
        "aftertaste": "不動の静寂。世界がどれほど狂騒を極めても、あなたの魂は、その不変の安らぎに浸っている。",
        "example": "She sought the tranquility of the countryside to escape the chaos of city life.",
        "deep_dive": { "roots": [{"term": "kweie-", "meaning": "to rest, be quiet"}], "points": ["quiescence と共通の根。より『状態』としての持続性と広がりを感じさせる。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "stasis_stillness",
        "word": "Stasis",
        "meaning": "停滞、静止、均衡状態",
        "era": "18th Century Greek stasis",
        "etymology": {
            "components": ["histani (to set, make to stand)"],
            "original_statement": "From Greek stasis (a standing, a standing still, posture), related to histanai (to set, make to stand)."
        },
        "concept": "Standing still (力が拮抗し、その場に「立っている（stand）」かのように動かないこと)",
        "thinking": "進化や変化が止まっているように見える状態. しかしそれは「死」ではなく、反対方向の巨大な力が完璧にバランスし、互いを打ち消し合っている「極限の緊張状態」でもあります。嵐の前の静けさ、あるいは極限まで加速したコマが止まって見えるような、動的な静止。",
        "aftertaste": "拮抗する静止。動かないのではない。あらゆる方向に進もうとする意志が、今、ここで一つに重なっているのだ。",
        "example": "The diplomatic talks have reached a state of stasis, with neither side willing to make concessions.",
        "deep_dive": { "roots": [{"term": "sta-", "meaning": "to stand"}], "points": ["status（状態）や station（駅）、stable（安定した）と同じ『立つ』ことの力。"] },
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
        print(f"Success: Added {added} words in Cycle 90.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
