#!/usr/bin/python3
"""Read File Module"""


def read_file(filename=""):
    """Read File Function"""
    with read(filename) as f:
        print(f)
