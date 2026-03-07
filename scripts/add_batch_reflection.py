import json
import re

word_batch = [
    # Cycle 82: Reflection & Resonance
    {
        "id": "reverberation_sound",
        "word": "Reverberation",
        "meaning": "残響、反響、反射、(影響の)波及",
        "era": "16th Century Latin re- + verberare",
        "etymology": {
            "components": ["re- (back, again)", "verberare (to beat, strike, lash)"],
            "original_statement": "From Latin reverberatus, past participle of reverberare (to beat back, drive back), from re- (back) + verberare (to strike, beat), from verber (a lash, whip)."
        },
        "concept": "Beating back (壁に「打ち（beat）」当たり、何度も「跳ね返って（back）」くること)",
        "thinking": "音が止んだあとも、空間の壁に激突し、反射を繰り返しながら震え続ける余韻。それは単なる「響き」ではなく、過去の出来事や言葉が、現在の沈黙の中にまで何度も打ち寄せてくるような、消えることのない影響の連鎖です。一回の「打撃（strike）」が、永遠のこだまを生む。",
        "aftertaste": "止まない震え。あなたが放った一言は、まだ世界のどこかで、誰かの心に当たりながら響き続けている。",
        "example": "The decision had a profound reverberation throughout the entire organization.",
        "deep_dive": { "roots": [{"term": "wer-", "meaning": "to turn, bend"}], "points": ["verber（鞭）は、しなって戻ってくるもの。響きは『痛みの記憶』でもある。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "echo_sound",
        "word": "Echo",
        "meaning": "こだま、反響、模倣",
        "era": "14th Century Greek Ekho",
        "etymology": {
            "components": ["Ekho (a mountain nymph)"],
            "original_statement": "From Latin echo, from Greek ekho (sound, resonance, or the nymph Echo who could only repeat others' words)."
        },
        "concept": "A repeated voice (自らの声を失い、他者の言葉を「繰り返す」だけの存在)",
        "thinking": "ギリシャ神話の妖精エコー。彼女は自分の言葉を語ることを禁じられ、ただ相手の語尾を繰り返すだけの記憶の影となりました。それは孤独な投影であり、空虚な模倣。けれど、山びこ（echo）が返ってくる時、私たちは広い世界の中に「自分」が確かに存在し、何かに触れたという確信を得るのです。",
        "aftertaste": "返ってくる自分。鏡のない闇の中でも、あなたの声は世界の輪郭を教えてくれる。",
        "example": "His words were a strange echo of a conversation we had many years ago.",
        "deep_dive": { "roots": [{"term": "swagh-", "meaning": "to resound"}], "points": ["妖精の名前から普遍的な自然現象へ。自分の声が自分に戻るという哀しき円環。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "speculation_reflect",
        "word": "Speculation",
        "meaning": "推測、思索、投機、鏡に映ること",
        "era": "14th Century Latin speculum",
        "etymology": {
            "components": ["speculum (mirror)", "specere (to look)"],
            "original_statement": "From Latin speculationem (contemplation, observation), from speculari (to spy out, watch), from speculum (mirror), from specere (to look)."
        },
        "concept": "Reflecting in a mirror (「鏡（mirror）」を通して、見えない未来を「見る（look）」こと)",
        "thinking": "単なる当てずっぽうではなく、目の前の現象を「思考の鏡」に映し出し、その反射から真理や未来を読み解ようとする理知的で、かつ不確実な試み。語源の speculum は「鏡」。私たちは直接未来を見ることはできませんが、思考という鏡を磨くことで、その予兆（影）を捉えることができるのです。",
        "aftertaste": "鏡像の未来。確かではない。けれど、あなたの知覚はすでに、まだ見ぬ場所の光を捉えている。",
        "example": "The sudden rise in stock prices led to widespread speculation about a new tech breakthrough.",
        "deep_dive": { "roots": [{"term": "spek-", "meaning": "to observe"}], "points": ["spectacle（光景）や spy（スパイ）と同じ『見る』力の、内面への応用。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "introspection_reflect",
        "word": "Introspection",
        "meaning": "内省、内観、自己反省",
        "era": "17th Century Latin intro- + specere",
        "etymology": {
            "components": ["intro- (inward)", "specere (to look at)"],
            "original_statement": "From Latin introspectus, past participle of introspicere (to look into, look inside), from intro- (inward) + specere (to look at)."
        },
        "concept": "Looking inward (外の世界から目を逸らし、自分の「内側（inward）」を深く「見る（look）」こと)",
        "thinking": "外部の騒音を遮断し、自分自身の心という暗い洞窟に松明（たいまつ）を灯して探索すること。そこには驚くほど広大な、そして未踏の宇宙が広がっています. 自己を知ることは、すべての智慧（ちえ）の始まり。自分の中の「鏡（reflect）」を覗き込む、静かで勇気ある行為です。",
        "aftertaste": "暗闇のなかの光。一番遠い場所は、いつだってあなたの内側にある。",
        "example": "He spent years of deep introspection trying to understand his true desires.",
        "deep_dive": { "roots": [{"term": "spek-", "meaning": "to observe"}], "points": ["speculation と同じ『見る』ルーツ。視線を外から内へと 180 度回転させること。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "responsive_reflect",
        "word": "Responsive",
        "meaning": "反応が良い、共鳴する、(問いに)応じる",
        "era": "15th Century Latin re- + spondere",
        "etymology": {
            "components": ["re- (back)", "spondere (to pledge, promise)"],
            "original_statement": "From Latin responsivus, from respondere (to answer, reply, respond), from re- (back) + spondere (to pledge)."
        },
        "concept": "Pledging back (相手からの問いかけに対し、自分からも「誓い（pledge）」を返すこと)",
        "thinking": "ただ機械的に「反応」するのではなく、相手の存在を認め、それに対して自分の一部を差し出す（誓う）ような深い呼応。語源の spondere は神聖な「誓約」を意味します. 呼びかけに答える（respond）ことは、世界との約束を更新し続ける、命の温かなキャッチボールなのです。",
        "aftertaste": "温かなこだま。あなたが呼ぶから。私は今、ここで自らの声を誓いとして返します。",
        "example": "A truly responsive design adapts perfectly to any screen size or user preference.",
        "deep_dive": { "roots": [{"term": "spend-", "meaning": "to make an offering, perform a ritual"}], "points": ["spouse（配偶者：誓い合った者）や sponsor（保証人）と同じ、重みのある『約束』。"] },
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
        print(f"Success: Added {added} words in Cycle 82.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
