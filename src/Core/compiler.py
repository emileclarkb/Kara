# native
import os
import pathlib
import json
# kara
from Core.Scripts.colors import *

path = 'Core/Abilities/'

# confirm if changes were made
def quickCheck(abilities):
    incorrect = {}

    # iterate abilities
    for ability in abilities:
        # everything incorrect with the ability
        issues = []

        configPath = path + ability + '/config.json'

        # get ability files
        config = pathlib.Path(configPath)
        if config.is_file():
            # parse json
            with open(configPath, 'r') as file:
                configJSON = json.load(file) # parse json

                # read correct main file
                main = pathlib.Path(path + ability + '/' + configJSON['main'])
                # main doesn't exists
                if not main.is_file():
                    # issue encounter
                    issues.append('main')

                # requirement file given
                if configJSON['requirements']:
                    # read correct main file
                    require = pathlib.Path(path + ability + '/' +
                    configJSON['requirements'])
                    # requirements doesn't exists
                    if not require.is_file():
                        # issue encounter
                        issues.append('req')
        else:
            # issue encounter
            issues.append('conf')

        # if issues were raised
        if issues:
            # log incorrect interaction
            incorrect[ability] = issues
    return incorrect

def compile():
    # get abilities
    abilities = os.listdir(path)

    # quick check for errors
    errors = quickCheck(abilities)

    # error encounted
    if errors:
        # each ability that encounted errors
        for ability in errors:
            # list all abilities that failed
            print(red('[-] \"' + ability + '\" Ability Failed to Compile!'))
            for e in errors[ability]:
                # expand on error message
                if e == 'conf':
                    print(white('    ~ No Config File Found!'))
                elif e == 'req':
                    print(white('    ~ Requirements Linked But Not Found!'))
                elif e == 'main':
                    print(white('    ~ Main Not Found, Entry Failed!'))
            print() #empty line

    else:
        # no errors encountered
        print(green('[+] Successfully Compiled Abilities!'))
