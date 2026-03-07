import json
import re

words_data = [
    ("scorch", "Scorch", "表面を焦がす", "15th Century", "scorchen (burn superficially)", "Burn the surface of something with flame or heat", "対象の芯まで達することなく、表面の美しさや皮膚だけを炎で「薄く焼け焦がす」残虐な熱気。", "彼の「スコーチング（焼け付くような）」な嫌味は、私のプライドの表面だけをチリッと焦がしました。"),
    ("singe", "Singe", "薄く焦がす", "Old English", "sengan (to singe, burn slightly)", "Burn superficially or lightly", "炎の先がほんの一瞬だけ触れ、毛先や紙の端を黒く変色させて特有の匂いだけを残していく「いたずら」。", "髪の毛が「シンジ（少し焦げる）」程度の失敗なら、笑い話にしてしまえば良いのです。"),
    ("char", "Char", "炭にする", "17th Century", "charcoal (charring)", "Partially burn so as to blacken the surface", "生命の水分を炎の力で完全に蒸発させ、対象を燃えない黒い炭素の塊へと「変質させる」静かなる同化。", "黒く「チャー（炭化）」したバーベキューの肉も、大切な友人との楽しい思い出の味です。"),
    ("incinerate", "Incinerate", "焼却する、灰にする", "16th Century", "incinerare (to reduce to ashes)", "Destroy something by burning", "形あるものを完全に灰へと還元し、その存在そのものを跡形もなく「世界から消去」する絶対的な炎の刑。", "昔の日記を「インシネレイト（灰にする）」しても、刻まれたあなたの成長の証は残り続けます。"),
    ("conflagration", "Conflagration", "大火災", "16th Century", "con- (together) + flagrare (to blaze)", "An extensive fire which destroys a great deal of land or property", "小さな炎たちが「共に」手を結び、都市や森を飲み込んで怒り狂う、制御不能に陥った破壊する火の神。", "小さな嫉妬の火種が、やがて関係を壊す「コンフラグレーション（大火災）」になる前に。"),
    ("inferno", "Inferno", "地獄、烈火", "19th Century", "infernus (underground, hell)", "A large fire that is dangerously out of control", "この世の光景とは思えない、罪を浄化するための「地獄の底」から立ち昇るような息もできない絶望的な炎。", "夏の都会のアスファルトは、照り返しによるまるで「インフェルノ（地獄の炎）」そのものです。"),
    ("smolder", "Smolder", "くすぶる", "14th Century", "smolderen (to smother)", "Burn slowly with smoke but no flame", "炎を立てず、煙の下で自分の命をひたすら削りながら深く長く「静かに燃え続ける」執念の発熱。", "まだ解決していない「スモルダー（くすぶる）」な不満は、いずれ思いがけない発火を引き起こします。"),
    ("ignite", "Ignite", "点火する、発火する", "17th Century", "ignire (to set on fire)", "Catch fire or cause to catch fire", "暗闇と静寂の世界に、命という名の最初の一滴である熱を「与えて」燃焼のスイッチを入れる神聖な儀式。", "彼の力強い演説が、人々の眠っていた情熱に「イグナイト（点火）」の火花を散らしました。"),
    ("kindle", "Kindle", "火をつける", "12th Century", "cundel (to give birth)", "Light or set on fire", "冷たい薪に小さな熱を「産み落とし」、それが少しずつ大きな光へと育っていくのを優しく見守る母の炎。", "小さな興味に「キンドル（火を灯す）」してあげるのが、最高の教育なのかもしれません。"),
    ("extinguish", "Extinguish", "火を消す、消滅させる", "16th Century", "exstinguere (to quench)", "Cause a fire to cease to burn", "酸素や希望という生きるための糧を強制的に断ち切り、光り輝くものを決定的な「暗闇へと押し戻す」冷徹な水。", "どんなに厳しい現実も、あなたの心にある希望の火を「エクスティングイッシュ（消す）」させることはできません。")
]

words = []
for item in words_data:
    root1 = item[4].split(" ")[0]
    meaning1 = " ".join(item[4].split(" ")[1:]).strip("()")
    w = {
        "id": f"{item[0]}_fire",
        "word": item[0],
        "meaning": item[2],
        "era": item[3],
        "etymology": {
            "components": [item[4]],
            "original_statement": f"From {item[3]} {item[4]}."
        },
        "concept": item[5] + f" ({item[6]})",
        "thinking": item[6],
        "aftertaste": item[7],
        "example": f"The fire began to {item[0]} slowly.",
        "deep_dive": {
            "roots": [{"term": root1, "meaning": meaning1}],
            "points": ["炎は情熱と破壊の二面性を持つ究極のメタファー。"]
        },
        "part_of_speech": "noun" if item[0] in ["conflagration", "inferno"] else "verb"
    }
    words.append(w)

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
if match:
    prefix, json_array_str, suffix = match.groups()
    existing_words = json.loads(json_array_str)
    existing_ids = {w.get("id") for w in existing_words}
    existing_word_texts = set(w.get("word").lower() for w in existing_words)
    
    added = 0
    for w in words:
        if w["id"] not in existing_ids and w["word"].lower() not in existing_word_texts:
            existing_words.append(w)
            added += 1
            existing_word_texts.add(w["word"].lower())
            
    new_content = content[:match.start()] + prefix + json.dumps(existing_words, ensure_ascii=False, indent='\t') + suffix + content[match.end():]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Success: Added {added} words. Theme: Fire & Heat (Cycle 14).")
else:
    print("Error parsing data.js")
