import os
import speech_recognition as sr
import openai
import requests
import io
from pydub import AudioSegment
from pydub.playback import play

# --- Configuration ---
# Ollama (Local LLM) Configuration
try:
    client = openai.OpenAI(
        base_url='http://localhost:11434/v1',
        api_key='ollama',  # required, but unused by Ollama
    )
    print("[SETUP] OpenAI client configured to use local Ollama server.")
except Exception as e:
    print(f"Failed to initialize OpenAI client for Ollama: {e}")
    exit()

# Voicevox (Local TTS) Configuration
VOICEVOX_BASE_URL = "http://127.0.0.1:50021"
# You can change the speaker ID to any character you like from your Voicevox app.
# Common IDs: 1 (Zundamon), 3 (Shikoku Metan), 8 (Kasukabe Tsumugi)
SPEAKER_ID = 8
print(f"[SETUP] Voicevox configured for speaker ID: {SPEAKER_ID}")

# Assistant Configuration
WAKE_WORD = "konichiwa"
LOCAL_MODEL_NAME = "qwen3:1.7b"

# --- Global Recognizer Instance ---
try:
    r = sr.Recognizer()
    r.dynamic_energy_threshold = True
    print("[SETUP] Recognizer initialized.")
except Exception as e:
    print(f"Failed to initialize SpeechRecognition: {e}")
    exit()


# --- Core Functions ---

def speak(text):
    """
    Generates speech using a local VOICEVOX server and plays it.
    """
    if not text:
        print("[DEBUG] Speak function called with no text.")
        return
    try:
        print(f"Assistant: {text}")

        # 1. Create the audio query for Voicevox
        params = {"text": text, "speaker": SPEAKER_ID}
        query_response = requests.post(
            f"{VOICEVOX_BASE_URL}/audio_query",
            params=params,
            timeout=10  # Add a timeout to prevent indefinite hanging
        )
        query_response.raise_for_status()
        audio_query = query_response.json()

        # 2. Synthesize the voice audio data from the query
        synthesis_response = requests.post(
            f"{VOICEVOX_BASE_URL}/synthesis",
            headers={"Content-Type": "application/json"},
            json=audio_query,
            params={"speaker": SPEAKER_ID},
            timeout=25  # Add a longer timeout for synthesis
        )
        synthesis_response.raise_for_status()

        # 3. Play the audio from the response content
        audio_data = io.BytesIO(synthesis_response.content)
        audio_segment = AudioSegment.from_wav(audio_data)
        play(audio_segment)

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Could not connect to VOICEVOX server: {e}")
        print("        Please ensure the VOICEVOX application is running and accessible.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred during voice synthesis: {e}")


def listen_for_command(prompt="Listening..."):
    """Listens for audio input from the user and transcribes it."""
    with sr.Microphone() as source:
        print(prompt)
        try:
            audio = r.listen(source)
        except sr.WaitTimeoutError:
            return None

    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print(f"[ERROR] Google Speech Recognition request failed; {e}")
        return None


def get_ai_response(prompt):
    """Sends the user's prompt to the LOCAL LLM and gets a response."""
    if not prompt:
        return "I didn't catch that."

    try:
        response = client.chat.completions.create(
            model=LOCAL_MODEL_NAME,
            messages=[
                {"role": "system",
                 "content": "You are a helpful voice assistant. Keep your responses brief and conversational."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[ERROR] Could not get response from local LLM: {e}")
        return "I'm having trouble connecting to my local brain."


# --- Main Loop ---
def main():
    """Main function to run the voice assistant."""
    print("Calibrating microphone...")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1.5)
    print("Calibration complete.")

    speak("Voice assistant initialized")  # "Voice assistant initialized" in Japanese
    print(f"Voice Assistant initialized. Say '{WAKE_WORD}' to start.")

    while True:
        print("\n--- Waiting for wake word ---")
        command = listen_for_command(prompt="Listening for wake word...")

        if command and WAKE_WORD in command:
            speak("はい")  # "Yes, I'm listening" in Japanese
            user_prompt = listen_for_command(prompt="Listening for your command...")

            if user_prompt:
                ai_response = get_ai_response(user_prompt)
                speak(ai_response)
            else:
                speak("すみません、聞き取れませんでした")  # "Sorry, I couldn't hear that" in Japanese


if __name__ == "__main__":
    main()
