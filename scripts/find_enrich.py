
import json
import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()
    # Find Enrich object
    match = re.search(r'\{[^{}]*"word":\s*"Enrich"[^{}]*\}', content, re.DOTALL)
    if match:
        print(match.group(0))
    else:
        # Maybe case-insensitive?
        match = re.search(r'\{[^{}]*"word":\s*"enrich"[^{}]*\}', content, re.DOTALL | re.IGNORECASE)
        if match:
             print(match.group(0))
        else:
            print("Not found")
