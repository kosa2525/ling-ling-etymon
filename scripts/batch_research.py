import json
import os
import re
import sys
from datetime import datetime

# Configuration
DATA_JS_PATH = r"c:\Users\integ\OneDrive\デスクトップ\ling-ling-etymon\data.js"

def get_existing_ids():
    if not os.path.exists(DATA_JS_PATH):
        return set()
    try:
        with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
        match = re.search(r"const WORDS = (\[.*\]);", content, re.DOTALL)
        if match:
            words = json.loads(match.group(1))
            return {w["id"].lower() for w in words if "id" in w}
    except Exception as e:
        print(f"Error reading existing IDs: {e}")
    return set()

def save_words(new_words):
    try:
        with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
        
        match = re.search(r"const WORDS = (\[.*\]);", content, re.DOTALL)
        if not match:
            print("Could not find WORDS array")
            return False
            
        existing_words = json.loads(match.group(1))
        existing_words.extend(new_words)
        
        new_content = f"const WORDS = {json.dumps(existing_words, indent='\t', ensure_ascii=False)};\n"
        
        with open(DATA_JS_PATH, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    except Exception as e:
        print(f"Error saving words: {e}")
        return False

def main():
    existing_ids = get_existing_ids()
    print(f"Found {len(existing_ids)} existing words.")
    
    # Selection of 45 common/academic English words not already in the database
    # Focus on connectivity: roots like 'spect', 'port', 'dict', 'fact', 'tend'
    words_to_research = [
        "Inspect", "Prospect", "Aspect", "Retrospect", "Circumspect",
        "Export", "Import", "Transport", "Report", "Support",
        "Predict", "Contradict", "Dictate", "Verdict", "Indict",
        "Factory", "Manufacture", "Artifact", "Facilitate", "Benefactor",
        "Extend", "Intend", "Pretend", "Contend", "Distend",
        "Submit", "Admit", "Transmit", "Omit", "Permit",
        "Compose", "Oppose", "Propose", "Dispose", "Expose",
        "Contract", "Abstract", "Extract", "Retract", "Distract",
        "Revive", "Survive", "Convivial", "Vivid", "Vital"
    ]
    
    unique_targets = [w for w in words_to_research if w.lower() not in existing_ids][:45]
    
    if not unique_targets:
        print("All target words already exist.")
        # Fallback to some more advanced words if basic ones are taken
        unique_targets = ["Ethereal", "Ephemeral", "Labyrinth", "Melancholy", "Quintessential"] # Example placeholders
        # In a real run, I would regenerate this list dynamically
    
    print(f"Targeting {len(unique_targets)} words: {unique_targets}")
    # This script will be called in a loop.
    # The actual research will happen via browser or internal knowledge.
    # Since I'm the assistant, I'll generate the data in the next step.
    for word in unique_targets:
        print(f"QUEUED: {word}")

if __name__ == "__main__":
    main()
