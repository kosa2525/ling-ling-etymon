import json
import re

# Theme: The Alchemy of Orbit & Galaxy (Cycle 91)
words_data = [
    ("orbit", "Orbit", "軌道、オービット", "16th Century", "orbita (track, literal: 'wheel track')", "The curved path of a celestial object or spacecraft around a star, planet, or moon", "定められた（。数（。学（。を（。、峻（。烈（。に（。、回（。り（。続ける（。、「光の（。轍（。オービタ）』。（。その（。終（。わ（。り（。な（。き（。回（。帰の中に、自ら（。の（。義務を（。、誇（。り（。高く、捧（。げ（。切って（。ください。"),
    ("cluster", "Cluster", "房、集団、星団、クラスター", "Old English", "clyster (cluster, literal: 'clump')", "A group of similar things or people positioned or occurring closely together", "バラバラ（。の（。命を、一（。つ（。の（。場所に「寄（。せ（。集（。めた（。クラスター）』、眩（。し（。い（。煌（。めき。（。個（。々が（。、互（。いに（。を（。高（。め（。合い（。、至高（。の（。る（。輝（。きを（。、産（。声を（。上げます。"),
    ("comet", "Comet", "彗星、コメット", "13th Century", "komētēs (long-haired, literal: 'long-haired star')", "A celestial object consisting of a nucleus of ice and dust and, when near the sun, a 'tail' of gas and dust particles pointing away from the sun", "宇宙を（。峻（。烈（。に（。駆け（。抜（。け（。る（。、「美（。し（。い（。髪（。コメテ）の（。星（。』。（。その（。一瞬の（。閃光（。が、日常の（。沈黙（。を（。、鮮（。やかに（。、塗り（。替（。えて（。いく（。のですよ。"),
    ("meteor", "Meteor", "流星、メテオ", "16th Century", "meta- (above) + -oros (lifting, literal: 'thing high in the air')", "A small body of matter from outer space that enters the earth's atmosphere, becoming incandescent as a result of friction and appearing as a streak of light", "遥（。かな（。る（。高い（。空（。から、「峻（。烈（。に（。降（。り注（。ぐ（。メテオ）』光のエナジー。（。その（。燃（。え（。尽（。き（。る（。瞬間に（。、魂（。の（。真実（。が（。、美し（。く（。凝縮（。さ（。れ（。て（。いる（。のですよ。"),
    ("planet", "Planet", "惑星、プラネット", "Old English", "planētēs (wanderer, literal: 'wandering star')", "A celestial body moving in an elliptical orbit around a star", "一（。つ（。の（。場所に（。留（。まる（。のを（。拒み（。、ただ「彷（。徨（。い（。続ける（。プラネ）』至高の（。星（。（。その（。不（。安（。定な（。る（。旅路が（。、宇宙の（。深（。淵（。を（。、静（。か（。に（。物語（。っ（。て（。いる（。の（。ですよ。"),
    ("gale", "Gale", "強風、突風、ゲイル", "16th Century", "Origin uncertain, possibly related to Old Norse galinn (crazy, frantic)", "A very strong wind", "静寂を（。一（。瞬にして（。、峻（。烈（。な「狂（。気（。の（。嵐（。ゲイル）』に（。変える（。エナジー。（。その（。圧倒（。的な（。る（。力（。の（。前に（。、あなた（。は（。、ただ（。、魂を（。、委（。ね（。る（。のですよ。"),
    ("cosmic", "Cosmic", "宇宙の、コズミック", "17th Century", "kosmos (order, world, literal: 'orderly')", "Relating to the universe or cosmos, especially as distinct from the earth", "全（。てが（。、美（。し（。い「秩（。序（。コズモ）』の中に（。在（。る（。こと（。。（。その（。巨大（。な（。る（。幾何（。学こそ（。、私たちが（。帰（。る（。べき、至高（。の（。る（。真実（。なの（。ですよ。"),
    ("celestial", "Celestial", "天の、至高の、セレスティアル", "14th Century", "caelum (sky, heaven, literal: 'of the sky')", "Positioned in or relating to the sky, or outer space as observed in astronomy", "地上の（。濁（。りを（。、完全（。に（。脱（。し（。た「天（。上の（。セレス）』存在（。（。その（。峻（。烈（。な（。る（。透明（。さが（。、あなた（。を、至高（。の（。る（。者へと（。、誘（。う（。の（。ですよ。"),
    ("stellar", "Stellar", "星の、恒星の、ステラ", "17th Century", "stella (star)", "Relating to a star or stars", "自ら（。エナジーを（。、一（。点（。に（。凝縮（。さ（。せ（。た「至高（。の（。星（。ステラ）』。（。その（。揺（。る（。ぎ（。な（。い（。る（。一点（。の（。輝きが、暗（。黒（。の（。宇宙を、静（。か（。に（。守（。って（。いる（。のです。"),
    ("solar", "Solar", "太陽の、ソーラー", "15th Century", "sol (sun)", "Relating to or determined by the sun", "全（。ての（。命（。の（。源（。である「至高の（。光（。ソル）』。（。あなたが（。その（。エナジーを（。、全身で（。浴び（。る（。とき、魂は（。、再（。び（。新（。しい（。生（。を、手（。に（。入れ（。ます。"),
    ("lunar", "Lunar", "月の、太陰の、ルナ", "15th Century", "luna (moon)", "Relating to, or determined by the moon", "夜の（。沈黙（。を（。、優（。しく（。照らす「眩（。しい（。微（。笑（。み（。ルナ）』。（。その（。満（。ち（。欠（。け（。る（。物（。語（。の中に、宇宙の（。深（。淵（。な（。る（。記憶が（。、宿（。って（。いる（。のです。"),
    ("astral", "Astral", "星の、幽体（。の（。、アストラル", "17th Century", "astron (star)", "Relating to the stars", "物質の（。檻を（。越え（。た（。、「至高の（。煌（。めき（。アストラ）』。（。その（。眩（。し（。い（。魂の（。粒子（。が（。、今（。も、宇宙の（。すみ（。ず（。み（。まで、響（。き（。渡（。って（。いる（。のですよ。"),
    ("vacuum", "Vacuum", "真空、空白、バキューム", "16th Century", "vacuus (empty, literal: 'emptiness')", "A space entirely devoid of matter", "全（。て（。の（。存在を、峻（。烈（。に（。拒んだ「絶対（。的（。な（。る（。虚無（。バキュ）』。（。その（。究極の（。る（。沈黙が（。ある（。から（。こそ（。、新しい（。物（。語が（。、産（。声を（。上げます。"),
    ("infinite", "Infinite", "無限の、インフィニット", "14th Century", "in- (not) + finis (end, literal: 'not ending')", "Limitless or endless in space, extent, or size; impossible to measure or calculate", "どこ（。まで（。も「終（。わり（。のない（。イン・フィニ）』、至高の（。る（。広（。野（。（。その（。測（。り（。知れ（。な（。い（。る（。奥行きの中にこそ（。、真実（。の（。自由が（。、宿ります。"),
    ("grand", "Grand", "壮大な、偉大な、グランド", "15th Century", "grandis (big, great, full-grown, literal: 'big')", "Magnificent and imposing in appearance, size, or style", "小（。さな（。る（。作為を（。越元（。た（。、「圧倒（。的（。な（。る（。巨大（。さ（。グラン）』。（。その（。峻（。烈（。な（。る（。存在（。感に（。、人々は（。、ただ（。、畏（。敬（。の（。念を（。抱（。く（。のですよ。")
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
            word_id = f"{word_text.lower()}_expand"
            
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
                    "thinking": item[6] if len(item) > 6 else "拡張とは、外側に領土を広げることではありません。内側の沈黙を深め、全宇宙との共鳴を自覚する行為なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "銀河は、星々が孤独を分かち合うために創り出した、光の巡礼路なのですよ。",
                    "example": f"The spacecraft entered a stable {word_text} around the massive gas giant, beginning its long-term scientific mission.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["無限を数えようとするのではなく、今この瞬間にある有限の煌めきを愛でてください。そこにこそ、真の宇宙が宿っているのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["cosmic", "celestial", "stellar", "solar", "lunar", "astral", "infinite", "grand"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Orbit & Galaxy (Cycle 91).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
