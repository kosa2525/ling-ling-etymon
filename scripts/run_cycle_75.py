import json
import re

# Theme: The Alchemy of Synergy & Synthesis (Cycle 75)
words_data = [
    ("synergy", "Synergy", "相乗効果、シナジー", "17th Century", "sun- (together) + ergon (work)", "The interaction or cooperation of two or more organizations, substances, or other agents to produce a combined effect greater than the sum of their separate effects", "魂（。と（。魂が「共同で（。サン）働（。く（。エルゴン）」一瞬（。の（。火花（。（。一（。に（。一（。を（。足（。し（。て（。、二（。に（。な（。る（。のではなく（。、測り（。知（。れ（。な（。い（。巨大（。な（。光を、産む（。こと（。を（。こそ、調和（。という（。のですよ。"),
    ("nexus", "Nexus", "繋がり、核心、ネクサス", "17th Century", "nectere (to bind, literal: 'connection')", "A connection or series of connections linking two or more things", "バラバラ（。の（。事物（。を（。、峻（。烈（。に「繋（。ぎ（。止める（。ネク）」場所（。（。全（。ての（。エナジーが（。、一点に（。凝縮（。さ（。れる（。その（。結（。節（。にこそ（。、宇宙の（。真実（。が（。宿（。って（。いる（。のですよ。"),
    ("confluence", "Confluence", "合流、コンフルエンス", "15th Century", "com- (together) + fluere (to flow)", "The junction of two rivers, especially rivers of approximately equal width", "別（。々の（。河が「共（。に（。コン）流れ（。る（。フル）」こと（。。（。その（。烈（。し（。い（。交（。差（。点（。で（。、新しい（。物（。語（。が（。、音（。を（。立（。て（。て（。、動き（。出す（。のですよ。"),
    ("circuit", "Circuit", "巡回、回路、サーキット", "14th Century", "circum- (around) + ire (to go, literal: 'going around')", "A roughly circular line, route, or movement that starts and finishes at the same place", "迷（。う（。こと（。なく「周囲を（。サーカム）行く（。イ）」、美（。し（。い（。円（。環（。（。その（。閉（。じ（。た（。回廊（。を（。、エナジー（。は（。、永遠（。に（。、駆け（。抜（。け（。続け（。る（。のですよ。"),
    ("liaison", "Liaison", "連絡、密通、リエゾン", "17th Century", "ligare (to bind, literal: 'binding')", "Communication or cooperation which facilitates a close working relationship between people or organizations", "異（。な（。る（。領域（。を（。、そっと「結（。び（。付ける（。リエ）」見えない（。糸（。（。その（。静（。か（。な（。る（。媒介（。が（。ある（。から（。こそ（。、世界（。は（。、反発（。し（。合う（。こと（。なく（。、愛（。し（。合える（。のですよ。"),
    ("mediation", "Mediation", "調停、仲介、メディエーション", "14th Century", "medius (middle, literal: 'in the middle')", "Intervention in a dispute in order to resolve it; arbitration", "対立する（。二（。つの（。極の「真ん（。中（。メディ）に（。立つ（。）」こと（。。（。どちら（。にも（。肩（。入れ（。せず（。、ただ（。一（。つ（。の（。バランスを（。求（。める（。その（。沈黙（。の中に、真理（。は（。、宿（。る（。の（。ですよ。"),
    ("negotiation", "Negotiation", "交渉、ネゴシエーション", "16th Century", "neg- (not) + otium (leisure, literal: 'not leisure')", "Discussion aimed at reaching an agreement", "ただの（。休息（。を（。拒み（。、峻（。烈（。な「活（。動（。ネゴ）に（。身（。を（。投じる（。）」こと（。。（。言葉（。という（。名の（。、見（。え（。な（。い（。刃（。を（。交え（。て（。、新しい（。る（。均衡を（。、創り（。出す（。のですよ。"),
    ("compromise", "Compromise", "妥協、和解、コンプロマイズ", "15th Century", "com- (together) + promittere (to promise, literal: 'promising together')", "An agreement or a settlement of a dispute that is reached by each side making concessions", "互（。いに（。が（。一（。つ（。の（。希望（。を「共（。に（。コン）約束（。する（。プロマイズ）」こと（。。（。それは（。、敗（。北（。では（。なく（。、共（。存（。という（。名の（。、至高（。の（。る（。智（。慧（。なの（。ですよ。"),
    ("settlement", "Settlement", "和解、定住（。地（。、セトルメント", "14th Century", "setlan (to cause to sit)", "An official agreement intended to resolve a dispute or conflict", "荒（。れ（。狂（。う（。嵐を（。静（。め（。、「安（。ら（。かに（。座（。らせる（。セトル）」こと（。。（。その（。静（。な（。る（。決（。着（。が（。、新（。しい（。大地（。に、根（。を（。下（。ろ（。す（。、始（。まり（。に（。なる（。のですよ。"),
    ("federation", "Federation", "連邦、連合、フェデレーション", "17th Century", "foedus (league, treaty, literal: 'faith')", "A group of states with a central government but independence in internal affairs", "個（。々の（。誇り（。を（。保（。ち（。な（。がら（。、「信頼（。フェド）という（。名の（。契（。約（。）」で（。結（。ば（。れる（。こと（。。（。その（。多（。様（。性（。の（。中にある（。、一（。つ（。の（。意志が（。、世界を（。、支えて（。いる（。の（。ですよ。"),
    ("fellowship", "Fellowship", "仲間意識、特別研究員、フェローシップ", "Old English", "feolage (partner) + -ship", "Friendly association, especially with people who share one's interests", "一（。つ（。の（。目（。的に（。向（。かって（。、魂を「預（。け（。合う（。フェロー）」仲間たち（。（。その（。静（。か（。な（。る（。連帯（。の中にこそ（。、孤独（。を（。越元（。た（。、至高の（。る（。力（。が（。、宿ります。"),
    ("fraternity", "Fraternity", "友愛（。、男子（。学（。生（。親（。睦（。団体（。、フラタニティ", "14th Century", "frater (brother)", "A group of people sharing a common profession or interests", "血（。の（。繋（。が（。りを（。越え（。た（。、「兄（。弟（。フラ)のような（。強い（。る（。絆（。）」。（。そこ（。には（。、互（。いに（。を高（。め（。合う（。ための（。、矜（。持と（。、愛（。が（。、満（。ち（。（。溢（。れて（。いる（。のですよ。"),
    ("sorority", "Sorority", "女子学生（。親（。睦（。団体（。、ソロリティ", "16th Century", "soror (sister)", "A society for female students in a university or college", "優（。し（。さと（。強（。さを（。兼（。ね（。備（。えた（。、「姉（。妹（。ソロール）のような（。絆（。）」。（。その（。細（。や（。かな（。る（。共鳴（。が（。、不（。毛（。なる（。世界（。に（。、美し（。い（。花（。を（。、咲（。か（。せ（。続け（。る（。のですよ。"),
    ("collective", "Collective", "集合的（。な（。）、集団、コレクティブ", "15th Century", "com- (together) + legere (to gather, literal: 'gathered together')", "Done by people acting as a group", "バラバラ（。の（。欠片（。を（。、「一（。つ（。に（。コン）集（。める（。レク）」こと（。。（。個（。の（。限界を（。越（。え（。た（。場所（。に（。、巨大（。な（。る（。意（。志（。の（。化身（。が（。、静（。か（。に（。、顕（。現（。する（。のですよ。"),
    ("synthesis", "Synthesis", "統合、合成、シンセシス", "17th Century", "sun- (together) + tithenai (to place, literal: 'placing together')", "The combination of ideas to form a theory or system", "全（。く（。異（。なる（。極性（。を（。、「共に（。サン）置（。く（。セシス）」こと（。。（。その（。融（。合（。の（。瞬間に（。、どこ（。にも（。な（。か（。っ（。た（。、眩（。しい（。第（。三（。の（。真（。理が（。、煌（。め（。き（。始める（。のですよ。")
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
            word_id = f"{word_text.lower()}_connect"
            
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
                    "thinking": item[6] if len(item) > 6 else "繋がりとは、自分を広げることではなく、他者という名の宇宙を、自らの中に迎え入れることなのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "調和は、静止した場所にあるのではありません。反発し合うエナジーが、奇跡的に均衡を保っている、その最前線にあるのですよ。",
                    "example": f"The successful {word_text} between the two research teams led to a major breakthrough in renewable energy technology.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["一人が見る夢はただの夢ですが、皆で共に置く夢は、いつか現実という名の大地を創り出すのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["collective", "synergistic", "synthetic"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Synergy & Synthesis (Cycle 75).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
