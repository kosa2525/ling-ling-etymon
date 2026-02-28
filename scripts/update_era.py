import os
import json
import re
import sys
from openai import OpenAI
import time

API_KEY = os.environ.get("OPENAI_API_KEY")
if not API_KEY:
    print("No OPENAI_API_KEY set.")
    sys.exit(1)

client = OpenAI(api_key=API_KEY)
DATA_PATH = r"c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js"

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const\s+WORDS\s*=\s*(\[.*\])\s*;?\s*$', text, re.DOTALL)
if not m:
    print("Could not find WORDS in data.js")
    sys.exit(1)

words = json.loads(m.group(1))
missing = [w for w in words if "era" not in w]

print(f"Total words missing era: {len(missing)}")

BATCH_SIZE = 100
for i in range(0, len(missing), BATCH_SIZE):
    batch = missing[i:i+BATCH_SIZE]
    batch_words = [w["word"] for w in batch]
    print(f"Processing batch {i//BATCH_SIZE+1}, {len(batch)} words...")
    
    prompt = "For the following words, provide their etymological origin era in exactly the following format: WORD | ERA\n"
    prompt += "Use standard eras like: PIE origin, Ancient Greek, Latin, 12th Century, 15th Century, etc.\n\n"
    prompt += "\n".join(batch_words)
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0
        )
        content = response.choices[0].message.content
        lines = content.strip().split('\n')
        era_map = {}
        for line in lines:
            parts = line.split('|')
            if len(parts) == 2:
                era_map[parts[0].strip().lower()] = parts[1].strip()
        
        for w in batch:
            era = era_map.get(w["word"].lower(), "Unknown Era")
            w["era"] = era
            
    except Exception as e:
        print(f"Error on batch: {e}")
        time.sleep(1)

new_json = json.dumps(words, indent=4, ensure_ascii=False)
new_text = text[:m.start(1)] + new_json + text[m.end(1):]

with open(DATA_PATH, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Finished updating data.js")
