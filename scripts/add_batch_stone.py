import json
import re

word_batch = [
    # Cycle 113: Stone & Time
    {
        "id": "endurance_stone",
        "word": "Endurance",
        "meaning": "忍耐、耐久力、辛抱、持続",
        "era": "14th Century Latin indurare",
        "etymology": {
            "components": ["indurare (to make hard)"],
            "original_statement": "From Old French endurance, from endurer (to undergo, bear), from Latin indurare (to make hard), from in- (into) + durus (hard)."
        },
        "concept": "Making hard within (内側を「石のように硬く（hard）」し 困難を「耐え抜く（undergo）」こと)",
        "thinking": "激しい風雨にさらされても 形を変えずに立ち続ける 巨石のような精神の強さ. 語源は「硬くすること」. それは単に我慢することではなく 痛みや時間を自らの血肉に変え より強固な自己へと結晶化させていくプロセスです. 耐え抜いた先には 決して壊れない真実の自分が残ります.",
        "aftertaste": "石の沈黙. あなたが今 耐えているその時間は 無意味な苦しみではない. それはあなたの魂を 永遠に色褪せない宝石へと 磨き上げている聖なる工程なのだ.",
        "example": " Marathon runners need incredible physical and mental endurance to finish the race.",
        "deep_dive": { "roots": [{"term": "deru-", "meaning": "to be firm, solid, steadfast"}], "points": ["tree（木）や trust（信頼）と同じ。根を張り、揺るがない存在。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "fortitude_stone",
        "word": "Fortitude",
        "meaning": "不屈の精神、勇気、剛勇",
        "era": "14th Century Latin fortis",
        "etymology": {
            "components": ["fortis (strong, brave, firm)"],
            "original_statement": "From Old French fortitude, from Latin fortitudo (strength, firmness, manliness), from fortis (strong, brave, firm, steadfast)."
        },
        "concept": "State of being strong (内なる「要塞（fort）」を築くように 精神を「強固（strong）」に保つこと)",
        "thinking": "逆境にあっても取り乱さず 自らの信念を静かに守り抜く 高潔な勇気. 語源の fortis は 物理的な強さだけでなく 精神的な揺るぎなさを指します. それは 嵐の中で灯火を守り続けるような 繊細にして強靭な力. 誰にも見られない場所で 独り正しくあり続けるための強さです.",
        "aftertaste": "内なる要塞. 世界がどんなに騒がしくても あなたの心の核にあるその聖域（サンクチュアリ）だけは 誰にも侵すことはできないのだから.",
        "example": "She faced her illness with remarkable fortitude and optimism.",
        "deep_dive": { "roots": [{"term": "bhergh-", "meaning": "high, to protect (possible related)"}], "points": ["fort（砦）や force（力）と同じ。守備的な強さの美学。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "constancy_stone",
        "word": "Constancy",
        "meaning": "不変、恒常性、節操、貞節",
        "era": "15th Century Latin con- + stare",
        "etymology": {
            "components": ["con- (together, altogether)", "stare (to stand)"],
            "original_statement": "From Middle French constance, from Latin constantia (a standing firm, firmness, steadiness), from constans (standing firm, constant), from con- + stare (to stand)."
        },
        "concept": "Standing firm together (すべてが「一体（together）」となって 「立ち続ける（stand）」揺るぎなき状態)",
        "thinking": "移ろいやすいこの世界で 唯一変わらないもの. 語源は「共に立つ」. 状況が変わっても 感情が波立っても 常に同じ場所に立ち続ける 北極星のような在り方. それは 愛や信念が時間を味方につけ 永遠という名の彫刻へと変わっていくプロセスです.",
        "aftertaste": "北極星の祈り. すべてが流れていく中で 変わらない一点を持っていること. それが あなたという旅人の 唯一にして最大の道標（しるべ）になる.",
        "example": "The constancy of her friendship was a source of great comfort during his difficult years.",
        "deep_dive": { "roots": [{"term": "sta-", "meaning": "to stand"}], "points": ["state（国家）や statue（像）と同じ。形を保ち続ける意志のルーツ。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "perpetuity_stone",
        "word": "Perpetuity",
        "meaning": "永続、不朽、終身",
        "era": "14th Century Latin per- + petere",
        "etymology": {
            "components": ["per- (through)", "petere (to seek, aim for, rush)"],
            "original_statement": "From Old French perpetuite, from Latin perpetuitatem (continuity, uninterrupted power), from perpetuus (continuous, universal, constant), from per- (through) + root of petere (to seek, go to, rush at)."
        },
        "concept": "Seeking through (時間を「突き抜けて（through）」 理想を「追い求め続ける（seek）」終わりのない航海)",
        "thinking": "世代を超え 時代を超えて 永久に繰り返されるリズム. 語源は「突き進む」. それは静止しているのではなく 常に先へ先へと連続していく 動的な永遠です. あなたが今 紡いでいる言葉や愛も またこの永続する物語の 一節となって未来へ繋がっていきます.",
        "aftertaste": "終わりのない円環. あなたの命はいつか尽きるかもしれないが あなたが世界に残した「善き意志」は 永遠という名の海を どこまでも流れてゆく.",
        "example": "The foundation was established to protect the historical site in perpetuity.",
        "deep_dive": { "roots": [{"term": "per-", "meaning": "forward, through"}, {"term": "pet-", "meaning": "to rush, fly"}], "points": ["petition（請願：求めること）と同じ。永遠とは、求め続ける意志。"] },
        "part_of_speech": "noun"
    },
    {
        "id": "invariant_stone",
        "word": "Invariant",
        "meaning": "不変の、一定の、不変量",
        "era": "19th Century Latin in- + varius",
        "etymology": {
            "components": ["in- (not)", "varius (changing, spotted)"],
            "original_statement": "From in- (not) + variant (changing). Coined by philosopher and mathematician James Joseph Sylvester."
        },
        "concept": "Not changing (どんなに「変換（change）」を加えても 「変わらない（not changing）」本質的な核)",
        "thinking": "変化こそが常態である宇宙において 頑（かたく）なにその姿を保ち続ける本質. 語源は「変化しない」. 数学用語では 変換を受けても等しいままの量を指します. あなたがどんなに成長し 境遇が変わっても 決して変わることのない「自分らしさ」の核. それこそが あなたの固有の美しさです.",
        "aftertaste": "黄金の核. 移ろう日々に惑わされないで。あなたの心の奥底には どんな嵐も、どんな時間も 決して変えることのできない 輝く真実が眠っているのだから.",
        "example": "The laws of physics are believed to be invariant across the entire universe.",
        "deep_dive": { "roots": [{"term": "ne-", "meaning": "not"}, {"term": "wer-", "meaning": "to turn, bend"}], "points": ["various（多様な）の否定。多様性の中にある、たった一つの不変。"] },
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
        print(f"Success: Added {added} words in Cycle 113.")
    else:
        print("Error: Could not find array in data.js")
except Exception as e:
    print(f"Error: {e}")
