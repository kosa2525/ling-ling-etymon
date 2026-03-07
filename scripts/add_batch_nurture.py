import json
import re

word_batch = [
    {
        "id": "cradle_life",
        "word": "Cradle",
        "meaning": "ゆりかご、揺藍、発祥の地",
        "era": "Old English cradol",
        "etymology": {
            "components": ["cradol (basket, cradle)"],
            "original_statement": "From Old English cradol, from Proto-Germanic *kradulaz, related to *krat- (to gather, basket)."
        },
        "concept": "A small basket for protection (守るための小さな、編まれた籠)",
        "thinking": "ただ寝る場所ではなく、柔らかな繭（まゆ）のように生命を包み込み、優しく「揺らす」ことで、その成長を促す場所。文明のクレイドル（発祥地）という言葉には、かつてそこで何かが大切に育まれ、世界へと羽ばたく準備をしていたという慈愛の響きが含まれています。",
        "aftertaste": "すべての偉大なものは、一度、この小さな揺らぎの中で眠っていた。",
        "example": "Mesopotamia is often called the cradle of Western civilization.",
        "deep_dive": {
            "roots": [{"term": "ger-", "meaning": "to twist, wind, turn"}],
            "points": ["cart（荷車：回転するもの）や circle（円）と同じルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "nurture_life",
        "word": "Nurture",
        "meaning": "養育する、育てる、育む",
        "era": "14th Century Old French/Latin nutrire",
        "etymology": {
            "components": ["nutrire (to feed, nourish, cherish)"],
            "original_statement": "From Old French norture, from Late Latin nutritura (a nursing, a suckling), from nutrire (to nurse, feed)."
        },
        "concept": "To feed and cherish (栄養を注ぎ込み、大切にいつくしむこと)",
        "thinking": "物理的な食べ物を与えるだけでなく、相手が本来持っている可能性に「光と水」を注ぎ、その個性が花開くのをじっと見守ること。それは、教育（education）よりも遥かに有機的で、魂の奥深くまで潤わせるような、温かく継続的なプロセスの名前です。",
        "aftertaste": "あなたが信じて注いだすべての時間は、いつか、美しき大樹になる。",
        "example": "He spent years nurturing his dream of becoming a writer.",
        "deep_dive": {
            "roots": [{"term": "neu-", "meaning": "to flow, float (possible)"}],
            "points": ["nurse（看護師/保母）や nourish（栄養を与える）と同じ慈愛の系譜。"]
        },
        "part_of_speech": "verb"
    },
    {
        "id": "cherish_life",
        "word": "Cherish",
        "meaning": "慈しむ、大切にする、心に抱く",
        "era": "14th Century Old French/Latin carus",
        "etymology": {
            "components": ["carus (dear, precious)"],
            "original_statement": "From Old French cherir (to cherish), from cher (dear), from Latin carus (dear, precious)."
        },
        "concept": "To hold something as dear (誰（何）かを「最上級に大切なもの」として扱うこと)",
        "thinking": "ただ「持っている」のではなく、それが自分にとって、どれほど「かけがえのない宝物（precious）」であるかを深く自覚し、両手でそっと包み込むこと。壊れやすい美しさ、過ぎ去る時間。それらを心の内側で温め、永遠のものにしようとする、静かな愛の所作です。",
        "aftertaste": "宝物は、持っていることではない。それを『慈しむ心』の中にだけ存在する。",
        "example": "I will cherish the memories of our friendship forever.",
        "deep_dive": {
            "roots": [{"term": "ka-", "meaning": "to desire, love"}],
            "points": ["charity（慈善）や caress（愛撫）と同じ、愛される価値への眼差し。"]
        },
        "part_of_speech": "verb"
    },
    {
        "id": "foster_life",
        "word": "Foster",
        "meaning": "育てる、養う、促進する",
        "era": "Old English fostrian",
        "etymology": {
            "components": ["foda (food)"],
            "original_statement": "From Old English fostrian (to nourish), from fostor (nourishment), related to foda (food)."
        },
        "concept": "Providing food for growth (成長のための糧（かて）を供給し、守ること)",
        "thinking": "血の繋がりを超えて、必要とされる「栄養（food/foda）」と「居場所」を提供し、その存在が社会の中で自立できるよう支援すること。それは、一つの命に対する「無私の貢献」であり、より良い未来を信じて「種」を蒔き続ける、農夫のような尊い行為です。",
        "aftertaste": "あなたの蒔いた糧が、誰かの新しい人生の最初の土台になる。",
        "example": "The city aims to foster a creative environment for local artists.",
        "deep_dive": {
            "roots": [{"term": "pa-", "meaning": "to feed, protect"}],
            "points": ["pasture（牧草地）や food（食べ物）と同じ『養い』の仲間。"]
        },
        "part_of_speech": "verb"
    },
    {
        "id": "bloom_life",
        "word": "Bloom",
        "meaning": "花、開花、最盛期",
        "era": "12th Century Old Norse blom",
        "etymology": {
            "components": ["bhl- (to swell, blossom)"],
            "original_statement": "From Old Norse blome (flower, blossom), from Proto-Germanic *blomon, from PIE root *bhlō- (to swell, bloom)."
        },
        "concept": "A swelling out into life (内側から溢れ出して、生命が開くこと)",
        "thinking": "蕾（つぼみ）がパンパンに「膨らみ（swell）」、その内圧に耐えきれなくなってブワッと外へと開かれる瞬間。それは生命の美しさが極限に達し、その輝きを世界と分かち合う「最盛期」です。ただ咲くだけではなく、生命力がほとばしっていることの代弁。",
        "aftertaste": "長い沈黙の末。内なる熱量が、ついに一つの美しき形として爆発する。",
        "example": "The roses in the garden are in full bloom this month.",
        "deep_dive": {
            "roots": [{"term": "bhel-", "meaning": "to swell"}],
            "points": ["bold（大胆な）や ball（膨らんだもの）と同じ、膨張するエネルギーのルーツ。"]
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
