import json
import re

# Theme: The Alchemy of Velvet & Gossamer (Cycle 118)
words_data = [
    ("velvet", "Velvet", "天鵞絨（。てんがじゅう（。）」、ビロード、ベルベット", "14th Century", "villus (shaggy hair, literal: 'shaggy')", "A closely woven fabric of silk, cotton, or nylon, that has a thick short pile on one side to make it feel very soft"),
    ("gossamer", "Gossamer", "薄いクモの糸、繊細なもの、ゴッサマー", "14th Century", "gose (goose) + summer (summer, literal: 'goose summer')", "A fine, filmy substance consisting of cobwebs spun by small spiders, typically seen in autumn"),
    ("satin", "Satin", "繻子（。しゅす（。）」、サテン", "14th Century", "Zaitun (Quanzhou, a port in China, literal: 'from Zaitun')", "A smooth, glossy fabric, typically of silk, produced by a weave in which the threads of the warp are caught and looped by the weft only at certain intervals"),
    ("lace", "Lace", "レース、ひも、レース", "13th Century", "laqueus (noose, snare, literal: 'snare')", "A fine open fabric of cotton or silk, made by looping, twisting, or knitting thread in patterns and used especially for trimming garments"),
    ("ribbon", "Ribbon", "リボン、飾り紐（。、リボン", "14th Century", "Middle English riban (related to Old French riban 'ribbon')", "A long, narrow strip of fabric, used especially for tying something or for decoration"),
    ("canvas", "Canvas", "キャンバス、帆布、カンバス", "14th Century", "cannabis (hemp, literal: 'made of hemp')", "A strong, coarse unbleached cloth made from hemp, flax, cotton, or a similar yarn, used to make items such as sails and tents and as a surface for oil painting"),
    ("linen", "Linen", "リネン、亜麻（。あま（。）」、リネン", "14th Century", "linum (flax, literal: 'made of flax')", "Cloth woven from flax"),
    ("wool", "Wool", "羊毛、毛、ウール", "Old English", "wull (wool, literal: 'fleece')", "The fine, soft, curly or wavy hair forming the coat of a sheep, goat, or similar animal"),
    ("cotton", "Cotton", "綿、コットン", "14th Century", "al-qutn (cotton, literal: 'the cotton')", "A soft white fibrous substance that surrounds the seeds of a tropical and subtropical plant and is used as textile fiber and in thread for sewing"),
    ("felt", "Felt", "フェルト、不織布", "Old English", "felt (related to West Germanic felt 'felt')", "A kind of cloth made by rolling and pressing wool or another suitable textile together, with moisture or heat, which causes the constituent fibers to mat together to create a smooth surface")
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
            word_id = f"{word_text.lower()}_silk_iii"
            
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
                    "thinking": item[6] if len(item) > 6 else "柔らかさとは、弱さではありません。どんなに強い力に対しても、自らをしなやかに変容させ、その衝撃さえも美しき余韻に変えてしまう、魂の絶対的なる品位なのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "糸を紡ぎ、布を織ることは、祈りを形にすること。あなたが日々の暮らしの中で丁寧に紡ぎ出す想いが、いつか世界を優しく包み込む、至高のる衣裳となるのですよ。",
                    "example": f"The curtains, crafted from the finest {word_text}, shimmered softly in the evening twilight, casting long and elegant shadows across the marble floor of the grand library.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["繊細なものに目を向けることは、宇宙の細部を愛でること。蜘蛛の糸一本に宿る美しさに、ただ魂で、感謝を捧げるのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Velvet & Gossamer (Cycle 118).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
