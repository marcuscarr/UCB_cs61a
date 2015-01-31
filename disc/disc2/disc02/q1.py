def is_prime(n):
    assert n > 1, "N must be greater than 1."
    x = n - 1
    while x > 1:
        if n % x == 0:
            return False
        x = x - 1
    return True
