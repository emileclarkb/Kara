import subprocess

# download all modules given in a requirements file
def setup(path):
    requirements = []

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
                requirements.append(pkg)

    # install given package
    for package in requirements:
        subprocess.call('pip install ' + package, shell=True)
