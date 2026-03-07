import json
import re

word_batch = [
    # Cycle 70: Resonance & Echo (Sound)
    {
        "id": "sonorous_sound",
        "word": "Sonorous",
        "meaning": "朗々とした、響き渡る、(声が)深い",
        "era": "17th Century Latin sonor",
        "etymology": {
            "components": ["sonor (sound, noise)"],
            "original_statement": "From Latin sonorus (resounding, sonorous), from sonor (sound, noise), from sonare (to sound)."
        },
        "concept": "Full of sound (音に満ちあふれ、豊かに響き渡ること)",
        "thinking": "ただ大きな音ではなく、深く、重厚で、聞く者の胸の奥にまで染み渡るような響き。語源の sonare は「鳴る」を意味し、楽器が共鳴（resonance）して豊かな倍音を生み出す様子を指します。堂々とした声、あるいは真実を告げる鐘の音のように、空間を支配する圧倒的な存在感です。",
        "aftertaste": "静寂を切り裂くのではなく、静寂そのものを震わせ、歌わせるような深き響き。",
        "example": "He had a sonorous voice that filled the entire cathedral without a microphone.",
        "deep_dive": { "roots": [{"term": "swen-", "meaning": "to sound"}], "points": ["sonic（音の）や sonata（ソナタ）、person（人：仮面を通して響く声）と同じルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "discordance_sound",
        "word": "Discordance",
        "meaning": "不調和、不一致、不快な音の重なり",
        "era": "14th Century Old French/Latin dis- + cors",
        "etymology": {
            "components": ["dis- (apart)", "cors (heart)"],
            "original_statement": "From Old French descordance, from descorder, from Latin discordare (to be at variance), from dis- (apart) + cors (genitive cordis) (heart)."
        },
        "concept": "Hearts being apart (心が「離れ（dis-）」てしまい、バラバラに鳴っている状態)",
        "thinking": "音が噛み合わず、耳障りな不協和音を生み出していること。語源が「心が離れている（hearts apart）」であることは非常に示唆的です。単なる音の問題ではなく、人間関係や社会において、互いのリズムが合わず、ぎすぎすとぶつかり合っている悲しい距離感の象徴でもあります。",
        "aftertaste": "重ならない鼓動。その摩擦から生まれる不快な火花。調和への渇望の裏返し。",
        "example": "There was a sharp discordance between his words and his subsequent actions.",
        "deep_dive": { "roots": [{"term": "kerd-", "meaning": "heart"}], "points": ["concordance（調和：心が一箇所にある）や courage（勇気：心の力）と同類。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "cacophony_sound",
        "word": "Cacophony",
        "meaning": "不快な音、不協和音、騒音",
        "era": "17th Century French/Greek kakos + phone",
        "etymology": {
            "components": ["kakos (bad, evil)", "phone (voice, sound)"],
            "original_statement": "From French cacophonie, from Greek kakophonia, from kakophonos (harsh-sounding), from kakos (bad, evil) + phone (voice, sound)."
        },
        "concept": "Bad voices (「悪い（kakos）」声や音が、無秩序に溢れかえっていること)",
        "thinking": "いくつもの騒がしい音が混ざり合い、意味をなさない騒音となっている状態。都会の喧騒、あるいは議論が紛糾する議場。美しさ（euphony）の反対語。それは耳を塞ぎたくなるようなカオスですが、同時に、生命の無秩序で野生的なエネルギーが爆発している瞬間でもあります。",
        "aftertaste": "溢れるノイズ。その中から、あなただけの旋律を拾い上げるのは容易ではない。",
        "example": "As the market opened, a cacophony of shouts and bells filled the air.",
        "deep_dive": { "roots": [{"term": "bha-", "meaning": "to speak, tell"}], "points": ["telephone（電話）や symphony（交響曲）と同じ『音/声』のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "euphemism_sound",
        "word": "Euphemism",
        "meaning": "遠回しな表現、婉曲語法",
        "era": "17th Century Greek eu + pheme",
        "etymology": {
            "components": ["eu- (well, good)", "pheme (speaking)"],
            "original_statement": "From Greek euphemismos, from euphemizein (speak with fair words), from eu- (good, well) + pheme (speaking, voice)."
        },
        "concept": "Speaking well (不吉なことや無礼なことを、あえて「良く（eu-）」言い換えること)",
        "thinking": "本来は、神聖な儀式の最中に不吉な言葉（死や呪いなど）を避けるために「美しい言葉」に置き換えたことに由来します。真実をぼやかす（filter）ための優しさ、あるいは臆病さ。言葉の「響き」を整えることで、現実という毒を和らげようとする、人間らしい知恵の痕跡です。",
        "aftertaste": "包み紙の中の真実。直接触れるには熱すぎる何かを、冷ますための作法。",
        "example": "The phrase 'passed away' is a common euphemism for the act of dying.",
        "deep_dive": { "roots": [{"term": "bha-", "meaning": "to speak, tell"}], "points": ["prophet（預言者：先に語る人）や fame（名声：語られること）と同じ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "mellifluous_sound",
        "word": "Mellifluous",
        "meaning": "(声や音楽が)甘く流れるような、滑らかな",
        "era": "15th Century Latin mel + fluere",
        "etymology": {
            "components": ["mel (honey)", "fluere (to flow)"],
            "original_statement": "From Late Latin mellifluus (flowing like honey), from Latin mel (genitive mellis) (honey) + fluere (to flow)."
        },
        "concept": "Flowing like honey (「蜂蜜（mel）」のように、甘く、とろりと流れる響き)",
        "thinking": "ただ滑らかなだけでなく、聞く者の心を癒し、うっとりとさせるような「甘美な」音色や声。言葉の粒が、金色の液体となって耳から心へと染み込んでいくような感覚。それは時間という概念をも忘れさせる、完璧な安らぎを伴う音楽的快楽の名前です。",
        "aftertaste": "耳に注がれる黄金の果実。心までもが、甘い沈黙へと溶けてゆく。",
        "example": "The actress's mellifluous voice was perfect for the audio book narration.",
        "deep_dive": { "roots": [{"term": "mel-", "meaning": "honey"}, {"term": "bhleu-", "meaning": "to swell, flow"}], "points": ["melody（メロディ）とは語源が異なりますが（melos: 歌）、感覚的には繋がっています。"] },
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
        print(f"Success: Added {added} words in Cycle 70.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
