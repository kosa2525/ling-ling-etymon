import json
import re

word_batch = [
    # Cycle 137: Mirror & Symmetry (Refinement)
    {
        "id": "speculum_mirror",
        "word": "Speculum",
        "meaning": "鏡、反射体、(医学)検鏡、翼鏡",
        "era": "16th Century Latin specere",
        "etymology": {
            "components": ["specere (to look at, behold)"],
            "original_statement": "From Latin speculum (mirror), from specere (to look at, behold, see)."
        },
        "concept": "Instrument for looking (「見る（look）」ための 「道具（instrument）」 としての 澄み切った 「鏡面」)",
        "thinking": "受動的に映るだけでなく 自らの意思によって 真実を「見出す」ための 聖なる覗き窓（ウィンドウ）. 語源は「見るためのもの」. 医療で体の深部を照らすように この「スペキュラム（鏡）」は 私たちの意識の奥底にある 隠れた光や 影を 鮮明に浮かび上がらせる 知性のツールです.",
        "aftertaste": "深部の探究. 外側の美しさに 惑わされないで. あなたの心の鏡を 磨き上げ、奥底を照らす（スペキュラム）ことで 誰にも奪えない 真実の自分を 救い出すことができるのだから.",
        "example": "The physician used a specialized speculum to examine the patient's inner ear more clearly.",
        "deep_dive": { "roots": [{"term": "spek-", "meaning": "to observe"}], "points": ["species（種：見える形）や scope（視野）と同じ。世界の解像度を上げる力。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "rebound_balance",
        "word": "Rebound",
        "meaning": "跳ね返る、立ち直る、(バスケ)リバウンド",
        "era": "14th Century re- + bound (to leap)",
        "etymology": {
            "components": ["re- (back)", "bound (to leap, jump)"],
            "original_statement": "From Old French rebondir (to leap back), from re- (back) + bondir (to leap, jump)."
        },
        "concept": "Leaping back (「衝撃（impact）」を 成長の 「ばね（spring）」に変えて 再び 「高く跳ぶ（leap）」こと)",
        "thinking": "沈み込み（絶望）があればあるほど その力（エネルギー）を 利用して より高く、より強く 復活を遂げるという 生命 warehouse の強靭な パターン. 語源は「跳ね返り」. それは 失敗を「終わり」と捉えるのではなく 次の飛躍のための 助走として 祝福する 逞しい生命力のアクションです.",
        "aftertaste": "跳躍の季節。どん底にいることを 嘆かないで。今はただ「リバウンド」するための エネルギーを 溜めているだけなのだから。次に跳ぶときは 以前よりも ずっと高い場所へ 辿り着けるはずだ。",
        "example": "The economy showed a surprising rebound after the major financial crisis began to subside.",
        "deep_dive": { "roots": [{"term": "re-", "meaning": "back"}, {"term": "unknown", "meaning": "none"}], "points": ["bondir（跳ぶ）は元々「大きな音を立てる」という意味。存在の力強い顕現。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "parity_balance",
        "word": "Parity",
        "meaning": "同等、等価、均衡、(物理)パリティ",
        "era": "16th Century Latin par",
        "etymology": {
            "components": ["par (equal)"],
            "original_statement": "From Latin paritas (equality), from par (equal, same, like)."
        },
        "concept": "State of equal (上下や 貴賤ではなく 「等しい（equal）」 尊厳を持って 向き合う 「水平（horizontal）」な 均衡)",
        "thinking": "力の差による支配を捨て お互いを 唯一無二の「対等な存在」として 認め合うことで生まれる 平和な秩序. 語源は「等しさ」. それは 完璧な一致ではなく お互いの「重み（価値）」が 釣り合っているという 黄金律（バランス）の 究極の形です.",
        "aftertaste": "対等の祝福. 誰かを「下」に見ることは 自分を「上」に縛り付けることだ. 全てのものとの「パリティ（同等性）」を 認めることで あなたは本当の自由と 安らぎを 手にすることができるのだから.",
        "example": "The two major political parties are currently struggling to achieve parity in popular support.",
        "deep_dive": { "roots": [{"term": "per-", "meaning": "to assign, allot (possible for par)"}], "points": ["compare（比較する：等しく並べる）や peer（貴族、仲間）と同じ。価値の共有。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "poise_balance",
        "word": "Poise",
        "meaning": "落ち着き、釣り合い、平衡、身構え",
        "era": "14th Century Latin pendere",
        "etymology": {
            "components": ["pendere (to weigh)"],
            "original_statement": "From Old French pois (weight, balance, scales), from Latin pensum (something weighed out), from pendere (to weigh, pay, cause to hang)."
        },
        "concept": "Weighted balance (「重み（weight）」を 知ることで 生まれる 揺るぎない 「静かな（composed）」 均衡)",
        "thinking": "外側の嵐（激動）に 振り回されることなく 自分の内側にある 「秤（はかり）」の 中心（センター）を じっと見つめ続ける 精神の気高さ. 語源は「重さを量ること」. それは 停滞ではなく 絶え間ない微調整によって 保たれる 尊厳に満ちた「美しき身構え」です.",
        "aftertaste": "静止する真剣。焦って動き出さないで。自分の中の「ポイズ（平衡）」が 整うのを じっと待つのだ。整った一歩は どんな力強い疾走よりも 遥かに遠くまで あなたを運んでくれるのだから。",
        "example": "Despite the intense pressure of the broadcast, she maintained her poise and delivered a perfect speech.",
        "deep_dive": { "roots": [{"term": "spen-", "meaning": "to draw, stretch, spin"}], "points": ["depend（依存する：ぶら下がる）や pound（ポンド：重さ）と同じ。存在の重力。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "compensate_balance",
        "word": "Compensate",
        "meaning": "埋め合わせる、補償する、償う、相殺する",
        "era": "17th Century Latin con- + pendere",
        "etymology": {
            "components": ["con- (together)", "pendere (to weigh)"],
            "original_statement": "From Latin compensatus, past participle of compensare (to weigh one thing against another), from con- (together, with) + pensare, frequentative of pendere (to weigh)."
        },
        "concept": "Weighing together (欠けた部分を 「他の重み（other weight）」で 補い 再び 「釣り合い（balance）」を 取ること)",
        "thinking": "失われたものや 過ち（マイナス）を 恨みとして残すのではなく 新しい価値（プラス）を 差し出すことで 宇宙の帳尻を 合わせようとする 愛の試み. 語源は「共に測る」. それは 自分の不完全さを 認め 誠実さによって 均衡を 取り戻そうとする 尊い回復のプロセスです.",
        "aftertaste": "均衡の回復. 失ったものを 数えなくていい. 今 あなたができる「補償（コンペンセイト）」は 何か. その誠実な一歩が あなたの世界の 破れた調和を 再び美しく 繋ぎ合わせてゆくのだから.",
        "example": "He tried to compensate for his lack of experience by working harder than anyone else in the office.",
        "deep_dive": { "roots": [{"term": "spen-", "meaning": "to draw, stretch, spin"}], "points": ["pension（年金：量られた分配）や expense（費用）と同じ。命の分配と均衡。"] },
        "part_of_speech": "verb"
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
        print(f"Success: Added {added} words in Cycle 137.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
