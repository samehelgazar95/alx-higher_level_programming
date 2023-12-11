#!/usr/bin/python3
""" Base Module """
import json


class Base:
    """ Base Class """

    __nb_objects = 0

    def __init__(self, id=None):
        """Base Constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ dict to JSON str repr"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
