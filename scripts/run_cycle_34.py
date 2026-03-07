import json
import re

# Theme: The Pulse of Emotion & Spirit (Cycle 34)
words_data = [
    ("compassion", "Compassion", "慈悲、共感的な深き愛", "14th Century", "com- (together) + pati (to suffer)", "Sympathetic pity and concern for the sufferings or misfortunes of others", "相手の（。苦しみを（。遠くから（。眺める（。のではなく（。、自らも（。その（。痛みを「共に（。コン）受（。け（。パティ）止める（。）」ことで（。生まれる（。、魂の（。深い（。震（。えと（。愛の（。行動。"),
    ("equanimity", "Equanimity", "平静、落ち着き", "17th Century", "aequis (equal) + animus (mind)", "Mental calmness, composure, and evenness of temper, especially in a difficult situation", "どんなに（。周囲が（。嵐（。であっても（。、自らの「心（。アニムス）を（。常に（。平（。らな（。エクス）状態に（。）」保（。ち（。続ける（。、内なる（。静寂の（。砦。"),
    ("serenity", "Serenity", "静謐、うららかさ", "15th Century", "serenus (clear, bright)", "The state of being calm, peaceful, and untroubled", "雲一（。つ（。ない（。青空（。のように（。、「澄み（。渡った（。セレナス）」心の（。状態（。。（。一切の（。澱（。みを（。手放し（。、ただ（。光（。だけを（。反射（。して（。いる（。、魂の（。透明（。感。"),
    ("euphoria", "Euphoria", "幸福感、多幸感", "18th Century", "eu- (well) + pherein (to carry)", "A feeling or state of intense excitement and happiness", "肉体（。の（。限界を（。越え（。、魂が（。まるで「快く（。ウー）運（。ば（。フォー）れて（。いる（。）」かのような（。、浮遊（。感（。を（。伴（。った（。、圧倒的（。な（。歓喜。"),
    ("ecstasy", "Ecstasy", "無我夢中、恍惚", "14th Century", "ex- (out) + istanai (to stand)", "An overwhelming feeling of great happiness or joyful excitement", "思考（。という（。檻（。の「外（。エクス）へと（。自らを（。立た（。せる（。イスタ）」ことで（。、宇宙（。の（。巨大（。な（。エナジー（。と（。直結（。した（。瞬間の（。、眩（。い（。ばかりの（。自己喪失。"),
    ("zeal", "Zeal", "熱意、情熱", "14th Century", "zelos (ardor, jealousy, fervor)", "Great energy or enthusiasm in pursuit of a cause or an objective", "静（。かな（。確信（。の（。奥底（。で（。、青白く（。「燃（。え（。上がる（。ゼロス）」不滅（。の（。火（。。（。誰（。に（。言わ（。れる（。までも（。なく（。、自ら（。を（。焚（。き（。付け（。駆（。り（。立てる（。、生命の（。根源的（。な（。熱。"),
    ("altruism", "Altruism", "利他主義", "19th Century", "alter (other)", "The belief in or practice of disinterested and selfless concern for the well-being of others", "自己（。の（。殻を（。破り（。、常に「他者（。アルター）」の（。幸福（。を（。自らの（。喜び（。として（。感（。じ取（。ろう（。とする（。、知性の（。究極の（。洗練。"),
    ("benevolence", "Benevolence", "慈愛、博愛", "14th Century", "bene (well) + velle (to wish)", "The quality of being well meaning; kindness", "相手が（。誰（。であれ（。、ただ「良（。く（。ベネ）あれと（。願う（。ボレン）」、見返り（。を（。求め（。ない（。魂の（。放射。"),
    ("magnanimity", "Magnanimity", "度量の大きさ、寛大さ", "14th Century", "magnus (great) + animus (mind, spirit)", "Generosity in forgiving an insult or injury; free from petty resentiveness or vindictiveness", "些細（。な（。侮辱（。や（。損害（。を（。飲み込み（。、さらに（。それを（。「巨大（。な（。マグナス）精神（。アニメ）」の（。海で（。中和（。して（。しまう（。、王者の（。ような（。心の（。広さ。"),
    ("fortitude", "Fortitude", "不屈の精神、堅忍不抜", "14th Century", "fortis (strong)", "Courage in pain or adversity", "ただの（。蛮勇（。ではなく（。、嵐の（。夜（。にも（。黙々（。と（。自らの（。信じる（。正義の（。上に「強く（。フォルティス）立ち（。続ける（。）」、静かな（。覚悟。"),
    ("audacity", "Audacity", "大胆さ、厚かましさ", "15th Century", "audere (to dare)", "The willingness to take bold risks", "常識（。という（。ブレーキ（。を（。外し（。、未知（。なる（。深淵（。へと「あえて（。オード）挑（。む（。）」、若々（。しい（。魂の（。蛮勇。"),
    ("humility", "Humility", "謙虚さ", "14th Century", "humus (earth, ground)", "A modest or low view of one's own importance; humbleness", "自らを（。誇示（。せず（。、常に「大地（。ヒューマス）の（。ように（。低（。く（。）」ある（。ことで（。、世界の（。豊かさ（。を（。一滴（。残（。さず（。受け（。入れよう（。とする（。、最高の（。知性。"),
    ("modesty", "Modesty", "控えめな態度、謙虚", "16th Century", "modus (measure, limit)", "The quality or state of being unassuming or moderate in the estimation of one's abilities", "自らの（。能力を（。ひけらかさず（。、常に「正しい（。節度（。モード）の（。中に（。）」自らを（。収（。め（。て（。おく（。ことの（。できる（。、大人（。の（。余裕。"),
    ("prudence", "Prudence", "慎重、思慮分別", "14th Century", "providentia (foresight, providing for)", "The quality of being prudent; cautiousness", "目先の（。快楽（。に（。惑わされず（。、遥（。か（。先の（。未来を「あらかじめ（。プロ）見通（。し（。ヴィデ）」、今な（。すべきことを（。静かに（。選び取る（。、瞳（。の（。力。"),
    ("temperance", "Temperance", "節制、自制", "14th Century", "temperare (to mix, restrain)", "Abstinence from objective alcoholic drink", "極端（。な（。欲望（。の（。波を（。、理性という（。名の（。冷静（。な（。水で「絶妙に（。混ぜ（。合わせ（。テンパー）」、常に（。安定（。した（。中庸を（。保（。ち（。続ける（。、内なる（。調律。"),
    ("integrity", "Integrity", "誠実、完全性、統合", "14th Century", "integer (whole, untouched)", "The quality of being honest and having strong moral principles; moral uprightness", "外部（。の（。批判（。や（。誘惑（。に（。よって（。、自らの（。信念を（。断片（。（。化（。させ（。ず（。、常に「一つの（。完全（。な（。インティジャー）かたち（。）」として（。保（。ち（。続ける（。、魂の（。純粋さ。"),
    ("authenticity", "Authenticity", "本物であること、確実性", "17th Century", "authentikos (original, genuine, primary)", "The quality of being authentic", "誰（。かの（。コピー（。では（。なく（。、自らが「最初（。の（。作者（。オート）」であり（。、その（。言葉（。と（。行動が（。（。一致（。して（。いる（。という（。、揺るぎ（。ない（。自身（。の（。証拠。"),
    ("sincerity", "Sincerity", "誠実、偽りのなさ", "16th Century", "sine (without) + cera (wax)", "The quality of being free from pretense, deceit, or hypocrisy", "自らの（。欠点（。を（。隠（。す（。ための「蝋（。ワックス・セラ）を（。持（。たない（。シネ）」、傷跡（。さえも（。剥（。き（。出し（。にした（。ままの（。、清々（。しい（。告白。"),
    ("fidelity", "Fidelity", "忠誠、忠実、フィデリティ", "15th Century", "fides (faith, trust)", "Faithfulness to a person, cause, or belief, demonstrated by continuing loyalty and support", "一度（。誓（。った（。約束（。を（。、魂の（。深い（。場所で「信（。じ（。フィデ）続け（。）」、決して（。背（。か（。ない（。という（。、人格の（。最深の（。根っこ。"),
    ("devotion", "Devotion", "献身、熱愛、信仰心", "13th Century", "de- (away) + vovere (to vow)", "Love, loyalty, or enthusiasm for a person, activity, or cause", "自分（。の（。小さな（。エゴを「手放し（。デ）、捧げる（。ヴォート）」こと（。を（。通（。じて（。、自分（。よりも（。大きな（。存在と（。一体（。に（。なろうと（。する（。、愛の（。究極の（。形。"),
    ("veneration", "Veneration", "尊敬、崇拝", "15th Century", "venus (love, beauty, charm)", "Great respect; reverence", "相手の（。内側に（。ある（。聖なる「美（。ヴィーナス）」を（。見出し（。、それ（。に（。対して（。深く（。頭（。を（。下げる（。、魂の（。礼拝。"),
    ("reverence", "Reverence", "畏敬、崇敬", "14th Century", "re- (again) + vereri (to fear, respect)", "Deep respect for someone or something", "ただの（。恐怖（。では（。なく（。、その（。圧倒的（。な（。崇高（。さに（。対し（。、「何度も（。リ）畏（。れ（。ヴェレ）敬う（。）」、静寂（。に（。満ちた（。祈りの（。姿勢。"),
    ("bliss", "Bliss", "至福、無上の喜び", "Old English", "blīths (happiness, kindness, joy)", "Perfect happiness; great joy", "日常（。の（。些細（。な（。不満を（。（。全て（。消し（。去る（。、宇宙（。から（。（。の（。祝福（。。（。ただ（。存在（。して（。いる（。だけで（。、涙（。が（。出る（。ほどに（。幸福である（。という（。、原初（。の（。喜び。"),
    ("solace", "Solace", "慰め、癒し", "13th Century", "solari (to console, soothe)", "Comfort or consolation in a time of distress or sadness", "凍（。り（。ついた（。心に（。、そっと（。寄り添（。い「温め（。（。和（。ら（。げる（。ソラ）」、静（。かな（。愛の（。毛布（。）。", "あなたが（。誰（。かの（。ために（。かける（。、ただ一言（。の（。言葉。"),
    ("ataraxy", "Ataraxy", "アタラクシア、心の平穏", "17th Century", "a- (not) + tarassein (to disturb)", "A state of freedom from emotional disturbance and anxiety", "感情（。の（。波風を「かき（。乱（。される（。タラッ）ことのない（。ア）」、完全（。なる（。内面の（。静寂（。。（。知性（。による（。、運命（。への（。静かなる（。勝利。"),
    ("eudaemonia", "Eudaemonia", "エウダイモニア、幸福、繁栄", "19th Century", "eu- (good) + daimon (spirit)", "A Greek word commonly translated as happiness or welfare", "単なる（。快楽（。では（。なく（。、自らの（。内なる「良（。き（。エウ）霊魂（。ダイモン）」を（。輝（。か（。せ（。、自分（。本来（。の（。使命を（。生（。き（。切って（。いる（。とき（。の（。、深い（。充足感。"),
    ("catharsis", "Catharsis", "カタルシス、浄化", "19th Century", "kathairein (to purify, cleanse)", "The process of releasing, and thereby providing relief from, strong or repressed emotions", "心の（。奥底に（。澱（。（。んで（。いた（。濁（。りを（。、劇的な（。感情の（。噴出（。によって「洗い（。流（。し（。カタル）清（。める（。）」、魂の（。洗濯。"),
    ("psyche", "Psyche", "精神、プシュケ、魂", "17th Century", "psykhein (to breathe)", "The human soul, mind, or spirit", "肉体（。の（。中を（。そっと（。通り（。抜（。ける「息（。プシュケ）」のような（。、（。目（。には（。見えない（。けれど（。、そこに（。ある（。、あなた（。を（。あなた（。たらし（。めて（。いる（。中心。"),
    ("charisma", "Charisma", "カリスマ、特別な才能", "17th Century", "kharis (grace, favor, gift)", "Compelling attractiveness or charm that can inspire devotion in others", "自らの（。力（。ではなく（。、神格（。からの（。「恩寵（。カリス）」として（。授（。け（。られた（。、他者の（。魂を（。不可抗力的に（。惹き（。つけて（。しまう（。、眩（。しい（。輝き。")
]

def run_cycle():
    file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
        if not match:
            print("Error: Could not find WORDS array in data.js")
            return

        prefix, json_array_str, suffix = match.groups()
        existing_words = json.loads(json_array_str)
        existing_ids = {w.get("id") for w in existing_words}
        existing_word_texts = {w.get("word").lower() for w in existing_words}

        added_count = 0
        for item in words_data:
            word_text = item[0]
            word_id = f"{word_text.lower()}_emo"
            
            if word_id not in existing_ids and word_text.lower() not in existing_word_texts:
                new_word = {
                    "id": word_id,
                    "word": word_text,
                    "meaning": item[2],
                    "era": item[3],
                    "etymology": {
                        "components": [item[4]],
                        "original_statement": f"From {item[3]} {item[4]}."
                    },
                    "concept": item[5] + f" ({item[6]})",
                    "thinking": item[6],
                    "aftertaste": item[7] if len(item) > 7 else "心は、世界という巨大な海を渡るための、唯一の羅針盤です。",
                    "example": f"Her presence radiated a sense of absolute {word_text} that comforted everyone around her.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["感情は、魂が奏でる音楽の調べそのものです。"]
                    },
                    "part_of_speech": "noun"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Emotion & Spirit (Cycle 34).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
