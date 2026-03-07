import json
import re

word_batch = [
    # Cycle 115: Bridge & Path
    {
        "id": "pilgrimage_path",
        "word": "Pilgrimage",
        "meaning": "巡礼、長い旅、魂の旅路",
        "era": "12th Century Latin peregrinus",
        "etymology": {
            "components": ["peregrinus (foreign)"],
            "original_statement": "From Old French peligrinage, from peligrin (pilgrim), from Latin peregrinus (foreign, coming from abroad)."
        },
        "concept": "Journey through fields (住み慣れた土地を離れ 「野（fields）」を「横断（through）」し 聖なる場所を目指す旅)",
        "thinking": "単なる移動ではなく 目的地に辿り着くまでの「過程」そのものを通じて 魂を浄化し 真実の自分に出会うための神聖な旅. 語源は「外国の」や「野を越える」こと. それは 自分が知っている安全な境界線を飛び出し 未知の世界へ、あるいは内なる深淵へと足を踏み出す 勇気ある冒険です.",
        "aftertaste": "魂の巡礼. あなたが今 迷っているその道も また聖なる旅の一部なのだ. 目的地に急ぐ必要はない. その一歩一歩の揺らぎの中にこそ 真実の美しさが宿っているのだから.",
        "example": "For many, the journey to the ancient temple was a life-changing pilgrimage of faith.",
        "deep_dive": { "roots": [{"term": "per-", "meaning": "through"}, {"term": "ager-", "meaning": "field"}], "points": ["peregrine（ハヤブサ：旅する鳥）と同じ。自由と越境の象徴。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "transit_path",
        "word": "Transit",
        "meaning": "通過、変遷、乗り継ぎ、移ろい",
        "era": "15th Century Latin trans- + ire",
        "etymology": {
            "components": ["trans- (across)", "ire (to go)"],
            "original_statement": "From Latin transitus (a passing over, passage), from transire (to go over, go across, pass)."
        },
        "concept": "Going across (境界や時間を「超えて（across）」 「進んでいく（go）」 絶え間なき移動)",
        "thinking": "一つの状態に留まることなく 常に次の場所へと「移ろい続けている」 その儚くも力強い動性. 語源は「横切ること」. 私たちは人生という名の巨大な駅の待合室にいるような存在で すべては一時的な（transient）通過点に過ぎません. その「移ろい」を愛したとき 執着という名の呪縛から解放されます.",
        "aftertaste": "移ろう景色. 人生は目的地ではなく 常に「通過（トランジット）」の中にある. 流れゆく車窓の景色を 慈しむような心で 今日という日を通り抜けてゆこう.",
        "example": "The package is currently in transit and should arrive by tomorrow evening.",
        "deep_dive": { "roots": [{"term": "trans-", "meaning": "across"}, {"term": "ei-", "meaning": "to go"}], "points": ["exit（出口）や transition（変遷）と同じ。とどまらぬ生命のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "passageway_path",
        "word": "Passageway",
        "meaning": "通路、廊下、(人生の)過渡期",
        "era": "17th Century pass + way",
        "etymology": {
            "components": ["pass (to step, go by)", "way (path, road)"],
            "original_statement": "From passage + way. Passage from Latin passus (a step)."
        },
        "concept": "A path of steps (「一歩（step）」ずつ踏み締めながら 「通り抜けていく（pass）」ための 「道（way）」)",
        "thinking": "広い広場ではなく 限定された細長い空間. それは どこからどこかへ繋がる 必然的な「導線」であり 選択が許されないからこそ 迷いなく進める場所でもあります. 語源の passus は「歩み」. 暗いトンネルのような時期も それは次の輝かしい扉へと続く 確かな通路（パッサージュ）なのです.",
        "aftertaste": "導きの回廊. 通路が暗いのは 出口の光をより鮮やかに見せるためだ. 足元の感触を信じて 迷わずその一歩を 進め続けてゆけばいい.",
        "example": "He walked down the narrow stone passageway leading to the hidden garden secret.",
        "deep_dive": { "roots": [{"term": "pete-", "meaning": "to spread (possible for pass)"}], "points": ["compass（コンパス：共に歩む一歩）と同じ。歩幅こそが、世界の広さを決める。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "conduit_path",
        "word": "Conduit",
        "meaning": "導管、水路、媒介、(情報の)伝達路",
        "era": "14th Century Latin con- + ducere",
        "etymology": {
            "components": ["con- (together)", "ducere (to lead)"],
            "original_statement": "From Old French conduit, from Medieval Latin conductus (a defense, escort; a pipe, canal), from Latin conducere (to lead together, join, combine)."
        },
        "concept": "Leading together (エネルギーや情報を「束ねて（together）」 目的地へと「導く（lead）」管)",
        "thinking": "自分自身が源泉（ソース）になるのではなく 大いなる何かを運ぶための「透明なパイプ」になること. 語源は「共に導く」. あなたがエゴを捨て 純粋な媒介（コンジット）となったとき 宇宙の豊かな智慧や愛が あなたという管を通って 世界へと淀みなく流れ出していきます.",
        "aftertaste": "透明な器. あなたが世界の美しさや悲しみを 伝えるための「通り道」になれたなら. そのとき あなたの人生は 宇宙の大きな循環の一部として 永遠の価値を持つだろう.",
        "example": "The arts often serve as a conduit for cultural understanding and cross-border empathy.",
        "deep_dive": { "roots": [{"term": "deuk-", "meaning": "to lead"}], "points": ["educate（教育する：引き出す）や duke（公爵：導く人）と同じ。導きの力のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "wayfare_path",
        "word": "Wayfare",
        "meaning": "旅をする、道を行く、旅情",
        "era": "14th Century way + fare",
        "etymology": {
            "components": ["way (path)", "fare (to go, travel)"],
            "original_statement": "From Middle English weyferen, from way (noun) + fare (verb)."
        },
        "concept": "Going on the way (自分の決めた「道（way）」を 「進んでいく（go）」 終わりのない旅)",
        "thinking": "特定の目的地に着くことよりも 旅をすることそのものに 喜びと生きがいを見出すこと. 語源の fare は「行く」こと. 別れの挨拶「Farewell（さらば：善く行け）」にも含まれるこの言葉は 人生そのものが 一瞬一瞬の別れと出会いを繰り返す 永遠の道行（みちゆき）であることを教えてくれます.",
        "aftertaste": "終わらぬ道行. どこへ行くかではなく どう歩くか. あなたが踏み出すその一歩に 誠実さと愛が宿っているなら その道はどこへ通じていても 常に正解なのだ.",
        "example": "The weary wayfarer stopped to rest by the side of the road as the sun began to set.",
        "deep_dive": { "roots": [{"term": "por-", "meaning": "going, passage (possible for fare)"}], "points": ["ferry（フェリー）や ford（浅瀬）と同じ。渡り、進む力のルーツ。"] },
        "part_of_speech": "verb"
    }
]

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
    if match:
        prefix, json_array_str, suffix = match.groups()
        words = json.loads(json_array_str)
        existing_ids = {w.get("id") for w in words}
        
        added = 0
        for item in word_batch:
            if item["id"] not in existing_ids:
                words.append(item)
                added += 1
        
        new_content = content[:match.start()] + prefix + json.dumps(words, ensure_ascii=False, indent='\t') + suffix + content[match.end():]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Success: Added {added} words in Cycle 115.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
