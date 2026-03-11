import json
import re

def clean_text_advanced(text):
    if not isinstance(text, str):
        return text

    # Remove the reading parentheses in thinking/concept/aftertaste texts
    # e.g., （つ）, （ひ）, （コ）, （二人）
    # But wait, we might just want to remove all （.*） ?
    # Let's remove them:
    text = re.sub(r'（[^）]+）', '', text)
    text = re.sub(r'\([^)]+\)', '', text)
    
    # 」。あなたは。「 -> 」あなたは
    text = text.replace('」。あなたは。「', '」あなたは')
    text = text.replace('」。あなたは', '」あなたは')
    text = text.replace('」あなたは。「', '」あなたは')
    text = text.replace('」あなたは', '」あなたは')
    text = text.replace('」は。「', '」は')

    # こと」を。「価値」だと。ぬるい」言葉で自分」を甘やかして」はいませんか。 
    text = text.replace('」を。「', 'を。「')
    text = text.replace('」だと。ぬるい」', '」だとぬるい')
    text = text.replace('」だとぬるい」', '」だとぬるい')
    text = text.replace('言葉で自分」を', '言葉で自分を')
    text = text.replace('甘やかして」はいませんか', '甘やかしてはいませんか')
    
    # Remove all lone 」 that don't match a 「 
    # Actually, just removing 」 that appear indiscriminately.
    # We can do targeted:
    text = text.replace('峻烈」に', '峻烈に')
    text = text.replace('今。引き受け', '今引き受け')
    text = text.replace('一瞬」で', '一瞬で')
    text = text.replace('スーーーッ」と', 'スーーーッと')
    text = text.replace('ガツンッ」と', 'ガツンッと')
    text = text.replace('パッ」と', 'パッと')
    text = text.replace('気づいて」は', '気づいては')
    text = text.replace('自分」を', '自分を')
    text = text.replace('今。', '今')
    text = text.replace('すべてが。', 'すべてが')
    text = text.replace('自分が。', '自分が')
    text = text.replace('」。', '」')
    text = text.replace('。「', '「')
    text = text.replace('。という', 'という')
    text = text.replace('こと」を', 'ことを')
    text = text.replace('こと」が', 'ことが')
    text = text.replace('こと」は', 'ことは')
    text = text.replace('こと」で', 'ことで')
    
    # なさい震える -> なさい、震える
    text = re.sub(r'なさい(?=[一-龥ぁ-んァ-ン])', 'なさい、', text)

    # Some missed periods
    text = text.replace('。へと', 'へと')
    text = text.replace('に。', 'に')
    text = text.replace('で。', 'で')
    text = text.replace('の。', 'の')
    text = text.replace('を。', 'を')
    text = text.replace('て。', 'て')
    text = text.replace('と。', 'と')
    text = text.replace('は。', 'は')
    text = text.replace('が。', 'が')
    text = text.replace('も。', 'も')
    text = text.replace('し。', 'し')
    
    # After doing particles + period, we might have fixed '自分一人で。完結' to '自分一人で完結'
    # Wait, the user's example had: 「自分一人で。完結していることを。「価値」
    # So the user kept `で。`? "あなたは自分一人で。完結していることを。"
    # No, look at the user's desired:
    # "「コバリアンス」あなたは自分一人で。完結していることを。「価値」だとぬるい言葉で自分を甘やかしてはいませんか。"
    # "連れ出しなさい。" 
    # "あなたがすべての凄絶な影響を峻烈に今引き受けなさい、震えることは最強です。"
    # Let me just clean up ALL the weird punctuation that breaks Japanese grammar. The user says "そういった処理をしてください" (Do that kind of processing).
    
    text = text.replace('「「', '「')
    text = text.replace('」」', '」')
    
    # Let's clean up orphaned brackets
    text = text.replace('「', '')
    text = text.replace('」', '')
    text = text.replace('『', '')
    text = text.replace('』', '')
    
    # Wait, if we remove ALL brackets, that might be too much. But the texts have random quotes everywhere.
    # Let's restore the quotes for "word" and exact concepts if possible?
    # No, user explicitly had: 「コバリアンス」あなたは... を「価値」だと... 「真実」になること。
    
    return text

# Let's do a smarter approach for quotes
def smart_clean(text):
    if not isinstance(text, str): return text
    
    # Drop ruby and parenthesis annotations
    text = re.sub(r'（[^）]+）', '', text)
    text = re.sub(r'\([^)]+\)', '', text)
    
    # Remove periods following particles (except for specific intentional pauses, but usually they are typos here)
    text = re.sub(r'(て|に|を|は|が|の|と|で|も|へ|し|な)\。', r'\1', text)
    
    # Fix broken quotes 」。あなたは。「 -> 」あなたは
    text = text.replace('」。あなたは。「', '」あなたは')
    text = text.replace('」。あなたは', '」あなたは')
    text = text.replace('」あなたは。「', '」あなたは')
    text = text.replace('」あなたは', '」あなたは')
    
    # Clean up excess 」 and 「
    text = text.replace('」を。「', '」を「')
    text = text.replace('」だ', 'だ')
    text = text.replace('」言葉', '言葉')
    text = text.replace('自分」', '自分')
    text = text.replace('甘やかして」', '甘やかして')
    text = text.replace('峻烈」に', '峻烈に')
    text = text.replace('一瞬」で', '一瞬で')
    text = text.replace('ッ」と', 'ッと')
    text = text.replace('気づいて」は', '気づいては')
    text = text.replace('今。', '今')
    text = text.replace('なさい(?![、。])', 'なさい、')
    text = re.sub(r'なさい(?=[一-龥ぁ-んァ-ン])', 'なさい、', text)
    text = text.replace('棄て棄て', '棄て')
    text = text.replace('。。', '。')
    text = text.replace('、、', '、')
    text = text.replace('。、', '。')
    text = text.replace('、。', '。')
    
    # Removing unbalanced quotes is tough using regex. Let's just remove all lonely quotes.
    # Actually, the user's example kept 「コバリアンス」, 「価値」, and 「真実」.
    
    return text

# Let's write a script to just process the data.
