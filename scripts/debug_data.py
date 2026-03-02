import json
import re

with open(r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()
    match = re.search(r'WORDS\s*=\s*(\[.*\])', content, re.DOTALL)
    words = json.loads(match.group(1))

anomalies = []
for w in words:
    word = w.get('word', '').strip()
    for b in w.get('etymology', {}).get('breakdown', []):
        morpheme = b.get('text', '').replace('-', '').strip()
        if len(morpheme) > len(word):
            anomalies.append((word, morpheme, b.get('type')))

print(f"Found {len(anomalies)} anomalies: {anomalies}")
