import json
import re

word_batch = [
    # Cycle 155: Bird & Sky (Refined)
    {
        "id": "aquiline_bird",
        "word": "Aquiline",
        "meaning": "鷲(わし)のような、(鼻が)鉤形の、鋭い",
        "era": "17th Century Latin aquila",
        "etymology": {
            "components": ["aquila (eagle)"],
            "original_statement": "From Latin aquilinus (of or pertaining to an eagle), from aquila (eagle)."
        },
        "concept": "Like an eagle (「高い視座（high view）」から 「獲物（truth）」を 鋭く 「射貫く（pierce）」 誇り高き 精神の 形状)",
        "thinking": "地上の 些事（さじ）に 囚われず、遥か 上空から 全体像を 把握し、ここぞという 瞬間に 迷いなく 急降下して 本質を 掴み取る（つかみとる）、峻厳（しゅんげん）な 知性の あり方. 語源は「鷲」. それは 誰にも 媚びず 自らの 信念に従って 孤独に 空を舞う、魂の 高潔さの 象徴です. 鋭さは、自由です.",
        "aftertaste": "鷲の視座. 目の前の 混乱に 翻弄されないで. あなたが「アキライン（鷲のような）」な 鋭い洞察を 持つとき 世界の 複雑な 仕組みは 明快な 地図となって あなたの 眼下に 広がるのだから.",
        "example": "He had a prominent, aquiline nose that gave his face a look of fierce intelligence and determination.",
        "deep_dive": { "roots": [{"term": "ak-", "meaning": "sharp"}], "points": ["acute（鋭い）や acid（酸っぱい）と同じ。真実を切り分ける、原初的な力。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "halcyon_bird",
        "word": "Halcyon",
        "meaning": "穏やかな、平和な、輝かしい、(伝説の)カワセミ",
        "era": "14th Century Greek halkyon",
        "etymology": {
            "components": ["hals (sea)", "kyon (conceiving)"],
            "original_statement": "From Latin halcyon, from Greek halkyon (kingfisher), from halk- (sea) + kyon (conceiving), from kyein (to swell, conceive)."
        },
        "concept": "Calming the sea (「荒れ狂う嵐（storm）」を 「静寂（stillness）」へと 変え 「平穏（peace）」を 呼び戻す 聖なる 存在感)",
        "thinking": "どんなに 周囲が 騒がしくても その存在が そこにあるだけで 誰もが 心穏やかに なれるような、圧倒的な「静謐（せいひつ）」の 輝き. 語源は「カワセミ（海で卵を産む時に風を鎮める鳥）」. それは 過去の 美しい 記憶（ハルシオン・デイズ）を 守り抜き 今、この瞬間に 再現しようとする 慈愛のアクションです.",
        "aftertaste": "静寂の魔法. 騒がしい 世界の ペースに 飲み込まれないで. あなたが「ハルシオン（平穏な）」な 精神を 保ち続けることで あなたの 周囲には 聖なる 凪（なぎ）が 広がり 全ては 本来の 輝きを 取り戻すのだから.",
        "example": "She often looked back on the halcyon days of her childhood, before the war changed everything forever.",
        "deep_dive": { "roots": [{"term": "sal-", "meaning": "salt (for hals)"}, {"term": "kew-", "meaning": "to swell (for kyon)"}], "points": ["salt（塩）や cup（カップ：膨らんだもの）と同じ。海と生命の神秘。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "plume_bird",
        "word": "Plume",
        "meaning": "羽飾り、(煙などの)柱、誇りに思う、(鳥が)羽を整える",
        "era": "14th Century Latin pluma",
        "etymology": {
            "components": ["pluma (feather, down)"],
            "original_statement": "From Old French plume, from Latin pluma (a feather, down)."
        },
        "concept": "Ornamental feather (「実用（utility）」を 越え 「美（beauty）」を 「誇視（display）」し 精神の 「気高さ」を 表現すること)",
        "thinking": "単なる 飛ぶための 道具 ではなく 自らの 存在の 素晴らしさを 世界に向けて 宣言するための 聖なる「装飾」. 語源は「羽毛」. それは 自分の 才能や 成就した 仕事を 正当に 誇り（自尊心） 自らを 最高の 状態に 整えようとする、前向きで 美しい 精神の 営みです. 誇りは、輝きです.",
        "aftertaste": "自尊の羽飾り. 謙遜しすぎて 自分を 卑下しないで. 自分の 成し遂げたことに「プリューム（羽飾り）」のような 誇りを持ち 颯爽（さっそう）と 胸を張って 生きていいのだから.",
        "example": "A magnificent plume of white smoke rose from the volcano, reaching high into the clear blue sky.",
        "deep_dive": { "roots": [{"term": "plu-", "meaning": "to fly, float (possible root)"}], "points": ["fly（飛ぶ）や float（浮く）と同じ。空気と戯れる、軽やかな美。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "aviary_bird",
        "word": "Aviary",
        "meaning": "大型鳥舎、(集合的な)鳥たち",
        "era": "16th Century Latin avis",
        "etymology": {
            "components": ["avis (bird)"],
            "original_statement": "From Latin aviarium (place where birds are kept), from avis (bird)."
        },
        "concept": "House of birds (「自由な魂（birds）」を 「保護（protect）」し 「多様な共鳴（harmonious songs）」を 育む 聖なる 空間)",
        "thinking": "個々の 鳥が それぞれの 歌を 歌いながらも 一つの 共同体（アヴィアリー）として 調和している 音楽的な 空間の 隠喩. 語源は「鳥の場所」. それは 私たちの 精神が 様々な インスピレーション（鳥）を取り込み それらを 安全に 育て上げ、羽ばたかせるための 聖なる「知性の 揺りかご」です.",
        "aftertaste": "インスピレーションの籠. 自分の心に 飛び込んできた 幽かな アイディア（鳥）を 逃がさないで. その「アヴィアリー（鳥舎）」の中で 大切に 育むことで それは やがて 世界を 驚かせる 美しい 歌声に なるのだから.",
        "example": "The zoo's new tropical aviary allowed visitors to walk among hundreds of exotic species flying freely.",
        "deep_dive": { "roots": [{"term": "awi-", "meaning": "bird"}], "points": ["aviation（航空）や auspicious（幸先の良い：鳥占いから）と同じ。空からの導き。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "soar_bird",
        "word": "Soar",
        "meaning": "舞い上がる、急上昇する、(希望などが)高まる",
        "era": "14th Century Latin ex- + aura",
        "etymology": {
            "components": ["ex- (out)", "aura (breeze, air)"],
            "original_statement": "From Old French essorer (to fly up, to soar), from Vulgar Latin exaurare (to expose to the air), from ex- (out) + aura (breeze, air)."
        },
        "concept": "Exerting into the air (「重力（limit）」の 束縛を 断ち切り 「天空（infinity）」へと 魂の 翼を 一気に 押し広げること)",
        "thinking": "羽ばたき（努力）を やめるのではなく 風の力を 味方につけることで 最小限の 労力で 最大限の 高みへと 辿り着く、優雅で 圧倒的な 飛翔. 語源は「空気に晒す（さらす）」. それは 閉ざされた 部屋を 出て 宇宙の 巨大な 流れと 一体化しようとする、聖なる「解放」の アクションです.",
        "aftertaste": "無限の飛翔. 安全な 地面ばかりを 見つめないで. あなたの 魂が「ソアー（舞い上がる）」し 自由の風に 身を任せたとき 人生は かつてない 壮大で 清々しい 景色を 見せてくれるのだから.",
        "example": "Our spirits began to soar as we finally reached the mountain peak and saw the sun rising over the clouds.",
        "deep_dive": { "roots": [{"term": "wer-", "meaning": "to raise, lift (associated with aura)"}], "points": ["aura（オーラ：空気、輝き）や air（空気）と同じ。目に見えない力の「現出」。"] },
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
        print(f"Success: Added {added} words in Cycle 155.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
