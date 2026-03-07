import json
import re

word_batch = [
    # Cycle 96: Wonder & Awe
    {
        "id": "astonishment_awe",
        "word": "Astonishment",
        "meaning": "驚き、驚愕、仰天",
        "era": "14th Century Latin ex- + tonare",
        "etymology": {
            "components": ["ex- (out)", "tonare (to thunder)"],
            "original_statement": "From Old French astoner (to stun, daze, stupefy), from Vulgar Latin extonare (to leave thunderstruck), from ex- (out) + tonare (to thunder)."
        },
        "concept": "Thunderstruck (雷の「音（thunder）」に打たれたかのように、魂が震え、衝撃を受けること)",
        "thinking": "単なる驚きではなく、目の前で雷鳴が轟（とどろ）いたときのように、言葉を失い、思考が一時的に停止してしまうほどの圧倒的な衝撃. 語源の ex- + tonare は「雷に打たれる」ことを意味します。既成概念が崩れ去り、世界が全く新しい姿で立ち現れたときの、魂の震えです。",
        "aftertaste": "光の衝撃。世界は、あなたが思っていたよりも遥かに巨大で、予測不能で、そして美しい。",
        "example": "To my utter astonishment, she remembered my name after twenty years.",
        "deep_dive": { "roots": [{"term": "ten-", "meaning": "to stretch, thunder"}], "points": ["thunder（雷）や stun（気絶させる）と同じ、圧倒的な力のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "reverence_awe",
        "word": "Reverence",
        "meaning": "敬意、崇拝、畏敬",
        "era": "14th Century Latin re- + vereri",
        "etymology": {
            "components": ["re- (intensive)", "vereri (to fear, respect, revere)"],
            "original_statement": "From Old French reverence, from Latin reverentia (awe, respect), from revereri (to stand in awe of, respect, honor), from re- (intensive) + vereri (to fear, respect)."
        },
        "concept": "Standing in awe (気高いもの、聖なるものの前に立ち、「畏れ（fear）」と「敬い（respect）」を感じること)",
        "thinking": "恐怖ではなく、対象のあまりの気高さや深淵さに触れ、身が引き締まると同時に深い喜びを感じる心. 語源の vereri は「恐れる」ことと「守る」こと、両方の意味を含みます。それは、自分よりも大きな存在を認め、それに対して自らを低くする、謙虚でありながら豊かな精神の姿勢です。",
        "aftertaste": "聖なる沈黙。ひざまずくことは、負けることではない。より大きな光に、自分を開くことなのだ。",
        "example": "He spoke of his former teacher with profound reverence and gratitude.",
        "deep_dive": { "roots": [{"term": "wer-", "meaning": "to perceive, watch over"}], "points": ["ward（守る）や aware（気づいている）と同じ、対象への深い集中。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "sublimity_awe",
        "word": "Sublimity",
        "meaning": "崇高、壮大、卓越",
        "era": "17th Century Latin sub- + limen",
        "etymology": {
            "components": ["sub- (up to)", "limen (threshold, lintel, crossbeam)"],
            "original_statement": "From sublime (adjective), from Latin sublimis (uplifted, high, lofty, exalted), probably from sub- (up to) + limen (threshold, lintel)."
        },
        "concept": "Up to the threshold (日常の「敷居（threshold）」ギリギリまで、「高く（high）」引き上げられること)",
        "thinking": "単なる「美」を超え、どこか恐ろしさや絶大さを感じさせるほどの圧倒的な高み. 語源の limen は、家の入り口の横木。それは、人間が理解できる限界の「境界線」にまで達している状態です。巨大な山脈や、宇宙の深淵。美しすぎて震えが止まらない、あの「極限」の感覚です。",
        "aftertaste": "境界線の向こう側. あなた今、日常という器をはみ出し、宇宙の広大さと直結している。",
        "example": "The sublimity of the starry sky often moves people to deep philosophical reflection.",
        "deep_dive": { "roots": [{"term": "ele-", "meaning": "to lift (possible for limen)"}], "points": ["subliminal（潜在意識の：敷居の下）の対極。意識の最高到達点。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "marvel_awe",
        "word": "Marvel",
        "meaning": "驚くべきもの、不思議、驚嘆",
        "era": "13th Century Latin mirari",
        "etymology": {
            "components": ["mirari (to wonder at, admire, be astonished)"],
            "original_statement": "From Old French marveille (a wonder, marvel, miracle), from Vulgar Latin mirabilia (wonderful things), from Latin mirari (to wonder at)."
        },
        "concept": "Wonder at (思わず見惚（みと）れてしまうような、信じがたい「不思議（wonder）」)",
        "thinking": "見慣れたはずの風景の中に、突如として奇跡のような輝きを見つけ出すこと. 語源の mirari は「見る」ことも意味します。鏡（Mirror）が真実を映し出すように、Marvel はこの世界の隠された美しさを、私たちの驚嘆の眼差しを通じて映し出します。それは、世界を初めて見る子供の瞳を取り戻す体験です。",
        "aftertaste": "魔法のひとしずく。日常という灰色のヴェールの下で、世界は今も、奇跡を隠し持っている。",
        "example": "The intricate design of a butterfly's wing is a true marvel of nature.",
        "deep_dive": { "roots": [{"term": "smei-", "meaning": "to smile, laugh"}], "points": ["smile（微笑む）や mirror（鏡）と同じ。驚きは、魂の静かな微笑みでもある。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "enchantment_awe",
        "word": "Enchantment",
        "meaning": "魅惑、魔法、喜び",
        "era": "14th Century Latin in- + cantare",
        "etymology": {
            "components": ["in- (in, into)", "cantare (to sing)"],
            "original_statement": "From Old French enchantement, from enchanter (to bewitch, charm), from Latin incantare (to sing a magic spell over), from in- (into) + cantare (to sing)."
        },
        "concept": "Singing into (誰かの心の中に「歌（song）」を注ぎ込み、恍惚（こうこつ）とさせること)",
        "thinking": "言葉としての理解を超え、調べそのものが持つ魔力によって心を奪われてしまう状態. 語源は「歌いかける（Incantare）」。魔法とは、説明することではなく、響かせることです。あなたの魂が、世界が奏でる言葉のない旋律と完璧に調和したとき、そこには至福の「魔法」がかかります。",
        "aftertaste": "消えない音楽。論理が眠りにつくとき、あなたの心の奥底で、世界という歌が鳴り始める。",
        "example": "The forest was filled with the enchantment of twilight, shadowy and mysterious.",
        "deep_dive": { "roots": [{"term": "kan-", "meaning": "to sing"}], "points": ["cantor（合唱隊長）や accent（アクセント）と同じ。美しさは『響き』のなかに宿る。"] },
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
        print(f"Success: Added {added} words in Cycle 96.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
