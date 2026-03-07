import json
import re

word_batch = [
    # Cycle 140: Crystal & Clarity (Refined)
    {
        "id": "pellucid_clarity",
        "word": "Pellucid",
        "meaning": "透明な、澄み渡った、(文体などが)明快な",
        "era": "17th Century Latin per- + lucidus",
        "etymology": {
            "components": ["per- (through)", "lucer (to shine)"],
            "original_statement": "From Latin pellucidus, from per- (through) + lucidus (light, bright, clear), from lucere (to shine)."
        },
        "concept": "Shining through (光が 「どこまでも（thoroughly）」 貫き 「淀み（cloudiness）」を 一切 残さない 究極の 透明感)",
        "thinking": "単なる透明（トランスパレント）を超え、その向こう側にある真実が、まるで目の前にあるかのように鮮やかに浮かび上がる、極限の明晰さ. 語源は「完全に光り輝く」. それは 迷いや誤解が入り込む隙が微塵（みじん）もない、聖なる知性の極致です.",
        "aftertaste": "極限の明晰。あなたの思考を「ペルシッド（澄明）」に研ぎ澄まそう。濁りを捨て、ただ光を通すことで 世界はその本当の美しさを あなたに惜しみなく語りかけるのだから。",
        "example": "The pellucid water of the tropical lagoon allowed us to see every detail of the coral reef below.",
        "deep_dive": { "roots": [{"term": "leuk-", "meaning": "light, brightness"}], "points": ["lucid（明快な）の強意形。一切の不純を許さない、絶対的な清らかさ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "hyaline_clarity",
        "word": "Hyaline",
        "meaning": "ガラス状の、透明な、(生物)硝子(しょうし)質の",
        "era": "16th Century Greek hyalos",
        "etymology": {
            "components": ["hyalos (glass)"],
            "original_statement": "From Latin hyalinus, from Greek hyalinos (of glass), from hyalos (glass, crystal)."
        },
        "concept": "Like glass (「ガラス（glass）」のように 非結晶で 「静謐な（silent）」 滑らかさと 透明度を 持つもの)",
        "thinking": "生命の躍動を 一時的に 凍結させたような 秩序正しく、かつ 壊れやすい ギリギリの 均衡の上に成り立つ 美しさ. 語源は「ガラス」. それは 物理的な透明さであると同時に 魂が 不純物を 削ぎ落とした末に 辿り着く 無私の 境地を 指しているようでもあります.",
        "aftertaste": "硝子の静寂. 自分の形（エゴ）を 強く主張しないで. あなたが「ハイアリン（硝子質）」のように 澄み渡ることで 世界の光は より純粋に あなたを 通り抜けてゆくのだから.",
        "example": "The creature's hyaline wings shimmered with iridescent colors under the microscope.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["ヒアルロン酸（hyaluronic acid）の語源。潤いと透明感の根源。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "diaphanous_clarity",
        "word": "Diaphanous",
        "meaning": "透き通るような、(布などが)ごく薄い、天国的な",
        "era": "17th Century Greek dia- + phainein",
        "etymology": {
            "components": ["dia- (through)", "phainein (to show)"],
            "original_statement": "From Medieval Latin diaphanus, from Greek diaphanes (transparent), from dia- (through) + phainein (to show, make appear)."
        },
        "concept": "Showing through (「向こう側（through）」が 幽かに 「透けて見える（show）」 儚くも 聖なる 境界)",
        "thinking": "完全に透明（見えない）ではなく、柔らかな光を纏いながら、微かにその存在を主張する、繊細で天国的な質感. 語源は「透けて見える」. それは 物質と精神の境界線にあるような 圧倒的な軽やかさと 慈悲深さを 象徴しています. 天使の羽衣のような.",
        "aftertaste": "天上の軽やかさ. 重苦しい現実（重力）に 縛られないで. あなたの心を「ダイアファナス（透明）」に保つことで どんな困難も 柔らかな光とともに 潜り抜けることができるのだから.",
        "example": "The bride wore a diaphanous silk veil that floated around her like a soft morning mist.",
        "deep_dive": { "roots": [{"term": "bha-", "meaning": "to shine"}], "points": ["phenomenon（現象）や epiphany（顕現）と同じ。真理が幽かに現れる瞬間。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "distinct_clarity",
        "word": "Distinct",
        "meaning": "はっきりした、明瞭な、全く別の、独特な",
        "era": "14th Century Latin dis- + stinguere",
        "etymology": {
            "components": ["dis- (apart)", "stinguere (to prick, mark)"],
            "original_statement": "From Latin distinctus, past participle of distinguere (to separate, divide, mark off), from dis- (apart) + stinguere (to prick, puncture, mark)."
        },
        "concept": "Marked apart (「境界線（mark）」を 鋭く 「刻む（prick）」ことで 曖昧さを 完全に 「排除する」こと)",
        "thinking": "他の何者でもない 自分自身の「固有の輪郭」を 鮮やかに 立ち上がらせる 潔き 知性の決断. 語源は「突き分ける」. それは 混ざり合う（カオス）ことを 拒み 唯一無二の アイデンティティを 確立するための 誇り高い 境界線の 宣言です. 違いは、尊厳です.",
        "aftertaste": "輪郭の誇り. 誰かの色に 染まろうとしなくていい. あなたが「ディスティンクト（明瞭）」であることで あなたという 唯一の奇跡は 世界の中で 誰にも真似できない 輝きを放つのだから.",
        "example": "There is a distinct possibility that the project will be completed ahead of schedule.",
        "deep_dive": { "roots": [{"term": "steig-", "meaning": "to stick, prick"}], "points": ["sting（刺す）や instinct（本能）と同じ。刻み込まれた、消せない証（あかし）。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "perspicuous_clarity",
        "word": "Perspicuous",
        "meaning": "(文章などが)明快な、分かりやすい、洞察力のある",
        "era": "16th Century Latin per- + specere",
        "etymology": {
            "components": ["per- (through)", "specere (to look)"],
            "original_statement": "From Latin perspicuus (transparent, clear), from perspicere (to see through), from per- (through) + specere (to look at)."
        },
        "concept": "Looking through (「複雑なもの（complex）」を 「透かし見る（look through）」ことで 本質を 鮮やかに 「捉える」こと)",
        "thinking": "表面的な 飾りを 削ぎ落とし 誰の心にも まっすぐ 届くような 淀みのない 言葉の 選び方. 語源は「透かし見る」. それは 自分の知性を ひけらかすことではなく 相手の知性を 信じ 共に 真理の地平へと 降り立つための 誠実な 知性の 橋渡しです.",
        "aftertaste": "透明な対話. 言葉を 重ねるよりも その透明度を 磨こう. あなたの「パースピキュアス（明快）」な表現が 誰かの心の霧を晴らし 新しい理解への 扉を 開くのだから.",
        "example": "He had a remarkable talent for explaining perspicuous solutions to extremely complex problems.",
        "deep_dive": { "roots": [{"term": "spek-", "meaning": "to observe"}], "points": ["perspective（遠近法、視点）の兄弟語。本質を射抜く、真っ直ぐな視線。"] },
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
        print(f"Success: Added {added} words in Cycle 140.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
