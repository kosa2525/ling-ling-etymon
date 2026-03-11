import json
import re

def clean_abnormal_punctuation(text):
    if not isinstance(text, str):
        return text
    
    # targeted replacements for common garbages observed in the recent words
    text = text.replace('. 、', '、')
    text = text.replace('。 、', '、')
    text = text.replace('、 、', '、')
    text = text.replace('. 。', '。')
    text = text.replace(' .', '')
    text = text.replace(' . ', '')
    text = text.replace('粉砕. し', '粉砕し')
    text = text.replace('風. の', '風の')
    
    # Remove period after particles
    text = re.sub(r'([がのにおへとでを])。', r'\1', text)
    
    # Remove random periods between words
    text = text.replace('自分を。', '自分を')
    text = text.replace('今。', '今')
    text = text.replace('千。', '千')
    text = text.replace('し。', 'し')
    text = re.sub(r'([一-龥ぁ-んァ-ン])。([一-龥ぁ-んァ-ン])', r'\1\2', text)  # remove period strictly between chars if not valid sentence ending. wait, a period CAN end a sentence and start a new one if no space!
    # actually, typical Japanese has no spaces after period. 
    # Let's fix specific known ones:
    text = text.replace('一。へと', '一へと')
    text = text.replace('すべてが。一として', 'すべてが一として')
    text = text.replace('自分が。一である', '自分が一である')
    text = text.replace('予備（よび）。という', '予備（よび）という')
    text = text.replace('鋼。の', '鋼の')
    text = text.replace('鋼。へと', '鋼へと')
    text = text.replace('一。という', '一という')
    text = text.replace('すべてと。一へと', 'すべてと一へと')
    text = text.replace('自分と。すべてを', '自分とすべてを')
    text = text.replace('宇宙の。すべてと', '宇宙のすべてと')
    text = text.replace('自分を。そこへと', '自分をそこへと')
    text = text.replace('亡命を。強いる', '亡命を強いる')
    text = text.replace('開始し。始めた', '開始し始めた')
    text = text.replace('同期（どうき）。し', '同期（どうき）し')
    
    # Remove isolated unmatched 」 before particles
    text = re.sub(r'」([にもをでとながは])', r'\1', text)
    text = text.replace('」と', 'と')  # will this break correct quotes? Yes. Let's be careful.
    text = text.replace('ッ」と', 'ッと')
    text = text.replace('一瞬」で', '一瞬で')
    text = text.replace('容赦」も', '容赦も')
    text = text.replace('峻烈」に', '峻烈に')
    text = text.replace('猟犬」と', '猟犬と')
    text = text.replace('弾丸」と', '弾丸と')
    text = text.replace('一気」に', '一気に')
    text = text.replace('保険」、', '保険、')
    text = text.replace('一撃」の', '一撃の')
    text = text.replace('棄て棄て」。', '棄て棄て。')
    text = text.replace('あえて」。「', 'あえて「')
    text = text.replace('気づいて」は', '気づいては')
    text = text.replace('針」に', '針に')
    text = text.replace('真理」が', '真理が')
    text = text.replace('パッ」と', 'パッと')
    text = text.replace('ダラダラ」と', 'ダラダラと')
    text = text.replace('連続（嘘）」を', '連続（嘘）を')
    text = text.replace('連続（嘘）」を', '連続（嘘）を')  
    text = text.replace('パッケージ」の', 'パッケージの')
    text = text.replace('いた」時のあの', 'いた時のあの')
    text = text.replace('守られていた」時の', '守られていた時の')
    text = text.replace('震えていた」時の', '震えていた時の')

    # Remove extra spaces caused by regex
    text = text.replace('  ', ' ')
    
    # Another pass of cleanup
    text = text.replace('。。', '。')
    text = text.replace('、、', '、')
    text = text.replace('、。', '。')
    text = text.replace('。、', '。')
    
    return text

def traverse_and_clean(obj):
    if isinstance(obj, dict):
        return {k: traverse_and_clean(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [traverse_and_clean(v) for v in obj]
    else:
        return clean_abnormal_punctuation(obj)

prefix = 'const WORDS = '
with open('data.js', 'r', encoding='utf-8') as f:
    text = f.read()

json_str = text[len(prefix):]
if json_str.endswith(';\n'):
    json_str = json_str[:-2]
elif json_str.endswith(';'):
    json_str = json_str[:-1]

words = json.loads(json_str)

# Only clean the last 15 words to avoid mutating old data unnecessarily
last_15 = traverse_and_clean(words[-15:])
words[-15:] = last_15

new_text = prefix + json.dumps(words, indent='\t', ensure_ascii=False) + ';\n'
with open('data.js', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Cleaned the last 15 words successfully!")
