import json
import re

word_batch = [
    # Cycle 72: Strength & Sustainability
    {
        "id": "stamina_strength",
        "word": "Stamina",
        "meaning": "スタミナ、精力、持久力",
        "era": "18th Century Latin stamen",
        "etymology": {
            "components": ["stamen (thread, warp of a fabric)"],
            "original_statement": "Plural of Latin stamen (thread, warp of a fabric, thread spun by the Fates)."
        },
        "concept": "The threads of life (運命の女神が紡ぐ「生命の糸（stamen）」)",
        "thinking": "もともとは、運命の三女神が一人ひとりの寿命として紡ぎ出す「糸」の複数形（stamina）。一本の糸は細くても、それが束ねられ、織り込まれることで、長期間の困難に耐えうる「持続的な強さ」に変わります。瞬間的な爆発力ではなく、最後まで糸を切らさずに走り抜ける、生命の底力です。",
        "aftertaste": "細い糸の集積。それが、どんな嵐にも負けない強靭な布（いのち）を織り上げる。",
        "example": "Running a full marathon requires not just speed, but incredible physical and mental stamina.",
        "deep_dive": { "roots": [{"term": "sta-", "meaning": "to stand"}], "points": ["stand（立つ）や status（地位）と同じく、その場に留まり続ける力のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "endurance_strength",
        "word": "Endurance",
        "meaning": "忍耐、耐久力、辛抱",
        "era": "15th Century Old French/Latin durus",
        "etymology": {
            "components": ["durus (hard)"],
            "original_statement": "From Old French endurance, from endurer, from Latin indurare (make hard), from durus (hard)."
        },
        "concept": "Making oneself hard (自らを「硬く（durus）」し、磨り減りに耐えること)",
        "thinking": "外部からの圧力や時間の経過に対しても、形を変えず、屈しないこと。ダイヤモンドのような「硬度」を自らの中に育むプロセスです。ただ我慢するのではなく、磨かれることでより輝きを増す石のように、苦難を糧にして自らの核を固めてゆく、静かなる闘いです。",
        "aftertaste": "硬き意志。時の試練を経てなお、変わらぬ輝きを放つものだけが本物。 ",
        "example": "The endurance of the ancient stone monuments has fascinated archaeologists for centuries.",
        "deep_dive": { "roots": [{"term": "dere-", "meaning": "hard, solid"}], "points": ["durable（耐久性のある）や during（〜の間：続いているとき）と同じ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "tenacity_strength",
        "word": "Tenacity",
        "meaning": "粘り強さ、不屈、固執",
        "era": "15th Century Latin tenere",
        "etymology": {
            "components": ["tenere (to hold)"],
            "original_statement": "From Latin tenacitas (the act of holding fast), from tenax (holding fast), from tenere (to hold)."
        },
        "concept": "The act of holding fast (一度掴んだら、絶対に「離さない（tenere）」こと)",
        "thinking": "「スタミナ」や「エンデュランス」が受け身の強さだとしたら、テナシティはより能動的で食い下がるような強さ。目標や希望を、食らいついて離さない「執着の美学」。語源の tenere は、腱（tendon）のようにピンと張り詰め、つなぎ止める力を指しています。",
        "aftertaste": "食らいつく牙。不格好でもいい、ただ最後の一瞬までその手を離さないこと。",
        "example": "It was her sheer tenacity that finally convinced the investors to back the risky project.",
        "deep_dive": { "roots": [{"term": "ten-", "meaning": "to stretch"}], "points": ["tension（緊張）や contain（含む：一緒に持つ）と同じ『保持』のダイナミズム。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "resilience_strength_2",
        "word": "Elasticity",
        "meaning": "弾力、伸縮性、融通性",
        "era": "17th Century Greek elastikos",
        "etymology": {
            "components": ["elaunein (to drive, beat out)"],
            "original_statement": "From Modern Latin elasticus, from Greek elastikos (propulsive), from elaunein (to drive, beat out, forge)."
        },
        "concept": "Power to drive back (打ち負かされても、押し返す力)",
        "thinking": "金属を叩いて（beat out）薄く延ばしながらも、決して切れない「展延性」に近い性質。衝撃を受けて変形しても、その衝撃をエネルギーに変えて元の形、あるいはそれ以上の形へと「押し戻す」力。硬すぎるものは脆（もろ）いけれど、弾力のある心は、どんな悲しみもバネに変えることができます。",
        "aftertaste": "しなやかな復元。沈んだ分だけ、次はもっと高く跳ぶことができる。",
        "example": "The great advantage of this material is its high elasticity and resistance to wear.",
        "deep_dive": { "roots": [{"term": "el-", "meaning": "to drive, move"}], "points": ["elastic（ゴム/弾性）の語源。常に動き、反発する生のエネルギー。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "fortitude_strength_2",
        "word": "Stalwart",
        "meaning": "忠実な、たくましい、信念の強い人",
        "era": "Old English stalu + weorc",
        "etymology": {
            "components": ["steall (place)", "weorc (work)"],
            "original_statement": "From Scots variant of Middle English stalworth, from Old English stælwierþe (serviceable, sturdy), probably from stæl (place) + wierþe (worth)."
        },
        "concept": "Worth the place (その「場所（place）」に立つに値する、盤石な信頼感)",
        "thinking": "嵐が来ようと、仲間が去ろうと、自分が決めたその「場所（stall/place）」に仁王立ちし続ける人。その姿は古びた石塔のように頼もしく、周囲に安心感を与えます。本来は「場所としての価値（worth）」から。あなたがそこにいるだけで、その場の意味が確定されるような、圧倒的な存在の重み。",
        "aftertaste": "動かない背中。時代の流行に流されず、ただ自らの正義の丘に立ち続ける誇り。",
        "example": "He has been a stalwart supporter of the environmental movement for over forty years.",
        "deep_dive": { "roots": [{"term": "stel-", "meaning": "to put, stand"}], "points": ["stall（牛舎/売店）や still（静止した）と同じ『置かれた場所』の系譜。"] },
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
        print(f"Success: Added {added} words in Cycle 72.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
