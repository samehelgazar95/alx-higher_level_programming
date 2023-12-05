#!/usr/bin/python3
"""writes an Object to a text file module"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file func"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj, sort_keys=True))
