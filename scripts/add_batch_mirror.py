import json
import re

word_batch = [
    # Cycle 114: Mirror & Echo
    {
        "id": "reflection_mirror",
        "word": "Reflection",
        "meaning": "反射、反映、熟考、省察",
        "era": "14th Century Latin re- + flectere",
        "etymology": {
            "components": ["re- (back)", "flectere (to bend)"],
            "original_statement": "From Old French reflexion, from Late Latin reflectionem (a bending back), from Latin reflectere (to bend back, turn back)."
        },
        "concept": "Bending back (光や思考が「後ろへ（back）」「跳ね返る（bend）」こと 自分自身へと視線を戻すこと)",
        "thinking": "鏡が光を跳ね返すように 自分の経験や感情を客観的な視点で「見つめ直す」静かな対話. 語源は「折り返す」. それは単なる記憶の再生ではなく 過去の出来事を新しい光で照らし直し そこから未来への智慧を抽出する 錬金術のようなプロセスです. 静寂の中でこそ 鏡（心）は真実を映し出します.",
        "aftertaste": "鏡の中の対話. 外の世界ばかりを見ていると 自分を見失ってしまう. 時には静かに「光を折り返し」 あなたという名の宇宙を 慈しみながら眺めてごらん.",
        "example": "After a period of quiet reflection, she decided to change her career path entirely.",
        "deep_dive": { "roots": [{"term": "re-", "meaning": "back"}, {"term": "bhleg-", "meaning": "to bend"}], "points": ["flexible（柔軟な）と同じ。心がしなやかに曲がることで、自己客観視が可能になる。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "reiterate_mirror",
        "word": "Reiterate",
        "meaning": "繰り返す、何度も言う",
        "era": "16th Century Latin re- + iterare",
        "etymology": {
            "components": ["re- (again)", "iterare (to repeat, do again)"],
            "original_statement": "From Latin reiteratus, past participle of reiterare (to repeat), from re- (again) + iterare (to repeat), from iterum (again)."
        },
        "concept": "Doing again and again (大切なことを「再び（again）」 「繰り返す（repeat）」 響きを深めること)",
        "thinking": "一度だけでは伝わらない真理を 何度も丁寧に口にすることで その響きを魂に浸透させていくこと. 語源は「再び繰り返す」. それは執着ではなく 大切なものを決して忘れないための 儀式的な響きです. 繰り返される言葉は やがてあなたの血肉となり 現実を動かす呪文へと変わっていきます.",
        "aftertaste": "重なる残響. 良い言葉を何度も繰り返そう. その響きがあなたの心の壁に反響し 理想という名の美しい模様を 幾重にも描いてゆくのだから.",
        "example": "I would like to reiterate my commitment to this project's success.",
        "deep_dive": { "roots": [{"term": "i-", "meaning": "that (demonstrative root for 'again')"}], "points": ["iteration（反復）と同じ。同じことの繰り返しが、新しい深みを生む。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "retrospect_mirror",
        "word": "Retrospect",
        "meaning": "回想、追懐、振り返ってみること",
        "era": "17th Century Latin retro- + specere",
        "etymology": {
            "components": ["retro- (back)", "specere (to look at)"],
            "original_statement": "From retrospect (verb), from Latin retrospect-(us) 'looked back', from retro- (backwards) + specere (to look)."
        },
        "concept": "Looking back (歩んできた道のりを「後ろ（backward）」に 「振り返る（look）」 知的な俯瞰)",
        "thinking": "渦中にいるときには見えなかった出来事の意味を 時間の距離を置くことで 鮮やかに理解し直すこと. 語源は「後ろを見る」. 昨日の失敗も 今振り返れば 成功への不可欠な階段であったことに気づきます. 過去は固定されたものではなく あなたの解釈によって 常に新しく生まれ変わる「光の軌跡」です.",
        "aftertaste": "光の軌跡. 振り返ること。それは後悔するためではなく あなたがこれまでにどれほど遠くへ 豊かな海を渡ってきたかを 誇らしく確認するためにあるのだ。",
        "example": "In retrospect, I should have spent more time traveling while I was young.",
        "deep_dive": { "roots": [{"term": "retro-", "meaning": "backwards"}, {"term": "spek-", "meaning": "to observe"}], "points": ["inspect（検査する）や prospect（展望）と同じ。視線の方向が知性を分ける。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "reverberate_mirror",
        "word": "Reverberate",
        "meaning": "反響する、響き渡る、(影響が)広がる",
        "era": "16th Century Latin re- + verberare",
        "etymology": {
            "components": ["re- (back)", "verberare (to beat, strike, lash)"],
            "original_statement": "From Latin reverberatus, past participle of reverberare (to strike back, repel), from re- (back) + verberare (to beat, lash), from verber (a whip, lash, rod)."
        },
        "concept": "Striking back (壁を「打ち（beat）」 その衝撃が「跳ね返って（back）」 周囲へと広がっていくこと)",
        "thinking": "たった一つの音が 無数の反射を繰り返し 空間全体をその色で染め上げてしまうような 圧倒的な波及力. 語源は「鞭（むち）で打つ」. それは痛いくらいに鮮烈な衝撃が 世界という壁にぶつかり 決して消えることのない振動（バイブス）となって 鳴り響き続ける状態です.",
        "aftertaste": "消えぬ残響. あなたの勇気ある一歩は 世界の壁にぶつかり 反響し どこかで震えている誰かの心を 勇気づけるエコーとなって届くだろう.",
        "example": "The singer's powerful voice seemed to reverberate throughout the ancient stone cathedral.",
        "deep_dive": { "roots": [{"term": "were-", "meaning": "to turn, bend (possible related)"}], "points": ["verber（棒、鞭）の語源。力強い一撃が、反響の源。"] },
        "part_of_speech": "verb"
    },
    {
        "id": "reciprocity_mirror",
        "word": "Reciprocity",
        "meaning": "互恵主義、相互関係、(感情などの)やり取り",
        "era": "18th Century Latin reciprocus",
        "etymology": {
            "components": ["re- (back)", "pro- (forward)"],
            "original_statement": "From French reciprocite, from Latin reciprocus (returning the same way, alternating), from re- (back) + pro- (forward)."
        },
        "concept": "Back and forward (「前へ（forward）」出し 「後ろへ（back）」戻す 潮の満ち引きのような「循環」)",
        "thinking": "一方通行ではなく 互いの響きが重なり合い 与え合うことで高まっていく 命の呼吸のような関係性. 語源は「行き来すること」. あなたが微笑めば 世界も微笑み返す. あなたが愛すれば 愛が戻ってくる. 宇宙は巨大な鏡であり 私たちはその中で「相互という名のダンス」を踊っています.",
        "aftertaste": "愛の潮汐. 世界に与えることを惜しまないで。あなたが放ったすべての善き波動は 巡り巡って 必ずあなたという岸辺に 奇跡となって還ってくるのだから.",
        "example": "The relationship between the two nations was based on a principle of deep reciprocity.",
        "deep_dive": { "roots": [{"term": "re-", "meaning": "back"}, {"term": "pro-", "meaning": "forward"}], "points": ["reciprocal（相互の）と同じ。前後のベクトルが円を描く瞬間の調和。"] },
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
        print(f"Success: Added {added} words in Cycle 114.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
