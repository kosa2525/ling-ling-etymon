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
    
    # Extract the JSON part between [ and ]
    # Note: data.js is 'const WORDS = [...];'
    words_match = re.search(r"const WORDS = (\[.*\]);", content_js, re.DOTALL)
    if not words_match:
        print("Error: Could not find WORDS array in data.js")
        return
    
    existing_words_raw = json.loads(words_match.group(1))
    existing_ids = {w["id"].lower() for w in existing_words_raw if "id" in w}
    
    # 2. Read new words from newdate.txt (from line 12768)
    print("Reading newdate.txt...")
    with open(newdate_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Line 12768 is index 12767
    new_content = "".join(lines[12767:])
    
    # Extract objects { ... }
    matches = re.findall(r"\{[\s\n]*\"id\":.*?\}", new_content, re.DOTALL)
    
    newly_added = []
    skipped_duplicates = []
    
    print(f"Found {len(matches)} potential objects in newdate.txt")
    
    for m in matches:
        # Clean up trailing commas if any inside the match for json.loads
        # This is a bit tricky, but let's try basic json.loads first
        try:
            # Basic cleanup for common non-strict JSON issues
            m_clean = m.strip()
            if m_clean.endswith(","):
                m_clean = m_clean[:-1]
            
            obj = json.loads(m_clean)
            word_id = obj.get("id", "").lower()
            
            if word_id and word_id not in existing_ids:
                newly_added.append(obj)
                existing_ids.add(word_id)
            else:
                skipped_duplicates.append(word_id)
        except Exception as e:
            # Try a more lenient parse if needed, but for now just report
            continue

    print(f"New unique words to add: {len(newly_added)}")
    print(f"Skipped duplicates: {len(skipped_duplicates)}")
    
    if not newly_added:
        print("No new unique words to add.")
        return

    # 3. Update data.js
    # We append to the existing list and rewrite
    updated_words = existing_words_raw + newly_added
    
    # Format with indentation matching data.js (2 tabs or 8 spaces? standard seems to be 2 tabs/8 spaces in your file)
    # Looking at data.js head, it uses tabs.
    new_words_json = json.dumps(updated_words, indent="\t", ensure_ascii=False)
    
    new_js_content = f"const WORDS = {new_words_json};\n"
    
    with open(data_js_path, "w", encoding="utf-8") as f:
        f.write(new_js_content)
    
    print("Successfully updated data.js")

if __name__ == "__main__":
    extract_and_deduplicate()
