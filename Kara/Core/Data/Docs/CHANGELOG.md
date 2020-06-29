# Kara - Change Log

All major changes and notable features will be documented in this file.

### Project Start: June 15th, 2020


## Kara is Now in Alpha!
### [v0.1-alpha] - Jun 19, 2020:
- Although she can only tell you the time... Kara is now in a functioning
  state! a module system has been finalized, allowing for her abilities to
  be created with ease! this system took 4 days to make, Kara's Time ability
  took 10 minutes. she mightn't have much now but the potential is there for
  anyone to create command's of their own.

## Kara Time
### [v0.1.1-alpha] - Jun 20, 2020:
- Added fully functioning Time ability
- Added 3 new commands: date, month, and year
- Various compilation improvements

## Kara Weather Support
### [v0.1.2-alpha] - Jun 20, 2020:
- Added new Weather ability
- Added four new commands: weather, sun rise, sun set, and air pressure (idk why lol)
- Fixed issues with the Time ability
- Added new arguements

## Integrations
### [v0.1.3-alpha] - Jun 21, 2020:
- Added Kara integration functionality
- Added new arguements
- Added custom ability and cache paths
- Added change log
- Improved documentation
- Improved release documentation

## Stability
### [v0.1.4-alpha] - Jun 22, 2020:
- Various documentation improvements
- Added Kara logo and icon
- Altered all paths to support relative methods
- Allow Kara to work when being called from anywhere
- Fixed a plethora of bugs
- Improved error handling
- Fixed a bug that stopped cache clearing when the cache was corrupt
- Prepared project for package upload

## Beta
### [v1.0.0-beta] - Jun 25, 2020:
- Added optional "silent" timer parameter to --time
- Added command "exact" field (opposed to only "keywords")
- Added command "fallback" field (default command to execute if all else fails)
- Added Conversational ability
- Added four new commands: greeting, howru, thanks, repeat
- Added "last" command file to cache
- Added weather search in specific location
- Removed excess files
- Removed accidental file overriding
- Removed --setup and --link
- Added handling when no command heard
- Added config key error checking
- Fixed date in x amount of days command
- Fixed ability and integration initialization issues
- Fixed a bug causing hour to be 0 when the hour was 12 am/pm
- Fixed keywords detecting inside of words
- Fixed some issues with the readme
- Improved and simplified many backend processes
- Improved and remodeled Kara's command compilation to support command repeating
- Improved error handling
- Improved keyword handling
- Improved usage (--usage)

## Knowledge
### [v1.0.1-beta] - Jun 27, 2020:
- Added a Maths ability
- Added new commands: generalMaths, coinflip, diceroll
- Added sneakpeak file to view the future!
- Added weather information tomorrow or in the next X days
- Added more backend error handling
- Added speech printing for debugging what Kara hears (--print)
- Removed all previous links to Wolfram-Alpha
- Removed some of Kara's apologies...
- Removed recommended changes to config message
- Fixed an issue causing "Exception: " to randomly appear on-screen
- Fixed an issue not linking an ability if no requirements file was given
- Improved Conversational ability

## Packaging
### [v1.1.0-beta] - Jun 28, 2020:
- Added support for python packaging
- Added Kara to PyPi
- Removed empty requirements files
- Fixed abilities with no requirements always considered "new"
- Fixed negative number handling from generalMath
- Fixed Weather know no locations
- Fixed repeat command from speaking twice
- Improved Maths ability
- Improved install documentation to support package handling

## Integrations V2
### [v1.2.0-beta] - Jun 29, 2020:
- Added confirm function
- Added manual input function
- Added Manual Support For:
    ~ kara.listen()
    ~ kara.confirm()
- Added Kara utilities library
- Fixed -h
- Fixed Weather not knowing anything
- Fixed nothing being written to "last.txt"
- Fixed repeat command says nothing when "last.txt" is empty
- Fixed templating
- Fixed integration linking
- Improved manual mode for integration debugging
- Improved Kara importation for usage in integration
- Improved and simplified many backend processes
- Improved integration templates
- Improved linking process through a "path differencing" algorithm

## Integrations V2 (and a half)
### [v1.2.1-beta] - Jun 30, 2020
- Added integration documentation
- Added integration mode to fix some linking errors
- Removed config.json from integration template
- Fixed importation error from linking file
- Fixed documentation 404 error
