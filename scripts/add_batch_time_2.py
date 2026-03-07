import json
import re

word_batch = [
    # Cycle 86: Time & Eternity
    {
        "id": "eternity_time",
        "word": "Eternity",
        "meaning": "永遠、不滅、長い年月",
        "era": "14th Century Latin aevum",
        "etymology": {
            "components": ["aevum (age, time, eternity)"],
            "original_statement": "From Old French eternite, from Latin aeternitatem (eternity, immortality), from aeternus (everlasting, eternal), from aevum (age, time)."
        },
        "concept": "Beyond even the longest age (どんな「時代（age）」をも超えて、果てしなく続くこと)",
        "thinking": "時計の針が刻む時間（Chronos）をすべて繋ぎ合わせても届かない、円環的で静止した「無限」。それは未来に続く長さではなく、今この瞬間の深淵に潜んでいる「終わりのない現在」です。愛や真理が時間という川に流されず、岩のようにそこにあり続けることへの驚嘆。",
        "aftertaste": "終わりのない一瞬。あなたは今、永遠という名の巨大な静寂のなかに、ひとしずくの命を落としている。",
        "example": "To see a World in a Grain of Sand / And a Heaven in a Wild Flower / Hold Infinity in the palm of your hand / And Eternity in an hour.",
        "deep_dive": { "roots": [{"term": "aiw-", "meaning": "vital force, life, long life"}], "points": ["ever（常に）や age（時代）と同じ、枯れることのない生命力のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "ephemeral_time",
        "word": "Ephemeral",
        "meaning": "はけない、短命な、一日の",
        "era": "16th Century Greek epi- + hemera",
        "etymology": {
            "components": ["epi- (on, for)", "hemera (day)"],
            "original_statement": "From Greek ephemeros (lasting only a day), from epi- (on, applied to) + hemera (day)."
        },
        "concept": "For a single day (ただ「一日（day）」のためだけに咲き、消えていくこと)",
        "thinking": "蜉蝣（かげろう）のように、太陽が昇って沈むまでの間だけ存在を許された美しさ。それは「短い」からこそ、この瞬間の密度を極限まで高めます。永遠（Eternity）の対極にあるようでいて、その一瞬の輝きの中にこそ、私たちは永遠の面影を見てしまうのです。",
        "aftertaste": "はかなき光。消えてしまうからこそ、その色彩は、誰の記憶にも深く、鋭く刻まれる。",
        "example": "The beauty of cherry blossoms is ephemeral, lasting only a week or two each year.",
        "deep_dive": { "roots": [{"term": "Unknown source for hemera"}], "points": ["journal（日記）や diary（日記）と同じく、今日という『一日』を祝福する言葉。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "perpetual_time",
        "word": "Perpetual",
        "meaning": "絶え間ない、終身の、永続的な",
        "era": "14th Century Latin per- + petere",
        "etymology": {
            "components": ["per- (through)", "petere (to seek, aim for, rush at)"],
            "original_statement": "From Old French perpetuel, from Latin perpetualis (universal), from perpetuus (continuous, universal, constant), from per- (through) + second element related to petere (to seek, go to, aim at)."
        },
        "concept": "Seeking through out (目的を目指して、どこまでも「走り（rush）」続けること)",
        "thinking": "静止している「永遠」とは違い、常に動き続け、更新され続けながら、決して途切れることがないダイナミックな永続性. 波の音、心臓の鼓動、宇宙の膨張。それは「止まらない」という意志を持った時間の流れ。疲れることを知らない、生命の純粋なリズムです。",
        "aftertaste": "止まらぬ鼓動. 世界は常に新しくなり続け、その連続性のなかで、あなたは守られている。",
        "example": "The project was designed to be a perpetual source of clean energy for the local community.",
        "deep_dive": { "roots": [{"term": "pete-", "meaning": "to rush, fly"}], "points": ["petition（請願：求めること）や feather（羽：空を飛ぶもの）と同じ、前進への渇望。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "transient_time",
        "word": "Transient",
        "meaning": "一時的な、はかない、(人が)短期滞在の",
        "era": "16th Century Latin trans- + ire",
        "etymology": {
            "components": ["trans- (across)", "ire (to go)"],
            "original_statement": "From Latin transientem, from transire (to pass over, pass by), from trans- (across) + ire (to go)."
        },
        "concept": "Passing across (目の前を「通り（go）」過ぎ、どこかへ消え去ること)",
        "thinking": "旅人が街を通り過ぎるように、ある場所に留まることなく、常に変化し続けている状態。喜びも悲しみも、今のあなたの感情も、すべては通過地点に過ぎません。それは寂しさでもありますが、「この苦しみもまた過ぎ去る」という、再生への希望の言葉でもあります。",
        "aftertaste": "移ろう景色。立ち止まることはできない。だからこそ、今この車窓から見える光を、愛おしく思う。",
        "example": "We should remember that our problems are often transient and will pass in time.",
        "deep_dive": { "roots": [{"term": "ei-", "meaning": "to go"}], "points": ["transition（移行）や exit（出口）と同じ『歩み』のルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "ancestry_time",
        "word": "Ancestry",
        "meaning": "家系、系譜、祖先",
        "era": "14th Century Old French/Latin ante- + cedere",
        "etymology": {
            "components": ["ante- (before)", "cedere (to go)"],
            "original_statement": "From Old French ancesserie, from ancestre (forefather), from Latin antecessor (predecessor), from antecedere (to go before), from ante- (before) + cedere (to go)."
        },
        "concept": "Going before (自分よりも「前（before）」を「歩いて（go）」いった人々)",
        "thinking": "あなたは突然この世界に現れたのではなく、数え切れないほどの人々が前を歩き、道を作り、言葉を紡いできた、その長い「歩みの連鎖」の先端にいます。あなたの血の中に、彼らの物語が眠っています. 時間の流れを、垂直な一本の「道」として捉えるとき、あなたは決して一人ではありません。",
        "aftertaste": "長い行列。あなたの背後には、幾千の顔、幾億の祈りが、盾のように連なっている。",
        "example": "He was proud of his Native American ancestry and worked to preserve their traditions.",
        "deep_dive": { "roots": [{"term": "ked-", "meaning": "to go, yield"}], "points": ["antecedent（前例）や cede（譲る）と同じ。時間は『譲り（give way）』、受け継がれるもの。"] },
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
        print(f"Success: Added {added} words in Cycle 86.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
