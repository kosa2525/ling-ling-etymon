import json
import re

def fix_and_load(file_path):
    print(f"Reading {file_path}...")
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    match = re.search(r'const WORDS = (\[.*\]);', content, re.DOTALL)
    if not match:
        print("WORDS array not found.")
        return

    json_str = match.group(1)

    print("Attempting to parse JSON...")
    
    # 手動で壊れた部分をパッチする (Gibe) などの部分
    # エラーが出た近辺を見ると辞書のキーやクオートの閉じ忘れなどがある。
    # 今回は少し強引に、壊れたオブジェクトを除去または修正する。
    
    # 連続で置換をかけてJSONを復旧させる
    json_str = json_str.replace('"(Gibe)",ster",\n\t\t"part_of_sp', '"source": "Merriam-Webster",\n\t\t"part_of_sp')
    json_str = json_str.replace('ster",\n\t\t"part_of_sp', '"source": "Merriam-Webster",\n\t\t"part_of_speech": "noun",')
    
    # 完全に壊れているオブジェクトを一旦スキップする手段として、
    # JSONDecoderを使って1つずつパースする。
    
    decoder = json.JSONDecoder()
    pos = 0
    words = []
    errors = 0
    
    while pos < len(json_str):
        # オブジェクトの開始を探す
        match = re.search(r'\{[\s\n]*"id":', json_str[pos:])
        if not match:
            break
            
        start_index = pos + match.start()
        try:
            obj, end_index = decoder.raw_decode(json_str[start_index:])
            # オブジェクトが取得できたら追加
            if 'id' in obj and 'word' in obj:
                words.append(obj)
            pos = start_index + end_index
        except json.JSONDecodeError:
            errors += 1
            # パースに失敗した場合は、次の "id": を見つけるために少し進める
            pos = start_index + 1
            
    print(f"Successfully rescued {len(words)} valid words.")
    print(f"Encountered {errors} errors while parsing.")
    
    return words

if __name__ == '__main__':
    words = fix_and_load('data.js')
    if words:
        # 重複を削除して名前順にソートする
        unique_words = {w['id'].lower(): w for w in words}
        final_words = list(unique_words.values())
        final_words.sort(key=lambda x: str(x.get('word', '')).lower())
        
        print(f"Total unique words: {len(final_words)}")
        
        with open('data.js', 'w', encoding='utf-8') as f:
            f.write("const WORDS = ")
            json.dump(final_words, f, indent='\t', ensure_ascii=False)
            f.write(";\n")
        print("Saved repaired data to data.js")
