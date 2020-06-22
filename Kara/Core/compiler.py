# native
import os
import pathlib
import json
# kara
from Kara.Core.Scripts.colors import *
from Kara.Core.Scripts.setup import setup


# main compilation process
def deepCompile(abilities, abilitiesPath='Abilities/', cachePath='Cache/'):
    incorrect = {}

    # json to dump into abilities.json
    abilitiesJSON = {}

    # all abilities changed
    changes = {}

    # iterate abilities
    for ability in abilities:
        # everything incorrect with the ability
        issues = []

        # init ability's changes
        changes[ability] = []

        # config.json path
        configPath = abilitiesPath + ability + '/config.json'

        # get ability files
        config = pathlib.Path(configPath)
        if config.is_file():
            # parse json
            with open(configPath, 'r') as file:
                configJSON = json.load(file) # parse json

                # read correct main file
                main = pathlib.Path(abilitiesPath + ability + '/' + configJSON['main'])
                # main doesn't exists
                if not main.is_file():
                    # issue encounter
                    issues.append('main')

                # path to requirements
                requirePath = abilitiesPath + ability + '/' + configJSON['requirements']
                # requirement file given
                if configJSON['requirements']:
                    # read correct requirements file
                    require = pathlib.Path(requirePath)
                    # requirements doesn't exists
                    if not require.is_file():
                        # issue encounter
                        issues.append('req')


                # if no issues were raised
                if not issues:
                    # if ability has atleast one command
                    if configJSON['commands']:
                        # specific parts of config file to dump
                        # ignore name, description, etc.
                        dump = {'version': configJSON['version'],
                                'main': configJSON['main'],
                                'requirements': configJSON['requirements'],
                                'commands': configJSON['commands']}

                        # add working ability to list
                        abilitiesJSON[ability] = dump

                        # change detection
                        # read previously logged configuration
                        with open(cachePath + 'abilities.json', 'r') as log:
                            logJSON = json.load(log) # parse json

                            #abililty doesn't exist
                            try:
                                # values that should be shared
                                shared = ['version', 'main', 'requirements', 'commands']

                                # no changes were made
                                # (compare current config file to previous log)
                                if configJSON == logJSON[ability]:
                                    continue # next ability

                                # iterate all shared attributes
                                for attr in shared:
                                    # is not shared
                                    if not configJSON[attr] == logJSON[ability][attr]:
                                        changes[ability].append(attr) # log change

                            except KeyError:
                                changes[ability].append('Added Ability') # log change
        else:
            # issue encountered (config file doesn't exist)
            issues.append('conf')

        # if issues were raised
        if issues:
            # log incorrect interaction
            incorrect[ability] = issues

        # no changes occured
        if not changes[ability]:
            # remove empty list
            del changes[ability]

    # log compiled ability data
    with open(cachePath + 'abilities.json', 'w') as log:
        # dump json to file
        # arguements given make the json file look neat and structured
        json.dump(abilitiesJSON, log,
                  sort_keys=True, indent=4, separators=(',', ': '))

    return incorrect, changes


# generate linking file
def link(abilitiesPath='Abilities/', cachePath='Cache/'):
    # write linking file
    with open(cachePath + 'link.py', 'w') as link:
        # read logged abilities
        with open(cachePath + 'abilities.json', 'r') as log:
            abilities = json.load(log) # parse json

            # iterate abilities and their commands
            for ability in abilities:
                for command in abilities[ability]['commands']:
                    # get main file and format for an import statement
                    main = abilities[ability]['main']
                    main = main.split('.')[0] # "file.py" -> "file"

                    # "Kara/Abilities/" -> "Kara.Abilities."
                    module = '.'.join(abilitiesPath.split('/'))

                    line = 'from {}{}.{} import {}'.format(module, ability, main,
                           abilities[ability]['commands'][command]['target'])
                    link.write(line + '\n') # write import link


# compress abilities to increase speed
def compress(cachePath='Cache/'):
    # read abilities
    with open(cachePath + 'abilities.json', 'r') as abilities:
        JSON = json.load(abilities) # parse json

        # condensed json file to write to commands
        compressed = []

        # find all commands in find
        for ability in JSON:
            for command in JSON[ability]['commands']:
                # add command
                compressed.append(JSON[ability]['commands'][command])

        # write compressed json
        with open(cachePath + 'commands.json', 'w') as commands:
            # neatly dump data
            json.dump(compressed, commands,
                      sort_keys=True, indent=4, separators=(',', ': '))

# error handling compilation process
def compile(abilitiesPath='Abilities/', cachePath='Cache/'):
    # ability and cache path were implement for (and will only change when)
    # using integrating Kara

    # get abilities
    abilities = os.listdir(abilitiesPath)

    # quick check for errors
    errors, changes = deepCompile(abilities,
                      abilitiesPath=abilitiesPath, cachePath=cachePath)


    # changes detected
    if changes:
        print(yellow('[!] Installing Requirements...\n'))

        # formatted changes to print
        formatted = []

        # iterate changes
        for ability in changes:
            # ability has no changes
            if not changes[ability]:
                continue

            # add ability to formatted text
            formatted.append('    ~ ' + ability)

            # iterate ability's changes
            for change in changes[ability]:
                # add change to formatted text
                formatted.append('        - ' + change)

            # install requirements of changed Ability
            # read config file
            with open(abilitiesPath + ability + '/config.json', 'r') as config:
                # get requirements file
                require = json.load(config)['requirements'] # parse json
                # setup correct requirements
                setup(abilitiesPath + ability + '/' + require)

        # format changes
        print(yellow('\n[!] Ability Changes Were Detected!'))
        print(white('\n'.join(formatted)))
        print() # empty line
    else:
        print(green('[+] No Ability Changes Detected!'))

    # error encounted
    if errors:
        # each ability that encounted errors
        for ability in errors:
            # list all abilities that failed
            print(red('\n[-] \"' + ability + '\" Ability Failed to Compile!'))
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

    # generate compressed ability file
    compress(cachePath=cachePath)
    print(green('[+] Compressed Abilities File!'))

    # generate linking file
    link(abilitiesPath=abilitiesPath, cachePath=cachePath)
    print(green('[+] Generated Linking File!'))
