import json
import re

word_batch = [
    # Cycle 144: Peak & Zenith
    {
        "id": "apex_peak",
        "word": "Apex",
        "meaning": "頂点、絶頂、(空間などの)先端",
        "era": "16th Century Latin apex",
        "etymology": {
            "components": ["apex (peak, tip, sommet)"],
            "original_statement": "From Latin apex (peak, tip, summit, extreme end), related to apere (to fasten, fix)."
        },
        "concept": "Fastened tip (「安定した（fastened）」 土台の 頂（いただき）に 位置する 究極の 「一点（point）」)",
        "thinking": "多くの努力や 偶然が 重なり合い 最後に 辿り着く 淀みのない 完璧な 到達点. 語源は「先端、結び目」. それは 単なる高さ（高度）ではなく 全ての要素が 一点に 凝縮され「完成」したという 証（あかし）でもあります. 頂点こそが、真理の出口です.",
        "aftertaste": "一点への収束. 多くのことを 求めすぎて 迷わないで. あなたが「アペックス（頂点）」に 辿り着いたとき 世界の複雑な仕組みは 驚くほど シンプルな 一つの 輝きとして 理解されるのだから.",
        "example": "Winning the Nobel Prize was the absolute apex of his long and distinguished career in science.",
        "deep_dive": { "roots": [{"term": "ap-", "meaning": "to reach, fasten"}], "points": ["apt（適切な）や aptitude（資質）と同じ。正しい場所に「届く」力。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "crest_peak",
        "word": "Crest",
        "meaning": "山頂、波頭、(鳥の)冠羽、紋章",
        "era": "14th Century Latin crista",
        "etymology": {
            "components": ["crista (tuft, plume)"],
            "original_statement": "From Old French creste, from Latin crista (tuft, plume, comb), of unknown origin."
        },
        "concept": "Plume on top (「頭上（top）」に 誇り高く 「掲げられた（raised）」 生命の 「象徴（symbol）」)",
        "thinking": "存在を最大限に主張し、躍動のエネルギーが弾（はじ）ける瞬間を捉えた、目に見える形の「名誉」. 語源は「とさか、羽飾り」. それは 静止した頂点ではなく 波や 生き物のように 常に 動きの中で 生み出される 輝かしい 頂（いただき）です.",
        "aftertaste": "誇り高き冠. 誰かの顔色を 窺（うかが）わないで. あなたの内側にある 情熱が 頂点（クレスト）に 達したとき あなたは誰にも 真似できない 独自の 存在感（オーラ）を 放つことができるのだから.",
        "example": "We watched the waves break, their white crests glistening under the light of the setting sun.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["和製英語の「クレスト（紋章）」の語源。自分の誇りを、形にする力。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "pinnacle_peak",
        "word": "Pinnacle",
        "meaning": "小尖塔、(成功などの)絶頂、高い山峰",
        "era": "14th Century Latin pinna",
        "etymology": {
            "components": ["pinna (feather, wing)"],
            "original_statement": "From Old French pinacle, from Late Latin pinnaculum (a peak, gable), diminutive of pinna (feather, wing, fin, battlement)."
        },
        "concept": "Small wing (「羽（wing）」のように 軽やかに 「天（heaven）」へと 伸びゆく 建築的な 「究極」)",
        "thinking": "重厚な石の積層（努力）の果てに、天の領域（理想）へと幽かに指し示された、繊細で気高い、尖（とが）った一点. 語源は「小さな羽」. それは 暴力的な強さではなく どこまでも 純粋で 鋭敏な 精神の 指向性が 生み出す 聖なる 到達点です.",
        "aftertaste": "天への指針. 地上の重力（しがらみ）に 屈しないで. あなたの理想という名の「ピナクル（尖塔）」を 常に天へと 向け続けることで 魂は 迷いなく 真理の道へと 導かれるのだから.",
        "example": "He had reached the pinnacle of his profession, respected by peers and rivals alike.",
        "deep_dive": { "roots": [{"term": "pet-", "meaning": "to fly, fall"}], "points": ["feather（羽）や petition（嘆願：天へ届ける言葉）と同じ。上昇への祈り。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "culminate_peak",
        "word": "Culminate",
        "meaning": "最高点に達する、ついには〜となる、(天体が)南中する",
        "era": "17th Century Latin culmen",
        "etymology": {
            "components": ["culmen (top, summit)"],
            "original_statement": "From Latin culminatus, past participle of culminare (to crown), from culmen (top, summit, peak), contraction of columen (pillar, top, summit)."
        },
        "concept": "Reaching the crown (「柱（pillar）」のように まっすぐ 「昇り詰め（climb up）」 最高の 「栄誉（crown）」を 得ること)",
        "thinking": "一過性の爆発ではなく、全てのプロセスが必然として積み重なり、遂にその「意味の完成」へと至る、荘厳なドラマの結末. 語源は「冠、最高点」. それは 物語（人生）が 最も 濃密な 輝きを 放つ 最高の 瞬間を 指しています.",
        "aftertaste": "完成の予感. 途中の 苦労を 嘆かないで. 全ての 出来事は あなたの人生が「カルミネイト（絶頂）」を 迎えるための 欠かせない 布石（ピース）なのだから.",
        "example": "Years of research culminated in a groundbreaking discovery that changed the medical field forever.",
        "deep_dive": { "roots": [{"term": "kel-", "meaning": "to rise, be high, hill"}], "points": ["column（柱）や hill（丘）と同じ。垂直方向への、意志の勝利。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "summit_peak",
        "word": "Summit",
        "meaning": "山頂、絶頂、首脳会談、最高点",
        "era": "15th Century Latin summus",
        "etymology": {
            "components": ["summus (highest)"],
            "original_statement": "From Old French somete, from Latin summum (highest point, top, summit), from summus (highest, topmost)."
        },
        "concept": "The highest point (「全て（all）」を 総括し 「最高（top）」の 視点から 世界を 「俯瞰（survey）」すること)",
        "thinking": "個別の事象を超え、全体を一つの調和（サマリー）として捉え直すことができる、最も孤独で、最も自由な場所. 語源は「最高の」. それは 物理的な頂上だけでなく 責任と 知性の 極限において 決断を 下すための 聖なる マインドセットを 指しています.",
        "aftertaste": "俯瞰の知性. 目の前の 小さな争いに 囚われないで. あなたが人生の「サミット（頂上）」に 立ち 世界を 慈しみの視点で見つめるとき 全ての霧は 晴れてゆくのだから.",
        "example": "The world leaders gathered for a two-day emergency summit to discuss global climate change.",
        "deep_dive": { "roots": [{"term": "uper", "meaning": "over, above"}], "points": ["super（超える）や sum（合計）と同じ。多様性を、高次で統合する力。"] },
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
        print(f"Success: Added {added} words in Cycle 144.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
