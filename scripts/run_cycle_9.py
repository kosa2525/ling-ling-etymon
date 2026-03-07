import json
import re

words_data = [
    ("murmur", "Murmur", "つぶやき", "14th Century", "murmurare (mutter)", "A soft, indistinct sound made by a person or group of people speaking quietly.", "意味よりも音の連なりとして空間を満たし、深い安らぎと親密さを醸し出す水音のような声。", "小川の「マーマー（せせらぎ、ささやき）」に耳を傾ける時、私たちは宇宙の胎内に帰ります。"),
    ("babble", "Babble", "片言を言う", "13th Century", "babbelen (chatter indistinctly)", "Talk rapidly and continuously in a foolish, excited, or incomprehensible way", "赤ちゃんの口から溢れ出す、言語の形を成す前の無垢で爆発的な生命力の音。", "愛する二人の間に意味のある会話は必要なく、ただ「バブル（意味のないおしゃべり）」するだけで完璧です。"),
    ("prattle", "Prattle", "ぺちゃくちゃしゃべる", "16th Century", "prate (chatter) + -le", "Talk at length in a foolish or inconsequential way", "深い思考を放棄し、舌先だけで生み出される軽く意味のない、しかし愛嬌のある小鳥のさえずり。", "真面目な会議の最中、彼女の陽気な「プラットル（くだらないおしゃべり）」が場を救いました。"),
    ("gossip", "Gossip", "ゴシップ、噂話", "Old English", "godsibb (godparent, close friend)", "Casual conversation or reports about other people, typically involving details that are not confirmed", "もとは「神の前の親族」を意味し、親しい者同士の密愛が、やがて他者の秘密を消費する娯楽へと堕落した姿。", "他人の「ゴシップ（噂話）」で盛り上がるより、自分自身の伝説を作り上げる方に時間を使ってください。"),
    ("sermon", "Sermon", "説教", "13th Century", "sermo (discourse, talk)", "A talk on a religious or moral subject, especially one given during a church service", "高みから一方的に放たれ、魂の迷いを正そうとする権威と重みを持った言葉のシャワー。", "父親の長い「サーモン（お説教）」を嫌がっていた頃が、実は一番安全で愛されていた時代でした。"),
    ("discourse", "Discourse", "言説、談話", "14th Century", "discursus (running to and fro)", "Written or spoken communication or debate", "知性が「あちこち走り回り」、論理と論理をぶつけ合いながら高度な真実に迫ろうとする知的スポーツ。", "知的な「ディスコース（論争）」は、お互いの感情を傷つけることなく世界を深く理解するための最高の遊戯です。"),
    ("dialogue", "Dialogue", "対話", "13th Century", "dialogos (conversation)", "Conversation between two or more people as a feature of a book, play, or movie", "言葉が二つの魂の間を橋渡しし、互いの違いを認め合いながら新しい一つの合意を生み出す奇跡。", "暴力ではなく、根気強い「ダイアログ（対話）」だけが、この世界に残された最後の希望です。"),
    ("debate", "Debate", "討論、ディベート", "13th Century", "debatre (to fight)", "A formal discussion on a particular topic in a public meeting", "もとは「戦い」を意味し、武器ではなく論理と思考力を使って相手を論破しようとする現代の騎士の決闘。", "相手を打ち負かす「ディベート（議論）」の勝利に酔いしれると、大切な友人という財産を失います。"),
    ("dispute", "Dispute", "論争、紛争", "14th Century", "disputare (to estimate, dispute)", "A disagreement, argument, or debate", "意見が鋭く対立し、双方が一歩も譲らずに境界線を争う、知的な暴力のギリギリの緊張状態。", "所有権の「ディスピュート（争い）」から手を引き、ただ夕日を共有する喜びに変えられれば。"),
    ("quarrel", "Quarrel", "口論", "14th Century", "querela (complaint)", "An angry argument or disagreement", "理性を失い、傷つけるための言葉を泥玉のように投げ合う、愛情の裏返しであるみにくい感情の衝突。", "恋人との「クォーレル（口論）」の後は、いつもより深く愛し合っている自分たちに気づくはず。"),
    ("feud", "Feud", "確執、抗争", "Middle English", "fede (enmity)", "A prolonged and bitter quarrel or dispute", "代々にわたって引き継がれ、なぜ争い始めたのかさえ忘れてしまったほどの、呪いのように深い怨念の歴史。", "血を洗うような「フュード（長年の確執）」に終止符を打つのは、たった一つの許しの言葉です。")
]

words = []
for item in words_data:
    meaning1 = "known origin"
    root1 = item[4]
    w = {
        "id": f"{item[0]}_comm",
        "word": item[0],
        "meaning": item[2],
        "era": item[3],
        "etymology": {
            "components": [item[4]],
            "original_statement": f"From {item[3]} {item[4]}."
        },
        "concept": item[5] + f" ({item[6]})",
        "thinking": item[6],
        "aftertaste": item[7] if len(item) > 7 else "言葉は魂への入り口。",
        "example": f"The {item[0]} continued for a while.",
        "deep_dive": {
            "roots": [{"term": root1, "meaning": meaning1}],
            "points": ["コミュニケーションのあり方が、関係性の質を決める。"]
        },
        "part_of_speech": "noun"
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
    print(f"Success: Added {added} words. Theme: Communication (Cycle 9).")
else:
    print("Error parsing data.js")
