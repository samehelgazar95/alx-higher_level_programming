#!/usr/bin/python3
"""Square attribute."""


class Square:
    """ Class For Square
    Attributes:
        size: the size of square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def propert(self, value):
        if not isinstance(value, tuple) or\
            len(value) != 2 or\
            not all(not isinstance(num, int) for num in value) or\
            not all(num >= 0 for num in value)
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print("")
