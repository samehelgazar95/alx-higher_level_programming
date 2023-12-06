#!/usr/bin/python3
""" Class Rectangle Module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class"""

    def __init__(self, width, height):
        """Constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the square"""
        return (self.__width * self.__height)

    def __str__(self):
        """String representation for the class"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
