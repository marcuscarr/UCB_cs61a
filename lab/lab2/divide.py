def divide(num, divisor):
    """
    >>> divide(8, 2)
    4
    """
    k = 0
    prod = k * divisor
    remainder = num % divisor

    while (prod + remainder) < num:
       k = k + 1
       prod = k * divisor

    return k

