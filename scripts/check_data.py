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

    def get_objects(s):
        objects = []
        depth = 0
        in_string = False
        escape = False
        start = -1
        
        for i, c in enumerate(s):
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
                        objects.append(s[start:i+1])
        return objects

    objs = get_objects(array_str)
    print(f"Found {len(objs)} objects based on braces.")

    bad_indices = []
    # Japanese characters block check
    japanese_chars = re.compile(r'[\u3040-\u30FF\u4E00-\u9FAF]')
    
    for idx, obj_str in enumerate(objs):
        m = re.search(r'"word"\s*:\s*"([^"]+)"', obj_str)
        if m:
            w = m.group(1)
            if japanese_chars.search(w):
                print(f"Japanese in word field at {idx}: {w}")
                bad_indices.append(idx)
        else:
            print(f"No word field found in obj {idx}")
            bad_indices.append(idx)
            
    # Check the last few entries for JSON syntax validity because the file might be cut off
    for idx in range(max(0, len(objs) - 5), len(objs)):
        obj_str = objs[idx]
        # cleanup
        cleaned = re.sub(r'//.*', '', obj_str)
        cleaned = re.sub(r',\s*}', '}', cleaned)
        cleaned = re.sub(r',\s*]', ']', cleaned)
        try:
            json.loads(cleaned)
        except json.JSONDecodeError as e:
            if idx not in bad_indices:
                print(f"JSON decode error at index {idx}: {e}")
                bad_indices.append(idx)

    print(f"Total bad objects: {len(bad_indices)}")

    # We will also create a fixed version
    if len(bad_indices) > 0:
        valid_objs = [objs[i] for i in range(len(objs)) if i not in bad_indices]
        print(f"Keeping {len(valid_objs)} valid objects.")
        
        # reconstruct data.js
        head_text = text[:match.start(1)]
        new_array_str = "[\n" + ",\n".join(valid_objs) + "\n];\n"
        
        with open('data.js.fixed', 'w', encoding='utf-8') as f:
            f.write(head_text)
            f.write(new_array_str)
        print("Saved fixed data to data.js.fixed")

if __name__ == '__main__':
    main()
