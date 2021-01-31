# ShabakCTF@2021 

import speech_recognition as sr
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './mongolian_audio.aiff')

harvard = sr.AudioFile(filename)
r = sr.Recognizer()

with harvard as source:
    audio = r.record(source)
    # print(audio)
    # 'mn' stands for Mongolian:
    response = r.recognize_google(audio, language='mn', show_all=True)

print(response['alternative'][0]['transcript'])

# Unfortunately, implemanting a translator was too much work so just paste in google translate :)