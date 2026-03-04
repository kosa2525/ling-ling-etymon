
import re

def fix_data():
    file_path = r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix jibe duplicate
    # Pattern to match the specific stub entry
    jibe_stub_pattern = re.compile(r'\t\{\s*\"id\":\s*\"jibe\",\s*\"word\":\s*\"Jibe\",\s*\"part_of_speech\":\s*\"verb\",\s*\"meaning\":\s*\"一致する、調和する\",\s*\"core\":\s*\"パズルの破片がカチリと噛み合うような、矛盾のない統合\",\s*\"era\":\s*\"Unknown Era\"\s*\},', re.MULTILINE)
    content = jibe_stub_pattern.sub('', content)

    # Dictionary of translations
    translations = {
        'specific': ('"word": "明確な、具体的な、特定の、スペシフィック"', '"word": "Specific"'),
        'doctor': ('"word": "医者、博士、ドクター"', '"word": "Doctor"'),
        'doctrine': ('"word": "教義、主義、ドクトリン"', '"word": "Doctrine"'),
        'document': ('"word": "文書、記録、ドキュメント"', '"word": "Document"'),
        'format': ('"word": "形式、フォーマット"', '"word": "Format"'),
        'deform': ('"word": "変形させる、奇形にする"', '"word": "Deform"'),
        'gene': ('"word": "遺伝子"', '"word": "Gene"'),
        'general': ('"word": "一般的な、大将、ジェネラル"', '"word": "General"'),
        'local': ('"word": "地元の、局所的な、ローカル"', '"word": "Local"'),
        'magnificent': ('"word": "壮大な、素晴らしい、マグニフィセント"', '"word": "Magnificent"'),
        'master': ('"word": "主人、達人、マスター、支配する"', '"word": "Master"'),
        'dismal': ('"word": "陰鬱な、みじめな"', '"word": "Dismal"'),
        'bonus': ('"word": "ボーナス、特別手当、思いがけない贈り物"', '"word": "Bonus"'),
        'matter': ('"word": "物質、事態、問題、重要である"', '"word": "Matter"'),
        'material': ('"word": "材料、物質の"', '"word": "Material"'),
        'paternal': ('"word": "父親の、父方"', '"word": "Paternal"'),
        'maternal': ('"word": "母親の、母方の"', '"word": "Maternal"')
    }

    for word_id, (old_word, new_word) in translations.items():
        # Find the block for this ID and replace the word
        pattern = re.compile(r'\"id\":\s*\"' + word_id + r'\",\s*' + re.escape(old_word), re.MULTILINE)
        content = pattern.sub(f'"id": "{word_id}",\n\t\t{new_word}', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Successfully updated data.js")

if __name__ == "__main__":
    fix_data()
