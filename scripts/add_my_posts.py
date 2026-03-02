import os, re

path = 'c:/Users/integ/OneDrive/デスクトップ/ling-ling-etymon/scripts/subscription_server.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

new_api = """
@app.route('/api/my-posts', methods=['GET'])
def get_my_posts():
    username = request.args.get('username')
    if not username:
        return jsonify(status='error', message='Missing username'), 400
    
    result = {'words': [], 'essays': [], 'reflections': []}
    
    # 自分の単語を取得
    try:
        with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
            data_content = f.read()
        match = re.search(r'const\s+WORDS\s*=\s*(\[.*?\])\s*;?\s*$', data_content, re.DOTALL)
        if match:
            existing_words = json.loads(match.group(1))
            result['words'] = [w for w in existing_words if w.get('author') == username]
    except Exception as e:
        print(f"Error reading words: {e}")

    # 自分のエッセイとリフレクションを取得
    conn = get_db_connection()
    p = get_placeholder()
    try:
        with conn:
            cur = conn.cursor()
            
            # Essays
            if DATABASE_URL:
                cur.execute(f"SELECT id, title, date FROM user_essays WHERE author={p} AND is_deleted = FALSE", (username,))
            else:
                cur.execute(f"SELECT id, title, date FROM user_essays WHERE author={p} AND is_deleted = 0", (username,))
            for r in cur.fetchall():
                result['essays'].append({'id': f"essay_user_{r[0]}", 'db_id': r[0], 'title': r[1], 'date': r[2]})
                
            # Reflections
            if DATABASE_URL:
                cur.execute(f"SELECT id, word_id, content, date FROM reflections WHERE username={p} AND is_deleted = FALSE", (username,))
            else:
                cur.execute(f"SELECT id, word_id, content, date FROM reflections WHERE username={p} AND is_deleted = 0", (username,))
            for r in cur.fetchall():
                result['reflections'].append({'id': r[0], 'word_id': r[1], 'content': r[2][:50] + '...' if len(r[2])>50 else r[2], 'date': r[3]})
                
    except Exception as e:
        print(f"Database error in my-posts: {e}")
    finally:
        conn.close()
        
    return jsonify(result)

@app.route('/api/my-delete', methods=['POST'])
def delete_my_post():
    data = request.json
    username = data.get('username')
    item_type = data.get('type')
    item_id = data.get('id')
    
    if not username or not item_type or not item_id:
        return jsonify(status='error', message='Missing data'), 400
        
    try:
        if item_type == 'word':
            # 単語の削除
            with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
                data_content = f.read()
            match = re.search(r'const\s+WORDS\s*=\s*(\[.*?\])\s*;?\s*$', data_content, re.DOTALL)
            if match:
                existing_words = json.loads(match.group(1))
                new_words = [w for w in existing_words if not (w.get('id') == item_id and w.get('author') == username)]
                
                with open(DATA_JS_PATH, 'w', encoding='utf-8') as f:
                    f.write(f"const WORDS = {json.dumps(new_words, indent=8, ensure_ascii=False)};\\n")
            return jsonify(status='success')
            
        elif item_type == 'essay':
            db_id = int(str(item_id).replace('essay_user_', ''))
            conn = get_db_connection()
            p = get_placeholder()
            with conn:
                cur = conn.cursor()
                if DATABASE_URL:
                    cur.execute(f"UPDATE user_essays SET is_deleted=TRUE WHERE id={p} AND author={p}", (db_id, username))
                else:
                    cur.execute(f"UPDATE user_essays SET is_deleted=1 WHERE id={p} AND author={p}", (db_id, username))
            conn.close()
            return jsonify(status='success')
            
        elif item_type == 'reflection':
            conn = get_db_connection()
            p = get_placeholder()
            with conn:
                cur = conn.cursor()
                if DATABASE_URL:
                    cur.execute(f"UPDATE reflections SET is_deleted=TRUE WHERE id={p} AND username={p}", (item_id, username))
                else:
                    cur.execute(f"UPDATE reflections SET is_deleted=1 WHERE id={p} AND username={p}", (item_id, username))
            conn.close()
            return jsonify(status='success')
            
        return jsonify(status='error', message='Invalid type'), 400
    except Exception as e:
        return jsonify(status='error', message=str(e)), 500
"""

content = content.replace("@app.route('/api/tts'", new_api + "\n@app.route('/api/tts'")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated!")
