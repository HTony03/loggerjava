import time
import loggerjava
from loggerjava.exceptionhandler import *

if __name__ == '__main__':

    pass

ver = "v0.8.0"
name = "log"
absolutepath = False
showdetailedtime = False
showinconsole = True
fileextension = ".log"
file_encoding = "utf-8"
route = r"log.log"
debugmode = False
fatalclose = False


# noinspection PyTypeChecker
def log(txt, type="i", pos="main", **overrides):
    """
        :param txt: the detail description of this log
        :param type: the type of the log,using:debug,info,warn,error,fatal
        accept types:
        debug: "D", "d", "debug"
        info: "I", "i", "INFO", "info"
        warn:"W", "w", "WARN", "warn"
        error:"E", "e", "ERROR", "error"
        fatal:"F", "f", "FATAL", "fatal"

        :param pos: show where the log's actual called positon in the code
        :param overrides: the overrides of the current config,only actives once
        available overrides: showinconsole , showdetailedtime
        format: override_name = override_value
        :return: log
        """
    detailtime = showdetailedtime
    inconsole = showinconsole
    debugmodein = debugmode
    for overridename, data in overrides.items():
        if overridename == "showdetailedtime":
            if _formats.testformat(data, 1):
                detailtime = data
            else:
                log("wrong detailed time override. Set as False", type="W", pos="main_loggerjava", showinconsole=True)
                detailtime = False
        elif overridename == "showinconsole":
            if _formats.testformat(data, 1):
                inconsole = data
            else:
                log("wrong show in console override. Set as True", type="W", pos="main_loggerjava", showinconsole=True)
                inconsole = True
        elif overridename == "debugmode":
            if _formats.testformat(data, 1):
                debugmodein = data
            else:
                log("wrong debug override. Set as False", type="W", pos="main_loggerjava", showinconsole=True)
                debugmodein = False

    level = _formats.typeformat(type)
    if absolutepath:
        f = open(route, mode="at+", encoding=file_encoding)
    else:
        f = open(name + fileextension, mode="at+", encoding=file_encoding)
    if detailtime:
        timelog = time.asctime()
    else:
        timelog = _formats.time1()
    if inconsole:
        print(_formats.format(timelog, pos, level, txt))
    if not debugmodein:
        f.write(_formats.format(timelog, pos, level, txt))
        f.close()
    if debugmodein:
        return _formats.format(timelog, pos, level, txt)
    del detailtime, inconsole, debugmodein, timelog


def debug(txt, pos="main", **overrides):
    """
        :param txt: the detail description of this log
        :param pos: show where the log's actual called positon in the code
        :param overrides: the overrides of the current config,only actives once
        available overrides: showinconsole , showdetailedtime
        :return: debug log
        """
    if debugmode:
        return log(txt, type='debug', pos=pos, **overrides)
    else:
        log(txt, type='debug', pos=pos, **overrides)


def info(txt, pos="main", **overrides):
    """
        :param txt: the detail description of this log
        :param pos: show where the log's actual called positon in the code
        :return: info log
        """
    if debugmode:
        return log(txt, type='INFO', pos=pos, **overrides)
    else:
        log(txt, type='INFO', pos=pos, **overrides)


def warn(txt, pos="main", **overrides):
    """
        :param txt: the detail description of this log
        :param pos: show where the log's actual called positon in the code
        :param overrides: the overrides of the current config,only actives once
        available overrides: showinconsole , showdetailedtime
        :return: warning log
        """
    if debugmode:
        return log(txt, type='WARN', pos=pos, **overrides)
    else:
        log(txt, type='WARN', pos=pos, **overrides)


def error(txt, pos="main", **overrides):
    """
        :param txt: the detail description of this log
        :param pos: show where the log's actual called positon in the code
        :param overrides: the overrides of the current config,only actives once
        available overrides: showinconsole , showdetailedtime
        :return: error log
        """
    if debugmode:
        return log(txt, type='ERROR', pos=pos, **overrides)
    else:
        log(txt, type='ERROR', pos=pos, **overrides)


def fatal(txt, pos="main", **overrides):
    """
        :param txt: the detail description of this log
        :param pos: show where the log's actual called positon in the code
        :param overrides: the overrides of the current config,only actives once
        available overrides: showinconsole , showdetailedtime
        :return: fatal log
    """
    if debugmode:
        return log(txt, type='FATAL', pos=pos, **overrides)
    else:
        log(txt, type='FATAL', pos=pos, **overrides)
    if fatalclose:
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
    global showinconsole, showdetailedtime, absolutepath, name, fileextension, file_encoding, route, debugmode, fatalclose
    for configname, configdata in kwargs.items():

        if configname == "name":
            name = configdata
            f = open(name + fileextension, mode="w", encoding=file_encoding)
            f.close()

        elif configname == "fileextension":
            fileextension = configdata
            f = open(name + fileextension, mode="w", encoding=file_encoding)
            f.close()

        elif configname == "route":
            route = configdata
            f = open(route, mode="w", encoding=file_encoding)
            f.close()

        elif configname == "file_encoding":
            try:
                if absolutepath:
                    tmpf = open(route, mode="w", encoding=configname)
                else:
                    tmpf = open(name + fileextension, mode="w", encoding=configname)
                tmpf.close()
                file_encoding = configname
                if absolutepath:
                    f = open(route, mode="w", encoding=file_encoding)
                else:
                    f = open(name + fileextension, mode="w", encoding=file_encoding)
                f.close()
            except LookupError:
                warn("wrong file encoding config.this config is set to default", pos="main_loggerjava",
                     showinconsole=True)
                file_encoding = "utf-8"

        elif configname == "showdetailedtime":
            if _formats.testformat(configdata, 1):
                showdetailedtime = configdata
            else:
                warn("wrong detailed time config.this config is set to default", pos="main_loggerjava",
                     showinconsole=True)
                showdetailedtime = False

        elif configname == "showinconsole":
            if _formats.testformat(configdata, 1):
                showinconsole = configdata
            else:
                showinconsole = True
                warn("wrong show in console config.this config is set to default", pos="main_loggerjava",
                     showinconsole=True)

        elif configname == "absolutepath":
            if _formats.testformat(configdata, 1):
                absolutepath = configdata
                if absolutepath:
                    f = open(route, mode="w", encoding=file_encoding)
                else:
                    f = open(name + fileextension, mode="w", encoding=file_encoding)
                f.close()
            else:
                warn("wrong absolute path config.this config is set to default", pos="main_loggerjava",
                     showinconsole=True)
                absolutepath = False
                f = open(name + fileextension, mode="w", encoding=file_encoding)
                f.close()
        elif configname == "debugmode":
            debugmode = configdata
        elif configname == "fatalexit":
            if _formats.testformat(configdata, 1):
                fatalclose = configdata
            else:
                warn("wrong fatal exit config.this config is set to default", pos="main_loggerjava", showinconsole=True)
                fatalclose = False
        # log("all given configs modified",type="D",pos="main_loggerjava.config",showinconsole=False)


def clearcurrentlog():
    """
    clean the current log file
    :return: nothing
    """
    if absolutepath:
        f = open(route, mode="w", encoding=file_encoding)
    else:
        f = open(name + fileextension, mode="w", encoding=file_encoding)
    f.write("")
    f.close()


def version():
    """
    show the current version of loggerjava
    :return:
    """
    print("Current loggerjava ver:%s" % ver)


def test():
    loggerjava.test_loggerjava.testin()


def exportconfig():
    """
    export current config
    use loadconfig(config) to load this exported config
    returning as a lib
    :return: a dictonary contains configs
    """
    i = {"name": name, "fileextension": fileextension, "absolutepath": absolutepath,
         "route": route, "showdetailedtime": showdetailedtime, "showinconsole": showinconsole,
         "file_encoding": file_encoding, "fatalexit": fatalclose}
    return i


def loadconfig(inputconfig):
    """
    :param inputconfig: the config lib exported from exportconfig()
    :return: nothing
    """
    global name, showdetailedtime, showinconsole, absolutepath, fileextension, file_encoding, route, fatalclose

    if _formats.testformat(inputconfig["absolutepath"], 1):
        absolutepath = inputconfig["absolutepath"]
    else:
        warn("wrong absolute path config.this config is set to default", pos="main_loggerjava", showinconsole=True)
        absolutepath = False

    name = inputconfig["name"]
    fileextension = inputconfig["fileextension"]
    route = inputconfig["route"]

    try:
        if absolutepath:
            tmpf = open(route, mode="w", encoding=inputconfig["file_encoding"])
        else:
            tmpf = open(name + fileextension, mode="w", encoding=inputconfig["file_encoding"])
        tmpf.close()
        file_encoding = inputconfig["file_encoding"]
    except LookupError:
        warn("wrong file encoding config.this config is set to default", pos="main_loggerjava", showinconsole=True)
        file_encoding = "utf-8"

    if absolutepath:
        f = open(route, mode="at+", encoding=file_encoding)
    else:
        f = open(name + fileextension, mode="at+", encoding=file_encoding)
    f.close()

    if _formats.testformat(inputconfig["showdetailedtime"], 1):
        showdetailedtime = inputconfig["showdetailedtime"]
    else:
        warn("wrong detailed time config.this config is set to default", pos="main_loggerjava", showinconsole=True)
        showdetailedtime = False

    if _formats.testformat(inputconfig["showinconsole"], 1):
        showinconsole = inputconfig["showinconsole"]
    else:
        showinconsole = True
        warn("wrong show in console config.this config is set to default", pos="main_loggerjava", showinconsole=True)

    if _formats.testformat(inputconfig["fatalexit"], 1):
        fatalclose = inputconfig["fatalexit"]
    else:
        fatalclose = False
        warn("wrong fatal close config.this config is set to default", pos="main_loggerjava", showinconsole=True)


# noinspection PyMethodParameters


class _formats:
    def typeformat(type):
        debugformat = ["D", "d", "debug"]
        infoformat = ["I", "i", "INFO", "info"]
        warnformat = ["W", "w", "WARN", "warn"]
        errorformat = ["E", "e", "ERROR", "error"]
        fatalformat = ["F", "f", "FATAL", "fatal"]

        if type in debugformat:
            return "debug"
        elif type in infoformat:
            return "INFO"
        elif type in warnformat:
            return "WARN"
        elif type in errorformat:
            return "ERROR"
        elif type in fatalformat:
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
        return str(time.localtime().tm_hour).rjust(2, "0") + ":" + \
            str(time.localtime().tm_min).rjust(2, "0") + ":" + str(time.localtime().tm_sec).rjust(2, "0")
