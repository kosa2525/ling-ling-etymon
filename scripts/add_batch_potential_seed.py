import json
import re

word_batch = [
    # Cycle 103: Potential & Seed
    {
        "id": "latency_potential",
        "word": "Latency",
        "meaning": "潜在、潜伏、待ち時間、可能性",
        "era": "17th Century Latin latens",
        "etymology": {
            "components": ["latere (to lie hidden, lurk)"],
            "original_statement": "From Latin latentia (a lying hidden), from latens (hidden, concealed, secret), from latere (to lie hidden)."
        },
        "concept": "Lying hidden (表面には見えず、奥底で「隠れて（hidden）」じっと出番を「待って（lie）」いること)",
        "thinking": "まだ発動していないけれど、解き放たれるその瞬間を、静かに、しかし強烈に予感させるエネルギー. 語源は「隠れる」。冬の土の下で眠る種や、内気な少年の奥に眠る熱い情熱。それは「無い」のではなく、爆発の予兆を孕（はら）んだ、豊かな沈黙の状態です。",
        "aftertaste": "静かなる蓄積。あなたのなかには今、まだ誰も知らない太陽が、目を覚ますその時を待っている。",
        "example": "There is a significant period of latency before the symptoms of the infection appear.",
        "deep_dive": { "roots": [{"term": "lat-", "meaning": "to hide"}], "points": ["latent（潜在的な）や lethal（致命的な：冥府の隠れた力）と同じ、神秘のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "germination_potential",
        "word": "Germination",
        "meaning": "発芽、兆し、(考えなどの)芽生え",
        "era": "15th Century Latin germen",
        "etymology": {
            "components": ["germen (sprout, bud, germ)"],
            "original_statement": "From Middle French germination, from Latin germinationem (a sprouting, budding), from germinare (to sprout, bud, germinate), from germen (seed, germ)."
        },
        "concept": "Sprouting seed (固い殻を破り、生命が「芽吹く（sprout）」瞬間、最初の「兆し（bud）」)",
        "thinking": "長い準備期間（潜伏）を経て、ついに目に見える形となってこの世界に名乗りを上げること. 語源の germen は、生命の本質的な「芽」。単なる成長ではなく、何もないと思っていた荒野に、突如として緑の閃光が走るような、あの劇的な始まりの感覚です。",
        "aftertaste": "はじまりの震え。殻を破る痛みは、あなたが新しい世界に歓迎されているという、確かな証（あかし）だ。",
        "example": "The initial idea for the startup was still in the germination phase.",
        "deep_dive": { "roots": [{"term": "gene-", "meaning": "to give birth, beget"}], "points": ["generation（世代）や genius（天才：生まれ持った資質）と同じ、生命の源。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "embryonic_potential",
        "word": "Embryonic",
        "meaning": "胎芽の、未発達な、初期段階の",
        "era": "19th Century Greek en- + bryein",
        "etymology": {
            "components": ["en- (in)", "bryein (to swell, grow, teem)"],
            "original_statement": "From embryo + -ic. From Medieval Latin embryo, from Greek embryon (fetus, the young of an animal in the womb), from en- (in) + bryein (to swell, teem)."
        },
        "concept": "Swelling in (内側で「膨らみ（swell）」、命が「満ちて（teem）」いく、始まりの「容器（in）」)",
        "thinking": "まだ輪郭は曖昧（あいまい）だけれど、生命の最も基本的な設計図はすべて揃っており、爆発的なスピードで形作られようとしている状態. 語源の bryein は、何かが溢れ出すような「膨らみ」を指します。可能性という名の海に浮かぶ、一粒のダイヤモンドのような初期状態。",
        "aftertaste": "溢れる予感。あなたは今、完成された何者かになる手前の、最も自由で最も力強いカオスのなかにいる。",
        "example": "Their business was still in an embryonic stage, with many details yet to be finalized.",
        "deep_dive": { "roots": [{"term": "bhreu-", "meaning": "to swell, boil, sprout"}], "points": ["burgeon（芽吹く）や breed（繁殖する）と同じ、生命の脈動のルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "incipient_potential",
        "word": "Incipient",
        "meaning": "始まりの、初期の、発端の",
        "era": "17th Century Latin in- + capere",
        "etymology": {
            "components": ["in- (in, on)", "capere (to take)"],
            "original_statement": "From Latin incipientem (beginning), from incipere (to begin, take in hand), from in- (on) + capere (to take)."
        },
        "concept": "Taking in hand (新しい旅へと「踏み出し（take in hand）」、扉を「開ける（in）」こと)",
        "thinking": "予兆が現実になり、具体的な行動として第一歩が踏み出された、あの清冽（せいれつ）な発端. 語源の capere は「掴み取る」。運命の手綱を自らの手に取り、未知の世界へと乗り出していく勇気。何かがこの瞬間に「始まった」という、取り返しのつかない喜び。",
        "aftertaste": "清冽な発端。あなたが最初の一歩を踏み出したとき、世界もまた、あなたを迎え入れるために動き出す。",
        "example": "He detected an incipient signs of rebellion among the crew members.",
        "deep_dive": { "roots": [{"term": "kap-", "meaning": "to grasp"}], "points": ["accept（受け入れる）や capture（捕らえる）と同じ。意志を形にする力のルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "nascent_potential",
        "word": "Nascent",
        "meaning": "発生しようとしている、初期の、生まれつつある",
        "era": "17th Century Latin nasci",
        "etymology": {
            "components": ["nasci (to be born)"],
            "original_statement": "From Latin nascentem (arising, beginning, immature), from nasci (to be born)."
        },
        "concept": "Being born (たった今、この世界に「生まれて（born）」くる、瑞々（みずみず）しい「産声（arising）」)",
        "thinking": "存在しなかったものが、突如として存在になり、呼吸を始める瞬間の美しさ. 語源は「生まれる」。まだ脆（もろ）くて壊れやすいけれど、誰にも汚されていない、処女地のような可能性。それがこれからどんな色に染まり、どんな花を咲かせるかは、まだ誰も知らない、神の秘密です。",
        "aftertaste": "産声の響き。あなたいま、何ものでもなかったものが「何か」になる、宇宙で最も尊い瞬間を目撃している。",
        "example": "The nascent democracy faced many challenges from old political factions.",
        "deep_dive": { "roots": [{"term": "gene-", "meaning": "to give birth"}], "points": ["native（故郷の）や nature（自然：生み出すもの）と同じ、生命の本質のルーツ。"] },
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
        print(f"Success: Added {added} words in Cycle 103.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
