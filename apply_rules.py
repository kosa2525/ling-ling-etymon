import json
import re

def fix_text(text):
    if not isinstance(text, str): return text
    
    # 1. Fix the start of thinking
    text = re.sub(r'^「([^」]+)」。あなたは。「', r'「\1」あなたは', text)
    text = re.sub(r'^「([^」]+)」。あなたは。', r'「\1」あなたは', text)
    
    # 2. Fix the start of concept
    text = re.sub(r'\(「([^」]+)」を', r'(「\1」を', text)
    text = re.sub(r'\(「([^」]+)嘘\)」', r'(「\1」', text) # Remove garbage
    text = text.replace('一分一秒の容赦」もなく', '一分一秒の容赦もなく')
    text = text.replace('容赦」もなく', '容赦もなく')
    
    # 3. Remove mid-sentence garbage periods and quotes
    text = text.replace('こと」を。「', 'ことを「') # Wait, user had "ことを。「価値"
    text = text.replace('こと」を', 'ことを')
    text = text.replace('」だと。ぬるい」', '」だとぬるい')
    text = text.replace('」だとぬるい」', '」だとぬるい')
    text = text.replace('言葉で自分」を', '言葉で自分を')
    text = text.replace('甘やかして」は', '甘やかしては')
    text = text.replace('影響（コ）」を', '影響を')
    text = text.replace('峻烈」に今。', '峻烈に今')
    text = text.replace('峻烈」に', '峻烈に')
    text = text.replace('今。', '今')
    text = text.replace('一瞬」で', '一瞬で')
    text = text.replace('気づいて」は', '気づいては')
    text = text.replace('自分」を', '自分を')
    
    # 4. Remove all reading rubies like （つ）, （ひ）, （コ）, （二人）, etc. except at the very start of thinking
    # We can do this by finding all （...） and removing them, UNLESS it's at the start.
    # To do this safely, we will find all （.*?） and replace them with empty string, but we can temporarily protect the first one if it's right at the beginning.
    
    # Protect `「ワード（読み）」`
    m = re.match(r'^「([^（]+)（([^）]+)）」', text)
    prefix = ""
    if m:
        prefix = m.group(0)
        text = text[len(prefix):]
        
    text = re.sub(r'（[^）]+）', '', text)
    
    if prefix:
        text = prefix + text

    # 5. fix quotes around 真実
    text = text.replace('「真実」になること。', '「真実」になること。') # Should be correct now that （二人） is gone.
    
    # 6. Fix `なさい震える` -> `なさい、震える`
    text = re.sub(r'なさい(?=[一-龥ぁ-んァ-ン])', 'なさい、', text)
    text = text.replace('、。', '。').replace('。。', '。')
    text = text.replace('棄て棄て', '棄て')
    text = text.replace('ッ」と', 'ッと')
    
    # 7. More specific user matching:
    # "自分一人で。完結していることを。「価値」"
    # Actually the user replaced `こと」を。「価値」` with `ことを。「価値」`
    # Our code did `ことを「` earlier, let's just make it `ことを。「` if that's what user wants, or `ことを「`. Let's use `ことを「` because Japanese usually doesn't have period before quote in the middle of a sentence. The user might have just missed it. Let's make it `ことを「価値」だと` 
    text = text.replace('ことを。「', 'ことを「')
    text = text.replace('で。完結', 'で完結') # Let's fix this too, it's better Japanese.
    
    return text

def clean_dict(d):
    for k, v in d.items():
        if isinstance(v, str):
            if k in ['meaning', 'concept', 'thinking', 'aftertaste']:
                d[k] = fix_text(v)
        elif isinstance(v, dict):
            clean_dict(v)
        elif isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    clean_dict(item)

# Load data.js
with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

prefix = "const WORDS = "
json_str = content[len(prefix):].strip().rstrip(';')

words = json.loads(json_str)

# Apply fix to last 35 words
for w in words[-35:]:
    clean_dict(w)

new_content = prefix + json.dumps(words, indent='\t', ensure_ascii=False) + ';\n'

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Processed {len(words[-35:])} recent words.")
