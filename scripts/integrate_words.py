import json
import re
import os

def extract_and_deduplicate():
    newdate_path = r"c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\newdate.txt"
    data_js_path = r"c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js"
    
    # 1. Read existing words from data.js
    print("Reading data.js...")
    with open(data_js_path, "r", encoding="utf-8") as f:
        content_js = f.read()
    
    words_match = re.search(r"const WORDS = (\[.*\]);", content_js, re.DOTALL)
    if not words_match:
        print("Error: Could not find WORDS array in data.js")
        return
    
    existing_words_raw = json.loads(words_match.group(1))
    existing_ids = {w["id"].lower() for w in existing_words_raw if "id" in w}
    print(f"Current words in data.js: {len(existing_words_raw)}")
    
    # 2. Read new words from newdate.txt (from line 12768)
    print("Reading newdate.txt...")
    with open(newdate_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    new_content = "".join(lines[12767:])
    
    # Extract objects using JSONDecoder for robustness with nested structures
    decoder = json.JSONDecoder()
    pos = 0
    newly_added = []
    skipped_duplicates = []
    errors = 0
    
    while pos < len(new_content):
        # Look for the start of an object
        match = re.search(r'\{[\s\n]*"id":', new_content[pos:])
        if not match:
            break
            
        start_index = pos + match.start()
        try:
            obj, end_index = decoder.raw_decode(new_content[start_index:])
            pos = start_index + end_index
            
            word_id = obj.get("id", "").lower()
            if word_id and word_id not in existing_ids:
                newly_added.append(obj)
                existing_ids.add(word_id)
            else:
                skipped_duplicates.append(word_id)
        except json.JSONDecodeError:
            errors += 1
            pos = start_index + 1
            continue

    print(f"Found {len(newly_added) + len(skipped_duplicates) + errors} potential objects in newdate.txt")
    print(f"New unique words to add: {len(newly_added)}")
    print(f"Skipped duplicates: {len(skipped_duplicates)}")
    if errors:
        print(f"Errors occurred during parsing: {errors}")
    
    if not newly_added:
        print("No new unique words to add.")
        return

    # 3. Update data.js
    updated_words = existing_words_raw + newly_added
    
    # Using tabs for alignment as in original file
    new_words_json = json.dumps(updated_words, indent="\t", ensure_ascii=False)
    new_js_content = f"const WORDS = {new_words_json};\n"
    
    with open(data_js_path, "w", encoding="utf-8") as f:
        f.write(new_js_content)
    
    print(f"Successfully updated data.js. New total: {len(updated_words)}")

if __name__ == "__main__":
    extract_and_deduplicate()
