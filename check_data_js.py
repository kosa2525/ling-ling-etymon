import json
import re

def check_json():
    with open('data.js', 'r', encoding='utf-8') as f:
        text = f.read()
    
    prefix = 'const WORDS = '
    if not text.startswith(prefix):
        print("Invalid file prefix")
        return
    
    js_content = text[len(prefix):].strip()
    if js_content.endswith(';'):
        js_content = js_content[:-1]
    
    try:
        json.loads(js_content)
        print("JSON is valid!")
    except json.JSONDecodeError as e:
        print(f"JSON is invalid: {e.msg} at line {e.lineno} col {e.colno}")
        # Print snippet around the error
        lines = js_content.splitlines()
        if e.lineno-1 < len(lines):
            print(f"Error line: {lines[e.lineno-1]}")

check_json()
