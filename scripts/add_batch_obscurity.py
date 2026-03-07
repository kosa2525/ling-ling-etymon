import json
import re

word_batch = [
    # Cycle 145: Shadow & Depth (Refined)
    {
        "id": "obscurity_shadow",
        "word": "Obscurity",
        "meaning": "無名、忘却、曖昧(あいまい)さ、暗がり",
        "era": "14th Century Latin obscurus",
        "etymology": {
            "components": ["obscurus (dark, dusky, shady)"],
            "original_statement": "From Old French oscurité, from Latin obscuritatem (darkness, obscurity), from obscurus (dark, dusky, shady, covered over)."
        },
        "concept": "Covered over (「光（light）」からは 「隠され（covered）」 誰にも 「見つからない（unseen）」 聖なる 沈黙の領域)",
        "thinking": "世間の評価や 視線から 解き放たれ、ただ自らの魂とだけ向き合う、静かで豊かな「無名」の状態. 語源は「覆い隠された」. それは 敗北ではなく 自分の真実を 守り抜き、じっくりと 育てるための 慈悲深い 暗闇（マテリアル）でもあります. 影の中に、本質は潜みます.",
        "aftertaste": "無名の自由. 目立つことだけが 価値ではない. あなたが「オブスリティ（無名）」の 静寂の中で 磨き上げたその光こそが 誰にも奪えない 本物の 輝きになるのだから.",
        "example": "He spent most of his life in obscurity, only to be recognized as a genius long after his death.",
        "deep_dive": { "roots": [{"term": "skeu-", "meaning": "to cover, conceal"}], "points": ["sky（空：雲が覆うもの）や hide（隠す）と同じ。保護と深淵のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "silhouette_shadow",
        "word": "Silhouette",
        "meaning": "シルエット、影絵、輪郭、(不況時の)倹約",
        "era": "18th Century Etienne de Silhouette",
        "etymology": {
            "components": ["Etienne de Silhouette (French finance minister)"],
            "original_statement": "Named after Étienne de Silhouette (1709–1767), French controller-general of finances, possibly as a joke on his short tenure or his cheapness (shadow portraits being the cheapest portrait option)."
        },
        "concept": "Detailed shadow (「詳細（detail）」を 削ぎ落とし 「本質的な形（essence）」だけを 浮かび上がらせる 潔い 表現)",
        "thinking": "色の鮮やかさや 表面の飾りに 惑わされず、その存在が持つ 根源的な「構え（スタンス）」を 一瞬で捉えること. 語源は「人の名前（倹約家）」. それは 最小限の要素で 最大限の意味を 伝えるという 究極の「引き算の美学」の 象徴です. 影は、嘘をつきません.",
        "aftertaste": "本質の輪郭. 飾り立てることを やめてごらん. あなたが「シルエット（輪郭）」だけになったとき そこに立ち現れる 揺るぎない 意志こそが あなたという 存在の 正体（コア）なのだから.",
        "example": "The profile of the ancient castle was visible as a dark silhouette against the fiery sunset.",
        "deep_dive": { "roots": [{"term": "namesake", "meaning": "history of language"}], "points": ["皮肉（安上がり）から生まれた言葉が、今や「洗練」の象徴へ。意味の変容のドラマ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "penumbra_shadow",
        "word": "Penumbra",
        "meaning": "半影、薄暗がり、(権利などの)周辺領域",
        "era": "17th Century Latin paene + umbra",
        "etymology": {
            "components": ["paene (almost)", "umbra (shadow)"],
            "original_statement": "Coined by Kepler in 1604 from Latin paene (almost) + umbra (shadow)."
        },
        "concept": "Almost shadow (「光（light）」と 「影（shadow）」が 幽かに 「溶け合う（mingle）」 境界の ニュアンス)",
        "thinking": "白黒（善悪）のはっきりした決断を拒み、矛盾や多義性をそのまま抱擁する、豊かで曖昧な領域. 語源は「ほとんど影」. それは 答えの出ない問いに 耐え、その宙づりの 状態から 新しい 意味を 紡ぎ出そうとする 哲学的な「余白（マージン）」です. 境界に、真理は宿ります.",
        "aftertaste": "グラデーションの叡智. どちらか一方に 決めつけなくていい. あなたが「ペナンブラ（半影）」の 曖昧さを 愛せるとき 世界はもっと 奥行きのある 優しさに 満ちた場所に 変わってゆくのだから.",
        "example": "The astronomer carefully mapped the penumbra of the moon during the partial solar eclipse.",
        "deep_dive": { "roots": [{"term": "and-", "meaning": "none"}], "points": ["umbrella（傘：小さな影）と同じ。守られ、溶け合う場所。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "subterranean_depth",
        "word": "Subterranean",
        "meaning": "地下の、潜行的な、隠れた、秘密の",
        "era": "17th Century Latin sub- + terra",
        "etymology": {
            "components": ["sub- (under)", "terra (earth)"],
            "original_statement": "From Latin subterraneus (underground), from sub- (under) + terra (earth, land, ground)."
        },
        "concept": "Under the earth (「日常の地表（surface）」の 下で 「静かに（silently）」 進行している 巨大な 潮流)",
        "thinking": "目に見える華やかさの背後で、文明や 命を 支えている 根源的な 仕組み（根っこ）. 語源は「土の下」. それは 隠蔽（ネガティブ）ではなく 表に出ることを 求めず 黙々と 本質的な役割を 果たし続ける 聖なる「伏流（アンダーグラウンド）」のアクションです.",
        "aftertaste": "伏流の誇り. 表舞台で 拍手をもらわなくてもいい. あなたが「サブタレイニアン（地下）」で 必死に 張り巡らせた 努力の根っこが 世界を 支えているという 事実を 誇りに思っていいのだから.",
        "example": "An ancient subterranean river was found flowing beneath the modern city's foundations.",
        "deep_dive": { "roots": [{"term": "ters-", "meaning": "dry (possible for terra)"}], "points": ["territory（領土）や terrace（テラス）と同じ。存在の「足がかり」を 掘り下げる力。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "unfathomable_depth",
        "word": "Unfathomable",
        "meaning": "測り知れない、不可解な、底知れぬ",
        "era": "17th Century un- + fathom",
        "etymology": {
            "components": ["un- (not)", "fathom (reach with arms)"],
            "original_statement": "From un- (not) + fathomable, from fathom (embrace, measure with outstretched arms)."
        },
        "concept": "Cannot be embraced (「人間の知性（human logos）」の 尺度を 完全に 「超え（beyond）」 永遠に 届かない 深淵)",
        "thinking": "理解しよう、制御しようという傲慢な試みを、その「底なしの静寂」によって優しく拒絶する、圧倒的な他者（宇宙）. 語源は「抱きしめることができない」. それは 絶望ではなく 私たちが 謙虚に 敬意を払うべき 神秘の 最終防衛ラインとしての 聖性を 持っています.",
        "aftertaste": "神秘への降伏. 全てを 解き明かそうとしなくていい. 「アンファゾマブル（不可解）」という名の 壮大なパズルを そのまま 慈しむことで あなたの人生は 誰にも 汚されない 輝きを 放つのだから.",
        "example": "He stared into the dark, starless sky, overwhelmed by the unfathomable scale of the universe.",
        "deep_dive": { "roots": [{"term": "pet-", "meaning": "to spread"}], "points": ["paten（聖皿）や expand（広がる）と同じ。自分の器を広げても、なお届かない「外」の驚異。"] },
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
        print(f"Success: Added {added} words in Cycle 145.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
