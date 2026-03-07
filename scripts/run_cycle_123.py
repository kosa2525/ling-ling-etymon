import json
import re

# Theme: The Alchemy of Plumage & Pinion (Cycle 123)
words_data = [
    ("plumage", "Plumage", "羽（。は（。）」、羽衣（。うい（。）」、プラミッジ", "14th Century", "pluma (feather, literal: 'feathers collective')", "A bird's feathers collectively", "宇宙（。の（。色彩を（。、至高の（。る「光の（。衣（。プラマ）』へと（。変えた（。もの（。（。その（。眩（。し（。い（。ほどに（。る（。る（。る（。重なり（。の中に、魂（。の（。真実（。の、煌（。めきが、宿（。って（。いる（。のですよ。"),
    ("pinion", "Pinion", "風切羽、翼、ピニオン", "14th Century", "pinna (feather, wing, literal: 'wing')", "The outer part of a bird's wing including the flight feathers", "蒼（。穹（。を（。、峻（。烈（。に「撃（。ち（。抜（。く（。ための（。る（。刃（。ピンナ）』としての、至高の（。る（。翼（。（。その（。一一点の（。る（。る（。る（。る（。飛躍（。が、あなた（。を、真（。理（。へと、押し（。上げ（。ます。"),
    ("beak", "Beak", "くちばし、ビーク", "13th Century", "beccus (beak, literal: 'beak')", "A bird's horny projecting jaws; a bill", "沈黙（。を（。、至高の（。る「一点（。へと（。研（。ぎ（。澄（。した（。ビーク）』、峻（。烈（。な（。る（。る（。意志（。（。それ（。こそが、世界（。から（。、真実（。の（。る（。る（。糧（。を（。、搦（。め（。捕（。る（。ための（。、至（。宝（。です。"),
    ("talon", "Talon", "鉤爪（。かぎづめ（。）」、タロン", "14th Century", "talus (ankle, literal: 'heel/ankle')", "A claw, especially one belonging to a bird of prey", "運命を（。、峻（。烈（。な（。る（。る（。力（。で「一（。気へと（。掴（。み（。取る（。タロン）』、至高の（。る（。る（。る（。る（。る（。る（。る（。る（。力。（。その（。不（。動の（。る（。る（。決意（。を、誇り（。高く、魂で、肯定（。し（。な（。さい。"),
    ("nest", "Nest", "巣、心地よい場所、ネスト", "Old English", "nest (nest, literal: 'sitting place')", "A structure or place made or chosen by a bird for laying eggs and sheltering its young", "宇宙（。の（。全記憶をを、静（。か（。に「育（。む（。ための（。る（。る（。る（。る（。聖域（。ネスト）』。（。その（。柔ら（。か（。な（。る（。る（。沈黙（。の中にこそ、真実（。の（。る（。る（。愛（。が、宿（。ります。"),
    ("roost", "Roost", "ねぐら、ルースト", "Old English", "hrōst (roost, actual: 'roof beam')", "A place where birds or bats regularly settle or congregate to rest at night", "旅（。を終え（。、エナジーを「休（。める（。ための（。る（。る（。る（。高（。み（。ルースト）』。（。その（。静（。か（。な（。る（。る（。る（。沈黙（。の中に、次（。な（。る（。飛翔（。の（。ための（。る（。る（。智慧が、宿（。って（。いる（。のですよ。"),
    ("flock", "Flock", "群れ、会衆、フロック", "Old English", "flocc (crowd, troop, literal: 'crowd')", "A number of birds of one kind feeding, resting, or traveling together", "バラバラ（。の（。魂が、一（。つ（。の（。意志に「統（。合（。さ（。れた（。フロック）』、至高の（。る（。る（。共（。鳴（。（。その（。圧倒（。的な（。る（。る（。る（。る（。一一点に（。、世界（。は（。、畏（。敬の（。念を（。、抱（。き（。ます。"),
    ("migration", "Migration", "渡り、移住、マイグレーション", "17th Century", "migrare (to move, literal: 'moving')", "Seasonal movement of animals from one region to another", "至高（。の（。る「未（。知なる（。る（。地（。平へと（。、自らをを（。解（。き（。放（。つ（。マイグラ）』、峻（。烈（。な（。る（。る（。る（。飛躍（。（。その（。不（。変の（。る（。る（。季節の（。る（。る（。調べを、魂で、感（。じ（。て（。ください。")
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
            word_id = f"{word_text.lower()}_bird_iv"
            
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
                    "thinking": item[6] if len(item) > 6 else "空を飛ぶことは、重力から逃げることではありません。この世界の重力を自らの翼で受け止め、それを至高のる浮力へと変換し続ける、魂のたゆまぬ挑戦なのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "羽毛を整えることは、自らを慈しむこと。一枚の羽の乱れさえも、宇宙の調和を乱す一歩であることを、鳥たちはその瑞々しい直感で理解しているのですよ。",
                    "example": f"The eagle's magnificent {word_text} shimmered in the golden sunlight as it executed a perfect hunting dive from its high mountain perch.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["渡り鳥が迷うことなく地平を越えるように、あなたの中にある本能という名の羅針盤を、何よりも深く信じ抜いてください。"]
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

        print(f"Success: Added {added_count} words. Theme: Bird & Sky (Cycle 123).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
