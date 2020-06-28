# Kara launcher

# ASSETS
# native
import sys
import subprocess
import os
import time
# kara
from Core.core import *
from Core.compiler import *
from Core.Scripts.handler import *
from Core.Scripts.colors import *
from Core.Scripts.setup import *



def main():
    # time comparison
    start = time.time()

    # get path
    path = os.path.dirname(os.path.abspath(__file__))

    # ability and cache paths
    abPath = path + '/Core/Abilities/'
    cPath = path + '/Core/Data/Cache/'
    #abPath = 'Core/Abilities/'
    #cPath = 'Core/Data/Cache/'

    # instance kara
    kara = Kara(abilitiesPath=abPath, cachePath=cPath)

    # handler given arguements (excluding *.py)
    args = argHandle(kara, sys.argv[1:])

    # whether to debug time
    kara.debugTime = args['debugTime']

    # system progress
    print(green('\n[+] Arguements Active!'))
    # skip compilation
    if args['recompile']:
        print(yellow('[!] Compiling Abilities...'))
        # compile abilities
        compile(abilitiesPath=abPath, cachePath=cPath)

    # system progress
    print(yellow('[!] Reloading Linking File...'))
    kara.reload()

    # using speech
    if not isinstance(args['manual'], str):
        # finish booting
        with open(path + '/Core/Data/boot.txt', 'r') as logo:
            print(logo.read()) # logo


    # infinite listening
    while True:
        # compile text not speech
        # manual data given
        if isinstance(args['manual'], str):
            # run through Kara
            kara.compile(args['manual'])

            # log time taken
            if args['time']:
                # rounded time taken
                taken = round(time.time() - start, 3)
                # time taken to complete
                print(yellow("\n[!] Completed in: " + str(taken) + ' sec'))
            break

        # listen for input
        text = kara.listen()
        # print text heard
        if args['print']:
            print(text)

        # wake word in input
        for word in kara.wake:
            # wake word detected in text
            if word in text:
                # only "listen" once kara is said
                text = text.split(word)[-1].strip()

                # run through Kara
                kara.compile(text)

                # listen again
                break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
