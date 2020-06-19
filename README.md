# Kara

## Description
Simply put, Kara is a voice assistant that steals 0% of your data so you stay free!
She is a actively maintained, modular, and designed to customize.

The bones of this project was built in 4 days as a challenge (Jun 15, 2020 - Jun 19, 2020),
however I have decided to continue production while also maintaining other projects.
Currently Kara does not have many "Abilities" though many are planned for release within
the next weeks!

## Installation
`python kara.py -s`
or
`python kara.py --setup`
## Abilities

Kara is designed specifically to be modified by the community and given additional
functionality or "Abilities".

initializing an Ability is as simple as:
`python kara.py -i YOUR_ABILITY_NAME`

Abilities are stored within `Core/Abilities`, an entire Ability will already be
templated once it is initialized. It's up to you to give it a purpose!


## Arguements
- -h or --help: show Kara's usage
- -i or --init: initialize new Ability
- -v or --validate: validate ability integrity
- -s or --setup: download all requirements
- -l or --link: regenerate linking file
- -c or --cache : remove all cached data (abilities.json, link.py)
