#!/usr/bin/python3
"""LockedClass Class Module"""


class LockedClass:
    """
        A class with restricted attribute creation using __slots__.

        Attributes:
        __slots__ (tuple): A tuple containing the allowed attribute names.
        first_name (str): The first name of an instance.

        Methods:
        __init__(): Initializes an instance of the LockedClass.
    """

    __slots__ = ('first_name',)
