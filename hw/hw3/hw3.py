# Name:
# Email:

# Q1.

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"

        
    if n <= 3:
        return n
    else:
        curr, prior1, prior2, prior3, k = 0, 3, 2, 1, n % 3


# Q2.

def has_seven(k):
    """Has a has_seven
    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"
    if k % 10 == 7:
        return True
    elif k == 0:
        return False
    else:
        return has_seven(k // 10)

# Q3.

"1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6"


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    "*** YOUR CODE HERE ***"

    value, increment, k = 0, 1, 1

#    while k <= n:
        #if has_seven(k) or k % 7 == 0:
            #value, increment = value + increment, -1 * increment
        #else:
            #value = value + increment

        #print("At %i, value is %i and increment is %i." % (k, value, increment))
        #k = k + 1

    #return value

    if n == 1:
        return 1
    else:
        return pingpong(n - 1) + (-1) ** sum([x % 7 == 0 or has_seven(x) for x in range(1, n)])


# Q4.

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"

    if n == 0:
        return 0
    else:
        return sum([(n % 10) + int(x) == 10 for x in str(n // 10)]) + ten_pairs(n // 10)

# Q5.

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"

    from math import log

    
    if amount == 0:
        return 0
    if amount == 1:
        return 1
    if amount == 2:
        return 2

    max_pow2 = pow(2, int(log(amount - 1, 2)))

    if amount % max_pow2 == 0:
        return 1 + 2 * count_change(amount / 2)
    else:
        return 1 + count_change(amount - max_pow2) + count_change(max_pow2)

# Q6.

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return (lambda b: (lambda a, b: a(a, b))(lambda a, b: b * a(b - 1) if b > 0 else 1, b))
