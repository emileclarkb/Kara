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

Additionally when using Kara for your own project you don't have to use the
Abilities that come with here (ie. Time, Weather, etc.). You can simply delete
these and recompile her. Everything about Kara is customizable!

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
When creating Abilities it is recommended to only store your commands within your
main file and to import supporting code from a different python file.

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

### Compiling Abilities

Kara has a lot of command line arguements to make development easier for you.
These are documented in the [README](../../../../README.md) or can be seen through
`python kara.py -h`.

Upon running Kara she goes through various booting stages, the most important for
us is the compilation stage. During this the data of all Abilities is "compiled"
into three files (these files are called our cached data). This allows Kara to
have all her data in known locations, for greater simplicity, and also speed.

Everytime your `config.json` is changed you must recompile UNLESS you don't want
Kara to access the changes yet. Compilation automatically occurs when you run
Kara. To manually call the compilation and nothing else we use `python kara.py
-r`. To NOT compile while still booting Kara we use `python kara.py -r 0`. To
empty our cache (if something went wrong during compilation) we have access to
`python kara.py -c`.

During compilation the compiler detects any changes that occured by comparing the
new configs and the cached data. Any changes and their respective Abilities will
be shown on the screen. When a change occurs to an Ability Kara will automatically
attempt to install everything within the Ability's requirements file.

Compilation can take some time and if you're not changing anything `-r 0` might
speed up your booting process.


## More

If you're looking for a deeper look into Abilities check out the
[source code](../../Abilities/) for other Abilities.
