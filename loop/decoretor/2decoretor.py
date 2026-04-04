def debug(func):
    def wrapper(*args, **kwargs):
        arg_valu='. '.join(str(arg)for arg in args)
        kwargs_value='. '.join(f"{key}={value}"for key,value in kwargs.items())
        print(f"Calling {func.__name__} with args: {arg_valu}, kwargs: {kwargs_value}")
        result=func(*args,**kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper
    
@debug
def add(a,b):
    return a+b

add(1,2)