# native
import os
import pathlib
import json
# kara
from Core.Scripts.colors import *
from Core.Scripts.setup import setup

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

                # check what keys given in config file
                # required fields
                keyRequire = ['name', 'version', 'author', 'description', 'main']

                # all config keys
                keys = list(configJSON.keys())

                keyErrors = []

                # check which key fields exist
                # required fields
                for key in keyRequire:
                    # not found
                    if not key in keys:
                        keyErrors.append(key)

                # config key errors found
                if keyErrors:
                    # error statement
                    print(red('\n[-] Config Keys Were Not Detected For ' +
                              '\"' + ability + '\"!'))
                    print(yellow('[!] Ability May Not Function As Expected...'))

                    # indent
                    print(red((' ' * 4) + 'Required:'))
                    # list errors
                    for error in keyErrors:
                        print(red((' ' * 8) + '~ ' + error))
                    # empty line
                    print()

                    # remove change data
                    del changes[ability]
                    continue


                # read correct main file
                main = pathlib.Path(abilitiesPath + ability + '/' + configJSON['main'])
                # main doesn't exists
                if not main.is_file():
                    # issue encounter
                    issues.append('main')

                try:
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
                except:
                    # file has no requirements
                    pass

                # if no issues were raised
                if not issues:
                    # if ability has atleast one command
                    if configJSON['commands']:
                        # specific parts of config file to dump
                        # ignore name, description, etc.
                        dump = {'version': configJSON['version'],
                                'main': configJSON['main'],
                                'commands': configJSON['commands']}

                        # try to add requirements
                        try:
                            dump['requirements'] = configJSON['requirements']
                        except:
                            # file has no requirements
                            pass

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

                            except KeyError as e:
                                # if it's requirement related do nothing
                                if str(e) != '\'requirements\'':
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
                    module = abilitiesPath.replace('/', '.')
                    module = module.replace('\\', '.')
                    # current path
                    current = os.path.dirname(os.path.abspath(__file__))
                    current = current.replace('/', '.')
                    current = current.replace('\\', '.')

                    # remove full directory to leave relative path to Abilities
                    module = module.replace(current, '')
                    try:
                        line = 'from ..{}{}.{} import {}'.format(module, ability, main,
                               abilities[ability]['commands'][command]['target'])
                        link.write(line + '\n') # write import link
                    # no target given
                    except KeyError:
                        pass


# store fallback command
def fallback(abilitiesPath='Abilities/', cachePath='Cache/'):
    # write fallback file
    with open(cachePath + 'fallback.txt', 'w') as file:
        # read logged abilities
        with open(cachePath + 'commands.json', 'r') as log:
            commands = json.load(log) # parse json

            # all fallback commands given
            fallbacks = []

            # iterate commands
            for command in commands:
                #print(commands)
                # fallback given
                if 'fallback' in command:
                    # is fallback
                    if command['fallback']:
                        fallbacks.append(command)

            # multiple fallbacks given
            if len(fallbacks) > 1:
                print(red('\n[-] Multiple Fallback Commands Given!'))
                print(yellow('[!] Using First Fallback as Default...\n'))
            # no fallback given
            elif not len(fallbacks):
                # write empty
                file.write('')
                return

            # write executable command
            file.write('self.link.{}(self, text)'.format(fallbacks[0]['target']))





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
                # get all data on command
                commandData = JSON[ability]['commands'][command]
                # target given
                if 'target' in commandData:
                    # add command
                    compressed.append(JSON[ability]['commands'][command])
                # no target given
                else:
                    print(red('\n[-] No Target Given For Command \"' +
                          command + '\"!'))
                    print(yellow('[!] Skipping Command...\n'))


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
                try:
                    # get requirements file
                    require = json.load(config)['requirements'] # parse json
                    # setup correct requirements
                    if require:
                        setup(abilitiesPath + ability + '/' + require)
                except:
                    # no requirements
                    pass


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

    # generate fallback file
    fallback(abilitiesPath=abilitiesPath, cachePath=cachePath)
    print(green('[+] Generated Fallback Data!'))
