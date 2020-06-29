# Kara Object

# native
import os
import sys
import json
import importlib
import shutil
# 3rd Party
import pyttsx3
import speech_recognition as sr
# Kara
from Kara.Core.Scripts.colors import red, yellow, green, white



class Kara:
    def __init__(self, abilitiesPath='Abilities/', cachePath='Cache/'):
        # custom paths
        self.abilitiesPath = abilitiesPath
        self.cachePath = cachePath

        # speech recognizer
        self.recognizer = sr.Recognizer()
        # speech microphone
        self.microphone = sr.Microphone()

        # wake words (my lisp sucks...)
        self.wake = ['kara', 'cara', 'kawa', 'cowra']

        # all acceptable responses
        self.responses = {'yes': ['yes', 'yep', 'yeah', 'ya'],
                          'no': ['no', 'nah', 'nope']}

        # manual mode
        self.manual = False

        # init engine and voices
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        # set properties
        self.engine.setProperty('rate', 125)
        self.engine.setProperty('volume', 1.0)
        self.engine.setProperty('voice', self.voices[1].id)

        # don't speak, just time how long abilities take to work
        self.debugTime = False

        # import linking file
        try:
            # "Cache/" -> "Cache."
            cacheModule = cachePath.replace('/', '.')
            cacheModule = cacheModule.replace('\\', '.')

            # current path
            current = os.path.dirname(os.path.abspath(__file__))
            current = current.replace('/', '.')
            current = current.replace('\\', '.')

            # remove full directory to leave relative path to Abilities
            cacheModule = cacheModule.replace(current, '')

            self.link = importlib.import_module('Kara.Core.Data.Cache.link')#cacheModule + 'link', package='Core')
        except:
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
        # don't speak anything (measure speed of an ability)
        if self.debugTime:
            return

        # save text to file
        if save:
            filename = text.replace(' ', '_')
            self.engine.save_to_file(text, path + filename + '.mp3')
        else:
            self.engine.say(text)

        self.engine.runAndWait()

    # speech to text
    def listen(self):
        # manual input
        if self.manual:
            text = self.input()
        else:
            with self.microphone as source:
                audio = self.recognizer.listen(source)

                try:
                    text = self.recognizer.recognize_google(audio)
                except sr.UnknownValueError:
                    text = ""

        return text.lower()

    # manual input
    def input(self):
        print(yellow('[!] Manual Input'))
        text = input('>> ').lower()
        return text

    # confirm an action
    def confirm(self, message, loop=False):
        while True:
            # speak confirmation
            self.speak('Are you sure you want to ' + message)

            # get manual response
            if self.manual:
                response = self.input()
            # get speech response
            else:
                response = self.listen()

            # list words in response
            response = response.split(' ')


            # text given
            if response:
                outcome = ''
                # iterate words
                for word in response:
                    # iterate all response types (yes, no, etc.)
                    for key in self.responses:
                        # response type is accepted
                        if key in ['yes', 'no']:
                            # all responses for type
                            for val in self.responses[key]:
                                # response is the same as the current word
                                if val == word:
                                    outcome = key

            try:
                if outcome == 'yes':
                    return 1
                elif outcome == 'no':
                    return 0
                else:
                    self.speak('Please answer with yes or no')
            # no text given
            except NameError:
                pass

            # don't loop
            if not loop:
                break


    # create new ability template
    def ability(self, name):
        # get Kara's path (so templating works with integration)
        absPath = os.path.abspath(os.path.dirname(__file__))

        print(yellow('[!] Making Directory...'))

        # make ability
        try:
            os.mkdir(name)
        except FileExistsError:
            # error message
            return 1

        print(yellow('[!] Referencing Templates...'))

        # Copy Template Files
        # main.py
        shutil.copyfile(absPath + '/Data/Templates/Ability/main.py',
                        name + '/main.py')
        # config.json
        shutil.copyfile(absPath + '/Data/Templates/Ability/config.json',
                        name + '/config.json')
        # requirements.txt
        shutil.copyfile(absPath + '/Data/Templates/Ability/requirements.txt',
                        name + '/requirements.txt')


        return 0


    # init new integration
    def integration(self):
        # get Kara's path (so Kara can be called from anywhere)
        absPath = os.path.abspath(os.path.dirname(__file__))

        print(yellow('\n[!] Creating Default Paths...'))
        # make default paths
        try:
            # abilities
            os.mkdir('Abilities')
        except FileExistsError:
            # error message
            print(red('[!] Abilities Path Already Exists!'))

        try:
            # cache
            os.mkdir('Cache')

            print(yellow('[!] Creating Cache...'))

            # write empty ability cache file
            with open('Cache/abilities.json', 'w') as file:
                file.write('{}') # empty json
        except FileExistsError:
            # error message
            print(red('[!] Cache Path Already Exists!'))


        print(yellow('[!] Referencing Templates...'))

        # config.json
        shutil.copyfile(absPath + '/Data/Templates/Integration/config.json', 'config.json')
        # main.py
        shutil.copyfile(absPath + '/Data/Templates/Integration/main.py', 'main.py')

        print(green('\n[+] Successfully Instanced New Integration!'))


    # compile given text to find relevant command to execute
    def compile(self, text):
        # no text given
        if not text:
            self.speak('Sorry, I didn\'t get that')
            return

        # read all logged abilities
        with open(self.cachePath + 'commands.json', 'r') as log:
            commands = json.load(log) # parse json

            # iterate abilities and their commands to find correct response
            for command in commands:
                # command match found
                match = False

                # use exact value
                if 'exact' in command:
                    # given as string
                    if isinstance(command['exact'], str):
                        # string matches command
                        if command['exact'] == text:
                            match = True
                    else:
                        # given as list
                        for val in command['exact']:
                            if val == text:
                                match = True
                                break

                # keywords exist and match wasn't already found
                if 'keywords' in command and not match:
                    # check command's keywords against given text
                    for keywords in command['keywords']:
                        # use True as default for greater efficency
                        match = True

                        # iterate all keywords
                        for keyword in keywords.split(' '):
                            # keyword doesn't match
                            if not keyword in text.split(' '):
                                match = False
                                break

                        # keywords match
                        if match:
                            break

                # check if a match was detected
                if match:
                    # default new "last" as failed message
                    last = 'failed'

                    # target given
                    if 'target' in command:
                        func = command['target']
                        # "last" command
                        last = 'self.link.{}(self, text)'.format(func)
                        # pass Kara and command to command
                        exec(last)
                    else:
                        print(red('\n[!] No Target Specified For Command!'))

                    # don't log a repeat command (causes a weird infinite loop)
                    if not '.repeat(' in last:
                        # log command for "repeat"
                        with open(self.cachePath + 'last.txt', 'w') as file:
                            # write executable code for repeat function()
                            file.write('Kara.link.{}(Kara, \"{}\")'.format(func, text))

                    return

        # no matches
        # execute fallback command
        with open(self.cachePath + 'fallback.txt') as last:
            # get fallback command
            fallback = last.readline()

            # no fallback given
            if not fallback:
                self.speak('Sorry, I don\'t know that')
                return

            # run fallback func
            exec(fallback)
