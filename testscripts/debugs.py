#import loggerjava
import time

import loggerjava.exceptionhandler

from loggerjava import debugging
import loggerjava
loggerjava.clearcurrentlog()
loggerjava.config(showinconsole=False)

@debugging("pre")
def test(arg,**kwargs):
    print(arg + " test")

#@debugging("pre")
class testss():
    @debugging("pre")
    def p(self,*arg,**kwargs):print(arg)
    @debugging("post")
    def te(self,*arg,**kwargs):
        print("woah:"+str(arg)+str(kwargs))


if __name__ == "__main__":
    pass
#loggerjava.exceptionhandler.register_def(test)
loggerjava.exceptionhandler.register_def(testss)
test("test",test=True)
a = testss()
a.p("testt",test=True)
a.te("hmm?")
