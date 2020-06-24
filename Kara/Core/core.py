# Kara Object

# native
import os
import sys
import json
import importlib
import pathlib
import shutil
# 3rd Party
import pyttsx3
import speech_recognition as sr
# Kara
from Core.Scripts.colors import red, yellow, green


class Kara:
    def __init__(self, abilitiesPath='Abilities/', cachePath='Cache/'):
        # custom paths
        self.abilitiesPath = abilitiesPath
        self.cachePath = cachePath

        # wake words (my lisp sucks...)
        self.wake = ['kara', 'cara', 'kawa', 'cowra']

        # init engine and voices
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        # set properties
        self.engine.setProperty('rate', 125)
        self.engine.setProperty('volume', 1.0)
        self.engine.setProperty('voice', self.voices[1].id)

        # don't speak, just time how long abilities take to work
        self.debugTime = False

        # last command
        self.last = ''

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

            self.link = importlib.import_module('Core.Data.Cache.link')#cacheModule + 'link', package='Core')
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
    def template(self, name):
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
            os.mkdir('Ability')
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


    def compile(self, text):
        # read all logged abilities
        with open(self.cachePath + 'commands.json', 'r') as log:
            self.abilities = json.load(log) # parse json

        # iterate abilities and their commands to find correct response
        for command in self.abilities:
            # command match found
            match = False

            # use exact value
            if 'exact' in command:
                for val in command[exact]:
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
                        if not keyword in text:
                            match = False
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

                return 0
