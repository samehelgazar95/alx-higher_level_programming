#!/usr/bin/python3
"""Handling setattr with more one feature module"""


def add_attribute(obj, val, key):
    """Handling setattr with more one feature func
    Args:
        obj: the object
        key: key of the attr
        val: value of the attr
    Raises:
        TypeError: if the obj type is not object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, val, key)
