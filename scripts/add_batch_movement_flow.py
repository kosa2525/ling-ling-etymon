import json
import re

word_batch = [
    # Cycle 102: Movement & Flow
    {
        "id": "momentum_movement",
        "word": "Momentum",
        "meaning": "勢い、弾み、運動量",
        "era": "17th Century Latin movere",
        "etymology": {
            "components": ["movere (to move)"],
            "original_statement": "From Latin momentum (movement, moving power, impulse), contraction of movimentum, from movere (to move)."
        },
        "concept": "Moving power (「動かす（move）」力そのもの、一度動き出したものが持つ「衝動（impulse）」)",
        "thinking": "静止していたものが動き出し、速度を得て、もはや自分自身の重みだけで進み続ける強大なエネルギー。語源は「瞬間（Moment）」とも重なります。一瞬の決断が大きな流れを作り、やがて誰にも止められない奔流（ほんりゅう）となる。変化の最初の一歩が、宇宙を震わせる力に変わる過程です。",
        "aftertaste": "止まらぬ奔流。あなたは今、追い風の中にいる。その勢いを信じて、どこまでも遠くへ、自分を解き放とう。",
        "example": "The movement for social reform gained momentum as more people joined the cause.",
        "deep_dive": { "roots": [{"term": "meue-", "meaning": "to push away"}], "points": ["mobile（移動可能な）や emotion（感情：外へ動かすもの）と同じ。生命は動き。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "velocity_movement",
        "word": "Velocity",
        "meaning": "速度、速さ、(一方向への)速力",
        "era": "16th Century Latin velox",
        "etymology": {
            "components": ["velox (swift, quick)"],
            "original_statement": "From Middle French velocite, from Latin velocitatem (swiftness, speed), from velox (swift, quick)."
        },
        "concept": "Swiftness in direction (単なる速さ（speed）ではなく、明確な「方角（direction）」を持って「速く（swift）」進むこと)",
        "thinking": "当てもなく彷徨（さまよ）うのではなく、目的地を見据えて一直線に突き進む、研ぎ澄まされた速さ。語源の velox は、ヴェールを引き裂くような鋭い動き。それは目標を貫く矢のような、迷いのない意志の速度です。無駄を削ぎ落としたとき、あなたの進む力は光になります。",
        "aftertaste": "光の矢。目的地さえ決まれば、あなたはもう、風の抵抗さえも自分の加速に変えることができる。",
        "example": "The project progressed with incredible velocity once the initial obstacles were removed.",
        "deep_dive": { "roots": [{"term": "weg-", "meaning": "to go, move, transport"}], "points": ["way（道）や vehicle（乗り物）と同じ。目的地への到達。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "flux_movement",
        "word": "Flux",
        "meaning": "流動、絶え間ない変化、流出",
        "era": "14th Century Latin fluere",
        "etymology": {
            "components": ["fluere (to flow)"],
            "original_statement": "From Old French flux, from Latin fluxus (a flowing, a fluid), from fluere (to flow)."
        },
        "concept": "A flowing (川の水が「流れる（flow）」ように、固定されず常に「移ろう（change）」こと)",
        "thinking": "世界は一瞬たりとも静止しておらず、すべての境界は溶け合い、常に新しい形へと再編され続けているという事実。語源は「流れる」。固定観念の氷を溶かし、液体のしなやかさで状況に適応していくこと。変化を「喪失」ではなく、常に新鮮な自分と出会うための「更新」として捉える思想です。",
        "aftertaste": "溶け合う世界. 固執を捨てたとき、あなたは世界という大きな流れと一体になり、自由という名の翼を得る。",
        "example": "The political situation in the region remains in a state of constant flux.",
        "deep_dive": { "roots": [{"term": "bhleu-", "meaning": "to swell, well up, flow"}], "points": ["fluid（液体）や influence（影響：流れ込むもの）と同じ。影響し合う万物。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "current_movement",
        "word": "Current",
        "meaning": "潮流、流れ、現在の、通用している",
        "era": "14th Century Latin currere",
        "etymology": {
            "components": ["currere (to run)"],
            "original_statement": "From Old French corant (running), from Latin currentem, from currere (to run, move quickly)."
        },
        "concept": "Running flow (水や時が「走る（run）」ように動き、今この瞬間を支配している「勢い」)",
        "thinking": "表面的な動きの下で、すべてをある方向へと運び去る力強い地下水流。語源は「走る」。現在（Current）とは、立ち止まるための点ではなく、未来へと疾走し続ける流れの一部です。時代という名の潮流を読み、それに乗ることは、世界のリズムとダンスを踊ることでもあります。",
        "aftertaste": "時代の鼓動。あなたは今、巨大な流れの中心で、自分というユニークな航跡を刻んでいる。",
        "example": "He found it difficult to swim against the strong current of public opinion.",
        "deep_dive": { "roots": [{"term": "kers-", "meaning": "to run"}], "points": ["course（進路）や courier（使者）と同じ。届けられるエネルギー。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "meander_movement",
        "word": "Meander",
        "meaning": "曲がりくねって進む、あてもなく彷徨う、蛇行",
        "era": "16th Century Greek Maiandros",
        "etymology": {
            "components": ["Maiandros (the name of a river in Phrygia noted for its winding course)"],
            "original_statement": "From Latin maeander, from Greek Maiandros, the name of a river in Phrygia noted for its winding course."
        },
        "concept": "The winding river (「曲がりくねった川（winding river）」のように、直線ではない「優雅な回り道」)",
        "thinking": "効率や最短距離だけを追い求めるのではなく、寄り道を楽しみ、地形に合わせてゆっくりと、しなやかに進むこと。語源はトルコの実在する蛇行河川。それは、目的地の達成よりも、その過程で出会う景色や予期せぬ発見を大切にする、大人の余裕と遊び心に満ちた歩みです。",
        "aftertaste": "優雅な寄り道。直線では見つけられなかった宝物が、あの曲がり角の向こうで、あなたを待っている。",
        "example": "We spent the afternoon meandering through the narrow streets of the old city.",
        "deep_dive": { "roots": [{"term": "Proper Name", "meaning": "River Maiandros"}], "points": ["固有名詞が一般名詞化した例。自然の形こそが、最も自由な形。"] },
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
        print(f"Success: Added {added} words in Cycle 102.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
