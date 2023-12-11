#!/usr/bin/python3
""" Rectangle Module """
from base import Base


class Rectangle(Base):
    """ Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getters
    @property
    def width(self):
        """Width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    # Setters
    @width.setter
    def width(self, val):
        """Width setter"""
        self.validate_int("width", val)
        self.__width = val

    @height.setter
    def height(self, val):
        """height setter"""
        self.validate_int("height", val)
        self.__height = val

    @x.setter
    def x(self, val):
        """x setter"""
        self.validate_int("x", val, False)
        self.__x = val

    @y.setter
    def y(self, val):
        """y setter"""
        self.validate_int("y", val, False)
        self.__y = val

    def validate_int(self, name, value, is_w_h=True):
        """Validate the attrs"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif is_w_h and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif not is_w_h and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """area"""
        return (self.width * self.height)

    def display(self):
        """display"""
        for y_axis in range(self.y):
            print("")

        for h in range(self.height):
            print(" " * self.x, end='')
            for w in range(self.width):
                print('#', end='')
            print('')

    def __str__(self):
        """str overwritting"""
        i = self.id
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        cls_str = "[Rectangle] ({}) {}/{} - {}/{}".format(i, x, y, w, h)
        return cls_str

    def update(self, *args, **kwargs):
        """update"""
        if args:
            keys = ["width", "height", "x", "y", "id"]
            for i in range(min(len(args), len(keys))):
                setattr(self, keys[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dict of the obj"""
        my_dict = {}

        if self.x:
            my_dict['x'] = self.x
        if self.y:
            my_dict['y'] = self.y
        if self.id:
            my_dict['id'] = self.id
        if self.width:
            my_dict['width'] = self.width
        if self.height:
            my_dict['height'] = self.height

        return (my_dict)
