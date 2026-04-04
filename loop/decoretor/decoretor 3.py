import time

def  cach(func):
    cache={}
    print(cache)
    def wrapper(*args,):
        if args in cache:
            return cache[args]
        result=func(*args)
        cache[args]=result
        return result
    return wrapper

@cach
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10))