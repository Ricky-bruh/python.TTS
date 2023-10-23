from gtts import gTTS
import os

def text_to_speech(text):
    tts = gTTS(text=text, lang='it')
    filename = "speech.mp3"
    tts.save(filename)
    os.system(f"start {filename}")

if _name_ == "_main_":
    text = "La vita è ciò che succede mentre sei occupato a fare altri progetti. - Jonh Lennon"
    text_to_speech(text)