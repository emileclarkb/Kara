# Arguement Handling

# Native
import sys
import json
# Kara
from Core.compiler import compile, link
from Core.Scripts.colors import *
from Core.Scripts.setup import setup


# Kara usage
def usage():
    # read usage
    with open('Core/Data/usage.txt', 'r') as file:
        # return usage to screen
        print('\n' + white(file.read()))

# main handler
def argHandle(kara, args):
    # exit the booting process once args handled
    exit = True
    # arguements to return to Kara
    argReturn = {'manual': '', 'recompile': 1}

    # looking for a value
    current = {'value': '', 'optional': False}
    # all commands
    commands = ['-h', '--help', '-i', '--init', '-r', '--recompile',
                '-s', '--setup', '-l', '--link', '-c', '--cache',
                '-v', '--version', '-m', '--manual']

    for arg in args:
        # searching for a value of an arguement (ie. --init VALUE)
        if current['value']:
            # value passed was a command (and value wasn't optional)
            if arg in commands and not current['optional']:
                # error message
                print(red('\n[-] Cannot Pass Value \"' + arg + \
                '\" to Arguement \"' + current['value'] + '\"'))

                # reset current
                current = ''
                break

            # create new ability
            if current['value'] == 'init':
                result = kara.abilityTemp(arg)
                if result:
                    print(red('\n[-] Failed To Template New Ability: ' + \
                    'Directory Already Exists'))
                else:
                    print(green('\n[+] Template Successful! New Ability Created'))
            # recompile abilities
            if current['value'] == 'recompile':
                # skip compilation process
                if arg == '0':
                    argReturn['recompile'] = 0
                    exit = False # continue booting
                # anything else given
                else:
                    compile()
            # add text to return
            elif current['value'] == 'manual':
                argReturn['manual'] = arg
                exit = False

            # reset current
            current['value'] = ''


        # read usage
        if arg in commands[0:2]:
            usage()
        # create new ability
        elif arg in commands[2:4]:
            # look for a value to use as ability name
            current['value'] = 'init'
        # recompile abilities
        elif arg in commands[4:6]:
            current['value'] = 'recompile'
            current['optional'] = True
        # download required modules
        elif arg in commands[6:8]:
            setup('Core/Data/requirements.txt')
        # force ability linking
        elif arg in commands[8:10]:
            # generate linking file
            link()
            print(green('\n[+] Generated Linking File!'))
        # clear cache files
            # write nothing to file (wipe it)
        elif arg in commands[10:12]:
            open('Core/Data/abilities.json', 'w').close()
            open('Core/Data/link.py', 'w').close()
        # display current version
        elif arg in commands[12:14]:
            with open('Core/Data/kara.json', 'r') as config:
                # get Kara version
                version = json.load(config)['version'] # parse json
                print('Kara ' + version)
        # skip voice step and use text instead
        elif arg in commands[14:16]:
            # look for value
            current['value'] = 'manual'


    # on exitting check to see if nothing was ever passed to arguements
    # recompile abilities
    if current['value'] == 'recompile':
        print(yellow('\n[!] Forcing Compilation...'))
        compile()

    # value never passed to arguement (and not optional)
    if current['value'] and not current['optional']:
        # error
        print(red('\n[-] No Supporting Value Passed to Arguement \"' +
                  current['value'] + '\"!'))
        sys.exit(1) # terminate

    # end
    if exit:
        sys.exit(1)
    else:
        # return arg data
        return argReturn
