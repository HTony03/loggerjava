import unittest
import loggerjava as lj
import pytest
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
def test():
    lj.config(debuging = True)
    print("\n")
    assert lj.info("test1") == "["+str(time.localtime().tm_hour).rjust(2, "0") + ":" + \
            str(time.localtime().tm_min).rjust(2, "0") + ":" + str(time.localtime().tm_sec).rjust(2, "0")+"] [main/INFO]: test1\n"
    assert lj.debug("test2") == "[" + str(time.localtime().tm_hour).rjust(2, "0") + ":" + \
           str(time.localtime().tm_min).rjust(2, "0") + ":" + str(time.localtime().tm_sec).rjust(2,"0") + "] [main/debug]: test2\n"
    assert lj.warn("test3") == "[" + str(time.localtime().tm_hour).rjust(2, "0") + ":" + \
           str(time.localtime().tm_min).rjust(2, "0") + ":" + str(time.localtime().tm_sec).rjust(2,"0") + "] [main/WARN]: test3\n"
    assert lj.error("test4") == "[" + str(time.localtime().tm_hour).rjust(2, "0") + ":" + \
           str(time.localtime().tm_min).rjust(2, "0") + ":" + str(time.localtime().tm_sec).rjust(2,"0") + "] [main/ERROR]: test4\n"
    assert lj.fatal("test5") == "[" + str(time.localtime().tm_hour).rjust(2, "0") + ":" + \
           str(time.localtime().tm_min).rjust(2, "0") + ":" + str(time.localtime().tm_sec).rjust(2,"0") + "] [main/FATAL]: test5\n"
    lj.config(name = "test")
    assert lj.name == "test"
    lj.config(showdetailedtime = True)
    assert lj.info("test7") == "[" + time.asctime() + "] [main/INFO]: test7\n"