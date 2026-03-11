import json
import re

def clean_text(text):
    if not isinstance(text, str):
        return text
    
    # Repeated symbols
    text = re.sub(r'。{2,}', '。', text)
    text = re.sub(r'、{2,}', '、', text)
    text = re.sub(r'・{2,}', '・', text)
    text = re.sub(r'\.{2,}', '.', text)
    text = re.sub(r'!{2,}', '!', text)
    text = re.sub(r'\?{2,}', '?', text)
    
    # Combined Japanese punctuation
    text = re.sub(r'。、', '。', text)
    text = re.sub(r'、。', '。', text)
    
    # Empty brackets
    text = text.replace('()', '')
    text = text.replace('（）', '')
    text = text.replace('「」', '')
    text = text.replace('『』', '')
    text = text.replace('【】', '')
    
    # Punctuation at the start of strings
    text = re.sub(r'^[。、・\.\s]+', '', text)
    
    # Fix odd quote fragments from previous bad edits
    text = text.replace('峻烈」に『。', '峻烈に')
    text = text.replace('一撃」で', '一撃で')
    text = text.replace('書き」換え', '書き換え')
    
    # Clean up double periods or spaces
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    return text

def traverse_and_clean(obj):
    if isinstance(obj, dict):
        return {k: traverse_and_clean(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [traverse_and_clean(v) for v in obj]
    else:
        return clean_text(obj)

def run_cleanup():
    input_file = 'data.js'
    prefix = 'const WORDS = '
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.startswith(prefix):
        print("Invalid file prefix")
        return
        
    js_content = content[len(prefix):].strip()
    if js_content.endswith(';'):
        js_content = js_content[:-1]
    
    data = json.loads(js_content)
    print(f"Loaded {len(data)} entries.")
    
    cleaned_data = traverse_and_clean(data)
    
    # Use standard format for data.js
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(prefix)
        # Using indent='\t' to match the typical manual style
        f.write(json.dumps(cleaned_data, ensure_ascii=False, indent='\t'))
        f.write(';')
    
    print("Cleanup complete.")

if __name__ == "__main__":
    run_cleanup()
