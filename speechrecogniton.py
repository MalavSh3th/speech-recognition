# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:56:44 2020

@author: Malav
"""

import speech_recognition as sr
import webbrowser
r = sr.Recognizer()

with sr.Microphone() as source:
        print("what do you want to search?\n")
        audio = r.listen(source)
        
print('opening : ' +r.recognize_google(audio))

p = r.recognize_google(audio)
webbrowser.open(p)