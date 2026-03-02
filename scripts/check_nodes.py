
import json
import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()
    match = re.search(r'const\s+WORDS\s*=\s*(\[.*?\])\s*;?\s*$', content, re.DOTALL)
    words = json.loads(match.group(1)) if match else []

for w in words:
    for b in w.get('etymology', {}).get('breakdown', []):
        text = b.get('text', '').lower().replace('-', '').strip()
        if text == 'enrich' or text == 'en':
            print(f"Word {w['word']} text={b.get('text')} type={b.get('type')}")
