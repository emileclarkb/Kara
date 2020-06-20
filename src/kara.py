# Kara launcher

# ASSETS
# native
import sys
import subprocess
import os
# kara
from Core.core import Kara
from Core.compiler import compile
from Core.Scripts.handler import argHandle
from Core.Scripts.colors import green, yellow
from Core.Scripts.setup import setup



def main():
    # instance kara
    kara = Kara()

    # default args value
    args = {'manual': '', 'recompile': 1}
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
        compile()

    # system progress
    print(yellow('[!] Reloading Linking File...'))
    kara.reload()

    # using speech
    if not args['manual']:
        # finish booting
        with open('Core/Data/boot.txt', 'r') as logo:
            print(logo.read()) # logo


    # infinite listening
    while True:
        # compile text not speech
        if args['manual']:
            kara.compile(args['manual'])
            break

        # listen for input
        text = kara.listen()

        # wake word in input
        for word in kara.wake:
            # wake word detected in text
            if word in text:
                # format text
                text = text.split('kara')[-1].strip()

                # speak result of input
                kara.compile(text)

                # listen again
                break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
