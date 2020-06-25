# Kara - Change Log

All major changes and notable features will be documented in this file.

### Project Start: June 15th, 2020


## Kara is Now in Alpha!
### [v0.1-alpha] - Jun 19, 2020:
- Although she can only tell you the time... kara is now in a functioning
  state! a module system has been finalized, allowing for her abilities to
  be created with ease! this system took 4 days to make, kara's time ability
  took 10 minutes. she mightn't have much now but the potential is there for
  anyone to create command's of their own.

## Kara Time
### [v0.1.1-alpha] - Jun 20, 2020:
- Added fully functioning time ability
- Added 3 new commands: date, month, and year
- Various compilation improvements

## Kara Weather Support
### [v0.1.2-alpha] - Jun 20, 2020:
- Added four new abilities: weather, sun rise, sun set, and air pressure (idk why lol)
- Fixed issues with the time ability
- Added new arguements

## Integrations
### [v0.1.3-alpha] - Jun 21, 2020:
- Added kara integration functionality
- Added new arguements
- Added custom ability and cache paths
- Added change log
- Improved documentation
- Improved release documentation

## Stability
### [v0.1.4-alpha] - Jun 22, 2020:
- Various documentation improvements
- Added kara logo and icon
- Altered all paths to support relative methods
- Allow kara to work when being called from anywhere
- Fixed a plethora of bugs
- Improved error handling
- Fixed a bug that stopped cache clearing when the cache was corrupt
- Prepared project for package upload

## Beta
### [v1.0.0-beta] - Jun xx, 2020:
- Added optional "silent" timer parameter to --time
- Added command "exact" field (opposed to only "keywords")
- Added command "fallback" field (default command to execute if all else fails)
- Added conversational ability
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
- Improved and remodeled kara's command compilation to support command repeating
- Improved error handling
- Improved keyword handling
- Improved usage (--usage)
