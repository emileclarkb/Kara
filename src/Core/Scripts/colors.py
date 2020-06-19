# ASSETS
from sys import platform
from termcolor import colored


# on windows
if platform == 'win32':
    # install if not already
    import colorama
    # initialize
    colorama.init()

# print red text
def red(value):
    return colored(value, 'red', attrs=['bold'])
# print green text
def green(value):
    return colored(value, 'green', attrs=['bold'])
# print white text
def white(value):
    return colored(value, 'white', attrs=['bold'])
# print yellow text
def yellow(value):
    return colored(value, 'yellow', attrs=['bold'])
