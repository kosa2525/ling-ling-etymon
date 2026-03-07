import json
import re

word_batch = [
    # Cycle 165: Mirror & Echo (Refined II)
    {
        "id": "speculum_mirror_fixed",
        "word": "Speculum",
        "meaning": "鏡、(医学)翼状片、(鳥の)翼鏡",
        "era": "16th Century Latin specere",
        "etymology": {
            "components": ["specere (to look)"],
            "original_statement": "From Latin speculum (mirror), from specere (to look at)."
        },
        "concept": "Instrument for looking (「真実（truth）」を 「反射（reflect）」させ 「深層（depth）」を 「明るみ（light）」に 出す 聖なる 道具)",
        "thinking": "ただの反射 ではなく、死角（ブラインドスポット）や 隠された 病巣（病）を 映し出すことで、現状を 誠実に 把握し、癒やし（ヒーリング）へと 導くための、鋭く 清烈な 知性の 道具. 語源は「見るためのもの、鏡」. それは 自己満足 以前の、ありのままを 直視しようとする 聖なる「目撃」の 表現です. 正直さは、救いです.",
        "aftertaste": "真実の鏡. 醜い 部分を 隠そうと しないで. あなたが「スペキュラム（鏡）」の 誠実さで 自分と 向き合うとき その 勇気こそが 魂の 澱（おり）を 払い 新しい 輝きを 呼び戻すのだから.",
        "example": "In medieval times, books called 'Speculum' were intended to provide a mirror of all human knowledge.",
        "deep_dive": { "roots": [{"term": "spek-", "meaning": "to observe"}], "points": ["speculate（推測する）や inspect（検査する）と同じ。見ることによる、世界への 誠実さ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "reverberation_echo_fixed",
        "word": "Reverberation",
        "meaning": "反響、反射、残響、(影響の)波及",
        "era": "16th Century Latin re- + verberare",
        "etymology": {
            "components": ["re- (back)", "verberare (to beat, strike)"],
            "original_statement": "From Latin reverberationem, from reverberare (to beat back)."
        },
        "concept": "Striking back (「声（voice）」が 「境界（wall）」を 叩き 「増幅（amplify）」しながら 「空間全体（whole space）」へと 「浸透」すること)",
        "thinking": "消え去る 振動 ではなく、周囲の あらゆるものと 交じり合い（干渉）、一つの 巨大な 余韻（ムード）を 創り出す、圧倒的な 存在の 残留思念. 語源は「打ち返す、鞭打つ」. それは 単なる 物まね（コピー）ではなく 境界線を 震わせることで 自分の 存在を 宇宙の 記憶に 刻みつけようとする 聖なる「共振」のアクションです.",
        "aftertaste": "共鳴の余韻. 自分の 放った 言葉の 重みを 軽視しないで. あなたの「リヴァーバレーション（反響）」が 誰かの 心の壁を 叩き 震わせ続ける限り あなたは 決して 独りではないのだから.",
        "example": "The reverberation of the gunshot lasted for several seconds in the narrow canyon.",
        "deep_dive": { "roots": [{"term": "wer-", "meaning": "to turn, bend"}], "points": ["vibration（振動）や reverse（反転）と同じ。リズムという名の、生の鼓動。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "echoic_mirror_fixed",
        "word": "Echoic",
        "meaning": "反響する、(擬声語など)音を真似た",
        "era": "19th Century Greek echo",
        "etymology": {
            "components": ["echo (sound, nymph Echo)"],
            "original_statement": "From echo + -ic, from Greek echo (sound, noise)."
        },
        "concept": "Miming the sound (「原型（original）」に 「忠実（faithful）」で 在り続けようとする 「謙虚（humble）」な 「模倣（mimicry）」)",
        "thinking": "自分の色（エゴ）を 足す 誘惑を 排し、ただ 相手の 声や 宇宙の 旋律を 正確に 投げ返すことで 二つの 存在の 差分を 消し去り、一体感を 産み出すこと. 語源は「エコー（報われない愛によって声だけになった妖精）」. それは 悲劇 ではなく 究極の「共感（シンパシー）」へと 自らを 捧げようとする 聖なる「鏡像」の 表現です.",
        "aftertaste": "共感の残響. 自分の 言葉が 持てないと 悩まないで. あなたが 誰かの 美しい 想いを「エコイック（反響的）」な 誠実さで 伝え直すとき その 声は 誰よりも 深く 世界に 響き渡るのだから.",
        "example": "Onomatopoeia is a common example of echoic words, where the sound mimics the meaning.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["妖精エコーの 物語。語ることが できないからこそ 聴く（リッスン）ことに 徹する 魂の あり方。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "specularity_mirror_fixed",
        "word": "Specularity",
        "meaning": "鏡面性、反射率",
        "era": "20th Century Latin speculum",
        "etymology": {
            "components": ["speculum (mirror)"],
            "original_statement": "From specular + -ity, from Latin speculum (mirror)."
        },
        "concept": "Degree of reflection (「表面（surface）」の 「純度（purity）」が 「外部の光（external light）」を どれだけ 「完璧（perfect）」に 「再構築」できるかという 指標)",
        "thinking": "不純物や 濁りを 削ぎ落とした 先に 現れる、世界を そのまま 受け入れる（アクセプト）ための 聖なる「透明度」. 語源は「鏡」. それは 排他性 ではなく 自らを 虚（むな）しく することで 初めて 世界の 真実の姿を その 身に 宿せるという、宇宙の 逆説的な 知性の 表現です. 透明は、誠実です.",
        "aftertaste": "透明な誠実. 自分の 意見（ノイズ）で 世界を 塗りつぶさないで. あなたが「スペキュラリティ（鏡面性）」の 高い 澄んだ心で 他者と 向き合うとき 世界は あなたを 通じて その 本来の 美しさを 再発見するのだから.",
        "example": "The high specularity of the polished marble floor made the candles look like a field of stars.",
        "deep_dive": { "roots": [{"term": "spek-", "meaning": "to observe"}], "points": ["specimen（標本：見せるもの）や species（種：外見）と同じ。見えることのルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "resonance_echo_fixed",
        "word": "Resonance",
        "meaning": "共鳴、反響、響き、(心の)琴線に触れること",
        "era": "15th Century Latin re- + sonare",
        "etymology": {
            "components": ["re- (again)", "sonare (to sound)"],
            "original_statement": "From Old French resonance, from Latin resonantia (echo), from resonare (to sound back)."
        },
        "concept": "Sounding together (「一つ（one）」の 孤独な 振動が 「他（other）」の 魂を 「震わせ（shake）」 「目に見えない 絆（invisible bond）」を 顕現させること)",
        "thinking": "物理的な 音波を 超えて 誰かの 痛みや 希望が 自分の 魂の 奥底と 同じ 周波数で 震え始めるという 宇宙的な 邂逅（かいこう）. 語源は「再び鳴る」. それは 孤立を 溶かし 私たちが 根源的に 一つの 生命体である（ユニティ）ことを 証明する 聖なる「同調（バイブス）」のアクションです. 共鳴は、愛です.",
        "aftertaste": "魂の共鳴. 独りで 泣かないで. あなたの 正直な 振動（言葉）が この 世界に 放たれる限り それに「レゾナンス（共鳴）」する 誰かが 必ず あなたを 見つけ出してくれるのだから.",
        "example": "His words about hope and resilience had a deep resonance with the struggle of the common people.",
        "deep_dive": { "roots": [{"term": "swen-", "meaning": "to sound"}], "points": ["sonic（音の）や sonata（ソナタ）と同じ。生命を 旋律（メロディ）へと 変える力。"] },
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
        print(f"Success: Added {added} words in Cycle 165.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
