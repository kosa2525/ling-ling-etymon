import re

path = 'c:/Users/integ/OneDrive/デスクトップ/ling-ling-etymon/scripts/subscription_server.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update init_db
table_sql = """
            if DATABASE_URL:
                cur.execute('''CREATE TABLE IF NOT EXISTS user_words 
                                (id SERIAL PRIMARY KEY, word_id TEXT, word_data JSONB, author TEXT, date TEXT, is_deleted BOOLEAN DEFAULT FALSE)''')
            else:
                cur.execute('''CREATE TABLE IF NOT EXISTS user_words 
                                (id INTEGER PRIMARY KEY AUTOINCREMENT, word_id TEXT, word_data TEXT, author TEXT, date TEXT, is_deleted INTEGER DEFAULT 0)''')
"""

if 'CREATE TABLE IF NOT EXISTS user_words' not in content:
    content = content.replace("CREATE TABLE IF NOT EXISTS user_essays", table_sql.strip() + "\n                cur.execute('''CREATE TABLE IF NOT EXISTS user_essays")

# 2. Update submit_word
new_submit_word = """
@app.route('/api/submit-word', methods=['POST'])
def submit_word():
    data = request.json
    username = data.get('username')
    word_payload = data.get('wordData')
    
    if not username or not word_payload:
        return jsonify(status="error", message="Missing data"), 400

    word_payload['author'] = username
    word_payload['date'] = datetime.now().strftime("%Y-%m-%d")
    
    conn = get_db_connection()
    p = get_placeholder()
    try:
        with conn:
            cur = conn.cursor()
            # PostgreSQL requires jsonb, SQLite uses TEXT
            import json
            word_id = word_payload['id']
            author = username
            date_str = word_payload['date']
            json_data = json.dumps(word_payload, ensure_ascii=False)
            
            # Check if exists
            if DATABASE_URL:
                cur.execute(f"SELECT id FROM user_words WHERE word_id={p} AND author={p} AND is_deleted=FALSE", (word_id, author))
            else:
                cur.execute(f"SELECT id FROM user_words WHERE word_id={p} AND author={p} AND is_deleted=0", (word_id, author))
            
            existing = cur.fetchone()
            if existing:
                if DATABASE_URL:
                    cur.execute(f"UPDATE user_words SET word_data={p}::jsonb, date={p} WHERE id={p}", (json_data, date_str, existing[0]))
                else:
                    cur.execute(f"UPDATE user_words SET word_data={p}, date={p} WHERE id={p}", (json_data, date_str, existing[0]))
            else:
                if DATABASE_URL:
                    cur.execute(f"INSERT INTO user_words (word_id, word_data, author, date) VALUES ({p}, {p}::jsonb, {p}, {p})", (word_id, json_data, author, date_str))
                else:
                    cur.execute(f"INSERT INTO user_words (word_id, word_data, author, date) VALUES ({p}, {p}, {p}, {p})", (word_id, json_data, author, date_str))
                    
        notify_followers(username, f"{username} さんが新しい単語を投稿しました：{word_payload['word']}", "archive")
        return jsonify(status="success")
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify(status="error", message=str(e)), 500
    finally:
        conn.close()
"""

# Replace existing submit_word
content = re.sub(r"@app\.route\('/api/submit-word', methods=\['POST'\]\).*?def submit_word\(\).*?(?=@app\.route\('/api/reflections/<word_id>)", new_submit_word + '\n', content, flags=re.DOTALL)

# 3. Add API to fetch all user words
new_api = """
@app.route('/api/user-words', methods=['GET'])
def get_user_words():
    conn = get_db_connection()
    result = []
    try:
        with conn:
            cur = conn.cursor()
            if DATABASE_URL:
                cur.execute("SELECT word_data FROM user_words WHERE is_deleted=FALSE")
            else:
                cur.execute("SELECT word_data FROM user_words WHERE is_deleted=0")
            for row in cur.fetchall():
                import json
                try:
                    wd = row[0] if isinstance(row[0], dict) else json.loads(row[0])
                    result.append(wd)
                except:
                    pass
    except Exception as e:
        print(f"Error fetching user words: {e}")
    finally:
        conn.close()
    return jsonify(result)
"""

if '/api/user-words' not in content:
    content = content.replace("@app.route('/api/submit-essay'", new_api + "\n@app.route('/api/submit-essay'")

# 4. Modify my-delete for words
new_delete = """
        if item_type == 'word':
            conn = get_db_connection()
            p = get_placeholder()
            with conn:
                cur = conn.cursor()
                if DATABASE_URL:
                    cur.execute(f"UPDATE user_words SET is_deleted=TRUE WHERE word_id={p} AND author={p}", (item_id, username))
                else:
                    cur.execute(f"UPDATE user_words SET is_deleted=1 WHERE word_id={p} AND author={p}", (item_id, username))
            conn.close()
            return jsonify(status='success')
"""
content = re.sub(r"        if item_type == 'word':(?:(?!elif item_type == 'essay').)*", new_delete.strip() + "\n            \n", content, flags=re.DOTALL)


# 5. Modify my-posts for words
new_my_posts = """
    # 自分の単語を取得
    conn = get_db_connection()
    p = get_placeholder()
    try:
        with conn:
            cur = conn.cursor()
            if DATABASE_URL:
                cur.execute(f"SELECT id, word_id, word_data, date FROM user_words WHERE author={p} AND is_deleted = FALSE", (username,))
            else:
                cur.execute(f"SELECT id, word_id, word_data, date FROM user_words WHERE author={p} AND is_deleted = 0", (username,))
            for r in cur.fetchall():
                import json
                wd = r[2] if isinstance(r[2], dict) else json.loads(r[2])
                result['words'].append({'id': r[1], 'word': wd.get('word', r[1]), 'date': r[3]})
except Exception as e:
        print(f"Error reading words: {e}")
"""
content = re.sub(r"    # 自分の単語を取得.*?except Exception as e:\n        print\(f\"Error reading words: \{e\}\"\)", new_my_posts.strip() + "\n", content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated API!")
