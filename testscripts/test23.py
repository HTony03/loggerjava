import loggerjava
import loggerjava.exceptionhandler
if __name__ == "__main__":pass
def test1(a):
    print(b)
class test2():
    def printa():
        print(b)
loggerjava.exceptionhandler.register_def(test1)
loggerjava.exceptionhandler.register_def(test2)
if __name__ == "__main__":
    try:
        test1(1)
    except Exception as E:
        loggerjava.error(loggerjava.exceptionhandler.handler(E))
    try:
        a = test2
        a.printa()
    except Exception as E:
        loggerjava.error(loggerjava.exceptionhandler.handler(E))