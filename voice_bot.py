import whisper
from transformers import pipeline
from gtts import gTTS
import tempfile, os
from playsound import playsound

# Load Whisper model for STT
stt_model = whisper.load_model("base")

# Load a small local text-generation model
generator = pipeline("text-generation", model="facebook/opt-125m")  # lightweight

def transcribe(audio_file):
    result = stt_model.transcribe(audio_file)
    return result["text"]

def generate_response(prompt):
    result = generator(prompt, max_length=100, do_sample=True)
    return result[0]['generated_text']

def speak(text):
    tts = gTTS(text=text, lang='en')
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(tmp_file.name)
    playsound(tmp_file.name)
    os.remove(tmp_file.name)

# Example usage
audio_file = "input.wav"  # Replace with your recorded voice file
print("Transcribing audio...")
text = transcribe(audio_file)
print("You said:", text)

reply = generate_response(text)
print("Bot:", reply)
speak(reply)
