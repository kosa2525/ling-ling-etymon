import json
import re

word_batch = [
    # Cycle 138: Stillness & Empty
    {
        "id": "vacant_void",
        "word": "Vacant",
        "meaning": "空いている、空虚な、うつろな、(職が)欠員の",
        "era": "13th Century Latin vacare",
        "etymology": {
            "components": ["vacare (to be empty, be free, be at leisure)"],
            "original_statement": "From Old French vacant, from Latin vacantem, from vacare (to be empty, be free, have leisure)."
        },
        "concept": "State of empty (何かに 「占有（occupy）」 されるのを やめ 「自由（free）」な 余白に 立ち戻ること)",
        "thinking": "何もないことは 欠乏ではなく 新しい何かが 訪れるための 「準備」が 整っているという 豊溢な可能性の状態. 語源は「空であること」. それは 忙しさという名の 鎖から解き放たれ 魂が羽を伸ばして 寛（くつろ）ぐための 聖なる「空地（あきち）」です. 空っぽであることは 軽やかさです.",
        "aftertaste": "空虚の祝福. あなたの心に 意図的に「ベイカント（空白）」を 作ってごらん. そこには 必ず 宇宙からの 新しい閃き（インスピレーション）が 満ち溢れてくるのだから.",
        "example": "He stared into the distance with a vacant expression, lost in his own private world of memory.",
        "deep_dive": { "roots": [{"term": "eu-", "meaning": "to lack, abandon, be empty"}], "points": ["vacuum（真空）や vacation（休暇：空にする時）と同じ。存在の余白。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "evacuate_void",
        "word": "Evacuate",
        "meaning": "避難させる、立ち退く、空にする、(腸を)排泄する",
        "era": "16th Century Latin ex- + vacuus",
        "etymology": {
            "components": ["ex- (out)", "vacuus (empty)"],
            "original_statement": "From Latin evacuatus, past participle of evacuare (to empty out), from ex- (out) + vacuus (empty)."
        },
        "concept": "To empty out (「中にあるもの（content）」を 「外へ出し（out）」 根源的な 「純粋さ（purity）」を 取り戻すこと)",
        "thinking": "自分を 守ろうとして 抱え込みすぎていた 執着や 恐怖を 「一気に手放し」 身を軽くして 危機から 脱出すること. 語源は「空っぽにして出す」. それは 消極的な逃避ではなく 命を守るために 全てを ゼロにリセットする 潔く、力強い 決断のアクションです.",
        "aftertaste": "リセットの勇気. 古い自分（執着）を 「エバキュエイト（排出）」しよう. 器を空にすることで 初めて あなたは 新しい次元の 自分へと 生まれ変わることができるのだから.",
        "example": "The stadium was quickly evacuated following a suspicious phone call, preventing any potential harm.",
        "deep_dive": { "roots": [{"term": "eu-", "meaning": "empty"}], "points": ["vain（無駄な：空の）や avoid（避ける：空にする）と同じ。浄化と生存。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "void_stillness",
        "word": "Void",
        "meaning": "虚空、空虚な、無効な、欠けている",
        "era": "13th Century Latin vocare",
        "etymology": {
            "components": ["vocare (to empty)"],
            "original_statement": "From Old French voide, from Vulgar Latin vocitus, related to Latin vacuus (empty)."
        },
        "concept": "The great empty (万物が 「生まれる前（before birth）」の 根源的な 「静寂」と 「可能性」の 空間)",
        "thinking": "地上のあらゆる 喧騒や 形が 消え去った後に 残る 途方もない 奥行きと 沈黙. 語源は「空っぽの」. 仏教の「空（くう）」に近いこの概念は 私たちのエゴが 溶け去ったときに 現れる 宇宙そのものの 意識の状態を 指しています. 虚空とは 全てが在る場所です.",
        "aftertaste": "虚空の深淵. 孤独という名の「ヴォイド（空虚）」を 恐れないで. その深淵を見つめ続けることで あなたは自分の中に 宇宙と同じ 広大さ（自由）が 宿っていることに 気立つるのだから.",
        "example": "His death left a painful void in the hearts of his family that nothing could ever truly fill.",
        "deep_dive": { "roots": [{"term": "eu-", "meaning": "empty"}], "points": ["waste（荒地：空の場所）や vanish（消える）と同じ。存在の背景。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "hollow_stillness",
        "word": "Hollow",
        "meaning": "空洞の、うつろな、不実な、窪（くぼ）み",
        "era": "Pre-12th Century Old English holh",
        "etymology": {
            "components": ["holh (hollow place, hole)"],
            "original_statement": "From Old English holh, representing a Germanic base meaning 'cave, hole'."
        },
        "concept": "Cave within (「硬い外殻（hard shell）」の 内側に 潜む 「神秘的（mystical）」な 空白のデザイン)",
        "thinking": "中身が詰まっていないことは 欠陥ではなく 響き（レゾナンス）を 生むための 「共鳴箱」としての 究極の 機能美. 語源は「穴、洞窟」. それは 外部の音や 光を 受け入れ 自分の中で じっくりと 反響させ、育むための 守られた 聖なる空間です.",
        "aftertaste": "共鳴の器. 「ホロウ（空洞）」であることを 恥じなくていい. その空白があるからこそ あなたの声は 誰かの心にまで 深く、美しく 響き渡ることができるのだから.",
        "example": "Inside the hollow trunk of the ancient oak tree, several small birds had built their snug nests.",
        "deep_dive": { "roots": [{"term": "kel-", "meaning": "to cover, conceal, save"}], "points": ["hell（地獄：隠された場所）や hall（広間）と同じ。隠伏と受容。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "abyss_stillness",
        "word": "Abyss",
        "meaning": "深淵、奈落、絶望、測り知れないもの",
        "era": "14th Century Greek a- + byssos",
        "etymology": {
            "components": ["a- (without)", "byssos (bottom)"],
            "original_statement": "From Late Latin abyssimus, from Greek abyssos (bottomless), from a- (without) + byssos (bottom of the sea)."
        },
        "concept": "Bottomless depth (「底（bottom）」に 辿り着くことが ないほど 「際限なく（limitless）」 深い 意識の 裂け目)",
        "thinking": "論理や 言葉が 通じない 圧倒的な 垂直の 深度. 語源は「底がない」. それは 恐怖を 呼び起こす 場所でもありますが 同時に その暗闇の 奥（最深部）を 覗き込むことで 魂は 究極の「無私の境地」へと 導かれる 聖なる 滝壺とも言えます.",
        "aftertaste": "底なしの真実. 落下することを 恐れないで. あなたが「アビス（深淵）」へと 飛び込む勇気を持ったとき 重力さえも 消え去り あなたは宇宙（自由）そのものに 変容するのだから.",
        "example": "The explorers stared down into the vast abyss of the canyon, awestruck by its sheer scale.",
        "deep_dive": { "roots": [{"term": "bhudh-", "meaning": "bottom"}], "points": ["bottom（底）や Buddhist（仏教徒：目覚めた者、根源に触れる者）との 心理的な繋がり。"] },
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
        print(f"Success: Added {added} words in Cycle 138.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
