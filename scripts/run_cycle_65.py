import json
import re

# Theme: The Alchemy of Root & Blossom (Cycle 65)
words_data = [
    ("rhizome", "Rhizome", "根茎（こんけい）、根源、リゾーム", "19th Century", "rhizoun (to cause to strike root, literal: 'rooting')", "A continuously growing horizontal underground stem which puts out lateral shoots and adventitious roots at intervals", "地上（。を（。拒（。み（。、暗い（。土の（。中で（。、水平に（。どこ（。までも（。広がる「根（。リゾマ）の（。ような（。茎、。（。中心（。を（。持（。た（。ず（。、絶（。え（。間（。なく（。繋（。が（。り（。、増（。殖（。し（。続ける、自（。律（。的（。な（。る（。エナジー。"),
    ("bulb", "Bulb", "電球、球根、バルブ", "16th Century", "bolbos (onion)", "A rounded underground storage organ present in some plants, notably those of the lily family, consisting of a short stem surrounded by fleshy scale leaves or leaf bases and lying dormant over winter", "静止（。し（。た（。「玉（。ねぎ（。ボルボス）」のように、内（。側（。に（。すべて（。の（。可能（。性を（。凝縮（。させた（。器（。。（。その（。暗い（。球体（。の（。中（。には（。、いつか（。眩（。し（。い（。光を（。放（。つ（。ための、未来（。の（。設計図が（。眠（。って（。いる（。のですよ。"),
    ("tuber", "Tuber", "塊茎（かいけい）、隆起、チューバー", "17th Century", "tuber (hump, swelling, literal: 'swelling')", "A much thickened underground part of a stem or rhizome, e.g. in the potato, serving as a food reserve and bearing buds from which new plants arise", "荒（。れ（。荒（。んだ（。大地（。の（。下で（。、静（。かに「膨（。ら（。み（。チューバ）蓄（。え（。た（。）」、命の（。貯（。金（。箱（。。（。その（。無（。骨（。な（。外（。見の（。中（。には（。、過（。酷（。な（。季節（。を（。生き（。抜く（。ための（。、濁（。り（。な（。き（。祈り（。が（。詰（。まって（。いる（。のですよ。"),
    ("sprout", "Sprout", "芽、新芽、スプラウト", "Old English", "sprūtan (to sprout)", "A newly grown shoots of a plant", "硬（。い（。殻を（。打ち（。破（。り（。、ただ（。光だけを（。求めて「噴（。き（。出す（。スプラウト）」第一（。歩（。。（。その（。透明（。に（。震（。える（。若緑（。に（。、宇宙（。の（。全（。新（。鮮（。な（。る（。エナジーが（。、集約（。さ（。れて（。いる（。のですよ。"),
    ("pollen", "Pollen", "花粉、粉、ポレン", "16th Century", "pollen (fine flour, dust)", "A fine powdery substance, typically yellow, consisting of microscopic grains discharged from the male part of a flower or from a male cone", "風（。の（。ように（。軽（。やか（。な「粉（。ポレン）』として（。、遠（。く（。の（。恋（。人へと（。、命を（。運（。ぶ（。もの（。。（。その（。一粒（。一粒（。には（。、何（。億（。年（。という（。時間の（。記憶が（。、美し（。く（。封（。じ（。込め（。られて（。いる（。のです。"),
    ("nectar", "Nectar", "蜜、ネクター、神酒", "16th Century", "nektar (death-overcoming, literal: 'overcoming death')", "A sugary fluid secreted by plants, especially within flowers to encourage pollination by insects and other animals", "生（。き（。る（。こと（。の（。苦（。しみを（。癒（。し（。、一（。時（。の「不死（。ネクタル）』を（。与（。えて（。くれる（。、聖なる（。雫（。。（。その（。甘（。い（。誘（。惑に（。、魂（。は（。、一（。瞬（。にして（。、肉（。体の（。枷（。を（。、忘（。れて（。しま（。う（。のですよ。"),
    ("petal", "Petal", "花びら、ペタル", "18th Century", "petalon (leaf, thin plate, literal: 'outstretched')", "Each of the segments of the corolla of a flower, which are modified leaves and are typically colored", "優（。しく「広（。げ（。られた（。ペタロン）」、色彩（。の（。翼（。。（。ただ（。鳥（。を（。、そして（。風（。を（。呼（。ぶ（。ため（。だけに（。、精（。密（。に（。創（。り（。出さ（。れた（。、一（。瞬（。の（。色彩（。の（。奇（。跡。"),
    ("sepals", "Sepals", "萼片（がくへん）、シーパル", "18th Century", "sepalon (separate, separate leaf)", "Each of the parts of the calyx of a flower, enclosing the petals and typically green and leaflike", "眩（。し（。い（。花の（。宴が（。、始まる（。直（。前まで（。、その（。命を「包（。み（。隔（。て（。て（。いた（。セパル）」、厚（。手の（。衣（。。（。その（。静（。かな（。る（。忍耐（。があってこそ（。、花（。は（。一きわ（。、美し（。く（。弾（。ける（。の（。ですよ。"),
    ("stamen", "Stamen", "雄（。お（。し（。）」べ、ステイメン、気骨（。きこつ（。）」", "17th Century", "stamen (thread, warp, literal: 'stand')", "The male fertilizing organ of a flower, typically consisting of a pollen-containing anther and a filament", "ただ（。ひたすら（。天（。を（。仰（。ぎ、「立ち（。続ける（。スタ）」ための（。、一本（。の（。糸（。。（。その（。不（。屈（。な（。る（。垂直（。性（。が（。、やがて（。、新（。しい（。命（。の（。雨（。を（。、宇宙（。へと（。降（。らす（。のです。"),
    ("pistil", "Pistil", "雌（。め（。し（。）」べ、ピスティル", "18th Century", "pistillus (pestle, literal: 'pounder')", "The female organs of a flower, comprising the stigma, style, and ovary", "命（。を（。、自（。らの（。中で「静く（。噛（。み（。砕（。く（。ピスティル）」、聖（。なる（。乳（。鉢（。。（。その（。深（。い（。闇の中に（。、全（。てを（。受け（。入れ（。、一（。つ（。の（。純粋（。な（。る（。種（。子（。へと（。、結晶（。さ（。せる（。のですよ。"),
    ("resin", "Resin", "樹脂、レジン、松脂", "14th Century", "resina (resin)", "A sticky flammable organic substance, insoluble in water, exuded by some trees and other plants", "傷（。付い（。た（。肌（。を（。、自（。ら（。の（。血（。で（。、「癒（。し（。守（。る（。レジナ）」黄金（。の（。涙（。。（。その（。粘（。り（。強（。い（。沈黙（。の中に（。、何（。千万（。年（。という（。時間の（。記憶が（。、琥（。珀（。となって（。、閉じ（。込め（。られて（。いる（。のです。"),
    ("flora", "Flora", "植物相、フローラ、花の女神", "17th Century", "Flōs (flower, Florae, goddess of flowers)", "The plants of a particular region, habitat, or geological period", "大地を（。彩（。る「花（。フロラ）の（。女神』たちの（。宴（。（。その（。場所（。に（。根（。を（。下（。し（。、共（。に（。生き（。る（。全（。ての（。緑（。の（。命（。に（。、宇宙の（。美（。しき（。秩序が（。、宿（。って（。いる（。のですよ。"),
    ("sap", "Sap", "樹液、活力、サップ", "Old English", "sæp (sap)", "The fluid, chiefly water with dissolved sugars and mineral salts, that circulates in the vascular system of a plant", "目（。には（。見えない（。地底（。の（。記憶を（。、天へへ（。と（。運（。ぶ「生命（。の（。甘（。い（。サップ）』。（。その（。絶（。え（。間（。ない（。巡（。り（。が（。、硬（。い（。樹（。皮の（。裏側（。で（。、確（。かに（。、宇宙を（。駆動（。さ（。せて（。いる（。のですよ。"),
    ("thorn", "Thorn", "刺（とげ）、苦難、ソーン", "Old English", "thorn (thorn)", "A stiff, sharp-pointed woody projection on the stem or other part of a plant", "優（。し（。すぎる（。世界に（。、ただ（。一（。つ（。の「痛（。み（。ソーン）』を（。加（。える（。こと（。。（。その（。鋭（。い（。一（。点（。がある（。から（。こそ（。、蕾（。は（。、侵（。さ（。れ（。ざ（。る（。聖（。域（。として、静（。か（。に（。、咲（。き誇（。れる（。の（。ですよ。"),
    ("blossom", "Blossom", "開花、全盛期、ブロッサム", "Old English", "blōstm (blossom)", "A flower or a mass of flowers on a tree or bush", "限界（。まで（。高（。まった（。エナジーが（。、一気に「溢（。れ（。出し（。ブロ）膨（。ら（。む（。）」こと（。。（。その（。眩（。し（。い（。爆発（。に（。、宇宙（。の（。全（。てが（。、今（。一度（。、祝福（。の（。言葉（。を（。、送（。って（。くれ（。る（。のですよ。")
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
            word_id = f"{word_text.lower()}_nature"
            
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
                    "thinking": item[6] if len(item) > 6 else "根は、闇を愛することで、光という名の花を産み落とすことができるのですよ。",
                    "aftertaste": item[7] if len(item) > 7 else "香りは、目に見えない命のメッセージであり、魂が故郷を思い出すための、たった一つの手がかりなのです。",
                    "example": f"The biologist identified the unique {word_text} structure to understand the plant's adaptation to the desert environment.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["成長とは、空へ伸びることではなく、自らの本質という名の地平へ、深く沈み込んでいくことなのですよ。"]
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

        print(f"Success: Added {added_count} words. Theme: Root & Blossom (Cycle 65).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
