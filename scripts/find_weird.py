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
                    objects.append((start, i, array_str[start:i+1]))
                    last_end = i

    print(f"Parsed {len(objects)} objects")
    
    suspicious_patterns = [
        r'（。', r'（。）', r'（。）」'
    ]
    
    fixed_count = 0
    new_objects = []
    
    for _, _, obj_str in objects:
        original = obj_str
        
        # We need to find the odd occurrences of （。 and replace them.
        # It seems like there's a pattern: "節（。ふし（。）、交点" => "節（ふし）、交点"
        # "火傷（。を（。させる（。" => "火傷（をやけど）させる" ? Or just "火傷をさせる"
        # Actually, "火傷（。を（。させる（。" -> "火傷をさせる"?
        # "熱（。湯を（。かける（。" -> "熱湯をかける"?
        
        # Let's print out what we find first before writing to file.
        has_weird = False
        for p in suspicious_patterns:
            if re.search(p, obj_str):
                has_weird = True
                
        # Also maybe check for other weird stuff: `て（。`
        if '（。' in obj_str:
            has_weird = True

        if has_weird:
            # Let's clean it. But how?
            # It seems the AI outputted `（。` where it probably meant a parenthesis or nothing.
            # "節（。ふし（。）" -> "節（ふし）"
            print(f"-- ORIGINAL -----------\n{obj_str}")
            
            # Replace （。 with ( 
            # OR, if it's "節（。ふし（。）", replacing （。 with （ and ） will be good?
            # Let's just output the original for now to see all of them.
            pass
            
if __name__ == '__main__':
    main()
