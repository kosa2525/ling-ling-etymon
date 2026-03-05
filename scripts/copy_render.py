import json
import re

file_path = 'data_render.js'
out_path = 'data.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

try:
    m = re.search(r'const WORDS = (\[.*\]);', content, re.DOTALL)
    if m:
        words = json.loads(m.group(1))
        print(f"Valid JSON! It contains {len(words)} words.")
        
        # Override data.js
        with open(out_path, 'w', encoding='utf-8') as out:
            out.write(content)
        print("Successfully copied data_render.js to data.js")
    else:
        print("Could not find WORDS array.")
except Exception as e:
    print(f"Error parsing JSON: {e}")
