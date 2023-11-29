#!/usr/bin/python3
"""Rectangle Class Module"""


class Rectangle():
    """ Simple Rectangle Class """

    def __init__(self, width=0, height=0):
        """The Instance"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Width Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width Setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Heigth Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Heigth Setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
