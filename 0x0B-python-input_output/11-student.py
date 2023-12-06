#!/usr/bin/python3
"""Class Student module"""


class Student:
    """Class Student func"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            dict = {}
            for attr in attrs:
                value = getattr(self, attr, "Error")
                if value == "Error":
                    continue
                dict[attr] = value
            return dict

    def reload_from_json(self, json):
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
