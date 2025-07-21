import json

def load_history():
    try:
        with open("chat_history.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print("[HISTORY LOAD ERROR]", e)
        return []

def save_history(history):
    with open("chat_history.json", "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)