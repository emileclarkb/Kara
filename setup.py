# PyPi setup

import pathlib
from setuptools import setup
import Kara
# current path
path = pathlib.Path(__file__).parent

# read README
with open(path / 'README.md', 'r') as file:
    README = file.read()

# setup package
setup(
    name = 'Kara',
    version = Kara.__version__,
    description = 'Modular and Fully Customizable Virtual Assistant',
    long_description = README,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/emileclarkb/Kara',
    author = 'Emile Clark-Boman',
    author_email = 'eclarkboman@gmail.com',
    license = 'GPLv3',
    classifiers = [
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent'
    ],
    packages = ['Kara'],
    include_package_data = True,
    keywords = ['voice', 'alexa', 'siri', 'cortana', 'google', 'assistant',
                'customize', 'recognition', 'assistant', 'control', 'commands',
                'artificial', 'intelligence'],
    entry_points = {
        'console_scripts': [
            'kara = Kara.__main__:main',
        ]
    },
    python_requires = '>=3.0'
)
