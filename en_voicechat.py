from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os

motor = sr.Recognizer()

def record():
    with sr.Microphone() as source:
        print("Asistan: Dinliyorum...")
        audio = motor.listen(source)

    try:
        text = motor.recognize_google(audio, language="tr-TR")
        print(f"Sen: {text}")
        return text
        
    except sr.UnknownValueError:
        print("Asistan: Anlayamadım")
        return ""
        
    except sr.RequestError as e:
        print(f"Servis hatası: {e}")
        return ""

def response(text):
    if "merhaba" in text.lower():
        return "Sana da Merhaba!"
    elif "ne haber" in text.lower() or "naber" in text.lower():
        return "İyi senden naber?"
    else:
        return "Benim hafızayı aştın."
    
def speak(text):
    prompt = gTTS(text=text, lang="tr")
    print(f"Asistan: {text}")
    file_name = "speech.mp3"
    prompt.save(file_name)
    playsound(file_name)
    os.remove(file_name)

def main():
    while True:
        message = record()
        if message:
            phrase = response(message)
            speak(phrase)

if __name__ == '__main__':
    main()