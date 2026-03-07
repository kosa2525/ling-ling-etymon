import json
import re

# Theme: The Pulse of Conflict & Harmony (Cycle 35)
words_data = [
    ("discord", "Discord", "不和、不協和音", "13th Century", "dis- (apart) + cor (heart)", "Lack of harmony between notes sounding together", "お互い（。の（。想いが（。、「心（。コア）から（。離（。れて（。ディス）しまった（。）」状態（。。（。響（。き（。合（。う（。ことが（。できず（。、バラバラに（。震（。えて（。いる（。、痛（。み（。を（。伴（。った（。沈黙。"),
    ("strife", "Strife", "論争、闘争、衝突", "13th Century", "estrif (discord, conflict)", "Angry or bitter disagreement over fundamental issues; conflict", "ただの（。喧嘩（。ではなく（。、自らの（。信じる（。正義のために（。、「激しく（。努力（。し（。ストライブ）戦（。う（。）」こと（。。（。避（。け（。られない（。衝突（。が（。、魂を（。研（。ぎ（。澄（。ませ（。、新しい（。真実を（。引（。き（。ず（。り（。出す（。、苦着（。な（。陣痛。"),
    ("controversy", "Controversy", "論争、物議", "14th Century", "contra- (against) + vertere (to turn)", "Disagreement, typically when prolonged, public, and heated", "相手の（。意見に（。対して（。、「反対の（。コントラ）方向へと（。言葉を（。向ける（。ヴァース）」こと（。。（。平行線（。を（。たどる（。議論（。が（。、世界（。の（。多層性（。を（。浮（。き（。彫（。りに（。する。"),
    ("defiance", "Defiance", "挑戦的態度、無視", "14th Century", "dis- (un-) + fidere (to trust)", "Open resistance; bold disobedience", "今（。までの（。信頼（。や（。ルールを（。「一度（。捨て（。ディス）去（。る（。フィ）」ことで（。、自ら（。の（。誇り（。を（。守（。ろう（。と（。する（。、孤独（。で（。峻烈（。な（。反抗。"),
    ("agitation", "Agitation", "動揺、扇動、攪拌（かくはん）", "16th Century", "agere (to drive, do, act)", "A state of anxiety or nervous excitement", "心の（。湖面に（。石を（。投（。げ（。入れ（。、「激しく（。動（。か（。し（。アグ）続ける（。）」こと（。。（。不安（。の（。中から（。、新しい（。決意（。が（。結晶（。化（。する（。直前の（。、震（。える（。混沌。"),
    ("turmoil", "Turmoil", "騒乱、混乱", "16th Century", "Origin uncertain, possibly related to tremere (to tremble)", "A state of great disturbance, confusion, or uncertainty", "秩序（。が（。崩れ（。、全てが（。予測不可能な（。うねりとなって（。、「震（。え（。トレム）狂（。って（。いる（。）」状態（。。（。古い（。建物（。（。を（。壊（。し（。、更（。地（。に（。する（。ための（。、運命の（。荒療治。"),
    ("upheaval", "Upheaval", "（地殻の）隆起、大激変", "19th Century", "up + heave (to lift)", "A violent or sudden change or disruption to something", "平穏（。な（。大地が（。、内なる（。巨大な（。エナジーによって（。、「一気（。に（。持ち（。上げ（。られる（。ヒーヴ）」こと（。。（。今（。までの（。常識（。が（。一瞬（。で（。崩れ（。去（。る（。、創造的（。な（。破壊。"),
    ("reconciliation", "Reconciliation", "和解、調和", "14th Century", "re- (again) + conciliare (to bring together)", "The restoration of friendly relations", "一度（。離（。れ（。離（。れに（。なった（。心（。を（。、再び（。一つの「場所（。議会（。コンシル）へと（。集（。め（。直（。す（。リ）」こと（。。（。傷跡（。を（。噛（。み（。締め（。ながら（。も（。、共（。に（。歩む（。こと（。を（。選（。ぶ（。、人間らしい（。勇気。"),
    ("mediation", "Mediation", "調停、仲介", "14th Century", "medius (middle)", "Intervention in a dispute in order to resolve it; arbitration", "対立（。する（。二つの（。勢力の（。「真（。ん中（。メディ）に（。立ち（。）」、お互い（。の（。怒り（。を（。言葉（。の（。橋で（。繋ぎ（。合わせ（。よう（。とする（。、知的な（。忍耐。"),
    ("arbitration", "Arbitration", "仲裁、裁定", "14th Century", "arbitrari (to judge, decide)", "The use of an arbitrator to settle a dispute", "当事者（。では（。解決（。できない（。争（。いに（。対（。し（。、公平（。な「第三者の（。意志（。アービト）によって（。決断（。を（。下（。す（。）」こと（。。（。混沌（。に（。終止符（。を（。打（。つ（。、冷徹（。な（。理性。"),
    ("negotiation", "Negotiation", "交渉", "16th Century", "neg- (not) + otium (leisure)", "Discussion aimed at reaching an agreement", "ただの（。お喋り（。ではなく（。、「安（。ら（。ぎ（。オティウム）を（。一時的に（。捨て（。ネグ）て（。）」、真剣勝負（。で（。自分（。たちの（。正義（。を（。擦（。り（。合わ（。せ（。よう（。とする（。、知的な（。格闘。"),
    ("compromise", "Compromise", "妥協、歩み寄り", "15th Century", "com- (together) + promittere (to promise)", "An agreement or a settlement of a dispute that is reached by each side making concessions", "自分（。の（。全（。ての（。主張（。を（。通（。す（。のを（。止め（。、相手（。と「共（。に（。コン）妥当な（。場所（。を（。約束（。する（。プロミス）」こと（。。（。それは（。敗北（。ではなく（。、共に（。生き残る（。ための（。賢明な（。後退。"),
    ("accord", "Accord", "一致、調和、協定", "12th Century", "ad- (to) + cor (heart)", "Give or grant someone (power, status, or recognition)", "他人（。の（。意志に（。対して（。、自らの「心（。コア）を（。寄り添（。わせ（。アド）る（。）」ことで（。生まれる（。、静かなる（。同意（。。（。言葉（。を（。超（。え（。た（。、魂の（。握手。"),
    ("treaty", "Treaty", "条約、協定", "14th Century", "trahere (to draw)", "A formally concluded and ratified agreement between countries", "激しい（。争いの（。血潮を（。拭（。い（。、未来（。のあるべき（。形を「言葉（。として（。引き（。トラ）出した（。）」、不変（。の（。契約（。。（。紙（。の（。上の（。平和（。が（。、いつか（。本物の（。安らぎに（。成（。る（。まで（。の（。、楔。"),
    ("alliance", "Alliance", "同盟、提携", "13th Century", "ad- (to) + ligare (to bind)", "A union or association formed for mutual benefit, especially between countries or organizations", "個々（。の（。脆弱（。さを（。認（。め（。、一（。つの（。目的（。に（。向（。かって「固（。く（。結（。び（。リガ）合（。わ（。された（。アド）」連帯（。。（。多様性（。を（。殺（。さ（。ず（。に（。、一つの（。力と（。成（。る（。、知的な（。武装。"),
    ("unison", "Unison", "調和、一斉に、ユニゾン", "15th Century", "unus (one) + sonus (sound)", "Simultaneous performance of action or utterance of speech", "バラバラの（。音（。が（。、一瞬（。にして「一（。つの（。ユニ）響き（。ソン）」へと（。重（。なり（。合（。う（。こと（。。（。個（。を（。捨（。てる（。のではなく（。、個（。が（。全体と（。完璧（。に（。共鳴（。して（。いる（。幸福。"),
    ("symphony", "Symphony", "交響曲、シンフォニー", "14th Century", "sun- (together) + phone (voice, sound)", "An elaborate musical composition for full orchestra, typically in four movements, at least one of which is traditionally in sonata form", "不協（。和音（。さえも（。、長大（。な（。時間の（。中で「共に（。シン）聴（。こえて（。フォン）くる（。）」、巨大（。な（。調和（。。（。宇宙（。の（。全記憶（。を（。一つの（。音楽（。へと（。昇華（。させる（。、魂の（。叙事詩。"),
    ("orchestration", "Orchestration", "管弦楽、組織化", "19th Century", "orkhestra (place for dancing)", "The planning or coordination of the elements of a situation to produce a desired effect", "ただ（。並べる（。のではなく（。、各々（。が（。最高（。の（。パフォ（。ー（。マンス（。を（。発揮（。できる「舞（。台（。を（。整える（。オーケストラ）」こと（。。（。見えない（。指揮者（。の（。眼差し（。による（。、高度（。な（。秩序の（。構築。"),
    ("equilibrium", "Equilibrium", "均衡、つり合い", "14th Century", "aequis (equal) + libra (balance, scales)", "A state in which opposing forces or influences are balanced", "激（。しく（。対立（。する（。二つの（。エナジーが（。、天上の「秤（。リブラ）の上で（。等し（。く（。エクイ）並（。ん（。だ（。）」、奇跡（。的な（。静止（。。（。揺（。れ（。ながら（。も（。、中心（。を（。決（。して（。逸（。ら（。さない（。、動的（。な（。平和。"),
    ("stability", "Stability", "安定、持続性", "13th Century", "stare (to stand)", "The state of being stable", "一（。時の（。感情（。に（。流（。され（。ず（。、大地（。の上に（。しっかりと「立ち（。スタ）続ける（。）」こと（。。（。静（。かな（。継続（。こそが（。、最も（。強力（。な（。エナジー（。を（。生み出す（。のだという（。、生命の（。証明。"),
    ("armistice", "Armistice", "休戦、停戦協定", "17th Century", "arma (arms, weapons) + sistere (to stand, stop)", "An agreement made by opposing sides in a war to stop fighting for a certain time; a truce", "銃火（。を（。交（。わす（。のを（。止（。め（。、自らの「武器（。アルマ）を（。一度（。静止（。シスト）させる（。）」儀式（。。（。真（。の（。平和（。に（。至（。る（。前（。の（。、祈り（。に（。満ち（。た（。沈黙。"),
    ("truce", "Truce", "休戦、一時的停戦", "14th Century", "treow (faith, truth, pledge)", "An agreement between enemies or opponents to stop fighting or arguing for a certain time", "今（。までの（。憎（。し（。みを（。横（。に（。置き（。、「真（。実（。トゥルー）への（。誓い（。）」を（。一時的に（。交（。わ（。す（。こと（。。（。戦いの（。荒野（。に（。咲（。く（。、小さな（。一輪の（。花（。のような（。安らぎ。"),
    ("amnesty", "Amnesty", "恩赦、大赦", "16th Century", "a- (not) + mnasthai (to remember)", "An official pardon for people who have been convicted of political offenses", "過去（。の（。罪（。や（。過ちを（。、あえて「覚（。え（。ムネ）て（。いない（。ア）」ことに（。する（。、強者の（。寛大（。な（。忘却（。。（。新しい（。歴史（。を（。始める（。ための（。、潔（。い（。リセット。"),
    ("solidarity", "Solidarity", "連帯、団結", "19th Century", "solidus (solid, whole)", "Unity or agreement of feeling or action, especially among individuals with a common interest; mutual support within a group", "個々（。が（。バラバラに（。震（。える（。のを（。止め（。、一つの「強固（。な（。ソリッド）塊」となって（。運命（。に（。立ち（。向かう（。こと（。。（。弱（。き（。者たちが（。、最大の（。勇気（。を（。手（。に入（。れる（。ための（。魔法。"),
    ("coherence", "Coherence", "一貫性、密着", "16th Century", "com- (together) + haerere (to stick)", "The quality of being logical and consistent", "言葉（。と（。行動が（。、磁石（。のように（。「共に（。コン）密着（。して（。ヘア）離れない（。）」状態（。。（。その（。ブレ（。のない（。姿勢（。が（。、周囲に（。圧倒的（。な（。信頼（。を（。産み出す。"),
    ("impact", "Impact", "衝撃、影響、衝突", "16th Century", "in- (into) + pangere (to fix, drive in)", "The action of one object coming forcibly into contact with another", "単なる（。接触（。ではなく（。、相手（。の（。内（。側（。（。イン）へと（。自らの（。意志を（。「打ち（。込（。む（。パクト）」こと（。。（。一瞬（。の（。激突（。が（。、世界（。の（。軌道（。を（。永遠（。に（。書き換（。える。"),
    ("repercussion", "Repercussion", "影響、反動、跳ね返り", "15th Century", "re- (back) + per- (through) + quatere (to shake)", "An unintended consequence occurring some time after an event or action, especially an unwelcome one", "放たれた（。衝撃（。が（。、壁（。を（。突（。き（。抜（。け（。、「再び（。リ）震（。え（。クッシュ）を（。伴（。って（。戻（。って（。くる（。）」こと（。。（。自分（。の（。投（。げ（。た（。石（。が（。、忘（。れた（。頃（。に（。大きな（。波紋（。となって（。、自ら（。を（。揺（。さぶ（。る（。こと。"),
    ("bridge", "Bridge", "橋、ブリッジ", "Old English", "brycg (bridge)", "A structure carrying a road, path, railroad, or canal across a river, ravine, road, railroad, or other obstacle", "断絶（。した（。二つの（。岸辺（。を（。、言葉（。と（。愛の（。力で（。繋ぎ（。合わせ（。、一歩（。踏み出（。せば（。、向こう（。岸（。の（。真実（。へと（。辿り（。着ける（。ように（。する（。ための（。、勇気（。の（。建築物。"),
    ("matrix", "Matrix", "基盤、母体、行列、マトリックス", "14th Century", "mater (mother)", "An environment or material in which something develops; a surrounding medium or structure", "全ての（。エナジー（。を（。包（。み（。込み（。、育（。む（。ための「母（。マター）」なる（。構造（。。（。見えない（。網（。の（。目の中で（。、生命は（。そっと（。守（。られ（。ながら（。、自ら（。の（。かたち（。を（。獲得（。して（。いく（。のです。"),
    ("infrastructure", "Infrastructure", "インフラ、基盤施設", "20th Century", "infra- (below) + structure (building)", "The basic physical and organizational structures and facilities (e.g. buildings, roads, power supplies) needed for the operation of a society or enterprise", "華やかな（。表舞台を（。支える（。、目（。に見えない「下部（。インフラ）の（。構造（。ストラクチャ）」。（。感謝（。さえ（。さ（。れ（。ない（。けれど（。、それが（。なければ（。、世界（。は（。一瞬（。にして（。瓦解（。して（。しまう（。、沈黙（。の（。功労者。")
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
            word_id = f"{word_text.lower()}_harm"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "葛藤を恐れないでください。それは、新しい調和が生まれるための産声なのですから。",
                    "example": f"The diplomat worked tirelessly to reach a lasting {word_text} between the two nations.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["調和とは、静止した状態ではなく、異なる命が激しくダンスを踊り続けている瞬間の奇跡です。"]
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

        print(f"Success: Added {added_count} words. Theme: Conflict & Harmony (Cycle 35).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
