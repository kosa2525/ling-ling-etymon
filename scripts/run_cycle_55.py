import json
import re

# Theme: The Alchemy of Bridge & Path (Cycle 55)
words_data = [
    ("viaduct", "Viaduct", "高架橋、陸橋、バイアダクト", "19th Century", "via (way) + duct (lead, literal: 'lead through')", "A long bridge-like structure, typically a series of arches, carrying a road or railway across a valley or other low ground", "大地を（。滑る（。ように（。、「道（。ヴィア）を（。導（。いて（。ダクト）行く（。）」巨大な（。アーチ。（。谷（。を（。越え（。、新しい（。地平へと（。、あなた（。を（。誘（。う（。、知的な（。飛躍。"),
    ("causeway", "Causeway", "堤道、土手道、コーズウェイ", "15th Century", "calx (limestone, literal: 'paved way')", "A raised road or track across low or wet ground", "泥（。まみれ（。の（。大地（。に（。、「石（。カルシ）で（。築（。き（。上げた（。）」、揺るぎ（。ない（。道（。。（。困難（。な（。季節（。を（。越える（。ための（。、あなた（。だけの（。聖（。なる（。足場。"),
    ("thoroughfare", "Thoroughfare", "幹線道路、公道、通り抜け", "14th Century", "thorough (through) + fare (go)", "A road or path forming a route between two places", "一箇所に（。留（。ま（。ら（。ず（。、世界（。を「貫（。き（。抜（。いて（。スルー）行く（。フェア）」ための（。大動脈（。。（。そこ（。には（。、絶（。え（。間（。ない（。出会いと（。別れが（。、美し（。い（。リズム（。を（。刻（。んで（。いる（。のですよ。"),
    ("traverse", "Traverse", "横断する、詳しく検討する、トラバース", "14th Century", "trans- (across) + vertere (to turn)", "Travel across or through", "既定（。の（。ルート（。を（。拒み（。、あえて「横（。切（。る（。トランス）よう（。に（。向（。く（。ヴァース）」こと（。。（。未知（。なる（。領域（。へと（。踏（。み（。込む（。、勇気（。ある（。斜行。"),
    ("conduit", "Conduit", "導管、パイプ、仲介者", "14th Century", "com- (together) + ducere (to lead)", "A channel for conveying water or other fluid", "目（。には（。見えない（。エナジーを（。、一つに「共に（。コン）導（。き（。出す（。ドゥ）」ための（。管（。。（。自分（。を（。主張（。する（。のではなく（。、ただ（。光（。を（。運（。ぶ（。ため（。だけの（。、透明（。な（。る（。媒介。"),
    ("interface", "Interface", "インターフェース、接点、仲立ち", "19th Century", "inter- (between) + face", "A point where two systems, subjects, organizations, etc., meet and interact", "異（。なる（。世界（。と（。世界の「間（。インター）に（。ある（。顔（。フェース）」。（。そこ（。で（。交わ（。される（。静（。かな（。る（。火花が（。、新（。しい（。意味を（。産（。み（。出す（。のですよ。"),
    ("concierge", "Concierge", "コンシェルジュ、門衛、案内人", "17th Century", "com- (with) + servus (slave, keep, literal: 'fellow slave')", "A hotel staff member who helps guests by making a restaurant reservation, etc.", "入り（。口（。で（。、旅人の「全（。てを（。共に（。コン）守り（。抜く（。シェルジュ）」者（。。（。あなた（。の（。不安（。を（。、一瞬の（。微笑みで（。安（。ら（。ぎへと（。変（。える（。、境界（。の（。守護者。"),
    ("vestibule", "Vestibule", "前庭、入り口の広間、ベスチビュール", "17th Century", "vestis (garment, literal: 'place where garments are removed')", "An antechamber, hall, or lobby next to the outer door of a building", "日常（。の「衣（。装（。ヴェスティ）を（。脱ぎ（。捨てる（。）」ための（。、浄（。聖（。なる（。空間（。。（。そこ（。から（。は（。、もう（。昨日（。までの（。自分（。では（。ない（。、新しい（。物語が（。始まり（。ます。"),
    ("concourse", "Concourse", "（駅などの）中央ホール、合流", "14th Century", "com- (together) + currere (to run)", "A large open area inside or in front of a public building, as in a hotel or airport", "無数（。の（。意志が（。、「共に（。コン）駆け（。寄（。る（。カース）」場所（。。（。混沌（。と（。した（。エナジーが（。、束（。の（。間（。だけ（。交差（。し（。、また（。旅へと（。戻（。って（。いく（。、運命の（。交差（。点。"),
    ("terminal", "Terminal", "終着駅、端末、末期の", "15th Century", "terminus (end, boundary, limit)", "Of, forming, or situated at the end or extremity of something", "旅の「最後（。の（。端（。ターミナ）」であり（。、同時（。に（。新（。しい（。始まりの（。門（。。（。全（。てを（。精算（。し（。、無限（。へと（。漕（。ぎ（。出す（。ための（。、沈黙（。の（。境界（。線。"),
    ("liaison", "Liaison", "連絡、連絡係、リエゾン", "17th Century", "ligare (to bind)", "Communication or cooperation which facilitates a close working relationship between people or organizations", "バラバラ（。の（。組織（。を（。、見えない（。糸で「固く（。結び（。付ける（。リガ）」こと（。。（。あなた（。の（。一言（。の（。配慮（。が（。、巨大（。な（。不協和音（。を（。、美し（。い（。調和へと（。変（。える（。のですよ。"),
    ("synergy", "Synergy", "シナジー、相乗効果", "17th Century", "sun- (together) + ergon (work)", "The interaction or cooperation of two or more organizations, substances, or other agents to produce a combined effect greater than the sum of their separate effects", "一人（。の（。力（。では（。なく（。、「共に（。サン）働く（。エルゴン）」ことで（。生まれる（。、未知（。なる（。エナジー。（。一（。足（。す（。一（。が（。、無限（。へと（。至（。る（。、奇跡（。の（。掛け（。算。"),
    ("altruism", "Altruism", "利他主義、愛他主義", "19th Century", "alter (other)", "The belief in or practice of disinterested and selfless concern for the well-being of others", "自分（。の（。エゴ（。を（。捨て（。去り（。、ただ「他（。者（。オルト）」の（。ために（。命を（。燃（。やす（。こと（。。（。その（。無償（。の（。愛が（。、巡（。り（。巡（。って（。、あなた（。自身（。を（。救（。う（。の（。ですよ。"),
    ("heritage", "Heritage", "遺産、継承物、ヘリテージ", "13th Century", "heres (heir)", "Property that is or may be inherited; an inheritance", "過去から（。現代へと（。、「受け（。継（。ぐ（。ヘレス）べき（。）」、至高（。の（。記憶（。。（。石（。の（。壁（。にも（。、一枚（。の（。布（。にも（。、先祖（。たちの（。祈り（。が（。刻ま（。れて（。いる（。のですよ。"),
    ("foundation", "Foundation", "基礎、土台、ファンデーション", "14th Century", "fundus (bottom)", "The lowest load-bearing part of a building, typically below ground level", "目（。には（。見えない（。地底に（。、あらかじめ「底（。フンド）として（。築かれた（。）」もの（。。（。土台（。が（。盤石（。であ（。ればこそ（。、塔（。は（。どこ（。まで（。も（。高く（。、天を（。指し（。し（。め（。す（。ことが（。できる（。の（。ですよ。")
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
            word_id = f"{word_text.lower()}_bridge"
            
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
                    "thinking": item[6] if len(item) > 6 else "道とは、どこかへ行くための手段ではなく、歩むことそのものが目的地なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "架け橋は、二つの異なる絶望を、一つの希望へと繋ぎ止めるための祈りです。",
                    "example": f"The architectural firm specialized in designing elegant {word_text} that harmonized with the natural landscape.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["境界とは、世界を分断するものではなく、二つの異なる美しさを繋ぎ止めるための接点なのです。"]
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

        print(f"Success: Added {added_count} words. Theme: Bridge & Path (Cycle 55).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
