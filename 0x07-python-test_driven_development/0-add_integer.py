#!/usr/bin/python3
"""
    add two integers module
    Returns:
        the sum of two integers
"""


def add_integer(a, b=98):
    """ add two integers function

        Args:
            a: the first number
            b: the second numebr

        Rasies:
            TypeError: if a or b is not int or float
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == '__main__':
    import doctest
    doctest.testfile("./tests/0-add_integer.txt")
