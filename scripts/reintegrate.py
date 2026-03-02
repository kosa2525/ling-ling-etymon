import json
import re

def extract_json_arrays(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Extract JSON arrays [...]
    # The format in newdate.txt seems to be multiple [ {...}, {...} ] arrays
    matches = re.finditer(r'\[\s*{.*?}\s*\]', content, re.DOTALL)
    all_words = []
    for match in matches:
        try:
            words = json.loads(match.group(0))
            if isinstance(words, list):
                all_words.extend(words)
        except:
            continue
    return all_words

def integrate():
    new_words = extract_json_arrays('../newdate.txt')
    print(f"Extracted {len(new_words)} words from newdate.txt")
    
    with open('../data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_marker = 'const WORDS = '
    end_marker = '];'
    start_idx = content.find(start_marker) + len(start_marker)
    end_idx = content.rfind(end_marker) + 1
    
    if start_idx == -1 or end_idx == -1:
        print("Could not find WORDS array in data.js")
        return
    
    words_json = content[start_idx:end_idx]
    try:
        existing_words = json.loads(words_json)
    except Exception as e:
        print(f"Failed to parse existing words: {e}")
        return

    print(f"Existing words count: {len(existing_words)}")
    
    existing_ids = {w['id'] for w in existing_words if 'id' in w}
    added_count = 0
    for w in new_words:
        w_id = w.get('id')
        if w_id and w_id not in existing_ids:
            existing_words.append(w)
            existing_ids.add(w_id)
            added_count += 1
    
    print(f"Added {added_count} new words.")
    
    # Sort by word name
    existing_words.sort(key=lambda x: x.get('word', '').lower())
    
    new_words_json = json.dumps(existing_words, ensure_ascii=False, indent=4)
    new_content = content[:start_idx] + new_words_json + content[end_idx:]
    
    with open('../data.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Final word count: {len(existing_words)}")

if __name__ == "__main__":
    integrate()
