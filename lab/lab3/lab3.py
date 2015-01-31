def sum(n):
    if n == 0:
        return 0
    else:
        return sum(n - 1) + n

def ab_plus_c(a, b, c):
    if b == 0:
        return c
    else:
        return ab_plus_c(a, b - 1, a) + c


def hailstone(n):
    """Print the hailstone sequence starting at n and return its length.

    >>> a = hailstone(10)  # Seven elements are 10, 5, 16, 8, 4, 2, 1
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(3*n + 1)

def compose1(f, g):
    """"Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def repeated(f, n):
    """Return the function that computes the nth application of f.

    f -- a function that takes one argument
    n -- a positive integer

    >>> repeated(square, 2)(5)
    625
    >>> repeated(square, 4)(5)
    152587890625
    """
    if n == 1:
        def g(x):
            return f(x)
        return g
    else:
        return compose1(repeated(f, n - 1), f)

def square(x):
    """Return x squared."""
    return x * x

def make_deriv(f):
    def g(x):
        return f(x + 1) - f(x)
    return g

def make_product(f, g):
    def h(x):
        return make_deriv(f)(x) * g(x+1) + make_deriv(g)(x) * f(x)
    return h

def blondie(f):
    return lambda x: f(x + 1)

tuco = blondie(lambda x: x * x)
