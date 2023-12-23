import time
if __name__ == '__main__':
    pass

ver = "0.0.4"
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
    global showdetailedtimein, showinconsolein,namein
    namein = name
    f = open(namein + ".log", "w")
    f.close()
    if not showdetailedtime or showdetailedtime:
        showdetailedtimein = showdetailedtime
    else:
        print("wrong detailed time config\nthis config is set to normal")
        showdetailedtimein = False
    if not showinconsole or showinconsole:
        showinconsolein = showinconsole
    else:
        print("wrong detailed time config\nthis config is set to normal")
        showinconsolein = True


def version():
    """
    show the current version of loggerjava
    :return:
    """
    print("Current loggerjava ver:%s"%ver)


# noinspection PyMethodParameters
class _output:

    def format(time1, place, level, txt):
        return "[%s] [%s/%s]: %s\n" % (time1, place, level, txt)

    def time1():
        return str(time.localtime().tm_hour).rjust(2, "0") + ":" + \
            str(time.localtime().tm_min).rjust(2, "0") + ":" + str(time.localtime().tm_sec).rjust(2, "0")