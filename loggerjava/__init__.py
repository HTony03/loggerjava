import time
if __name__ == '__main__':
    pass

ver = "0.0.5"
namein = "log"
f = open(namein + ".log", "w")
f.close()
showdetailedtimein = False
showinconsolein = True


def debug(txt, pos="main"):
    """

        :param txt: the detail description of this log
        :param pos: show where the log's actual called positon in the code
        :return:
        """
    level = 'debug'
    f = open(namein + ".log", "at+")
    if showdetailedtimein and showinconsolein:
        f.write(_output.format(time.asctime(), pos, level, txt))
        print(_output.format(time.asctime(), pos, level, txt))
    elif not showdetailedtimein and showinconsolein:
        f.write(_output.format(_output.time1(), pos, level, txt))
        print(_output.format(_output.time1(), pos, level, txt))
    elif showdetailedtimein and not showinconsolein:
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
    f = open(namein + ".log", "at+")
    if showdetailedtimein and showinconsolein:
        f.write(_output.format(time.asctime(), pos, level, txt))
        print(_output.format(time.asctime(), pos, level, txt))
    elif not showdetailedtimein and showinconsolein:
        f.write(_output.format(_output.time1(), pos, level, txt))
        print(_output.format(_output.time1(), pos, level, txt))
    elif showdetailedtimein and not showinconsolein:
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
    f = open(namein + ".log", "at+")
    if showdetailedtimein and showinconsolein:
        f.write(_output.format(time.asctime(), pos, level, txt))
        print(_output.format(time.asctime(), pos, level, txt))
    elif not showdetailedtimein and showinconsolein:
        f.write(_output.format(_output.time1(), pos, level, txt))
        print(_output.format(_output.time1(), pos, level, txt))
    elif showdetailedtimein and not showinconsolein:
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
    f = open(namein + ".log", "at+")
    if showdetailedtimein and showinconsolein:
        f.write(_output.format(time.asctime(), pos, level, txt))
        print(_output.format(time.asctime(), pos, level, txt))
    elif not showdetailedtimein and showinconsolein:
        f.write(_output.format(_output.time1(), pos, level, txt))
        print(_output.format(_output.time1(), pos, level, txt))
    elif showdetailedtimein and not showinconsolein:
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
    f = open(namein + ".log", "at+")
    if showdetailedtimein and showinconsolein:
        f.write(_output.format(time.asctime(), pos, level, txt))
        print(_output.format(time.asctime(), pos, level, txt))
    elif not showdetailedtimein and showinconsolein:
        f.write(_output.format(_output.time1(), pos, level, txt))
        print(_output.format(_output.time1(), pos, level, txt))
    elif showdetailedtimein and not showinconsolein:
        f.write(_output.format(time.asctime(), pos, level, txt))
    else:
        f.write(_output.format(_output.time1(), pos, level, txt))
    f.close()


def config(name="log", showdetailedtime=False, showinconsole=True):
    """

    :param name: output log file name
    :param showdetailedtime: output log time format,False for short time, True for long time
    :param showinconsole:whether output log will show in python console
    :return:
    """
    global namein, showdetailedtimein, showinconsolein
    namein = name
    f = open(namein + ".log", "w")
    f.close()
    if showdetailedtime or not showdetailedtime:
        showdetailedtimein = showdetailedtime
    else:
        tmpin = showinconsolein
        showinconsolein = True
        warn("wrong detailed time config.this config is set to normal", pos="main_loggerjava")
        showinconsolein = tmpin
        showdetailedtimein = False
        del tmpin
    if showinconsole or not showinconsole:
        showinconsolein = showinconsole
    else:
        showinconsolein = True
        warn("wrong show in console config.this config is set to normal", pos="main_loggerjava")


def version():
    """
    show the current version of loggerjava
    :return:
    """
    print("Current loggerjava ver:%s" % ver)


def outputconfig():
    """
    output current config
    use loadconfig(config) to load this outputed config
    returning as a lib
    :return:
    """
    i = {"name": namein, "showdetailedtime": showdetailedtimein, "showinconsole": showinconsolein}
    return i


def loadconfig(inputconfig):
    """

    :param inputconfig: the config lib outputed from outputconfig()
    :return:
    """
    global namein, showdetailedtimein, showinconsolein
    namein = inputconfig["name"]
    f = open(namein + ".log", "w")
    f.close()
    if inputconfig["showdetailedtime"] or not inputconfig["showdetailedtime"]:
        showdetailedtimein = inputconfig["showdetailedtime"]
    else:
        tmpin = showinconsolein
        showinconsolein = True
        warn("wrong detailed time config.this config is set to normal", pos="main_loggerjava")
        showinconsolein = tmpin
        showdetailedtimein = False
        del tmpin
    if inputconfig["showinconsole"] or not inputconfig["showinconsole"]:
        showinconsolein = inputconfig["showinconsole"]
    else:
        showinconsolein = True
        warn("wrong show in console config.this config is set to normal", pos="main_loggerjava")

# noinspection PyMethodParameters


class _output:

    def format(time1, place, level, txt):
        return "[%s] [%s/%s]: %s\n" % (time1, place, level, txt)

    def time1():
        return str(time.localtime().tm_hour).rjust(2, "0") + ":" + \
            str(time.localtime().tm_min).rjust(2, "0") + ":" + str(time.localtime().tm_sec).rjust(2, "0")
