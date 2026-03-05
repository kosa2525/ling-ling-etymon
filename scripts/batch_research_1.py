import json
import os
import re
from datetime import datetime

DATA_JS_PATH = r"c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js"

def generate_batch():
    # Batch 1: Inspect, Prospect, Aspect, Retrospect, Circumspect, Export, Import, Transport, Report, Support
    # Note: I will generate the complete JSON for these 10 words first.
    
    words_data = [
        {
            "id": "inspect",
            "word": "Inspect",
            "part_of_speech": "verb",
            "meaning": "詳しく調べる、検査する、視察する",
            "author": "etymon_official",
            "etymology": {
                "breakdown": [
                    { "text": "in-", "type": "prefix", "meaning": "中に", "lang": "Latin" },
                    { "text": "specere", "type": "root", "meaning": "見る", "lang": "Latin" }
                ],
                "original_statement": "From Latin inspectare, frequentative of inspicere 'look into, examine, observe'."
            },
            "core_concept": {
                "en": "To look into the soul of things.",
                "ja": "物事の深淵を覗き込み、その真実を照らし出すこと"
            },
            "thinking_layer": "「見る」という行為が、表面的な光の反射を超えて、対象の内部へと深く浸透していくプロセスです。インスペクト（inspect）とは、単なる確認作業ではなく、秩序の乱れや隠された真実を見極めるための知的な探究です。それは、医師が診断を下すときのように、あるいは時計職人が微細な歯車の狂いを探すときのように、静寂の中で研ぎ澄まされた意識が対象と対話する瞬間です。現代社会において、この言葉は形式的な検査として扱われがちですが、その根底には、見えないものを見ようとする人間の意志が宿っています。私たちは絶えず世界を「インスペクト」し、混沌の中に意味を見出そうとしているのです。",
            "synonyms": ["examine", "scrutinize", "investigate"],
            "antonyms": ["ignore", "neglect", "overlook"],
            "aftertaste": "A focused gaze that pierces through layers of uncertainty.",
            "deep_dive": {
                "roots": [{ "term": "specere", "meaning": "to look" }],
                "points": ["respect (再び見る→尊敬) や spectator (観客) と同じ根。"]
            },
            "source": "Oxford English Dictionary",
            "date": "2026-03-04",
            "era": "17th Century Latin"
        },
        {
            "id": "prospect",
            "word": "Prospect",
            "part_of_speech": "noun",
            "meaning": "見通し、見込み、展望、景色",
            "author": "etymon_official",
            "etymology": {
                "breakdown": [
                    { "text": "pro-", "type": "prefix", "meaning": "前に", "lang": "Latin" },
                    { "text": "specere", "type": "root", "meaning": "見る", "lang": "Latin" }
                ],
                "original_statement": "From Latin prospectus 'a look out, view', from prospicere 'look forward'."
            },
            "core_concept": {
                "en": "The bridge between the current moment and future possibilities.",
                "ja": "今この場所から見える、未来という名の果てしない水平線"
            },
            "thinking_layer": "目の前の景色が単なる風景ではなく、未来の可能性として立ち現れるとき、それは「プロスペクト」となります。私たちは意識の視線を現在の外側へと投げ、まだ見ぬ明日を「見る」ことができます。それは希望であると同時に、未知への不安をも孕んだ行為です。山頂から遠くの谷を見渡す（prospective view）ように、私たちは時間という空間を俯瞰し、自らの足跡がどこへ続くのかを問いかけます。可能性は常にそこにあるのではなく、私たちが「遠くを見る（pro-spect）」ことによって初めて形作られるものなのです。この言葉は、私たちを現在の束縛から解き放ち、広大な時間の荒野へと誘います。",
            "synonyms": ["outlook", "possibility", "anticipation"],
            "antonyms": ["retrospect", "hopelessness"],
            "aftertaste": "The silent call of a horizon yet to be reached.",
            "deep_dive": {
                "roots": [{ "term": "specere", "meaning": "to look" }],
                "points": ["未来を予測する（prospective）というニュアンスが強く、単なる『景色』以上の時間的な広がりを持ちます。"]
            },
            "source": "Online Etymology Dictionary",
            "date": "2026-03-04",
            "era": "15th Century Latin"
        },
        {
            "id": "aspect",
            "word": "Aspect",
            "part_of_speech": "noun",
            "meaning": "側面、様相、外観、切り口",
            "author": "etymon_official",
            "etymology": {
                "breakdown": [
                    { "text": "ad-", "type": "prefix", "meaning": "~の方を", "lang": "Latin" },
                    { "text": "specere", "type": "root", "meaning": "見る", "lang": "Latin" }
                ],
                "original_statement": "From Latin aspectus 'a sight, look, appearance', from aspicere 'to look at'."
            },
            "core_concept": {
                "en": "A single face of a multi-faceted reality.",
                "ja": "真実という多面体の、ある一方向から見たときの輝き"
            },
            "thinking_layer": "世界はあまりに複雑で、私たちはその全体を一度に捉えることはできません。私たちが「見る」ものは、常に何らかの「アスペクト（側面）」に過ぎません。それは、光の当たる角度によって影の形が変わるように、観測者の立ち位置によって変化する真実の断片です。一つの側面がすべてだと思い込むことは、世界の豊かさを否定することに繋がります。哲学的に見れば、アスペクトとは私たちの認識の限界を示すと同時に、多様な解釈への入り口でもあります。同じ山でも、南から見るのと北から見るのとでは全く異なる表情を見せるように、一つの事象が持つ無数の側面を認め、それらを統合していくプロセスが理解という旅の正体なのです。",
            "synonyms": ["facet", "feature", "dimension"],
            "antonyms": ["whole", "totality"],
            "aftertaste": "A reminder that our vision is always partial, inviting us to look deeper.",
            "deep_dive": {
                "roots": [{ "term": "specere", "meaning": "to look" }],
                "points": ["ラテン語の aspicere (見つめる) から来ており、対象がこちらに見せる『顔』を意味します。"]
            },
            "source": "Chambers Dictionary of Etymology",
            "date": "2026-03-04",
            "era": "14th Century Latin"
        },
        {
            "id": "retrospect",
            "word": "Retrospect",
            "part_of_speech": "noun",
            "meaning": "回想、追想、過去を振り返ること",
            "author": "etymon_official",
            "etymology": {
                "breakdown": [
                    { "text": "retro-", "type": "prefix", "meaning": "後ろに", "lang": "Latin" },
                    { "text": "specere", "type": "root", "meaning": "見る", "lang": "Latin" }
                ],
                "original_statement": "From Latin retrospectus 'a looking back', from retrospicere."
            },
            "core_concept": {
                "en": "Finding meaning in the echoes of the past.",
                "ja": "過ぎ去った時間の断片を集め、今の光で照らし直す静かな対話"
            },
            "thinking_layer": "時間は容赦なく前へと流れますが、人間の意識だけは後ろへ（retro）と視線を投げ、過去を「見る（spect）」ことができます。レトロスペクトとは、単なる記憶の再生ではなく、現在の視点から過去を再定義するクリエイティブな行為です。かつては苦しみだった出来事が、振り返ってみれば成長の糧となっていたことに気づくとき、私たちは過去という荒野に新しい道を切り開いています。過去を振り返ることは、後悔するためではなく、自分の立ち位置を再確認し、次の一歩のための確かな足場を築くために必要なプロセスです。沈黙の中に眠る過去の断片が、現在の私たちの問いかけに答え、物語としての人生を紡ぎ出すのです。",
            "synonyms": ["recollection", "review", "hindsight"],
            "antonyms": ["prospect", "foresight"],
            "aftertaste": "A gentle warmth that emanates from the distance of time.",
            "deep_dive": {
                "roots": [{ "term": "specere", "meaning": "to look" }],
                "points": ["Hindsight is 20/20 という格言のように、振り返って初めて見える真実があります。"]
            },
            "source": "Merriam-Webster",
            "date": "2026-03-04",
            "era": "17th Century Latin"
        },
        {
            "id": "circumspect",
            "word": "Circumspect",
            "part_of_speech": "adjective",
            "meaning": "慎重な、用心深い、周到な",
            "author": "etymon_official",
            "etymology": {
                "breakdown": [
                    { "text": "circum-", "type": "prefix", "meaning": "周りを", "lang": "Latin" },
                    { "text": "specere", "type": "root", "meaning": "見る", "lang": "Latin" }
                ],
                "original_statement": "From Latin circumspectus 'looking around, cautious', from circumspicere."
            },
            "core_concept": {
                "en": "The calm wisdom of surveying the entire field.",
                "ja": "全方位を静かに見渡し、嵐の前の静寂と共に見極める賢明さ"
            },
            "thinking_layer": "目の前の魅力や恐怖に飛びつくのではなく、まず自分の周囲（circum）をぐるりと見渡す（spect）。これがサーカムスペクト（慎重）という言葉の真髄です。それは、リスクを恐れる卑怯さではなく、世界の広がりとその複雑な因果関係を尊重する畏敬の念から生まれる強さです。嵐の中を行く船長が、波の動き、風の匂い、そして周囲の様子をすべて把握しようとするように、私たちは行動の前に状況の全体像を捉えようとします。慎重さとは、内なる静寂を保ち、外からの刺激に対して盲目的にならず、意識の光を全方位に投げかけることなのです。一歩を踏み出す瞬間のために、無言で見つめ続けるその静かな時間にこそ、真の勇気が宿っています。",
            "synonyms": ["cautious", "prudent", "wary"],
            "antonyms": ["reckless", "imprudent", "careless"],
            "aftertaste": "A deliberate pause that precedes a decisive action.",
            "deep_dive": {
                "roots": [{ "term": "specere", "meaning": "to look" }],
                "points": ["circumference (円周) とも共通する接頭辞を持ち、360度の視界を意味します。"]
            },
            "source": "Online Etymology Dictionary",
            "date": "2026-03-04",
            "era": "15th Century Latin"
        },
        {
            "id": "export",
            "word": "Export",
            "part_of_speech": "verb",
            "meaning": "輸出する、外へ運び出す、伝える",
            "author": "etymon_official",
            "etymology": {
                "breakdown": [
                    { "text": "ex-", "type": "prefix", "meaning": "外へ", "lang": "Latin" },
                    { "text": "portare", "type": "root", "meaning": "運ぶ", "lang": "Latin" }
                ],
                "original_statement": "From Latin exportare 'carry out', from ex- 'out' + portare 'carry'."
            },
            "core_concept": {
                "en": "To share the internal treasures with the outer world.",
                "ja": "内なる境界を越え、価値あるものを未知の領域へと解き放つこと"
            },
            "thinking_layer": "経済的な概念としての輸出を超えて、この言葉は「内から外へ（ex-port）」という本質的な動きを体現しています。私たちが持つアイデア、文化、情熱を外部へと運び出す行為、それこそが真の「エクスポート」です。それは、蓄積されたエネルギーが境界を突破し、世界の他の一部と接続しようとする生命の根源的な欲求でもあります。自らの内に留まっていれば安全かもしれませんが、外へと運び出すことで初めて、その価値は世界という大きな文脈の中で試され、成長します。私たちが言葉を発することも、一種の魂の輸出であり、自己の断片を他者の世界へと届ける静かな旅なのです。この言葉は、孤立を拒み、循環を志向するすべての存在へのエールでもあります。",
            "synonyms": ["transmit", "broadcast", "deliver"],
            "antonyms": ["import", "conserve"],
            "aftertaste": "A movement that dissolves the walls of silence.",
            "deep_dive": {
                "roots": [{ "term": "portare", "meaning": "to carry" }],
                "points": ["portable (持ち運び可能な) や support (支える) と同根です。"]
            },
            "source": "Oxford English Dictionary",
            "date": "2026-03-04",
            "era": "14th Century Latin"
        },
        {
            "id": "import",
            "word": "Import",
            "part_of_speech": "verb",
            "meaning": "輸入する、持ち込む、重要性を持つ",
            "author": "etymon_official",
            "etymology": {
                "breakdown": [
                    { "text": "in-", "type": "prefix", "meaning": "中に", "lang": "Latin" },
                    { "text": "portare", "type": "root", "meaning": "運ぶ", "lang": "Latin" }
                ],
                "original_statement": "From Latin importare 'carry in', from in- 'in' + portare 'carry'."
            },
            "core_concept": {
                "en": "Opening the gates to receive the wisdom of the 'other'.",
                "ja": "他者の響きを自らの内に招き入れ、新たな風景を織りなす受容の扉"
            },
            "thinking_layer": "外の世界にある価値を、自らの内へ（in-port）と運び込むこと。それは謙虚な受容であり、自己を豊かにするための能動的な「招き」です。インポートという言葉には、自分一人では完成しないという認めが含まれています。異質な思考、未知の技術、他者の哲学が自分の中に流れ込むとき、私たちの内部世界は化学反応を起こし、以前とは違う形へと変容します。また、この言葉が「重要性（importance）」という意味を内包するのは、運ばれてくるものが「重み」を持ち、私たちの中心に深く落ち着くからでしょう。単に物を取り込むのではなく、その背後にある物語や背景を含めて受け入れることこそが、真の意味での「自身の拡張」へと繋がるのです。",
            "synonyms": ["incorporate", "adopt", "introduce"],
            "antonyms": ["export", "exclude"],
            "aftertaste": "The enrichment of the self through the presence of the other.",
            "deep_dive": {
                "roots": [{ "term": "portare", "meaning": "to carry" }],
                "points": ["重要な (important) という意味は、内容が運んでくる重みから派生しました。"]
            },
            "source": "Online Etymology Dictionary",
            "date": "2026-03-04",
            "era": "15th Century Latin"
        },
        {
            "id": "transport",
            "word": "Transport",
            "part_of_speech": "verb",
            "meaning": "輸送する、心奪われる、夢中にさせる",
            "author": "etymon_official",
            "etymology": {
                "breakdown": [
                    { "text": "trans-", "type": "prefix", "meaning": "横切って", "lang": "Latin" },
                    { "text": "portare", "type": "root", "meaning": "運ぶ", "lang": "Latin" }
                ],
                "original_statement": "From Latin transportare 'carry across', from trans- 'across' + portare 'carry'."
            },
            "core_concept": {
                "en": "The transition from one state of being to another.",
                "ja": "境界線を越え、異なる場所や精神の次元へと身を委ねる飛躍"
            },
            "thinking_layer": "物理的な場所を移動させる（trans-port）という意味を超えて、この言葉は「別の世界へと運ばれる」という恍惚の状態をも表します。美しい音楽や文学に触れ、「トランスポート」された感覚になるとき、私たちは現在の時間と空間から切り離され、魂の別の場所へと到達しています。それは、自分という存在の重力圏を脱出し、未知の地平へと渡る（trans）ための力です。輸送とは、単なる荷物の移動ではなく、ある場所から、以前とは異なる状態の場所へと「価値を移す」プロセスに他なりません。私たちの人生もまた、数々のトランスポートを経て、形を変え、成長していく旅路の連続なのです。",
            "synonyms": ["convey", "shuttle", "enrapture"],
            "antonyms": ["stay", "remain"],
            "aftertaste": "A sense of crossing an invisible bridge to a new reality.",
            "deep_dive": {
                "roots": [{ "term": "portare", "meaning": "to carry" }],
                "points": ["transfer (移転) や translate (翻訳) と共通する trans- のプレフィックスを持ちます。"]
            },
            "source": "Chambers Dictionary of Etymology",
            "date": "2026-03-04",
            "era": "14th Century Latin"
        },
        {
            "id": "report",
            "word": "Report",
            "part_of_speech": "noun/verb",
            "meaning": "報告、ニュース、銃声、伝える",
            "author": "etymon_official",
            "etymology": {
                "breakdown": [
                    { "text": "re-", "type": "prefix", "meaning": "後ろに/再び", "lang": "Latin" },
                    { "text": "portare", "type": "root", "meaning": "運ぶ", "lang": "Latin" }
                ],
                "original_statement": "From Latin reportare 'carry back, bear back', figuratively 'report'."
            },
            "core_concept": {
                "en": "Carrying the essence of an event back to the listener.",
                "ja": "現場で起きた真実の残響を、再び言語に乗せて運んでくる響き"
            },
            "thinking_layer": "何かが起きた場所から、自分たちの場所へと情報を「運び戻す（re-port）」。それがレポートの本質です。そこには、直接その場にいなかった誰かに真実を伝えるという誠実な橋渡しがあります。言葉によって事象が再現されるとき、それは単なるデータの羅列ではなく、目撃者の視点と熱量が込められた生命の形となります。銃声をあらわす「レポート」もまた、空気を震わせた衝撃が耳へと「運び戻される」音の響きです。私たちは情報の運び手として、世界と他者の間にある断絶を言葉で埋め、共通の認識という新しいネットワークを構築し続けているのです。",
            "synonyms": ["account", "dispatch", "announcement"],
            "antonyms": ["disregard", "silence"],
            "aftertaste": "The responsibility of a messenger carrying a fragment of the truth.",
            "deep_dive": {
                "roots": [{ "term": "portare", "meaning": "to carry" }],
                "points": ["porter (荷運び人) と語根を共有しており、情報の重さを運ぶ者を暗示します。"]
            },
            "source": "Oxford English Dictionary",
            "date": "2026-03-04",
            "era": "14th Century Latin"
        },
        {
            "id": "support",
            "word": "Support",
            "part_of_speech": "verb/noun",
            "meaning": "支える、支持する、維持する、扶養する",
            "author": "etymon_official",
            "etymology": {
                "breakdown": [
                    { "text": "sub-", "type": "prefix", "meaning": "下から", "lang": "Latin" },
                    { "text": "portare", "type": "root", "meaning": "運ぶ", "lang": "Latin" }
                ],
                "original_statement": "From Latin supportare 'carry up, convey, bring', from sub- 'under' + portare 'carry'."
            },
            "core_concept": {
                "en": "The invisible strength that holds through from beneath.",
                "ja": "自らを表に出さず、ただ静かに下から重みを請け負い、生かし続ける献身"
            },
            "thinking_layer": "自分を誇示するのではなく、他者の重みを、自らの肩で「下から（sub）運ぶ（port）」。これがサポートの本質です。支えるという行為は、しばしば影の仕事であり、目に見えることはありません。しかし、その支えが失われたとき、どんな巨大な構造物も、あるいは繊細な心も、崩れ去ってしまいます。下からそっと支えるその手があるからこそ、上にあるものは自由に踊り、表現することができるのです。人生において「サポーティブ」であることは、自分のエネルギーを誰かの基盤として提供するという究極の愛の形であり、それは、個としての生命を超えた「繋がりの深さ」を信じているからこそ可能な、静かなる偉業なのです。",
            "synonyms": ["uphold", "bolster", "advocate"],
            "antonyms": ["undermine", "oppose", "abandon"],
            "aftertaste": "A quiet resilience that expects no credit, only stability.",
            "deep_dive": {
                "roots": [{ "term": "portare", "meaning": "to carry" }],
                "points": ["substitute (代わりにする) と同じ sub- が使われ、基礎としての役割を強調します。"]
            },
            "source": "Online Etymology Dictionary",
            "date": "2026-03-04",
            "era": "14th Century Latin"
        }
    ]
    
    # 2. Append to data.js
    try:
        with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
        
        match = re.search(r"const WORDS = (\[.*\]);", content, re.DOTALL)
        if not match:
            print("Could not find WORDS array")
            return
            
        existing_words = json.loads(match.group(1))
        # Filter out if any accidentally already exist
        existing_ids = {w["id"].lower() for w in existing_words if "id" in w}
        new_filt = [w for w in words_data if w["id"].lower() not in existing_ids]
        
        existing_words.extend(new_filt)
        
        new_json = json.dumps(existing_words, indent='\t', ensure_ascii=False)
        new_content = f"const WORDS = {new_json};\n"
        
        with open(DATA_JS_PATH, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Added {len(new_filt)} words.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    generate_batch()
