import json
import re

word_batch = [
    {
        "id": "covenant_rule",
        "word": "Covenant",
        "meaning": "誓約、契約",
        "era": "14th Century Old French/Latin convenire",
        "etymology": {
            "components": ["con- (together)", "venire (to come)"],
            "original_statement": "From Old French covenant, from convenio (to come together, agree, unite)."
        },
        "concept": "A coming together of minds (心が集まる、一堂に会する誓い)",
        "thinking": "法的な契約（contract）よりも宗教的で、魂の重みを伴う重大な約束。二つの意志が一点で「出会い（convenire）」、一つの運命を共にすることの宣言です。かつては人間と神との間の聖なる約束を指し、破ることのできない厳粛な絆を意味しました。",
        "aftertaste": "形式だけではない。同じ地点に出会った、魂の調印。",
        "example": "Marriage is often seen as a spiritual covenant between two people.",
        "deep_dive": {
            "roots": [{"term": "gwa-", "meaning": "to go, come"}],
            "points": ["avenue（並木道：至る場所）や adventure（冒険：来るもの）と同族。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "statute_rule",
        "word": "Statute",
        "meaning": "制定法、法令、成文化された規定",
        "era": "14th Century Old French/Latin statutus",
        "etymology": {
            "components": ["statuere (to cause to stand, set up, establish)"],
            "original_statement": "From Old French statut, from Latin statutum (law, decree), from statutus, from statuere (to set up, establish)."
        },
        "concept": "Something established to stand (揺るぎなく「立たされた」規定)",
        "thinking": "浮足立った口約束ではなく、紙の上に文字として刻まれ、何者にも動かされないように「立てられた（statuere）」構造物。それは、気まぐれな力から人々の正義を守るために設置された、文明の不変の柱のような存在を指します。",
        "aftertaste": "誰もが、その不動の言葉の影で平等に守られる。",
        "example": "There are several federal statutes regarding child labor and rights.",
        "deep_dive": {
            "roots": [{"term": "sta-", "meaning": "to stand"}],
            "points": ["statue（彫像）や standard（標準：立っている目印）と同じルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "sanction_rule",
        "word": "Sanction",
        "meaning": "制裁、是認、認可、承認する",
        "era": "16th Century Latin sancire",
        "etymology": {
            "components": ["sancire (to make sacred, decree, confirm, ratify)"],
            "original_statement": "From Latin sanctionem (a decree, law, ordinance), from sancire (to make sacred, ratify)."
        },
        "concept": "Making something sacred (神聖化された決定、不可侵の法規定)",
        "thinking": "「制裁」と「承認」、相反する二つの意味を持つ不思議な言葉。共通するのは「ある行為を『公式』な法として神聖（sacred）に確認する」ということ。法を侵す者に罰を与えることも、正しい行為とお墨付きを与えることも、すべては厳粛な決定に基づいています。",
        "aftertaste": "公式のハンコが押された瞬間、ただの行為は法となる。",
        "example": "The government imposed harsh economic sanctions on the attacking country.",
        "deep_dive": {
            "roots": [{"term": "sak-", "meaning": "to sanctify"}],
            "points": ["sacred（神聖な）、saint（聖人）と同じく『聖域化』がルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "legacy_society",
        "word": "Heritage",
        "meaning": "遺産、伝統、継承物",
        "era": "13th Century Old French/Latin heres",
        "etymology": {
            "components": ["heres (heir)"],
            "original_statement": "From Old French heritage, from heriter (to inherit), from Late Latin hereditare, from heres (heir, successor)."
        },
        "concept": "What an heir is destined to receive (跡継ぎが受け取る運命のもの)",
        "thinking": "個人が残す「legacy」に対し、より広い「社会や民族全体が受け継ぐもの」というスケールを持つ言葉。建物、記憶、芸術。それは「跡継ぎ（heir）」としての誇りを持ち、未来へと繋ぐべきバトンのような、重みと誇りに満ちた輝きのある贈り物です。",
        "aftertaste": "過去のすべての努力が結晶となり、今のあなたの価値を形作っている。",
        "example": "The city is very proud of its rich architectural heritage.",
        "deep_dive": {
            "roots": [{"term": "gher-", "meaning": "to take, seize (possible)"}],
            "points": ["heir（相続人）は『掴み取る者』という意味。手を差し出して受け継ぐイメージ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "citizen_society",
        "word": "Citizen",
        "meaning": "市民、国民、住民",
        "era": "14th Century Old French/Latin civitas",
        "etymology": {
            "components": ["civitas (city-state)", "civis (member of the state)"],
            "original_statement": "From Old French citeien, based on cite (city), from Latin civitatem (city-state, assembly of citizens)."
        },
        "concept": "A member of the city (都市を構成する細胞、一員)",
        "thinking": "ただその土地に住んでいるというだけではなく、「都市（city/civitas）」という一つの巨大な共同体を守り、形作る責任と権利を分かち合うアクティブな一人。一人が都市を作り、都市が一人の誇りを守るという、対等で調和の取れた関係の名称です。",
        "aftertaste": "一粒の小麦が集まってパンになるように、一人の意思が国を作る。",
        "example": "Every citizen should exercise their constitutional right to vote.",
        "deep_dive": {
            "roots": [{"term": "kei-", "meaning": "to lie, bed, settle, home"}],
            "points": ["civil（文明の/丁重な）や city と同族。そこを「我が家（home）」とする者の自覚から。"]
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
