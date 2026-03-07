import json
import re

# Theme: The Pulse of Ink & Paper (Cycle 54)
words_data = [
    ("codex", "Codex", "写本、法典、コーデックス", "16th Century", "caudex (trunk of a tree, book)", "An ancient manuscript text in book form"),
    ("parchment", "Parchment", "羊皮紙、パーチメント", "13th Century", "Pergamum (city in Asia Minor)", "A stiff, flat, thin material made from the prepared skin of an animal and used as a durable surface for writing, painting, or pocketing", "木（。簡を（。超え（。、動物の（。命を（。纏（。った「聖なる（。紙（。ペルガモン）」。（。そこ（。には（。、何（。百（。年（。という（。時間の（。荒波に（。耐（。え（。抜（。く（。、言葉（。の（。凄（。みが（。宿（。って（。いる（。のですよ。"),
    ("vellum", "Vellum", "上質（。じょうしつ（。）」羊皮紙、ヴェラム", "15th Century", "veal (calf)", "Fine parchment made originally from the skin of a calf", "さらに（。若（。い（。命の（。肌を（。使った（。、「至高の（。紙（。ヴェール（。）」。（。透（。き（。通（。る（。ような（。滑（。らかさと（。、強（。靭（。さを（。併（。せ（。持（。つ（。、王（。侯（。貴族（。の（。ための（。聖域。"),
    ("quill", "Quill", "（。鳥の（。）」羽（。ペン、羽軸、クイル", "16th Century", "kiel (quill, stalk, literal: 'stalk')", "A pen made from a main wing or tail feather of a large bird", "空（。を（。飛（。んでいた（。鳥の「一本の（。羽（。キール）』を（。、地上に（。真理を（。綴（。る（。ための（。杖（。へと（。変（。えた（。もの（。。（。その（。軽（。やかな（。一（。閃（。に（。、思考（。の（。風（。が（。宿（。る（。のですよ。"),
    ("stylus", "Stylus", "尖筆（。せんぴつ（。）」、レコード（。針、スタイラス", "18th Century", "stilus (stake, pale, literal: 'pointed stick')", "An ancient writing implement, consisting of a small rod with a pointed end for scratching letters on wax-covered tablets, and a blunt end for obliterating them", "蝋（。の（。板（。に（。、魂の（。エナジーを「突（。き（。刺（。す（。スティ）」ことで（。刻（。み（。込（。む（。、鋭（。い（。意志（。。（。その（。一一点（。に、宇宙（。の（。全記憶（。を（。凝縮（。させた（。、尖（。端（。の（。知性。"),
    ("inscription", "Inscription", "碑文、刻銘、インスクリプション", "14th Century", "in- (into, upon) + scribere (to write)", "Words inscribed, as on a monument or in a book", "ただ（。の（。紙に（。ではなく（。、石（。や（。金属の（。表面（。に「刻（。み（。込（。まれ（。た（。スクリプト）中（。イン）」もの（。。（。それは（。、消（。し（。去（。ること（。の（。できない（。、永遠（。への（。誓（。い（。の（。証（。なのです。"),
    ("epitaph", "Epitaph", "墓碑銘、エピタフ", "14th Century", "epi- (upon) + taphos (tomb, literal: 'on the tomb')", "A phrase or statement written in memory of a person who has died, especially as an inscription on a tombstone", "人生という（。物語が（。終わった（。後（。に（。、そっと「墓石の（。上へと（。エピ）置（。かれた（。）」最後（。の（。一行（。。（。死（。を（。越（。えた（。場所（。から（。届（。く（。、静（。かな（。る（。自己（。肯定。"),
    ("eulogy", "Eulogy", "追悼（。ついとう（。）」演説、賛辞、ユーロジー", "16th Century", "eu- (well) + logos (word, speaker, literal: 'praise')", "A speech or piece of writing that praises someone or something highly, typically someone who has just died", "去（。り（。行（。っ（。た（。魂に（。対して（。、「溢（。れ（。んばかりの（。良（。き（。ユー）言葉（。ロゴス）」を（。送（。る（。こと（。。（。悲（。し（。みを（。越（。えた（。場所（。にある（。、真（。な（。る（。人間（。への（。敬意。"),
    ("prologue", "Prologue", "序文、幕開け、プロローグ", "14th Century", "pro- (before, forward) + logos (word, story)", "A separate introductory section of a literary or musical work", "本（。題を（。語（。る（。、「前（。プロ）に（。置（。かれた（。ロゴス）」。静（。かな（。る（。期待（。と（。予感を（。孕（。み（。ながら（。、これから（。始まる（。巨大な（。宇宙へと（。、あなた（。を（。誘（。う（。のです。"),
    ("epilogue", "Epilogue", "結びの言葉、エピローグ", "15th Century", "epi- (upon, after) + logos (word)", "A section or speech at the end of a book or play that serves as a comment on or a conclusion to what has happened", "物語が（。収束（。した（。後、そっと「付け（。加え（。られた（。エピ）締めくくり（。の（。ロゴス）」。（。余韻（。を（。噛（。み（。締（。め（。ながら（。、日常（。へと（。還（。る（。ための（。、優（。し（。い（。通過（。点。"),
    ("glossary", "Glossary", "用語集、グロッサリー", "14th Century", "glossa (tongue, language, foreign word, literal: 'tongue')", "An alphabetical list of terms in a particular domain of knowledge with the definitions for those terms", "全（。てを（。語（。る（。のではなく（。、難解（。な「言葉（。グロッサ）」だけ（。を（。集（。めた（。、知性の（。鍵（。束（。。（。そこ（。には（。、未知（。なる（。領域（。へと（。漕（。ぎ（。出す（。ための（。、最小（。の（。地図（。が（。あります。"),
    ("footnote", "Footnote", "脚注、フットノート", "18th Century", "foot + note", "An additional piece of information printed at the bottom of a page", "思考の（。本流（。から（。一瞬（。外れ（。、頁の「足下（。フット）」へと（。そっと（。置（。かれた（。密（。かな（。囁（。き（。。（。そこ（。にこそ（。、著者（。の（。真（。実（。の（。想（。いが（。、隠（。されて（。いる（。の（。かも（。しれ（。ません。"),
    ("illumination", "Illumination", "照明、解明、彩色（。さいしき（。）」写本", "14th Century", "in- (into, upon) + lumen (light)", "The action of illuminating or state of being illuminated", "ただの（。文字に（。、「光（。ルーメン）を（。投げ（。込む（。イン）」ことで（。、命（。を（。宿（。ら（。せる（。こと（。。（。黄金（。と（。極彩色（。で（。彩（。ら（。れた（。頁（。は（。、そのまま（。一つの（。小（。宇宙（。なの（。ですよ。"),
    ("glyph", "Glyph", "象形文字、記号、グリフ", "18th Century", "gluph- (to carve, hollow out, literal: 'to hollow out')", "A hieroglyphic character or symbol", "表面的な（。意味（。を（。環境（。を（。捨て（。、石（。を「彫（。り（。抜く（。グリフ）」ことで（。抽出（。さ（。れた（。、原初（。の（。かたち（。。（。その（。一（。点（。の（。窪（。みに（。、宇宙の（。全エナジー（。を（。、封印（。した（。もの。"),
    ("cipher", "Cipher", "暗号、数字のゼロ、サイファー", "14th Century", "sifr (empty, zero, literal: 'empty')", "A secret or disguised way of writing; a code", "全（。てを（。さら（。け（。出す（。のを（。止め（。、「空（。っぽ（。シフル）」の（。ふり（。を（。し（。て（。真実（。を（。隠（。す（。こと（。。（。その（。謎（。を（。解（。ける（。者だけが（。、聖なる（。智（。恵を受け（。継（。ぐ（。ことが（。できる（。のですよ。")
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
            word_id = f"{word_text.lower()}_ink"
            
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
                    "thinking": item[6] if len(item) > 6 else "言葉は、沈黙という名の広大な海に浮かぶ、美しき島々です。",
                    "aftertaste": item[7] if len(item) > 7 else "インクは、魂の叫びを静止させ、永遠という名の時間に刻み込むための血潮です。",
                    "example": f"The scholar spent years translating the ancient {word_text} to uncover the secrets of the lost civilization.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["書くとは、世界を一度殺し、紙の上に新しい命を産み落とす行為なのかもしれません。"]
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

        print(f"Success: Added {added_count} words. Theme: Ink & Paper (Cycle 54).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
