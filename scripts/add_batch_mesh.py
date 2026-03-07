import json
import re

word_batch = [
    # Cycle 128: Web & Entanglement
    {
        "id": "complex_web",
        "word": "Complex",
        "meaning": "複雑な、複合体、込み入った",
        "era": "17th Century Latin com- + plectere",
        "etymology": {
            "components": ["com- (together)", "plectere (to weave, braid, twine)"],
            "original_statement": "From Latin complexus, past participle of complecti (to encircle, embrace, comprise), from com- (together) + plectere (to weave, braid, twine)."
        },
        "concept": "Woven together (多くの要素を 「一体（together）」と して 「織り合わせる（weave）」 逃れがたき 構築体)",
        "thinking": "単純な一本の線ではなく 無数の糸が 幾重にも重なり合い、結びつき合い 一つの 豊潤で 迷宮的な全体を 形作っている状態. 語源は「共に織る」. 物事を「複雑（コンプレックス）」と捉えることは それをありのままに、深い敬意を持って 眺めることの 始まりでもあります.",
        "aftertaste": "重なる色彩. 複雑であることは 美しいことだ. あなたの人生の 絡み合った糸の一つひとつを 慈しみながら その壮大な模様（タペストリー）を 誇らしく眺めてごらん.",
        "example": "The human brain is the most complex structure known to exist in the entire universe.",
        "deep_dive": { "roots": [{"term": "plek-", "meaning": "to plait"}], "points": ["multiply（掛け合わせる：幾重にも折る）や simple（単純な：一重の）と同じ、折り重ねの知性。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "intricate_web",
        "word": "Intricate",
        "meaning": "入り組んだ、複雑な、(芸術的に)精巧な",
        "era": "15th Century Latin in- + tricae",
        "etymology": {
            "components": ["in- (into)", "tricae (perplexities, hindrances, toys, trifles)"],
            "original_statement": "From Latin intricatus, past participle of intricare (to entangle, perplex, embarrass), from in- (into, in) + tricae (perplexities, hindrances, toys, trifles, viles)."
        },
        "concept": "Into perplexities (「迷い（perplexities）」の 中へと 「引きずり込む（into）」 ほどに 精巧な 絡まり)",
        "thinking": "単に込み入っているだけでなく その一つひとつが 圧倒的な繊細さと 必然性を持って 配置されている 芸術的な極致. 語源は「当惑の中へ」. それは 見る者を「嬉しい当惑」へと誘い 視線を離させないほどに 神秘的で 完成された 迷宮のような美しさです.",
        "aftertaste": "精緻なる迷宮. その「入り組んだ美しさ」を 解こうとしなくていい. ただその細部を 愛でることで あなたの心は 日常の粗野なリズムから 解き放たれてゆくのだから.",
        "example": "The lacework was so intricate that it must have taken months of painstaking labor to complete.",
        "deep_dive": { "roots": [{"term": "ter-", "meaning": "to cross, pass over (possible for tricae)"}], "points": ["trick（策略）と同じルーツ。私たちの注意を、巧妙に惹きつける力。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "mesh_web",
        "word": "Mesh",
        "meaning": "網目、噛み合うこと、絡み合う",
        "era": "14th Century Germanic mask-",
        "etymology": {
            "components": ["mask- (to knit, twist)"],
            "original_statement": "From Middle Dutch masche, from Proto-Germanic maskwon (to knit, twist; a knot, loop, mesh)."
        },
        "concept": "The knotted loop (糸を 「結び（knot）」 「輪に変える（loop）」 ことで生まれる 強固な 「繋がり」)",
        "thinking": "一本では弱い糸も 規則正しく結び合わされることで 巨大な獲物や 思想を 逃さず捉えるための 「面（構造）」へと 変容すること. 語源は「結ぶ」. あなたの行動が 他者の意志と「メッシュ（噛み合う）」とき そこには 個人を超越した 巨大なエネルギーが 流れ出します.",
        "aftertaste": "共鳴の網目. あなたという一節（ノード）が 誰かと正しく結ばれたとき. その瞬間 世界を救い上げるための 聖なる「網（メッシュ）」が また少し 広く、強くなるのだ.",
        "example": "Their business styles mesh perfectly, leading to a highly successful and productive partnership.",
        "deep_dive": { "roots": [{"term": "mez-", "meaning": "to knit (possible root)"}], "points": ["match（一致する）とは違う、物理的な「食い込み」と「連結」のニュアンス。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "entangle_web",
        "word": "Entangle",
        "meaning": "絡ませる、巻き込む、もつれさせる",
        "era": "16th Century en- + tangle",
        "etymology": {
            "components": ["en- (in)", "tangle (seaweed; to twist together)"],
            "original_statement": "From en- (in) + tangle (noun). Tangle probably related to seaweed (tangle) that twists together."
        },
        "concept": "Wrapped in seaweed (「海藻（seaweed）」の ように 「複雑に（twist）」 絡め取られ 抗（あらが）えなくなること)",
        "thinking": "意図せず 何かに自分を 奪われてしまう不自由さと 同時に 否定できない「親密な繋がり」への 墜落. 語源は「海藻に絡まる」. 強い愛や 信念というものは 私たちを心地よく（あるいは苦しく）「エンタングル（拘束）」し 孤独という名の 岸辺から 遠ざけてゆくのです.",
        "aftertaste": "甘美なる拘束. 何にも縛られない自由もいいけれど 何かと深く 抜き差しならぬほどに 絡まり合って生きること. それもまた 人生の深い豊かさ（海）へと 潜るための 唯一の道なのだ.",
        "example": "The dolphin became hopelessly entangled in the discarded fishing net, unable to surface for air.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["quantum entanglement（量子もつれ）と同じ。物理的な距離を超えた、根源的な繋がりの隠喩。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "plexus_web",
        "word": "Plexus",
        "meaning": "(血管・神経などの)網状組織、絡まり、集合体",
        "era": "17th Century Latin plectere",
        "etymology": {
            "components": ["plectere (to weave, braid)"],
            "original_statement": "From Latin plexus (a weaving, plaiting), from plectere (to weave, braid, twine, entwine)."
        },
        "concept": "The woven center (生命を維持する 枢要な 「神経や情報の（neural）」 「織り合わされた（woven）」 中心)",
        "thinking": "中心（センター）でありながら それ自体が 複雑な「網」として 血液や情報を 循環させている 命のハブ. 語源は「織ること」. 感情の高ぶりが 胃のあたり（太陽神経叢）に響くように この「プレクサス（網状組織）」は 私たちの理性と本能を 密やかに 繋いでいる 聖なる中継地点です.",
        "aftertaste": "命の交差点. あなたの内側にある この「複雑な連帯」を感じてごらん. 数え切れないほどの信号が 織りなすその調和（リズム）が あなたという 唯一の奇跡を 支え続けているのだから.",
        "example": "The solar plexus is often described as the second brain of the human body, sensitive to deep emotions.",
        "deep_dive": { "roots": [{"term": "plek-", "meaning": "to plait"}], "points": ["complex（複雑な）の兄弟語。生命そのものが「織物」であるという、古代の直感。"] },
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
        print(f"Success: Added {added} words in Cycle 128.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
