import json
import re

# Theme: The Alchemy of Color & Vision (Cycle 43)
words_data = [
    ("pigment", "Pigment", "顔料、色素", "14th Century", "pingere (to paint)", "The natural coloring matter of animal or plant tissue", "世界を「染（。め（。ピン）上げる（。）」ための（。エッセンス（。。（。命（。が（。内側（。から（。絞（。り（。出（。した（。、強烈（。な（。意志の（。色。"),
    ("hue", "Hue", "色合い、色彩、ヒュー", "Old English", "hīw (form, appearance, color)", "A color or shade", "単なる（。色（。を超え（。、その（。ものが（。纏（。って（。いる「姿（。かたち（。ヒュー）」その（。もの（。。（。光（。の（。当たり（。方（。で（。刻（。一刻（。と（。変（。わ（。る（。、存在の（。表情。"),
    ("tint", "Tint", "淡い色、色合い、ティン", "18th Century", "tingere (to dye, stain)", "A slight or pale coloration; a shade or variety of a color", "真っ白（。な（。心に（。、一滴（。の（。エッセンスを「染（。め（。込（。めた（。ティン）」色彩（。。（。主張（。し（。すぎ（。ず（。、けれど（。確（。かな（。余韻を（。残（。す（。、魂の（。吐息。"),
    ("shade", "Shade", "影、色合い、物陰", "Old English", "sceadu (shadow, darkness)", "Comparative darkness caused by the interception of rays of light", "光が（。届（。かない（。ことで（。生まれる「影（。シェード）」。（。そこ（。には（。、白日の（。下（。では（。見（。え（。な（。かった（。、深（。い（。真実（。が（。静（。か（。に（。息（。を（。潜（。めて（。いる（。の（。ですよ。"),
    ("tone", "Tone", "音色、色調、トーン", "14th Century", "tonos (stretching, tension, pitch)", "A musical or vocal sound with reference to its pitch, quality, and strength", "ピンと「張（。られた（。トノス）弦」が（。奏（。で（。る（。ような（。、色彩（。の（。響き（。。（。あなた（。の（。放（。つ（。言葉の（。トーン（。が（。、今日（。の（。世界（。の色を（。決（。める（。のですよ。"),
    ("value", "Value", "価値、明度、値", "14th Century", "valere (to be strong, be worth)", "The regard that something is held to deserve; the importance, worth, or usefulness of something", "色の「強（。さ（。ヴァル）」であり（。、その（。存在の（。重み（。。（。明る（。い（。場所（。にも（。暗（。い（。場所（。にも（。、等（。しく（。宿（。って（。いる（。、不変（。の（。輝き。"),
    ("saturation", "Saturation", "彩度、飽和、サチュレーション", "16th Century", "satur (full)", "The state or process that occurs when no more of something can be absorbed, combined with, or added", "これ（。以上（。入（。ら（。ないほど「満ち（。足りた（。サトゥル）」状態（。。（。純粋（。な（。エナジーが（。、限界（。まで（。凝縮（。された（。とき（。、世界は（。最も（。鮮やか（。な（。色を（。放（。ち（。始め（。ます。"),
    ("brilliance", "Brilliance", "光輝、才気、卓越", "18th Century", "berillus (beryl, a precious stone)", "Exceptional talent or intelligence", "「宝石（。ベリル）」の（。ように（。、自ら（。の（。内側（。から（。光（。を（。放（。ち（。、周囲（。を（。圧倒（。する（。輝き（。。（。それは（。、研（。ぎ（。澄（。ま（。さ（。れた（。知性の（。絶唱（。なの（。ですよ。"),
    ("radiance", "Radiance", "光輝、放射、ラディアンス", "17th Century", "radius (ray)", "Light or heat as emitted or reflected by something", "中心から「一条の（。光（。レイ）として（。）」溢（。れ（。出す（。、目（。に（。見えない（。エナジー（。の（。奔流（。。（。喜び（。に（。満ち（。た（。魂（。は（。、それ（。だけで（。世界を（。照（。らす（。太陽に（。なれる（。のです。"),
    ("luster", "Luster", "光沢、艶、ラスター", "16th Century", "lustrare (to illuminate, purify)", "A gentle sheen or soft glow, especially that of a partly reflective surface", "単なる（。反射（。ではなく（。、表面（。を「清（。め（。磨き（。上げた（。ルストラ）」果てに（。得（。られる（。、奥（。深（。い（。艶（。。（。長い（。時間（。が（。育（。んだ（。、経験（。という（。名の（。輝き。"),
    ("shimmer", "Shimmer", "煌めき、微光", "Old English", "scimerian (to shine, glitter)", "A soft, slightly wavering light or reflection", "水面（。のように（。、「不（。確実に（。揺（。れ（。動き（。ながら（。シマー）」輝（。く（。こと（。。（。捉（。え（。どころ（。の（。ない（。けれど（。、確（。かに（。そこ（。に（。ある（。、幻（。のような（。美しさ。"),
    ("flicker", "Flicker", "明滅、ゆらぎ", "Old English", "flicorian (to flutter, hover)", "Of a light or source of light shine unsteadily; vary rapidly in brightness", "「羽（。ば（。た（。く（。フリコ）」ように（。、付（。いたり（。消（。え（。たり（。を（。繰（。り（。返（。す（。光（。。（。その（。危（。うい（。ゆら（。ぎの中にこそ（。、生命（。の（。拍動が（。宿（。って（。いる（。のですよ。"),
    ("opaque", "Opaque", "不透明な、難解な、オパル", "15th Century", "opacus (shaded, dark, bushy)", "Not able to be seen through; not transparent", "光（。を（。通（。さ（。ず（。、自（。らの中に「影（。オパ）を（。抱（。き（。込（。んで（。いる（。）」状態（。。（。その（。沈黙（。の（。重みが（。、存在の（。絶対的な（。境界（。を（。形（。作（。って（。いる（。の（。ですよ。"),
    ("translucent", "Translucent", "半透明な、光を通す", "16th Century", "trans- (across) + lucere (to shine)", "Of a substance allowing light, but not detailed images, to pass through; semitransparent", "自分を（。主張（。し（。すぎ（。ず（。、光（。を「向こう（。岸へと（。トランス）透（。かし（。輝（。か（。せる（。ル）」こと（。を（。許（。す（。姿勢（。。（。完璧（。な（。透明（。より（。も（。、どこ（。か（。優（。し（。い（。、魂の（。ヴェール。"),
    ("iridescent", "Iridescent", "虹色の、真珠光沢の", "18th Century", "iris (rainbow)", "Showing luminous colors that seem to change when seen from different angles", "見（。る（。角度（。に（。よって（。、様々（。な「虹（。イリス）」の（。色彩（。を（。放（。つ（。こと（。。（。一（。つの（。側面（。では（。語（。り（。切（。れ（。ない（。、あなた（。の（。中（。の（。豊（。か（。な（。矛盾。"),
    ("opalescent", "Opalescent", "乳白色の、オパールのような", "19th Century", "upala (precious stone)", "Showing varying colors as an opal does", "「聖なる（。石（。ウパラ）」の（。ように（。、内側（。から（。乳白色（。の（。光（。を（。放（。ち（。、優しく（。全（。て（。を（。包（。み（。込む（。輝き（。。（。母（。性（。のような（。、静（。か（。な（。る（。包容力。"),
    ("prismatic", "Prismatic", "プリズムの、分光の、多面的な", "19th Century", "prisma (something sawed, literal: 'to saw')", "Relating to, resembling, or produced by a prism", "透明（。な（。光（。を「鋸（。のこぎ（。り（。プリスマ）で（。切り（。分（。け（。た（。）」ように（。、色（。鮮（。やかに（。分（。散（。させる（。こと（。。（。単純（。な（。真実（。を（。、無限（。の（。側面（。から（。眺（。める（。ための（。装置。"),
    ("palette", "Palette", "パレット、色彩板", "17th Century", "pale (spade, shovel)", "A thin board or slab on which an artist lays and mixes colors", "色（。を（。選（。び（。、混ぜ（。合わせ（。る（。ための「小さな（。シャベル（。ペール）」。（。あなたの（。選んだ（。言葉（。という（。色が（。、今日（。の（。世界（。を（。鮮（。やかに（。彩（。り（。ます。"),
    ("silhouette", "Silhouette", "シルエット、影絵", "18th Century", "Étienne de Silhouette (French politician)", "The dark shape and outline of someone or something visible against a lighter background, especially in dim light", "細（。部（。を（。捨（。て（。去（。り（。、ただ「輪郭（。だけを（。際（。立（。たせ（。た（。）」、峻烈（。な（。影（。。（。余計（。な（。装飾（。を（。削（。ぎ（。落（。した（。とき（。、魂の（。真（。実（。の（。かたちが（。浮（。き（。彫（。りに（。なり（。ます。"),
    ("perspective", "Perspective", "遠近法、視点、見方", "14th Century", "per- (through) + specere (to look)", "The art of drawing solid objects on a two-dimensional surface so as to give the right impression of their height, width, depth, and position in relation to each other when viewed from a particular point", "透明（。な（。窓（。を「透（。かして（。パー）見つめる（。スぺ）」ことで（。、世界に（。奥行きを（。与（。える（。方法（。。（。自分（。の（。視点（。が（。変わ（。れば（。、昨日（。までの（。絶望（。さえ（。、一枚（。の（。美（。しい（。風景（。に（。変わる（。のですよ。"),
    ("dimension", "Dimension", "次元、寸法、ディメンション", "14th Century", "dis- (apart) + metiri (to measure)", "An aspect or feature of a situation, problem, or thing", "世界を「バラバラ（。ディ）に（。して（。測（。る（。メン）」ことで（。得（。られる（。、空間（。の（。広（。がり（。。（。一つ（。の（。数字（。では（。語（。り（。切（。れ（。ない（。、あなた（。の（。存在（。の（。多層性。"),
    ("illuminate", "Illuminate", "照らす、解明する、啓蒙する", "16th Century", "in- (into, upon) + lumen (light)", "Make (something) visible or bright by shining light on it; help to clarify or explain (a subject or matter)", "暗闇（。の（。中に（。、「光（。ルーメン）を（。投げ（。込む（。イン）」こと（。。（。ただ（。明る（。く（。する（。だけでなく（。、そこに（。ある（。ものの（。本質（。を（。浮（。き（。彫（。りに（。する（。、知性の（。炎。"),
    ("transfiguration", "Transfiguration", "変容、変貌、トランスフィギュレーション", "14th Century", "trans- (across) + figura (shape)", "A complete change of form or appearance into a more beautiful or spiritual state", "今（。までの「姿（。かたち（。フィギュラ）を（。飛び越し（。トランス）」て（。）、全く（。別（。な（。輝きへと（。変（。わ（。る（。こと（。。（。苦（。し（。みの（。果てに（。得（。られる（。、魂の（。神（。々（。しい（。飛躍。"),
    ("luminosity", "Luminosity", "光度、華やかさ", "17th Century", "lumen (light)", "The intrinsic brightness of a celestial object (as distinct from its apparent brightness diminished by distance)", "自（。ら（。の（。内（。側（。に（。、どれほど（。の「光（。ルーメン）」を（。宿（。して（。いる（。か（。。（。外部（。の（。反射（。に（。頼（。ら（。ず（。、暗闇（。の（。中で（。こそ（。真（。価（。を（。発揮（。する（。、静（。かな（。る（。輝き。"),
    ("aesthetics", "Aesthetics", "美学、美意識", "18th Century", "aisthanesthai (to perceive, feel)", "A set of principles concerned with the nature and appreciation of beauty, especially in art", "ただ（。見る（。のではなく（。、心で「感（。じ（。取（。る（。アイス）」こと（。。（。あなた（。が（。何を（。美しい（。と（。思う（。か（。、その（。一瞬（。一瞬（。の（。選択（。が（。、あなた（。という（。作品を（。創（。り（。上げ（。て（。いく（。の（。ですよ。")
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
            word_id = f"{word_text.lower()}_vision"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "色彩は、光が私たちの魂に語りかけるための、無言の言葉です。",
                    "example": f"The artist used a vibrant {word_text} to bring the landscape to life.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["視覚とは、物理的な光だけでなく、魂の奥底にある光を見出すための窓なのです。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["opaque", "translucent", "iridescent", "opalescent", "prismatic", "chromatic"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Color & Vision (Cycle 43).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
