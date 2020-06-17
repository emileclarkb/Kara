# Kara launcher

# ASSETS
# native
import sys
import subprocess
import os
# kara
from Core.core import Kara
from Core.compiler import compile
from Core.handler import argHandle



def main():
    # instance kara
    kara = Kara()

    # only
    if len(sys.argv) > 1:
        # skip first arguement (*.py)
        argHandle(kara, sys.argv[1:])

    # check file credibility
    #compile()
    sys.exit(0)

    while True:
        text = kara.listen()

        for word in kara.wake:
            # wake word detected in text
            if word in text:
                # speak result of input
                kara.speak(kara.compile(text))

                # exit for loop
                break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
