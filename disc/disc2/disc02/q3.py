def every(func, n):
    x = 1
    while x <= n:
        print(func(x))
        x = x + 1

def keep(cond, n):
    if cond(n):
        print(n)

def and_add_one(f):
    def g(x):
        return f(x) + 1
    return g

def square(x):
    return x * x
