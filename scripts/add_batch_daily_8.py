import json
import re

word_batch = [
    {
        "id": "echo",
        "word": "Echo",
        "meaning": "反響、エコー、共鳴",
        "era": "14th Century Greek ēkhō",
        "etymology": {
            "components": ["ēkhō (sound, noise)"],
            "original_statement": "From Old French echo, from Latin echo, from Greek ēkhō (sound, noise, ringing), personified as a nymph."
        },
        "concept": "A sound that returns (戻ってくる音)",
        "thinking": "ギリシャ神話のニンフ（妖精）エコー。彼女は神に呪われ、他人の言葉を繰り返すことしかできなくなりました。山びこのように、自分の声が時間差で世界から跳ね返ってくる現象。それは、過去の自分の行いが現在に響き、共鳴することの比喩でもあります。",
        "aftertaste": "世界に放った言葉は、いつか自分のもとに旋律を変えて還る。",
        "example": "His words found an echo in the hearts of his listeners.",
        "deep_dive": {
            "roots": [{"term": "wagh-", "meaning": "to resound"}],
            "points": ["catechism（教理問答：向こう側に『響かせて』教えを問う）の -echi- と同類。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "whisper",
        "word": "Whisper",
        "meaning": "ささやき、密談",
        "era": "Old English hwisprian",
        "etymology": {
            "components": ["hw- (onomatopoeic sound of breath)"],
            "original_statement": "From Old English hwisprian (to whisper), of imitative origin, mimicking the sound of soft breath."
        },
        "concept": "A soft breath of sound (柔らかな一息の音、模倣語)",
        "thinking": "言葉を声（喉の振動）ではなく、単なる「息の漏れ」として伝えること。それは親密さの証であり、あるいは秘密を共有する共犯者の合図です。静寂を破ることなく、相手の耳元に直接、心魂を届けるための極めて私的な通信手段。",
        "aftertaste": "声にならない吐息が、千の言葉よりも雄弁に秘密を語る。",
        "example": "A soft whisper can sometimes be louder than a shout.",
        "deep_dive": {
            "roots": [{"term": "kwei-", "meaning": "to whistle, hiss (possible)"}],
            "points": ["whistle（笛を吹く）と同じく、空気の摩擦音そのものがルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "harbor",
        "word": "Harbor",
        "meaning": "港、避難所、(思いを)抱く",
        "era": "12th Century Old English herberge",
        "etymology": {
            "components": ["here (army)", "beorg (shelter)"],
            "original_statement": "From Old English herebeorg (shelter, lodging, guest house), from here (army) + beorg (shelter, refuge)."
        },
        "concept": "A shelter for an army (軍隊のための避難所・野営地)",
        "thinking": "もともとは「船の港」ではなく「軍隊（here）」が夜に体を休めるための「野営地・避難所（beorg）」を指していました。外の荒ぶる海から守られ、深呼吸できる場所。転じて、心の中にそっと大切な思いや願いを『抱き続ける（harboring a feeling）』という意味にもなりました。",
        "aftertaste": "荒波を超えて。静かな入り江に、すべての重荷を降ろす。",
        "example": "The small fishing boats sought harbor before the storm broke.",
        "deep_dive": {
            "roots": [{"term": "koro-", "meaning": "war, army"}, {"term": "bhergh-", "meaning": "to protect"}],
            "points": ["herald（使者：軍の命令を伝える者）の her- も同じルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "anchor",
        "word": "Anchor",
        "meaning": "錨(いかり)、(心の)支え、頼みの綱",
        "era": "Old English ancor/Greek ankyra",
        "etymology": {
            "components": ["ank- (bent, hook)"],
            "original_statement": "From Latin ancora, from Greek ankyra (anchor, hook)."
        },
        "concept": "A bent hook to hold firm (しっかり固定するための曲がったフック)",
        "thinking": "激しい潮流の中でも、船が流されないように海底の岩をガッチリと掴んで離さない「曲がったフック（ank-）」。それは不安な日々の中で、自分という軸がブレないように繋ぎ止めてくれる「信念」や「愛」の強固なメタファーでもあります。",
        "aftertaste": "目には見えない深い場所で、あなたは大地と繋がっている。",
        "example": "Hope is the anchor of the soul during difficult times.",
        "deep_dive": {
            "roots": [{"term": "ang-", "meaning": "corner, bend"}],
            "points": ["angle（角度・角）や ankle（くるぶし：曲がっているところ）と同じ仲間。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "feather",
        "word": "Feather",
        "meaning": "羽、羽毛、軽微なもの",
        "era": "Old English feðer",
        "etymology": {
            "components": ["pet- (to fly, rush)"],
            "original_statement": "From Old English feðer, from Proto-Germanic *fethrō- (feather), from PIE *pet- (to fly, rush)."
        },
        "concept": "The instrument of flying (空飛ぶための道具、飛翔の片鱗)",
        "thinking": "空を飛ぶための極限まで軽量化された、美しくも機能的な一枚の部品。それは「軽さ」の象徴であり、一陣の風にすら惑わされる心の不確かさを表すこともあれば、空高く羽ばたく自由を約束する証（しるし）でもあります。",
        "aftertaste": "重力に抗う意志が、一枚の柔らかな繊維に凝縮されている。",
        "example": "A single white feather lay quietly in the palm of her hand.",
        "deep_dive": {
            "roots": [{"term": "pet-", "meaning": "to rush, fly"}],
            "points": ["petition（請願：突進して求める）や pen（ペン：羽ペン）の pet- は『飛ぶ・急ぐ』という同じ勢いの語源。"]
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
