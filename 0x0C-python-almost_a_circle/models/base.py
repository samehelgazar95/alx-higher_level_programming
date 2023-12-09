#!/usr/bin/python3
"""Models Package Base Class"""


class Base:
    """ Base Class to id for other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Base Constructor"""
        self.id = id
        if id is None:
            __nb_objects += 1
            self.id = __nb_objects
