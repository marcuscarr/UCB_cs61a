def countdown(n):
    """
    >>> countdown(3)
    3
    2
    1
    """

    if n == 1:
        print(1)
    else:
        print(n)
        countdown(n - 1)

def countup(n):
    """
    >>> countup(3)
    1
    2
    3
    """

    if n == 1:
        print(1)
    else:
        countup(n - 1)
        print(n)

def expt(base, power):
    """
    >>> expt(3, 2)
    9
    >>> expt(2, 3)
    8
    >>> expt(100, 0)
    1
    >>> expt(10, 4)
    10000
    """
    if power == 0:
        return 1
    else:
        return base * expt(base, power - 1)

def count_stair_ways(n):
    """
    >>> count_stair_ways(1)
    1
    >>> count_stair_ways(3)
    3
    >>> count_stair_ways(4)
    5
    """
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)

def pascal(row, column):
    assert column <= row, 'COLUMN must be less than or equal to ROW'
    if column == 0:
        return 1
    elif column == row:
        return 1
    else:
        return pascal(row - 1, column) + pascal(row - 1, column - 1)

def sum_less_than(total, num):
    """
    >>> sum_less_than(8, 5) # 5 + 3 = 8
    True
    >>> sum_less_than(23, 5) # no way to make 23 by summing 1-5
    False
    """
    if total == 0:
        return True
    if num == 0:
        return False
    return sum_less_than(total, num - 1) or sum_less_than(total - num, num - 1)
