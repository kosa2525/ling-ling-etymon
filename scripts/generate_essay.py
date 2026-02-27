import os
import json
import openai
import re
from datetime import datetime

# --- Configuration ---
api_key = os.environ.get("OPENAI_API_KEY", "")
client = openai.OpenAI(api_key=api_key)
ESSAY_JS_PATH = os.path.join(os.path.dirname(__file__), "..", "essays.js")

PROMPT_TEMPLATE = f"""
あなたは世界最高峰の言語学者であり、哲学者です。英語の語源と思想史についての深く、学術的で、かつ詩的なエッセイを執筆してください。

【制約条件】
1. 文字数: 日本語で4000文字〜6000文字程度の圧倒的なボリューム。
2. 言語: 主文は日本語。語源用語、引用、学術的参照のみ英語を使用。
3. トーン: 極めて知的で、格調高く、読者を魅了するプレミアムな文体。
4. 内容: 単なる辞書的な説明を超え、言葉の背後にある人類の思考の歴史や哲学的な洞察を提供すること。
5. テーマ例: '光と言葉の語源学', '法思想におけるラテン語の鼓動', '印欧語根が形作る現代のデジタル世界' などから一つ選び、あるいはそれと同等かそれ以上の深さを持つテーマを独自に設定してください。

【出力形式】
以下のJSONオブジェクトのみを出力してください。
{{
    "id": "essay_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
    "title": "エッセイのタイトル",
    "content": "ここにマークダウン形式で全エッセイ本文。非常に長く、詳細に記述すること。段落を適切に分け、読者が思考の深淵に触れられるようにすること。",
    "date": "{datetime.now().strftime('%Y-%m-%d')}"
}}
"""

def extract_valid_essays(text):
    """強力なJSON抽出ロジック"""
    essays = []
    # 単純な全体パースを試みる
    match = re.search(r'const\s+ESSAYS\s*=\s*(\[.*\])\s*;?\s*$', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except:
            pass
    
    # 失敗した場合は個別のオブジェクトを抽出
    starts = [m.start() for m in re.finditer(r'\{\s*"id":\s*"essay_', text)]
    for start in starts:
        brace_count = 0
        in_string = False
        escape = False
        for i in range(start, len(text)):
            c = text[i]
            if not escape and c == '"': in_string = not in_string
            if not in_string and c == '{': brace_count += 1
            if not in_string and c == '}':
                brace_count -= 1
                if brace_count == 0:
                    try:
                        obj = json.loads(text[start:i+1])
                        essays.append(obj)
                    except: pass
                    break
            escape = (c == '\\' and not escape)
    return essays

def generate_essay():
    print("Generating a massive, premium weekly essay (4000-6000 chars)...")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": PROMPT_TEMPLATE}],
        response_format={ "type": "json_object" }
    )
    essay_data = json.loads(response.choices[0].message.content)
    
    # Check current content
    existing_essays = []
    if os.path.exists(ESSAY_JS_PATH):
        with open(ESSAY_JS_PATH, "r", encoding="utf-8") as f:
            content = f.read()
            existing_essays = extract_valid_essays(content)

    print(f"Found {len(existing_essays)} existing essays. Merging...")
    
    # Merge (latest first)
    updated_essays = [e for e in existing_essays if e['id'] != essay_data['id']]
    updated_essays.insert(0, essay_data)
    
    os.makedirs(os.path.dirname(ESSAY_JS_PATH), exist_ok=True)
    with open(ESSAY_JS_PATH, "w", encoding="utf-8") as f:
        # 見やすくインデント付きで保存
        f.write(f"const ESSAYS = {json.dumps(updated_essays, indent=8, ensure_ascii=False)};\n")
    
    print(f"Successfully saved '{essay_data['title']}' ({len(essay_data['content'])} chars)")

if __name__ == "__main__":
    generate_essay()
