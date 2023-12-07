#!/usr/bin/python3
"""Hello, iam BaseGeometry module"""


class BaseGeometry:
    """Hello, iam BaseGeometry Class"""

    def area(self):
        """Hello, iam area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Hello, iam Validating Int Method"""
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
