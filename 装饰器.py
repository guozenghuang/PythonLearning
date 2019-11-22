import time

def set_fun(func):
    def call_fun():
        starttime = time.time()
        func()
        stoptime = time.time()
        print("time:%f" % (stoptime - starttime))
    return call_fun

@set_fun # 等价于test = set_fun(test1)
def test():
    print("---test---")
    for i in range(10000):
        pass

test()

test()
