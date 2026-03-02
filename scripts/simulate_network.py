import json
import re
import random

def search_anomaly():
    with open(r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        match = re.search(r'WORDS\s*=\s*(\[.*\])', content, re.DOTALL)
        all_words = json.loads(match.group(1))

    root_map = {}
    type_map = {}
    for w in all_words:
        for b in w.get('etymology', {}).get('breakdown', []):
            b_type = b.get('type', '').lower()
            if 'root' in b_type or 'prefix' in b_type or 'suffix' in b_type:
                root_text = b.get('text', '').lower().replace('-', '').strip()
                if not root_text: continue
                if root_text not in root_map: root_map[root_text] = []
                root_map[root_text].append(w['word'])
                
                if 'prefix' in b_type:
                    type_map[root_text] = 'prefix'
                elif 'suffix' in b_type:
                    type_map[root_text] = 'suffix'
                elif 'root' in b_type and root_text not in type_map:
                    type_map[root_text] = 'root'
    
    # Check if 'enrich' is a root
    if 'enrich' in root_map:
        print(f"'enrich' is a root! Connected words: {root_map['enrich']}")
    
    # Check if 'en' is a word
    words_labeled_en = [w['word'] for w in all_words if w['word'].lower().strip() == 'en']
    if words_labeled_en:
        print(f"'en' is a word! Entries: {words_labeled_en}")

search_anomaly()
