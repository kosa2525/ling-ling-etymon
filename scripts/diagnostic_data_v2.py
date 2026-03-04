
import json
import re

def check_data():
    file_path = r"c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Use regex to find all objects in the WORDS array
    # This is safer than json.loads for potentially large or slightly malformed JS files
    entries = []
    # Simplified regex for extracting word objects
    # Note: This might not be perfect but let's try to capture the objects
    # A better way is to split by "}," then try to clean each part
    
    # Actually, let's try a better approach: find all "id": "..." and then look at the surrounding object
    id_matches = re.finditer(r'"id":\s*"([^"]+)"', content)
    
    jp_regex = re.compile(r'[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f]')
    
    results = []
    ids = []
    
    for match in id_matches:
        start = match.start()
        # Find the start of the object {
        obj_start = content.rfind('{', 0, start)
        # Find the end of the object }
        obj_end = content.find('}', start)
        
        if obj_start != -1 and obj_end != -1:
            obj_str = content[obj_start:obj_end+1]
            try:
                # Clean up the string to be valid JSON
                # This is tricky because it's JS, might have trailing commas or different quotes
                # But let's look for "word": "..." directly in the string
                word_match = re.search(r'"word":\s*"([^"]+)"', obj_str)
                word_id = match.group(1)
                ids.append(word_id)
                
                if word_match:
                    word_text = word_match.group(1)
                    if jp_regex.search(word_text):
                        results.append({"id": word_id, "word": word_text})
            except:
                continue

    print(f"Total entries found by ID: {len(ids)}")
    
    from collections import Counter
    counts = Counter(ids)
    duplicates = [item for item, count in counts.items() if count > 1]
    print(f"Duplicates: {duplicates}")
    
    print("\nEntries with Japanese in 'word' field:")
    for r in results:
        print(f"ID: {r['id']}, Word: {r['word']}")

if __name__ == "__main__":
    check_data()
