import json
import re

words_data = [
    ("forge", "Forge", "鍛造する、偽造する", "14th Century", "fabrica (workshop)", "Make or shape a metal object by heating it in a fire or furnace and beating or hammering it", "高熱で赤く溶かした鉄を、人間の強靭な意志というハンマーで打ち据え、新しい「形」と「使い道」を持つ存在へと強制的に作り変えること。", "私たちの絆は、楽しい思い出だけでなく、共に乗り越えた幾つもの「フォージ（試練の鍛冶）」によって強固になるのです。"),
    ("smelt", "Smelt", "精錬する、溶解する", "16th Century", "smelten (to melt)", "Extract metal from its ore by a process involving heating and melting", "不純物にまみれた原石から、極限の熱を与えて本当に価値のあるピュアな本質だけを「選別し抽出」する残酷で必要なプロセス。", "自分の感情を「スメルト（精錬）」して、怒りという不純物から真っ直ぐな願いだけを取り出せれば。"),
    ("alloy", "Alloy", "合金、混ぜる", "16th Century", "alligare (to bind)", "A metal made by combining two or more metallic elements", "一つの金属では弱すぎるため、性質の異なる別の金属を「深く結合」させて、弱点を補い合う新しい完全体を生み出すこと。", "純粋な正義だけでは折れやすい。そこに優しさという「アロイ（合金）」を混ぜることで、初めてしなやかな強さが生まれます。"),
    ("temper", "Temper", "鍛える、和らげる", "Old English", "temperare (to mix, moderate)", "Improve the hardness and elasticity of an alloy or other metal by reheating and then cooling it", "灼熱と極寒の世界を交互に何度も体験させることで、その性質を「中庸（ちょうど良いバランス）」へと導き、絶対に折れないしなやかさを与えること。", "過酷な経験が人の心を「テンパー（鍛え、和らげ）」し、どんな悲しみにも耐えうる優しい強さを作り出します。"),
    ("anvil", "Anvil", "金床（かなとこ）", "Old English", "anfilte (anvil)", "A heavy iron block with a flat top, concave sides, and typically a pointed end, on which metal can be hammered and shaped", "何度ハンマーで力任せに打ち据えられても、決して自分が砕けることなく、相手が「形作られる」ための圧倒的に無口で硬い土台。", "怒りの「アンヴィル（金床）」の上で感情を叩き直せば、それはやがて誰かを守るための盾になります。"),
    ("hammer", "Hammer", "ハンマー、ハンマーで打つ", "Old English", "hamor (hammer)", "A tool with a heavy head and a handle, used for tasks such as breaking things and driving in nails", "理屈ではなく、純粋な物理的衝撃と「叩きつける力」だけを用いて、相手の抵抗をねじ伏せ自らの意志通りの形を強要する暴力の象徴。", "繊細な「ハンマー（木槌）」の使い分けを知らない人は、やがて全てを壊してしまうでしょう。"),
    ("weld", "Weld", "溶接する", "16th Century", "wellen (to boil, well up)", "Join together metal parts by heating the surfaces to the point of melting using a blowpipe, electric arc, or other means", "本来はバラバラの存在である二つの冷たい金属を、限界を超える熱で共に一旦「溶かし」、冷える時には一つの新しい命として繋ぎとめる奇跡。", "二人の人生を「ウェルド（溶接）」してひとつにするのが結婚ですが、火傷には注意が必要です。"),
    ("solder", "Solder", "はんだ付けする、結合する", "14th Century", "solidare (to make solid)", "Join with solder", "強引に一体化させるのではなく、二つの物質の間に入り込み、自らの身を溶かして冷え固まることで隙間なく「個体を繋ぐ」繊細な接着。", "壊れた関係も、コミュニケーションという「ソルダー（はんだ）」を使えば、前よりも美しく修復できることがあります。"),
    ("rivet", "Rivet", "リベットで留める、釘付けにする", "14th Century", "river (to attach)", "A short metal pin or bolt for holding together two plates of metal", "熱で溶かすのではなく、金属のピンを「貫通させて」物理的に強固に固定し、二度と引き剥がせないようにする確固たる絆。", "そのあまりに美しい歌声は、その場にいた観客全員の心を舞台へ「リベット（釘付けに）」してしまいました。"),
    ("grind", "Grind", "粉砕する、研磨する、辛い仕事", "Old English", "grindan (to rub together, crush)", "Reduce something to small particles or powder by crushing it", "二つの硬い面を過酷な圧力で「すり合わせ」、不要な表面を容赦なく削り落としていくことで、そこに滑らかで美しい輝きを生み出す摩擦の儀式。", "毎日の退屈な「グラインド（骨の折れる単純作業）」こそが、最後に最高のエスプレッソ（結果）を抽出するための準備なのです。")
]

words = []
for item in words_data:
    root1 = item[4].split(" ")[0]
    meaning1 = " ".join(item[4].split(" ")[1:]).strip("()")
    w = {
        "id": f"{item[0]}_metal",
        "word": item[0],
        "meaning": item[2],
        "era": item[3],
        "etymology": {
            "components": [item[4]],
            "original_statement": f"From {item[3]} {item[4]}."
        },
        "concept": item[5] + f" ({item[6]})",
        "thinking": item[6],
        "aftertaste": item[7],
        "example": f"The blacksmith expertly began to {item[0]} the piece.",
        "deep_dive": {
            "roots": [{"term": root1, "meaning": meaning1}],
            "points": ["金属の加工は、人間の精神的な試練と成熟の象徴です。"]
        },
        "part_of_speech": "noun" if item[0] in ["alloy", "anvil", "hammer", "rivet"] else "verb"
    }
    words.append(w)

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
if match:
    prefix, json_array_str, suffix = match.groups()
    existing_words = json.loads(json_array_str)
    existing_ids = {w.get("id") for w in existing_words}
    existing_word_texts = set(w.get("word").lower() for w in existing_words)
    
    added = 0
    for w in words:
        if w["id"] not in existing_ids and w["word"].lower() not in existing_word_texts:
            existing_words.append(w)
            added += 1
            existing_word_texts.add(w["word"].lower())
            
    new_content = content[:match.start()] + prefix + json.dumps(existing_words, ensure_ascii=False, indent='\t') + suffix + content[match.end():]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Success: Added {added} words. Theme: Metal & Forging (Cycle 15).")
else:
    print("Error parsing data.js")
