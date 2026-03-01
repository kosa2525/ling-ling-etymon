import json
import os
import sys
import re

DATA_JS_PATH = os.path.join(os.path.dirname(__file__), "..", "data.js")

def merge_data(new_data_list):
    if not os.path.exists(DATA_JS_PATH):
        print(f"Error: {DATA_JS_PATH} not found.")
        return

    with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'const\s+WORDS\s*=\s*(\[.*\])', content, re.DOTALL)
    if not match:
        print("Error: Could not find WORDS array in data.js")
        return

    try:
        existing_list = json.loads(match.group(1))
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from data.js: {e}")
        return

    # Map by id (lowercase) for quick lookup/update
    words_dict = {w['id'].lower(): w for w in existing_list}

    added = 0
    updated = 0
    for item in new_data_list:
        item_id = item['id'].lower()
        if item_id in words_dict:
            words_dict[item_id] = item
            updated += 1
        else:
            words_dict[item_id] = item
            added += 1

    # Re-build sorted list
    final_list = list(words_dict.values())
    final_list.sort(key=lambda x: x['word'].lower())

    with open(DATA_JS_PATH, 'w', encoding='utf-8') as f:
        f.write(f"const WORDS = {json.dumps(final_list, indent=8, ensure_ascii=False)};\n")
    
    print(f"Merged successfully: Added {added}, Updated {updated}.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python merge_gpt_data.py <path_to_new_json_file>")
        sys.exit(1)
    
    json_path = sys.argv[1]
    with open(json_path, 'r', encoding='utf-8') as f:
        new_data = json.load(f)
    
    merge_data(new_data)
