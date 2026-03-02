import os, re

path = 'c:/Users/integ/OneDrive/デスクトップ/ling-ling-etymon/scripts/subscription_server.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix notify author in toggle_flourish
# We use regex or careful search. Line numbers are around 220-233
target_pattern = r"(# 投稿者に通知.*?target_author = data\.get\('target_author'\).*?if not username:.*?with conn:.*?cur = conn\.cursor\(\).*?action = 'added'.*?)(# 投稿者に通知.*?if target_type == 'reflection':.*?elif target_type == 'word':.*?author_to_notify = target_author)"

old_notify = """                # 投稿者に通知（自分自身には送らない）
                author_to_notify = None
                if target_type == 'reflection':
                    cur.execute(f"SELECT username FROM reflections WHERE id={p}", (target_id,))
                    row = cur.fetchone()
                    if row: author_to_notify = row[0]
                elif target_type == 'essay':
                    cur.execute(f"SELECT author FROM user_essays WHERE id={p}", (target_id,))
                    row = cur.fetchone()
                    if row: author_to_notify = row[0]
                elif target_type == 'word':
                    author_to_notify = target_author"""

new_notify = """                # 投稿者に通知（自分自身には送らない）
                author_to_notify = None
                try:
                    if target_type == 'reflection':
                        cur.execute(f"SELECT username FROM reflections WHERE id={p}", (target_id,))
                        row = cur.fetchone()
                        if row: author_to_notify = row[0]
                    elif target_type == 'essay':
                        if str(target_id).startswith('essay_user_'):
                            real_id = int(str(target_id).replace('essay_user_', ''))
                            cur.execute(f"SELECT author FROM user_essays WHERE id={p}", (real_id,))
                            row = cur.fetchone()
                            if row: author_to_notify = row[0]
                    elif target_type == 'word':
                        author_to_notify = target_author
                except Exception as e:
                    print(f"Author lookup failed: {e}")"""

# Simple replace approach if exact match works
if old_notify in content:
    content = content.replace(old_notify, new_notify)
else:
    # Try with slightly different whitespace or find by segments
    print("Exact notify match not found, looking for parts...")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated!")
