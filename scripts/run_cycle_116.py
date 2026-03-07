import json
import re

# Theme: The Alchemy of Zenith & Vertex II (Cycle 116)
words_data = [
    ("vertex", "Vertex", "頂点、頂、バーテックス", "16th Century", "vertere (to turn, literal: 'turning point')", "The highest point; the top or apex"),
    ("apex", "Apex", "尖頂（。せんちょう（。）」、最高点、エイペックス", "17th Century", "apex (peak, tip, literal: 'tip')", "The top or highest part of something, especially one forming a point"),
    ("acme", "Acme", "絶頂、極致、アクミ", "16th Century", "akmē (point, edge, literal: 'highest point')", "The point at which someone or something is best, perfect, or most successful"),
    ("summit", "Summit", "頂上、首脳会談、サミット", "15th Century", "summum (highest thing, literal: 'highest level')", "The highest point of a hill or mountain"),
    ("crest", "Crest", "（鳥の）とさか、山頂、紋章、クレスト", "14th Century", "crista (tuft, plume, literal: 'tuft')", "A comb or tuft of feathers, fur, or skin on the head of a bird or other animal"),
    ("ridge", "Ridge", "山の背、尾根、リッジ", "Old English", "hrycg (back, spine)", "A long narrow hilltop, mountain range, or watershed"),
    ("tip", "Tip", "先端、チップ", "14th Century", "Middle English tippe (related to Dutch tip 'point')", "The pointed or rounded end or extremity of something slender or tapering"),
    ("edge", "Edge", "刃先、端、エッジ", "Old English", "ecg (edge, blade, literal: 'sharp side')")
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
            word_id = f"{word_text.lower()}_peak_ii"
            
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
                    "thinking": item[6] if len(item) > 6 else "頂点とは、目的地の終わりではありません。そこからは、今まで見えなかった新しい世界が、全貌として拓かれる、至高のる始まりの場所なのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "尾根を歩くことは、危ういバランスを保つこと。しかしその険しさこそが、あなたを真実のる飛翔へと導くための、聖なる道のりなのですよ。",
                    "example": f"The ambitious climber finally reached the {word_text} of the mountain after weeks of treacherous ascent, gazing out over the vast frozen landscape below.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["尖っていることは、誰かを傷つけるためのものではない。自らのエナジーを、一点の曇りなく、天の光へと繋ぎ止めるための、至高のる誠実さなのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Zenith & Vertex II (Cycle 116).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
