import json
import re

words_data = [
    ("say", "Say", "言う", "Old English", "secgan (to say, speak)", "Utter words so as to convey information, an opinion, a feeling or intention, or an instruction", "自分の内にある情報を、特定の人間ではなく「世界という空間に向けてポツリとただ解放」する最も普遍的でプレーンな音声の提示。", "誰に宛てるでもなく「セイ（言う）」した独り言こそが、嘘偽りのない一番の本音だったりします。"),
    ("tell", "Tell", "話す、伝える", "Old English", "tellan (to calculate, count, narrate)", "Communicate information, facts, or news to someone in spoken or written words", "もともと「数える」という意味のように、自分が持っている情報を明確な「受信者としての相手」を選び、正確に一つ一つ渡し切る確実な配達。", "彼に「テル（伝える）」する時は、回りくどい言い回しよりも、事実を数えるように真っ直ぐ言葉を投げて。"),
    ("speak", "Speak", "話す、声を出す", "Old English", "specan (to speak)", "Say something in order to convey information, an opinion, or a feeling", "会話のキャッチボールよりも、声帯を震わせて「言語を発声する」という行為そのもの、あるいはある特定の言語能力のシステムを使用すること自体。", "彼女が人前で堂々と全開で「スピーク（発言する）」した時、その熱量だけで会議の空気は完全に変わりました。"),
    ("talk", "Talk", "話す、会話する", "13th Century", "tale (tale)", "Speak in order to give information or express ideas or feelings", "一方的な伝達ではなく、相手の目を見て、互いの言葉のパスを交換し合いながら、意味や関係性を「共に形作っていく」カジュアルで最も美しい人間的交流。", "ただ情報を報告するのではなく、二人でコーヒーを飲みながらじっくり「トーク（語り合う）」したいのです。"),
    ("chat", "Chat", "おしゃべりする", "15th Century", "chateren (to chatter)", "Talk in a friendly and informal way", "重要な議題や結論など一切目的とせず、ただ言語を用いた「音の触れ合い」を楽しむことで、お互いの存在を確認し合う小鳥のような安全確認。", "結論の出ない「チャット（雑談）」を心から楽しめる相手なら、一生の友になれると信じています。"),
    ("whisper", "Whisper", "ささやく", "Old English", "hwisprian (to murmur)", "Speak very softly using one's breath without one's vocal cords", "声帯の振動を故意に消し、「息の漏れる音だけで」意味を紡ぐことで、あなたと私以外の全世界を蚊帳の外へと閉め出す究極の親密な排除。", "秘密を「ウィスパー（囁く）」する時のあなたの声は、どんな美しい音楽よりも残酷に私の心を捕らえます。"),
    ("mutter", "Mutter", "つぶやく、愚痴を言う", "14th Century", "moteren (to mutter)", "Say something in a low or barely audible voice, especially in dissatisfaction or irritation", "言葉が外界へと完全に飛び立つことを恐れ（または拒絶し）、口の中だけで「もぐもぐと不発のまま」燻らせる、行き場のない不満のガス。", "誰にも聞こえないように「マター（ブツブツ文句を言う）」くらいなら、思い切って海に向かって叫んできなさい。"),
    ("mumble", "Mumble", "もごもご言う", "14th Century", "momelan (to mumble)", "Say something indistinctly and quietly", "意志の弱さや恥ずかしさから、唇と舌による言語の彫刻を怠り、「形を持たない粘土のような音」だけを曖昧に口からこぼし落とすこと。", "自信のなさを「マンブル（もごもご言う）」することでごまかさず、下手でもいいから大きな声でハッキリと！"),
    ("shout", "Shout", "叫ぶ", "14th Century", "schouten (to prompt)", "Say something very loudly", "届かない距離、あるいは聞こえないふりをする厚い壁を強行突破するため、声帯に限界の圧力をかけて放たれる「音の砲弾」。", "怒りで「シャウト（怒鳴り散らす）」したくなったら、10秒だけ目を閉じて深呼吸。大抵はそれだけで消える炎です。"),
    ("scream", "Scream", "悲鳴を上げる", "12th Century", "screamen (to cry out)", "Give a long, loud, piercing cry or cries expressing emotion or pain", "理性による言語化というプロセスを完全にバイパスし、恐怖や激烈な痛みが直接「喉から引き裂くように飛び出してくる」原初の生命のSOS。", "ローラーコースターでの「スクリーム（絶叫）」は、大人が合法的にパニックを楽しめる最高のストレス発散法です。"),
    ("yell", "Yell", "大声を出す、叫ぶ", "Old English", "giellan (to sound, shout)", "A loud, sharp cry, especially of pain, surprise, or delight", "遠くの相手の注意を物理的に強制して引きつけるため、あるいはスポーツなどで熱狂的な感情を応援に乗せて「鋭く鋭角的に飛ばす」意志の矢。", "彼が応援席から「イェル（大声でエールを送る）」してくれたから、私は最後のカーブを全速力で曲がり切れました。")
]

words = []
for item in words_data:
    meaning1 = "known origin"
    root1 = item[4]
    w = {
        "id": f"{item[0]}_speech",
        "word": item[0],
        "meaning": item[2],
        "era": item[3],
        "etymology": {
            "components": [item[4]],
            "original_statement": f"From {item[3]} {item[4]}."
        },
        "concept": item[5] + f" ({item[6]})",
        "thinking": item[6],
        "aftertaste": item[7] if len(item) > 7 else "言葉は、発声の手段で意味が変化します。",
        "example": f"Please {item[0]} loudly.",
        "deep_dive": {
            "roots": [{"term": root1, "meaning": meaning1}],
            "points": ["発話の形式は、相手との関係性の現れ。"]
        },
        "part_of_speech": "verb"
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
    print(f"Success: Added {added} words. Theme: Speech (Cycle 20).")
else:
    print("Error parsing data.js")
