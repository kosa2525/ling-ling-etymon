
import json
import re

def check_data():
    file_path = r"c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract the WORDS array
    match = re.search(r"const WORDS = (\[.*\]);", content, re.DOTALL)
    if not match:
        print("Could not find WORDS array in data.js")
        return

    try:
        words = json.loads(match.group(1))
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        # Try to find common JSON errors like trailing commas
        return

    ids = set()
    duplicates = []
    japanese_words = []
    japanese_ids = []
    single_quote_ids = []
    missing_fields = []

    jp_regex = re.compile(r'[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f]')

    for entry in words:
        word_id = entry.get("id")
        word_text = entry.get("word")

        if not word_id:
            missing_fields.append({"entry": entry, "field": "id"})
            continue

        if word_id in ids:
            duplicates.append(word_id)
        ids.add(word_id)

        if word_text and jp_regex.search(word_text):
            japanese_words.append(entry)
        
        if word_id and jp_regex.search(word_id):
            japanese_ids.append(entry)

        if word_id and "'" in word_id:
            single_quote_ids.append(word_id)

        if not word_text:
            missing_fields.append({"id": word_id, "field": "word"})

    print(f"Total words: {len(words)}")
    print(f"Duplicates: {duplicates}")
    print(f"IDs with single quotes: {single_quote_ids}")
    print(f"Entries with Japanese in 'word': {[w.get('id') for w in japanese_words]}")
    print(f"Entries with Japanese in 'id': {[w.get('id') for w in japanese_ids]}")
    
    if japanese_words:
        print("\nJapanese words entries:")
        for w in japanese_words:
            print(f"ID: {w.get('id')}, Word: {w.get('word')}")

if __name__ == "__main__":
    check_data()
