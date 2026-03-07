import json
import re

word_batch = [
    {
        "id": "thicket",
        "word": "Thicket",
        "meaning": "茂み、藪",
        "era": "Old English þiccett",
        "etymology": {
            "components": ["thick (dense, crowded)"],
            "original_statement": "From Old English þiccet, from þicce (thick)."
        },
        "concept": "A dense growth of bushes (密集して生えた低木の茂み)",
        "thinking": "ただの木立ではありません。枝と枝が複雑に絡み合い、視線さえも通さない「厚み（thick）」を持った藪。それは、物事が複雑に絡み合って抜け出せない「困難な問題」の比喩でもあります。その中心には、守られている何か、あるいは隠されている何かがあるかもしれません。",
        "aftertaste": "暗がりを潜り抜け、絡みつく枝を払った先にこそ、真実の光はある。",
        "example": "The small animal disappeared in a dense thicket of thorns.",
        "deep_dive": {
            "roots": [{"term": "tigu-", "meaning": "thick, strong"}],
            "points": ["thick（厚い）そのものの名詞形。密集した状態を端的に示します。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "glade",
        "word": "Glade",
        "meaning": "森の中の空き地",
        "era": "16th Century Middle English glade",
        "etymology": {
            "components": ["glad (bright, shining)"],
            "original_statement": "From Middle English glade, related to glad (bright, shining, smooth)."
        },
        "concept": "A bright open space (明るい開けた場所、光の溜まり場)",
        "thinking": "うっそうとした暗い森の中に、突如として現れる「ぽっかりと光が降り注ぐ広場」。語源は「嬉しい（glad）」と同じ、「輝いている」ことです。そこは、生命の休息の場であり、静寂が満ちる神聖な場所。コントラストが描き出す、美の中庭です。",
        "aftertaste": "暗い迷宮を抜けた先。そこには、ただ一点の光が、草花を照らしている。",
        "example": "A single deer was standing quietly in the forest glade.",
        "deep_dive": {
            "roots": [{"term": "ghel-", "meaning": "to shine, yellow"}],
            "points": ["glad（嬉しい）はもともと『光り輝く（beaming）』という意味。幸福は光なのです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "stream_flow",
        "word": "Stream",
        "meaning": "小川、流れ、連続",
        "era": "Old English stream",
        "etymology": {
            "components": ["srew- (to flow)"],
            "original_statement": "From Old English stream, from Proto-Germanic *straumaz, from PIE root *sreu- (to flow)."
        },
        "concept": "A continuous flow (絶え間ない流れ)",
        "thinking": "激流よりも穏やかで、しかし決して留まることのない「流れ（sreu-）」。それは情報のストリームであり、意識のストリーム（consciousness）でもあります。一点にとどまらず、絶えず新しい何かに更新され続ける、フレッシュな時間のプロセスそのものです。",
        "aftertaste": "留まることは淀むこと。常に新しき血潮に、自己を委ねよ。",
        "example": "A stream of ideas flowed from the meeting discussions.",
        "deep_dive": {
            "roots": [{"term": "sreu-", "meaning": "to flow"}],
            "points": ["rhythm（リズム：刻まれた流れ）や rheum（リウマチ：体液が流れる病気）と同じファミリー。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "threshold_entry",
        "word": "Threshold",
        "meaning": "敷居、入り口、始まり、境界線",
        "era": "Old English þerscold",
        "etymology": {
            "components": ["þrescan (to thresh, stomp)", "wald- (wood, possible)"],
            "original_statement": "From Old English þerscold (threshing floor), related to þrescan (to thresh, stamp with the feet)."
        },
        "concept": "A place to tread (足で踏みつけ、脱穀する場所、扉の足元)",
        "thinking": "「踏みつける（thresh）」という言葉に関連があり、もともとは収穫した麦などを足で踏んで殻を外す場所（threshing floor）が玄関の足元にあったことに由来します。一つの世界が終わり、新しい世界へと足を踏み出すための「決意の境界線（boundary）」です。",
        "aftertaste": "足元に引かれた、目に見えない線。それを越えたとき、すべてが変わる。",
        "example": "The country is on the threshold of a new scientific era.",
        "deep_dive": {
            "roots": [{"term": "ter-", "meaning": "to rub, turn, thresh"}],
            "points": ["thread（糸：撚り合わされたもの）や turn（回る）と同系統の、回転や摩擦のルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "clue",
        "word": "Clue",
        "meaning": "手がかり、ヒント",
        "era": "16th Century Middle English clewe",
        "etymology": {
            "components": ["clewe (ball of thread)"],
            "original_statement": "From Middle English clewe (a ball of thread/yarn). The meaning 'key to a riddle' comes from the story of Theseus and Ariadne's thread in the Labyrinth."
        },
        "concept": "A ball of thread (迷宮から脱出するための「糸玉」)",
        "thinking": "迷宮（Labyrinth）から脱出するために、アリアドネがテセウスに渡した「糸の玉（clewe）」が語源。複雑に絡み合った混迷（Mystery）の中で、たった一本の、しかし確実な繋がりを示す糸。それさえ手放さなければ、必ず出口（答え）へと導かれるという、信頼の糸です。",
        "aftertaste": "複雑な事象の中に、必ず一本の光る糸がつながっている。それを見逃すな。",
        "example": "The detective found a vital clue at the crime scene.",
        "deep_dive": {
            "roots": [{"term": "gleu-", "meaning": "to ball, gather, clod"}],
            "points": ["glue（接着剤：集めて固めるもの）や cloud（雲：集まった塊）と同じ『塊』を意味する言葉から。"]
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
