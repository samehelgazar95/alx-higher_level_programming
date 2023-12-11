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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Write obj to file.json """
        content = Base.to_json_string(
            [instance.to_dictionary() for instance in list_objs]
            )
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(content)
