import subprocess
import os

# download all modules given in a requirements file
def setup(path):
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
                subprocess.call('pip install ' + pkg, shell=True)
