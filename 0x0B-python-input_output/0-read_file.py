#!/usr/bin/python3
"""Read File Module"""


def read_file(filename=""):
    """Read File Function"""
    with open(filename, 'r') as f:
        print(f.read())
