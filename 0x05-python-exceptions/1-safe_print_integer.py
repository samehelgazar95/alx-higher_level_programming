#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # raise TypeError(value, "is not an integer")
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
