#!/usr/bin/python3
"""load_add_save to a text file module"""
import json
import sys


def load_add_save():
    """load_add_save to a text file func"""

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    my_list = []
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])

    print(my_list)
    save_to_json_file(my_list, "add_item.json")


if __name__ == '__main__':
    load_add_save()
