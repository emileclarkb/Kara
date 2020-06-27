import math

# acceptable math terms
accepted = '+-/**'


# perform math operations
# format command to become an equation
def maths(Kara, command):
    # add blank whitespace to front and back
    command = ' ' + command + ' '

    # replace strings with acceptable python
    command = command.replace(' x ', ' * ')
    command = command.replace(' pi ', ' math.pi ')
    command = command.replace(' ^ ', ' ** ')
    command = command.replace(' squared ', ' ** 2 ')
    command = command.replace(' cubed ', ' ** 3 ')

    eq = ''

    # remove unnecessary "words"
    for word in command.split():
        # is acceptable
        if word == 'math.pi' or word in accepted or word.isdigit():
            # add padding (white space)
            eq += word + ' '

    # evaluate string and round to four decimal places
    answer = eval(eq)
    answer = round(answer, 4)

    # format equation again for speech
    # *, /, math.pi,
    speech = ' ' + eq + ' '
    speech = speech.replace(' * ', ' times ')
    speech = speech.replace(' math.pi ', ' pi ')
    speech = speech.replace(' / ', ' divided by ')
    speech = speech.replace(' ** 2 ', ' squared ')
    speech = speech.replace(' ** 3 ', ' cubed ')
    speech = speech.replace(' ** ', ' to the power of ')

    Kara.speak(speech + ' is ' + str(answer))
