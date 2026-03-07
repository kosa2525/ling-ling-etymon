import json
import re

# Theme: The Alchemy of Garment & Thread (Cycle 64)
words_data = [
    ("textile", "Textile", "織物、テキスタイル", "15th Century", "texere (to weave)", "A type of cloth or woven fabric", "ただの（。糸の（。集（。まり（。ではなく（。、思考の（。断片を「織（。り（。上げ（。る（。テク）」ことで（。創（。り出（。さ（。れた（。、物語（。。（。その（。表面（。の（。手触りに（。、人類が（。紡（。い（。できた（。、文明（。の（。温（。か（。みが（。宿（。って（。いる（。のですよ。"),
    ("shuttle", "Shuttle", "杼（ひ）、シャトル、往復便", "Old English", "scytel (dart, arrow, literal: 'shoot')", "A form of transport that travels regularly between two places", "織（。機の（。中を「矢（。シャト）のように（。）」、右（。から（。左へと（。駆け抜ける（。もの（。。（。その（。烈（。しい（。往復運動（。が（。、バラバラ（。の（。糸に（。、一つの（。美し（。い（。秩序（。を（。与（。えて（。いく（。のですよ。"),
    ("spindle", "Spindle", "紡錘（ぼうすい）、回転軸、スピンドル", "Old English", "spinnan (to spin)", "A slender rounded rod with tapered ends used in hand-spinning to twist and wind stock from a distaff into yarn", "混沌（。とした（。原棉（。から（。、命の（。糸を「紡（。ぎ（。出す（。スピン）」ための（。、静（。か（。な（。る（。回転（。。（。一点（。を（。軸（。に（。し（。て（。、無（。窮（。なる（。エナジーを（。、線（。へと（。変えて（。いく（。、魔法（。の（。杖。"),
    ("bobbin", "Bobbin", "糸巻き、ボビン", "16th Century", "bobine (spool)", "A cylinder or cone holding thread, yarn, or wire, used especially in weaving, machine sewing, and lacemaking", "紡（。が（。れた（。糸を、一（。時（。的に「預（。か（。る（。ボビン）』ための（。器（。。（。そこ（。には（。、次（。なる（。創造（。を（。夢見（。る（。、静（。か（。な（。る（。待機（。の（。エナジーが（。、幾（。重（。にも（。巻（。か（。れて（。いる（。のですよ。"),
    ("fiber", "Fiber", "繊維、ファイバー、気質", "14th Century", "fibra (fiber, literal: 'entrail')", "A thread or filament from which a vegetable tissue, mineral substance, or textile is formed", "物体の（。奥深くに（。、まるで「内臓（。フィブラ）」のように張り巡らさ（。れた（。、細（。い（。筋（。。（。その（。一本（。一本（。の（。強（。靭（。さが（。、巨大（。な（。調和（。を（。、底（。知（。れ（。ぬ（。力（。で（。支えて（。いる（。のですよ。"),
    ("stitch", "Stitch", "一縫い、ステッチ、ひきつれ", "Old English", "sticce (prick, sting, literal: 'to prick')", "A loop of thread or yarn resulting from a single pass or movement of the needle in sewing, knitting, or embroidering", "針を（。刺（。し「突き（。抜（。く（。スティ）」ことで（。、二（。つの（。運命（。を（。繋（。ぎ（。止（。める（。一瞬（。の（。火花（。。（。その（。小（。さな（。点（。の（。連（。なりが（。、いつしか（。巨大な（。愛（。の（。紋様（。を（。描き出す（。のです。"),
    ("seam", "Seam", "縫い目、継ぎ目、シーム", "Old English", "sēam (seam, suture)", "A line where two pieces of fabric are sewn together in a garment or other article", "異（。なる（。布と（。布を「結び（。合わせた（。シーム）」痕跡（。。（。隠（。さ（。れた（。その（。継（。ぎ目（。にこそ（。、職人（。の（。誠実（。さと（。、構造（。の（。真（。実（。が（。、密（。かに（。、宿（。って（。いる（。のですよ。"),
    ("cuff", "Cuff", "袖口（そでぐち）、カフス", "14th Century", "Origin uncertain, possibly related to glove", "The end part of a sleeve, where the material of the sleeve is turned back or a separate band is sewn on", "手（。の（。動き（。を（。邪魔（。し（。ない（。ように（。、そっと「包（。み（。守（。る（。カフ）」場所（。。（。その（。円（。環（。状の（。秩序（。が（。、あなた（。の（。指先（。に（。、静（。か（。な（。る（。矜（。持（。を（。与（。えて（。くれ（。る（。のですよ。"),
    ("embroidery", "Embroidery", "刺繍（ししゅう）、潤色", "14th Century", "en- (in) + broder (to edge, literal: 'on the edge')", "The art or pastime of embroidering cloth", "ただの（。布に（。、色（。鮮（。やかな（。エナジーを「刺（。し（。込（。む（。ブロード）中（。イン）」こと（。。（。その（。立体（。的（。な（。煌（。め（。き（。は（。、日常（。の（。平坦（。さを（。越（。え（。た（。場所（。にある（。、至高（。の（。遊悦。"),
    ("brocade", "Brocade", "錦（にしき）、金襴（きんらん）", "16th Century", "broccus (projecting, literal: 'to prick')", "A rich fabric, typically silk, woven with a raised pattern, typically with gold or silver thread", "厚（。手の（。布（。に（。、美し（。い（。文様を「浮（。き（。出さ（。せた（。ブロッ）」織物（。。（。そこ（。には（。、権威（。と（。豊饒（。が（。、金（。銀（。の（。糸（。と（。共（。に（。、幾（。重（。にも（。、織（。り（。込（。ま（。れて（。いる（。のですよ。"),
    ("satin", "Satin", "朱子（。しゅす（。）」、サテン", "14th Century", "Zaitun (Quanzhou, city in China)", "A smooth, glossy fabric, typically of silk, produced by a weave in which the threads of the warp are caught and looped by the weft only at certain intervals", "遥（。か（。な（。る（。東方の「都市（。ザイトン）』から（。届（。いた（。、至高（。の（。滑（。らかさ（。。（。光（。を（。優（。しく（。滑（。ら（。せ（。、魂を（。、官能（。という（。名の（。、甘（。い（。微（。睡（。みへと（。誘（。い（。ます。"),
    ("apparel", "Apparel", "衣服、装具、アパレル", "13th Century", "ad- (to) + parere (to join, make ready, literal: 'to prepare')", "Clothing in general", "裸（。の（。自分を（。、社会（。と「繋（。ぎ（。止（。める（。アダ、パラ）」ために（。、あらかじめ（。整（。え（。られた（。もの（。。（。あなた（。が（。今日（。、何（。を（。纏（。う（。のか、それ（。が（。あなた（。の（。言葉（。その（。もの（。に（。なる（。のですよ。"),
    ("wardrobe", "Wardrobe", "衣装だんす、持ち衣装、ワードローブ", "14th Century", "ward (to guard) + robe (garment)", "A large, tall cabinet in which clothes may be hung or stored", "多（。色（。多（。様な（。自分（。という（。名の「隠（。れ（。みの（。ローブ）を（。守る（。ワード）」場所（。。（。扉（。を（。開（。けるた（。びに（。、あなた（。は（。、全（。く（。新（。しい（。自分を（。、再（。発見（。する（。のです。"),
    ("mantle", "Mantle", "マント、覆い、地殻", "Old English", "mantel (cloak)", "A loose sleeveless cloak or shawl, worn especially by women", "自（。らを（。大きく（。見（。せ（。、全（。てを「優（。しく（。覆（。い（。隠（。す（。マンテル）」衣（。裳（。（。そこ（。には（。、使命（。と（。いう（。名の（。重厚（。な（。る（。尊厳が（。、肩（。の（。上（。に（。、誇（。り（。高く（。、宿（。って（。いる（。のですよ。"),
    ("hosiery", "Hosiery", "靴下類、メリヤス、ホージャリー", "17th Century", "hose (legging) + -ery", "Stockings, socks, and tights collectively", "大地と（。直（。接（。触（。れる（。足を、静（。かに「包み（。守（。る（。ホース）」もの（。たちの（。総（。称（。（。その（。密（。かな（。る（。支（。えが（。、あなた（。の（。一歩（。一歩（。を（。、軽（。やかに（。、し（。な（。やかに（。、して（。くれる（。のですよ。")
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
            word_id = f"{word_text.lower()}_garment"
            
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
                    "thinking": item[6] if len(item) > 6 else "衣服は、魂がこの世界で震えないための、第二の皮膚なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "糸の一本一本は、バラバラな心を繋ぎ止めるための、静かなる誓いなのです。",
                    "example": f"The shop offered a wide variety of {word_text} made from high-quality natural fibers.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["纏うという行為は、世界に対して自らをどう定義するか、という無言の宣言なのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Garment & Thread (Cycle 64).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
