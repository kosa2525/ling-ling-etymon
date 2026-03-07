import json
import re

word_batch = [
    {
        "id": "merit",
        "word": "Merit",
        "meaning": "功績、長所、価値がある",
        "era": "13th Century Old French/Latin meritus",
        "etymology": {
            "components": ["merere (to earn, deserve, gain a share)"],
            "original_statement": "From Old French merite, from Latin meritum (anything that deserves reward), from merēre (to earn, earn as pay, deserve, acquire)."
        },
        "concept": "A share that one has earned (自らの働きで勝ち取った取り分)",
        "thinking": "ただ授けられた幸運ではなく、自分の汗と努力で「相応の報い（earn）」として手に入れた成果。本来は「自分の分け前を勝ち取る」という意味が込められており、そこから現在では、対象が持っている「本質的な価値」そのものを指すようになりました。",
        "aftertaste": "誰も見ていなくても。ただ淡々と、自らの価値を磨く者への賞讃。",
        "example": "Selection for the team will be based solely on artistic merit.",
        "deep_dive": {
            "roots": [{"term": "smer-", "meaning": "to allot, assign a share"}],
            "points": ["mercenary（傭兵：報酬のために働く者）の mer- も同じルーツです。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "virtue",
        "word": "Virtue",
        "meaning": "美徳、徳目、(有効な)力",
        "era": "13th Century Old French/Latin virtus",
        "etymology": {
            "components": ["vir (man)", "virtus (manliness, worth, strength)"],
            "original_statement": "From Old French vertu, from Latin virtutem (manliness, moral strength, high character, excellence), from vir (man)."
        },
        "concept": "The power of a true human (人としての真なる力、卓越性)",
        "thinking": "もともとは、一人の成熟した人間としての「力強さ、男気、卓越（virtus）」を意味しました。それは単なる道徳的な潔癖さではなく、困難な事態を切り抜けるための、しなやかで強靭な「内なる精神の力」そのもののことです。",
        "aftertaste": "正しくあること。それは、魂が放つ最強の力となる。",
        "example": "Patience is a great virtue to have in the modern world.",
        "deep_dive": {
            "roots": [{"term": "wi-ro-", "meaning": "man, hero"}],
            "points": ["werewolf（人狼）の were も『人間』を意味するこの vir 系の一員。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "worth",
        "word": "Worth",
        "meaning": "価値がある、値打ち、相当する",
        "era": "Old English weorþ",
        "etymology": {
            "components": ["weorth (worthy, honorable, expensive)"],
            "original_statement": "From Old English weorþ (value, amount, price, dignity)."
        },
        "concept": "The weight of value (価値が持つ、ずっしりとした重み、尊厳)",
        "thinking": "ただの数字で測れる「価格（price）」ではなく、そのものが内包している「重みや尊厳（dignity）」に根ざした価値。あなたの「ありのまま」の存在が持っている価値。それは誰に評価されるまでもなく、最初からそこに備わっているものです。",
        "aftertaste": "他人の物差しではなく、自分の中にある静かな自尊心の重さ。",
        "example": "Self-worth is the most valuable thing an individual can possess.",
        "deep_dive": {
            "roots": [{"term": "wer-", "meaning": "to turn, twist (possible)"}],
            "points": ["word（言葉）などは『wer-（話す）』系ですが、こちらは『重さ/回転』に関連するとされる説も。"]
        },
        "part_of_speech": "adjective"
    },
    {
        "id": "honor",
        "word": "Honor",
        "meaning": "名誉、光栄、敬う",
        "era": "12th Century Old French/Latin honos",
        "etymology": {
            "components": ["honos (dignity, office, reputation, ornament)"],
            "original_statement": "From Latin honor/honos (reputation, public esteem, official dignity)."
        },
        "concept": "Public respect or ornament of character (公的な尊厳、魂を飾る気高き名声)",
        "thinking": "もともとは、公職（公的な立場）にある人間の「品位（dignity）」を指しました。それは、周囲からの視線に耐えうる、一点の曇りもない誠実さと責任感によって形作られます。自分よりも大きなもののために尽くす決意が放つ、目に見えない飾り（ornament）のこと。",
        "aftertaste": "誰の前でも、自分自身に嘘をつかずに立てる誇り。",
        "example": "It is a great honor to be chosen as the leader of this team.",
        "deep_dive": {
            "roots": [],
            "points": ["honest（正直な）の hon- もその誠実さの仲間。"]
        },
        "part_of_speech": "noun"
    },
    {
        "id": "grace",
        "word": "Grace",
        "meaning": "優雅、恩寵、上品、(数日間の)猶予",
        "era": "12th Century Old French/Latin gratia",
        "etymology": {
            "components": ["gratus (pleasing, agreeable, thankful)"],
            "original_statement": "From Old French grace, from Latin gratia (agreeableness, charm, favor, thanks), from gratus (pleasing, thankworthy)."
        },
        "concept": "A pleasing favor (他者に喜びを与える優雅さ、好意)",
        "thinking": "単なる外面的なしなやかさではなく、相手に対して快く(agreeable)、感謝(thanks)を込めて接するその心そのもの。また、「猶予（grace period）」という言葉には、厳しい法規に対しても、人としての好意を忘れないという温かさが込められています。",
        "aftertaste": "余白こそが、美しさ。心をふわりとゆるめる、柔らかな光。",
        "example": "She handled the difficult situation with incredible grace and dignity.",
        "deep_dive": {
            "roots": [{"term": "gwer-", "meaning": "to lift up, favor, praise"}],
            "points": ["congratulate（祝う）の grat も『喜び』を共有する意味で繋がります。"]
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
