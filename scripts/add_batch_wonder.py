import json
import re

word_batch = [
    {
        "id": "mystery_wonder",
        "word": "Mystery",
        "meaning": "神秘、謎、推理小説",
        "era": "14th Century Old French/Greek mysterion",
        "etymology": {
            "components": ["myein (to shut one's eyes or mouth)"],
            "original_statement": "From Old French mistere, from Latin mysterium, from Greek mysterion (secret rite, secret thing), from mystes (one initiated), from myein (to shut, close)."
        },
        "concept": "To shut the eyes or mouth (口を閉ざす、沈黙を強いる秘密の儀式)",
        "thinking": "もともとは、選ばれた者だけが参加を許される秘密の儀式を指しました。その内容は口外してはならず、口を「閉ざす（myein）」こと。完全には暴けない、沈黙の向こう側にある深淵。それが、私たちが畏敬の念を持って見つめる「神秘」の正体です。",
        "aftertaste": "言葉にした瞬間に消えてしまう。ただ見つめることしかできない深み。",
        "example": "The origins of life are still a profound mystery to modern science.",
        "deep_dive": {
            "roots": [{"term": "mu-", "meaning": "to close, mute (onomatopoeic)"}],
            "points": ["mute（無言の）や myopia（近視：目を細めて見る）と、この『閉じる』感覚で繋がります。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "admire_wonder",
        "word": "Admire",
        "meaning": "感嘆する、賞賛する、心酔する",
        "era": "16th Century Middle French/Latin mirari",
        "etymology": {
            "components": ["ad- (at)", "mirari (to wonder at)"],
            "original_statement": "From Latin admirari (to wonder at), from ad- (at) + mirari (to wonder at, look at with amazement)."
        },
        "concept": "To look at with amazement (驚愕の目で見つめる、見惚れる)",
        "thinking": "ただ褒めるのではなく、目を見開いて（ad-mirari）「なんてこった、素晴らしい！」と驚くこと。対象の持つ圧倒的な魅力や価値に心が撃ち抜かれ、驚嘆の余韻に浸っている状態。鏡（mirror）を覗き込んで自分の姿に驚くのと同じ、原初的な感動の形です。",
        "aftertaste": "美しさに、言葉を奪われる。ただ、その輝きに自分を預けるだけ。",
        "example": "I really admire her courage in standing up for justice in court.",
        "deep_dive": {
            "roots": [{"term": "smeiros", "meaning": "smiling"}],
            "points": ["miracle（奇跡）や smile（微笑み）のルーツ。心が喜びで満たされること。"]
        },
        "part_of_speech": "verb"
    },
    {
        "id": "revere_wonder",
        "word": "Revere",
        "meaning": "崇める、畏敬する、深く尊敬する",
        "era": "17th Century Middle French/Latin vereri",
        "etymology": {
            "components": ["re- (intensive)", "vereri (to stand in awe, fear)"],
            "original_statement": "From Latin revereri (to stand in awe of, respect), from re- (intensive prefix) + vereri (to respect, fear, be in awe)."
        },
        "concept": "To stand in intense awe (強烈な畏れを持って「見つめる」、一歩下がる)",
        "thinking": "ただの尊敬（respect）よりも、もう少し距離があり、少しの「恐れ（fear）」を含んだ「畏敬」。対象の持つ神秘的なまでの尊厳（dignity）の前に、思わず立ち止まり、一歩下がって頭を垂れるような、静寂に満ちた最高の礼賛です。",
        "aftertaste": "眩しすぎる光の前に。ただ無言でひざまずく、魂の最敬礼。",
        "example": "Many cultures revere their ancestors as wise guardians and protectors.",
        "deep_dive": {
            "roots": [{"term": "wer-", "meaning": "to watch, guard, perceive"}],
            "points": ["aware（気づいている）や ward（守る）と同族の『注意深く見守る』ルーツ。"]
        },
        "part_of_speech": "verb"
    },
    {
        "id": "fascination_wonder",
        "word": "Fascination",
        "meaning": "魅了、恍惚(こうこつ)、強固な惹きつけ",
        "era": "17th Century Latin fascinum",
        "etymology": {
            "components": ["fascinum (witchcraft, charm, spell)"],
            "original_statement": "From Latin fascinationem, from fascinari (to bewitch, enchant), from fascinum (a spell, witchcraft)."
        },
        "concept": "Under a magic spell (魔法（呪文）をかけられたように、抗えない吸引力)",
        "thinking": "もともとは、魔力によって相手を動けなくさせる「呪文（fascinum）」を指しました。蛇が獲物を睨みつけて一歩も動けなくさせるような、呪術的なまでの強烈な惹きつけ。対象の美しさや面白さによって、自分の意志が奪われ、釘付けになってしまった状態です。",
        "aftertaste": "目は離せない。逃げることもできない。その魅力に囚われた虜（とりこ）。",
        "example": "The detailed study of ancient Egypt has been a source of fascination for him.",
        "deep_dive": {
            "roots": [{"term": "bhask-", "meaning": "bundle, band (possible)"}],
            "points": ["faggot（束ねられた薪）の root と近く、相手を『束縛して動けなくする』イメージ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "enchant_wonder",
        "word": "Enchant",
        "meaning": "魅了する、魔法にかける、大いなる喜びを与える",
        "era": "14th Century Old French/Latin incantare",
        "etymology": {
            "components": ["in- (into, upon)", "cantare (to sing)"],
            "original_statement": "From Old French enchanter, from Latin incantare (to enchant, cast a spell upon), from in- (upon, into) + cantare (to sing)."
        },
        "concept": "To sing a spell into someone (歌（呪文）を、誰かの魂に「歌い込む」こと)",
        "thinking": "視覚で捉える視線ではなく、「歌（chant：cantare）」を相手に吹き込み、その心を蕩（とろ）けさせて支配すること。メロディーという魔法の糸が、相手の内側に流れ込み（in-）、いつの間にか心地よい「酔い（trance）」の中に閉じ込められてしまった幸福な魔法を指します。",
        "aftertaste": "耳元で鳴り止まない調べ。誰がかけたかも忘れる、甘い魔法。",
        "example": "The visitors were completely enchanted by the beauty of the mountain lake village.",
        "deep_dive": {
            "roots": [{"term": "kan-", "meaning": "to sing"}],
            "points": ["accent（アクセント：添えられた歌）や incentive（動機：かつて相手に音色の刺激を与えたこと）と同類。"]
        },
        "part_of_speech": "verb"
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
