import os
import json
import time
import re
from typing import List, Dict
try:
    import openai
except ImportError:
    print("Error: 'openai' library not found.")
    exit(1)

# --- Configuration ---
api_key = os.environ.get("OPENAI_API_KEY", "")
client = openai.OpenAI(api_key=api_key)
DATA_JS_PATH = os.path.join(os.path.dirname(__file__), "..", "data.js")

def get_existing_data() -> List[Dict]:
    if not os.path.exists(DATA_JS_PATH): return []
    with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    if "const WORDS =" in content:
        json_part = content.split("const WORDS =", 1)[1].strip()
        if json_part.endswith(";"): json_part = json_part[:-1].strip()
        return json.loads(json_part)
    return []

def save_data(data: List[Dict]):
    json_str = json.dumps(data, indent=8, ensure_ascii=False)
    with open(DATA_JS_PATH, 'w', encoding='utf-8') as f:
        f.write(f"const WORDS = {json_str};\n")

def process_batch(words: List[str]) -> Dict[str, Dict]:
    prompt = f"""
    Provide the part of speech and a concise Japanese meaning for the following English words.
    Words: {", ".join(words)}
    
    Output ONLY a JSON object where keys are the lowercase words and values are objects containing:
    "pos": "part of speech (noun, verb, adjective, etc.)"
    "meaning": "concise Japanese definition"
    
    Example:
    {{
        "apple": {{"pos": "noun", "meaning": "リンゴ"}},
        "run": {{"pos": "verb", "meaning": "走る"}}
    }}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        response_format={ "type": "json_object" }
    )
    return json.loads(response.choices[0].message.content)

def main():
    all_words = get_existing_data()
    targets = [w for w in all_words if not w.get('meaning') or not w.get('part_of_speech')]
    
    if not targets:
        print("All words already have meaning and part of speech.")
        return

    print(f"Total words to update: {len(targets)}")
    batch_size = 30
    
    for i in range(0, len(targets), batch_size):
        batch = targets[i:i+batch_size]
        batch_word_names = [w['word'] for w in batch]
        print(f"Processing batch {i//batch_size + 1}: {', '.join(batch_word_names)}")
        
        try:
            results = process_batch(batch_word_names)
            
            # Map results back to all_words
            for w in batch:
                lower_name = w['word'].lower()
                if lower_name in results:
                    res = results[lower_name]
                    w['part_of_speech'] = res.get('pos', 'noun')
                    w['meaning'] = res.get('meaning', '--')
                else:
                    # Fallback for case sensitivity or slight mismatch
                    w['part_of_speech'] = 'noun'
                    w['meaning'] = '--'
            
            # Intermediate save
            save_data(all_words)
            print(f"Saved batch {i//batch_size + 1}")
            time.sleep(1)
        except Exception as e:
            print(f"Error processing batch: {e}")
            continue

    print("Migration complete!")

if __name__ == "__main__":
    main()
