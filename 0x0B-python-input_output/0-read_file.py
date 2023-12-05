#!/usr/bin/python3
"""Read File Module"""


def read_file(filename=""):
    """Read File Function"""
    with open(filename) as f:
        content = f.read()

        if content[-1] == '\n':
            content = content[:-1]

        print(content)
