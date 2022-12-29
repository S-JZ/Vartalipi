def speak(text):
    import os
    import azure.cognitiveservices.speech as speechsdk

    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription="SECRET_KEY", region="eastus")
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name='en-US-ChristopherNeural'

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")


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

