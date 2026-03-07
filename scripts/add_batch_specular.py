import json
import re

word_batch = [
    # Cycle 152: Mirror & Echo (Refined)
    {
        "id": "specular_mirror",
        "word": "Specular",
        "meaning": "鏡のような、鏡面反射の、(医学)翼状片の",
        "era": "16th Century Latin speculum",
        "etymology": {
            "components": ["speculum (mirror)", "specere (to look)"],
            "original_statement": "From Latin specularis (of or like a mirror), from speculum (mirror), from specere (to look at)."
        },
        "concept": "Mirror-like reflection (「光（light）」を 「散らさず（orderly）」に 跳ね返し 「真の姿（true image）」を そのまま 「再現」すること)",
        "thinking": "表面で光を吸収したり乱したりすることなく、入ってきたエネルギーを 完璧な 秩序（アングル）で 投げ返す、揺るぎない 正直さ. 語源は「鏡、見る」. それは 自分の主張を 排し 世界のありのままを 肯定しようとする 聖なる「目撃」の 質感です. 反射は、敬意の一つの形です.",
        "aftertaste": "正直な反射. 自分自身の「解釈」という名の ノイズを 取り除こう. あなたが「スペキュラー（鏡面の）」な 心で 世界と向き合うとき 隠されていた 本質の美しさが 鮮やかに 浮かび上がるのだから.",
        "example": "The specular reflection of the mountains in the smooth surface of the lake was so clear it looked like another world.",
        "deep_dive": { "roots": [{"term": "spek-", "meaning": "to observe"}], "points": ["speculate（推測する：鏡に映る予兆を見る）と同じ。見えない先を、今の光で捉える力。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "reverberate_echo",
        "word": "Reverberate",
        "meaning": "鳴り響く、反響する、(影響が)残る、照り返す",
        "era": "16th Century Latin re- + verberare",
        "etymology": {
            "components": ["re- (back)", "verberare (to beat, strike)"],
            "original_statement": "From Latin reverberatus, past participle of reverberare (to beat back, repel), from re- (back) + verberare (to beat, strike, lash), from verber (a whip, lash, rod)."
        },
        "concept": "Striking back (「声（voice）」が 「境界（wall）」を 叩き 「再び（again）」 戻ってくることで 意味を 「増幅」させること)",
        "thinking": "一度の 発声で 終わることなく 周囲の環境（他者）との 絶え間ない 相互作用によって 音が 空間全体を 支配していく 圧倒的な 余韻. 語源は「打ち返す、鞭打つ」. それは 単なる反復ではなく 境界線を 叩くことで 自分の 存在を 再確認（エコー）し続ける 聖なる「共鳴」のアクションです.",
        "aftertaste": "共鳴の余韻. あなたの言葉が「リヴァーバレイト（反響）」し 誰かの心の壁を 叩くことを 恐れないで. その 震えの 往復こそが 孤独な魂を 結び付ける 唯一の 絆に なるのだから.",
        "example": "The judge's powerful and stern voice continued to reverberate through the silent courtroom.",
        "deep_dive": { "roots": [{"term": "wer-", "meaning": "to turn, bend"}], "points": ["vibrate（振動する）や verse（韻文：繰り返し戻るもの）と同じ。リズムという名の、生の鼓動。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "catoptric_mirror",
        "word": "Catoptric",
        "meaning": "反射光学の、反射の",
        "era": "17th Century Greek kata- + optos",
        "etymology": {
            "components": ["kata- (down, back)", "optos (seen)"],
            "original_statement": "From Greek katoptrikos, from katoptron (mirror), from kata- (down, against, back) + opsesthai (to be going to see), from root of op- (to see)."
        },
        "concept": "Seeing back (「視線（sight）」が 「反転（reverse）」し 「自分自身（self）」を 客観的な 「光」として 捉え直すこと)",
        "thinking": "真っ直ぐに進むだけでは 気付くことのできない 自分の 背後や 盲点を 鏡という名の「介入者」を 通じて 誠実に 認識し直すこと. 語源は「反射して見える」. それは 自己満足の 殻を 打ち破り 世界と 自分を 対等な 光の 往来として 理解しようとする 高次な 知性の 視座です.",
        "aftertaste": "客観の視え（みえ）. 自分の見たいものだけを 見つめないで. あなたが「カトプトリック（反射的）」な 視点を持てたとき あなたは 誰よりも 深く 自らの 可能性と 誠実に 出会うことができるのだから.",
        "example": "Early telescopes used catoptric systems with curved mirrors to focus distant starlight.",
        "deep_dive": { "roots": [{"term": "okw-", "meaning": "to see"}], "points": ["optic（光学の）や eye（目）と同じ。光を「受け止める」という、受容のアクション。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "resonate_echo",
        "word": "Resonate",
        "meaning": "共鳴する、響き渡る、(心に)響く、共感する",
        "era": "19th Century Latin re- + sonare",
        "etymology": {
            "components": ["re- (again)", "sonare (to sound)"],
            "original_statement": "From Latin resonatus, past participle of resonare (to sound back, resound, echo), from re- (again) + sonare (to sound)."
        },
        "concept": "Sounding again (「一つ（one）」の 振動が 「他（other）」を 「震わせ（shake）」 全体が 「調和（harmony）」の 只中（ただなか）に 在ること)",
        "thinking": "物理的な音波を超えて、誰かの想いや 普遍的な真理が、自分の魂と同じ周波数で 震え始めるという、宇宙的な「出会い」の瞬間. 語源は「再び鳴る」. それは 孤立した自我を 溶かし 私たちが 根源的に 繋がっていることを 証明する、聖なる「共振（バイブス）」です.",
        "aftertaste": "魂の共振. 孤独だと思わないで. あなたが 正直な 振動（言葉）を 放ち続ける限り それに「レゾネイト（共鳴）」する 誰かが 必ず この世界の どこかに 現れるのだから.",
        "example": "The themes of love and sacrifice in the movie really resonated with audiences around the world.",
        "deep_dive": { "roots": [{"term": "swen-", "meaning": "to sound"}], "points": ["sonic（音の）や sonata（ソナタ）と同じ。生命を 旋律へと 変える力。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "reflect_echo",
        "word": "Reflect",
        "meaning": "反射する、反映する、熟考する、反省する",
        "era": "14th Century Latin re- + flectere",
        "etymology": {
            "components": ["re- (back)", "flectere (to bend)"],
            "original_statement": "From Old French reflectir, from Latin reflectere (to bend back, turn back), from re- (back) + flectere (to bend)."
        },
        "concept": "Bending back (「外（out）」へと 向かう 「エネルギー」を 「内（in）」へと 「折り返し（bend back）」 意味を 掘り下げること)",
        "thinking": "ただ跳ね返す（物理的反射）だけでなく、その光を自らの内側へと導き、過去の経験や 知識と 衝突させて、新しい理解（熟考）を 生み出すこと. 語源は「後ろへ曲げる」. それは 闇雲な 前進を 止め 静止の中で 意味を 再構築しようとする 知性の 最も 誠実な 祈りの形です.",
        "aftertaste": "折り返しの叡智. 外側の 刺激に 振り回されないで. あなたが 出来事を 内側へと「リフレクト（熟考/反射）」し 自分の核と 照らし合わせるとき 人生は 初めて 深い 輝きと 意味を 宿すのだから.",
        "example": "Take some time to reflect on your achievements this year and plan for your next big challenges.",
        "deep_dive": { "roots": [{"term": "bhelg-", "meaning": "to bend"}], "points": ["flexible（柔軟な）や deflect（逸らす）と同じ。しなやかに、しかし確固として 軌道を変える力。"] },
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
        print(f"Success: Added {added} words in Cycle 152.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
