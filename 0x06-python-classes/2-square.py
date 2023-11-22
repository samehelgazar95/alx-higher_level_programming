#!/usr/bin/python3
"""Square attribute."""


class Square:
    """ Class For Square
    Attributes:
        size: the size of square
    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
