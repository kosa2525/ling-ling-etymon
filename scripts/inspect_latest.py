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
    print(f"Data length after last valid object: {len(array_str) - last_end}")
    
    if len(array_str) - last_end > 10:
        remainder = array_str[last_end+1:]
        print("\nRemainder of file:")
        print(remainder[:200])
        
    # We will reconstruct the file perfectly up to the last valid object
    print("\nReconstructing file...")
    head_text = text[:match.start(1)]
    valid_obj_strs = [o[2] for o in objects]
    
    # Actually wait, maybe some valid objects inside the list are corrupted. 
    # The user says "新しく登録してもらったものの中に、内容がおかしいものが散見される。"
    # This means there are multiple WEIRD objects completely parsed as valid JS but semantically wrong.
    # For example, what did the user add recently? Energy or motion words? (from chat history)
    # Let's check the last 50 objects and print their words and meanings to see what's weird.
    
    print("\nLast 30 objects:")
    for idx, (s, e, obj_str) in enumerate(objects[-30:]):
        # clean and parse
        cleaned = re.sub(r'//.*', '', obj_str)
        cleaned = re.sub(r',\s*}', '}', cleaned)
        cleaned = re.sub(r',\s*]', ']', cleaned)
        try:
            parsed = json.loads(cleaned)
            print(f"- {parsed.get('word', '?')}: {parsed.get('meaning', '?')}")
        except:
            print(f"- [UNPARSEABLE] {obj_str[:50]}...")
            
if __name__ == '__main__':
    main()
