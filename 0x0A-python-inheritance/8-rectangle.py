#!/usr/bin/python3
""" Class Rectangle Module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class"""

    def __init__(self, width, height):
        self.__width = width
        self.integer_validator("height", height)
        self.height = height
