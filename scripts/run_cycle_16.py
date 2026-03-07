import json
import re

words_data = [
    ("weave", "Weave", "織る、編む", "Old English", "wefan (to weave)", "Form fabric or a fabric item by interlacing long threads passing in one direction with others at a right angle to them", "バラバラの細い糸である経糸（運命）と緯糸（自由意志）を、摩擦と交差によって「一つの面」へとまとめ上げる創造のパズル。", "人生は、出逢いという縦糸と、選択という横糸を「ウィーヴ（織って）」一枚の奇跡のような布を作ることです。"),
    ("spin", "Spin", "紡ぐ、回転する", "Old English", "spinnan (to draw out and twist fibers into thread)", "Draw out and twist the fibers of wool, cotton, or other material to convert them into yarn", "混沌とした羊毛の塊から、指先の回転と祈りのような繊細な引っ張りによって、一本の連続した「意味の糸」を引き出す原初の魔法。", "おとぎ話の「スピン（糸紡ぎ）」の音が、過去から未来への途切れない物語を語り継いできたのです。"),
    ("knit", "Knit", "編む、密着させる", "Old English", "cnyttan (to tie together)", "Make a garment, blanket, etc., by interlocking loops of wool or other yarn with knitting needles", "ただ一本の毛糸を、針の奇跡的な動きによって「結びと輪の連続」へと変え、伸縮性を持った温かい布地を立体的につくり出すこと。", "私たちの折れた骨は、時間という見えない名医が再び強く「ニット（癒着し結合）」してくれます。"),
    ("stitch", "Stitch", "縫う、ひと針", "Old English", "stician (to stick, pierce)", "Make, mend, or join something with stitches", "布同士の隙間に鋭い針を「深く突き刺し」、糸を強引に通すことで二つの異なる端を縫合し、破れを愛で塞ぐ痛みを伴う修復。", "大笑いしすぎてお腹が「スティッチ（チクチク痛む）」のは、一番幸せな病気の症状です。"),
    ("sew", "Sew", "縫う", "Old English", "siwian (to sew, mend)", "Join, fasten, or repair something by making stitches with a needle and thread", "ほころんだものを「一つの完全なる布地」へと修復し、着る者を風や冷たい視線から守る包容力を持った手作業。", "「ソウ（縫い合わせて修繕する）」されたぬいぐるみは、買ったばかりの新品よりも遥かに温かい魂を持っています。"),
    ("tangle", "Tangle", "もつれ、絡ませる", "14th Century", "tagla (to intertwine)", "Twist together into a confused mass", "秩序立っていた糸の群れが、不用意な動きや悪意によって互いを完全に巻き込み、容易には元に戻せない「致命的な混乱」へと堕ちる状態。", "恋人たちの「タングル（複雑にもつれた）」な感情は、無理に引っ張らずに、手元から一つ一つ解くしかありません。"),
    ("unravel", "Unravel", "ほどく、解明する", "16th Century", "un- (not) + ravel (tangle)", "Undo twisted, knitted, or woven threads", "固くもつれた糸の塊や複雑な謎の糸口を見つけ出し、全ての結び目を「論理と根気を用いて」美しく一本の直線へと戻していく知的作業。", "探偵のように、入り組んだトリックの糸束を少しずつ「アンラヴェル（解きほぐす）」していく知的な快感。"),
    ("embroider", "Embroider", "刺繍する、話を誇張する", "14th Century", "brouder (to embroider)", "Decorate cloth by sewing patterns on it with thread", "無地の退屈な布をキャンバスに見立て、色とりどりの糸で「本来そこになかった」新しい花や生命を幻術のように縫い付ける飾り立て。", "事実を少しだけ「エンブロイダー（刺繍して誇張する）」して語る彼の昔話は、嘘だとしても魅力的で憎めません。"),
    ("patch", "Patch", "継ぎ当て、つぎはぎ", "14th Century", "pacche (piece of cloth)", "A piece of cloth or other material used to mend or strengthen a torn or weak point", "完璧な布が破れたとき、同じ布ではなく「あえて異なる布（色）」を当てて穴を塞ぎ、傷跡を新しいデザインとして肯定する生き方。", "お気に入りのジーンズに作られたいくつもの「パッチ（継ぎ接ぎ）」は、ともに歩んだ誇り高き勲章です。"),
    ("thread", "Thread", "糸、筋道", "Old English", "thræd (thread)", "A long, thin strand of cotton, nylon, or other fibers used in sewing or weaving", "迷宮を進むテセウスのように、混乱の世界で自分を見失わないための「細いが切れない命綱」であり、物語を一本に繋ぐ論理の経路。", "どれほど複雑な議論の中でも、この一つの「スレッド（文脈の糸）」さえ見失わなければ必ず真理に辿り着けます。")
]

words = []
for item in words_data:
    root1 = item[4].split(" ")[0]
    meaning1 = " ".join(item[4].split(" ")[1:]).strip("()")
    w = {
        "id": f"{item[0]}_fabric",
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
        "example": f"I watched her gracefully {item[0]} the fabric.",
        "deep_dive": {
            "roots": [{"term": root1, "meaning": meaning1}],
            "points": ["布を織り、修繕する行為は、人間関係や歴史のメタファーです。"]
        },
        "part_of_speech": "noun" if item[0] in ["tangle", "patch", "thread"] else "verb"
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
    print(f"Success: Added {added} words. Theme: Weaving & Fabric (Cycle 16).")
else:
    print("Error parsing data.js")
