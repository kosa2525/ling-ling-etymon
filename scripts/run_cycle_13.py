import json
import re

words_data = [
    ("gush", "Gush", "勢いよく流れ出る", "15th Century", "guschen (to rush out violently)", "Flow out of something in a rapid and plentiful stream", "抑圧されていた水や感情が限界に達し、狭い出口から「勢いよく」暴力的に解放される瞬間のカタルシス。", "喜びで「ガッシュ（あふれ出る）」するような涙は、どんな悲しい涙よりも美しく煌めきます。"),
    ("spout", "Spout", "吹き出す、噴出する", "14th Century", "spouten (to spit or spew)", "Send out liquid forcefully in a stream", "鯨の潮吹きのように、細い管を通って重力に逆らう高い圧力で空高く「吹き出す」生命のエネルギー。", "愚痴を「スパウト（堰を切ったように喋る）」してすっきりした後は、また新しい明日を始めましょう。"),
    ("seep", "Seep", "にじみ出る", "Old English", "sipian (to soak, macerate)", "Flow or leak slowly through porous material or small holes", "岩の隙間や心の壁を見つけ出し、微量ながらも執拗に時間をかけて「にじみ出て」くる静かな力。", "気づかないうちに「シープ（沁み透る）」してきた優しさが、いつしか心を完全に満たしていました。"),
    ("ooze", "Ooze", "にじみ出る、漏れる", "Old English", "wos (juice, sap)", "Slowly trickle or seep out of something", "粘り気のある水や血が、傷口から重く、そして後戻りできない確実さで「ゆっくりと漏れ出す」様。", "自信が体の毛穴から「ウーズ（にじみ出る）」するような人こそが、本当の意味で美しいのです。"),
    ("drip", "Drip", "したたる", "14th Century", "drippen (to fall in drops)", "Fall or let fall in drops", "液体が自らの重さに耐えきれなくなり、「一滴ずつ」切り離され落下していく等間隔の悲しいリズム。", "疲れた日は、雨の「ドリップ（ポタポタ落ちる音）」を聞きながらコーヒーを淹れる時間を大切に。"),
    ("drain", "Drain", "排水する、消耗させる", "Old English", "drehnian (to strain, draw off)", "Cause the water or other liquid in something to run out", "不要になった液体を最後まで「引き抜いて」空っぽにすることで、新しいものを受け入れる準備を整えること。", "心まで「ドレイン（消耗）」されてしまう前に、休むという名の栓を閉める勇気を持ちましょう。"),
    ("leak", "Leak", "漏れる", "14th Century", "leken (to let water in or out)", "Accidentally lose or admit contents through a hole", "厳重に守られていたはずの容器や秘密が、小さな穴から「意図せず」少しずつ外へ逃げ出してしまう失敗。", "涙が「リーク（漏れ出る）」するのは、我慢という名のダムが正常に機能している証拠です。"),
    ("drench", "Drench", "びしょ濡れにする", "Old English", "drencan (to sink, drown, cause to drink)", "Wet thoroughly; soak", "水が対象のすべてを隙間なく支配し、元の重さや色を完全に奪い去るという、愛にも似た「圧倒的」な沈水。", "突然の雨に「ドレンチト（ずぶ濡れに）」になったからこそ、帰りのホットミルクが格別に美味しいのです。"),
    ("soak", "Soak", "浸す、ずぶぬれにする", "Old English", "socian (to lie in liquid)", "Make or allow something to become thoroughly wet by immersing it in liquid", "長時間液体の中に身を置き、時間をかけて全体に「深く水分を染み込ませて」柔らかくすること。", "温泉に肩まで「ソーク（浸かる）」すれば、心の強張（こわば）りごと全て溶かして流してくれます。"),
    ("steep", "Steep", "浸す、急な", "14th Century", "stepen (to soak)", "Soak in water or other liquid so as to extract its flavor or to soften it", "紅茶の茶葉が熱湯の中で少しずつ成分を放ち、全体をその味と色で「深く染め上げる」静寂の儀式。", "歴史に「スティープト（深く浸された）」な古い町並みを歩くと、自分の人生も壮大な物語の一部に思えてきます。")
]

words = []
for item in words_data:
    meaning1 = "known origin"
    root1 = item[4]
    w = {
        "id": f"{item[0]}_water_flow",
        "word": item[0],
        "meaning": item[2],
        "era": item[3],
        "etymology": {
            "components": [item[4]],
            "original_statement": f"From {item[3]} {item[4]}."
        },
        "concept": item[5] + f" ({item[6]})",
        "thinking": item[6],
        "aftertaste": item[7] if len(item) > 7 else "水の動きに、感情の静かなる機微を見出す。",
        "example": f"I watched the water {item[0]} gently.",
        "deep_dive": {
            "roots": [{"term": root1, "meaning": meaning1}],
            "points": ["水の持つ「流れ・浸透・破壊」という多面的な性格。"]
        },
        "part_of_speech": "verb"
    }
    words.append(w)

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
if match:
    prefix, json_array_str, suffix = match.groups()
    existing_words = json.loads(json_array_str)
    existing_ids = {w.get("id") for w in existing_words}
    existing_word_texts = set(w.get("word").lower() for w in existing_words)
    
    added = 0
    for w in words:
        if w["id"] not in existing_ids and w["word"].lower() not in existing_word_texts:
            existing_words.append(w)
            added += 1
            existing_word_texts.add(w["word"].lower())
            
    new_content = content[:match.start()] + prefix + json.dumps(existing_words, ensure_ascii=False, indent='\t') + suffix + content[match.end():]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Success: Added {added} words. Theme: Water Flow (Cycle 13).")
else:
    print("Error parsing data.js")
