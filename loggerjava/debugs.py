import loggerjava
import time


def debugging(when):
    def log(f,*args,**kwargs):
        print("""func called:
        function : %s
        args : %s
        kwargs : %s
        """%(f, args, kwargs))
    def pre_log(f):
        def wrapper(*args,**kwargs):
            log(f,*args,**kwargs)
            return f(*args,**kwargs)
        return wrapper
    def post_log(f):
        def wrapper(*args,**kwatgs):
            now = time.time()
            try:
                return f(*args,**kwatgs)
            finally:
                log(f,*args,**kwatgs)
                print("time dela : "+(time.time()-now))
        return  wrapper
    try:
        return {"pre":pre_log,"post":post_log}[when]
    except KeyError:
        raise ValueError
@debugging("pre")
def test(arg):
    print(arg+" test")

if __name__ == "__main__":
    pass
test("test")