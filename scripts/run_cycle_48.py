import json
import re

# Theme: The Alchemy of Flesh & Bone (Cycle 48)
words_data = [
    ("physiology", "Physiology", "生理学、生理", "16th Century", "phusi- (nature) + -logia (study of)", "The branch of biology that deals with the normal functions of living organisms and their parts", "冷徹な（。機械的な（。動き（。ではなく（。、生命（。が（。本来（。持（。って（。いる「自然（。フュシス）の（。理（。理（。）」。（。そこ（。には（。、何（。億（。年（。という（。時間が（。育（。ん（。だ（。、完璧（。な（。調和（。が（。あります。"),
    ("neuron", "Neuron", "神経細胞、ニューロン", "19th Century", "neuron (sinew, nerve, fiber)", "A specialized cell transmitting nerve impulses; a nerve cell", "情報を（。ただ（。流す（。だけでなく（。、魂の（。エナジーを（。一点へと「結ぶ（。ニューロ）繊維（。）」。（。その（。一本（。い（。っぽ（。ん（。の（。震（。えが（。、あなた（。という（。宇宙の（。意識を（。形（。作（。って（。いる（。のですよ。"),
    ("synapse", "Synapse", "シナプス、接合部", "19th Century", "sun- (together) + haptein (to join)", "A junction between two nerve cells, consisting of a minute gap across which impulses pass by diffusion of a neurotransmitter", "情報（。と（。情報（。が（。、一瞬（。だけ「共に（。サン）結び（。合（。わ（。される（。ハプト）」聖（。なる（。場所（。。（。その（。微（。小（。な（。隙間（。を（。、言葉（。という（。名の（。火花が（。飛（。び（。越（。え（。て（。いく（。のです。"),
    ("cardiac", "Cardiac", "心臓の、心臓病の", "16th Century", "kardia (heart)", "Of or relating to the heart", "自覚（。する（。よりも（。遥（。かに（。深く（。、ひたすら（。ビート（。を（。刻（。み（。続ける「心（。カルディア）」の（。鼓動（。。（。生きて（。いる（。という（。こと（。の（。、残酷（。な（。までに（。眩（。しい（。根拠。"),
    ("arterial", "Arterial", "動脈の、幹線の", "14th Century", "arteria (windpipe, artery)", "Of or relating to an artery", "酸素（。という（。名の（。希望を（。、全身へと（。運ぶ「生命（。の（。管（。アルテリア）」。（。そこ（。を（。流れる（。情熱が（。、あなた（。を（。常に（。新しい（。明日へと（。突き（。動かす（。の（。ですよ。"),
    ("hormone", "Hormone", "ホルモン、刺激するもの", "20th Century", "hormon (setting in motion, urging on)", "A regulatory substance produced in an organism and transported in tissue fluids such as blood or sap to stimulate specific cells or tissues into action", "ただそこに（。ある（。だけでなく（。、魂を「激しく（。駆（。り（。立て（。る（。ホルモ）」、微小（。な（。化学（。分子。（。喜び（。も（。悲しみ（。も（。、すべては（。この（。小さな（。使者（。たちが（。運んで（。くる（。の（。かも（。しれ（。ません。"),
    ("enzyme", "Enzyme", "酵素、エンザイム", "19th Century", "en- (in) + zume (leaven, yeast)", "A substance produced by a living organism which acts as a catalyst to bring about a specific biochemical reaction", "複雑（。な（。物質（。を（。、命（。に（。変え（。て（。いく（。ための「中（。イン）にある（。酵（。母（。ズーメ）」。（。目（。には（。見えない（。けれど（。、確（。かに（。存在（。する（。、生命（。変容（。の（。錬金術師。"),
    ("metabolism", "Metabolism", "新陳代謝、メタボリズム", "19th Century", "meta- (change, beyond) + ballein (to throw)", "The chemical processes that occur within a living organism in order to maintain life", "古い（。記憶を（。脱（。ぎ（。捨て（。、自らを「向こう（。側へと（。メタ）新（。しく（。投げ（。出す（。バロ）」こと（。。（。この（。絶（。え（。間（。ない（。変化（。こそが（。、生きて（。いる（。と（。いう（。、唯一（。の（。証明。"),
    ("respiration", "Respiration", "呼吸、一息", "14th Century", "re- (again) + spirare (to breathe)", "The action of breathing", "宇宙（。の（。エナジーを（。吸い（。込み（。、再び（。「繰（。り（。返し（。リ）息（。を（。吐（。き（。出す（。スピラ）」こと（。。（。あなた（。の（。一呼吸（。一呼吸（。が（。、世界（。と（。の（。密（。かな（。る（。対話（。なのです。"),
    ("marrow", "Marrow", "骨髄、核心、マロウ", "Old English", "mearg (pith, marrow)", "A soft fatty substance in the cavities of bones, in which blood cells are produced", "硬い（。骨（。の（。奥底に（。隠された（。、「命の（。源泉（。メアグ）」。（。そこ（。から（。、絶（。える（。こと（。なく（。情熱が（。産（。み（。出（。さ（。れ（。て（。いる（。の（。ですよ。"),
    ("reflex", "Reflex", "反射、不随意の反応", "16th Century", "re- (back) + flectere (to bend)", "An action that is performed as a response to a stimulus and without conscious thought", "考える（。暇（。さ（。え（。与（。え（。ず（。、刺激（。をその（。まま「後ろ（。に（。リ）曲（。げ（。戻（。す（。フレク）」こと（。。（。命（。が（。、自ら（。を（。守るため（。に（。用意（。した（。、光速（。の（。対（。抗。"),
    ("stimulus", "Stimulus", "刺激、スチムラス", "17th Century", "stimulus (goad, prick, pointed stick)", "A thing or event that evokes a specific functional reaction in an organ or tissue", "退屈（。な（。日常に（。、不（。意（。に（。突（。き（。刺（。さ（。る「尖（。った（。棒（。スチラム）」。（。その（。鋭（。い（。痛みだけが（。、深い（。眠り（。の（。淵から（。、あなた（。を（。呼び（。覚（。ます（。の（。ですよ。"),
    ("instinct", "Instinct", "本能、直感、インスティンクト", "15th Century", "in- (into, on) + stinguere (to prick, urge)", "An innate, typically fixed pattern of behavior in animals in response to certain stimuli", "学習（。する（。前（。から（。、心（。の（。中に「鋭（。く（。刻（。ま（。れた（。スティン）衝動（。）」。（。理性（。の（。嵐（。の（。中（。でも（。、決して（。揺（。る（。ぐ（。こと（。の（。ない（。、生命（。の（。絶対的な（。コンパス。"),
    ("volition", "Volition", "意志、決断、ヴォリション", "17th Century", "velle (to wish, will)", "The faculty or power of using one's will", "ただ（。流（。さ（。れる（。のを（。止め（。、自ら（。の（。内側から「願（。い（。ヴェレ）を（。絞（。り（。出す（。）」こと（。。（。その（。一瞬（。の（。決断（。が（。、あなたの（。運命（。を（。、永遠（。に（。書き（。換（。える（。のです。"),
    ("anatomy", "Anatomy", "解剖学、構造、アナトミー", "14th Century", "ana- (up, through) + temnein (to cut)", "The branch of science concerned with the bodily structure of humans, animals, and other living organisms, especially as revealed by dissection and the separation of parts", "表面（。を（。滑（。る（。のを（。止め（。、真理を（。求めて「徹底的に（。アナ）切り（。分（。ける（。トミー）」こと（。。（。バラバラ（。に（。して（。こそ（。見えてくる（。、生命（。という（。名の（。、精（。緻（。な（。伽（。藍（。）。")
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
            word_id = f"{word_text.lower()}_flesh"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "肉体は、魂がこの世界で踊るための、美しい衣裳に過ぎません。",
                    "example": f"The study of human {word_text} reveals the incredible complexity of life.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["生命とは、ただの物質の集まりではなく、絶え間ない変化と調和の中に宿る、奇跡そのものです。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["cardiac", "arterial", "venous", "instinctive"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Flesh & Bone (Cycle 48).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
