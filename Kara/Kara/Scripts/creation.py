# native
import os
import pathlib
# Kara
from Kara.Kara.Scripts.colors import yellow, green


# create new ability template
def template(name, abilitiesPath='Abilities/', cachePath='Cache/'):
    # path to abilities
    path = abilitiesPath + name

    # make ability
    try:
        os.mkdir(path)
    except FileExistsError:
        # error message
        return 1

    # absolute path (so templating works with integration)
    absPath = os.path.abspath(os.path.dirname(__file__))

    # write main.py template
    with open(absPath + 'Data/Templates/main.py', 'r') as template:
        # write config
        with open(path + '/main.py', 'w') as file:
            # write template to main.py
            file.write(template.read())

    # write config.json file
    # open template
    with open(absPath + 'Data/Templates/config.json', 'r') as template:
        # write config
        with open(path + '/config.json', 'w') as file:
            # write template to config.json
            file.write(template.read())

    # write requirements.txt file
    # open template
    with open(absPath + 'Data/Templates/requirements.txt', 'r') as template:
        # write config
        with open(path + '/requirements.txt', 'w') as file:
            # write template to requirements.txt
            file.write(template.read())

    return 0


# init new integration
def integration(abilitiesPath='Abilities/', cachePath='Cache/'):
    print(green('\n[+] Creating Default Paths...'))
    # make default paths
    try:
        # abilities
        os.mkdir(abilitiesPath)
    except FileExistsError:
        # error message
        print(yellow('[!] Abilities Path Already Exists...'))
    try:
        # cache
        os.mkdir(cachePath)
    except FileExistsError:
        # error message
        print(yellow('[!] Cache Path Already Exists...'))

    print(green('[+] Creating Cache Files...'))

    # if file doens't exist
    # write empty json file
    with open(cachePath + 'abilities.json', 'w') as file:
        file.write('{}') # empty json

    print(green('\n[+] Successfully Instanced New Integration!'))
