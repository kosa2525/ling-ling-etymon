
import json
import re

count = 0
with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()
    # Find all "id": "..."
    ids = re.findall(r'"id":', content)
    print(len(ids))
