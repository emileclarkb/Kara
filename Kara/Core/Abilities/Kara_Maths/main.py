import math

# acceptable math terms
accepted = '+-/**'
# acceptable special strings
special = ['math.pi', 'math.sin(', 'math.cos(', 'math.tan(']

# root (special: square, cube)
# sign cosine tangent

# perform math operations
# format command to become an equation
def generalMaths(Kara, command):
    # add blank whitespace to front and back
    command = ' ' + command + ' '

    # replace strings with acceptable python
    command = command.replace(' x ', ' * ')
    command = command.replace(' pi ', ' math.pi ')
    command = command.replace(' sign ', ' math.sin( ')
    command = command.replace(' cosine ', ' math.cos( ')
    command = command.replace(' tangent ', ' math.tan( ')
    command = command.replace(' ^ ', ' ** ')
    command = command.replace(' squared ', ' ** 2 ')
    command = command.replace(' cubed ', ' ** 3 ')

    eq = ''

    # last amount of words that were functions
    func = 0

    # remove unnecessary "words"
    for word in command.split():
        # is acceptable
        if word in special or word in accepted or word.isdigit():
            # add padding (white space)
            eq += word + ' '

            # function discovered
            if word in special:
                func += 1
            # not currently a function and functions previous
            elif func:
                # end functions
                eq += ')' * func


    # evaluate string and round to four decimal places
    try:
        answer = eval(eq)
        answer = round(answer, 4)
    except ZeroDivisionError:
        Kara.speak('no')
        return


    # format equation again for speech
    # *, /, math.pi,
    speech = ' ' + eq + ' '
    speech = speech.replace(' * ', ' times ')
    speech = speech.replace(' math.pi ', ' pi ')
    speech = speech.replace(' / ', ' divided by ')
    speech = speech.replace(' ** 2 ', ' squared ')
    speech = speech.replace(' ** 3 ', ' cubed ')
    speech = speech.replace(' ** ', ' to the power of ')
    speech = speech.replace('(', '')
    speech = speech.replace(')', '')
    speech = speech.replace(' math.sin ', ' sine of ')
    speech = speech.replace(' math.cos ', ' cosine of ')
    speech = speech.replace(' math.tan ', ' tangent of ')

    Kara.speak(speech + ' is ' + str(answer))
