import json
import re

word_batch = [
    # Cycle 68: Natural Motion & Energy
    {
        "id": "cascade_nature",
        "word": "Cascade",
        "meaning": "小滝、階段状に落ちるもの、連鎖反応",
        "era": "17th Century Italian/Latin cadere",
        "etymology": {
            "components": ["cadere (to fall)"],
            "original_statement": "From French cascade, from Italian cascata (a fall), from cascare (to fall), from Latin cadere (to fall)."
        },
        "concept": "A series of falls (次々に「落ちていく（fall）」連鎖の連なり)",
        "thinking": "ただ一箇所で落ちるのではなく、岩肌を伝うように「次から次へと連続して」流れ落ちていく状態。それは物理的な水だけでなく、一つのミスが次を招く「障害の連鎖」や、美しい情報が広まる「情報の連鎖」など、重力に逆らえない圧倒的なエネルギーの転移そのものを指しています。",
        "aftertaste": "止まらない。最初の一滴が放たれたとき、その終わりはすでに運命づけられている。",
        "example": "A cascade of light golden hair fell down over her narrow shoulders.",
        "deep_dive": { "roots": [{"term": "kad-", "meaning": "to fall"}], "points": ["casual（偶然の：ふとした拍子に落ちてきたもの）や decay（腐敗：落ちていくこと）と同類。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "ebb_nature",
        "word": "Ebb",
        "meaning": "引き潮、衰退、次第に弱まる",
        "era": "Old English ebba",
        "etymology": {
            "components": ["ib- (back, off)"],
            "original_statement": "From Old English ebba (the reflux of the tide), from Proto-Germanic *af-tipon (a going off)."
        },
        "concept": "A going back (潮が「引いていく（off）」、遠ざかる引き潮)",
        "thinking": "満ちる（flow）ことの対極。海が静かに、しかし抗いがたい力で足元から遠ざかっていく様子。人生のエネルギーや人気の「衰退」を意味することも。しかし、引くことは決して悪いことではありません。次の「満ち潮」のために、世界が深呼吸をして、新しい水を準備している貴重な静止の時間なのです。",
        "aftertaste": "引く波。それは喪失ではなく、再び満たされるための壮大な『後退』という名の準備。",
        "example": "The intense enthusiasm for the new project began to ebb after the first difficult month.",
        "deep_dive": { "roots": [{"term": "apo-", "meaning": "away, off"}], "points": ["after（後に）や off（離れて）と同じ『引き』のニュアンス。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "surge_nature",
        "word": "Surge",
        "meaning": "(感情や波の)急増、押し寄せる力、波のように高まる",
        "era": "15th Century Old French/Latin surgere",
        "etymology": {
            "components": ["sub- (up from below)", "regere (to keep straight, lead)"],
            "original_statement": "From Middle French sourge, from Latin surgere (to rise, spring up), from sub- (up from below) + regere (to keep straight, guide)."
        },
        "concept": "Rising up from below (下から突き上げて、真っ直ぐに「立ち上がる（rise）」こと)",
        "thinking": "静かだった水面が突然爆発するように盛り上がること。あるいは、胸の奥から熱い感情が「こみ上げてくる」こと。語源の surgere は、指揮者（regere）がタクトを執るように、混沌から一つの「真っ直ぐな力」が生じ、上へと真っ直ぐ導かれる（sub-）様を表します。力強い生の噴出です。",
        "aftertaste": "制御不能な、内なる爆発。それは、あなたを今いる場所よりも高く押し上げる。",
        "example": "A sudden surge of adrenalin made him feel like he could run for many more miles.",
        "deep_dive": { "roots": [{"term": "reg-", "meaning": "to move in a straight line"}], "points": ["rectify（修正する：真っ直ぐにする）や source（源泉）と同じルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "torrent_nature",
        "word": "Torrent",
        "meaning": "急流、土砂降り、(言葉などの)ほとばしり",
        "era": "16th Century Latin torrens",
        "etymology": {
            "components": ["torrere (to parch, burn, boil)"],
            "original_statement": "From French torrent, from Latin torrentem (a rushing stream), originally 'burning, parching', hence 'boiling, roaring like a boiling stream'."
        },
        "concept": "A boiling rush (あまりの勢いに、水が「煮え立っている（boiling）」かのように見える激流)",
        "thinking": "ただの早い流れではありません。その勢いゆえに泡立ち、熱を帯びているかのように「吠えている（roaring）」状態。激しい雨、あるいは怒涛のように溢れ出した「言葉のほとばしり（a torrent of words）」。それは、理性というダムが決壊したあとに訪れる、圧倒的な表現の暴力です。",
        "aftertaste": "熱い水の咆哮。それはすべてを飲み込み、世界を新しい形へと削り取ってゆく。",
        "example": "The mountain stream turned into a raging torrent after the heavy summer rainfall.",
        "deep_dive": { "roots": [{"term": "ters-", "meaning": "to dry"}], "points": ["thirst（喉の乾き）や toast（トースト：焼く）と同じルーツから『沸き立つ激流』が生まれた皮肉。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "vortex_nature",
        "word": "Vortex",
        "meaning": "渦、渦巻き、(人を)巻き込むもの",
        "era": "17th Century Latin vertere",
        "etymology": {
            "components": ["vertere (to turn, roll, wheel)"],
            "original_statement": "From Latin vortex, variant of vertex (an eddy, whirlpool, summit), from vertere (to turn)."
        },
        "concept": "A place that turns around (中心を持って激しく「回転（turn）」し続ける場所)",
        "thinking": "中心に向かってすべてを吸い込み、猛烈なスピードで回転し続ける「渦」。一度その重力の圏内に入ってしまえば、自力で抜け出すことは困難な「逃れられない引力」。思考の渦、情熱の渦。それは破壊的でありながら、同時に新しいエネルギーを生成するための、宇宙のリサイクル装置のようでもあります。",
        "aftertaste": "中心の静寂。その周りでは、すべてが狂おしく踊り、溶け合っている。",
        "example": "He felt himself being drawn into a vortex of controversy and endless legal battles.",
        "deep_dive": { "roots": [{"term": "wer-", "meaning": "to turn, bend"}], "points": ["verse（詩：行を折り返すもの）や reverse（逆転）と同じ、回転のダイナミズム。"] },
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
        print(f"Success: Added {added} words in Cycle 68.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
