from loggerjava.exceptionhandler import *
from loggerjava.test_loggerjava import *
import time
import os.path

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



# noinspection PyUnresolvedReferences,PyIncorrectDocstring
class log:
    def __init__(self):
        self._name = "log"
        self._absolutepath = False
        self._showdetailedtime = False
        self._showinconsole = True
        self._fileextension = ".log"
        self._file_encoding = "utf-8"
        self._route = r"log.log"
        self._debugmode = False
        self._fatalexit = False
        self._debuginanotherfile = False
        self._debugfilename = "_debug"

    def levelformat(self, level):
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
            self.warn({'txt': "unknown given format", 'pos': "main_loggerjava", 'showinconsole': True})
            return "WARN"

    def testformat(self, name, type):
        if type == 1:
            if name or not name:
                return True
            else:
                return False
        elif type == 2:
            pass

    def format(self, time1, place, level, txt):
        return "[%s] [%s/%s]: %s\n" % (time1, place, level, txt)

    def time1(self):
        return "%02d:%02d:%02d" % (time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec)
        # return str(time.localtime().tm_hour).rjust(2, "0") + ":" + \
        #    str(time.localtime().tm_min).rjust(2, "0") + ":" + str(time.localtime().tm_sec).rjust(2, "0")

    def log(self, params):
        """
            :param params: a dict contains:
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
            :type params: dict
            :type txt: str
            :type level: str
            :type pos: str, default: 'main'
            :return: log
            """

        # override
        detailtime = self._showdetailedtime
        inconsole = self._showinconsole
        debugmodein = self._debugmode
        for overridename, data in params.items():
            if overridename == "showdetailedtime":
                if self.testformat(data, 1):
                    detailtime = data
                else:
                    self.log(
                        {'txt': "wrong detailed time override. Set as False", 'level': "W", 'pos': "main_loggerjava",
                         'showinconsole': True})
                    detailtime = False
            elif overridename == "showinconsole":
                if self.testformat(data, 1):
                    inconsole = data
                else:
                    self.log(
                        {'txt': "wrong show in console override. Set as True", 'level': "W", 'pos': "main_loggerjava",
                         'showinconsole': True})
                    inconsole = True
            elif overridename == "debugmode":
                if self.testformat(data, 1):
                    debugmodein = data
                else:
                    self.log({'txt': "wrong debug override. Set as False", 'showinconsole': True})
                    debugmodein = False
        # log cfg
        level = self.levelformat(params['level'])
        if 'pos' not in params:
            pos = "main"
        else:
            pos = params['pos']
        txt = params['txt']
        # log
        if self._absolutepath:
            f = open(self._route, mode="at+", encoding=self._file_encoding)
            if self._debuginanotherfile:
                f_debug = open(
                    os.path.splitext(self._route)[0] + self._debugfilename + os.path.splitext(self._route)[1],
                    mode='at+', encoding=self._file_encoding)
        else:
            f = open(self._name + self._fileextension, mode="at+", encoding=self._file_encoding)
            if self._debuginanotherfile:
                f_debug = open(self._name + self._debugfilename + self._fileextension, mode='at+',
                               encoding=self._file_encoding)
        if detailtime:
            timelog = time.asctime()
        else:
            timelog = self.time1()
        if inconsole:
            print(self.format(timelog, pos, level, txt))
        if not debugmodein:
            if not self._debuginanotherfile:
                f.write(self.format(timelog, pos, level, txt))
                f.close()
            if self._debuginanotherfile and level == 'debug':
                f_debug.write(self.format(timelog, pos, level, txt))
                f_debug.close()
                f.close()
            elif self._debuginanotherfile:
                f.write(self.format(timelog, pos, level, txt))
                f_debug.write(self.format(timelog, pos, level, txt))
                f_debug.close()
                f.close()
        if debugmodein:
            return self.format(timelog, pos, level, txt)
        del detailtime, inconsole, debugmodein, timelog

    def debug(self, params):
        """
            :param params: a dict contains:
            :param txt: the detail description of this log
            :param pos: show where the log's actual called positon in the code
            :param overrides: the overrides of the current config,only actives once
            available overrides: showinconsole , showdetailedtime
            :type params: dict
            :type txt: str
            :type pos: str, default:'main'
            :return: debug log
            """
        params['level'] = 'debug'
        if self._debugmode:
            return self.log(params)
        else:
            self.log(params)

    def info(self, params):
        """
            :param params: a dict contains:
            :param txt: the detail description of this log
            :param pos: show where the log's actual called positon in the code
            :type params: dict
            :type txt: str
            :type pos: str, default:'main'
            :return: info log
            """
        params['level'] = 'INFO'
        if self._debugmode:
            return self.log(params)
        else:
            self.log(params)

    def warn(self, params):
        """
            :param params: a dict contains:
            :param txt: the detail description of this log
            :param pos: show where the log's actual called positon in the code
            :param overrides: the overrides of the current config,only actives once
            available overrides: showinconsole , showdetailedtime
            :type params: dict
            :type txt: str
            :type pos: str, default:'main'
            :return: warning log
            """
        params['level'] = 'WARN'
        if self._debugmode:
            return self.log(params)
        else:
            self.log(params)

    def error(self, params):
        """
            :param params: a dict contains:
            :param txt: the detail description of this log
            :param pos: show where the log's actual called positon in the code
            :param overrides: the overrides of the current config,only actives once
            available overrides: showinconsole , showdetailedtime
            :type params: dict
            :type txt: str
            :type pos: str, default:'main'
            :return: error log
            """
        params['level'] = 'ERROR'
        if self._debugmode:
            return self.log(params)
        else:
            self.log(params)

    def fatal(self, params):
        """
            :param params: a dict contains:
            :param txt: the detail description of this log
            :param pos: show where the log's actual called positon in the code
            :param overrides: the overrides of the current config,only actives once
            available overrides: showinconsole , showdetailedtime
            :type params: dict
            :type txt: str
            :type pos: str, default:'main'
            :return: fatal log
        """
        params['level'] = 'FATAL'
        if self._debugmode:
            return self.log(params)
        else:
            self.log(params)
        if self._fatalexit:
            exit(10)

    def config(self, **kwargs):
        """
        :param kwargs:input config names and config data
        format: config_name = config_data
        :type kwargs: dict
        below are config_name and the description

        name : change the name of the log file, only actives when abolutepath config is off
        :type name: str, default 'log'

        fileextension : change the extension of the log file, only actives when abolutepath config is off
        :type fileextension: str, default '.log'

        absolutepath : change whether inputing the absolute path of the log file,
        True for using the name and fileextension to create file in the program running location
        False for using the route to create file in the specific location
        (note:the route should contain the extension of the file,like:D:\test.log)
        :type absolutepath: bool, default False

        route : change the file location, only activates when abolutepath config is on
        the route should contain the extension of the file
        :type route: str, default 'log.log'

        file_encoding : change the file encoding method
        :type file_encoding: encoding str, default 'utf-8'

        showdetailedtime : whether to show detailed time in the log file
        :type showdetailedtime: bool, default False

        showinconsole : whether to show the log in the python console
        :type showinconsole: bool, default True

        fatalexit : whether to exit the program after a fatal log
        :type fatalexit: bool, default False

        debuginanotherfile: whether to save debug logs in another file
        True: saving in <filename><debugfilename><fileextension>
        False:saving in <filename><fileextension>
        :type debuginanotherfile: bool, default False

        debugfilename: the <debugfilename> part above
        :type debugfilename: str, default '_debug'

        :return: complete config changing debug log
        """
        for configname, configdata in kwargs.items():

            if configname == "name":
                self._name = configdata
                f = open(self._name + self._fileextension, mode="w", encoding=self._file_encoding)
                f.close()

            if configname == 'debugfilename':
                self._debugfilename = configname

            elif configname == "fileextension":
                self._fileextension = configdata
                f = open(self._name + self._fileextension, mode="w", encoding=self._file_encoding)
                f.close()

            elif configname == "route":
                self._route = configdata
                f = open(self._route, mode="w", encoding=self._file_encoding)
                f.close()

            elif configname == "file_encoding":
                try:
                    if self._absolutepath:
                        tmpf = open(self._route, mode="w", encoding=configname)
                    else:
                        tmpf = open(self._name + self._fileextension, mode="w", encoding=configname)
                    tmpf.close()
                    self._file_encoding = configname
                except LookupError:
                    self.warn(
                        {'txt': "wrong file encoding config.this config is set to default", 'pos': "main_loggerjava",
                         'showinconsole': True})
                    self._file_encoding = "utf-8"

            elif configname == "showdetailedtime":
                if self.testformat(configdata, 1):
                    self._showdetailedtime = configdata
                else:
                    self.warn(
                        {'txt': "wrong detailed time config.this config is set to default", 'pos': "main_loggerjava",
                         'showinconsole': True})
                    self._showdetailedtime = False

            elif configname == "showinconsole":
                if self.testformat(configdata, 1):
                    self._showinconsole = configdata
                else:
                    self._showinconsole = True
                    self.warn(
                        {'txt': "wrong show in console config.this config is set to default", 'pos': "main_loggerjava"})

            elif configname == "absolutepath":
                if self.testformat(configdata, 1):
                    self._absolutepath = configdata
                    if self._absolutepath:
                        f = open(self._route, mode="w", encoding=self._file_encoding)
                    else:
                        f = open(self._name + self._fileextension, mode="w", encoding=self._file_encoding)
                    f.close()
                else:
                    self.warn(
                        {'txt': "wrong absolute path config.this config is set to default", 'pos': "main_loggerjava",
                         'showinconsole': True})
                    self._absolutepath = False
                    f = open(self._name + self._fileextension, mode="w", encoding=self._file_encoding)
                    f.close()

            elif configname == "debugmode":
                self._debugmode = configdata

            elif configname == "fatalexit":
                if self.testformat(configdata, 1):
                    self._fatalexit = configdata
                else:
                    self.warn({'txt': "wrong fatal exit config.this config is set to default", 'pos': "main_loggerjava",
                               'showinconsole': True})
                    self._fatalexit = False

            elif configname == "debuginanotherfile":
                if self.testformat(configdata, 1):
                    self._debuginanotherfile = configdata
                else:
                    self.warn({'txt': 'wrong debug in another file config. this config is set to default',
                               'pos': 'main_loggerjava', 'showinconsole': True})
                    self._debuginanotherfile = False
            self.log({'txt': "all given configs modified", 'level': "D", 'pos': "main_loggerjava.config",
                      'showinconsole': False})

    def clearcurrentlog(self):
        """
        clean the current log file
        :return: nothing
        """
        if self._absolutepath:
            f = open(self._route, mode="w", encoding=self._file_encoding)
        else:
            f = open(self._name + self._fileextension, mode="w", encoding=self._file_encoding)
        f.write("")
        f.close()
        if self._debuginanotherfile and self._absolutepath:
            f = open(os.path.splitext(self._route)[0] + self._debugfilename + os.path.splitext(self._route)[1],
                     mode='w', encoding=self._file_encoding)
        elif self._debuginanotherfile and not self._absolutepath:
            f = open(self._name + self._debugfilename + self._fileextension, mode='w', encoding=self._file_encoding)
        f.write("")
        f.close()

    def version(self):
        """
        show the current version of loggerjava
        :return: ver
        """
        print("Current loggerjava ver:%s" % self.ver)

    def test(self):
        """
        test the module
        :return: test outputs
        """
        test_loggerjava.testin()

    def exportconfig(self):
        """
        export current config
        use loadconfig(config) to load this exported config
        :return: a dictonary contains configs
        :rtype: dict
        """
        i = {"name": self._name, "fileextension": self._fileextension, "absolutepath": self._absolutepath,
             "route": self._route, "showdetailedtime": self._showdetailedtime, "showinconsole": self._showinconsole,
             "file_encoding": self._file_encoding, "fatalexit": self._fatalexit,
             "debuginanotherfile": self._debuginanotherfile, "debugfilename": self._debugfilename}
        return i

    def loadconfig(self, inputconfig):
        """
        load your saved config
        :param inputconfig: the config lib exported from exportconfig()
        :type inputconfig: dict
        :return: nothing
        """

        if self.testformat(inputconfig["absolutepath"], 1):
            self._absolutepath = inputconfig["absolutepath"]
        else:
            self.warn({'txt': "wrong absolute path config.this config is set to default", 'pos': "main_loggerjava",
                       'showinconsole': True})
            self._absolutepath = False

        self._name = inputconfig["name"]
        self._fileextension = inputconfig["fileextension"]
        self._route = inputconfig["route"]
        self._debugfilename = inputconfig['debugfilename']
        try:
            if _absolutepath:
                tmpf = open(_route, mode="w", encoding=inputconfig["file_encoding"])
            else:
                tmpf = open(_name + _fileextension, mode="w", encoding=inputconfig["file_encoding"])
            tmpf.close()
            self._file_encoding = inputconfig["file_encoding"]
        except LookupError:
            self.warn({'txt': "wrong file encoding config.this config is set to default",
                       'pos': "main_loggerjava", 'showinconsole': True})
            self._file_encoding = "utf-8"

        if _absolutepath:
            f = open(_route, mode="at+", encoding=_file_encoding)
        else:
            f = open(_name + _fileextension, mode="at+", encoding=_file_encoding)
        f.close()

        if self.testformat(inputconfig["showdetailedtime"], 1):
            self._showdetailedtime = inputconfig["showdetailedtime"]
        else:
            self.warn({'txt': "wrong detailed time config.this config is set to default",
                       'pos': "main_loggerjava", 'showinconsole': True})
            self._showdetailedtime = False

        if self.testformat(inputconfig["showinconsole"], 1):
            self._showinconsole = inputconfig["showinconsole"]
        else:
            self._showinconsole = True
            self.warn({'txt': "wrong show in console config.this config is set to default",
                       'pos': "main_loggerjava", 'showinconsole': True})

        if self.testformat(inputconfig["fatalexit"], 1):
            self._fatalexit = inputconfig["fatalexit"]
        else:
            self._fatalexit = False
            self.warn({'txt': "wrong fatal close config.this config is set to default",
                       'pos': "main_loggerjava", 'showinconsole': True})

        if self.testformat(inputconfig['debuginanotherfile'], 1):
            self._debuginanotherfile = inputconfig['debuginanotherfile']
        else:
            self._debuginanotherfile = False
            self.warn({'txt': "wrong debug in another file config.this config is set to default",
                       'pos': "main_loggerjava", 'showinconsole': True})
