import json
import re

word_batch = [
    # Cycle 92: Connection & Attachment
    {
        "id": "nexus_connection",
        "word": "Nexus",
        "meaning": "連結、中心、結びつき",
        "era": "17th Century Latin nectere",
        "etymology": {
            "components": ["nectere (to bind, tie, fasten)"],
            "original_statement": "From Latin nexus (a binding, connection), past participle of nectere (to bind)."
        },
        "concept": "Binding together (バラバラのものを一つに強く「縛り（bind）」、結びつけること)",
        "thinking": "単なる接点ではなく、そこを中心としてあらゆる要素が複雑に、かつ必然的に結びついている「核」となる場所. 語源の nectere は、糸を結ぶことを意味します。あなたと世界、過去と未来。それらが交差し、意味を成すための決定的な結び目。それは存在のネットワークの特異点です。",
        "aftertaste": "強固な結び目。そこを解（とき）放てば、世界という織物はバラバラに解けてしまうほどの、聖なる重心。",
        "example": "The small café became a nexus for local artists and intellectuals to share ideas.",
        "deep_dive": { "roots": [{"term": "ned-", "meaning": "to bind, tie"}], "points": ["connect（接続する）や net（網）と同じ、関係性のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "affinity_connection",
        "word": "Affinity",
        "meaning": "親和性、相性、密接な関係",
        "era": "14th Century Latin ad- + finis",
        "etymology": {
            "components": ["ad- (to)", "finis (border, boundary, end)"],
            "original_statement": "From Old French affinite, from Latin affinitatem (relationship by marriage), from affinis (neighboring, related), literally 'bordering on,' from ad- (to) + finis (border, boundary, end)."
        },
        "concept": "Bordering on (「境界線（border）」を接していること、隣り合わせの親密さ)",
        "thinking": "努力して作る関係ではなく、気づけば隣り合わせに立っていたような、磁石のように引き合う自然な結びつき. 語源の finis は「境界」。境界線を共有しているということは、相手の終わりが自分の始まりであり、互いの領域が浸透し合っていることを意味します。魂の「型の近さ」による共鳴。",
        "aftertaste": "隣り合う色。言葉を交わさなくても、あなたと私は同じ風に吹かれ、同じ重力のなかにいることを知っている。",
        "example": "He felt a natural affinity with the ocean and spent every summer sailing.",
        "deep_dive": { "roots": [{"term": "dhei-", "meaning": "to fix, fasten (possible for finis)"}], "points": ["finite（有限の）や refine（洗練する：境界を定める）と同じ、限定された親密さ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "adhesion_connection",
        "word": "Adhesion",
        "meaning": "接着、執着、支持",
        "era": "16th Century Latin ad- + haerere",
        "etymology": {
            "components": ["ad- (to)", "haerere (to stick, cling)"],
            "original_statement": "From Latin adhaesionem, from adhaerere (to stick to), from ad- (to) + haerere (to stick)."
        },
        "concept": "Sticking to (磁力や糊（のり）のように、対象に「ぴたりと張り付く（stick）」こと)",
        "thinking": "ただ繋がっているのではなく、表面と表面が分子レベルで密着し、容易には引き剥がせないほどの一体感. 語源の haerere は「くっつく」。それは物理的な接着だけでなく、信念や人物に対する揺るぎない「忠誠（Support）」や、過去に対する「執着」をも含んでいます。離れがたき密着。",
        "aftertaste": "剥がれぬ肌. あなたが選んだその場所に、あなたは自分という存在のすべてを預け、一体化している。",
        "example": "The success of the new policy depends on the firm adhesion of all community members.",
        "deep_dive": { "roots": [{"term": "ghais-", "meaning": "to hesitate (possible root of stick, stay)"}], "points": ["hesitate（ためらう：立ち止まって固まる）や inherent（固有の：内側に張り付いた）と同じ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "cohesion_connection",
        "word": "Cohesion",
        "meaning": "凝集、結束、一貫性",
        "era": "17th Century Latin co- + haerere",
        "etymology": {
            "components": ["co- (together)", "haerere (to stick)"],
            "original_statement": "From Latin cohaesionem, from cohaerere (to stick together), from co- (together) + haerere (to stick)."
        },
        "concept": "Sticking together (内部から引き合い、全体として一つに「固まる（stick together）」こと)",
        "thinking": "外部から押し固められるのではなく、個々の要素が自発的に「共にありたい」と願い、内側から結びつくことで生まれる強固な一体性. 語源は adhesion（付着）と同じ「くっつく（haerere）」ですが、co-（共に）がつくことで、集団としての美しさと一貫性が際立ちます。バラバラの音が一つの音楽へと溶け合う力。",
        "aftertaste": "一つの命。個であることはもう重要ではない. 私たちは今、一つの波としてこの世界を流れている。",
        "example": "The team's lack of cohesion led to their disappointing performance in the final match.",
        "deep_dive": { "roots": [{"term": "ghais-", "meaning": "to hesitate"}], "points": ["adhesion（異物間の接着）に対し、cohesion（同質のもの同士の結合）のニュアンス。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "alliance_connection",
        "word": "Alliance",
        "meaning": "同盟、提携、結びつき",
        "era": "13th Century Latin ad- + ligare",
        "etymology": {
            "components": ["ad- (to)", "ligare (to bind, tie)"],
            "original_statement": "From Old French aliance, from alier (to combine, unite), from Latin alligare (to bind to, tie up), from ad- (to) + liare (to bind)."
        },
        "concept": "Binding towards (共通の目的のために、互いを「縛り（bind）」合わせること)",
        "thinking": "友情や親和性（Affinity）とは違い、特定の目的や危機を共有することで結ばれる、意志的な契約. 語源の ligare は「結ぶ」。それは自由を一部差し出し、運命を共にすることの誓いです。私たちは一人では弱くても、誰かと結び合う（alligate）ことで、嵐を象（かたど）る強靭な帆となることができます。",
        "aftertaste": "結ばれた指。約束という糸が、あなたと私を、一つの嵐へと繋ぎ止めている。",
        "example": "The two companies formed a strategic alliance to compete with their global rivals.",
        "deep_dive": { "roots": [{"term": "leig-", "meaning": "to bind, tie"}], "points": ["religion（宗教：神と結びつくこと）や ligament（靭帯）と同じ、断ち切れぬ絆のルーツ。"] },
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
        print(f"Success: Added {added} words in Cycle 92.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
