import json
import re

def fix_data_js():
    file_path = "data.js"
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    # Find where the array starts
    match = re.search(r"const initialNodes = (\[.*)", content, re.DOTALL)
    if not match:
        print("Could not find initialNodes")
        return

    array_str = match.group(1)
    
    # Try to extract valid JSON objects from the string
    # We can try to split by '}, {' or similar, but let's try a regex for the JSON object
    
    # Let's just find the last valid index of '}'
    curr_str = array_str
    
    while curr_str:
        try:
            # try to parse as json. wait, it might end with `];`
            # this is not strictly JSON, it's JS. It might have single quotes or unquoted keys.
            pass
        except Exception as e:
            pass

    print("Checking...")

if __name__ == '__main__':
    fix_data_js()
