# 💡 Simple--Lightweight-Chatbot

A super lightweight, local chatbot designed for desktop/laptop use — ideal for minimal setups, offline usage, and quick experimentation.

🛠️ This is my first chatbot project, later refined and optimized before being shared publicly for others to explore and learn from.

---

## 🚀 Features

- 💬 Local LLM chatbot powered by Ollama
- 🧠 Custom persistent memory using memory.json
- 📝 Chat and journal history stored in chat_history.json
- ⚡ Lightweight and clean architecture (accessible via local Wi-Fi)
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

app.py                  → Main Flask application  
brain.py                → Core chatbot logic  
functions/              → Modular helper functions  
• history_func.py       → Conversation history  
• journal_func.py       → Journaling logic  
• memory_func.py        → Memory system  
• model_runner.py       → Ollama interaction  
• prompt.py             → Prompt construction  

templates/  
• index.html            → Main chat UI  
• history.html          → History & journal viewer  

static/  
• style.css             → Styling  
• script.js             → Frontend logic  

memory.json             → Persistent chatbot memory  
chat_history.json       → Stored chats & journals  
demo.gif                → UI preview  

---

## 🧠 Ollama Model Setup

1. Install Ollama  
   https://ollama.com

2. Pull a model (example: Phi-2)

   ollama pull phi:2

3. Run the model

   ollama run phi:2

Phi-2 is used for its balance of speed and performance.  
You may also use models like mistral or llama3.

---

## 🔧 How to Run the App

1. Clone the repository

   git clone https://github.com/Pranziss/Simple--Lightweight-Chatbot.git  
   cd Simple--Lightweight-Chatbot

2. (Optional) Create a virtual environment

   python -m venv venv  
   venv\Scripts\activate   (Windows)  
   source venv/bin/activate (Mac/Linux)

3. Install dependencies

   pip install flask

4. Start Ollama and run the app

   ollama run phi:2  
   python app.py

5. Open in browser

   http://localhost:5000

---

## ✉️ Contact

Built with ❤️ by Pranziss / yubedaoneineed

This is my first public chatbot project — feel free to fork, star ⭐, or reach out with feedback and ideas.
