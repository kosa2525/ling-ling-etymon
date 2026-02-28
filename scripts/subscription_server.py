from flask import Flask, jsonify, request, redirect, url_for, send_from_directory
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import stripe
import os
import json
import re
from datetime import datetime
import random
import hashlib
try:
    import psycopg2
    from psycopg2.extras import DictCursor
except ImportError:
    psycopg2 = None

# アプリケーションの初期化
app = Flask(__name__, static_folder='../')
CORS(app)

# --- 設定 ---
# 環境変数から取得（Renderの設定画面で入力）
stripe.api_key = os.environ.get("STRIPE_API_KEY", "")
PRICE_ID = os.environ.get("STRIPE_PRICE_ID", "")
DOMAIN = os.environ.get("DOMAIN", "http://localhost:5000")
# DATABASE_URL があれば PostgreSQL (Supabase等) を使用、なければ SQLite
DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASE_SQLITE = os.path.join(os.path.dirname(__file__), 'users.db')
DATA_JS_PATH = os.path.join(os.path.dirname(__file__), '..', 'data.js')
ESSAYS_JS_PATH = os.path.join(os.path.dirname(__file__), '..', 'essays.js')

def get_db_connection():
    if DATABASE_URL:
        # PostgreSQL
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    else:
        # SQLite
        import sqlite3
        conn = sqlite3.connect(DATABASE_SQLITE)
        return conn

def get_placeholder():
    return "%s" if DATABASE_URL else "?"

# --- データベース初期化 ---
def init_db():
    conn = get_db_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                if DATABASE_URL:
                    cur.execute('''CREATE TABLE IF NOT EXISTS users 
                                    (username TEXT PRIMARY KEY, password TEXT, is_premium BOOLEAN DEFAULT FALSE, is_operator BOOLEAN DEFAULT FALSE)''')
                    cur.execute('''CREATE TABLE IF NOT EXISTS reflections 
                                    (id SERIAL PRIMARY KEY, word_id TEXT, username TEXT, content TEXT, date TEXT, is_deleted BOOLEAN DEFAULT FALSE)''')
                    cur.execute('''CREATE TABLE IF NOT EXISTS replies 
                                    (id SERIAL PRIMARY KEY, reflection_id INTEGER, username TEXT, content TEXT, date TEXT, is_deleted BOOLEAN DEFAULT FALSE)''')
                    cur.execute('''CREATE TABLE IF NOT EXISTS reports 
                                    (id SERIAL PRIMARY KEY, reporter TEXT, target_username TEXT, target_type TEXT, target_id INTEGER, reason TEXT, date TEXT, status TEXT DEFAULT 'pending')''')
                    cur.execute('''CREATE TABLE IF NOT EXISTS blocks 
                                    (blocker TEXT, blocked TEXT, PRIMARY KEY (blocker, blocked))''')
                    cur.execute('''CREATE TABLE IF NOT EXISTS hidden_items 
                                    (username TEXT, target_type TEXT, target_id INTEGER, PRIMARY KEY (username, target_type, target_id))''')
                    cur.execute('''CREATE TABLE IF NOT EXISTS follows 
                                    (follower TEXT, followed TEXT, PRIMARY KEY (follower, followed))''')
                    cur.execute('''CREATE TABLE IF NOT EXISTS notifications 
                                    (id SERIAL PRIMARY KEY, username TEXT, type TEXT, message TEXT, link TEXT, date TEXT, is_read BOOLEAN DEFAULT FALSE)''')
                    cur.execute('''CREATE TABLE IF NOT EXISTS user_essays 
                                    (id SERIAL PRIMARY KEY, title TEXT, content TEXT, author TEXT, date TEXT, is_deleted BOOLEAN DEFAULT FALSE)''')
                else:
                    cur.execute('''CREATE TABLE IF NOT EXISTS users 
                                    (username TEXT PRIMARY KEY, password TEXT, is_premium BOOLEAN DEFAULT 0, is_operator BOOLEAN DEFAULT 0)''')
                    cur.execute('''CREATE TABLE IF NOT EXISTS reflections 
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT, word_id TEXT, username TEXT, content TEXT, date TEXT, is_deleted INTEGER DEFAULT 0)''')
                    cur.execute('''CREATE TABLE IF NOT EXISTS replies 
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT, reflection_id INTEGER, username TEXT, content TEXT, date TEXT, is_deleted INTEGER DEFAULT 0)''')
                    cur.execute('''CREATE TABLE IF NOT EXISTS reports 
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT, reporter TEXT, target_username TEXT, target_type TEXT, target_id INTEGER, reason TEXT, date TEXT, status TEXT DEFAULT 'pending')''')
                    cur.execute('''CREATE TABLE IF NOT EXISTS blocks 
                                    (blocker TEXT, blocked TEXT, PRIMARY KEY (blocker, blocked))''')
                    cur.execute('''CREATE TABLE IF NOT EXISTS hidden_items 
                                    (username TEXT, target_type TEXT, target_id INTEGER, PRIMARY KEY (username, target_type, target_id))''')
                    cur.execute('''CREATE TABLE IF NOT EXISTS follows 
                                    (follower TEXT, followed TEXT, PRIMARY KEY (follower, followed))''')
                    cur.execute('''CREATE TABLE IF NOT EXISTS notifications 
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, type TEXT, message TEXT, link TEXT, date TEXT, is_read INTEGER DEFAULT 0)''')
                    cur.execute('''CREATE TABLE IF NOT EXISTS user_essays 
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT, author TEXT, date TEXT, is_deleted INTEGER DEFAULT 0)''')
                
                # スキーマの自動アップグレード（カラムが足りない場合に追加）
                if DATABASE_URL:
                    cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name='users'")
                    columns = [row[0] for row in cur.fetchall()]
                    if 'is_operator' not in columns:
                        cur.execute("ALTER TABLE users ADD COLUMN is_operator BOOLEAN DEFAULT FALSE")
                    if 'is_premium' not in columns:
                        cur.execute("ALTER TABLE users ADD COLUMN is_premium BOOLEAN DEFAULT FALSE")
                    
                    # Reflections migration (more robust)
                    cur.execute("SELECT count(*) FROM information_schema.columns WHERE table_name='reflections' AND column_name='is_deleted'")
                    if cur.fetchone()[0] == 0:
                        cur.execute("ALTER TABLE reflections ADD COLUMN is_deleted BOOLEAN DEFAULT FALSE")
                        
                    # Replies migration (more robust)
                    cur.execute("SELECT count(*) FROM information_schema.columns WHERE table_name='replies' AND column_name='is_deleted'")
                    if cur.fetchone()[0] == 0:
                        cur.execute("ALTER TABLE replies ADD COLUMN is_deleted BOOLEAN DEFAULT FALSE")
                else:
                    cur.execute("PRAGMA table_info(users)")
                    columns = [row[1] for row in cur.fetchall()]
                    if 'is_operator' not in columns:
                        cur.execute("ALTER TABLE users ADD COLUMN is_operator INTEGER DEFAULT 0")
                    if 'is_premium' not in columns:
                        cur.execute("ALTER TABLE users ADD COLUMN is_premium INTEGER DEFAULT 0")
                    
                    # SQLite migration
                    cur.execute("PRAGMA table_info(reflections)")
                    cols_ref = [row[1] for row in cur.fetchall()]
                    if 'is_deleted' not in cols_ref:
                        cur.execute("ALTER TABLE reflections ADD COLUMN is_deleted INTEGER DEFAULT 0")
                    
                    cur.execute("PRAGMA table_info(replies)")
                    cols_rep = [row[1] for row in cur.fetchall()]
                    if 'is_deleted' not in cols_rep:
                        cur.execute("ALTER TABLE replies ADD COLUMN is_deleted INTEGER DEFAULT 0")

    finally:
        conn.close()
init_db()

# --- ユーティリティ ---
def is_operator(username):
    # 環境変数のOPERATORS（カンマ区切り）に含まれているか、DBのフラグを確認
    operators_env = os.environ.get("OPERATORS", "").split(",")
    if username in operators_env:
        return True
    
    conn = get_db_connection()
    p = get_placeholder()
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT is_operator FROM users WHERE username={p}", (username,))
            res = cur.fetchone()
    conn.close()
    return bool(res[0]) if res else False

# --- アカウント・UGC管理機能 ---

@app.route('/api/delete-account', methods=['POST'])
def delete_account():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    conn = get_db_connection()
    p = get_placeholder()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT password FROM users WHERE username={p}", (username,))
                user = cur.fetchone()
                if user and check_password_hash(user[0], password):
                    cur.execute(f"DELETE FROM users WHERE username={p}", (username,))
                    # 関連データも消す場合はここで追加
                    return jsonify(status="success")
    finally:
        conn.close()
    return jsonify(status="error", message="認証に失敗しました"), 401

@app.route('/api/report', methods=['POST'])
def report_item():
    data = request.json
    conn = get_db_connection()
    p = get_placeholder()
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO reports (reporter, target_username, target_type, target_id, reason, date, status) VALUES ({p}, {p}, {p}, {p}, {p}, {p}, {p})",
                         (data['reporter'], data['target_username'], data['target_type'], data['target_id'], data['reason'], datetime.now().strftime("%Y-%m-%d %H:%M"), 'pending'))
    conn.close()
    return jsonify(status="success")

@app.route('/api/block', methods=['POST'])
def block_user():
    data = request.json
    conn = get_db_connection()
    p = get_placeholder()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO blocks (blocker, blocked) VALUES ({p}, {p})",
                             (data['blocker'], data['blocked']))
    except:
        pass # 既にブロック済み
    finally:
        conn.close()
    return jsonify(status="success")

@app.route('/api/hide', methods=['POST'])
def hide_item():
    data = request.json
    conn = get_db_connection()
    p = get_placeholder()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO hidden_items (username, target_type, target_id) VALUES ({p}, {p}, {p})",
                             (data['username'], data['target_type'], data['target_id']))
    except:
        pass
    finally:
        conn.close()
    return jsonify(status="success")

@app.route('/api/blocked-users', methods=['GET'])
def get_blocked_users():
    username = request.args.get('username')
    conn = get_db_connection()
    p = get_placeholder()
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT blocked FROM blocks WHERE blocker={p}", (username,))
            res = cur.fetchall()
            return jsonify([row[0] for row in res])

@app.route('/api/unblock', methods=['POST'])
def unblock_user():
    data = request.json
    conn = get_db_connection()
    p = get_placeholder()
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"DELETE FROM blocks WHERE blocker={p} AND blocked={p}", (data['blocker'], data['blocked']))
    conn.close()
    return jsonify(status="success")

@app.route('/api/hidden-items', methods=['GET'])
def get_hidden_items():
    username = request.args.get('username')
    conn = get_db_connection()
    p = get_placeholder()
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT target_type, target_id FROM hidden_items WHERE username={p}", (username,))
            res = cur.fetchall()
            return jsonify([{"type": row[0], "id": row[1]} for row in res])

@app.route('/api/unhide', methods=['POST'])
def unhide_item():
    data = request.json
    conn = get_db_connection()
    p = get_placeholder()
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"DELETE FROM hidden_items WHERE username={p} AND target_type={p} AND target_id={p}", (data['username'], data['target_type'], data['target_id']))
    conn.close()
    return jsonify(status="success")

@app.route('/api/follow', methods=['POST'])
def follow_user():
    data = request.json
    conn = get_db_connection()
    p = get_placeholder()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO follows (follower, followed) VALUES ({p}, {p})", (data['follower'], data['followed']))
                # 通知を追加
                add_notification(data['followed'], 'follow', f"{data['follower']}さんがあなたをフォローしました。", f"/profile/{data['follower']}")
    except Exception as e:
        print(f"Follow error: {e}")
    conn.close()
    return jsonify(status="success")

@app.route('/api/unfollow', methods=['POST'])
def unfollow_user():
    data = request.json
    conn = get_db_connection()
    p = get_placeholder()
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"DELETE FROM follows WHERE follower={p} AND followed={p}", (data['follower'], data['followed']))
    conn.close()
    return jsonify(status="success")

@app.route('/api/follows', methods=['GET'])
def get_follows():
    username = request.args.get('username')
    conn = get_db_connection()
    p = get_placeholder()
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT followed FROM follows WHERE follower={p}", (username,))
            res = cur.fetchall()
            return jsonify([row[0] for row in res])

def add_notification(username, n_type, message, link):
    conn = get_db_connection()
    p = get_placeholder()
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO notifications (username, type, message, link, date, is_read) VALUES ({p}, {p}, {p}, {p}, {p}, {p})",
                         (username, n_type, message, link, datetime.now().strftime("%Y-%m-%d %H:%M"), False if DATABASE_URL else 0))
    conn.close()

def notify_followers(followed_user, message, link):
    conn = get_db_connection()
    p = get_placeholder()
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT follower FROM follows WHERE followed={p}", (followed_user,))
            followers = cur.fetchall()
            for f in followers:
                add_notification(f[0], 'new_post', message, link)
    conn.close()

@app.route('/api/notifications', methods=['GET'])
def get_notifications():
    username = request.args.get('username')
    conn = get_db_connection()
    p = get_placeholder()
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT id, type, message, link, date, is_read FROM notifications WHERE username={p} ORDER BY date DESC LIMIT 20", (username,))
            res = cur.fetchall()
            return jsonify([{"id":r[0], "type":r[1], "message":r[2], "link":r[3], "date":r[4], "is_read":bool(r[5])} for r in res])

@app.route('/api/notifications/read', methods=['POST'])
def mark_read():
    data = request.json
    conn = get_db_connection()
    p = get_placeholder()
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"UPDATE notifications SET is_read={p} WHERE id={p}", (True if DATABASE_URL else 1, data['id']))
    conn.close()
    return jsonify(status="success")

@app.route('/api/submit-essay', methods=['POST'])
def submit_essay():
    data = request.json
    username = data.get('username')
    
    # 有料会員チェック
    conn = get_db_connection()
    p = get_placeholder()
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT is_premium FROM users WHERE username={p}", (username,))
            user = cur.fetchone()
            if not user or not user[0]:
                return jsonify(status="error", message="エッセイ投稿にはPremium会員である必要があります。"), 403
            
            cur.execute(f"INSERT INTO user_essays (title, content, author, date) VALUES ({p}, {p}, {p}, {p})",
                         (data['title'], data['content'], username, datetime.now().strftime("%Y-%m-%d")))
    conn.close()
    
    notify_followers(username, f"{username} さんが新しいエッセイを投稿しました：{data['title']}", "essays")
    return jsonify(status="success")

@app.route('/api/user-essays', methods=['GET'])
def get_user_essays():
    conn = get_db_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, title, content, author, date FROM user_essays WHERE is_deleted IS NOT TRUE ORDER BY date DESC")
            res = cur.fetchall()
            return jsonify([{"id":f"u_{r[0]}", "title":r[1], "content":r[2], "author":r[3], "date":r[4]} for r in res])

# --- オペレーター向け管理 API ---

@app.route('/api/admin/reports', methods=['GET'])
def get_reports():
    admin_user = request.args.get('username')
    if not is_operator(admin_user):
        return jsonify(status="error", message="Unauthorized"), 403
    
    conn = get_db_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM reports WHERE status='pending' ORDER BY date DESC")
            reports = cur.fetchall()
            result = []
            for r in reports:
                # DBのカラムに合わせてマッピング
                result.append({
                    "id": r[0], "reporter": r[1], "target_username": r[2],
                    "target_type": r[3], "target_id": r[4], "reason": r[5], "date": r[6]
                })
    conn.close()
    return jsonify(result)

@app.route('/api/admin/delete-content', methods=['POST'])
def admin_delete_content():
    data = request.json
    admin_user = data.get('admin_username')
    if not is_operator(admin_user):
        return jsonify(status="error", message="Unauthorized"), 403
    
    target_type = data.get('target_type') # 'reflection' or 'reply'
    target_id = data.get('target_id')
    report_id = data.get('report_id')

    conn = get_db_connection()
    p = get_placeholder()
    with conn:
        with conn.cursor() as cur:
            table = "reflections" if target_type == "reflection" else "replies"
            cur.execute(f"UPDATE {table} SET is_deleted={p} WHERE id={p}", (True, target_id))
            if report_id:
                cur.execute(f"UPDATE reports SET status={p} WHERE id={p}", ('resolved', report_id))
    conn.close()
    return jsonify(status="success")

# --- アプリ（フロントエンド）の配信 ---
@app.route('/')
def serve_app():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/data.js')
def serve_data():
    return send_from_directory(os.path.dirname(DATA_JS_PATH), 'data.js')

@app.route('/essays.js')
def serve_essays():
    # essays.jsが存在しない場合は空の配列を返す
    if not os.path.exists(ESSAYS_JS_PATH):
        return "const ESSAYS = [];", 200, {'Content-Type': 'application/javascript'}
    return send_from_directory(os.path.dirname(ESSAYS_JS_PATH), 'essays.js')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# --- ログイン・登録 API ---
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # パスワードを暗号化（ハッシュ化）
    hashed_password = generate_password_hash(password)
    
    try:
        conn = get_db_connection()
        p = get_placeholder()
        with conn:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO users VALUES ({p}, {p}, {p})", (username, hashed_password, False))
        conn.close()
        return jsonify(status="success")
    except Exception as e:
        print(f"Register error: {e}")
        return jsonify(status="error", message="そのユーザー名は既に使われています。"), 400

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    conn = get_db_connection()
    p = get_placeholder()
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT password, is_premium FROM users WHERE username={p}", (username,))
            user = cur.fetchone()
    conn.close()
    
    if user:
        stored_hash = user[0]
        # 保存されているハッシュと入力されたパスワードを比較
        if check_password_hash(stored_hash, password):
            # オペレーターかどうかも取得
            conn = get_db_connection()
            p = get_placeholder()
            with conn:
                with conn.cursor() as cur:
                    cur.execute(f"SELECT is_operator FROM users WHERE username={p}", (username,))
                    res = cur.fetchone()
            conn.close()
            return jsonify(status="success", is_premium=bool(user[1]), is_operator=bool(res[0]) if res else False)
    
    return jsonify(status="error", message="ユーザー名またはパスワードが違います。"), 401

# --- Stripe 決済 API ---
@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    username = request.args.get('username')
    if not username:
        return jsonify(error="ログインが必要です"), 401
    
    try:
        checkout_session = stripe.checkout.Session.create(
            mode='subscription',
            payment_method_types=['card'],
            line_items=[{'price': PRICE_ID, 'quantity': 1}],
            success_url=f"{DOMAIN}?session_id={{CHECKOUT_SESSION_ID}}&user={username}",
            cancel_url=DOMAIN,
        )
        return jsonify(id=checkout_session.id)
    except Exception as e:
        return jsonify(error=str(e)), 403

@app.route('/check-subscription', methods=['GET'])
def check_subscription():
    session_id = request.args.get('session_id')
    username = request.args.get('user')
    
    if not session_id or not username:
        return jsonify(status='unpaid')

    try:
        session = stripe.checkout.Session.retrieve(session_id)
        if session.payment_status == 'paid':
            conn = get_db_connection()
            p = get_placeholder()
            with conn:
                with conn.cursor() as cur:
                    cur.execute(f"UPDATE users SET is_premium={p} WHERE username={p}", (True, username))
            conn.close()
            return jsonify(status='paid')
    except Exception as e:
        print(f"Checkout check failed: {e}")
    
    return jsonify(status='unpaid')

@app.route('/api/submit-word', methods=['POST'])
def submit_word():
    data = request.json
    username = data.get('username')
    word_payload = data.get('wordData')
    
    if not username or not word_payload:
        return jsonify(status="error", message="Missing data"), 400

    data_js_path = DATA_JS_PATH
    try:
        with open(data_js_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        match = re.search(r'const\s+WORDS\s*=\s*(\[.*?\])\s*;?\s*$', content, re.DOTALL)
        if match:
            existing_words = json.loads(match.group(1))
        else:
            existing_words = []

        word_payload['author'] = username
        word_payload['date'] = datetime.now().strftime("%Y-%m-%d")
        
        new_list = [w for w in existing_words if w['id'] != word_payload['id']]
        new_list.append(word_payload)
        
        with open(data_js_path, 'w', encoding='utf-8') as f:
            f.write(f"const WORDS = {json.dumps(new_list, indent=8, ensure_ascii=False)};\n")
        
        notify_followers(username, f"{username} さんが新しい単語を投稿しました：{word_payload['word']}", "archive")
        return jsonify(status="success")
    except Exception as e:
        return jsonify(status="error", message=str(e)), 500

@app.route('/api/reflections/<word_id>', methods=['GET'])
def get_reflections(word_id):
    current_user = request.args.get('username')
    conn = get_db_connection()
    p = get_placeholder()
    
    # ブロックしているユーザーと非表示アイテムのリストを取得
    blocked_users = []
    hidden_refs = []
    hidden_reps = []
    if current_user:
        with conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT blocked FROM blocks WHERE blocker={p}", (current_user,))
                blocked_users = [row[0] for row in cur.fetchall()]
                cur.execute(f"SELECT target_id, target_type FROM hidden_items WHERE username={p}", (current_user,))
                for row in cur.fetchall():
                    if row[1] == 'reflection': hidden_refs.append(row[0])
                    else: hidden_reps.append(row[0])

    with conn:
        with conn.cursor() as cur:
            # is_deleted が False(0) のものだけ取得
            cur.execute(f"SELECT id, username, content, date FROM reflections WHERE word_id={p} AND (is_deleted IS NULL OR is_deleted = {p})", (word_id, False if DATABASE_URL else 0))
            reflections = cur.fetchall()
            result = []
            for r in reflections:
                # ブロックしているユーザーや非表示にした投稿を除外
                if r[1] in blocked_users or r[0] in hidden_refs: continue
                
                cur.execute(f"SELECT id, username, content, date FROM replies WHERE reflection_id={p} AND (is_deleted IS NULL OR is_deleted = {p})", (r[0], False if DATABASE_URL else 0))
                replies = cur.fetchall()
                filtered_replies = []
                for rep in replies:
                    if rep[1] in blocked_users or rep[0] in hidden_reps: continue
                    filtered_replies.append({"id": rep[0], "username": rep[1], "content": rep[2], "date": rep[3]})

                result.append({
                    "id": r[0],
                    "username": r[1],
                    "content": r[2],
                    "date": r[3],
                    "replies": filtered_replies
                })
    conn.close()
    return jsonify(result)

@app.route('/api/user-essays', methods=['GET'])
def get_user_essays():
    conn = get_db_connection()
    result = []
    try:
        with conn:
            with conn.cursor() as cur:
                if DATABASE_URL:
                    cur.execute("SELECT id, title, content, author, date FROM user_essays WHERE is_deleted = FALSE")
                else:
                    cur.execute("SELECT id, title, content, author, date FROM user_essays WHERE is_deleted = 0")
                rows = cur.fetchall()
                for r in rows:
                    result.append({"id": f"essay_user_{r[0]}", "title": r[1], "content": r[2], "author": r[3], "date": r[4]})
    finally:
        conn.close()
    return jsonify(result)

@app.route('/api/submit-essay', methods=['POST'])
def submit_essay():
    data = request.json
    username = data.get('username')
    title = data.get('title')
    content = data.get('content')
    if not username or not title or not content:
        return jsonify(status="error", message="Missing fields")
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    conn = get_db_connection()
    p = get_placeholder()
    try:
        with conn:
            with conn.cursor() as cur:
                if DATABASE_URL:
                    cur.execute(f"INSERT INTO user_essays (title, content, author, date) VALUES ({p}, {p}, {p}, {p}) RETURNING id",
                                 (title, content, username, date_str))
                    new_id = cur.fetchone()[0]
                else:
                    cur.execute(f"INSERT INTO user_essays (title, content, author, date) VALUES ({p}, {p}, {p}, {p})",
                                 (title, content, username, date_str))
                    new_id = cur.lastrowid
        return jsonify(status="success", id=f"essay_user_{new_id}")
    except Exception as e:
        return jsonify(status="error", message=str(e))
    finally:
        conn.close()

@app.route('/api/reflections', methods=['POST'])
def post_reflection():
    data = request.json
    word_id = data.get('word_id')
    username = data.get('username')
    content = data.get('content')
    target_author = data.get('target_author')
    word_name = data.get('word_name', word_id)

    conn = get_db_connection()
    p = get_placeholder()
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO reflections (word_id, username, content, date) VALUES ({p}, {p}, {p}, {p})",
                         (word_id, username, content, datetime.now().strftime("%Y-%m-%d %H:%M")))
            
            # 著者に通知
            if target_author and target_author != username:
                add_notification(target_author, 'reflection', f"{username} さんがあなたの投稿「{word_name}」に思索を残しました。", f"/word/{word_id}")
                
    conn.close()
    return jsonify(status="success")

@app.route('/api/replies', methods=['POST'])
def post_reply():
    data = request.json
    conn = get_db_connection()
    p = get_placeholder()
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO replies (reflection_id, username, content, date) VALUES ({p}, {p}, {p}, {p})",
                         (data['reflection_id'], data['username'], data['content'], datetime.now().strftime("%Y-%m-%d %H:%M")))
    conn.close()
    return jsonify(status="success")

@app.route('/api/tts', methods=['POST'])
def get_tts():
    data = request.json
    text = data.get('text')
    username = data.get('username')
    
    # プレミアム確認
    conn = get_db_connection()
    p = get_placeholder()
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT is_premium FROM users WHERE username={p}", (username,))
            res = cur.fetchone()
    conn.close()
    if not res or not res[0]:
        return jsonify(status="error", message="Premium required"), 403

    if not text:
        return jsonify(status="error", message="No text provided"), 400

    try:
        # キャッシュの確認
        text_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
        cache_dir = os.path.join(os.path.dirname(__file__), 'tts_cache')
        os.makedirs(cache_dir, exist_ok=True)
        cache_path = os.path.join(cache_dir, f"{text_hash}.mp3")

        if os.path.exists(cache_path):
            with open(cache_path, 'rb') as f:
                return f.read(), 200, {'Content-Type': 'audio/mpeg'}

        from openai import OpenAI
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        # 'echo' voice is a deep, calm male voice
        response = client.audio.speech.create(
            model="tts-1",
            voice="echo", 
            input=text[:4000] # Limit length
        )
        
        # 結果をキャッシュに保存
        with open(cache_path, 'wb') as f:
            f.write(response.content)
            
        return response.content, 200, {'Content-Type': 'audio/mpeg'}
    except Exception as e:
        return jsonify(status="error", message=str(e)), 500

@app.route('/api/word-network', methods=['GET'])
def get_word_network():
    mode = request.args.get('mode', 'global') # 'global' or 'personal'
    username = request.args.get('username')
    
    try:
        with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'const\s+WORDS\s*=\s*(\[.*?\])\s*;?\s*$', content, re.DOTALL)
            all_words = json.loads(match.group(1)) if match else []

        if mode == 'personal' and username:
            saved_ids = request.args.get('ids', '').split(',')
            words = [w for w in all_words if w['id'] in saved_ids]
        else:
            # パフォーマンスと「新しさ」のため最新を優先
            words = all_words[-300:]
        
        # 語根(root)や接頭辞(prefix)ごとに単語をグループ化
        root_map = {}
        type_map = {} # パーツがrootかprefixか保持
        for w in words:
            for b in w.get('etymology', {}).get('breakdown', []):
                b_type = b.get('type', '').lower()
                if 'root' in b_type or 'prefix' in b_type:
                    root_text = b.get('text', '').lower().replace('-', '').strip()
                    if not root_text: continue
                    if root_text not in root_map: root_map[root_text] = []
                    root_map[root_text].append(w['word'])
                    
                    if 'prefix' in b_type:
                        type_map[root_text] = 'prefix'
                    elif 'root' in b_type and root_text not in type_map:
                        type_map[root_text] = 'root'
        
        # 繋がり（2つ以上登録されているもの）がある語根だけを抽出
        valid_roots = {r: words_list for r, words_list in root_map.items() if len(words_list) >= 2}
        
        # 該当する語根が多すぎる場合はランダムに選ぶ
        root_keys = list(valid_roots.keys())
        limit = 200 if mode == 'personal' else 500
        if len(root_keys) > limit:
            root_keys = random.sample(root_keys, limit)
        # ネットワーク用データ（ノードとエッジ）
        nodes = []
        edges = []
        seen_words = set()
        
        for root in root_keys:
            related_words = valid_roots[root]
            root_id = f"root_{root}"
            r_type = type_map.get(root, 'root')
            
            nodes.append({
                "id": root_id, 
                "label": root, 
                "group": r_type, 
                "title": f"{r_type.capitalize()}: {root} (Connected to {len(related_words)} words)"
            })
            
            for rw in related_words:
                if rw not in seen_words:
                    nodes.append({
                        "id": rw, 
                        "label": rw, 
                        "group": "word",
                        "title": f"Word: {rw}"
                    })
                    seen_words.add(rw)
                edges.append({"from": root_id, "to": rw})
                    
        return jsonify(nodes=nodes, edges=edges)
    except Exception as e:
        return jsonify(status="error", message=str(e)), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print(f"--- ling-ling-etymon サーバー起動中 ---")
    print(f"ポート: {port}")
    app.run(host='0.0.0.0', port=port, debug=False)
