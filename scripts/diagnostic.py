import json
import os
import re

DATA_JS_PATH = r"c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js"

def fix_data():
    try:
        with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
            
        print(f"Content length: {len(content)}")
        
        # Try to find common JSON errors
        # If the file is extremely large, searching via regex might be slow but necessary.
        
        # Check if the end of the file is correct
        tail = content[-100:]
        print(f"File tail: {repr(tail)}")
        
        # Use a more robust split to find the JSON part
        marker = "const WORDS = "
        if marker not in content:
            print("Marker not found")
            return
            
        parts = content.split(marker, 1)
        json_data = parts[1].strip()
        if json_data.endswith(";"):
            json_data = json_data[:-1].strip()
            
        print("Attempting to parse JSON...")
        try:
            data = json.loads(json_data)
            print(f"Successfully parsed! Word count: {len(data)}")
        except json.JSONDecodeError as e:
            print(f"Parse error at line {e.lineno}, col {e.colno}, offset {e.pos}")
            
            # Print surrounding context of error
            start = max(0, e.pos - 50)
            end = min(len(json_data), e.pos + 50)
            print(f"Error context: {repr(json_data[start:end])}")
            
    except Exception as e:
        print(f"Fix failed: {e}")

if __name__ == "__main__":
    fix_data()
