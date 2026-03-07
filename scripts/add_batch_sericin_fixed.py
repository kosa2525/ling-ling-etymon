import json
import re

word_batch = [
    # Cycle 163: Silk & Softness (Refined)
    {
        "id": "sericin_silk",
        "word": "Sericin",
        "meaning": "セリシン、絹膠(けんこう)",
        "era": "19th Century Greek serikos",
        "etymology": {
            "components": ["serikos (silken)", "Seres (the people from whom silk was obtained, the Chinese)"],
            "original_statement": "From Greek serikos (silken), related to Ser (a Silk-worm), and Seres (the Silk-people, the Chinese)."
        },
        "concept": "Silk glue (「純粋な絹（fibroin）」を 「一つ（one）」に 纏める（まとめる） 「膠（glue）」のように 万物を 「慈愛」で 包み込むこと)",
        "thinking": "表に出る 輝き（シルク）を 陰で 支え、繊細な 繊維を 守り、繋ぎ止める、目に見えない 献身の 知性. 語源は「絹の、東方の民の」. それは 自分の 主張 ではなく 他者の 輝きを 最大限に 引き出すための 聖なる「潤滑剤」と 絆の 表現です. 守りは、愛です.",
        "aftertaste": "見えない絆. 自分の 役割が 小さく 見えても 嘆かないで. あなたが「セリシン（絹膠）」のように 誰かを 支え 繋ぎ合わせているからこそ この世界には 美しい 輝きの 織物（シルク）が 存在できるのだから.",
        "example": "Sericin is a protein created by silkworms that holds the silk fibers together in a cocoon.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["Silk（シルク）の 語源となった セレス（中国の人々）との 繋がり。遥かなる 道（シルクロード）の記憶。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "velvety_softness",
        "word": "Velvety",
        "meaning": "ベルベットのような、滑らかな、柔らかい",
        "era": "16th Century Latin villus",
        "etymology": {
            "components": ["villus (shaggy hair, tuft of hair)"],
            "original_statement": "From velvet + -y, from Old French velu (shaggy, hairy), from Latin villus (shaggy hair, tuft of wool)."
        },
        "concept": "Shaggy elegance (「無数の微細な毛（infinite hairs）」が 「光（light）」を 「深層（depth）」へと 誘い（いざない） 魂を 「安堵」させる 質感)",
        "thinking": "平坦な 滑らかさ ではなく、触れるたびに 指先が 沈み込み、世界の 攻撃性を 無効化してしまうような、圧倒的な 受容の 極致. 語源は「むく毛、羊毛の房」. それは 激しい 主張 ではなく 全てを 優しく 包み込み、沈黙（シャイン）の中に 意味を 溶け込ませる 聖なり「慈愛」の 表現です.",
        "aftertaste": "受容の極致. 世界の 厳しさに 疲れたとき 自分の 内側にある「ヴェルヴェティ（滑らかな）」な 優しさを 思い出そう. その 深い 柔らかさの中にこそ 傷ついた 魂が 真に 休息できる 聖なる場所が あるのだから.",
        "example": "The red wine had a rich, velvety texture that lingered long on the palate.",
        "deep_dive": { "roots": [{"term": "wel-", "meaning": "to hair, wool"}], "points": ["wool（羊毛）や villi（絨毛）と同じ。生命を 温めるための、原初的な 装備。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "mollify_softness",
        "word": "Mollify",
        "meaning": "和らげる、なだめる、(苦痛などを)軽減する",
        "era": "14th Century Latin mollis",
        "etymology": {
            "components": ["mollis (soft)", "facere (to make)"],
            "original_statement": "From Old French mollifier, from Late Latin mollificare (to make soft), from Latin mollis (soft) + facere (to make)."
        },
        "concept": "Making soft (「硬化（hardening）」した 「心（heart）」に 「慈悲（mercy）」という名の 「水（water）」を 注ぎ 「柔軟（flexibility）」を 取り戻すこと)",
        "thinking": "力によって 屈服させる のではなく、相手の 頑なな（かたくなな）境界線を 解きほぐし、再び 命が 流れるように 導く、高度な 共感の アート. 語源は「柔らかくすること」. それは 弱さ ではなく どんな 強固な 壁も 溶かしてしまう 聖なる「愛の 浸透力」の 表現です. 許しは、潤いです.",
        "aftertaste": "和解の浸透. 怒りの 鎧（よろい）を 着たままの 誰かを 責めないで. あなたが「モリファイ（和らげる）」な 言葉で そっと 触れるとき その 頑なな（かたくなな）心は 魔法のように 解け（とけ） 新しい 絆が 芽生えるのだから.",
        "example": "The manager tried to mollify the angry customer by offering a sincere apology and a full refund.",
        "deep_dive": { "roots": [{"term": "mldu-", "meaning": "soft"}], "points": ["mild（穏やかな）や melt（溶ける）と同じ。境界を 溶かし 一体化する力。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "gossamer_silk",
        "word": "Gossamer",
        "meaning": "繊細な、非常に薄い、蜘蛛の糸、(秋の日の)薄霧",
        "era": "14th Century Middle English gosesomer",
        "etymology": {
            "components": ["gos (goose)", "somer (summer)"],
            "original_statement": "Probably from goose + summer, perhaps referring to 'St. Martin's summer' (a period of mild weather in late autumn) when geese are eaten and spider webs are common."
        },
        "concept": "Goose summer (「秋（autumn）」の 終わりの 「幽かな希望（faint hope）」のように 「透明（transparent）」で 「儚い（fragile）」 繋がり)",
        "thinking": "存在するか どうかも 分からないほどの 幽かな（かすかな）輝きでありながら、光を 浴びた瞬間に、この 世界が 美しい 繋がりで 満ちていることを 証明する、奇跡的な 繊細さ. 語源は「ガチョウ、夏（小春日和）」. それは 執着 ではなく 漂う（サスペンド）ことに よってのみ 保たれる 聖なる「純粋さ」の 表現です. 儚さは、真実です.",
        "aftertaste": "繊細な導き. 自分の 想いが 弱く 儚く思えても 絶望しないで. あなたの「ゴッサマー（繊細な）」な 繋がりの 糸が 世界を 密かに 結びつけ 誰かの 心を 救う 聖なる 網目に なっているのだから.",
        "example": "The morning dew sparkled on the gossamer threads of a spider's web stretched between the trees.",
        "deep_dive": { "roots": [{"term": "ghans-", "meaning": "goose"}, {"term": "sem-", "meaning": "summer"}], "points": ["小春日和（聖マルティンの夏）という、死の前の 最後の 輝き。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "supple_softness",
        "word": "Supple",
        "meaning": "しなやかな、柔軟な、(態度が)追従的な、順応性のある",
        "era": "13th Century Latin sub- + plicare",
        "etymology": {
            "components": ["sub- (under)", "plicare (to fold)"],
            "original_statement": "From Old French souple (soft, flexible), from Latin supplex (submissive, kneeling), from sub- (under) + plicare (to fold, bend)."
        },
        "concept": "Folding under (「硬い自我（rigid ego）」を 「謙虚（humility）」に 「折り畳む（fold）」ことで 「嵐（storm）」を 受け流し 生き残ること)",
        "thinking": "折れる ことも 屈する ことも なく、自在に 形を 変えることで どんな 外部からの 圧力も 自身の 成長の エナジーへと 変換してしまう、最強の 柔軟性. 語源は「下に 折り畳む、跪く（ひざまずく）」. それは 卑屈さ ではなく 自然の 巨大な 流れに 逆らわず 常に 最適な 状態で 在り続けようとする 聖なる「順応」のアクションです.",
        "aftertaste": "しなやかな強さ. 正しさを 振りかざして 誰かと 衝突しないで. あなたが「サプル（しなやかな）」な 心で 状況を 受け入れ 自分を 折り畳むとき あなたは 誰よりも 速く 真理の核心へと 辿り着くことが できるのだから.",
        "example": "He practiced yoga every day to keep his body supple and his mind open to new possibilities.",
        "deep_dive": { "roots": [{"term": "plek-", "meaning": "to plait, fold"}], "points": ["complex（複雑な）や simple（単純な：一回折った）と同じ。折り畳みのルーツ。"] },
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
        print(f"Success: Added {added} words in Cycle 163.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
