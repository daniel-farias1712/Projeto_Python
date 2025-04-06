import speech_recognition as sr

def reconhecer_fala():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            frase = recognizer.recognize_google(audio, language='pt-BR')
            return frase
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None
