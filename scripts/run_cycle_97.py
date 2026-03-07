import json
import re

# Theme: The Alchemy of Reclusion & Reminiscence (Cycle 97)
words_data = [
    ("reclusion", "Reclusion", "隠遁、隔離、リクルージョン", "15th Century", "re- (back) + claudere (to close, literal: 'closed back')", "The state of being recluse; retirement or seclusion from the world", "喧（。騒（。の（。世界（。を（。完全（。に「閉（。じ（。た（。リク）』、至高の（。る（。孤独（。（。あなたが（。その（。沈黙の（。回廊を（。、一一人（。で（。歩（。む（。とき、宇宙（。の（。深（。淵（。な（。る（。囁（。きが、眩（。しい（。ほど（。に（。、響（。き（。渡る（。のですよ。"),
    ("reminiscence", "Reminiscence", "追憶、回想、レミニセンス", "16th Century", "re- (again) + memini (to remember, literal: 'remembering again')", "A story told about a past event remembered by the narrator", "遥（。かな（。る（。過去（。の（。欠片（。を、再び「心で（。愛（。で（。る（。レミニ）』こと（。（。その（。眩（。し（。い（。残像が（。ある（。から（。こそ（。、現在（。という（。名の（。孤独（。は、美し（。い（。調べへと（。変元（。り（。ます。"),
    ("hermit", "Hermit", "隠者、仙人、ハーミット", "12th Century", "erēmitēs (living in the desert, literal: 'of the desert')", "A person living in solitude as a religious discipline", "広大（。な（。る「砂（。漠（。エレミ）』の（。如（。き（。沈黙を、自（。らの（。糧（。に（。し（。た（。峻（。烈（。な（。る（。魂（。（。その（。孤（。高（。な（。る（。沈黙に、あなた（。は（。、何（。を（。、視（。る（。の（。でしょうか。"),
    ("monk", "Monk", "修道士、僧侶、モンク", "Old English", "monakhos (solitary, literal: 'single')", "A member of a religious community of men typically living under vows of poverty, chastity, and obedience", "ただ（。一（。つ（。の（。真理（。を（。追い（。求（。め（。て、「唯（。一（。の（。モノ）』存在へと（。自らを（。、変（。じ（。た（。者たち（。（。その（。静（。か（。な（。る（。る（。祈りが（。、世界（。を（。、至高（。の（。る（。調和（。へと（。導（。い（。て（。いる（。のですよ。"),
    ("novice", "Novice", "初心者、修練生、ノービス", "14th Century", "novus (new, literal: 'new person')", "A person new to or inexperienced in a field or situation; a person who has entered a religious order and is under probation, before taking vows", "全（。てが（。眩（。し（。い「新（。し（。さ（。ノヴァ）』の中に（。在（。る（。こと（。（。その（。一一点（。の（。純粋（。な（。る（。驚き（。を、一生（。涯（。、魂の（。中で（。、飼い（。馴ら（。し（。て（。いて（。ください。"),
    ("youth", "Youth", "青年、若さ、ユース", "Old English", "geoguð (youth, literal: 'quality of being young')", "The period between childhood and adult age; the qualities of vigor, freshness, immaturity, etc., associated with being young", "命の（。エナジーが、峻（。烈（。に「眩（。し（。く（。煌（。め（。く（。ユース）』一一点（。（。その（。危（。う（。い（。ほどの（。る（。飛躍が（。、あなた（。を、宇宙の（。真実（。へと（。、一（。気へと（。、押し（。上げ（。ます。"),
    ("adult", "Adult", "大人、成人、アダルト", "16th Century", "alere (to nourish, literal: 'grown up')", "A person who is fully grown or developed; mature", "魂を（。至高の（。る（。智慧で「育（。て（。上げた（。アダ）』、完結（。し（。た（。る（。一一点（。（。その（。静（。か（。な（。る（。る（。責任（。を、誇り（。高く、その（。背中に、担（。い（。続け（。な（。さい。"),
    ("elder", "Elder", "長老、先輩、エルダー", "Old English", "eldra (older, literal: 'older person')", "A person of a greater age than someone else", "遥（。かな（。る（。時間の（。る（。積（。層を（。、魂に「刻（。み（。付け（。た（。エルダ）』至高の（。る（。る（。象（。徴。（。その（。一一つ（。一一つ（。の（。る（。の（。る（。る（。皺（。の中に、宇宙（。の（。全記憶が、宿ります。"),
    ("target", "Target", "目標、標的、ターゲット", "14th Century", "targe (shield, literal: 'little shield')", "A person, object, or place selected as the aim of an attack", "全（。ての（。意志を、一（。つ（。に（。凝縮（。さ（。せ（。た「至高の（。る（。中心（。タール）』。（。その（。一一点（。を（。視（。つ（。める（。とき（。、あなた（。は（。、真実（。の（。る（。る（。矢へと、変（。容（。し（。ます。"),
    ("spring", "Spring", "春、泉、バネ、スプリング", "Old English", "springan (to leap, burst forth, literal: 'bursting forth')", "A place where water or oil wells up from an underground source, or the season in which vegetation begins to appear", "深淵（。から、エナジーが（。一（。気へと「跳（。ね（。出した（。スプリン）』至高の（。る（。る（。瑞々（。し（。さ（。（。その（。始（。ま（。り（。の（。眩（。し（。い（。余韻を、魂で、感（。じ（。て（。ください。"),
    ("source", "Source", "源、情報源、ソース", "14th Century", "surgere (to rise, literal: 'rising up')", "A place, person, or thing from which something comes or can be obtained", "命の（。奔（。流（。が「湧（。き（。上が（。った（。ソース）』、峻（。烈（。な（。る（。起点（。（。その（。一（。つの（。点（。にこそ（。、全（。ての（。物（。語が、静（。か（。に（。、横（。たわ（。って（。いる（。のですよ。")
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
            word_id = f"{word_text.lower()}_solitude"
            
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
                    "thinking": item[6] if len(item) > 6 else "孤独とは、誰とも繋がっていないことではありません。自分という名の宇宙の中に、無限の対話の伴侶を見出すことなのです。",
                    "aftertaste": item[7] if len(item) > 7 else "追憶は、過去への逃避ではありません。今の自分を形成している、目に見えない光の糸を、一本ずつ丁寧に手繰り寄せる行為なのですよ。",
                    "example": f"The philosopher chose a life of {word_text} and reflection in a remote mountain cabin to complete his final works in peace.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["泉のように湧き出す想いを大切に。その瑞々しさが枯れない限り、あなたという物語は永遠に続くのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Reclusion & Reminiscence (Cycle 97).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
