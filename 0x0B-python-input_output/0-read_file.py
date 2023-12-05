#!/usr/bin/python3
"""Read File Module"""


def read_file(filename=""):
    """Read File Function"""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
