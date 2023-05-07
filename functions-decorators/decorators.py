import time


def write_decorator(func):
    def wrapper(*args):
        seconds = time.time()
        f = open("log.txt", "a")
        f.write(f"Arguments: {args} {time.ctime(seconds)}\n")
        f.close()
    return wrapper


def time_decorator(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        return (end - start)
    return wrapper


def slowdown(func):
    def wrapper(*args):
        time.sleep(1)
        func(*args)
    return wrapper


def sharpshooter(func):
    def wrapper(*args):
        return func() + ', the sharpshooter'
    return wrapper


def stealthy(func):
    def wrapper(*args):
        return func() + ', the stealthy'
    return wrapper


@write_decorator
def add(*args):
    return sum(args)


@write_decorator
def printer(text):
    return text


@time_decorator
def time_this(*args):
    for i in range(1000):
        print(i)
    return sum(args)


@slowdown
def countdown(n):
    if not n:   # 0 is false, not false is true
        print('liftoff')
    else:
        print(n)
        countdown(n-1)  # call the same function with n as one less


@sharpshooter
@stealthy
def player():
    return 'Im the player character'


# add(1, 5)
# printer('Hello my friend')
# x = time_this(1, 5, 2, 10, 2100, 50)
# print(x)
countdown(5)
# print(player())
