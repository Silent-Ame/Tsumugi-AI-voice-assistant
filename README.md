# 💬 Tsumugi-AI-Voice-Assistant

**Tsumugi-AI-Voice-Assistant** is a fully offline anime-style voice assistant that combines the power of [Ollama](https://ollama.com) for local LLM processing with [VOICEVOX](https://voicevox.hiroshiba.jp/) for cute, anime waifu–like voice output. Think of it as your own personal AI companion that talks like your favorite anime girl — all without sending a single request to the cloud.

---

## ✨ Features

- 🧠 Fully local LLM responses powered by **Ollama**
- 🗣️ Anime-style text-to-speech via **VOICEVOX**
- 🔌 100% offline — no API keys, no external servers
- 🧋 Customizable voice and model pairing (e.g., LLaMA + Tsumugi)
- 🎤 Optional voice input (mic-to-response loop)

---

## 🛠️ Requirements

- [VOICEVOX Engine](https://voicevox.hiroshiba.jp/)  
- [Ollama](https://ollama.com)  
- Python 3.8 or higher  
- A microphone and speakers

---

## 📦 Installation

1. **Clone this repository**:


git clone https://github.com/yourusername/Tsumugi-AI-Voice-Assistant.git
cd Tsumugi-AI-Voice-Assistant
Install Python dependencies:

pip install -r requirements.txt

Start the VOICEVOX engine:

Run this executable:

C:\Program Files\VOICEVOX\vv-engine\run.exe

Start Ollama:

Make sure Ollama is running and load your model (e.g. llama3):

ollama run llama3

Run the voice assistant:

python voice_assistant.py

Enjoy chatting with your anime waifu–style AI assistant 💬🎀

🧪 Technologies Used
Ollama – local LLM backend

VOICEVOX – anime TTS engine

Python – for scripting and integration

SpeechRecognition – for optional voice input

📜 License
This project is licensed under the MIT License.
See LICENSE for more information.

🙏 Acknowledgements
Huge thanks to the creators of VOICEVOX and Ollama

Inspired by anime fans, tinkerers, and local-first developers
