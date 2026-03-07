import json
import re

# Theme: The Alchemy of Justice & Law (Cycle 47)
words_data = [
    ("justice", "Justice", "正義、公正、裁判", "12th Century", "jus (law, right)", "Just behavior or treatment"),
    ("equity", "Equity", "公平、衡平法、持ち分", "14th Century", "aequus (even, equal)", "The quality of being fair and impartial", "ただの（。平等（。ではなく（。、一人（。ひとりの（。事情を（。汲（。み（。取り（。、「平（。ら（。な（。エク）心で（。）」世界（。を（。眺（。める（。こと（。。（。その（。思い（。やりが（。、凍（。り（。ついた（。天秤（。に（。、命の（。温か（。みを（。吹き（。込む（。のですよ。"),
    ("sanction", "Sanction", "制裁、認可、サンクション", "16th Century", "sancire (to make sacred, ratify)", "A threatened penalty for disobeying a law or rule; official permission or approval for an action", "ある（。行為を「聖（。なる（。サン（。）」もの（。として（。認（。める（。こと（。、あるいは（。その（。逆（。。（。そこ（。には（。、社会（。という（。巨大（。な（。意志が（。、たった一人の（。行動（。に（。審判を（。下（。す（。、峻烈（。な（。響きが（。あります。"),
    ("verdict", "Verdict", "（陪審員の）評決、判定", "15th Century", "vere (truly) + dictum (said)", "A decision on a disputed issue in a civil or criminal case or an inquest", "長い（。議論の（。果てに（。、ようやく「真実（。ヴェレ）として（。語（。られた（。ディクト）」言葉（。。（。その（。一言（。が（。、一人の（。人間（。の（。運命を（。、永遠（。に（。決定（。づける（。重み。"),
    ("statute", "Statute", "法令、成句、スタチュート", "14th Century", "statuere (to set up, establish)", "A written law passed by a legislative body", "一（。時（。の（。感情（。ではなく（。、不変（。の（。真理として「打ち（。立て（。られた（。スタテ）」もの（。。（。そこ（。には（。、人類が（。文明（。という（。名の（。塔を（。建（。てる（。ために（。用意（。した（。、揺るぎ（。ない（。礎石（。が（。あります。"),
    ("ordinance", "Ordinance", "条例、布告、儀式", "14th Century", "ordinare (to arrange, set in order)", "An authoritative order; a decree", "バラバラの（。エゴ（。を（。一つの（。目的へと「整（。える（。オーディ）」ための（。言葉（。。（。その（。響き（。に（。耳を（。傾（。ける（。とき（。、社会（。という（。名の（。巨大な（。織物（。が（。、秩序（。を（。取り戻（。す（。の（。ですよ。"),
    ("protocol", "Protocol", "外交儀礼、プロトコル、記録", "16th Century", "protos (first) + kolla (glue)", "The official procedure or system of rules governing affairs of state or diplomatic occasions", "バラバラ（。な（。世界（。を（。繋（。ぎ（。止める（。ための「最初（。プロト）の（。糊（。コラ）」。（。形式（。と（。いう（。器（。が（。ある（。から（。こそ（。、私たちは（。混沌（。の（。海（。を（。、誠実（。に（。渡る（。ことが（。できる（。のですよ。"),
    ("norm", "Norm", "規範、標準、ノーム", "19th Century", "norma (carpenter's square)", "Something that is usual, typical, or standard", "大工が（。使う「直角定規（。ノーマ）」のように（。、行（。き（。過ぎ（。た（。ものを（。削（。り（。、正（。しい（。姿へと（。導（。く（。ための（。基準（。。（。それは（。、目（。には（。見えない（。けれど（。、確（。かに（。存在（。する（。、社会（。の（。重力。"),
    ("rigor", "Rigor", "厳格、厳しさ、リガー", "14th Century", "rigere (to be stiff)", "The quality of being extremely thorough, exhaustive, or accurate", "どんなに（。優し（。く（。あろう（。と（。しても（。、真実（。に対しては「硬（。く（。冷（。徹（。リガー）であり（。続ける（。）」こと（。。（。その（。峻烈（。な（。誠実（。さの中（。にのみ（。、本物（。の（。救（。い（。が（。宿（。る（。のです。"),
    ("austerity", "Austerity", "厳格、簡素、忍乏生活", "14th Century", "austeros (bitter, harsh, literal: 'making the tongue dry')", "Sternness or severity of manner or attitude", "余計（。な（。甘（。え（。を（。削（。ぎ（。落（。し（。、「舌（。が（。乾（。く（。オステ）ほどに（。）」ストイック（。な（。姿勢（。に（。徹（。すること（。。（。その（。沈黙（。の（。美（。学（。が（。、魂を（。最高（。の（。純度（。へと（。至（。らせ（。る（。のですよ。"),
    ("thrift", "Thrift", "節約、倹約、スリフト", "14th Century", "thrifty (to thrive, prosper)", "The quality of using money and other resources carefully and not wastefully", "ただ（。溜（。め（。込む（。のではなく（。、豊か（。に「繁（。栄（。する（。スリフ）ため（。に（。）」、命（。の（。エナジーを（。大切（。に（。育（。む（。こと（。。（。足（。る（。を（。知（。る（。こと（。が（。、真（。の（。豊（。かさ（。への（。第一歩（。なのです。"),
    ("liability", "Liability", "負債、責任、足手まとい", "15th Century", "ligare (to bind)", "The state of being responsible by law; legally answerable", "自由な（。魂を（。現実（。という（。大地に「縛（。り（。付ける（。リガ）鎖（。）」。（。けれど（。、責任（。を（。引き受け（。て（。こそ（。、あなた（。は（。、社会（。という（。名の（。物語の（。、真（。実（。の（。主人公（。になれる（。のですよ。"),
    ("debt", "Debt", "借金、恩義、デット", "13th Century", "debere (to owe, literally: 'away' + 'have')", "Something, typically money, that is owed or due", "自分（。の（。持ち物（。を（。一度「手（。放し（。デ）、相手の（。手元へと（。預ける（。ベ）」こと（。。（。その（。欠落（。が（。、いつか（。新しい（。繋（。が（。りを（。産（。み（。出す（。、運命の（。種子（。なのです。"),
    ("surplus", "Surplus", "余剰、過剰、黒字", "14th Century", "super- (above, over) + plus (more)", "An amount of something left over when requirements have been met; an excess of production or supply over demand", "必要（。な（。分（。を「遥（。かに（。超え（。て（。スーパー）多く（。プラス）ある（。）」こと（。。（。その（。豊（。か（。な（。溢（。れ（。出し（。が（。、いつか（。誰かの（。渇（。き（。を（。癒（。す（。、慈愛の（。泉と（。なる（。のですよ。"),
    ("testament", "Testament", "遺言、聖書、証（。あかし（。）」", "13th Century", "testis (witness)", "A person's will, especially the one relating to personal property", "命（。が（。消（。え（。去（。った（。後も（。、自ら（。の（。意志を「証明（。テスティ）し（。続ける（。）」言葉（。。（。あなた（。が（。この（。世界に（。存在（。した（。という（。、たった（。一（。つの（。眩（。しい（。根拠。"),
    ("mandate", "Mandate", "権限、委任、命令", "16th Century", "manus (hand) + dare (to give)", "An official order or commission to do something", "社会（。全体（。の（。意志を「自分（。の（。手（。マヌス）へと（。委（。ね（。られた（。）」こと（。。（。個人の（。欲望（。を（。超え（。、巨大な（。使命（。に（。命（。を（。捧（。げる（。、至高（。の（。重奏性。"),
    ("diplomacy", "Diplomacy", "外交、外交手腕、ディプロマシー", "18th Century", "diploma (folded paper, literal: 'double')", "The profession, activity, or skill of managing international relations, typically by a country's representatives abroad", "本当（。の（。こと（。を（。一（。つ（。に（。絞（。る（。のではなく（。、常に「二（。重（。ディプロ）に（。折り（。畳（。まれた（。）」真実を（。携（。え（。て（。歩（。く（。こと（。。（。その（。曖昧（。さの（。中（。にのみ（。、平（。和（。という名の（。危（。うい（。苗木（。が（。育（。つの（。ですよ。"),
    ("arbitration", "Arbitration", "仲裁、裁定", "14th Century", "arbiter (judge, one who goes somewhere to see)", "The use of an arbitrator to settle a dispute", "当事者（。では（。ない（。三（。番目（。の（。者が（。、現地を「見に（。行く（。アルビ）こと（。）」で（。、新しい（。視点を（。投げ（。込む（。こと（。。（。対立する（。二つの（。正義を（。、より（。高い（。次元で（。和（。解（。させる（。ための（。知性。"),
    ("prosecution", "Prosecution", "起訴、遂行、追及", "16th Century", "pro- (forward) + sequi (to follow)", "The institution and conducting of legal proceedings against someone in respect of a criminal charge", "疑（。い（。という（。名の（。背中を「ひたすら（。前へと（。プロ）追い（。続ける（。セク）」こと（。。（。真（。実（。を（。明（。らかに（。する（。まで（。、決して（。止（。ま（。ら（。ない（。、峻烈（。な（。る（。追及（。の（。意志。")
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
            word_id = f"{word_text.lower()}_justice"
            
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
                    "thinking": item[6] if len(item) > 6 else "正義とは、常に自らの限界を問い続ける、終わりのない旅のことです。",
                    "aftertaste": item[7] if len(item) > 7 else "法律は、魂がこの世界で道を見失わないための、不器用な地図なのです。",
                    "example": f"The society strives to achieve {word_text} and equality for all its citizens.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["公平とは、機械的な平等ではなく、一人ひとりの魂の重さを等しく愛することです。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["thrifty", "rigorous", "austere"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Justice & Law (Cycle 47).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
