# 💬 Tsumugi-AI-Voice-Assistant

*Your fully offline, anime-style voice assistant—powered by local LLMs and adorable text-to-speech!*

> **Tsumugi-AI-Voice-Assistant** blends [Ollama](https://ollama.com) for fast, local language models with [VOICEVOX](https://voicevox.hiroshiba.jp/) for cute, anime waifu–like voices. No cloud. No tracking. Just pure, local AI companionship.

## ✨ Features

- 🧠 **100% local LLM** responses with **Ollama**—runs entirely offline!
- 🗣️ **Anime-style text-to-speech** using **VOICEVOX**
- 🔐 **Privacy-first:** No API keys, no internet required, everything runs on your device
- 🧋 **Customizable:** Mix and match models and voices
- 🎤 **Optional voice input:** Talk hands-free with your mic
- 🖥️ **Cross-platform:** Works on Windows, macOS, and Linux


## 🛠️ Requirements

- [VOICEVOX Engine](https://voicevox.hiroshiba.jp/)
- [Ollama](https://ollama.com)
- Python 3.8+
- Microphone and speakers


## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/Tsumugi-AI-Voice-Assistant.git
cd Tsumugi-AI-Voice-Assistant
```

2. **Install Python dependencies:**

```bash
pip install -r requirements.txt
```

3. **Start the VOICEVOX engine:**
    - Windows:
`C:\Program Files\VOICEVOX\vv-engine\run.exe`
    - (See VOICEVOX docs for macOS/Linux instructions.)
4. **Start Ollama and load a model (e.g., llama3):**

```bash
ollama run llama3
```

5. **Run the assistant:**

```bash
python voice_assistant.py
```


*That’s it! Enjoy chatting with your own anime waifu–style AI assistant 💬🎀*

## 🧪 Technologies Used

| Tech | Purpose |
| :-- | :-- |
| Ollama | Local LLM backend |
| VOICEVOX | Anime TTS engine |
| Python | Scripting/integration |
| SpeechRecognition | Optional voice input |

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgements

- Huge thanks to the creators of **VOICEVOX** and **Ollama**
- Inspired by anime fans, local-first tinkerers, and open-source communities!

*Feel free to fork, star, and contribute!*

<div style="text-align: center">⁂</div>

[^1]: https://ollama.com

