import json
import re

word_batch = [
    # Cycle 104: Transcendence & Beyond
    {
        "id": "ethereal_beyond",
        "word": "Ethereal",
        "meaning": "優美な、霊妙な、この世のものとは思えない",
        "era": "16th Century Greek aither",
        "etymology": {
            "components": ["aither (upper air, pure air, sky)"],
            "original_statement": "From Latin aetherius, from Greek aitherios (of or pertaining to the upper air), from aither (pure air, ether)."
        },
        "concept": "Of the upper air (「天上の空気（upper air）」のように、希薄で、光に満ちた「霊妙（spiritual）」な美しさ)",
        "thinking": "重力や肉体といった物質的な束縛から解き放たれ、ただ光と風の粒子だけで構成されているかのような、危ういほどの気高さ. 語源の aither は、神々が呼吸する最も純粋な大気。それは、地上にありながら天上の記憶を運び、見る者の魂を一瞬にして高みへと引き上げる、奇跡のような存在感です。",
        "aftertaste": "天上の薫り。あなたは今、日常という重たい靴を脱ぎ捨て、魂という名の光の翼で、未知の青空を泳いでいる。",
        "example": "The singer's ethereal voice seemed to transport the audience to another world.",
        "deep_dive": { "roots": [{"term": "aidh-", "meaning": "to burn, glow"}], "points": ["edifice（大建築物：崇高なもの）や ether（エーテル）と同じ、輝きのルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "ephemeral_beyond",
        "word": "Ephemeral",
        "meaning": "はかない、一時の、一日限りの",
        "era": "16th Century Greek epi- + hemera",
        "etymology": {
            "components": ["epi- (on, upon)", "hemera (day)"],
            "original_statement": "From Greek ephemeros (lasting only a day), from epi- (upon) + hemera (day)."
        },
        "concept": "Upon a day (「一日（day）」という短い時間の「器（upon）」の中にだけ存在する、極限の「はかなさ」)",
        "thinking": "咲いた瞬間に散り始める花や、朝霧の中に消える虹のように、その美しさが永遠ではないからこそ、狂おしいほどに愛おしく、気高いこと. 語源は「一日限りの」。失われることがあらかじめ約束されている、その残酷なまでの「今」という瞬間の輝きに、私たちは真実を見出します。",
        "aftertaste": "一瞬の永遠。消えゆくものへの愛惜が、あなたの心をより深く、より優しく、今この瞬間に繋ぎ止める。",
        "example": "The beauty of cherry blossoms is notoriously ephemeral, lasting only a few days.",
        "deep_dive": { "roots": [{"term": "epi-", "meaning": "on"}, {"term": "amer-", "meaning": "day"}], "points": ["hemera は『昼』の意味も。太陽が昇り、沈むまでの、短い祝福。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "transient_beyond",
        "word": "Transient",
        "meaning": "一時的な、移り変わる、はかない",
        "era": "17th Century Latin trans- + ire",
        "etymology": {
            "components": ["trans- (across)", "ire (to go)"],
            "original_statement": "From Latin transientem (passing over or away), from transire (to go over, pass over), from trans- (across) + ire (to go)."
        },
        "concept": "Going across (ある場所から別の場所へ、「通り過ぎ（pass）」、決して「留まらない（not stay）」こと)",
        "thinking": "自分という場所を、出来事や感情がただ通り過ぎていく旅人のような性質. 語源の trans- + ire は「境界を越えて行く」。すべては流転し、固定された安住の地などどこにもない。けれど、その「通り過ぎる」という動的なプロセスの中にこそ、生命の真の躍動と自由が宿っています。",
        "aftertaste": "旅する魂. 留まろうとすることをやめたとき、あなたは世界という大きな旅の一部になり、軽やかになれる。",
        "example": "The feelings of anger were transient, and he soon regained his composure.",
        "deep_dive": { "roots": [{"term": "ter-", "meaning": "to cross over"}, {"term": "ei-", "meaning": "to go"}], "points": ["exit（出口）や transition（変遷）と同じ。移動は、進化。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "ultramundane_beyond",
        "word": "Ultramundane",
        "meaning": "超俗的な、現世の外の、天上の",
        "era": "17th Century Latin ultra- + mundus",
        "etymology": {
            "components": ["ultra- (beyond)", "mundus (world)"],
            "original_statement": "From Latin ultra (beyond) + mundus (world)."
        },
        "concept": "Beyond the world (この俗世という「世界（world）」の「向こう側（beyond）」にある、超越的な領域)",
        "thinking": "日々の損得や、人間の小さな愛憎が一切届かない、宇宙的な沈黙と光の領域. 語源の ultra は「極限」。mundus は「整理された世界」。人間の秩序を遥かに超越した、冷徹で、しかし絶対的な美を持つ場所。そこには、星々の運行と同じ、厳粛な真理だけが漂っています。",
        "aftertaste": "現世の向こう側。日常という名の檻（おり）を抜け出し、あなたは今、永遠の風が吹く荒野に立っている。",
        "example": "The composer's later works have an almost ultramundane quality, untouched by earthly concerns.",
        "deep_dive": { "roots": [{"term": "al-", "meaning": "beyond"}, {"term": "me-", "meaning": "to world (possible root)"}], "points": ["mundane（日常の）の対極. 世界の秩序を塗り替える超越。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "metaphysical_beyond",
        "word": "Metaphysical",
        "meaning": "形而上学的な、極めて抽象的な、現実離れした",
        "era": "16th Century Greek meta- + physika",
        "etymology": {
            "components": ["meta- (after, beyond)", "physika (physics, nature)"],
            "original_statement": "From Medieval Latin metaphysicus, from Greek (ta) meta (ta) physika (that which comes after the physical), the title of Aristotle's treatise on the subject."
        },
        "concept": "After nature (肉体や物質といった「自然（nature）」の「後に（after）」、あるいは「背後に（beyond）」隠された真理)",
        "thinking": "目に見える果実（現象）の下に隠された、目に見えない根（原理）を探求すること. 語源はアリストテレスの著書の配列順（自然学＝フィジカの『後』）に由来。物質的な便利さを超えて、なぜ私たちはここに在り、どこへ向かうのかという、魂の最も深い問いに答えようとする営みです。",
        "aftertaste": "背後の真実。目に見えるものはすべて、目に見えない巨大な意味の、氷山の一角に過ぎない。",
        "example": "The poet explored the metaphysical connections between the human soul and the vast universe.",
        "deep_dive": { "roots": [{"term": "meta-", "meaning": "change, after"}, {"term": "bheu-", "meaning": "to grow, be"}], "points": ["physics（物理学）や nature（自然）の根本を探る。在ることの意味。"] },
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
        print(f"Success: Added {added} words in Cycle 104.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
