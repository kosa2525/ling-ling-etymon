import json
import re

word_batch = [
    {
        "id": "habit",
        "word": "Habit",
        "meaning": "習慣、癖、(修道士などの)服",
        "era": "13th Century Old French/Latin habitus",
        "etymology": {
            "components": ["habere (to have, hold)"],
            "original_statement": "From Old French habit, from Latin habitus (condition, appearance, dress), from habere (to have, hold, possess)."
        },
        "concept": "The way one 'holds' oneself (自分をどう持っているか)",
        "thinking": "元々は「持っている状態（condition）」や「外見」を指していました。それが、何度も繰り返されることで身に付いた「自分自身の持ち方（習慣）」となり、さらには身に纏う「特定の服（修道服など）」という意味にもなりました。自分の一部として持っているものです。",
        "aftertaste": "一度身に付けた『持ち物』は、無意識のうちに自分を形作る。",
        "example": "He has a habit of biting his nails when he's nervous.",
        "deep_dive": {
            "roots": [{"term": "ghabh-", "meaning": "to give or receive"}],
            "points": ["ability（能力：持っていること）や inhabit（住む：そこに身を置く）と同根です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "casual",
        "word": "Casual",
        "meaning": "カジュアルな、何気ない、偶然の",
        "era": "14th Century Middle French/Latin casualis",
        "etymology": {
            "components": ["casus (fall, chance, accident)"],
            "original_statement": "From Middle French casuel, from Latin casualis (happening by chance), from casus (fall, chance, occasion)."
        },
        "concept": "Something that 'falls' into place (偶然転がり落ちてきたもの)",
        "thinking": "「落ちる（cadere）」ことに由来する言葉。予測していなかったのに、ふとした拍子に「転がり落ちてきた（casus）」ような偶然の出来事。そこから、気負いのない、形式張らない「何気ない」ニュアンスに発展しました。",
        "aftertaste": "狙ったものではなく、ふとした瞬間の軽やかさ。",
        "example": "We had a casual conversation about the weather.",
        "deep_dive": {
            "roots": [{"term": "kad-", "meaning": "to fall"}],
            "points": ["case（場合）や accident（事故）と同じく、『落ちてくる』感覚がベース。"]
        },
        "part_of_speech": "adjective"
    },
    {
        "id": "routine",
        "word": "Routine",
        "meaning": "ルーチン、日課、決まりきった手順",
        "era": "17th Century French route",
        "etymology": {
            "components": ["route (way, path, road)"],
            "original_statement": "From French routine, from route (way, road, path), from Latin via rupta (broken way, a road forced through)."
        },
        "concept": "A well-beaten path (踏み固められた道)",
        "thinking": "何度も通ることで踏み固められた「道（route）」のこと。迷わずに歩けるその道筋は、思考を介さずに実行できる「いつもの手順」を指すようになりました。日々の繰り返しで作られる心の舗装道路です。",
        "aftertaste": "繰り返すことで、心に確かな道ができてゆく。",
        "example": "Exercise has become part of my daily routine.",
        "deep_dive": {
            "roots": [{"term": "reup-", "meaning": "to snatch, break"}],
            "points": ["rupture（破裂）や corrupt（汚職：共に壊す）の『壊す（break）』が語源。道を切り開く（break through）からです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "sincere",
        "word": "Sincere",
        "meaning": "誠実な、心からの、偽りのない",
        "era": "16th Century Middle French/Latin sincerus",
        "etymology": {
            "components": ["sin- (one)", "cera (wax) - possible folk etymology"],
            "original_statement": "From Latin sincerus (whole, clean, pure), possibly from sem- (one) + crescere (to grow), meaning 'growing as one' (not mixed)."
        },
        "concept": "Pure and unmixed (混じりけのない)",
        "thinking": "俗説では「蜜蝋（wax: cera）を塗っていない」が語源と言われますが、本来は「一つ（sin-）に成長（crescere）している」、つまり外面と内面が分裂していないという『一貫した純粋さ』を指しています。混じりけのない真心のことです。",
        "aftertaste": "表と裏が重なり合う、一点の曇りもない透明感。",
        "example": "I would like to express my sincere gratitude for your help.",
        "deep_dive": {
            "roots": [{"term": "sem-", "meaning": "one, together"}, {"term": "ker-", "meaning": "to grow"}],
            "points": ["create（創造する）や crescent（三日月）の cres-（成長する）が隠れています。"]
        },
        "part_of_speech": "adjective"
    },
    {
        "id": "trivial",
        "word": "Trivial",
        "meaning": "些細な、取るに足らない、ありふれた",
        "era": "15th Century Latin trivialis",
        "etymology": {
            "components": ["tri- (three)", "via (way, road)"],
            "original_statement": "From Latin trivialis (common, ordinary), from trivium (place where three roads meet), from tri- (three) + via (way)."
        },
        "concept": "Found at the crossroads (三叉路で見かけるようなもの)",
        "thinking": "三叉路（trivium）は、人が集まり世間話をするありふれた場所。そこで交わされるような「誰でも知っていること」や「大したことのない話題」が語源です。かつては学問の基礎三科を指しましたが、いつしか「些細な」という意味が強まりました。",
        "aftertaste": "道端に落ちている、ありふれた日常の断片。",
        "example": "Don't get upset over such a trivial matter.",
        "deep_dive": {
            "roots": [{"term": "tri-", "meaning": "three"}, {"term": "wegh-", "meaning": "to go, move"}],
            "points": ["trivia（トリビア）の語源そのもの。街角の雑談が始まりです。"]
        },
        "part_of_speech": "adjective"
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
