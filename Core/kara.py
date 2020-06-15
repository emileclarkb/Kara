import pyttsx3
import speech_recognition as sr

class Kara:
    def __init__(self):
        # wake words (my lisp sucks...)
        self.wake = ['kara', 'cara', 'kawa']

        # init engine and voices
        self.engine = pyttsx3.init()
        self.voices = engine.getProperty('voices')
        # set properties
        self.engine.setProperty('rate', 125)
        self.engine.setProperty('volume',1.0)
        self.engine.setProperty('voice', voices[1].id)

    # text to speech
    def speak(self, text, save=False):
        # save text to file
        if save:
            filename = text.replace(' ', '_')
            self.engine.save_to_file(text, text+'.mp3')
        else:
            self.engine.say(text)

        self.engine.runAndWait()

    # speech to text
    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            text = ""

            try:
                text = r.recognize_google(audio)
            except Exception as e:
                print("Exception: " + str(e))

        return text.lower()

    def compile(self, text):
        pass
