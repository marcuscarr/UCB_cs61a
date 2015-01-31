def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def approx_e(iter = 100):
    val_e, k = 0, 0
    while k < iter:
        val_e, k = val_e + 1/factorial(k), k + 1
    return val_e

def make_unit(catchphrase, damage):
    return (catchphrase, damage)

def get_catchphrase(unit):
    return unit[0]

def get_damage(unit):
    return unit[1]

def battle(first, second):
    """Simulates a battle between the first and second unit
    >>> zealot = make_unit('My life for Aiur!', 16)
    >>> zergling = make_unit('GRAAHHH!', 5)
    >>> winner = battle(zergling, zealot)
    GRAAHHH!
    My life for Aiur!
    >>> winner is zealot
    True
    """

    print(get_catchphrase(first))
    print(get_catchphrase(second))

    if get_damage(second) > get_damage(first):
        return second
    else:
        return first


