import json
import re

# Theme: The Alchemy of Paradox & Oxymoron (Cycle 105)
words_data = [
    ("oxymoron", "Oxymoron", "撞着語法、反対語の組み合わせ、オクシモロン", "17th Century", "oxus (sharp) + mōros (foolish, literal: 'sharp-foolish')", "A figure of speech in which apparently contradictory terms appear in conjunction", "「鋭（。く（。オクス）愚（。か（。な（。モーロス）』至高の（。る（。均衡（。（。相反（。する（。二（。つの（。エナジーを、一一点で（。繋（。ぎ（。止める（。とき（。、物（。語（。は、盤石（。な（。る（。る（。真実へと、昇（。華（。さ（。れ（。ます。"),
    ("irony", "Irony", "皮肉、逆説的状況、アイロニー", "16th Century", "eirōneia (dissimulation, feigned ignorance, literal: 'pretending')", "The expression of one's meaning by using language that normally signifies the opposite, typically for humorous or emphatic effect", "表面（。的な（。る「偽（。装（。アイロ）』の下（。に、至高の（。る（。真実を、そっと（。仕（。舞（。う（。こと（。（。その（。峻（。烈（。な（。る（。逆（。説（。の中にこそ（。、魂（。の（。る（。瑞々（。し（。い（。智慧（。が、宿（。って（。いる（。のですよ。"),
    ("satire", "Satire", "風刺、サタイア", "16th Century", "satura (poetic medley, food mixture, literal: 'full/mixed dish')", "The use of humor, irony, exaggeration, or ridicule to expose and criticize people's stupidity or vices, particularly in the context of contemporary politics and other topical issues", "世界を（。一つの「混合（。料理（。サツラ）』として、峻（。烈（。な（。る（。笑（。いの（。中で。調理（。する（。こと（。（。その（。眩（。し（。い（。ほど（。に（。鋭（。利な（。る（。視座が、不（。条理を、光へと、変えます。"),
    ("parody", "Parody", "パロディ、模倣風刺", "16th Century", "para- (beside) + ōidē (song, literal: 'singing beside')", "An imitation of the style of a particular writer, artist, or genre with deliberate exaggeration for comic effect", "真実の（。る（。る（。旋（。律に「寄り（。添（。う（。パラ）歌（。オデイ）』。（。その（。美し（。き（。残像の中にこそ（。、本来の（。る（。煌（。めきは、永遠に（。、保存（。さ（。れ（。て（。いく（。のですよ。"),
    ("allegory", "Allegory", "寓意、アレゴリー", "14th Century", "allos (other) + agoreuein (to speak, literal: 'speaking otherwise')", "A story, poem, or picture that can be interpreted to reveal a hidden meaning, typically a moral or political one", "真理（。をを、峻（。烈（。な（。る「他（。の（。物語（。アロス）』の中に（。封（。じ（。込（。め（。て（。、静（。か（。に（。語（。る（。こと（。（。その（。多（。層（。的（。な（。る（。沈黙を、魂で、読み（。解（。い（。て（。ください。")
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
            word_id = f"{word_text.lower()}_paradox"
            
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
                    "thinking": item[6] if len(item) > 6 else "逆説とは、矛盾ではありません。一つの真理が、あまりにも巨大すぎるために、私たちの限定された視点からは、正反対の二つの相として見えているだけのことなのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "鋭い愚かさを愛することは、完璧であることよりも、はるかに困難で、そして美しい行為なのですよ。",
                    "example": f"The author used a clever {word_text} to highlight the complex relationship between technological progress and the loss of human connection in the modern era.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["偽装の下にある真実を見抜くこと。それは、世界という名の巨大な皮肉を、至高のる知恵で微笑みながら受け入れるということなのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Paradox & Oxymoron (Cycle 105).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
