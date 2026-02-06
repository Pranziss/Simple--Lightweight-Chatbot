# 💡 Simple-Lightweight-Chatbot

A super lightweight, **local-first chatbot** designed for desktop/laptop use — ideal for minimal setups, **offline usage**, and quick experimentation.

🛠️ This is my **first chatbot project**, later refined and optimized before being shared publicly for others to explore, learn from, and build upon.

---

## 🧠 Design Philosophy (Local-First AI)

This chatbot is intentionally designed to run **locally** using Ollama instead of cloud-based AI APIs.

**Why local-first?**
- 💸 No API or usage costs
- 🔒 Improved data privacy
- 🔌 Fully offline-capable
- 🧠 Full control over the AI model and prompts
- 🧪 Ideal for experimentation and learning system architecture

Due to hardware and runtime requirements, this project is **not deployed on free cloud hosting platforms** and is meant to be run on personal machines.

---

## 🚀 Features

- 💬 Local LLM chatbot powered by Ollama
- 🧠 Custom persistent memory using `memory.json`
- 📝 Chat and journal history stored in `chat_history.json`
- ⚡ Lightweight and clean architecture
- 🌐 Accessible via browser on the same local machine or local network
- 📦 Uses models pulled directly from Ollama (no LM Studio required)
- 🖥️ Optimized for laptops and desktops
- 🔌 Offline-capable
- 🔧 Built for simplicity and future extensibility

---

## 🎞️ Demo Preview

![Chatbot Demo](demo.gif)

---

## 🖥️ System Requirements

Developed and tested on:

- Intel Core i5-13420H  
- RTX 4050 Laptop GPU  
- 16GB RAM  
- Windows 11  

Minimum recommended:

- Quad-core CPU
- 8–16GB RAM
- Optional discrete GPU
- Smaller quantized models (e.g. Phi-2) work well on modest hardware

---

## 📁 Folder Structure
   app.py → Main Flask application
brain.py → Core chatbot logic

functions/
├─ history_func.py → Conversation history handling
├─ journal_func.py → Journaling logic
├─ memory_func.py → Persistent memory system
├─ model_runner.py → Ollama model interaction
└─ prompt.py → Prompt construction

templates/
├─ index.html → Main chat UI
└─ history.html → History & journal viewer

static/
├─ style.css → Styling
└─ script.js → Frontend logic

memory.json → Persistent chatbot memory
chat_history.json → Stored chats & journals
demo.gif → UI preview


---

## 🧠 Ollama Model Setup

1. Install Ollama  
   https://ollama.com

2. Pull a model (example: Phi-2)
ollama pull phi:2

3. Run the model
ollama run phi:2


Phi-2 is used for its balance of speed and performance.  
You may also use models like `mistral` or `llama3`.

---

## 🔧 How to Run the App

1. Clone the repository
-git clone https://github.com/Pranziss/Simple--Lightweight-Chatbot.git
-cd Simple--Lightweight-Chatbot

2. (Optional) Create a virtual environment
-python -m venv venv
venv\Scripts\activate # Windows
source venv/bin/activate # Mac/Linux

3. Install dependencies
-pip install flask

4. Start Ollama and run the app
ollama run phi:2
python app.py

5. Run it


---

## 🚀 Future Improvements

- Optional cloud-based deployment using external AI APIs
- Streaming responses (WebSockets)
- UI modernization using React + Tailwind
- Enhanced memory retrieval strategies

---

## 📜 Credits & Licensing

This project builds on open-source tools that make local AI experimentation accessible:

- **Ollama** — local LLM runtime for on-device inference
- Language models used via Ollama retain their **original licenses**
  (e.g. Phi-2, Mistral, LLaMA-based models)

This project itself is released under the **MIT License**.  
See the `LICENSE` file for more details.

---

## ⚠️ Disclaimer

This chatbot was developed as a **learning and experimentation project**.

AI-generated responses may be inaccurate, incomplete, or misleading.
This system is **not intended for production or critical use**.
Always verify important information independently.

Local model behavior depends heavily on hardware, model choice,
and prompt configuration.

---

## ✉️ Contact

Built with ❤️ by **Pranziss / yubedaoneineed**

This is my first public chatbot project — feel free to fork, star ⭐, or reach out with feedback and ideas.

