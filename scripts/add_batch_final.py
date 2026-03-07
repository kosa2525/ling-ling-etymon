import json
import re

word_batch = [
    {
        "id": "epilogue_story",
        "word": "Epilogue",
        "meaning": "結びの言葉、エピローグ、後日談",
        "era": "15th Century Old French/Greek epilogos",
        "etymology": {
            "components": ["epi- (in addition)", "logos (word, speech)"],
            "original_statement": "From Old French epilogue, from Latin epilogus, from Greek epilogos (conclusion of a speech), from epi- (in addition) + logos (word, speech)."
        },
        "concept": "An addition to the speech (物語の後に添えられた、余韻の言葉)",
        "thinking": "本編が終わった後、観客や読者に向けて最後に「付け加えられる（epi-）」言葉。それは劇の幕が降りた後の静寂の中で、これまでの物語を咀嚼し、未来へと繋げるための橋渡しです。すべてが終わったからこそ語れる、静かで深い納得の場所。",
        "aftertaste": "幕は降りた。けれど、物語はあなたの心の中で、密やかに続いてゆく。",
        "example": "The novel's epilogue explains what happened to the characters ten years later.",
        "deep_dive": {
            "roots": [{"term": "leg-", "meaning": "to speak"}],
            "points": ["prologue（序文：前に語るもの）の対義語。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "denouement_story",
        "word": "Denouement",
        "meaning": "大団円、(事件の)解決、結末",
        "era": "18th Century French denouer",
        "etymology": {
            "components": ["de- (reversal)", "nouer (to knot)"],
            "original_statement": "From French dénouement (an untying), from dénouer (to untie), from Old French desnoer, from des- (reversal) + nouer (to knot), from Latin nodus (knot)."
        },
        "concept": "An untying of the knot (複雑に絡まった「結び目」を解くこと)",
        "thinking": "物語のクライマックスを過ぎ、複雑に絡み合っていた伏線や人間関係の「結び目（knot/nodus）」が、するすると「解かれる（untying）」プロセス。緊張から解放され、すべての真実が白日の下に晒される、安堵とカタルシスの瞬間です。",
        "aftertaste": "絡まった糸が一本に解（ほど）ける。世界は、あるべき秩序を取り戻した。",
        "example": "The denouement of the mystery film was unexpected and quite brilliant.",
        "deep_dive": {
            "roots": [{"term": "ned-", "meaning": "to bind, tie"}],
            "points": ["node（節/結び目）の逆を行く、知的で鮮やかな解決。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "resonance_story",
        "word": "Resonance",
        "meaning": "響き、共鳴、深い感動、レゾナンス",
        "era": "15th Century Old French/Latin resonare",
        "etymology": {
            "components": ["re- (again)", "sonare (to sound)"],
            "original_statement": "From Latin resonantia (echo), from resonare (to sound again, resound)."
        },
        "concept": "Sounding again (再び、繰り返し響き渡ること)",
        "thinking": "音が一度鳴って消えるのではなく、何かにぶつかって「再び鳴り（re-sound）」、周囲と共振すること。それは物理的な音だけでなく、誰かの言葉や行為が、自分の魂の震動数と一致し、いつまでも心の深くに響き続ける「深い納得感」をも指します。",
        "aftertaste": "声が止んでも、胸の奥の波紋は、いつまでも静かに揺れている。",
        "example": "His speech had a deep resonance with the struggles of ordinary people.",
        "deep_dive": {
            "roots": [{"term": "swen-", "meaning": "to sound"}],
            "points": ["sonata（ソナタ）や sound（音）と同じ、心地よい響きの系譜。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "legacy_final",
        "word": "Legacy",
        "meaning": "遺産、受け継がれしもの、名残",
        "era": "14th Century Old French/Latin legatus",
        "etymology": {
            "components": ["legare (to appoint by will, send as ambassador)"],
            "original_statement": "From Old French legacie, from Latin legatus (ambassador, envoy), from legare (to appoint by a last will, send with a commission)."
        },
        "concept": "Something sent from the past (過去からの使者として託された、尊き名残)",
        "thinking": "物語が終わり、人が去った後に、残された者たちの中に生き続ける「意志の欠片」。それは物質的な富だけでなく、その人がいたからこそ変わった世界の「手触り」です。死や終焉を超えて、未来という見知らぬ大地へ派遣された「使者（ambassador）」のような贈り物。",
        "aftertaste": "姿は見えなくても。あなたの残した光が、今も誰かの足元を照らしている。",
        "example": "The artist's true legacy lies in the countless people he inspired to create.",
        "deep_dive": {
            "roots": [{"term": "leg-", "meaning": "to collect, speak"}],
            "points": ["legal（法律）と同じく、公的に『任ぜられた』重みがあります。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "tranquility_final",
        "word": "Tranquility",
        "meaning": "平穏、静寂、落ち着き",
        "era": "14th Century Old French/Latin tranquillus",
        "etymology": {
            "components": ["trans- (over, beyond)", "quies (rest, peace)"],
            "original_statement": "From Latin tranquillus (quiet, calm, still, serene), possibly from trans- (over) + quies (rest)."
        },
        "concept": "Beyond the restlessness (騒がしさの「向こう側」にある安息)",
        "thinking": "激動の物語をすべて読み終え、本を閉じた後に訪れる、どこまでも深い「凪（なぎ）」。嵐を「通り抜けて（trans-）」辿りついた、究極の「休み（quies）」。それは何もない空虚ではなく、すべてを経験した者だけが手にできる、満ち足りた沈黙の境地です。",
        "aftertaste": "すべては終わった。そして、すべてが静かな光の中に溶けてゆく。",
        "example": "The tranquility of the forest after the storm was profound and healing.",
        "deep_dive": {
            "roots": [{"term": "kweie-", "meaning": "to rest, be quiet"}],
            "points": ["quiet（静かな）や quit（辞める）の、究極の完了形。"]
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
