if __name__ == '__main__':
    pass
import time

"""
class loggerjava:

    def __init__(self):
        self.name = "log"
        f = open(self.name+".log", "w")
        f.close()
        self.showdetailedtime = False
        self.showinconsole = True

    def debug(self, txt, pos="main"):
        level = 'debug'
        f = open(self.name + ".log", "at+")
        if self.showdetailedtime and self.showinconsole:
            f.write(self._formats.format(time.asctime(), pos, level, txt))
            print(self._formats.format(time.asctime(), pos, level, txt))
        elif not self.showdetailedtime and self.showinconsole:
            f.write(self._formats.format(self._formats.time1(), pos, level, txt))
            print(self._formats.format(self._formats.time1(), pos, level, txt))
        elif self.showdetailedtime and not self.showinconsole:
            f.write(self._formats.format(time.asctime(), pos, level, txt))
        else:
            f.write(self._formats.format(self._formats.time1(), pos, level, txt))
        f.close()

    def info(self, txt, pos="main"):
        level = 'INFO'
        f = open(self.name+".log", "at+")
        if self.showdetailedtime and self.showinconsole:
            f.write(self._formats.format(time.asctime(), pos, level, txt))
            print(self._formats.format(time.asctime(), pos, level, txt))
        elif not self.showdetailedtime and self.showinconsole:
            f.write(self._formats.format(self._formats.time1(), pos, level, txt))
            print(self._formats.format(self._formats.time1(), pos, level, txt))
        elif self.showdetailedtime and not self.showinconsole:
            f.write(self._formats.format(time.asctime(), pos, level, txt))
        else:
            f.write(self._formats.format(self._formats.time1(), pos, level, txt))
        f.close()

    def warn(self, txt, pos="main"):
        level = 'WARN'
        f = open(self.name + ".log", "at+")
        if self.showdetailedtime and self.showinconsole:
            f.write(self._formats.format(time.asctime(), pos, level, txt))
            print(self._formats.format(time.asctime(), pos, level, txt))
        elif not self.showdetailedtime and self.showinconsole:
            f.write(self._formats.format(self._formats.time1(), pos, level, txt))
            print(self._formats.format(self._formats.time1(), pos, level, txt))
        elif self.showdetailedtime and not self.showinconsole:
            f.write(self._formats.format(time.asctime(), pos, level, txt))
        else:
            f.write(self._formats.format(self._formats.time1(), pos, level, txt))
        f.close()

    def Error(self, txt, pos="main"):
        level = 'ERROR'
        f = open(self.name + ".log", "at+")
        if self.showdetailedtime and self.showinconsole:
            f.write(self._formats.format(time.asctime(), pos, level, txt))
            print(self._formats.format(time.asctime(), pos, level, txt))
        elif not self.showdetailedtime and self.showinconsole:
            f.write(self._formats.format(self._formats.time1(), pos, level, txt))
            print(self._formats.format(self._formats.time1(), pos, level, txt))
        elif self.showdetailedtime and not self.showinconsole:
            f.write(self._formats.format(time.asctime(), pos, level, txt))
        else:
            f.write(self._formats.format(self._formats.time1(), pos, level, txt))
        f.close()

    def FATAL(self, txt, pos="main"):
        level = 'FATAL'
        f = open(self.name + ".log", "at+")
        if self.showdetailedtime and self.showinconsole:
            f.write(self._formats.format(time.asctime(), pos, level, txt))
            print(self._formats.format(time.asctime(), pos, level, txt))
        elif not self.showdetailedtime and self.showinconsole:
            f.write(self._formats.format(self._formats.time1(), pos, level, txt))
            print(self._formats.format(self._formats.time1(), pos, level, txt))
        elif self.showdetailedtime and not self.showinconsole:
            f.write(self._formats.format(time.asctime(), pos, level, txt))
        else:
            f.write(self._formats.format(self._formats.time1(), pos, level, txt))
        f.close()

    def config(self, name="log", showdetailedtime=False, showinconsole=False):
        self.name = name
        f = open(self.name + ".log", "w")
        f.close()
        if not showdetailedtime or showdetailedtime:
            self.showdetailedtime = showdetailedtime
        else:
            print("wrong detailed time config\nthis config is set to normal")
            self.showdetailedtime = False
        if not showinconsole or showinconsole:
            self.showinconsole = showinconsole
        else:
            print("wrong detailed time config\nthis config is set to normal")
            self.showinconsole = False

    # noinspection PyMethodParameters
    class _formats:
        def format(time1, place, level, txt):
            return "[%s] [%s/%s]: %s\n" % (time1, place, level, txt)

        def time1():
            return str(time.localtime().tm_hour).rjust(2, "0")+":" +\
                str(time.localtime().tm_min).rjust(2, "0")+":"+str(time.localtime().tm_sec).rjust(2, "0")


"""