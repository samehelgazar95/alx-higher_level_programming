#!/usr/bin/python3
"""Modified isinstance module"""


def inherits_from(obj, a_class):
    """Modified isinstance Function

        @obj: the object
        @a_class: the class
    """

    if type(obj).__name__ == a_class.__name__:
        return False

    return isinstance(obj, a_class)
