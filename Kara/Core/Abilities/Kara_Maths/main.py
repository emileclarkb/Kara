import math

# acceptable math terms
accepted = '+-/**'
# acceptable special strings
functions = ['math.sin(', 'math.cos(', 'math.tan(']
special = ['math.pi']
special += functions

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
            if word in functions:
                func += 1
            # not currently a function and functions previous
            elif func:
                # end functions
                eq += ')' * func + ' '
                func = 0


    # evaluate string and round to four decimal places
    try:
        answer = eval(eq)
    except ZeroDivisionError:
        Kara.speak('no')
        return


    # format equation again for speech
    # *, /, math.pi,
    speech = ' ' + eq + ' '
    speech = speech.replace(' + ', ' plus ')
    speech = speech.replace(' - ', ' subtract ')
    speech = speech.replace(' * ', ' times ')
    speech = speech.replace(' / ', ' divided by ')
    speech = speech.replace(' ** 2 ', ' squared ')
    speech = speech.replace(' ** 3 ', ' cubed ')
    speech = speech.replace(' ** ', ' to the power of ')
    speech = speech.replace('(', '')
    speech = speech.replace(')', '')
    speech = speech.replace(' math.pi ', ' pi ')
    speech = speech.replace(' math.sin ', ' the sine of ')
    speech = speech.replace(' math.cos ', ' the cosine of ')
    speech = speech.replace(' math.tan ', ' the tangent of ')
    

    # round answer
    # scientific notation
    if 'e' in str(answer):
        answer = '{:0.4e}'.format(answer)
    # decimal
    else:
        answer = round(answer, 4)

    # temporarily conver to string
    answer = str(answer)
    # say negative instead of minus
    negative = ''
    # answer is negative
    if answer[0] == '-':
        negative = 'negative '
        # convert answer to positive and back to int
        answer = answer[1:]

    Kara.speak('{} is {} {}'.format(speech, negative, answer))
