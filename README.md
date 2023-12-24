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
### Config
```python
logger.confg(name="log", showdetailedtime=False, showinconsole=True)
"""
:param name: output log file name
:param showdetailedtime: output log time format,False for short time, True for long time
:param showinconsole:whether output log will show in python console
:return:
"""
```
using `logger.exportconfig()` to export your current config

and using `logger.inportconfig(inputconfig)` to inport your config
### Versions

`0.0.5.1` rename outputconfig -> exportconfig

`0.0.5` added the outputconfig and the loadconfig function,edited the config part to let it output log

`0.0.4` upgrade the config sys and add helps

`0.0.3` upload the descriptions

`0.0.2` initial upload