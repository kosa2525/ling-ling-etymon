import json
import re

word_batch = [
    {
        "id": "mathematics_logic",
        "word": "Mathematics",
        "meaning": "数学、算数",
        "era": "16th Century Greek mathematike",
        "etymology": {
            "components": ["mathema (knowledge, study, learning)"],
            "original_statement": "From Greek mathematike (tekhne) (mathematical art), from mathema (that which is learned, science), from manthanein (to learn)."
        },
        "concept": "That which is learned (学ばれたこと、学習の対象)",
        "thinking": "本来は単なる「数」を扱う学問ではなく、学問全般において「学ばれ、知識とされるべき対象（learning）」そのものを指していました。それは、推論によって導き出される、疑いようのない「知」の体系。宇宙の言語としての数学の、最も真摯な姿です。",
        "aftertaste": "思考を極限まで削ぎ落とし、抽象の宇宙を描き出す共通言語。",
        "example": "Mathematics provides the logical foundation for ancient star navigation.",
        "deep_dive": {
            "roots": [{"term": "mn-", "meaning": "to think, remember"}],
            "points": ["mind（精神）や memory（記憶）と同じ『考える』の源泉。宇宙そのものを憶えようとする試みです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "axiom_logic",
        "word": "Axiom",
        "meaning": "公理、自明の理、格言",
        "era": "15th Century Old French/Greek axioma",
        "etymology": {
            "components": ["axios (worthy)"],
            "original_statement": "From Greek axioma (that which is thought worthy, fit), from axios (worthy, of like value)."
        },
        "concept": "That which is thought worthy (価値あるものとして（議論なしに）認められること)",
        "thinking": "議論を始める前に、それ以上証明する必要がないほど「明らかな価値（worthy：axios）」があるとして、無条件に受け入れられる前提。思考のピラミッドの最下段に置かれる、最初の一歩であり、究極の信頼そのもの。",
        "aftertaste": "疑いえない、最初の一歩。そこからすべてという世界が始まる。",
        "example": "In geometry, Euclid established five fundamental axioms for logic.",
        "deep_dive": {
            "roots": [{"term": "ag-", "meaning": "to drive, move"}],
            "points": ["軸（axis）や動かす（act/agent）と同根で、『バランスをとって釣り合わせる』イメージ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "algorithm_logic",
        "word": "Algorithm",
        "meaning": "アルゴリズム、(計算や問題解決の)手順",
        "era": "13th Century Arabic Al-Khwarizmi",
        "etymology": {
            "components": ["Al-Khwarizmi (Persian mathematician)"],
            "original_statement": "A blend of Medieval Latin algorismus and Greek arithmos (number), originally from the name of the great mathematician Al-Khwarizmi."
        },
        "concept": "The method of Al-Khwarizmi (アル＝フワーリズミーのやり方、計算の方式)",
        "thinking": "9世紀のアラビアの数学者「アル＝フワーリズミー（Al-Khwarizmi）」の名前に由来します。もともとは数学の「筆算」を指しましたが、後に「ギリシャ語の数字（arithmos）」という言葉の意味を吸収して、複雑な問題を解くための、論理的で迷いのない「手順の連鎖」を意味するようになりました。",
        "aftertaste": "混沌の中から、一筋の意味の糸を紡ぎ出す、論理の迷宮脱出法。",
        "example": "The computer uses a complex algorithm to optimize the best search results.",
        "deep_dive": {
            "roots": [{"term": "arithmos", "meaning": "number"}],
            "points": ["arithmetic（算術）と同じ響きに変化したことで、いっそう『数』の響きが強まりました。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "syllogism_logic",
        "word": "Syllogism",
        "meaning": "三段論法、演繹的推論",
        "era": "14th Century Old French/Greek syllogismos",
        "etymology": {
            "components": ["syn- (together)", "logos (reason, reckoning)"],
            "original_statement": "From Greek syllogismos (inference, conclusion), from syllogizesthai (to conclude), from syn- (together) + logizesthai (to reckon, compute, reason), from logos (word, reason)."
        },
        "concept": "Reckoning together (理由を集めて一つにすること)",
        "thinking": "バラバラの事実（言葉/ロゴス）を「一緒に（syn-）」集めて計算し、そこから一つの真実を導き出すこと。AはB、BはC、ゆえにAはC。それらは論理の鎖。鎖の環を繋いでいくように、誰も否定できない結論へと他者を導くための、思考の究極のコンパスです。",
        "aftertaste": "二つの点を繋ぐ。三つ目の点に、光が灯る。",
        "example": "Classic logic relies heavily on the use of clear and valid syllogisms.",
        "deep_dive": {
            "roots": [{"term": "leg-", "meaning": "to share, collect, speak"}],
            "points": ["logistics（物流：集めて計算する）や collect（集める）と同族です。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "hypothesis_logic",
        "word": "Hypothesis",
        "meaning": "仮説、仮定",
        "era": "16th Century Late Latin/Greek hupothesis",
        "etymology": {
            "components": ["hupo- (under)", "thesis (a placing)"],
            "original_statement": "From Greek hupothesis (supposition, base, basis), from hupotithenai (to place under, suppose), from hupo- (under) + tithenai (to place)."
        },
        "concept": "Placing something under (土台として下に置かれたもの、仮の前提)",
        "thinking": "立派な理論や「命題（Thesis）」を打ち立てる前に、あえて一旦その「下に（hupo-）」土台として「置いて（thesis）」みるもの。それは確実な真理ではないけれど、そこから思考を積み上げるための、勇気ある未完成の問いかけです。仮の台座なしには、いかなる巨大な思考の像も立てることはできません。",
        "aftertaste": "もしも、これが正しいとしたら。そこから、未知の冒険が始まる。",
        "example": "The scientist proposed a bold new hypothesis based on the gathered data.",
        "deep_dive": {
            "roots": [{"term": "dhe-", "meaning": "to set, put"}],
            "points": ["hypodermic（皮下の）の hypo- や do（する）の源流 dhe- と繋がっています。"]
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
