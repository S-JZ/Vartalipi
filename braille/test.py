import speech_recognition as sr
import os
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
msg = "नमस्ते दुनिया"
engine.setProperty("voice", voices[1].id)
engine.say(msg)
engine.runAndWait()