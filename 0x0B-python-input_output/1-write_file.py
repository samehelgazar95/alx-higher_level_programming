#!/usr/bin/python3
"""Write to file Module"""


def write_file(filename="", text=""):
    """Write to file Function"""
    with open(filename, 'w', encoding='utf-8') as f:
        return (f.write(text))
