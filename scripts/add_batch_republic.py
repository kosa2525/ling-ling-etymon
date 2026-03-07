import json
import re

word_batch = [
    {
        "id": "republic_state",
        "word": "Republic",
        "meaning": "共和国、共和政",
        "era": "16th Century Middle French/Latin res publica",
        "etymology": {
            "components": ["res (thing, matter, affair)", "publica (public, people's)"],
            "original_statement": "From Latin res publica (the public thing, people's matter)."
        },
        "concept": "The public thing (みんなのこと、共有された利益)",
        "thinking": "王や特定個人の私物（res privata）ではなく、すべての「市民（publica）」が共有し、全員で責任を持つべき「公的なもの（res）」のこと。社会全体の利益を守るための、開かれた運営の精神を指します。一人が決めるのではない、対等な関係の集大成としての国。",
        "aftertaste": "私物ではない。ここにいる全員の意志を編み上げたもの。",
        "example": "Ancient Rome transitioned from a monarchy to a republic in 509 BC.",
        "deep_dive": {
            "roots": [{"term": "re-", "meaning": "thing (possible)"}, {"term": "pue-", "meaning": "to swell (pop-" }],
            "points": ["real（現実の：実在するres）や property（財産）と、この『物（res）』の感覚で繋がります。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "policy_governance",
        "word": "Policy",
        "meaning": "政策、方針、規定、契約",
        "era": "14th Century Old French/Greek politeia",
        "etymology": {
            "components": ["polis (city-state)"],
            "original_statement": "From Old French policie (civil administration), from Latin politia, from Greek politeia (citizenship, government), from polis (city)."
        },
        "concept": "The way of managing a city (都市（国家）を運営するための知恵)",
        "thinking": "ただのルールではなく、その「都市（polis）」という船が、どこを目指して進んでいくかを示す確かな航海術のこと。混乱を避けるために敷かれた知的なレールであり、一貫した行動原理です。市民の幸福を最大化するための、実務的な知恵の集積。",
        "aftertaste": "行き当たりばったりではない、遥か先を見据えた一つの意志の線。",
        "example": "Company policy strictly forbids any form of the bullying in the workplace.",
        "deep_dive": {
            "roots": [{"term": "pele-", "meaning": "citadel, enclosure"}],
            "points": ["police（警察）や politics（政治）と同じ、都市運営のファミリー。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "diplomacy_state",
        "word": "Diplomacy",
        "meaning": "外交、外交術、(対人関係の)駆け引き",
        "era": "18th Century Modern Latin/Greek diploma",
        "etymology": {
            "components": ["diploma (folded paper, license)"],
            "original_statement": "From Modern Latin diplomatia, from Latin diploma (a letter of recommendation), from Greek diploma (folded paper)."
        },
        "concept": "The management of folded papers (折りたたまれた公文書（特権証）を扱う技術)",
        "thinking": "もともとは身分や役割を証明する「二つ折りの書面（diploma）」を携えた、公式の使者が行う交渉のこと。二面性（double/di-）を持つ折り畳まれた紙に込められた交渉、言葉の裏側までを読み、相手と折り合いを付けるという、きわめて知的な「交渉の芸術」。",
        "aftertaste": "剣を抜かずに、紙を広げて、二人の世界の均衡を保つ術。",
        "example": "The crisis will require skilled diplomacy and patient communication between nations.",
        "deep_dive": {
            "roots": [{"term": "di-", "meaning": "two"}, {"term": "plo-", "meaning": "fold"}],
            "points": ["duplicate（複製する：二重に折る）や double の di- がその二重性の証拠。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "forum_society",
        "word": "Forum",
        "meaning": "フォーラム、公開討論会、広場",
        "era": "15th Century Latin forum",
        "etymology": {
            "components": ["forus (outside, yard, door)"],
            "original_statement": "From Latin forum (public square, market, court), related to foris (outside, door)."
        },
        "concept": "The place outside (家の「外」にある、みんなが集まる公共の場所)",
        "thinking": "古代ローマの都市の中心にあった、市場であり、法廷であり、議論の場でもあった「広場」。そこは、家の閉じられた扉の「外（foris）」に開かれた、文字通りの公共空間（Public space）です。異なる意見が激しくぶつかり合い、そこから新しい社会的合意が形成されてゆく、活気ある情報の交差点。",
        "aftertaste": "誰の前でも、自分の言葉を広場に投げ出し、吟味される勇気。",
        "example": "The online forum has become a platform for open and honest discussion.",
        "deep_dive": {
            "roots": [{"term": "dhwer-", "meaning": "door"}],
            "points": ["foreign（外国の/外部の）や forest（森：外の世界）と同じ『扉の向こう』の感覚。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "integrity_justice",
        "word": "Integrity",
        "meaning": "誠実、真摯、高潔、完全な状態",
        "era": "14th Century Old French/Latin integer",
        "etymology": {
            "components": ["integer (whole, untouched, entire)"],
            "original_statement": "From Old French integrité, from Latin integritatem (soundness, wholeness, blamelessness), from integer (untouched, whole, intact)."
        },
        "concept": "A state of being whole and untouched (一点の欠けもない、真っさらで全体的な状態)",
        "thinking": "ただ嘘をつかないという以上の意味。「一切汚されていない、一つの完全な全体（integer）」を保っていること。周囲の誘惑によって自分の信念が削り取られたり、分裂したりすることを拒む、精神の頑強な一貫性。他人が見ていようがいまいが、自分という「全体」を守り抜く姿勢です。",
        "aftertaste": "欠片（パーツ）ではない。自分を自分として完成させる、揺るぎない一つの意志。",
        "example": "The candidate was chosen because of her long-standing reputation for professional integrity.",
        "deep_dive": {
            "roots": [{"term": "in-", "meaning": "not"}, {"term": "tag-", "meaning": "to touch"}],
            "points": ["entire（全体の）は integer の変形。接触（tangible）されていない処女性の強さ。"]
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
