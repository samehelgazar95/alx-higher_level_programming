#!/usr/bin/python3
"""Append to file Module"""


def append_write(filename="", text=""):
    """Append to file Function"""
    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
