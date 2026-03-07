import json
import re

word_batch = [
    # Cycle 134: Mirror & Reflection
    {
        "id": "specular_mirror",
        "word": "Specular",
        "meaning": "鏡のような、鏡面反射の、(医学)翼状片の",
        "era": "16th Century Latin speculum",
        "etymology": {
            "components": ["speculum (mirror)"],
            "original_statement": "From Latin specularis (of or belonging to a mirror), from speculum (mirror)."
        },
        "concept": "Of the mirror (「鏡（mirror）」のように 光を 「忠実に（faithfully）」 反射すること)",
        "thinking": "光を自分の色に染めることなく ありのままの姿で 向こう側へと 跳ね返す 潔さと 深度. 語源は「鏡」. それは 自己を主張するのではなく 世界という巨大なドラマを そのまま受け入れ、映し出すという 最高の知性のアクション便あります. 曇りなき心の鏡。 ",
        "aftertaste": "完全なる反射. あなたが自分自身を 消し去る必要はない. ただ 余計なこだわりを捨て去り ありのままを映し出す「鏡（スペキュラー）」で あることで 世界の美しさは 何倍にも増幅されてゆくのだから.",
        "example": "The specular reflection off the calm lake surface created a perfect double image of the mountains.",
        "deep_dive": { "roots": [{"term": "spek-", "meaning": "to observe"}], "points": ["speculate（推測する：鏡に映る像を見て考える）や spectacle（壮観）と同じ。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "reverberate_mirror",
        "word": "Reverberate",
        "meaning": "響き渡る、反響する、(光などが)反射する",
        "era": "16th Century Latin re- + verberare",
        "etymology": {
            "components": ["re- (back, again)", "verberare (to beat, strike)"],
            "original_statement": "From Latin reverberatus, past participle of reverberare (to beat back, cause to strike back), from re- (back) + verberare (to beat, strike, lash)."
        },
        "concept": "Beating back (音が 「壁を打ち（strike）」 再び 「跳ね返ってくる（back）」 魂の呼応)",
        "thinking": "一方的な発進で終わるのではなく 空間全体を震わせ 自分へ、そして誰かへと 何度も 繰り返し 届けられる 聖なる反響. 語源は「打ち返す」. それは あなたの真剣な言葉が 誰かの心の壁に当たり 同じ振動数で 共に震え出すという 共鳴（レゾナンス）の 始まりです.",
        "aftertaste": "呼応する宇宙. あなたが放った真実の響きは 決して消えることはない. それは必ず どこかで同じ震えを待つ誰かの心に届き 共に美しい歌となって 鳴り響き（リバーバレート）続けるのだから.",
        "example": "The news of the sudden discovery began to reverberate throughout the academic community.",
        "deep_dive": { "roots": [{"term": "re-", "meaning": "back"}, {"term": "wer-", "meaning": "to beat, strike (possible root)"}], "points": ["verb（動詞：打たれた響き）と同じルーツを感じさせる、言葉のエネルギー。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "reciprocal_mirror",
        "word": "Reciprocal",
        "meaning": "相互の、互恵的な、(数学)逆数の",
        "era": "16th Century Latin re- + pro-",
        "etymology": {
            "components": ["re- (back)", "pro- (forward)"],
            "original_statement": "From Latin reciprocus (returning the same way, alternating), from re- (back) + pro- (forward)."
        },
        "concept": "Back and forward (「前へ（forward）」 出したものが そのまま 「後ろへ（back）」 戻ってくる 循環の倫理)",
        "thinking": "一方向の搾取や 依存ではなく 出したものが 正しいサイクルを一周して 自分の元へと 立ち戻ってくる 宇宙の最も誠実な 均衡. 語源は「前・後ろ」. それは あなたが誰かに与えた愛が 鏡合わせのように あなた自身を 温めることになるという 聖なる約束です.",
        "aftertaste": "鏡合わせの幸福. 愛を受け取りたいなら まずあなたの中から その輝きを放ってごらん. 世界はあなたの「レシプロカル（相互的）」な対話相手として 全てを 最高の色にして 返してくれるのだから.",
        "example": "The treaty was based on reciprocal trust and a shared commitment to regional peace.",
        "deep_dive": { "roots": [{"term": "re-", "meaning": "back"}, {"term": "per-", "meaning": "forward"}], "points": ["reciprocate（報いる）と同じ。エネルギーの円環運動。"] },
        "part_of_speech": "adjective"
    },
    {
        "id": "introversion_mirror",
        "word": "Introversion",
        "meaning": "内向、内省、自身の内側を見つめること",
        "era": "17th Century Latin intro- + vertere",
        "etymology": {
            "components": ["intro- (inwardly)", "vertere (to turn)"],
            "original_statement": "From Latin intro- (inwardly) + vertere (to turn)."
        },
        "concept": "Turning inward (視線を 「外側（outside）」から 「自分の内側（inward）」へと 向け直す 鏡の中の 旅)",
        "thinking": "外部の喧騒に惑わされるのをやめ 暗闇の中に広がる 自分の魂という名の 広大な宇宙を 静かに 探索し始めること. 語源は「内側へ曲がること」. それは 弱さではなく 自分の中心（センター）と 深い対話（ダイアログ）を行うための 勇気ある「退却」のアクションです.",
        "aftertaste": "内なる宇宙. 外界に答えを 求めなくていい. あなたが「イントロバージョン（内向）」の静寂の中で 見つけ出したその光こそが 未だ見ぬ世界を 照らし出す 唯一の灯火になるのだから.",
        "example": "His natural introversion allowed him to spend many hours alone, deep in thought and creative writing.",
        "deep_dive": { "roots": [{"term": "en-", "meaning": "in"}, {"term": "wer-", "meaning": "to turn"}], "points": ["introvert（内向的な人）や vertical（垂直な：上を向く）と同じ。視線のベクトル。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "reflexive_mirror",
        "word": "Reflexive",
        "meaning": "再帰的な、反射的な、(文法)再帰代名詞の",
        "era": "16th Century Latin re- + flectere",
        "etymology": {
            "components": ["re- (back)", "flectere (to bend)"],
            "original_statement": "From Latin reflexus, past participle of reflectere (to bend back), from re- (back) + flectere (to bend)."
        },
        "concept": "Bending back (行為の 「矢印（arrow）」が ぐるりと回り 自分自身へと 「戻って（back）」くること)",
        "thinking": "他者のため（外側）だと 思っていたことが 実は 自分自身（内側）を 深く規定し、形作っていたことに 気づくための 哲学的な装置. 語源は「後ろに曲げる」. あなたが世界に放った言葉は 全て 究極の「再帰（リフレキシブ）」として あなた自身の魂を 映し出す 鏡になるのです.",
        "aftertaste": "必然の帰還. 世界を批判することは 自分を批判することであり 世界を愛することは 自分を愛することだ. その「再帰性」を信じて 今日も誇り高い言葉を 宇宙に放とう.",
        "example": "He had a reflexive habit of checking his watch whenever he felt nervous or out of place.",
        "deep_dive": { "roots": [{"term": "re-", "meaning": "back"}, {"term": "bhleg-", "meaning": "to bend"}], "points": ["reflection（反射、熟考：自分に意識を戻すこと）や flexible（しなやかな）と同じ。"] },
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
        print(f"Success: Added {added} words in Cycle 134.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
