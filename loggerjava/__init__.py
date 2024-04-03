import time
import loggerjava

if __name__ == '__main__':
    pass

ver = "v0.0.7.5"
name = "log"
absolutepath = False
showdetailedtime = False
showinconsole = True
filetype = ".log"
file_encoding = "utf-8"
route = r"log.log"
debugin = False
fatalclose = False


# noinspection PyTypeChecker
def log(txt, type="i", pos="main", **overrides):
    """
        :param txt: the detail description of this log
        :param type: the type of the log,using:debug,info,warn,error,fatal
        :param pos: show where the log's actual called positon in the code
        :return: log
        """
    for configname, configdata in overrides.items():
        pass
    level = _formats.typeformat(type)
    if absolutepath:
        f = open(route, mode="at+", encoding=file_encoding)
    else:
        f = open(name + filetype, mode="at+", encoding=file_encoding)
    if showdetailedtime and showinconsole:
        # noinspection PyTypeChecker
        f.write(_formats.format(time.asctime(), pos, level, txt))
        print(_formats.format(time.asctime(), pos, level, txt))
    elif not showdetailedtime and showinconsole:
        f.write(_formats.format(_formats.time1(), pos, level, txt))
        print(_formats.format(_formats.time1(), pos, level, txt))
    elif showdetailedtime and not showinconsole:
        f.write(_formats.format(time.asctime(), pos, level, txt))
    else:
        f.write(_formats.format(_formats.time1(), pos, level, txt))
    if debugin and not showdetailedtime:
        return _formats.format(_formats.time1(), pos, level, txt)
    elif debugin and showdetailedtime:
        return _formats.format(time.asctime(), pos, level, txt)
    f.close()


def debug(txt, pos="main"):
    """
        :param txt: the detail description of this log
        :param pos: show where the log's actual called positon in the code
        :return: debug log
        """
    if debugin:
        return log(txt, type='debug', pos=pos)
    else:
        log(txt, type='debug', pos=pos)


def info(txt, pos="main"):
    """
        :param txt: the detail description of this log
        :param pos: show where the log's actual called positon in the code
        :return: info log
        """
    if debugin:
        return log(txt, type='INFO', pos=pos)
    else:
        return log(txt, type='INFO', pos=pos)


def warn(txt, pos="main"):
    """
        :param txt: the detail description of this log
        :param pos: show where the log's actual called positon in the code
        :return: warning log
        """
    if debugin:
        return log(txt, type='WARN', pos=pos)
    else:
        log(txt, type='WARN', pos=pos)


def error(txt, pos="main"):
    """
        :param txt: the detail description of this log
        :param pos: show where the log's actual called positon in the code
        :return: error log
        """
    if debugin:
        return log(txt, type='ERROR', pos=pos)
    else:
        log(txt, type='ERROR', pos=pos)


def fatal(txt, pos="main"):
    """
    :param txt: the detail description of this log
    :param pos: show where the log's actual called positon in the code
    :return: fatal log
    """
    if debugin:
        return log(txt, type='FATAL', pos=pos)
    else:
        log(txt, type='FATAL', pos=pos)
    if fatalclose:
        exit(10)


def config(**kwargs):
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
    global showinconsole, showdetailedtime, absolutepath, name, filetype, file_encoding, route, debugin, fatalclose
    for configname, configdata in kwargs.items():

        if configname == "name":
            name = configdata
            f = open(name + filetype, mode="w", encoding=file_encoding)
            f.close()

        elif configname == "filetype":
            filetype = configdata
            f = open(name + filetype, mode="w", encoding=file_encoding)
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
                    tmpf = open(name + filetype, mode="w", encoding=configname)
                tmpf.close()
                file_encoding = configname
                del tmpf
                if absolutepath:
                    f = open(route, mode="w", encoding=file_encoding)
                else:
                    f = open(name + filetype, mode="w", encoding=file_encoding)
                f.close()
            except LookupError:
                warn("wrong file encoding config.this config is set to normal", pos="main_loggerjava")
                file_encoding = "utf-8"

        elif configname == "showdetailedtime":
            if _formats.testformat(configdata, 1):
                showdetailedtime = configdata
            else:
                tmpin = showinconsole
                showinconsole = True
                warn("wrong detailed time config.this config is set to normal", pos="main_loggerjava")
                showinconsole = tmpin
                showdetailedtime = False
                del tmpin

        elif configname == "showinconsole":
            if _formats.testformat(configdata, 1):
                showinconsole = configdata
            else:
                showinconsole = True
                warn("wrong show in console config.this config is set to normal", pos="main_loggerjava")

        elif configname == "absolutepath":
            if _formats.testformat(configdata, 1):
                absolutepath = configdata
                if absolutepath:
                    f = open(route, mode="w", encoding=file_encoding)
                else:
                    f = open(name + filetype, mode="w", encoding=file_encoding)
                f.close()
            else:
                tmpin = showinconsole
                showinconsole = True
                warn("wrong absolute path config.this config is set to normal", pos="main_loggerjava")
                showinconsole = tmpin
                absolutepath = False
                f = open(name + filetype, mode="w", encoding=file_encoding)
                f.close()
                del tmpin
        elif configname == "debuging":
            debugin = configdata
        elif configname == "fatalexit":
            if _formats.testformat(configdata, 1):
                fatalclose = configdata
            else:
                warn("wrong fatal exit config.this config is set to normal", pos="main_loggerjava")
                fatalclose = False


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
    :return:
    """
    i = {"name": name, "filetype": filetype, "absolutepath": absolutepath,
         "route": route, "showdetailedtime": showdetailedtime, "showinconsole": showinconsole,
         "file_encoding": file_encoding, "fatalexit": fatalclose}
    return i


def loadconfig(inputconfig):
    """
    :param inputconfig: the config lib exported from exportconfig()
    :return:
    """
    global name, showdetailedtime, showinconsole, absolutepath, filetype, file_encoding, route, fatalclose

    if _formats.testformat(inputconfig["absolutepath"], 1):
        absolutepath = inputconfig["absolutepath"]
    else:
        tmpin = showinconsole
        showinconsole = True
        warn("wrong absolute path config.this config is set to normal", pos="main_loggerjava")
        showinconsole = tmpin
        absolutepath = False
        del tmpin

    name = inputconfig["name"]
    filetype = inputconfig["filetype"]
    route = inputconfig["route"]

    try:
        if absolutepath:
            tmpf = open(route, mode="w", encoding=inputconfig["file_encoding"])
        else:
            tmpf = open(name + filetype, mode="w", encoding=inputconfig["file_encoding"])
        tmpf.close()
        file_encoding = inputconfig["file_encoding"]
        del tmpf
    except LookupError:
        warn("wrong file encoding config.this config is set to normal", pos="main_loggerjava")
        file_encoding = "utf-8"

    if absolutepath:
        f = open(route, mode="at+", encoding=file_encoding)
    else:
        f = open(name + filetype, mode="at+", encoding=file_encoding)
    f.close()

    if _formats.testformat(inputconfig["showdetailedtime"], 1):
        showdetailedtime = inputconfig["showdetailedtime"]
    else:
        tmpin = showinconsole
        showinconsole = True
        warn("wrong detailed time config.this config is set to normal", pos="main_loggerjava")
        showinconsole = tmpin
        showdetailedtime = False
        del tmpin

    if _formats.testformat(inputconfig["showinconsole"], 1):
        showinconsole = inputconfig["showinconsole"]
    else:
        showinconsole = True
        warn("wrong show in console config.this config is set to normal", pos="main_loggerjava")

    if _formats.testformat(inputconfig["fatalexit"], 1):
        fatalclose = inputconfig["fatalexit"]
    else:
        fatalclose = False
        tmpin = showinconsole
        showinconsole = True
        warn("wrong fatal close config.this config is set to normal", pos="main_loggerjava")
        showinconsole = tmpin
        del tmpin


# noinspection PyMethodParameters


class _formats:
    def typeformat(type):
        debugformat = ["D", "d", "DEBUG", "debug"]
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
            warn("unknown given format", pos="main_loggerjava")
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
