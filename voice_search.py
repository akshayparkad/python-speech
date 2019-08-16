#libraries required : SpeechRecognition, PyAudio

'''
   Valid Commands:

   contact
   about
   portfolio
   gallery
   services
   
'''

import speech_recognition as sr
import os
commands = ["contact", "about", "portfolio", "gallery", "services"]
rec = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    print("Say something...")
    audio = rec.listen(source)    
raw = rec.recognize_google(audio) #Google Speech API
print("Command Recognize: " + raw)
if raw not in commands:
    print("Website doesn't have " + raw + " page. Try another command")
else:
    print("Opening " + raw + " Page....")
    os.system("start \"\" https://voiceapi.000webhostapp.com/" + raw + ".html")
