from loggerjava.exceptionhandler import *
from loggerjava.test_loggerjava import *

if __name__ == '__main__':pass

ver = "v0.8.1"
_name = "log"
_absolutepath = False
_showdetailedtime = False
_showinconsole = True
_fileextension = ".log"
_file_encoding = "utf-8"
_route = r"log.log"
_debugmode = False
_fatalclose = False


class testm:
    def __init__(self):
        self._testval = {"test":True}

    def change(self,val):
        self._testval["test"] = val

    def out(self):
        print(self._testval)



# noinspection PyTypeChecker
def log(txt, level="i", pos="main", **overrides):
    """
        :param txt: the detail description of this log
        :param level: the level of the log,using: debug, info, warn, error, fatal
        accept levels:
        debug: "D", "d", "debug"
        info: "I", "i", "INFO", "info", "Info"
        warn:"W", "w", "WARN", "warn", "Warn"
        error:"E", "e", "ERROR", "error", "Error"
        fatal:"F", "f", "FATAL", "fatal", "Fatal"

        :param pos: show where the log's actual called positon in the code
        :param overrides: the overrides of the current config, only actives once
        available overrides: showinconsole , showdetailedtime
        format: override_name = override_value
        :return: log
        """
    detailtime = _showdetailedtime
    inconsole = _showinconsole
    debugmodein = _debugmode
    for overridename, data in overrides.items():
        if overridename == "showdetailedtime":
            if __formats.testformat(data, 1):
                detailtime = data
            else:
                log("wrong detailed time override. Set as False", level="W", pos="main_loggerjava", showinconsole=True)
                detailtime = False
        elif overridename == "showinconsole":
            if __formats.testformat(data, 1):
                inconsole = data
            else:
                log("wrong show in console override. Set as True", level="W", pos="main_loggerjava", showinconsole=True)
                inconsole = True
        elif overridename == "debugmode":
            if __formats.testformat(data, 1):
                debugmodein = data
            else:
                log("wrong debug override. Set as False", level="W", pos="main_loggerjava", showinconsole=True)
                debugmodein = False

    level = __formats.levelformat(level)
    if _absolutepath:
        f = open(_route, mode="at+", encoding=_file_encoding)
    else:
        f = open(_name + _fileextension, mode="at+", encoding=_file_encoding)
    if detailtime:
        timelog = time.asctime()
    else:
        timelog = __formats.time1()
    if inconsole:
        print(__formats.format(timelog, pos, level, txt))
    if not debugmodein:
        f.write(__formats.format(timelog, pos, level, txt))
        f.close()
    if debugmodein:
        return __formats.format(timelog, pos, level, txt)
    del detailtime, inconsole, debugmodein, timelog


def debug(txt, pos="main", **overrides):
    """
        :param txt: the detail description of this log
        :param pos: show where the log's actual called positon in the code
        :param overrides: the overrides of the current config,only actives once
        available overrides: showinconsole , showdetailedtime
        :return: debug log
        """
    if _debugmode:
        return log(txt, level='debug', pos=pos, **overrides)
    else:
        log(txt, level='debug', pos=pos, **overrides)


def info(txt, pos="main", **overrides):
    """
        :param txt: the detail description of this log
        :param pos: show where the log's actual called positon in the code
        :return: info log
        """
    if _debugmode:
        return log(txt, level='INFO', pos=pos, **overrides)
    else:
        log(txt, level='INFO', pos=pos, **overrides)


def warn(txt, pos="main", **overrides):
    """
        :param txt: the detail description of this log
        :param pos: show where the log's actual called positon in the code
        :param overrides: the overrides of the current config,only actives once
        available overrides: showinconsole , showdetailedtime
        :return: warning log
        """
    if _debugmode:
        return log(txt, level='WARN', pos=pos, **overrides)
    else:
        log(txt, level='WARN', pos=pos, **overrides)


def error(txt, pos="main", **overrides):
    """
        :param txt: the detail description of this log
        :param pos: show where the log's actual called positon in the code
        :param overrides: the overrides of the current config,only actives once
        available overrides: showinconsole , showdetailedtime
        :return: error log
        """
    if _debugmode:
        return log(txt, level='ERROR', pos=pos, **overrides)
    else:
        log(txt, level='ERROR', pos=pos, **overrides)


def fatal(txt, pos="main", **overrides):
    """
        :param txt: the detail description of this log
        :param pos: show where the log's actual called positon in the code
        :param overrides: the overrides of the current config,only actives once
        available overrides: showinconsole , showdetailedtime
        :return: fatal log
    """
    if _debugmode:
        return log(txt, level='FATAL', pos=pos, **overrides)
    else:
        log(txt, level='FATAL', pos=pos, **overrides)
    if _fatalclose:
        exit(10)


def config(**kwargs):
    """
    :param kwargs:input config names and config data
    format: config_name = config_data

    below are config_name and the description

    name : change the name of the log file, only actives when abolutepath config is off

    fileextension : change the extension of the log file, only actives when abolutepath config is off

    absolutepath : change whether inputing the absolute path of the log file,
    True for using the name and fileextension to create file in the program running location
    False for using the route to create file in the specific location
    (note:the route should contain the extension of the file,like:D:\test.log)

    route : change the file location, only activates when abolutepath config is on
    the route should contain the extension of the file

    file_encoding : change the file encoding method

    showdetailedtime : whether to show detailed time in the log file

    showinconsole : whether to show the log in the python console

    fatalexit : whether to exit the program after a fatal log

    :return: none
    """
    global _showinconsole, _showdetailedtime, _absolutepath, _name, _fileextension, _file_encoding, _route, \
        _debugmode, _fatalclose
    for configname, configdata in kwargs.items():

        if configname == "name":
            _name = configdata
            f = open(_name + _fileextension, mode="w", encoding=_file_encoding)
            f.close()

        elif configname == "fileextension":
            _fileextension = configdata
            f = open(_name + _fileextension, mode="w", encoding=_file_encoding)
            f.close()

        elif configname == "route":
            _route = configdata
            f = open(_route, mode="w", encoding=_file_encoding)
            f.close()

        elif configname == "file_encoding":
            try:
                if _absolutepath:
                    tmpf = open(_route, mode="w", encoding=configname)
                else:
                    tmpf = open(_name + _fileextension, mode="w", encoding=configname)
                tmpf.close()
                _file_encoding = configname
                if _absolutepath:
                    f = open(_route, mode="w", encoding=_file_encoding)
                else:
                    f = open(_name + _fileextension, mode="w", encoding=_file_encoding)
                f.close()
            except LookupError:
                warn("wrong file encoding config.this config is set to default", pos="main_loggerjava",
                     showinconsole=True)
                _file_encoding = "utf-8"

        elif configname == "showdetailedtime":
            if __formats.testformat(configdata, 1):
                _showdetailedtime = configdata
            else:
                warn("wrong detailed time config.this config is set to default", pos="main_loggerjava",
                     showinconsole=True)
                _showdetailedtime = False

        elif configname == "showinconsole":
            if __formats.testformat(configdata, 1):
                _showinconsole = configdata
            else:
                _showinconsole = True
                warn("wrong show in console config.this config is set to default", pos="main_loggerjava",
                     showinconsole=True)

        elif configname == "absolutepath":
            if __formats.testformat(configdata, 1):
                _absolutepath = configdata
                if _absolutepath:
                    f = open(_route, mode="w", encoding=_file_encoding)
                else:
                    f = open(_name + _fileextension, mode="w", encoding=_file_encoding)
                f.close()
            else:
                warn("wrong absolute path config.this config is set to default", pos="main_loggerjava",
                     showinconsole=True)
                _absolutepath = False
                f = open(_name + _fileextension, mode="w", encoding=_file_encoding)
                f.close()
        elif configname == "debugmode":
            _debugmode = configdata
        elif configname == "fatalexit":
            if __formats.testformat(configdata, 1):
                _fatalclose = configdata
            else:
                warn("wrong fatal exit config.this config is set to default", pos="main_loggerjava", showinconsole=True)
                _fatalclose = False
        # log("all given configs modified",level="D",pos="main_loggerjava.config",showinconsole=False)


def clearcurrentlog():
    """
    clean the current log file
    :return: nothing
    """
    if _absolutepath:
        f = open(_route, mode="w", encoding=_file_encoding)
    else:
        f = open(_name + _fileextension, mode="w", encoding=_file_encoding)
    f.write("")
    f.close()


def version():
    """
    show the current version of loggerjava
    :return:
    """
    print("Current loggerjava ver:%s" % ver)


def test():
    test_loggerjava.testin()


def exportconfig():
    """
    export current config
    use loadconfig(config) to load this exported config
    returning as a lib
    :return: a dictonary contains configs
    """
    i = {"_name": _name, "fileextension": _fileextension, "absolutepath": _absolutepath,
         "route": _route, "showdetailedtime": _showdetailedtime, "showinconsole": _showinconsole,
         "file_encoding": _file_encoding, "fatalexit": _fatalclose}
    return i


def loadconfig(inputconfig):
    """
    :param inputconfig: the config lib exported from exportconfig()
    :return: nothing
    """
    global _name, _showdetailedtime, _showinconsole, _absolutepath, _fileextension, _file_encoding, _route, _fatalclose

    if __formats.testformat(inputconfig["absolutepath"], 1):
        _absolutepath = inputconfig["absolutepath"]
    else:
        warn("wrong absolute path config.this config is set to default", pos="main_loggerjava", showinconsole=True)
        _absolutepath = False

    _name = inputconfig["_name"]
    _fileextension = inputconfig["fileextension"]
    _route = inputconfig["route"]

    try:
        if _absolutepath:
            tmpf = open(_route, mode="w", encoding=inputconfig["file_encoding"])
        else:
            tmpf = open(_name + _fileextension, mode="w", encoding=inputconfig["file_encoding"])
        tmpf.close()
        _file_encoding = inputconfig["file_encoding"]
    except LookupError:
        warn("wrong file encoding config.this config is set to default", pos="main_loggerjava", showinconsole=True)
        _file_encoding = "utf-8"

    if _absolutepath:
        f = open(_route, mode="at+", encoding=_file_encoding)
    else:
        f = open(_name + _fileextension, mode="at+", encoding=_file_encoding)
    f.close()

    if __formats.testformat(inputconfig["showdetailedtime"], 1):
        _showdetailedtime = inputconfig["showdetailedtime"]
    else:
        warn("wrong detailed time config.this config is set to default", pos="main_loggerjava", showinconsole=True)
        _showdetailedtime = False

    if __formats.testformat(inputconfig["showinconsole"], 1):
        _showinconsole = inputconfig["showinconsole"]
    else:
        _showinconsole = True
        warn("wrong show in console config.this config is set to default", pos="main_loggerjava", showinconsole=True)

    if __formats.testformat(inputconfig["fatalexit"], 1):
        _fatalclose = inputconfig["fatalexit"]
    else:
        _fatalclose = False
        warn("wrong fatal close config.this config is set to default", pos="main_loggerjava", showinconsole=True)


def debugging(when):
    def log(f, *args, **kwargs):
        debug("""
func called:
function : %s
ownership : %s
args : %s
kwargs : %s
""" % (f.__name__, exceptionhandler.query_def_ownership(f.__name__), args, kwargs))

    def pre_log(f):
        def wrapper(*args, **kwargs):
            log(f, *args, **kwargs)
            return f(*args, **kwargs)

        return wrapper

    def post_log(f):
        def wrapper(*args, **kwatgs):
            now = time.time()
            try:
                return f(*args, **kwatgs)
            finally:
                log(f, *args, **kwatgs)
                debug("time dela : " + str(time.time() - now))

        return wrapper

    try:
        return {"pre": pre_log, "post": post_log}[when]
    except KeyError:
        raise ValueError


# noinspection PyMethodParameters


class __formats:
    def levelformat(level):
        debugformat = ["D", "d", "debug"]
        infoformat = ["I", "i", "INFO", "info", "Info"]
        warnformat = ["W", "w", "WARN", "warn", "Warn"]
        errorformat = ["E", "e", "ERROR", "error", "Error"]
        fatalformat = ["F", "f", "FATAL", "fatal", "Fatal"]

        if level in debugformat:
            return "debug"
        elif level in infoformat:
            return "INFO"
        elif level in warnformat:
            return "WARN"
        elif level in errorformat:
            return "ERROR"
        elif level in fatalformat:
            return "FATAL"
        else:
            warn("unknown given format", pos="main_loggerjava", showinconsole=True)
            return "WARN"

    def testformat(name, type):
        if type == 1:
            if name or not name:
                return True
            else:
                return False
        elif type == 2:
            pass

    def format(time1, place, level, txt):
        return "[%s] [%s/%s]: %s\n" % (time1, place, level, txt)

    def time1():
        return "%02d:%02d:%02d" % (time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec)
        # return str(time.localtime().tm_hour).rjust(2, "0") + ":" + \
        #    str(time.localtime().tm_min).rjust(2, "0") + ":" + str(time.localtime().tm_sec).rjust(2, "0")
