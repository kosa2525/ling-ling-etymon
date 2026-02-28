import os
import json
import sys
import re
import tempfile
import time
from typing import Dict, Any, List
from datetime import datetime

try:
    import openai
except ImportError:
    print("Error: 'openai' library not found. Please run 'pip install openai' to use this script.")
    sys.exit(1)

# --- Configuration ---
api_key = os.environ.get("OPENAI_API_KEY", "")
client = openai.OpenAI(api_key=api_key)

# データの保存先 (プロジェクトルート)
DATA_JS_PATH = os.path.join(os.path.dirname(__file__), "..", "data.js")

# 単語プールを分離（現在は日常的な単語を優先、動詞も積極的に採用）
INTELLECTUAL_POOL = [
    "Imagine", "Create", "Evolve", "Discover", "Understand",
    "Believe", "Transform", "Achieve", "Listen", "Wander",
    "History", "Memory", "Energy", "Music", "Philosophy",
    "Universe", "Future", "Planet", "Culture", "Sustain"
]

EVERYDAY_POOL = [
    "Breakfast", "Window", "Salary", "Company", "Education",
    "Travel", "Celebrate", "Experience", "Connect", "Explore",
    "Pantry", "Muscle", "Camera", "Galaxy", "Alphabet",
    "Digital", "Sincere", "Disaster", "Candid", "Trivia"
]

PROMPT_TEMPLATE = """
Generate a JSON object for the etymology of the word '{word}', following the exact structure below. 

REQUIREMENTS:
1. You MUST provide at least one reliable etymological source.
2. The 'thinking_layer' MUST be a deep, philosophical, and poetic explanation in Japanese (minimum 250 words).
3. The 'core_concept' in 'ja' should be a concise but beautiful essence of the word.
4. Provide the 'meaning' in Japanese (concise definition).
5. Provide the 'part_of_speech' (noun, verb, adjective, etc.).
6. Tone: Intellectual, scholarly, and premium.

Structure:
{{
    "id": "{word_lower}",
    "word": "{word_cap}",
    "part_of_speech": "noun/verb/adjective",
    "meaning": "日本語での簡潔な意味",
    "author": "etymon_official",
    "etymology": {{
        "breakdown": [
            {{ "text": "prefix/root-", "type": "prefix/root", "meaning": "Japanese", "lang": "Origin" }}
        ],
        "original_statement": "Short historical snippet."
    }},
    "core_concept": {{
        "en": "Poetic English core essence.",
        "ja": "核となる概念の日本語訳"
    }},
    "thinking_layer": "思索の層（日本語、250文字以上の深く哲学的な論考）...",
    "synonyms": ["Word 1", "Word 2"],
    "antonyms": ["Word 1", "Word 2"],
    "aftertaste": "A single, powerful English sentence.",
    "deep_dive": {{
        "roots": [
            {{ "term": "root", "meaning": "meaning" }}
        ],
        "points": [
            "高度な語源学的知見（日本語）"
        ]
    }},
    "source": "Specific source",
    "date": "{date}"
}}
"""

def extract_valid_json_objects(text: str) -> List[Dict]:
    objects = []
    starts = [m.start() for m in re.finditer(r'\{\s*"id":', text)]
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
                    obj_str = text[start:i+1]
                    try:
                        obj = json.loads(obj_str)
                        if "id" in obj: objects.append(obj)
                    except: pass
                    break
            escape = (c == '\\' and not escape)
    return objects

def get_existing_data() -> List[Dict]:
    if not os.path.exists(DATA_JS_PATH): return []
    try:
        with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        
        if "const WORDS =" in content:
            # "const WORDS =" の後から最後までを取得し、末尾のセミコロンを除去
            json_part = content.split("const WORDS =", 1)[1].strip()
            if json_part.endswith(";"):
                json_part = json_part[:-1].strip()
            return json.loads(json_part)
    except Exception as e:
        print(f"Loading error in get_existing_data: {e}")
    return []

def suggest_batch_words(existing_ids, count=10):
    """
    日常的で語源が面白い単語を提案します。
    """
    suggestions = []
    
    # 既存のプールから日常単語を優先的に抽出
    pool = EVERYDAY_POOL + INTELLECTUAL_POOL
    for word in pool:
        if word.lower() not in existing_ids and word.lower() not in [s.lower() for s in suggestions]:
            suggestions.append(word)
            if len(suggestions) >= count: break

    if len(suggestions) < count:
        needed = count - len(suggestions)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Suggest common everyday English words with surprising etymologies. Mix nouns and interesting VERBS (actions/states). Output ONLY comma-separated words."},
                {"role": "user", "content": f"Exclude: {', '.join(existing_ids)}. Need {needed} words (at least 50% verbs)."}
            ]
        )
        suggestions.extend([w.strip() for w in response.choices[0].message.content.split(',') if w.strip()])

    return suggestions[:count]

def generate_word_data(word: str) -> Dict[str, Any]:
    print(f"Investigating: {word}...")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a multilingual etymologist and philosopher."},
            {"role": "user", "content": PROMPT_TEMPLATE.format(
                word=word, 
                word_lower=word.lower().replace(" ", "_"), 
                word_cap=word.capitalize(),
                date=datetime.now().strftime("%Y-%m-%d")
            )}
        ],
        response_format={ "type": "json_object" }
    )
    return json.loads(response.choices[0].message.content)

def main():
    batch_count = 10
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        batch_count = int(sys.argv[1])

    print(f"--- Task Scheduler Insight Mode: {batch_count} Everyday Words ---")
    
    existing_data = get_existing_data()
    existing_ids = [item.get("id").lower() for item in existing_data if item.get("id")]
    
    words_to_process = suggest_batch_words(existing_ids, batch_count)
    print(f"Target Words: {', '.join(words_to_process)}")

    success_count = 0
    for word in words_to_process:
        try:
            current_data = get_existing_data()
            if word.lower() in [item.get("id", "").lower() for item in current_data]:
                print(f"Skipping {word}, already exists.")
                continue

            data = generate_word_data(word)
            updated_list = [w for w in current_data if w.get("id") != data.get("id")]
            updated_list.append(data)
            
            json_str = json.dumps(updated_list, indent=8, ensure_ascii=False)
            with open(DATA_JS_PATH, 'w', encoding='utf-8') as f:
                f.write(f"const WORDS = {json_str};\n")
            
            print(f"Successfully added '{word}' to Archive.")
            success_count += 1
            time.sleep(1)
            
        except Exception as e:
            print(f"Failed '{word}': {e}")

    print(f"\n--- Batch Process Finished ---")
    print(f"Processed: {success_count} words")
    print(f"Total in Archive: {len(get_existing_data())}")

if __name__ == "__main__":
    main()
