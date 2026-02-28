import json
import os

DATA_JS_PATH = 'data.js'

def check():
    if not os.path.exists(DATA_JS_PATH):
        print("data.js not found")
        return
    with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    
    if "const WORDS =" in content:
        json_part = content.split("const WORDS =", 1)[1].strip()
        if json_part.endswith(";"):
            json_part = json_part[:-1].strip()
        data = json.loads(json_part)
        
        total = len(data)
        missing = [w['word'] for w in data if not w.get('meaning') or not w.get('part_of_speech')]
        
        print(f"Total words in data.js: {total}")
        print(f"Words missing info: {len(missing)}")
        if missing:
            print(f"Sample missing: {', '.join(missing[:10])}")

if __name__ == "__main__":
    check()
