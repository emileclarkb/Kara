# Kara launcher

# ASSETS
# native
import sys
import subprocess
import os
import time
# kara
from Kara.Core.core import Kara
from Kara.Core.compiler import compile
from Kara.Core.Scripts.handler import argHandle
from Kara.Core.Scripts.colors import green, yellow
from Kara.Core.Scripts.setup import setup



def main():
    # time comparison
    start = time.time()

    # ability and cache paths
    abPath = 'Kara/Core/Abilities/'
    cPath = 'Kara/Core/Data/Cache/'

    # instance kara
    kara = Kara(abilitiesPath=abPath, cachePath=cPath)

    # default args value
    args = {'manual': '', 'recompile': 1, 'time': 0}
    # handle arguements
    if len(sys.argv) > 1:
        # skip first arguement (*.py)
        args = argHandle(kara, sys.argv[1:])



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
    if not args['manual']:
        # finish booting
        with open('Kara/Core/Data/boot.txt', 'r') as logo:
            print(logo.read()) # logo


    # infinite listening
    while True:
        # compile text not speech
        if args['manual']:
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

        # wake word in input
        for word in kara.wake:
            # wake word detected in text
            if word in text:
                # format text
                text = text.split('kara')[-1].strip()

                # run through Kara
                kara.compile(text)

                # listen again
                break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
