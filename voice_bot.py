import openai
import speech_recognition as sr
import pyttsx3

openai.api_key = "YOUR_OPENAI_API_KEY"

# Initialize TTS
engine = pyttsx3.init()

# Initialize STT
r = sr.Recognizer()
mic = sr.Microphone()

def listen():
    with mic as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)  # Using Google STT
        print("You said:", text)
        return text
    except:
        return ""

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]
    )
    return response['choices'][0]['message']['content']

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    text = listen()
    if text.lower() in ["exit", "quit"]:
        break
    if text:
        reply = generate_response(text)
        print("Bot:", reply)
        speak(reply)
