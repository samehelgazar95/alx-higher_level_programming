#!/usr/bin/python3
"""3-say_my_name module"""


def say_my_name(first_name, last_name=""):
    """ say_my_name function

        Args:
            first_name: the first name
            last_name: the last name

        Raises:
            TypeError: if first_name or last_name is not str
    """

    if not type(first_name) == str:
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == '__main__':
    import doctest
    doctest.testfile("./tests/3-say_my_name.txt")
