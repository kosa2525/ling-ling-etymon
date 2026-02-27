import os
import re
import json

DATA_JS_PATH = r"c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js"

def get_existing_data():
    if not os.path.exists(DATA_JS_PATH): return "NOT FOUND"
    try:
        with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"Content length: {len(content)}")
        array_match = re.search(r'const\s+WORDS\s*=\s*(.*);\s*$', content.strip(), re.DOTALL)
        if array_match:
            data_str = array_match.group(1).split('=', 1)[-1].strip() if 'const WORDS =' not in array_match.group(1) else array_match.group(1).replace('const WORDS =', '').strip()
            # Let's try simpler regex
            array_match_simple = re.search(r'const\s+WORDS\s*=\s*(\[.*\])', content, re.DOTALL)
            if array_match_simple:
                print("Simple match found")
                return len(json.loads(array_match_simple.group(1)))
            return "MATCH FAILED"
    except Exception as e:
        return f"ERROR: {e}"
    return "UNKNOWN"

print(get_existing_data())
