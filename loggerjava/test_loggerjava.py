import time

import loggerjava as lj
import loggerjava.exceptionhandler


def _test1():
    raise UserWarning('testing warning')

class _test2():
    def prtest(self):
        raise ValueError


loggerjava.exceptionhandler.register_def(_test1)
loggerjava.exceptionhandler.register_def(_test2)


def testin():
    print('\n')
    logger = lj
    logger.config(debugmode=True, showdetailedtime=False)
    try:
        _test1()
    except Exception as e:
        a = loggerjava.exceptionhandler.handler(e)
        assert a == 'UserWarning: testing warning\n' \
                    '    at testin (test_loggerjava.py:24)\n' \
                    '    at _test1._test1 (test_loggerjava.py:8)\n'
    try:
        a = _test2
        a.prtest(a)
    except Exception as e:
        assert loggerjava.exceptionhandler.handler(e) == 'ValueError: \n'\
                                                        '    at testin (test_loggerjava.py:32)\n'\
                                                        '    at _test2.prtest (test_loggerjava.py:12)\n'

    print("\n")
    assert logger.info("test1") == "[%02d:%02d:%02d]" % (time.localtime().tm_hour, time.localtime().tm_min,
                                                         time.localtime().tm_sec) + " [main/INFO]: test1\n"
    assert logger.debug("test2") == "[%02d:%02d:%02d]" % (time.localtime().tm_hour, time.localtime().tm_min,
                                                          time.localtime().tm_sec) + " [main/debug]: test2\n"
    assert logger.warn("test3") == "[%02d:%02d:%02d]" % (time.localtime().tm_hour, time.localtime().tm_min,
                                                         time.localtime().tm_sec) + " [main/WARN]: test3\n"
    assert logger.error("test4") == "[%02d:%02d:%02d]" % (time.localtime().tm_hour, time.localtime().tm_min,
                                                          time.localtime().tm_sec) + " [main/ERROR]: test4\n"
    assert logger.fatal("test5") == "[%02d:%02d:%02d]" % (time.localtime().tm_hour, time.localtime().tm_min,
                                                          time.localtime().tm_sec) + " [main/FATAL]: test5\n"
    assert logger.info("test6", pos="testing") == "[%02d:%02d:%02d]" % (
        time.localtime().tm_hour, time.localtime().tm_min,
        time.localtime().tm_sec) + " [testing/INFO]: test6\n"
    # logger.config(name="test")
    # assert logger._name == "test"
    logger.config(showdetailedtime=True)
    assert logger.info("test8") == "[" + time.asctime() + "] [main/INFO]: test8\n"
    logger.config(showdetailedtime=False)
    assert logger.log("testoverride", level="d",
                      showdetailedtime=True) == "[" + time.asctime() + "] [main/debug]: testoverride\n"
    assert logger.warn("testoverride", showdetailedtime=True) == "[" + time.asctime() + "] [main/WARN]: testoverride\n"


if __name__ == "__main__":
    testin()
