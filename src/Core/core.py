# Kara Object

# native
import os
import json
import importlib #
# 3rd Party
import pyttsx3
import speech_recognition as sr
# linking file
import Core.Data.link as link


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
        with open('Core/Data/abilities.json', 'r') as log:
            self.abilities = json.load(log) # parse json

    # reload linking file
    def reload(self):
        importlib.reload(link)

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
        for ability in self.abilities:
            for command in self.abilities[ability]['commands']:
                # check command's keywords against given text
                for keyword in self.abilities[ability]['commands'][command]['keywords']:
                    if keyword in text:
                        func = self.abilities[ability]['commands'][command]['target']
                        # pass Kara and command to command
                        exec('link.' + func + '(self, text)')
