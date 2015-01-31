def add1(x):
    return x + 1

def add3(x):
    return x + 3

def cycle(f1, f2):
    def my_func(x):
        return f2(f1(x))

    return my_func



