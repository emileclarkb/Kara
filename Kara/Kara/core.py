# Kara Object

# native
import json
import importlib
# 3rd Party
import pyttsx3
import speech_recognition as sr
# Kara
from Kara.Kara.Scripts.colors import red


class Kara:
    def __init__(self, abilitiesPath='Abilities/', cachePath='Cache/'):
        # custom paths
        self.abilitiesPath = abilitiesPath
        self.cachePath = cachePath

        # wake words (my lisp sucks...)
        self.wake = ['kara', 'cara', 'kawa']

        # init engine and voices
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        # set properties
        self.engine.setProperty('rate', 125)
        self.engine.setProperty('volume',1.0)
        self.engine.setProperty('voice', self.voices[1].id)

        # import linking file
        try:
            # "Cache/" -> "Cache."
            cacheModule = cachePath.replace('/', '.')
            #import Kara.Data.Cache.link as link
            self.link = importlib.import_module(cacheModule + 'link')
        except ModuleNotFoundError:
            print(red('\n[-] Failed to Load Linking File!'))


    # reload linking file
    def reload(self):
        # handle if link was made incorrectly
        try:
            importlib.reload(self.link)
        except AttributeError:
            print(red('\n[-] Cached Linking File Failed to Operate!'))
            sys.exit(1)

    # text to speech
    def speak(self, text, path='', save=False):
        # save text to file
        if save:
            filename = text.replace(' ', '_')
            self.engine.save_to_file(text, path + filename + '.mp3')
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
        # read all logged abilities
        with open(self.cachePath + 'commands.json', 'r') as log:
            self.abilities = json.load(log) # parse json

        # iterate abilities and their commands to find correct response
        for command in self.abilities:
            # check command's keywords against given text
            for keywords in command['keywords']:
                # keywords match criteria
                match = True

                # iterate all keywords
                for keyword in keywords.split(' '):
                    # keyword doesn't match
                    if not keyword in text:
                        match = False
                        break

                # all keywords matched
                if match:
                    func = command['target']
                    # pass Kara and command to command
                    exec('self.link.{}(self, text)'.format(func))

                    return 0
