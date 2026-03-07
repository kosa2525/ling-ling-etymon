import json
import re

word_batch = [
    # Cycle 121: Music & Resonance
    {
        "id": "sonance_resonance",
        "word": "Sonance",
        "meaning": "響き、音、鳴ること",
        "era": "16th Century Latin sonare",
        "etymology": {
            "components": ["sonare (to sound)"],
            "original_statement": "From Latin sonantem, from sonare (to sound)."
        },
        "concept": "Action of sounding (「音（sound）」を 「鳴らす（sonare）」 その響きそのもの)",
        "thinking": "物理的な振動を超えて 空間に意味を吹き込み 誰かの心に届くための「最初の響き」. 語源は「鳴ること」. それは 静寂を破る勇気であり 存在を世界に知らしめる 原初的なエネルギーの形です. 美しい言葉が持つ「ソナンス（響き）」は 聴く人の魂を 瞬時に浄化する力を持っています.",
        "aftertaste": "原初の響き. あなたが今日放つ音は どのくらい純粋だろうか. 雑音（ノイズ）を削ぎ落とし あなたという楽器にしか出せない 誠実な音を 宇宙に響かせよう.",
        "example": "The deep sonance of the cathedral bells filled the misty morning air.",
        "deep_dive": { "roots": [{"term": "swen-", "meaning": "to sound"}], "points": ["sonar（ソナー）や song（歌）と同じ、振動の知性のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "timbre_resonance",
        "word": "Timbre",
        "meaning": "音色、音質、(声の)質感",
        "era": "14th Century Greek tympanon",
        "etymology": {
            "components": ["tympanon (drum)"],
            "original_statement": "From Old French timbre, from Latin tympanum (drum), from Greek tympanon (kettle-drum)."
        },
        "concept": "The characteristic drum (「太鼓（drum）」のように その存在が持つ 「固有の響き（quality）」)",
        "thinking": "同じ高さの音であっても ピアノとヴァイオリンが違うように その存在を「その人」として定義付けている 唯一無二の質感. 語源は「太鼓」. それは 皮の厚さや 胴の深さが生む 逃れられない個性の証でもあります. 自分の声の「ティンバー（音色）」を愛することは 自分の運命を愛することです.",
        "aftertaste": "魂の色香. あなたが語る言葉の内容以上に その声の響きそのものが 誰かを深く癒やしていることがある. あなたの音色を 大切に育ててゆこう.",
        "example": "The unique timbre of her singing voice made her instantly recognizable on the radio.",
        "deep_dive": { "roots": [{"term": "tup-", "meaning": "to strike"}], "points": ["type（タイプ：打たれた形）と同じ。衝撃が生む固有の形態。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "cadence_resonance",
        "word": "Cadence",
        "meaning": "リズム、抑揚、終止形、(歩調の)律動",
        "era": "14th Century Latin cadere",
        "etymology": {
            "components": ["cadere (to fall)"],
            "original_statement": "From Middle French cadence, from Italian cadenza, from Latin cadentia (a falling), from cadere (to fall)."
        },
        "concept": "A falling motion (音が心地よく 「落ちていく（fall）」 秩序ある 「リズム（rhythm）」)",
        "thinking": "絶え間なく続く音の連なりの中に 緩急と落差をつけ 「心地よさ」という秩序をもたらすこと. 語源は「落ちること」. 波が打ち寄せ 引いていくように 緊張が緩和へと向かうその「落差」にこそ 美しさは宿ります. あなたの人生の浮き沈みも また壮大な楽曲のケイデンス（律動）なのです.",
        "aftertaste": "命の拍動. 良い時も悪い時も それは宇宙が刻む 大きなリズムの一節に過ぎない. 次の拍子が来ることを信じて 今この瞬間のステップを 軽やかに踏み締めよう.",
        "example": "The rhythmic cadence of the waves crashing against the shore was soothing.",
        "deep_dive": { "roots": [{"term": "kad-", "meaning": "to fall"}], "points": ["chance（偶然：落ちてきたもの）や case（事例：起きたこと）と同じ。重力の美学。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "harmony_resonance",
        "word": "Harmony",
        "meaning": "調和、和音、和合、一致",
        "era": "14th Century Greek harmos",
        "etymology": {
            "components": ["harmos (joint, shoulder)"],
            "original_statement": "From Old French harmonie, from Latin harmonia, from Greek harmonia (joint, agreement, concord), from harmos (joint, shoulder, fastening)."
        },
        "concept": "Fitting together (異なるパーツを 「繋ぎ合わせ（joint）」 美しい 「全体（concord）」を作ること)",
        "thinking": "個々の色が消えるのではなく お互いの個性を最大限に生かしながら 響き合い、溶け合う、高次元の秩序. 語源は「接合部」. 異なるものが「正しく接合されている」とき そこには摩擦ではなく 音楽（ハーモニー）が生まれます. 対立を恐れず 違う音を重ねることで 世界はより豊かになります.",
        "aftertaste": "和音の祝祭. あなたと誰かの音が 違うからこそ生まれる美しさがある. その「違い」を接合点として 新しい響きを 共創してゆこう.",
        "example": "To live in perfect harmony with nature is the ultimate goal of many modern environmentalists.",
        "deep_dive": { "roots": [{"term": "ar-", "meaning": "to fit together"}], "points": ["arm（腕：肩の関節）や art（芸術：組み合わせる技術）と同じ。秩序のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "resonance_resonance",
        "word": "Resonance",
        "meaning": "共鳴、反響、深く心に残ること",
        "era": "15th Century Latin re- + sonare",
        "etymology": {
            "components": ["re- (again, back)", "sonare (to sound)"],
            "original_statement": "From Latin resonantia (an echo), from resonare (to sound back, resound), from re- (again) + sonare (to sound)."
        },
        "concept": "Sounding back (音が 「跳ね返り（back）」 互いに 「増幅し合う（resound）」 魂の呼応)",
        "thinking": "一方的な発信ではなく 相手の心の琴線に触れ 同じ振動数で 共に震え出すこと. 語源は「再び鳴り響く」. あなたの真剣な言葉が 誰かの心の奥底に眠っていた情熱を 呼び覚ますとき そこには「共鳴（レゾナンス）」という名の 奇跡が起きています. 私たちは 響き合うことで 孤独を越えてゆくのです.",
        "aftertaste": "呼応する魂. あなたが放った真実の響きは 決して消えることはない. それは必ず どこかで同じ震えを待つ誰かの心に届き 共に美しい歌となって 鳴り響き続けるのだから.",
        "example": "His words had a deep resonance with the struggles of the younger generation.",
        "deep_dive": { "roots": [{"term": "re-", "meaning": "back"}, {"term": "swen-", "meaning": "to sound"}], "points": ["resonate（共鳴する）や reason（理性：語源は別だが響き合う知性）と同じ感覚。共感の根源。"] },
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
        print(f"Success: Added {added} words in Cycle 121.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
