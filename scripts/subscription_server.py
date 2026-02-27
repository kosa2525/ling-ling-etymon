from flask import Flask, jsonify, request, redirect, url_for, send_from_directory
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import stripe
import sqlite3
import os
import json
import re
from datetime import datetime

# アプリケーションの初期化
app = Flask(__name__, static_folder='../')
CORS(app)

# --- 設定 ---
# 環境変数から取得（Renderの設定画面で入力）
stripe.api_key = os.environ.get("STRIPE_API_KEY", "")
PRICE_ID = os.environ.get("STRIPE_PRICE_ID", "")
DOMAIN = os.environ.get("DOMAIN", "http://localhost:5000")
DATABASE = os.path.join(os.path.dirname(__file__), 'users.db')
DATA_JS_PATH = os.path.join(os.path.dirname(__file__), '..', 'data.js')
ESSAYS_JS_PATH = os.path.join(os.path.dirname(__file__), '..', 'essays.js')

# --- データベース初期化 ---
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users 
                        (username TEXT PRIMARY KEY, password TEXT, is_premium BOOLEAN)''')
        conn.execute('''CREATE TABLE IF NOT EXISTS reflections 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, word_id TEXT, username TEXT, content TEXT, date TEXT)''')
        conn.execute('''CREATE TABLE IF NOT EXISTS replies 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, reflection_id INTEGER, username TEXT, content TEXT, date TEXT)''')
init_db()

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
        with sqlite3.connect(DATABASE) as conn:
            conn.execute("INSERT INTO users VALUES (?, ?, ?)", (username, hashed_password, False))
        return jsonify(status="success")
    except Exception as e:
        return jsonify(status="error", message="そのユーザー名は既に使われています。"), 400

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    with sqlite3.connect(DATABASE) as conn:
        user = conn.execute("SELECT password, is_premium FROM users WHERE username=?", 
                            (username,)).fetchone()
    
    if user:
        stored_hash = user[0]
        # 保存されているハッシュと入力されたパスワードを比較
        if check_password_hash(stored_hash, password):
            return jsonify(status="success", is_premium=bool(user[1]))
    
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
            with sqlite3.connect(DATABASE) as conn:
                conn.execute("UPDATE users SET is_premium=? WHERE username=?", (True, username))
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
            
        return jsonify(status="success")
    except Exception as e:
        return jsonify(status="error", message=str(e)), 500

@app.route('/api/reflections/<word_id>', methods=['GET'])
def get_reflections(word_id):
    with sqlite3.connect(DATABASE) as conn:
        reflections = conn.execute("SELECT id, username, content, date FROM reflections WHERE word_id=?", (word_id,)).fetchall()
        result = []
        for r in reflections:
            replies = conn.execute("SELECT username, content, date FROM replies WHERE reflection_id=?", (r[0],)).fetchall()
            result.append({
                "id": r[0],
                "username": r[1],
                "content": r[2],
                "date": r[3],
                "replies": [{"username": rep[0], "content": rep[1], "date": rep[2]} for rep in replies]
            })
    return jsonify(result)

@app.route('/api/reflections', methods=['POST'])
def post_reflection():
    data = request.json
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("INSERT INTO reflections (word_id, username, content, date) VALUES (?, ?, ?, ?)",
                     (data['word_id'], data['username'], data['content'], datetime.now().strftime("%Y-%m-%d %H:%M")))
    return jsonify(status="success")

@app.route('/api/replies', methods=['POST'])
def post_reply():
    data = request.json
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("INSERT INTO replies (reflection_id, username, content, date) VALUES (?, ?, ?, ?)",
                     (data['reflection_id'], data['username'], data['content'], datetime.now().strftime("%Y-%m-%d %H:%M")))
    return jsonify(status="success")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print(f"--- ling-ling-etymon サーバー起動中 ---")
    print(f"ポート: {port}")
    app.run(host='0.0.0.0', port=port, debug=False)
