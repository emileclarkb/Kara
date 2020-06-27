from random import choice, randint

greetings = ['hey', 'hi', 'hello', 'how\'s it going']
status = ['amazing', 'i\'m great today! How are you?', 'spectacular', 'better than ever']
thank = ['my pleasure', 'you\'re welcome', 'just doing my job', 'all good']
coin = ['heads', 'tails']

# hello
def greeting(Kara, command):
    Kara.speak(choice(greetings))

# how are you
def howru(Kara, command):
    Kara.speak(choice(status))

# thanks
def thanks(Kara, command):
    Kara.speak(choice(thank))

# repeat last command
def repeat(Kara, command):
    try:
        # read last file
        with open(Kara.cachePath + 'last.txt', 'r') as file:
            # get last command
            last = file.readline()

            # last command failed
            if last == 'failed':
                Kara.speak('Your last command failed')
            else:
                # execute command
                exec(last)
    except:
        Kara.speak('You haven\'t said anything yet')

# flip a coin
def coinflip(Kara, command):
    Kara.speak(choice(coin))

# roll a dice
def diceroll(Kara, command):
    Kara.speak(randint(1, 6))
