#!/usr/bin/python3
"""writes an Object to a text file module"""
import json


def load_from_json_file(filename):
    """writes an Object to a text file func"""
    with open(filename, 'r') as f:
        return json.loads(f.read())
