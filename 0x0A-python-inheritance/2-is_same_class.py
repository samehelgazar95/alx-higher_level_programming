#!/usr/bin/python3
"""Simple isInstance Alernative Module"""


def is_same_class(obj, a_class):
    """Simple isInstance Alernative Function

    @obj: the object
    @a_class: the class
    Return: True or False
    """
    return type(obj).__name__ == a_class.__name__
