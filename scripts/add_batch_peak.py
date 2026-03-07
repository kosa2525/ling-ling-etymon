import json
import re

word_batch = [
    # Cycle 116: Crown & Peak
    {
        "id": "pinnacle_peak",
        "word": "Pinnacle",
        "meaning": "頂点、高い峰、小尖塔、最高点",
        "era": "14th Century Latin pinna",
        "etymology": {
            "components": ["pinna (feather, wing, fin)"],
            "original_statement": "From Old French pinacle, from Late Latin pinnaculum (peak, gable, pinnacle), diminutive of Latin pinna (feather; wing; fin)."
        },
        "concept": "Tiny wing (鳥の「羽根（feather）」のように 鋭く天を指し示す 「極小の尖塔（peak）」)",
        "thinking": "どんなに高く険しい道のりも 最終的にはこの「鋭い一点」へと収束していく その極致. 語源は「小さな羽根」. 建築用語としては 尖塔のさらに先端にある細かな装飾を指しますが 転じて 人生の最高潮や 成功の頂を意味するようになりました. それは 脆（もろ）くも美しい 緊張感に満ちた場所です.",
        "aftertaste": "天を衝く尖塔. 頂点に立つことは 孤高であることを意味する. その鋭利な静寂の中で あなたにしか見えない景色を 心ゆくまで刻み込んでおこう.",
        "example": "Reaching the presidency was the pinnacle of his long and distinguished political career.",
        "deep_dive": { "roots": [{"term": "pet-", "meaning": "to rush, fly"}], "points": ["pen（ペン：羽根ペン）や petulant（強情な：突進する）と同じ、鋭さのルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "zenith_peak",
        "word": "Zenith",
        "meaning": "天頂、絶頂、最高点",
        "era": "14th Century Arabic samt",
        "etymology": {
            "components": ["samt (path)"],
            "original_statement": "From Old French zenith, from Old Spanish zenit, from Arabic samt (ar-ras) 'path (of the head)'."
        },
        "concept": "Path of the head (自分の「頭（head）」の 真上を通る 「天の道（path）」)",
        "thinking": "大地から最も離れ 星々と最も近づくことができる 垂直方向の限界点. 語源はアラビア語の「頭上の道」. 天文学的な天頂であると同時に あなたの運勢や才能が 最大限に花開いている 黄金の瞬間を指します. そこは 影が最も短くなり 自分という存在が最も濃密になる場所です.",
        "aftertaste": "真昼の冠. あなたが今 絶頂の中にいるのなら その光を恐れないでほしい. あなたが磨き上げてきた魂が 今 正当に宇宙の真ん中で 輝いているのだから.",
        "example": "He felt that his creative style reached its zenith during his years in Paris.",
        "deep_dive": { "roots": [{"term": "se-", "meaning": "to separate (possible root for path)"}], "points": ["nadir（天底）の対義語。上下の軸がもたらす、存在の垂直性。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "summit_peak",
        "word": "Summit",
        "meaning": "頂上、首脳会談、最高峰",
        "era": "15th Century Latin super",
        "etymology": {
            "components": ["summus (highest)"],
            "original_statement": "From Old French somete, from Latin summum (highest part, summit, highest degree), from summus (highest)."
        },
        "concept": "The highest part (すべてを「合計（sum）」した 結果として現れる 「最高の場所（highest）」)",
        "thinking": "一歩一歩の積み重ね（Sum）が 最後に到達する物理的な限界としての頂. 語源は「最も高い」. 単なる高さだけでなく 重要な決定を下す「首脳会談」の意味を持つのは そこが世界を俯瞰し 導くための場所だからです. 山頂の風は冷たいですが そこには地上の喧騒が届かない 神聖な沈黙があります.",
        "aftertaste": "沈黙の山頂. 山を登りきったとき あなたを待っているのは 賞賛ではなく 宇宙との静かな一体感だ. その孤独な高揚を 魂の糧にしよう.",
        "example": "The mountain summit offered a breathtaking panoramic view of the entire valley below.",
        "deep_dive": { "roots": [{"term": "uper-", "meaning": "over"}], "points": ["summary（要約）や sum（合計）と同じ。本質だけが結集する場所。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "apex_peak",
        "word": "Apex",
        "meaning": "頂点、先端、(三角形などの)頂角",
        "era": "16th Century Latin apex",
        "etymology": {
            "components": ["ap- (to fit, fasten)"],
            "original_statement": "From Latin apex (summit, peak, tip), originally the small rod at the top of a priest's cap, from apere (to fasten, join, fit)."
        },
        "concept": "The fastened tip (神官の帽子の「先端（tip）」に 「固定（fasten）」された 小さな棒のような 象徴的な頂点)",
        "thinking": "広がりを持つ底辺から 幾何学的な必然性を持って 鋭く収束していく「尖った最先端」. 語源は 神官が被る帽子の先端にある飾り. それはある種の「権威」や「神聖さ」が 凝縮されて現れた形です. あなたの知性が 複雑な問題を一つの解に導いたとき その答えは美しいアペックスとなります.",
        "aftertaste": "幾何学の純粋. 無駄なものを削ぎ落としてゆけば 最後にはこの鋭い先端（アペックス）だけが残る. それはあなたの 嘘偽りのない本質の形だ.",
        "example": "The project represents the apex of two years of research and collaboration between multiple departments.",
        "deep_dive": { "roots": [{"term": "ap-", "meaning": "to reach, fasten"}], "points": ["apt（適切な）や approach（近づく）と同じ。到達すべき目標地点。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "culmination_peak",
        "word": "Culmination",
        "meaning": "最高点、絶頂、集大成、(天体の)南中",
        "era": "17th Century Latin culmen",
        "etymology": {
            "components": ["culmen (top, summit, roof)"],
            "original_statement": "From Medieval Latin culminationem, from Latin culminare (to reach the highest point), from culmen (summit, peak)."
        },
        "concept": "Reaching the roof (家の「屋根（roof）」に 辿り着くように 長いプロセスが 「最高点（top）」に達すること)",
        "thinking": "突発的な成功ではなく 粘り強く積み上げてきた努力や物語が ついに実を結び 最高の輝きを放つ「集大成」の瞬間. 語源は「屋根」. それは 基礎を固め 壁を積み上げた者だけが 最後に掲げることのできる 完結の印です. すべての伏線が回収される 美しいフィナーレ.",
        "aftertaste": "集大成の鐘. 長い年月をかけて磨いてきたものが 今 ついに完成の時を迎える. その瞬間の 震えるような達成感を 心の奥に深く刻んでおこう.",
        "example": "The award ceremony was the culmination of many years of dedicated service to the community.",
        "deep_dive": { "roots": [{"term": "kelunit-", "meaning": "high (possible related)"}], "points": ["column（円柱）や hill（丘）と同じ。垂直にそびえ立つもののルーツ。"] },
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
        print(f"Success: Added {added} words in Cycle 116.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
