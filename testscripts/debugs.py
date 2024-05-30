#import loggerjava
import time

import loggerjava.exceptionhandler

from loggerjava import debugging

def debugging1(when):
    from loggerjava import debug
    def log(f, *args, **kwargs):
        debug("""func called:
        function : %s
        args : %s
        kwargs : %s
        """ % (f, args, kwargs),type='D')

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
                debug("time dela : " + (time.time() - now),type='D')

        return wrapper

    try:
        return {"pre": pre_log, "post": post_log}[when]
    except KeyError:
        raise ValueError


@debugging("pre")
def test(arg,**kwargs):
    print(arg + " test")

#@debugging("pre")
class testss():
    @debugging("pre")
    def p(self,*arg,**kwargs):print(arg)

    def te(self):
        print(testa)


if __name__ == "__main__":
    pass
#loggerjava.exceptionhandler.register_def(test)
loggerjava.exceptionhandler.register_def(testss)
test("test",test=True)
a = testss()
a.p("testt",test=True)
try:
    a.te()
except Exception as E:
    print(loggerjava.exceptionhandler.handler(E))