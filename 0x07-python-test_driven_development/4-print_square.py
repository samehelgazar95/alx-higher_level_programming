#!/usr/bin/python3
""" 4-print_square module """


def print_square(size):
    """ print_square function

        Args:
            size: the size of the matrix

        Raises:
            TypeError: if the size is not int
            ValueError: if the size is less than or equals to 0
    """

    res = [[]]
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size > 0:
        res = [['#'] * size for _ in range(size)]

        for row in res:
            for ele in row:
                print(ele, end="")
            print("")


if __name__ == '__main__':
    import doctest
    doctest.testfile("./tests/4-print_square.txt")
