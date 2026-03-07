import json
import re

word_batch = [
    {
        "id": "balance_order",
        "word": "Balance",
        "meaning": "均衡、バランス、残高",
        "era": "13th Century Old French/Latin bilanx",
        "etymology": {
            "components": ["bi- (two)", "lanx (plate, scale)"],
            "original_statement": "From Old French balance, from Medieval Latin bilancia, from Latin bilanx (having two scales), from bi- (two) + lanx (dish, plate, scale of a balance)."
        },
        "concept": "Having two scales (二つの皿を持つ天秤)",
        "thinking": "もともとは、二つの「皿（lanx）」を吊るして重さを比べる天秤のこと。どちらにも偏らず、一つの軸の上に静かに静止している状態。それは、心、生活、あるいは宇宙のあらゆる力が、対立しながらも調和しているという、動的で美しい安定の形です。",
        "aftertaste": "重なり合う二つの皿。その水平な線の上に、真理が宿る。",
        "example": "Nature maintains a delicate balance between all living species.",
        "deep_dive": {
            "roots": [{"term": "bi-", "meaning": "two"}, {"term": "lek-", "meaning": "to bend, twist (possible)"}],
            "points": ["level（水平：天秤の錘）と同じく、公正さと平穏を象徴する言葉。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "order_order",
        "word": "Order",
        "meaning": "順序、秩序、命令、注文",
        "era": "13th Century Old French/Latin ordo",
        "etymology": {
            "components": ["ordiri (to begin to weave)"],
            "original_statement": "From Old French ordre, from Latin ordinem (row, rank, series, arrangement), originally 'a row of threads in a loom', related to ordiri (to begin to weave)."
        },
        "concept": "The first row of threads (織機の最初の糸の列)",
        "thinking": "もともとは織物を作る際に、最初に張られる「一列の糸（ordo）」のこと。そこから、物事がバラバラにならず、一定の法則に従って美しく並んでいる「秩序」を意味するようになりました。世界のカオスに一本の糸を通し、意味のある布へと織り上げていくための、最初の設計図です。",
        "aftertaste": "カオスの中に引かれた、最初の真っ直ぐな糸。それがすべての形を作る。",
        "example": "The chaotic library was finally put back into a logical order.",
        "deep_dive": {
            "roots": [{"term": "ar-", "meaning": "to fit together"}],
            "points": ["harmony（調和）や art（芸術）と同じ、ぴったりと合わせる情熱。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "sustain_order",
        "word": "Sustain",
        "meaning": "維持する、支える、耐える",
        "era": "13th Century Old French/Latin sustinere",
        "etymology": {
            "components": ["sub- (up from under)", "tenere (to hold)"],
            "original_statement": "From Old French sustenir, from Latin sustinere (hold up, upright, or aloft; keep up, support; endure), from sub- (up from under) + tenere (to hold)."
        },
        "concept": "To hold up from below (下からグッと持ち上げて支え続けること)",
        "thinking": "一時的に助けるのではなく、対象の下に回り込み（sub-）、その重みをしっかりと「掴んで（tenere）」離さず、ずっと支え続けること。それは生命の継続であり、責任の完遂です。あなたがそこにあり続けられるように、世界は見えない力であなたをサステインしています。",
        "aftertaste": "力強く、しかし静かに。崩れそうな何かを、下から支え抜く手のひら。",
        "example": "The small income from his farm was barely enough to sustain his family.",
        "deep_dive": {
            "roots": [{"term": "ten-", "meaning": "to stretch"}],
            "points": ["tendon（腱）や tension（緊張）と同じ。ピンと張り詰めて支える力。"]
        },
        "part_of_speech": "verb"
    },
    {
        "id": "structure_order",
        "word": "Structure",
        "meaning": "構造、建物、組織",
        "era": "15th Century Old French/Latin structura",
        "etymology": {
            "components": ["struere (to build, pile up)"],
            "original_statement": "From Old French structure, from Latin structura (a fitting together, adaptation, building), from structus, past participle of struere (to pile up, build, assemble)."
        },
        "concept": "A piling up of layers (層を積み重ねて作り上げること)",
        "thinking": "ただの塊ではなく、一つ一つの要素が意味を持って「積み上げられ（struere）」、全体として一つの機能をなしている状態。建物も、文章も、社会も。見えない骨組み（structure）があるからこそ、私たちは複雑な世界を理解可能な形として捉えることができます。",
        "aftertaste": "一つ一つのレンガが、意味を持って重なり、空へと至る形になる。",
        "example": "The internal structure of the company was completely reorganized last year.",
        "deep_dive": {
            "roots": [{"term": "stere-", "meaning": "to spread, extend"}],
            "points": ["street（通り：舗装され積み上げられた道）や strategy（戦略）と同族。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "rhythm_order",
        "word": "Rhythm",
        "meaning": "リズム、周期、律動",
        "era": "16th Century Middle French/Greek rhythmos",
        "etymology": {
            "components": ["rhein (to flow)"],
            "original_statement": "From Middle French rhythme, from Latin rhythmus, from Greek rhythmos (measured flow, movement), from rhein (to flow)."
        },
        "concept": "A measured flow (規則正しく区切られた流れ、大気の拍動)",
        "thinking": "心臓の鼓動も、季節の移ろいも、潮の満ち引きも。すべては流れる（rhein）水のように、一定の周期（measure）を持って繰り返されます。秩序化された時間こそがリズム。それは、カオスな連続体に「意味」という拍子を刻み込み、宇宙を音楽へと変える魔法のパルスです。",
        "aftertaste": "流れる。けれど、ただ流されるのではない。自らの鼓動で時を刻め。",
        "example": "Her life had a calm, steady rhythm that set everyone at ease.",
        "deep_dive": {
            "roots": [{"term": "sreu-", "meaning": "to flow"}],
            "points": ["stream（小川）や rhyme（韻）と同じファミリー。淀みのない連続。"]
        },
        "part_of_speech": "noun"
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
