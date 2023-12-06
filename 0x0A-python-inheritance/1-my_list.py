#!/usr/bin/python3
"""Print list sorted module"""


class MyList(list):
    """Print list sorted class"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
