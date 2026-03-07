import json
import re

word_batch = [
    # Cycle 168: Seed & Origin (Refined II)
    {
        "id": "seminal_seed_fixed",
        "word": "Seminal",
        "meaning": "種子の、精液の、(後に大きな影響を与える)独創的な、重大な",
        "era": "14th Century Latin semen",
        "etymology": {
            "components": ["semen (seed)"],
            "original_statement": "From Old French seminal, from Latin seminalis (of or belonging to seed), from semen (seed)."
        },
        "concept": "Containing seeds (「現在（present）」の 「小さな形（small form）」の中に 「未来（future）」の 「巨大な 構造（giant structure）」が 「情報」として 畳み込まれていること)",
        "thinking": "派手な 成果 ではなく、その後の あらゆる 変化の 起点（ソース）となり、歴史の 流れを 決定づけてしまうような、根源的で 濃密な インスピレーション. 語源は「種子の、種」. それは 完成 ではなく 可能性の 爆発力であり 私たちが 宇宙の 新しい サイクルを 始動させるための 聖なる「遺伝子」の 表現です.",
        "aftertaste": "未来の設計図. 自分の 小さな 発想を 軽んじないで. あなたの 放つ「セミナル（独創的な）」な 一言や 行動が 遠い 未来で 巨大な 智慧の 森へと 育ち 多くの 人々を 癒やす（いやす） 木陰を 作るのだから.",
        "example": "His seminal work on linguistics changed the way philosophers understood the relationship between thought and language.",
        "deep_dive": { "roots": [{"term": "se-", "meaning": "to sow"}], "points": ["season（季節：種まきの時期）や disseminate（普及させる：種を散らす）と同じ。生命の 拡散のルーツ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "dormant_seed",
        "word": "Dormant",
        "meaning": "休眠状態の、眠っている、(火山などが)活動休止中の",
        "era": "14th Century Latin dormire",
        "etymology": {
            "components": ["dormire (to sleep)"],
            "original_statement": "From Old French dormant, present participle of dormir (to sleep), from Latin dormire (to sleep)."
        },
        "concept": "Sleeping vitality (「表面（surface）」では 「静止（stillness）」しているが 「内部（inside）」では 「爆発（explosion）」の 「タイミング」を 密かに 待ち続けていること)",
        "thinking": "何もしない 怠惰 ではなく、来るべき 覚醒の 瞬間のために、エナジーを 外部へ 漏らさず（セーブ）、静寂の 中で 自己を 研ぎ澄ませ続ける、聖なる「猶予（ゆうよ）」の 状態. 語源は「眠っている」. それは 忘却 ではなく 季節（タイミング）が 巡り来る までの 宇宙との 聖なる「沈黙の 約束」の 表現です. 休眠は、準備です.",
        "aftertaste": "静かなる胎動. 今、成果が 出せずに じっとしている 自分を 責めないで. あなたの 魂が「ドーマント（休眠中）」な 状態に 在るとき その 内側では かつてない 巨大な 生命の 飛躍が 虎視眈々と 準備されているのだから.",
        "example": "The seeds remained dormant in the dry desert soil for decades, waiting for the first touch of rain to bloom.",
        "deep_dive": { "roots": [{"term": "drem-", "meaning": "to sleep"}], "points": ["dormitory（寮）と同じ。休息という名の、エナジーの 充填。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "germinate_seed",
        "word": "Germinate",
        "meaning": "芽を出す、発芽させる、(考えなどが)生じる",
        "era": "16th Century Latin germen",
        "etymology": {
            "components": ["germen (sprout, bud, germ)"],
            "original_statement": "From Latin germinatus, past participle of germinare (to sprout, bud), from germen (a sprout, bud, germ)."
        },
        "concept": "Sprouting into life (「静止（stillness）」という 殻を 「内側からの 意志（inner will）」で 「打ち破り（break）」 「世界（world）」へと 「介入」し 始めること)",
        "thinking": "単なる 成長 ではなく、昨日までの 自分を 守っていた 殻（境界）を 破壊してでも、外の世界（他者）へと 手を 伸ばそうとする、勇気ある 変容の 第一歩. 語源は「芽吹く、萌え出る」. それは 痛み ではなく 自らの 内部にある 輝き（ギフト）を 現実のものと させようとする 聖なる「始動」の アクションです. 発芽は、越境です.",
        "aftertaste": "境界の破壊. 変化に伴う 恐れ（痛み）を 拒絶しないで. あなたの 構想が「ジャーミネイト（発芽）」し 厚い 殻を 割って 地上に 姿を 現したとき そこには 全く新しい 光り輝く 可能性の 大地が 拓けているのだから.",
        "example": "It took several months for the seed of a business idea to finally germinate into a concrete plan.",
        "deep_dive": { "roots": [{"term": "gene-", "meaning": "to give birth, beget"}], "points": ["generation（世代）や genius（天才：産み出された才能）と同じ。生命の 産声。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "matrix_origin",
        "word": "Matrix",
        "meaning": "(数学・コンピューター)行列、基板、母体、発生源",
        "era": "14th Century Latin mater",
        "etymology": {
            "components": ["mater (mother)"],
            "original_statement": "From Latin matrix (breeding animal, later womb, source, origin), from mater (mother)."
        },
        "concept": "Maternal source (「個（individual）」が 「誕生（birth）」する 前の 「あらゆる 可能性」が 「液体状（liquid）」で 「混ざり合い（mixed）」 守られている 聖なる 「孵化場（hatchery）」)",
        "thinking": "目に見える 形 を規定する 前の、パターンや 規則性が 渦巻いている（ヴォルテックス）、根源的な 情報の 海. 語源は「母体、子宮、繁殖する動物」. それは 拘束 ではなく 私たちが 宇宙という 巨大な 意志から 産み分けられた 聖なる「履歴」の 表現であり 私たちが 常に 全体（マザー）と 繋がっていることの 証明です.",
        "aftertaste": "根源の揺りかご. 独りで 戦っていると 絶望しないで. あなたの 根底には「マトリックス（母体）」としての 宇宙の 無限の 智慧が 常に 流れており 必要と あらば いつでも あなたに 必要な 力と 導きを 与えてくれるのだから.",
        "example": "The researcher studied the complex matrix of environmental factors that influenced the migration of the birds.",
        "deep_dive": { "roots": [{"term": "mater-", "meaning": "mother"}], "points": ["maternal（母方の）や matter（物質：母なる素材）と同じ。形を 産み出す 究極の 慈愛。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "primordial_origin",
        "word": "Primordial",
        "meaning": "原始の、最初の、根本的な、(生物)原生の",
        "era": "14th Century Latin primus + ordiri",
        "etymology": {
            "components": ["primus (first)", "ordiri (to begin)"],
            "original_statement": "From Late Latin primordialis (first of all, original), from Latin primordium (the beginning, origin), from primus (first) + ordiri (to begin a web, begin)."
        },
        "concept": "First weaving (「無秩序（chaos）」の 闇の中に 「最初（first）」の 「秩序の糸（thread of order）」が 「織り込まれた（woven）」 聖なる 「瞬間の 輝き」)",
        "thinking": "歴史や 文明による 装飾 を剥ぎ取った 剥き出し（ネイキッド）の、純粋で 暴力的なまでに 強大な 生命の エネルギーそのもの. 語源は「最初の、織り始めること」. それは 古臭さ ではなく 私たちが どんな時も 立ち返ることができる、汚されることのない 聖なる「野生」と「真実」の 表現です. 根源は、叫びです.",
        "aftertaste": "純粋な叫び. 社会の 枠組みに 囚われ（とらわれ） 自画像が 歪んで 見えても 迷わないで. あなたの 魂の 深奥に 眠る「プライモーディアル（根源的な）」な 輝きは 宇宙が 誕生した 瞬間の 熱量を そのまま 今も 宿しているのだから.",
        "example": "The geologists discovered primordial rocks that dated back to the very early stages of the planet's formation.",
        "deep_dive": { "roots": [{"term": "per-", "meaning": "forward, first (for primus)"}, {"term": "ar-", "meaning": "to fit, join (for ordiri)"}], "points": ["order（秩序：織物の整列）や primal（原始の）と同じ。宇宙を 織り上げる 最初の 手順。"] },
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
        print(f"Success: Added {added} words in Cycle 168.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
