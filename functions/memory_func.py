import json

def load_memory():
    try:
        with open("memory.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print("[MEMORY LOAD ERROR]", e)
        return {}

def save_memory(memory):
    with open("memory.json", "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)