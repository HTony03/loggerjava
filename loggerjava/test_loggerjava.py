import unittest
import loggerjava as lj
# import pytest
import time

"""
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
        """

"""
if __name__ == '__main__':
    unittest.main()
"""


def testin():
    logger = lj
    logger.config(debuging=True, showdetailedtime=False)
    print("\n")
    assert logger.info("test1") == "[" + str(time.localtime().tm_hour).rjust(2, "0") + ":" + \
           str(time.localtime().tm_min).rjust(2, "0") + ":" + str(time.localtime().tm_sec).rjust(2,
                                                                                                 "0") + "] [main/INFO]: test1\n"
    assert logger.debug("test2") == "[" + str(time.localtime().tm_hour).rjust(2, "0") + ":" + \
           str(time.localtime().tm_min).rjust(2, "0") + ":" + str(time.localtime().tm_sec).rjust(2,
                                                                                                 "0") + "] [main/debug]: test2\n"
    assert logger.warn("test3") == "[" + str(time.localtime().tm_hour).rjust(2, "0") + ":" + \
           str(time.localtime().tm_min).rjust(2, "0") + ":" + str(time.localtime().tm_sec).rjust(2,
                                                                                                 "0") + "] [main/WARN]: test3\n"
    assert logger.error("test4") == "[" + str(time.localtime().tm_hour).rjust(2, "0") + ":" + \
           str(time.localtime().tm_min).rjust(2, "0") + ":" + str(time.localtime().tm_sec).rjust(2,
                                                                                                 "0") + "] [main/ERROR]: test4\n"
    assert logger.fatal("test5") == "[" + str(time.localtime().tm_hour).rjust(2, "0") + ":" + \
           str(time.localtime().tm_min).rjust(2, "0") + ":" + str(time.localtime().tm_sec).rjust(2,
                                                                                                 "0") + "] [main/FATAL]: test5\n"
    assert logger.info("test6", pos="testing") == "[" + str(time.localtime().tm_hour).rjust(2, "0") + ":" + \
           str(time.localtime().tm_min).rjust(2, "0") + ":" + str(time.localtime().tm_sec).rjust(2,
                                                                                                 "0") + "] [testing/INFO]: test6\n"
    logger.config(name="test")
    assert logger.name == "test"
    logger.config(showdetailedtime=True)
    assert logger.info("test8") == "[" + time.asctime() + "] [main/INFO]: test8\n"


if __name__ == "__main__":
    testin()
