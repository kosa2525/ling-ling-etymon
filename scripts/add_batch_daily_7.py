import json
import re

word_batch = [
    {
        "id": "shelter",
        "word": "Shelter",
        "meaning": "避難所、隠れ家、保護する",
        "era": "16th Century English shell + troop",
        "etymology": {
            "components": ["shield (shield, covering)", "troop (troop, company)"],
            "original_statement": "Probably from a blend of shield (protection) and Middle English shel-trouthe (troop-shield), a formation of soldiers for protection."
        },
        "concept": "A protective covering for a troop (仲間を守るための覆い)",
        "thinking": "もともとは戦場で兵士たちが一箇所に集まり、盾（shield）を重ね合わせて自分の「仲間（troop）」を守るための防御隊形のこと。そこから、激しい雨風や危険から身を隠し、静かに安全を確保できる物理的な「覆い」全般を意味するようになりました。安全への防壁です。",
        "aftertaste": "外敵から身を隠し、再び立ち上がる力を蓄える場所。",
        "example": "The small cabin provided a much-needed shelter from the storm.",
        "deep_dive": {
            "roots": [{"term": "skel-", "meaning": "to cut, split"}],
            "points": ["shield（盾：切り出した板）と同じルーツ。世界を『分断』して安全圏を作ります。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "shadow_daily",
        "word": "Shadow",
        "meaning": "影、日陰、暗い部分",
        "era": "Old English sceadu",
        "etymology": {
            "components": ["skadwaz (darkness, shade)"],
            "original_statement": "From Old English sceadu, from Proto-Germanic *skadwaz."
        },
        "concept": "Protection by obscuring light (光を遮ることで生まれる守り)",
        "thinking": "強すぎる日差しから身を守るための「日陰（shade）」が本来の感覚。不気味なものではなく、かつては涼しさや休息の場を与えてくれるものでした。光があるところに必ず寄り添う、切り離せない伴走者。そして、何かの「予兆」としての意味も含んでいます。",
        "aftertaste": "光の不在が描き出す、もう一つの沈黙の輪郭。",
        "example": "The long shadows on the grass signalled that evening was near.",
        "deep_dive": {
            "roots": [{"term": "ske-", "meaning": "to cover"}],
            "points": ["shed（小屋：覆い隠す場所）や shoe（靴：足を覆うもの）と同じ『覆い』の一族です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "harvest",
        "word": "Harvest",
        "meaning": "収穫、実り、秋",
        "era": "Old English hærfest",
        "etymology": {
            "components": ["hær- (autumn, to pick, pluck)"],
            "original_statement": "From Old English hærfest (autumn, harvesting), related to German Herbst, from PIE *kerp- (to gather, pluck, harvest)."
        },
        "concept": "A time for plucking (（実りを）摘み取る時期、秋)",
        "thinking": "もともとは「秋（Autumn/Herbst）」そのものを指す言葉でした。大地からの恵みを「摘み取る（pluck）」こと。それは一年という時間のサイクルが最も美しく、最も豊かな結実を迎える瞬間のことです。人生の努力が成果となることへの比喩としても最高です。",
        "aftertaste": "流した汗が、黄金色の重みとなって手の平に還る。",
        "example": "The village held a festival to celebrate the successful harvest.",
        "deep_dive": {
            "roots": [{"term": "kerp-", "meaning": "to gather, pluck, crop"}],
            "points": ["carpet（絨毯：もとは糸を『つまみ取って』短くした織物）や excerpt（抜粋：摘み出したもの）と同根。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "journey_step",
        "word": "Journey",
        "meaning": "旅、旅路、道のり",
        "era": "13th Century Old French/Latin diurnum",
        "etymology": {
            "components": ["dies (day)", "-ata (pertaining to)"],
            "original_statement": "From Old French journee (a day's work, a day's travel), from Latin diurnum (daily)."
        },
        "concept": "A path taken day by day (一日一日の積み重ね、日々の行程)",
        "thinking": "本来は一生の長い旅ではなく、馬車が一日に進める「一日分（jour）」の距離のこと。そこには「今日一日を生きる（旅をする）」という静かな覚悟が宿っています。その単位が積み重なって、私たちは初めて「人生」という果てしない旅路を認識するのです。",
        "aftertaste": "遠い目的地ではなく、今日一日という『一歩』にフォーカスせよ。",
        "example": "Focus on the small joy of each day's journey.",
        "deep_dive": {
            "roots": [{"term": "dyeu-", "meaning": "to shine, sky, day"}],
            "points": ["diary（日記）や journal（日々の記録）と同じく、かつては太陽の『光』の物語でした。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "bridge_connect",
        "word": "Bridge",
        "meaning": "橋、架け橋",
        "era": "Old English brycg",
        "etymology": {
            "components": ["bru- (beam, log, bridge)"],
            "original_statement": "From Old English brycg, from Proto-Germanic *brugjō."
        },
        "concept": "A log placed across a gap (裂け目に置かれた一本の丸太)",
        "thinking": "裂かれた二つの岸。渡れない境界を繋ぎ直す一本の「梁（beam）」。物理的な構造物でありながら、それはコミュニケーションや理解の最も力強いシンボルです。リスクを冒して「橋を架ける」とき、世界は初めて一つに繋がります。",
        "aftertaste": "分断を超える。そこに道が通る。世界が再び合致する。",
        "example": "Good communication is the best bridge to solving conflicts.",
        "deep_dive": {
            "roots": [{"term": "bhru-", "meaning": "brow, bridge, log"}],
            "points": ["brow（眉毛：両岸からせり出した毛）と同源と言われます。形としての共通性。"]
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
