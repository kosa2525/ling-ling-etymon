import json
import re

# Theme: The Pulse of Mind & Perspective (Cycle 39)
words_data = [
    ("cognition", "Cognition", "認知、認識", "15th Century", "com- (together) + gnoscere (to know)", "The mental action or process of acquiring knowledge and understanding through thought, experience, and the senses", "バラバラの（。情報や（。感覚を（。一つに「共に（。コン）知る（。グノーシス）」ことで（。、世界に（。意味という（。秩序（。を（。与（。える（。、知性の（。崇高な（。営み。"),
    ("subconscious", "Subconscious", "潜在意識、下意識", "19th Century", "sub- (under) + conscious (knowing together)", "Of or concerning the part of the mind of which one is not fully aware but which influences one's actions and feelings", "意識の（。明るい（。舞台の（。「下（。サブ）に（。潜（。り（。込（。んだ（。）」、本人（。さえ（。気づ（。かない（。、巨大な（。感情と（。記憶の（。貯蔵庫。"),
    ("bias", "Bias", "偏見、バイアス、斜め", "16th Century", "biais (slant, slope)", "Prejudice in favor of or against one thing, person, or group compared with another, often in a way considered to be unfair", "真っ直ぐに（。真実を（。見つめる（。のを（。止め（。、心が「斜（。め（。バイアス）に（。傾（。いた（。）」まま（。世界を（。眺めて（。しまう（。、知性の（。危（。うい（。歪み。"),
    ("delusion", "Delusion", "妄想、欺瞞", "14th Century", "de- (down, away) + ludere (to play)", "An idiosyncratic belief or impression that is firmly maintained despite being contradicted by what is generally accepted as reality or rational argument, typically a symptom of mental disorder", "真実との（。誠実な（。対話を（。止め（。、自分（。自身を「弄（。び（。ロード）欺（。く（。デ）」ことで（。作り（。上げた（。、孤独（。な（。幻（。の世界。"),
    ("hallucination", "Hallucination", "幻覚", "17th Century", "alucinari (to wander in mind, to dream)", "An experience involving the apparent perception of something not present", "現実の（。大地から（。足（。が（。離（。れ（。、心が「夢の（。中を（。彷徨（。い（。アルー）狂（。う（。）」こと（。。（。そこ（。には（。、本人（。に（。しか（。見えない（。、残酷（。な（。までに（。美しい（。光景（。が（。広が（。って（。いる（。のですよ。"),
    ("insight", "Insight", "洞察、インサイト", "13th Century", "in- (into) + sight", "The capacity to gain an accurate and deep intuitive understanding of a person or thing", "表面的な（。言葉の（。裏側にある（。、相手の「内（。側（。イン）の（。風景（。サイト）」を（。一瞬（。にして（。見抜（。く（。、瞳の（。知性。"),
    ("clarity", "Clarity", "明快さ、透明度", "14th Century", "clarus (clear)", "The quality of being coherent and intelligible", "迷（。いの（。霧が（。晴れ（。、精神が「澄み（。渡った（。クラルス）」状態（。。（。真実（。を（。一滴（。の（。淀（。み（。もなく（。、透明（。に（。映（。し出す（。、知性の（。最高（。の（。純度。"),
    ("vigilance", "Vigilance", "警戒、用心、不眠の守り", "17th Century", "vigil (awake, watchful)", "The action or state of keeping careful watch for possible danger or difficulties", "どんなに（。安（。ら（。ぎ（。の中に（。あっても（。、魂の（。一部が「目（。を（。覚（。まし（。ヴィジル）ている（。）」こと（。。（。大切な（。ものを（。守（。り（。抜（。くための（。、孤独（。で（。誠実（。な（。眼差し。"),
    ("mindfulness", "Mindfulness", "マインドフルネス、今ここにあること", "16th Century", "mind + -ful + -ness", "A mental state achieved by focusing one's awareness on the present moment, while calmly acknowledging and accepting one's feelings, thoughts, and bodily sensations", "過去の（。後悔（。や（。未来への（。不安（。に（。心を（。捕（。らわ（。さ（。れ（。ず（。、ただ「今（。この（。瞬間（。の（。全（。て（。マインドフル）」を（。、全（。身で（。あり（。の（。まま（。に（。受け（。入れる（。、魂の（。安息。"),
    ("contemplation", "Contemplation", "熟考、沈思、コンテンプレーション", "13th Century", "com- (together) + templum (temple, space for observation)", "The action of looking thoughtfully at something for a long time", "外部（。の（。喧騒を（。断（。ち（。切り（。、自らの（。心の中に「聖（。なる（。神殿（。テンプル）を（。共に（。コン）築く（。）」ように（。、静（。か（。に（。真理を（。見つめ（。続ける（。、祈りの（。知性。"),
    ("retrospection", "Retrospection", "回顧、追憶", "17th Century", "retro- (back) + specere (to look)", "The action of looking back on or reviewing past events or situations, especially those in one's own life", "現在（。の（。自分（。を（。一度（。止（。め（。、「過去を（。後ろ向きに（。レトロ）見つめ（。スぺ）直す（。）」こと（。。（。過ぎ（。去（。った（。出来事（。の（。中に（。、今（。を（。生きる（。ための（。知恵（。の（。欠片（。を（。探（。す（。旅。"),
    ("introspection", "Introspection", "内省、自己観察", "17th Century", "intro- (inside) + specere (to look)", "The examination or observation of one's own mental and emotional processes", "他人の（。こと（。を（。気に（。する（。のを（。止（。め（。、ひたすら「自分（。自身の（。内（。側（。イントロ）を（。見つめる（。スぺ）」こと（。。（。魂の（。鏡を（。磨（。き（。、自ら（。の（。正体に（。誠実（。に（。向き（。合う（。、勇気（。ある（。孤独。"),
    ("speculation", "Speculation", "推測、投機、思索", "14th Century", "speculum (mirror)", "The forming of a theory or conjecture without firm evidence", "確（。かな（。証拠（。が（。ない（。中で（。、心の「鏡（。スぺキュラム）」に（。映（。る（。影（。を（。頼（。りに（。、宇宙の（。真理（。を（。夢想（。し（。よう（。とする（。、知性の（。冒険。"),
    ("deduction", "Deduction", "演繹、控除、デダクション", "15th Century", "de- (down, away) + ducere (to lead)", "The inference of particular instances from a general law", "絶対的（。な（。真理から（。、一段（。ずつ（。論理を「引き（。導（。く（。ドゥ）き（。下（。ろす（。デ）」ことで（。、個別の（。事象（。を（。解（。き（。明か（。そう（。とする（。、数学的（。な（。美（。を（。持（。った（。思考の（。ステップ。"),
    ("induction", "Induction", "帰納、誘導、インダクション", "14th Century", "in- (into) + ducere (to lead)", "The inference of a general law from particular instances", "無数の（。経験（。の（。断片を（。、一つの（。普遍的（。な（。法則へと「中に（。イン）導（。き（。ドゥ）き（。入れる（。）」こと（。。（。混沌（。から（。秩序（。を（。産（。み（。出す（。、粘（。り（。強（。い（。観察の（。果ての（。飛躍。"),
    ("inference", "Inference", "推論、推定", "16th Century", "in- (into) + ferre (to bring, carry)", "A conclusion reached on the basis of evidence and reasoning", "今（。見（。えて（。いる（。事実の（。中（。イン）へと（。、新しい（。意味を「運び（。フェリー）込む（。）」こと（。。（。点（。と（。点（。を（。繋（。ぎ（。、まだ（。見（。ぬ（。真理（。の（。輪郭（。を（。描（。き（。出す（。知的な（。想像力。"),
    ("hypothesis", "Hypothesis", "仮説、ハイポセシス", "16th Century", "hupo- (under) + tithenai (to place, put)", "A supposed or proposed explanation made on the basis of limited evidence as a starting point for further investigation", "真実と（。認（。める（。前（。に（。、「暫定（。的な（。土台（。ハポ）として（。置（。かれた（。セシス）」言葉（。。（。それが（。正（。しい（。か（。を（。試（。す（。ため（。に（。、勇気（。を持って（。暗闇（。へと（。投（。げ（。入れ（。られる（。、思考（。の（。灯。"),
    ("tenet", "Tenet", "教義、信条、テネット", "16th Century", "tenere (to hold)", "A principle or belief, especially one of the main principles of a religion or philosophy", "誰（。に（。何と（。言わ（。れて（。も（。、自らの（。魂が「しっかりと（。把（。持（。して（。テネ）離（。さない（。）」絶対（。の（。確信（。。（。あなた（。を（。最後（。まで（。支（。える（。、精神の（。背骨。"),
    ("dogma", "Dogma", "独断、教義、ドグマ", "16th Century", "dokein (to seem good, think)", "A principle or set of principles laid down by an authority as incontrovertibly true", "かつて（。は「良（。き（。ドケ）こと」だと（。信（。じ（。られ（。て（。いた（。はずの（。、今では（。凝り（。固（。まって（。、自由な（。思考（。を（。阻（。む（。檻（。と（。なって（。しまった（。、冷（。たい（。正義。"),
    ("creed", "Creed", "信条、クリード", "Old English", "credo (I believe)", "A system of Christian or other religious belief; a faith", "理屈を（。超え（。、自らの「心（。コア）を（。預（。け（。る（。クレド）」という（。、魂の（。深い（。誓い（。。（。暗い（。夜を（。歩（。く（。とき（。、あなたの（。胸（。の（。奥で（。、確（。かに（。熱（。を（。放（。って（。いる（。、静（。かな（。る（。火（。種。"),
    ("conviction", "Conviction", "信念、確信、有罪判決", "15th Century", "com- (together) + vincere (to conquer)", "A firmly held belief or opinion", "迷（。いや（。恐怖（。を（。、論理（。と（。経験によって「完全に（。コン）征服（。し（。ヴィン）た（。）」果てに（。得（。られる（。、揺るぎ（。ない（。精神の（。勝利（。の（。かたち。"),
    ("skepticism", "Skepticism", "懐疑主義", "17th Century", "skepsis (inquiry, examination, reflection)", "Skeptical attitude; doubt as to the truth of something", "ただ（。何（。でも（。疑（。う（。のではなく（。、真実を（。求（。めて「入念（。に（。吟味（。し（。スケプ）調査（。する（。）」、知性の（。誠実（。な（。関門。"),
    ("resolve", "Resolve", "決意する、分解する、解決する", "14th Century", "re- (again) + solvere (to loosen, unbind)", "Settle or find a solution to (a problem, dispute, or contentious matter)", "複雑（。に（。絡（。み（。合（。った（。迷（。いを（。、一度「バラバラに（。解（。き（。放（。し（。ソルヴ）、再び（。リ）組み立て（。直す（。）」こと（。。（。そこ（。に（。一点の（。曇り（。も（。なくなった（。とき（。、あなた（。の（。中には（。、鋼（。の（。ような（。意志が（。、静（。かに（。宿（。る（。のです。"),
    ("patience", "Patience", "忍耐、ぺイシェンス", "13th Century", "pati (to suffer)", "The capacity to accept or tolerate delay, trouble, or suffering without getting angry or upset", "ただ（。耐（。える（。のではなく（。、自らの（。痛みや（。不条理を「共（。に（。引（。き（。受（。け（。パティ）味わ（。う（。）」、魂の（。知（。的な（。成熟（。。（。時（。が（。満（。ち（。る（。のを（。、微笑（。み（。ながら（。待（。てる（。、心の（。余裕。"),
    ("psyche", "Psyche", "精神、魂、プシュケ", "17th Century", "psykhein (to breathe)", "The human soul, mind, or spirit", "肉体（。という（。仮面（。の（。裏側（。で（。、そっと（。出（。入り（。する「息（。プシュケ）」のような（。存在（。。（。目（。には（。見えない（。けれど（。、あなたが（。生きて（。いる（。という（。、たった（。一つの（。眩（。しい（。根拠。")
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
            word_id = f"{word_text.lower()}_mind"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "まなざしは、世界に色を付けるための、魔法の筆です。",
                    "example": f"The philosopher explored the depths of human {word_text} and its relation to ethics.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["知性とは、暗闇の中に新しい光を見出すための、不屈の勇気のことです。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["subconscious", "momentary", "transient", "permanent", "perpetual", "immortal", "archaic", "contemporary", "sequential", "chronological", "sporadic", "intermittent", "persistent", "perennial"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Mind & Perspective (Cycle 39).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
