from random import choice

greetings = ['hey', 'hi', 'hello', 'how\'s it going']
status = ['amazing', 'i\'m great today! How are you?', 'spectacular', 'better than ever']
thank = ['my pleasure', 'you\'re welcome', 'just doing my job', 'all good']

# hello
def greeting(Kara, command):
    Kara.speak(choice(greetings))

# how are you
def howru(Kara, command):
    Kara.speak(choice(status))

# thanks
def thanks(Kara, command):
    Kara.speak(choice(thank))
