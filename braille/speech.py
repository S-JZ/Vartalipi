def speak(msg: str, language='english'):
    import speech_recognition as sr
    import os
    import pyttsx3

    engine = pyttsx3.init()
    if language == "english":
        voices = engine.getProperty('voices')
        engine.setProperty("voice", voices[0].id)
    else:
        engine.setProperty("voice", voices[1].id)
    # initialize Text-to-speech engine
    engine.say(msg)
    # play the speech
    engine.runAndWait()


def write_to_file(text):
    f = open("sample_text.txt", "ab")
    f.write(text.encode("utf8"))
    f.close()


def audio_to_text(sr, r, lang='eng', question=False):
    try:
        with sr.Microphone() as source:
            # read the audio data from the default microphone
            audio_data = r.record(source, duration=5)
            print("Recognizing...")
            print(lang)
            # convert speech to text
            if lang == "eng":
                lang = 'en-US'
            else:  
                lang = 'hi-IN' 
            text = r.recognize_google(audio_data, language=lang)
            print(text)
            if question:
                return text.lower()
            else:
                write_to_file(text)
    except Exception as e:
        print(e)
        return None

def get_language(sr, r):
    lang_question = "Which language do you prefer?"
    speak(lang_question)
    language = audio_to_text(sr, r, question=True)
    print("in get lang", language)
    if language is not None:
        speak("You have chosen " + language)
    else:
        language = get_language(sr, r)
    if language[:3] == "eng":
        return "eng"
    elif language[:3] == "hin":
        return "hin"


def launch_project():
    import speech_recognition as sr
    import os
    import pyttsx3 
    r = sr.Recognizer()
    engine = pyttsx3.init()
    msg = "Welcome to Varta Lipi."
    file = open("sample_text.txt", "w")
    file.close()
    speak(msg)
    language = get_language(sr, r)
    try:
        audio_to_text(sr, r, lang=language)
    except Exception as e:
        return None
    audio_to_text(sr, r)
    return language

