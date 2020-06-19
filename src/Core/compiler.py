# native
import os
import pathlib
import json
# kara
from Core.Scripts.colors import *


# main compilation process
def deepCompile(abilities):
    incorrect = {}

    # Paths
    # abilities main
    path = 'Core/Abilities/'
    # abilities stored in one place after compile
    logPath = 'Core/Data/abilities.json'

    # json to dump into abilities.json
    abilitiesJSON = {}

    # all abilities changed
    changes = []

    # iterate abilities
    for ability in abilities:
        # everything incorrect with the ability
        issues = []

        # config.json path
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

                # path to requirements
                requirePath = path + ability + '/' + configJSON['requirements']
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
                    # add working ability to list
                    abilitiesJSON[ability] = configJSON

                    # read previously logged configuration
                    with open(logPath, 'r') as log:
                        logJSON = json.load(log) # parse json

                        #abililty doesn't exist
                        try:
                            # no changes were made
                            # (compare current config file to previous log)
                            if configJSON == logJSON['Ability']:
                                continue # next ability
                        except KeyError:
                            changes.append(ability) # log change


                    '''
                    # read requirements source
                    with open(requirePath, 'r') as src:
                        # target path
                        path = 'Core/Data/Require/Abilities/'
                        # write requirements target
                        with open(path + ability + '.txt', 'w') as target:
                            target.write(src.read())
                    '''
        else:
            # issue encounter
            issues.append('conf')

        # if issues were raised
        if issues:
            # log incorrect interaction
            incorrect[ability] = issues

    # log compiled ability data
    with open(logPath, 'w') as log:
        # dump json to file
        json.dump(abilitiesJSON, log,
                  sort_keys=True, indent=4, separators=(',', ': '))

    return incorrect, changes


# error handling compilation process
def compile():
    # abilities path
    path = 'Core/Abilities/'

    # get abilities
    abilities = os.listdir(path)

    # quick check for errors
    errors, changes = deepCompile(abilities)

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
