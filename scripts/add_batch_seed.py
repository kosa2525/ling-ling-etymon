import json
import re

word_batch = [
    # Cycle 133: Seed & Potential
    {
        "id": "seminal_seed",
        "word": "Seminal",
        "meaning": "独創的な、重大な影響を与える、根源的な、種子の",
        "era": "16th Century Latin semen",
        "etymology": {
            "components": ["semen (seed, sprout)"],
            "original_statement": "From Latin seminalis (of or belonging to seed), from semen (seed, sprout, race, lineage)."
        },
        "concept": "Of the seed (「種（seed）」の中に 宿る 「爆発的な（explosive）」 生命の 可能性)",
        "thinking": "その後の全ての歴史を 変えうるような 根源的な アイデアや 発見の 眩（まばゆ）い 萌芽. 語源は「種子の」. それは 物理的な大きさは小さくても 他の全ての事象を 規定し、生み出していくという 圧倒的な「始まりの力」を 象徴しています. あなたの小さき一歩が 世界の形を変えるのです.",
        "aftertaste": "始まりの衝撃. あなたの中に 密かに芽生えた その小さな「セミナル（根源的）」な予感を 決して 侮（あなど）らないで. それは やがて時代を動かす 巨大な大樹になるための 聖なる種火なのだから.",
        "example": "His seminal work on linguistics changed how we understand the evolution of human language.",
        "deep_dive": { "roots": [{"term": "se-", "meaning": "to sow"}], "points": ["season（季節：種まきの時）や nursery（保育園：育てる場所）と同じ。生命の播種。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "germinate_seed",
        "word": "Germinate",
        "meaning": "芽生える、成長を始める、(考えなどが)生まれる",
        "era": "16th Century Latin germen",
        "etymology": {
            "components": ["germen (sprout, bud, germ)"],
            "original_statement": "From Latin germinatus, past participle of germinare (to sprout, bud, germinate), from germen (sprout, bud, germ)."
        },
        "concept": "To put forth sprouts (長い 「潜伏期間（dormancy）」を 終え 土を突き破る 「生命の意志（will）」)",
        "thinking": "長い忍耐の末に 蓄積されたエネルギーが 内側から限界を突き破り ついに「目に見える形」へと 移行する 決断の瞬間. 語源は「芽吹く」. それは 植物だけでなく 誰かの心の中で 静かに温められてきた夢が 現実という土壌に 参入していく 勇敢なアクションです.",
        "aftertaste": "芽吹きの鼓動. 停滞しているように見えても 水面下では 確かな成長（ジャーミネーション）が 続いている. 準備が整えば あなたは必ず 太陽に向かって その手を 伸ばすことができるのだから.",
        "example": "The idea for her startup began to germinate during a long conversation with her mentor.",
        "deep_dive": { "roots": [{"term": "gen-", "meaning": "to produce, give birth to"}], "points": ["gene（遺伝子）や genius（天才：産む力）と同じ。内在する創造性。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "prolific_seed",
        "word": "Prolific",
        "meaning": "多作の、多産の、豊かな、実りの多い",
        "era": "17th Century Latin proles",
        "etymology": {
            "components": ["proles (offspring)", "facere (to make)"],
            "original_statement": "From Middle French prolifique, from Latin proles (offspring) + facere (to make)."
        },
        "concept": "Making offspring (惜しみない 「情熱（passion）」を 「注ぎ続ける（pour out）」 ことで 豊かな 「実り（fruit）」を 生むこと)",
        "thinking": "出し惜しみをせず 自らの内なるリソースを 次々と 形（作品や結果）に変えていく 溢れんばかりの 生命の横溢（おういつ）. 語源は「子をなす」. それは 完璧主義という名の 呪縛を捨て去り 多様であること、豊かであることを 全身で謳歌する 逞しい創造の状態です.",
        "aftertaste": "豊穣の祝祭. 失敗を恐れず 数多くの種（トライ）を 蒔き続けてごらん. その「プロリフィック（多作）」な活動の中から 誰の目にも 輝かしい奇跡が 必ず 生まれてくるのだから.",
        "example": "Isaac Asimov was an incredibly prolific writer, publishing over 500 books during his career.",
        "deep_dive": { "roots": [{"term": "al-", "meaning": "to grow, nourish (possible for proles)"}], "points": ["adult（大人：成長したもの）や alimony（扶養料：養うもの）と同じ。生命の拡大。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "burgeon_seed",
        "word": "Burgeon",
        "meaning": "急成長する、芽吹く、急速に広がる",
        "era": "14th Century Old French burjon",
        "etymology": {
            "components": ["burjon (bud, sprout)"],
            "original_statement": "From Old French burjoner (to bud, sprout), from burjon (a bud, shoot, sprout)."
        },
        "concept": "To put forth buds (「蕾（bud）」が 勢いよく 「膨らみ（swell）」 爆発的に 「拡大（expand）」 していくこと)",
        "thinking": "昨日までの風景を一変させるような 勢いのある成長と 可能性の連鎖反応. 語源は「蕾」. それは 一箇所の芽吹きが 合図（シグナル）となり 全ての命が一斉に 目覚め出すような 生命の壮大な シンフォニーの 開始地点を 指します. 変化は 止められません.",
        "aftertaste": "急成長の予感. あなたの周りで 今 まさに始まりつつある その「広がり（バジョン）」を 信じて身を委ねよう. それは あなたを想像もしなかった 遥かなる地平へと 運んでいくのだから.",
        "example": "The burgeoning online education market has completely transformed how people learn new skills.",
        "deep_dive": { "roots": [{"term": "bhreu-", "meaning": "to swell, sprout"}], "points": ["breast（胸）や bud（蕾）と同じ。内側から盛り上がる、圧倒的な生命の力感。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "spawn_seed",
        "word": "Spawn",
        "meaning": "産卵する、(大量に)生み出す、〜の原因となる",
        "era": "15th Century Latin ex- + pandere",
        "etymology": {
            "components": ["ex- (out)", "pandere (to spread, extend)"],
            "original_statement": "From Old French espandre (to spread out, expand), from Latin expandere, from ex- (out) + pandere (to spread)."
        },
        "concept": "Spreading out (「内（in）」に 溜めた エネルギーを 「外（out）」へと 「一気に放つ（release）」 荒々しい 生成)",
        "thinking": "一つ一つの洗練（洗練）よりも 圧倒的な「数（ボリューム）」と「生命力」によって 世界を 自分の色に 塗り替えていく 原始的な衝動. 語源は「広げる」. それは 時には 制御不能な 混沌を 生みますが 同時に 新しい時代を 形作るための 沃土（あぶら）を 提供する 聖なる生成です.",
        "aftertaste": "生成の濁流. あなたという存在が放つ その「生（スポーン）」の エネルギーを 枯らさないで. 溢れ出す情熱こそが 未だ見ぬ世界を 創造するための 唯一無二の 源泉なのだから.",
        "example": "The cult film's unexpected success helped to spawn a whole new genre of indie horror movies.",
        "deep_dive": { "roots": [{"term": "pete-", "meaning": "to spread"}], "points": ["expand（拡大する）や fathom（深さを測る：両手を広げる）と同じ。拡散と充満。"] },
        "part_of_speech": "verb"
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
        print(f"Success: Added {added} words in Cycle 133.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
