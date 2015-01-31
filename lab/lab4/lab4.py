def add_matrices(a, b):
    """ Performs element-wise matrix addition of A and B, 
    represented as two 2D lists.

    >>> add_matrices([[1, 3], [2, 0]], [[-3, 0], [1, 2]])
    [[-2, 3], [3, 2]]
    """

    assert len(a) == len(b), "Matrices must have same number of rows."
    result = []

    for idx_row in range(len(a)):
        row_a = a[idx_row]
        row_b = b[idx_row]
        assert len(row_a) == len(row_b), "Rows must be same lenght."
        this_row = []
        for idx_col in range(len(row_a)):
            this_row.append(row_a[idx_col] + row_b[idx_col])
        result.append(this_row)

    return result

suits = ["heart", "diamond", "spade", "club"]
cards = list(range(1,14))

deck = [(suit, card) for suit in suits for card in cards]

print(deck)
print(len(deck))

from random import shuffle
from operator import getitem

shuffle(deck)
print(deck)

deck.sort(key = lambda x: x[0])
deck.sort(key = lambda x: x[1])
print(deck)
