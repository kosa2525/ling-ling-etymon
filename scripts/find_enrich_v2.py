
import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()
    # Find Enrich object accurately
    # Match id, word, etc.
    words = re.findall(r'\{[^{}]*"word":\s*"[^"]*enrich[^"]*"[^{}]*\}', content, re.DOTALL | re.IGNORECASE)
    for word in words:
        print(word)
