if __name__ == '__main__':
    pass

import time
import test_loggerjava

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
        self._fatalclose = False
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
        if 'pos' not in params.items():
            pos = "main"
        else:
            pos = params['pos']
        txt = params['txt']
        # log
        if self._absolutepath:
            f = open(self._route, mode="at+", encoding=self._file_encoding)
            if self._debuginanotherfile:
                f_debug = open(self._route + self._debugfilename, mode='at+', encoding=self._file_encoding)
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
            :param txt: the detail description of this log
            :param pos: show where the log's actual called positon in the code
            :param overrides: the overrides of the current config,only actives once
            available overrides: showinconsole , showdetailedtime
            :return: debug log
            """
        params['level'] = 'debug'
        if self._debugmode:
            return self.log(params)
        else:
            self.log(params)

    def info(self, params):
        """
            :param txt: the detail description of this log
            :param pos: show where the log's actual called positon in the code
            :return: info log
            """
        params['level'] = 'INFO'
        if self._debugmode:
            return self.log(params)
        else:
            self.log(params)

    def warn(self, params):
        """
            :param txt: the detail description of this log
            :param pos: show where the log's actual called positon in the code
            :param overrides: the overrides of the current config,only actives once
            available overrides: showinconsole , showdetailedtime
            :return: warning log
            """
        params['level'] = 'WARN'
        if self._debugmode:
            return self.log(params)
        else:
            self.log(params)

    def error(self, params):
        """
            :param txt: the detail description of this log
            :param pos: show where the log's actual called positon in the code
            :param overrides: the overrides of the current config,only actives once
            available overrides: showinconsole , showdetailedtime
            :return: error log
            """
        params['level'] = 'ERROR'
        if self._debugmode:
            return self.log(params)
        else:
            self.log(params)

    def fatal(self, params):
        """
            :param txt: the detail description of this log
            :param pos: show where the log's actual called positon in the code
            :param overrides: the overrides of the current config,only actives once
            available overrides: showinconsole , showdetailedtime
            :return: fatal log
        """
        params['level'] = 'FATAL'
        if self._debugmode:
            return self.log(params)
        else:
            self.log(params)
        if self._fatalclose:
            exit(10)


    def config(self, **kwargs):
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
        for configname, configdata in kwargs.items():

            if configname == "name":
                self._name = configdata
                f = open(self._name + self._fileextension, mode="w", encoding=self._file_encoding)
                f.close()

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
                    self.warn({'txt':"wrong file encoding config.this config is set to default", 'pos':"main_loggerjava",
                         'showinconsole':True})
                    self._file_encoding = "utf-8"

            elif configname == "showdetailedtime":
                if self.testformat(configdata, 1):
                    self._showdetailedtime = configdata
                else:
                    self.warn({'txt':"wrong detailed time config.this config is set to default", 'pos':"main_loggerjava",
                         'showinconsole':True})
                    self._showdetailedtime = False

            elif configname == "showinconsole":
                if self.testformat(configdata, 1):
                    self._showinconsole = configdata
                else:
                    self._showinconsole = True
                    self.warn({'txt':"wrong show in console config.this config is set to default", 'pos':"main_loggerjava"})

            elif configname == "absolutepath":
                if self.testformat(configdata, 1):
                    self._absolutepath = configdata
                    if self._absolutepath:
                        f = open(self._route, mode="w", encoding=self._file_encoding)
                    else:
                        f = open(self._name + self._fileextension, mode="w", encoding=self._file_encoding)
                    f.close()
                else:
                    self.warn({'txt':"wrong absolute path config.this config is set to default", 'pos':"main_loggerjava",
                         'showinconsole':True})
                    self._absolutepath = False
                    f = open(self._name + self._fileextension, mode="w", encoding=self._file_encoding)
                    f.close()
            elif configname == "debugmode":
                self._debugmode = configdata
            elif configname == "fatalexit":
                if self.testformat(configdata, 1):
                    self._fatalclose = configdata
                else:
                    self.warn({'txt':"wrong fatal exit config.this config is set to default", 'pos':"main_loggerjava", 'showinconsole':True})
                    self._fatalclose = False
            self.log({'txt':"all given configs modified",'level':"D",'pos':"main_loggerjava.config",'showinconsole':False})


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
        # TODO:debug type
        if self._debuginanotherfile and self._absolutepath:
            f = open(self._route[:-4])


    def version(self):
        """
        show the current version of loggerjava
        :return:
        """
        print("Current loggerjava ver:%s" % self.ver)


    def test(self):
        test_loggerjava.testin()


    def exportconfig(self):
        """
        export current config
        use loadconfig(config) to load this exported config
        returning as a lib
        :return: a dictonary contains configs
        """
        i = {"_name": self._name, "fileextension": self._fileextension, "absolutepath": self._absolutepath,
             "route": self._route, "showdetailedtime": self._showdetailedtime, "showinconsole": self._showinconsole,
             "file_encoding": self._file_encoding, "fatalexit": self._fatalclose,
             "debuginanotherfile": self._debuginanotherfile, "debugfilename":self._debugfilename}
        return i
