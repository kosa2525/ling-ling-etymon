import json
import re

word_batch = [
    # Cycle 120: Crystal & Clarity
    {
        "id": "crystalline_clarity",
        "word": "Crystalline",
        "meaning": "水晶のような、澄み切った、透明な、結晶の",
        "era": "15th Century Greek krystallos",
        "etymology": {
            "components": ["krystallos (ice, crystal)"],
            "original_statement": "From Old French cristallin, from Latin crystallinus, from Greek krystallos (ice; rock-crystal)."
        },
        "concept": "Like ice (「氷（ice）」のように 澄み渡り 「規則正しい構造（structure）」を 持つこと)",
        "thinking": "不純物が一切混じらず 本質だけが幾何学的な美しさを持って 整列している状態. 語源は「氷」. それは 冷徹なまでの明晰さと 揺るぎない構造美を兼ね備えています. あなたの思考が「クリスタリン（結晶的）」になったとき 複雑な世界は一つの明解な理（ことわり）として立ち現れます.",
        "aftertaste": "透明な秩序. 迷いを削ぎ落としてゆけば 最後にはこの結晶のような純粋さが残る. その透き通った瞳で 世界の真理を射抜こう.",
        "example": "The mountain stream was crystalline, allowing us to see every smooth pebble on the bottom.",
        "deep_dive": { "roots": [{"term": "kruos-", "meaning": "icy cold, frost"}], "points": ["crystal（水晶）や crust（地殻：固まったもの）と同じ。凍結した美。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "translucent_clarity",
        "word": "Translucent",
        "meaning": "半透明の、光を通す",
        "era": "16th Century Latin trans- + lucere",
        "etymology": {
            "components": ["trans- (through)", "lucere (to shine)"],
            "original_statement": "From Latin translucentem, from translucere (to shine through), from trans- (through) + lucere (to shine)."
        },
        "concept": "Shining through (光を「向こう側まで（through）」 「通す（shine）」 柔らかな透明感)",
        "thinking": "すべてを見透かすのではなく 光を優しく受け入れ 拡散させながら 向こう側の気配を伝えること. 語源は「透き通って光る」. それは 隠し事がない潔さと 同時にすべてをさらけ出さない奥ゆかしさを 併せ持っています. ヴェール越しに見る世界のような 慈悲深い明瞭さです.",
        "aftertaste": "光の透過. あなたが透明である必要はない. ただ 訪れる光を拒まず 向こう側へと受け流す「しなやかさ」があれば それだけで世界は明るくなるのだから.",
        "example": "The translucent petals of the cherry blossoms glowed softly in the morning light.",
        "deep_dive": { "roots": [{"term": "trans-", "meaning": "across"}, {"term": "leuk-", "meaning": "light, brightness"}], "points": ["lucid（明快な）や light（光）と同じ。媒介としての美。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "pellucid_clarity",
        "word": "Pellucid",
        "meaning": "清明な、透明な、(文体などが)明快な",
        "era": "17th Century Latin per- + lucidus",
        "etymology": {
            "components": ["per- (thoroughly)", "lucidus (bright, clear)"],
            "original_statement": "From Latin pellucidus (transparent, clear), from per- (thoroughly) + lucidus (bright, clear), from lucere (to shine)."
        },
        "concept": "Thoroughly bright (「徹底的に（thoroughly）」 「輝いている（bright）」 曇りなき透明度)",
        "thinking": "一滴の濁りもなく 視線がどこまでも突き抜けていくような 圧倒的な清らかさ. 語源は「完全に光り輝く」. 水面が静まり返り 底の砂粒までが手に取るように見える あの静謐な瞬間. あなたの言葉が「ペルシード（清明）」であるとき 聴く人の心からは すべての霧が晴れてゆきます.",
        "aftertaste": "極致の清明. 濁りを恐れないで. 濁りを沈殿させ 徹底的に濾過（ろか）し続けた先にこそ この透き通った「明快さ」が待っているのだから.",
        "example": "His pellucid prose made even the most complex philosophical ideas easy to grasp.",
        "deep_dive": { "roots": [{"term": "per-", "meaning": "through"}, {"term": "leuk-", "meaning": "brightness"}], "points": ["Lucifer（明けの明星：光を運ぶもの）と同じルーツ。純化された知性。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "diaphanous_clarity",
        "word": "Diaphanous",
        "meaning": "透明に近い、透き通るような、繊細な",
        "era": "17th Century Greek dia- + phainein",
        "etymology": {
            "components": ["dia- (through)", "phainein (to show)"],
            "original_statement": "From Medieval Latin diaphanus, from Greek diaphanes (transparent), from dia- (through) + phaineine (to show, make appear)."
        },
        "concept": "Showing through (「向こう側を（through）」 「見せる（show）」 絹のように薄く 繊細な質感)",
        "thinking": "物質としての重さをほとんど感じさせない 妖精の羽や朝霧のような 儚（はかな）い透明感. 語源は「透けて見える」. それは 現実の向こう側にある「イデア（理想）」が わずかにこちらの世界に 漏れ出しているかのような 神秘的な美しさを湛（たた）えています. 触れれば消えてしまいそうな 純粋さ.",
        "aftertaste": "薄衣の神秘. 強すぎる光よりも この「透き通るような繊細さ」を愛したい. 儚いからこそ それは永遠に傷つかない 理想の姿なのだから.",
        "example": "The bride wore a diaphanous silk veil that floated around her like a cloud.",
        "deep_dive": { "roots": [{"term": "dia-", "meaning": "through"}, {"term": "bha-", "meaning": "to shine"}], "points": ["phenomenon（現象：現れるもの）や fantasy（空想）と同じ。光の顕現。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "limpid_clarity",
        "word": "Limpid",
        "meaning": "澄んだ、透明な、(目が)澄みきった",
        "era": "17th Century Latin limpidus",
        "etymology": {
            "components": ["limpidus (clear, bright, transparent)"],
            "original_statement": "From Latin limpidus (clear, bright, transparent), related to lympha (clear water, water goddess)."
        },
        "concept": "Clear water (「清らかな水（water）」のように 淀みがなく 「澄み切った（bright）」 瞳や水面)",
        "thinking": "生まれたての泉や 邪気のない子供の瞳のように 邪念が一切混じっていない 純真な透明さ. 語源は「清らかな水」. それは 知識による明快さというよりも 魂そのものが持っている 根源的な清涼感です. この「リンピッド（澄明）」な境地にあるとき 世界はありのままの姿を あなたに見せてくれます.",
        "aftertaste": "原生の泉. 難しく考えるのをやめてごらん. あなたの心という泉から 濁りを取り除けば 世界は最初から こんなにも「澄み切っていた」ことに 気づくはずだ.",
        "example": "She looked at me with limpid blue eyes that seemed to see right through my lies.",
        "deep_dive": { "roots": [{"term": "limpa-", "meaning": "clear water"}], "points": ["lymph（リンパ：清らかな液）の語源。生命を浄化する水のルーツ。"] },
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
        print(f"Success: Added {added} words in Cycle 120.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
