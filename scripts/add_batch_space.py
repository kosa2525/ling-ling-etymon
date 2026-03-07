import json
import re

word_batch = [
    {
        "id": "cosmos_space",
        "word": "Cosmos",
        "meaning": "宇宙、秩序ある体系",
        "era": "12th Century Greek kosmos",
        "etymology": {
            "components": ["kosmos (order, good arrangement, ornament)"],
            "original_statement": "From Greek kosmos (order, good arrangement, ornament, world, universe), the opposite of chaos."
        },
        "concept": "Order in the vastness (広大な中に宿る「秩序」と「装飾」)",
        "thinking": "ギリシャ人は宇宙のことを、ただの空虚（void）ではなく、極めて精緻に整えられた「宝石のような装飾品（ornament）」であると考えました。「カオス（混沌）」の対義語としてのコスモス。それは、星々の運行から道徳的な調和まで、すべてがしかるべき位置にあるという美しき確信の別名です。",
        "aftertaste": "暗闇の中を貫く、絶対的な美の法則。私たちは秩序の中に抱かれている。",
        "example": "The ancient philosophers sought to understand the laws that govern the cosmos.",
        "deep_dive": {
            "roots": [{"term": "kens-", "meaning": "to proclaim, announce (possible)"}],
            "points": ["cosmetic（化粧品：整えて美しくするもの）も同じ語源。宇宙は美しく整えられたものです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "galaxy_space",
        "word": "Galaxy",
        "meaning": "銀河、天の川、華やかな集まり",
        "era": "14th Century Old French/Greek galaxias",
        "etymology": {
            "components": ["gala (milk)"],
            "original_statement": "From Old French galaxie, from Greek galaxias (kyklos) (milky circle), from gala (milk)."
        },
        "concept": "A circle of milk (空に零（こぼ）れた「母なる乳の輪」)",
        "thinking": "ギリシャ神話で、女神ヘラの母乳が空にほとばしってできた「乳の道（Milky Way）」。それは生命の源泉が宇宙へと拡張されたメタファーです。何千億もの光が寄り添い、一つの渦を巻く姿は、個を超えた巨大な生命の脈動そのもののように見えます。",
        "aftertaste": "零れた乳が、永遠の光の道となった。私たちは、その光の粒子の一つ。",
        "example": "The Andromeda Galaxy is the closest major galaxy to our own Milky Way.",
        "deep_dive": {
            "roots": [{"term": "galakt-", "meaning": "milk"}],
            "points": ["lactose（乳糖）や lacteal（乳の）の la- もこの gala- がラテン語化したもの。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "nebula_space",
        "word": "Nebula",
        "meaning": "星雲、(比喩的に)ぼんやりしたもの",
        "era": "15th Century Latin nebula",
        "etymology": {
            "components": ["nebula (mist, vapor, cloud)"],
            "original_statement": "From Latin nebula (mist, vapor, cloud), from PIE root *nebh- (cloud)."
        },
        "concept": "A celestial mist (星々の間に漂う、光り輝く「霧」)",
        "thinking": "形を持たず、ぼんやりと宇宙を漂う「霧（mist）」。それは新しい星が生まれる「ゆりかご（nursery）」であり、あるいは星が死にゆく際の名残（残骸）でもあります。曖昧でありながら、すべての生命の材料が凝縮されている、可能性の雲。",
        "aftertaste": "形のない霧から、いつか一つの太陽が生まれる。混沌は、創造の母。",
        "example": "The Orion Nebula is clearly visible even with a small telescope on a dark night.",
        "deep_dive": {
            "roots": [{"term": "nebh-", "meaning": "cloud, vapor"}],
            "points": ["nimbus（雨雲/後光）や nimbus と同じ、湿気を帯びた空気のルーツ。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "asteroid_space",
        "word": "Asteroid",
        "meaning": "小惑星、星のようなもの",
        "era": "19th Century Greek aster + -oeides",
        "etymology": {
            "components": ["aster (star)", "eidos (form, shape)"],
            "original_statement": "Coined in 1802 by astronomer William Herschel, from Greek asteroeides (star-like), from aster (star) + -oeides (form, shape)."
        },
        "concept": "A star-like form (本当の星ではないけれど、星のような「形」をしたもの)",
        "thinking": "望遠鏡で見ると、惑星（円盤状に見える）とは違い、遠くの「恒星（aster）」のように点として輝いて見えたことに由来します。宇宙の広大な空間をひっそりと旅する、名もなき石。それは完成されなかった世界の欠片、あるいは、いつか衝突して変化をもたらす「運命の矢」かもしれません。",
        "aftertaste": "主役ではないけれど。ただ一筋の軌道を、誰にも知られず守り抜く。",
        "example": "The belt of asteroids between Mars and Jupiter contains billions of rocky objects.",
        "deep_dive": {
            "roots": [{"term": "ster-", "meaning": "star"}],
            "points": ["astronomy（天文学）や asterisk（※：小さな星）と同じ『星（aster）』のファミリー。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "zenith_space",
        "word": "Zenith",
        "meaning": "天頂、絶頂、極致",
        "era": "14th Century Old French/Arabic samt",
        "etymology": {
            "components": ["samt (way, path, head)"],
            "original_statement": "From Middle French zenith, from Old Spanish zenit, from Arabic samt (ar-ras) (the path over the head)."
        },
        "concept": "The path over the head (頭の真上を通り抜ける「天の頂」)",
        "thinking": "もともとはアラビア語で「（頭の上の）道（path）」を意味しました。自分を世界の中心としたとき、垂直に見上げた先にある、宇宙で最も高い一点。それは、実力や情熱が極限に達し、これ以上にない「最高の輝き」を放つ瞬間の代名詞となりました。",
        "aftertaste": "真っ直ぐに見上げた先。そこには、あなただけの天頂が待っている。",
        "example": "The sun reached its zenith at noon, casting almost no shadows.",
        "deep_dive": {
            "roots": [],
            "points": ["nadir（天底：足元。アラビア語の nazir が由来）と対をなす言葉。"]
        },
        "part_of_speech": "noun"
    }
]

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
    if match:
        prefix = match.group(1)
        json_array_str = match.group(2)
        suffix = match.group(3)
        
        words = json.loads(json_array_str)
        existing_ids = {w.get("id") for w in words}
        
        added_count = 0
        for item in word_batch:
            if item["id"] not in existing_ids:
                words.append(item)
                added_count += 1
                
        new_json_str = json.dumps(words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Success: Added {added_count} words.")
    else:
        print("Error: Could not find WORDS array in data.js.")
except Exception as e:
    print(f"Error: {e}")
