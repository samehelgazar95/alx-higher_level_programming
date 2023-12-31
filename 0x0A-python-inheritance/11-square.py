#!/usr/bin/python3
"""Square Class Module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculate the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """String representation for the class"""
        return "[Square] {}/{}".format(self.__size, self.__size)
