import json
import re

# Theme: The Alchemy of Elements & Matter (Cycle 38)
words_data = [
    ("reagent", "Reagent", "試薬、反応物", "18th Century", "re- (back, again) + agere (to do, act)", "A substance or mixture for use in chemical analysis or other reactions", "ただ（。そこに（。ある（。だけでなく（。、相手に（。刺激を与え「再び（。リ）動か（。し（。アグ）反応させる（。）」ための（。エッセンス（。。（。あなた（。の（。言葉が（。、誰（。かの（。心に（。火（。を（。つける（。、聖なる（。試薬と（。なる（。のですよ。"),
    ("compound", "Compound", "化合物、複合の、混ぜ合わせる", "14th Century", "com- (together) + ponere (to put, place)", "A thing that is composed of two or more separate elements; a mixture", "バラバラの（。素材を（。、意図を持って「一つに（。コン）配置（。ポーズ）した（。）」もの（。。（。異純（。な（。ものが（。混ざり（。合い（。（。、全く（。新（。しい（。輝きを（。放（。ち（。始める（。、調和の（。結晶。"),
    ("alloy", "Alloy", "合金、混ぜ物", "14th Century", "ad- (to) + ligare (to bind)", "A metal made by combining two or more metallic elements, especially to give greater strength or resistance to corrosion", "単独では（。脆く（。ても（。、別の（。強（。さと（。「固く（。結び（。リガ）合わ（。さ（。れた（。アド）」とき（。、何物（。にも（。屈（。しない（。、強靭な（。精神（。へと（。変貌（。する（。、連帯の（。輝き。"),
    ("vapor", "Vapor", "蒸気、気体、儚いもの", "14th Century", "vapor (steam, warm exhalation)", "A substance diffused or suspended in the air, especially one normally liquid or solid", "熱（。という（。エナジーによって（。、自ら（。の（。境界線を（。捨て（。、「天空へと（。昇（。る（。ヴェイパー）」、透明で（。自由な（。魂の（。吐息。"),
    ("silicon", "Silicon", "シリコン、ケイ素", "19th Century", "silex (flint)", "The chemical element of atomic number 14, a nonmetal with semiconducting properties", "太古の（。昔（。、人類が（。初めて（。火（。を（。手（。に入（。れた「火打石（。サイレックス）」の（。記憶。今（。では（。、世界（。の（。知性（。を（。司（。る（。、透明（。な（。回路（。の（。中核。"),
    ("mineral", "Mineral", "鉱物、ミネラル", "13th Century", "mina (mine)", "A solid inorganic substance of natural occurrence", "太陽の（。光さえ（。届（。かない（。、「暗（。い（。地底の（。穴（。マイン）」の中で（。、長い（。長い（。時間（。を（。かけて（。、沈黙（。の（。うちに（。自らを（。磨き（。上げた（。、大地の（。記憶。"),
    ("fossil", "Fossil", "化石", "16th Century", "fodere (to dig)", "The remains or impression of a prehistoric organism preserved in petrified form or as a mold or cast in rock", "かつて（。鮮やかに（。生きて（。いた（。証（。を（。、「地（。中を（。掘り（。フォド）起こす（。）」ことで（。、再び（。今（。へと（。蘇（。らせ（。た（。、石（。に（。刻まれた（。永遠（。の（。メッセージ。"),
    ("mercury", "Mercury", "水銀、マーキュリー", "14th Century", "Mercurius (Roman god Mercury)", "The chemical element of atomic number 80, a heavy silvery-white metal which is liquid at ordinary temperatures", "死（。を（。意味（。する（。冷徹な（。重工（。感（。を（。持ち（。ながら（。、水（。のように（。自由に（。か（。たち（。を（。変える（。、神々の（。使者（。マーキュリー）のような（。、神（。秘（。的（。で（。危険（。な（。流動体。"),
    ("phosphorus", "Phosphorus", "リン", "17th Century", "phos- (light) + phoros (bringing)", "The chemical element of atomic number 15, a poisonous, combustible nonmetal which exists in two common allotropic forms", "闇（。の（。中（。で（。、自ら（。燃（。え（。上が（。る（。ことで（。「光を（。フォス）運（。んで（。くる（。フォロス）」、静（。かな（。る（。生命（。の（。火（。種（。。（。あなた（。の（。祈り（。も（。、そうであ（。り（。たい（。もの（。ですね。"),
    ("toxin", "Toxin", "毒素、トキシン", "19th Century", "toxikon (poison for arrows)", "An antigenic poison or venom of plant or animal origin, especially one produced by or derived from microorganisms and causing disease when present at low concentration in the body", "元来（。は（。、自分（。を（。守（。る（。ための「弓（。用の（。毒（。トキシ）」。（。あまりに（。純粋（。な（。エナジーは（。、時に（。他（。人（。を（。傷つける（。刃（。になる（。ことを（。、忘れ（。ないで（。ください。"),
    ("venom", "Venom", "（蛇などの）毒、恨み", "13th Century", "venenum (poison, magic potion, drug)", "A poisonous substance secreted by animals such as snakes, spiders, and scorpions and typically injected into prey or aggressors by biting or stinging", "ただの（。汚れ（。ではなく（。、生命（。が（。究極（。の（。窮地で（。絞（。り（。出（。した「魔法（。の（。薬（。ヴェネーナム）」。（。その（。鋭（。い（。痛みは（。、真（。実（。を（。自覚（。させる（。ための（。劇薬（。なの（。かも（。しれ（。ません。"),
    ("solvent", "Solvent", "溶剤、解決策、支払い能力のある", "17th Century", "solvere (to loosen, unbind)", "Able to dissolve other substances", "硬（。い（。結び（。目（。を「解（。き（。放（。す（。ソルヴ）」、自由（。な（。エナジーの（。海（。。（。どんな（。困難（。な（。問題（。も（。、愛（。という（。液体（。に（。浸せば（。、いつか（。美（。しく（。溶（。け（。去（。る（。はず（。ですよ。"),
    ("arsenic", "Arsenic", "ヒ素", "14th Century", "arsenikon (yellow orpiment, literally 'masculine')", "The chemical element of atomic number 33, a brittle steel-gray metalloid", "強力（。な（。エナジーを（。秘め（。た「男性的（。アーセニ）」な（。毒。（。古（。代（。の（。錬金術師（。たちは（。、この（。危険（。な（。黄色（。い（。輝（。きの（。中（。に（。、太陽の（。欠片（。を（。見（。て（。いた（。の（。ですよ。"),
    ("uranium", "Uranium", "ウラン", "18th Century", "Uranus (planet Uranus)", "The chemical element of atomic number 92, a gray dense radioactive metal used as a fuel in nuclear reactors", "広大（。な「星空（。ウラヌス）」の（。記憶（。を（。、この（。小さな（。重（。い（。石（。の（。中に（。封印（。した（。もの（。。（。そこ（。から（。放（。た（。れる（。光（。は（。、世界（。を（。変える（。ほど（。の（。破壊（。と（。創造を（。孕んで（。いる（。のです。"),
    ("radium", "Radium", "ラジウム", "19th Century", "radius (ray)", "The chemical element of atomic number 88, a rare radioactive metal", "暗闇（。の中から（。、絶え（。ず「一条の（。光（。レイ）」を（。放（。ち（。続ける（。、（。誇（。り（。高い（。存在（。。（。誰（。に（。褒（。め（。られ（。なく（。ても（。、自ら（。の（。内側から（。輝き（。を（。絞（。り（。出（。し（。つづ（。ける（。魂の（。象徴。"),
    ("helium", "Helium", "ヘリウム", "19th Century", "helios (sun)", "The chemical element of atomic number 2, an inert gas that is the lightest member of the noble gas series", "「太陽（。ヘリオス）」の（。中で（。、今（。この（。瞬間も（。激（。しく（。燃（。え（。て（。いる（。、歓喜（。の（。エナジーの（。残り（。香（。。（。透明で（。、重力（。を（。も（。嘲笑（。し（。て（。空へと（。昇（。って（。いく（。、純粋（。な（。憧憬。"),
    ("argon", "Argon", "アルゴン", "19th Century", "a- (not) + ergon (work)", "The chemical element of atomic number 18, an inert gaseous element of the noble gas series", "誰（。とも（。交（。わらず（。、決して「働（。き（。エルゴン）かけ（。ない（。ア）」、冷（。徹（。で（。孤（。高（。な（。沈黙（。。（。その（。不動（。の（。姿勢（。の中に（。、宇宙の（。深遠（。な（。調和（。が（。宿（。って（。いる（。の（。ですよ。"),
    ("neon", "Neon", "ネオン", "19th Century", "neos (new)", "The chemical element of atomic number 10, an inert gaseous element used in strip lamps", "日常（。の（。退屈（。な（。景色（。の（。中を（。、眩（。いばかりの（。光波で（。、「新（。しく（。ネオス）」彩（。る（。、人工（。の（。オーロラ（。。（。都会の（。闇を（。希望の（。色で（。塗り（。替（。える（。、欲望と（。夢の（。道標。"),
    ("platinum", "Platinum", "白金、プラチナ", "18th Century", "platina (little silver)", "A precious silvery-white metal", "「銀（。銀（。の（。小粒（。プラチナ）」だと（。見（。く（。び（。られて（。いた（。過去（。を（。越え（。、今（。では（。不（。変（。の（。価値（。の（。代名詞と（。なった（。存在（。。（。あなたの（。中（。の（。小さな（。輝（。きを（。、最後（。まで（。信じ（。抜（。いて（。あげて（。ください。"),
    ("titanium", "Titanium", "チタン", "18th Century", "Titans (giants in Greek mythology)", "The chemical element of atomic number 22, a hard silver-gray metal", "「巨人（。タイタン）」の（。ような（。圧倒的（。な（。強（。さと（。耐（。久性を（。、信（。じ（。られ（。ない（。ほどの（。軽（。さの（。中に（。宿（。した（。、現代（。の（。鎧（。。（。しなやか（。で（。い（。て（。、折（。れ（。ない（。、強靭な（。意志。"),
    ("aluminum", "Aluminum", "アルミニウム", "19th Century", "alumen (alum)", "The chemical element of atomic number 13, a light silvery-white metal", "かつて（。は（。黄金（。よりも（。貴（。重（。だった（。「明（。礬（。アルメン）」の（。精（。。（。空気（。を（。味方（。に（。し（。て（。、世界（。の（。距離を（。縮める（。翼（。へと（。変（。身（。した（。、知性の（。結晶。"),
    ("marble", "Marble", "大理石、マーブル", "12th Century", "marmaros (shining stone)", "A hard crystalline metamorphic form of limestone, typically white with mottlings or streaks of color", "大地の（。巨大な（。圧力（。に（。よって（。、ただの（。石（。が（。、「眩（。い（。ばかりに（。光（。り輝く（。マルマロス）神殿（。の（。魂」へと（。至（。った（。もの（。。（。そこ（。には（。、太（。古の（。海（。の（。囁（。き（。が（。、美し（。い（。模様（。として（。残（。って（。いる（。のですよ。"),
    ("obsidian", "Obsidian", "黒曜石", "17th Century", "Obsidius (Roman discoverer)", "A hard, dark, glasslike volcanic rock formed by the rapid solidification of lava without crystallization", "火（。山の（。激しい（。情熱が（。、一瞬（。にして（。冷却（。され（。、漆（。黒（。の（。ガラス（。へと（。結晶（。した（。もの（。。（。その（。鋭（。い（。欠片（。は（。、嘘（。を（。断（。ち（。切（。る（。ための（。、静（。かな（。る（。刃。"),
    ("amber", "Amber", "琥珀、アンバー", "14th Century", "anbar (ambergris)", "Hard translucent fossilized resin typically yellowish in color", "数（。千（。万年（。という（。時間の（。流れ（。を（。、黄金の（。一（。滴（。の中に（。封じ（。込めた（。「樹脂の（。涙（。）」。（。その（。中（。には（。、かつて（。の（。生命（。の（。輝（。きが（。、温（。かな（。まま（。（。保存（。されて（。いる（。のですよ。"),
    ("tincture", "Tincture", "チンキ、色合い、気味", "14th Century", "tingere (to dye, stain)", "A medicine made by dissolving a drug in alcohol", "ただ（。薬を（。溶（。かす（。だけでなく（。、魂を「染（。め（。上げ（。る（。ティン）」ほどの（。鮮烈（。な（。エッセンス（。。（。言葉（。にも（。、一滴（。の（。誠実（。な（。真理（。を（。混ぜて（。ください（。。（。それ（。だけで（。、退屈（。な（。日常（。は（。一瞬（。にして（。、色彩（。を（。取り戻（。す（。のですから。")
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
            word_id = f"{word_text.lower()}_matter"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "物質は、魂が現実という舞台で踊るための、美しい衣裳です。",
                    "example": f"The scientist added a drops of {word_text} to the solution to observe the reaction.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["変容とは、自分自身の本質を新しい光の下で再定義する行為です。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["compound", "reagent", "mineral"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Elements & Matter (Cycle 38).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
