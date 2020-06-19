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

    # handle arguements
    if len(sys.argv) > 1:
        # skip first arguement (*.py)
        args = argHandle(kara, sys.argv[1:])

    # system progress
    print(green('\n[+] Arguements Active!'))
    print(yellow('[!] Compiling Abilities...'))
    # check file credibility
    compile()

    # system progress
    print(yellow('[!] Reloading Linking File...'))
    kara.reload()

    print(yellow('[!] Listening'))
    # infinite listening
    while True:
        text = kara.listen()

        for word in kara.wake:
            # wake word detected in text
            if word in text:
                # format text
                text = text.split('kara')[-1].strip()

                # speak result of input
                kara.compile(text)

                # exit for loop
                break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
