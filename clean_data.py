import json
import re

with open('data.js', 'r', encoding='utf-8') as f:
    text = f.read()

prefix = 'const WORDS = '
if text.startswith(prefix):
    json_str = text[len(prefix):]
    if json_str.endswith(';'):
        json_str = json_str[:-1]
    elif json_str.endswith(';\n'):
        json_str = json_str[:-2]
    
    words = json.loads(json_str)
    
    modified = 0
    for word in words:
        if 'word' in word:
            old_word = word['word']
            new_word = re.sub(r'[、。]', '', old_word)
            if old_word != new_word:
                word['word'] = new_word
                modified += 1
                print(f"Fixed word: {old_word} -> {new_word}")
                
        if 'id' in word:
            old_id = word['id']
            new_id = re.sub(r'[、。]', '', old_id)
            if old_id != new_id:
                word['id'] = new_id
                modified += 1
                print(f"Fixed id: {old_id} -> {new_id}")
                
    if modified > 0:
        new_text = prefix + json.dumps(words, indent='\t', ensure_ascii=False) + ';\n'
        with open('data.js', 'w', encoding='utf-8') as f:
            f.write(new_text)
        print(f"Total modified: {modified}")
    else:
        print("No words needed fixing.")
else:
    print("Does not start with prefix")
