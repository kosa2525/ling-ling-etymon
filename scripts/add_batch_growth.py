import json
import re

word_batch = [
    # Cycle 91: Expansion & Growth
    {
        "id": "proliferation_growth",
        "word": "Proliferation",
        "meaning": "激増、拡散、増殖",
        "era": "18th Century Latin proles + ferre",
        "etymology": {
            "components": ["proles (offspring)", "ferre (to bear, carry)"],
            "original_statement": "From French prolifération, from proliférer, from Latin proles (offspring) + ferre (to bear, carry)."
        },
        "concept": "Bearing offspring (次々と「子孫（offspring）」を「生み出す（bear）」こと、爆発的な広がり)",
        "thinking": "単なる増加ではなく、細胞が分裂を繰り返すように、一つの核から次々と新しい存在が生まれ、幾何学的に広がっていくプロセス. 語源の proles は命の連鎖を指します。アイデア、技術、あるいは生命。それらが制御不能なほどの勢いで世界を埋め尽くしていく、豊穣（ほうじょう）で、時に畏怖を覚えるほどの生命力を指します。",
        "aftertaste": "止まらぬ連鎖。一つの火花が、いつの間にか全天を焼き尽くすほどの光の海へと変わっている。",
        "example": "The proliferation of digital devices has fundamentally changed how we communicate.",
        "deep_dive": { "roots": [{"term": "al-", "meaning": "to grow, nourish"}, {"term": "bher-", "meaning": "to carry"}], "points": ["pro-（前へ）＋ al-（成長）＋ fer（運ぶ）。未来へと成長を運び続けること。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "burgeon_growth",
        "word": "Burgeon",
        "meaning": "急成長する、芽吹く、発展する",
        "era": "14th Century Old French burjon",
        "etymology": {
            "components": ["burjon (bud, shoot)"],
            "original_statement": "From Old French burjoner (to put forth buds), from burjon (a bud, shoot, pimple)."
        },
        "concept": "Putting forth buds (春の訪れとともに、固い殻を破って「芽（bud）」が吹き出すこと)",
        "thinking": "長い沈黙や準備期間を経て、ついに生命のエネルギーが「形」となって外側の世界へ飛び出す瞬間. それは柔らかく、瑞々（みずみず）しく、しかしアスファルトを突き破るほどの力強さを秘めています。可能性が現実へと変わり始める、最もエネルギッシュで美しい変化のプロセスです。",
        "aftertaste": "芽吹きの予感。内側に溜め込んだ熱が、今、ついに世界という大地を優しく、しかし力強く押し上げている。",
        "example": "The tech industry began to burgeon in the valley during the late 1990s.",
        "deep_dive": { "roots": [{"term": "bhereu-", "meaning": "to swell, boil"}], "points": ["膨らみ（swell）、沸騰する（boil）ほどの内圧。成長は内なる爆発でもある。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "crescendo_growth",
        "word": "Crescendo",
        "meaning": "最高潮、次第に強く、強まり",
        "era": "18th Century Latin crescere",
        "etymology": {
            "components": ["crescere (to grow, increase)"],
            "original_statement": "Italian, literally 'increasing,' from Latin crescendo, gerund of crescere (to grow, increase)."
        },
        "concept": "Increasing in volume (音が、あるいは勢いが、目に見えて「成長（grow）」し続けること)",
        "thinking": "小さなさざ波が、やがて巨大なうねりとなり、最高潮（Peak）へと向かっていくダイナミックなプロセス. 語源の crescere は、三日月（Crescent）が満月へと満ちていく様子も指します。終わりへと向かうのではなく、その「強まっていく過程」そのものが持つ、圧倒的な期待感と高揚感。",
        "aftertaste": "高まる鼓動。静寂を糧にして、音は今、天を突くほどの巨大な叫びへと育っていく。",
        "example": "The public outcry reached a crescendo following the announcement of the new tax hikes.",
        "deep_dive": { "roots": [{"term": "ker-", "meaning": "to grow"}], "points": ["cereal（穀物：成長するもの）や create（創造する）と同じ、生成のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "propagation_growth",
        "word": "Propagation",
        "meaning": "普及、伝播、増殖、(植物の)繁殖",
        "era": "15th Century Latin pro- + pangere",
        "etymology": {
            "components": ["pro- (forth)", "pangere (to fasten, fix)"],
            "original_statement": "From Latin propagationem (a spreading), from propagare (to set forward, extend, spread, multiply), from pro- (forth) + root of pangere (to fasten, fix)."
        },
        "concept": "Fastening forth (苗を「前（forth）」へと「植え付ける（fasten）」ことで、命を広げていくこと)",
        "thinking": "ただ広がるのではなく、一歩ずつ確実に「根」を下ろし、その場所を自分のものにしながら広がっていく着実な拡大. 語源の pangere は「固定する」こと。アイデアや信仰が、人々の心に深く刺さり、そこからまた新しい「芽」を伸ばしていく、静かで抗い難い浸透のプロセスです。",
        "aftertaste": "広がる根。あなたが植えた一粒の言葉は、今この瞬間も、見えない土壌で誰かの魂と結びついている。",
        "example": "The internet allows for the rapid propagation of information across the globe.",
        "deep_dive": { "roots": [{"term": "pag-", "meaning": "to fasten"}], "points": ["page（ページ：文字を固定するもの）や compact（密集した）と同じ、結合のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "nascent_growth",
        "word": "Nascent",
        "meaning": "発生しようとしている、初期の、初発の",
        "era": "17th Century Latin nasci",
        "etymology": {
            "components": ["nasci (to be born)"],
            "original_statement": "From Latin nascentem, present participle of nasci (to be born)."
        },
        "concept": "About to be born (まさに今、「生まれ（born）」ようとしている、未分化の可能性)",
        "thinking": "形になる直前の、もっとも繊細で、しかし最も純粋なエネルギーの塊. まだ名前もつけられていない、新しい時代の胎動。語源の nasci は「誕生」。それは脆弱（ぜいじゃく）でありながら、未来を丸ごと飲み込んでしまうほどの、爆発的な「始まり」の予感に満ちています。",
        "aftertaste": "誕生の直前。産声（うぶごえ）をあげる前の、あの震えるような沈黙の中に、すべての未来が詰まっている。",
        "example": "The nascent space tourism industry faces significant technological and regulatory challenges.",
        "deep_dive": { "roots": [{"term": "gene-", "meaning": "to give birth, beget"}], "points": ["nature（自然：生まれてくるもの）や nation（国家：同じ生まれの集団）と同じ、母なるルーツ。"] },
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
        print(f"Success: Added {added} words in Cycle 91.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
