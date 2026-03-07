import json
import re

word_batch = [
    # Cycle 125: Pattern & Symmetry
    {
        "id": "mosaic_pattern",
        "word": "Mosaic",
        "meaning": "モザイク、寄せ集め、(異なる要素の)組み合わせ",
        "era": "15th Century Greek Mousa",
        "etymology": {
            "components": ["Mousa (Muse)"],
            "original_statement": "From Old French mosaique, from Italian mosaico, from Medieval Latin musaicum (work of the Muses), from Greek mouseios (belonging to the Muses)."
        },
        "concept": "Work of the Muses (「女神（Muse）」に 捧げられた 小さな破片を 「繋ぎ合わせた（fitting razem）」 神聖な芸術)",
        "thinking": "バラバラな破片（経験や感情）を 絶妙なバランスで 配置し直すことで 遠くから見れば 壮大な物語（絵）を 描き出す手法. 語源は「ミューズ（芸術の女神）の仕事」. あなたの人生の 欠けた部分や 痛みの記憶も また全体という モザイク（模様）の中では 欠かすことのできない 輝く一辺になのです.",
        "aftertaste": "断片の聖遺物. 完璧である必要はない. その不揃いな破片たちを 愛を持って繋ぎ合わせれば あなたという名の 唯一無二の芸術が 世界に浮かび上がるのだから.",
        "example": "The history of the region is a rich mosaic of different cultures and traditions.",
        "deep_dive": { "roots": [{"term": "men-", "meaning": "to think (source of Muse)"}], "points": ["music（音楽：ミューズの術）や museum（博物館：ミューズの家）と同じ。創造性の源泉。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "mandala_pattern",
        "word": "Mandala",
        "meaning": "マンダラ、宇宙図、聖域の象徴",
        "era": "19th Century Sanskrit mandala",
        "etymology": {
            "components": ["manda (essence)", "-la (container)"],
            "original_statement": "From Sanskrit mandala (circle, orb), literally 'essence-container' (manda 'essence' + -la 'container')."
        },
        "concept": "Essence container (本質を 「円環（circle）」の中に 「封じ込めた（container）」 宇宙の縮図)",
        "thinking": "中心（自己）から放射状に広がりながらも 常に一貫した秩序を保ち 万物の調和を表現する 幾何学的な祈りの形. 語源は「本質の器」. それは 混沌とした日常の中に 聖なる中心軸を 打ち立てることの大切さを教えてくれます. あなたの心の中に 揺るぎない円（調和）を 描いてみましょう.",
        "aftertaste": "中心の静寂. 外側の嵐に惑わされないで. あなたの心の奥底には 常に完璧な秩序を保った「マンダラ（聖域）」が広がっている. そこに戻れば いつでも本当の自分に会える.",
        "example": "The artist spent weeks meticulously painting a complex mandala as a form of meditation.",
        "deep_dive": { "roots": [{"term": "med-", "meaning": "to measure, take appropriate steps (possible related)"}], "points": ["circle（円）としての曼荼羅。自分という宇宙を、幾何学で読み解く知恵。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "fractal_pattern",
        "word": "Fractal",
        "meaning": "フラクタル、自己相似形、断片的な",
        "era": "20th Century Latin fractus",
        "etymology": {
            "components": ["fractus (broken)"],
            "original_statement": "Coined by Benoit Mandelbrot in 1975, from Latin fractus (broken, fragmented)."
        },
        "concept": "Self-similarity in fragments (「破片（fragment）」の中に 「全体の構造（whole structure）」が 繰り返し現れる 宇宙の再帰性)",
        "thinking": "部分を見れば全体が見え 全体を見れば部分が宿る 一つにして多、多にして一という 宇宙の奥深いデザイン原理. 語源は「砕かれた」. あなたの今日一日の 些細な振る舞いや 思いつきも また人生という 巨大なフラクタル（相似形）の 一片として 全てを象徴しているのです.",
        "aftertaste": "微小な巨視. 目の前の一歩を 疎（おろそ）かにしないで. その小さな断片の中に あなたの宇宙の 全ての法則が 密やかに 完璧に 刻み込まれているのだから.",
        "example": "Clouds, coastlines, and cauliflower are all natural examples of fractal patterns.",
        "deep_dive": { "roots": [{"term": "bhreg-", "meaning": "to break"}], "points": ["fraction（分数：分割されたもの）や fragile（脆い：砕けやすい）と同じ、分割の知性。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "labyrinth_pattern",
        "word": "Labyrinth",
        "meaning": "迷宮、迷路、複雑に絡み合ったもの",
        "era": "14th Century Greek labyrinthos",
        "etymology": {
            "components": ["labrys (double-edged axe)"],
            "original_statement": "From Latin labyrinthus, from Greek labyrinthos (maze), possibly related to labrys (double-edged axe, symbol of royal power)."
        },
        "concept": "Structure of the axe (「王権（royal power）」の 象徴である 「両刃の斧（axe）」が 守る 複雑怪奇な 道筋)",
        "thinking": "行き止まりの多い「迷路（Maze）」とは違い たった一本の道が 執拗にねじれ、折れ曲がりながら 中心へと至る 瞑想的な巡礼の道. 語源は「斧の館」. 迷うことは 遠回りではなく 自己の深部へと至るために 必要な通過儀礼（イニシエーション）です. 焦らず 迷いを楽しむ勇気を.",
        "aftertaste": "ねじ曲がった直線. 迷っているように見えても あなたは確かに「中心」へと導かれている. 足元の道がどこへ続いていても その「迷宮（ラビリンス）」の 終わりには 輝く真実が待っている.",
        "example": "He found himself lost in a labyrinth of conflicting emotions after the unexpected news.",
        "deep_dive": { "roots": [{"term": "pre-Greek root", "meaning": "unknown"}], "points": ["maze（迷路）との違い。ラビリンスは「辿り着くための道」であり、迷わせるためだけのものではない。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "tapestry_pattern",
        "word": "Tapestry",
        "meaning": "タペストリー、綴れ織、(歴史などの)複雑な織り成し",
        "era": "15th Century Greek tapes",
        "etymology": {
            "components": ["tapes (carpet, rug)"],
            "original_statement": "From Old French tapisserie, from tapis (carpet), from Late Latin tapetum, from Greek tapes (carpet, rug)."
        },
        "concept": "Woven story (「糸（thread）」を 複雑に 「織り合わせる（weave）」 ことで 壮大な 「歴史（story）」を 描き出すこと)",
        "thinking": "背後にある 無数の縦糸と横糸（人々や出来事）が 複雑に絡み合い 一枚の 圧倒的な物語（風景）を 完成させている状態. 語源は「カーペット」. 表から見れば美しい模様も 裏返せば 無数の結び目と 絡まりに溢れています. その「絡まり」こそが 強さと美しさの源です.",
        "aftertaste": "絆の綴れ織. あなたの人生というタペストリーに どのような色の糸を 加えようか. 喜びも悲しみも 全てを鮮やかに織り込んで 世界にたった一つの 絶景を完成させよう.",
        "example": "The novel vividly portrays the complex tapestry of life in a small Victorian village.",
        "deep_dive": { "roots": [{"term": "pre-Indo-European", "meaning": "unknown"}], "points": ["textile（織物）よりも「図像（ストーリー）」に重点を置いた表現。記憶の織物。"] },
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
        print(f"Success: Added {added} words in Cycle 125.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
