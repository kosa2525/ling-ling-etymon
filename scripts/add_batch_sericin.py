import json
import re

word_batch = [
    # Cycle 150: Silk & Softness (Refined)
    {
        "id": "sericin_silk",
        "word": "Sericin",
        "meaning": "セリシン、絹膠(けんこう)、シルクの光沢成分",
        "era": "19th Century Greek serikos",
        "etymology": {
            "components": ["serikos (silken)"],
            "original_statement": "From Greek serikos (of silk), from seres (the Chinese, literally 'silk people')."
        },
        "concept": "Silk glue (「絆（bond）」を 司る 聖なる 「膠（glue）」 として 繊細な 命の糸を 「守り、輝かせる」こと)",
        "thinking": "シルクの繊維を包み込み、保護し、あの独特の深みのある光沢を与える、目に見えない「慈愛のベール」. 語源は「シルクの民（中国）」. それは 表面的な美しさではなく 芯にある強さを 守り抜き、世界に向けて 最高の色を 放たせるための 献身的な 存在です. 守護は、輝きです.",
        "aftertaste": "守護のベール. 自分の繊細な 部分を 恥じないで. あなたの内側にある「セリシン（絹膠）」が その繊細さを 守り抜き いつか 世界を 魅了する 本物の 輝きへと 変えてくれるのだから.",
        "example": "Sericin is a natural protein produced by silkworms that helps bind the silk fibers together during cocoon formation.",
        "deep_dive": { "roots": [{"term": "ser-", "meaning": "silk (non-IE)"}], "points": ["sericulture（養蚕）の語源。絹の道（シルクロード）が運んだ、知性の手触り。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "velvety_softness",
        "word": "Velvety",
        "meaning": "ベルベットのような、滑らかな、(ワインなどが)口当たりのよい",
        "era": "16th Century Latin villus",
        "etymology": {
            "components": ["villus (shaggy hair, tuft of hair)"],
            "original_statement": "From Old French velu (shaggy, hairy), from Latin villus (shaggy hair, tuft of hair, nap of cloth)."
        },
        "concept": "Like shaggy hair (「微細な（microscopic）」 柔らかさが 重なり合い 「触れ合う（touch）」 全てのものを 「優しく包み込む」こと)",
        "thinking": "硬い衝突を拒み、あらゆる刺激を 吸収して 穏やかな 喜びに変えてしまう、圧倒的な「受容性」の 質感. 語源は「むくむくした毛」. それは 物理的な手触りだけでなく 誰かの 過ちや 孤独を さりげなく 包み込んでしまう 慈悲深い 精神の あり方の 隠喩でもあります.",
        "aftertaste": "受容の優しさ. 尖（とが）った心で 誰かを 傷つけないで. あなたが「ヴェルヴェッティ（滑らかな）」な 寛容さを 持つとき どんな冷たい言葉も 聖なる 癒やしに 変わってゆくのだから.",
        "example": "The wine had a rich, velvety texture that lingered pleasantly on the palate.",
        "deep_dive": { "roots": [{"term": "wel-", "meaning": "to tear, pull (possible root)"}], "points": ["villus（じゅう毛）や villi（小腸の突起）と同じ。吸収し、同化する生命の根源。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "downy_softness",
        "word": "Downy",
        "meaning": "うぶ毛のような、ふわふわした、柔らかな",
        "era": "16th Century Old Norse dunn",
        "etymology": {
            "components": ["dunn (down, feather)"],
            "original_statement": "From Old Norse dunn (down, plumage), related to German Daune."
        },
        "concept": "Like down (「重力（gravity）」を 忘れたかのような 「軽やかさ（lightness）」で 命を 「温める（warm up）」 慈しみの羽装)",
        "thinking": "この世界に生まれたばかりの、無垢で最も傷つきやすい時期を支える、神様からの「最初の贈り物」. 語源は「羽毛」. それは 強さを誇示するのではなく 弱さを そのまま 肯定し 守り抜きための 宇宙の 繊細な 配慮です. 柔らかさは、最強の防壁です.",
        "aftertaste": "無垢な防壁. 強くあろうとして 鎧を固めなくていい. あなたの「ダウニー（うぶ毛のような）」な 感受性を 大切にすることで あなたは 真実の 輝きを 守り抜くことができるのだから.",
        "example": "The newborn ducklings were covered in a layer of soft, yellow, downy feathers.",
        "deep_dive": { "roots": [{"term": "unknown", "meaning": "none"}], "points": ["ダウンジャケット（down jacket）の語源。命の火を絶やさない、極上の断熱材。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "supple_softness",
        "word": "Supple",
        "meaning": "しなやかな、柔軟な、(革などが)柔らかい、融通の利く",
        "era": "13th Century Latin sub- + plicare",
        "etymology": {
            "components": ["sub- (under)", "plicare (to fold)"],
            "original_statement": "From Old French souple (soft, flexible), from Latin supplex (submissive, kneeling), literally 'folding under', from sub- (under) + plicare (to fold)."
        },
        "concept": "Folding under (「圧力（pressure）」に 折れることなく 「しなやかに（pliant）」 変化し 「本質（core）」を 逃がす 知恵)",
        "thinking": "硬直した正義よりも、変化し続ける柔軟性を愛し、どんな嵐の中でも、風を受け流して生き残る「柳のような」強さ. 語源は「跪く（ひざまずく）、折り畳む」. それは 屈服ではなく 相手の力を 利用して 自らを 進化させるための 聖なる「融通（アダプテーション）」のアクションです.",
        "aftertaste": "しなやかな覚悟. 頑（かたく）なであることに 誇りを持たないで. あなたが「サップル（しなやかな）」であり続けることで どんな困難も あなたの魂を 磨くための 恩恵に 変わってゆくのだから.",
        "example": "Yoga helps to keep the body supple and the mind focused and clear.",
        "deep_dive": { "roots": [{"term": "plek-", "meaning": "to plait"}], "points": ["duplicate（複製する：二重に折る）や apply（応用する：折り重ねる）と同じ。重なり合う知性の多様性。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "mollify_softness",
        "word": "Mollify",
        "meaning": "和らげる、なだめる、(怒りなどを)静める",
        "era": "14th Century Latin mollis + ficare",
        "etymology": {
            "components": ["mollis (soft)", "facere (to make)"],
            "original_statement": "From Old French mollifier, from Late Latin mollificare (to make soft), from Latin mollis (soft) + facere (to make)."
        },
        "concept": "Making soft (「硬化した（hardened）」 心の壁を 「慈愛（love）」によって 「解きほぐし（melt）」 調和を 取り戻すこと)",
        "thinking": "論理で論破するのではなく、存在そのもので包み込み、相手のトゲ（防衛本能）を溶かしていく、究極の対人芸術. 語源は「柔らかくする」. それは 凍てついた 世界に 春の風を 送り込み 全ての 敵意を 聖なる 相互理解へと 変貌させる 慈悲深い 知性の 錬金術です.",
        "aftertaste": "雪解けの対話. 正しさで 誰かを 裁かないで. あなたの「モリファイ（和らげる）」する 優しい言葉が 誰かの心の氷を溶かし 笑顔を取り戻す 唯一の 鍵に なるのだから.",
        "example": "The manager tried to mollify the angry customers by offering them a full refund and a sincere apology.",
        "deep_dive": { "roots": [{"term": "mel-", "meaning": "soft"}], "points": ["mellow（熟した、芳醇な）や mildew（カビ：柔らかい付着物）と同じ。時間をかけて馴染ませる力。"] },
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
        print(f"Success: Added {added} words in Cycle 150.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
