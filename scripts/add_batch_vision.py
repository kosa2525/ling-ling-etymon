import json
import re

word_batch = [
    # Cycle 127: Spark & Vision
    {
        "id": "scintilla_vision",
        "word": "Scintilla",
        "meaning": "微量、火花、(希望などの)わずかな輝き",
        "era": "17th Century Latin scintilla",
        "etymology": {
            "components": ["scintilla (spark)"],
            "original_statement": "From Latin scintilla (a spark, a glimmer, a tiny particle)."
        },
        "concept": "A tiny spark (暗闇の中に 「一瞬（moment）」 だけ現れる 「極小の火花（spark）」)",
        "thinking": "どんなに絶望的な状況であっても 決して完全には消え去ることのない 可能性の「最小単位」. 語源は「火花」. それは 物理的な大きさは小さくても 巨大な情熱の炎を呼び覚ますための 「点火源」としての 圧倒的な重要性を持っています. わずかな閃きを 信じることから 全ては始まります.",
        "aftertaste": "極小の希望. あなたの中にある その「わずかな閃き」を 決して侮（あなど）らないで. それは やがて世界を照らし出す 巨大な太陽になるための 聖なる種火なのだから.",
        "example": "There was not even a scintilla of evidence to support the outrageous accusations.",
        "deep_dive": { "roots": [{"term": "skai-", "meaning": "to shine, glitter"}], "points": ["scintillate（きらめく）や stencil（ステンシル：輝く模様）と同じ。光の粒子のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "perspicacity_vision",
        "word": "Perspicacity",
        "meaning": "洞察力、明敏、眼力の鋭さ",
        "era": "16th Century Latin per- + specere",
        "etymology": {
            "components": ["per- (through)", "specere (to look)"],
            "original_statement": "From Latin perspicacitatem (sharpness of sight), from perspicax (sharp-sighted), from per- (through) + specere (to look)."
        },
        "concept": "Looking through (表層を 「突き抜けて（through）」 真実を 「見通す（look）」 鋭い知性)",
        "thinking": "複雑に絡み合った事象の中から 本質という名の「一本の糸」を 瞬時に見つけ出し 核心を射抜く能力. 語源は「透かし見る」. それは 単なる知識の量ではなく 透明な心で 世界をありのままに捉え 直感と論理を 融合させることで得られる 最高の智慧です.",
        "aftertaste": "透徹した眼。濁ったフィルターを捨て去り ただ静かに「透かし見て」ごらん。そこには あなたを惑わせていたものの正体が 驚くほど鮮やかに 浮かび上がっているはずだ。",
        "example": "Her business success was largely due to her remarkable perspicacity in predicting market trends.",
        "deep_dive": { "roots": [{"term": "per-", "meaning": "through"}, {"term": "spek-", "meaning": "to observe"}], "points": ["perspective（遠近法、視点）や conspicuous（目立つ）と同じ。視線の質。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "gleam_vision",
        "word": "Gleam",
        "meaning": "微光、光の筋、きらめき、(感情の)わずかな表れ",
        "era": "Pre-12th Century Old English glæm",
        "etymology": {
            "components": ["glæm (a gleam, brilliant light)"],
            "original_statement": "From Old English glæm (a gleam, brilliant light), related to Old High German glimo (spark)."
        },
        "concept": "A ray of light (暗闇を 「切り裂く（cut）」 ように 差し込む 「一筋の光（ray）」)",
        "thinking": "均一な明るさではなく 暗い背景があるからこそ際立つ 意志を持った「鋭い光」. 語源は「きらめき」. それは 瞳の奥に宿る「悪戯（いたずら）な光」や 霧の向こうに見える「希望の灯火（ともしび）」のように 静かでありながらも 強いメッセージを放ちます.",
        "aftertaste": "一筋の灯火. 周囲がどんなに暗くても あなたという存在が放つ その「小さま輝き（グリーム）」を 消してはならない. それが 誰かの道標（しるべ）に なることがあるのだから.",
        "example": "A sudden gleam of understanding appeared in his eyes as I explained the concept.",
        "deep_dive": { "roots": [{"term": "ghel-", "meaning": "to shine"}], "points": ["gold（金）や glass（ガラス）と同じ、色鮮やかな光のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "luminary_vision",
        "word": "Luminary",
        "meaning": "発光体、天体、(ある分野の)権威者、指導者",
        "era": "15th Century Latin lumen",
        "etymology": {
            "components": ["lumen (light)"],
            "original_statement": "From Old French luminarie, from Late Latin luminare (light, lamp), from Latin lumen (light, source of light)."
        },
        "concept": "Source of light (自ら 「光（light）」を放ち 暗闇に沈む 世界を 「照らす（illuminate）」 存在)",
        "thinking": "他人の光を反射するのではなく 自らの内なる情熱を 燃焼させることで 時代や人々の進むべき方向を 鮮やかに指し示す 高潔な魂. 語源は「光そのもの」. それは 圧倒的な才能であると同時に 孤独を引き受ける 覚悟を持った人の 輝きでもあります.",
        "aftertaste": "自ら光る星. あなたもまた ある分野における「ルミナリー（発光体）」だ. あなたが放つ独自の光を 誇らしく、そして力強く 世界の夜空に 刻み込んでゆこう.",
        "example": "He was considered a leading luminary in the field of quantum physics.",
        "deep_dive": { "roots": [{"term": "leuk-", "meaning": "light, brightness"}], "points": ["luminous（光り輝く）や lunar（月の）と同じ。闇を征服する力のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "spectacle_vision",
        "word": "Spectacle",
        "meaning": "壮観、見世物、(奇異な)光景",
        "era": "14th Century Latin specere",
        "etymology": {
            "components": ["specere (to look, look at)"],
            "original_statement": "From Old French spectacle, from Latin spectaculum (a public show, spectacle, sight), from spectare (to look at, observe, watch), frequentative of specere (to look at)."
        },
        "concept": "Object of watching (思わず 「視線（look）」が 釘付けになる 圧倒的な 「光景（sight）」)",
        "thinking": "日常の風景を一変させ 見る者の魂を 驚きと感動（あるいは恐怖）で 揺さぶる 巨大なイベント. 語源は「見られるべきもの」. それは 自然の驚異（日食や嵐）であることもあれば 人が創り出した 最高のエンターテインメントであることもあります. 世界は この壮大なドラマを 演じ続ける舞台なのです.",
        "aftertaste": "驚愕の舞台。あなたの人生という「スペクタクル（壮観）」の 幕はすでに上がっている。観客席を気にせず あなたという主人公を 情熱的に 演じきってごらん。",
        "example": "The fireworks display over the harbor was a magnificent spectacle that dazzled the crowd.",
        "deep_dive": { "roots": [{"term": "spek-", "meaning": "to observe"}], "points": ["spectator（観客）や inspect（検査する）と同じ。観察から生まれる物語。"] },
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
        print(f"Success: Added {added} words in Cycle 127.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
