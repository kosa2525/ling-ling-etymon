import json
import re

word_batch = [
    {
        "id": "molecule_micro",
        "word": "Molecule",
        "meaning": "分子、微粒子",
        "era": "18th Century French/Latin moles",
        "etymology": {
            "components": ["moles (mass, barrier)", "-cule (little)"],
            "original_statement": "From French molécule, from New Latin molecula, diminutive of Latin moles (mass, block, barrier, heap)."
        },
        "concept": "A tiny mass (極小の塊、生命の最小限の質量)",
        "thinking": "本来は巨大な「塊（mass/moles）」を意味する言葉に、小さなものを表す（-cule）がついた言葉。目に見えないほど小さいけれど、そこには確かに「質量」があり、世界を構成する確かな手応えがある。最小の断片が集まって、巨大な宇宙（現実）を作るという事実の驚異。",
        "aftertaste": "小さきもの。それが集まって、この世界のすべての手触りを生み出す。",
        "example": "Water is composed of oxygen and hydrogen molecules.",
        "deep_dive": {
            "roots": [{"term": "me-", "meaning": "to measure (possible)"}],
            "points": ["mole（ほくろ/塊）や demolish（破壊する：崩す）と同じ『重い塊』の系譜。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "organism_micro",
        "word": "Organism",
        "meaning": "有機体、生物、組織体",
        "era": "18th Century French/Greek organon",
        "etymology": {
            "components": ["organon (instrument, implement, tool)"],
            "original_statement": "From French organisme, from New Latin organismus, from organum (organ, instrument), from Greek organon (implement, tool)."
        },
        "concept": "A collection of instruments (各パーツが「道具」として機能する、動的な集合体)",
        "thinking": "ただの物体ではなく、それぞれが目的を持った「道具（organon）」として繋がり、相互に助け合いながら全体として生きているもの。それは、個別の音が合わさって奏でられる一つのシンフォニー。生命は、自ら自身を使いこなし、意味を生み出し続ける壮大な楽器です。",
        "aftertaste": "完璧な調律。たった一つの細胞さえも、この世界と共鳴する楽器の一部。",
        "example": "Lichens are complex organisms composed of algae and fungi coexisting.",
        "deep_dive": {
            "roots": [{"term": "werg-", "meaning": "to work, do"}],
            "points": ["work（仕事）や energy（エネルギー：中の働き）と同じ『活動』の源泉。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "nucleus_micro",
        "word": "Nucleus",
        "meaning": "核、中心、(細胞の)核、(原子)核",
        "era": "18th Century Latin nux",
        "etymology": {
            "components": ["nux (nut)", "-uleus (diminutive/result)"],
            "original_statement": "From Latin nucleus (kernel, inner part of a nut), diminutive of nux (nut)."
        },
        "concept": "The kernel of a nut (木の実（ナッツ）の「一番大切な中身」)",
        "thinking": "硬い殻に守られた、一番柔らかく、かつ生命が凝縮された「実（kernel）」のこと。そこから、あらゆる物事の決定権を握る「中心部」や「核」を意味するようになりました。小さく、しかしすべてを制御し、未来の設計図（DNAなど）を抱きしめている神聖な中枢。",
        "aftertaste": "一番奥深くに、一番小さな種がある。それがすべてを動かしてゆく。",
        "example": "Inside the nucleus of each cell, the hereditary information is stored.",
        "deep_dive": {
            "roots": [{"term": "knew-", "meaning": "nut"}],
            "points": ["nut（ナッツ）そのもののルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "enzyme_micro",
        "word": "Enzyme",
        "meaning": "酵素",
        "era": "19th Century Greek en + zyme",
        "etymology": {
            "components": ["en- (in)", "zyme (leaven, sourdough)"],
            "original_statement": "From Greek enzymos (leavened), from en- (in) + zyme (leavened bread, sourdough, fermentation)."
        },
        "concept": "In the leaven (（パンを膨らませる）酵母の中に宿る力)",
        "thinking": "パンを発酵させ、内側から膨らませる不思議な力。生命活動の中で、それ自体は変化せず、しかし他者を劇的に変容させ、反応を加速させる「触媒（catalyst）」。それは、ただ存在しているだけで世界を温め、変化の連鎖を巻き起こす、密かな魔法のエッセンスです。",
        "aftertaste": "そこにあるだけで、止まっていた何かが、ふつふつと動き出す。",
        "example": "Digestive enzymes break down complex food into smaller components.",
        "deep_dive": {
            "roots": [{"term": "yes-", "meaning": "to boil, foam, bubble"}],
            "points": ["yeast（イースト/酵母）や jealousy（嫉妬：心が沸騰すること）と同じ沸き立つルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "dormant_micro",
        "word": "Dormant",
        "meaning": "休眠中の、活動休止の、静止した",
        "era": "14th Century Old French/Latin dormire",
        "etymology": {
            "components": ["dormire (to sleep)"],
            "original_statement": "From Old French dormant, present participle of dormir (to sleep), from Latin dormire (to sleep)."
        },
        "concept": "Lying in sleep (深く、静かに「眠っている」状態)",
        "thinking": "死んでいるのではなく、ただ「眠っている（sleeping）」だけ。冬を越す種子や、噴火を待つ火山のように、内側には強大なエネルギーを秘めたまま、来るべき瞬間のために活動を最小限に抑えている状態。蓄えられた静寂こそが、いつか訪れる劇的な覚醒を準備しています。",
        "aftertaste": "静かなる呼吸。今はただ、目覚めるべき季節まで夢を見ている。",
        "example": "The seeds can lie dormant for many years before finally sprouting.",
        "deep_dive": {
            "roots": [{"term": "drem-", "meaning": "to sleep"}],
            "points": ["dormitory（寮：寝る場所）と同じ。"]
        },
        "part_of_speech": "adjective"
    }
]

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
    if match:
        prefix = match.group(1)
        json_array_str = match.group(2)
        suffix = match.group(3)
        
        words = json.loads(json_array_str)
        existing_ids = {w.get("id") for w in words}
        
        added_count = 0
        for item in word_batch:
            if item["id"] not in existing_ids:
                words.append(item)
                added_count += 1
                
        new_json_str = json.dumps(words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Success: Added {added_count} words.")
    else:
        print("Error: Could not find WORDS array in data.js.")
except Exception as e:
    print(f"Error: {e}")
