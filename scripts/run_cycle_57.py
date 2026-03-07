import json
import re

# Theme: The Alchemy of Star & Nebula (Cycle 57)
words_data = [
    ("stellar", "Stellar", "星の、恒星の、輝かしい", "17th Century", "stella (star)", "Relating to a star or stars"),
    ("nebula", "Nebula", "星雲、ネビュラ、朧（おぼろ）", "17th Century", "nebula (mist, vapor, cloud)", "A cloud of gas and dust in outer space, visible in the night sky either as an indistinct bright patch or as a dark silhouette against other luminous matter", "宇宙（。の（。暗闇（。の中に（。、微（。か（。に（。漂（。う「霧（。ネビュラ）」。（。星々が（。産（。声を（。上げる（。前の（。、混沌（。と（。静寂が（。混ざり（。合った（。、原初（。の（。ゆりかご。"),
    ("galaxy", "Galaxy", "銀河、ギャラリー、華やかな集まり", "14th Century", "gala (milk, literal: 'milky circle')", "A system of millions or billions of stars, together with gas and dust, held together by gravitational attraction", "夜空（。を（。横（。切（。る「溢（。れ（。出し（。た（。ミルク（。ガラ）」のような（。、巨大（。な（。光の（。渦（。（。私たち（。という（。存在（。は（。、その（。一粒（。の（。光に（。過ぎ（。ない（。けれど（。、確（。かに（。宇宙（。の一部（。なの（。ですよ。"),
    ("pulsar", "Pulsar", "パルサー、脈動変光星", "20th Century", "pulse + -ar", "A celestial object, thought to be a rapidly rotating neutron star, that emits regular pulses of radio waves and other electromagnetic radiation at rates of up to one thousand pulses per second", "宇宙の（。深淵（。から（。、一寸（。の（。狂（。い（。もなく「脈動（。パルス）」を（。送り（。続ける（。、独（。り（。ぼっちの（。灯台（。（。その（。厳格（。な（。リズムが（。、虚無（。という（。名の（。闇を（。打ち（。破（。って（。いく（。のです。"),
    ("quasar", "Quasar", "クエーサー、準星", "20th Century", "quasi- (as if, almost) + stellar", "A massive and extremely remote celestial object, emitting exceptionally large amounts of energy, and typically having a starlike image in a telescope", "遥（。か（。な（。時空（。の（。果てで（。、まるで「星（。ステラ）の（。よう（。に（。クワシ）」振る舞（。う（。、巨大な（。エナジーの（。塊（。（。その（。眩（。し（。い（。咆（。哮（。は（。、宇宙の（。始まりの（。記憶を（。今に（。伝えて（。いる（。の（。ですよ。"),
    ("supernova", "Supernova", "超新星、スーパーノヴァ", "20th Century", "super- (above, over) + nova (new)", "A star that suddenly increases greatly in brightness because of a catastrophic explosion that ejects most of its mass", "自らの（。重みに（。耐（。え（。かね（。て（。、烈（。しく「新（。しく（。ノヴァ）超（。え（。て（。ゆく（。スーパー）」、最後（。の（。輝き（。（。その（。爆発（。が（。、次（。なる（。命（。の（。種子（。を（。宇宙へと（。散（。り（。ば（。める（。の（。ですよ。"),
    ("trajectory", "Trajectory", "軌道、弾道、トラジェクトリー", "17th Century", "trans- (across) + jacere (to throw)", "The path followed by a projectile flying or an object moving under the action of given forces", "見えない（。重力（。に（。身を（。任せ（。、空（。を「横（。切（。る（。トランス）よう（。に（。投げ（。出さ（。れた（。ジェクト）」道（。（。あなた（。の（。人生（。という（。名の（。旅（。も（。、美し（。い（。曲線（。を（。描い（。て（。いる（。のですよ。"),
    ("eclipse", "Eclipse", "日食、月食、失墜、エクリプス", "14th Century", "ek- (out) + leipein (to leave)", "An obscurement of the light from one celestial body by the passage of another between it and the observer or between it and its source of illumination", "一時（。的に（。光の（。領域を「離（。れ（。去（。る（。リプ）」こと（。（。その（。静（。か（。な（。る（。暗転（。の（。中に（。、私たちは（。普段（。忘（。れて（。いる（。、真実（。の（。太陽（。を（。想（。い出す（。のですよ。"),
    ("solstice", "Solstice", "至（。し（。）、夏至（。・冬至（。、至り（。いた（。り（。）」", "13th Century", "sol (sun) + sistere (to stand still)", "Either of the two times in the year, the summer solstice and the winter solstice, when the sun reaches its highest or lowest point in the sky at noon, marked by the longest and shortest days", "太陽（。が（。天の（。頂（。で（。、一瞬（。だけ「立ち（。止（。まった（。スティ）」瞬間（。（。影（。が（。最も（。短く（。、あるいは（。最も（。長く（。なる（。とき（。、世界は（。静（。か（。な（。る（。転換（。を（。迎える（。のです。"),
    ("meteor", "Meteor", "流星、メテオ、空中現象", "15th Century", "meta- (beyond) + aeirein (to lift, raise, literal: 'thing in the air')", "A small body of matter from outer space that enters the earth's atmosphere, becoming incandescent as a result of friction and appearing as a streak of light", "宇宙の（。果てから（。、大気（。の「高（。みへと（。メテ）舞（。い（。上が（。った（。）」眩（。し（。い（。一瞬（。（。燃（。え（。尽（。き（。る（。その（。最後（。の（。一きわ（。の（。輝きに（。、人々は（。永遠の（。願（。い（。を（。託す（。のです。"),
    ("comet", "Comet", "彗（。すい（。）」星、コメット、ほうき星", "13th Century", "kometes (long-haired)", "A celestial object consisting of a nucleus of ice and dust and, when near the sun, a 'tail' of gas and dust particles pointing away from the sun", "長い「髪（。を（。なび（。か（。せた（。コメット）」、宇宙の（。放浪者（。（。数（。十（。年（。に（。一度の（。再会を（。果（。た（。し（。、再び（。孤独（。な（。旅路へと（。戻（。って（。いく（。、哀（。し（。き（。美し（。さ。"),
    ("observatory", "Observatory", "天文台、展望台、オブザーバトリー", "18th Century", "ob- (against, before) + servare (to keep, watch)", "A room or building housing an astronomical telescope or other scientific equipment for the study of natural phenomena", "真理（。を（。求めて（。、ただ「目の（。前の（。オブ）景色を（。守り（。見（。続ける（。サーーヴァ）」場所（。（。その（。巨（。大な（。瞳（。が（。、何（。億（。光年（。の（。彼（。方（。にある（。、小さな（。囁（。きを（。拾い（。上げる（。のですよ。"),
    ("luminosity", "Luminosity", "光度、明るさ、ルミノシティ", "17th Century", "lumen (light)", "The intrinsic brightness of a celestial object", "単なる（。反射（。ではなく（。、内側（。から「溢（。れ（。出す（。光（。ルーメン）」その（。もの（。（。自（。らが（。燃（。え（。て（。こそ（。、世界（。を（。照（。らし（。、誰（。かの（。道（。し（。る（。べに（。な（。れる（。の（。ですよ。"),
    ("magnitude", "Magnitude", "等級、規模、マグニチュード", "15th Century", "magnus (great)", "The great size or extent of something", "宇宙（。という（。名の「巨大（。な（。マグ）」定規（。（。一人（。の（。人間（。には（。推（。し（。量（。れ（。ない（。ほどの（。深淵（。が（。、そこには（。確（。かに（。（。横たわ（。って（。いる（。の（。ですよ。"),
    ("ethereal", "Ethereal", "エーテルのような、天上の、希薄な", "16th Century", "aither (upper air)", "Extremely delicate and light in a way that seems too perfect for this world", "地上（。の（。埃（。を（。持（。た（。ず（。、ただ「高き（。空の（。空気（。エテール）」の（。ように（。、澄み（。渡った（。もの（。（。その（。危（。うい（。美し（。さは（。、あなた（。を（。、高（。次元（。な（。る（。調和へと（。誘（。う（。の（。ですよ。")
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
            word_id = f"{word_text.lower()}_stars"
            
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
                    "thinking": item[6] if len(item) > 6 else "星は、宇宙が孤独に耐えきれなくなって、自らの名前を呼ぶために点した灯火なのです。",
                    "aftertaste": item[7] if len(item) > 7 else "銀河は、魂が再び一つに還る場所を夢見て、夜空に描き出したミルクの流れです。",
                    "example": f"The astronomer studied the {word_text} for signs of cosmic radiation and planetary formation.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["遠くの星が光って見えるのは、それが過去の輝きを今に届けているからなのですよ。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["stellar", "ethereal", "celestial", "astral", "cosmic"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Star & Nebula (Cycle 57).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
