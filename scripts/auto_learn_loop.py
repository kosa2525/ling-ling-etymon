import json
import re

word_batches = [
    # Batch 1: Urban Life & Architecture (Cycle 65)
    [
        {
            "id": "avenue_urban",
            "word": "Avenue",
            "meaning": "大通り、並木道、(目標への)手段",
            "era": "16th Century French/Latin venire",
            "etymology": {
                "components": ["ad- (to)", "venire (to come)"],
                "original_statement": "From Old French avenue (a way of approach), from avenir (to come to, arrive), from Latin advenire (to come to)."
            },
            "concept": "A way to arrive (目的地へと「辿り着く」ための道)",
            "thinking": "ただの道（road）ではなく、ある特定の場所（邸宅や都市の中心など）へと「向かっていく（ad-venire）」ことを意識した道。それは物理的な通りであると同時に、問題解決や成功へと至るための「アプローチ（手段）」という抽象的な意味も内包しています。常に、何かの始まりへと繋がっている道です。",
            "aftertaste": "並木を抜けた先に。あなたが辿り着くべき場所が、静かに待っている。",
            "example": "The committee is exploring every possible avenue to resolve the funding crisis.",
            "deep_dive": { "roots": [{"term": "gwa-", "meaning": "to go, come"}], "points": ["adventure（冒険）や souvenir（思い出）と同じく、何かが『やって来る』ことの象徴。"] },
            "part_of_speech": "noun"
        },
        {
            "id": "façade_urban",
            "word": "Facade",
            "meaning": "建物の正面、(実体とは異なる)外見",
            "era": "17th Century French/Italian faccia",
            "etymology": {
                "components": ["facia (face)"],
                "original_statement": "From French façade, from Italian facciata (face), from faccia."
            },
            "concept": "The face of a thing (物事の「顔」としての正面)",
            "thinking": "建物の一番目立つ「顔」の部分。それは美しく整えられていますが、その背後には複雑な配管や構造が隠されています。転じて、人間の社交的な「外面（そとづら）」、あるいは困難を隠して平静を装う「虚勢」を意味するようになりました。内面と外面のあわいに立つ、美しき境界。",
            "aftertaste": "完璧な表面の裏側で。本当の自分が、静かに息を潜めている。",
            "example": "He managed to maintain a cheerful façade despite his inner overwhelming sadness.",
            "deep_dive": { "roots": [{"term": "dhe-", "meaning": "to set, put"}], "points": ["face（顔）と同じ。表に『置かれた』形。"] },
            "part_of_speech": "noun"
        },
        {
            "id": "threshold_urban",
            "word": "Threshold",
            "meaning": "敷居、入り口、限界値",
            "era": "Old English þerscold",
            "etymology": {
                "components": ["þrescan (to thresh, stomp)"],
                "original_statement": "From Old English þerscold (threshing floor, doorsill), related to þrescan (to tread, stamp)."
            },
            "concept": "A place to tread (足元で踏みしめ、境界を越える場所)",
            "thinking": "もともとは収穫した麦を脱穀するために足で「踏みしめる（thresh）」場所。それが家の入り口にあったことに由来します。一つの世界から次の世界へ足を踏み出すための、運命の分水嶺。「これ以上は耐えられない」という痛みや音の限界値（しきい値）という意味も、この足元の境界線から生まれました。",
            "aftertaste": "その一線を越えたとき。あなたはもう、以前のあなたではいられない。",
            "example": "The company is on the threshold of a major breakthrough in AI technology.",
            "deep_dive": { "roots": [{"term": "ter-", "meaning": "to rub, turn"}], "points": ["摩擦と回転のルーツ。境界線は常に磨り減り、変化し続ける場所。"] },
            "part_of_speech": "noun"
        }
    ],
    # Batch 2: Light & Visibility (Cycle 66)
    [
        {
            "id": "halo_light",
            "word": "Halo",
            "meaning": "(太陽・月の)光輪、後光、栄光",
            "era": "16th Century Latin/Greek halos",
            "etymology": {
                "components": ["halos (threshing floor, disc of the sun/moon)"],
                "original_statement": "From Latin halos, from Greek halos (threshing floor; also the disc of the sun or moon), because the threshing floor was round."
            },
            "concept": "A circular threshing floor (円形の脱穀場のように丸く輝く光)",
            "thinking": "もともとは、家畜がぐるぐると円を描きながら歩いて麦を脱穀した「円形の場所」を指していました。その美しい円の形が、太陽や月の周りに見える光輝、さらには聖人の頭上に描かれる「後光」へと転じたのです。日常的な労働の場が、神聖な光の象徴へと昇華された言葉です。",
            "aftertaste": "足元に描いた円が、いつか頭上の光輪（ハロー）となって輝きだす。",
            "example": "The moon was surrounded by a beautiful white halo in the cold night sky.",
            "deep_dive": { "roots": [{"term": "ghel-", "meaning": "to shine"}], "points": ["glow（輝く）や gold（金）と同じく、光そのもののルーツ。"] },
            "part_of_speech": "noun"
        },
        {
            "id": "glimmer_light",
            "word": "Glimmer",
            "meaning": "微かな光、明滅、(かすかな)兆し",
            "era": "15th Century Scandinavian/Middle English glimmer",
            "etymology": {
                "components": ["glim- (to shine slightly, blink)"],
                "original_statement": "From Middle English glimeryn, related to gleam and Scandinavian glimme (to shine slightly)."
            },
            "concept": "A faint, unstable light (消えそうに瞬く、不安定な微光)",
            "thinking": "煌々（こうこう）と照らす光ではなく、暗闇の中で今にも消えてしまいそうに揺れる、弱く、しかし確かな光。それは完全なる絶望の中に現れる「かすかな希望の兆し（a glimmer of hope）」のメタファーでもあります。不安定だからこそ、目を離せない美しさがあります。",
            "aftertaste": "暗闇を深く見つめる者だけが。その微かな瞬きを、希望として捉えることができる。",
            "example": "The light of the distant campfire began to glimmer through the trees and thick fog.",
            "deep_dive": { "roots": [{"term": "ghel-", "meaning": "to shine"}], "points": ["gleam（光り輝く）や glitter（きらめく）の、最も大人しく謙虚な親族。"] },
            "part_of_speech": "noun"
        }
    ],
    # Batch 3: Knowledge & Philosophy (Cycle 67)
    [
        {
            "id": "paradigm_phil",
            "word": "Paradigm",
            "meaning": "パラダイム、枠組み、理論的モデル、模範",
            "era": "15th Century Greek para- + deigma",
            "etymology": {
                "components": ["para- (beside)", "deiknumi (to show)"],
                "original_statement": "From Greek paradeigma (pattern, model), from paradeiknunai (show side by side), from para- (beside) + deiknumi (to show)."
            },
            "concept": "Showing by the side (何かと「並べて」示される模範、パターン)",
            "thinking": "単なる例示ではなく、物事を考えるための「根本的な枠組み」。ある時代の常識を支配する、巨大な考え方のパターンです。それが変化することを「パラダイム・シフト」と呼びます。新しい世界を見るためには、今の思考を「横（para-）」から眺めて、新しいモデルと並べてみる必要があります。",
            "aftertaste": "あなたが信じている現実は。ただの『考え方の慣習』という名の箱に過ぎないのかもしれない。",
            "example": "The internet caused a complete paradigm shift in how we communicate and consume news.",
            "deep_dive": { "roots": [{"term": "deik-", "meaning": "to point out, show"}], "points": ["dictate（命じる）や digit（指/数字）と同じ。指し示されるもの。"] },
            "part_of_speech": "noun"
        },
        {
            "id": "dogma_phil",
            "word": "Dogma",
            "meaning": "教条、独断、定説",
            "era": "16th Century Greek dokin",
            "etymology": {
                "components": ["dokeein (to seem good, think)"],
                "original_statement": "From Greek dogma (opinion, tenet), from dokein (to seem good, think, suppose)."
            },
            "concept": "What seems good to be true (「正しいはずだ」と一方的に思われていること)",
            "thinking": "本来は、あるグループや宗教において「正しいと思われる意見」のことでした。それがいつしか、議論を許さない「絶対的な決まり事」という意味に変わりました。思考を止めて盲信するのではなく、その「ドグマ」がどこから来たのかを問い直すことが、真の知性の始まりです。",
            "aftertaste": "疑うことを忘れた正義は。時として、思考を凍りつかせる呪文となる。",
            "example": "We should not blindly accept traditional policies and political dogma without question.",
            "deep_dive": { "roots": [{"term": "dek-", "meaning": "to take, accept"}], "points": ["decorum（礼儀）や decent（きちんとした）と同じ『受け入れられる』という感覚。"] },
            "part_of_speech": "noun"
        }
    ]
]

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'

def run_update(batch_index):
    batch = word_batches[batch_index]
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
        if not match:
            return f"Error: Could not find array in Batch {batch_index}"

        prefix, json_array_str, suffix = match.groups()
        words = json.loads(json_array_str)
        existing_ids = {w.get("id") for w in words}
        
        added = 0
        for item in batch:
            if item["id"] not in existing_ids:
                words.append(item)
                added += 1
        
        new_content = content[:match.start()] + prefix + json.dumps(words, ensure_ascii=False, indent='\t') + suffix + content[match.end():]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return f"Success: Added {added} words in Cycle {65 + batch_index}."
    except Exception as e:
        return f"Error in Batch {batch_index}: {e}"

# Execute all cycles
results = []
for i in range(len(word_batches)):
    results.append(run_update(i))

print("\n".join(results))
