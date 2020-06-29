# Kara - Integrations

## Overview

Imagine it like it this, abilities give Kara functionality and allow her to
perform and control new commands. Integrations allow Kara to work inside of your
project and hand the controller over to it too. This means you can have greater
control of how she performs tasks.

## Developers Guide

Integrations are different from abilities and should not be confused. Integrations
allow you as a developer to use Kara as a module. Voice Control and Virtual
Assistants are something every industry could benefit from, so why don't they?
No one wants to reinvent the wheel! This is the thought behind Kara, we made her
so you don't have to.

Instead of Kara running standalone, integrations give you the capabilities to
easily control all her movements INSIDE of your own application. Why not
integrate her into a mirror, phone, speaker, the possibilities are endless!

Let's take a look at how you can start your first integration! First off, make
sure you have read the [installation guide](../../../README.md) and have the
latest version of Kara on your system.

Next we run the following command: `Kara -i`. This will setup the necessary paths
for Kara to operate. The `main.py` is simply and template and can show you the basics
of working with Kara.

Kara currently only has two integration paths: `Abilities` and `Cache`, both
contained inside `Data`. The `Cache` is where Kara temporarily stores all her
data, mainly on current commands and abilities she has access too. The `Abilities`
path as you may already have guessed holds all of her "abilities". For more on
abilities check out it's [documentation](abilities.md)!

If you trying running `main.py` you'll notice Kara doesn't know ANYTHING. So why
is this? Well integrations only have access to the abilities stored in `Data/Abilities`
so if you want features, either download them from our abilities repository
(COMING SOON...) or make them!

## Features

Current features found in the Kara object (`from Kara import Kara`):
- `speak`: Make Kara talk (ie. `speak('hello world')`)
- `listen`: Begin listening for speech
- `compile`: Directly pass command to Kara (ie. `compile('what time is it')`)
- `input`: Manually receive input through text
- `confirm`: Make the user confirm an action
- `ability`: Template new ability in current directory
- `integrate`: Template new integration in current directory


Compiler (`import Kara.Core.compiler`)
- `compile`: Runs all the compilation processes (general compilation function)
- `deepCompile`: Compile abilities.json
- `compress`: Compress abilities.json into commands.json
- `link`: Generate ability linking data
- `fallback`: Generate command fallback data

## Utilities

On top of her default functions Kara also comes with a utility library
(`import Kara.util`), this houses some less important functions although these
still can prove useful during development. For instance the `prior` command which
gets the word before another word in a string.

## Additional

Unfortunately I haven't had time to work on much documentation, if you are
interested in using Kara and gaining greater knowledge feel free to message me
at eclarkboman@gmail.com or join our [discord server](https://discord.gg/7hK6PFT).
