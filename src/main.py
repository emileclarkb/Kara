# ASSETS
from kara import Kara

def main():
    # instance kara
    kara = Kara()

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
