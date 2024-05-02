import unittest
import loggerjava as lj
# import pytest
import time

import loggerjava.exceptionhandler

"""
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
        """

"""
if __name__ == '__main__':
    unittest.main()
"""


def _test1():
    raise UserWarning('testing warning')


loggerjava.exceptionhandler.register_def(_test1)


def testin():
    print('\n')
    logger = lj
    logger.config(debugmode=True, showdetailedtime=False)
    try:

        _test1()
    except Exception as e:
        a = loggerjava.exceptionhandler.handler(e)
        assert a == 'UserWarning: testing warning\n' \
                    '    at testin (test_loggerjava.py:33)\n' \
                    '    at _test1._test1 (test_loggerjava.py:21)\n'
        assert logger.warn(loggerjava.exceptionhandler.handler(e)) == \
               "[%02d:%02d:%02d]"%(time.localtime().tm_hour , time.localtime().tm_min , time.localtime().tm_sec) +  \
               " [main/WARN]: %s\n" %a
    print("\n")
    assert logger.info("test1") == "[%02d:%02d:%02d]"%(time.localtime().tm_hour , time.localtime().tm_min , \
                                                     time.localtime().tm_sec) + " [main/INFO]: test1\n"
    assert logger.debug("test2") == "[%02d:%02d:%02d]"%(time.localtime().tm_hour , time.localtime().tm_min , \
                                                     time.localtime().tm_sec) + " [main/debug]: test2\n"
    assert logger.warn("test3") == "[%02d:%02d:%02d]"%(time.localtime().tm_hour , time.localtime().tm_min , \
                                                     time.localtime().tm_sec) + " [main/WARN]: test3\n"
    assert logger.error("test4") == "[%02d:%02d:%02d]"%(time.localtime().tm_hour , time.localtime().tm_min , \
                                                     time.localtime().tm_sec) + " [main/ERROR]: test4\n"
    assert logger.fatal("test5") == "[%02d:%02d:%02d]"%(time.localtime().tm_hour , time.localtime().tm_min , \
                                                     time.localtime().tm_sec) + " [main/FATAL]: test5\n"
    assert logger.info("test6", pos="testing") == "[%02d:%02d:%02d]"%(time.localtime().tm_hour , time.localtime().tm_min , \
                                                     time.localtime().tm_sec) + " [testing/INFO]: test6\n"
    logger.config(name="test")
    assert logger._name == "test"
    logger.config(showdetailedtime=True)
    assert logger.info("test8") == "[" + time.asctime() + "] [main/INFO]: test8\n"
    logger.config(showdetailedtime=False)
    assert logger.log("testoverride", type="d",
                      showdetailedtime=True) == "[" + time.asctime() + "] [main/debug]: testoverride\n"
    assert logger.warn("testoverride", showdetailedtime=True) == "[" + time.asctime() + "] [main/WARN]: testoverride\n"

if __name__ == "__main__":
    testin()
