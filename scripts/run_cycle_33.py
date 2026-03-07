import json
import re

# Theme: The Pulse of Society & Structure (Cycle 33)
words_data = [
    ("hierarchy", "Hierarchy", "階層、ヒエラルキー", "14th Century", "hieros (sacred) + arkhein (to rule)", "A system or organization in which people or groups are ranked one above the other according to status or authority", "天上の「聖なる（。ヒエロス）秩序（。アーク）」が、地上の（。不完全な（。社会へと（。投影（。された（。もの（。。（。頂点（。から（。底（。へと（。流（。れる（。、不可逆な（。力の（。勾配。"),
    ("bureaucracy", "Bureaucracy", "官僚機構、お役所仕事", "18th Century", "bureau (desk, office) + kratein (to rule)", "A system of government in which most of the important decisions are made by state officials rather than by elected representatives", "開（。か（。れた（。広場（。ではなく（。、閉（。ざ（。された「事務所の（。机（。ビューロー）を（。支配（。する者（。たち（。）」による（。政治（。。（。規則（。と（。書類の（。森の中で（。、知性が（。歯車へと（。変わって（。いく（。、冷徹な（。自動（。機械。"),
    ("aristocracy", "Aristocracy", "貴族政治、特権階級", "14th Century", "aristos (best) + kratein (to rule)", "The highest class in certain societies, especially those holding hereditary titles or offices", "数（。に（。頼（。る（。のではなく（。、自らを「最も（。優（。れた（。アリスト）者」だと（。自負（。する（。少数の（。人間（。による（。支配（。。（。洗練（。された（。美学（。と（。、選（。ば（。れ（。た（。責任（。の（。誇り。"),
    ("democracy", "Democracy", "民主主義", "16th Century", "demos (the people) + kratein (to rule)", "A system of government by the whole population or all the eligible members of a state, typically through elected representatives", "一人の（。天才（。や（。王を（。信（。じる（。のを（。止め（。、名もなき「民衆（。デモス）全員が（。支配（。クラシー）する」という（。、混沌（。の中に（。英知（。を見出（。そう（。とする（。、壮大な（。実験。"),
    ("monarchy", "Monarchy", "君主制", "14th Century", "monos (alone, single) + arkhein (to rule)", "A form of government with a monarch at the head", "対立（。する（。意見（。を（。ねじ伏せ（。、ただ「一人の（。モノ）意志（。アーク）だけで（。全てを（。決（。める（。）」という（。、暴力（。的な（。までの（。効率性（。と（。、孤独（。な（。責任の（。王座。"),
    ("oligarchy", "Oligarchy", "寡頭（かとう）政治", "16th Century", "oligos (few) + arkhein (to rule)", "A small group of people having control of a country, organization, or institution", "民衆（。を（。嘲笑（。し（。、特権（。を（。分け（。合う「少数の（。オリゴ）権力者（。アーク）」による（。、閉鎖（。的（。な（。支配（。。（。血（。と（。利権（。で（。固められた（。、変化（。を（。拒む（。権威。"),
    ("anarchy", "Anarchy", "無政府状態、アナーキー", "16th Century", "a- (without) + arkhein (to rule)", "A state of disorder due to absence or nonrecognition of authority", "いかなる（。権力（。も（。認め（。ず（。、「支配（。アーク）を持（。たない（。ア）」という（。極限（。の（。自由（。。（。真の（。自律（。か（。、あるいは（。絶望（。的な（。混沌（。か。"),
    ("hegemony", "Hegemony", "覇権、ヘゲモニー", "16th Century", "hegemon (leader, ruler)", "Leadership or dominance, especially by one country or social group over others", "直接（。的な（。暴力（。を（。超え（。、価値観（。の（。押し付け（。によって（。、自らを「唯一の（。指導者（。ヘゲモン）」として（。認め（。させる（。、目（。に（。見えない（。支配の（。網。"),
    ("authority", "Authority", "権威、権限", "13th Century", "auctor (author, originator)", "The power or right to give orders, make decisions, and enforce obedience", "ただの（。力（。ではなく（。、そこ（。に（。一つの（。価値を「産（。み（。出した（。オクター）」と（。いう（。、歴史（。への（。貢献（。に（。裏打ち（。された（。、揺るぎ（。ない（。正統性。"),
    ("legitimacy", "Legitimacy", "正統性、適法性", "17th Century", "lex (law)", "Conformity to the law or to rules", "剥（。き（。出しの（。暴力（。が（。、いつしか「法（。レックス）という（。美しい（。服（。）」を（。纏（。い（。、誰一人（。疑わ（。ない（。秩序（。へと（。変貌（。した（。、歴史の（。洗練の（。結果。"),
    ("sovereignty", "Sovereignty", "主権、統治権", "14th Century", "super (above)", "Supreme power or authority", "他者の（。意志を（。一切（。介在（。させ（。ず（。、自分が（。自分に（。対して「最上位（。スーパー）である」と（。宣言（。する（。、誇り（。高い（。独立（。の（。中心。"),
    ("jurisdiction", "Jurisdiction", "司法権、管轄権", "14th Century", "jus (law) + dicere (to say)", "The official power to make legal decisions and judgments", "ある（。土地（。や（。人の（。存亡（。に対し（。、「法（。ジュリ）を（。宣告（。ディクション）する」ことのできる（。、運命（。の（。境界線。"),
    ("legislature", "Legislature", "立法府、議会", "17th Century", "lex (law) + latus (carried, proposed)", "The legislative body of a country or state", "出来事（。の（。後（。追い（。ではなく（。、未来（。のあるべき（。形を「法（。レックス）として（。提出（。レト）し（。）」、社会の（。設計図（。を（。書き（。換えて（。いく（。、言葉の（。工房。"),
    ("judiciary", "Judiciary", "司法、司法制度", "16th Century", "judex (judge)", "The judicial authorities of a country; judges collectively", "激（。しい（。感情（。から（。距離（。を（。置き（。、「正しい（。ジュ）道（。ディッシュ）を示（。す者（。）」によって（。、混沌（。から（。真実（。を（。抽出（。し（。、公平（。という（。名の（。秤（。を（。守（。る（。砦。"),
    ("federal", "Federal", "連邦の、同盟の", "17th Century", "foedus (league, treaty, compact)", "Relating to or denoting the central government of a federation", "独立（。した（。個々（。の（。意志（。が（。、「信頼（。フィデス）という（。結び（。目（。）」によって（。一つ（。に（。繋（。が（。り（。、巨大（。な（。共同体（。へと（。進展（。した（。、知的な（。連帯の（。形。"),
    ("municipal", "Municipal", "地方自治体の、市制の", "16th Century", "munia (duties) + capere (to take up)", "Relating to a city or town or its governing body", "遠（。い（。中心（。に（。頼（。らず（。、自ら（。の（。街の（。課題（。を「自分（。たちの（。崇高な（。義務（。ミューニア）として（。取（。り（。上げ（。る（。）」、最も（。身近（。な（。自律（。の（。輝き。"),
    ("civic", "Civic", "市民の、公民の", "16th Century", "civis (citizen)", "Relating to a city or town, especially its administration; municipal", "ただの（。居住者（。では（。なく（。、社会（。という（。建物（。の（。一部を「担（。う者（。シヴィス）」としての（。自覚（。と（。、公的（。な（。美徳（。への（。献身。"),
    ("pluralism", "Pluralism", "複数主義、多様性", "17th Century", "plus (more)", "A condition or system in which two or more states, groups, principles, sources of authority, etc., coexist", "一（。つの（。正解（。へと（。他者を（。暴力（。的に（。染める（。のを（。止め（。、「より（。多く（。プルス）の（。価値観」が（。共生（。する（。ことを（。喜（。び（。、豊かさ（。を（。受け（。入（。れよう（。とする（。、知性の（。寛容。"),
    ("consensuses", "Consensus", "合意、コンセンサス", "19th Century", "com- (together) + sentire (to feel)", "A general agreement", "言葉（。による（。説得（。を（。超え（。、全員（。が「共に（。コン）感じ（。セン）取り（。）」、深い（。納得（。の（。うちに（。、一つの（。方向（。へと（。魂（。が（。向き（。揃（。う（。、調和（。の（。瞬間。"),
    ("diplomacy", "Diplomacy", "外交", "18th Century", "diploma (folded paper)", "The profession, activity, or skill of managing international relations", "銃火（。を（。交（。わす（。代わりに（。、「折り畳（。ま（。れた（。ディ）書（。簡（。プローマ）」を（。交換（。し（。、言葉（。の（。糸（。を（。手繰（。り（。寄せ（。、破局（。を（。かろ（。やかに（。回避（。する（。、知的な（。ダンス。"),
    ("coalition", "Coalition", "連合、提携、連立", "17th Century", "com- (together) + alescere (to grow)", "An alliance for combined action, especially a temporary alliance of political parties forming a government or of states", "敵（。対（。して（。いた（。者（。同士が（。、共通の（。目標（。を（。求めて「共に（。コン）育（。ち（。アリ）始める（。）」、ダイナミック（。で（。戦略的な（。、一時的（。な（。融合。"),
    ("partisan", "Partisan", "熱心な支持者、党派心の強い、パルチザン", "16th Century", "part (part, share)", "A strong supporter of a party, cause, or person", "全体（。を（。見る（。視力（。を（。一時（。的に（。捨て（。、自らが「分け（。られた（。パート）一部」で（。ある（。ことを（。誇（。り（。に（。し（。、特定（。の（。旗（。の（。ために（。身（。を（。投（。じる（。、狂熱（。の（。忠誠。"),
    ("espionage", "Espionage", "スパイ活動、間諜", "18th Century", "espion (spy)", "The practice of spying or of using spies, typically by governments, to obtain political and military information", "公的（。な（。顔の（。裏側（。で（。、沈黙（。の（。闇を（。、「見（。張（。る（。エスパイ）」こと（。。（。情報（。という（。名の（。毒（。を（。抽出（。し（。、国家（。の（。運命（。を（。歪（。める（。、見えない（。手の（。動き。"),
    ("surveillance", "Surveillance", "監視、サーベイランス", "19th Century", "sur- (over) + veiller (to watch)", "Close observation, especially of a suspected spy or criminal", "全ての（。行動を（。、「上（。シュール）から（。見つめ（。ヴェ）続ける（。）」、逃（。げ（。場（。の（。ない（。まなざし（。。（。安全法（。という（。名の（。檻（。と（。、自由（。という（。名の（。砂漠。"),
    ("propaganda", "Propaganda", "宣伝、プロパガンダ", "18th Century", "propagare (to set forward, extend, spread)", "Information, especially of a biased or misleading nature, used to promote or publicize a particular political cause or point of view", "真実（。の（。探求（。ではなく（。、ある（。特定の（。思想（。を「増殖（。プロパ）させ（。）、植（。え付ける（。）」ことで（。、大衆（。の（。脳（。を（。同じ（。色（。に（。染（。め（。上げ（。ようと（。する（。、知的な（。感染。")
]

def run_cycle():
    file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
        if not match:
            print("Error: Could not find WORDS array in data.js")
            return

        prefix, json_array_str, suffix = match.groups()
        existing_words = json.loads(json_array_str)
        existing_ids = {w.get("id") for w in existing_words}
        existing_word_texts = {w.get("word").lower() for w in existing_words}

        added_count = 0
        for item in words_data:
            word_text = item[0]
            word_id = f"{word_text.lower()}_soc"
            
            if word_id not in existing_ids and word_text.lower() not in existing_word_texts:
                new_word = {
                    "id": word_id,
                    "word": word_text,
                    "meaning": item[2],
                    "era": item[3],
                    "etymology": {
                        "components": [item[4]],
                        "original_statement": f"From {item[3]} {item[4]}."
                    },
                    "concept": item[5] + f" ({item[6]})",
                    "thinking": item[6],
                    "aftertaste": item[7] if len(item) > 7 else "社会とは、孤独な魂たちが寄り添って作り上げた、巨大な物語の集積です。",
                    "example": f"The country's political {word_text} has undergone significant changes in recent years.",
                    "deep_dive": {
                        "roots": [{"term": item[4].split(" ")[0] if " " in item[4] else item[4], "meaning": " ".join(item[4].split(" ")[1:]).strip("()") if " " in item[4] else "origin"}],
                        "points": ["秩序は、混沌を愛という名の毛布で包み込んだ結果です。"]
                    },
                    "part_of_speech": "noun" if item[0] not in ["federal", "municipal", "civic", "secular", "pluralism", "partisan"] else "adjective"
                }
                existing_words.append(new_word)
                added_count += 1
                existing_ids.add(word_id)
                existing_word_texts.add(word_text.lower())

        new_json_str = json.dumps(existing_words, ensure_ascii=False, indent='\t')
        new_content = content[:match.start()] + prefix + new_json_str + suffix + content[match.end():]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Success: Added {added_count} words. Theme: Society & Structure (Cycle 33).")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_cycle()
