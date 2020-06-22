# Kara

![Kara Logo](/design/logo.png)

## Description
Simply put, Kara is a voice assistant that steals 0% of your data so you stay free!
She is a actively maintained, modular, and designed to customize.

The bones of this project was built in 4 days as a challenge (Jun 15, 2020 - Jun 19, 2020),
however I have decided to continue production while also maintaining other projects.
Currently Kara does not have many "Abilities" though many are planned for release within
the next weeks!

If you're interested in supporting, adding to, or using the project check out
our [official server](https://discord.gg/7hK6PFT)! I'm always online and happy
to help people.

## Installation
`python kara.py -s`
or
`python kara.py --setup`

## Integrations

Sometimes you don't want Kara to control everything and instead want to control
how she acts that little bit more, this is why Integrations exist. Integrations
allow you to quickly and efficiently control Kara's functionality through any
of your projects.

Initializing a new integration is as simple as:
`python kara.py -i`

Integrations are different from Abilities. Imagine it like it this, Abilities give
Kara functionality and allow her to perform and control new commands.
Integrations allow Kara to work inside of your project and hand the controller
over to it too. This means you can have greater control of how she performs tasks.

For more on working integrating Kara check out it's
[documentation](src/Kara/Data/Docs/integrations.md)!

## Abilities

Kara is designed specifically to be modified by the community and given additional
functionality or "Abilities". By default she has no features program directly into
her, all her capabilities come from stored Abilities.

Initializing an Ability is as simple as:
`python kara.py -a YOUR_ABILITY_NAME`

For more on working with Abilities check out it's
[documentation](src/Kara/Data/Docs/abilities.md)!


## Arguements
- `-h` or `--help`: show Kara's usage
- `-a` or `--ability`: initialize new Ability
- `-r` or `--recompile`: recompile abilities
- `-s` or `--setup`: download all requirements
- `-l` or `--link`: regenerate linking file
- `-c` or `--cached`: remove all cached data (abilities.json, link.py)
- `-v` or `--version`: display current version of Kara
- `-m` or `--manual`: pass text to Kara, temporarily disables STT
- `-t` or `--time`: show the time taken for Kara to complete a command (only works for manual entries)
- `-i` or `--init`: initialize a new Integration

## Change Log

Detailed breakdown of important changes and new features can be found
[here](src/Kara/Data/Docs/CHANGELOG.md)

## All Links

### General
- [Discord](https://discord.gg/7hK6PFT)
- [Trello Board](https://trello.com/b/O3cQUJXu)
### Technical
- [Change Log](src/Kara/Data/Docs/CHANGELOG.md)
- [Ability Documentation](src/Kara/Data/Docs/abilities.md)
- [Integration Documentation](src/Kara/Data/Docs/integrations.md)
