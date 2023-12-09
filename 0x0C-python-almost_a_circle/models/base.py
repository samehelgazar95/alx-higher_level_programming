#!/usr/bin/python3
"""Models Package Base Class"""


class Base:
    """ Base Class to id for other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Base Constructor"""
	if id is None:
		Base.__nb_objects += 1
		self.id = Base.__nb_objects
	else:
        	self.id = id

