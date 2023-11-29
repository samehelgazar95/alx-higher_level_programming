#!/usr/bin/python3
""" Rectangle Class Module """


class Rectangle():
    """ Simple Rectangle Class """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle instance."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """ Destructor"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """The area equation"""
        return self.width * self.height

    def perimeter(self):
        """The perimeter equation"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """ str Implementation """
        if self.width == 0 or self.height == 0:
            return ""

        return "\n".join(['#' * self.width for _ in range(self.height)])

    def __repr__(self):
        """ repr Implementation """
        return "Rectangle({}, {})".format(self.width, self.height)
