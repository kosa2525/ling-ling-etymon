import json
import re

word_batch = [
    # Cycle 141: Bloom & Garden (Refined)
    {
        "id": "efflorescence_bloom",
        "word": "Efflorescence",
        "meaning": "開花、開花期、(表面に生じる)粉、(科学・芸術の)全盛期",
        "era": "17th Century Latin ex- + flore",
        "etymology": {
            "components": ["ex- (out, forth)", "flore (flower)"],
            "original_statement": "From Latin efflorescere (to bloom, blossom, flourish), from ex- (out, forth) + florescere (to begin to bloom), from florere (to bloom), from flos (flower)."
        },
        "concept": "Blooming forth (「内（in）」に 秘めた 美しさが 「一気に外へと（forth）」 溢れ出し 「全盛（zenith）」を 迎えること)",
        "thinking": "長い潜伏期間を経て、ついに才能や美しさが目に見える形として結晶化し、周囲を圧倒するような輝きを放つこと. 語源は「外に向かって咲く」. それは 物理的な花だけでなく 文明や 芸術が 最も 純粋で 完璧な形を 現す 聖なる 瞬間を 指しています. 結実の喜び.",
        "aftertaste": "才能の噴出. あなたが今まで 密かに育んできた努力は 決して裏切らない. 時が来れば それは「エフロレッセンス（開花）」として 誰の目にも明らかな 輝きとなって 世界を彩るのだから.",
        "example": "The Renaissance was the ultimate efflorescence of human creativity and intellectual curiosity.",
        "deep_dive": { "roots": [{"term": "bhel-", "meaning": "to thrive, bloom, blossom"}], "points": ["flourish（繁栄する）や floral（花の）と同じ。生命の「全開」のアクション。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "florid_bloom",
        "word": "Florid",
        "meaning": "華やかな、(顔色が)赤らんだ、(文体などが)華美な",
        "era": "17th Century Latin flos",
        "etymology": {
            "components": ["flos (flower)"],
            "original_statement": "From Latin floridus (flowery, blooming, abounding in flowers), from flos (flower)."
        },
        "concept": "Flowery state (「花（flower）」が 咲き乱れる ように 「色彩（color）」と 「装飾（decoration）」に 満ちた 豊かさ)",
        "thinking": "簡素（シンプル）であることのストイックさを超え 生命が持つ 本能的な サービス精神と 祝祭性を 全身で 肯定すること. 語源は「花の」. それは 健康的な 血色であり 溢れんばかりの 語彙によって 綴られた 美しい物語であり 私たちの生（せい）を 肯定する 華麗な 旋律です.",
        "aftertaste": "祝祭の色彩. 地味であることに 縛られないで. あなたの内側にある その「華やかさ」を 存分に 表現（フリッド）してごらん. 世界はあなたの その彩りを 待っているのだから.",
        "example": "The author's florid prose was filled with complex metaphors and vivid descriptions.",
        "deep_dive": { "roots": [{"term": "bhel-", "meaning": "to bloom"}], "points": ["Florida（フロリダ：花に満ちた場所）の語源。生命の「熱度」の表現。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "anthesis_bloom",
        "word": "Anthesis",
        "meaning": "開花期、開花(の瞬間)",
        "era": "19th Century Greek anthos",
        "etymology": {
            "components": ["anthos (flower)"],
            "original_statement": "From Greek anthesis (a blooming), from anthein (to bloom), from anthos (flower)."
        },
        "concept": "State of flower (「花（flower）」としての 「完成（completion）」を 宇宙に 宣言する 究極の 瞬間)",
        "thinking": "蕾（つぼみ）が 開き切り 花弁が 外気と 触れ合う 最初の 震え. 語源は「開花」. 植物学的な用語でありながら それは 誰かの隠されていた 意志や 想いが 言葉（カタチ）となって 表出した 最初の 一点（ポイント）としての 聖性を 持ち合わせています. 告白の瞬間.",
        "aftertaste": "顕現の瞬間. あなたの言葉が「アンセシス（開花）」を迎えるとき. その震えるような 誠実さが 世界のどこかで 待っている 誰かの心を 深く 揺さぶることになるのだ.",
        "example": "The whole garden reached its anthesis simultaneously, creating an overwhelming sensory experience.",
        "deep_dive": { "roots": [{"term": "and-", "meaning": "to bloom (possible root)"}], "points": ["anthology（詩選集：花のコレクション）の anthos。言葉こそが、魂の花である。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "horticulture_garden",
        "word": "Horticulture",
        "meaning": "園芸(学)、草花栽培",
        "era": "17th Century Latin hortus + cultura",
        "etymology": {
            "components": ["hortus (garden)", "cultura (culture, tilling)"],
            "original_statement": "From Latin hortus (garden) + cultura (culture, tilling, care), from colere (to till)."
        },
        "concept": "Caring for the garden (「庭（garden）」という 小さな 宇宙を 「慈しみ（care）」 育む 知性と 愛のアート)",
        "thinking": "野生のまま 放置するのではなく 適切な 干渉（剪定や水やり）によって 自然の美しさを 最大限に 引き出そうとする 謙虚な 協働作業. 語源は「庭の耕作」. それは 自分の心（庭）を 耕し 雑草を抜いて 聖なる種を 育てるという 精神的な 修養の 隠喩でもあります.",
        "aftertaste": "慈しみの庭. 自分の心を 放っておかないで. 毎日 少しずつ「ホーティカルチャー（園芸）」のように 丁寧に 手入れをすることで あなたの魂は 誰をも 癒やす 美しい秘密の花園に 変わってゆくのだから.",
        "example": "Her deep knowledge of horticulture allowed her to maintain a lush, flourishing garden even in the dry climate.",
        "deep_dive": { "roots": [{"term": "gher-", "meaning": "to grasp, enclose (for hortus)"}, {"term": "kwel-", "meaning": "to revolve, dwell (for colere)"}], "points": ["yard（庭）や colony（植民地：耕された場所）と同じ。囲われ、守られた場所。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "foliage_garden",
        "word": "Foliage",
        "meaning": "葉、(一本の樹木の)全葉、葉飾",
        "era": "15th Century Latin folium",
        "etymology": {
            "components": ["folium (leaf)"],
            "original_statement": "From Old French feuillage, from feuille (leaf), from Latin folia (leaves), plural of folium (leaf)."
        },
        "concept": "Collection of leaves (無数の 「葉（leaf）」が 重なり合い 「緑の深み（greenery）」を 作り出す 生命の 充満)",
        "thinking": "一枚一枚の 個性を超え 集合体として 揺らぎ、光を反射し、酸素を 産み出し続ける 生命の「面」. 語源は「葉の集まり」. それは 陰（かげ）を作り 休息の場所を 提供する 寛容な 豊かさであり 私たちが 大地（ルーツ）と 繋がっていることを 証明する 瑞々しい（みずみずしい） 衣です.",
        "aftertaste": "緑の安らぎ. 派手な花でなくてもいい. あなたという「フォリッジ（葉）」が 誰かにとっての 涼やかな陰となり 心を癒やす 休息の場所になれることを 誇りに思っていいのだから.",
        "example": "The autumn foliage in the mountains turned into a spectacular tapestry of red, gold, and orange.",
        "deep_dive": { "roots": [{"term": "bhel-", "meaning": "to thrive, bloom, blossom"}], "points": ["folio（二つ折りの紙：一枚の葉）や portfolio（折り畳みの紙入れ）と同じ。広がり。"] },
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
        print(f"Success: Added {added} words in Cycle 141.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
