import functools
import time

def timing(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        val = func(*args,**kwargs)
        end = time.time()
        print(func,'\ntime spend',round(end-start,5))
        return val
    return wrapper

@timing
def f(num):
    for i in range(num):
        pass

@timing
def g(num):
    for i in range(num):
        pass


count = 1000000
f(count)
g(count)
