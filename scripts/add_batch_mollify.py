import json
import re

word_batch = [
    # Cycle 131: Silk & Softness
    {
        "id": "velvet_softness",
        "word": "Velvet",
        "meaning": "ベルベット、ビロード、柔らかい、滑らかな",
        "era": "14th Century Latin villus",
        "etymology": {
            "components": ["villus (shaggy hair, tuft of hair)"],
            "original_statement": "From Old French veluet, from Latin villus (shaggy hair, tuft of hair, fleece)."
        },
        "concept": "Tuft of hair (「柔らかな毛（hair）」が 密集し 「滑らかな（smooth）」 質感を生み出すこと)",
        "thinking": "光を優しく吸収し、深みのある影を作り出す 圧倒的に贅沢で 心地よい「触覚」の極致. 語源は「むく毛」. それは 鋭い角（かど）を一切持たず 全てを包み込み 安らぎを与える 慈悲深い質感を象徴しています. あなたの言葉が「ベルベット」のように 誰かの心を包み込むとき そこには深い癒やしが生まれます.",
        "aftertaste": "漆黒の安らぎ. 尖った心で 世界と向き合わないで. あなたの内側にある その「柔らかさ」を差し出すことで 世界はもっと 優しく、暖かな場所に 変わってゆくのだから.",
        "example": "The night sky was a deep, velvet blue, sprinkled with brilliant stars.",
        "deep_dive": { "roots": [{"term": "wel-", "meaning": "to tear, pull (possible root for fleece)"}], "points": ["villous（綿毛のある）と同じ。生命が持つ「柔らかい防壁」。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "satin_softness",
        "word": "Satin",
        "meaning": "サテン、繻子(しゅす)、滑らかな、光沢のある",
        "era": "14th Century Arabic Zaitun",
        "etymology": {
            "components": ["Zaitun (Quanzhou, China)"],
            "original_statement": "From Old French satin, possibly from Arabic Zaitun (Quanzhou, China), a major medieval port for silk."
        },
        "concept": "Lustrous port (「遥か東方の港（port）」から 運ばれてきた 「光沢（luster）」に 満ちた 布地)",
        "thinking": "光を反射し 水面のように 滑らかに滑り落ちていく 涼やかで 洗練された美しさ. 語源は「泉州（中国の港の名）」. それは 遥か彼方への憧れと 贅を尽くした技術が交わる場所に生まれる 「気品」の象徴です. 摩擦を恐れず 軽やかに世界を滑り抜けていく しなやかさ.",
        "aftertaste": "光の滑走。あなたの思考を「サテン」のように 滑らかに研ぎ澄まそう。停滞（ひっかかり）を捨てて 流れるように生きることで あなたの人生は より輝かしく、自由なものになる。",
        "example": "Her skin was as smooth as satin, glowing under the soft candlelight.",
        "deep_dive": { "roots": [{"term": "none", "meaning": "none"}], "points": ["silk（絹）の変奏曲。光と影の劇的なコントラスト。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "mollify_softness",
        "word": "Mollify",
        "meaning": "和らげる、なだめる、(苦痛などを)軽減する",
        "era": "14th Century Latin mollis",
        "etymology": {
            "components": ["mollis (soft)", "facere (to make)"],
            "original_statement": "From Old French mollifier, from Latin mollificare (to make soft), from mollis (soft) + facere (to make)."
        },
        "concept": "To make soft (硬く 「こわばった（hard）」 心を 「柔らかく（soft）」 ほぐし、溶かすこと)",
        "thinking": "激しい怒りや 頑なな拒絶を 慈愛に満ちた言葉や 行動によって じわじわと 粘土のように 柔らかく変えていくプロセス. 語源は「柔らかくする」. それは 暴力に対抗する力ではなく 全てを包み込み 溶かしてしまう 究極の「受容」の力です.",
        "aftertaste": "氷解の魔法. 正義を武器に 戦わないで. 相手の心を「モリファイ（軟化）」させるのは 鋭い正論ではなく あなたの温かな眼差しと 静かな沈黙なのだから.",
        "example": "The manager tried to mollify the angry customer by offering a full refund and a sincere apology.",
        "deep_dive": { "roots": [{"term": "meld-", "meaning": "to crush, soften"}], "points": ["mollusk（軟体動物）や melt（溶ける）と同じ。硬直からの解放。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "lenient_softness",
        "word": "Lenient",
        "meaning": "寛大な、情け深い、(処罰などが)軽い",
        "era": "17th Century Latin lenis",
        "etymology": {
            "components": ["lenis (soft, mild, gentle)"],
            "original_statement": "From Latin lenientem, from lenire (to soften, alleviate), from lenis (soft, mild, gentle)."
        },
        "concept": "Gentle state (「厳格（strict）」に 裁くのではなく 「柔らかく（mild）」 包み込む 情けの深さ)",
        "thinking": "過ちを 糾弾して 排除するのではなく 成長のための「余白」として 緩やかに 許し、受け入れること. 語源は「穏やかな」. それは 弱さではなく 強さゆえに可能な「慈悲」の形です. 厳しさよりも 柔らかさが 人を真に 変えることがあります.",
        "aftertaste": "許しの余白. 自分に対しても、他人に対しても 時には「レニエント（寛大）」であっていい. 完璧を求めすぎず その不完全さを 柔らかく抱きしめることから 本当の愛は始まるのだから.",
        "example": "The judge was surprisingly lenient with the first-time offender, offering him a chance for rehabilitation.",
        "deep_dive": { "roots": [{"term": "le-", "meaning": "to let go, slacken"}], "points": ["relent（和らぐ）や lenis（音声学の弱音）と同じ。緊張の緩和。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "supple_softness",
        "word": "Supple",
        "meaning": "しなやかな、柔軟な、(思考などが)適応性のある",
        "era": "14th Century Latin sub- + plicare",
        "etymology": {
            "components": ["sub- (under)", "plicare (to fold)"],
            "original_statement": "From Old French souple (soft, flexible), from Latin supplex (submissive), literally 'folding under', from sub- (under) + plicare (to fold)."
        },
        "concept": "Folding under (「下へと（under）」 「折り曲げる（fold）」 ことができる 自由で 逞しい 柔軟性)",
        "thinking": "折れるのではなく 柳のように 形を変えて 衝撃を受け流し 何度でも 元の美しい姿へと 立ち戻ることができる 強さを秘めた 柔らかさ. 語源は「下に折る」. それは 謙虚さであり 同時に どんな環境にも 適応できる 究極の生命力でもあります.",
        "aftertaste": "柳の強さ. 頑丈な大樹（理論やプライド）は 嵐の夜に 根こそぎ倒れることがある. しかし「サプル（しなやか）」な心を持ったあなたは どんな風にも 軽やかに身を委ね どこまでも高く 成長し続けるのだ。",
        "example": "The dancer's body was incredibly supple, moving with a fluidity that seemed almost impossible.",
        "deep_dive": { "roots": [{"term": "sub-", "meaning": "under"}, {"term": "plek-", "meaning": "to plait"}], "points": ["ply（〜重の）や complicit（共謀する）と同じ。重なりと折り曲げ。"] },
        "part_of_speech": "adjective"
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
        print(f"Success: Added {added} words in Cycle 131.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
