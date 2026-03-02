
import json
import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()
    match = re.search(r'const\s+WORDS\s*=\s*(\[.*?\])\s*;?\s*$', content, re.DOTALL)
    words = json.loads(match.group(1)) if match else []

root_map = {}
type_map = {}
for w in words:
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

valid_roots = {r: words_list for r, words_list in root_map.items() if len(words_list) >= 2}

nodes = []
seen_words = set()
for root in valid_roots:
    related_words = valid_roots[root]
    root_id = f"root_{root}"
    r_type = type_map.get(root, 'root')
    
    nodes.append({
        "id": root_id, 
        "label": root, 
        "group": r_type
    })
    
    for rw in related_words:
        if rw not in seen_words:
            nodes.append({
                "id": rw, 
                "label": rw, 
                "group": "word"
            })
            seen_words.add(rw)

with open('nodes_dump.json', 'w', encoding='utf-8') as f:
    json.dump(nodes, f, ensure_ascii=False, indent=2)

print("Nodes dumped to nodes_dump.json")
