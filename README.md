# loggerjava

---
an easy logger outputs like java logs
### How to use
```python
import loggerjava
logger = loggerjava
logger.info("test")
logger.warn("test",pos="insidecommand")
logger.log("test",type="w",pos="main_test",showinconsole=False)
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
- [X] override config once


### Config
```python
import loggerjava
loggerjava.config(**kwargs)
"""
:param kwargs:input config names and config data
format: config_name = config_data

below are config_name and the description

name : change the name of the log file, only actives when abolutepath config is off

fileextension : change the extension of the log file, only actives when abolutepath config is off

absolutepath : change whether inputing the absolute path of the log file,
True for using the name and fileextension to create file in the program running location
False for using the route to create file in the specific location(note:you need to enter the file format,like:test.log)

route : change the file location, only activates when abolutepath config is on
the route should contain the

file_encoding : change the file encoding method

showdetailedtime : whether to show detailed time in the log file

showinconsole : whether to show the log in the python console

fatalexit : whether to exit the program after a fatal log

:return: none
"""
```
using `logger.exportconfig()` to export your current config

and using `logger.inportconfig(inputconfig)` to inport your config

### Exception handler
using the `loggerjava.exceptionhandler.exception(exc)` function to process an Exception

remember to register the defs/classes after you created them

```python
import loggerjava
import loggerjava.exceptionhandler
def test1(a):
    print(b)
class test2():
    def printa(self):
        print(self.b)
loggerjava.exceptionhandler.register_def(test1)
loggerjava.exceptionhandler.register_def(test2)
if __name__ == "__main__":
    try:
        test1(1)
    except Exception as E:
        loggerjava.error(loggerjava.exceptionhandler.handler(E))
    try:
        a = test2
        a.printa()
    except Exception as E:
        loggerjava.error(loggerjava.exceptionhandler.handler(E))
```
#### Output：
```commandline
[20:39:00] [main/ERROR]: NameError: name 'b' is not defined
    at <module> (test.py:30)
    at test1.test1 (test.py:21)

[20:39:00] [main/ERROR]: AttributeError: 'test2' object has no attribute 'b'
    at <module> (test.py:35)
    at test2.printa (test.py:25)
```
### Versions

`v0.8.0` added the exceptionhandler and clearcurrentlog function

`v0.7.6` change filetype -> fileextension, simplified the code, completed the override funciton

`v0.7.5.dev1` follow SemVer, no actual updates

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