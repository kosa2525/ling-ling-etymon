import json
import re

word_batch = [
    # Cycle 112: Flame & Passion
    {
        "id": "ardor_passion",
        "word": "Ardor",
        "meaning": "情熱、熱意、熱心、燃えるような熱さ",
        "era": "14th Century Latin ardere",
        "etymology": {
            "components": ["ardere (to burn)"],
            "original_statement": "From Old French ardor, from Latin ardorem (a flame, fire, burning, heat), from ardere (to burn)."
        },
        "concept": "Burning heat (内側から「燃え上がる（burn）」ような 切実で激しい「熱量（heat）」)",
        "thinking": "単なる好きという感情を超え 魂が薪（まき）となって燃え尽きることを厭わないほどの 烈（はげ）しい意志. 語源は「燃える」. それは暗闇を照らす灯火（ともしび）であり 凍えた心を溶かす太陽でもあります. あなたが何かに我を忘れて没頭するとき そこには聖なる火が宿っています.",
        "aftertaste": "燃ゆる魂. あなたの胸にあるその火を 絶やしてはならない. それはあなたがこの世界で 命を燃やして生きているという 唯一の証明なのだから.",
        "example": "He spoke with such ardor about his vision for the future that the entire audience was moved.",
        "deep_dive": { "roots": [{"term": "as-", "meaning": "to burn, glow"}], "points": ["ash（灰）や arid（乾燥した：焼けた）と同じ、火の極致のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "fervor_passion",
        "word": "Fervor",
        "meaning": "熱烈、熱情、白熱",
        "era": "14th Century Latin fervere",
        "etymology": {
            "components": ["fervere (to boil, glow, rage)"],
            "original_statement": "From Old French fervor, from Latin fervorem (boiling heat, heat, ardor), from fervere (to boil, glow, rage)."
        },
        "concept": "Boiling heat (水が「沸騰（boil）」するように 感情が激しく「煮え立つ」熱気)",
        "thinking": "冷静さを保てなくなるほどに 内部エネルギーが極限まで高まり 溢れ出そうとしている状態. 語源は「沸騰する」. それは静かな熱ではなく 泡立ち 弾け 周囲を巻き込んでいく動的な力です. 信仰や愛が「白熱」するとき 人は限界を越えた力を発揮します.",
        "aftertaste": "煮えたぎる予感. 冷静な知性もいいけれど 時にはその沸騰する熱情に身を任せ 魂の深部を熱く焦がしてみるのも悪くない.",
        "example": "The spectators cheered with religious fervor as their team scored the winning goal.",
        "deep_dive": { "roots": [{"term": "bhreu-", "meaning": "to boil, bubble, burn"}], "points": ["brew（醸造する）や breath（息：温かい空気）と同じ、生命の熱量。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "incandescence_passion",
        "word": "Incandescence",
        "meaning": "白熱、光輝、強烈な輝き",
        "era": "18th Century Latin in- + candere",
        "etymology": {
            "components": ["in- (within, into)", "candere (to shine, be white)"],
            "original_statement": "From French incandescence, from Latin incandescere (to become white-hot, glow), from in- (within) + candescere (to begin to glow), from candere (to shine, be white)."
        },
        "concept": "Shining from within (内なる熱によって 物質が「白く（white）」光り輝く「白熱（glow）」状態)",
        "thinking": "極限まで高められた情熱が ついに「光」へと変わる奇跡的な瞬間. 語源の candere は 混じりけのない「白」や「輝き」を指します. あなたの意志が不純物を焼き尽くし 純粋な光となって周囲を照らし出すとき それはもはや言葉を必要としない 圧倒的な説得力となります.",
        "aftertaste": "白光の意志. あなたが本気で燃えるとき 世界はその輝きに目を細め あなたという眩い存在を 祝福せずにはいられないだろう.",
        "example": "The incandescence of her genius was evident in every brushstroke of the painting.",
        "deep_dive": { "roots": [{"term": "kand-", "meaning": "to shine"}], "points": ["candidate（候補者：白い服を着た人）や candle（ロウソク）と同じ、純粋な光。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "zeal_passion",
        "word": "Zeal",
        "meaning": "熱意、熱心、熱衷",
        "era": "14th Century Greek zelos",
        "etymology": {
            "components": ["zelos (emulation, jealousy, fervor)"],
            "original_statement": "From Old French zel, from Late Latin zelus, from Greek zelos (emulation, rivalry, jealousy, fervor)."
        },
        "concept": "Eager rivalry (誰かと競い合うような 激しく「ひたむき」な「情熱（fervor）」)",
        "thinking": "特定の目的や理想を追い求める際に 脇目も振らずに突き進む 鋭角な熱意. 語源には「嫉妬」や「競合」の意味も含まれていました. それは 誰よりも 何よりもそれを大切にしたいという 独占的で切実な愛の形でもあります. あなたの「ひたむきさ」は 世界を動かす最初の一撃です.",
        "aftertaste": "ひたむきな刃. あなたがその目標に注ぐ熱意は どんなに厚い壁をもいつか必ず 鮮やかに切り裂いてゆくだろう.",
        "example": "He approached his new job with a zeal that impressed even the most veteran employees.",
        "deep_dive": { "roots": [{"term": "ya-", "meaning": "to seek, desire"}], "points": ["zealous（熱心な）のルーツ。情熱は、欠由を埋めようとする『飢え』でもある。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "ignite_passion",
        "word": "Ignite",
        "meaning": "火を点ける、燃え上がらせる、感情を燃え立たせる",
        "era": "17th Century Latin ignis",
        "etymology": {
            "components": ["ignis (fire)"],
            "original_statement": "From Latin ignitus, past participle of ignire (to set on fire), from ignis (fire)."
        },
        "concept": "Setting on fire (「火（fire）」を放ち 沈黙していた存在を「燃え上がらせ（ignire）」ること)",
        "thinking": "静止していた心に 一つの火花が散り そこから新しい物語が爆発的に始まること. 語源の ignis は 聖なる火をも意味します. あなたの何気ない出会いや言葉が 他人の心に火を点け 時代を照らす灯明（とうみょう）になるかもしれない. 点火の瞬間 それは宇宙が誕生した瞬間の再現です.",
        "aftertaste": "点火の瞬間. あなたの言葉が 誰かの心の冷えた暗闇に 最初の小さな火を灯した. その火は やがて大きな未来を照らし出すだろう.",
        "example": "His speech was intended to ignite the listeners' passion for social justice.",
        "deep_dive": { "roots": [{"term": "egni-", "meaning": "fire"}], "points": ["igneous（火成の）や ignition（点火）と同じ。意志の火のルーツ。"] },
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
        print(f"Success: Added {added} words in Cycle 112.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
