from flask import Flask, render_template, request, jsonify
import random
from datetime import datetime
import json

from functions.memory_func import load_memory, save_memory
from functions.history_func import load_history, save_history
from functions.journal_func import save_to_journal
from functions.model_runner import run_model, summarize_convo
from functions.prompt import create_prompt, create_summary_prompt

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message", "")
    memory = load_memory()
    memory_facts = memory.get("memories", [])

    moods = ["chill", "curious", "goofy", "snarky", "gentle"]
    mood = random.choice(moods)

    prompt = create_prompt(user_input, memory_facts, mood)
    reply = run_model(prompt)

    history = load_history()
    history.append({"user": user_input, "nova": reply})
    save_history(history[-50:])

    save_to_journal({
        "timestamp": datetime.now().isoformat(),
        "user": user_input,
        "nova": reply
    })

    if "remember that" in user_input.lower():
        memory.setdefault("memories", []).append(user_input)
        save_memory(memory)

    return jsonify({"response": reply})

@app.route("/history", methods=["GET"])
def get_history():
    return jsonify(load_history())

@app.route("/clear-history", methods=["POST"])
def clear_history():
    save_history([])
    return jsonify({"status": "History cleared"})

@app.route("/view-history")
def view_history():
    return render_template("history.html")

@app.route("/journal", methods=["GET"])
def view_journal():
    try:
        with open("journal.json", "r", encoding="utf-8") as f:
            journal = json.load(f)
            return jsonify(journal if isinstance(journal, list) else [])
    except Exception as e:
        print("[VIEW JOURNAL ERROR]", e)
        return jsonify([])

@app.route("/summarize-journal", methods=["GET"])
def summarize_journal():
    try:
        with open("journal.json", "r", encoding="utf-8") as f:
            journal = json.load(f)

        if not isinstance(journal, list) or len(journal) < 2:
            return jsonify({"summary": "Not enough entries to summarize just yet."})

        convo_text = "\n".join(
            f"User: {entry['user']}\nNova: {entry['nova']}" for entry in journal[-10:]
        )

        summary_prompt = create_summary_prompt(convo_text)
        summary = summarize_convo(summary_prompt)
        return jsonify({"summary": summary or "Something went blank—try again."})

    except Exception as e:
        print("[SUMMARY ERROR]", e)
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    print("🚀 Nova is booting u11p on http://192.168.1.21:5000/ (accessible on your local network)")
    app.run(host="0.0.0.0", port=5000, debug=True)