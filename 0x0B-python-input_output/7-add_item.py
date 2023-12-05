#!/usr/bin/python3
"""load_add_save to a text file module"""
import sys
import os


def load_add_save():
    """load_add_save to a text file func"""

    save_ = __import__('5-save_to_json_file').save_to_json_file
    load_ = __import__('6-load_from_json_file').load_from_json_file

    my_list = []

    if os.path.exists("add_item.json"):
        my_list.extend(load_("add_item.json"))

    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])

    save_(my_list, "add_item.json")


if __name__ == '__main__':
    load_add_save()
