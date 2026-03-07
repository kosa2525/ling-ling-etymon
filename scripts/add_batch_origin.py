import json
import re

word_batch = [
    # Cycle 117: Seed & Origin
    {
        "id": "lineage_origin",
        "word": "Lineage",
        "meaning": "血統、系譜、家柄、列",
        "era": "14th Century Latin linea",
        "etymology": {
            "components": ["linea (linen thread, string, line)"],
            "original_statement": "From Old French lignage, from ligne (line), from Latin linea (linen thread, string, line)."
        },
        "concept": "A continuous line (「糸（line）」のように 過去から未来へと 途切れることなく 「繋がっている（continuous）」こと)",
        "thinking": "あなたが今ここにいるのは 数え切れないほどの命のバトンが 絶えることなく繋がれてきた結果であるという 厳粛な事実. 語源は「糸」。一本の細い糸が 幾多の歴史を縫い合わせ あなたという存在を形作っています. それは 誇りであると同時に 守り抜くべき責任でもあります.",
        "aftertaste": "命の縦糸. あなたの背後には 数千年の時間が列をなして立っている. その重みを感じるとき あなたの一歩は より深く 確かなものになるだろう.",
        "example": "He can trace his lineage back to the aristocrats of the 17th century.",
        "deep_dive": { "roots": [{"term": "linon-", "meaning": "flax"}], "points": ["linen（リネン）や linear（直線的な）と同じ。植物の繊維が紡ぐ命の物語。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "genealogy_origin",
        "word": "Genealogy",
        "meaning": "系図、家系学、系統学",
        "era": "14th Century Greek genea + logos",
        "etymology": {
            "components": ["genea (family, race, generation)", "logos (study, account)"],
            "original_statement": "From Old French genealogie, from Late Latin genealogia, from Greek genealogia, from genea (generation, descent) + logos (account, study)."
        },
        "concept": "Account of descent (一族の「発生（generation）」を 「論理的（logos）」に解き明かし 言葉として記録すること)",
        "thinking": "混沌とした歴史の中から 自分のルーツへと続く道を 科学的な眼差しで再構築する知の営み. 語源の genea は「新しく生まれること」. それは 単なる名前の羅列ではなく どのような意志が受け継がれ どのような情熱が自分の中に流れているのかを知るための 魂の地図作りです.",
        "aftertaste": "時を遡る航海. 系図を辿ることは 自分の源泉へと川を遡るようなものだ. 始まりの場所を知ったとき あなたは今いる場所を もっと深く愛せるようになる.",
        "example": "She developed an interest in genealogy and spent months researching her family tree.",
        "deep_dive": { "roots": [{"term": "gene-", "meaning": "to give birth, beget"}], "points": ["genius（天才：生まれ持った精霊）や generate（発生させる）と同じ、創造のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "progenitor_origin",
        "word": "Progenitor",
        "meaning": "始祖、先祖、創始者",
        "era": "14th Century Latin pro- + gignere",
        "etymology": {
            "components": ["pro- (forth)", "gignere (to beget, produce)"],
            "original_statement": "From Old French progeniteur, from Latin progenitorem (ancestor), from progignere (to bring forth, beget), from pro- (forth) + gignere (to beget)."
        },
        "concept": "Begetting forth (次の世代を「前へと（forth）」 「産み出す（beget）」 始まりの存在)",
        "thinking": "すべてがまだ何もなかった場所に 最初の種を蒔いた 伝説的な存在. 語源は「前に産み出すもの」. あなたが今持っている才能や 抱いている夢も もしかしたら遠い祖先が 密かに産み落とした火種が 形を変えて現れたものかもしれません. 始まりを敬うことは 未来を信じることです.",
        "aftertaste": "始まりの祈り. あなたもまた 誰かの「プロジェニター（創始者）」になり得る存在だ. 今日蒔くその小さな種が 数百年後の誰かの森になることを信じよう.",
        "example": "The ancient philosopher is considered the progenitor of modern logical thinking.",
        "deep_dive": { "roots": [{"term": "gene-", "meaning": "to give birth"}], "points": ["pregnant（妊娠した）や kin（親族）と同じ。生命の連続性と拡張。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "ancestry_origin",
        "word": "Ancestry",
        "meaning": "先祖、家系、祖先伝来の性質",
        "era": "14th Century Latin ante- + cedere",
        "etymology": {
            "components": ["ante- (before)", "cedere (to go)"],
            "original_statement": "From Old French ancesserie, from ancestre (ancestor), from Latin antecessorem (predecessor), from antecedere (to go before)."
        },
        "concept": "Those who went before (自分より「前（before）」を 「歩んでいった（go）」 先駆者たち)",
        "thinking": "すでにこの世にはいなくても あなたの骨の中に、血の中に、言葉の中に 確かに息づいている先人たちの気配. 語源は「前に行く者」. 彼らが切り拓いた道があるからこそ あなたは今 平坦な道を歩むことができています. 感謝とは 自分の背後に続く 巨大な足跡を認めることです.",
        "aftertaste": "背中を守る盾. あなたは決して一人で戦っているのではない. あなたの背後には 幾千もの祖先が盾となって立ち あなたの勝利を静かに 確信しているのだから.",
        "example": "Tracing one's ancestry has become much easier with the help of modern DNA testing.",
        "deep_dive": { "roots": [{"term": "ant-", "meaning": "before"}, {"term": "ked-", "meaning": "to go, yield"}], "points": ["predecessor（前任者）や proceed（進む）と同じ。時間のベクトル。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "heritage_origin",
        "word": "Heritage",
        "meaning": "遺産、継承物、伝統、(天から授かった)運命",
        "era": "13th Century Latin heres",
        "etymology": {
            "components": ["heres (heir)"],
            "original_statement": "From Old French heritage, from heriter (inherit), from Late Latin hereditare, from Latin hereditatem (inheritance, state of being an heir), from heres (heir)."
        },
        "concept": "The state of an heir (「後継者（heir）」としての 「身分」あるいは「受け継ぐもの（inheritance）」)",
        "thinking": "金銭的なものだけでなく 精神性、伝統、あるいはこの美しい地球そのものなど 「過去から託されたすべての贈り物」. 語源は「相続人」. それはあなたが勝ち取ったものではなく 恩寵（おんちょう）として与えられたものです. 善きものを守り 次の世代へさらに美しくして手渡すこと。それが私たちの役割です.",
        "aftertaste": "託された星. あなたが手にしたその「遺産」は あなた一人のためのものではない. それを慈しみ 未来の子供たちに笑顔で手渡せるよう 今日を精一杯 生きよう.",
        "example": "The local festival is an important part of the region's cultural heritage.",
        "deep_dive": { "roots": [{"term": "gher-", "meaning": "to leave (possible related to heir being left behind)"}], "points": ["inherit（相続する）や heredity（遺伝）と同じ。残されるものの重み。"] },
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
        print(f"Success: Added {added} words in Cycle 117.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
