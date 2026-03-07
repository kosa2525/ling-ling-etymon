import json
import re

word_batch = [
    # Cycle 126: Gravity & Center
    {
        "id": "gravitation_center",
        "word": "Gravitation",
        "meaning": "重力、引力、(思想などへの)惹き付けられる力",
        "era": "17th Century Latin gravis",
        "etymology": {
            "components": ["gravis (heavy, serious)"],
            "original_statement": "From Modern Latin gravitationem, from gravitare (to weigh, gravitate), from Latin gravis (heavy, serious, important)."
        },
        "concept": "State of being heavy (「重さ（heavy）」を 持つことで 他の存在を 「惹き付ける（attract）」 宇宙の法則)",
        "thinking": "単なる物理現象ではなく 魂が本質的な価値や 巨大な愛（中心）に向かって 抗（あらが）いようもなく 惹き寄せられていく その「切実な渇望」. 語源は「重いこと」. あなたが何かに強く惹かれるとき そこには 逃れられない 聖なる重力が 働いているのです.",
        "aftertaste": "魂の重力. 惹きつけられる力に 逆らわないで. その「重さ」こそが あなたが今 ここに存在し 世界と深く関わっているという 揺るぎない証なのだから.",
        "example": "The artistic gravitation towards more abstract forms defined the movement of the decade.",
        "deep_dive": { "roots": [{"term": "gwere-", "meaning": "heavy"}], "points": ["grave（重大な、墓：重みのある場所）や grief（悲しみ：重苦しい感情）と同じ、重厚さのルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "centripetal_center",
        "word": "Centripetal",
        "meaning": "求心の、中心にむかう",
        "era": "17th Century Latin centrum + petere",
        "etymology": {
            "components": ["centrum (center)", "petere (to seek)"],
            "original_statement": "From New Latin centripetus, from centrum (center) + petere (to seek)."
        },
        "concept": "Seeking the center (「中心（center）」を 狂おしく 「追い求める（seek）」 収束のエネルギー)",
        "thinking": "拡散し、霧散しそうになる自己を ぐっと内側へと繋ぎ止め 唯一の「核」へと 立ち戻らせようとする 強い意志のベクトル. 語源は「中心を求める」. 情報過多で自分を見失いそうな時代こそ この「求心力」を研ぎ澄まし 自分の重心を 確実に見定めることが必要です.",
        "aftertaste": "内側への帰還. 外界の喧騒に 魂を奪われないで. 常に自分の「中心（センター）」を問い続け そこにある静止した情熱へと 立ち戻る努力を 忘れないようにしよう.",
        "example": "The centripetal force of his personality kept the diverse team focused on a single goal.",
        "deep_dive": { "roots": [{"term": "kentron-", "meaning": "to prick, point"}, {"term": "pet-", "meaning": "to rush, fly"}], "points": ["centrifugal（遠心の：中心から逃げる）の対義語。一点への疾走。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "ballast_center",
        "word": "Ballast",
        "meaning": "底荷、バラスト、(精神的な)安定、重石",
        "era": "16th Century Middle Dutch bal- + last",
        "etymology": {
            "components": ["bad (useless, bad)", "last (load)"],
            "original_statement": "Possibly from Middle Low German ballast, from bal- (useless, bad) + last (load, burden); perhaps 'useless load' because it's not commercial cargo but serves for stability."
        },
        "concept": "Necessary burden (「不要な荷（useless load）」で ありながら 荒波の中で 「安定（stability）」を 保つために 不可不可な重石)",
        "thinking": "華やかな成功や利益（貨物）ではないけれど 自分の人生という船が 転覆しないために 心の底に深く沈めておくべき「重い教訓」や「哲学」. 語源は「役に立たない荷物」. 一見無駄に見える苦労や 孤独な時間こそが あなたの人生に 誰にも揺るがされない 安定（バラスト）をもたらします.",
        "aftertaste": "沈黙のバランス. あなたが抱えている その「重荷」は あなたを苦しめるためのものではない. それは 激動の時代という海を あなたが優雅に、そして力強く 渡り切るための 聖なる重石なのだ.",
        "example": "His deep religious faith provided the spiritual ballast he needed during those turbulent years.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["船舶用語からの転用。見えない部分の「重さ」が、見える部分의「自由」を支える。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "poise_center",
        "word": "Poise",
        "meaning": "落ち着き、釣り合い、平衡、(動作の)端正さ",
        "era": "14th Century Latin pendere",
        "etymology": {
            "components": ["pendere (to weigh)"],
            "original_statement": "From Old French pois (weight), earlier pess (weight), from Latin pensum (weight, portion of wool weighed out), from pendere (to weigh)."
        },
        "concept": "The weighed state (「重さ（weight）」を 「量り、整える（weigh）」 ことで生まれる 静かで 完璧な 「平衡（equilibrium）」)",
        "thinking": "激しい動きのただ中にあっても 自分の重心（センター）を 完璧に掌握し いつでも次の瞬間へと 移行できる 凛とした静止状態. 語源は「重さを量ること」. それは 外側からの力に対抗するのではなく 自らの重みを 正しく自覚し 宇宙の調和（バランス）へと 調律し直す知的な力です.",
        "aftertaste": "凛冽たる静止. 焦らず、気負わず、ただ自分の「重み」を 信じて佇んでごらん. その揺るぎない「ポイズ（端正さ）」こそが 世界を静かに 圧倒してゆくのだから.",
        "example": "Even under intense pressure, the young diplomat maintained an extraordinary level of poise and grace.",
        "deep_dive": { "roots": [{"term": "pendo-", "meaning": "to hang, weigh"}], "points": ["pendant（ペンダント）や compensate（補足する：釣り合わせる）と同じ。測定と調和。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "equilibrium_center",
        "word": "Equilibrium",
        "meaning": "均衡、平衡、心の平安",
        "era": "17th Century Latin aequus + libra",
        "etymology": {
            "components": ["aequus (equal)", "libra (balance, weight)"],
            "original_statement": "From Latin aequilī brium (horizontal position, balance), from aequilī bris (balanced), from aequus (equal) + libra (balance, pair of scales)."
        },
        "concept": "Equal balance (「重さ（weight）」が 「等しく（equal）」 釣り合い あらゆる 葛藤（conflict）が 静止（stillness）した 奇跡の瞬間)",
        "thinking": "対立する力が 完全に拮抗（きっこう）し 完璧な静寂が訪れている 極致の状態. 語源は「等しい天秤」. それは どちらか一方が勝つのではなく 両方の価値を 正しく認め合うことでしか 辿り着けない 聖なる沈黙です. 心の「イクイリブリアム（均衡）」は 知性と愛が 交わる場所に 宿ります.",
        "aftertaste": "天秤の祈り. 私たちの心は常に 激しく揺れ動いている. しかし その揺らぎの極致には 必ずこの「完璧な静止」が 待っていることを 決して忘れないで.",
        "example": "The yoga teacher emphasized the importance of finding one's internal equilibrium through mindful breathing.",
        "deep_dive": { "roots": [{"term": "aik-", "meaning": "equal"}, {"term": "lithra-", "meaning": "pound, unit of weight"}], "points": ["libra（てんびん座）と同じ。公正と調和の象徴。"] },
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
        print(f"Success: Added {added} words in Cycle 126.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
