# Kara Object

# native
import os
import json
import importlib #
# 3rd Party
import pyttsx3
import speech_recognition as sr
# Kara
from Core.Scripts.colors import red
# linking file
try:
    import Core.Data.link as link
except SyntaxError:
    print(red('\n[-] Failed to Load Linking File!'))


class Kara:
    def __init__(self):
        # wake words (my lisp sucks...)
        self.wake = ['kara', 'cara', 'kawa']

        # init engine and voices
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        # set properties
        self.engine.setProperty('rate', 125)
        self.engine.setProperty('volume',1.0)
        self.engine.setProperty('voice', self.voices[1].id)

        # read all logged abilities
        with open('Core/Data/commands.json', 'r') as log:
            self.abilities = json.load(log) # parse json

    # reload linking file
    def reload(self):
        # handle if link was made incorrectly
        try:
            importlib.reload(link)
        except NameError:
            print(red('\n[-] Cached Linking File Failed to Operate!'))
            sys.exit(1)

    # text to speech
    def speak(self, text, save=False):
        # save text to file
        if save:
            filename = text.replace(' ', '_')
            self.engine.save_to_file(text, filename+'.mp3')
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

    # create new ability template
    def abilityTemp(self, name):
        # path to abilities
        path = 'Core/Abilities/' + name

        # make ability
        try:
            os.mkdir(path)
        except FileExistsError:
            # error message
            return 1

        # write main.py template
        with open('Core/Data/Templates/main.py', 'r') as template:
            # write config
            with open(path + '/main.py', 'w') as file:
                # write template to main.py
                file.write(template.read())

        # write config.json file
        # open template
        with open('Core/Data/Templates/config.json', 'r') as template:
            # write config
            with open(path + '/config.json', 'w') as file:
                # write template to config.json
                file.write(template.read())

        # write requirements.txt file
        # open template
        with open('Core/Data/Templates/requirements.txt', 'r') as template:
            # write config
            with open(path + '/requirements.txt', 'w') as file:
                # write template to requirements.txt
                file.write(template.read())

        return 0

    def compile(self, text):
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
                    exec('link.' + func + '(self, text)')

                    return 0
