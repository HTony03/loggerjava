# loggerjava

---
an easy logger outputs like java logs
### How to use
```python
import loggerjava
logger = loggerjava
logger.info("test")
logger.warn("test",pos="insidecommand")
```

### Outputs
```commandline
[20:39:00] [main/debug]: test
[20:39:00] [main/info]: test
[20:39:00] [main/WARNING]: test
[20:39:00] [main/ERROR]: test
[20:39:00] [main/FATAL]: test
```

### Developing features
- [ ] mutiple variable with different configs
- [x] new config format
- [ ] catch and format errors
- [ ] override config once


### Config
```python
import loggerjava
loggerjava.config(**kwargs)
"""
:param kwargs:input config names and config data
format: config_name = config_data

below are config_name and the description

name : change the name of the log file, only actives when abolutepath config is off

filetype : change the file type of the log file, only actives when abolutepath config is off

absolutepath : change whether inputing the absolute path of the log file,
True for using the name and filetype to create file in the program running location
False for using the route to create file in the specific location(note:you need to enter the file format,like:test.log)

route : change the file location, only activates when abolutepath config is on

file_encoding : change the file encoding method

showdetailedtime : whether to show detailed time in the log file

showinconsole : whether to show the log in the python console

fatalexit : whether to exit the program after a fatal log

:return:
"""
```
using `logger.exportconfig()` to export your current config

and using `logger.inportconfig(inputconfig)` to inport your config
### Versions

`v0.0.7.5` edited the original log codes,adding "log" feature,add the fatalexit config

`v0.0.7.2` adding the "fatalexit" feature,adding an easier log function(not completed)

`v0.0.7.1` adding debug config,adding debug

`v0.0.7` no actual updates, updating version num to ver x.x.x

`0.0.6.1` update readme

`0.0.6` change the config method, adding file_encoding,absolutepath,filetype config

`0.0.5.1` rename outputconfig -> exportconfig

`0.0.5` added the outputconfig and the loadconfig function,edited the config part to let it output log

`0.0.4` upgrade the config sys and add helps

`0.0.3` upload the descriptions

`0.0.2` initial upload