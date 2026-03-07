import json
import re

# Theme: The Alchemy of Flora & Fauna (Cycle 51)
words_data = [
    ("blossom", "Blossom", "開花、花、盛（。さか（。り（。）」", "Old English", "blōstm (flower, blossom)", "A flower or a mass of flowers on a tree or bush", "ただ（。の（。花（。では（。なく（。、命（。が（。内側（。から（。烈（。しく「溢（。れ（。出し（。プロ（。ス（。ト）輝（。く（。）」こと（。。（。その（。眩（。し（。い（。一瞬の（。為（。だけに（。、植物は（。全（。力を（。懸（。けて（。生き（。て（。いる（。のですよ。"),
    ("petal", "Petal", "花弁、花びら", "18th Century", "petalon (leaf, spread out)", "Each of the segments of the corolla of a flower, which are modified leaves and are typically colored", "花（。を（。包む「薄（。い（。板（。ペタロン）」のような（。、精（。緻（。な（。る（。ヴェール（。。（。一枚（。いち（。ま（。い（。の（。震（。えが（。、美し（。い（。調和（。という名の（。、宇宙の（。設計図を（。描き出す（。のです。"),
    ("nectar", "Nectar", "蜜、ネクタル、甘露", "16th Century", "nek- (death) + -tar (overcoming)", "A sugary fluid secreted within flowers to encourage pollination by insects and other animals", "ただの（。甘（。い（。汁で（。は（。なく（。、「死（。ネク）を（。打ち破（。る（。タル）」ための（。、生命（。の（。エッセンス（。。（。神々（。の（。飲み物（。として（。、かつて（。は（。崇（。め（。られ（。て（。いた（。のですよ。"),
    ("canopy", "Canopy", "林冠、天蓋（てんがい）、キャノピー", "14th Century", "konops (mosquito)", "An ornamental cloth covering hung or held over a throne, berth, or bed", "かつて（。は「蚊帳（。カノポス）」だった（。もの（。が（。、今では（。森の（。頂を（。覆う（。、緑（。の（。聖壇へと（。変貌（。した（。姿（。。（。大地と（。天を（。繋ぐ（。、透明な（。境界。"),
    ("prairie", "Prairie", "大草原、プレーリー", "18th Century", "pratum (meadow)", "A large open area of grassland", "地（。平線（。まで（。続く「草原（。プラタム）」。（。風（。が（。吹き（。抜（。けるたびに（。、無数（。の（。命の（。囁（。きが（。、波波の（。ように（。押し寄（。せて（。くる（。、自由（。な（。る（。空間。"),
    ("marsh", "Marsh", "沼沢地、湿原、マーシュ", "Old English", "merisc (marshy, literal: 'of the sea')", "An area of low-lying land which is flooded in wet seasons or at high tide, and typically remains waterlogged at all times", "陸（。と（。海（。の（。境界（。に（。ある「水（。浸（。し（。メリスク）の（。大地」。（。そこ（。には（。、混沌（。と（。生命（。が（。混ざり（。合い（。、全（。く（。新（。しい（。物語が（。産（。み（。出さ（。れる（。、豊（。饒（。な（。る（。淵。"),
    ("reef", "Reef", "岩礁、礁（しょう）、リーフ", "16th Century", "rif (rib)", "A ridge of jagged rock, coral, or sand just above or below the surface of the sea", "海（。の（。底（。に（。横たた（。わる「肋（。骨（。リフ）』のような（。岩石（。。（。寄（。せ（。来る（。波を（。受け（。止め（。、静（。か（。な（。る（。入り（。江（。を（。創（。り出（。す（。、大地の（。守護。"),
    ("glacier", "Glacier", "氷河、グレイシャー", "18th Century", "glacies (ice)", "A slowly moving mass or river of ice formed by the accumulation and compaction of snow on mountains or near the poles", "数（。千（。万年（。という（。時間の（。流れを（。、「氷（。グラ）」の（。中に（。閉じ込（。めた（。、沈黙（。の（。大河（。。（。その（。一歩（。の（。進みは（。、いかなる（。文明（。の（。騒（。が（。し（。さ（。をも（。、無（。に（。還（。す（。のです。"),
    ("canyon", "Canyon", "峡谷、大峡谷、キャニオン", "19th Century", "cañun (tube, pipe, literal: 'reed')", "A deep gorge, typically one with a river flowing through it", "悠（。久（。の（。時（。を（。かけて（。、水（。が（。大地を（。穿（。ち（。抜いた「巨大（。な（。管（。管（。）」。（。そこ（。には（。、地層（。という（。名の（。、時間の（。断（。層（。が（。、美し（。く（。刻ま（。れて（。いる（。の（。ですよ。"),
    ("grotto", "Grotto", "小さな洞窟、グロット", "16th Century", "krupte (crypt, hidden place)", "A small picturesque cave, especially an artificial one in a park or garden", "暗い（。地下（。の「隠（。れた（。クリプ）場所（。）」。（。そこ（。に（。滴る（。一滴（。の（。水（。は（。、宇宙の（。深（。遠（。な（。智慧（。を（。、言葉を（。超（。え（。て（。伝えて（。くれる（。のですよ。"),
    ("puddle", "Puddle", "水たまり、パドル", "13th Century", "pudd (ditch, hole)", "A small pool of liquid, especially of rain water on the ground", "泥（。まみれ（。の（。大地（。に（。、不（。意（。に（。現（。れ（。た「小さな（。淵（。パッド）」。（。その（。濁った（。水面（。にも（。、天上（。の（。青い（。光が（。、等しく（。宿って（。いる（。のです。"),
    ("typhoon", "Typhoon", "台風、タイフーン", "16th Century", "tuphon (whirlwind, giant with wind powers)", "A tropical storm in the region of the Indian or western Pacific oceans", "「巨大（。な（。風の（。神（。テュポーン）」が（。、目（。覚（。め（。て（。舞（。い（。踊（。る（。姿（。。（。全（。て（。の（。偽善を（。吹（。き（。飛ば（。し（。、大地に（。新（。しい（。秩序（。を（。敷（。き（。直（。す（。ために。"),
    ("halo", "Halo", "後光、ハロー、暈（かさ）", "16th Century", "halos (threshing floor, literal: 'round threshing floor')", "A circle of light shown around or above the head of a holy person", "かつて（。は「丸い（。脱（。穀（。場（。）」だった（。かたち（。。（。光（。り（。輝（。く（。聖性（。が（。、円（。を描い（。て（。溢（。れ（。出し（。た（。とき（。、私たちは（。そこに（。神（。の（。影（。を見（。る（。のですよ。"),
    ("ore", "Ore", "鉱石、粗金（あらがね）", "Old English", "āra (brass, copper, bronze)", "A naturally occurring solid material from which a metal or valuable mineral can be profitably extracted", "ただの（。石（。から（。、「金属（。アーラ）」と（。なる（。ための（。純粋（。な（。エッセンスを（。孕（。ん（。だ（。、不器（。用（。な（。存在（。。（。火（。に（。焼（。かれ（。、打（。た（。れる（。ことで（。、至宝（。へと（。至（。る（。の（。ですよ。"),
    ("molecule", "Molecule", "分子、モレキュール", "18th Century", "moles (mass) + -cula (little)", "A group of atoms bonded together, representing the smallest fundamental unit of a chemical compound that can take part in a chemical reaction", "物体（。を（。構成（。する「小さな（。クーラ）塊（。モー）」。（。目（。には（。見えない（。極（。微（。な（。世界で（。、彼（。らは（。絶（。え（。間（。なく（。踊（。り（。続け（。、世界（。を（。形（。作（。って（。いる（。のですよ。")
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
            word_id = f"{word_text.lower()}_nature_iv"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "自然は、私たちが自らの本質を思い出すための、巨大な鏡なのです。",
                    "example": f"The cherry trees were in full {word_text}, attracting visitors from all over the country.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["生命とは、ただの生存の連鎖ではなく、宇宙が自らを知るための、眩しい実験なのです。"]
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

        print(f"Success: Added {added_count} words. Theme: Flora & Fauna (Cycle 51).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
