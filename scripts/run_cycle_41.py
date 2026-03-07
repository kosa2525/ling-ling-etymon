import json
import re

# Theme: The Pulse of Cosmos & Astronomy (Cycle 41)
words_data = [
    ("galaxy", "Galaxy", "銀河、ギャラリー、華やかな集まり", "14th Century", "gala (milk)", "A system of millions or billions of stars, together with gas and dust, held together by gravitational attraction", "夜空（。の（。深淵（。に（。溢（。れ（。出した（。、「白い（。ミルク（。ガラ）」のような（。光の（。大河（。。（。個（。々（。の（。星々が（。、巨大（。な（。引力（。によって（。寄り添（。い（。、一つの（。壮大（。な（。物語を（。紡（。い（。で（。いる（。、宇宙の（。揺り（。かご。"),
    ("nebula", "Nebula", "星雲、霧、ネビュラ", "15th Century", "nebula (mist, cloud, vapor)", "A cloud of gas and dust in outer space, visible in the night sky either as an indistinct bright patch or as a dark silhouette against other luminous matter", "まだ（。かたち（。を（。持（。た（。ず（。、ただ（。光（。り（。輝（。く「霧（。ネビュラ）」のように（。漂（。って（。いる（。もの（。。（。そこ（。には（。、数（。え（。切（。れない（。新しい（。命（。の（。誕生（。が（。、静（。か（。に（。約束（。されて（。いる（。のですよ。"),
    ("constellation", "Constellation", "星座、一団", "14th Century", "com- (together) + stella (star)", "A group of stars forming a recognizable pattern that is traditionally named after its apparent form or identified with a mythological figure", "バラバラの（。光（。を（。、人間が（。想像力（。という（。名の（。糸で「共（。に（。コン）一つの（。星（。ステラ）物語」へと（。繋（。ぎ（。合わ（。せた（。もの（。。（。暗闇（。の（。中（。に（。、座標（。を（。見出し（。、歩（。む（。ための（。知恵。"),
    ("asterisk", "Asterisk", "星印、アスタリスク", "14th Century", "asterikos (little star)", "A symbol (*) used as a reference mark or to indicate omission, doubtful matter, etc.", "言葉の（。森（。の（。中に（。そっと（。置（。かれた（。、「小さな（。星（。アステ）」。そこ（。には（。、本文（。では（。語（。り（。切（。れ（。な（。かった（。、大切（。な（。注（。釈（。や（。祈り（。が（。、密（。かに（。宿（。って（。いる（。のですよ。"),
    ("comet", "Comet", "彗星、ほうき星", "13th Century", "kometes (long-haired)", "A celestial object consisting of a nucleus of ice and dust and, when near the sun, a 'tail' of gas and dust particles pointing away from the sun", "夜空を（。静（。か（。に（。横（。切（。る（。、「長い（。髪（。コメテス）を（。なび（。か（。せ（。た（。）」旅（。人（。。（。遥（。か（。彼方（。から（。、宇宙の（。全記憶（。を（。凍（。り（。ついた（。まま（。今（。へと（。運ん（。で（。くる（。、氷（。の（。使者。"),
    ("meteor", "Meteor", "流星、メテオ", "15th Century", "meta- (beyond) + aeirein (to lift)", "A small body of matter from outer space that enters the earth's atmosphere, becoming incandescent as a result of friction and appearing as a streak of light", "天（。上の（。高（。みに「持ち（。上げ（。られ（。アエイ）た（。）」もの（。。（。大気に（。触（。れ（。た（。瞬間（。、自ら（。を（。烈（。しく（。燃や（。し（。、一瞬（。の（。閃光（。と（。なって（。消（。え（。ゆく（。、命（。の（。絶唱。"),
    ("asteroid", "Asteroid", "小惑星、アステロイド", "19th Century", "aster (star) + -oeides (form, shape)", "A small rocky body orbiting the sun", "惑星に（。なり（。切れ（。なかった（。、「星（。アステ）の（。形（。オイド）」を（。した（。岩（。屑（。。（。けれど（。その（。一つ（。ひとつに（。、宇宙の（。初期（。の（。情熱が（。、そのままの（。姿（。で（。刻（。ま（。れて（。いる（。のですよ。"),
    ("orbit", "Orbit", "軌道、眼窩、オービット", "14th Century", "orbita (track, rut made by a wheel)", "The curved path of a celestial object or spacecraft around a star, planet, or moon, especially a periodic elliptical revolution", "巨大（。な（。引力（。に（。抗（。わず（。、ただ（。一（。筋（。の「轍（。わだち・オビタ）」を（。描（。き（。続ける（。こと（。。（。その（。繰り返（。しが（。、いつしか（。宇宙の（。盤面を（。支（。える（。、盤石（。な（。秩序（。と（。なる（。のです。"),
    ("atmosphere", "Atmosphere", "大気、雰囲気、アトモスフィア", "17th Century", "atmos (vapor) + sphaira (sphere, ball)", "The envelope of gases surrounding the earth or another planet", "大地を（。優しく（。包（。む「蒸気（。アトモス）の（。球（。スフィア）」。（。目（。には（。見え（。ない（。けれど（。、それが（。なければ（。一瞬（。にして（。生命は（。消（。え（。て（。しまう（。、透明な（。愛の（。毛布（。）。", "あなた（。に（。しか（。あら（。わ（。せ（。ない「アトモスフィア（。情緒）」を（。大切に（。して（。ください（。。（。それ（。が（。、世界（。に（。唯一（。無二（。の（。彩（。り（。を（。与（。える（。の（。ですから。"),
    ("meridian", "Meridian", "子午線、絶頂、メリディアン", "14th Century", "medius (middle) + dies (day)", "A circle of constant longitude passing through a given place on the earth's surface and the terrestrial poles", "太陽が（。最高（。の（。高（。みに（。達（。する「真昼（。ミディ）の（。刻（。）」。（。光（。と（。影（。が（。分（。か（。れ（。、運命の（。境界（。が（。最も（。鮮やか（。に（。引（。か（。れる（。、真実（。の（。瞬間。"),
    ("longitude", "Longitude", "経度、経線", "14th Century", "longus (long)", "The angular distance of a place east or west of the meridian at Greenwich", "世界を（。縦（。に（。貫（。く「長い（。ロング）」糸（。。（。あなたが（。今（。どこに（。立ち（。、どちらを（。向（。いて（。いるか（。を（。、宇宙的（。な（。視点から（。示（。し（。て（。くれる（。、座標（。の（。一部。"),
    ("latitude", "Latitude", "緯度、許容範囲、自由", "14th Century", "latus (wide)", "The angular distance of a place north or south of the earth's equator", "世界を（。横（。に（。結ぶ「（。広い（。ラタス）」帯（。。（。単なる（。位置（。情報（。では（。なく（。、そこに（。どれほど（。の（。豊（。かさ（。や（。自由を（。許容（。できる（。かと（。いう（。、精神の（。広（。がり。"),
    ("altitude", "Altitude", "高度、高所、標高", "14th Century", "altus (high)", "The height of an object or point in relation to sea level or ground level", "ただ（。数字（。が（。増える（。のでは（。なく（。、魂を「高く（。アルタス）」持ち（。上げ（。る（。こと（。。（。視点（。が（。高（。ま（。れば（。、昨日（。までの（。苦（。し（。み（。さえ（。、一（。枚（。の（。美（。しい（。絵（。の（。ように（。見（。えて（。くる（。はずです。"),
    ("vector", "Vector", "ベクトル、媒介者、運ぶもの", "18th Century", "vehere (to carry)", "A quantity having direction as well as magnitude, especially as determining the position of one point in space relative to another", "単なる（。エナジー（。では（。なく（。、明確な（。目的地（。を（。持って「運（。ぶ（。ヴェ）者（。）」。（。あなた（。の（。意志（。が（。どちらの（。方向（。へ（。向（。かって（。いる（。か（。、それ（。が（。全（。て（。を（。決（。める（。のですよ。"),
    ("quantum", "Quantum", "量子、クォンタム、飛躍", "16th Century", "quantus (how great, how much)", "A discrete quantity of energy proportional in magnitude to the frequency of the radiation which it represents", "世界を（。構成（。する「どれほどの（。クォンタ）分量（。）」という（。、最小（。の（。魂の（。単位（。。（。連続（。性（。を（。分断（。し（。、一気（。に（。飛（。躍（。する（。、宇宙の（。隠（。れた（。拍動。"),
    ("singularity", "Singularity", "特異点、シンギュラリティ", "14th Century", "singulus (single, alone)", "The state, fact, or quality of being singular", "いかなる（。法則（。も（。通用（。し（。ない（。、たった「一（。つの（。シングル）」場所（。。（。そこ（。から（。全（。て（。が（。始（。まり（。、あるいは（。全（。て（。が（。飲（。み込ま（。れる（。、運命の（。無限の（。淵。"),
    ("supernova", "Supernova", "超新星", "20th Century", "super- (above, beyond) + nova (new)", "A star that suddenly increases greatly in brightness because of a catastrophic explosion that ejects most of its mass", "古い（。記憶（。を（。全（。て（。燃や（。し（。尽（。く（。し（。、常識（。を「遥（。かに（。超え（。た（。スーパー）新（。しさ（。ノヴァ）」と（。なって（。宇宙（。を（。照（。らし出（。す（。、最後（。にして（。最大（。の（。輝き。"),
    ("terrestrial", "Terrestrial", "地球の、大地の、地上の", "15th Century", "terra (earth)", "Of, on, or relating to the earth", "天（。上の（。高（。みに（。憧（。れ（。つつ（。も（。、私たちは「大地（。テラ）」に（。根（。を（。張（。り（。、泥（。に（。まみれ（。ながら（。生き（。て（。いく（。、愛（。お（。し（。き（。存在（。なのです。"),
    ("vacuum", "Vacuum", "真空、空白、虚無", "16th Century", "vacuus (empty)", "A space entirely devoid of matter", "一切の（。物質を（。捨て（。去（。った「空（。っぽ（。ヴァキュ）の（。状態（。）」。（。けれど（。、その（。虚無（。だからこそ（。、新しい（。エナジーが（。湧（。き（。出し（。て（。くる（。の（。ですよ。"),
    ("parallax", "Parallax", "視差、パララックス", "16th Century", "parallaxis (change, alternation)", "The effect whereby the position or direction of an object appears to differ when viewed from different positions, e.g. through the viewfinder and the lens of a camera", "視点（。が（。変わ（。れば（。、景色（。もまた「交互に（。入れ（。替（。わる（。パラ）」ということ（。。（。相手の（。座標（。に（。立（。って（。世界（。を（。眺（。め（。た（。とき（。、真（。の（。対話（。が（。始まり（。ます。"),
    ("refraction", "Refraction", "屈折、リフラクション", "17th Century", "re- (back) + frangere (to break)", "The fact or phenomenon of light, radio waves, etc. being deflected in passing obliquely through the interface between one medium and another or through a medium of varying density", "光が（。異（。なる（。世界へと（。入り（。込む（。とき（。、あえて（。自らを（。一度「後ろ向きに（。リ）壊（。す（。フラク）」ことで（。、新しい（。角度（。を（。描（。き出（。す（。、光の（。知性。"),
    ("observatory", "Observatory", "天文台、気象台、展望台", "17th Century", "observare (to watch, note, heed)", "A room or building housing an astronomical telescope or other scientific equipment for the study of natural phenomena", "ただ（。眺める（。のではない（。。（。敬意（。を（。持って「大切（。に（。守（。り（。見守（。る（。オプス）」ための（。場所（。。（。そこ（。からは（。、宇宙の（。深遠（。な（。囁（。き（。が（。、より（。鮮明（。に（。聴（。こ（。えて（。くる（。はずです。"),
    ("satellite", "Satellite", "衛星、人工衛星、サテライト", "16th Century", "satelles (attendant, guard)", "An artificial body placed in orbit around the earth or moon or another planet in order to collect information or for communication", "一人の（。英雄（。では（。なく（。、常に（。寄り添（。い（。、静（。か（。な（。る「従者（。サテレス）」として（。世界（。を（。見守（。る（。存在（。。（。見（。え（。ない（。糸（。で（。繋（。が（。り（。な（。がら（。、孤独（。な（。軌道（。を（。刻（。み（。続（。ける（。もの。"),
    ("shuttle", "Shuttle", "シャトル、往復便、織機（しょっき）のひ", "Old English", "scutel (dart, arrow)", "A vehicle or aircraft that travels regularly between two places", "二つの（。岸辺を（。、「矢（。スカトル）のように（。）」行（。ったり（。来たり（。し（。ながら（。、バラバラ（。な（。世界（。を（。一つの（。布（。へと（。織（。り（。上（。げて（。いく（。、繋（。ぎ（。手。"),
    ("capsule", "Capsule", "カプセル、小箱、要約", "17th Century", "capsa (box)", "A small case or container, especially a round or cylindrical one", "大切な（。記憶（。や（。エナジーを（。、外界（。から（。守（。る（。ための「小さな（。箱（。カプサ）」。（。宇宙（。という（。過酷（。な（。海（。を（。渡る（。ための（。、唯一（。の（。聖域。")
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
            word_id = f"{word_text.lower()}_cosmos"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "私たちは、宇宙という巨大な夢の一部を見ている、星の欠片なのです。",
                    "example": f"The new space telescope captured breathtaking images of a distant {word_text}.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["無限とは、遠い場所にあるのではなく、今この瞬間の深みの中に、そっと息を潜めています。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["terrestrial", "planetary", "solar", "lunar", "stellar", "astral", "infinite"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Cosmos & Astronomy (Cycle 41).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
