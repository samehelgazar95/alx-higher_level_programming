#!/usr/bin/python3
""" Square Module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Main Constructor for the Square class

            Args:
            size: the size
            x: x-axis
            y: y-axis
            id: id of the instance
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size Getter"""
        return self.width

    @size.setter
    def size(self, val):
        """Size Setter"""
        if type(val) is not int:
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        self.width = val
        self.height = val

    def __str__(self):
        """str overwritting function"""
        i = self.id
        x = self.x
        y = self.y
        s = self.size
        cls_str = "[Square] ({}) {}/{} - {}".format(i, x, y, s)
        return cls_str

    def update(self, *args, **kwargs):
        """ Update the object with new values
            Args:
                args: the array of strings
                kwargs: the dict of args
        """
        if args:
            keys = ["id", "size", "x", "y"]
            for i in range(min(len(args), len(keys))):
                setattr(self, keys[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Generate dict for the obj"""
        my_dict = {}

        if hasattr(self, 'x'):
            my_dict['x'] = self.x
        if hasattr(self, 'y'):
            my_dict['y'] = self.y
        if hasattr(self, 'id'):
            my_dict['id'] = self.id
        if hasattr(self, 'width'):
            my_dict['size'] = self.size

        return (my_dict)
