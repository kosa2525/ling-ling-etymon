import json
import re

word_batch = [
    # Cycle 80: Epiphany & Insight
    {
        "id": "revelation_insight",
        "word": "Revelation",
        "meaning": "啓示、驚くべき新事実、(隠されていたものの)暴露",
        "era": "14th Century Old French/Latin re- + velare",
        "etymology": {
            "components": ["re- (opposite, reverse)", "velare (to cover, veil)"],
            "original_statement": "From Old French revelacion, from Latin revelationem, from revelare (unveil, uncover), from re- (opposite of) + velare (to cover, veil)."
        },
        "concept": "Unveiling (「ヴェール（veil）」を剥ぎ取り、隠されていた真実を晒け出すこと)",
        "thinking": "表面的な修正ではなく、今までヴェールに包まれて見えなかったものが、劇的に（しばしば神聖な力によって）開示される瞬間。それは世界の見方を一変させるほどの衝撃を伴います。真実は常にそこにあったけれど、それを見るための準備が整ったとき、ヴェールは静かに（あるいは激しく）取り払われます。",
        "aftertaste": "露（あら）わになる光。もう二度と、知らないふりをして生きていくことはできない。",
        "example": "He had a sudden revelation about the true nature of their friendship during the crisis.",
        "deep_dive": { "roots": [{"term": "weg-", "meaning": "to weave (possible)"}], "points": ["reveal（明かす）や veil（ヴェール）と同じ、織られた境界線の向こう側。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "epiphany_insight",
        "word": "Epiphany",
        "meaning": "悟り、突然のひらめき、公現祭",
        "era": "14th Century Greek epi- + phainein",
        "etymology": {
            "components": ["epi- (upon, to)", "phainein (to show, bring to light)"],
            "original_statement": "From Greek epiphaneia (appearance, manifestation), from epiphanein (to manifest, show forth), from epi- (upon) + phainein (to show, bring to light)."
        },
        "concept": "Manifestation upon (頭上に、あるいは目の前に、真実が「現れ（show）」出ること)",
        "thinking": "日常の何気ない瞬間に、突然「世界の核心」を掴んでしまうような、雷光のような閃き。語源の phainein は「光り輝く」を意味し、暗闇の中にあったパズルの最後のピースがハマり、全体像が光として現れる感覚を指します。それは知的な理解を超えた、魂の「目覚め」に近い体験です。",
        "aftertaste": "閃光。世界が一時停止し、あなたは自分自身と宇宙が一つであるという事実に、ただ立ち尽くす。",
        "example": "While walking home in the snow, she experienced a profound epiphany about her career path.",
        "deep_dive": { "roots": [{"term": "bha-", "meaning": "to shine"}], "points": ["phantom（幻影）や phenomenon（現象：現れるもの）と同じ『光と影』の系譜。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "perspicacity_insight",
        "word": "Perspicacity",
        "meaning": "洞察力、先見の明、鋭い知覚",
        "era": "16th Century Latin per- + specere",
        "etymology": {
            "components": ["per- (through)", "specere (to look at)"],
            "original_statement": "From Latin perspicacitatem (sharp-sightedness), from perspicax (sharp-sighted), from perspicere (to see through, look closely)."
        },
        "concept": "Seeing through (表面的な嘘を「通り抜けて（through）」、その奥を見通すこと)",
        "thinking": "霧の中でも本質を見極めることができる、知的な「視力の鋭さ」。語源の specere は「見る」であり、per- が加わることで、X線のように障壁を通過して確信に辿り着くニュアンスが生まれます。それは単なる頭の良さではなく、物事の背後にある複雑な糸組みを一瞬で解きほぐす、精神の透明度です。",
        "aftertaste": "透き通る世界。あなたが深く見つめるほど、世界の謎はその形を失い、法則へと変わってゆく。",
        "example": "Investors always admired his perspicacity in predicting emerging market trends.",
        "deep_dive": { "roots": [{"term": "spek-", "meaning": "to observe"}], "points": ["perspective（遠近法/視点）や spectator（観客）と同じ、観察する者の力。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "intuition_insight",
        "word": "Intuition",
        "meaning": "直感、直観、内省的な知識",
        "era": "15th Century Latin in- + tueri",
        "etymology": {
            "components": ["in- (at, on, into)", "tueri (to look at, watch over)"],
            "original_statement": "From Late Latin intuitionem (a looking at, gaze), from intueri (to look at, consider), from in- (at, on) + tueri (to look at, watch over)."
        },
        "concept": "Gazing within (自分の「内側（inside）」をじっと「見つめる（gaze）」ことで得られる知識)",
        "thinking": "論理（Logic）の階段を一段ずつ登るのではなく、目的地へと一足飛びに跳躍する、魂のショートカット. 語源の tueri は「守る（tutor）」という意味も含み、内なる精霊があなたの耳元で真実を囁くような感覚です。説明はできないけれど、絶対に正しいと知っている。その静かな、しかし強固な確信。",
        "aftertaste": "震える確信。根拠はない。けれど、あなたのすべての細胞が『これだ』と叫んでいる。",
        "example": "He had an uncanny intuition about people and could always tell when someone was lying.",
        "deep_dive": { "roots": [{"term": "teu-", "meaning": "to pay attention to"}], "points": ["trust（信頼）とも遠い関係にあり、見守り、信じる知性の形。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "discernment_insight",
        "word": "Discernment",
        "meaning": "識別、眼識、わきまえ",
        "era": "16th Century Latin dis- + cernere",
        "etymology": {
            "components": ["dis- (off, apart)", "cernere (to separate, sift)"],
            "original_statement": "From Latin discernere (to separate, set apart, divide, distribute), from dis- (off, away) + cernere (to distinguish, separate, sift)."
        },
        "concept": "Sifting apart (価値あるものとゴミを、ふるい（sift）にかけて「切り分ける（separate）」こと)",
        "thinking": "混沌とした情報の中から、真に価値のある真実だけを選び取る力。語源の cernere は「篩（ふるい）にかける」こと。あえて「切り捨てる（dis-）」ことで、中心にある本質を際立たせます。本物を見分けるためには、まずその周りにある余分なノイズを冷静に選別する「冷徹な知性」が必要なのです。",
        "aftertaste": "選別する指先。削ぎ落としの静寂のなかで、本当に守るべき何かが光を放ち始める。",
        "example": "Classic literature teaches us the discernment of human character in all its complexity.",
        "deep_dive": { "roots": [{"term": "krei-", "meaning": "to sieve, discriminate"}], "points": ["crisis（危機：判断すべきポイント）や critic（評論家）と同じ、峻別（しゅんべつ）のルーツ。"] },
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
        print(f"Success: Added {added} words in Cycle 80.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
