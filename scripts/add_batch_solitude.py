import json
import re

word_batch = [
    # Cycle 97: Solitude & Reflection
    {
        "id": "seclusion_solitude",
        "word": "Seclusion",
        "meaning": "隔離、隠遁、人里離れた場所",
        "era": "15th Century Latin se- + claudere",
        "etymology": {
            "components": ["se- (apart, aside)", "claudere (to shut, close)"],
            "original_statement": "From Latin seclusionem, from secludere (to shut up apart, keep out, exclude), from se- (apart) + claudere (to shut)."
        },
        "concept": "Shut apart (喧騒から離れた場所に、自分を「閉じ込め（shut）」、「隔てる（apart）」こと)",
        "thinking": "社会的な繋がりを一時的に遮断し、自分だけの聖域を確保すること. 語源の se- + claudere は、扉を閉めて外界を閉め出す動作を指します。それは孤独（Loneliness）ではなく、自分の魂の声を聞くための、能動的で贅沢な引き籠もり。沈黙の壁によって守られた、精神の避難所です。",
        "aftertaste": "守られた沈黙。扉を閉めたとき、初めてあなたは、自分の心の奥底で鳴り響く真実の調べに気づく。",
        "example": "He spent the summer in seclusion, finishing his latest novel in a remote mountain cabin.",
        "deep_dive": { "roots": [{"term": "kleu-", "meaning": "hook, peg, key"}], "points": ["close（閉じる）や clause（条項）と同じ、境界を定めるルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "introspection_reflection",
        "word": "Introspection",
        "meaning": "内省、自己反省",
        "era": "17th Century Latin intro- + specere",
        "etymology": {
            "components": ["intro- (inward, within)", "specere (to look at)"],
            "original_statement": "From Latin introspectionem, from introspectus, past participle of introspicere (to look into, look at attentively), from intro- (inward) + specere (to look at)."
        },
        "concept": "Looking inward (自分の内面の奥深くに、鋭い視線を「向け（look）」、観察すること)",
        "thinking": "自分の感情や思考の動きを、あたかも他人の持ち物を調べるように、客観的かつ深く観察するプロセス. 語源の specere は「見る」こと。外側の世界に向かっていた好奇心を180度反転させ、自分という深淵に向ける。そこに広がる未踏の森を探索する、知的で勇気ある行為です。",
        "aftertaste": "内なる探検。あなたは自分の中に、宇宙と同じくらい広大な景色が広がっていることを発見する。",
        "example": "After the failure of his project, he spent weeks in deep introspection, trying to understand his errors.",
        "deep_dive": { "roots": [{"term": "spek-", "meaning": "to observe"}], "points": ["spectacle（光景）や scope（範囲）と同じ。視線は、内側を照らすトーチになる。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "meditation_solitude",
        "word": "Meditation",
        "meaning": "瞑想、熟考、黙想",
        "era": "14th Century Latin mederi",
        "etymology": {
            "components": ["mederi (to heal, cure, measure)"],
            "original_statement": "From Old French meditacion, from Latin meditationem (a thinking over, contemplation), from meditari (to meditate, think over, reflect, consider), related to mederi (to heal)."
        },
        "concept": "Measuring and healing (心のバランスを「量り（measure）」、静寂によって「癒やす（heal）」こと)",
        "thinking": "思考を止めることではなく、特定のテーマや存在そのものに対して、心をゆったりと据え置き、その本質を味わい尽くすこと. 語源の mederi は「治療」や「計測」。瞑想とは、乱れた心の目盛りをゼロにリセットし、自分を魂の健康な状態へと連れ戻すための、聖なる調整です。",
        "aftertaste": "ゼロへの復帰。思考の波が静まるとき、あなたは世界と一つになり、深い平安に癒やされる。",
        "example": "Daily meditation helped him manage the stress of his demanding career.",
        "deep_dive": { "roots": [{"term": "med-", "meaning": "to take appropriate measures"}], "points": ["medicine（薬）や moderate（適度な）と同じ。中庸（バランス）を保つための行為。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "remoteness_solitude",
        "word": "Remoteness",
        "meaning": "遠さ、かけ離れていること、疎遠",
        "era": "15th Century Latin re- + movere",
        "etymology": {
            "components": ["re- (back, away)", "movere (to move)"],
            "original_statement": "From remote (adjective), from Latin remotus (removed, distant, far off), past participle of removere (to move back, take away), from re- (back) + movere (to move)."
        },
        "concept": "Moved back (自分のいる場所から、遥か「遠く（away）」へと「遠ざけ（move）」られていること)",
        "thinking": "ただの物理的な距離ではなく、文明の騒音や日々のしがらみから完全に切り離された「隔絶」の感覚. 語源の movere は「動かす」。遠い場所へ自分を動かしたとき、日常の声はかすかな囁きとなり、星の瞬きが雄弁な言葉となります。孤独が心地よさに変わるための、必要な距離感。",
        "aftertaste": "清冽な隔絶。この遠さがあるからこそ、あなたは誰にも邪魔されず、自分という存在の重さを享受できる。",
        "example": "The remoteness of the village added to its charm, making it a perfect getaway.",
        "deep_dive": { "roots": [{"term": "meue-", "meaning": "to push away"}], "points": ["motion（動き）や mobile（移動可能な）と同じ。移動は、自分を取り戻すための旅。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "contemplation_reflection",
        "word": "Contemplation",
        "meaning": "凝視、熟考、静観",
        "era": "14th Century Latin con- + templum",
        "etymology": {
            "components": ["con- (intensive, together)", "templum (place marked out for observation, sanctuary)"],
            "original_statement": "From Latin contemplationem (surveying, gazing at), from contemplari (to survey, observe, gaze at), from con- (together) + templum (place marked out for observation, space for augury)."
        },
        "concept": "In the sanctuary (「神殿（sanctuary）」のような聖なる空間に身を置き、世界を静かに「眺める」こと)",
        "thinking": "一時の感情に流されず、高い場所から景色を見通すように、物事の全体像をじっと見守ること. 語源の templum は、占い師が空を区切った聖なる空間「テンプル（神殿）」。観照とは、日常の混乱を聖なる図形の中に閉じ込め、そこに潜む意味を読み解こうとする、受容的な知性です。",
        "aftertaste": "神殿のまなざし。あなたはただ、そこにいる。そして世界が語りかけてくるのを、静かに、深く待っている。",
        "example": "He sat in quiet contemplation by the lake, watching the ripples on the water's surface.",
        "deep_dive": { "roots": [{"term": "tem-", "meaning": "to cut (space)"}], "points": ["temple（神殿）や time（時間：区切られたもの）同じ。思考を『区切る』こと。"] },
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
        print(f"Success: Added {added} words in Cycle 97.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
