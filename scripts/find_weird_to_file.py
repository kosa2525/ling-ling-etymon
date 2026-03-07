import sys
import json
import re

def main():
    with open('data.js', 'r', encoding='utf-8', errors='replace') as f:
        text = f.read()

    match = re.search(r"const WORDS = (\[.*)", text, re.DOTALL)
    if not match:
        print("Could not find const WORDS")
        return

    array_str = match.group(1)

    objects = []
    depth = 0
    in_string = False
    escape = False
    start = -1
    last_end = -1
    
    for i, c in enumerate(array_str):
        if escape:
            escape = False
            continue
        if c == '\\':
            escape = True
            continue
            
        if c == '"':
            in_string = not in_string
            continue
            
        if not in_string:
            if c == '{':
                if depth == 0:
                    start = i
                depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0 and start != -1:
                    objects.append(array_str[start:i+1])
                    last_end = i

    weird_count = 0
    with open('weird.txt', 'w', encoding='utf-8') as fout:
        for obj_idx, obj_str in enumerate(objects[-50:]): # wait, check all objects
            pass
            
        for obj_idx, obj_str in enumerate(objects):
            if '（。' in obj_str or '（ ）' in obj_str or '（。）」' in obj_str:
                fout.write(f"Index {obj_idx}\n{obj_str}\n---\n")
                weird_count += 1
                
    print(f"Found {weird_count} weird objects.")

if __name__ == '__main__':
    main()
