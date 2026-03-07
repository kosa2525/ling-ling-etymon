import json
import re

word_batch = [
    # Cycle 135: Bridge & Connection
    {
        "id": "liaison_bridge",
        "word": "Liaison",
        "meaning": "連絡、提携、(料理の)つなぎ、情事",
        "era": "16th Century Latin ligare",
        "etymology": {
            "components": ["ligare (to bind)"],
            "original_statement": "From French liaison (a binding, connection), from Late Latin ligationem (a binding), from Latin ligare (to bind, tie, band)."
        },
        "concept": "A binding connection (異なる組織や 思想を 「一つに結び付ける（bind）」 聖なる 「絆（bond）」)",
        "thinking": "バラバラに存在する要素の間に 意味という名の 糸を通し 淀みのない 循環（コミュニケーション）を 作り出すこと. 語源は「結びつけること」. それは 単なる情報伝達ではなく お互いの存在を 深く認め合い、溶け合わせるための 誠実なアクションです.",
        "aftertaste": "架け橋の祈り. あなたが誰かと誰かの 間に立つとき. その「リエゾン（連絡）」という名の 献身的な 繋ぎ合わせが 世界に新しい 調和（ハーモニー）を もたらすのだから.",
        "example": "He served as a crucial liaison between the local community and the city government during the crisis.",
        "deep_dive": { "roots": [{"term": "leig-", "meaning": "to bind"}], "points": ["religion（宗教：神と結びつくこと）や ligament（靱帯）と同じ。不可分なる結合。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "nexus_bridge",
        "word": "Nexus",
        "meaning": "連結、核心、結合、関係",
        "era": "17th Century Latin nectere",
        "etymology": {
            "components": ["nectere (to bind, tie, fasten)"],
            "original_statement": "From Latin nexus (a binding, a joining), past participle of nectere (to bind, tie, fasten, join together)."
        },
        "concept": "The point of joining (万物が 「交差し（cross）」 最も深く 「結び合わされている（fastened）」 運命の交差点)",
        "thinking": "末端の現象ではなく、全てが一点に収束し、そこからまた新たな可能性が放射状に広がっていく「中心的な核」. 語源は「結び」. インターネットの網目や、人と人との絆が最も色濃く現れる場所です. あなたがその「ネクサス（核心）」に触れたとき、世界の複雑怪奇な糸は一本の理（ことわり）として解けていきます.",
        "aftertaste": "核心の静寂。多くの情報に 惑わされないで。物事の「結び目（ネクサス）」が どこにあるのかを 静かに見極めることで あなたの進むべき道は 驚くほど鮮やかに 浮かび上がってくるのだから。",
        "example": "The city has become the central nexus for international trade and technological innovation in the region.",
        "deep_dive": { "roots": [{"term": "ned-", "meaning": "to bind, tie"}], "points": ["net（網）や node（節）と同じ。構造を支える「結び目」の哲学。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "interface_bridge",
        "word": "Interface",
        "meaning": "接点、界面、やり取りの手段、対話",
        "era": "19th Century Latin inter- + facies",
        "etymology": {
            "components": ["inter- (between)", "facies (form, appearance, face)"],
            "original_statement": "Coined in the 19th century from inter- (between) + face (noun), from Latin facies (form, appearance, face)."
        },
        "concept": "Between faces (「顔（face）」と 「顔（face）」が 向かい合い 「境界線（boundary）」で 響き合うこと)",
        "thinking": "全く違う法則で動く二つの世界が ぶつかり合い、お互いを理解可能な 言語へと 翻訳し合う ドラマチックな 境界領域. 語源は「顔の間」. それは 道具だけでなく 人と人の対話においても 相手の懐に 敬意を持って 踏み込むための 聖なる「接点」です.",
        "aftertaste": "境界の翻訳者. あなたの言葉が 誰かの心という名の 「インターフェース」を 震わせるとき. 違う宇宙（こころ）同士が 一つの意味（共感）を 共有し始めるという 奇跡が起きるのだ.",
        "example": "The user-friendly interface made the complex software accessible to even the most non-technical users.",
        "deep_dive": { "roots": [{"term": "dhē-", "meaning": "to set, put (possible for facies)"}], "points": ["surface（表面：上の顔）と同じ。存在が外側へと現れる「界面」の美. "] },
        "part_of_speech": "noun"
    },
    {
        "id": "conduit_bridge",
        "word": "Conduit",
        "meaning": "導管、水路、(情報の)伝達路、仲介者",
        "era": "14th Century Latin con- + ducere",
        "etymology": {
            "components": ["con- (together)", "ducere (to lead)"],
            "original_statement": "From Old French conduit, from Medieval Latin conductus (a defense, escort, bridge), from Latin conducere (to lead together)."
        },
        "concept": "Leading together (「一緒（together）」に 「導き（lead）」 溢れ出す エネルギーを 「正しい方向（path）」へと 運ぶもの)",
        "thinking": "自分の中に留めておくのではなく 価値あるものを 次の場所へと 淀みなく 流し続けるための 献身的な「通路」としての 存在. 語源は「共に導く」. 水が大地を潤し、情報が知性を育むように あなたは 大いなる意思の「導管（コンジット）」として 生きることができるのです.",
        "aftertaste": "流転の聖域. 全てを独占しようとしないで. あなたが「透明な通路」であるとき 宇宙の豊かなエネルギーは あなたを通り抜け 世界の隅々まで 自在に 届けられるようになるのだから.",
        "example": "The local library acts as a vital conduit of information and education for the underprivileged children.",
        "deep_dive": { "roots": [{"term": "deuk-", "meaning": "to lead"}], "points": ["duct（ダクト）や educate（教育する：引き出す）と同じ。流れを導く力. "] },
        "part_of_speech": "noun"
    },
    {
        "id": "alloy_bridge",
        "word": "Alloy",
        "meaning": "合金、混じり物、(価値を)下げるもの、統合",
        "era": "14th Century Latin ad- + ligare",
        "etymology": {
            "components": ["ad- (to)", "ligare (to bind)"],
            "original_statement": "From Old French aloier (to combine, mix), from Latin alligare (to bind to, tie to), from ad- (to) + ligare (to bind, tie)."
        },
        "concept": "Binding to (異なる性質の 「金属（metal）」を 「強く結び合わせ（bind together）」 唯一無二の 「強靭さ（strength）」を 作ること)",
        "thinking": "純粋であることの脆（もろ）さを捨て 異質なものを受け入れることで 以前よりも 遥かに強く、美しく 生まれ変わるという 創造のダイナミズム. 語源は「結びつける」. それは 混じり物（不純）を 祝福に変え 新しい次元のアイデンティティを 確立するプロセスです.",
        "aftertaste": "交わりの錬金術. 自分の個性が 消えることを 恐れないで. 誰かの色と「アロイ（合金）」することで あなたの魂は 誰にも決して 折ることができない 究極の強靭さを 手にすることができるのだから.",
        "example": "Brass is an alloy of copper and zinc, combining the best properties of both metals.",
        "deep_dive": { "roots": [{"term": "leig-", "meaning": "to bind"}], "points": ["ally（同盟者）や rely（信頼する：強く結びつく）と同じ。連帯が生む強さ. "] },
        "part_of_speech": "noun"
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
        print(f"Success: Added {added} words in Cycle 135.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
