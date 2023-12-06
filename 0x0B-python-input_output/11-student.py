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
        new_first = json['first_name'] if json['age'] else self.first_name
        new_last = json['last_name'] if json['age'] else self.last_name
        new_age = json['age'] if json['age'] else self.age
        self.first_name = new_first
        self.last_name = new_last
        self.age = new_age
