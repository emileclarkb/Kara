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
functionality or "Abilities". By default she has no features program directly into
her, all her capabilities come from stored Abilities,

Initializing an Ability is as simple as:
`python kara.py -i YOUR_ABILITY_NAME`

For more working with Abilities check out it's [documentation](Core/Data/Docs/abilities.md)!


## Arguements
- -h or --help: show Kara's usage
- -i or --init: initialize new Ability
- -r or --recompile: recompile abilities
- -s or --setup: download all requirements
- -l or --link: regenerate linking file
- -c or --cached: remove all cached data (abilities.json, link.py)
- -v or --version: display current version of Kara
- -m or --manual: pass text to Kara, temporarily disables STT
- -t or --time: show the time taken for Kara to complete a command (only works for manual entries)
