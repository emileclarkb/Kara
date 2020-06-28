import subprocess
import os
from Kara.Core.Scripts.colors import red

# download all modules given in a requirements file
def setup(path):
    try:
        # read requirements
        with open(path, 'r') as file:
            # iterate lines
            for line in file.readlines():
                pkg = ''
                for char in line:
                    # comment support
                    if char == '#':
                        break
                    # correct pkg code on line
                    pkg += char
                # remove excess whitespace
                pkg = pkg.strip()
                # pkg not empty
                if pkg:
                    # install package
                    subprocess.call('python -m pip install ' + pkg, shell=True)
                    print() # empty trailing line
    # no access
    except PermissionError:
        print(red('\n[!] Permission Error Opening: \"' + path + '\"!'))
