# Kara - Abilities

## Overview

Kara is designed specifically to be modified by the community and given additional
functionality or "Abilities". By default she has no features program directly into
her, all her capabilities come from stored Abilities.

## Developers Guide

To develop a new ability run `python kara.py -i ABILITY_NAME`, this will
automatically generate the template for a new Ability, to view and work on your
Ability you can travel to `src/Core/Abilities/ABILITY_NAME`.

Every Ability has 3 core files: `config.json`, `main.py`, and `requirements.txt`.
`config.json` stores and communicates all of your Ability so Kara can easily
interpret and compile her Abilities at run time. `config.json` includes links to
your main and requirements file, if you change the names of these files they must
also be changed within your `config.json`! Your `requirements.txt` is optional and
only necessary if your Ability contains any 3rd party python modules, setting specific
versions and adding comments is also supported. Finally your `main.py` is the brains
of your Ability and is REQUIRED in every Ability. All of your Ability's commands
will be handled in here aswell

Although unnecessary it is recommended to fill in the name, version, author,
description, and long description. If `config.json` is filled incorrectly Kara
will automatically inform you.

### Making Your First Ability

By this point you should have an empty Ability template. An Ability by itself won't
do anything, in order to make features we need to write commands. Let's start with
the classic "Hello World" programming experience!

```
def myCommand(Kara, command):
    Kara.speak('Hello World!')
```

This function takes two parameters: `Kara`, and `command`. This is the conventional
naming given to them. `Kara` is an instance of Kara and currently is only capable
of `Kara.speak()` and `Kara.listen()` within an Ability. Finally in the function
we call `Kara.speak()` which obviously results in Kara's Text to Speech Abilities.

Although we've created a command Kara still doesn't know what to do with it, this
is where we use `"commands"` within `config.json`. Let's create a basic command.

```
"commands": {
    "commandName": {
        "target": "myCommand",
        "keywords": ["hello"]
    }
}
```

This simple JSON will create a new command named `"commandName"` (name can
be anything). Every command we created MUST contain both a `"target"` and
`"keywords"`. Your command's `"keywords"` dictate when the command should be
activated and the `"target"` is the function called when the `"keywords"` logic
is met. For more on keywords keep reading!

### Keywords

Keywords are a requirement for every command and have a unit set of logic attached
to them. Operating specifically with `AND` and `OR` logic. Within your `config.json`
file `"keywords"` must be given as an array of strings.

`"keywords": ["what time", "what date"]`

Each string is considered a "set of keys", with each word being a "key". This is
how keywords operate. For the given example it's target will activate if either:
"what" AND "time" are in the command, OR "what" AND "date" are in the command.
Everything within each key set goes through AND logic, if one key set doesn't
result as `True` Kara moves on to looking through the next key set (OR logic).
