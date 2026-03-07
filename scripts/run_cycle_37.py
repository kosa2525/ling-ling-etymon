import json
import re

# Theme: The Pulse of Journey & Transit (Cycle 37)
words_data = [
    ("pilgrimage", "Pilgrimage", "巡礼、聖地巡り", "13th Century", "per- (through) + ager (field, land)", "A journey to a place associated with someone or something well known or respected", "ただの（。観光（。ではなく（。、自らの（。魂を（。清めるために「荒野（。アゲル）を（。突き（。抜け（。パー）て（。行く（。）」こと（。。（。困難（。な（。道のり（。の（。果てに（。、真の（。自分と（。出逢う（。ための（。、聖なる（。旅。"),
    ("odyssey", "Odyssey", "オデュッセイア、長旅、波乱万丈の旅", "16th Century", "Odusseus (Odysseus)", "A long and eventful or adventurous journey or experience", "故（。郷（。を（。離れ（。、十（。年（。もの（。歳月（。を（。かけて（。荒波（。を（。越（。える「オデュッセウスの（。ような（。旅」。（。失（。う（。ことで（。得（。られる（。、深い（。智慧（。と（。不屈の（。精神。"),
    ("expedition", "Expedition", "遠征、探検、迅速さ", "15th Century", "ex- (out) + pes (foot)", "A journey undertaken by a group of people with a particular purpose, especially that of exploration, scientific research, or war", "住み（。慣れた（。場所から（。、「足（。ペス）を（。外へと（。エクス）踏（。み（。出す（。）」こと（。。（。未知（。の（。領域を（。拓（。く（。ための（。、目的（。意識（。に（。満ちた（。、迅速（。な（。進軍。"),
    ("excursion", "Excursion", "遠足、小旅行", "14th Century", "ex- (out) + currere (to run)", "A short journey or trip, especially one engaged in as a leisure activity", "日常の（。義務（。から（。、「外へと（。エクス）走り（。出る（。カー）」こと（。。（。心（。の（。羽（。を（。伸ばし（。、普段（。見落（。して（。いる（。美（。しさを（。再発（。見（。する（。ための（。、軽（。やかな（。跳躍。"),
    ("voyage", "Voyage", "航海、空の旅", "13th Century", "via (way)", "A long journey involving travel by sea or in space", "大地を（。離れ（。、波（。や（。風の（。リズム（。に（。身（。を（。任せて「道（。ヴィア）を（。往く」こと（。。（。遥（。かなる（。水平線（。を（。目指し（。、自ら（。の（。限界を（。更新（。し（。続ける（。、壮大（。な（。船足。"),
    ("transit", "Transit", "通行、輸送、トランジット", "15th Century", "trans- (across) + ire (to go)", "The carrying of people, goods, or materials from one place to another", "ある（。場所から（。別の（。場所へと「越（。えて（。トランス）去（。る（。イ）」こと（。。（。ただの（。移動（。の中に（。、変化（。の（。予感（。が（。潜（。んで（。いる（。、通過（。儀礼の（。ような（。時間。"),
    ("transition", "Transition", "変遷、移行、過渡期", "16th Century", "trans- (across) + ire (to go)", "The process of changing from one state or condition to another", "かたち（。が（。定（。まる（。前（。の（。、境界（。を「越（。えて（。トランス）行く（。イ）」過程（。。（。古（。き自分（。を（。脱（。ぎ（。捨て（。、新（。しい（。光へと（。至（。る（。まで（。の（。、静（。かな（。る（。脱皮。"),
    ("passage", "Passage", "通行、通路、一節", "13th Century", "passus (step)", "The action or process of moving through or past somewhere on the way from one place to another", "一歩（。一歩（。の「歩（。み（。パス）」が（。重（。なり（。、一つの（。意味（。を（。形作る（。こと（。。（。時間（。という（。長い（。廊下（。を（。、私たちは（。今日（。も（。一歩ずつ（。確（。かに（。進んで（。いる（。のですよ。"),
    ("itinerary", "Itinerary", "旅行日程、旅程", "15th Century", "itiner- (journey, way)", "A planned route or journey", "未知（。なる（。場所への「道（。イティネ）」を（。、あらかじめ（。言葉（。で（。描き（。出した（。地図（。。（。計画（。は（。あっても（。、その（。通り（。に（。行（。かない（。こと（。こそが（。、旅の（。醍醐味（。なの（。ですが。"),
    ("arrival", "Arrival", "到着", "14th Century", "ad- (to) + ripa (shore, bank)", "The action or process of arriving somewhere", "長い（。航海（。が（。終わり（。、ようやく「岸辺（。リパ）へと（。アド）辿（。り（。着（。く（。）」こと（。。（。安堵（。と（。、新しい（。大地への（。期待（。が（。、一つの（。輝きに（。変わる（。瞬間。"),
    ("departure", "Departure", "出発、旅立ち", "14th Century", "de- (away) + part (part, share)", "The action of leaving, especially to start a journey", "慣れ（。親しんだ（。場所（。から「離（。れ（。ディ）分（。か（。れ（。パート）る」こと（。。（。寂（。しさ（。を（。抱（。き（。し（。め（。ながら（。、まだ（。見ぬ（。未来（。へと（。背中（。を（。向（。ける（。、希望（。の（。儀式。"),
    ("terminal", "Terminal", "終着駅、ターミナル、末期の", "15th Century", "terminus (end, limit)", "Of, forming, or situated at the end or extremity of something", "道の（。最後（。の「境界（。テルミヌス）」。（。そこ（。は（。、終わりの（。場所（。である（。と（。同時に（。、新しい（。旅の（。出発点（。でも（。あるの（。ですよ。"),
    ("harbor", "Harbor", "港、避難所、心に抱く", "Old English", "here (army) + beorg (shelter)", "A place on the coast where vessels may find shelter, especially one protected from rough water by piers, jetties, and other artificial structures", "かつて（。戦いに（。疲れた「軍隊（。ヒア）が（。身体（。を（。休めた（。バーグ）場所」。（。荒波（。を（。越えて（。きた（。魂を（。、優しく（。包（。み（。込（。んで（。くれる（。、安らぎの（。懐（ふところ）。", "あなた（。の（。心の中（。に（。、誰（。にも（。邪魔（。さ（。れ（。ない「ハーバー（。聖なる避難所）」を（。持（。って（。ください（。。（。そこ（。で（。羽（。を（。休（。めれば（。、また（。明日（。、無限（。の（。海へと（。漕（。ぎ（。出せ（。ます。"),
    ("aviation", "Aviation", "航空、飛行", "19th Century", "avis (bird)", "The flying or operating of aircraft", "重力（。という（。鎖（。を（。断（。ち（。切り（。、自ら「鳥（。アヴィス）のように（。）」天（。を（。駆（。け（。る（。こと（。。（。視点（。が（。高（。ま（。れば（。、地上（。の（。苦しみ（。は（。、一粒（。の（。砂（。のように（。小（。さく（。見（。える（。はずです。"),
    ("navigation", "Navigation", "航海術、ナビゲーション", "16th Century", "navis (ship) + agere (to drive, lead)", "The process or activity of accurately ascertaining one's position and planning and following a route", "不（。確かな（。海（。の上（。で（。、「船（。ネイヴィ）を（。正しく（。導（。く（。アグ）」智恵（。。（。嵐（。の（。中（。でも（。、自ら（。の（。北極星（。を（。見失（。わ（。ない（。、強靭な（。知性。"),
    ("compass", "Compass", "羅針盤、コンパス、範囲", "14th Century", "com- (together) + passus (step)", "An instrument containing a magnetized pointer which shows the direction of magnetic north and bearings from it", "足元（。を（。確かめ（。、「共に（。コン）歩（。み（。パス）を（。揃える（。）」ための（。道具（。。（。自分（。の（。中心（。が（。どちら（。を（。向（。いて（。いる（。か（。、常（。に（。問い（。直（。させて（。くれる（。、誠実（。な（。友。"),
    ("horizon", "Horizon", "地平線、視野、オリゾン", "14th Century", "horizein (to bound, limit)", "The line at which the earth's surface and the sky appear to meet", "空（。と（。大地（。が（。溶（。け（。合う（。、「境界（。ホライズン）」。見（。ゆる（。世界（。の（。果（。て（。であり（。、未知（。なる（。領域（。への（。入り口。"),
    ("baggage", "Baggage", "手荷物、心の重荷", "15th Century", "bague (bundle, sack)", "Sacks, trunks, and containers that hold a traveler's belongings", "旅に（。必要（。だと（。信じて（。、「袋（。バッグ）に（。詰（。め（。込んだ（。）」もの。（。多（。す（。ぎる（。荷物（。は（。、あなた（。の（。足取り（。を（。重（。く（。する（。だけかも（。し（。れませんよ（。。（。時（。々（。は（。身軽（。に（。な（。って（。みては（。？"),
    ("milestone", "Milestone", "画期的な出来事、マイル石", "18th Century", "mile + stone", "A stone set up beside a road to mark the distance in miles to a particular place", "長い（。道のり（。の（。途中で（。、どれだけ（。歩いて（。きたかを（。確かめる（。ための（。「石（。ストーン）」。一つ（。ひとつの（。成功（。を（。噛（。み（。締（。め（。、また（。次（。の一（。歩（。への（。勇気（。を（。得（。る（。ための（。標章。"),
    ("souvenir", "Souvenir", "お土産、思い出", "18th Century", "sub- (under) + venire (to come)", "A thing that is kept as a reminder of a person, place, or event", "旅の（。情景（。を（。、心の「下（。サブ）から（。再び（。来（。させる（。ヴェニール）」ための（。欠片（。。（。形（。を（。持（。った（。、魔法（。の（。記憶（。の（。トリガー。"),
    ("nomad", "Nomad", "遊牧民、ノマド", "16th Century", "nomad- (pasturing)", "A member of a people having no permanent abode, and who travel from place to place to find fresh pasture for their livestock", "一（。つの（。場所に（。安住（。せず（。、常（。に「新しい（。草地（。ノマ）を（。求め（。）」て（。彷徨（。う（。魂。（。所有（。する（。こと（。より（。、経験（。し（。続ける（。こと（。を（。選（。んだ（。、自由（。な（。狩人。"),
    ("vagabond", "Vagabond", "放浪者、浮浪者、バガボンド", "15th Century", "vagari (to wander)", "A person who wanders from place to place without a home or regular work", "目的（。さえ（。持（。た（。ず（。、ただ（。風（。の（。吹く（。まま（。に「彷徨（。う（。バガ）」こと（。。（。社会（。の（。枠組み（。から（。はみ出し（。、剥（。き（。出し（。の（。世界（。を（。愛（。する（。、孤独（。な（。哲学者。"),
    ("pioneer", "Pioneer", "先駆者、開拓者", "16th Century", "pion (foot soldier)", "A person who is among the first to explore or settle a new country or area", "軍隊の（。最前線を（。、「歩（。行く（。ピオン）兵士」のように（。突（。き（。進（。み（。、誰も（。見た（。ことの（。ない（。道を（。切り拓（。く（。者（。。（。背中（。に（。浴びる（。風（。は（。冷たく（。も（。、その（。瞳は（。常に（。未来（。を（。見据（。えて（。いる。"),
    ("refugee", "Refugee", "難民、亡命者", "17th Century", "re- (back) + fugere (to flee)", "A person who has been forced to leave their country in order to escape war, persecution, or natural disaster", "安らぎ（。の（。場所（。を（。奪わ（。れ（。、「後（。ろ（。リ）も（。見（。ず（。逃（。げ（。る（。フュジ）」こと（。を（。余儀（。なく（。さ（。れた（。者。", "彼（。の（。孤独（。な（。瞳（。の（。中に（。、かつて（。の（。私たちの（。姿（。を（。見（。る（。こと（。。（。それ（。が（。本当（。の（。愛（。の（。始（。まり（。なの（。ですよ。"),
    ("habitat", "Habitat", "生息地、住みか", "18th Century", "habitare (to dwell, live in)", "The natural home or environment of an animal, plant, or other organism", "単なる（。住所（。では（。なく（。、生命（。が（。最も（。自分らしく「住み（。ハビ）続ける（。）」ことの（。できる（。、聖なる（。場所。")
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
            word_id = f"{word_text.lower()}_journey"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "人生は、目的地に辿り着くことではなく、その道のりそのものです。",
                    "example": f"The character embarked on a life-changing {word_text} across Northern India.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["旅とは、自分自身の殻を脱ぎ捨て、新しい風を肺いっぱいに吸い込む行為です。"]
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

        print(f"Success: Added {added_count} words. Theme: Journey & Transit (Cycle 37).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
