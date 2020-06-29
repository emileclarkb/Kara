# Arguement Handling

# Native
import os
import sys
import json
# Kara
from Kara.Core.core import Kara
from Kara.Core.compiler import compile
from Kara.Core.Scripts.colors import *
from ...__init__ import __version__


# Kara usage
def usage(path):
    # read usage
    with open(path + 'usage.txt', 'r') as file:
        # return usage to screen
        print('\n' + white(file.read()))

# main handler
def argHandle(kara, args):
    # exit the booting process once args handled
    exit = True
    # arguements to return to Kara
    argReturn = {'manual': 0, 'recompile': 1, 'time': 0, 'debugTime': 0,
                 'text': 0}

    # no arguements given
    if not len(args):
        return argReturn

    # looking for a value
    current = {'value': '', 'optional': False}
    # all commands
    commands = ['-h', '--help', '-a', '--ability', '-r', '--recompile',
                '-c', '--cached', '-v', '--version', '-m', '--manual',
                '-t', '--time', '-i', '--init', '-s', '--speech',
                '-p', '--path']

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
                result = kara.ability(arg)
                if result:
                    print(red('\n[-] Failed To Template New Ability: ' + \
                    'Directory Already Exists'))
                else:
                    print(green('\n[+] Template Successful! New Ability Created'))
            # recompile abilities
            elif current['value'] == 'recompile':
                # skip compilation process
                if arg == '0':
                    argReturn['recompile'] = 0
                    exit = False # continue booting
                # anything else given
                else:
                    # compile through Kara's given paths
                    compile(abilitiesPath=kara.abilitiesPath,
                            cachePath=kara.cachePath)
            # manual compile text
            elif current['value'] == 'manual':
                # add text to return
                argReturn['manual'] = arg
                exit = False
            # time Kara
            elif current['value'] == 'time':
                # skip compilation process
                if arg == '1':
                    argReturn['debugTime'] = 1

            # reset current
            current['value'] = ''


        # read usage
        if arg in commands[0:2]:
            # remove 'Cache/' from end
            usage(kara.cachePath[:-6])
        # create new integration
        elif arg in commands[2:4]:
            # look for a value to use as ability name
            current['value'] = 'init'
        # recompile abilities
        elif arg in commands[4:6]:
            current['value'] = 'recompile'
            current['optional'] = True
        # clear cache files
        elif arg in commands[6:8]:
            # write empty braces to indict blank json file
            # no data causes json.load to raise errors
            f = open(kara.cachePath + 'abilities.json', 'w')
            f.write('{}')
            f.close()
            # empty command data
            f = open(kara.cachePath + 'commands.json', 'w')
            f.write('{}')
            f.close()
            # write nothing to file (wipe it)
            open(kara.cachePath + 'link.py', 'w').close()
            # write nothing to file (wipe it)
            open(kara.cachePath + 'last.txt', 'w').close()
            print(green('\n[+] Cleared Cached Data!'))
        # display current version
        elif arg in commands[8:10]:
            print('Kara ' + __version__)
        # skip voice step and use text instead
        elif arg in commands[10:12]:
            # look for value
            current['value'] = 'manual'
        # time Kara
        elif arg in commands[12:14]:
            # look for supporting value
            current['value'] = 'time'
            current['optional'] = True
            # start timing
            argReturn['time'] = 1
            exit = False
            ''' Note: look into "optional" '''
        # init new integration
        elif arg in commands[14:16]:
            kara.integration()
        # print speech text detected
        elif arg in commands[16:18]:
            # return message to print
            argReturn['text'] = 1
            exit = False
        # print package path
        elif arg in commands[18:20]:
            # get path
            path = os.path.dirname(os.path.abspath(__file__))

            # print info
            print(green('\nPackage Path:'))
            print(white(path[:-13]))
        # unknown arguement
        else:
            # if no arguement given (ie. "")
            if arg:
                if arg[0] == '-':
                    print(red('\n[-] Unkown Arguement \"' + arg + '\"! Try -h For Help'))


    # on exitting check to see if nothing was ever passed to arguements
    # recompile abilities
    if current['value'] == 'recompile':
        print(yellow('\n[!] Forcing Compilation...'))
        compile(abilitiesPath=kara.abilitiesPath, cachePath=kara.cachePath)

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
