from gtts import gTTS
import os
import subprocess

def text_to_speech(text):
    tts = gTTS(text=text, lang='it')
    filename = "speech.mp3"
    tts.save(filename)
    if os.name == 'nt':
        # Se stai utilizzando Windows, usa il comando "start" per aprire il file audio
        subprocess.Popen(['start', filename], shell=True)
    else:
        # Altrimenti, usa il lettore multimediale predefinito del sistema per riprodurre il file
        subprocess.Popen(['xdg-open', filename])

if __name__ == "__main__":
    text = "La vita è ciò che succede mentre sei occupato a fare altri progetti. - Jonh Lennon"
    text_to_speech(text)
