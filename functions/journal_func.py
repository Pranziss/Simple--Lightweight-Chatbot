import json
import os

def save_to_journal(entry):
    try:
        if not os.path.exists("journal.json"):
            journal = []
        else:
            with open("journal.json", "r", encoding="utf-8") as f:
                journal = json.load(f)
                if not isinstance(journal, list):
                    raise ValueError("journal.json must be a list")

        journal.append(entry)

        with open("journal.json", "w", encoding="utf-8") as f:
            json.dump(journal, f, indent=2)

    except Exception as e:
        print("[JOURNAL SAVE ERROR]", e)