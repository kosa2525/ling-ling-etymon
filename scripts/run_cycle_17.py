import json
import re

words_data = [
    ("luminescence", "Luminescence", "冷光、発光", "19th Century", "lumen (light)", "The emission of light by a substance that has not been heated", "一切の熱気を伴わず、化学反応や生命の神秘のみによって暗闇の中に静かに生み出される、純粋で幽霊のような「青白い結晶」。", "深海のクラゲが放つ「ルミネッセンス（冷光）」は、熱狂することなく感情を伝える最高のコミュニケーションです。"),
    ("incandescence", "Incandescence", "白熱、高温発光", "18th Century", "incandescere (glow)", "The emission of light from a hot body as a result of its temperature", "物質が自らの限界まで温度を上げ、熱エネルギーが光となって溢れ出してしまう、圧倒的な「物理的燃焼」の極北。", "フィラメントの「インカンデッセンス（白熱の輝き）」を見ると、全ての命を燃やし尽くす潔さを感じます。"),
    ("fluorescence", "Fluorescence", "蛍光", "19th Century", "fluorite (a mineral)", "The visible or invisible radiation emitted by certain substances as a result of incident radiation of a shorter wavelength", "外部から目に見えないエネルギーを受け取り、それを独自の毒々しくも魅力的な「極彩色の光」へと変換して反射する自己主張。", "サイバーパンクな街並みに輝く「フルオレッセンス（蛍光色）」の看板は、眠らない欲望のサインです。"),
    ("phosphorescence", "Phosphorescence", "燐光（りんこう）", "18th Century", "phosphorus (light-bringing)", "Light emitted by a substance without combustion or perceptible heat", "光が消え去った後も、蓄えられたエネルギーを少しずつ放出することで、時間そのものを「発光しながら遅延させる」記憶の残響。", "暗闇でぼんやりと緑色に「フォスフォレッセント（燐光を放つ）」時計の針は、夜という時間の深さを教えてくれます。"),
    ("bioluminescence", "Bioluminescence", "生物発光", "20th Century", "bios (life) + luminescence", "The biochemical emission of light by living organisms", "電気でも太陽でもなく、自らの体内で化学物質を調合し、暗黒の深海や夜空に生命の「意志の光」を灯す奇跡のメカニズム。", "ホタルの「バイオルミネッセンス（生命の光）」は、短い夏だけ開かれる光の儚いオーケストラです。"),
    ("iridescence", "Iridescence", "虹色、真珠光沢", "18th Century", "iris (rainbow)", "A lustrous rainbow-like play of color caused by differential refraction of light waves", "見る角度によって色が万華鏡のように変化し続け、決して一つの「真実の色」を固定させないシャボン玉や真珠の魔法。", "カラスの濡れ羽の「イリデッセンス（虹色の光沢）」は、不遇の象徴ではなく宇宙の複雑さの現れです。"),
    ("opalescence", "Opalescence", "オパール光沢、乳白色の輝き", "19th Century", "opalus (opal)", "Exhibiting a milky iridescence like that of an opal", "乳白色のベールの内部で、青やピンクの柔らかな光が雲の奥から差し込む太陽のように「ぼんやりと乱反射」する神秘性。", "朝霧に包まれた湖面は「オパレッセンス（乳白色の虹彩）」を放ち、現実世界を幻想のフィルムでおおいます。"),
    ("effulgence", "Effulgence", "まばゆい輝き、さんさんたる光", "17th Century", "ex- (out) + fulgere (to shine)", "A brilliant radiance; a shining forth", "内側から抑えきれずに溢れ出し、周囲の闇を完全に圧倒して何も見えなくしてしまうような、神々しく暴力的な「光の氾濫」。", "彼女のドレス姿の「エファルジェンス（まばゆい輝き）」に、その場の誰もが呼吸を忘れて立ち尽くしました。"),
    ("coruscation", "Coruscation", "きらめき、ひらめき", "15th Century", "coruscare (to flash)", "A sudden gleam or flash of light", "ダイヤモンドが光を浴びたときのように、鋭く、鋭角的に「無数の閃光」をパラパラと周囲に弾き飛ばす硬質な美しさ。", "彼の天才的なアイデアは、退屈な会話の中で時折「コーラスケーション（鋭い閃光）」を放ち、場を魅了しました。"),
    ("scintillation", "Scintillation", "火花を散らすこと、才気煥発", "17th Century", "scintilla (spark)", "A flash or sparkle of light", "星の瞬きのように、チカチカと不規則に「細かく明滅」を繰り返し、対象の存在を捉えどころのない魅力的なものにする光のダンス。", "ワイングラスの中で弾ける「シンティレーション（繊細な煌めき）」のように、私たちの会話もずっと美しく続きました。")
]

words = []
for item in words_data:
    root1 = item[4].split(" ")[0]
    meaning1 = " ".join(item[4].split(" ")[1:]).strip("()")
    w = {
        "id": f"{item[0]}_glow",
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
        "example": f"I was mesmerized by its {item[0]}.",
        "deep_dive": {
            "roots": [{"term": root1, "meaning": meaning1}],
            "points": ["光の色や性質を区別することは、感受性の解像度を上げることです。"]
        },
        "part_of_speech": "noun"
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
    print(f"Success: Added {added} words. Theme: Various Glows (Cycle 17).")
else:
    print("Error parsing data.js")
