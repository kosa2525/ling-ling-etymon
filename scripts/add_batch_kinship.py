import json
import re

word_batch = [
    {
        "id": "kinship",
        "word": "Kinship",
        "meaning": "親族関係、血縁、連帯感",
        "era": "19th Century Old English cynn",
        "etymology": {
            "components": ["cynn (family, race, kind)", "-ship (state, condition)"],
            "original_statement": "From Old English cynn (family, race, kind, rank) + -ship (condition, state of being)."
        },
        "concept": "The state of being of the same kind (同じ種類であるという状態)",
        "thinking": "ただの親戚という意味を超え、根源的に「同じ種（kind/cynn）」に属しているという強烈な連帯感。それは大地に根を張る一つの大きな樹木が、地下で根を絡ませ合っているような、分かちがたい結びつきを指します。種類（kind）や親切（kind）と同音であることも、その温かさを示唆しています。",
        "aftertaste": "遠く離れていても、同じ血の旋律が静かに脈打っている。",
        "example": "He felt a strong sense of kinship with the local fishermen.",
        "deep_dive": {
            "roots": [{"term": "gene-", "meaning": "to give birth, beget"}],
            "points": ["gene（遺伝子）や generate（生成する）と同じ『生む』の源流。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "legacy",
        "word": "Legacy",
        "meaning": "遺産、受け継いだもの、名残",
        "era": "14th Century Old French/Latin legatus",
        "etymology": {
            "components": ["legare (to appoint by a last will, send as an ambassador)"],
            "original_statement": "From Old French legacie, from Latin legatus (ambassador, envoy), from legare (to appoint by a last will)."
        },
        "concept": "Something sent from the past (過去から送られてきたもの、委任されたもの)",
        "thinking": "お金や土地といった財産だけでなく、誰かが生きた証、その意志、あるいは文化的な響き。誰かが「大使（legatus）」として未来のあなたへ託したメッセージのようなもの。あなたが今ここにいること自体が、誰かの残した壮大なレガシーの一部なのです。",
        "aftertaste": "今は亡き誰かが、あなたの指先を通じて今を生きている。",
        "example": "The elderly professor left a legacy of inspired students.",
        "deep_dive": {
            "roots": [{"term": "leg-", "meaning": "to collect, gather (possible)"}],
            "points": ["legal（法律の）や college（大学：共に集まる場所）と、根底にある『選ばれしもの』の意味で繋がります。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "bond",
        "word": "Bond",
        "meaning": "絆、結束、束縛、債券",
        "era": "13th Century Old English/Old Norse band",
        "etymology": {
            "components": ["bindan (to bind, tie)"],
            "original_statement": "From Middle English bond, an alteration of band (anything that binds), from the root of bindan (to bind)."
        },
        "concept": "That which ties things together (物事をつなぎとめるもの、縛るもの)",
        "thinking": "「縛る（bind）」という物理的な行為が語源。それは自由を奪う「鎖」にもなれば、困難な時に絶対に離れない「絆」にもなります。二つの個体を、一つの運命として強固に結びつける、目に見えないほど細く、しかし鋼鉄より強い糸のこと。",
        "aftertaste": "縛られているからこそ、孤独ではないという逆説。",
        "example": "The shared experience created a permanent bond between the two soldiers.",
        "deep_dive": {
            "roots": [{"term": "bhendh-", "meaning": "to bind"}],
            "points": ["bundle（束）や bandwidth（帯域幅）と同じ。何かをギュッとまとめる力。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "trust",
        "word": "Trust",
        "meaning": "信頼、信用、委託、コンツェルン",
        "era": "12th Century Old Norse traust",
        "etymology": {
            "components": ["traust (confidence, help, protection)"],
            "original_statement": "From Old Norse traust (confidence, help, protection, firmness), from Proto-Germanic *traustam."
        },
        "concept": "Firmness and reliability (揺るぎない確固とした状態、助け)",
        "thinking": "語源は「木（tree/treu）」のようにドッシリと立っていることに関連します。風が吹いても、嵐が来ても、そこにあると信じられる「強固さ（firmness）」。相手に自分の背中を預けても、決して崩れないという静かな確信のことです。",
        "aftertaste": "目に見えない大地。一番深く、最も確かな足場。",
        "example": "Trust is the foundation of any healthy relationship.",
        "deep_dive": {
            "roots": [{"term": "deru-", "meaning": "be firm, solid, steadfast"}],
            "points": ["true（真実の）や tree（木）と同じ。真っ直ぐに、硬く立っている様子。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "rival",
        "word": "Rival",
        "meaning": "ライバル、競争相手、匹敵する",
        "era": "16th Century Middle French/Latin rivalis",
        "etymology": {
            "components": ["ripa (riverbank)"],
            "original_statement": "From Middle French rival, from Latin rivalis (pertaining to a river, one who uses the same stream), from ripa (bank)."
        },
        "concept": "Someone using the same stream (同じ川を利用する者、岸辺を共にする者)",
        "thinking": "「川（river/ripa）」の対岸に住む者同士のこと。同じ水資源を奪い合い、時に境界を巡って争い、しかし同じ環境に生きる運命共同体。憎しみ合う敵（enemy）ではなく、切磋琢磨し、相手の存在があるからこそ自分が磨かれる、写し鏡のような存在です。",
        "aftertaste": "川という境界を挟んで。あなたの強さが、今の私を作っている。",
        "example": "The two companies have been fierce rivals for decades.",
        "deep_dive": {
            "roots": [{"term": "rei-", "meaning": "to scratch, tear, cut"}],
            "points": ["river（川：岸を削るもの）と同じ。削り取られた境界線が始まり。"]
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
