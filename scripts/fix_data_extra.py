
import re

def fix_data():
    file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Dictionary of translations
    translations = {
        'incur': ('"word": "(負債・危険などを)招く、負う"', '"word": "Incur"'),
        'second': ('"word": "2番目の、秒"', '"word": "Second"')
    }

    for word_id, (old_word, new_word) in translations.items():
        # Find the block for this ID and replace the word
        pattern = re.compile(r'\"id\":\s*\"' + word_id + r'\",\s*' + re.escape(old_word), re.MULTILINE)
        content = pattern.sub(f'"id": "{word_id}",\n\t\t{new_word}', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Successfully updated incur and second in data.js")

if __name__ == "__main__":
    fix_data()
