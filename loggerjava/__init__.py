import time
if __name__ == '__main__':
    pass

ver = "0.0.6"
name = "log"
absolutepath = False
showdetailedtime = False
showinconsole = True
filetype = ".log"
file_encoding = "utf-8"
route = r"log.log"


# noinspection PyTypeChecker
def debug(txt, pos="main"):
    """

        :param txt: the detail description of this log
        :param pos: show where the log's actual called positon in the code
        :return:
        """
    level = 'debug'
    if absolutepath:
        f = open(route, mode="at+", encoding=file_encoding)
    else:
        f = open(name + filetype, mode="at+", encoding=file_encoding)
    if showdetailedtime and showinconsole:
        f.write(_output.format(time.asctime(), pos, level, txt))
        print(_output.format(time.asctime(), pos, level, txt))
    elif not showdetailedtime and showinconsole:
        f.write(_output.format(_output.time1(), pos, level, txt))
        print(_output.format(_output.time1(), pos, level, txt))
    elif showdetailedtime and not showinconsole:
        f.write(_output.format(time.asctime(), pos, level, txt))
    else:
        f.write(_output.format(_output.time1(), pos, level, txt))
    f.close()


def info(txt, pos="main"):
    """

        :param txt: the detail description of this log
        :param pos: show where the log's actual called positon in the code
        :return:
        """
    level = 'INFO'
    if absolutepath:
        f = open(route, mode="at+", encoding=file_encoding)
    else:
        f = open(name + filetype, mode="at+", encoding=file_encoding)
    if showdetailedtime and showinconsole:
        # noinspection PyTypeChecker
        f.write(_output.format(time.asctime(), pos, level, txt))
        print(_output.format(time.asctime(), pos, level, txt))
    elif not showdetailedtime and showinconsole:
        f.write(_output.format(_output.time1(), pos, level, txt))
        print(_output.format(_output.time1(), pos, level, txt))
    elif showdetailedtime and not showinconsole:
        f.write(_output.format(time.asctime(), pos, level, txt))
    else:
        f.write(_output.format(_output.time1(), pos, level, txt))
    f.close()


def warn(txt, pos="main"):
    """

        :param txt: the detail description of this log
        :param pos: show where the log's actual called positon in the code
        :return:
        """
    level = 'WARN'
    if absolutepath:
        f = open(route, mode="at+", encoding=file_encoding)
    else:
        f = open(name + filetype, mode="at+", encoding=file_encoding)
    if showdetailedtime and showinconsole:
        f.write(_output.format(time.asctime(), pos, level, txt))
        print(_output.format(time.asctime(), pos, level, txt))
    elif not showdetailedtime and showinconsole:
        f.write(_output.format(_output.time1(), pos, level, txt))
        print(_output.format(_output.time1(), pos, level, txt))
    elif showdetailedtime and not showinconsole:
        f.write(_output.format(time.asctime(), pos, level, txt))
    else:
        f.write(_output.format(_output.time1(), pos, level, txt))
    f.close()


def error(txt, pos="main"):
    """

        :param txt: the detail description of this log
        :param pos: show where the log's actual called positon in the code
        :return:
        """
    level = 'ERROR'
    if absolutepath:
        f = open(route, mode="at+", encoding=file_encoding)
    else:
        f = open(name + filetype, mode="at+", encoding=file_encoding)
    if showdetailedtime and showinconsole:
        f.write(_output.format(time.asctime(), pos, level, txt))
        print(_output.format(time.asctime(), pos, level, txt))
    elif not showdetailedtime and showinconsole:
        f.write(_output.format(_output.time1(), pos, level, txt))
        print(_output.format(_output.time1(), pos, level, txt))
    elif showdetailedtime and not showinconsole:
        f.write(_output.format(time.asctime(), pos, level, txt))
    else:
        f.write(_output.format(_output.time1(), pos, level, txt))
    f.close()


def fatal(txt, pos="main"):
    """

    :param txt: the detail description of this log
    :param pos: show where the log's actual called positon in the code
    :return:
    """
    level = 'FATAL'
    if absolutepath:
        f = open(route, mode="at+", encoding=file_encoding)
    else:
        f = open(name + filetype, mode="at+", encoding=file_encoding)
    if showdetailedtime and showinconsole:
        f.write(_output.format(time.asctime(), pos, level, txt))
        print(_output.format(time.asctime(), pos, level, txt))
    elif not showdetailedtime and showinconsole:
        f.write(_output.format(_output.time1(), pos, level, txt))
        print(_output.format(_output.time1(), pos, level, txt))
    elif showdetailedtime and not showinconsole:
        f.write(_output.format(time.asctime(), pos, level, txt))
    else:
        f.write(_output.format(_output.time1(), pos, level, txt))
    f.close()


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

    :return:
    """
    global showinconsole, showdetailedtime, absolutepath, name, filetype, file_encoding, route
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
                    tmpf = open(name+filetype, mode="w", encoding=configname)
                tmpf.close()
                file_encoding = configname
                del tmpf
                if absolutepath:
                    f = open(route, mode="w", encoding=file_encoding)
                else:
                    f = open(name+filetype, mode="w", encoding=file_encoding)
                f.close()
            except LookupError:
                warn("wrong file encoding config.this config is set to normal", pos="main_loggerjava")
                file_encoding = "utf-8"

        elif configname == "showdetailedtime":
            if configdata or not configdata:
                showdetailedtime = configdata
            else:
                tmpin = showinconsole
                showinconsole = True
                warn("wrong detailed time config.this config is set to normal", pos="main_loggerjava")
                showinconsole = tmpin
                showdetailedtime = False
                del tmpin

        elif configname == "showinconsole":
            if configdata or not configdata:
                showinconsole = configdata
            else:
                showinconsole = True
                warn("wrong show in console config.this config is set to normal", pos="main_loggerjava")

        elif configname == "absolutepath":
            if configdata or not configdata:
                absolutepath = configdata
                if absolutepath:
                    f = open(route, mode="w", encoding=file_encoding)
                else:
                    f = open(name+filetype, mode="w", encoding=file_encoding)
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


def version():
    """
    show the current version of loggerjava
    :return:
    """
    print("Current loggerjava ver:%s" % ver)


def exportconfig():
    """
    export current config
    use loadconfig(config) to load this exported config
    returning as a lib
    :return:
    """
    i = {"name": name, "filetype": filetype, "absolutepath": absolutepath,
         "route": route, "showdetailedtime": showdetailedtime, "showinconsole": showinconsole,
         "file_encoding": file_encoding}
    return i


def loadconfig(inputconfig):
    """

    :param inputconfig: the config lib exported from exportconfig()
    :return:
    """
    global name, showdetailedtime, showinconsole, absolutepath, filetype, file_encoding, route

    if inputconfig["absolutepath"] or not inputconfig["absolutepath"]:
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

    if inputconfig["showdetailedtime"] or not inputconfig["showdetailedtime"]:
        showdetailedtime = inputconfig["showdetailedtime"]
    else:
        tmpin = showinconsole
        showinconsole = True
        warn("wrong detailed time config.this config is set to normal", pos="main_loggerjava")
        showinconsole = tmpin
        showdetailedtime = False
        del tmpin

    if inputconfig["showinconsole"] or not inputconfig["showinconsole"]:
        showinconsole = inputconfig["showinconsole"]
    else:
        showinconsole = True
        warn("wrong show in console config.this config is set to normal", pos="main_loggerjava")

# noinspection PyMethodParameters


class _output:

    def format(time1, place, level, txt):
        return "[%s] [%s/%s]: %s\n" % (time1, place, level, txt)

    def time1():
        return str(time.localtime().tm_hour).rjust(2, "0") + ":" + \
            str(time.localtime().tm_min).rjust(2, "0") + ":" + str(time.localtime().tm_sec).rjust(2, "0")
