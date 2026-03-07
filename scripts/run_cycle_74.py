import json
import re

# Theme: The Alchemy of Verity & Axiom (Cycle 74)
words_data = [
    ("verity", "Verity", "真実、真理、至言", "14th Century", "veritas (truth)", "A true principle or belief, especially one of fundamental importance", "宇宙の（。全記憶を（。一（。つ（。の（。言葉に（。凝縮（。させた「真（。実（。ヴェリタス）』。（。それは（。、揺（。る（。ぎ（。な（。い（。一点（。の（。光（。として、あなた（。の（。魂を（。、永遠（。に（。、導（。き（。続け（。る（。のですよ。"),
    ("axiom", "Axiom", "自明の理、公理、アクシオン", "15th Century", "axios (worthy, literal: 'that which is thought worthy')", "A statement or proposition which is regarded as being established, accepted, or self-evidently true", "証明（。を（。必（。要（。と（。し（。な（。い（。ほどに「価値（。アクシオ）の（。ある（。）」土台（。。（。その（。峻（。烈（。な（。る（。一点（。を（。出発点（。に（。し（。て（。、全（。ての（。知性（。の（。伽（。藍（。は（。、誇（。り（。高く（。、建（。ち（。上がる（。のです。"),
    ("postulate", "Postulate", "仮定、自明のこととして仮定する、ポスチュレート", "16th Century", "postulare (to demand, literal: 'to request')", "Suggest or assume the existence, fact, or truth of something as a basis for reasoning, discussion, or belief", "真理に（。至る（。ために、まず「要（。件を（。求（。め（。る（。ポスチュル）」こと（。。（。その（。謙虚（。な（。る（。一歩（。が（。、未だ（。見（。ぬ（。世界（。への（。扉（。を（。、静（。か（。に（。、叩（。き（。開ける（。のですよ。"),
    ("doctrine", "Doctrine", "教義、主義、ドクトリン", "14th Century", "docere (to teach)", "A belief or set of beliefs held and taught by a church, political party, or other group", "長（。い（。時間を（。かけて（。、「教（。え（。説（。か（。れた（。ドクトリ）」真理の（。体（。系（。（。その（。峻（。烈（。な（。る（。羅針盤（。が（。、あなた（。の（。エナジーを、正しい（。高みへと（。、導いて（。くれる（。のですよ。"),
    ("dogma", "Dogma", "独断、教義、ドグマ", "16th Century", "dokein (to seem, literal: 'that which seems true')", "A principle or set of principles laid down by an authority as incontrovertibly true", "「正しい（。ドケ）と（。思（。わ（。れる（。）」、峻（。烈（。な（。る（。断定（。（。たとえ（。世界が（。否定（。し（。て（。も（。、その（。一（。点（。を（。信じ（。抜く（。ことは（。、時に（。、至高の（。る（。力（。を、産む（。のですよ。"),
    ("ideology", "Ideology", "イデオロギー、観念形態", "18th Century", "idea (form) + logos (word)", "A system of ideas and ideals, especially one which forms the basis of economic or political theory and policy", "思考の（。断片を「言葉（。ロゴス）という（。名のかたち（。イデア）に（。）」編（。み（。上げ（。た（。もの（。。（。その（。見えない（。眼鏡（。を（。通して（。、あなた（。は（。、今日（。の（。世界（。を（。、再（。定義（。する（。のですよ。"),
    ("paradigm", "Paradigm", "パラダイム、枠組み、模範", "15th Century", "para- (beside) + deiknunai (to show, literal: 'showing beside')", "A typical example or pattern of something; a model", "世界を「横（。側（。パラ）から（。指（。し（。し（。め（。す（。ダイグマ）」、巨大な（。る（。枠組み（。（。その（。枠（。が（。一（。瞬（。にして（。崩（。れ（。去（。る（。とき（。、新（。しい（。宇宙が（。、静（。か（。に（。、産声を（。上げ（。ます。"),
    ("theory", "Theory", "理論、説、セオリー", "16th Century", "theoros (spectator, literal: 'viewing')", "A supposition or a system of ideas intended to explain something", "ただの（。観測（。を（。越え（。、世界（。を「観（。客（。テオ）として（。視（。る（。）」ための（。、美し（。い（。幾何（。学。（。その（。論理の（。翼が（。、あなた（。を、真理（。の（。彼方へ（。と（。運（。んで（。いく（。のです。"),
    ("hypothesis", "Hypothesis", "仮説、ハイポセシス", "16th Century", "hupo- (under) + tithenai (to place, literal: 'placing under')", "A supposition or proposed explanation made on the basis of limited evidence as a starting point for further investigation", "真理の（。重みを（。支える（。ために、「下（。側（。ハイポ）に（。置（。かれた（。セシス）」、危（。う（。い（。る（。仮（。定（。（。その（。不安定（。な（。る（。一点（。が（。、いつか（。、巨大（。な（。山（。を（。、動か（。す（。のですよ。"),
    ("premise", "Premise", "前提、根拠、プレミス", "14th Century", "prae- (before) + mittere (to send, literal: 'sent before')", "A previous statement or proposition from which another is inferred or follows as a conclusion", "思考を（。始める（。前に、あらかじめ「前（。へへと（。プレ）送（。り（。ださ（。れた（。ミス）」、峻（。烈（。な（。る（。土台（。（。その（。静（。かな（。る（。起点（。に、意味（。の（。全（。てが（。、宿ります。"),
    ("corollary", "Corollary", "系（。けい（。）」、当然の結果、コロラリー", "14th Century", "corollarium (gift, literal: 'money for a small wreath')", "A proposition that follows from (and is often appended to) one already proved", "巨大な（。る（。真理に（。、そっと（。添え（。られた「小（。さな（。花冠（。コロラ）という（。名の（。贈り物』。（。その（。当然の（。る（。結末の中に（。、美（。し（。い（。調和（。が（。満た（。さ（。れて（。いる（。のですよ。"),
    ("lemma", "Lemma", "補題（。ほだい（。）」、レマ、前提", "16th Century", "lambanein (to take, literal: 'something taken')", "A subsidiary proposition derived from another and used in a proof", "真理（。への（。旅路で、「そっと（。受け（。取（。った（。レンマ）」、小（。さな（。る（。真実（。。（。その（。一（。つ（。一（。つ（。が（。、やがて（。、巨大（。な（。証明（。へと（。、繋（。が（。っ（。て（。いく（。のですよ。"),
    ("theorem", "Theorem", "定理、セオレム", "16th Century", "theorema (spectacle, literal: 'that which is looked at')", "A general proposition not self-evident but proved by a chain of reasoning; a truth established by means of accepted truths", "知性（。が（。究（。め（。た「至高の（。光景（。テオレマ）』。（。誰（。にも（。汚（。さ（。れ（。な（。い（。、その（。永遠（。の（。幾何（。学に（。、宇宙の（。設計図が（。、刻ま（。れて（。いる（。のです。"),
    ("testimony", "Testimony", "証言、証拠、テスティモニー", "14th Century", "testis (witness)", "A formal written or spoken statement, especially one given in a court of law", "自（。らが（。、その（。瞬間（。「証人（。テスティ）として（。そこに（。いた（。）」、烈（。し（。い（。魂の（。言葉（。（。あなた（。の（。沈黙（。を（。破る（。その（。声が（。、真実（。を（。、永遠へと（。刻む（。のです。"),
    ("oath", "Oath", "誓い、宣誓、オース", "Old English", "āth (oath)", "A solemn promise, often invoking a divine witness, regarding one's future action or behavior", "沈黙という（。名の（。檻を（。破り（。、ただ（。一（。つ（。の「言葉（。オース）』に（。身を（。委（。ね（。る（。こと（。。（。その（。誓（。い（。が（。、あなた（。を（。、不（。可能（。を（。可能（。に（。する（。場所へと（。、誘（。い（。ます。")
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
            word_id = f"{word_text.lower()}_truth"
            
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
                    "concept": (item[5] + f" ({item[6]})") if len(item) > 6 else item[5],
                    "thinking": item[6] if len(item) > 6 else "真理とは、発見するものではなく、自らの魂を削って、そこに刻み込んでいく行為そのものなのです。",
                    "aftertaste": item[7] if len(item) > 7 else "公理は、疑うことをやめた場所にあるのではありません。信じ抜くことを決意した、峻烈なる一点にあるのですよ。",
                    "example": f"The scientific community accepted the new {word_text} after rigorous peer review and extensive replication experiments.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["証明とは、他者を説得することではなく、自らの内なる宇宙との対話を、究極まで突き詰めることなのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["veritable", "axiomatic", "dogmatic", "theoretical", "hypothetical"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Verity & Axiom (Cycle 74).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
