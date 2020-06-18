# Arguement Handling

# Native
import sys
# Kara
from Core.compiler import compile
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
    argReturn = {}

    # looking for a value
    current = ''
    # all commands
    commands = ['-h', '--help', '-i', '--init', '-v', '--validate',
                '-s', '--setup']

    for arg in args:
        # searching for a value of an arguement (ie. --init VALUE)
        if current:
            # value passed was a command
            if current in commands:
                # error message
                print(red('\n[-] Cannot Pass Value \"' + arg + \
                '\" to Arguement \"' + current + '\"'))
            # create new ability
            if '--' + current in commands[2:4]:
                result = kara.abilityTemp(arg)
                if result:
                    print(red('\n[-] Failed To Template New Ability: ' + \
                    'Directory Already Exists'))
                else:
                    print(green('\n[+] Template Successful! New Ability Created'))

            # reset current
            current = ''


        # read usage
        if arg in commands[0:2]:
            usage()
        # create new ability
        elif arg in commands[2:4]:
            # look for a value to use as ability name
            current = 'init'
        # validate abilities integrity
        elif arg in commands[4:6]:
            compile()
        # download required modules
        elif arg in commands[6:8]:
            setup('Core/Data/requirements.txt')

    # end
    if exit:
        sys.exit(1)
    else:
        # return arg data
        return argReturn
