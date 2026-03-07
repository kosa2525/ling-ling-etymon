import json
import re

word_batch = [
    # Cycle 107: Radiance & Aura
    {
        "id": "halo_radiance",
        "word": "Halo",
        "meaning": "後光、輪、ハロー、(太陽や月の)かさ",
        "era": "16th Century Greek halos",
        "etymology": {
            "components": ["halos (threshing floor, disk)"],
            "original_statement": "From Latin halos, from Greek halos (threshing floor; disk of the sun or moon; halo); originally a circular threshing floor."
        },
        "concept": "The circular floor (穀物を脱穀するための「円形の床（disk）」のように、中心から放射状に広がる光の「輪」)",
        "thinking": "聖人や選ばれし者の頭上に現れる、内なる神性の象徴. 語源は「脱穀場」。それは、生命を育む糧を収穫し、大切に守るための場所でした。光の輪とは、あなたが大切に育ててきた徳や智慧が、もはや隠しきれずに外側へと溢れ出し、周囲を聖なる静寂で包み込んでいる状態です。",
        "aftertaste": "静かなる結界。あなたがただそこにいるだけで、世界の一部が浄化され、新しい光で満たされてゆく。",
        "example": "The moon was surrounded by a beautiful halo in the misty night sky.",
        "deep_dive": { "roots": [{"term": "ghel-", "meaning": "to shine"}], "points": ["glow（輝く）や gold（黄金）と同じ、内なる光のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "aura_radiance",
        "word": "Aura",
        "meaning": "雰囲気、オーラ、微風、香気",
        "era": "14th Century Greek aura",
        "etymology": {
            "components": ["aura (breeze, breath)"],
            "original_statement": "From Latin aura (a breeze, a breath, air), from Greek aura (breeze, breath, air in motion)."
        },
        "concept": "A gentle breeze (人の周囲を漂う「そよ風（breeze）」のような、目に見えない「気配」あるいは「香り」)",
        "thinking": "言葉や行動よりも先に、その人の存在そのものが発している、独特の質感や色合い. 語源は「そよ風」。それは掴もうとすれば消えてしまいますが、確かにそこにある生命の「呼吸」です。あなたが纏（まと）っている雰囲気は、あなたの魂が宇宙と交わしている、秘密の会話の残響なのです。",
        "aftertaste": "存在の呼吸。あなたは、自分でも気づかないうちに、出会うすべての人に自分という名の風を届けている。",
        "example": "She had an aura of confidence that made everyone feel at ease in her presence.",
        "deep_dive": { "roots": [{"term": "wer-", "meaning": "to raise, lift"}], "points": ["air（空気）と同じ。魂の軽やかさが生む、存在のヴェール。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "effulgence_radiance",
        "word": "Effulgence",
        "meaning": "輝き、きらめき、光り輝くこと",
        "era": "17th Century Latin ex- + fulgere",
        "etymology": {
            "components": ["ex- (out)", "fulgere (to shine)"],
            "original_statement": "From Latin effulgentem, from effulgere (to shine forth, glitter), from ex- (out) + fulgere (to shine)."
        },
        "concept": "Shining forth (内側にある光が「外へ（out）」溢れ出し、眩（まぶ）しく「輝く（shine）」こと)",
        "thinking": "抑えようとしても抑えきれない、圧倒的な歓喜や生命力の爆発. 語源の fulgere は、稲妻の閃光を意味します。それは、あなたが真実に触れたとき、あるいは誰かを深く愛したときに、魂の奥底から噴き出す、黄金のマグマのような光です。世界を一瞬で塗り替える、能動的な輝き。",
        "aftertaste": "溢れ出す生命. あなたの内なる光が、今日、世界というキャンバスに最初の一筆を書き加える。",
        "example": "The sun rose with an effulgence that blinded us for a few moments.",
        "deep_dive": { "roots": [{"term": "bhel-", "meaning": "to shine, flash, burn"}], "points": ["bright（明るい）や flame（炎）と同じ。魂の燃焼。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "iridescence_radiance",
        "word": "Iridescence",
        "meaning": "虹彩、玉虫色、(角度によって変わる)きらめき",
        "era": "19th Century Greek iris",
        "etymology": {
            "components": ["iris (rainbow)"],
            "original_statement": "From Latin iris (rainbow) + -escent (becoming)."
        },
        "concept": "Becoming a rainbow (「虹（rainbow）」のように、見る角度によって色彩が「移ろう（becoming）」こと、変幻自在な美)",
        "thinking": "一つの決まった色に留まらず、周囲の光や見る位置によって、千変万化の表情を見せるしなやかな美. 語源は虹の女神イリス。それは、あなたが多様な経験や感情を抱え、それらすべてを光の粒子として自分の表面に纏（まと）っている状態です。矛盾さえも輝きに変える、多層的な魅力。",
        "aftertaste": "移ろう色彩. あなたは一つの定義に縛られる必要はない。光の数だけ、あなたは新しくなれるのだから。",
        "example": "The soap bubble floated in the air, its surface shimmering with iridescence.",
        "deep_dive": { "roots": [{"term": "wei-", "meaning": "to turn, bend (possible for iris)"}], "points": ["iris（瞳の虹彩）や iris（アヤメの花）と同じ、色彩の架け橋。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "phosphorescence_radiance",
        "word": "Phosphorescence",
        "meaning": "燐光、(熱を伴わない)発光、残光",
        "era": "18th Century Greek phos + phoros",
        "etymology": {
            "components": ["phos (light)", "phoros (bringing)"],
            "original_statement": "From phosphorus + -escence (process of becoming). From Greek phosphoros (bringing light), from phos (light) + phoros (bringing)."
        },
        "concept": "Bringing light (光の「源（light）」を自ら「運び（bringing）」、静かな暗闇で「独り（alone）」輝くこと)",
        "thinking": "強い外光が去った後も、自らの内に蓄えた光を密やかに放ち続ける、忍耐強く、孤独な輝き. 語源は「光を運ぶもの」。太陽が沈んだ後の海面や、深い森の朽木。それは、かつて受け取った愛や知識を、自分の血肉に変えて、暗闇を照らす力として再創造している状態です。",
        "aftertaste": "運ばれる光. たとえ太陽が見えなくても、あなたの内側には、かつて見た光が今も静かに息づいている。",
        "example": "The waves glowed with phosphorescence as they crashed against the shore in the dark.",
        "deep_dive": { "roots": [{"term": "bha-", "meaning": "to shine"}, {"term": "bher-", "meaning": "to carry"}], "points": ["photo（写真）や berry（果実：運ばれるもの）と同じ。光を蓄え、運ぶ重み。"] },
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
        print(f"Success: Added {added} words in Cycle 107.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
