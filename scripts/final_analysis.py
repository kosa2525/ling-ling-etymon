
import re
import collections

def analyze():
    content = open(r'c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js', 'r', encoding='utf-8').read()
    
    # regexes
    jp_re = re.compile(r'[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f]')
    id_re = re.compile(r'\"id\":\s*\"([^\"]+)\"')
    word_re = re.compile(r'\"word\":\s*\"([^\"]+)\"')
    concept_re = re.compile(r'\"concept\":')
    
    ids = []
    jp_words = []
    broken = []
    
    for match in id_re.finditer(content):
        word_id = match.group(1)
        ids.append(word_id)
        
        # approximate object boundaries
        obj_start = content.rfind('{', 0, match.start())
        obj_end = content.find('}', match.start())
        
        if obj_start != -1 and obj_end != -1:
            obj_str = content[obj_start:obj_end+1]
            
            if concept_re.search(obj_str):
                broken.append(word_id)
            
            wm = word_re.search(obj_str)
            if wm:
                w_txt = wm.group(1)
                if jp_re.search(w_txt):
                    jp_words.append((word_id, w_txt))
                    
    counts = collections.Counter(ids)
    dupes = [x for x in counts if counts[x] > 1]
    
    print(f'Total IDs: {len(ids)}')
    print(f'Duplicates: {dupes}')
    print(f'Broken entries (with "concept"): {len(broken)}')
    print(f'Japanese words ({len(jp_words)}):')
    for jid, jw in jp_words:
        print(f'  {jid}: {jw}')

if __name__ == "__main__":
    analyze()
