import json
import re

file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'(const WORDS = )(\[.*\])(;)', content, re.DOTALL)
if match:
    prefix, json_array_str, suffix = match.groups()
    words = json.loads(json_array_str)
    
    seen_words = {}
    duplicates = []
    
    unique_words = []
    
    for w in words:
        word_lower = w['word'].lower().strip()
        if word_lower in seen_words:
            duplicates.append(w['word'])
        else:
            seen_words[word_lower] = w
            unique_words.append(w)
            
    print(f"Found {len(duplicates)} duplicates: {duplicates}")
    
    # Save back without duplicates
    new_content = content[:match.start()] + prefix + json.dumps(unique_words, ensure_ascii=False, indent='\t') + suffix + content[match.end():]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Removed duplicates. Total words now: {len(unique_words)}")
else:
    print("Could not parse data.js")
