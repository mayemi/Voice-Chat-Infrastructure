from playsound import playsound
from gtts import gTTS
import os
import speech_recognition as sr

motor = sr.Recognizer()

def sesDinleCevir():
    with sr.Microphone() as kaynak:
        print("Dinliyorum")
        ses = motor.listen(kaynak)

    try:
        yazi = motor.recognize_google(ses, language="tr-TR")
        print(f"Sen: {yazi}")
        return yazi
    
    except sr.UnknownValueError:
        print("Asistan: Anlayamadım.")
        return ""
    
    except sr.RequestError as e:
        print(f"Servis hatası: {e}")
        return ""

def cevapla(yazi):
    if "selam" in yazi.lower():
        return "Selamlar"
    else:
        return "Cevap bulamadım, sanırım hafızamda tanımlı olmayan bir şey söyledin."

def seslendir(yazi):
    okunacakYazi = gTTS(text=yazi, lang="tr")
    print(f"Asistan: {yazi}")
    dosyaAdi = "prompt.mp3"
    okunacakYazi.save(dosyaAdi)
    playsound(dosyaAdi)
    os.remove(dosyaAdi)

def main():
    while True:
        ileti = sesDinleCevir()
        if ileti:
            cevap = cevapla(ileti)
            seslendir(cevap)

if __name__ == '__main__':
    main()