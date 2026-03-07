import json
import re

# Theme: The Pulse of Time & Eternity (Cycle 36)
words_data = [
    ("duration", "Duration", "持続期間、継続", "14th Century", "durare (to last, harden)", "The time during which something continues", "柔らかい（。感情（。が（。、時間の（。波に（。洗（。われ（。て（。、「硬（。く（。ドゥラ）定着（。した（。）」もの（。。（。その（。愛が（。どれほど（。誠実（。に（。、時間（。を（。耐（。え（。抜（。いた（。か（。という（。、不変（。の（。証明。"),
    ("interval", "Interval", "間隔、休憩、インターバル", "14th Century", "inter- (between) + vallum (wall)", "An intervening time or space", "出来事（。と（。出来事の（。「壁（。ヴァル）の（。間（。インター）」に（。用意された（。、静かな（。真空の（。空間（。。（。次（。の一歩を（。踏み出す（。ための（。、魂の（。深呼吸。"),
    ("instant", "Instant", "瞬間、即座の、インスタント", "14th Century", "in- (upon) + stare (to stand)", "A precise moment of time", "永遠の（。流れの中に（。、「今まさに（。イン）立ち（。スタ）尽くして（。いる（。）」、一点の（。煌（。めき（。。（。逃（。せ（。ば（。二度と（。戻（。らない（。、残酷（。な（。までに（。純粋（。な（。、時の（。一滴。"),
    ("momentary", "Momentary", "瞬間的な、束の間の", "16th Century", "movimentum (movement)", "Lasting for a very short time", "単なる（。短い（。時間で（。はなく（。、運命が（。大きく「動（。き（。ムーブ）変（。わる（。）」、その（。一瞬（。の（。衝撃（。。（。稲妻（。のように（。、世界（。の（。輪郭（。を（。一瞬（。だけ（。照（。らし出（。す（。、時の（。火花。"),
    ("transient", "Transient", "一時的な、儚い、通り過ぎる", "16th Century", "trans- (across) + ire (to go)", "Lasting only for a short time; impermanent", "一つの（。場所に（。留（。まらず（。、常に「向こう（。岸へと（。トランス）去（。り（。イ）ゆく（。）」宿命（。。（。去（。って（。いくから（。こそ（。、今（。ここ（。にある（。輝き（。が（。、狂（。お（。しい（。ほど（。愛（。お（。しく（。なる。"),
    ("fleeting", "Fleeting", "束の間の、流れるような", "Old English", "flēotan (to float, flow, swim)", "Lasting for a very short time", "掴（。もう（。と（。すれば（。、指の間を「川の（。ように（。流（。れ（。フリート）去（。る（。）」、捉（。え（。どころ（。の（。ない（。美しさ（。。（。追い（。求める（。のを（。止（。めた（。時（。、あなたは（。その（。流れ（。その（。ものと（。一体（。になれる（。はずです。"),
    ("permanent", "Permanent", "永続的な、恒久的な、パーマ", "15th Century", "per- (through) + manere (to stay)", "Lasting or intended to last or remain unchanged indefinitely", "流行（。の（。風が（。吹き（。抜（。けて（。も（。、その（。場に「ずっと（。パー）留まり（。マネー）続ける（。）」こと（。。（。時代（。の（。審判（。を（。耐（。え（。抜き（。、変わらない（。本質（。を（。守り（。抜いた（。、静かなる（。勝利。"),
    ("perpetual", "Perpetual", "絶え間のない、永久の", "14th Century", "per- (through) + petere (to seek)", "Never ending or changing", "途切（。れる（。ことなく（。、常に「高み（。を（。求め（。ペト）続ける（。パー）」、魂の（。飢え（。と（。渇（。き（。。（。決して（。満足（。せず（。、宇宙（。の（。果（。て（。まで（。一（。つ（。に（。繋（。が（。ろう（。とする（。、巨大（。な（。エナジー（。の（。螺旋。"),
    ("immortal", "Immortal", "不死の、不滅の", "14th Century", "in- (not) + mors (death)", "Living forever; never dying or decaying", "肉体（。という（。檻（。を（。脱（。ぎ（。捨て（。、「死（。モータル）を（。持（。たない（。イ）」、言葉（。や（。旋律（。へと（。昇華（。された（。、精神の（。純粋（。な（。残（。像。"),
    ("archaic", "Archaic", "古風な、古語の", "18th Century", "arkhe (beginning)", "Of, relating to, or characteristic of a much earlier or primitive period", "単に（。古い（。のではなく（。、文明（。が（。始まった「最初（。アーク）の（。記憶（。）」を（。宿（。して（。いる（。こと（。。（。剝（。き（。出し（。の（。剥（。製（。のように（。、原初（。の（。エナジー（。を（。今（。へと（。運（。んで（。くる（。、聖なる（。遺物。"),
    ("contemporary", "Contemporary", "現代の、同時代の", "17th Century", "com- (together) + tempus (time)", "Living or occurring at the same time", "過去の（。亡霊（。に（。囚（。われ（。ず（。、今（。この（。瞬間を「共（。に（。コン）刻（。む（。テンパス）」者（。たち（。。（。激（。しく（。移（。ろ（。い（。ゆく（。現在（。という（。荒野（。を（。、共（。に（。駆（。け（。抜ける（。、孤独（。な（。同志。"),
    ("sequential", "Sequential", "連続的な、順次の", "19th Century", "sequi (to follow)", "Forming or following in a logical order or sequence", "混沌（。とした（。出来事（。の中から（。、一つ（。ひとつの（。因果関係（。を「後に（。続く（。セクイ）もの（。）」として（。丁寧（。（。に（。繋（。ぎ（。合（。わ（。せ（。た（。、知性の（。鎖。"),
    ("chronological", "Chronological", "年代順の", "17th Century", "khronos (time) + logos (word, study)", "Starting with the earliest and following the order in which they occurred", "「時（。クロノス）の（。言葉（。ロゴス）」。（。残酷（。な（。までに（。正確（。な（。、過去（。から（。未来へと（。至（。る（。、戻（。ら（。ない（。一方（。通行の（。記録（。の（。階段。"),
    ("sporadic", "Sporadic", "散発的な、時々起こる", "17th Century", "sporas (scattered)", "Occurring at irregular intervals or only in few places; scattered or isolated", "一貫性（。の（。鎖（。から（。外れ（。、まるで「種（。が（。蒔（。き（。散（。ら（。さ（。れた（。スポラ）」ように（。、予期（。せぬ（。場所（。に（。不意（。に（。あら（。わ（。れる（。、運命の（。さざ波。"),
    ("intermittent", "Intermittent", "断続的な、時々途切れる", "16th Century", "inter- (between) + mittere (to send)", "Occurring at irregular intervals; not continuous or steady", "常に（。押し（。寄せる（。のではなく（。、束の間の（。静寂の「間に（。インター）送（。り（。込ま（。れる（。ミッ）」、エナジーの（。断片（。。（。呼吸（。と（。拍動の（。ように（。、生と（。死の（。隙間を（。縫（。い（。合わせ（。て（。いく（。、時の（。点描画。"),
    ("persistent", "Persistent", "持続的な、粘り強い", "16th Century", "per- (through) + sistere (to stand)", "Continuing firmly or obstinately in a course of action in spite of difficulty or opposition", "嵐が（。吹き（。荒（。れ（。て（。も（。、その（。場所に「ずっと（。パー）立ち（。シスト）続ける（。）」、静（。かな（。る（。決意（。。（。一途（。な（。までの（。執念（。が（。、いつか（。運命（。の（。岩壁を（。も（。穿（。つ（。のですよ。"),
    ("longevity", "Longevity", "長寿、寿命", "17th Century", "longus (long) + aevum (age)", "Long life", "ただ（。長い（。だけでなく（。、一つ一つの「時代（。アエヴム）を（。長く（。ロング）引き（。延（。ばし（。）」、豊か（。な（。経験（。を（。魂に（。刻（。み（。込んだ（。果ての（。、存在の（。重み。"),
    ("obsolescence", "Obsolescence", "風化、旧式化、時代遅れ", "18th Century", "ob- (away) + solere (to be used to)", "The process of becoming obsolete or outdated and no longer used", "かつて（。当たり前（。だった（。習慣（。が（。、いつの間にか（。手元（。から「遠（。ざ（。か（。り（。オブ）忘れ（。去（。ら（。れて（。いく（。）」こと（。。（。新（。しい（。光が（。、古い（。影を（。飲（。み（。込（。んで（。いく（。、冷徹（。な（。時の（。選別。"),
    ("ancestry", "Ancestry", "祖先、系統、家系", "14th Century", "ante- (before) + cedere (to go)", "One's family or ethnic descent", "自分（。という（。川（。の（。流れ（。の（。「遥か（。前（。アンテ）を（。歩（。んで（。いた（。セド）者（。たち（。）」の（。記憶（。。（。あなた（。の（。中には（。、数（。え（。切れない（。魂の（。バトン（。が（。（。今も（。、静（。かに（。眠って（。いる（。のですよ。"),
    ("posterity", "Posterity", "後世、子孫", "14th Century", "posterus (coming after)", "All future generations of people", "自分（。が（。去（。った（。「後に（。ポスト）来る（。）」、まだ（。見ぬ（。者たちへの（。贈り（。物（。。（。あなた（。の（。今日（。の一行が（。、遥（。かな（。未来（。を（。生きる（。誰（。かの（。、暗い（。夜を（。照（。らす（。星（。に（。なる（。かも（。し（。れません。"),
    ("epoch", "Epoch", "新時代、画期的な事件", "17th Century", "epokhe (check, stop, fixed point)", "A period of time in history or a person's life, typically one marked by notable events or particular characteristics", "漫然（。と（。流れる（。時間の（。川を（。、「一時（。停止（。エポケー）」させて（。しまう（。ほどの（。、巨大（。な（。一歩（。。（。そこ（。から（。世界（。の（。色（。が（。一変（。して（。しまう（。、運命の（。転換点。"),
    ("millennium", "Millennium", "千年紀、ミレニアム", "17th Century", "mille (thousand) + annus (year)", "A period of a thousand years", "「千（。ミレ）の（。太陽（。年（。アン））」が（。巡（。り（。、国家（。や（。言語（。さえも（。変貌（。させて（。しまう（。、宇宙的（。な（。時間の（。スケール（。。（。その（。巨大（。な（。歴史（。の（。前（。では（。、一つ一つの（。悩み（。は（。、一瞬（。の（。瞬き（。に（。過（。ぎ（。ません。"),
    ("perennial", "Perennial", "多年生の、永続する、多年生植物", "17th Century", "per- (through) + annus (year)", "Lasting or existing for a long or apparently infinite time; enduring or continually recurring", "冬の（。寒（。さに（。一度（。枯（。れた（。ように（。見えても（。、地下（。深くで（。エナジーを（。蓄（。え（。、「年（。アン）を（。通（。じて（。パー）」何度（。でも（。蘇（。り（。、花（。を（。咲（。か（。せ（。続ける（。、生命（。の（。不屈の（。リズム。"),
    ("anachronism", "Anachronism", "時代錯誤、時代遅れのもの", "17th Century", "ana- (against, backwards) + khronos (time)", "A thing belonging or appropriate to a period other than that in which it exists, especially a thing that is conspicuously old-fashioned", "本来（。の「時（。クロノス）の流れ（。の中には（。、あり（。得ない（。アナ）」不純（。物の（。混入（。。（。過去（。の（。誇（。りを（。今に（。持ち（。込（。む（。、あるいは（。未来（。を（。先取り（。し（。すぎ（。た（。、孤独（。な（。異邦（。人。"),
    ("synchronicity", "Synchronicity", "共時性、シンクロニシティ", "19th Century", "sun- (together) + khronos (time)", "The simultaneous occurrence of events which appear significantly related but have no discernible causal connection", "因果（。関係（。を（。超え（。、二つの（。出来事が「共に（。シン）同じ（。時（。クロノス）に（。）」あら（。わ（。れる（。、宇宙（。の（。粋（。な（。計（。らい（。。（。偶然（。を（。装（。った（。、運命の（。ウィンク。")
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
            word_id = f"{word_text.lower()}_time"
            
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
                    "aftertaste": item[7] if len(item) > 7 else "時間は、命が自らのかたちを刻み込むための、透明な彫刻刀です。",
                    "example": f"The {word_text} of the concert was exactly two hours.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["永遠とは、長い時間の果てにあるものではなく、今この瞬間の深みの中に隠されているものです。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["momentary", "transient", "permanent", "perpetual", "immortal", "archaic", "contemporary", "sequential", "chronological", "sporadic", "intermittent", "persistent", "perennial"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Time & Eternity (Cycle 36).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
