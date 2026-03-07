import json
import re

word_batch = [
    # Cycle 153: Music & Resonance (Refined)
    {
        "id": "orchestrate_music",
        "word": "Orchestrate",
        "meaning": "編成する、調整する、(ひそかに)画策する",
        "era": "19th Century Greek orchestra",
        "etymology": {
            "components": ["orchestra (place for dancing)"],
            "original_statement": "From orchestra + -ate, from Greek orchestra (place for dancing), from orcheisthai (to dance)."
        },
        "concept": "Arranging for dance (「多様な楽器（diversity）」を 「一つの意志（one will）」で 「調和（harmony）」させ 壮大な 運動を 創り出すこと)",
        "thinking": "個々の音（才能）を 殺すのではなく それぞれの 特性を 最大限に 活かしながら、それらが 互いに 響き合い、一つの 完璧な 秩序へと 辿り着くように導く、極めて 高度な 知性の デザイン術. 語源は「踊る場所」. それは 静止した 計画ではなく、常に 躍動し続ける 生命の 祝祭を デザインする アクションです.",
        "aftertaste": "調和の指揮. バラバラであることに 絶望しないで. あなたが「オーケストレイト（調整）」し 多様な声を 一つの 聖なる 旋律へと 結び付けるとき 世界は かつてない 壮大な 輝きを 放ち始めるのだから.",
        "example": "The marketing team carefully orchestrated the product launch to achieve maximum global impact.",
        "deep_dive": { "roots": [{"term": "ergh-", "meaning": "to move, stir, spring"}], "points": ["exhort（強く勧める）と同じ。内側からエネルギーを「沸き立たせる」力。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "sonorous_music",
        "word": "Sonorous",
        "meaning": "(音が)朗々とした、響きのよい、堂々とした",
        "era": "17th Century Latin sonor",
        "etymology": {
            "components": ["sonor (sound)"],
            "original_statement": "From Latin sonorus (sounding, resounding), from sonor (a sound, din), from sonare (to sound)."
        },
        "concept": "Full of sound (「空間（space）」を 「重厚な響き（resonant sound）」で 「満たし（fill）」 威厳を 確立すること)",
        "thinking": "細く 震えるような 音ではなく 大地から 湧き上がり、空気を 支配し、聞く者の 魂を その 豊かな 響きの中に 閉じ込めてしまうような、圧倒的な 存在感. 語源は「音」. それは 語られる内容 以前に その「声の質」そのものが 真実を 証明してしまっているような、聖なる 確信の 響きです.",
        "aftertaste": "朗々たる確信. 低く、深く、自分自身の「本物の声」を 出してごらん. あなたが「ソノラス（朗々とした）」な 響きを 放ち始めたとき 世界は その豊かさに 圧倒され 自然と 静寂を 守り始めるのだから.",
        "example": "He had a deep, sonorous voice that made his speeches feel incredibly authoritative and wise.",
        "deep_dive": { "roots": [{"term": "swen-", "meaning": "to sound"}], "points": ["swan（白鳥：歌う鳥）の語源に関わる説も。美しき響きの使者。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "euphony_music",
        "word": "Euphony",
        "meaning": "快音、心地よい響き、音韻美",
        "era": "17th Century Greek eu- + phone",
        "etymology": {
            "components": ["eu- (good, well)", "phone (sound, voice)"],
            "original_statement": "From Middle French euphonie, from Late Latin euphonia, from Greek euphonia (goodness of voice), from eu- (good) + phone (voice, sound)."
        },
        "concept": "Good sound (「言葉（word）」が 「耳（ear）」を 撫で 「魂（soul）」を 「安撫（soothe）」する 究極の 旋律美)",
        "thinking": "意味を伝えるという 道具的な役割を 超え 言葉の発音そのものが 物理的な 快楽（ハーモニー）を 産み出し、世界の 攻撃性を 削ぎ落としていく、癒やしの アート. 語源は「良い声」. それは 激しい主張を 捨て 存在を 祝福する 旋律（メロディ）へと 自らを 開放する 聖なる「調和」の 状態です.",
        "aftertaste": "快音の慈愛. 刺々（とげとげ）しい言葉で 誰かを 屈服させようと しないで. あなたが「ユーフォニー（快音）」を 奏でるように 語りかけるとき 世界の 緊張は 魔法のように 溶け去ってゆくのだから.",
        "example": "The poet was famous for the incredible euphony of his verses, choosing words as much for their sound as their meaning.",
        "deep_dive": { "roots": [{"term": "asu-", "meaning": "good (for eu-)"}, {"term": "bha-", "meaning": "to speak (for phone)"}], "points": ["eulogy（賛辞：良い言葉）や symphony（交響曲）と同じ。善き響きのルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "cadence_music",
        "word": "Cadence",
        "meaning": "韻律、調子、(行進などの)足取り、終止形",
        "era": "14th Century Latin cadere",
        "etymology": {
            "components": ["cadere (to fall)"],
            "original_statement": "From Old Italian cadenza, from Vulgar Latin cadentia (a falling), from Latin cadere (to fall)."
        },
        "concept": "A falling (「声（voice）」が 「重力（gravity）」に 抗わず 「着地（land）」する 瞬間の 心地よい リズム)",
        "thinking": "ずっと 上昇し続けるのではなく 適切な場所で「落ちる（終結する）」ことで、全体に 安心感と 周期的な リズムを 与える、生命の 呼吸のような 揺らぎ. 語源は「落下」. それは 挫折ではなく 真理が 地上に 降り立ち 確かな 足取り（ステップ）を 刻み始めるための 聖なる「着地」の パルスです.",
        "aftertaste": "リズムの安寧. 常に 走り続けなくていい. あなた自身の人生の「ケイデンス（韻律）」を 大切にしよう. その 周期的な 揺らぎの中にこそ 魂が 真に 休息できる 聖なる場所が あるのだから.",
        "example": "I could hear the steady cadence of the waves drum against the rocks as I drifted off to sleep.",
        "deep_dive": { "roots": [{"term": "kad-", "meaning": "to fall"}], "points": ["casual（偶然の：落ちてきた）や case（事象）と同じ。運命が「落ちてくる」場所。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "philharmonic_music",
        "word": "Philharmonic",
        "meaning": "音楽愛好の、交響楽団の",
        "era": "18th Century Greek philos + harmonikos",
        "etymology": {
            "components": ["philos (loving)", "harmonikos (harmonic)"],
            "original_statement": "From French philharmonique, from Greek philos (loving) + harmonikos (harmonic)."
        },
        "concept": "Love for harmony (「完璧な調和（perfect harmony）」を 「熱愛（loving）」し それを 解体しようとする 「無秩序（chaos）」に 立ち向かうこと)",
        "thinking": "単なる 楽器の 演奏技術 ではなく 「調和（ハーモニー）」という 宇宙的な 概念 そのものを 愛し、それを 地上に 実現しようとする、気高く、情熱的な 共同体（オーケストラ）. 語源は「調和を愛する」. それは 響き合う喜びを 分かち合い、孤独な音を、壮大な 物語（交響曲）へと 昇華させる 聖なる「愛の 結集」です.",
        "aftertaste": "調和への情熱. 一人の力で 全てを 解決しようと しないで. あなたが「フィルハーモニック（調和愛）」の 精神で 誰かと響き合うとき そこには 宇宙の 完璧な 美しさが 幽かに 再現されるのだから.",
        "example": "Attending a concert by the Vienna Philharmonic is a once-in-a-lifetime experience for many music lovers.",
        "deep_dive": { "roots": [{"term": "bhilo-", "meaning": "dear, friendly"}, {"term": "ar-", "meaning": "to fit together"}], "points": ["philosophy（哲学：知を愛する）や article（記事：繋ぎ合わされたもの）と同じ。結合への欲望。"] },
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
        print(f"Success: Added {added} words in Cycle 153.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
