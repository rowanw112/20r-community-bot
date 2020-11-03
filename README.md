test test testy
# 20r Gaming Discord Bot #

*Gaming Discord Bot*



**Discord Gaming bot that is used to register users, add users to a spreadsheet.**

*Primary focus is on to make a lot of actions within the community to become automated and make everybody's job easier.*

**Created and Maintained by Rowan Watson**

## Table of Contents ##

[[_TOC_]]

## Features ##
- Automatic inform when a user joins the server.
-- Automatic assign of correct roles when a new user joins
-- Welcome message
-- Automatic assign of game roles when a user joins
- Anti-Bot spam verification system
- Handing of json data of embedded messages
- Commands
- Basic Looking for Game system
- Registration of users
-- Adds user to the correct spreadsheet with correct information
-- Assigning of correct roles once registered
- Automatic removal of users from the spreadsheet
-- via the remove command or leaving the discord server
- connection to other APIs to grab live game data
-- update live member count
-- update of server status
-- update of channel names with the status of the server
-- Live update of users in the discord and in voice chat
-- Announcement message for when to join a server with live server details.
- Automatic assign roles once a user reacts to a message.
- Verification of users who are actually in an outfit on PlanetSide 2.



## Tasks / Ideas ##
- [ ] gameIDs json file for steam games
- [ ] use steamapi instead of battlemetrics api
- [ ] Load roles from json instead of ctx.guild
- [ ] Rework most json data handling to a database (going to use sqllite)
- [ ] new application format with private messaging to handle application
- [ ] clean up the code
- [ ] commenting code
- [ ] use a more advanced look for game system that uses steamapi
- [ ] rework .add and .remove with a database instead of google sheets
...
## Installation ##
Download .zip file
Create a new file called bot.yml in Configuration folder
enter this data
```
token: ""
devToken: ""
api20rkey: ""
devapi20rkey: ""
apips2key: ""
devapips2key: ""
devStart: False
battlemetrickey: ""
steamkey: ""
activity: ""
prefix: "."
case_insensitive: True
log level: "INFO"
logpath: "../../logs" # Relative path to Bot.core.__main__.py
JSONDirectory: "../../Data/JSON" # Relative path to Bot.core.__main__.py
CogDirectory: "../cogs" # Relative path to Bot.core.__main__.py

```

## License ##
Please follow LICENSE file for the License.