import json
import re

word_batch = [
    # Cycle 98: Change & Transformation
    {
        "id": "metamorphosis_change",
        "word": "Metamorphosis",
        "meaning": "変態、変形、変容",
        "era": "16th Century Greek meta- + morphe",
        "etymology": {
            "components": ["meta- (change)", "morphe (form)"],
            "original_statement": "From Latin metamorphosis, from Greek metamorphosis (a transforming), from metamorphoun (to transform, to be transfigured), from meta- (change) + morphe (form)."
        },
        "concept": "Change of form (「形（form）」を劇的に「変える（change）」こと、本質的な変容)",
        "thinking": "単なる外面の変化ではなく、幼虫が蝶になるように、古い自分を脱ぎ捨てて全く別の存在へと生まれ変わるプロセス. 語源の meta- は「超越」をも意味します。それは、これまでの限界を超えて、新しい次元の自分へと、不可逆的な跳躍を遂げることです。",
        "aftertaste": "脱ぎ捨てる勇気。痛みとともに古い殻を破るとき、あなたの背中には、まだ見ぬ空を飛ぶための美しい羽が宿っている。",
        "example": "The company underwent a complete metamorphosis after the new CEO took over.",
        "deep_dive": { "roots": [{"term": "mer-", "meaning": "to shimmer (possible for morphe)"}], "points": ["morphine（モルヒネ：形を曖昧にするもの）や morphology（形態学）と同じ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "innovation_change",
        "word": "Innovation",
        "meaning": "革新、刷新、新機軸",
        "era": "15th Century Latin in- + novus",
        "etymology": {
            "components": ["in- (into)", "novus (new)"],
            "original_statement": "From Latin innovationem (a renewal, a newness), from innovatus, past participle of innovare (to renew, restore), from in- (into) + novus (new)."
        },
        "concept": "Into the new (古い制度や考え方の内側（into）から、全く「新しい（new）」光を放つこと)",
        "thinking": "ゼロから何かを作るのではなく、既存のものの中に、新しい息吹を注ぎ込み、その価値を再定義すること. 語源の novus は「新しい」。それは現状に対する健全な違和感から始まり、世界をより良く、より美しく塗り替えていこうとする、能動的な情熱の形です。",
        "aftertaste": "新しい夜明け。あなたが持ち込んだその「新しさ」が、凝り固まった世界に、再び流動性と希望をもたらす。",
        "example": "Technological innovation is the primary driver of economic growth in the 21st century.",
        "deep_dive": { "roots": [{"term": "newo-", "meaning": "new"}], "points": ["novel（小説：新しい物語）や novice（初心者）と同じ、始まりのルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "vicissitude_change",
        "word": "Vicissitude",
        "meaning": "変遷、浮沈、変化",
        "era": "16th Century Latin vicis",
        "etymology": {
            "components": ["vicis (a change, interchange, turn, stead)"],
            "original_statement": "From Middle French vicissitude, from Latin vicissitudo (change, alteration), from vicis (a change, interchange, turn, stead)."
        },
        "concept": "Turning in stead (代わり番こに「回転（turn）」し、状況が移り変わっていくこと)",
        "thinking": "人生の波のように、幸運と不運、光と影が、代わる代わる訪れる避けられない変化. 語源の vicis は「交代」。定点にとどまることなく、常に変化し続けることこそが、世界の真理であり、美しさでもあります。移ろうからこそ、今この瞬間の輝きは、かけがえのないものになります。",
        "aftertaste": "巡る季節. 喜びも悲しみも、永遠には続かない。変化し続けるという、その唯一の不変を、あなたは愛している。",
        "example": "The vicissitudes of fortune are often unpredictable and follow no logical pattern.",
        "deep_dive": { "roots": [{"term": "weik-", "meaning": "to bend, wind"}], "points": ["vice versa（逆もまた然り）や week（週：巡る時間）と同じ、回転のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "catalyst_change",
        "word": "Catalyst",
        "meaning": "触媒、きっかけ、促進させるもの",
        "era": "20th Century Greek kata- + lyein",
        "etymology": {
            "components": ["kata- (down)", "lyein (to loosen)"],
            "original_statement": "From catalysis, from Greek katalysis (dissolution, a loosening), from katalyein (to dissolve), from kata- (down) + lyein (to loosen)."
        },
        "concept": "Loosening down (強固に結びついたものを「解き（loosen）」、変化を加速させること)",
        "thinking": "自分自身は変わることなく、周囲の状況に劇的な変化をもたらす存在. 語源の lyein は、結び目を解くこと。膠着（こうちゃく）した状況を揺さぶり、新しい反応を引き起こす、静かで強力なきっかけ。あなたがそこにいるだけで、何かが動き出し、世界の色が変わり始める。そのような存在の力。",
        "aftertaste": "解き放つ者。あなたが投じた一石が、大きな波紋となり、止まっていた時間を再び流し始める。",
        "example": "The young activist's speech served as a catalyst for environmental reform in the city.",
        "deep_dive": { "roots": [{"term": "leu-", "meaning": "to loosen, divide"}], "points": ["loose（緩い）や analysis（分析：解き分けること）と同じ、分解と解放のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "mutability_change",
        "word": "Mutability",
        "meaning": "変わりやすさ、無常、格段の差",
        "era": "14th Century Latin mutare",
        "etymology": {
            "components": ["mutare (to change)"],
            "original_statement": "From Old French mutabilite, from Latin mutabilitatem (changeableness, mutability), from mutabilis (changeable), from mutare (to change)."
        },
        "concept": "Ability to change (常に「変化（change）」し続け、一定の状態に留まらない、という性質)",
        "thinking": "この世のあらゆるものは、次の瞬間には別のものへと変わっているという厳粛な「無常」. 語源の mutare は、交換することを意味します。固定された「自分」などどこにもおらず、世界との交換を繰り返す流れの中にこそ、生命のダイナミズムが宿ります。変化を恐れることは、生きることを恐れること。",
        "aftertaste": "移ろう形。一定であることの重圧から、あなたはもう自由だ。変化の波に身を任せ、どこまでも新しくなり続けよう。",
        "example": "The mutability of fashion trends makes it difficult for brands to stay relevant for long.",
        "deep_dive": { "roots": [{"term": "mei-", "meaning": "to change, go, move"}], "points": ["mutation（変異）や common（共通の：交換される）と同じ、移動と交換のルーツ。"] },
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
        print(f"Success: Added {added} words in Cycle 98.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
