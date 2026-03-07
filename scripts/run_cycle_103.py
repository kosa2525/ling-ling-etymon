import json
import re

# Theme: The Alchemy of Germ & Genesis (Cycle 103)
words_data = [
    ("germ", "Germ", "萌芽、起源、微生物、ジャーム", "16th Century", "germen (sprout, seed, literal: 'seed')", "A portion of an organism capable of developing into a new one or part of one", "潜（。在（。する（。巨大（。な（。る（。エナジーを、一（。点（。に「閉じ（。込（。め（。た（。芽（。ジャーム）』。（。その（。小（。さな（。る（。欠片（。の中に、宇宙（。の（。全記録（。が（。、静（。か（。に（。、横（。たわ（。って（。いる（。のですよ。"),
    ("genesis", "Genesis", "創世記、起源、ジェネシス", "14th Century", "gignesthai (to be born, literal: 'generation')", "The origin or mode of formation of something", "全（。ての（。物（。語が、至高の（。る（。力によって「産声を（。上げた（。ジェネシス）』、峻（。烈（。な（。る（。爆発（。（。その（。一一点（。から、宇宙（。の（。全（。幾（。何（。学（。が、美し（。く（。、拓（。か（。れ（。て（。いく（。のですよ。"),
    ("bud", "Bud", "つぼみ、バッド", "14th Century", "Middle English budde (related to Dutch bot 'bud')", "A compact knoblike growth on a plant that develops into a leaf, flower, or shoot", "静（。か（。に（。、想いを（。一（。つに（。凝縮（。させた（。、「眩（。し（。い（。る（。る（。可能性（。バッド）』。（。その（。閉じ（。られた（。る（。沈黙（。の中にこそ（。、真実（。の（。る（。開（。花が、宿（。って（。いる（。の（。ですよ。"),
    ("bloom", "Bloom", "開花、真っ（。盛り（。、ブルーム", "12th Century", "blōma (flower, blossom, literal: 'flower')", "A flower, especially one cultivated for its beauty", "魂（。の（。エナジーが、一（。気へと「外へと（。開（。い（。た（。ブルーム）』、至高の（。る（。る（。輝き（。（。その（。圧倒（。的な（。る（。美（。しさに（。、世界（。は（。、一瞬（。にして（。、祝（。福（。さ（。れ（。ます。"),
    ("blossom", "Blossom", "花、開花、ブロッサム", "Old English", "blōstm (flower, blossom, literal: 'blossom')", "A flower or a mass of flowers on a tree or bush", "木（。々（。が（。、至高の（。る（。力を（。得（。て「至高の（。る（。冠（。ブロッサム）』を（。戴（。く（。こと（。（。その（。瑞々（。し（。い（。る（。生命の（。鼓動を、魂で、感（。じ（。て（。ください。"),
    ("fruit", "Fruit", "果実、成果、フルーツ", "12th Century", "frui (to enjoy, literal: 'enjoyable thing')", "The sweet and fleshy product of a tree or other plant that contains seed and can be eaten as food", "沈黙の（。果てに（。、魂が（。結（。び（。、産（。んだ「至高の（。る（。甘（。露（。フルーツ）』。（。その（。豊饒（。な（。る（。真実を、誇り（。高く、噛（。み（。締（。め（。な（。さい。"),
    ("harvest", "Harvest", "収穫、ハーベスト", "Old English", "hærfest (autumn, harvest time, literal: 'picking time')", "The process or period of gathering in crops", "時間の（。る（。回（。廊（。を（。、峻（。烈（。に（。駆け（。抜（。け（。た（。物（。語が「至高（。の（。る（。完成（。ハーベスト）』へと（。、至（。る（。瞬間（。（。その（。豊かな（。る（。の（。る（。沈黙（。こそが、宇宙（。の（。る（。答え（。です。"),
    ("stock", "Stock", "蓄え、株、ストック", "Old English", "stoc (tree trunk, stem, literal: 'trunk, stem')", "The goods or merchandise kept on the premises of a business or warehouse and available for sale or distribution", "魂の（。峻（。烈（。な（。る（。る「中（。軸（。ストック）』。（。そこに（。蓄え（。られた（。真実（。の（。エナジーが、いつか（。、巨大（。な（。る（。枝（。葉を、広（。げ（。て（。いき（。ます。")
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
            word_id = f"{word_text.lower()}_potential"
            
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
                    "thinking": item[6] if len(item) > 6 else "可能性とは、外部に答えを求めることではありません。自らの内側にある沈黙の種子が、時間の重みに耐えきれなくなって、未知という名の花を咲かせる瞬間なのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "萌芽は、力強く大地を押し上げる。それは、自らの存在を肯定し、宇宙の光へと手を伸ばそうとする、魂の最も純粋な意志なのです。",
                    "example": f"The scientist studied the minute {word_text} that eventually developed into a complex neural network within the experimental organism.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["成果を急がないでください。種が土の中で沈黙を守るように、あなたも自らの深淵で、真実が熟成されるのを待つのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Germ & Genesis (Cycle 103).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
