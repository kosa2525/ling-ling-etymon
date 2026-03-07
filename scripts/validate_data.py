import json
import re

def main():
    with open('data.js', 'r', encoding='utf-8', errors='replace') as f:
        text = f.read()

    # Find where the array starts
    match = re.search(r"const initialNodes = (\[.*)", text, re.DOTALL)
    if not match:
        print("Could not find initialNodes")
        return

    array_str = match.group(1)
    
    # We will try to parse using ast.literal_eval or json if we clean it up, but it's JS.
    # Let's write a simple chunker that counts objects
    
    # Just grab all the IDs and words using regex to detect broken ones
    # An entry usually starts with:
    # {
    #   "id": "...",
    #   "word": "...",
    #   ...
    
    # Let's compile a list of all nodes based on the curly braces, this is safer.
    import ast
    
    # We can use chomp method to extract complete braces.
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
    
    # Check each object for errors
    bad_indices = []
    japanese_chars = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]')
    
    for idx, obj_str in enumerate(objs):
        # We can try to json parse it after some cleanup
        # JS object keys might be unquoted, or have trailing commas
        cleaned = re.sub(r'//.*', '', obj_str)
        cleaned = re.sub(r',\s*}', '}', cleaned)
        cleaned = re.sub(r',\s*]', ']', cleaned)
        try:
            parsed = json.loads(cleaned)
            # check if it has japanese in word
            word = parsed.get("word", "")
            if japanese_chars.search(word):
                print(f"Warning: Japanese characters found in word at index {idx}: {word}")
                bad_indices.append(idx)
        except json.JSONDecodeError as e:
            # Maybe keys are not quoted
            print(f"JSON decode error at index {idx}, obj length {len(obj_str)}: {e}")
            bad_indices.append(idx)
            
    print(f"Total bad indices found: {len(bad_indices)}")

if __name__ == '__main__':
    main()
