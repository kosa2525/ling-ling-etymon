import json
import re

word_batch = [
    # Cycle 81: Light & Radiance
    {
        "id": "luminescence_light",
        "word": "Luminescence",
        "meaning": "冷光、ルミネセンス、(熱を伴わない)発光",
        "era": "19th Century Latin lumen",
        "etymology": {
            "components": ["lumen (light)"],
            "original_statement": "From Latin lumen (light) + -escence (beginning to be, becoming)."
        },
        "concept": "Becoming light without heat (熱を持たず、ただ冷たく「光（light）」へと変容すること)",
        "thinking": "燃え上がる炎のような熱い光ではなく、深海や月光、あるいは蛍のように、静かに、しかし鮮やかにそこにある光。それは情熱という名の「熱」が引いたあとに、純粋な「存在の本質」だけが放ち始める、透明な輝きを指しています。静寂の中で、自らを光へと変えてゆく奇跡。",
        "aftertaste": "冷たい光。それは、燃え尽きることのない、魂の深淵から届く永遠の信号。",
        "example": "The ocean was filled with the otherworldly blue luminescence of plankton at night.",
        "deep_dive": { "roots": [{"term": "leuk-", "meaning": "light, brightness"}], "points": ["lucid（明快な）や lunar（月の）と同じ、澄み切った光のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "phosphorescence_light",
        "word": "Phosphorescence",
        "meaning": "青光り、燐光、(光を蓄えて)光ること",
        "era": "18th Century Greek phos + phoros",
        "etymology": {
            "components": ["phos (light)", "phoros (bearing, carrying)"],
            "original_statement": "From phosphorus, from Greek phosphoros (bringing light), from phos (light) + phoros (bringing)."
        },
        "concept": "Bearing light within (光を「運び（carry）」、内側に蓄えて、闇の中で放つこと)",
        "thinking": "外部からの光を一度自分の内側に取り込み、それが消えた後も、自らの力で思い出を反芻（はんすう）するように光り続けること。それは過去の喜びや愛を、今の暗闇を照らす「内なる灯火」へと変えた人の、静かなる意志の輝きです。",
        "aftertaste": "蓄えられた余韻。かつての光が、今のあなたを優しく包み込み、明日への道を指し示す。",
        "example": "The trails of phosphorescence left by the boat in the tropical water were magical.",
        "deep_dive": { "roots": [{"term": "bha-", "meaning": "to shine"}, {"term": "bher-", "meaning": "to carry"}], "points": ["flashlight や photograph（光で描くもの）と同じ、光の使者の末裔。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "effulgence_light",
        "word": "Effulgence",
        "meaning": "まばゆい輝き、光り輝くこと、光輝",
        "era": "17th Century Latin ex- + fulgere",
        "etymology": {
            "components": ["ex- (out, forth)", "fulgere (to shine, flash)"],
            "original_statement": "From Latin effulgentem, from effulgere (to shine forth), from ex- (out) + fulgere (to shine)."
        },
        "concept": "Shining out (内側から溢れ出し、周囲を圧倒するほどに「光り輝く（shine forth）」こと)",
        "thinking": "控えめな光ではなく、ダムが決壊したように一気に放出される、圧倒的で壮麗な輝き。語源の fulgere は「稲妻が光る（lightning flash）」ことを意味します。美しさや真理が、あまりの純度ゆえに隠しきれず、世界をその色彩で塗り替えてゆくような、暴力的なまでの肯定の光です。",
        "aftertaste": "溢れる祝福。その輝きを前にして、影はもはや存在することすら許されない。",
        "example": "The effulgence of the sunrise over the Himalayas left us absolutely breathless.",
        "deep_dive": { "roots": [{"term": "bhel-", "meaning": "to shine, flash, burn"}], "points": ["blaze（炎）や flame（火焔）と同じ、灼熱の閃光の系譜。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "refulgence_light",
        "word": "Refulgence",
        "meaning": "燦然とした輝き、光り輝く美しさ",
        "era": "16th Century Latin re- + fulgere",
        "etymology": {
            "components": ["re- (back, intense)", "fulgere (to shine, flash)"],
            "original_statement": "From Latin refulgentem, from refulgere (to flash back, shine brightly), from re- (back/again) + fulgere (to shine)."
        },
        "concept": "Flashing back (光が「跳ね返り（back）」、あるいは「再び」響き合うように輝くこと)",
        "thinking": "一方的な放射ではなく、世界そのものが光に応答し、鏡合わせのように燦然（さんぜん）と輝き合っている状態。豊かさ、高貴さ、そして神聖さ。語源の re- は「強調」も意味し、そこには繰り返される波のように絶え間なく押し寄せる、最高度の光の体験が凝縮されています。",
        "aftertaste": "光の共鳴。宇宙そのものが、あなたの存在を祝福して輝きを返してくる、その黄金の対話。",
        "example": "The cathedral was bathed in the refulgence of the multi-colored stained-glass windows.",
        "deep_dive": { "roots": [{"term": "bhel-", "meaning": "to shine, flash, burn"}], "points": ["effulgence とは、光が放たれる『向き』と『密度』の微細な違い。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "halo_light_2",
        "word": "Nimbus",
        "meaning": "後光、雨雲、(取り巻く)雰囲気",
        "era": "17th Century Latin nimbus",
        "etymology": {
            "components": ["nimbus (cloud, rainstorm, halo)"],
            "original_statement": "From Latin nimbus (cloud, rainstorm, bright cloud surrounding a god)."
        },
        "concept": "A bright cloud (神の周囲を包む、神聖で湿り気を帯びた「光の雲」)",
        "thinking": "単なる光の輪（halo）よりも密度が高く、まるで霧や雲のようにその人を「包み込んでいる」光。語源は「雨雲（rainstorm）」に由来し、そこには命を潤す慈雨のような、静かで、しかし重厚な威厳が漂います。偉大な人物や芸術作品が放つ、空間を規定するような無形のオーラを指します。",
        "aftertaste": "包容する気配。その人のそばにいるだけで、まるで聖なる雲のなかに守られているような静かな高揚感。",
        "example": "The saint was often depicted in old paintings with a golden nimbus around her head.",
        "deep_dive": { "roots": [{"term": "nebh-", "meaning": "cloud, vapor"}], "points": ["nebula（星雲）と同じ、形を持たないからこそ無限に広がる『気配』のルーツ。"] },
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
        print(f"Success: Added {added} words in Cycle 81.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
