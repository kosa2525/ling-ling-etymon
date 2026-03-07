import json
import re

word_batch = [
    # Cycle 118: Silk & Softness
    {
        "id": "texture_softness",
        "word": "Texture",
        "meaning": "感触、質感、織り方、構造",
        "era": "15th Century Latin texere",
        "etymology": {
            "components": ["texere (to weave)"],
            "original_statement": "From Latin textura (a web, texture, structure), from texere (to weave)."
        },
        "concept": "Woven structure (糸を「織り合わせる（weave）」ことで生まれる 独特の「手触り（feel）」)",
        "thinking": "表面的な見た目だけでなく 指先や心で触れたときに感じる その存在に固有の「粗さ」や「滑らかさ」. 語源は「織ること」. どんなに複雑に見える現実も 一本一本の糸（出来事）が織り成す テクスチャの積み重ねです. あなたのこれまでの経験も またあなたの人生という織物の 豊かな質感を作り出しています.",
        "aftertaste": "魂の手触り. あなたの言葉には あなたにしか出せない質感がある. その滑らかさや、時として心地よい粗さを 恐れずに世界に差し出してみよう.",
        "example": "The smoothness of the silk was a stark contrast to the rough texture of the wool.",
        "deep_dive": { "roots": [{"term": "teks-", "meaning": "to weave, fabricate"}], "points": ["text（文章：織られた言葉）や technical（技術的な：織る技術）と同じ、構築のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "fabric_softness",
        "word": "Fabric",
        "meaning": "織物、布、構造、枠組み",
        "era": "15th Century Latin faber",
        "etymology": {
            "components": ["faber (craftsman)"],
            "original_statement": "From Middle French fabrique, from Latin fabrica (workshop; art, trade; product of skilled labor, structure, fabric), from faber (worker in hard materials, craftsman)."
        },
        "concept": "Product of craft (「職人（craftsman）」が 生み出した 「精巧な構造（structure）」)",
        "thinking": "個々の糸を統合し 一つの「面」として機能させたもの. 語源は「職人の仕事」. 社会の「ファブリック（枠組み）」という言葉があるように それは単なる布を超えて 私たちを包み込み 支えてくれる目に見えない構造でもあります. 信頼という糸が密に編まれるほど その構造は強く 柔軟になります.",
        "aftertaste": "絆の織物. 私たちは皆 世界という巨大なファブリックを構成する 一本の糸だ. あなたの隣の糸と どのように重なり どのような模様を創るか. それが人生という芸術だ.",
        "example": "The social fabric of the small town was tightly knit and supportive of everyone.",
        "deep_dive": { "roots": [{"term": "dhabh-", "meaning": "to fit together"}], "points": ["forge（鍛造する）や fashion（流行：形作ること）と同じ、創造性のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "subtle_softness",
        "word": "Subtle",
        "meaning": "微妙な、繊細な、捉えがたい、巧妙な",
        "era": "14th Century Latin sub- + tela",
        "etymology": {
            "components": ["sub- (under)", "tela (web, warp, loom)"],
            "original_statement": "From Old French sotil, from Latin subtilis (fine, thin, precise, subtle), from sub- (under) + tela (web, net, warp of a fabric)."
        },
        "concept": "Under the web (織物の「網目（web）」を 「潜り抜ける（under）」ほど 細かく捉えがたいこと)",
        "thinking": "声高に叫ぶのではなく わずかなニュアンスや 呼吸の間に宿る「微細な」美しさ. 語源は「織り糸の下を通る」. それは 注意深く観察しなければ見落としてしまうほど 繊細な真実です. 粗野な力ではなく この「サブトル（微妙）」な感性こそが 人を深く癒やし 世界を静かに変えていきます.",
        "aftertaste": "繊細な囁き. 真実はいつも 騒がしい場所ではなく あなたの心の網目を潜り抜けるような 静かで微細な感覚の中に 密やかに宿っているのだから.",
        "example": "There was a subtle change in his tone of voice that suggested he was nervous.",
        "deep_dive": { "roots": [{"term": "upo-", "meaning": "under"}, {"term": "teks-", "meaning": "to weave"}], "points": ["textile（テキスタイル）の否定的な洗練。見えない糸を読み解く力。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "finery_softness",
        "word": "Finery",
        "meaning": "華麗な装飾、美しい衣服",
        "era": "17th Century French fin",
        "etymology": {
            "components": ["fin (fine, pure, delicate)"],
            "original_statement": "From fine (adjective) + -ery. Fine from Latin finis (end, limit; peak, summit)."
        },
        "concept": "Refined state (不純物を削ぎ落とし 「極致（limit）」まで 「洗練された（fine）」 最高の装い)",
        "thinking": "特別な日のための 最も美しく 誇らしい自分を表現するための「装い」. 語源は「終わり」や「極致」. それは単なる贅沢ではなく 自分の魂の輝きを 外面的な美しさへと昇華（しょうか）させた結果です. 丁寧に織り上げられた衣服は 着る人の心もまた 凛（りん）と整えてくれます.",
        "aftertaste": "誇りのドレス. あなたが自分を慈しみ 美しく装うとき 世界もまた あなたを祝福の対象として眺める. あなたの輝きを 最高の形（ファイナリー）で 表現しよう.",
        "example": "The guests arrived for the wedding dressed in all their Sunday finery.",
        "deep_dive": { "roots": [{"term": "dhei-", "meaning": "to shine, look (possible related to fine)"}], "points": ["finish（終える）や finite（限定された）と同じ。完成された美のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "gossamer_softness",
        "word": "Gossamer",
        "meaning": "極めて薄い(布)、クモの糸、儚いもの",
        "era": "14th Century goose + summer",
        "etymology": {
            "components": ["goose (bird)", "summer (seasons)"],
            "original_statement": "From goose (noun) + summer (noun). Apparently literally 'goose summer', from the time of year (St. Martin's summer) when geese are in season and cobwebs are frequent."
        },
        "concept": "Summer of geese (「ガチョウ（goose）」が旬の 「小春日和（summer）」に 宙を舞うクモの糸のような 頼りなき美)",
        "thinking": "触れれば破れてしまいそうなほど 薄く、白く、どこまでも「儚（はかな）い」質感. 語源は「ガチョウの夏（小春日和）」. 穏やかな午後の陽光の中で 風に乗って漂うクモの糸。それは、現実にしっかりと根ざしているというよりは 夢と現実の境界を漂う 霊的な美しさを象徴しています.",
        "aftertaste": "陽光の中の糸. 儚いことは 弱いことではない. その繊細な光を掴もうとせず ただその揺らぎを愛でることで あなたの心は 限りなく透明に近づいていく.",
        "example": "The morning dew sparkled on the gossamer threads of the spider's web.",
        "deep_dive": { "roots": [{"term": "ghans-", "meaning": "goose"}, {"term": "sem-", "meaning": "summer"}], "points": ["季節と自然現象の詩的な融合。言葉が持つ質感の極致。"] },
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
        print(f"Success: Added {added} words in Cycle 118.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
