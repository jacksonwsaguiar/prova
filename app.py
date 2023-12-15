import speech_recognition as sr
from gtts import gTTS
import pyttsx3 
 
r = sr.Recognizer() 
 
def speak_text(command):     
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

def generate_audio(phrase):
    try:
        tts = gTTS(phrase, lang='pt', tld='com.br')
        print('speaking...')
        speak_text(tts)
    except Exception as e:
        print(f"Erro ao sintetizar o áudio: {str(e)}")

if __name__ == "__main__":
    terminal = ""
    while True:
        terminal = str(input("Digite uma frase (digite sair, para encerrar):"))
        
        if(terminal=="sair"): break

        generate_audio(terminal)
 