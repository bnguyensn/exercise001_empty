from typing import List


def fibonacci_from_zero(how_many: int) -> List[int]:
    """Return an array of length how_many, filled with Fibonacci numbers,
    starting from 0

    Arguments:
    int - how_many: how many Fibonacci numbers in the returned array
    """
    if (how_many < 1):
        return []

    if (how_many == 1):
        return [0]

    a, b = 0, 1
    number_list = [a, b]

    i = 2
    while i < how_many:
        a, b = b, a + b
        number_list.append(b)
        i += 1

    return number_list
