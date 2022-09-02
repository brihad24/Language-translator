import speech_recognition
import pyttsx3
        
def speechConversion():

    recogniser = speech_recognition.Recognizer()

    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recogniser.adjust_for_ambient_noise(mic, duration = 0.2)
                audio = recogniser.listen(mic, phrase_time_limit= 5)

                text = recogniser.recognize_google(audio)
                text = text.lower()

                return text
        
        except speech_recognition.UnknownValueError():
            recogniser = speech_recognition.Recognizer()
            continue