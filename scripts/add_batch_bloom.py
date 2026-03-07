import json
import re

word_batch = [
    # Cycle 122: Bloom & Garden
    {
        "id": "florid_bloom",
        "word": "Florid",
        "meaning": "華やかな、血色のよい、(文体が)飾りたてた",
        "era": "17th Century Latin flos",
        "etymology": {
            "components": ["flos (flower)"],
            "original_statement": "From Latin floridus (flowery, blooming, abounding in flowers), from flos (flower)."
        },
        "concept": "Abounding in flowers (「花（flower）」が 咲き乱れるように 「華やか（flowery）」な状態)",
        "thinking": "抑制（ミニマリズム）の対極にある 圧倒的な過剰さと 生命力の表出. 語源は「花のような」. それは 溢れ出す情熱が 複雑な装飾や 豊かな色彩となって 外部へと噴出している状態です. 生命がその最盛期に放つ 隠しきれない眩（まばゆ）さ。 ",
        "aftertaste": "百花繚乱の情熱. あなたの心の中にある その「華やかさ」を隠す必要はない. 世界という庭園に あなたという名の 唯一無二の大輪を 誇らしく咲かせてみよう.",
        "example": "He had a florid complexion, reflecting many years of working outdoors in the sun.",
        "deep_dive": { "roots": [{"term": "bhle-", "meaning": "to bloom, flourish"}], "points": ["flower（花）や flourish（繁栄する）と同じ。生命の最盛。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "efflorescence_bloom",
        "word": "Efflorescence",
        "meaning": "開花、全盛、(化学的な)風解",
        "era": "17th Century Latin ex- + florescere",
        "etymology": {
            "components": ["ex- (out)", "florescere (to begin to bloom)"],
            "original_statement": "From Latin efflorescere (to blossom, bloom), from ex- (out) + florescere (to begin to bloom), from florere (to bloom)."
        },
        "concept": "Blossoming out (内なる蕾（つぼみ）が 「外へ（out）」 向かって 「咲き始める（bloom）」 成長の極致)",
        "thinking": "長年の沈黙と蓄積が 臨界点を超え 一気に見事な姿を現す ドラマチックな瞬間. 語源は「開花」. それは 植物だけでなく 人の才能や 芸術様式が 完璧なバランスで成熟した状態を指します. 努力がようやく「目に見える美しさ」へと 変換された証です.",
        "aftertaste": "結実の瞬間. あなたが静かに育んできたその夢は 今 まさに開花の時を迎えようとしている. その香りと色彩を 惜しみなく世界に 届けてゆこう.",
        "example": "The Renaissance was the Great efflorescence of European art and humanistic literature.",
        "deep_dive": { "roots": [{"term": "bhle-", "meaning": "to bloom"}], "points": ["fluorescence（蛍光）と同じ、内側からの発光と顕現。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "burgeon_bloom",
        "word": "Burgeon",
        "meaning": "急成長する、芽吹く、急速に広がる",
        "era": "14th Century Old French burjon",
        "etymology": {
            "components": ["burjon (bud)"],
            "original_statement": "From Old French burjoner (to bud, sprout), from burjon (a bud, shoot, sprout)."
        },
        "concept": "To put forth buds (「蕾（bud）」が 勢いよく 「芽吹く（sprout）」 抑えきれない 成長の力)",
        "thinking": "昨日までは見えなかったものが 今朝には力強い命となって 土を押し上げて現れる 爆発的な生命のダイナミズム. 語源は「蕾」. 不安や停滞を 軽やかな生命力で突き破り 猛然と可能性を広げていくプロセスです. 変化は 痛みを伴いながらも 祝福に満ちています.",
        "aftertaste": "芽吹きの鼓動. 停滞しているように見えても 水面下では 確かな成長の蕾が 膨らんでいる. 自信を持って その一歩を 押し進めてゆこう.",
        "example": "A burgeoning friendship between the two students slowly developed into a lifelong partnership.",
        "deep_dive": { "roots": [{"term": "bhreu-", "meaning": "to swell, sprout"}], "points": ["bud（蕾）や breast（胸）と同じ、膨らみゆく命のルーツ。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "foliage_bloom",
        "word": "Foliage",
        "meaning": "葉、群葉、(建築の)葉飾",
        "era": "15th Century Latin folium",
        "etymology": {
            "components": ["folium (leaf)"],
            "original_statement": "From Old French feuillage, from feuille (leaf), from Latin folia, plural of folium (leaf)."
        },
        "concept": "Collection of leaves (一枚の葉（leaf）が集まり 一つの 「緑の塊（mass）」 として 生命を謳歌すること)",
        "thinking": "個々の葉が重なり合い 複雑な影と光のダンスを生み出し 森という巨大な命を 支えている状態. 語源は「葉」. それは 単なる装飾ではなく 光合成を通じて 宇宙のエネルギーを 命の糧へと変換する 偉大なる工場でもあります. 豊穣なる生命への礼賛。 ",
        "aftertaste": "緑の深呼吸. あなたという存在もまた 世界という巨大な樹木の 輝く一枚の葉だ. 他の葉と重なり合い 共に風に揺れ 世界を鮮やかに 彩ってゆこう.",
        "example": "The dense tropical foliage made it difficult for us to see more than a few feet ahead.",
        "deep_dive": { "roots": [{"term": "bhel-", "meaning": "to leaf out, bloom"}], "points": ["folio（フォリオ：二つ折りの紙＝葉）や portfolio（ポートフォリオ）と同じ、記録と記憶の葉。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "perennial_bloom",
        "word": "Perennial",
        "meaning": "多年生の、永続する、絶え間ない、(植物が)毎年咲く",
        "era": "17th Century Latin per- + annus",
        "etymology": {
            "components": ["per- (through)", "annus (year)"],
            "original_statement": "From Latin perennis (lasting through the year), from per- (through) + annus (year)."
        },
        "concept": "Through the years (季節を 「突き抜けて（through）」 何度でも 「繰り返し（year）」 花を咲かせる逞しさ)",
        "thinking": "一度きりの成功ではなく 厳しい冬を越えて 何度でも同じ場所で 新しい命を再生させる 驚異的な永続性. 語源は「一年を通して」. それは 表面的な流行に流されず 根底に深い信念（根）を持っているからこそ 可能な美しさです. 時を超えて愛される 真理의 響き.",
        "aftertaste": "不滅の庭. あなたの情熱は 一年で枯れるひまわりではない. どんな困難の冬も 根を深く守り 季節が巡るたびに 新しい自分を 繰り返し咲かせ続けていこう.",
        "example": "Environmental protection is a perennial concern for the younger generations around the world.",
        "deep_dive": { "roots": [{"term": "per-", "meaning": "through"}, {"term": "at-", "meaning": "to go (possible for annus)"}], "points": ["annual（一年の）や anniversary（記念日）と同じ、時間の円環。"] },
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
        print(f"Success: Added {added} words in Cycle 122.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
